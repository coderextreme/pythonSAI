from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
component2 = component()
component2.setName("H-Anim")
component2.setLevel(1)

head1.addComponent(component2)
meta3 = meta()
meta3.setName("title")
meta3.setContent("HAnimSpecificationLOA3Animation.x3d")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("description")
meta4.setContent("HAnim Specification reference example providing full coverage and visibility of all specified HAnim constructs, plus motion animations. Geometry visualizations are derived from HAnimSpecificationLOA3Invisible.x3d visualization report. Resusable exemplar animations also added via heads-up display (HUD) interface to confirm proper parent-child relationships.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("reference")
meta5.setContent("https://www.web3d.org/files/specifications/19774/V1.0/HAnim/BodyDimensionsAndLOAs.html#LOA3ExampleSourceWithDiamonds")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("created")
meta6.setContent("24 April 2013")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("modified")
meta7.setContent("4 July 2020")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("TODO")
meta8.setContent("Convert to X3D4 HAnim2")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("Image")
meta9.setContent("HAnimSpecificationLOA3MotionH3DViewer.png")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("Image")
meta10.setContent("HAnimSpecificationLOA3MotionInstantReality.png")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("Image")
meta11.setContent("HAnimSpecificationLOA3MotionOctagaVS.png")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("Image")
meta12.setContent("HAnimSpecificationLOA3MotionView3dscene.png")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("reference")
meta13.setContent("HAnimSpecificationLOA3Illustrated.x3d")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("reference")
meta14.setContent("HAnimSpecificationLOA3Invisible.x3d")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("reference")
meta15.setContent("HAnimSpecificationExampleChangeLog.txt")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("Image")
meta16.setContent("images/BonesAllSkeletonFrontViewLOA1.png")

head1.addMeta(meta16)
meta17 = meta()
meta17.setName("Image")
meta17.setContent("images/BonesAllSkeletonFrontViewLOA2.png")

head1.addMeta(meta17)
meta18 = meta()
meta18.setName("Image")
meta18.setContent("images/BonesAllSkeletonFrontViewLOA3.png")

head1.addMeta(meta18)
meta19 = meta()
meta19.setName("reference")
meta19.setContent("Norman Badler et al., ANTHROPOMETRY FOR COMPUTER GRAPHICS HUMAN FIGURES, University of Pennsylvania, 1989.")

head1.addMeta(meta19)
meta20 = meta()
meta20.setName("reference")
meta20.setContent("http://www.cis.upenn.edu/~badler/anthro/89-71.ps")

head1.addMeta(meta20)
meta21 = meta()
meta21.setName("reference")
meta21.setContent("tables/AnthropometryForComputerGraphicsHumanFigures89-71.pdf")

head1.addMeta(meta21)
meta22 = meta()
meta22.setName("creator")
meta22.setContent("Matthew T. Beitler, Joe D. Williams, Don Brutzman")

head1.addMeta(meta22)
meta23 = meta()
meta23.setName("translator")
meta23.setContent("Don Brutzman and Joe Williams")

head1.addMeta(meta23)
meta24 = meta()
meta24.setName("generator")
meta24.setContent("BS Contact Geo 8.001, http://www.bitmanagement.de/en/products/interactive-3d-clients/bs-contact-geo")

head1.addMeta(meta24)
meta25 = meta()
meta25.setName("reference")
meta25.setContent("originals/LOA3ExampleSourceWithDiamondsOriginal.wrl")

head1.addMeta(meta25)
meta26 = meta()
meta26.setName("reference")
meta26.setContent("originals/LOA3ExampleSourceWithDiamondsOriginal.x3d")

head1.addMeta(meta26)
meta27 = meta()
meta27.setName("reference")
meta27.setContent("originals/LOA3ExampleSourceWithDiamondsOriginalBsContactExport.x3d")

head1.addMeta(meta27)
meta28 = meta()
meta28.setName("generator")
meta28.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta28)
meta29 = meta()
meta29.setName("identifier")
meta29.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Specifications/HAnimSpecificationLOA3Animation.x3d")

head1.addMeta(meta29)
meta30 = meta()
meta30.setName("license")
meta30.setContent("../license.html")

head1.addMeta(meta30)

X3D0.setHead(head1)
Scene31 = Scene()
Background32 = Background()
Background32.setSkyColor([0.3,0.3,0.3])

Scene31.addChildren(Background32)
NavigationInfo33 = NavigationInfo()

Scene31.addChildren(NavigationInfo33)
Group34 = Group()
Group34.setDEF("Original_WorldInfo")
WorldInfo35 = WorldInfo()
WorldInfo35.setInfo([" HANIM 200x Default Joint Centers, Level-Of-Articulation 3 HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://HAnim.org/Specifications/HAnim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "])
WorldInfo35.setTitle("HANIM 200x Default Joint Centers, LOA3")

Group34.addChildren(WorldInfo35)

Scene31.addChildren(Group34)
#TODO move viewpoints to be internal to HAnimHumanoid
#Viewpoint centerOfRotation=\"0 0.9149 0.0016\" matches initial at-rest locaton of the sacroliac. Note that these viewpoints are external to the HAnimHumanoid and do not move with the human.
Viewpoint36 = Viewpoint()
Viewpoint36.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint36.setDescription("Humanoid LOA 3 Front")
Viewpoint36.setPosition([0,0.4,4])

Scene31.addChildren(Viewpoint36)
Viewpoint37 = Viewpoint()
Viewpoint37.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint37.setDescription("Humanoid LOA 3 Front Close")
Viewpoint37.setPosition([0,0.8,2])

Scene31.addChildren(Viewpoint37)
Viewpoint38 = Viewpoint()
Viewpoint38.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint38.setDescription("Humanoid LOA 3 Front Closer")
Viewpoint38.setPosition([0,1.2,1])

Scene31.addChildren(Viewpoint38)
Viewpoint39 = Viewpoint()
Viewpoint39.setCenterOfRotation([0,1.5,0.0016])
Viewpoint39.setDescription("Humanoid LOA 3 Front Face")
Viewpoint39.setPosition([0,1.63,1])

Scene31.addChildren(Viewpoint39)
Viewpoint40 = Viewpoint()
Viewpoint40.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint40.setDescription("Humanoid LOA 3 Right Side")
Viewpoint40.setOrientation([0,1,0,1.5708])
Viewpoint40.setPosition([2.6,0.8,0])

Scene31.addChildren(Viewpoint40)
Viewpoint41 = Viewpoint()
Viewpoint41.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint41.setDescription("Humanoid LOA 3 Right Side Close")
Viewpoint41.setOrientation([0,1,0,1.2])
Viewpoint41.setPosition([1,0.8,0.5])

Scene31.addChildren(Viewpoint41)
Viewpoint42 = Viewpoint()
Viewpoint42.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint42.setDescription("Humanoid LOA 3 Left Side Close")
Viewpoint42.setOrientation([0,1,0,-1.2])
Viewpoint42.setPosition([-1,0.8,0.5])

Scene31.addChildren(Viewpoint42)
Viewpoint43 = Viewpoint()
Viewpoint43.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint43.setDescription("Humanoid LOA 3 Left Side")
Viewpoint43.setOrientation([0,1,0,-1.5708])
Viewpoint43.setPosition([-2.6,0.8,0])

Scene31.addChildren(Viewpoint43)
Viewpoint44 = Viewpoint()
Viewpoint44.setCenterOfRotation([0,0.9149,0.0016])
Viewpoint44.setDescription("Humanoid LOA 3 Top")
Viewpoint44.setOrientation([1,0,0,-1.5708])
Viewpoint44.setPosition([0,3.5,0])

Scene31.addChildren(Viewpoint44)
HAnimHumanoid45 = HAnimHumanoid()
HAnimHumanoid45.setName("humanoid")
HAnimHumanoid45.setDEF("hanim_humanoid")
HAnimHumanoid45.setInfo(["authorName=Matthew T. Beitler Joe D. Williams Don Brutzman","authorEmail=HAnim@web3D.org","copyright=none","creationDate=12 May 1999","usageRestrictions=none","humanoidVersion=2.0","height=1.7504"])
HAnimHumanoid45.setVersion("1.0")
HAnimJoint46 = HAnimJoint()
HAnimJoint46.setName("humanoid_root")
HAnimJoint46.setDEF("hanim_humanoid_root")
HAnimJoint46.setCenter([0,0.824,0.0277])
HAnimJoint46.setStiffness([0,0,0])
HAnimSegment47 = HAnimSegment()
HAnimSegment47.setName("sacrum")
HAnimSegment47.setDEF("hanim_sacrum")
#<HAnimJoint name='humanoid_root'/> visualization sphere within <HAnimSegment name='sacrum'/>
TouchSensor48 = TouchSensor()
TouchSensor48.setDescription("HAnimJoint HumanoidRoot, HAnimSegment sacrum")

HAnimSegment47.addChildren(TouchSensor48)
Transform49 = Transform()
Transform49.setTranslation([0,0.824,0.0277])
Shape50 = Shape()
Shape50.setDEF("HAnimJointShape")
Sphere51 = Sphere()
Sphere51.setRadius(0.006)

Shape50.setGeometry(Sphere51)
Appearance52 = Appearance()
Appearance52.setDEF("HAnimJointAppearance")
Material53 = Material()
Material53.setDiffuseColor([1,0.5,0])
Material53.setTransparency(0.5)

Appearance52.setMaterial(Material53)

Shape50.setAppearance(Appearance52)

Transform49.addChildren(Shape50)

HAnimSegment47.addChildren(Transform49)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='sacroiliac'/>
Shape54 = Shape()
LineSet55 = LineSet()
LineSet55.setVertexCount([2])
Coordinate56 = Coordinate()
Coordinate56.setPoint([0,0.824,0.0277,0,0.9149,0.0016])

LineSet55.setCoord(Coordinate56)
ColorRGBA57 = ColorRGBA()
ColorRGBA57.setDEF("HAnimSegmentLineColorRGBA")
ColorRGBA57.setColor([1,1,0,1,1,1,0,0.1])

LineSet55.setColor(ColorRGBA57)

Shape54.setGeometry(LineSet55)

HAnimSegment47.addChildren(Shape54)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='vl5'/>
Shape58 = Shape()
LineSet59 = LineSet()
LineSet59.setVertexCount([2])
Coordinate60 = Coordinate()
Coordinate60.setPoint([0,0.824,0.0277,0.0028,1.0568,-0.0776])

LineSet59.setCoord(Coordinate60)
ColorRGBA61 = ColorRGBA()
ColorRGBA61.setUSE("HAnimSegmentLineColorRGBA")

LineSet59.setColor(ColorRGBA61)

Shape58.setGeometry(LineSet59)

HAnimSegment47.addChildren(Shape58)

HAnimJoint46.addChildren(HAnimSegment47)
HAnimJoint62 = HAnimJoint()
HAnimJoint62.setName("sacroiliac")
HAnimJoint62.setDEF("hanim_sacroiliac")
HAnimJoint62.setCenter([0,0.9149,0.0016])
HAnimJoint62.setStiffness([0,0,0])
HAnimSegment63 = HAnimSegment()
HAnimSegment63.setName("pelvis")
HAnimSegment63.setDEF("hanim_pelvis")
#<HAnimJoint name='sacroiliac'/> visualization sphere within <HAnimSegment name='pelvis'/>
TouchSensor64 = TouchSensor()
TouchSensor64.setDescription("HAnimJoint sacroiliac, HAnimSegment pelvis")

HAnimSegment63.addChildren(TouchSensor64)
Transform65 = Transform()
Transform65.setTranslation([0,0.9149,0.0016])
Shape66 = Shape()
Shape66.setUSE("HAnimJointShape")

Transform65.addChildren(Shape66)

HAnimSegment63.addChildren(Transform65)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='l_hip'/>
Shape67 = Shape()
LineSet68 = LineSet()
LineSet68.setVertexCount([2])
Coordinate69 = Coordinate()
Coordinate69.setPoint([0,0.9149,0.0016,0.0961,0.9124,-0.0001])

LineSet68.setCoord(Coordinate69)
ColorRGBA70 = ColorRGBA()
ColorRGBA70.setUSE("HAnimSegmentLineColorRGBA")

LineSet68.setColor(ColorRGBA70)

Shape67.setGeometry(LineSet68)

HAnimSegment63.addChildren(Shape67)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='r_hip'/>
Shape71 = Shape()
LineSet72 = LineSet()
LineSet72.setVertexCount([2])
Coordinate73 = Coordinate()
Coordinate73.setPoint([0,0.9149,0.0016,-0.0961,0.9124,-0.0001])

LineSet72.setCoord(Coordinate73)
ColorRGBA74 = ColorRGBA()
ColorRGBA74.setUSE("HAnimSegmentLineColorRGBA")

LineSet72.setColor(ColorRGBA74)

Shape71.setGeometry(LineSet72)

HAnimSegment63.addChildren(Shape71)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_iliocristale'/>
Shape75 = Shape()
LineSet76 = LineSet()
LineSet76.setVertexCount([2])
Coordinate77 = Coordinate()
Coordinate77.setPoint([0,0.9149,0.0016,-0.1525,1.0628,0.0035])

LineSet76.setCoord(Coordinate77)
ColorRGBA78 = ColorRGBA()
ColorRGBA78.setDEF("HAnimSiteLineColorRGBA")
ColorRGBA78.setColor([1,0,0,1,1,0,0,0.1])

LineSet76.setColor(ColorRGBA78)

Shape75.setGeometry(LineSet76)

HAnimSegment63.addChildren(Shape75)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_trochanterion'/>
Shape79 = Shape()
LineSet80 = LineSet()
LineSet80.setVertexCount([2])
Coordinate81 = Coordinate()
Coordinate81.setPoint([0,0.9149,0.0016,-0.1689,0.8419,0.0352])

LineSet80.setCoord(Coordinate81)
ColorRGBA82 = ColorRGBA()
ColorRGBA82.setUSE("HAnimSiteLineColorRGBA")

LineSet80.setColor(ColorRGBA82)

Shape79.setGeometry(LineSet80)

HAnimSegment63.addChildren(Shape79)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_iliocristale'/>
Shape83 = Shape()
LineSet84 = LineSet()
LineSet84.setVertexCount([2])
Coordinate85 = Coordinate()
Coordinate85.setPoint([0,0.9149,0.0016,0.1612,1.0537,0.0008])

LineSet84.setCoord(Coordinate85)
ColorRGBA86 = ColorRGBA()
ColorRGBA86.setUSE("HAnimSiteLineColorRGBA")

LineSet84.setColor(ColorRGBA86)

Shape83.setGeometry(LineSet84)

HAnimSegment63.addChildren(Shape83)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_trochanterion'/>
Shape87 = Shape()
LineSet88 = LineSet()
LineSet88.setVertexCount([2])
Coordinate89 = Coordinate()
Coordinate89.setPoint([0,0.9149,0.0016,0.1677,0.8336,0.0303])

LineSet88.setCoord(Coordinate89)
ColorRGBA90 = ColorRGBA()
ColorRGBA90.setUSE("HAnimSiteLineColorRGBA")

LineSet88.setColor(ColorRGBA90)

Shape87.setGeometry(LineSet88)

HAnimSegment63.addChildren(Shape87)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_asis'/>
Shape91 = Shape()
LineSet92 = LineSet()
LineSet92.setVertexCount([2])
Coordinate93 = Coordinate()
Coordinate93.setPoint([0,0.9149,0.0016,-0.0887,1.0021,0.1112])

LineSet92.setCoord(Coordinate93)
ColorRGBA94 = ColorRGBA()
ColorRGBA94.setUSE("HAnimSiteLineColorRGBA")

LineSet92.setColor(ColorRGBA94)

Shape91.setGeometry(LineSet92)

HAnimSegment63.addChildren(Shape91)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_asis'/>
Shape95 = Shape()
LineSet96 = LineSet()
LineSet96.setVertexCount([2])
Coordinate97 = Coordinate()
Coordinate97.setPoint([0,0.9149,0.0016,0.0925,0.9983,0.1052])

LineSet96.setCoord(Coordinate97)
ColorRGBA98 = ColorRGBA()
ColorRGBA98.setUSE("HAnimSiteLineColorRGBA")

LineSet96.setColor(ColorRGBA98)

Shape95.setGeometry(LineSet96)

HAnimSegment63.addChildren(Shape95)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_psis'/>
Shape99 = Shape()
LineSet100 = LineSet()
LineSet100.setVertexCount([2])
Coordinate101 = Coordinate()
Coordinate101.setPoint([0,0.9149,0.0016,-0.0716,1.019,-0.1138])

LineSet100.setCoord(Coordinate101)
ColorRGBA102 = ColorRGBA()
ColorRGBA102.setUSE("HAnimSiteLineColorRGBA")

LineSet100.setColor(ColorRGBA102)

Shape99.setGeometry(LineSet100)

HAnimSegment63.addChildren(Shape99)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_psis'/>
Shape103 = Shape()
LineSet104 = LineSet()
LineSet104.setVertexCount([2])
Coordinate105 = Coordinate()
Coordinate105.setPoint([0,0.9149,0.0016,0.0774,1.019,-0.1151])

LineSet104.setCoord(Coordinate105)
ColorRGBA106 = ColorRGBA()
ColorRGBA106.setUSE("HAnimSiteLineColorRGBA")

LineSet104.setColor(ColorRGBA106)

Shape103.setGeometry(LineSet104)

HAnimSegment63.addChildren(Shape103)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='crotch'/>
Shape107 = Shape()
LineSet108 = LineSet()
LineSet108.setVertexCount([2])
Coordinate109 = Coordinate()
Coordinate109.setPoint([0,0.9149,0.0016,0.0034,0.8266,0.0257])

LineSet108.setCoord(Coordinate109)
ColorRGBA110 = ColorRGBA()
ColorRGBA110.setUSE("HAnimSiteLineColorRGBA")

LineSet108.setColor(ColorRGBA110)

Shape107.setGeometry(LineSet108)

HAnimSegment63.addChildren(Shape107)
HAnimSite111 = HAnimSite()
HAnimSite111.setName("r_iliocristale_pt")
HAnimSite111.setDEF("hanim_r_iliocristale_pt")
HAnimSite111.setTranslation([-0.1525,1.0628,0.0035])
#HAnimSite visualization shape
TouchSensor112 = TouchSensor()
TouchSensor112.setDescription("HAnimSite r_iliocristale")

HAnimSite111.addChildren(TouchSensor112)
Shape113 = Shape()
Shape113.setDEF("HAnimSiteShape")
IndexedFaceSet114 = IndexedFaceSet()
IndexedFaceSet114.setDEF("DiamondIFS")
IndexedFaceSet114.setCoordIndex([0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1])
IndexedFaceSet114.setCreaseAngle(0.5)
IndexedFaceSet114.setSolid(False)
Coordinate115 = Coordinate()
Coordinate115.setPoint([0,0.008,0,-0.008,0,0,0,0,0.008,0.008,0,0,0,0,-0.008,0,-0.008,0])

IndexedFaceSet114.setCoord(Coordinate115)

Shape113.setGeometry(IndexedFaceSet114)
Appearance116 = Appearance()
Material117 = Material()
Material117.setDiffuseColor([1,0,0])

Appearance116.setMaterial(Material117)

Shape113.setAppearance(Appearance116)

HAnimSite111.addChildren(Shape113)

HAnimSegment63.addChildren(HAnimSite111)
HAnimSite118 = HAnimSite()
HAnimSite118.setName("r_trochanterion_pt")
HAnimSite118.setDEF("hanim_r_trochanterion_pt")
HAnimSite118.setTranslation([-0.1689,0.8419,0.0352])
#HAnimSite visualization shape
TouchSensor119 = TouchSensor()
TouchSensor119.setDescription("HAnimSite r_trochanterion")

HAnimSite118.addChildren(TouchSensor119)
Shape120 = Shape()
Shape120.setUSE("HAnimSiteShape")

HAnimSite118.addChildren(Shape120)

HAnimSegment63.addChildren(HAnimSite118)
HAnimSite121 = HAnimSite()
HAnimSite121.setName("l_iliocristale_pt")
HAnimSite121.setDEF("hanim_l_iliocristale_pt")
HAnimSite121.setTranslation([0.1612,1.0537,0.0008])
#HAnimSite visualization shape
TouchSensor122 = TouchSensor()
TouchSensor122.setDescription("HAnimSite l_iliocristale")

HAnimSite121.addChildren(TouchSensor122)
Shape123 = Shape()
Shape123.setUSE("HAnimSiteShape")

HAnimSite121.addChildren(Shape123)

HAnimSegment63.addChildren(HAnimSite121)
HAnimSite124 = HAnimSite()
HAnimSite124.setName("l_trochanterion_pt")
HAnimSite124.setDEF("hanim_l_trochanterion_pt")
HAnimSite124.setTranslation([0.1677,0.8336,0.0303])
#HAnimSite visualization shape
TouchSensor125 = TouchSensor()
TouchSensor125.setDescription("HAnimSite l_trochanterion")

HAnimSite124.addChildren(TouchSensor125)
Shape126 = Shape()
Shape126.setUSE("HAnimSiteShape")

HAnimSite124.addChildren(Shape126)

HAnimSegment63.addChildren(HAnimSite124)
HAnimSite127 = HAnimSite()
HAnimSite127.setName("r_asis_pt")
HAnimSite127.setDEF("hanim_r_asis_pt")
HAnimSite127.setTranslation([-0.0887,1.0021,0.1112])
#HAnimSite visualization shape
TouchSensor128 = TouchSensor()
TouchSensor128.setDescription("HAnimSite r_asis")

HAnimSite127.addChildren(TouchSensor128)
Shape129 = Shape()
Shape129.setUSE("HAnimSiteShape")

HAnimSite127.addChildren(Shape129)

HAnimSegment63.addChildren(HAnimSite127)
HAnimSite130 = HAnimSite()
HAnimSite130.setName("l_asis_pt")
HAnimSite130.setDEF("hanim_l_asis_pt")
HAnimSite130.setTranslation([0.0925,0.9983,0.1052])
#HAnimSite visualization shape
TouchSensor131 = TouchSensor()
TouchSensor131.setDescription("HAnimSite l_asis")

HAnimSite130.addChildren(TouchSensor131)
Shape132 = Shape()
Shape132.setUSE("HAnimSiteShape")

HAnimSite130.addChildren(Shape132)

HAnimSegment63.addChildren(HAnimSite130)
HAnimSite133 = HAnimSite()
HAnimSite133.setName("r_psis_pt")
HAnimSite133.setDEF("hanim_r_psis_pt")
HAnimSite133.setTranslation([-0.0716,1.019,-0.1138])
#HAnimSite visualization shape
TouchSensor134 = TouchSensor()
TouchSensor134.setDescription("HAnimSite r_psis")

HAnimSite133.addChildren(TouchSensor134)
Shape135 = Shape()
Shape135.setUSE("HAnimSiteShape")

HAnimSite133.addChildren(Shape135)

HAnimSegment63.addChildren(HAnimSite133)
HAnimSite136 = HAnimSite()
HAnimSite136.setName("l_psis_pt")
HAnimSite136.setDEF("hanim_l_psis_pt")
HAnimSite136.setTranslation([0.0774,1.019,-0.1151])
#HAnimSite visualization shape
TouchSensor137 = TouchSensor()
TouchSensor137.setDescription("HAnimSite l_psis")

HAnimSite136.addChildren(TouchSensor137)
Shape138 = Shape()
Shape138.setUSE("HAnimSiteShape")

HAnimSite136.addChildren(Shape138)

HAnimSegment63.addChildren(HAnimSite136)
HAnimSite139 = HAnimSite()
HAnimSite139.setName("crotch_pt")
HAnimSite139.setDEF("hanim_crotch_pt")
HAnimSite139.setTranslation([0.0034,0.8266,0.0257])
#HAnimSite visualization shape
TouchSensor140 = TouchSensor()
TouchSensor140.setDescription("HAnimSite crotch")

HAnimSite139.addChildren(TouchSensor140)
Shape141 = Shape()
Shape141.setUSE("HAnimSiteShape")

HAnimSite139.addChildren(Shape141)

HAnimSegment63.addChildren(HAnimSite139)

HAnimJoint62.addChildren(HAnimSegment63)
HAnimJoint142 = HAnimJoint()
HAnimJoint142.setName("l_hip")
HAnimJoint142.setDEF("hanim_l_hip")
HAnimJoint142.setCenter([0.0961,0.9124,-0.0001])
HAnimJoint142.setStiffness([0,0,0])
HAnimSegment143 = HAnimSegment()
HAnimSegment143.setName("l_thigh")
HAnimSegment143.setDEF("hanim_l_thigh")
#<HAnimJoint name='l_hip'/> visualization sphere within <HAnimSegment name='l_thigh'/>
TouchSensor144 = TouchSensor()
TouchSensor144.setDescription("HAnimJoint l_hip, HAnimSegment l_thigh")

HAnimSegment143.addChildren(TouchSensor144)
Transform145 = Transform()
Transform145.setTranslation([0.0961,0.9124,-0.0001])
Shape146 = Shape()
Shape146.setUSE("HAnimJointShape")

Transform145.addChildren(Shape146)

HAnimSegment143.addChildren(Transform145)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_hip'/> to <HAnimJoint name='l_knee'/>
Shape147 = Shape()
LineSet148 = LineSet()
LineSet148.setVertexCount([2])
Coordinate149 = Coordinate()
Coordinate149.setPoint([0.0961,0.9124,-0.0001,0.104,0.4867,0.0308])

LineSet148.setCoord(Coordinate149)
ColorRGBA150 = ColorRGBA()
ColorRGBA150.setUSE("HAnimSegmentLineColorRGBA")

LineSet148.setColor(ColorRGBA150)

Shape147.setGeometry(LineSet148)

HAnimSegment143.addChildren(Shape147)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_knee_crease'/>
Shape151 = Shape()
LineSet152 = LineSet()
LineSet152.setVertexCount([2])
Coordinate153 = Coordinate()
Coordinate153.setPoint([0.0961,0.9124,-0.0001,0.0993,0.4881,-0.0309])

LineSet152.setCoord(Coordinate153)
ColorRGBA154 = ColorRGBA()
ColorRGBA154.setUSE("HAnimSiteLineColorRGBA")

LineSet152.setColor(ColorRGBA154)

Shape151.setGeometry(LineSet152)

HAnimSegment143.addChildren(Shape151)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_lateral_epicn'/>
Shape155 = Shape()
LineSet156 = LineSet()
LineSet156.setVertexCount([2])
Coordinate157 = Coordinate()
Coordinate157.setPoint([0.0961,0.9124,-0.0001,0.1598,0.4967,0.0297])

LineSet156.setCoord(Coordinate157)
ColorRGBA158 = ColorRGBA()
ColorRGBA158.setUSE("HAnimSiteLineColorRGBA")

LineSet156.setColor(ColorRGBA158)

Shape155.setGeometry(LineSet156)

HAnimSegment143.addChildren(Shape155)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_medial_epicn'/>
Shape159 = Shape()
LineSet160 = LineSet()
LineSet160.setVertexCount([2])
Coordinate161 = Coordinate()
Coordinate161.setPoint([0.0961,0.9124,-0.0001,0.0398,0.4946,0.0303])

LineSet160.setCoord(Coordinate161)
ColorRGBA162 = ColorRGBA()
ColorRGBA162.setUSE("HAnimSiteLineColorRGBA")

LineSet160.setColor(ColorRGBA162)

Shape159.setGeometry(LineSet160)

HAnimSegment143.addChildren(Shape159)
HAnimSite163 = HAnimSite()
HAnimSite163.setName("l_knee_crease_pt")
HAnimSite163.setDEF("hanim_l_knee_crease_pt")
HAnimSite163.setTranslation([0.0993,0.4881,-0.0309])
#HAnimSite visualization shape
TouchSensor164 = TouchSensor()
TouchSensor164.setDescription("HAnimSite l_knee_crease")

HAnimSite163.addChildren(TouchSensor164)
Shape165 = Shape()
Shape165.setUSE("HAnimSiteShape")

HAnimSite163.addChildren(Shape165)

HAnimSegment143.addChildren(HAnimSite163)
HAnimSite166 = HAnimSite()
HAnimSite166.setName("l_femoral_lateral_epicn_pt")
HAnimSite166.setDEF("hanim_l_femoral_lateral_epicn_pt")
HAnimSite166.setTranslation([0.1598,0.4967,0.0297])
#HAnimSite visualization shape
TouchSensor167 = TouchSensor()
TouchSensor167.setDescription("HAnimSite l_femoral_lateral_epicn")

HAnimSite166.addChildren(TouchSensor167)
Shape168 = Shape()
Shape168.setUSE("HAnimSiteShape")

HAnimSite166.addChildren(Shape168)

HAnimSegment143.addChildren(HAnimSite166)
HAnimSite169 = HAnimSite()
HAnimSite169.setName("l_femoral_medial_epicn_pt")
HAnimSite169.setDEF("hanim_l_femoral_medial_epicn_pt")
HAnimSite169.setTranslation([0.0398,0.4946,0.0303])
#HAnimSite visualization shape
TouchSensor170 = TouchSensor()
TouchSensor170.setDescription("HAnimSite l_femoral_medial_epicn")

HAnimSite169.addChildren(TouchSensor170)
Shape171 = Shape()
Shape171.setUSE("HAnimSiteShape")

HAnimSite169.addChildren(Shape171)

HAnimSegment143.addChildren(HAnimSite169)

HAnimJoint142.addChildren(HAnimSegment143)
HAnimJoint172 = HAnimJoint()
HAnimJoint172.setName("l_knee")
HAnimJoint172.setDEF("hanim_l_knee")
HAnimJoint172.setCenter([0.104,0.4867,0.0308])
HAnimJoint172.setStiffness([0,0,0])
HAnimSegment173 = HAnimSegment()
HAnimSegment173.setName("l_calf")
HAnimSegment173.setDEF("hanim_l_calf")
#<HAnimJoint name='l_knee'/> visualization sphere within <HAnimSegment name='l_calf'/>
TouchSensor174 = TouchSensor()
TouchSensor174.setDescription("HAnimJoint l_knee, HAnimSegment l_calf")

HAnimSegment173.addChildren(TouchSensor174)
Transform175 = Transform()
Transform175.setTranslation([0.104,0.4867,0.0308])
Shape176 = Shape()
Shape176.setUSE("HAnimJointShape")

Transform175.addChildren(Shape176)

HAnimSegment173.addChildren(Transform175)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_knee'/> to <HAnimJoint name='l_ankle'/>
Shape177 = Shape()
LineSet178 = LineSet()
LineSet178.setVertexCount([2])
Coordinate179 = Coordinate()
Coordinate179.setPoint([0.104,0.4867,0.0308,0.1101,0.0656,-0.0736])

LineSet178.setCoord(Coordinate179)
ColorRGBA180 = ColorRGBA()
ColorRGBA180.setUSE("HAnimSegmentLineColorRGBA")

LineSet178.setColor(ColorRGBA180)

Shape177.setGeometry(LineSet178)

HAnimSegment173.addChildren(Shape177)

HAnimJoint172.addChildren(HAnimSegment173)
HAnimJoint181 = HAnimJoint()
HAnimJoint181.setName("l_ankle")
HAnimJoint181.setDEF("hanim_l_ankle")
HAnimJoint181.setCenter([0.1101,0.0656,-0.0736])
HAnimJoint181.setStiffness([0,0,0])
HAnimSegment182 = HAnimSegment()
HAnimSegment182.setName("l_hindfoot")
HAnimSegment182.setDEF("hanim_l_hindfoot")
#<HAnimJoint name='l_ankle'/> visualization sphere within <HAnimSegment name='l_hindfoot'/>
TouchSensor183 = TouchSensor()
TouchSensor183.setDescription("HAnimJoint l_ankle, HAnimSegment l_hindfoot")

HAnimSegment182.addChildren(TouchSensor183)
Transform184 = Transform()
Transform184.setTranslation([0.1101,0.0656,-0.0736])
Shape185 = Shape()
Shape185.setUSE("HAnimJointShape")

Transform184.addChildren(Shape185)

HAnimSegment182.addChildren(Transform184)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ankle'/> to <HAnimJoint name='l_subtalar'/>
Shape186 = Shape()
LineSet187 = LineSet()
LineSet187.setVertexCount([2])
Coordinate188 = Coordinate()
Coordinate188.setPoint([0.1101,0.0656,-0.0736,0.1086,0.0001,-0.0368])

LineSet187.setCoord(Coordinate188)
ColorRGBA189 = ColorRGBA()
ColorRGBA189.setUSE("HAnimSegmentLineColorRGBA")

LineSet187.setColor(ColorRGBA189)

Shape186.setGeometry(LineSet187)

HAnimSegment182.addChildren(Shape186)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_lateral_malleolus'/>
Shape190 = Shape()
LineSet191 = LineSet()
LineSet191.setVertexCount([2])
Coordinate192 = Coordinate()
Coordinate192.setPoint([0.1101,0.0656,-0.0736,0.1308,0.0597,-0.1032])

LineSet191.setCoord(Coordinate192)
ColorRGBA193 = ColorRGBA()
ColorRGBA193.setUSE("HAnimSiteLineColorRGBA")

LineSet191.setColor(ColorRGBA193)

Shape190.setGeometry(LineSet191)

HAnimSegment182.addChildren(Shape190)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_medial_malleolus'/>
Shape194 = Shape()
LineSet195 = LineSet()
LineSet195.setVertexCount([2])
Coordinate196 = Coordinate()
Coordinate196.setPoint([0.1101,0.0656,-0.0736,0.089,0.0716,-0.0881])

LineSet195.setCoord(Coordinate196)
ColorRGBA197 = ColorRGBA()
ColorRGBA197.setUSE("HAnimSiteLineColorRGBA")

LineSet195.setColor(ColorRGBA197)

Shape194.setGeometry(LineSet195)

HAnimSegment182.addChildren(Shape194)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_sphyrion'/>
Shape198 = Shape()
LineSet199 = LineSet()
LineSet199.setVertexCount([2])
Coordinate200 = Coordinate()
Coordinate200.setPoint([0.1101,0.0656,-0.0736,0.089,0.0575,-0.0943])

LineSet199.setCoord(Coordinate200)
ColorRGBA201 = ColorRGBA()
ColorRGBA201.setUSE("HAnimSiteLineColorRGBA")

LineSet199.setColor(ColorRGBA201)

Shape198.setGeometry(LineSet199)

HAnimSegment182.addChildren(Shape198)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_calcaneous_post'/>
Shape202 = Shape()
LineSet203 = LineSet()
LineSet203.setVertexCount([2])
Coordinate204 = Coordinate()
Coordinate204.setPoint([0.1101,0.0656,-0.0736,0.0974,0.0259,-0.1171])

LineSet203.setCoord(Coordinate204)
ColorRGBA205 = ColorRGBA()
ColorRGBA205.setUSE("HAnimSiteLineColorRGBA")

LineSet203.setColor(ColorRGBA205)

Shape202.setGeometry(LineSet203)

HAnimSegment182.addChildren(Shape202)
HAnimSite206 = HAnimSite()
HAnimSite206.setName("l_lateral_malleolus_pt")
HAnimSite206.setDEF("hanim_l_lateral_malleolus_pt")
HAnimSite206.setTranslation([0.1308,0.0597,-0.1032])
#HAnimSite visualization shape
TouchSensor207 = TouchSensor()
TouchSensor207.setDescription("HAnimSite l_lateral_malleolus")

HAnimSite206.addChildren(TouchSensor207)
Shape208 = Shape()
Shape208.setUSE("HAnimSiteShape")

HAnimSite206.addChildren(Shape208)

HAnimSegment182.addChildren(HAnimSite206)
HAnimSite209 = HAnimSite()
HAnimSite209.setName("l_medial_malleolus_pt")
HAnimSite209.setDEF("hanim_l_medial_malleolus_pt")
HAnimSite209.setTranslation([0.089,0.0716,-0.0881])
#HAnimSite visualization shape
TouchSensor210 = TouchSensor()
TouchSensor210.setDescription("HAnimSite l_medial_malleolus")

HAnimSite209.addChildren(TouchSensor210)
Shape211 = Shape()
Shape211.setUSE("HAnimSiteShape")

HAnimSite209.addChildren(Shape211)

HAnimSegment182.addChildren(HAnimSite209)
HAnimSite212 = HAnimSite()
HAnimSite212.setName("l_sphyrion_pt")
HAnimSite212.setDEF("hanim_l_sphyrion_pt")
HAnimSite212.setTranslation([0.089,0.0575,-0.0943])
#HAnimSite visualization shape
TouchSensor213 = TouchSensor()
TouchSensor213.setDescription("HAnimSite l_sphyrion")

HAnimSite212.addChildren(TouchSensor213)
Shape214 = Shape()
Shape214.setUSE("HAnimSiteShape")

HAnimSite212.addChildren(Shape214)

HAnimSegment182.addChildren(HAnimSite212)
HAnimSite215 = HAnimSite()
HAnimSite215.setName("l_calcaneous_post_pt")
HAnimSite215.setDEF("hanim_l_calcaneous_post_pt")
HAnimSite215.setTranslation([0.0974,0.0259,-0.1171])
#HAnimSite visualization shape
TouchSensor216 = TouchSensor()
TouchSensor216.setDescription("HAnimSite l_calcaneous_post")

HAnimSite215.addChildren(TouchSensor216)
Shape217 = Shape()
Shape217.setUSE("HAnimSiteShape")

HAnimSite215.addChildren(Shape217)

HAnimSegment182.addChildren(HAnimSite215)

HAnimJoint181.addChildren(HAnimSegment182)
HAnimJoint218 = HAnimJoint()
HAnimJoint218.setName("l_subtalar")
HAnimJoint218.setDEF("hanim_l_subtalar")
HAnimJoint218.setCenter([0.1086,0.0001,-0.0368])
HAnimJoint218.setStiffness([0,0,0])
HAnimSegment219 = HAnimSegment()
HAnimSegment219.setName("l_midproximal")
HAnimSegment219.setDEF("hanim_l_midproximal")
#<HAnimJoint name='l_subtalar'/> visualization sphere within <HAnimSegment name='l_midproximal'/>
TouchSensor220 = TouchSensor()
TouchSensor220.setDescription("HAnimJoint l_subtalar, HAnimSegment l_midproximal")

HAnimSegment219.addChildren(TouchSensor220)
Transform221 = Transform()
Transform221.setTranslation([0.1086,0.0001,-0.0368])
Shape222 = Shape()
Shape222.setUSE("HAnimJointShape")

Transform221.addChildren(Shape222)

HAnimSegment219.addChildren(Transform221)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_subtalar'/> to <HAnimJoint name='l_midtarsal'/>
Shape223 = Shape()
LineSet224 = LineSet()
LineSet224.setVertexCount([2])
Coordinate225 = Coordinate()
Coordinate225.setPoint([0.1086,0.0001,-0.0368,0.1086,0.0001,0.0368])

LineSet224.setCoord(Coordinate225)
ColorRGBA226 = ColorRGBA()
ColorRGBA226.setUSE("HAnimSegmentLineColorRGBA")

LineSet224.setColor(ColorRGBA226)

Shape223.setGeometry(LineSet224)

HAnimSegment219.addChildren(Shape223)

HAnimJoint218.addChildren(HAnimSegment219)
HAnimJoint227 = HAnimJoint()
HAnimJoint227.setName("l_midtarsal")
HAnimJoint227.setDEF("hanim_l_midtarsal")
HAnimJoint227.setCenter([0.1086,0.0001,0.0368])
HAnimJoint227.setStiffness([0,0,0])
HAnimSegment228 = HAnimSegment()
HAnimSegment228.setName("l_middistal")
HAnimSegment228.setDEF("hanim_l_middistal")
#<HAnimJoint name='l_midtarsal'/> visualization sphere within <HAnimSegment name='l_middistal'/>
TouchSensor229 = TouchSensor()
TouchSensor229.setDescription("HAnimJoint l_midtarsal, HAnimSegment l_middistal")

HAnimSegment228.addChildren(TouchSensor229)
Transform230 = Transform()
Transform230.setTranslation([0.1086,0.0001,0.0368])
Shape231 = Shape()
Shape231.setUSE("HAnimJointShape")

Transform230.addChildren(Shape231)

HAnimSegment228.addChildren(Transform230)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_midtarsal'/> to <HAnimJoint name='l_metatarsal'/>
Shape232 = Shape()
LineSet233 = LineSet()
LineSet233.setVertexCount([2])
Coordinate234 = Coordinate()
Coordinate234.setPoint([0.1086,0.0001,0.0368,0.1086,0,0.0762])

LineSet233.setCoord(Coordinate234)
ColorRGBA235 = ColorRGBA()
ColorRGBA235.setUSE("HAnimSegmentLineColorRGBA")

LineSet233.setColor(ColorRGBA235)

Shape232.setGeometry(LineSet233)

HAnimSegment228.addChildren(Shape232)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_midtarsal'/> to <HAnimSite name='l_metatarsal_pha1'/>
Shape236 = Shape()
LineSet237 = LineSet()
LineSet237.setVertexCount([2])
Coordinate238 = Coordinate()
Coordinate238.setPoint([0.1086,0.0001,0.0368,0.0816,0.0232,0.0106])

LineSet237.setCoord(Coordinate238)
ColorRGBA239 = ColorRGBA()
ColorRGBA239.setUSE("HAnimSiteLineColorRGBA")

LineSet237.setColor(ColorRGBA239)

Shape236.setGeometry(LineSet237)

HAnimSegment228.addChildren(Shape236)
HAnimSite240 = HAnimSite()
HAnimSite240.setName("l_metatarsal_pha1_pt")
HAnimSite240.setDEF("hanim_l_metatarsal_pha1_pt")
HAnimSite240.setTranslation([0.0816,0.0232,0.0106])
#HAnimSite visualization shape
TouchSensor241 = TouchSensor()
TouchSensor241.setDescription("HAnimSite l_metatarsal_pha1")

HAnimSite240.addChildren(TouchSensor241)
Shape242 = Shape()
Shape242.setUSE("HAnimSiteShape")

HAnimSite240.addChildren(Shape242)

HAnimSegment228.addChildren(HAnimSite240)

HAnimJoint227.addChildren(HAnimSegment228)
HAnimJoint243 = HAnimJoint()
HAnimJoint243.setName("l_metatarsal")
HAnimJoint243.setDEF("hanim_l_metatarsal")
HAnimJoint243.setCenter([0.1086,0,0.0762])
HAnimJoint243.setStiffness([0,0,0])
HAnimSegment244 = HAnimSegment()
HAnimSegment244.setName("l_forefoot")
HAnimSegment244.setDEF("hanim_l_forefoot")
#<HAnimJoint name='l_metatarsal'/> visualization sphere within <HAnimSegment name='l_forefoot'/>
TouchSensor245 = TouchSensor()
TouchSensor245.setDescription("HAnimJoint l_metatarsal, HAnimSegment l_forefoot")

HAnimSegment244.addChildren(TouchSensor245)
Transform246 = Transform()
Transform246.setTranslation([0.1086,0,0.0762])
Shape247 = Shape()
Shape247.setUSE("HAnimJointShape")

Transform246.addChildren(Shape247)

HAnimSegment244.addChildren(Transform246)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_forefoot_tip'/>
Shape248 = Shape()
LineSet249 = LineSet()
LineSet249.setVertexCount([2])
Coordinate250 = Coordinate()
Coordinate250.setPoint([0.1086,0,0.0762,0.1354,0.0016,0.1476])

LineSet249.setCoord(Coordinate250)
ColorRGBA251 = ColorRGBA()
ColorRGBA251.setUSE("HAnimSiteLineColorRGBA")

LineSet249.setColor(ColorRGBA251)

Shape248.setGeometry(LineSet249)

HAnimSegment244.addChildren(Shape248)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_metatarsal_pha5'/>
Shape252 = Shape()
LineSet253 = LineSet()
LineSet253.setVertexCount([2])
Coordinate254 = Coordinate()
Coordinate254.setPoint([0.1086,0,0.0762,0.1825,0.007,0.0928])

LineSet253.setCoord(Coordinate254)
ColorRGBA255 = ColorRGBA()
ColorRGBA255.setUSE("HAnimSiteLineColorRGBA")

LineSet253.setColor(ColorRGBA255)

Shape252.setGeometry(LineSet253)

HAnimSegment244.addChildren(Shape252)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_digit2'/>
Shape256 = Shape()
LineSet257 = LineSet()
LineSet257.setVertexCount([2])
Coordinate258 = Coordinate()
Coordinate258.setPoint([0.1086,0,0.0762,0.1195,0.0079,0.1433])

LineSet257.setCoord(Coordinate258)
ColorRGBA259 = ColorRGBA()
ColorRGBA259.setUSE("HAnimSiteLineColorRGBA")

LineSet257.setColor(ColorRGBA259)

Shape256.setGeometry(LineSet257)

HAnimSegment244.addChildren(Shape256)
HAnimSite260 = HAnimSite()
HAnimSite260.setName("l_forefoot_tip")
HAnimSite260.setDEF("hanim_l_forefoot_tip")
HAnimSite260.setTranslation([0.1354,0.0016,0.1476])
#HAnimSite visualization shape
TouchSensor261 = TouchSensor()
TouchSensor261.setDescription("HAnimSite l_forefoot_tip")

HAnimSite260.addChildren(TouchSensor261)
Shape262 = Shape()
Shape262.setUSE("HAnimSiteShape")

HAnimSite260.addChildren(Shape262)

HAnimSegment244.addChildren(HAnimSite260)
HAnimSite263 = HAnimSite()
HAnimSite263.setName("l_metatarsal_pha5_pt")
HAnimSite263.setDEF("hanim_l_metatarsal_pha5_pt")
HAnimSite263.setTranslation([0.1825,0.007,0.0928])
#HAnimSite visualization shape
TouchSensor264 = TouchSensor()
TouchSensor264.setDescription("HAnimSite l_metatarsal_pha5")

HAnimSite263.addChildren(TouchSensor264)
Shape265 = Shape()
Shape265.setUSE("HAnimSiteShape")

HAnimSite263.addChildren(Shape265)

HAnimSegment244.addChildren(HAnimSite263)
HAnimSite266 = HAnimSite()
HAnimSite266.setName("l_digit2_pt")
HAnimSite266.setDEF("hanim_l_digit2_pt")
HAnimSite266.setTranslation([0.1195,0.0079,0.1433])
#HAnimSite visualization shape
TouchSensor267 = TouchSensor()
TouchSensor267.setDescription("HAnimSite l_digit2")

HAnimSite266.addChildren(TouchSensor267)
Shape268 = Shape()
Shape268.setUSE("HAnimSiteShape")

HAnimSite266.addChildren(Shape268)

HAnimSegment244.addChildren(HAnimSite266)

HAnimJoint243.addChildren(HAnimSegment244)

HAnimJoint227.addChildren(HAnimJoint243)

HAnimJoint218.addChildren(HAnimJoint227)

HAnimJoint181.addChildren(HAnimJoint218)

HAnimJoint172.addChildren(HAnimJoint181)

HAnimJoint142.addChildren(HAnimJoint172)

HAnimJoint62.addChildren(HAnimJoint142)
HAnimJoint269 = HAnimJoint()
HAnimJoint269.setName("r_hip")
HAnimJoint269.setDEF("hanim_r_hip")
HAnimJoint269.setCenter([-0.0961,0.9124,-0.0001])
HAnimJoint269.setStiffness([0,0,0])
HAnimSegment270 = HAnimSegment()
HAnimSegment270.setName("r_thigh")
HAnimSegment270.setDEF("hanim_r_thigh")
#<HAnimJoint name='r_hip'/> visualization sphere within <HAnimSegment name='r_thigh'/>
TouchSensor271 = TouchSensor()
TouchSensor271.setDescription("HAnimJoint r_hip, HAnimSegment r_thigh")

HAnimSegment270.addChildren(TouchSensor271)
Transform272 = Transform()
Transform272.setTranslation([-0.0961,0.9124,-0.0001])
Shape273 = Shape()
Shape273.setUSE("HAnimJointShape")

Transform272.addChildren(Shape273)

HAnimSegment270.addChildren(Transform272)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_hip'/> to <HAnimJoint name='r_knee'/>
Shape274 = Shape()
LineSet275 = LineSet()
LineSet275.setVertexCount([2])
Coordinate276 = Coordinate()
Coordinate276.setPoint([-0.0961,0.9124,-0.0001,-0.104,0.4867,0.0308])

LineSet275.setCoord(Coordinate276)
ColorRGBA277 = ColorRGBA()
ColorRGBA277.setUSE("HAnimSegmentLineColorRGBA")

LineSet275.setColor(ColorRGBA277)

Shape274.setGeometry(LineSet275)

HAnimSegment270.addChildren(Shape274)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_knee_crease'/>
Shape278 = Shape()
LineSet279 = LineSet()
LineSet279.setVertexCount([2])
Coordinate280 = Coordinate()
Coordinate280.setPoint([-0.0961,0.9124,-0.0001,-0.0825,0.4932,-0.0326])

LineSet279.setCoord(Coordinate280)
ColorRGBA281 = ColorRGBA()
ColorRGBA281.setUSE("HAnimSiteLineColorRGBA")

LineSet279.setColor(ColorRGBA281)

Shape278.setGeometry(LineSet279)

HAnimSegment270.addChildren(Shape278)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_lateral_epicn'/>
Shape282 = Shape()
LineSet283 = LineSet()
LineSet283.setVertexCount([2])
Coordinate284 = Coordinate()
Coordinate284.setPoint([-0.0961,0.9124,-0.0001,-0.1421,0.4992,0.031])

LineSet283.setCoord(Coordinate284)
ColorRGBA285 = ColorRGBA()
ColorRGBA285.setUSE("HAnimSiteLineColorRGBA")

LineSet283.setColor(ColorRGBA285)

Shape282.setGeometry(LineSet283)

HAnimSegment270.addChildren(Shape282)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_medial_epicn'/>
Shape286 = Shape()
LineSet287 = LineSet()
LineSet287.setVertexCount([2])
Coordinate288 = Coordinate()
Coordinate288.setPoint([-0.0961,0.9124,-0.0001,-0.0221,0.5014,0.0289])

LineSet287.setCoord(Coordinate288)
ColorRGBA289 = ColorRGBA()
ColorRGBA289.setUSE("HAnimSiteLineColorRGBA")

LineSet287.setColor(ColorRGBA289)

Shape286.setGeometry(LineSet287)

HAnimSegment270.addChildren(Shape286)
HAnimSite290 = HAnimSite()
HAnimSite290.setName("r_knee_crease_pt")
HAnimSite290.setDEF("hanim_r_knee_crease_pt")
HAnimSite290.setTranslation([-0.0825,0.4932,-0.0326])
#HAnimSite visualization shape
TouchSensor291 = TouchSensor()
TouchSensor291.setDescription("HAnimSite r_knee_crease")

HAnimSite290.addChildren(TouchSensor291)
Shape292 = Shape()
Shape292.setUSE("HAnimSiteShape")

HAnimSite290.addChildren(Shape292)

HAnimSegment270.addChildren(HAnimSite290)
HAnimSite293 = HAnimSite()
HAnimSite293.setName("r_femoral_lateral_epicn_pt")
HAnimSite293.setDEF("hanim_r_femoral_lateral_epicn_pt")
HAnimSite293.setTranslation([-0.1421,0.4992,0.031])
#HAnimSite visualization shape
TouchSensor294 = TouchSensor()
TouchSensor294.setDescription("HAnimSite r_femoral_lateral_epicn")

HAnimSite293.addChildren(TouchSensor294)
Shape295 = Shape()
Shape295.setUSE("HAnimSiteShape")

HAnimSite293.addChildren(Shape295)

HAnimSegment270.addChildren(HAnimSite293)
HAnimSite296 = HAnimSite()
HAnimSite296.setName("r_femoral_medial_epicn_pt")
HAnimSite296.setDEF("hanim_r_femoral_medial_epicn_pt")
HAnimSite296.setTranslation([-0.0221,0.5014,0.0289])
#HAnimSite visualization shape
TouchSensor297 = TouchSensor()
TouchSensor297.setDescription("HAnimSite r_femoral_medial_epicn")

HAnimSite296.addChildren(TouchSensor297)
Shape298 = Shape()
Shape298.setUSE("HAnimSiteShape")

HAnimSite296.addChildren(Shape298)

HAnimSegment270.addChildren(HAnimSite296)

HAnimJoint269.addChildren(HAnimSegment270)
HAnimJoint299 = HAnimJoint()
HAnimJoint299.setName("r_knee")
HAnimJoint299.setDEF("hanim_r_knee")
HAnimJoint299.setCenter([-0.104,0.4867,0.0308])
HAnimJoint299.setStiffness([0,0,0])
HAnimSegment300 = HAnimSegment()
HAnimSegment300.setName("r_calf")
HAnimSegment300.setDEF("hanim_r_calf")
#<HAnimJoint name='r_knee'/> visualization sphere within <HAnimSegment name='r_calf'/>
TouchSensor301 = TouchSensor()
TouchSensor301.setDescription("HAnimJoint r_knee, HAnimSegment r_calf")

HAnimSegment300.addChildren(TouchSensor301)
Transform302 = Transform()
Transform302.setTranslation([-0.104,0.4867,0.0308])
Shape303 = Shape()
Shape303.setUSE("HAnimJointShape")

Transform302.addChildren(Shape303)

HAnimSegment300.addChildren(Transform302)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_knee'/> to <HAnimJoint name='r_ankle'/>
Shape304 = Shape()
LineSet305 = LineSet()
LineSet305.setVertexCount([2])
Coordinate306 = Coordinate()
Coordinate306.setPoint([-0.104,0.4867,0.0308,-0.1101,0.0656,-0.0736])

LineSet305.setCoord(Coordinate306)
ColorRGBA307 = ColorRGBA()
ColorRGBA307.setUSE("HAnimSegmentLineColorRGBA")

LineSet305.setColor(ColorRGBA307)

Shape304.setGeometry(LineSet305)

HAnimSegment300.addChildren(Shape304)

HAnimJoint299.addChildren(HAnimSegment300)
HAnimJoint308 = HAnimJoint()
HAnimJoint308.setName("r_ankle")
HAnimJoint308.setDEF("hanim_r_ankle")
HAnimJoint308.setCenter([-0.1101,0.0656,-0.0736])
HAnimJoint308.setStiffness([0,0,0])
HAnimSegment309 = HAnimSegment()
HAnimSegment309.setName("r_hindfoot")
HAnimSegment309.setDEF("hanim_r_hindfoot")
#<HAnimJoint name='r_ankle'/> visualization sphere within <HAnimSegment name='r_hindfoot'/>
TouchSensor310 = TouchSensor()
TouchSensor310.setDescription("HAnimJoint r_ankle, HAnimSegment r_hindfoot")

HAnimSegment309.addChildren(TouchSensor310)
Transform311 = Transform()
Transform311.setTranslation([-0.1101,0.0656,-0.0736])
Shape312 = Shape()
Shape312.setUSE("HAnimJointShape")

Transform311.addChildren(Shape312)

HAnimSegment309.addChildren(Transform311)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ankle'/> to <HAnimJoint name='r_subtalar'/>
Shape313 = Shape()
LineSet314 = LineSet()
LineSet314.setVertexCount([2])
Coordinate315 = Coordinate()
Coordinate315.setPoint([-0.1101,0.0656,-0.0736,-0.1086,0.0001,-0.0368])

LineSet314.setCoord(Coordinate315)
ColorRGBA316 = ColorRGBA()
ColorRGBA316.setUSE("HAnimSegmentLineColorRGBA")

LineSet314.setColor(ColorRGBA316)

Shape313.setGeometry(LineSet314)

HAnimSegment309.addChildren(Shape313)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_lateral_malleolus'/>
Shape317 = Shape()
LineSet318 = LineSet()
LineSet318.setVertexCount([2])
Coordinate319 = Coordinate()
Coordinate319.setPoint([-0.1101,0.0656,-0.0736,-0.1006,0.0658,-0.1075])

LineSet318.setCoord(Coordinate319)
ColorRGBA320 = ColorRGBA()
ColorRGBA320.setUSE("HAnimSiteLineColorRGBA")

LineSet318.setColor(ColorRGBA320)

Shape317.setGeometry(LineSet318)

HAnimSegment309.addChildren(Shape317)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_medial_malleolus'/>
Shape321 = Shape()
LineSet322 = LineSet()
LineSet322.setVertexCount([2])
Coordinate323 = Coordinate()
Coordinate323.setPoint([-0.1101,0.0656,-0.0736,-0.0591,0.076,-0.0928])

LineSet322.setCoord(Coordinate323)
ColorRGBA324 = ColorRGBA()
ColorRGBA324.setUSE("HAnimSiteLineColorRGBA")

LineSet322.setColor(ColorRGBA324)

Shape321.setGeometry(LineSet322)

HAnimSegment309.addChildren(Shape321)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_sphyrion'/>
Shape325 = Shape()
LineSet326 = LineSet()
LineSet326.setVertexCount([2])
Coordinate327 = Coordinate()
Coordinate327.setPoint([-0.1101,0.0656,-0.0736,-0.0603,0.061,-0.1002])

LineSet326.setCoord(Coordinate327)
ColorRGBA328 = ColorRGBA()
ColorRGBA328.setUSE("HAnimSiteLineColorRGBA")

LineSet326.setColor(ColorRGBA328)

Shape325.setGeometry(LineSet326)

HAnimSegment309.addChildren(Shape325)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_calcaneous_post'/>
Shape329 = Shape()
LineSet330 = LineSet()
LineSet330.setVertexCount([2])
Coordinate331 = Coordinate()
Coordinate331.setPoint([-0.1101,0.0656,-0.0736,-0.0692,0.0297,-0.1221])

LineSet330.setCoord(Coordinate331)
ColorRGBA332 = ColorRGBA()
ColorRGBA332.setUSE("HAnimSiteLineColorRGBA")

LineSet330.setColor(ColorRGBA332)

Shape329.setGeometry(LineSet330)

HAnimSegment309.addChildren(Shape329)
HAnimSite333 = HAnimSite()
HAnimSite333.setName("r_lateral_malleolus_pt")
HAnimSite333.setDEF("hanim_r_lateral_malleolus_pt")
HAnimSite333.setTranslation([-0.1006,0.0658,-0.1075])
#HAnimSite visualization shape
TouchSensor334 = TouchSensor()
TouchSensor334.setDescription("HAnimSite r_lateral_malleolus")

HAnimSite333.addChildren(TouchSensor334)
Shape335 = Shape()
Shape335.setUSE("HAnimSiteShape")

HAnimSite333.addChildren(Shape335)

HAnimSegment309.addChildren(HAnimSite333)
HAnimSite336 = HAnimSite()
HAnimSite336.setName("r_medial_malleolus_pt")
HAnimSite336.setDEF("hanim_r_medial_malleolus_pt")
HAnimSite336.setTranslation([-0.0591,0.076,-0.0928])
#HAnimSite visualization shape
TouchSensor337 = TouchSensor()
TouchSensor337.setDescription("HAnimSite r_medial_malleolus")

HAnimSite336.addChildren(TouchSensor337)
Shape338 = Shape()
Shape338.setUSE("HAnimSiteShape")

HAnimSite336.addChildren(Shape338)

HAnimSegment309.addChildren(HAnimSite336)
HAnimSite339 = HAnimSite()
HAnimSite339.setName("r_sphyrion_pt")
HAnimSite339.setDEF("hanim_r_sphyrion_pt")
HAnimSite339.setTranslation([-0.0603,0.061,-0.1002])
#HAnimSite visualization shape
TouchSensor340 = TouchSensor()
TouchSensor340.setDescription("HAnimSite r_sphyrion")

HAnimSite339.addChildren(TouchSensor340)
Shape341 = Shape()
Shape341.setUSE("HAnimSiteShape")

HAnimSite339.addChildren(Shape341)

HAnimSegment309.addChildren(HAnimSite339)
HAnimSite342 = HAnimSite()
HAnimSite342.setName("r_calcaneous_post_pt")
HAnimSite342.setDEF("hanim_r_calcaneous_post_pt")
HAnimSite342.setTranslation([-0.0692,0.0297,-0.1221])
#HAnimSite visualization shape
TouchSensor343 = TouchSensor()
TouchSensor343.setDescription("HAnimSite r_calcaneous_post")

HAnimSite342.addChildren(TouchSensor343)
Shape344 = Shape()
Shape344.setUSE("HAnimSiteShape")

HAnimSite342.addChildren(Shape344)

HAnimSegment309.addChildren(HAnimSite342)

HAnimJoint308.addChildren(HAnimSegment309)
HAnimJoint345 = HAnimJoint()
HAnimJoint345.setName("r_subtalar")
HAnimJoint345.setDEF("hanim_r_subtalar")
HAnimJoint345.setCenter([-0.1086,0.0001,-0.0368])
HAnimJoint345.setStiffness([0,0,0])
HAnimSegment346 = HAnimSegment()
HAnimSegment346.setName("r_midproximal")
HAnimSegment346.setDEF("hanim_r_midproximal")
#<HAnimJoint name='r_subtalar'/> visualization sphere within <HAnimSegment name='r_midproximal'/>
TouchSensor347 = TouchSensor()
TouchSensor347.setDescription("HAnimJoint r_subtalar, HAnimSegment r_midproximal")

HAnimSegment346.addChildren(TouchSensor347)
Transform348 = Transform()
Transform348.setTranslation([-0.1086,0.0001,-0.0368])
Shape349 = Shape()
Shape349.setUSE("HAnimJointShape")

Transform348.addChildren(Shape349)

HAnimSegment346.addChildren(Transform348)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_subtalar'/> to <HAnimJoint name='r_midtarsal'/>
Shape350 = Shape()
LineSet351 = LineSet()
LineSet351.setVertexCount([2])
Coordinate352 = Coordinate()
Coordinate352.setPoint([-0.1086,0.0001,-0.0368,-0.1086,0.0001,0.0368])

LineSet351.setCoord(Coordinate352)
ColorRGBA353 = ColorRGBA()
ColorRGBA353.setUSE("HAnimSegmentLineColorRGBA")

LineSet351.setColor(ColorRGBA353)

Shape350.setGeometry(LineSet351)

HAnimSegment346.addChildren(Shape350)

HAnimJoint345.addChildren(HAnimSegment346)
HAnimJoint354 = HAnimJoint()
HAnimJoint354.setName("r_midtarsal")
HAnimJoint354.setDEF("hanim_r_midtarsal")
HAnimJoint354.setCenter([-0.1086,0.0001,0.0368])
HAnimJoint354.setStiffness([0,0,0])
HAnimSegment355 = HAnimSegment()
HAnimSegment355.setName("r_middistal")
HAnimSegment355.setDEF("hanim_r_middistal")
#<HAnimJoint name='r_midtarsal'/> visualization sphere within <HAnimSegment name='r_middistal'/>
TouchSensor356 = TouchSensor()
TouchSensor356.setDescription("HAnimJoint r_midtarsal, HAnimSegment r_middistal")

HAnimSegment355.addChildren(TouchSensor356)
Transform357 = Transform()
Transform357.setTranslation([-0.1086,0.0001,0.0368])
Shape358 = Shape()
Shape358.setUSE("HAnimJointShape")

Transform357.addChildren(Shape358)

HAnimSegment355.addChildren(Transform357)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_midtarsal'/> to <HAnimJoint name='r_metatarsal'/>
Shape359 = Shape()
LineSet360 = LineSet()
LineSet360.setVertexCount([2])
Coordinate361 = Coordinate()
Coordinate361.setPoint([-0.1086,0.0001,0.0368,-0.1086,0,0.0762])

LineSet360.setCoord(Coordinate361)
ColorRGBA362 = ColorRGBA()
ColorRGBA362.setUSE("HAnimSegmentLineColorRGBA")

LineSet360.setColor(ColorRGBA362)

Shape359.setGeometry(LineSet360)

HAnimSegment355.addChildren(Shape359)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_midtarsal'/> to <HAnimSite name='r_metatarsal_pha1'/>
Shape363 = Shape()
LineSet364 = LineSet()
LineSet364.setVertexCount([2])
Coordinate365 = Coordinate()
Coordinate365.setPoint([-0.1086,0.0001,0.0368,-0.0521,0.026,0.0127])

LineSet364.setCoord(Coordinate365)
ColorRGBA366 = ColorRGBA()
ColorRGBA366.setUSE("HAnimSiteLineColorRGBA")

LineSet364.setColor(ColorRGBA366)

Shape363.setGeometry(LineSet364)

HAnimSegment355.addChildren(Shape363)
HAnimSite367 = HAnimSite()
HAnimSite367.setName("r_metatarsal_pha1_pt")
HAnimSite367.setDEF("hanim_r_metatarsal_pha1_pt")
HAnimSite367.setTranslation([-0.0521,0.026,0.0127])
#HAnimSite visualization shape
TouchSensor368 = TouchSensor()
TouchSensor368.setDescription("HAnimSite r_metatarsal_pha1")

HAnimSite367.addChildren(TouchSensor368)
Shape369 = Shape()
Shape369.setUSE("HAnimSiteShape")

HAnimSite367.addChildren(Shape369)

HAnimSegment355.addChildren(HAnimSite367)

HAnimJoint354.addChildren(HAnimSegment355)
HAnimJoint370 = HAnimJoint()
HAnimJoint370.setName("r_metatarsal")
HAnimJoint370.setDEF("hanim_r_metatarsal")
HAnimJoint370.setCenter([-0.1086,0,0.0762])
HAnimJoint370.setStiffness([0,0,0])
HAnimSegment371 = HAnimSegment()
HAnimSegment371.setName("r_forefoot")
HAnimSegment371.setDEF("hanim_r_forefoot")
#<HAnimJoint name='r_metatarsal'/> visualization sphere within <HAnimSegment name='r_forefoot'/>
TouchSensor372 = TouchSensor()
TouchSensor372.setDescription("HAnimJoint r_metatarsal, HAnimSegment r_forefoot")

HAnimSegment371.addChildren(TouchSensor372)
Transform373 = Transform()
Transform373.setTranslation([-0.1086,0,0.0762])
Shape374 = Shape()
Shape374.setUSE("HAnimJointShape")

Transform373.addChildren(Shape374)

HAnimSegment371.addChildren(Transform373)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_forefoot_tip'/>
Shape375 = Shape()
LineSet376 = LineSet()
LineSet376.setVertexCount([2])
Coordinate377 = Coordinate()
Coordinate377.setPoint([-0.1086,0,0.0762,-0.1043,0.0227,0.145])

LineSet376.setCoord(Coordinate377)
ColorRGBA378 = ColorRGBA()
ColorRGBA378.setUSE("HAnimSiteLineColorRGBA")

LineSet376.setColor(ColorRGBA378)

Shape375.setGeometry(LineSet376)

HAnimSegment371.addChildren(Shape375)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_metatarsal_pha5'/>
Shape379 = Shape()
LineSet380 = LineSet()
LineSet380.setVertexCount([2])
Coordinate381 = Coordinate()
Coordinate381.setPoint([-0.1086,0,0.0762,-0.1523,0.0166,0.0895])

LineSet380.setCoord(Coordinate381)
ColorRGBA382 = ColorRGBA()
ColorRGBA382.setUSE("HAnimSiteLineColorRGBA")

LineSet380.setColor(ColorRGBA382)

Shape379.setGeometry(LineSet380)

HAnimSegment371.addChildren(Shape379)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_digit2'/>
Shape383 = Shape()
LineSet384 = LineSet()
LineSet384.setVertexCount([2])
Coordinate385 = Coordinate()
Coordinate385.setPoint([-0.1086,0,0.0762,-0.0883,0.0134,0.1383])

LineSet384.setCoord(Coordinate385)
ColorRGBA386 = ColorRGBA()
ColorRGBA386.setUSE("HAnimSiteLineColorRGBA")

LineSet384.setColor(ColorRGBA386)

Shape383.setGeometry(LineSet384)

HAnimSegment371.addChildren(Shape383)
HAnimSite387 = HAnimSite()
HAnimSite387.setName("r_forefoot_tip")
HAnimSite387.setDEF("hanim_r_forefoot_tip")
HAnimSite387.setTranslation([-0.1043,0.0227,0.145])
#HAnimSite visualization shape
TouchSensor388 = TouchSensor()
TouchSensor388.setDescription("HAnimSite r_forefoot_tip")

HAnimSite387.addChildren(TouchSensor388)
Shape389 = Shape()
Shape389.setUSE("HAnimSiteShape")

HAnimSite387.addChildren(Shape389)

HAnimSegment371.addChildren(HAnimSite387)
HAnimSite390 = HAnimSite()
HAnimSite390.setName("r_metatarsal_pha5_pt")
HAnimSite390.setDEF("hanim_r_metatarsal_pha5_pt")
HAnimSite390.setTranslation([-0.1523,0.0166,0.0895])
#HAnimSite visualization shape
TouchSensor391 = TouchSensor()
TouchSensor391.setDescription("HAnimSite r_metatarsal_pha5")

HAnimSite390.addChildren(TouchSensor391)
Shape392 = Shape()
Shape392.setUSE("HAnimSiteShape")

HAnimSite390.addChildren(Shape392)

HAnimSegment371.addChildren(HAnimSite390)
HAnimSite393 = HAnimSite()
HAnimSite393.setName("r_digit2_pt")
HAnimSite393.setDEF("hanim_r_digit2_pt")
HAnimSite393.setTranslation([-0.0883,0.0134,0.1383])
#HAnimSite visualization shape
TouchSensor394 = TouchSensor()
TouchSensor394.setDescription("HAnimSite r_digit2")

HAnimSite393.addChildren(TouchSensor394)
Shape395 = Shape()
Shape395.setUSE("HAnimSiteShape")

HAnimSite393.addChildren(Shape395)

HAnimSegment371.addChildren(HAnimSite393)

HAnimJoint370.addChildren(HAnimSegment371)

HAnimJoint354.addChildren(HAnimJoint370)

HAnimJoint345.addChildren(HAnimJoint354)

HAnimJoint308.addChildren(HAnimJoint345)

HAnimJoint299.addChildren(HAnimJoint308)

HAnimJoint269.addChildren(HAnimJoint299)

HAnimJoint62.addChildren(HAnimJoint269)

HAnimJoint46.addChildren(HAnimJoint62)
HAnimJoint396 = HAnimJoint()
HAnimJoint396.setName("vl5")
HAnimJoint396.setDEF("hanim_vl5")
HAnimJoint396.setCenter([0.0028,1.0568,-0.0776])
HAnimJoint396.setStiffness([0,0,0])
HAnimSegment397 = HAnimSegment()
HAnimSegment397.setName("l5")
HAnimSegment397.setDEF("hanim_l5")
#<HAnimJoint name='vl5'/> visualization sphere within <HAnimSegment name='l5'/>
TouchSensor398 = TouchSensor()
TouchSensor398.setDescription("HAnimJoint vl5, HAnimSegment l5")

HAnimSegment397.addChildren(TouchSensor398)
Transform399 = Transform()
Transform399.setTranslation([0.0028,1.0568,-0.0776])
Shape400 = Shape()
Shape400.setUSE("HAnimJointShape")

Transform399.addChildren(Shape400)

HAnimSegment397.addChildren(Transform399)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl5'/> to <HAnimJoint name='vl4'/>
Shape401 = Shape()
LineSet402 = LineSet()
LineSet402.setVertexCount([2])
Coordinate403 = Coordinate()
Coordinate403.setPoint([0.0028,1.0568,-0.0776,0.0035,1.0925,-0.0787])

LineSet402.setCoord(Coordinate403)
ColorRGBA404 = ColorRGBA()
ColorRGBA404.setUSE("HAnimSegmentLineColorRGBA")

LineSet402.setColor(ColorRGBA404)

Shape401.setGeometry(LineSet402)

HAnimSegment397.addChildren(Shape401)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='waist_preferred_post'/>
Shape405 = Shape()
LineSet406 = LineSet()
LineSet406.setVertexCount([2])
Coordinate407 = Coordinate()
Coordinate407.setPoint([0.0028,1.0568,-0.0776,0,1.0915,-0.1091])

LineSet406.setCoord(Coordinate407)
ColorRGBA408 = ColorRGBA()
ColorRGBA408.setUSE("HAnimSiteLineColorRGBA")

LineSet406.setColor(ColorRGBA408)

Shape405.setGeometry(LineSet406)

HAnimSegment397.addChildren(Shape405)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='navel'/>
Shape409 = Shape()
LineSet410 = LineSet()
LineSet410.setVertexCount([2])
Coordinate411 = Coordinate()
Coordinate411.setPoint([0.0028,1.0568,-0.0776,0.0069,1.0966,0.1017])

LineSet410.setCoord(Coordinate411)
ColorRGBA412 = ColorRGBA()
ColorRGBA412.setUSE("HAnimSiteLineColorRGBA")

LineSet410.setColor(ColorRGBA412)

Shape409.setGeometry(LineSet410)

HAnimSegment397.addChildren(Shape409)
HAnimSite413 = HAnimSite()
HAnimSite413.setName("waist_preferred_post_pt")
HAnimSite413.setDEF("hanim_waist_preferred_post_pt")
HAnimSite413.setTranslation([0,1.0915,-0.1091])
#HAnimSite visualization shape
TouchSensor414 = TouchSensor()
TouchSensor414.setDescription("HAnimSite waist_preferred_post")

HAnimSite413.addChildren(TouchSensor414)
Shape415 = Shape()
Shape415.setUSE("HAnimSiteShape")

HAnimSite413.addChildren(Shape415)

HAnimSegment397.addChildren(HAnimSite413)
HAnimSite416 = HAnimSite()
HAnimSite416.setName("navel_pt")
HAnimSite416.setDEF("hanim_navel_pt")
HAnimSite416.setTranslation([0.0069,1.0966,0.1017])
#HAnimSite visualization shape
TouchSensor417 = TouchSensor()
TouchSensor417.setDescription("HAnimSite navel")

HAnimSite416.addChildren(TouchSensor417)
Shape418 = Shape()
Shape418.setUSE("HAnimSiteShape")

HAnimSite416.addChildren(Shape418)

HAnimSegment397.addChildren(HAnimSite416)

HAnimJoint396.addChildren(HAnimSegment397)
HAnimJoint419 = HAnimJoint()
HAnimJoint419.setName("vl4")
HAnimJoint419.setDEF("hanim_vl4")
HAnimJoint419.setCenter([0.0035,1.0925,-0.0787])
HAnimJoint419.setStiffness([0,0,0])
HAnimSegment420 = HAnimSegment()
HAnimSegment420.setName("l4")
HAnimSegment420.setDEF("hanim_l4")
#<HAnimJoint name='vl4'/> visualization sphere within <HAnimSegment name='l4'/>
TouchSensor421 = TouchSensor()
TouchSensor421.setDescription("HAnimJoint vl4, HAnimSegment l4")

HAnimSegment420.addChildren(TouchSensor421)
Transform422 = Transform()
Transform422.setTranslation([0.0035,1.0925,-0.0787])
Shape423 = Shape()
Shape423.setUSE("HAnimJointShape")

Transform422.addChildren(Shape423)

HAnimSegment420.addChildren(Transform422)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl4'/> to <HAnimJoint name='vl3'/>
Shape424 = Shape()
LineSet425 = LineSet()
LineSet425.setVertexCount([2])
Coordinate426 = Coordinate()
Coordinate426.setPoint([0.0035,1.0925,-0.0787,0.0041,1.1276,-0.0796])

LineSet425.setCoord(Coordinate426)
ColorRGBA427 = ColorRGBA()
ColorRGBA427.setUSE("HAnimSegmentLineColorRGBA")

LineSet425.setColor(ColorRGBA427)

Shape424.setGeometry(LineSet425)

HAnimSegment420.addChildren(Shape424)

HAnimJoint419.addChildren(HAnimSegment420)
HAnimJoint428 = HAnimJoint()
HAnimJoint428.setName("vl3")
HAnimJoint428.setDEF("hanim_vl3")
HAnimJoint428.setCenter([0.0041,1.1276,-0.0796])
HAnimJoint428.setStiffness([0,0,0])
HAnimSegment429 = HAnimSegment()
HAnimSegment429.setName("l3")
HAnimSegment429.setDEF("hanim_l3")
#<HAnimJoint name='vl3'/> visualization sphere within <HAnimSegment name='l3'/>
TouchSensor430 = TouchSensor()
TouchSensor430.setDescription("HAnimJoint vl3, HAnimSegment l3")

HAnimSegment429.addChildren(TouchSensor430)
Transform431 = Transform()
Transform431.setTranslation([0.0041,1.1276,-0.0796])
Shape432 = Shape()
Shape432.setUSE("HAnimJointShape")

Transform431.addChildren(Shape432)

HAnimSegment429.addChildren(Transform431)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl3'/> to <HAnimJoint name='vl2'/>
Shape433 = Shape()
LineSet434 = LineSet()
LineSet434.setVertexCount([2])
Coordinate435 = Coordinate()
Coordinate435.setPoint([0.0041,1.1276,-0.0796,0.0045,1.1546,-0.08])

LineSet434.setCoord(Coordinate435)
ColorRGBA436 = ColorRGBA()
ColorRGBA436.setUSE("HAnimSegmentLineColorRGBA")

LineSet434.setColor(ColorRGBA436)

Shape433.setGeometry(LineSet434)

HAnimSegment429.addChildren(Shape433)

HAnimJoint428.addChildren(HAnimSegment429)
HAnimJoint437 = HAnimJoint()
HAnimJoint437.setName("vl2")
HAnimJoint437.setDEF("hanim_vl2")
HAnimJoint437.setCenter([0.0045,1.1546,-0.08])
HAnimJoint437.setStiffness([0,0,0])
HAnimSegment438 = HAnimSegment()
HAnimSegment438.setName("l2")
HAnimSegment438.setDEF("hanim_l2")
#<HAnimJoint name='vl2'/> visualization sphere within <HAnimSegment name='l2'/>
TouchSensor439 = TouchSensor()
TouchSensor439.setDescription("HAnimJoint vl2, HAnimSegment l2")

HAnimSegment438.addChildren(TouchSensor439)
Transform440 = Transform()
Transform440.setTranslation([0.0045,1.1546,-0.08])
Shape441 = Shape()
Shape441.setUSE("HAnimJointShape")

Transform440.addChildren(Shape441)

HAnimSegment438.addChildren(Transform440)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl2'/> to <HAnimJoint name='vl1'/>
Shape442 = Shape()
LineSet443 = LineSet()
LineSet443.setVertexCount([2])
Coordinate444 = Coordinate()
Coordinate444.setPoint([0.0045,1.1546,-0.08,0.0048,1.1912,-0.0805])

LineSet443.setCoord(Coordinate444)
ColorRGBA445 = ColorRGBA()
ColorRGBA445.setUSE("HAnimSegmentLineColorRGBA")

LineSet443.setColor(ColorRGBA445)

Shape442.setGeometry(LineSet443)

HAnimSegment438.addChildren(Shape442)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='r_rib10'/>
Shape446 = Shape()
LineSet447 = LineSet()
LineSet447.setVertexCount([2])
Coordinate448 = Coordinate()
Coordinate448.setPoint([0.0045,1.1546,-0.08,-0.0711,1.1941,0.1016])

LineSet447.setCoord(Coordinate448)
ColorRGBA449 = ColorRGBA()
ColorRGBA449.setUSE("HAnimSiteLineColorRGBA")

LineSet447.setColor(ColorRGBA449)

Shape446.setGeometry(LineSet447)

HAnimSegment438.addChildren(Shape446)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='l_rib10'/>
Shape450 = Shape()
LineSet451 = LineSet()
LineSet451.setVertexCount([2])
Coordinate452 = Coordinate()
Coordinate452.setPoint([0.0045,1.1546,-0.08,0.0871,1.1925,0.0992])

LineSet451.setCoord(Coordinate452)
ColorRGBA453 = ColorRGBA()
ColorRGBA453.setUSE("HAnimSiteLineColorRGBA")

LineSet451.setColor(ColorRGBA453)

Shape450.setGeometry(LineSet451)

HAnimSegment438.addChildren(Shape450)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='rib10_midspine'/>
Shape454 = Shape()
LineSet455 = LineSet()
LineSet455.setVertexCount([2])
Coordinate456 = Coordinate()
Coordinate456.setPoint([0.0045,1.1546,-0.08,0.0049,1.1908,-0.1113])

LineSet455.setCoord(Coordinate456)
ColorRGBA457 = ColorRGBA()
ColorRGBA457.setUSE("HAnimSiteLineColorRGBA")

LineSet455.setColor(ColorRGBA457)

Shape454.setGeometry(LineSet455)

HAnimSegment438.addChildren(Shape454)
HAnimSite458 = HAnimSite()
HAnimSite458.setName("r_rib10_pt")
HAnimSite458.setDEF("hanim_r_rib10_pt")
HAnimSite458.setTranslation([-0.0711,1.1941,0.1016])
#HAnimSite visualization shape
TouchSensor459 = TouchSensor()
TouchSensor459.setDescription("HAnimSite r_rib10")

HAnimSite458.addChildren(TouchSensor459)
Shape460 = Shape()
Shape460.setUSE("HAnimSiteShape")

HAnimSite458.addChildren(Shape460)

HAnimSegment438.addChildren(HAnimSite458)
HAnimSite461 = HAnimSite()
HAnimSite461.setName("l_rib10_pt")
HAnimSite461.setDEF("hanim_l_rib10_pt")
HAnimSite461.setTranslation([0.0871,1.1925,0.0992])
#HAnimSite visualization shape
TouchSensor462 = TouchSensor()
TouchSensor462.setDescription("HAnimSite l_rib10")

HAnimSite461.addChildren(TouchSensor462)
Shape463 = Shape()
Shape463.setUSE("HAnimSiteShape")

HAnimSite461.addChildren(Shape463)

HAnimSegment438.addChildren(HAnimSite461)
HAnimSite464 = HAnimSite()
HAnimSite464.setName("rib10_midspine_pt")
HAnimSite464.setDEF("hanim_rib10_midspine_pt")
HAnimSite464.setTranslation([0.0049,1.1908,-0.1113])
#HAnimSite visualization shape
TouchSensor465 = TouchSensor()
TouchSensor465.setDescription("HAnimSite rib10_midspine")

HAnimSite464.addChildren(TouchSensor465)
Shape466 = Shape()
Shape466.setUSE("HAnimSiteShape")

HAnimSite464.addChildren(Shape466)

HAnimSegment438.addChildren(HAnimSite464)

HAnimJoint437.addChildren(HAnimSegment438)
HAnimJoint467 = HAnimJoint()
HAnimJoint467.setName("vl1")
HAnimJoint467.setDEF("hanim_vl1")
HAnimJoint467.setCenter([0.0048,1.1912,-0.0805])
HAnimJoint467.setStiffness([0,0,0])
HAnimSegment468 = HAnimSegment()
HAnimSegment468.setName("l1")
HAnimSegment468.setDEF("hanim_l1")
#<HAnimJoint name='vl1'/> visualization sphere within <HAnimSegment name='l1'/>
TouchSensor469 = TouchSensor()
TouchSensor469.setDescription("HAnimJoint vl1, HAnimSegment l1")

HAnimSegment468.addChildren(TouchSensor469)
Transform470 = Transform()
Transform470.setTranslation([0.0048,1.1912,-0.0805])
Shape471 = Shape()
Shape471.setUSE("HAnimJointShape")

Transform470.addChildren(Shape471)

HAnimSegment468.addChildren(Transform470)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl1'/> to <HAnimJoint name='vt12'/>
Shape472 = Shape()
LineSet473 = LineSet()
LineSet473.setVertexCount([2])
Coordinate474 = Coordinate()
Coordinate474.setPoint([0.0048,1.1912,-0.0805,0.0051,1.2278,-0.0808])

LineSet473.setCoord(Coordinate474)
ColorRGBA475 = ColorRGBA()
ColorRGBA475.setUSE("HAnimSegmentLineColorRGBA")

LineSet473.setColor(ColorRGBA475)

Shape472.setGeometry(LineSet473)

HAnimSegment468.addChildren(Shape472)

HAnimJoint467.addChildren(HAnimSegment468)
HAnimJoint476 = HAnimJoint()
HAnimJoint476.setName("vt12")
HAnimJoint476.setDEF("hanim_vt12")
HAnimJoint476.setCenter([0.0051,1.2278,-0.0808])
HAnimJoint476.setStiffness([0,0,0])
HAnimSegment477 = HAnimSegment()
HAnimSegment477.setName("t12")
HAnimSegment477.setDEF("hanim_t12")
#<HAnimJoint name='vt12'/> visualization sphere within <HAnimSegment name='t12'/>
TouchSensor478 = TouchSensor()
TouchSensor478.setDescription("HAnimJoint vt12, HAnimSegment t12")

HAnimSegment477.addChildren(TouchSensor478)
Transform479 = Transform()
Transform479.setTranslation([0.0051,1.2278,-0.0808])
Shape480 = Shape()
Shape480.setUSE("HAnimJointShape")

Transform479.addChildren(Shape480)

HAnimSegment477.addChildren(Transform479)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt12'/> to <HAnimJoint name='vt11'/>
Shape481 = Shape()
LineSet482 = LineSet()
LineSet482.setVertexCount([2])
Coordinate483 = Coordinate()
Coordinate483.setPoint([0.0051,1.2278,-0.0808,0.0053,1.2679,-0.081])

LineSet482.setCoord(Coordinate483)
ColorRGBA484 = ColorRGBA()
ColorRGBA484.setUSE("HAnimSegmentLineColorRGBA")

LineSet482.setColor(ColorRGBA484)

Shape481.setGeometry(LineSet482)

HAnimSegment477.addChildren(Shape481)

HAnimJoint476.addChildren(HAnimSegment477)
HAnimJoint485 = HAnimJoint()
HAnimJoint485.setName("vt11")
HAnimJoint485.setDEF("hanim_vt11")
HAnimJoint485.setCenter([0.0053,1.2679,-0.081])
HAnimJoint485.setStiffness([0,0,0])
HAnimSegment486 = HAnimSegment()
HAnimSegment486.setName("t11")
HAnimSegment486.setDEF("hanim_t11")
#<HAnimJoint name='vt11'/> visualization sphere within <HAnimSegment name='t11'/>
TouchSensor487 = TouchSensor()
TouchSensor487.setDescription("HAnimJoint vt11, HAnimSegment t11")

HAnimSegment486.addChildren(TouchSensor487)
Transform488 = Transform()
Transform488.setTranslation([0.0053,1.2679,-0.081])
Shape489 = Shape()
Shape489.setUSE("HAnimJointShape")

Transform488.addChildren(Shape489)

HAnimSegment486.addChildren(Transform488)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt11'/> to <HAnimJoint name='vt10'/>
Shape490 = Shape()
LineSet491 = LineSet()
LineSet491.setVertexCount([2])
Coordinate492 = Coordinate()
Coordinate492.setPoint([0.0053,1.2679,-0.081,0.0056,1.2848,-0.0822])

LineSet491.setCoord(Coordinate492)
ColorRGBA493 = ColorRGBA()
ColorRGBA493.setUSE("HAnimSegmentLineColorRGBA")

LineSet491.setColor(ColorRGBA493)

Shape490.setGeometry(LineSet491)

HAnimSegment486.addChildren(Shape490)

HAnimJoint485.addChildren(HAnimSegment486)
HAnimJoint494 = HAnimJoint()
HAnimJoint494.setName("vt10")
HAnimJoint494.setDEF("hanim_vt10")
HAnimJoint494.setCenter([0.0056,1.2848,-0.0822])
HAnimJoint494.setStiffness([0,0,0])
HAnimSegment495 = HAnimSegment()
HAnimSegment495.setName("t10")
HAnimSegment495.setDEF("hanim_t10")
#<HAnimJoint name='vt10'/> visualization sphere within <HAnimSegment name='t10'/>
TouchSensor496 = TouchSensor()
TouchSensor496.setDescription("HAnimJoint vt10, HAnimSegment t10")

HAnimSegment495.addChildren(TouchSensor496)
Transform497 = Transform()
Transform497.setTranslation([0.0056,1.2848,-0.0822])
Shape498 = Shape()
Shape498.setUSE("HAnimJointShape")

Transform497.addChildren(Shape498)

HAnimSegment495.addChildren(Transform497)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt10'/> to <HAnimJoint name='vt9'/>
Shape499 = Shape()
LineSet500 = LineSet()
LineSet500.setVertexCount([2])
Coordinate501 = Coordinate()
Coordinate501.setPoint([0.0056,1.2848,-0.0822,0.0057,1.3126,-0.0838])

LineSet500.setCoord(Coordinate501)
ColorRGBA502 = ColorRGBA()
ColorRGBA502.setUSE("HAnimSegmentLineColorRGBA")

LineSet500.setColor(ColorRGBA502)

Shape499.setGeometry(LineSet500)

HAnimSegment495.addChildren(Shape499)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt10'/> to <HAnimSite name='substernale'/>
Shape503 = Shape()
LineSet504 = LineSet()
LineSet504.setVertexCount([2])
Coordinate505 = Coordinate()
Coordinate505.setPoint([0.0056,1.2848,-0.0822,0.0085,1.2995,0.1147])

LineSet504.setCoord(Coordinate505)
ColorRGBA506 = ColorRGBA()
ColorRGBA506.setUSE("HAnimSiteLineColorRGBA")

LineSet504.setColor(ColorRGBA506)

Shape503.setGeometry(LineSet504)

HAnimSegment495.addChildren(Shape503)
HAnimSite507 = HAnimSite()
HAnimSite507.setName("substernale_pt")
HAnimSite507.setDEF("hanim_substernale_pt")
HAnimSite507.setTranslation([0.0085,1.2995,0.1147])
#HAnimSite visualization shape
TouchSensor508 = TouchSensor()
TouchSensor508.setDescription("HAnimSite substernale")

HAnimSite507.addChildren(TouchSensor508)
Shape509 = Shape()
Shape509.setUSE("HAnimSiteShape")

HAnimSite507.addChildren(Shape509)

HAnimSegment495.addChildren(HAnimSite507)

HAnimJoint494.addChildren(HAnimSegment495)
HAnimJoint510 = HAnimJoint()
HAnimJoint510.setName("vt9")
HAnimJoint510.setDEF("hanim_vt9")
HAnimJoint510.setCenter([0.0057,1.3126,-0.0838])
HAnimJoint510.setStiffness([0,0,0])
HAnimSegment511 = HAnimSegment()
HAnimSegment511.setName("t9")
HAnimSegment511.setDEF("hanim_t9")
#<HAnimJoint name='vt9'/> visualization sphere within <HAnimSegment name='t9'/>
TouchSensor512 = TouchSensor()
TouchSensor512.setDescription("HAnimJoint vt9, HAnimSegment t9")

HAnimSegment511.addChildren(TouchSensor512)
Transform513 = Transform()
Transform513.setTranslation([0.0057,1.3126,-0.0838])
Shape514 = Shape()
Shape514.setUSE("HAnimJointShape")

Transform513.addChildren(Shape514)

HAnimSegment511.addChildren(Transform513)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt9'/> to <HAnimJoint name='vt8'/>
Shape515 = Shape()
LineSet516 = LineSet()
LineSet516.setVertexCount([2])
Coordinate517 = Coordinate()
Coordinate517.setPoint([0.0057,1.3126,-0.0838,0.0057,1.3382,-0.0845])

LineSet516.setCoord(Coordinate517)
ColorRGBA518 = ColorRGBA()
ColorRGBA518.setUSE("HAnimSegmentLineColorRGBA")

LineSet516.setColor(ColorRGBA518)

Shape515.setGeometry(LineSet516)

HAnimSegment511.addChildren(Shape515)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='r_thelion'/>
Shape519 = Shape()
LineSet520 = LineSet()
LineSet520.setVertexCount([2])
Coordinate521 = Coordinate()
Coordinate521.setPoint([0.0057,1.3126,-0.0838,-0.0736,1.3385,0.1217])

LineSet520.setCoord(Coordinate521)
ColorRGBA522 = ColorRGBA()
ColorRGBA522.setUSE("HAnimSiteLineColorRGBA")

LineSet520.setColor(ColorRGBA522)

Shape519.setGeometry(LineSet520)

HAnimSegment511.addChildren(Shape519)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='l_thelion'/>
Shape523 = Shape()
LineSet524 = LineSet()
LineSet524.setVertexCount([2])
Coordinate525 = Coordinate()
Coordinate525.setPoint([0.0057,1.3126,-0.0838,0.0918,1.3382,0.1192])

LineSet524.setCoord(Coordinate525)
ColorRGBA526 = ColorRGBA()
ColorRGBA526.setUSE("HAnimSiteLineColorRGBA")

LineSet524.setColor(ColorRGBA526)

Shape523.setGeometry(LineSet524)

HAnimSegment511.addChildren(Shape523)
HAnimSite527 = HAnimSite()
HAnimSite527.setName("r_thelion_pt")
HAnimSite527.setDEF("hanim_r_thelion_pt")
HAnimSite527.setTranslation([-0.0736,1.3385,0.1217])
#HAnimSite visualization shape
TouchSensor528 = TouchSensor()
TouchSensor528.setDescription("HAnimSite r_thelion")

HAnimSite527.addChildren(TouchSensor528)
Shape529 = Shape()
Shape529.setUSE("HAnimSiteShape")

HAnimSite527.addChildren(Shape529)

HAnimSegment511.addChildren(HAnimSite527)
HAnimSite530 = HAnimSite()
HAnimSite530.setName("l_thelion_pt")
HAnimSite530.setDEF("hanim_l_thelion_pt")
HAnimSite530.setTranslation([0.0918,1.3382,0.1192])
#HAnimSite visualization shape
TouchSensor531 = TouchSensor()
TouchSensor531.setDescription("HAnimSite l_thelion")

HAnimSite530.addChildren(TouchSensor531)
Shape532 = Shape()
Shape532.setUSE("HAnimSiteShape")

HAnimSite530.addChildren(Shape532)

HAnimSegment511.addChildren(HAnimSite530)

HAnimJoint510.addChildren(HAnimSegment511)
HAnimJoint533 = HAnimJoint()
HAnimJoint533.setName("vt8")
HAnimJoint533.setDEF("hanim_vt8")
HAnimJoint533.setCenter([0.0057,1.3382,-0.0845])
HAnimJoint533.setStiffness([0,0,0])
HAnimSegment534 = HAnimSegment()
HAnimSegment534.setName("t8")
HAnimSegment534.setDEF("hanim_t8")
#<HAnimJoint name='vt8'/> visualization sphere within <HAnimSegment name='t8'/>
TouchSensor535 = TouchSensor()
TouchSensor535.setDescription("HAnimJoint vt8, HAnimSegment t8")

HAnimSegment534.addChildren(TouchSensor535)
Transform536 = Transform()
Transform536.setTranslation([0.0057,1.3382,-0.0845])
Shape537 = Shape()
Shape537.setUSE("HAnimJointShape")

Transform536.addChildren(Shape537)

HAnimSegment534.addChildren(Transform536)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt8'/> to <HAnimJoint name='vt7'/>
Shape538 = Shape()
LineSet539 = LineSet()
LineSet539.setVertexCount([2])
Coordinate540 = Coordinate()
Coordinate540.setPoint([0.0057,1.3382,-0.0845,0.0058,1.3625,-0.0833])

LineSet539.setCoord(Coordinate540)
ColorRGBA541 = ColorRGBA()
ColorRGBA541.setUSE("HAnimSegmentLineColorRGBA")

LineSet539.setColor(ColorRGBA541)

Shape538.setGeometry(LineSet539)

HAnimSegment534.addChildren(Shape538)

HAnimJoint533.addChildren(HAnimSegment534)
HAnimJoint542 = HAnimJoint()
HAnimJoint542.setName("vt7")
HAnimJoint542.setDEF("hanim_vt7")
HAnimJoint542.setCenter([0.0058,1.3625,-0.0833])
HAnimJoint542.setStiffness([0,0,0])
HAnimSegment543 = HAnimSegment()
HAnimSegment543.setName("t7")
HAnimSegment543.setDEF("hanim_t7")
#<HAnimJoint name='vt7'/> visualization sphere within <HAnimSegment name='t7'/>
TouchSensor544 = TouchSensor()
TouchSensor544.setDescription("HAnimJoint vt7, HAnimSegment t7")

HAnimSegment543.addChildren(TouchSensor544)
Transform545 = Transform()
Transform545.setTranslation([0.0058,1.3625,-0.0833])
Shape546 = Shape()
Shape546.setUSE("HAnimJointShape")

Transform545.addChildren(Shape546)

HAnimSegment543.addChildren(Transform545)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt7'/> to <HAnimJoint name='vt6'/>
Shape547 = Shape()
LineSet548 = LineSet()
LineSet548.setVertexCount([2])
Coordinate549 = Coordinate()
Coordinate549.setPoint([0.0058,1.3625,-0.0833,0.0059,1.3866,-0.08])

LineSet548.setCoord(Coordinate549)
ColorRGBA550 = ColorRGBA()
ColorRGBA550.setUSE("HAnimSegmentLineColorRGBA")

LineSet548.setColor(ColorRGBA550)

Shape547.setGeometry(LineSet548)

HAnimSegment543.addChildren(Shape547)

HAnimJoint542.addChildren(HAnimSegment543)
HAnimJoint551 = HAnimJoint()
HAnimJoint551.setName("vt6")
HAnimJoint551.setDEF("hanim_vt6")
HAnimJoint551.setCenter([0.0059,1.3866,-0.08])
HAnimJoint551.setStiffness([0,0,0])
HAnimSegment552 = HAnimSegment()
HAnimSegment552.setName("t6")
HAnimSegment552.setDEF("hanim_t6")
#<HAnimJoint name='vt6'/> visualization sphere within <HAnimSegment name='t6'/>
TouchSensor553 = TouchSensor()
TouchSensor553.setDescription("HAnimJoint vt6, HAnimSegment t6")

HAnimSegment552.addChildren(TouchSensor553)
Transform554 = Transform()
Transform554.setTranslation([0.0059,1.3866,-0.08])
Shape555 = Shape()
Shape555.setUSE("HAnimJointShape")

Transform554.addChildren(Shape555)

HAnimSegment552.addChildren(Transform554)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt6'/> to <HAnimJoint name='vt5'/>
Shape556 = Shape()
LineSet557 = LineSet()
LineSet557.setVertexCount([2])
Coordinate558 = Coordinate()
Coordinate558.setPoint([0.0059,1.3866,-0.08,0.006,1.4102,-0.0745])

LineSet557.setCoord(Coordinate558)
ColorRGBA559 = ColorRGBA()
ColorRGBA559.setUSE("HAnimSegmentLineColorRGBA")

LineSet557.setColor(ColorRGBA559)

Shape556.setGeometry(LineSet557)

HAnimSegment552.addChildren(Shape556)

HAnimJoint551.addChildren(HAnimSegment552)
HAnimJoint560 = HAnimJoint()
HAnimJoint560.setName("vt5")
HAnimJoint560.setDEF("hanim_vt5")
HAnimJoint560.setCenter([0.006,1.4102,-0.0745])
HAnimJoint560.setStiffness([0,0,0])
HAnimSegment561 = HAnimSegment()
HAnimSegment561.setName("t5")
HAnimSegment561.setDEF("hanim_t5")
#<HAnimJoint name='vt5'/> visualization sphere within <HAnimSegment name='t5'/>
TouchSensor562 = TouchSensor()
TouchSensor562.setDescription("HAnimJoint vt5, HAnimSegment t5")

HAnimSegment561.addChildren(TouchSensor562)
Transform563 = Transform()
Transform563.setTranslation([0.006,1.4102,-0.0745])
Shape564 = Shape()
Shape564.setUSE("HAnimJointShape")

Transform563.addChildren(Shape564)

HAnimSegment561.addChildren(Transform563)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt5'/> to <HAnimJoint name='vt4'/>
Shape565 = Shape()
LineSet566 = LineSet()
LineSet566.setVertexCount([2])
Coordinate567 = Coordinate()
Coordinate567.setPoint([0.006,1.4102,-0.0745,0.0061,1.432,-0.0675])

LineSet566.setCoord(Coordinate567)
ColorRGBA568 = ColorRGBA()
ColorRGBA568.setUSE("HAnimSegmentLineColorRGBA")

LineSet566.setColor(ColorRGBA568)

Shape565.setGeometry(LineSet566)

HAnimSegment561.addChildren(Shape565)

HAnimJoint560.addChildren(HAnimSegment561)
HAnimJoint569 = HAnimJoint()
HAnimJoint569.setName("vt4")
HAnimJoint569.setDEF("hanim_vt4")
HAnimJoint569.setCenter([0.0061,1.432,-0.0675])
HAnimJoint569.setStiffness([0,0,0])
HAnimSegment570 = HAnimSegment()
HAnimSegment570.setName("t4")
HAnimSegment570.setDEF("hanim_t4")
#<HAnimJoint name='vt4'/> visualization sphere within <HAnimSegment name='t4'/>
TouchSensor571 = TouchSensor()
TouchSensor571.setDescription("HAnimJoint vt4, HAnimSegment t4")

HAnimSegment570.addChildren(TouchSensor571)
Transform572 = Transform()
Transform572.setTranslation([0.0061,1.432,-0.0675])
Shape573 = Shape()
Shape573.setUSE("HAnimJointShape")

Transform572.addChildren(Shape573)

HAnimSegment570.addChildren(Transform572)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt4'/> to <HAnimJoint name='vt3'/>
Shape574 = Shape()
LineSet575 = LineSet()
LineSet575.setVertexCount([2])
Coordinate576 = Coordinate()
Coordinate576.setPoint([0.0061,1.432,-0.0675,0.0062,1.4583,-0.057])

LineSet575.setCoord(Coordinate576)
ColorRGBA577 = ColorRGBA()
ColorRGBA577.setUSE("HAnimSegmentLineColorRGBA")

LineSet575.setColor(ColorRGBA577)

Shape574.setGeometry(LineSet575)

HAnimSegment570.addChildren(Shape574)

HAnimJoint569.addChildren(HAnimSegment570)
HAnimJoint578 = HAnimJoint()
HAnimJoint578.setName("vt3")
HAnimJoint578.setDEF("hanim_vt3")
HAnimJoint578.setCenter([0.0062,1.4583,-0.057])
HAnimJoint578.setStiffness([0,0,0])
HAnimSegment579 = HAnimSegment()
HAnimSegment579.setName("t3")
HAnimSegment579.setDEF("hanim_t3")
#<HAnimJoint name='vt3'/> visualization sphere within <HAnimSegment name='t3'/>
TouchSensor580 = TouchSensor()
TouchSensor580.setDescription("HAnimJoint vt3, HAnimSegment t3")

HAnimSegment579.addChildren(TouchSensor580)
Transform581 = Transform()
Transform581.setTranslation([0.0062,1.4583,-0.057])
Shape582 = Shape()
Shape582.setUSE("HAnimJointShape")

Transform581.addChildren(Shape582)

HAnimSegment579.addChildren(Transform581)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt3'/> to <HAnimJoint name='vt2'/>
Shape583 = Shape()
LineSet584 = LineSet()
LineSet584.setVertexCount([2])
Coordinate585 = Coordinate()
Coordinate585.setPoint([0.0062,1.4583,-0.057,0.0063,1.4761,-0.0484])

LineSet584.setCoord(Coordinate585)
ColorRGBA586 = ColorRGBA()
ColorRGBA586.setUSE("HAnimSegmentLineColorRGBA")

LineSet584.setColor(ColorRGBA586)

Shape583.setGeometry(LineSet584)

HAnimSegment579.addChildren(Shape583)

HAnimJoint578.addChildren(HAnimSegment579)
HAnimJoint587 = HAnimJoint()
HAnimJoint587.setName("vt2")
HAnimJoint587.setDEF("hanim_vt2")
HAnimJoint587.setCenter([0.0063,1.4761,-0.0484])
HAnimJoint587.setStiffness([0,0,0])
HAnimSegment588 = HAnimSegment()
HAnimSegment588.setName("t2")
HAnimSegment588.setDEF("hanim_t2")
#<HAnimJoint name='vt2'/> visualization sphere within <HAnimSegment name='t2'/>
TouchSensor589 = TouchSensor()
TouchSensor589.setDescription("HAnimJoint vt2, HAnimSegment t2")

HAnimSegment588.addChildren(TouchSensor589)
Transform590 = Transform()
Transform590.setTranslation([0.0063,1.4761,-0.0484])
Shape591 = Shape()
Shape591.setUSE("HAnimJointShape")

Transform590.addChildren(Shape591)

HAnimSegment588.addChildren(Transform590)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt2'/> to <HAnimJoint name='vt1'/>
Shape592 = Shape()
LineSet593 = LineSet()
LineSet593.setVertexCount([2])
Coordinate594 = Coordinate()
Coordinate594.setPoint([0.0063,1.4761,-0.0484,0.0065,1.4951,-0.0387])

LineSet593.setCoord(Coordinate594)
ColorRGBA595 = ColorRGBA()
ColorRGBA595.setUSE("HAnimSegmentLineColorRGBA")

LineSet593.setColor(ColorRGBA595)

Shape592.setGeometry(LineSet593)

HAnimSegment588.addChildren(Shape592)

HAnimJoint587.addChildren(HAnimSegment588)
HAnimJoint596 = HAnimJoint()
HAnimJoint596.setName("vt1")
HAnimJoint596.setDEF("hanim_vt1")
HAnimJoint596.setCenter([0.0065,1.4951,-0.0387])
HAnimJoint596.setStiffness([0,0,0])
HAnimSegment597 = HAnimSegment()
HAnimSegment597.setName("t1")
HAnimSegment597.setDEF("hanim_t1")
#<HAnimJoint name='vt1'/> visualization sphere within <HAnimSegment name='t1'/>
TouchSensor598 = TouchSensor()
TouchSensor598.setDescription("HAnimJoint vt1, HAnimSegment t1")

HAnimSegment597.addChildren(TouchSensor598)
Transform599 = Transform()
Transform599.setTranslation([0.0065,1.4951,-0.0387])
Shape600 = Shape()
Shape600.setUSE("HAnimJointShape")

Transform599.addChildren(Shape600)

HAnimSegment597.addChildren(Transform599)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='vc7'/>
Shape601 = Shape()
LineSet602 = LineSet()
LineSet602.setVertexCount([2])
Coordinate603 = Coordinate()
Coordinate603.setPoint([0.0065,1.4951,-0.0387,0.0066,1.5132,-0.0301])

LineSet602.setCoord(Coordinate603)
ColorRGBA604 = ColorRGBA()
ColorRGBA604.setUSE("HAnimSegmentLineColorRGBA")

LineSet602.setColor(ColorRGBA604)

Shape601.setGeometry(LineSet602)

HAnimSegment597.addChildren(Shape601)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='l_sternoclavicular'/>
Shape605 = Shape()
LineSet606 = LineSet()
LineSet606.setVertexCount([2])
Coordinate607 = Coordinate()
Coordinate607.setPoint([0.0065,1.4951,-0.0387,0.082,1.4488,-0.0353])

LineSet606.setCoord(Coordinate607)
ColorRGBA608 = ColorRGBA()
ColorRGBA608.setUSE("HAnimSegmentLineColorRGBA")

LineSet606.setColor(ColorRGBA608)

Shape605.setGeometry(LineSet606)

HAnimSegment597.addChildren(Shape605)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='r_sternoclavicular'/>
Shape609 = Shape()
LineSet610 = LineSet()
LineSet610.setVertexCount([2])
Coordinate611 = Coordinate()
Coordinate611.setPoint([0.0065,1.4951,-0.0387,-0.082,1.4488,-0.0353])

LineSet610.setCoord(Coordinate611)
ColorRGBA612 = ColorRGBA()
ColorRGBA612.setUSE("HAnimSegmentLineColorRGBA")

LineSet610.setColor(ColorRGBA612)

Shape609.setGeometry(LineSet610)

HAnimSegment597.addChildren(Shape609)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='suprasternale'/>
Shape613 = Shape()
LineSet614 = LineSet()
LineSet614.setVertexCount([2])
Coordinate615 = Coordinate()
Coordinate615.setPoint([0.0065,1.4951,-0.0387,0.0084,1.4714,0.0551])

LineSet614.setCoord(Coordinate615)
ColorRGBA616 = ColorRGBA()
ColorRGBA616.setUSE("HAnimSiteLineColorRGBA")

LineSet614.setColor(ColorRGBA616)

Shape613.setGeometry(LineSet614)

HAnimSegment597.addChildren(Shape613)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='cervicale'/>
Shape617 = Shape()
LineSet618 = LineSet()
LineSet618.setVertexCount([2])
Coordinate619 = Coordinate()
Coordinate619.setPoint([0.0065,1.4951,-0.0387,0.0064,1.52,-0.0815])

LineSet618.setCoord(Coordinate619)
ColorRGBA620 = ColorRGBA()
ColorRGBA620.setUSE("HAnimSiteLineColorRGBA")

LineSet618.setColor(ColorRGBA620)

Shape617.setGeometry(LineSet618)

HAnimSegment597.addChildren(Shape617)
HAnimSite621 = HAnimSite()
HAnimSite621.setName("suprasternale_pt")
HAnimSite621.setDEF("hanim_suprasternale_pt")
HAnimSite621.setTranslation([0.0084,1.4714,0.0551])
#HAnimSite visualization shape
TouchSensor622 = TouchSensor()
TouchSensor622.setDescription("HAnimSite suprasternale")

HAnimSite621.addChildren(TouchSensor622)
Shape623 = Shape()
Shape623.setUSE("HAnimSiteShape")

HAnimSite621.addChildren(Shape623)

HAnimSegment597.addChildren(HAnimSite621)
HAnimSite624 = HAnimSite()
HAnimSite624.setName("cervicale_pt")
HAnimSite624.setDEF("hanim_cervicale_pt")
HAnimSite624.setTranslation([0.0064,1.52,-0.0815])
#HAnimSite visualization shape
TouchSensor625 = TouchSensor()
TouchSensor625.setDescription("HAnimSite cervicale")

HAnimSite624.addChildren(TouchSensor625)
Shape626 = Shape()
Shape626.setUSE("HAnimSiteShape")

HAnimSite624.addChildren(Shape626)

HAnimSegment597.addChildren(HAnimSite624)

HAnimJoint596.addChildren(HAnimSegment597)
HAnimJoint627 = HAnimJoint()
HAnimJoint627.setName("vc7")
HAnimJoint627.setDEF("hanim_vc7")
HAnimJoint627.setCenter([0.0066,1.5132,-0.0301])
HAnimJoint627.setStiffness([0,0,0])
HAnimSegment628 = HAnimSegment()
HAnimSegment628.setName("c7")
HAnimSegment628.setDEF("hanim_c7")
#<HAnimJoint name='vc7'/> visualization sphere within <HAnimSegment name='c7'/>
TouchSensor629 = TouchSensor()
TouchSensor629.setDescription("HAnimJoint vc7, HAnimSegment c7")

HAnimSegment628.addChildren(TouchSensor629)
Transform630 = Transform()
Transform630.setTranslation([0.0066,1.5132,-0.0301])
Shape631 = Shape()
Shape631.setUSE("HAnimJointShape")

Transform630.addChildren(Shape631)

HAnimSegment628.addChildren(Transform630)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc7'/> to <HAnimJoint name='vc6'/>
Shape632 = Shape()
LineSet633 = LineSet()
LineSet633.setVertexCount([2])
Coordinate634 = Coordinate()
Coordinate634.setPoint([0.0066,1.5132,-0.0301,0.0066,1.5357,-0.0143])

LineSet633.setCoord(Coordinate634)
ColorRGBA635 = ColorRGBA()
ColorRGBA635.setUSE("HAnimSegmentLineColorRGBA")

LineSet633.setColor(ColorRGBA635)

Shape632.setGeometry(LineSet633)

HAnimSegment628.addChildren(Shape632)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='r_neck_base'/>
Shape636 = Shape()
LineSet637 = LineSet()
LineSet637.setVertexCount([2])
Coordinate638 = Coordinate()
Coordinate638.setPoint([0.0066,1.5132,-0.0301,-0.0419,1.5149,-0.022])

LineSet637.setCoord(Coordinate638)
ColorRGBA639 = ColorRGBA()
ColorRGBA639.setUSE("HAnimSiteLineColorRGBA")

LineSet637.setColor(ColorRGBA639)

Shape636.setGeometry(LineSet637)

HAnimSegment628.addChildren(Shape636)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='l_neck_base'/>
Shape640 = Shape()
LineSet641 = LineSet()
LineSet641.setVertexCount([2])
Coordinate642 = Coordinate()
Coordinate642.setPoint([0.0066,1.5132,-0.0301,0.0646,1.5141,-0.038])

LineSet641.setCoord(Coordinate642)
ColorRGBA643 = ColorRGBA()
ColorRGBA643.setUSE("HAnimSiteLineColorRGBA")

LineSet641.setColor(ColorRGBA643)

Shape640.setGeometry(LineSet641)

HAnimSegment628.addChildren(Shape640)
HAnimSite644 = HAnimSite()
HAnimSite644.setName("r_neck_base_pt")
HAnimSite644.setDEF("hanim_r_neck_base_pt")
HAnimSite644.setTranslation([-0.0419,1.5149,-0.022])
#HAnimSite visualization shape
TouchSensor645 = TouchSensor()
TouchSensor645.setDescription("HAnimSite r_neck_base")

HAnimSite644.addChildren(TouchSensor645)
Shape646 = Shape()
Shape646.setUSE("HAnimSiteShape")

HAnimSite644.addChildren(Shape646)

HAnimSegment628.addChildren(HAnimSite644)
HAnimSite647 = HAnimSite()
HAnimSite647.setName("l_neck_base_pt")
HAnimSite647.setDEF("hanim_l_neck_base_pt")
HAnimSite647.setTranslation([0.0646,1.5141,-0.038])
#HAnimSite visualization shape
TouchSensor648 = TouchSensor()
TouchSensor648.setDescription("HAnimSite l_neck_base")

HAnimSite647.addChildren(TouchSensor648)
Shape649 = Shape()
Shape649.setUSE("HAnimSiteShape")

HAnimSite647.addChildren(Shape649)

HAnimSegment628.addChildren(HAnimSite647)

HAnimJoint627.addChildren(HAnimSegment628)
HAnimJoint650 = HAnimJoint()
HAnimJoint650.setName("vc6")
HAnimJoint650.setDEF("hanim_vc6")
HAnimJoint650.setCenter([0.0066,1.5357,-0.0143])
HAnimJoint650.setStiffness([0,0,0])
HAnimSegment651 = HAnimSegment()
HAnimSegment651.setName("c6")
HAnimSegment651.setDEF("hanim_c6")
#<HAnimJoint name='vc6'/> visualization sphere within <HAnimSegment name='c6'/>
TouchSensor652 = TouchSensor()
TouchSensor652.setDescription("HAnimJoint vc6, HAnimSegment c6")

HAnimSegment651.addChildren(TouchSensor652)
Transform653 = Transform()
Transform653.setTranslation([0.0066,1.5357,-0.0143])
Shape654 = Shape()
Shape654.setUSE("HAnimJointShape")

Transform653.addChildren(Shape654)

HAnimSegment651.addChildren(Transform653)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc6'/> to <HAnimJoint name='vc5'/>
Shape655 = Shape()
LineSet656 = LineSet()
LineSet656.setVertexCount([2])
Coordinate657 = Coordinate()
Coordinate657.setPoint([0.0066,1.5357,-0.0143,0.0066,1.552,-0.0082])

LineSet656.setCoord(Coordinate657)
ColorRGBA658 = ColorRGBA()
ColorRGBA658.setUSE("HAnimSegmentLineColorRGBA")

LineSet656.setColor(ColorRGBA658)

Shape655.setGeometry(LineSet656)

HAnimSegment651.addChildren(Shape655)

HAnimJoint650.addChildren(HAnimSegment651)
HAnimJoint659 = HAnimJoint()
HAnimJoint659.setName("vc5")
HAnimJoint659.setDEF("hanim_vc5")
HAnimJoint659.setCenter([0.0066,1.552,-0.0082])
HAnimJoint659.setStiffness([0,0,0])
HAnimSegment660 = HAnimSegment()
HAnimSegment660.setName("c5")
HAnimSegment660.setDEF("hanim_c5")
#<HAnimJoint name='vc5'/> visualization sphere within <HAnimSegment name='c5'/>
TouchSensor661 = TouchSensor()
TouchSensor661.setDescription("HAnimJoint vc5, HAnimSegment c5")

HAnimSegment660.addChildren(TouchSensor661)
Transform662 = Transform()
Transform662.setTranslation([0.0066,1.552,-0.0082])
Shape663 = Shape()
Shape663.setUSE("HAnimJointShape")

Transform662.addChildren(Shape663)

HAnimSegment660.addChildren(Transform662)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc5'/> to <HAnimJoint name='vc4'/>
Shape664 = Shape()
LineSet665 = LineSet()
LineSet665.setVertexCount([2])
Coordinate666 = Coordinate()
Coordinate666.setPoint([0.0066,1.552,-0.0082,0.0066,1.5662,-0.0084])

LineSet665.setCoord(Coordinate666)
ColorRGBA667 = ColorRGBA()
ColorRGBA667.setUSE("HAnimSegmentLineColorRGBA")

LineSet665.setColor(ColorRGBA667)

Shape664.setGeometry(LineSet665)

HAnimSegment660.addChildren(Shape664)

HAnimJoint659.addChildren(HAnimSegment660)
HAnimJoint668 = HAnimJoint()
HAnimJoint668.setName("vc4")
HAnimJoint668.setDEF("hanim_vc4")
HAnimJoint668.setCenter([0.0066,1.5662,-0.0084])
HAnimJoint668.setStiffness([0,0,0])
HAnimSegment669 = HAnimSegment()
HAnimSegment669.setName("c4")
HAnimSegment669.setDEF("hanim_c4")
#<HAnimJoint name='vc4'/> visualization sphere within <HAnimSegment name='c4'/>
TouchSensor670 = TouchSensor()
TouchSensor670.setDescription("HAnimJoint vc4, HAnimSegment c4")

HAnimSegment669.addChildren(TouchSensor670)
Transform671 = Transform()
Transform671.setTranslation([0.0066,1.5662,-0.0084])
Shape672 = Shape()
Shape672.setUSE("HAnimJointShape")

Transform671.addChildren(Shape672)

HAnimSegment669.addChildren(Transform671)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc4'/> to <HAnimJoint name='vc3'/>
Shape673 = Shape()
LineSet674 = LineSet()
LineSet674.setVertexCount([2])
Coordinate675 = Coordinate()
Coordinate675.setPoint([0.0066,1.5662,-0.0084,0.0066,1.58,-0.0103])

LineSet674.setCoord(Coordinate675)
ColorRGBA676 = ColorRGBA()
ColorRGBA676.setUSE("HAnimSegmentLineColorRGBA")

LineSet674.setColor(ColorRGBA676)

Shape673.setGeometry(LineSet674)

HAnimSegment669.addChildren(Shape673)

HAnimJoint668.addChildren(HAnimSegment669)
HAnimJoint677 = HAnimJoint()
HAnimJoint677.setName("vc3")
HAnimJoint677.setDEF("hanim_vc3")
HAnimJoint677.setCenter([0.0066,1.58,-0.0103])
HAnimJoint677.setStiffness([0,0,0])
HAnimSegment678 = HAnimSegment()
HAnimSegment678.setName("c3")
HAnimSegment678.setDEF("hanim_c3")
#<HAnimJoint name='vc3'/> visualization sphere within <HAnimSegment name='c3'/>
TouchSensor679 = TouchSensor()
TouchSensor679.setDescription("HAnimJoint vc3, HAnimSegment c3")

HAnimSegment678.addChildren(TouchSensor679)
Transform680 = Transform()
Transform680.setTranslation([0.0066,1.58,-0.0103])
Shape681 = Shape()
Shape681.setUSE("HAnimJointShape")

Transform680.addChildren(Shape681)

HAnimSegment678.addChildren(Transform680)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc3'/> to <HAnimJoint name='vc2'/>
Shape682 = Shape()
LineSet683 = LineSet()
LineSet683.setVertexCount([2])
Coordinate684 = Coordinate()
Coordinate684.setPoint([0.0066,1.58,-0.0103,0.0066,1.5928,-0.0103])

LineSet683.setCoord(Coordinate684)
ColorRGBA685 = ColorRGBA()
ColorRGBA685.setUSE("HAnimSegmentLineColorRGBA")

LineSet683.setColor(ColorRGBA685)

Shape682.setGeometry(LineSet683)

HAnimSegment678.addChildren(Shape682)

HAnimJoint677.addChildren(HAnimSegment678)
HAnimJoint686 = HAnimJoint()
HAnimJoint686.setName("vc2")
HAnimJoint686.setDEF("hanim_vc2")
HAnimJoint686.setCenter([0.0066,1.5928,-0.0103])
HAnimJoint686.setStiffness([0,0,0])
HAnimSegment687 = HAnimSegment()
HAnimSegment687.setName("c2")
HAnimSegment687.setDEF("hanim_c2")
#<HAnimJoint name='vc2'/> visualization sphere within <HAnimSegment name='c2'/>
TouchSensor688 = TouchSensor()
TouchSensor688.setDescription("HAnimJoint vc2, HAnimSegment c2")

HAnimSegment687.addChildren(TouchSensor688)
Transform689 = Transform()
Transform689.setTranslation([0.0066,1.5928,-0.0103])
Shape690 = Shape()
Shape690.setUSE("HAnimJointShape")

Transform689.addChildren(Shape690)

HAnimSegment687.addChildren(Transform689)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc2'/> to <HAnimJoint name='vc1'/>
Shape691 = Shape()
LineSet692 = LineSet()
LineSet692.setVertexCount([2])
Coordinate693 = Coordinate()
Coordinate693.setPoint([0.0066,1.5928,-0.0103,0.0066,1.6144,-0.0034])

LineSet692.setCoord(Coordinate693)
ColorRGBA694 = ColorRGBA()
ColorRGBA694.setUSE("HAnimSegmentLineColorRGBA")

LineSet692.setColor(ColorRGBA694)

Shape691.setGeometry(LineSet692)

HAnimSegment687.addChildren(Shape691)

HAnimJoint686.addChildren(HAnimSegment687)
HAnimJoint695 = HAnimJoint()
HAnimJoint695.setName("vc1")
HAnimJoint695.setDEF("hanim_vc1")
HAnimJoint695.setCenter([0.0066,1.6144,-0.0034])
HAnimJoint695.setStiffness([0,0,0])
HAnimSegment696 = HAnimSegment()
HAnimSegment696.setName("c1")
HAnimSegment696.setDEF("hanim_c1")
#<HAnimJoint name='vc1'/> visualization sphere within <HAnimSegment name='c1'/>
TouchSensor697 = TouchSensor()
TouchSensor697.setDescription("HAnimJoint vc1, HAnimSegment c1")

HAnimSegment696.addChildren(TouchSensor697)
Transform698 = Transform()
Transform698.setTranslation([0.0066,1.6144,-0.0034])
Shape699 = Shape()
Shape699.setUSE("HAnimJointShape")

Transform698.addChildren(Shape699)

HAnimSegment696.addChildren(Transform698)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc1'/> to <HAnimJoint name='skullbase'/>
Shape700 = Shape()
LineSet701 = LineSet()
LineSet701.setVertexCount([2])
Coordinate702 = Coordinate()
Coordinate702.setPoint([0.0066,1.6144,-0.0034,0.0044,1.6209,0.0236])

LineSet701.setCoord(Coordinate702)
ColorRGBA703 = ColorRGBA()
ColorRGBA703.setUSE("HAnimSegmentLineColorRGBA")

LineSet701.setColor(ColorRGBA703)

Shape700.setGeometry(LineSet701)

HAnimSegment696.addChildren(Shape700)

HAnimJoint695.addChildren(HAnimSegment696)
HAnimJoint704 = HAnimJoint()
HAnimJoint704.setName("skullbase")
HAnimJoint704.setDEF("hanim_skullbase")
HAnimJoint704.setCenter([0.0044,1.6209,0.0236])
HAnimJoint704.setStiffness([0,0,0])
HAnimSegment705 = HAnimSegment()
HAnimSegment705.setName("skull")
HAnimSegment705.setDEF("hanim_skull")
#<HAnimJoint name='skullbase'/> visualization sphere within <HAnimSegment name='skull'/>
TouchSensor706 = TouchSensor()
TouchSensor706.setDescription("HAnimJoint skullbase, HAnimSegment skull")

HAnimSegment705.addChildren(TouchSensor706)
Transform707 = Transform()
Transform707.setTranslation([0.0044,1.6209,0.0236])
Shape708 = Shape()
Shape708.setUSE("HAnimJointShape")

Transform707.addChildren(Shape708)

HAnimSegment705.addChildren(Transform707)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyeball_joint'/>
Shape709 = Shape()
LineSet710 = LineSet()
LineSet710.setVertexCount([2])
Coordinate711 = Coordinate()
Coordinate711.setPoint([0.0044,1.6209,0.0236,0.0336,1.6332,0.0502])

LineSet710.setCoord(Coordinate711)
ColorRGBA712 = ColorRGBA()
ColorRGBA712.setUSE("HAnimSegmentLineColorRGBA")

LineSet710.setColor(ColorRGBA712)

Shape709.setGeometry(LineSet710)

HAnimSegment705.addChildren(Shape709)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyelid_joint'/>
Shape713 = Shape()
LineSet714 = LineSet()
LineSet714.setVertexCount([2])
Coordinate715 = Coordinate()
Coordinate715.setPoint([0.0044,1.6209,0.0236,0.0336,1.6332,0.0502])

LineSet714.setCoord(Coordinate715)
ColorRGBA716 = ColorRGBA()
ColorRGBA716.setUSE("HAnimSegmentLineColorRGBA")

LineSet714.setColor(ColorRGBA716)

Shape713.setGeometry(LineSet714)

HAnimSegment705.addChildren(Shape713)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyebrow_joint'/>
Shape717 = Shape()
LineSet718 = LineSet()
LineSet718.setVertexCount([2])
Coordinate719 = Coordinate()
Coordinate719.setPoint([0.0044,1.6209,0.0236,0.0336,1.635,0.0506])

LineSet718.setCoord(Coordinate719)
ColorRGBA720 = ColorRGBA()
ColorRGBA720.setUSE("HAnimSegmentLineColorRGBA")

LineSet718.setColor(ColorRGBA720)

Shape717.setGeometry(LineSet718)

HAnimSegment705.addChildren(Shape717)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyeball_joint'/>
Shape721 = Shape()
LineSet722 = LineSet()
LineSet722.setVertexCount([2])
Coordinate723 = Coordinate()
Coordinate723.setPoint([0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502])

LineSet722.setCoord(Coordinate723)
ColorRGBA724 = ColorRGBA()
ColorRGBA724.setUSE("HAnimSegmentLineColorRGBA")

LineSet722.setColor(ColorRGBA724)

Shape721.setGeometry(LineSet722)

HAnimSegment705.addChildren(Shape721)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyelid_joint'/>
Shape725 = Shape()
LineSet726 = LineSet()
LineSet726.setVertexCount([2])
Coordinate727 = Coordinate()
Coordinate727.setPoint([0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502])

LineSet726.setCoord(Coordinate727)
ColorRGBA728 = ColorRGBA()
ColorRGBA728.setUSE("HAnimSegmentLineColorRGBA")

LineSet726.setColor(ColorRGBA728)

Shape725.setGeometry(LineSet726)

HAnimSegment705.addChildren(Shape725)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyebrow_joint'/>
Shape729 = Shape()
LineSet730 = LineSet()
LineSet730.setVertexCount([2])
Coordinate731 = Coordinate()
Coordinate731.setPoint([0.0044,1.6209,0.0236,-0.0336,1.635,0.0506])

LineSet730.setCoord(Coordinate731)
ColorRGBA732 = ColorRGBA()
ColorRGBA732.setUSE("HAnimSegmentLineColorRGBA")

LineSet730.setColor(ColorRGBA732)

Shape729.setGeometry(LineSet730)

HAnimSegment705.addChildren(Shape729)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='temporomandibular'/>
Shape733 = Shape()
LineSet734 = LineSet()
LineSet734.setVertexCount([2])
Coordinate735 = Coordinate()
Coordinate735.setPoint([0.0044,1.6209,0.0236,0,1.63,0.015])

LineSet734.setCoord(Coordinate735)
ColorRGBA736 = ColorRGBA()
ColorRGBA736.setUSE("HAnimSegmentLineColorRGBA")

LineSet734.setColor(ColorRGBA736)

Shape733.setGeometry(LineSet734)

HAnimSegment705.addChildren(Shape733)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='skull_tip'/>
Shape737 = Shape()
LineSet738 = LineSet()
LineSet738.setVertexCount([2])
Coordinate739 = Coordinate()
Coordinate739.setPoint([0.0044,1.6209,0.0236,0.005,1.7504,0.0055])

LineSet738.setCoord(Coordinate739)
ColorRGBA740 = ColorRGBA()
ColorRGBA740.setUSE("HAnimSiteLineColorRGBA")

LineSet738.setColor(ColorRGBA740)

Shape737.setGeometry(LineSet738)

HAnimSegment705.addChildren(Shape737)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='sellion'/>
Shape741 = Shape()
LineSet742 = LineSet()
LineSet742.setVertexCount([2])
Coordinate743 = Coordinate()
Coordinate743.setPoint([0.0044,1.6209,0.0236,0.0058,1.6316,0.0852])

LineSet742.setCoord(Coordinate743)
ColorRGBA744 = ColorRGBA()
ColorRGBA744.setUSE("HAnimSiteLineColorRGBA")

LineSet742.setColor(ColorRGBA744)

Shape741.setGeometry(LineSet742)

HAnimSegment705.addChildren(Shape741)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_infraorbitale'/>
Shape745 = Shape()
LineSet746 = LineSet()
LineSet746.setVertexCount([2])
Coordinate747 = Coordinate()
Coordinate747.setPoint([0.0044,1.6209,0.0236,-0.0237,1.6171,0.0752])

LineSet746.setCoord(Coordinate747)
ColorRGBA748 = ColorRGBA()
ColorRGBA748.setUSE("HAnimSiteLineColorRGBA")

LineSet746.setColor(ColorRGBA748)

Shape745.setGeometry(LineSet746)

HAnimSegment705.addChildren(Shape745)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_infraorbitale'/>
Shape749 = Shape()
LineSet750 = LineSet()
LineSet750.setVertexCount([2])
Coordinate751 = Coordinate()
Coordinate751.setPoint([0.0044,1.6209,0.0236,0.0341,1.6171,0.0752])

LineSet750.setCoord(Coordinate751)
ColorRGBA752 = ColorRGBA()
ColorRGBA752.setUSE("HAnimSiteLineColorRGBA")

LineSet750.setColor(ColorRGBA752)

Shape749.setGeometry(LineSet750)

HAnimSegment705.addChildren(Shape749)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='supramenton'/>
Shape753 = Shape()
LineSet754 = LineSet()
LineSet754.setVertexCount([2])
Coordinate755 = Coordinate()
Coordinate755.setPoint([0.0044,1.6209,0.0236,0.0061,1.541,0.0805])

LineSet754.setCoord(Coordinate755)
ColorRGBA756 = ColorRGBA()
ColorRGBA756.setUSE("HAnimSiteLineColorRGBA")

LineSet754.setColor(ColorRGBA756)

Shape753.setGeometry(LineSet754)

HAnimSegment705.addChildren(Shape753)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_tragion'/>
Shape757 = Shape()
LineSet758 = LineSet()
LineSet758.setVertexCount([2])
Coordinate759 = Coordinate()
Coordinate759.setPoint([0.0044,1.6209,0.0236,-0.0646,1.6347,0.0302])

LineSet758.setCoord(Coordinate759)
ColorRGBA760 = ColorRGBA()
ColorRGBA760.setUSE("HAnimSiteLineColorRGBA")

LineSet758.setColor(ColorRGBA760)

Shape757.setGeometry(LineSet758)

HAnimSegment705.addChildren(Shape757)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_gonion'/>
Shape761 = Shape()
LineSet762 = LineSet()
LineSet762.setVertexCount([2])
Coordinate763 = Coordinate()
Coordinate763.setPoint([0.0044,1.6209,0.0236,-0.052,1.5529,0.0347])

LineSet762.setCoord(Coordinate763)
ColorRGBA764 = ColorRGBA()
ColorRGBA764.setUSE("HAnimSiteLineColorRGBA")

LineSet762.setColor(ColorRGBA764)

Shape761.setGeometry(LineSet762)

HAnimSegment705.addChildren(Shape761)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_tragion'/>
Shape765 = Shape()
LineSet766 = LineSet()
LineSet766.setVertexCount([2])
Coordinate767 = Coordinate()
Coordinate767.setPoint([0.0044,1.6209,0.0236,0.0739,1.6348,0.0282])

LineSet766.setCoord(Coordinate767)
ColorRGBA768 = ColorRGBA()
ColorRGBA768.setUSE("HAnimSiteLineColorRGBA")

LineSet766.setColor(ColorRGBA768)

Shape765.setGeometry(LineSet766)

HAnimSegment705.addChildren(Shape765)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_gonion'/>
Shape769 = Shape()
LineSet770 = LineSet()
LineSet770.setVertexCount([2])
Coordinate771 = Coordinate()
Coordinate771.setPoint([0.0044,1.6209,0.0236,0.0631,1.553,0.033])

LineSet770.setCoord(Coordinate771)
ColorRGBA772 = ColorRGBA()
ColorRGBA772.setUSE("HAnimSiteLineColorRGBA")

LineSet770.setColor(ColorRGBA772)

Shape769.setGeometry(LineSet770)

HAnimSegment705.addChildren(Shape769)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='nuchale'/>
Shape773 = Shape()
LineSet774 = LineSet()
LineSet774.setVertexCount([2])
Coordinate775 = Coordinate()
Coordinate775.setPoint([0.0044,1.6209,0.0236,0.0039,1.5972,-0.0796])

LineSet774.setCoord(Coordinate775)
ColorRGBA776 = ColorRGBA()
ColorRGBA776.setUSE("HAnimSiteLineColorRGBA")

LineSet774.setColor(ColorRGBA776)

Shape773.setGeometry(LineSet774)

HAnimSegment705.addChildren(Shape773)
#TODO move skull_tip x to zero
HAnimSite777 = HAnimSite()
HAnimSite777.setName("skull_tip")
HAnimSite777.setDEF("hanim_skull_tip")
HAnimSite777.setTranslation([0.005,1.7504,0.0055])
#HAnimSite visualization shape
TouchSensor778 = TouchSensor()
TouchSensor778.setDescription("HAnimSite skull_tip")

HAnimSite777.addChildren(TouchSensor778)
Shape779 = Shape()
Shape779.setUSE("HAnimSiteShape")

HAnimSite777.addChildren(Shape779)

HAnimSegment705.addChildren(HAnimSite777)
HAnimSite780 = HAnimSite()
HAnimSite780.setName("sellion_pt")
HAnimSite780.setDEF("hanim_sellion_pt")
HAnimSite780.setTranslation([0.0058,1.6316,0.0852])
#HAnimSite visualization shape
TouchSensor781 = TouchSensor()
TouchSensor781.setDescription("HAnimSite sellion")

HAnimSite780.addChildren(TouchSensor781)
Shape782 = Shape()
Shape782.setUSE("HAnimSiteShape")

HAnimSite780.addChildren(Shape782)

HAnimSegment705.addChildren(HAnimSite780)
HAnimSite783 = HAnimSite()
HAnimSite783.setName("r_infraorbitale_pt")
HAnimSite783.setDEF("hanim_r_infraorbitale_pt")
HAnimSite783.setTranslation([-0.0237,1.6171,0.0752])
#HAnimSite visualization shape
TouchSensor784 = TouchSensor()
TouchSensor784.setDescription("HAnimSite r_infraorbitale")

HAnimSite783.addChildren(TouchSensor784)
Shape785 = Shape()
Shape785.setUSE("HAnimSiteShape")

HAnimSite783.addChildren(Shape785)

HAnimSegment705.addChildren(HAnimSite783)
HAnimSite786 = HAnimSite()
HAnimSite786.setName("l_infraorbitale_pt")
HAnimSite786.setDEF("hanim_l_infraorbitale_pt")
HAnimSite786.setTranslation([0.0341,1.6171,0.0752])
#HAnimSite visualization shape
TouchSensor787 = TouchSensor()
TouchSensor787.setDescription("HAnimSite l_infraorbitale")

HAnimSite786.addChildren(TouchSensor787)
Shape788 = Shape()
Shape788.setUSE("HAnimSiteShape")

HAnimSite786.addChildren(Shape788)

HAnimSegment705.addChildren(HAnimSite786)
HAnimSite789 = HAnimSite()
HAnimSite789.setName("supramenton_pt")
HAnimSite789.setDEF("hanim_supramenton_pt")
HAnimSite789.setTranslation([0.0061,1.541,0.0805])
#HAnimSite visualization shape
TouchSensor790 = TouchSensor()
TouchSensor790.setDescription("HAnimSite supramenton")

HAnimSite789.addChildren(TouchSensor790)
Shape791 = Shape()
Shape791.setUSE("HAnimSiteShape")

HAnimSite789.addChildren(Shape791)

HAnimSegment705.addChildren(HAnimSite789)
HAnimSite792 = HAnimSite()
HAnimSite792.setName("r_tragion_pt")
HAnimSite792.setDEF("hanim_r_tragion_pt")
HAnimSite792.setTranslation([-0.0646,1.6347,0.0302])
#HAnimSite visualization shape
TouchSensor793 = TouchSensor()
TouchSensor793.setDescription("HAnimSite r_tragion")

HAnimSite792.addChildren(TouchSensor793)
Shape794 = Shape()
Shape794.setUSE("HAnimSiteShape")

HAnimSite792.addChildren(Shape794)

HAnimSegment705.addChildren(HAnimSite792)
HAnimSite795 = HAnimSite()
HAnimSite795.setName("r_gonion_pt")
HAnimSite795.setDEF("hanim_r_gonion_pt")
HAnimSite795.setTranslation([-0.052,1.5529,0.0347])
#HAnimSite visualization shape
TouchSensor796 = TouchSensor()
TouchSensor796.setDescription("HAnimSite r_gonion")

HAnimSite795.addChildren(TouchSensor796)
Shape797 = Shape()
Shape797.setUSE("HAnimSiteShape")

HAnimSite795.addChildren(Shape797)

HAnimSegment705.addChildren(HAnimSite795)
HAnimSite798 = HAnimSite()
HAnimSite798.setName("l_tragion_pt")
HAnimSite798.setDEF("hanim_l_tragion_pt")
HAnimSite798.setTranslation([0.0739,1.6348,0.0282])
#HAnimSite visualization shape
TouchSensor799 = TouchSensor()
TouchSensor799.setDescription("HAnimSite l_tragion")

HAnimSite798.addChildren(TouchSensor799)
Shape800 = Shape()
Shape800.setUSE("HAnimSiteShape")

HAnimSite798.addChildren(Shape800)

HAnimSegment705.addChildren(HAnimSite798)
HAnimSite801 = HAnimSite()
HAnimSite801.setName("l_gonion_pt")
HAnimSite801.setDEF("hanim_l_gonion_pt")
HAnimSite801.setTranslation([0.0631,1.553,0.033])
#HAnimSite visualization shape
TouchSensor802 = TouchSensor()
TouchSensor802.setDescription("HAnimSite l_gonion")

HAnimSite801.addChildren(TouchSensor802)
Shape803 = Shape()
Shape803.setUSE("HAnimSiteShape")

HAnimSite801.addChildren(Shape803)

HAnimSegment705.addChildren(HAnimSite801)
HAnimSite804 = HAnimSite()
HAnimSite804.setName("nuchale_pt")
HAnimSite804.setDEF("hanim_nuchale_pt")
HAnimSite804.setTranslation([0.0039,1.5972,-0.0796])
#HAnimSite visualization shape
TouchSensor805 = TouchSensor()
TouchSensor805.setDescription("HAnimSite nuchale")

HAnimSite804.addChildren(TouchSensor805)
Shape806 = Shape()
Shape806.setUSE("HAnimSiteShape")

HAnimSite804.addChildren(Shape806)

HAnimSegment705.addChildren(HAnimSite804)

HAnimJoint704.addChildren(HAnimSegment705)
HAnimJoint807 = HAnimJoint()
HAnimJoint807.setName("l_eyeball_joint")
HAnimJoint807.setDEF("hanim_l_eyeball_joint")
HAnimJoint807.setCenter([0.0336,1.6332,0.0502])
HAnimJoint807.setStiffness([0,0,0])
HAnimSegment808 = HAnimSegment()
HAnimSegment808.setName("l_eyeball")
HAnimSegment808.setDEF("hanim_l_eyeball")
#<HAnimJoint name='l_eyeball_joint'/> visualization sphere within <HAnimSegment name='l_eyeball'/>
TouchSensor809 = TouchSensor()
TouchSensor809.setDescription("HAnimJoint l_eyeball_joint, HAnimSegment l_eyeball")

HAnimSegment808.addChildren(TouchSensor809)
Transform810 = Transform()
Transform810.setTranslation([0.0336,1.6332,0.0502])
Shape811 = Shape()
Shape811.setUSE("HAnimJointShape")

Transform810.addChildren(Shape811)

HAnimSegment808.addChildren(Transform810)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_eyeball_joint'/> to <HAnimSite name='l_eyeball_site_view'/>
Shape812 = Shape()
LineSet813 = LineSet()
LineSet813.setVertexCount([2])
Coordinate814 = Coordinate()
Coordinate814.setPoint([0.0336,1.6332,0.0502,0.034,1.64,0.05])

LineSet813.setCoord(Coordinate814)
ColorRGBA815 = ColorRGBA()
ColorRGBA815.setDEF("HAnimSiteViewpointLineColorRGBA")
ColorRGBA815.setColor([0,0,1,1,0,0,1,0.1])

LineSet813.setColor(ColorRGBA815)

Shape812.setGeometry(LineSet813)

HAnimSegment808.addChildren(Shape812)
HAnimSite816 = HAnimSite()
HAnimSite816.setName("l_eyeball_site_view")
HAnimSite816.setDEF("hanim_l_eyeball_site_view")
HAnimSite816.setTranslation([0.034,1.64,0.05])
Viewpoint817 = Viewpoint()
Viewpoint817.setDEF("hanim_l_eyeball_site_viewpoint")
Viewpoint817.setDescription("l_eyeball_site_viewpoint looking forward")
Viewpoint817.setOrientation([0,1,0,3.141593])
Viewpoint817.setPosition([0,0,0])

HAnimSite816.addChildren(Viewpoint817)
#HAnimSite/Viewpoint visualization shape
Anchor818 = Anchor()
Anchor818.setDescription("HAnimSite Viewpoint hanim_l_eyeball_site_view")
Anchor818.setUrl(["#hanim_l_eyeball_site_viewpoint"])
LOD819 = LOD()
LOD819.setForceTransitions(True)
LOD819.setRange([0.04])
WorldInfo820 = WorldInfo()
WorldInfo820.setInfo(["hide diamond when close"])

LOD819.addChildren(WorldInfo820)
Shape821 = Shape()
Shape821.setDEF("HAnimSiteViewpointShape")
IndexedFaceSet822 = IndexedFaceSet()
IndexedFaceSet822.setDEF("SiteViewpointDiamondIFS")
IndexedFaceSet822.setCoordIndex([0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1])
IndexedFaceSet822.setCreaseAngle(0.5)
Coordinate823 = Coordinate()
Coordinate823.setPoint([0,0.01,0,-0.01,0,0,0,0,0.01,0.01,0,0,0,0,-0.01,0,-0.01,0])

IndexedFaceSet822.setCoord(Coordinate823)

Shape821.setGeometry(IndexedFaceSet822)
Appearance824 = Appearance()
Material825 = Material()
Material825.setDiffuseColor([0,0,1])
Material825.setTransparency(0.6)

Appearance824.setMaterial(Material825)

Shape821.setAppearance(Appearance824)

LOD819.addChildren(Shape821)

Anchor818.addChildren(LOD819)

HAnimSite816.addChildren(Anchor818)

HAnimSegment808.addChildren(HAnimSite816)

HAnimJoint807.addChildren(HAnimSegment808)

HAnimJoint704.addChildren(HAnimJoint807)
HAnimJoint826 = HAnimJoint()
HAnimJoint826.setName("l_eyelid_joint")
HAnimJoint826.setDEF("hanim_l_eyelid_joint")
HAnimJoint826.setCenter([0.0336,1.6332,0.0502])
HAnimJoint826.setStiffness([0,0,0])
HAnimSegment827 = HAnimSegment()
HAnimSegment827.setName("l_eyelid")
HAnimSegment827.setDEF("hanim_l_eyelid")
#<HAnimJoint name='l_eyelid_joint'/> visualization sphere within <HAnimSegment name='l_eyelid'/>
TouchSensor828 = TouchSensor()
TouchSensor828.setDescription("HAnimJoint l_eyelid_joint, HAnimSegment l_eyelid")

HAnimSegment827.addChildren(TouchSensor828)
Transform829 = Transform()
Transform829.setTranslation([0.0336,1.6332,0.0502])
Shape830 = Shape()
Shape830.setUSE("HAnimJointShape")

Transform829.addChildren(Shape830)

HAnimSegment827.addChildren(Transform829)

HAnimJoint826.addChildren(HAnimSegment827)

HAnimJoint704.addChildren(HAnimJoint826)
HAnimJoint831 = HAnimJoint()
HAnimJoint831.setName("l_eyebrow_joint")
HAnimJoint831.setDEF("hanim_l_eyebrow_joint")
HAnimJoint831.setCenter([0.0336,1.635,0.0506])
HAnimJoint831.setStiffness([0,0,0])
HAnimSegment832 = HAnimSegment()
HAnimSegment832.setName("l_eyebrow")
HAnimSegment832.setDEF("hanim_l_eyebrow")
#<HAnimJoint name='l_eyebrow_joint'/> visualization sphere within <HAnimSegment name='l_eyebrow'/>
TouchSensor833 = TouchSensor()
TouchSensor833.setDescription("HAnimJoint l_eyebrow_joint, HAnimSegment l_eyebrow")

HAnimSegment832.addChildren(TouchSensor833)
Transform834 = Transform()
Transform834.setTranslation([0.0336,1.635,0.0506])
Shape835 = Shape()
Shape835.setUSE("HAnimJointShape")

Transform834.addChildren(Shape835)

HAnimSegment832.addChildren(Transform834)

HAnimJoint831.addChildren(HAnimSegment832)

HAnimJoint704.addChildren(HAnimJoint831)
HAnimJoint836 = HAnimJoint()
HAnimJoint836.setName("r_eyeball_joint")
HAnimJoint836.setDEF("hanim_r_eyeball_joint")
HAnimJoint836.setCenter([-0.0336,1.6332,0.0502])
HAnimJoint836.setStiffness([0,0,0])
HAnimSegment837 = HAnimSegment()
HAnimSegment837.setName("r_eyeball")
HAnimSegment837.setDEF("hanim_r_eyeball")
#<HAnimJoint name='r_eyeball_joint'/> visualization sphere within <HAnimSegment name='r_eyeball'/>
TouchSensor838 = TouchSensor()
TouchSensor838.setDescription("HAnimJoint r_eyeball_joint, HAnimSegment r_eyeball")

HAnimSegment837.addChildren(TouchSensor838)
Transform839 = Transform()
Transform839.setTranslation([-0.0336,1.6332,0.0502])
Shape840 = Shape()
Shape840.setUSE("HAnimJointShape")

Transform839.addChildren(Shape840)

HAnimSegment837.addChildren(Transform839)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_eyeball_joint'/> to <HAnimSite name='r_eyeball_site_view'/>
Shape841 = Shape()
LineSet842 = LineSet()
LineSet842.setVertexCount([2])
Coordinate843 = Coordinate()
Coordinate843.setPoint([-0.0336,1.6332,0.0502,-0.034,1.64,0.05])

LineSet842.setCoord(Coordinate843)
ColorRGBA844 = ColorRGBA()
ColorRGBA844.setUSE("HAnimSiteViewpointLineColorRGBA")

LineSet842.setColor(ColorRGBA844)

Shape841.setGeometry(LineSet842)

HAnimSegment837.addChildren(Shape841)
HAnimSite845 = HAnimSite()
HAnimSite845.setName("r_eyeball_site_view")
HAnimSite845.setDEF("hanim_r_eyeball_site_view")
HAnimSite845.setTranslation([-0.034,1.64,0.05])
Viewpoint846 = Viewpoint()
Viewpoint846.setDEF("hanim_r_eyeball_site_viewpoint")
Viewpoint846.setDescription("r_eyeball_site_viewpoint looking forward")
Viewpoint846.setOrientation([0,1,0,3.141593])
Viewpoint846.setPosition([0,0,0])

HAnimSite845.addChildren(Viewpoint846)
#HAnimSite/Viewpoint visualization shape
Anchor847 = Anchor()
Anchor847.setDescription("HAnimSite Viewpoint hanim_r_eyeball_site_view")
Anchor847.setUrl(["#hanim_r_eyeball_site_viewpoint"])
LOD848 = LOD()
LOD848.setForceTransitions(True)
LOD848.setRange([0.04])
WorldInfo849 = WorldInfo()
WorldInfo849.setInfo(["hide diamond when close"])

LOD848.addChildren(WorldInfo849)
Shape850 = Shape()
Shape850.setUSE("HAnimSiteViewpointShape")

LOD848.addChildren(Shape850)

Anchor847.addChildren(LOD848)

HAnimSite845.addChildren(Anchor847)

HAnimSegment837.addChildren(HAnimSite845)

HAnimJoint836.addChildren(HAnimSegment837)

HAnimJoint704.addChildren(HAnimJoint836)
HAnimJoint851 = HAnimJoint()
HAnimJoint851.setName("r_eyelid_joint")
HAnimJoint851.setDEF("hanim_r_eyelid_joint")
HAnimJoint851.setCenter([-0.0336,1.6332,0.0502])
HAnimJoint851.setStiffness([0,0,0])
HAnimSegment852 = HAnimSegment()
HAnimSegment852.setName("r_eyelid")
HAnimSegment852.setDEF("hanim_r_eyelid")
#<HAnimJoint name='r_eyelid_joint'/> visualization sphere within <HAnimSegment name='r_eyelid'/>
TouchSensor853 = TouchSensor()
TouchSensor853.setDescription("HAnimJoint r_eyelid_joint, HAnimSegment r_eyelid")

HAnimSegment852.addChildren(TouchSensor853)
Transform854 = Transform()
Transform854.setTranslation([-0.0336,1.6332,0.0502])
Shape855 = Shape()
Shape855.setUSE("HAnimJointShape")

Transform854.addChildren(Shape855)

HAnimSegment852.addChildren(Transform854)

HAnimJoint851.addChildren(HAnimSegment852)

HAnimJoint704.addChildren(HAnimJoint851)
HAnimJoint856 = HAnimJoint()
HAnimJoint856.setName("r_eyebrow_joint")
HAnimJoint856.setDEF("hanim_r_eyebrow_joint")
HAnimJoint856.setCenter([-0.0336,1.635,0.0506])
HAnimJoint856.setStiffness([0,0,0])
HAnimSegment857 = HAnimSegment()
HAnimSegment857.setName("r_eyebrow")
HAnimSegment857.setDEF("hanim_r_eyebrow")
#<HAnimJoint name='r_eyebrow_joint'/> visualization sphere within <HAnimSegment name='r_eyebrow'/>
TouchSensor858 = TouchSensor()
TouchSensor858.setDescription("HAnimJoint r_eyebrow_joint, HAnimSegment r_eyebrow")

HAnimSegment857.addChildren(TouchSensor858)
Transform859 = Transform()
Transform859.setTranslation([-0.0336,1.635,0.0506])
Shape860 = Shape()
Shape860.setUSE("HAnimJointShape")

Transform859.addChildren(Shape860)

HAnimSegment857.addChildren(Transform859)

HAnimJoint856.addChildren(HAnimSegment857)

HAnimJoint704.addChildren(HAnimJoint856)
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimJoint861 = HAnimJoint()
HAnimJoint861.setName("temporomandibular")
HAnimJoint861.setDEF("hanim_temporomandibular")
HAnimJoint861.setCenter([0,1.63,0.015])
HAnimJoint861.setStiffness([0,0,0])
HAnimSegment862 = HAnimSegment()
HAnimSegment862.setName("jaw")
HAnimSegment862.setDEF("hanim_jaw")
#<HAnimJoint name='temporomandibular'/> visualization sphere within <HAnimSegment name='jaw'/>
TouchSensor863 = TouchSensor()
TouchSensor863.setDescription("HAnimJoint temporomandibular, HAnimSegment jaw")

HAnimSegment862.addChildren(TouchSensor863)
Transform864 = Transform()
Transform864.setTranslation([0,1.63,0.015])
Shape865 = Shape()
Shape865.setUSE("HAnimJointShape")

Transform864.addChildren(Shape865)

HAnimSegment862.addChildren(Transform864)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_l_site'/>
Shape866 = Shape()
LineSet867 = LineSet()
LineSet867.setVertexCount([2])
Coordinate868 = Coordinate()
Coordinate868.setPoint([0,1.63,0.015,0.045,1.63,0])

LineSet867.setCoord(Coordinate868)
ColorRGBA869 = ColorRGBA()
ColorRGBA869.setUSE("HAnimSiteLineColorRGBA")

LineSet867.setColor(ColorRGBA869)

Shape866.setGeometry(LineSet867)

HAnimSegment862.addChildren(Shape866)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_r_site'/>
Shape870 = Shape()
LineSet871 = LineSet()
LineSet871.setVertexCount([2])
Coordinate872 = Coordinate()
Coordinate872.setPoint([0,1.63,0.015,-0.045,1.63,0])

LineSet871.setCoord(Coordinate872)
ColorRGBA873 = ColorRGBA()
ColorRGBA873.setUSE("HAnimSiteLineColorRGBA")

LineSet871.setColor(ColorRGBA873)

Shape870.setGeometry(LineSet871)

HAnimSegment862.addChildren(Shape870)
HAnimSite874 = HAnimSite()
HAnimSite874.setName("temporomandibular_l_site_pt")
HAnimSite874.setDEF("hanim_temporomandibular_l_site_pt")
HAnimSite874.setTranslation([0.045,1.63,0])
#HAnimSite visualization shape
TouchSensor875 = TouchSensor()
TouchSensor875.setDescription("HAnimSite temporomandibular_l_site")

HAnimSite874.addChildren(TouchSensor875)
Shape876 = Shape()
Shape876.setUSE("HAnimSiteShape")

HAnimSite874.addChildren(Shape876)

HAnimSegment862.addChildren(HAnimSite874)
HAnimSite877 = HAnimSite()
HAnimSite877.setName("temporomandibular_r_site_pt")
HAnimSite877.setDEF("hanim_temporomandibular_r_site_pt")
HAnimSite877.setTranslation([-0.045,1.63,0])
#HAnimSite visualization shape
TouchSensor878 = TouchSensor()
TouchSensor878.setDescription("HAnimSite temporomandibular_r_site")

HAnimSite877.addChildren(TouchSensor878)
Shape879 = Shape()
Shape879.setUSE("HAnimSiteShape")

HAnimSite877.addChildren(Shape879)

HAnimSegment862.addChildren(HAnimSite877)

HAnimJoint861.addChildren(HAnimSegment862)

HAnimJoint704.addChildren(HAnimJoint861)

HAnimJoint695.addChildren(HAnimJoint704)

HAnimJoint686.addChildren(HAnimJoint695)

HAnimJoint677.addChildren(HAnimJoint686)

HAnimJoint668.addChildren(HAnimJoint677)

HAnimJoint659.addChildren(HAnimJoint668)

HAnimJoint650.addChildren(HAnimJoint659)

HAnimJoint627.addChildren(HAnimJoint650)

HAnimJoint596.addChildren(HAnimJoint627)
HAnimJoint880 = HAnimJoint()
HAnimJoint880.setName("l_sternoclavicular")
HAnimJoint880.setDEF("hanim_l_sternoclavicular")
HAnimJoint880.setCenter([0.082,1.4488,-0.0353])
HAnimJoint880.setStiffness([0,0,0])
HAnimSegment881 = HAnimSegment()
HAnimSegment881.setName("l_clavicle")
HAnimSegment881.setDEF("hanim_l_clavicle")
#<HAnimJoint name='l_sternoclavicular'/> visualization sphere within <HAnimSegment name='l_clavicle'/>
TouchSensor882 = TouchSensor()
TouchSensor882.setDescription("HAnimJoint l_sternoclavicular, HAnimSegment l_clavicle")

HAnimSegment881.addChildren(TouchSensor882)
Transform883 = Transform()
Transform883.setTranslation([0.082,1.4488,-0.0353])
Shape884 = Shape()
Shape884.setUSE("HAnimJointShape")

Transform883.addChildren(Shape884)

HAnimSegment881.addChildren(Transform883)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_sternoclavicular'/> to <HAnimJoint name='l_acromioclavicular'/>
Shape885 = Shape()
LineSet886 = LineSet()
LineSet886.setVertexCount([2])
Coordinate887 = Coordinate()
Coordinate887.setPoint([0.082,1.4488,-0.0353,0.0962,1.4269,-0.0424])

LineSet886.setCoord(Coordinate887)
ColorRGBA888 = ColorRGBA()
ColorRGBA888.setUSE("HAnimSegmentLineColorRGBA")

LineSet886.setColor(ColorRGBA888)

Shape885.setGeometry(LineSet886)

HAnimSegment881.addChildren(Shape885)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_clavicale'/>
Shape889 = Shape()
LineSet890 = LineSet()
LineSet890.setVertexCount([2])
Coordinate891 = Coordinate()
Coordinate891.setPoint([0.082,1.4488,-0.0353,0.0271,1.4943,0.0394])

LineSet890.setCoord(Coordinate891)
ColorRGBA892 = ColorRGBA()
ColorRGBA892.setUSE("HAnimSiteLineColorRGBA")

LineSet890.setColor(ColorRGBA892)

Shape889.setGeometry(LineSet890)

HAnimSegment881.addChildren(Shape889)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_acromion'/>
Shape893 = Shape()
LineSet894 = LineSet()
LineSet894.setVertexCount([2])
Coordinate895 = Coordinate()
Coordinate895.setPoint([0.082,1.4488,-0.0353,0.2032,1.476,-0.049])

LineSet894.setCoord(Coordinate895)
ColorRGBA896 = ColorRGBA()
ColorRGBA896.setUSE("HAnimSiteLineColorRGBA")

LineSet894.setColor(ColorRGBA896)

Shape893.setGeometry(LineSet894)

HAnimSegment881.addChildren(Shape893)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_ant'/>
Shape897 = Shape()
LineSet898 = LineSet()
LineSet898.setVertexCount([2])
Coordinate899 = Coordinate()
Coordinate899.setPoint([0.082,1.4488,-0.0353,0.1777,1.4065,-0.0075])

LineSet898.setCoord(Coordinate899)
ColorRGBA900 = ColorRGBA()
ColorRGBA900.setUSE("HAnimSiteLineColorRGBA")

LineSet898.setColor(ColorRGBA900)

Shape897.setGeometry(LineSet898)

HAnimSegment881.addChildren(Shape897)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_post'/>
Shape901 = Shape()
LineSet902 = LineSet()
LineSet902.setVertexCount([2])
Coordinate903 = Coordinate()
Coordinate903.setPoint([0.082,1.4488,-0.0353,0.1706,1.4072,-0.0875])

LineSet902.setCoord(Coordinate903)
ColorRGBA904 = ColorRGBA()
ColorRGBA904.setUSE("HAnimSiteLineColorRGBA")

LineSet902.setColor(ColorRGBA904)

Shape901.setGeometry(LineSet902)

HAnimSegment881.addChildren(Shape901)
HAnimSite905 = HAnimSite()
HAnimSite905.setName("l_clavicale_pt")
HAnimSite905.setDEF("hanim_l_clavicale_pt")
HAnimSite905.setTranslation([0.0271,1.4943,0.0394])
#HAnimSite visualization shape
TouchSensor906 = TouchSensor()
TouchSensor906.setDescription("HAnimSite l_clavicale")

HAnimSite905.addChildren(TouchSensor906)
Shape907 = Shape()
Shape907.setUSE("HAnimSiteShape")

HAnimSite905.addChildren(Shape907)

HAnimSegment881.addChildren(HAnimSite905)
HAnimSite908 = HAnimSite()
HAnimSite908.setName("l_acromion_pt")
HAnimSite908.setDEF("hanim_l_acromion_pt")
HAnimSite908.setTranslation([0.2032,1.476,-0.049])
#HAnimSite visualization shape
TouchSensor909 = TouchSensor()
TouchSensor909.setDescription("HAnimSite l_acromion")

HAnimSite908.addChildren(TouchSensor909)
Shape910 = Shape()
Shape910.setUSE("HAnimSiteShape")

HAnimSite908.addChildren(Shape910)

HAnimSegment881.addChildren(HAnimSite908)
HAnimSite911 = HAnimSite()
HAnimSite911.setName("l_axilla_ant_pt")
HAnimSite911.setDEF("hanim_l_axilla_ant_pt")
HAnimSite911.setTranslation([0.1777,1.4065,-0.0075])
#HAnimSite visualization shape
TouchSensor912 = TouchSensor()
TouchSensor912.setDescription("HAnimSite l_axilla_ant")

HAnimSite911.addChildren(TouchSensor912)
Shape913 = Shape()
Shape913.setUSE("HAnimSiteShape")

HAnimSite911.addChildren(Shape913)

HAnimSegment881.addChildren(HAnimSite911)
HAnimSite914 = HAnimSite()
HAnimSite914.setName("l_axilla_post_pt")
HAnimSite914.setDEF("hanim_l_axilla_post_pt")
HAnimSite914.setTranslation([0.1706,1.4072,-0.0875])
#HAnimSite visualization shape
TouchSensor915 = TouchSensor()
TouchSensor915.setDescription("HAnimSite l_axilla_post")

HAnimSite914.addChildren(TouchSensor915)
Shape916 = Shape()
Shape916.setUSE("HAnimSiteShape")

HAnimSite914.addChildren(Shape916)

HAnimSegment881.addChildren(HAnimSite914)

HAnimJoint880.addChildren(HAnimSegment881)
HAnimJoint917 = HAnimJoint()
HAnimJoint917.setName("l_acromioclavicular")
HAnimJoint917.setDEF("hanim_l_acromioclavicular")
HAnimJoint917.setCenter([0.0962,1.4269,-0.0424])
HAnimJoint917.setStiffness([0,0,0])
HAnimSegment918 = HAnimSegment()
HAnimSegment918.setName("l_scapula")
HAnimSegment918.setDEF("hanim_l_scapula")
#<HAnimJoint name='l_acromioclavicular'/> visualization sphere within <HAnimSegment name='l_scapula'/>
TouchSensor919 = TouchSensor()
TouchSensor919.setDescription("HAnimJoint l_acromioclavicular, HAnimSegment l_scapula")

HAnimSegment918.addChildren(TouchSensor919)
Transform920 = Transform()
Transform920.setTranslation([0.0962,1.4269,-0.0424])
Shape921 = Shape()
Shape921.setUSE("HAnimJointShape")

Transform920.addChildren(Shape921)

HAnimSegment918.addChildren(Transform920)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_acromioclavicular'/> to <HAnimJoint name='l_shoulder'/>
Shape922 = Shape()
LineSet923 = LineSet()
LineSet923.setVertexCount([2])
Coordinate924 = Coordinate()
Coordinate924.setPoint([0.0962,1.4269,-0.0424,0.2029,1.4376,-0.0387])

LineSet923.setCoord(Coordinate924)
ColorRGBA925 = ColorRGBA()
ColorRGBA925.setUSE("HAnimSegmentLineColorRGBA")

LineSet923.setColor(ColorRGBA925)

Shape922.setGeometry(LineSet923)

HAnimSegment918.addChildren(Shape922)

HAnimJoint917.addChildren(HAnimSegment918)
HAnimJoint926 = HAnimJoint()
HAnimJoint926.setName("l_shoulder")
HAnimJoint926.setDEF("hanim_l_shoulder")
HAnimJoint926.setCenter([0.2029,1.4376,-0.0387])
HAnimJoint926.setStiffness([0,0,0])
HAnimSegment927 = HAnimSegment()
HAnimSegment927.setName("l_upperarm")
HAnimSegment927.setDEF("hanim_l_upperarm")
#<HAnimJoint name='l_shoulder'/> visualization sphere within <HAnimSegment name='l_upperarm'/>
TouchSensor928 = TouchSensor()
TouchSensor928.setDescription("HAnimJoint l_shoulder, HAnimSegment l_upperarm")

HAnimSegment927.addChildren(TouchSensor928)
Transform929 = Transform()
Transform929.setTranslation([0.2029,1.4376,-0.0387])
Shape930 = Shape()
Shape930.setUSE("HAnimJointShape")

Transform929.addChildren(Shape930)

HAnimSegment927.addChildren(Transform929)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_shoulder'/> to <HAnimJoint name='l_elbow'/>
Shape931 = Shape()
LineSet932 = LineSet()
LineSet932.setVertexCount([2])
Coordinate933 = Coordinate()
Coordinate933.setPoint([0.2029,1.4376,-0.0387,0.2014,1.1357,-0.0682])

LineSet932.setCoord(Coordinate933)
ColorRGBA934 = ColorRGBA()
ColorRGBA934.setUSE("HAnimSegmentLineColorRGBA")

LineSet932.setColor(ColorRGBA934)

Shape931.setGeometry(LineSet932)

HAnimSegment927.addChildren(Shape931)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_shoulder'/> to <HAnimSite name='l_humeral_lateral_epicn'/>
Shape935 = Shape()
LineSet936 = LineSet()
LineSet936.setVertexCount([2])
Coordinate937 = Coordinate()
Coordinate937.setPoint([0.2029,1.4376,-0.0387,0.228,1.1482,-0.11])

LineSet936.setCoord(Coordinate937)
ColorRGBA938 = ColorRGBA()
ColorRGBA938.setUSE("HAnimSiteLineColorRGBA")

LineSet936.setColor(ColorRGBA938)

Shape935.setGeometry(LineSet936)

HAnimSegment927.addChildren(Shape935)
HAnimSite939 = HAnimSite()
HAnimSite939.setName("l_humeral_lateral_epicn_pt")
HAnimSite939.setDEF("hanim_l_humeral_lateral_epicn_pt")
HAnimSite939.setTranslation([0.228,1.1482,-0.11])
#HAnimSite visualization shape
TouchSensor940 = TouchSensor()
TouchSensor940.setDescription("HAnimSite l_humeral_lateral_epicn")

HAnimSite939.addChildren(TouchSensor940)
Shape941 = Shape()
Shape941.setUSE("HAnimSiteShape")

HAnimSite939.addChildren(Shape941)

HAnimSegment927.addChildren(HAnimSite939)

HAnimJoint926.addChildren(HAnimSegment927)
HAnimJoint942 = HAnimJoint()
HAnimJoint942.setName("l_elbow")
HAnimJoint942.setDEF("hanim_l_elbow")
HAnimJoint942.setCenter([0.2014,1.1357,-0.0682])
HAnimJoint942.setStiffness([0,0,0])
HAnimSegment943 = HAnimSegment()
HAnimSegment943.setName("l_forearm")
HAnimSegment943.setDEF("hanim_l_forearm")
#<HAnimJoint name='l_elbow'/> visualization sphere within <HAnimSegment name='l_forearm'/>
TouchSensor944 = TouchSensor()
TouchSensor944.setDescription("HAnimJoint l_elbow, HAnimSegment l_forearm")

HAnimSegment943.addChildren(TouchSensor944)
Transform945 = Transform()
Transform945.setTranslation([0.2014,1.1357,-0.0682])
Shape946 = Shape()
Shape946.setUSE("HAnimJointShape")

Transform945.addChildren(Shape946)

HAnimSegment943.addChildren(Transform945)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_elbow'/> to <HAnimJoint name='l_wrist'/>
Shape947 = Shape()
LineSet948 = LineSet()
LineSet948.setVertexCount([2])
Coordinate949 = Coordinate()
Coordinate949.setPoint([0.2014,1.1357,-0.0682,0.1984,0.8663,-0.0583])

LineSet948.setCoord(Coordinate949)
ColorRGBA950 = ColorRGBA()
ColorRGBA950.setUSE("HAnimSegmentLineColorRGBA")

LineSet948.setColor(ColorRGBA950)

Shape947.setGeometry(LineSet948)

HAnimSegment943.addChildren(Shape947)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radial_styloid'/>
Shape951 = Shape()
LineSet952 = LineSet()
LineSet952.setVertexCount([2])
Coordinate953 = Coordinate()
Coordinate953.setPoint([0.2014,1.1357,-0.0682,0.1901,0.8645,-0.0415])

LineSet952.setCoord(Coordinate953)
ColorRGBA954 = ColorRGBA()
ColorRGBA954.setUSE("HAnimSiteLineColorRGBA")

LineSet952.setColor(ColorRGBA954)

Shape951.setGeometry(LineSet952)

HAnimSegment943.addChildren(Shape951)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_olecranon'/>
Shape955 = Shape()
LineSet956 = LineSet()
LineSet956.setVertexCount([2])
Coordinate957 = Coordinate()
Coordinate957.setPoint([0.2014,1.1357,-0.0682,0.1962,1.1375,-0.1123])

LineSet956.setCoord(Coordinate957)
ColorRGBA958 = ColorRGBA()
ColorRGBA958.setUSE("HAnimSiteLineColorRGBA")

LineSet956.setColor(ColorRGBA958)

Shape955.setGeometry(LineSet956)

HAnimSegment943.addChildren(Shape955)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_humeral_medial_epicn'/>
Shape959 = Shape()
LineSet960 = LineSet()
LineSet960.setVertexCount([2])
Coordinate961 = Coordinate()
Coordinate961.setPoint([0.2014,1.1357,-0.0682,0.1735,1.1272,-0.1113])

LineSet960.setCoord(Coordinate961)
ColorRGBA962 = ColorRGBA()
ColorRGBA962.setUSE("HAnimSiteLineColorRGBA")

LineSet960.setColor(ColorRGBA962)

Shape959.setGeometry(LineSet960)

HAnimSegment943.addChildren(Shape959)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radiale'/>
Shape963 = Shape()
LineSet964 = LineSet()
LineSet964.setVertexCount([2])
Coordinate965 = Coordinate()
Coordinate965.setPoint([0.2014,1.1357,-0.0682,0.2182,1.1212,-0.1167])

LineSet964.setCoord(Coordinate965)
ColorRGBA966 = ColorRGBA()
ColorRGBA966.setUSE("HAnimSiteLineColorRGBA")

LineSet964.setColor(ColorRGBA966)

Shape963.setGeometry(LineSet964)

HAnimSegment943.addChildren(Shape963)
HAnimSite967 = HAnimSite()
HAnimSite967.setName("l_radial_styloid_pt")
HAnimSite967.setDEF("hanim_l_radial_styloid_pt")
HAnimSite967.setTranslation([0.1901,0.8645,-0.0415])
#HAnimSite visualization shape
TouchSensor968 = TouchSensor()
TouchSensor968.setDescription("HAnimSite l_radial_styloid")

HAnimSite967.addChildren(TouchSensor968)
Shape969 = Shape()
Shape969.setUSE("HAnimSiteShape")

HAnimSite967.addChildren(Shape969)

HAnimSegment943.addChildren(HAnimSite967)
HAnimSite970 = HAnimSite()
HAnimSite970.setName("l_olecranon_pt")
HAnimSite970.setDEF("hanim_l_olecranon_pt")
HAnimSite970.setTranslation([0.1962,1.1375,-0.1123])
#HAnimSite visualization shape
TouchSensor971 = TouchSensor()
TouchSensor971.setDescription("HAnimSite l_olecranon")

HAnimSite970.addChildren(TouchSensor971)
Shape972 = Shape()
Shape972.setUSE("HAnimSiteShape")

HAnimSite970.addChildren(Shape972)

HAnimSegment943.addChildren(HAnimSite970)
HAnimSite973 = HAnimSite()
HAnimSite973.setName("l_humeral_medial_epicn_pt")
HAnimSite973.setDEF("hanim_l_humeral_medial_epicn_pt")
HAnimSite973.setTranslation([0.1735,1.1272,-0.1113])
#HAnimSite visualization shape
TouchSensor974 = TouchSensor()
TouchSensor974.setDescription("HAnimSite l_humeral_medial_epicn")

HAnimSite973.addChildren(TouchSensor974)
Shape975 = Shape()
Shape975.setUSE("HAnimSiteShape")

HAnimSite973.addChildren(Shape975)

HAnimSegment943.addChildren(HAnimSite973)
HAnimSite976 = HAnimSite()
HAnimSite976.setName("l_radiale_pt")
HAnimSite976.setDEF("hanim_l_radiale_pt")
HAnimSite976.setTranslation([0.2182,1.1212,-0.1167])
#HAnimSite visualization shape
TouchSensor977 = TouchSensor()
TouchSensor977.setDescription("HAnimSite l_radiale")

HAnimSite976.addChildren(TouchSensor977)
Shape978 = Shape()
Shape978.setUSE("HAnimSiteShape")

HAnimSite976.addChildren(Shape978)

HAnimSegment943.addChildren(HAnimSite976)

HAnimJoint942.addChildren(HAnimSegment943)
HAnimJoint979 = HAnimJoint()
HAnimJoint979.setName("l_wrist")
HAnimJoint979.setDEF("hanim_l_wrist")
HAnimJoint979.setCenter([0.1984,0.8663,-0.0583])
HAnimJoint979.setStiffness([0,0,0])
HAnimSegment980 = HAnimSegment()
HAnimSegment980.setName("l_hand")
HAnimSegment980.setDEF("hanim_l_hand")
#<HAnimJoint name='l_wrist'/> visualization sphere within <HAnimSegment name='l_hand'/>
TouchSensor981 = TouchSensor()
TouchSensor981.setDescription("HAnimJoint l_wrist, HAnimSegment l_hand")

HAnimSegment980.addChildren(TouchSensor981)
Transform982 = Transform()
Transform982.setTranslation([0.1984,0.8663,-0.0583])
Shape983 = Shape()
Shape983.setUSE("HAnimJointShape")

Transform982.addChildren(Shape983)

HAnimSegment980.addChildren(Transform982)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_thumb1'/>
Shape984 = Shape()
LineSet985 = LineSet()
LineSet985.setVertexCount([2])
Coordinate986 = Coordinate()
Coordinate986.setPoint([0.1984,0.8663,-0.0583,0.1924,0.8472,-0.0534])

LineSet985.setCoord(Coordinate986)
ColorRGBA987 = ColorRGBA()
ColorRGBA987.setUSE("HAnimSegmentLineColorRGBA")

LineSet985.setColor(ColorRGBA987)

Shape984.setGeometry(LineSet985)

HAnimSegment980.addChildren(Shape984)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_index0'/>
Shape988 = Shape()
LineSet989 = LineSet()
LineSet989.setVertexCount([2])
Coordinate990 = Coordinate()
Coordinate990.setPoint([0.1984,0.8663,-0.0583,0.1983,0.8024,-0.028])

LineSet989.setCoord(Coordinate990)
ColorRGBA991 = ColorRGBA()
ColorRGBA991.setUSE("HAnimSegmentLineColorRGBA")

LineSet989.setColor(ColorRGBA991)

Shape988.setGeometry(LineSet989)

HAnimSegment980.addChildren(Shape988)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_middle0'/>
Shape992 = Shape()
LineSet993 = LineSet()
LineSet993.setVertexCount([2])
Coordinate994 = Coordinate()
Coordinate994.setPoint([0.1984,0.8663,-0.0583,0.1987,0.8029,-0.053])

LineSet993.setCoord(Coordinate994)
ColorRGBA995 = ColorRGBA()
ColorRGBA995.setUSE("HAnimSegmentLineColorRGBA")

LineSet993.setColor(ColorRGBA995)

Shape992.setGeometry(LineSet993)

HAnimSegment980.addChildren(Shape992)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_ring0'/>
Shape996 = Shape()
LineSet997 = LineSet()
LineSet997.setVertexCount([2])
Coordinate998 = Coordinate()
Coordinate998.setPoint([0.1984,0.8663,-0.0583,0.1956,0.8019,-0.0794])

LineSet997.setCoord(Coordinate998)
ColorRGBA999 = ColorRGBA()
ColorRGBA999.setUSE("HAnimSegmentLineColorRGBA")

LineSet997.setColor(ColorRGBA999)

Shape996.setGeometry(LineSet997)

HAnimSegment980.addChildren(Shape996)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_pinky0'/>
Shape1000 = Shape()
LineSet1001 = LineSet()
LineSet1001.setVertexCount([2])
Coordinate1002 = Coordinate()
Coordinate1002.setPoint([0.1984,0.8663,-0.0583,0.1925,0.8066,-0.1036])

LineSet1001.setCoord(Coordinate1002)
ColorRGBA1003 = ColorRGBA()
ColorRGBA1003.setUSE("HAnimSegmentLineColorRGBA")

LineSet1001.setColor(ColorRGBA1003)

Shape1000.setGeometry(LineSet1001)

HAnimSegment980.addChildren(Shape1000)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha2'/>
Shape1004 = Shape()
LineSet1005 = LineSet()
LineSet1005.setVertexCount([2])
Coordinate1006 = Coordinate()
Coordinate1006.setPoint([0.1984,0.8663,-0.0583,0.2009,0.8139,-0.0237])

LineSet1005.setCoord(Coordinate1006)
ColorRGBA1007 = ColorRGBA()
ColorRGBA1007.setUSE("HAnimSiteLineColorRGBA")

LineSet1005.setColor(ColorRGBA1007)

Shape1004.setGeometry(LineSet1005)

HAnimSegment980.addChildren(Shape1004)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_ulnar_styloid'/>
Shape1008 = Shape()
LineSet1009 = LineSet()
LineSet1009.setVertexCount([2])
Coordinate1010 = Coordinate()
Coordinate1010.setPoint([0.1984,0.8663,-0.0583,0.2142,0.8529,-0.0648])

LineSet1009.setCoord(Coordinate1010)
ColorRGBA1011 = ColorRGBA()
ColorRGBA1011.setUSE("HAnimSiteLineColorRGBA")

LineSet1009.setColor(ColorRGBA1011)

Shape1008.setGeometry(LineSet1009)

HAnimSegment980.addChildren(Shape1008)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha5'/>
Shape1012 = Shape()
LineSet1013 = LineSet()
LineSet1013.setVertexCount([2])
Coordinate1014 = Coordinate()
Coordinate1014.setPoint([0.1984,0.8663,-0.0583,0.1929,0.786,-0.1122])

LineSet1013.setCoord(Coordinate1014)
ColorRGBA1015 = ColorRGBA()
ColorRGBA1015.setUSE("HAnimSiteLineColorRGBA")

LineSet1013.setColor(ColorRGBA1015)

Shape1012.setGeometry(LineSet1013)

HAnimSegment980.addChildren(Shape1012)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_hand_front_view'/>
Shape1016 = Shape()
LineSet1017 = LineSet()
LineSet1017.setVertexCount([2])
Coordinate1018 = Coordinate()
Coordinate1018.setPoint([0.1984,0.8663,-0.0583,0.3,0.75,0.45])

LineSet1017.setCoord(Coordinate1018)
ColorRGBA1019 = ColorRGBA()
ColorRGBA1019.setUSE("HAnimSiteViewpointLineColorRGBA")

LineSet1017.setColor(ColorRGBA1019)

Shape1016.setGeometry(LineSet1017)

HAnimSegment980.addChildren(Shape1016)
HAnimSite1020 = HAnimSite()
HAnimSite1020.setName("l_metacarpal_pha2_pt")
HAnimSite1020.setDEF("hanim_l_metacarpal_pha2_pt")
HAnimSite1020.setTranslation([0.2009,0.8139,-0.0237])
#HAnimSite visualization shape
TouchSensor1021 = TouchSensor()
TouchSensor1021.setDescription("HAnimSite l_metacarpal_pha2")

HAnimSite1020.addChildren(TouchSensor1021)
Shape1022 = Shape()
Shape1022.setUSE("HAnimSiteShape")

HAnimSite1020.addChildren(Shape1022)

HAnimSegment980.addChildren(HAnimSite1020)
HAnimSite1023 = HAnimSite()
HAnimSite1023.setName("l_ulnar_styloid_pt")
HAnimSite1023.setDEF("hanim_l_ulnar_styloid_pt")
HAnimSite1023.setTranslation([0.2142,0.8529,-0.0648])
#HAnimSite visualization shape
TouchSensor1024 = TouchSensor()
TouchSensor1024.setDescription("HAnimSite l_ulnar_styloid")

HAnimSite1023.addChildren(TouchSensor1024)
Shape1025 = Shape()
Shape1025.setUSE("HAnimSiteShape")

HAnimSite1023.addChildren(Shape1025)

HAnimSegment980.addChildren(HAnimSite1023)
HAnimSite1026 = HAnimSite()
HAnimSite1026.setName("l_metacarpal_pha5_pt")
HAnimSite1026.setDEF("hanim_l_metacarpal_pha5_pt")
HAnimSite1026.setTranslation([0.1929,0.786,-0.1122])
#HAnimSite visualization shape
TouchSensor1027 = TouchSensor()
TouchSensor1027.setDescription("HAnimSite l_metacarpal_pha5")

HAnimSite1026.addChildren(TouchSensor1027)
Shape1028 = Shape()
Shape1028.setUSE("HAnimSiteShape")

HAnimSite1026.addChildren(Shape1028)

HAnimSegment980.addChildren(HAnimSite1026)
HAnimSite1029 = HAnimSite()
HAnimSite1029.setName("l_hand_front_view")
HAnimSite1029.setDEF("hanim_l_hand_front_view")
HAnimSite1029.setTranslation([0.3,0.75,0.45])
Viewpoint1030 = Viewpoint()
Viewpoint1030.setDEF("hanim_l_hand_front_viewpoint")
Viewpoint1030.setCenterOfRotation([0,0.7,0])
Viewpoint1030.setDescription("left hand front")
Viewpoint1030.setPosition([0,0,0])

HAnimSite1029.addChildren(Viewpoint1030)
#HAnimSite/Viewpoint visualization shape
Anchor1031 = Anchor()
Anchor1031.setDescription("HAnimSite Viewpoint hanim_l_hand_front_view")
Anchor1031.setUrl(["#hanim_l_hand_front_viewpoint"])
LOD1032 = LOD()
LOD1032.setForceTransitions(True)
LOD1032.setRange([0.04])
WorldInfo1033 = WorldInfo()
WorldInfo1033.setInfo(["hide diamond when close"])

LOD1032.addChildren(WorldInfo1033)
Shape1034 = Shape()
Shape1034.setUSE("HAnimSiteViewpointShape")

LOD1032.addChildren(Shape1034)

Anchor1031.addChildren(LOD1032)

HAnimSite1029.addChildren(Anchor1031)

HAnimSegment980.addChildren(HAnimSite1029)

HAnimJoint979.addChildren(HAnimSegment980)
HAnimJoint1035 = HAnimJoint()
HAnimJoint1035.setName("l_thumb1")
HAnimJoint1035.setDEF("hanim_l_thumb1")
HAnimJoint1035.setCenter([0.1924,0.8472,-0.0534])
HAnimJoint1035.setStiffness([0,0,0])
HAnimSegment1036 = HAnimSegment()
HAnimSegment1036.setName("l_thumb_metacarpal")
HAnimSegment1036.setDEF("hanim_l_thumb_metacarpal")
#<HAnimJoint name='l_thumb1'/> visualization sphere within <HAnimSegment name='l_thumb_metacarpal'/>
TouchSensor1037 = TouchSensor()
TouchSensor1037.setDescription("HAnimJoint l_thumb1, HAnimSegment l_thumb_metacarpal")

HAnimSegment1036.addChildren(TouchSensor1037)
Transform1038 = Transform()
Transform1038.setTranslation([0.1924,0.8472,-0.0534])
Shape1039 = Shape()
Shape1039.setUSE("HAnimJointShape")

Transform1038.addChildren(Shape1039)

HAnimSegment1036.addChildren(Transform1038)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb1'/> to <HAnimJoint name='l_thumb2'/>
Shape1040 = Shape()
LineSet1041 = LineSet()
LineSet1041.setVertexCount([2])
Coordinate1042 = Coordinate()
Coordinate1042.setPoint([0.1924,0.8472,-0.0534,0.1951,0.8226,0.0246])

LineSet1041.setCoord(Coordinate1042)
ColorRGBA1043 = ColorRGBA()
ColorRGBA1043.setUSE("HAnimSegmentLineColorRGBA")

LineSet1041.setColor(ColorRGBA1043)

Shape1040.setGeometry(LineSet1041)

HAnimSegment1036.addChildren(Shape1040)

HAnimJoint1035.addChildren(HAnimSegment1036)
HAnimJoint1044 = HAnimJoint()
HAnimJoint1044.setName("l_thumb2")
HAnimJoint1044.setDEF("hanim_l_thumb2")
HAnimJoint1044.setCenter([0.1951,0.8226,0.0246])
HAnimJoint1044.setStiffness([0,0,0])
HAnimSegment1045 = HAnimSegment()
HAnimSegment1045.setName("l_thumb_proximal")
HAnimSegment1045.setDEF("hanim_l_thumb_proximal")
#<HAnimJoint name='l_thumb2'/> visualization sphere within <HAnimSegment name='l_thumb_proximal'/>
TouchSensor1046 = TouchSensor()
TouchSensor1046.setDescription("HAnimJoint l_thumb2, HAnimSegment l_thumb_proximal")

HAnimSegment1045.addChildren(TouchSensor1046)
Transform1047 = Transform()
Transform1047.setTranslation([0.1951,0.8226,0.0246])
Shape1048 = Shape()
Shape1048.setUSE("HAnimJointShape")

Transform1047.addChildren(Shape1048)

HAnimSegment1045.addChildren(Transform1047)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb2'/> to <HAnimJoint name='l_thumb3'/>
Shape1049 = Shape()
LineSet1050 = LineSet()
LineSet1050.setVertexCount([2])
Coordinate1051 = Coordinate()
Coordinate1051.setPoint([0.1951,0.8226,0.0246,0.1955,0.8159,0.0464])

LineSet1050.setCoord(Coordinate1051)
ColorRGBA1052 = ColorRGBA()
ColorRGBA1052.setUSE("HAnimSegmentLineColorRGBA")

LineSet1050.setColor(ColorRGBA1052)

Shape1049.setGeometry(LineSet1050)

HAnimSegment1045.addChildren(Shape1049)

HAnimJoint1044.addChildren(HAnimSegment1045)
HAnimJoint1053 = HAnimJoint()
HAnimJoint1053.setName("l_thumb3")
HAnimJoint1053.setDEF("hanim_l_thumb3")
HAnimJoint1053.setCenter([0.1955,0.8159,0.0464])
HAnimJoint1053.setStiffness([0,0,0])
HAnimSegment1054 = HAnimSegment()
HAnimSegment1054.setName("l_thumb_distal")
HAnimSegment1054.setDEF("hanim_l_thumb_distal")
#<HAnimJoint name='l_thumb3'/> visualization sphere within <HAnimSegment name='l_thumb_distal'/>
TouchSensor1055 = TouchSensor()
TouchSensor1055.setDescription("HAnimJoint l_thumb3, HAnimSegment l_thumb_distal")

HAnimSegment1054.addChildren(TouchSensor1055)
Transform1056 = Transform()
Transform1056.setTranslation([0.1955,0.8159,0.0464])
Shape1057 = Shape()
Shape1057.setUSE("HAnimJointShape")

Transform1056.addChildren(Shape1057)

HAnimSegment1054.addChildren(Transform1056)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_thumb3'/> to <HAnimSite name='l_thumb_distal_tip'/>
Shape1058 = Shape()
LineSet1059 = LineSet()
LineSet1059.setVertexCount([2])
Coordinate1060 = Coordinate()
Coordinate1060.setPoint([0.1955,0.8159,0.0464,0.1982,0.8061,0.0759])

LineSet1059.setCoord(Coordinate1060)
ColorRGBA1061 = ColorRGBA()
ColorRGBA1061.setUSE("HAnimSiteLineColorRGBA")

LineSet1059.setColor(ColorRGBA1061)

Shape1058.setGeometry(LineSet1059)

HAnimSegment1054.addChildren(Shape1058)
HAnimSite1062 = HAnimSite()
HAnimSite1062.setName("l_thumb_distal_tip")
HAnimSite1062.setDEF("hanim_l_thumb_distal_tip")
HAnimSite1062.setTranslation([0.1982,0.8061,0.0759])
#HAnimSite visualization shape
TouchSensor1063 = TouchSensor()
TouchSensor1063.setDescription("HAnimSite l_thumb_distal_tip")

HAnimSite1062.addChildren(TouchSensor1063)
Shape1064 = Shape()
Shape1064.setUSE("HAnimSiteShape")

HAnimSite1062.addChildren(Shape1064)

HAnimSegment1054.addChildren(HAnimSite1062)

HAnimJoint1053.addChildren(HAnimSegment1054)

HAnimJoint1044.addChildren(HAnimJoint1053)

HAnimJoint1035.addChildren(HAnimJoint1044)

HAnimJoint979.addChildren(HAnimJoint1035)
HAnimJoint1065 = HAnimJoint()
HAnimJoint1065.setName("l_index0")
HAnimJoint1065.setDEF("hanim_l_index0")
HAnimJoint1065.setCenter([0.1983,0.8024,-0.028])
HAnimJoint1065.setStiffness([0,0,0])
HAnimSegment1066 = HAnimSegment()
HAnimSegment1066.setName("l_index_metacarpal")
HAnimSegment1066.setDEF("hanim_l_index_metacarpal")
#<HAnimJoint name='l_index0'/> visualization sphere within <HAnimSegment name='l_index_metacarpal'/>
TouchSensor1067 = TouchSensor()
TouchSensor1067.setDescription("HAnimJoint l_index0, HAnimSegment l_index_metacarpal")

HAnimSegment1066.addChildren(TouchSensor1067)
Transform1068 = Transform()
Transform1068.setTranslation([0.1983,0.8024,-0.028])
Shape1069 = Shape()
Shape1069.setUSE("HAnimJointShape")

Transform1068.addChildren(Shape1069)

HAnimSegment1066.addChildren(Transform1068)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index0'/> to <HAnimJoint name='l_index1'/>
Shape1070 = Shape()
LineSet1071 = LineSet()
LineSet1071.setVertexCount([2])
Coordinate1072 = Coordinate()
Coordinate1072.setPoint([0.1983,0.8024,-0.028,0.1983,0.7815,-0.028])

LineSet1071.setCoord(Coordinate1072)
ColorRGBA1073 = ColorRGBA()
ColorRGBA1073.setUSE("HAnimSegmentLineColorRGBA")

LineSet1071.setColor(ColorRGBA1073)

Shape1070.setGeometry(LineSet1071)

HAnimSegment1066.addChildren(Shape1070)

HAnimJoint1065.addChildren(HAnimSegment1066)
HAnimJoint1074 = HAnimJoint()
HAnimJoint1074.setName("l_index1")
HAnimJoint1074.setDEF("hanim_l_index1")
HAnimJoint1074.setCenter([0.1983,0.7815,-0.028])
HAnimJoint1074.setStiffness([0,0,0])
HAnimSegment1075 = HAnimSegment()
HAnimSegment1075.setName("l_index_proximal")
HAnimSegment1075.setDEF("hanim_l_index_proximal")
#<HAnimJoint name='l_index1'/> visualization sphere within <HAnimSegment name='l_index_proximal'/>
TouchSensor1076 = TouchSensor()
TouchSensor1076.setDescription("HAnimJoint l_index1, HAnimSegment l_index_proximal")

HAnimSegment1075.addChildren(TouchSensor1076)
Transform1077 = Transform()
Transform1077.setTranslation([0.1983,0.7815,-0.028])
Shape1078 = Shape()
Shape1078.setUSE("HAnimJointShape")

Transform1077.addChildren(Shape1078)

HAnimSegment1075.addChildren(Transform1077)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index1'/> to <HAnimJoint name='l_index2'/>
Shape1079 = Shape()
LineSet1080 = LineSet()
LineSet1080.setVertexCount([2])
Coordinate1081 = Coordinate()
Coordinate1081.setPoint([0.1983,0.7815,-0.028,0.2017,0.7363,-0.0248])

LineSet1080.setCoord(Coordinate1081)
ColorRGBA1082 = ColorRGBA()
ColorRGBA1082.setUSE("HAnimSegmentLineColorRGBA")

LineSet1080.setColor(ColorRGBA1082)

Shape1079.setGeometry(LineSet1080)

HAnimSegment1075.addChildren(Shape1079)

HAnimJoint1074.addChildren(HAnimSegment1075)
HAnimJoint1083 = HAnimJoint()
HAnimJoint1083.setName("l_index2")
HAnimJoint1083.setDEF("hanim_l_index2")
HAnimJoint1083.setCenter([0.2017,0.7363,-0.0248])
HAnimJoint1083.setStiffness([0,0,0])
HAnimSegment1084 = HAnimSegment()
HAnimSegment1084.setName("l_index_middle")
HAnimSegment1084.setDEF("hanim_l_index_middle")
#<HAnimJoint name='l_index2'/> visualization sphere within <HAnimSegment name='l_index_middle'/>
TouchSensor1085 = TouchSensor()
TouchSensor1085.setDescription("HAnimJoint l_index2, HAnimSegment l_index_middle")

HAnimSegment1084.addChildren(TouchSensor1085)
Transform1086 = Transform()
Transform1086.setTranslation([0.2017,0.7363,-0.0248])
Shape1087 = Shape()
Shape1087.setUSE("HAnimJointShape")

Transform1086.addChildren(Shape1087)

HAnimSegment1084.addChildren(Transform1086)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index2'/> to <HAnimJoint name='l_index3'/>
Shape1088 = Shape()
LineSet1089 = LineSet()
LineSet1089.setVertexCount([2])
Coordinate1090 = Coordinate()
Coordinate1090.setPoint([0.2017,0.7363,-0.0248,0.2028,0.7139,-0.0236])

LineSet1089.setCoord(Coordinate1090)
ColorRGBA1091 = ColorRGBA()
ColorRGBA1091.setUSE("HAnimSegmentLineColorRGBA")

LineSet1089.setColor(ColorRGBA1091)

Shape1088.setGeometry(LineSet1089)

HAnimSegment1084.addChildren(Shape1088)

HAnimJoint1083.addChildren(HAnimSegment1084)
HAnimJoint1092 = HAnimJoint()
HAnimJoint1092.setName("l_index3")
HAnimJoint1092.setDEF("hanim_l_index3")
HAnimJoint1092.setCenter([0.2028,0.7139,-0.0236])
HAnimJoint1092.setStiffness([0,0,0])
HAnimSegment1093 = HAnimSegment()
HAnimSegment1093.setName("l_index_distal")
HAnimSegment1093.setDEF("hanim_l_index_distal")
#<HAnimJoint name='l_index3'/> visualization sphere within <HAnimSegment name='l_index_distal'/>
TouchSensor1094 = TouchSensor()
TouchSensor1094.setDescription("HAnimJoint l_index3, HAnimSegment l_index_distal")

HAnimSegment1093.addChildren(TouchSensor1094)
Transform1095 = Transform()
Transform1095.setTranslation([0.2028,0.7139,-0.0236])
Shape1096 = Shape()
Shape1096.setUSE("HAnimJointShape")

Transform1095.addChildren(Shape1096)

HAnimSegment1093.addChildren(Transform1095)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_index_distal_tip'/>
Shape1097 = Shape()
LineSet1098 = LineSet()
LineSet1098.setVertexCount([2])
Coordinate1099 = Coordinate()
Coordinate1099.setPoint([0.2028,0.7139,-0.0236,0.2089,0.6858,-0.0245])

LineSet1098.setCoord(Coordinate1099)
ColorRGBA1100 = ColorRGBA()
ColorRGBA1100.setUSE("HAnimSiteLineColorRGBA")

LineSet1098.setColor(ColorRGBA1100)

Shape1097.setGeometry(LineSet1098)

HAnimSegment1093.addChildren(Shape1097)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_dactylion'/>
Shape1101 = Shape()
LineSet1102 = LineSet()
LineSet1102.setVertexCount([2])
Coordinate1103 = Coordinate()
Coordinate1103.setPoint([0.2028,0.7139,-0.0236,0.2056,0.6743,-0.0482])

LineSet1102.setCoord(Coordinate1103)
ColorRGBA1104 = ColorRGBA()
ColorRGBA1104.setUSE("HAnimSiteLineColorRGBA")

LineSet1102.setColor(ColorRGBA1104)

Shape1101.setGeometry(LineSet1102)

HAnimSegment1093.addChildren(Shape1101)
HAnimSite1105 = HAnimSite()
HAnimSite1105.setName("l_index_distal_tip")
HAnimSite1105.setDEF("hanim_l_index_distal_tip")
HAnimSite1105.setTranslation([0.2089,0.6858,-0.0245])
#HAnimSite visualization shape
TouchSensor1106 = TouchSensor()
TouchSensor1106.setDescription("HAnimSite l_index_distal_tip")

HAnimSite1105.addChildren(TouchSensor1106)
Shape1107 = Shape()
Shape1107.setUSE("HAnimSiteShape")

HAnimSite1105.addChildren(Shape1107)

HAnimSegment1093.addChildren(HAnimSite1105)
HAnimSite1108 = HAnimSite()
HAnimSite1108.setName("l_dactylion_pt")
HAnimSite1108.setDEF("hanim_l_dactylion_pt")
HAnimSite1108.setTranslation([0.2056,0.6743,-0.0482])
#HAnimSite visualization shape
TouchSensor1109 = TouchSensor()
TouchSensor1109.setDescription("HAnimSite l_dactylion")

HAnimSite1108.addChildren(TouchSensor1109)
Shape1110 = Shape()
Shape1110.setUSE("HAnimSiteShape")

HAnimSite1108.addChildren(Shape1110)

HAnimSegment1093.addChildren(HAnimSite1108)

HAnimJoint1092.addChildren(HAnimSegment1093)

HAnimJoint1083.addChildren(HAnimJoint1092)

HAnimJoint1074.addChildren(HAnimJoint1083)

HAnimJoint1065.addChildren(HAnimJoint1074)

HAnimJoint979.addChildren(HAnimJoint1065)
HAnimJoint1111 = HAnimJoint()
HAnimJoint1111.setName("l_middle0")
HAnimJoint1111.setDEF("hanim_l_middle0")
HAnimJoint1111.setCenter([0.1987,0.8029,-0.053])
HAnimJoint1111.setStiffness([0,0,0])
HAnimSegment1112 = HAnimSegment()
HAnimSegment1112.setName("l_middle_metacarpal")
HAnimSegment1112.setDEF("hanim_l_middle_metacarpal")
#<HAnimJoint name='l_middle0'/> visualization sphere within <HAnimSegment name='l_middle_metacarpal'/>
TouchSensor1113 = TouchSensor()
TouchSensor1113.setDescription("HAnimJoint l_middle0, HAnimSegment l_middle_metacarpal")

HAnimSegment1112.addChildren(TouchSensor1113)
Transform1114 = Transform()
Transform1114.setTranslation([0.1987,0.8029,-0.053])
Shape1115 = Shape()
Shape1115.setUSE("HAnimJointShape")

Transform1114.addChildren(Shape1115)

HAnimSegment1112.addChildren(Transform1114)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle0'/> to <HAnimJoint name='l_middle1'/>
Shape1116 = Shape()
LineSet1117 = LineSet()
LineSet1117.setVertexCount([2])
Coordinate1118 = Coordinate()
Coordinate1118.setPoint([0.1987,0.8029,-0.053,0.1987,0.7818,-0.053])

LineSet1117.setCoord(Coordinate1118)
ColorRGBA1119 = ColorRGBA()
ColorRGBA1119.setUSE("HAnimSegmentLineColorRGBA")

LineSet1117.setColor(ColorRGBA1119)

Shape1116.setGeometry(LineSet1117)

HAnimSegment1112.addChildren(Shape1116)

HAnimJoint1111.addChildren(HAnimSegment1112)
HAnimJoint1120 = HAnimJoint()
HAnimJoint1120.setName("l_middle1")
HAnimJoint1120.setDEF("hanim_l_middle1")
HAnimJoint1120.setCenter([0.1987,0.7818,-0.053])
HAnimJoint1120.setStiffness([0,0,0])
HAnimSegment1121 = HAnimSegment()
HAnimSegment1121.setName("l_middle_proximal")
HAnimSegment1121.setDEF("hanim_l_middle_proximal")
#<HAnimJoint name='l_middle1'/> visualization sphere within <HAnimSegment name='l_middle_proximal'/>
TouchSensor1122 = TouchSensor()
TouchSensor1122.setDescription("HAnimJoint l_middle1, HAnimSegment l_middle_proximal")

HAnimSegment1121.addChildren(TouchSensor1122)
Transform1123 = Transform()
Transform1123.setTranslation([0.1987,0.7818,-0.053])
Shape1124 = Shape()
Shape1124.setUSE("HAnimJointShape")

Transform1123.addChildren(Shape1124)

HAnimSegment1121.addChildren(Transform1123)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle1'/> to <HAnimJoint name='l_middle2'/>
Shape1125 = Shape()
LineSet1126 = LineSet()
LineSet1126.setVertexCount([2])
Coordinate1127 = Coordinate()
Coordinate1127.setPoint([0.1987,0.7818,-0.053,0.2013,0.7273,-0.0503])

LineSet1126.setCoord(Coordinate1127)
ColorRGBA1128 = ColorRGBA()
ColorRGBA1128.setUSE("HAnimSegmentLineColorRGBA")

LineSet1126.setColor(ColorRGBA1128)

Shape1125.setGeometry(LineSet1126)

HAnimSegment1121.addChildren(Shape1125)

HAnimJoint1120.addChildren(HAnimSegment1121)
HAnimJoint1129 = HAnimJoint()
HAnimJoint1129.setName("l_middle2")
HAnimJoint1129.setDEF("hanim_l_middle2")
HAnimJoint1129.setCenter([0.2013,0.7273,-0.0503])
HAnimJoint1129.setStiffness([0,0,0])
HAnimSegment1130 = HAnimSegment()
HAnimSegment1130.setName("l_middle_middle")
HAnimSegment1130.setDEF("hanim_l_middle_middle")
#<HAnimJoint name='l_middle2'/> visualization sphere within <HAnimSegment name='l_middle_middle'/>
TouchSensor1131 = TouchSensor()
TouchSensor1131.setDescription("HAnimJoint l_middle2, HAnimSegment l_middle_middle")

HAnimSegment1130.addChildren(TouchSensor1131)
Transform1132 = Transform()
Transform1132.setTranslation([0.2013,0.7273,-0.0503])
Shape1133 = Shape()
Shape1133.setUSE("HAnimJointShape")

Transform1132.addChildren(Shape1133)

HAnimSegment1130.addChildren(Transform1132)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle2'/> to <HAnimJoint name='l_middle3'/>
Shape1134 = Shape()
LineSet1135 = LineSet()
LineSet1135.setVertexCount([2])
Coordinate1136 = Coordinate()
Coordinate1136.setPoint([0.2013,0.7273,-0.0503,0.2026,0.7011,-0.0494])

LineSet1135.setCoord(Coordinate1136)
ColorRGBA1137 = ColorRGBA()
ColorRGBA1137.setUSE("HAnimSegmentLineColorRGBA")

LineSet1135.setColor(ColorRGBA1137)

Shape1134.setGeometry(LineSet1135)

HAnimSegment1130.addChildren(Shape1134)

HAnimJoint1129.addChildren(HAnimSegment1130)
HAnimJoint1138 = HAnimJoint()
HAnimJoint1138.setName("l_middle3")
HAnimJoint1138.setDEF("hanim_l_middle3")
HAnimJoint1138.setCenter([0.2026,0.7011,-0.0494])
HAnimJoint1138.setStiffness([0,0,0])
HAnimSegment1139 = HAnimSegment()
HAnimSegment1139.setName("l_middle_distal")
HAnimSegment1139.setDEF("hanim_l_middle_distal")
#<HAnimJoint name='l_middle3'/> visualization sphere within <HAnimSegment name='l_middle_distal'/>
TouchSensor1140 = TouchSensor()
TouchSensor1140.setDescription("HAnimJoint l_middle3, HAnimSegment l_middle_distal")

HAnimSegment1139.addChildren(TouchSensor1140)
Transform1141 = Transform()
Transform1141.setTranslation([0.2026,0.7011,-0.0494])
Shape1142 = Shape()
Shape1142.setUSE("HAnimJointShape")

Transform1141.addChildren(Shape1142)

HAnimSegment1139.addChildren(Transform1141)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_middle3'/> to <HAnimSite name='l_middle_distal_tip'/>
Shape1143 = Shape()
LineSet1144 = LineSet()
LineSet1144.setVertexCount([2])
Coordinate1145 = Coordinate()
Coordinate1145.setPoint([0.2026,0.7011,-0.0494,0.208,0.6731,-0.0491])

LineSet1144.setCoord(Coordinate1145)
ColorRGBA1146 = ColorRGBA()
ColorRGBA1146.setUSE("HAnimSiteLineColorRGBA")

LineSet1144.setColor(ColorRGBA1146)

Shape1143.setGeometry(LineSet1144)

HAnimSegment1139.addChildren(Shape1143)
HAnimSite1147 = HAnimSite()
HAnimSite1147.setName("l_middle_distal_tip")
HAnimSite1147.setDEF("hanim_l_middle_distal_tip")
HAnimSite1147.setTranslation([0.208,0.6731,-0.0491])
#HAnimSite visualization shape
TouchSensor1148 = TouchSensor()
TouchSensor1148.setDescription("HAnimSite l_middle_distal_tip")

HAnimSite1147.addChildren(TouchSensor1148)
Shape1149 = Shape()
Shape1149.setUSE("HAnimSiteShape")

HAnimSite1147.addChildren(Shape1149)

HAnimSegment1139.addChildren(HAnimSite1147)

HAnimJoint1138.addChildren(HAnimSegment1139)

HAnimJoint1129.addChildren(HAnimJoint1138)

HAnimJoint1120.addChildren(HAnimJoint1129)

HAnimJoint1111.addChildren(HAnimJoint1120)

HAnimJoint979.addChildren(HAnimJoint1111)
HAnimJoint1150 = HAnimJoint()
HAnimJoint1150.setName("l_ring0")
HAnimJoint1150.setDEF("hanim_l_ring0")
HAnimJoint1150.setCenter([0.1956,0.8019,-0.0794])
HAnimJoint1150.setStiffness([0,0,0])
HAnimSegment1151 = HAnimSegment()
HAnimSegment1151.setName("l_ring_metacarpal")
HAnimSegment1151.setDEF("hanim_l_ring_metacarpal")
#<HAnimJoint name='l_ring0'/> visualization sphere within <HAnimSegment name='l_ring_metacarpal'/>
TouchSensor1152 = TouchSensor()
TouchSensor1152.setDescription("HAnimJoint l_ring0, HAnimSegment l_ring_metacarpal")

HAnimSegment1151.addChildren(TouchSensor1152)
Transform1153 = Transform()
Transform1153.setTranslation([0.1956,0.8019,-0.0794])
Shape1154 = Shape()
Shape1154.setUSE("HAnimJointShape")

Transform1153.addChildren(Shape1154)

HAnimSegment1151.addChildren(Transform1153)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring0'/> to <HAnimJoint name='l_ring1'/>
Shape1155 = Shape()
LineSet1156 = LineSet()
LineSet1156.setVertexCount([2])
Coordinate1157 = Coordinate()
Coordinate1157.setPoint([0.1956,0.8019,-0.0794,0.1956,0.7815,-0.0794])

LineSet1156.setCoord(Coordinate1157)
ColorRGBA1158 = ColorRGBA()
ColorRGBA1158.setUSE("HAnimSegmentLineColorRGBA")

LineSet1156.setColor(ColorRGBA1158)

Shape1155.setGeometry(LineSet1156)

HAnimSegment1151.addChildren(Shape1155)

HAnimJoint1150.addChildren(HAnimSegment1151)
HAnimJoint1159 = HAnimJoint()
HAnimJoint1159.setName("l_ring1")
HAnimJoint1159.setDEF("hanim_l_ring1")
HAnimJoint1159.setCenter([0.1956,0.7815,-0.0794])
HAnimJoint1159.setStiffness([0,0,0])
HAnimSegment1160 = HAnimSegment()
HAnimSegment1160.setName("l_ring_proximal")
HAnimSegment1160.setDEF("hanim_l_ring_proximal")
#<HAnimJoint name='l_ring1'/> visualization sphere within <HAnimSegment name='l_ring_proximal'/>
TouchSensor1161 = TouchSensor()
TouchSensor1161.setDescription("HAnimJoint l_ring1, HAnimSegment l_ring_proximal")

HAnimSegment1160.addChildren(TouchSensor1161)
Transform1162 = Transform()
Transform1162.setTranslation([0.1956,0.7815,-0.0794])
Shape1163 = Shape()
Shape1163.setUSE("HAnimJointShape")

Transform1162.addChildren(Shape1163)

HAnimSegment1160.addChildren(Transform1162)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring1'/> to <HAnimJoint name='l_ring2'/>
Shape1164 = Shape()
LineSet1165 = LineSet()
LineSet1165.setVertexCount([2])
Coordinate1166 = Coordinate()
Coordinate1166.setPoint([0.1956,0.7815,-0.0794,0.1973,0.7287,-0.0777])

LineSet1165.setCoord(Coordinate1166)
ColorRGBA1167 = ColorRGBA()
ColorRGBA1167.setUSE("HAnimSegmentLineColorRGBA")

LineSet1165.setColor(ColorRGBA1167)

Shape1164.setGeometry(LineSet1165)

HAnimSegment1160.addChildren(Shape1164)

HAnimJoint1159.addChildren(HAnimSegment1160)
HAnimJoint1168 = HAnimJoint()
HAnimJoint1168.setName("l_ring2")
HAnimJoint1168.setDEF("hanim_l_ring2")
HAnimJoint1168.setCenter([0.1973,0.7287,-0.0777])
HAnimJoint1168.setStiffness([0,0,0])
HAnimSegment1169 = HAnimSegment()
HAnimSegment1169.setName("l_ring_middle")
HAnimSegment1169.setDEF("hanim_l_ring_middle")
#<HAnimJoint name='l_ring2'/> visualization sphere within <HAnimSegment name='l_ring_middle'/>
TouchSensor1170 = TouchSensor()
TouchSensor1170.setDescription("HAnimJoint l_ring2, HAnimSegment l_ring_middle")

HAnimSegment1169.addChildren(TouchSensor1170)
Transform1171 = Transform()
Transform1171.setTranslation([0.1973,0.7287,-0.0777])
Shape1172 = Shape()
Shape1172.setUSE("HAnimJointShape")

Transform1171.addChildren(Shape1172)

HAnimSegment1169.addChildren(Transform1171)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring2'/> to <HAnimJoint name='l_ring3'/>
Shape1173 = Shape()
LineSet1174 = LineSet()
LineSet1174.setVertexCount([2])
Coordinate1175 = Coordinate()
Coordinate1175.setPoint([0.1973,0.7287,-0.0777,0.1983,0.7045,-0.0767])

LineSet1174.setCoord(Coordinate1175)
ColorRGBA1176 = ColorRGBA()
ColorRGBA1176.setUSE("HAnimSegmentLineColorRGBA")

LineSet1174.setColor(ColorRGBA1176)

Shape1173.setGeometry(LineSet1174)

HAnimSegment1169.addChildren(Shape1173)

HAnimJoint1168.addChildren(HAnimSegment1169)
HAnimJoint1177 = HAnimJoint()
HAnimJoint1177.setName("l_ring3")
HAnimJoint1177.setDEF("hanim_l_ring3")
HAnimJoint1177.setCenter([0.1983,0.7045,-0.0767])
HAnimJoint1177.setStiffness([0,0,0])
HAnimSegment1178 = HAnimSegment()
HAnimSegment1178.setName("l_ring_distal")
HAnimSegment1178.setDEF("hanim_l_ring_distal")
#<HAnimJoint name='l_ring3'/> visualization sphere within <HAnimSegment name='l_ring_distal'/>
TouchSensor1179 = TouchSensor()
TouchSensor1179.setDescription("HAnimJoint l_ring3, HAnimSegment l_ring_distal")

HAnimSegment1178.addChildren(TouchSensor1179)
Transform1180 = Transform()
Transform1180.setTranslation([0.1983,0.7045,-0.0767])
Shape1181 = Shape()
Shape1181.setUSE("HAnimJointShape")

Transform1180.addChildren(Shape1181)

HAnimSegment1178.addChildren(Transform1180)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ring3'/> to <HAnimSite name='l_ring_distal_tip'/>
Shape1182 = Shape()
LineSet1183 = LineSet()
LineSet1183.setVertexCount([2])
Coordinate1184 = Coordinate()
Coordinate1184.setPoint([0.1983,0.7045,-0.0767,0.2035,0.675,-0.0756])

LineSet1183.setCoord(Coordinate1184)
ColorRGBA1185 = ColorRGBA()
ColorRGBA1185.setUSE("HAnimSiteLineColorRGBA")

LineSet1183.setColor(ColorRGBA1185)

Shape1182.setGeometry(LineSet1183)

HAnimSegment1178.addChildren(Shape1182)
HAnimSite1186 = HAnimSite()
HAnimSite1186.setName("l_ring_distal_tip")
HAnimSite1186.setDEF("hanim_l_ring_distal_tip")
HAnimSite1186.setTranslation([0.2035,0.675,-0.0756])
#HAnimSite visualization shape
TouchSensor1187 = TouchSensor()
TouchSensor1187.setDescription("HAnimSite l_ring_distal_tip")

HAnimSite1186.addChildren(TouchSensor1187)
Shape1188 = Shape()
Shape1188.setUSE("HAnimSiteShape")

HAnimSite1186.addChildren(Shape1188)

HAnimSegment1178.addChildren(HAnimSite1186)

HAnimJoint1177.addChildren(HAnimSegment1178)

HAnimJoint1168.addChildren(HAnimJoint1177)

HAnimJoint1159.addChildren(HAnimJoint1168)

HAnimJoint1150.addChildren(HAnimJoint1159)

HAnimJoint979.addChildren(HAnimJoint1150)
HAnimJoint1189 = HAnimJoint()
HAnimJoint1189.setName("l_pinky0")
HAnimJoint1189.setDEF("hanim_l_pinky0")
HAnimJoint1189.setCenter([0.1925,0.8066,-0.1036])
HAnimJoint1189.setStiffness([0,0,0])
HAnimSegment1190 = HAnimSegment()
HAnimSegment1190.setName("l_pinky_metacarpal")
HAnimSegment1190.setDEF("hanim_l_pinky_metacarpal")
#<HAnimJoint name='l_pinky0'/> visualization sphere within <HAnimSegment name='l_pinky_metacarpal'/>
TouchSensor1191 = TouchSensor()
TouchSensor1191.setDescription("HAnimJoint l_pinky0, HAnimSegment l_pinky_metacarpal")

HAnimSegment1190.addChildren(TouchSensor1191)
Transform1192 = Transform()
Transform1192.setTranslation([0.1925,0.8066,-0.1036])
Shape1193 = Shape()
Shape1193.setUSE("HAnimJointShape")

Transform1192.addChildren(Shape1193)

HAnimSegment1190.addChildren(Transform1192)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky0'/> to <HAnimJoint name='l_pinky1'/>
Shape1194 = Shape()
LineSet1195 = LineSet()
LineSet1195.setVertexCount([2])
Coordinate1196 = Coordinate()
Coordinate1196.setPoint([0.1925,0.8066,-0.1036,0.1925,0.7866,-0.1036])

LineSet1195.setCoord(Coordinate1196)
ColorRGBA1197 = ColorRGBA()
ColorRGBA1197.setUSE("HAnimSegmentLineColorRGBA")

LineSet1195.setColor(ColorRGBA1197)

Shape1194.setGeometry(LineSet1195)

HAnimSegment1190.addChildren(Shape1194)

HAnimJoint1189.addChildren(HAnimSegment1190)
HAnimJoint1198 = HAnimJoint()
HAnimJoint1198.setName("l_pinky1")
HAnimJoint1198.setDEF("hanim_l_pinky1")
HAnimJoint1198.setCenter([0.1925,0.7866,-0.1036])
HAnimJoint1198.setStiffness([0,0,0])
HAnimSegment1199 = HAnimSegment()
HAnimSegment1199.setName("l_pinky_proximal")
HAnimSegment1199.setDEF("hanim_l_pinky_proximal")
#<HAnimJoint name='l_pinky1'/> visualization sphere within <HAnimSegment name='l_pinky_proximal'/>
TouchSensor1200 = TouchSensor()
TouchSensor1200.setDescription("HAnimJoint l_pinky1, HAnimSegment l_pinky_proximal")

HAnimSegment1199.addChildren(TouchSensor1200)
Transform1201 = Transform()
Transform1201.setTranslation([0.1925,0.7866,-0.1036])
Shape1202 = Shape()
Shape1202.setUSE("HAnimJointShape")

Transform1201.addChildren(Shape1202)

HAnimSegment1199.addChildren(Transform1201)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky1'/> to <HAnimJoint name='l_pinky2'/>
Shape1203 = Shape()
LineSet1204 = LineSet()
LineSet1204.setVertexCount([2])
Coordinate1205 = Coordinate()
Coordinate1205.setPoint([0.1925,0.7866,-0.1036,0.1938,0.7452,-0.1024])

LineSet1204.setCoord(Coordinate1205)
ColorRGBA1206 = ColorRGBA()
ColorRGBA1206.setUSE("HAnimSegmentLineColorRGBA")

LineSet1204.setColor(ColorRGBA1206)

Shape1203.setGeometry(LineSet1204)

HAnimSegment1199.addChildren(Shape1203)

HAnimJoint1198.addChildren(HAnimSegment1199)
HAnimJoint1207 = HAnimJoint()
HAnimJoint1207.setName("l_pinky2")
HAnimJoint1207.setDEF("hanim_l_pinky2")
HAnimJoint1207.setCenter([0.1938,0.7452,-0.1024])
HAnimJoint1207.setStiffness([0,0,0])
HAnimSegment1208 = HAnimSegment()
HAnimSegment1208.setName("l_pinky_middle")
HAnimSegment1208.setDEF("hanim_l_pinky_middle")
#<HAnimJoint name='l_pinky2'/> visualization sphere within <HAnimSegment name='l_pinky_middle'/>
TouchSensor1209 = TouchSensor()
TouchSensor1209.setDescription("HAnimJoint l_pinky2, HAnimSegment l_pinky_middle")

HAnimSegment1208.addChildren(TouchSensor1209)
Transform1210 = Transform()
Transform1210.setTranslation([0.1938,0.7452,-0.1024])
Shape1211 = Shape()
Shape1211.setUSE("HAnimJointShape")

Transform1210.addChildren(Shape1211)

HAnimSegment1208.addChildren(Transform1210)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky2'/> to <HAnimJoint name='l_pinky3'/>
Shape1212 = Shape()
LineSet1213 = LineSet()
LineSet1213.setVertexCount([2])
Coordinate1214 = Coordinate()
Coordinate1214.setPoint([0.1938,0.7452,-0.1024,0.1948,0.7277,-0.1017])

LineSet1213.setCoord(Coordinate1214)
ColorRGBA1215 = ColorRGBA()
ColorRGBA1215.setUSE("HAnimSegmentLineColorRGBA")

LineSet1213.setColor(ColorRGBA1215)

Shape1212.setGeometry(LineSet1213)

HAnimSegment1208.addChildren(Shape1212)

HAnimJoint1207.addChildren(HAnimSegment1208)
HAnimJoint1216 = HAnimJoint()
HAnimJoint1216.setName("l_pinky3")
HAnimJoint1216.setDEF("hanim_l_pinky3")
HAnimJoint1216.setCenter([0.1948,0.7277,-0.1017])
HAnimJoint1216.setStiffness([0,0,0])
HAnimSegment1217 = HAnimSegment()
HAnimSegment1217.setName("l_pinky_distal")
HAnimSegment1217.setDEF("hanim_l_pinky_distal")
#<HAnimJoint name='l_pinky3'/> visualization sphere within <HAnimSegment name='l_pinky_distal'/>
TouchSensor1218 = TouchSensor()
TouchSensor1218.setDescription("HAnimJoint l_pinky3, HAnimSegment l_pinky_distal")

HAnimSegment1217.addChildren(TouchSensor1218)
Transform1219 = Transform()
Transform1219.setTranslation([0.1948,0.7277,-0.1017])
Shape1220 = Shape()
Shape1220.setUSE("HAnimJointShape")

Transform1219.addChildren(Shape1220)

HAnimSegment1217.addChildren(Transform1219)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_pinky3'/> to <HAnimSite name='l_pinky_distal_tip'/>
Shape1221 = Shape()
LineSet1222 = LineSet()
LineSet1222.setVertexCount([2])
Coordinate1223 = Coordinate()
Coordinate1223.setPoint([0.1948,0.7277,-0.1017,0.2014,0.7009,-0.1012])

LineSet1222.setCoord(Coordinate1223)
ColorRGBA1224 = ColorRGBA()
ColorRGBA1224.setUSE("HAnimSiteLineColorRGBA")

LineSet1222.setColor(ColorRGBA1224)

Shape1221.setGeometry(LineSet1222)

HAnimSegment1217.addChildren(Shape1221)
HAnimSite1225 = HAnimSite()
HAnimSite1225.setName("l_pinky_distal_tip")
HAnimSite1225.setDEF("hanim_l_pinky_distal_tip")
HAnimSite1225.setTranslation([0.2014,0.7009,-0.1012])
#HAnimSite visualization shape
TouchSensor1226 = TouchSensor()
TouchSensor1226.setDescription("HAnimSite l_pinky_distal_tip")

HAnimSite1225.addChildren(TouchSensor1226)
Shape1227 = Shape()
Shape1227.setUSE("HAnimSiteShape")

HAnimSite1225.addChildren(Shape1227)

HAnimSegment1217.addChildren(HAnimSite1225)

HAnimJoint1216.addChildren(HAnimSegment1217)

HAnimJoint1207.addChildren(HAnimJoint1216)

HAnimJoint1198.addChildren(HAnimJoint1207)

HAnimJoint1189.addChildren(HAnimJoint1198)

HAnimJoint979.addChildren(HAnimJoint1189)

HAnimJoint942.addChildren(HAnimJoint979)

HAnimJoint926.addChildren(HAnimJoint942)

HAnimJoint917.addChildren(HAnimJoint926)

HAnimJoint880.addChildren(HAnimJoint917)

HAnimJoint596.addChildren(HAnimJoint880)
HAnimJoint1228 = HAnimJoint()
HAnimJoint1228.setName("r_sternoclavicular")
HAnimJoint1228.setDEF("hanim_r_sternoclavicular")
HAnimJoint1228.setCenter([-0.082,1.4488,-0.0353])
HAnimJoint1228.setStiffness([0,0,0])
HAnimSegment1229 = HAnimSegment()
HAnimSegment1229.setName("r_clavicle")
HAnimSegment1229.setDEF("hanim_r_clavicle")
#<HAnimJoint name='r_sternoclavicular'/> visualization sphere within <HAnimSegment name='r_clavicle'/>
TouchSensor1230 = TouchSensor()
TouchSensor1230.setDescription("HAnimJoint r_sternoclavicular, HAnimSegment r_clavicle")

HAnimSegment1229.addChildren(TouchSensor1230)
Transform1231 = Transform()
Transform1231.setTranslation([-0.082,1.4488,-0.0353])
Shape1232 = Shape()
Shape1232.setUSE("HAnimJointShape")

Transform1231.addChildren(Shape1232)

HAnimSegment1229.addChildren(Transform1231)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_sternoclavicular'/> to <HAnimJoint name='r_acromioclavicular'/>
Shape1233 = Shape()
LineSet1234 = LineSet()
LineSet1234.setVertexCount([2])
Coordinate1235 = Coordinate()
Coordinate1235.setPoint([-0.082,1.4488,-0.0353,-0.0962,1.4269,-0.0424])

LineSet1234.setCoord(Coordinate1235)
ColorRGBA1236 = ColorRGBA()
ColorRGBA1236.setUSE("HAnimSegmentLineColorRGBA")

LineSet1234.setColor(ColorRGBA1236)

Shape1233.setGeometry(LineSet1234)

HAnimSegment1229.addChildren(Shape1233)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_clavicale'/>
Shape1237 = Shape()
LineSet1238 = LineSet()
LineSet1238.setVertexCount([2])
Coordinate1239 = Coordinate()
Coordinate1239.setPoint([-0.082,1.4488,-0.0353,-0.0115,1.4943,0.04])

LineSet1238.setCoord(Coordinate1239)
ColorRGBA1240 = ColorRGBA()
ColorRGBA1240.setUSE("HAnimSiteLineColorRGBA")

LineSet1238.setColor(ColorRGBA1240)

Shape1237.setGeometry(LineSet1238)

HAnimSegment1229.addChildren(Shape1237)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_acromion'/>
Shape1241 = Shape()
LineSet1242 = LineSet()
LineSet1242.setVertexCount([2])
Coordinate1243 = Coordinate()
Coordinate1243.setPoint([-0.082,1.4488,-0.0353,-0.1905,1.4791,-0.0431])

LineSet1242.setCoord(Coordinate1243)
ColorRGBA1244 = ColorRGBA()
ColorRGBA1244.setUSE("HAnimSiteLineColorRGBA")

LineSet1242.setColor(ColorRGBA1244)

Shape1241.setGeometry(LineSet1242)

HAnimSegment1229.addChildren(Shape1241)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_ant'/>
Shape1245 = Shape()
LineSet1246 = LineSet()
LineSet1246.setVertexCount([2])
Coordinate1247 = Coordinate()
Coordinate1247.setPoint([-0.082,1.4488,-0.0353,-0.1626,1.4072,-0.0031])

LineSet1246.setCoord(Coordinate1247)
ColorRGBA1248 = ColorRGBA()
ColorRGBA1248.setUSE("HAnimSiteLineColorRGBA")

LineSet1246.setColor(ColorRGBA1248)

Shape1245.setGeometry(LineSet1246)

HAnimSegment1229.addChildren(Shape1245)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_post'/>
Shape1249 = Shape()
LineSet1250 = LineSet()
LineSet1250.setVertexCount([2])
Coordinate1251 = Coordinate()
Coordinate1251.setPoint([-0.082,1.4488,-0.0353,-0.1603,1.4098,-0.0826])

LineSet1250.setCoord(Coordinate1251)
ColorRGBA1252 = ColorRGBA()
ColorRGBA1252.setUSE("HAnimSiteLineColorRGBA")

LineSet1250.setColor(ColorRGBA1252)

Shape1249.setGeometry(LineSet1250)

HAnimSegment1229.addChildren(Shape1249)
HAnimSite1253 = HAnimSite()
HAnimSite1253.setName("r_clavicale_pt")
HAnimSite1253.setDEF("hanim_r_clavicale_pt")
HAnimSite1253.setTranslation([-0.0115,1.4943,0.04])
#HAnimSite visualization shape
TouchSensor1254 = TouchSensor()
TouchSensor1254.setDescription("HAnimSite r_clavicale")

HAnimSite1253.addChildren(TouchSensor1254)
Shape1255 = Shape()
Shape1255.setUSE("HAnimSiteShape")

HAnimSite1253.addChildren(Shape1255)

HAnimSegment1229.addChildren(HAnimSite1253)
HAnimSite1256 = HAnimSite()
HAnimSite1256.setName("r_acromion_pt")
HAnimSite1256.setDEF("hanim_r_acromion_pt")
HAnimSite1256.setTranslation([-0.1905,1.4791,-0.0431])
#HAnimSite visualization shape
TouchSensor1257 = TouchSensor()
TouchSensor1257.setDescription("HAnimSite r_acromion")

HAnimSite1256.addChildren(TouchSensor1257)
Shape1258 = Shape()
Shape1258.setUSE("HAnimSiteShape")

HAnimSite1256.addChildren(Shape1258)

HAnimSegment1229.addChildren(HAnimSite1256)
HAnimSite1259 = HAnimSite()
HAnimSite1259.setName("r_axilla_ant_pt")
HAnimSite1259.setDEF("hanim_r_axilla_ant_pt")
HAnimSite1259.setTranslation([-0.1626,1.4072,-0.0031])
#HAnimSite visualization shape
TouchSensor1260 = TouchSensor()
TouchSensor1260.setDescription("HAnimSite r_axilla_ant")

HAnimSite1259.addChildren(TouchSensor1260)
Shape1261 = Shape()
Shape1261.setUSE("HAnimSiteShape")

HAnimSite1259.addChildren(Shape1261)

HAnimSegment1229.addChildren(HAnimSite1259)
HAnimSite1262 = HAnimSite()
HAnimSite1262.setName("r_axilla_post_pt")
HAnimSite1262.setDEF("hanim_r_axilla_post_pt")
HAnimSite1262.setTranslation([-0.1603,1.4098,-0.0826])
#HAnimSite visualization shape
TouchSensor1263 = TouchSensor()
TouchSensor1263.setDescription("HAnimSite r_axilla_post")

HAnimSite1262.addChildren(TouchSensor1263)
Shape1264 = Shape()
Shape1264.setUSE("HAnimSiteShape")

HAnimSite1262.addChildren(Shape1264)

HAnimSegment1229.addChildren(HAnimSite1262)

HAnimJoint1228.addChildren(HAnimSegment1229)
HAnimJoint1265 = HAnimJoint()
HAnimJoint1265.setName("r_acromioclavicular")
HAnimJoint1265.setDEF("hanim_r_acromioclavicular")
HAnimJoint1265.setCenter([-0.0962,1.4269,-0.0424])
HAnimJoint1265.setStiffness([0,0,0])
HAnimSegment1266 = HAnimSegment()
HAnimSegment1266.setName("r_scapula")
HAnimSegment1266.setDEF("hanim_r_scapula")
#<HAnimJoint name='r_acromioclavicular'/> visualization sphere within <HAnimSegment name='r_scapula'/>
TouchSensor1267 = TouchSensor()
TouchSensor1267.setDescription("HAnimJoint r_acromioclavicular, HAnimSegment r_scapula")

HAnimSegment1266.addChildren(TouchSensor1267)
Transform1268 = Transform()
Transform1268.setTranslation([-0.0962,1.4269,-0.0424])
Shape1269 = Shape()
Shape1269.setUSE("HAnimJointShape")

Transform1268.addChildren(Shape1269)

HAnimSegment1266.addChildren(Transform1268)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_acromioclavicular'/> to <HAnimJoint name='r_shoulder'/>
Shape1270 = Shape()
LineSet1271 = LineSet()
LineSet1271.setVertexCount([2])
Coordinate1272 = Coordinate()
Coordinate1272.setPoint([-0.0962,1.4269,-0.0424,-0.2029,1.4376,-0.0387])

LineSet1271.setCoord(Coordinate1272)
ColorRGBA1273 = ColorRGBA()
ColorRGBA1273.setUSE("HAnimSegmentLineColorRGBA")

LineSet1271.setColor(ColorRGBA1273)

Shape1270.setGeometry(LineSet1271)

HAnimSegment1266.addChildren(Shape1270)

HAnimJoint1265.addChildren(HAnimSegment1266)
HAnimJoint1274 = HAnimJoint()
HAnimJoint1274.setName("r_shoulder")
HAnimJoint1274.setDEF("hanim_r_shoulder")
HAnimJoint1274.setCenter([-0.2029,1.4376,-0.0387])
HAnimJoint1274.setStiffness([0,0,0])
HAnimSegment1275 = HAnimSegment()
HAnimSegment1275.setName("r_upperarm")
HAnimSegment1275.setDEF("hanim_r_upperarm")
#<HAnimJoint name='r_shoulder'/> visualization sphere within <HAnimSegment name='r_upperarm'/>
TouchSensor1276 = TouchSensor()
TouchSensor1276.setDescription("HAnimJoint r_shoulder, HAnimSegment r_upperarm")

HAnimSegment1275.addChildren(TouchSensor1276)
Transform1277 = Transform()
Transform1277.setTranslation([-0.2029,1.4376,-0.0387])
Shape1278 = Shape()
Shape1278.setUSE("HAnimJointShape")

Transform1277.addChildren(Shape1278)

HAnimSegment1275.addChildren(Transform1277)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_shoulder'/> to <HAnimJoint name='r_elbow'/>
Shape1279 = Shape()
LineSet1280 = LineSet()
LineSet1280.setVertexCount([2])
Coordinate1281 = Coordinate()
Coordinate1281.setPoint([-0.2029,1.4376,-0.0387,-0.2014,1.1357,-0.0682])

LineSet1280.setCoord(Coordinate1281)
ColorRGBA1282 = ColorRGBA()
ColorRGBA1282.setUSE("HAnimSegmentLineColorRGBA")

LineSet1280.setColor(ColorRGBA1282)

Shape1279.setGeometry(LineSet1280)

HAnimSegment1275.addChildren(Shape1279)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_shoulder'/> to <HAnimSite name='r_humeral_lateral_epicn'/>
Shape1283 = Shape()
LineSet1284 = LineSet()
LineSet1284.setVertexCount([2])
Coordinate1285 = Coordinate()
Coordinate1285.setPoint([-0.2029,1.4376,-0.0387,-0.2224,1.1517,-0.1033])

LineSet1284.setCoord(Coordinate1285)
ColorRGBA1286 = ColorRGBA()
ColorRGBA1286.setUSE("HAnimSiteLineColorRGBA")

LineSet1284.setColor(ColorRGBA1286)

Shape1283.setGeometry(LineSet1284)

HAnimSegment1275.addChildren(Shape1283)
HAnimSite1287 = HAnimSite()
HAnimSite1287.setName("r_humeral_lateral_epicn_pt")
HAnimSite1287.setDEF("hanim_r_humeral_lateral_epicn_pt")
HAnimSite1287.setTranslation([-0.2224,1.1517,-0.1033])
#HAnimSite visualization shape
TouchSensor1288 = TouchSensor()
TouchSensor1288.setDescription("HAnimSite r_humeral_lateral_epicn")

HAnimSite1287.addChildren(TouchSensor1288)
Shape1289 = Shape()
Shape1289.setUSE("HAnimSiteShape")

HAnimSite1287.addChildren(Shape1289)

HAnimSegment1275.addChildren(HAnimSite1287)

HAnimJoint1274.addChildren(HAnimSegment1275)
HAnimJoint1290 = HAnimJoint()
HAnimJoint1290.setName("r_elbow")
HAnimJoint1290.setDEF("hanim_r_elbow")
HAnimJoint1290.setCenter([-0.2014,1.1357,-0.0682])
HAnimJoint1290.setStiffness([0,0,0])
HAnimSegment1291 = HAnimSegment()
HAnimSegment1291.setName("r_forearm")
HAnimSegment1291.setDEF("hanim_r_forearm")
#<HAnimJoint name='r_elbow'/> visualization sphere within <HAnimSegment name='r_forearm'/>
TouchSensor1292 = TouchSensor()
TouchSensor1292.setDescription("HAnimJoint r_elbow, HAnimSegment r_forearm")

HAnimSegment1291.addChildren(TouchSensor1292)
Transform1293 = Transform()
Transform1293.setTranslation([-0.2014,1.1357,-0.0682])
Shape1294 = Shape()
Shape1294.setUSE("HAnimJointShape")

Transform1293.addChildren(Shape1294)

HAnimSegment1291.addChildren(Transform1293)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_elbow'/> to <HAnimJoint name='r_wrist'/>
Shape1295 = Shape()
LineSet1296 = LineSet()
LineSet1296.setVertexCount([2])
Coordinate1297 = Coordinate()
Coordinate1297.setPoint([-0.2014,1.1357,-0.0682,-0.1984,0.8663,-0.0583])

LineSet1296.setCoord(Coordinate1297)
ColorRGBA1298 = ColorRGBA()
ColorRGBA1298.setUSE("HAnimSegmentLineColorRGBA")

LineSet1296.setColor(ColorRGBA1298)

Shape1295.setGeometry(LineSet1296)

HAnimSegment1291.addChildren(Shape1295)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radial_styloid'/>
Shape1299 = Shape()
LineSet1300 = LineSet()
LineSet1300.setVertexCount([2])
Coordinate1301 = Coordinate()
Coordinate1301.setPoint([-0.2014,1.1357,-0.0682,-0.1884,0.8676,-0.036])

LineSet1300.setCoord(Coordinate1301)
ColorRGBA1302 = ColorRGBA()
ColorRGBA1302.setUSE("HAnimSiteLineColorRGBA")

LineSet1300.setColor(ColorRGBA1302)

Shape1299.setGeometry(LineSet1300)

HAnimSegment1291.addChildren(Shape1299)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_olecranon'/>
Shape1303 = Shape()
LineSet1304 = LineSet()
LineSet1304.setVertexCount([2])
Coordinate1305 = Coordinate()
Coordinate1305.setPoint([-0.2014,1.1357,-0.0682,-0.1907,1.1405,-0.1065])

LineSet1304.setCoord(Coordinate1305)
ColorRGBA1306 = ColorRGBA()
ColorRGBA1306.setUSE("HAnimSiteLineColorRGBA")

LineSet1304.setColor(ColorRGBA1306)

Shape1303.setGeometry(LineSet1304)

HAnimSegment1291.addChildren(Shape1303)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_humeral_medial_epicn'/>
Shape1307 = Shape()
LineSet1308 = LineSet()
LineSet1308.setVertexCount([2])
Coordinate1309 = Coordinate()
Coordinate1309.setPoint([-0.2014,1.1357,-0.0682,-0.168,1.1298,-0.1062])

LineSet1308.setCoord(Coordinate1309)
ColorRGBA1310 = ColorRGBA()
ColorRGBA1310.setUSE("HAnimSiteLineColorRGBA")

LineSet1308.setColor(ColorRGBA1310)

Shape1307.setGeometry(LineSet1308)

HAnimSegment1291.addChildren(Shape1307)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radiale'/>
Shape1311 = Shape()
LineSet1312 = LineSet()
LineSet1312.setVertexCount([2])
Coordinate1313 = Coordinate()
Coordinate1313.setPoint([-0.2014,1.1357,-0.0682,-0.213,1.1305,-0.1091])

LineSet1312.setCoord(Coordinate1313)
ColorRGBA1314 = ColorRGBA()
ColorRGBA1314.setUSE("HAnimSiteLineColorRGBA")

LineSet1312.setColor(ColorRGBA1314)

Shape1311.setGeometry(LineSet1312)

HAnimSegment1291.addChildren(Shape1311)
HAnimSite1315 = HAnimSite()
HAnimSite1315.setName("r_radial_styloid_pt")
HAnimSite1315.setDEF("hanim_r_radial_styloid_pt")
HAnimSite1315.setTranslation([-0.1884,0.8676,-0.036])
#HAnimSite visualization shape
TouchSensor1316 = TouchSensor()
TouchSensor1316.setDescription("HAnimSite r_radial_styloid")

HAnimSite1315.addChildren(TouchSensor1316)
Shape1317 = Shape()
Shape1317.setUSE("HAnimSiteShape")

HAnimSite1315.addChildren(Shape1317)

HAnimSegment1291.addChildren(HAnimSite1315)
HAnimSite1318 = HAnimSite()
HAnimSite1318.setName("r_olecranon_pt")
HAnimSite1318.setDEF("hanim_r_olecranon_pt")
HAnimSite1318.setTranslation([-0.1907,1.1405,-0.1065])
#HAnimSite visualization shape
TouchSensor1319 = TouchSensor()
TouchSensor1319.setDescription("HAnimSite r_olecranon")

HAnimSite1318.addChildren(TouchSensor1319)
Shape1320 = Shape()
Shape1320.setUSE("HAnimSiteShape")

HAnimSite1318.addChildren(Shape1320)

HAnimSegment1291.addChildren(HAnimSite1318)
HAnimSite1321 = HAnimSite()
HAnimSite1321.setName("r_humeral_medial_epicn_pt")
HAnimSite1321.setDEF("hanim_r_humeral_medial_epicn_pt")
HAnimSite1321.setTranslation([-0.168,1.1298,-0.1062])
#HAnimSite visualization shape
TouchSensor1322 = TouchSensor()
TouchSensor1322.setDescription("HAnimSite r_humeral_medial_epicn")

HAnimSite1321.addChildren(TouchSensor1322)
Shape1323 = Shape()
Shape1323.setUSE("HAnimSiteShape")

HAnimSite1321.addChildren(Shape1323)

HAnimSegment1291.addChildren(HAnimSite1321)
HAnimSite1324 = HAnimSite()
HAnimSite1324.setName("r_radiale_pt")
HAnimSite1324.setDEF("hanim_r_radiale_pt")
HAnimSite1324.setTranslation([-0.213,1.1305,-0.1091])
#HAnimSite visualization shape
TouchSensor1325 = TouchSensor()
TouchSensor1325.setDescription("HAnimSite r_radiale")

HAnimSite1324.addChildren(TouchSensor1325)
Shape1326 = Shape()
Shape1326.setUSE("HAnimSiteShape")

HAnimSite1324.addChildren(Shape1326)

HAnimSegment1291.addChildren(HAnimSite1324)

HAnimJoint1290.addChildren(HAnimSegment1291)
HAnimJoint1327 = HAnimJoint()
HAnimJoint1327.setName("r_wrist")
HAnimJoint1327.setDEF("hanim_r_wrist")
HAnimJoint1327.setCenter([-0.1984,0.8663,-0.0583])
HAnimJoint1327.setStiffness([0,0,0])
HAnimSegment1328 = HAnimSegment()
HAnimSegment1328.setName("r_hand")
HAnimSegment1328.setDEF("hanim_r_hand")
#<HAnimJoint name='r_wrist'/> visualization sphere within <HAnimSegment name='r_hand'/>
TouchSensor1329 = TouchSensor()
TouchSensor1329.setDescription("HAnimJoint r_wrist, HAnimSegment r_hand")

HAnimSegment1328.addChildren(TouchSensor1329)
Transform1330 = Transform()
Transform1330.setTranslation([-0.1984,0.8663,-0.0583])
Shape1331 = Shape()
Shape1331.setUSE("HAnimJointShape")

Transform1330.addChildren(Shape1331)

HAnimSegment1328.addChildren(Transform1330)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_thumb1'/>
Shape1332 = Shape()
LineSet1333 = LineSet()
LineSet1333.setVertexCount([2])
Coordinate1334 = Coordinate()
Coordinate1334.setPoint([-0.1984,0.8663,-0.0583,-0.1924,0.8472,-0.0534])

LineSet1333.setCoord(Coordinate1334)
ColorRGBA1335 = ColorRGBA()
ColorRGBA1335.setUSE("HAnimSegmentLineColorRGBA")

LineSet1333.setColor(ColorRGBA1335)

Shape1332.setGeometry(LineSet1333)

HAnimSegment1328.addChildren(Shape1332)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_index0'/>
Shape1336 = Shape()
LineSet1337 = LineSet()
LineSet1337.setVertexCount([2])
Coordinate1338 = Coordinate()
Coordinate1338.setPoint([-0.1984,0.8663,-0.0583,-0.1983,0.8024,-0.028])

LineSet1337.setCoord(Coordinate1338)
ColorRGBA1339 = ColorRGBA()
ColorRGBA1339.setUSE("HAnimSegmentLineColorRGBA")

LineSet1337.setColor(ColorRGBA1339)

Shape1336.setGeometry(LineSet1337)

HAnimSegment1328.addChildren(Shape1336)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_middle0'/>
Shape1340 = Shape()
LineSet1341 = LineSet()
LineSet1341.setVertexCount([2])
Coordinate1342 = Coordinate()
Coordinate1342.setPoint([-0.1984,0.8663,-0.0583,-0.1987,0.8029,-0.053])

LineSet1341.setCoord(Coordinate1342)
ColorRGBA1343 = ColorRGBA()
ColorRGBA1343.setUSE("HAnimSegmentLineColorRGBA")

LineSet1341.setColor(ColorRGBA1343)

Shape1340.setGeometry(LineSet1341)

HAnimSegment1328.addChildren(Shape1340)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_ring0'/>
Shape1344 = Shape()
LineSet1345 = LineSet()
LineSet1345.setVertexCount([2])
Coordinate1346 = Coordinate()
Coordinate1346.setPoint([-0.1984,0.8663,-0.0583,-0.1956,0.8019,-0.0794])

LineSet1345.setCoord(Coordinate1346)
ColorRGBA1347 = ColorRGBA()
ColorRGBA1347.setUSE("HAnimSegmentLineColorRGBA")

LineSet1345.setColor(ColorRGBA1347)

Shape1344.setGeometry(LineSet1345)

HAnimSegment1328.addChildren(Shape1344)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_pinky0'/>
Shape1348 = Shape()
LineSet1349 = LineSet()
LineSet1349.setVertexCount([2])
Coordinate1350 = Coordinate()
Coordinate1350.setPoint([-0.1984,0.8663,-0.0583,-0.1925,0.8066,-0.1036])

LineSet1349.setCoord(Coordinate1350)
ColorRGBA1351 = ColorRGBA()
ColorRGBA1351.setUSE("HAnimSegmentLineColorRGBA")

LineSet1349.setColor(ColorRGBA1351)

Shape1348.setGeometry(LineSet1349)

HAnimSegment1328.addChildren(Shape1348)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha2'/>
Shape1352 = Shape()
LineSet1353 = LineSet()
LineSet1353.setVertexCount([2])
Coordinate1354 = Coordinate()
Coordinate1354.setPoint([-0.1984,0.8663,-0.0583,-0.1977,0.8169,-0.0177])

LineSet1353.setCoord(Coordinate1354)
ColorRGBA1355 = ColorRGBA()
ColorRGBA1355.setUSE("HAnimSiteLineColorRGBA")

LineSet1353.setColor(ColorRGBA1355)

Shape1352.setGeometry(LineSet1353)

HAnimSegment1328.addChildren(Shape1352)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_ulnar_styloid'/>
Shape1356 = Shape()
LineSet1357 = LineSet()
LineSet1357.setVertexCount([2])
Coordinate1358 = Coordinate()
Coordinate1358.setPoint([-0.1984,0.8663,-0.0583,-0.2117,0.8562,-0.0584])

LineSet1357.setCoord(Coordinate1358)
ColorRGBA1359 = ColorRGBA()
ColorRGBA1359.setUSE("HAnimSiteLineColorRGBA")

LineSet1357.setColor(ColorRGBA1359)

Shape1356.setGeometry(LineSet1357)

HAnimSegment1328.addChildren(Shape1356)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha5'/>
Shape1360 = Shape()
LineSet1361 = LineSet()
LineSet1361.setVertexCount([2])
Coordinate1362 = Coordinate()
Coordinate1362.setPoint([-0.1984,0.8663,-0.0583,-0.1929,0.789,-0.1064])

LineSet1361.setCoord(Coordinate1362)
ColorRGBA1363 = ColorRGBA()
ColorRGBA1363.setUSE("HAnimSiteLineColorRGBA")

LineSet1361.setColor(ColorRGBA1363)

Shape1360.setGeometry(LineSet1361)

HAnimSegment1328.addChildren(Shape1360)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_hand_front_view'/>
Shape1364 = Shape()
LineSet1365 = LineSet()
LineSet1365.setVertexCount([2])
Coordinate1366 = Coordinate()
Coordinate1366.setPoint([-0.1984,0.8663,-0.0583,-0.3,0.75,0.45])

LineSet1365.setCoord(Coordinate1366)
ColorRGBA1367 = ColorRGBA()
ColorRGBA1367.setUSE("HAnimSiteViewpointLineColorRGBA")

LineSet1365.setColor(ColorRGBA1367)

Shape1364.setGeometry(LineSet1365)

HAnimSegment1328.addChildren(Shape1364)
HAnimSite1368 = HAnimSite()
HAnimSite1368.setName("r_metacarpal_pha2_pt")
HAnimSite1368.setDEF("hanim_r_metacarpal_pha2_pt")
HAnimSite1368.setTranslation([-0.1977,0.8169,-0.0177])
#HAnimSite visualization shape
TouchSensor1369 = TouchSensor()
TouchSensor1369.setDescription("HAnimSite r_metacarpal_pha2")

HAnimSite1368.addChildren(TouchSensor1369)
Shape1370 = Shape()
Shape1370.setUSE("HAnimSiteShape")

HAnimSite1368.addChildren(Shape1370)

HAnimSegment1328.addChildren(HAnimSite1368)
HAnimSite1371 = HAnimSite()
HAnimSite1371.setName("r_ulnar_styloid_pt")
HAnimSite1371.setDEF("hanim_r_ulnar_styloid_pt")
HAnimSite1371.setTranslation([-0.2117,0.8562,-0.0584])
#HAnimSite visualization shape
TouchSensor1372 = TouchSensor()
TouchSensor1372.setDescription("HAnimSite r_ulnar_styloid")

HAnimSite1371.addChildren(TouchSensor1372)
Shape1373 = Shape()
Shape1373.setUSE("HAnimSiteShape")

HAnimSite1371.addChildren(Shape1373)

HAnimSegment1328.addChildren(HAnimSite1371)
HAnimSite1374 = HAnimSite()
HAnimSite1374.setName("r_metacarpal_pha5_pt")
HAnimSite1374.setDEF("hanim_r_metacarpal_pha5_pt")
HAnimSite1374.setTranslation([-0.1929,0.789,-0.1064])
#HAnimSite visualization shape
TouchSensor1375 = TouchSensor()
TouchSensor1375.setDescription("HAnimSite r_metacarpal_pha5")

HAnimSite1374.addChildren(TouchSensor1375)
Shape1376 = Shape()
Shape1376.setUSE("HAnimSiteShape")

HAnimSite1374.addChildren(Shape1376)

HAnimSegment1328.addChildren(HAnimSite1374)
HAnimSite1377 = HAnimSite()
HAnimSite1377.setName("r_hand_front_view")
HAnimSite1377.setDEF("hanim_r_hand_front_view")
HAnimSite1377.setTranslation([-0.3,0.75,0.45])
Viewpoint1378 = Viewpoint()
Viewpoint1378.setDEF("hanim_r_hand_front_viewpoint")
Viewpoint1378.setCenterOfRotation([0,0.7,0])
Viewpoint1378.setDescription("right hand front")
Viewpoint1378.setPosition([0,0,0])

HAnimSite1377.addChildren(Viewpoint1378)
#HAnimSite/Viewpoint visualization shape
Anchor1379 = Anchor()
Anchor1379.setDescription("HAnimSite Viewpoint hanim_r_hand_front_view")
Anchor1379.setUrl(["#hanim_r_hand_front_viewpoint"])
LOD1380 = LOD()
LOD1380.setForceTransitions(True)
LOD1380.setRange([0.04])
WorldInfo1381 = WorldInfo()
WorldInfo1381.setInfo(["hide diamond when close"])

LOD1380.addChildren(WorldInfo1381)
Shape1382 = Shape()
Shape1382.setUSE("HAnimSiteViewpointShape")

LOD1380.addChildren(Shape1382)

Anchor1379.addChildren(LOD1380)

HAnimSite1377.addChildren(Anchor1379)

HAnimSegment1328.addChildren(HAnimSite1377)

HAnimJoint1327.addChildren(HAnimSegment1328)
HAnimJoint1383 = HAnimJoint()
HAnimJoint1383.setName("r_thumb1")
HAnimJoint1383.setDEF("hanim_r_thumb1")
HAnimJoint1383.setCenter([-0.1924,0.8472,-0.0534])
HAnimJoint1383.setStiffness([0,0,0])
HAnimSegment1384 = HAnimSegment()
HAnimSegment1384.setName("r_thumb_metacarpal")
HAnimSegment1384.setDEF("hanim_r_thumb_metacarpal")
#<HAnimJoint name='r_thumb1'/> visualization sphere within <HAnimSegment name='r_thumb_metacarpal'/>
TouchSensor1385 = TouchSensor()
TouchSensor1385.setDescription("HAnimJoint r_thumb1, HAnimSegment r_thumb_metacarpal")

HAnimSegment1384.addChildren(TouchSensor1385)
Transform1386 = Transform()
Transform1386.setTranslation([-0.1924,0.8472,-0.0534])
Shape1387 = Shape()
Shape1387.setUSE("HAnimJointShape")

Transform1386.addChildren(Shape1387)

HAnimSegment1384.addChildren(Transform1386)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb1'/> to <HAnimJoint name='r_thumb2'/>
Shape1388 = Shape()
LineSet1389 = LineSet()
LineSet1389.setVertexCount([2])
Coordinate1390 = Coordinate()
Coordinate1390.setPoint([-0.1924,0.8472,-0.0534,-0.1951,0.8226,0.0246])

LineSet1389.setCoord(Coordinate1390)
ColorRGBA1391 = ColorRGBA()
ColorRGBA1391.setUSE("HAnimSegmentLineColorRGBA")

LineSet1389.setColor(ColorRGBA1391)

Shape1388.setGeometry(LineSet1389)

HAnimSegment1384.addChildren(Shape1388)

HAnimJoint1383.addChildren(HAnimSegment1384)
HAnimJoint1392 = HAnimJoint()
HAnimJoint1392.setName("r_thumb2")
HAnimJoint1392.setDEF("hanim_r_thumb2")
HAnimJoint1392.setCenter([-0.1951,0.8226,0.0246])
HAnimJoint1392.setStiffness([0,0,0])
HAnimSegment1393 = HAnimSegment()
HAnimSegment1393.setName("r_thumb_proximal")
HAnimSegment1393.setDEF("hanim_r_thumb_proximal")
#<HAnimJoint name='r_thumb2'/> visualization sphere within <HAnimSegment name='r_thumb_proximal'/>
TouchSensor1394 = TouchSensor()
TouchSensor1394.setDescription("HAnimJoint r_thumb2, HAnimSegment r_thumb_proximal")

HAnimSegment1393.addChildren(TouchSensor1394)
Transform1395 = Transform()
Transform1395.setTranslation([-0.1951,0.8226,0.0246])
Shape1396 = Shape()
Shape1396.setUSE("HAnimJointShape")

Transform1395.addChildren(Shape1396)

HAnimSegment1393.addChildren(Transform1395)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb2'/> to <HAnimJoint name='r_thumb3'/>
Shape1397 = Shape()
LineSet1398 = LineSet()
LineSet1398.setVertexCount([2])
Coordinate1399 = Coordinate()
Coordinate1399.setPoint([-0.1951,0.8226,0.0246,-0.1955,0.8159,0.0464])

LineSet1398.setCoord(Coordinate1399)
ColorRGBA1400 = ColorRGBA()
ColorRGBA1400.setUSE("HAnimSegmentLineColorRGBA")

LineSet1398.setColor(ColorRGBA1400)

Shape1397.setGeometry(LineSet1398)

HAnimSegment1393.addChildren(Shape1397)

HAnimJoint1392.addChildren(HAnimSegment1393)
HAnimJoint1401 = HAnimJoint()
HAnimJoint1401.setName("r_thumb3")
HAnimJoint1401.setDEF("hanim_r_thumb3")
HAnimJoint1401.setCenter([-0.1955,0.8159,0.0464])
HAnimJoint1401.setStiffness([0,0,0])
HAnimSegment1402 = HAnimSegment()
HAnimSegment1402.setName("r_thumb_distal")
HAnimSegment1402.setDEF("hanim_r_thumb_distal")
#<HAnimJoint name='r_thumb3'/> visualization sphere within <HAnimSegment name='r_thumb_distal'/>
TouchSensor1403 = TouchSensor()
TouchSensor1403.setDescription("HAnimJoint r_thumb3, HAnimSegment r_thumb_distal")

HAnimSegment1402.addChildren(TouchSensor1403)
Transform1404 = Transform()
Transform1404.setTranslation([-0.1955,0.8159,0.0464])
Shape1405 = Shape()
Shape1405.setUSE("HAnimJointShape")

Transform1404.addChildren(Shape1405)

HAnimSegment1402.addChildren(Transform1404)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_thumb3'/> to <HAnimSite name='r_thumb_distal_tip'/>
Shape1406 = Shape()
LineSet1407 = LineSet()
LineSet1407.setVertexCount([2])
Coordinate1408 = Coordinate()
Coordinate1408.setPoint([-0.1955,0.8159,0.0464,-0.1869,0.809,0.082])

LineSet1407.setCoord(Coordinate1408)
ColorRGBA1409 = ColorRGBA()
ColorRGBA1409.setUSE("HAnimSiteLineColorRGBA")

LineSet1407.setColor(ColorRGBA1409)

Shape1406.setGeometry(LineSet1407)

HAnimSegment1402.addChildren(Shape1406)
HAnimSite1410 = HAnimSite()
HAnimSite1410.setName("r_thumb_distal_tip")
HAnimSite1410.setDEF("hanim_r_thumb_distal_tip")
HAnimSite1410.setTranslation([-0.1869,0.809,0.082])
#HAnimSite visualization shape
TouchSensor1411 = TouchSensor()
TouchSensor1411.setDescription("HAnimSite r_thumb_distal_tip")

HAnimSite1410.addChildren(TouchSensor1411)
Shape1412 = Shape()
Shape1412.setUSE("HAnimSiteShape")

HAnimSite1410.addChildren(Shape1412)

HAnimSegment1402.addChildren(HAnimSite1410)

HAnimJoint1401.addChildren(HAnimSegment1402)

HAnimJoint1392.addChildren(HAnimJoint1401)

HAnimJoint1383.addChildren(HAnimJoint1392)

HAnimJoint1327.addChildren(HAnimJoint1383)
HAnimJoint1413 = HAnimJoint()
HAnimJoint1413.setName("r_index0")
HAnimJoint1413.setDEF("hanim_r_index0")
HAnimJoint1413.setCenter([-0.1983,0.8024,-0.028])
HAnimJoint1413.setStiffness([0,0,0])
HAnimSegment1414 = HAnimSegment()
HAnimSegment1414.setName("r_index_metacarpal")
HAnimSegment1414.setDEF("hanim_r_index_metacarpal")
#<HAnimJoint name='r_index0'/> visualization sphere within <HAnimSegment name='r_index_metacarpal'/>
TouchSensor1415 = TouchSensor()
TouchSensor1415.setDescription("HAnimJoint r_index0, HAnimSegment r_index_metacarpal")

HAnimSegment1414.addChildren(TouchSensor1415)
Transform1416 = Transform()
Transform1416.setTranslation([-0.1983,0.8024,-0.028])
Shape1417 = Shape()
Shape1417.setUSE("HAnimJointShape")

Transform1416.addChildren(Shape1417)

HAnimSegment1414.addChildren(Transform1416)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index0'/> to <HAnimJoint name='r_index1'/>
Shape1418 = Shape()
LineSet1419 = LineSet()
LineSet1419.setVertexCount([2])
Coordinate1420 = Coordinate()
Coordinate1420.setPoint([-0.1983,0.8024,-0.028,-0.1983,0.7815,-0.028])

LineSet1419.setCoord(Coordinate1420)
ColorRGBA1421 = ColorRGBA()
ColorRGBA1421.setUSE("HAnimSegmentLineColorRGBA")

LineSet1419.setColor(ColorRGBA1421)

Shape1418.setGeometry(LineSet1419)

HAnimSegment1414.addChildren(Shape1418)

HAnimJoint1413.addChildren(HAnimSegment1414)
HAnimJoint1422 = HAnimJoint()
HAnimJoint1422.setName("r_index1")
HAnimJoint1422.setDEF("hanim_r_index1")
HAnimJoint1422.setCenter([-0.1983,0.7815,-0.028])
HAnimJoint1422.setStiffness([0,0,0])
HAnimSegment1423 = HAnimSegment()
HAnimSegment1423.setName("r_index_proximal")
HAnimSegment1423.setDEF("hanim_r_index_proximal")
#<HAnimJoint name='r_index1'/> visualization sphere within <HAnimSegment name='r_index_proximal'/>
TouchSensor1424 = TouchSensor()
TouchSensor1424.setDescription("HAnimJoint r_index1, HAnimSegment r_index_proximal")

HAnimSegment1423.addChildren(TouchSensor1424)
Transform1425 = Transform()
Transform1425.setTranslation([-0.1983,0.7815,-0.028])
Shape1426 = Shape()
Shape1426.setUSE("HAnimJointShape")

Transform1425.addChildren(Shape1426)

HAnimSegment1423.addChildren(Transform1425)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index1'/> to <HAnimJoint name='r_index2'/>
Shape1427 = Shape()
LineSet1428 = LineSet()
LineSet1428.setVertexCount([2])
Coordinate1429 = Coordinate()
Coordinate1429.setPoint([-0.1983,0.7815,-0.028,-0.2017,0.7363,-0.0248])

LineSet1428.setCoord(Coordinate1429)
ColorRGBA1430 = ColorRGBA()
ColorRGBA1430.setUSE("HAnimSegmentLineColorRGBA")

LineSet1428.setColor(ColorRGBA1430)

Shape1427.setGeometry(LineSet1428)

HAnimSegment1423.addChildren(Shape1427)

HAnimJoint1422.addChildren(HAnimSegment1423)
HAnimJoint1431 = HAnimJoint()
HAnimJoint1431.setName("r_index2")
HAnimJoint1431.setDEF("hanim_r_index2")
HAnimJoint1431.setCenter([-0.2017,0.7363,-0.0248])
HAnimJoint1431.setStiffness([0,0,0])
HAnimSegment1432 = HAnimSegment()
HAnimSegment1432.setName("r_index_middle")
HAnimSegment1432.setDEF("hanim_r_index_middle")
#<HAnimJoint name='r_index2'/> visualization sphere within <HAnimSegment name='r_index_middle'/>
TouchSensor1433 = TouchSensor()
TouchSensor1433.setDescription("HAnimJoint r_index2, HAnimSegment r_index_middle")

HAnimSegment1432.addChildren(TouchSensor1433)
Transform1434 = Transform()
Transform1434.setTranslation([-0.2017,0.7363,-0.0248])
Shape1435 = Shape()
Shape1435.setUSE("HAnimJointShape")

Transform1434.addChildren(Shape1435)

HAnimSegment1432.addChildren(Transform1434)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index2'/> to <HAnimJoint name='r_index3'/>
Shape1436 = Shape()
LineSet1437 = LineSet()
LineSet1437.setVertexCount([2])
Coordinate1438 = Coordinate()
Coordinate1438.setPoint([-0.2017,0.7363,-0.0248,-0.2028,0.7139,-0.0236])

LineSet1437.setCoord(Coordinate1438)
ColorRGBA1439 = ColorRGBA()
ColorRGBA1439.setUSE("HAnimSegmentLineColorRGBA")

LineSet1437.setColor(ColorRGBA1439)

Shape1436.setGeometry(LineSet1437)

HAnimSegment1432.addChildren(Shape1436)

HAnimJoint1431.addChildren(HAnimSegment1432)
HAnimJoint1440 = HAnimJoint()
HAnimJoint1440.setName("r_index3")
HAnimJoint1440.setDEF("hanim_r_index3")
HAnimJoint1440.setCenter([-0.2028,0.7139,-0.0236])
HAnimJoint1440.setStiffness([0,0,0])
HAnimSegment1441 = HAnimSegment()
HAnimSegment1441.setName("r_index_distal")
HAnimSegment1441.setDEF("hanim_r_index_distal")
#<HAnimJoint name='r_index3'/> visualization sphere within <HAnimSegment name='r_index_distal'/>
TouchSensor1442 = TouchSensor()
TouchSensor1442.setDescription("HAnimJoint r_index3, HAnimSegment r_index_distal")

HAnimSegment1441.addChildren(TouchSensor1442)
Transform1443 = Transform()
Transform1443.setTranslation([-0.2028,0.7139,-0.0236])
Shape1444 = Shape()
Shape1444.setUSE("HAnimJointShape")

Transform1443.addChildren(Shape1444)

HAnimSegment1441.addChildren(Transform1443)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_index_distal_tip'/>
Shape1445 = Shape()
LineSet1446 = LineSet()
LineSet1446.setVertexCount([2])
Coordinate1447 = Coordinate()
Coordinate1447.setPoint([-0.2028,0.7139,-0.0236,-0.198,0.6883,-0.018])

LineSet1446.setCoord(Coordinate1447)
ColorRGBA1448 = ColorRGBA()
ColorRGBA1448.setUSE("HAnimSiteLineColorRGBA")

LineSet1446.setColor(ColorRGBA1448)

Shape1445.setGeometry(LineSet1446)

HAnimSegment1441.addChildren(Shape1445)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_dactylion'/>
Shape1449 = Shape()
LineSet1450 = LineSet()
LineSet1450.setVertexCount([2])
Coordinate1451 = Coordinate()
Coordinate1451.setPoint([-0.2028,0.7139,-0.0236,-0.1941,0.6772,-0.0423])

LineSet1450.setCoord(Coordinate1451)
ColorRGBA1452 = ColorRGBA()
ColorRGBA1452.setUSE("HAnimSiteLineColorRGBA")

LineSet1450.setColor(ColorRGBA1452)

Shape1449.setGeometry(LineSet1450)

HAnimSegment1441.addChildren(Shape1449)
HAnimSite1453 = HAnimSite()
HAnimSite1453.setName("r_index_distal_tip")
HAnimSite1453.setDEF("hanim_r_index_distal_tip")
HAnimSite1453.setTranslation([-0.198,0.6883,-0.018])
#HAnimSite visualization shape
TouchSensor1454 = TouchSensor()
TouchSensor1454.setDescription("HAnimSite r_index_distal_tip")

HAnimSite1453.addChildren(TouchSensor1454)
Shape1455 = Shape()
Shape1455.setUSE("HAnimSiteShape")

HAnimSite1453.addChildren(Shape1455)

HAnimSegment1441.addChildren(HAnimSite1453)
HAnimSite1456 = HAnimSite()
HAnimSite1456.setName("r_dactylion_pt")
HAnimSite1456.setDEF("hanim_r_dactylion_pt")
HAnimSite1456.setTranslation([-0.1941,0.6772,-0.0423])
#HAnimSite visualization shape
TouchSensor1457 = TouchSensor()
TouchSensor1457.setDescription("HAnimSite r_dactylion")

HAnimSite1456.addChildren(TouchSensor1457)
Shape1458 = Shape()
Shape1458.setUSE("HAnimSiteShape")

HAnimSite1456.addChildren(Shape1458)

HAnimSegment1441.addChildren(HAnimSite1456)

HAnimJoint1440.addChildren(HAnimSegment1441)

HAnimJoint1431.addChildren(HAnimJoint1440)

HAnimJoint1422.addChildren(HAnimJoint1431)

HAnimJoint1413.addChildren(HAnimJoint1422)

HAnimJoint1327.addChildren(HAnimJoint1413)
HAnimJoint1459 = HAnimJoint()
HAnimJoint1459.setName("r_middle0")
HAnimJoint1459.setDEF("hanim_r_middle0")
HAnimJoint1459.setCenter([-0.1987,0.8029,-0.053])
HAnimJoint1459.setStiffness([0,0,0])
HAnimSegment1460 = HAnimSegment()
HAnimSegment1460.setName("r_middle_metacarpal")
HAnimSegment1460.setDEF("hanim_r_middle_metacarpal")
#<HAnimJoint name='r_middle0'/> visualization sphere within <HAnimSegment name='r_middle_metacarpal'/>
TouchSensor1461 = TouchSensor()
TouchSensor1461.setDescription("HAnimJoint r_middle0, HAnimSegment r_middle_metacarpal")

HAnimSegment1460.addChildren(TouchSensor1461)
Transform1462 = Transform()
Transform1462.setTranslation([-0.1987,0.8029,-0.053])
Shape1463 = Shape()
Shape1463.setUSE("HAnimJointShape")

Transform1462.addChildren(Shape1463)

HAnimSegment1460.addChildren(Transform1462)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle0'/> to <HAnimJoint name='r_middle1'/>
Shape1464 = Shape()
LineSet1465 = LineSet()
LineSet1465.setVertexCount([2])
Coordinate1466 = Coordinate()
Coordinate1466.setPoint([-0.1987,0.8029,-0.053,-0.1987,0.7818,-0.053])

LineSet1465.setCoord(Coordinate1466)
ColorRGBA1467 = ColorRGBA()
ColorRGBA1467.setUSE("HAnimSegmentLineColorRGBA")

LineSet1465.setColor(ColorRGBA1467)

Shape1464.setGeometry(LineSet1465)

HAnimSegment1460.addChildren(Shape1464)

HAnimJoint1459.addChildren(HAnimSegment1460)
HAnimJoint1468 = HAnimJoint()
HAnimJoint1468.setName("r_middle1")
HAnimJoint1468.setDEF("hanim_r_middle1")
HAnimJoint1468.setCenter([-0.1987,0.7818,-0.053])
HAnimJoint1468.setStiffness([0,0,0])
HAnimSegment1469 = HAnimSegment()
HAnimSegment1469.setName("r_middle_proximal")
HAnimSegment1469.setDEF("hanim_r_middle_proximal")
#<HAnimJoint name='r_middle1'/> visualization sphere within <HAnimSegment name='r_middle_proximal'/>
TouchSensor1470 = TouchSensor()
TouchSensor1470.setDescription("HAnimJoint r_middle1, HAnimSegment r_middle_proximal")

HAnimSegment1469.addChildren(TouchSensor1470)
Transform1471 = Transform()
Transform1471.setTranslation([-0.1987,0.7818,-0.053])
Shape1472 = Shape()
Shape1472.setUSE("HAnimJointShape")

Transform1471.addChildren(Shape1472)

HAnimSegment1469.addChildren(Transform1471)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle1'/> to <HAnimJoint name='r_middle2'/>
Shape1473 = Shape()
LineSet1474 = LineSet()
LineSet1474.setVertexCount([2])
Coordinate1475 = Coordinate()
Coordinate1475.setPoint([-0.1987,0.7818,-0.053,-0.2013,0.7273,-0.0503])

LineSet1474.setCoord(Coordinate1475)
ColorRGBA1476 = ColorRGBA()
ColorRGBA1476.setUSE("HAnimSegmentLineColorRGBA")

LineSet1474.setColor(ColorRGBA1476)

Shape1473.setGeometry(LineSet1474)

HAnimSegment1469.addChildren(Shape1473)

HAnimJoint1468.addChildren(HAnimSegment1469)
HAnimJoint1477 = HAnimJoint()
HAnimJoint1477.setName("r_middle2")
HAnimJoint1477.setDEF("hanim_r_middle2")
HAnimJoint1477.setCenter([-0.2013,0.7273,-0.0503])
HAnimJoint1477.setStiffness([0,0,0])
HAnimSegment1478 = HAnimSegment()
HAnimSegment1478.setName("r_middle_middle")
HAnimSegment1478.setDEF("hanim_r_middle_middle")
#<HAnimJoint name='r_middle2'/> visualization sphere within <HAnimSegment name='r_middle_middle'/>
TouchSensor1479 = TouchSensor()
TouchSensor1479.setDescription("HAnimJoint r_middle2, HAnimSegment r_middle_middle")

HAnimSegment1478.addChildren(TouchSensor1479)
Transform1480 = Transform()
Transform1480.setTranslation([-0.2013,0.7273,-0.0503])
Shape1481 = Shape()
Shape1481.setUSE("HAnimJointShape")

Transform1480.addChildren(Shape1481)

HAnimSegment1478.addChildren(Transform1480)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle2'/> to <HAnimJoint name='r_middle3'/>
Shape1482 = Shape()
LineSet1483 = LineSet()
LineSet1483.setVertexCount([2])
Coordinate1484 = Coordinate()
Coordinate1484.setPoint([-0.2013,0.7273,-0.0503,-0.2026,0.7011,-0.0494])

LineSet1483.setCoord(Coordinate1484)
ColorRGBA1485 = ColorRGBA()
ColorRGBA1485.setUSE("HAnimSegmentLineColorRGBA")

LineSet1483.setColor(ColorRGBA1485)

Shape1482.setGeometry(LineSet1483)

HAnimSegment1478.addChildren(Shape1482)

HAnimJoint1477.addChildren(HAnimSegment1478)
HAnimJoint1486 = HAnimJoint()
HAnimJoint1486.setName("r_middle3")
HAnimJoint1486.setDEF("hanim_r_middle3")
HAnimJoint1486.setCenter([-0.2026,0.7011,-0.0494])
HAnimJoint1486.setStiffness([0,0,0])
HAnimSegment1487 = HAnimSegment()
HAnimSegment1487.setName("r_middle_distal")
HAnimSegment1487.setDEF("hanim_r_middle_distal")
#<HAnimJoint name='r_middle3'/> visualization sphere within <HAnimSegment name='r_middle_distal'/>
TouchSensor1488 = TouchSensor()
TouchSensor1488.setDescription("HAnimJoint r_middle3, HAnimSegment r_middle_distal")

HAnimSegment1487.addChildren(TouchSensor1488)
Transform1489 = Transform()
Transform1489.setTranslation([-0.2026,0.7011,-0.0494])
Shape1490 = Shape()
Shape1490.setUSE("HAnimJointShape")

Transform1489.addChildren(Shape1490)

HAnimSegment1487.addChildren(Transform1489)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_middle3'/> to <HAnimSite name='r_middle_distal_tip'/>
Shape1491 = Shape()
LineSet1492 = LineSet()
LineSet1492.setVertexCount([2])
Coordinate1493 = Coordinate()
Coordinate1493.setPoint([-0.2026,0.7011,-0.0494,-0.1969,0.6758,-0.0427])

LineSet1492.setCoord(Coordinate1493)
ColorRGBA1494 = ColorRGBA()
ColorRGBA1494.setUSE("HAnimSiteLineColorRGBA")

LineSet1492.setColor(ColorRGBA1494)

Shape1491.setGeometry(LineSet1492)

HAnimSegment1487.addChildren(Shape1491)
HAnimSite1495 = HAnimSite()
HAnimSite1495.setName("r_middle_distal_tip")
HAnimSite1495.setDEF("hanim_r_middle_distal_tip")
HAnimSite1495.setTranslation([-0.1969,0.6758,-0.0427])
#HAnimSite visualization shape
TouchSensor1496 = TouchSensor()
TouchSensor1496.setDescription("HAnimSite r_middle_distal_tip")

HAnimSite1495.addChildren(TouchSensor1496)
Shape1497 = Shape()
Shape1497.setUSE("HAnimSiteShape")

HAnimSite1495.addChildren(Shape1497)

HAnimSegment1487.addChildren(HAnimSite1495)

HAnimJoint1486.addChildren(HAnimSegment1487)

HAnimJoint1477.addChildren(HAnimJoint1486)

HAnimJoint1468.addChildren(HAnimJoint1477)

HAnimJoint1459.addChildren(HAnimJoint1468)

HAnimJoint1327.addChildren(HAnimJoint1459)
HAnimJoint1498 = HAnimJoint()
HAnimJoint1498.setName("r_ring0")
HAnimJoint1498.setDEF("hanim_r_ring0")
HAnimJoint1498.setCenter([-0.1956,0.8019,-0.0794])
HAnimJoint1498.setStiffness([0,0,0])
HAnimSegment1499 = HAnimSegment()
HAnimSegment1499.setName("r_ring_metacarpal")
HAnimSegment1499.setDEF("hanim_r_ring_metacarpal")
#<HAnimJoint name='r_ring0'/> visualization sphere within <HAnimSegment name='r_ring_metacarpal'/>
TouchSensor1500 = TouchSensor()
TouchSensor1500.setDescription("HAnimJoint r_ring0, HAnimSegment r_ring_metacarpal")

HAnimSegment1499.addChildren(TouchSensor1500)
Transform1501 = Transform()
Transform1501.setTranslation([-0.1956,0.8019,-0.0794])
Shape1502 = Shape()
Shape1502.setUSE("HAnimJointShape")

Transform1501.addChildren(Shape1502)

HAnimSegment1499.addChildren(Transform1501)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring0'/> to <HAnimJoint name='r_ring1'/>
Shape1503 = Shape()
LineSet1504 = LineSet()
LineSet1504.setVertexCount([2])
Coordinate1505 = Coordinate()
Coordinate1505.setPoint([-0.1956,0.8019,-0.0794,-0.1956,0.7815,-0.0794])

LineSet1504.setCoord(Coordinate1505)
ColorRGBA1506 = ColorRGBA()
ColorRGBA1506.setUSE("HAnimSegmentLineColorRGBA")

LineSet1504.setColor(ColorRGBA1506)

Shape1503.setGeometry(LineSet1504)

HAnimSegment1499.addChildren(Shape1503)

HAnimJoint1498.addChildren(HAnimSegment1499)
HAnimJoint1507 = HAnimJoint()
HAnimJoint1507.setName("r_ring1")
HAnimJoint1507.setDEF("hanim_r_ring1")
HAnimJoint1507.setCenter([-0.1956,0.7815,-0.0794])
HAnimJoint1507.setStiffness([0,0,0])
HAnimSegment1508 = HAnimSegment()
HAnimSegment1508.setName("r_ring_proximal")
HAnimSegment1508.setDEF("hanim_r_ring_proximal")
#<HAnimJoint name='r_ring1'/> visualization sphere within <HAnimSegment name='r_ring_proximal'/>
TouchSensor1509 = TouchSensor()
TouchSensor1509.setDescription("HAnimJoint r_ring1, HAnimSegment r_ring_proximal")

HAnimSegment1508.addChildren(TouchSensor1509)
Transform1510 = Transform()
Transform1510.setTranslation([-0.1956,0.7815,-0.0794])
Shape1511 = Shape()
Shape1511.setUSE("HAnimJointShape")

Transform1510.addChildren(Shape1511)

HAnimSegment1508.addChildren(Transform1510)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring1'/> to <HAnimJoint name='r_ring2'/>
Shape1512 = Shape()
LineSet1513 = LineSet()
LineSet1513.setVertexCount([2])
Coordinate1514 = Coordinate()
Coordinate1514.setPoint([-0.1956,0.7815,-0.0794,-0.1973,0.7287,-0.0777])

LineSet1513.setCoord(Coordinate1514)
ColorRGBA1515 = ColorRGBA()
ColorRGBA1515.setUSE("HAnimSegmentLineColorRGBA")

LineSet1513.setColor(ColorRGBA1515)

Shape1512.setGeometry(LineSet1513)

HAnimSegment1508.addChildren(Shape1512)

HAnimJoint1507.addChildren(HAnimSegment1508)
HAnimJoint1516 = HAnimJoint()
HAnimJoint1516.setName("r_ring2")
HAnimJoint1516.setDEF("hanim_r_ring2")
HAnimJoint1516.setCenter([-0.1973,0.7287,-0.0777])
HAnimJoint1516.setStiffness([0,0,0])
HAnimSegment1517 = HAnimSegment()
HAnimSegment1517.setName("r_ring_middle")
HAnimSegment1517.setDEF("hanim_r_ring_middle")
#<HAnimJoint name='r_ring2'/> visualization sphere within <HAnimSegment name='r_ring_middle'/>
TouchSensor1518 = TouchSensor()
TouchSensor1518.setDescription("HAnimJoint r_ring2, HAnimSegment r_ring_middle")

HAnimSegment1517.addChildren(TouchSensor1518)
Transform1519 = Transform()
Transform1519.setTranslation([-0.1973,0.7287,-0.0777])
Shape1520 = Shape()
Shape1520.setUSE("HAnimJointShape")

Transform1519.addChildren(Shape1520)

HAnimSegment1517.addChildren(Transform1519)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring2'/> to <HAnimJoint name='r_ring3'/>
Shape1521 = Shape()
LineSet1522 = LineSet()
LineSet1522.setVertexCount([2])
Coordinate1523 = Coordinate()
Coordinate1523.setPoint([-0.1973,0.7287,-0.0777,-0.1983,0.7045,-0.0767])

LineSet1522.setCoord(Coordinate1523)
ColorRGBA1524 = ColorRGBA()
ColorRGBA1524.setUSE("HAnimSegmentLineColorRGBA")

LineSet1522.setColor(ColorRGBA1524)

Shape1521.setGeometry(LineSet1522)

HAnimSegment1517.addChildren(Shape1521)

HAnimJoint1516.addChildren(HAnimSegment1517)
HAnimJoint1525 = HAnimJoint()
HAnimJoint1525.setName("r_ring3")
HAnimJoint1525.setDEF("hanim_r_ring3")
HAnimJoint1525.setCenter([-0.1983,0.7045,-0.0767])
HAnimJoint1525.setStiffness([0,0,0])
HAnimSegment1526 = HAnimSegment()
HAnimSegment1526.setName("r_ring_distal")
HAnimSegment1526.setDEF("hanim_r_ring_distal")
#<HAnimJoint name='r_ring3'/> visualization sphere within <HAnimSegment name='r_ring_distal'/>
TouchSensor1527 = TouchSensor()
TouchSensor1527.setDescription("HAnimJoint r_ring3, HAnimSegment r_ring_distal")

HAnimSegment1526.addChildren(TouchSensor1527)
Transform1528 = Transform()
Transform1528.setTranslation([-0.1983,0.7045,-0.0767])
Shape1529 = Shape()
Shape1529.setUSE("HAnimJointShape")

Transform1528.addChildren(Shape1529)

HAnimSegment1526.addChildren(Transform1528)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ring3'/> to <HAnimSite name='r_ring_distal_tip'/>
Shape1530 = Shape()
LineSet1531 = LineSet()
LineSet1531.setVertexCount([2])
Coordinate1532 = Coordinate()
Coordinate1532.setPoint([-0.1983,0.7045,-0.0767,-0.1934,0.6778,-0.0693])

LineSet1531.setCoord(Coordinate1532)
ColorRGBA1533 = ColorRGBA()
ColorRGBA1533.setUSE("HAnimSiteLineColorRGBA")

LineSet1531.setColor(ColorRGBA1533)

Shape1530.setGeometry(LineSet1531)

HAnimSegment1526.addChildren(Shape1530)
HAnimSite1534 = HAnimSite()
HAnimSite1534.setName("r_ring_distal_tip")
HAnimSite1534.setDEF("hanim_r_ring_distal_tip")
HAnimSite1534.setTranslation([-0.1934,0.6778,-0.0693])
#HAnimSite visualization shape
TouchSensor1535 = TouchSensor()
TouchSensor1535.setDescription("HAnimSite r_ring_distal_tip")

HAnimSite1534.addChildren(TouchSensor1535)
Shape1536 = Shape()
Shape1536.setUSE("HAnimSiteShape")

HAnimSite1534.addChildren(Shape1536)

HAnimSegment1526.addChildren(HAnimSite1534)

HAnimJoint1525.addChildren(HAnimSegment1526)

HAnimJoint1516.addChildren(HAnimJoint1525)

HAnimJoint1507.addChildren(HAnimJoint1516)

HAnimJoint1498.addChildren(HAnimJoint1507)

HAnimJoint1327.addChildren(HAnimJoint1498)
HAnimJoint1537 = HAnimJoint()
HAnimJoint1537.setName("r_pinky0")
HAnimJoint1537.setDEF("hanim_r_pinky0")
HAnimJoint1537.setCenter([-0.1925,0.8066,-0.1036])
HAnimJoint1537.setStiffness([0,0,0])
HAnimSegment1538 = HAnimSegment()
HAnimSegment1538.setName("r_pinky_metacarpal")
HAnimSegment1538.setDEF("hanim_r_pinky_metacarpal")
#<HAnimJoint name='r_pinky0'/> visualization sphere within <HAnimSegment name='r_pinky_metacarpal'/>
TouchSensor1539 = TouchSensor()
TouchSensor1539.setDescription("HAnimJoint r_pinky0, HAnimSegment r_pinky_metacarpal")

HAnimSegment1538.addChildren(TouchSensor1539)
Transform1540 = Transform()
Transform1540.setTranslation([-0.1925,0.8066,-0.1036])
Shape1541 = Shape()
Shape1541.setUSE("HAnimJointShape")

Transform1540.addChildren(Shape1541)

HAnimSegment1538.addChildren(Transform1540)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky0'/> to <HAnimJoint name='r_pinky1'/>
Shape1542 = Shape()
LineSet1543 = LineSet()
LineSet1543.setVertexCount([2])
Coordinate1544 = Coordinate()
Coordinate1544.setPoint([-0.1925,0.8066,-0.1036,-0.1925,0.7866,-0.1036])

LineSet1543.setCoord(Coordinate1544)
ColorRGBA1545 = ColorRGBA()
ColorRGBA1545.setUSE("HAnimSegmentLineColorRGBA")

LineSet1543.setColor(ColorRGBA1545)

Shape1542.setGeometry(LineSet1543)

HAnimSegment1538.addChildren(Shape1542)

HAnimJoint1537.addChildren(HAnimSegment1538)
HAnimJoint1546 = HAnimJoint()
HAnimJoint1546.setName("r_pinky1")
HAnimJoint1546.setDEF("hanim_r_pinky1")
HAnimJoint1546.setCenter([-0.1925,0.7866,-0.1036])
HAnimJoint1546.setStiffness([0,0,0])
HAnimSegment1547 = HAnimSegment()
HAnimSegment1547.setName("r_pinky_proximal")
HAnimSegment1547.setDEF("hanim_r_pinky_proximal")
#<HAnimJoint name='r_pinky1'/> visualization sphere within <HAnimSegment name='r_pinky_proximal'/>
TouchSensor1548 = TouchSensor()
TouchSensor1548.setDescription("HAnimJoint r_pinky1, HAnimSegment r_pinky_proximal")

HAnimSegment1547.addChildren(TouchSensor1548)
Transform1549 = Transform()
Transform1549.setTranslation([-0.1925,0.7866,-0.1036])
Shape1550 = Shape()
Shape1550.setUSE("HAnimJointShape")

Transform1549.addChildren(Shape1550)

HAnimSegment1547.addChildren(Transform1549)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky1'/> to <HAnimJoint name='r_pinky2'/>
Shape1551 = Shape()
LineSet1552 = LineSet()
LineSet1552.setVertexCount([2])
Coordinate1553 = Coordinate()
Coordinate1553.setPoint([-0.1925,0.7866,-0.1036,-0.1938,0.7452,-0.1024])

LineSet1552.setCoord(Coordinate1553)
ColorRGBA1554 = ColorRGBA()
ColorRGBA1554.setUSE("HAnimSegmentLineColorRGBA")

LineSet1552.setColor(ColorRGBA1554)

Shape1551.setGeometry(LineSet1552)

HAnimSegment1547.addChildren(Shape1551)

HAnimJoint1546.addChildren(HAnimSegment1547)
HAnimJoint1555 = HAnimJoint()
HAnimJoint1555.setName("r_pinky2")
HAnimJoint1555.setDEF("hanim_r_pinky2")
HAnimJoint1555.setCenter([-0.1938,0.7452,-0.1024])
HAnimJoint1555.setStiffness([0,0,0])
HAnimSegment1556 = HAnimSegment()
HAnimSegment1556.setName("r_pinky_middle")
HAnimSegment1556.setDEF("hanim_r_pinky_middle")
#<HAnimJoint name='r_pinky2'/> visualization sphere within <HAnimSegment name='r_pinky_middle'/>
TouchSensor1557 = TouchSensor()
TouchSensor1557.setDescription("HAnimJoint r_pinky2, HAnimSegment r_pinky_middle")

HAnimSegment1556.addChildren(TouchSensor1557)
Transform1558 = Transform()
Transform1558.setTranslation([-0.1938,0.7452,-0.1024])
Shape1559 = Shape()
Shape1559.setUSE("HAnimJointShape")

Transform1558.addChildren(Shape1559)

HAnimSegment1556.addChildren(Transform1558)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky2'/> to <HAnimJoint name='r_pinky3'/>
Shape1560 = Shape()
LineSet1561 = LineSet()
LineSet1561.setVertexCount([2])
Coordinate1562 = Coordinate()
Coordinate1562.setPoint([-0.1938,0.7452,-0.1024,-0.1948,0.7277,-0.1017])

LineSet1561.setCoord(Coordinate1562)
ColorRGBA1563 = ColorRGBA()
ColorRGBA1563.setUSE("HAnimSegmentLineColorRGBA")

LineSet1561.setColor(ColorRGBA1563)

Shape1560.setGeometry(LineSet1561)

HAnimSegment1556.addChildren(Shape1560)

HAnimJoint1555.addChildren(HAnimSegment1556)
HAnimJoint1564 = HAnimJoint()
HAnimJoint1564.setName("r_pinky3")
HAnimJoint1564.setDEF("hanim_r_pinky3")
HAnimJoint1564.setCenter([-0.1948,0.7277,-0.1017])
HAnimJoint1564.setStiffness([0,0,0])
HAnimSegment1565 = HAnimSegment()
HAnimSegment1565.setName("r_pinky_distal")
HAnimSegment1565.setDEF("hanim_r_pinky_distal")
#<HAnimJoint name='r_pinky3'/> visualization sphere within <HAnimSegment name='r_pinky_distal'/>
TouchSensor1566 = TouchSensor()
TouchSensor1566.setDescription("HAnimJoint r_pinky3, HAnimSegment r_pinky_distal")

HAnimSegment1565.addChildren(TouchSensor1566)
Transform1567 = Transform()
Transform1567.setTranslation([-0.1948,0.7277,-0.1017])
Shape1568 = Shape()
Shape1568.setUSE("HAnimJointShape")

Transform1567.addChildren(Shape1568)

HAnimSegment1565.addChildren(Transform1567)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_pinky3'/> to <HAnimSite name='r_pinky_distal_tip'/>
Shape1569 = Shape()
LineSet1570 = LineSet()
LineSet1570.setVertexCount([2])
Coordinate1571 = Coordinate()
Coordinate1571.setPoint([-0.1948,0.7277,-0.1017,-0.1938,0.7035,-0.0949])

LineSet1570.setCoord(Coordinate1571)
ColorRGBA1572 = ColorRGBA()
ColorRGBA1572.setUSE("HAnimSiteLineColorRGBA")

LineSet1570.setColor(ColorRGBA1572)

Shape1569.setGeometry(LineSet1570)

HAnimSegment1565.addChildren(Shape1569)
HAnimSite1573 = HAnimSite()
HAnimSite1573.setName("r_pinky_distal_tip")
HAnimSite1573.setDEF("hanim_r_pinky_distal_tip")
HAnimSite1573.setTranslation([-0.1938,0.7035,-0.0949])
#HAnimSite visualization shape
TouchSensor1574 = TouchSensor()
TouchSensor1574.setDescription("HAnimSite r_pinky_distal_tip")

HAnimSite1573.addChildren(TouchSensor1574)
Shape1575 = Shape()
Shape1575.setUSE("HAnimSiteShape")

HAnimSite1573.addChildren(Shape1575)

HAnimSegment1565.addChildren(HAnimSite1573)

HAnimJoint1564.addChildren(HAnimSegment1565)

HAnimJoint1555.addChildren(HAnimJoint1564)

HAnimJoint1546.addChildren(HAnimJoint1555)

HAnimJoint1537.addChildren(HAnimJoint1546)

HAnimJoint1327.addChildren(HAnimJoint1537)

HAnimJoint1290.addChildren(HAnimJoint1327)

HAnimJoint1274.addChildren(HAnimJoint1290)

HAnimJoint1265.addChildren(HAnimJoint1274)

HAnimJoint1228.addChildren(HAnimJoint1265)

HAnimJoint596.addChildren(HAnimJoint1228)

HAnimJoint587.addChildren(HAnimJoint596)

HAnimJoint578.addChildren(HAnimJoint587)

HAnimJoint569.addChildren(HAnimJoint578)

HAnimJoint560.addChildren(HAnimJoint569)

HAnimJoint551.addChildren(HAnimJoint560)

HAnimJoint542.addChildren(HAnimJoint551)

HAnimJoint533.addChildren(HAnimJoint542)

HAnimJoint510.addChildren(HAnimJoint533)

HAnimJoint494.addChildren(HAnimJoint510)

HAnimJoint485.addChildren(HAnimJoint494)

HAnimJoint476.addChildren(HAnimJoint485)

HAnimJoint467.addChildren(HAnimJoint476)

HAnimJoint437.addChildren(HAnimJoint467)

HAnimJoint428.addChildren(HAnimJoint437)

HAnimJoint419.addChildren(HAnimJoint428)

HAnimJoint396.addChildren(HAnimJoint419)

HAnimJoint46.addChildren(HAnimJoint396)

HAnimHumanoid45.setSkeleton(HAnimJoint46)
#USE nodes for inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes for viewing the humanoid without being affected by body motion
HAnimSite1576 = HAnimSite()
HAnimSite1576.setName("l_inclined_view")
HAnimSite1576.setDEF("hanim_l_inclined_view")
HAnimSite1576.setRotation([-0.113,0.993,0.0347,0.671])
HAnimSite1576.setTranslation([1.62,1.05,2.06])
Viewpoint1577 = Viewpoint()
Viewpoint1577.setDEF("hanim_l_inclined_viewpoint")
Viewpoint1577.setDescription("left inclined")
Viewpoint1577.setPosition([0,0,0])

HAnimSite1576.addChildren(Viewpoint1577)
#HAnimSite/Viewpoint visualization shape
Anchor1578 = Anchor()
Anchor1578.setDescription("HAnimSite Viewpoint hanim_l_inclined_view")
Anchor1578.setUrl(["#hanim_l_inclined_viewpoint"])
LOD1579 = LOD()
LOD1579.setForceTransitions(True)
LOD1579.setRange([0.04])
WorldInfo1580 = WorldInfo()
WorldInfo1580.setInfo(["hide diamond when close"])

LOD1579.addChildren(WorldInfo1580)
Shape1581 = Shape()
Shape1581.setUSE("HAnimSiteViewpointShape")

LOD1579.addChildren(Shape1581)

Anchor1578.addChildren(LOD1579)

HAnimSite1576.addChildren(Anchor1578)

HAnimHumanoid45.addViewpoints(HAnimSite1576)
HAnimSite1582 = HAnimSite()
HAnimSite1582.setName("r_inclined_view")
HAnimSite1582.setDEF("hanim_r_inclined_view")
HAnimSite1582.setRotation([-0.113,-0.993,0.0347,0.671])
HAnimSite1582.setTranslation([-1.62,1.05,2.06])
Viewpoint1583 = Viewpoint()
Viewpoint1583.setDEF("hanim_r_inclined_viewpoint")
Viewpoint1583.setCenterOfRotation([0,0.9,0])
Viewpoint1583.setDescription("right inclined")
Viewpoint1583.setPosition([0,0,0])

HAnimSite1582.addChildren(Viewpoint1583)
#HAnimSite/Viewpoint visualization shape
Anchor1584 = Anchor()
Anchor1584.setDescription("HAnimSite Viewpoint hanim_r_inclined_view")
Anchor1584.setUrl(["#hanim_r_inclined_viewpoint"])
LOD1585 = LOD()
LOD1585.setForceTransitions(True)
LOD1585.setRange([0.04])
WorldInfo1586 = WorldInfo()
WorldInfo1586.setInfo(["hide diamond when close"])

LOD1585.addChildren(WorldInfo1586)
Shape1587 = Shape()
Shape1587.setUSE("HAnimSiteViewpointShape")

LOD1585.addChildren(Shape1587)

Anchor1584.addChildren(LOD1585)

HAnimSite1582.addChildren(Anchor1584)

HAnimHumanoid45.addViewpoints(HAnimSite1582)
HAnimSite1588 = HAnimSite()
HAnimSite1588.setName("front_view")
HAnimSite1588.setDEF("hanim_front_view")
HAnimSite1588.setTranslation([0,0.85,2.58])
Viewpoint1589 = Viewpoint()
Viewpoint1589.setDEF("hanim_front_viewpoint")
Viewpoint1589.setCenterOfRotation([0,0.9,0])
Viewpoint1589.setDescription("front")
Viewpoint1589.setPosition([0,0,0])

HAnimSite1588.addChildren(Viewpoint1589)
#HAnimSite/Viewpoint visualization shape
Anchor1590 = Anchor()
Anchor1590.setDescription("HAnimSite Viewpoint hanim_front_view")
Anchor1590.setUrl(["#hanim_front_viewpoint"])
LOD1591 = LOD()
LOD1591.setForceTransitions(True)
LOD1591.setRange([0.04])
WorldInfo1592 = WorldInfo()
WorldInfo1592.setInfo(["hide diamond when close"])

LOD1591.addChildren(WorldInfo1592)
Shape1593 = Shape()
Shape1593.setUSE("HAnimSiteViewpointShape")

LOD1591.addChildren(Shape1593)

Anchor1590.addChildren(LOD1591)

HAnimSite1588.addChildren(Anchor1590)

HAnimHumanoid45.addViewpoints(HAnimSite1588)
HAnimSite1594 = HAnimSite()
HAnimSite1594.setName("back_view")
HAnimSite1594.setDEF("hanim_back_view")
HAnimSite1594.setRotation([0,1,0,3.14])
HAnimSite1594.setTranslation([0,0.85,-2.58])
Viewpoint1595 = Viewpoint()
Viewpoint1595.setDEF("hanim_back_viewpoint")
Viewpoint1595.setCenterOfRotation([0,0.9,0])
Viewpoint1595.setDescription("back")
Viewpoint1595.setPosition([0,0,0])

HAnimSite1594.addChildren(Viewpoint1595)
#HAnimSite/Viewpoint visualization shape
Anchor1596 = Anchor()
Anchor1596.setDescription("HAnimSite Viewpoint hanim_back_view")
Anchor1596.setUrl(["#hanim_back_viewpoint"])
LOD1597 = LOD()
LOD1597.setForceTransitions(True)
LOD1597.setRange([0.04])
WorldInfo1598 = WorldInfo()
WorldInfo1598.setInfo(["hide diamond when close"])

LOD1597.addChildren(WorldInfo1598)
Shape1599 = Shape()
Shape1599.setUSE("HAnimSiteViewpointShape")

LOD1597.addChildren(Shape1599)

Anchor1596.addChildren(LOD1597)

HAnimSite1594.addChildren(Anchor1596)

HAnimHumanoid45.addViewpoints(HAnimSite1594)
HAnimSite1600 = HAnimSite()
HAnimSite1600.setName("l_side_view")
HAnimSite1600.setDEF("hanim_l_side_view")
HAnimSite1600.setRotation([0,1,0,1.5708])
HAnimSite1600.setTranslation([2.6,0.854,0])
Viewpoint1601 = Viewpoint()
Viewpoint1601.setDEF("hanim_l_side_viewpoint")
Viewpoint1601.setCenterOfRotation([0,0.9,0])
Viewpoint1601.setDescription("left side")
Viewpoint1601.setPosition([0,0,0])

HAnimSite1600.addChildren(Viewpoint1601)
#HAnimSite/Viewpoint visualization shape
Anchor1602 = Anchor()
Anchor1602.setDescription("HAnimSite Viewpoint hanim_l_side_view")
Anchor1602.setUrl(["#hanim_l_side_viewpoint"])
LOD1603 = LOD()
LOD1603.setForceTransitions(True)
LOD1603.setRange([0.04])
WorldInfo1604 = WorldInfo()
WorldInfo1604.setInfo(["hide diamond when close"])

LOD1603.addChildren(WorldInfo1604)
Shape1605 = Shape()
Shape1605.setUSE("HAnimSiteViewpointShape")

LOD1603.addChildren(Shape1605)

Anchor1602.addChildren(LOD1603)

HAnimSite1600.addChildren(Anchor1602)

HAnimHumanoid45.addViewpoints(HAnimSite1600)
HAnimSite1606 = HAnimSite()
HAnimSite1606.setName("Top_view")
HAnimSite1606.setDEF("hanim_Top_view")
HAnimSite1606.setRotation([1,0,0,-1.57])
HAnimSite1606.setTranslation([0,3.5,0])
Viewpoint1607 = Viewpoint()
Viewpoint1607.setDEF("hanim_Top_viewpoint")
Viewpoint1607.setCenterOfRotation([0,0.9,0])
Viewpoint1607.setDescription("Top")
Viewpoint1607.setPosition([0,0,0])

HAnimSite1606.addChildren(Viewpoint1607)
#HAnimSite/Viewpoint visualization shape
Anchor1608 = Anchor()
Anchor1608.setDescription("HAnimSite Viewpoint hanim_Top_view")
Anchor1608.setUrl(["#hanim_Top_viewpoint"])
LOD1609 = LOD()
LOD1609.setForceTransitions(True)
LOD1609.setRange([0.04])
WorldInfo1610 = WorldInfo()
WorldInfo1610.setInfo(["hide diamond when close"])

LOD1609.addChildren(WorldInfo1610)
Shape1611 = Shape()
Shape1611.setUSE("HAnimSiteViewpointShape")

LOD1609.addChildren(Shape1611)

Anchor1608.addChildren(LOD1609)

HAnimSite1606.addChildren(Anchor1608)

HAnimHumanoid45.addViewpoints(HAnimSite1606)
HAnimSite1612 = HAnimSite()
HAnimSite1612.setName("front_close_view")
HAnimSite1612.setDEF("hanim_front_close_view")
HAnimSite1612.setTranslation([0,0.854,1.575])
Viewpoint1613 = Viewpoint()
Viewpoint1613.setDEF("hanim_front_close_viewpoint")
Viewpoint1613.setCenterOfRotation([0,0,1.575])
Viewpoint1613.setDescription("front close")
Viewpoint1613.setPosition([0,0,0])

HAnimSite1612.addChildren(Viewpoint1613)
#HAnimSite/Viewpoint visualization shape
Anchor1614 = Anchor()
Anchor1614.setDescription("HAnimSite Viewpoint hanim_front_close_view")
Anchor1614.setUrl(["#hanim_front_close_viewpoint"])
LOD1615 = LOD()
LOD1615.setForceTransitions(True)
LOD1615.setRange([0.04])
WorldInfo1616 = WorldInfo()
WorldInfo1616.setInfo(["hide diamond when close"])

LOD1615.addChildren(WorldInfo1616)
Shape1617 = Shape()
Shape1617.setUSE("HAnimSiteViewpointShape")

LOD1615.addChildren(Shape1617)

Anchor1614.addChildren(LOD1615)

HAnimSite1612.addChildren(Anchor1614)

HAnimHumanoid45.addViewpoints(HAnimSite1612)
HAnimSite1618 = HAnimSite()
HAnimSite1618.setName("side_close_view")
HAnimSite1618.setDEF("hanim_side_close_view")
HAnimSite1618.setRotation([0,1,0,1.5708])
HAnimSite1618.setTranslation([1.56,0.854,0])
Viewpoint1619 = Viewpoint()
Viewpoint1619.setDEF("hanim_side_close_viewpoint")
Viewpoint1619.setCenterOfRotation([1.6,0,0])
Viewpoint1619.setDescription("side close")
Viewpoint1619.setPosition([0,0,0])

HAnimSite1618.addChildren(Viewpoint1619)
#HAnimSite/Viewpoint visualization shape
Anchor1620 = Anchor()
Anchor1620.setDescription("HAnimSite Viewpoint hanim_side_close_view")
Anchor1620.setUrl(["#hanim_side_close_viewpoint"])
LOD1621 = LOD()
LOD1621.setForceTransitions(True)
LOD1621.setRange([0.04])
WorldInfo1622 = WorldInfo()
WorldInfo1622.setInfo(["hide diamond when close"])

LOD1621.addChildren(WorldInfo1622)
Shape1623 = Shape()
Shape1623.setUSE("HAnimSiteViewpointShape")

LOD1621.addChildren(Shape1623)

Anchor1620.addChildren(LOD1621)

HAnimSite1618.addChildren(Anchor1620)

HAnimHumanoid45.addViewpoints(HAnimSite1618)
HAnimSite1624 = HAnimSite()
HAnimSite1624.setName("head_front_close_view")
HAnimSite1624.setDEF("hanim_head_front_close_view")
HAnimSite1624.setTranslation([0,1.5,1])
Viewpoint1625 = Viewpoint()
Viewpoint1625.setDEF("hanim_head_front_close_viewpoint")
Viewpoint1625.setCenterOfRotation([0,0,1])
Viewpoint1625.setDescription("head front close")
Viewpoint1625.setPosition([0,0,0])

HAnimSite1624.addChildren(Viewpoint1625)
#HAnimSite/Viewpoint visualization shape
Anchor1626 = Anchor()
Anchor1626.setDescription("HAnimSite Viewpoint hanim_head_front_close_view")
Anchor1626.setUrl(["#hanim_head_front_close_viewpoint"])
LOD1627 = LOD()
LOD1627.setForceTransitions(True)
LOD1627.setRange([0.04])
WorldInfo1628 = WorldInfo()
WorldInfo1628.setInfo(["hide diamond when close"])

LOD1627.addChildren(WorldInfo1628)
Shape1629 = Shape()
Shape1629.setUSE("HAnimSiteViewpointShape")

LOD1627.addChildren(Shape1629)

Anchor1626.addChildren(LOD1627)

HAnimSite1624.addChildren(Anchor1626)

HAnimHumanoid45.addViewpoints(HAnimSite1624)
HAnimSite1630 = HAnimSite()
HAnimSite1630.setName("chest_front_close_view")
HAnimSite1630.setDEF("hanim_chest_front_close_view")
HAnimSite1630.setTranslation([0,1.2,1])
Viewpoint1631 = Viewpoint()
Viewpoint1631.setDEF("hanim_chest_front_close_viewpoint")
Viewpoint1631.setCenterOfRotation([0,0,1])
Viewpoint1631.setDescription("chest front close")
Viewpoint1631.setPosition([0,0,0])

HAnimSite1630.addChildren(Viewpoint1631)
#HAnimSite/Viewpoint visualization shape
Anchor1632 = Anchor()
Anchor1632.setDescription("HAnimSite Viewpoint hanim_chest_front_close_view")
Anchor1632.setUrl(["#hanim_chest_front_close_viewpoint"])
LOD1633 = LOD()
LOD1633.setForceTransitions(True)
LOD1633.setRange([0.04])
WorldInfo1634 = WorldInfo()
WorldInfo1634.setInfo(["hide diamond when close"])

LOD1633.addChildren(WorldInfo1634)
Shape1635 = Shape()
Shape1635.setUSE("HAnimSiteViewpointShape")

LOD1633.addChildren(Shape1635)

Anchor1632.addChildren(LOD1633)

HAnimSite1630.addChildren(Anchor1632)

HAnimHumanoid45.addViewpoints(HAnimSite1630)
HAnimSite1636 = HAnimSite()
HAnimSite1636.setName("pelvis_front_close_view")
HAnimSite1636.setDEF("hanim_pelvis_front_close_view")
HAnimSite1636.setTranslation([0,0.8,1])
Viewpoint1637 = Viewpoint()
Viewpoint1637.setDEF("hanim_pelvis_front_close_viewpoint")
Viewpoint1637.setCenterOfRotation([0,0,1])
Viewpoint1637.setDescription("pelvis front close")
Viewpoint1637.setPosition([0,0,0])

HAnimSite1636.addChildren(Viewpoint1637)
#HAnimSite/Viewpoint visualization shape
Anchor1638 = Anchor()
Anchor1638.setDescription("HAnimSite Viewpoint hanim_pelvis_front_close_view")
Anchor1638.setUrl(["#hanim_pelvis_front_close_viewpoint"])
LOD1639 = LOD()
LOD1639.setForceTransitions(True)
LOD1639.setRange([0.04])
WorldInfo1640 = WorldInfo()
WorldInfo1640.setInfo(["hide diamond when close"])

LOD1639.addChildren(WorldInfo1640)
Shape1641 = Shape()
Shape1641.setUSE("HAnimSiteViewpointShape")

LOD1639.addChildren(Shape1641)

Anchor1638.addChildren(LOD1639)

HAnimSite1636.addChildren(Anchor1638)

HAnimHumanoid45.addViewpoints(HAnimSite1636)
HAnimSite1642 = HAnimSite()
HAnimSite1642.setName("knees_front_close_view")
HAnimSite1642.setDEF("hanim_knees_front_close_view")
HAnimSite1642.setTranslation([0,0.4,1])
Viewpoint1643 = Viewpoint()
Viewpoint1643.setDEF("hanim_knees_front_close_viewpoint")
Viewpoint1643.setCenterOfRotation([0,0.4,0])
Viewpoint1643.setDescription("knees front close")
Viewpoint1643.setPosition([0,0,0])

HAnimSite1642.addChildren(Viewpoint1643)
#HAnimSite/Viewpoint visualization shape
Anchor1644 = Anchor()
Anchor1644.setDescription("HAnimSite Viewpoint hanim_knees_front_close_view")
Anchor1644.setUrl(["#hanim_knees_front_close_viewpoint"])
LOD1645 = LOD()
LOD1645.setForceTransitions(True)
LOD1645.setRange([0.04])
WorldInfo1646 = WorldInfo()
WorldInfo1646.setInfo(["hide diamond when close"])

LOD1645.addChildren(WorldInfo1646)
Shape1647 = Shape()
Shape1647.setUSE("HAnimSiteViewpointShape")

LOD1645.addChildren(Shape1647)

Anchor1644.addChildren(LOD1645)

HAnimSite1642.addChildren(Anchor1644)

HAnimHumanoid45.addViewpoints(HAnimSite1642)
HAnimSite1648 = HAnimSite()
HAnimSite1648.setName("feet_front_close_view")
HAnimSite1648.setDEF("hanim_feet_front_close_view")
HAnimSite1648.setTranslation([0,0,1])
Viewpoint1649 = Viewpoint()
Viewpoint1649.setDEF("hanim_feet_front_close_viewpoint")
Viewpoint1649.setDescription("feet front close")
Viewpoint1649.setPosition([0,0,0])

HAnimSite1648.addChildren(Viewpoint1649)
#HAnimSite/Viewpoint visualization shape
Anchor1650 = Anchor()
Anchor1650.setDescription("HAnimSite Viewpoint hanim_feet_front_close_view")
Anchor1650.setUrl(["#hanim_feet_front_close_viewpoint"])
LOD1651 = LOD()
LOD1651.setForceTransitions(True)
LOD1651.setRange([0.04])
WorldInfo1652 = WorldInfo()
WorldInfo1652.setInfo(["hide diamond when close"])

LOD1651.addChildren(WorldInfo1652)
Shape1653 = Shape()
Shape1653.setUSE("HAnimSiteViewpointShape")

LOD1651.addChildren(Shape1653)

Anchor1650.addChildren(LOD1651)

HAnimSite1648.addChildren(Anchor1650)

HAnimHumanoid45.addViewpoints(HAnimSite1648)
HAnimSite1654 = HAnimSite()
HAnimSite1654.setName("eye_level_view")
HAnimSite1654.setDEF("hanim_eye_level_view")
HAnimSite1654.setTranslation([0,1.6332,0.0502])
Viewpoint1655 = Viewpoint()
Viewpoint1655.setDEF("hanim_eye_level_viewpoint")
Viewpoint1655.setDescription("eye level looking forward")
Viewpoint1655.setOrientation([0,1,0,3.141593])
Viewpoint1655.setPosition([0,0,0])

HAnimSite1654.addChildren(Viewpoint1655)
#HAnimSite/Viewpoint visualization shape
Anchor1656 = Anchor()
Anchor1656.setDescription("HAnimSite Viewpoint hanim_eye_level_view")
Anchor1656.setUrl(["#hanim_eye_level_viewpoint"])
LOD1657 = LOD()
LOD1657.setForceTransitions(True)
LOD1657.setRange([0.04])
WorldInfo1658 = WorldInfo()
WorldInfo1658.setInfo(["hide diamond when close"])

LOD1657.addChildren(WorldInfo1658)
Shape1659 = Shape()
Shape1659.setUSE("HAnimSiteViewpointShape")

LOD1657.addChildren(Shape1659)

Anchor1656.addChildren(LOD1657)

HAnimSite1654.addChildren(Anchor1656)

HAnimHumanoid45.addViewpoints(HAnimSite1654)
HAnimSite1660 = HAnimSite()
HAnimSite1660.setUSE("hanim_l_eyeball_site_view")

HAnimHumanoid45.addSites(HAnimSite1660)
HAnimSite1661 = HAnimSite()
HAnimSite1661.setUSE("hanim_r_eyeball_site_view")

HAnimHumanoid45.addSites(HAnimSite1661)
HAnimSite1662 = HAnimSite()
HAnimSite1662.setUSE("hanim_l_hand_front_view")

HAnimHumanoid45.addSites(HAnimSite1662)
HAnimSite1663 = HAnimSite()
HAnimSite1663.setUSE("hanim_r_hand_front_view")

HAnimHumanoid45.addSites(HAnimSite1663)
HAnimJoint1664 = HAnimJoint()
HAnimJoint1664.setUSE("hanim_humanoid_root")

HAnimHumanoid45.addJoints(HAnimJoint1664)
HAnimJoint1665 = HAnimJoint()
HAnimJoint1665.setUSE("hanim_sacroiliac")

HAnimHumanoid45.addJoints(HAnimJoint1665)
HAnimJoint1666 = HAnimJoint()
HAnimJoint1666.setUSE("hanim_vl5")

HAnimHumanoid45.addJoints(HAnimJoint1666)
HAnimJoint1667 = HAnimJoint()
HAnimJoint1667.setUSE("hanim_vl4")

HAnimHumanoid45.addJoints(HAnimJoint1667)
HAnimJoint1668 = HAnimJoint()
HAnimJoint1668.setUSE("hanim_vl3")

HAnimHumanoid45.addJoints(HAnimJoint1668)
HAnimJoint1669 = HAnimJoint()
HAnimJoint1669.setUSE("hanim_vl2")

HAnimHumanoid45.addJoints(HAnimJoint1669)
HAnimJoint1670 = HAnimJoint()
HAnimJoint1670.setUSE("hanim_vl1")

HAnimHumanoid45.addJoints(HAnimJoint1670)
HAnimJoint1671 = HAnimJoint()
HAnimJoint1671.setUSE("hanim_vt12")

HAnimHumanoid45.addJoints(HAnimJoint1671)
HAnimJoint1672 = HAnimJoint()
HAnimJoint1672.setUSE("hanim_vt11")

HAnimHumanoid45.addJoints(HAnimJoint1672)
HAnimJoint1673 = HAnimJoint()
HAnimJoint1673.setUSE("hanim_vt10")

HAnimHumanoid45.addJoints(HAnimJoint1673)
HAnimJoint1674 = HAnimJoint()
HAnimJoint1674.setUSE("hanim_vt9")

HAnimHumanoid45.addJoints(HAnimJoint1674)
HAnimJoint1675 = HAnimJoint()
HAnimJoint1675.setUSE("hanim_vt8")

HAnimHumanoid45.addJoints(HAnimJoint1675)
HAnimJoint1676 = HAnimJoint()
HAnimJoint1676.setUSE("hanim_vt7")

HAnimHumanoid45.addJoints(HAnimJoint1676)
HAnimJoint1677 = HAnimJoint()
HAnimJoint1677.setUSE("hanim_vt6")

HAnimHumanoid45.addJoints(HAnimJoint1677)
HAnimJoint1678 = HAnimJoint()
HAnimJoint1678.setUSE("hanim_vt5")

HAnimHumanoid45.addJoints(HAnimJoint1678)
HAnimJoint1679 = HAnimJoint()
HAnimJoint1679.setUSE("hanim_vt4")

HAnimHumanoid45.addJoints(HAnimJoint1679)
HAnimJoint1680 = HAnimJoint()
HAnimJoint1680.setUSE("hanim_vt3")

HAnimHumanoid45.addJoints(HAnimJoint1680)
HAnimJoint1681 = HAnimJoint()
HAnimJoint1681.setUSE("hanim_vt2")

HAnimHumanoid45.addJoints(HAnimJoint1681)
HAnimJoint1682 = HAnimJoint()
HAnimJoint1682.setUSE("hanim_vt1")

HAnimHumanoid45.addJoints(HAnimJoint1682)
HAnimJoint1683 = HAnimJoint()
HAnimJoint1683.setUSE("hanim_vc7")

HAnimHumanoid45.addJoints(HAnimJoint1683)
HAnimJoint1684 = HAnimJoint()
HAnimJoint1684.setUSE("hanim_vc6")

HAnimHumanoid45.addJoints(HAnimJoint1684)
HAnimJoint1685 = HAnimJoint()
HAnimJoint1685.setUSE("hanim_vc5")

HAnimHumanoid45.addJoints(HAnimJoint1685)
HAnimJoint1686 = HAnimJoint()
HAnimJoint1686.setUSE("hanim_vc4")

HAnimHumanoid45.addJoints(HAnimJoint1686)
HAnimJoint1687 = HAnimJoint()
HAnimJoint1687.setUSE("hanim_vc3")

HAnimHumanoid45.addJoints(HAnimJoint1687)
HAnimJoint1688 = HAnimJoint()
HAnimJoint1688.setUSE("hanim_vc2")

HAnimHumanoid45.addJoints(HAnimJoint1688)
HAnimJoint1689 = HAnimJoint()
HAnimJoint1689.setUSE("hanim_vc1")

HAnimHumanoid45.addJoints(HAnimJoint1689)
HAnimJoint1690 = HAnimJoint()
HAnimJoint1690.setUSE("hanim_skullbase")

HAnimHumanoid45.addJoints(HAnimJoint1690)
HAnimJoint1691 = HAnimJoint()
HAnimJoint1691.setUSE("hanim_temporomandibular")

HAnimHumanoid45.addJoints(HAnimJoint1691)
HAnimJoint1692 = HAnimJoint()
HAnimJoint1692.setUSE("hanim_l_acromioclavicular")

HAnimHumanoid45.addJoints(HAnimJoint1692)
HAnimJoint1693 = HAnimJoint()
HAnimJoint1693.setUSE("hanim_r_acromioclavicular")

HAnimHumanoid45.addJoints(HAnimJoint1693)
HAnimJoint1694 = HAnimJoint()
HAnimJoint1694.setUSE("hanim_l_ankle")

HAnimHumanoid45.addJoints(HAnimJoint1694)
HAnimJoint1695 = HAnimJoint()
HAnimJoint1695.setUSE("hanim_r_ankle")

HAnimHumanoid45.addJoints(HAnimJoint1695)
HAnimJoint1696 = HAnimJoint()
HAnimJoint1696.setUSE("hanim_l_elbow")

HAnimHumanoid45.addJoints(HAnimJoint1696)
HAnimJoint1697 = HAnimJoint()
HAnimJoint1697.setUSE("hanim_r_elbow")

HAnimHumanoid45.addJoints(HAnimJoint1697)
HAnimJoint1698 = HAnimJoint()
HAnimJoint1698.setUSE("hanim_l_eyeball_joint")

HAnimHumanoid45.addJoints(HAnimJoint1698)
HAnimJoint1699 = HAnimJoint()
HAnimJoint1699.setUSE("hanim_r_eyeball_joint")

HAnimHumanoid45.addJoints(HAnimJoint1699)
HAnimJoint1700 = HAnimJoint()
HAnimJoint1700.setUSE("hanim_l_eyebrow_joint")

HAnimHumanoid45.addJoints(HAnimJoint1700)
HAnimJoint1701 = HAnimJoint()
HAnimJoint1701.setUSE("hanim_r_eyebrow_joint")

HAnimHumanoid45.addJoints(HAnimJoint1701)
HAnimJoint1702 = HAnimJoint()
HAnimJoint1702.setUSE("hanim_l_eyelid_joint")

HAnimHumanoid45.addJoints(HAnimJoint1702)
HAnimJoint1703 = HAnimJoint()
HAnimJoint1703.setUSE("hanim_r_eyelid_joint")

HAnimHumanoid45.addJoints(HAnimJoint1703)
HAnimJoint1704 = HAnimJoint()
HAnimJoint1704.setUSE("hanim_l_hip")

HAnimHumanoid45.addJoints(HAnimJoint1704)
HAnimJoint1705 = HAnimJoint()
HAnimJoint1705.setUSE("hanim_r_hip")

HAnimHumanoid45.addJoints(HAnimJoint1705)
HAnimJoint1706 = HAnimJoint()
HAnimJoint1706.setUSE("hanim_l_index0")

HAnimHumanoid45.addJoints(HAnimJoint1706)
HAnimJoint1707 = HAnimJoint()
HAnimJoint1707.setUSE("hanim_r_index0")

HAnimHumanoid45.addJoints(HAnimJoint1707)
HAnimJoint1708 = HAnimJoint()
HAnimJoint1708.setUSE("hanim_l_index1")

HAnimHumanoid45.addJoints(HAnimJoint1708)
HAnimJoint1709 = HAnimJoint()
HAnimJoint1709.setUSE("hanim_r_index1")

HAnimHumanoid45.addJoints(HAnimJoint1709)
HAnimJoint1710 = HAnimJoint()
HAnimJoint1710.setUSE("hanim_l_index2")

HAnimHumanoid45.addJoints(HAnimJoint1710)
HAnimJoint1711 = HAnimJoint()
HAnimJoint1711.setUSE("hanim_r_index2")

HAnimHumanoid45.addJoints(HAnimJoint1711)
HAnimJoint1712 = HAnimJoint()
HAnimJoint1712.setUSE("hanim_l_index3")

HAnimHumanoid45.addJoints(HAnimJoint1712)
HAnimJoint1713 = HAnimJoint()
HAnimJoint1713.setUSE("hanim_r_index3")

HAnimHumanoid45.addJoints(HAnimJoint1713)
HAnimJoint1714 = HAnimJoint()
HAnimJoint1714.setUSE("hanim_l_knee")

HAnimHumanoid45.addJoints(HAnimJoint1714)
HAnimJoint1715 = HAnimJoint()
HAnimJoint1715.setUSE("hanim_r_knee")

HAnimHumanoid45.addJoints(HAnimJoint1715)
HAnimJoint1716 = HAnimJoint()
HAnimJoint1716.setUSE("hanim_l_metatarsal")

HAnimHumanoid45.addJoints(HAnimJoint1716)
HAnimJoint1717 = HAnimJoint()
HAnimJoint1717.setUSE("hanim_r_metatarsal")

HAnimHumanoid45.addJoints(HAnimJoint1717)
HAnimJoint1718 = HAnimJoint()
HAnimJoint1718.setUSE("hanim_l_middle0")

HAnimHumanoid45.addJoints(HAnimJoint1718)
HAnimJoint1719 = HAnimJoint()
HAnimJoint1719.setUSE("hanim_r_middle0")

HAnimHumanoid45.addJoints(HAnimJoint1719)
HAnimJoint1720 = HAnimJoint()
HAnimJoint1720.setUSE("hanim_l_middle1")

HAnimHumanoid45.addJoints(HAnimJoint1720)
HAnimJoint1721 = HAnimJoint()
HAnimJoint1721.setUSE("hanim_r_middle1")

HAnimHumanoid45.addJoints(HAnimJoint1721)
HAnimJoint1722 = HAnimJoint()
HAnimJoint1722.setUSE("hanim_l_middle2")

HAnimHumanoid45.addJoints(HAnimJoint1722)
HAnimJoint1723 = HAnimJoint()
HAnimJoint1723.setUSE("hanim_r_middle2")

HAnimHumanoid45.addJoints(HAnimJoint1723)
HAnimJoint1724 = HAnimJoint()
HAnimJoint1724.setUSE("hanim_l_middle3")

HAnimHumanoid45.addJoints(HAnimJoint1724)
HAnimJoint1725 = HAnimJoint()
HAnimJoint1725.setUSE("hanim_r_middle3")

HAnimHumanoid45.addJoints(HAnimJoint1725)
HAnimJoint1726 = HAnimJoint()
HAnimJoint1726.setUSE("hanim_l_midtarsal")

HAnimHumanoid45.addJoints(HAnimJoint1726)
HAnimJoint1727 = HAnimJoint()
HAnimJoint1727.setUSE("hanim_r_midtarsal")

HAnimHumanoid45.addJoints(HAnimJoint1727)
HAnimJoint1728 = HAnimJoint()
HAnimJoint1728.setUSE("hanim_l_pinky0")

HAnimHumanoid45.addJoints(HAnimJoint1728)
HAnimJoint1729 = HAnimJoint()
HAnimJoint1729.setUSE("hanim_r_pinky0")

HAnimHumanoid45.addJoints(HAnimJoint1729)
HAnimJoint1730 = HAnimJoint()
HAnimJoint1730.setUSE("hanim_l_pinky1")

HAnimHumanoid45.addJoints(HAnimJoint1730)
HAnimJoint1731 = HAnimJoint()
HAnimJoint1731.setUSE("hanim_r_pinky1")

HAnimHumanoid45.addJoints(HAnimJoint1731)
HAnimJoint1732 = HAnimJoint()
HAnimJoint1732.setUSE("hanim_l_pinky2")

HAnimHumanoid45.addJoints(HAnimJoint1732)
HAnimJoint1733 = HAnimJoint()
HAnimJoint1733.setUSE("hanim_r_pinky2")

HAnimHumanoid45.addJoints(HAnimJoint1733)
HAnimJoint1734 = HAnimJoint()
HAnimJoint1734.setUSE("hanim_l_pinky3")

HAnimHumanoid45.addJoints(HAnimJoint1734)
HAnimJoint1735 = HAnimJoint()
HAnimJoint1735.setUSE("hanim_r_pinky3")

HAnimHumanoid45.addJoints(HAnimJoint1735)
HAnimJoint1736 = HAnimJoint()
HAnimJoint1736.setUSE("hanim_l_ring0")

HAnimHumanoid45.addJoints(HAnimJoint1736)
HAnimJoint1737 = HAnimJoint()
HAnimJoint1737.setUSE("hanim_r_ring0")

HAnimHumanoid45.addJoints(HAnimJoint1737)
HAnimJoint1738 = HAnimJoint()
HAnimJoint1738.setUSE("hanim_l_ring1")

HAnimHumanoid45.addJoints(HAnimJoint1738)
HAnimJoint1739 = HAnimJoint()
HAnimJoint1739.setUSE("hanim_r_ring1")

HAnimHumanoid45.addJoints(HAnimJoint1739)
HAnimJoint1740 = HAnimJoint()
HAnimJoint1740.setUSE("hanim_l_ring2")

HAnimHumanoid45.addJoints(HAnimJoint1740)
HAnimJoint1741 = HAnimJoint()
HAnimJoint1741.setUSE("hanim_r_ring2")

HAnimHumanoid45.addJoints(HAnimJoint1741)
HAnimJoint1742 = HAnimJoint()
HAnimJoint1742.setUSE("hanim_l_ring3")

HAnimHumanoid45.addJoints(HAnimJoint1742)
HAnimJoint1743 = HAnimJoint()
HAnimJoint1743.setUSE("hanim_r_ring3")

HAnimHumanoid45.addJoints(HAnimJoint1743)
HAnimJoint1744 = HAnimJoint()
HAnimJoint1744.setUSE("hanim_l_shoulder")

HAnimHumanoid45.addJoints(HAnimJoint1744)
HAnimJoint1745 = HAnimJoint()
HAnimJoint1745.setUSE("hanim_r_shoulder")

HAnimHumanoid45.addJoints(HAnimJoint1745)
HAnimJoint1746 = HAnimJoint()
HAnimJoint1746.setUSE("hanim_l_sternoclavicular")

HAnimHumanoid45.addJoints(HAnimJoint1746)
HAnimJoint1747 = HAnimJoint()
HAnimJoint1747.setUSE("hanim_r_sternoclavicular")

HAnimHumanoid45.addJoints(HAnimJoint1747)
HAnimJoint1748 = HAnimJoint()
HAnimJoint1748.setUSE("hanim_l_subtalar")

HAnimHumanoid45.addJoints(HAnimJoint1748)
HAnimJoint1749 = HAnimJoint()
HAnimJoint1749.setUSE("hanim_r_subtalar")

HAnimHumanoid45.addJoints(HAnimJoint1749)
HAnimJoint1750 = HAnimJoint()
HAnimJoint1750.setUSE("hanim_l_thumb1")

HAnimHumanoid45.addJoints(HAnimJoint1750)
HAnimJoint1751 = HAnimJoint()
HAnimJoint1751.setUSE("hanim_r_thumb1")

HAnimHumanoid45.addJoints(HAnimJoint1751)
HAnimJoint1752 = HAnimJoint()
HAnimJoint1752.setUSE("hanim_l_thumb2")

HAnimHumanoid45.addJoints(HAnimJoint1752)
HAnimJoint1753 = HAnimJoint()
HAnimJoint1753.setUSE("hanim_r_thumb2")

HAnimHumanoid45.addJoints(HAnimJoint1753)
HAnimJoint1754 = HAnimJoint()
HAnimJoint1754.setUSE("hanim_l_thumb3")

HAnimHumanoid45.addJoints(HAnimJoint1754)
HAnimJoint1755 = HAnimJoint()
HAnimJoint1755.setUSE("hanim_r_thumb3")

HAnimHumanoid45.addJoints(HAnimJoint1755)
HAnimJoint1756 = HAnimJoint()
HAnimJoint1756.setUSE("hanim_l_wrist")

HAnimHumanoid45.addJoints(HAnimJoint1756)
HAnimJoint1757 = HAnimJoint()
HAnimJoint1757.setUSE("hanim_r_wrist")

HAnimHumanoid45.addJoints(HAnimJoint1757)
HAnimSegment1758 = HAnimSegment()
HAnimSegment1758.setUSE("hanim_pelvis")

HAnimHumanoid45.addSegments(HAnimSegment1758)
HAnimSegment1759 = HAnimSegment()
HAnimSegment1759.setUSE("hanim_skull")

HAnimHumanoid45.addSegments(HAnimSegment1759)
HAnimSegment1760 = HAnimSegment()
HAnimSegment1760.setUSE("hanim_jaw")

HAnimHumanoid45.addSegments(HAnimSegment1760)
HAnimSegment1761 = HAnimSegment()
HAnimSegment1761.setUSE("hanim_c1")

HAnimHumanoid45.addSegments(HAnimSegment1761)
HAnimSegment1762 = HAnimSegment()
HAnimSegment1762.setUSE("hanim_c2")

HAnimHumanoid45.addSegments(HAnimSegment1762)
HAnimSegment1763 = HAnimSegment()
HAnimSegment1763.setUSE("hanim_c3")

HAnimHumanoid45.addSegments(HAnimSegment1763)
HAnimSegment1764 = HAnimSegment()
HAnimSegment1764.setUSE("hanim_c4")

HAnimHumanoid45.addSegments(HAnimSegment1764)
HAnimSegment1765 = HAnimSegment()
HAnimSegment1765.setUSE("hanim_c5")

HAnimHumanoid45.addSegments(HAnimSegment1765)
HAnimSegment1766 = HAnimSegment()
HAnimSegment1766.setUSE("hanim_c6")

HAnimHumanoid45.addSegments(HAnimSegment1766)
HAnimSegment1767 = HAnimSegment()
HAnimSegment1767.setUSE("hanim_c7")

HAnimHumanoid45.addSegments(HAnimSegment1767)
HAnimSegment1768 = HAnimSegment()
HAnimSegment1768.setUSE("hanim_t1")

HAnimHumanoid45.addSegments(HAnimSegment1768)
HAnimSegment1769 = HAnimSegment()
HAnimSegment1769.setUSE("hanim_t2")

HAnimHumanoid45.addSegments(HAnimSegment1769)
HAnimSegment1770 = HAnimSegment()
HAnimSegment1770.setUSE("hanim_t3")

HAnimHumanoid45.addSegments(HAnimSegment1770)
HAnimSegment1771 = HAnimSegment()
HAnimSegment1771.setUSE("hanim_t4")

HAnimHumanoid45.addSegments(HAnimSegment1771)
HAnimSegment1772 = HAnimSegment()
HAnimSegment1772.setUSE("hanim_t5")

HAnimHumanoid45.addSegments(HAnimSegment1772)
HAnimSegment1773 = HAnimSegment()
HAnimSegment1773.setUSE("hanim_t6")

HAnimHumanoid45.addSegments(HAnimSegment1773)
HAnimSegment1774 = HAnimSegment()
HAnimSegment1774.setUSE("hanim_t7")

HAnimHumanoid45.addSegments(HAnimSegment1774)
HAnimSegment1775 = HAnimSegment()
HAnimSegment1775.setUSE("hanim_t8")

HAnimHumanoid45.addSegments(HAnimSegment1775)
HAnimSegment1776 = HAnimSegment()
HAnimSegment1776.setUSE("hanim_t9")

HAnimHumanoid45.addSegments(HAnimSegment1776)
HAnimSegment1777 = HAnimSegment()
HAnimSegment1777.setUSE("hanim_t10")

HAnimHumanoid45.addSegments(HAnimSegment1777)
HAnimSegment1778 = HAnimSegment()
HAnimSegment1778.setUSE("hanim_t11")

HAnimHumanoid45.addSegments(HAnimSegment1778)
HAnimSegment1779 = HAnimSegment()
HAnimSegment1779.setUSE("hanim_t12")

HAnimHumanoid45.addSegments(HAnimSegment1779)
HAnimSegment1780 = HAnimSegment()
HAnimSegment1780.setUSE("hanim_l1")

HAnimHumanoid45.addSegments(HAnimSegment1780)
HAnimSegment1781 = HAnimSegment()
HAnimSegment1781.setUSE("hanim_l2")

HAnimHumanoid45.addSegments(HAnimSegment1781)
HAnimSegment1782 = HAnimSegment()
HAnimSegment1782.setUSE("hanim_l3")

HAnimHumanoid45.addSegments(HAnimSegment1782)
HAnimSegment1783 = HAnimSegment()
HAnimSegment1783.setUSE("hanim_l4")

HAnimHumanoid45.addSegments(HAnimSegment1783)
HAnimSegment1784 = HAnimSegment()
HAnimSegment1784.setUSE("hanim_l5")

HAnimHumanoid45.addSegments(HAnimSegment1784)
HAnimSegment1785 = HAnimSegment()
HAnimSegment1785.setUSE("hanim_sacrum")

HAnimHumanoid45.addSegments(HAnimSegment1785)
HAnimSegment1786 = HAnimSegment()
HAnimSegment1786.setUSE("hanim_l_calf")

HAnimHumanoid45.addSegments(HAnimSegment1786)
HAnimSegment1787 = HAnimSegment()
HAnimSegment1787.setUSE("hanim_r_calf")

HAnimHumanoid45.addSegments(HAnimSegment1787)
HAnimSegment1788 = HAnimSegment()
HAnimSegment1788.setUSE("hanim_l_clavicle")

HAnimHumanoid45.addSegments(HAnimSegment1788)
HAnimSegment1789 = HAnimSegment()
HAnimSegment1789.setUSE("hanim_r_clavicle")

HAnimHumanoid45.addSegments(HAnimSegment1789)
HAnimSegment1790 = HAnimSegment()
HAnimSegment1790.setUSE("hanim_l_eyeball")

HAnimHumanoid45.addSegments(HAnimSegment1790)
HAnimSegment1791 = HAnimSegment()
HAnimSegment1791.setUSE("hanim_r_eyeball")

HAnimHumanoid45.addSegments(HAnimSegment1791)
HAnimSegment1792 = HAnimSegment()
HAnimSegment1792.setUSE("hanim_l_eyebrow")

HAnimHumanoid45.addSegments(HAnimSegment1792)
HAnimSegment1793 = HAnimSegment()
HAnimSegment1793.setUSE("hanim_r_eyebrow")

HAnimHumanoid45.addSegments(HAnimSegment1793)
HAnimSegment1794 = HAnimSegment()
HAnimSegment1794.setUSE("hanim_l_eyelid")

HAnimHumanoid45.addSegments(HAnimSegment1794)
HAnimSegment1795 = HAnimSegment()
HAnimSegment1795.setUSE("hanim_r_eyelid")

HAnimHumanoid45.addSegments(HAnimSegment1795)
HAnimSegment1796 = HAnimSegment()
HAnimSegment1796.setUSE("hanim_l_forearm")

HAnimHumanoid45.addSegments(HAnimSegment1796)
HAnimSegment1797 = HAnimSegment()
HAnimSegment1797.setUSE("hanim_r_forearm")

HAnimHumanoid45.addSegments(HAnimSegment1797)
HAnimSegment1798 = HAnimSegment()
HAnimSegment1798.setUSE("hanim_l_forefoot")

HAnimHumanoid45.addSegments(HAnimSegment1798)
HAnimSegment1799 = HAnimSegment()
HAnimSegment1799.setUSE("hanim_r_forefoot")

HAnimHumanoid45.addSegments(HAnimSegment1799)
HAnimSegment1800 = HAnimSegment()
HAnimSegment1800.setUSE("hanim_l_hand")

HAnimHumanoid45.addSegments(HAnimSegment1800)
HAnimSegment1801 = HAnimSegment()
HAnimSegment1801.setUSE("hanim_r_hand")

HAnimHumanoid45.addSegments(HAnimSegment1801)
HAnimSegment1802 = HAnimSegment()
HAnimSegment1802.setUSE("hanim_l_hindfoot")

HAnimHumanoid45.addSegments(HAnimSegment1802)
HAnimSegment1803 = HAnimSegment()
HAnimSegment1803.setUSE("hanim_r_hindfoot")

HAnimHumanoid45.addSegments(HAnimSegment1803)
HAnimSegment1804 = HAnimSegment()
HAnimSegment1804.setUSE("hanim_l_index_distal")

HAnimHumanoid45.addSegments(HAnimSegment1804)
HAnimSegment1805 = HAnimSegment()
HAnimSegment1805.setUSE("hanim_r_index_distal")

HAnimHumanoid45.addSegments(HAnimSegment1805)
HAnimSegment1806 = HAnimSegment()
HAnimSegment1806.setUSE("hanim_l_index_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1806)
HAnimSegment1807 = HAnimSegment()
HAnimSegment1807.setUSE("hanim_r_index_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1807)
HAnimSegment1808 = HAnimSegment()
HAnimSegment1808.setUSE("hanim_l_index_middle")

HAnimHumanoid45.addSegments(HAnimSegment1808)
HAnimSegment1809 = HAnimSegment()
HAnimSegment1809.setUSE("hanim_r_index_middle")

HAnimHumanoid45.addSegments(HAnimSegment1809)
HAnimSegment1810 = HAnimSegment()
HAnimSegment1810.setUSE("hanim_l_index_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1810)
HAnimSegment1811 = HAnimSegment()
HAnimSegment1811.setUSE("hanim_r_index_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1811)
HAnimSegment1812 = HAnimSegment()
HAnimSegment1812.setUSE("hanim_l_middistal")

HAnimHumanoid45.addSegments(HAnimSegment1812)
HAnimSegment1813 = HAnimSegment()
HAnimSegment1813.setUSE("hanim_r_middistal")

HAnimHumanoid45.addSegments(HAnimSegment1813)
HAnimSegment1814 = HAnimSegment()
HAnimSegment1814.setUSE("hanim_l_middle_distal")

HAnimHumanoid45.addSegments(HAnimSegment1814)
HAnimSegment1815 = HAnimSegment()
HAnimSegment1815.setUSE("hanim_r_middle_distal")

HAnimHumanoid45.addSegments(HAnimSegment1815)
HAnimSegment1816 = HAnimSegment()
HAnimSegment1816.setUSE("hanim_l_middle_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1816)
HAnimSegment1817 = HAnimSegment()
HAnimSegment1817.setUSE("hanim_r_middle_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1817)
HAnimSegment1818 = HAnimSegment()
HAnimSegment1818.setUSE("hanim_l_middle_middle")

HAnimHumanoid45.addSegments(HAnimSegment1818)
HAnimSegment1819 = HAnimSegment()
HAnimSegment1819.setUSE("hanim_r_middle_middle")

HAnimHumanoid45.addSegments(HAnimSegment1819)
HAnimSegment1820 = HAnimSegment()
HAnimSegment1820.setUSE("hanim_l_middle_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1820)
HAnimSegment1821 = HAnimSegment()
HAnimSegment1821.setUSE("hanim_r_middle_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1821)
HAnimSegment1822 = HAnimSegment()
HAnimSegment1822.setUSE("hanim_l_midproximal")

HAnimHumanoid45.addSegments(HAnimSegment1822)
HAnimSegment1823 = HAnimSegment()
HAnimSegment1823.setUSE("hanim_r_midproximal")

HAnimHumanoid45.addSegments(HAnimSegment1823)
HAnimSegment1824 = HAnimSegment()
HAnimSegment1824.setUSE("hanim_l_pinky_distal")

HAnimHumanoid45.addSegments(HAnimSegment1824)
HAnimSegment1825 = HAnimSegment()
HAnimSegment1825.setUSE("hanim_r_pinky_distal")

HAnimHumanoid45.addSegments(HAnimSegment1825)
HAnimSegment1826 = HAnimSegment()
HAnimSegment1826.setUSE("hanim_l_pinky_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1826)
HAnimSegment1827 = HAnimSegment()
HAnimSegment1827.setUSE("hanim_r_pinky_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1827)
HAnimSegment1828 = HAnimSegment()
HAnimSegment1828.setUSE("hanim_l_pinky_middle")

HAnimHumanoid45.addSegments(HAnimSegment1828)
HAnimSegment1829 = HAnimSegment()
HAnimSegment1829.setUSE("hanim_r_pinky_middle")

HAnimHumanoid45.addSegments(HAnimSegment1829)
HAnimSegment1830 = HAnimSegment()
HAnimSegment1830.setUSE("hanim_l_pinky_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1830)
HAnimSegment1831 = HAnimSegment()
HAnimSegment1831.setUSE("hanim_r_pinky_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1831)
HAnimSegment1832 = HAnimSegment()
HAnimSegment1832.setUSE("hanim_l_ring_distal")

HAnimHumanoid45.addSegments(HAnimSegment1832)
HAnimSegment1833 = HAnimSegment()
HAnimSegment1833.setUSE("hanim_r_ring_distal")

HAnimHumanoid45.addSegments(HAnimSegment1833)
HAnimSegment1834 = HAnimSegment()
HAnimSegment1834.setUSE("hanim_l_ring_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1834)
HAnimSegment1835 = HAnimSegment()
HAnimSegment1835.setUSE("hanim_r_ring_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1835)
HAnimSegment1836 = HAnimSegment()
HAnimSegment1836.setUSE("hanim_l_ring_middle")

HAnimHumanoid45.addSegments(HAnimSegment1836)
HAnimSegment1837 = HAnimSegment()
HAnimSegment1837.setUSE("hanim_r_ring_middle")

HAnimHumanoid45.addSegments(HAnimSegment1837)
HAnimSegment1838 = HAnimSegment()
HAnimSegment1838.setUSE("hanim_l_ring_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1838)
HAnimSegment1839 = HAnimSegment()
HAnimSegment1839.setUSE("hanim_r_ring_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1839)
HAnimSegment1840 = HAnimSegment()
HAnimSegment1840.setUSE("hanim_l_scapula")

HAnimHumanoid45.addSegments(HAnimSegment1840)
HAnimSegment1841 = HAnimSegment()
HAnimSegment1841.setUSE("hanim_r_scapula")

HAnimHumanoid45.addSegments(HAnimSegment1841)
HAnimSegment1842 = HAnimSegment()
HAnimSegment1842.setUSE("hanim_l_thigh")

HAnimHumanoid45.addSegments(HAnimSegment1842)
HAnimSegment1843 = HAnimSegment()
HAnimSegment1843.setUSE("hanim_r_thigh")

HAnimHumanoid45.addSegments(HAnimSegment1843)
HAnimSegment1844 = HAnimSegment()
HAnimSegment1844.setUSE("hanim_l_thumb_distal")

HAnimHumanoid45.addSegments(HAnimSegment1844)
HAnimSegment1845 = HAnimSegment()
HAnimSegment1845.setUSE("hanim_r_thumb_distal")

HAnimHumanoid45.addSegments(HAnimSegment1845)
HAnimSegment1846 = HAnimSegment()
HAnimSegment1846.setUSE("hanim_l_thumb_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1846)
HAnimSegment1847 = HAnimSegment()
HAnimSegment1847.setUSE("hanim_r_thumb_metacarpal")

HAnimHumanoid45.addSegments(HAnimSegment1847)
HAnimSegment1848 = HAnimSegment()
HAnimSegment1848.setUSE("hanim_l_thumb_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1848)
HAnimSegment1849 = HAnimSegment()
HAnimSegment1849.setUSE("hanim_r_thumb_proximal")

HAnimHumanoid45.addSegments(HAnimSegment1849)
HAnimSegment1850 = HAnimSegment()
HAnimSegment1850.setUSE("hanim_l_upperarm")

HAnimHumanoid45.addSegments(HAnimSegment1850)
HAnimSegment1851 = HAnimSegment()
HAnimSegment1851.setUSE("hanim_r_upperarm")

HAnimHumanoid45.addSegments(HAnimSegment1851)
HAnimSite1852 = HAnimSite()
HAnimSite1852.setUSE("hanim_crotch_pt")

HAnimHumanoid45.addSites(HAnimSite1852)
HAnimSite1853 = HAnimSite()
HAnimSite1853.setUSE("hanim_skull_tip")

HAnimHumanoid45.addSites(HAnimSite1853)
HAnimSite1854 = HAnimSite()
HAnimSite1854.setUSE("hanim_sellion_pt")

HAnimHumanoid45.addSites(HAnimSite1854)
HAnimSite1855 = HAnimSite()
HAnimSite1855.setUSE("hanim_supramenton_pt")

HAnimHumanoid45.addSites(HAnimSite1855)
HAnimSite1856 = HAnimSite()
HAnimSite1856.setUSE("hanim_nuchale_pt")

HAnimHumanoid45.addSites(HAnimSite1856)
HAnimSite1857 = HAnimSite()
HAnimSite1857.setUSE("hanim_suprasternale_pt")

HAnimHumanoid45.addSites(HAnimSite1857)
HAnimSite1858 = HAnimSite()
HAnimSite1858.setUSE("hanim_cervicale_pt")

HAnimHumanoid45.addSites(HAnimSite1858)
HAnimSite1859 = HAnimSite()
HAnimSite1859.setUSE("hanim_substernale_pt")

HAnimHumanoid45.addSites(HAnimSite1859)
HAnimSite1860 = HAnimSite()
HAnimSite1860.setUSE("hanim_rib10_midspine_pt")

HAnimHumanoid45.addSites(HAnimSite1860)
HAnimSite1861 = HAnimSite()
HAnimSite1861.setUSE("hanim_waist_preferred_post_pt")

HAnimHumanoid45.addSites(HAnimSite1861)
HAnimSite1862 = HAnimSite()
HAnimSite1862.setUSE("hanim_navel_pt")

HAnimHumanoid45.addSites(HAnimSite1862)
HAnimSite1863 = HAnimSite()
HAnimSite1863.setUSE("hanim_l_acromion_pt")

HAnimHumanoid45.addSites(HAnimSite1863)
HAnimSite1864 = HAnimSite()
HAnimSite1864.setUSE("hanim_r_acromion_pt")

HAnimHumanoid45.addSites(HAnimSite1864)
HAnimSite1865 = HAnimSite()
HAnimSite1865.setUSE("hanim_r_asis_pt")

HAnimHumanoid45.addSites(HAnimSite1865)
HAnimSite1866 = HAnimSite()
HAnimSite1866.setUSE("hanim_l_asis_pt")

HAnimHumanoid45.addSites(HAnimSite1866)
HAnimSite1867 = HAnimSite()
HAnimSite1867.setUSE("hanim_l_axilla_ant_pt")

HAnimHumanoid45.addSites(HAnimSite1867)
HAnimSite1868 = HAnimSite()
HAnimSite1868.setUSE("hanim_r_axilla_ant_pt")

HAnimHumanoid45.addSites(HAnimSite1868)
HAnimSite1869 = HAnimSite()
HAnimSite1869.setUSE("hanim_l_axilla_post_pt")

HAnimHumanoid45.addSites(HAnimSite1869)
HAnimSite1870 = HAnimSite()
HAnimSite1870.setUSE("hanim_r_axilla_post_pt")

HAnimHumanoid45.addSites(HAnimSite1870)
HAnimSite1871 = HAnimSite()
HAnimSite1871.setUSE("hanim_l_calcaneous_post_pt")

HAnimHumanoid45.addSites(HAnimSite1871)
HAnimSite1872 = HAnimSite()
HAnimSite1872.setUSE("hanim_r_calcaneous_post_pt")

HAnimHumanoid45.addSites(HAnimSite1872)
HAnimSite1873 = HAnimSite()
HAnimSite1873.setUSE("hanim_l_clavicale_pt")

HAnimHumanoid45.addSites(HAnimSite1873)
HAnimSite1874 = HAnimSite()
HAnimSite1874.setUSE("hanim_r_clavicale_pt")

HAnimHumanoid45.addSites(HAnimSite1874)
HAnimSite1875 = HAnimSite()
HAnimSite1875.setUSE("hanim_l_dactylion_pt")

HAnimHumanoid45.addSites(HAnimSite1875)
HAnimSite1876 = HAnimSite()
HAnimSite1876.setUSE("hanim_r_dactylion_pt")

HAnimHumanoid45.addSites(HAnimSite1876)
HAnimSite1877 = HAnimSite()
HAnimSite1877.setUSE("hanim_l_digit2_pt")

HAnimHumanoid45.addSites(HAnimSite1877)
HAnimSite1878 = HAnimSite()
HAnimSite1878.setUSE("hanim_r_digit2_pt")

HAnimHumanoid45.addSites(HAnimSite1878)
HAnimSite1879 = HAnimSite()
HAnimSite1879.setUSE("hanim_l_femoral_lateral_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1879)
HAnimSite1880 = HAnimSite()
HAnimSite1880.setUSE("hanim_r_femoral_lateral_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1880)
HAnimSite1881 = HAnimSite()
HAnimSite1881.setUSE("hanim_l_femoral_medial_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1881)
HAnimSite1882 = HAnimSite()
HAnimSite1882.setUSE("hanim_r_femoral_medial_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1882)
HAnimSite1883 = HAnimSite()
HAnimSite1883.setUSE("hanim_l_forefoot_tip")

HAnimHumanoid45.addSites(HAnimSite1883)
HAnimSite1884 = HAnimSite()
HAnimSite1884.setUSE("hanim_r_forefoot_tip")

HAnimHumanoid45.addSites(HAnimSite1884)
HAnimSite1885 = HAnimSite()
HAnimSite1885.setUSE("hanim_r_gonion_pt")

HAnimHumanoid45.addSites(HAnimSite1885)
HAnimSite1886 = HAnimSite()
HAnimSite1886.setUSE("hanim_l_gonion_pt")

HAnimHumanoid45.addSites(HAnimSite1886)
HAnimSite1887 = HAnimSite()
HAnimSite1887.setUSE("hanim_l_humeral_lateral_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1887)
HAnimSite1888 = HAnimSite()
HAnimSite1888.setUSE("hanim_r_humeral_lateral_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1888)
HAnimSite1889 = HAnimSite()
HAnimSite1889.setUSE("hanim_l_humeral_medial_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1889)
HAnimSite1890 = HAnimSite()
HAnimSite1890.setUSE("hanim_r_humeral_medial_epicn_pt")

HAnimHumanoid45.addSites(HAnimSite1890)
HAnimSite1891 = HAnimSite()
HAnimSite1891.setUSE("hanim_r_iliocristale_pt")

HAnimHumanoid45.addSites(HAnimSite1891)
HAnimSite1892 = HAnimSite()
HAnimSite1892.setUSE("hanim_l_iliocristale_pt")

HAnimHumanoid45.addSites(HAnimSite1892)
HAnimSite1893 = HAnimSite()
HAnimSite1893.setUSE("hanim_l_index_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1893)
HAnimSite1894 = HAnimSite()
HAnimSite1894.setUSE("hanim_r_index_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1894)
HAnimSite1895 = HAnimSite()
HAnimSite1895.setUSE("hanim_r_infraorbitale_pt")

HAnimHumanoid45.addSites(HAnimSite1895)
HAnimSite1896 = HAnimSite()
HAnimSite1896.setUSE("hanim_l_infraorbitale_pt")

HAnimHumanoid45.addSites(HAnimSite1896)
HAnimSite1897 = HAnimSite()
HAnimSite1897.setUSE("hanim_l_knee_crease_pt")

HAnimHumanoid45.addSites(HAnimSite1897)
HAnimSite1898 = HAnimSite()
HAnimSite1898.setUSE("hanim_r_knee_crease_pt")

HAnimHumanoid45.addSites(HAnimSite1898)
HAnimSite1899 = HAnimSite()
HAnimSite1899.setUSE("hanim_l_lateral_malleolus_pt")

HAnimHumanoid45.addSites(HAnimSite1899)
HAnimSite1900 = HAnimSite()
HAnimSite1900.setUSE("hanim_r_lateral_malleolus_pt")

HAnimHumanoid45.addSites(HAnimSite1900)
HAnimSite1901 = HAnimSite()
HAnimSite1901.setUSE("hanim_l_medial_malleolus_pt")

HAnimHumanoid45.addSites(HAnimSite1901)
HAnimSite1902 = HAnimSite()
HAnimSite1902.setUSE("hanim_r_medial_malleolus_pt")

HAnimHumanoid45.addSites(HAnimSite1902)
HAnimSite1903 = HAnimSite()
HAnimSite1903.setUSE("hanim_l_metacarpal_pha2_pt")

HAnimHumanoid45.addSites(HAnimSite1903)
HAnimSite1904 = HAnimSite()
HAnimSite1904.setUSE("hanim_r_metacarpal_pha2_pt")

HAnimHumanoid45.addSites(HAnimSite1904)
HAnimSite1905 = HAnimSite()
HAnimSite1905.setUSE("hanim_l_metacarpal_pha5_pt")

HAnimHumanoid45.addSites(HAnimSite1905)
HAnimSite1906 = HAnimSite()
HAnimSite1906.setUSE("hanim_r_metacarpal_pha5_pt")

HAnimHumanoid45.addSites(HAnimSite1906)
HAnimSite1907 = HAnimSite()
HAnimSite1907.setUSE("hanim_l_metatarsal_pha1_pt")

HAnimHumanoid45.addSites(HAnimSite1907)
HAnimSite1908 = HAnimSite()
HAnimSite1908.setUSE("hanim_r_metatarsal_pha1_pt")

HAnimHumanoid45.addSites(HAnimSite1908)
HAnimSite1909 = HAnimSite()
HAnimSite1909.setUSE("hanim_l_metatarsal_pha5_pt")

HAnimHumanoid45.addSites(HAnimSite1909)
HAnimSite1910 = HAnimSite()
HAnimSite1910.setUSE("hanim_r_metatarsal_pha5_pt")

HAnimHumanoid45.addSites(HAnimSite1910)
HAnimSite1911 = HAnimSite()
HAnimSite1911.setUSE("hanim_l_middle_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1911)
HAnimSite1912 = HAnimSite()
HAnimSite1912.setUSE("hanim_r_middle_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1912)
HAnimSite1913 = HAnimSite()
HAnimSite1913.setUSE("hanim_r_neck_base_pt")

HAnimHumanoid45.addSites(HAnimSite1913)
HAnimSite1914 = HAnimSite()
HAnimSite1914.setUSE("hanim_l_neck_base_pt")

HAnimHumanoid45.addSites(HAnimSite1914)
HAnimSite1915 = HAnimSite()
HAnimSite1915.setUSE("hanim_l_olecranon_pt")

HAnimHumanoid45.addSites(HAnimSite1915)
HAnimSite1916 = HAnimSite()
HAnimSite1916.setUSE("hanim_r_olecranon_pt")

HAnimHumanoid45.addSites(HAnimSite1916)
HAnimSite1917 = HAnimSite()
HAnimSite1917.setUSE("hanim_l_pinky_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1917)
HAnimSite1918 = HAnimSite()
HAnimSite1918.setUSE("hanim_r_pinky_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1918)
HAnimSite1919 = HAnimSite()
HAnimSite1919.setUSE("hanim_r_psis_pt")

HAnimHumanoid45.addSites(HAnimSite1919)
HAnimSite1920 = HAnimSite()
HAnimSite1920.setUSE("hanim_l_psis_pt")

HAnimHumanoid45.addSites(HAnimSite1920)
HAnimSite1921 = HAnimSite()
HAnimSite1921.setUSE("hanim_l_radial_styloid_pt")

HAnimHumanoid45.addSites(HAnimSite1921)
HAnimSite1922 = HAnimSite()
HAnimSite1922.setUSE("hanim_r_radial_styloid_pt")

HAnimHumanoid45.addSites(HAnimSite1922)
HAnimSite1923 = HAnimSite()
HAnimSite1923.setUSE("hanim_l_radiale_pt")

HAnimHumanoid45.addSites(HAnimSite1923)
HAnimSite1924 = HAnimSite()
HAnimSite1924.setUSE("hanim_r_radiale_pt")

HAnimHumanoid45.addSites(HAnimSite1924)
HAnimSite1925 = HAnimSite()
HAnimSite1925.setUSE("hanim_r_rib10_pt")

HAnimHumanoid45.addSites(HAnimSite1925)
HAnimSite1926 = HAnimSite()
HAnimSite1926.setUSE("hanim_l_rib10_pt")

HAnimHumanoid45.addSites(HAnimSite1926)
HAnimSite1927 = HAnimSite()
HAnimSite1927.setUSE("hanim_l_ring_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1927)
HAnimSite1928 = HAnimSite()
HAnimSite1928.setUSE("hanim_r_ring_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1928)
HAnimSite1929 = HAnimSite()
HAnimSite1929.setUSE("hanim_temporomandibular_l_site_pt")

HAnimHumanoid45.addSites(HAnimSite1929)
HAnimSite1930 = HAnimSite()
HAnimSite1930.setUSE("hanim_temporomandibular_r_site_pt")

HAnimHumanoid45.addSites(HAnimSite1930)
HAnimSite1931 = HAnimSite()
HAnimSite1931.setUSE("hanim_l_sphyrion_pt")

HAnimHumanoid45.addSites(HAnimSite1931)
HAnimSite1932 = HAnimSite()
HAnimSite1932.setUSE("hanim_r_sphyrion_pt")

HAnimHumanoid45.addSites(HAnimSite1932)
HAnimSite1933 = HAnimSite()
HAnimSite1933.setUSE("hanim_r_thelion_pt")

HAnimHumanoid45.addSites(HAnimSite1933)
HAnimSite1934 = HAnimSite()
HAnimSite1934.setUSE("hanim_l_thelion_pt")

HAnimHumanoid45.addSites(HAnimSite1934)
HAnimSite1935 = HAnimSite()
HAnimSite1935.setUSE("hanim_l_thumb_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1935)
HAnimSite1936 = HAnimSite()
HAnimSite1936.setUSE("hanim_r_thumb_distal_tip")

HAnimHumanoid45.addSites(HAnimSite1936)
HAnimSite1937 = HAnimSite()
HAnimSite1937.setUSE("hanim_r_tragion_pt")

HAnimHumanoid45.addSites(HAnimSite1937)
HAnimSite1938 = HAnimSite()
HAnimSite1938.setUSE("hanim_l_tragion_pt")

HAnimHumanoid45.addSites(HAnimSite1938)
HAnimSite1939 = HAnimSite()
HAnimSite1939.setUSE("hanim_r_trochanterion_pt")

HAnimHumanoid45.addSites(HAnimSite1939)
HAnimSite1940 = HAnimSite()
HAnimSite1940.setUSE("hanim_l_trochanterion_pt")

HAnimHumanoid45.addSites(HAnimSite1940)
HAnimSite1941 = HAnimSite()
HAnimSite1941.setUSE("hanim_l_ulnar_styloid_pt")

HAnimHumanoid45.addSites(HAnimSite1941)
HAnimSite1942 = HAnimSite()
HAnimSite1942.setUSE("hanim_r_ulnar_styloid_pt")

HAnimHumanoid45.addSites(HAnimSite1942)

Scene31.addChildren(HAnimHumanoid45)
Group1943 = Group()
Group1943.setDEF("StopAnimation")
TimeSensor1944 = TimeSensor()
TimeSensor1944.setDEF("StopTimer")
TimeSensor1944.setCycleInterval(5.73)
TimeSensor1944.setLoop(True)

Group1943.addChildren(TimeSensor1944)
PositionInterpolator1945 = PositionInterpolator()
PositionInterpolator1945.setDEF("Stop_HumanoidRoot_TranslationInterpolator")
PositionInterpolator1945.setKey([0,0.5,1])
PositionInterpolator1945.setKeyValue([0,0,0,0,0,0,0,0,0])

Group1943.addChildren(PositionInterpolator1945)
OrientationInterpolator1946 = OrientationInterpolator()
OrientationInterpolator1946.setDEF("Stop_HumanoidRoot_RotationInterpolator")
OrientationInterpolator1946.setKey([0,0.5,1])
OrientationInterpolator1946.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1946)
OrientationInterpolator1947 = OrientationInterpolator()
OrientationInterpolator1947.setDEF("Stop_sacroiliac_RotationInterpolator")
OrientationInterpolator1947.setKey([0,0.5,1])
OrientationInterpolator1947.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1947)
OrientationInterpolator1948 = OrientationInterpolator()
OrientationInterpolator1948.setDEF("Stop_l_hip_RotationInterpolator")
OrientationInterpolator1948.setKey([0,0.5,1])
OrientationInterpolator1948.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1948)
OrientationInterpolator1949 = OrientationInterpolator()
OrientationInterpolator1949.setDEF("Stop_l_knee_RotationInterpolator")
OrientationInterpolator1949.setKey([0,0.5,1])
OrientationInterpolator1949.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1949)
OrientationInterpolator1950 = OrientationInterpolator()
OrientationInterpolator1950.setDEF("Stop_l_ankle_RotationInterpolator")
OrientationInterpolator1950.setKey([0,0.5,1])
OrientationInterpolator1950.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1950)
OrientationInterpolator1951 = OrientationInterpolator()
OrientationInterpolator1951.setDEF("Stop_l_subtalar_RotationInterpolator")
OrientationInterpolator1951.setKey([0,0.5,1])
OrientationInterpolator1951.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1951)
OrientationInterpolator1952 = OrientationInterpolator()
OrientationInterpolator1952.setDEF("Stop_l_midtarsal_RotationInterpolator")
OrientationInterpolator1952.setKey([0,0.5,1])
OrientationInterpolator1952.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1952)
OrientationInterpolator1953 = OrientationInterpolator()
OrientationInterpolator1953.setDEF("Stop_l_metatarsal_RotationInterpolator")
OrientationInterpolator1953.setKey([0,0.5,1])
OrientationInterpolator1953.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1953)
OrientationInterpolator1954 = OrientationInterpolator()
OrientationInterpolator1954.setDEF("Stop_r_hip_RotationInterpolator")
OrientationInterpolator1954.setKey([0,0.5,1])
OrientationInterpolator1954.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1954)
OrientationInterpolator1955 = OrientationInterpolator()
OrientationInterpolator1955.setDEF("Stop_r_knee_RotationInterpolator")
OrientationInterpolator1955.setKey([0,0.5,1])
OrientationInterpolator1955.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1955)
OrientationInterpolator1956 = OrientationInterpolator()
OrientationInterpolator1956.setDEF("Stop_r_ankle_RotationInterpolator")
OrientationInterpolator1956.setKey([0,0.5,1])
OrientationInterpolator1956.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1956)
OrientationInterpolator1957 = OrientationInterpolator()
OrientationInterpolator1957.setDEF("Stop_r_subtalar_RotationInterpolator")
OrientationInterpolator1957.setKey([0,0.5,1])
OrientationInterpolator1957.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1957)
OrientationInterpolator1958 = OrientationInterpolator()
OrientationInterpolator1958.setDEF("Stop_r_midtarsal_RotationInterpolator")
OrientationInterpolator1958.setKey([0,0.5,1])
OrientationInterpolator1958.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1958)
OrientationInterpolator1959 = OrientationInterpolator()
OrientationInterpolator1959.setDEF("Stop_r_metatarsal_RotationInterpolator")
OrientationInterpolator1959.setKey([0,0.5,1])
OrientationInterpolator1959.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1959)
OrientationInterpolator1960 = OrientationInterpolator()
OrientationInterpolator1960.setDEF("Stop_vl5_RotationInterpolator")
OrientationInterpolator1960.setKey([0,0.5,1])
OrientationInterpolator1960.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1960)
OrientationInterpolator1961 = OrientationInterpolator()
OrientationInterpolator1961.setDEF("Stop_vl4_RotationInterpolator")
OrientationInterpolator1961.setKey([0,0.5,1])
OrientationInterpolator1961.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1961)
OrientationInterpolator1962 = OrientationInterpolator()
OrientationInterpolator1962.setDEF("Stop_vl3_RotationInterpolator")
OrientationInterpolator1962.setKey([0,0.5,1])
OrientationInterpolator1962.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1962)
OrientationInterpolator1963 = OrientationInterpolator()
OrientationInterpolator1963.setDEF("Stop_vl2_RotationInterpolator")
OrientationInterpolator1963.setKey([0,0.5,1])
OrientationInterpolator1963.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1963)
OrientationInterpolator1964 = OrientationInterpolator()
OrientationInterpolator1964.setDEF("Stop_vl1_RotationInterpolator")
OrientationInterpolator1964.setKey([0,0.5,1])
OrientationInterpolator1964.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1964)
OrientationInterpolator1965 = OrientationInterpolator()
OrientationInterpolator1965.setDEF("Stop_vt12_RotationInterpolator")
OrientationInterpolator1965.setKey([0,0.5,1])
OrientationInterpolator1965.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1965)
OrientationInterpolator1966 = OrientationInterpolator()
OrientationInterpolator1966.setDEF("Stop_vt11_RotationInterpolator")
OrientationInterpolator1966.setKey([0,0.5,1])
OrientationInterpolator1966.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1966)
OrientationInterpolator1967 = OrientationInterpolator()
OrientationInterpolator1967.setDEF("Stop_vt10_RotationInterpolator")
OrientationInterpolator1967.setKey([0,0.5,1])
OrientationInterpolator1967.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1967)
OrientationInterpolator1968 = OrientationInterpolator()
OrientationInterpolator1968.setDEF("Stop_vt9_RotationInterpolator")
OrientationInterpolator1968.setKey([0,0.5,1])
OrientationInterpolator1968.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1968)
OrientationInterpolator1969 = OrientationInterpolator()
OrientationInterpolator1969.setDEF("Stop_vt8_RotationInterpolator")
OrientationInterpolator1969.setKey([0,0.5,1])
OrientationInterpolator1969.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1969)
OrientationInterpolator1970 = OrientationInterpolator()
OrientationInterpolator1970.setDEF("Stop_vt7_RotationInterpolator")
OrientationInterpolator1970.setKey([0,0.5,1])
OrientationInterpolator1970.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1970)
OrientationInterpolator1971 = OrientationInterpolator()
OrientationInterpolator1971.setDEF("Stop_vt6_RotationInterpolator")
OrientationInterpolator1971.setKey([0,0.5,1])
OrientationInterpolator1971.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1971)
OrientationInterpolator1972 = OrientationInterpolator()
OrientationInterpolator1972.setDEF("Stop_vt5_RotationInterpolator")
OrientationInterpolator1972.setKey([0,0.5,1])
OrientationInterpolator1972.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1972)
OrientationInterpolator1973 = OrientationInterpolator()
OrientationInterpolator1973.setDEF("Stop_vt4_RotationInterpolator")
OrientationInterpolator1973.setKey([0,0.5,1])
OrientationInterpolator1973.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1973)
OrientationInterpolator1974 = OrientationInterpolator()
OrientationInterpolator1974.setDEF("Stop_vt3_RotationInterpolator")
OrientationInterpolator1974.setKey([0,0.5,1])
OrientationInterpolator1974.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1974)
OrientationInterpolator1975 = OrientationInterpolator()
OrientationInterpolator1975.setDEF("Stop_vt2_RotationInterpolator")
OrientationInterpolator1975.setKey([0,0.5,1])
OrientationInterpolator1975.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1975)
OrientationInterpolator1976 = OrientationInterpolator()
OrientationInterpolator1976.setDEF("Stop_vt1_RotationInterpolator")
OrientationInterpolator1976.setKey([0,0.5,1])
OrientationInterpolator1976.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1976)
OrientationInterpolator1977 = OrientationInterpolator()
OrientationInterpolator1977.setDEF("Stop_vc7_RotationInterpolator")
OrientationInterpolator1977.setKey([0,0.5,1])
OrientationInterpolator1977.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1977)
OrientationInterpolator1978 = OrientationInterpolator()
OrientationInterpolator1978.setDEF("Stop_vc6_RotationInterpolator")
OrientationInterpolator1978.setKey([0,0.5,1])
OrientationInterpolator1978.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1978)
OrientationInterpolator1979 = OrientationInterpolator()
OrientationInterpolator1979.setDEF("Stop_vc5_RotationInterpolator")
OrientationInterpolator1979.setKey([0,0.5,1])
OrientationInterpolator1979.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1979)
OrientationInterpolator1980 = OrientationInterpolator()
OrientationInterpolator1980.setDEF("Stop_vc4_RotationInterpolator")
OrientationInterpolator1980.setKey([0,0.5,1])
OrientationInterpolator1980.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1980)
OrientationInterpolator1981 = OrientationInterpolator()
OrientationInterpolator1981.setDEF("Stop_vc3_RotationInterpolator")
OrientationInterpolator1981.setKey([0,0.5,1])
OrientationInterpolator1981.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1981)
OrientationInterpolator1982 = OrientationInterpolator()
OrientationInterpolator1982.setDEF("Stop_vc2_RotationInterpolator")
OrientationInterpolator1982.setKey([0,0.5,1])
OrientationInterpolator1982.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1982)
OrientationInterpolator1983 = OrientationInterpolator()
OrientationInterpolator1983.setDEF("Stop_vc1_RotationInterpolator")
OrientationInterpolator1983.setKey([0,0.5,1])
OrientationInterpolator1983.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1983)
OrientationInterpolator1984 = OrientationInterpolator()
OrientationInterpolator1984.setDEF("Stop_skullbase_RotationInterpolator")
OrientationInterpolator1984.setKey([0,0.5,1])
OrientationInterpolator1984.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1984)
OrientationInterpolator1985 = OrientationInterpolator()
OrientationInterpolator1985.setDEF("Stop_l_eyeball_joint_RotationInterpolator")
OrientationInterpolator1985.setKey([0,0.5,1])
OrientationInterpolator1985.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1985)
OrientationInterpolator1986 = OrientationInterpolator()
OrientationInterpolator1986.setDEF("Stop_r_eyeball_joint_RotationInterpolator")
OrientationInterpolator1986.setKey([0,0.5,1])
OrientationInterpolator1986.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1986)
OrientationInterpolator1987 = OrientationInterpolator()
OrientationInterpolator1987.setDEF("Stop_l_sternoclavicular_RotationInterpolator")
OrientationInterpolator1987.setKey([0,0.5,1])
OrientationInterpolator1987.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1987)
OrientationInterpolator1988 = OrientationInterpolator()
OrientationInterpolator1988.setDEF("Stop_l_acromioclavicular_RotationInterpolator")
OrientationInterpolator1988.setKey([0,0.5,1])
OrientationInterpolator1988.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1988)
OrientationInterpolator1989 = OrientationInterpolator()
OrientationInterpolator1989.setDEF("Stop_l_shoulder_RotationInterpolator")
OrientationInterpolator1989.setKey([0,0.5,1])
OrientationInterpolator1989.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1989)
OrientationInterpolator1990 = OrientationInterpolator()
OrientationInterpolator1990.setDEF("Stop_l_elbow_RotationInterpolator")
OrientationInterpolator1990.setKey([0,0.5,1])
OrientationInterpolator1990.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1990)
OrientationInterpolator1991 = OrientationInterpolator()
OrientationInterpolator1991.setDEF("Stop_l_wrist_RotationInterpolator")
OrientationInterpolator1991.setKey([0,0.5,1])
OrientationInterpolator1991.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1991)
OrientationInterpolator1992 = OrientationInterpolator()
OrientationInterpolator1992.setDEF("Stop_l_thumb1_RotationInterpolator")
OrientationInterpolator1992.setKey([0,0.5,1])
OrientationInterpolator1992.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1992)
OrientationInterpolator1993 = OrientationInterpolator()
OrientationInterpolator1993.setDEF("Stop_l_thumb2_RotationInterpolator")
OrientationInterpolator1993.setKey([0,0.5,1])
OrientationInterpolator1993.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1993)
OrientationInterpolator1994 = OrientationInterpolator()
OrientationInterpolator1994.setDEF("Stop_l_thumb3_RotationInterpolator")
OrientationInterpolator1994.setKey([0,0.5,1])
OrientationInterpolator1994.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1994)
OrientationInterpolator1995 = OrientationInterpolator()
OrientationInterpolator1995.setDEF("Stop_l_index0_RotationInterpolator")
OrientationInterpolator1995.setKey([0,0.5,1])
OrientationInterpolator1995.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1995)
OrientationInterpolator1996 = OrientationInterpolator()
OrientationInterpolator1996.setDEF("Stop_l_index1_RotationInterpolator")
OrientationInterpolator1996.setKey([0,0.5,1])
OrientationInterpolator1996.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1996)
OrientationInterpolator1997 = OrientationInterpolator()
OrientationInterpolator1997.setDEF("Stop_l_index2_RotationInterpolator")
OrientationInterpolator1997.setKey([0,0.5,1])
OrientationInterpolator1997.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1997)
OrientationInterpolator1998 = OrientationInterpolator()
OrientationInterpolator1998.setDEF("Stop_l_index3_RotationInterpolator")
OrientationInterpolator1998.setKey([0,0.5,1])
OrientationInterpolator1998.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1998)
OrientationInterpolator1999 = OrientationInterpolator()
OrientationInterpolator1999.setDEF("Stop_l_middle0_RotationInterpolator")
OrientationInterpolator1999.setKey([0,0.5,1])
OrientationInterpolator1999.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator1999)
OrientationInterpolator2000 = OrientationInterpolator()
OrientationInterpolator2000.setDEF("Stop_l_middle1_RotationInterpolator")
OrientationInterpolator2000.setKey([0,0.5,1])
OrientationInterpolator2000.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2000)
OrientationInterpolator2001 = OrientationInterpolator()
OrientationInterpolator2001.setDEF("Stop_l_middle2_RotationInterpolator")
OrientationInterpolator2001.setKey([0,0.5,1])
OrientationInterpolator2001.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2001)
OrientationInterpolator2002 = OrientationInterpolator()
OrientationInterpolator2002.setDEF("Stop_l_middle3_RotationInterpolator")
OrientationInterpolator2002.setKey([0,0.5,1])
OrientationInterpolator2002.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2002)
OrientationInterpolator2003 = OrientationInterpolator()
OrientationInterpolator2003.setDEF("Stop_l_ring0_RotationInterpolator")
OrientationInterpolator2003.setKey([0,0.5,1])
OrientationInterpolator2003.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2003)
OrientationInterpolator2004 = OrientationInterpolator()
OrientationInterpolator2004.setDEF("Stop_l_ring1_RotationInterpolator")
OrientationInterpolator2004.setKey([0,0.5,1])
OrientationInterpolator2004.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2004)
OrientationInterpolator2005 = OrientationInterpolator()
OrientationInterpolator2005.setDEF("Stop_l_ring2_RotationInterpolator")
OrientationInterpolator2005.setKey([0,0.5,1])
OrientationInterpolator2005.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2005)
OrientationInterpolator2006 = OrientationInterpolator()
OrientationInterpolator2006.setDEF("Stop_l_ring3_RotationInterpolator")
OrientationInterpolator2006.setKey([0,0.5,1])
OrientationInterpolator2006.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2006)
OrientationInterpolator2007 = OrientationInterpolator()
OrientationInterpolator2007.setDEF("Stop_l_pinky0_RotationInterpolator")
OrientationInterpolator2007.setKey([0,0.5,1])
OrientationInterpolator2007.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2007)
OrientationInterpolator2008 = OrientationInterpolator()
OrientationInterpolator2008.setDEF("Stop_l_pinky1_RotationInterpolator")
OrientationInterpolator2008.setKey([0,0.5,1])
OrientationInterpolator2008.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2008)
OrientationInterpolator2009 = OrientationInterpolator()
OrientationInterpolator2009.setDEF("Stop_l_pinky2_RotationInterpolator")
OrientationInterpolator2009.setKey([0,0.5,1])
OrientationInterpolator2009.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2009)
OrientationInterpolator2010 = OrientationInterpolator()
OrientationInterpolator2010.setDEF("Stop_l_pinky3_RotationInterpolator")
OrientationInterpolator2010.setKey([0,0.5,1])
OrientationInterpolator2010.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2010)
OrientationInterpolator2011 = OrientationInterpolator()
OrientationInterpolator2011.setDEF("Stop_r_sternoclavicular_RotationInterpolator")
OrientationInterpolator2011.setKey([0,0.5,1])
OrientationInterpolator2011.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2011)
OrientationInterpolator2012 = OrientationInterpolator()
OrientationInterpolator2012.setDEF("Stop_r_acromioclavicular_RotationInterpolator")
OrientationInterpolator2012.setKey([0,0.5,1])
OrientationInterpolator2012.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2012)
OrientationInterpolator2013 = OrientationInterpolator()
OrientationInterpolator2013.setDEF("Stop_r_shoulder_RotationInterpolator")
OrientationInterpolator2013.setKey([0,0.5,1])
OrientationInterpolator2013.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2013)
OrientationInterpolator2014 = OrientationInterpolator()
OrientationInterpolator2014.setDEF("Stop_r_elbow_RotationInterpolator")
OrientationInterpolator2014.setKey([0,0.5,1])
OrientationInterpolator2014.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2014)
OrientationInterpolator2015 = OrientationInterpolator()
OrientationInterpolator2015.setDEF("Stop_r_wrist_RotationInterpolator")
OrientationInterpolator2015.setKey([0,0.5,1])
OrientationInterpolator2015.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2015)
OrientationInterpolator2016 = OrientationInterpolator()
OrientationInterpolator2016.setDEF("Stop_r_thumb1_RotationInterpolator")
OrientationInterpolator2016.setKey([0,0.5,1])
OrientationInterpolator2016.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2016)
OrientationInterpolator2017 = OrientationInterpolator()
OrientationInterpolator2017.setDEF("Stop_r_thumb2_RotationInterpolator")
OrientationInterpolator2017.setKey([0,0.5,1])
OrientationInterpolator2017.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2017)
OrientationInterpolator2018 = OrientationInterpolator()
OrientationInterpolator2018.setDEF("Stop_r_thumb3_RotationInterpolator")
OrientationInterpolator2018.setKey([0,0.5,1])
OrientationInterpolator2018.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2018)
OrientationInterpolator2019 = OrientationInterpolator()
OrientationInterpolator2019.setDEF("Stop_r_index0_RotationInterpolator")
OrientationInterpolator2019.setKey([0,0.5,1])
OrientationInterpolator2019.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2019)
OrientationInterpolator2020 = OrientationInterpolator()
OrientationInterpolator2020.setDEF("Stop_r_index1_RotationInterpolator")
OrientationInterpolator2020.setKey([0,0.5,1])
OrientationInterpolator2020.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2020)
OrientationInterpolator2021 = OrientationInterpolator()
OrientationInterpolator2021.setDEF("Stop_r_index2_RotationInterpolator")
OrientationInterpolator2021.setKey([0,0.5,1])
OrientationInterpolator2021.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2021)
OrientationInterpolator2022 = OrientationInterpolator()
OrientationInterpolator2022.setDEF("Stop_r_index3_RotationInterpolator")
OrientationInterpolator2022.setKey([0,0.5,1])
OrientationInterpolator2022.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2022)
OrientationInterpolator2023 = OrientationInterpolator()
OrientationInterpolator2023.setDEF("Stop_r_middle0_RotationInterpolator")
OrientationInterpolator2023.setKey([0,0.5,1])
OrientationInterpolator2023.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2023)
OrientationInterpolator2024 = OrientationInterpolator()
OrientationInterpolator2024.setDEF("Stop_r_middle1_RotationInterpolator")
OrientationInterpolator2024.setKey([0,0.5,1])
OrientationInterpolator2024.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2024)
OrientationInterpolator2025 = OrientationInterpolator()
OrientationInterpolator2025.setDEF("Stop_r_middle2_RotationInterpolator")
OrientationInterpolator2025.setKey([0,0.5,1])
OrientationInterpolator2025.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2025)
OrientationInterpolator2026 = OrientationInterpolator()
OrientationInterpolator2026.setDEF("Stop_r_middle3_RotationInterpolator")
OrientationInterpolator2026.setKey([0,0.5,1])
OrientationInterpolator2026.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2026)
OrientationInterpolator2027 = OrientationInterpolator()
OrientationInterpolator2027.setDEF("Stop_r_ring0_RotationInterpolator")
OrientationInterpolator2027.setKey([0,0.5,1])
OrientationInterpolator2027.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2027)
OrientationInterpolator2028 = OrientationInterpolator()
OrientationInterpolator2028.setDEF("Stop_r_ring1_RotationInterpolator")
OrientationInterpolator2028.setKey([0,0.5,1])
OrientationInterpolator2028.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2028)
OrientationInterpolator2029 = OrientationInterpolator()
OrientationInterpolator2029.setDEF("Stop_r_ring2_RotationInterpolator")
OrientationInterpolator2029.setKey([0,0.5,1])
OrientationInterpolator2029.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2029)
OrientationInterpolator2030 = OrientationInterpolator()
OrientationInterpolator2030.setDEF("Stop_r_ring3_RotationInterpolator")
OrientationInterpolator2030.setKey([0,0.5,1])
OrientationInterpolator2030.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2030)
OrientationInterpolator2031 = OrientationInterpolator()
OrientationInterpolator2031.setDEF("Stop_r_pinky0_RotationInterpolator")
OrientationInterpolator2031.setKey([0,0.5,1])
OrientationInterpolator2031.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2031)
OrientationInterpolator2032 = OrientationInterpolator()
OrientationInterpolator2032.setDEF("Stop_r_pinky1_RotationInterpolator")
OrientationInterpolator2032.setKey([0,0.5,1])
OrientationInterpolator2032.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2032)
OrientationInterpolator2033 = OrientationInterpolator()
OrientationInterpolator2033.setDEF("Stop_r_pinky2_RotationInterpolator")
OrientationInterpolator2033.setKey([0,0.5,1])
OrientationInterpolator2033.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2033)
OrientationInterpolator2034 = OrientationInterpolator()
OrientationInterpolator2034.setDEF("Stop_r_pinky3_RotationInterpolator")
OrientationInterpolator2034.setKey([0,0.5,1])
OrientationInterpolator2034.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group1943.addChildren(OrientationInterpolator2034)
ROUTE2035 = ROUTE()
ROUTE2035.setFromField("fraction_changed")
ROUTE2035.setFromNode("StopTimer")
ROUTE2035.setToField("set_fraction")
ROUTE2035.setToNode("Stop_HumanoidRoot_TranslationInterpolator")

Group1943.addChildren(ROUTE2035)
ROUTE2036 = ROUTE()
ROUTE2036.setFromField("fraction_changed")
ROUTE2036.setFromNode("StopTimer")
ROUTE2036.setToField("set_fraction")
ROUTE2036.setToNode("Stop_HumanoidRoot_RotationInterpolator")

Group1943.addChildren(ROUTE2036)
ROUTE2037 = ROUTE()
ROUTE2037.setFromField("fraction_changed")
ROUTE2037.setFromNode("StopTimer")
ROUTE2037.setToField("set_fraction")
ROUTE2037.setToNode("Stop_sacroiliac_RotationInterpolator")

Group1943.addChildren(ROUTE2037)
ROUTE2038 = ROUTE()
ROUTE2038.setFromField("fraction_changed")
ROUTE2038.setFromNode("StopTimer")
ROUTE2038.setToField("set_fraction")
ROUTE2038.setToNode("Stop_l_hip_RotationInterpolator")

Group1943.addChildren(ROUTE2038)
ROUTE2039 = ROUTE()
ROUTE2039.setFromField("fraction_changed")
ROUTE2039.setFromNode("StopTimer")
ROUTE2039.setToField("set_fraction")
ROUTE2039.setToNode("Stop_l_knee_RotationInterpolator")

Group1943.addChildren(ROUTE2039)
ROUTE2040 = ROUTE()
ROUTE2040.setFromField("fraction_changed")
ROUTE2040.setFromNode("StopTimer")
ROUTE2040.setToField("set_fraction")
ROUTE2040.setToNode("Stop_l_ankle_RotationInterpolator")

Group1943.addChildren(ROUTE2040)
ROUTE2041 = ROUTE()
ROUTE2041.setFromField("fraction_changed")
ROUTE2041.setFromNode("StopTimer")
ROUTE2041.setToField("set_fraction")
ROUTE2041.setToNode("Stop_l_subtalar_RotationInterpolator")

Group1943.addChildren(ROUTE2041)
ROUTE2042 = ROUTE()
ROUTE2042.setFromField("fraction_changed")
ROUTE2042.setFromNode("StopTimer")
ROUTE2042.setToField("set_fraction")
ROUTE2042.setToNode("Stop_l_midtarsal_RotationInterpolator")

Group1943.addChildren(ROUTE2042)
ROUTE2043 = ROUTE()
ROUTE2043.setFromField("fraction_changed")
ROUTE2043.setFromNode("StopTimer")
ROUTE2043.setToField("set_fraction")
ROUTE2043.setToNode("Stop_l_metatarsal_RotationInterpolator")

Group1943.addChildren(ROUTE2043)
ROUTE2044 = ROUTE()
ROUTE2044.setFromField("fraction_changed")
ROUTE2044.setFromNode("StopTimer")
ROUTE2044.setToField("set_fraction")
ROUTE2044.setToNode("Stop_r_hip_RotationInterpolator")

Group1943.addChildren(ROUTE2044)
ROUTE2045 = ROUTE()
ROUTE2045.setFromField("fraction_changed")
ROUTE2045.setFromNode("StopTimer")
ROUTE2045.setToField("set_fraction")
ROUTE2045.setToNode("Stop_r_knee_RotationInterpolator")

Group1943.addChildren(ROUTE2045)
ROUTE2046 = ROUTE()
ROUTE2046.setFromField("fraction_changed")
ROUTE2046.setFromNode("StopTimer")
ROUTE2046.setToField("set_fraction")
ROUTE2046.setToNode("Stop_r_ankle_RotationInterpolator")

Group1943.addChildren(ROUTE2046)
ROUTE2047 = ROUTE()
ROUTE2047.setFromField("fraction_changed")
ROUTE2047.setFromNode("StopTimer")
ROUTE2047.setToField("set_fraction")
ROUTE2047.setToNode("Stop_r_subtalar_RotationInterpolator")

Group1943.addChildren(ROUTE2047)
ROUTE2048 = ROUTE()
ROUTE2048.setFromField("fraction_changed")
ROUTE2048.setFromNode("StopTimer")
ROUTE2048.setToField("set_fraction")
ROUTE2048.setToNode("Stop_r_midtarsal_RotationInterpolator")

Group1943.addChildren(ROUTE2048)
ROUTE2049 = ROUTE()
ROUTE2049.setFromField("fraction_changed")
ROUTE2049.setFromNode("StopTimer")
ROUTE2049.setToField("set_fraction")
ROUTE2049.setToNode("Stop_r_metatarsal_RotationInterpolator")

Group1943.addChildren(ROUTE2049)
ROUTE2050 = ROUTE()
ROUTE2050.setFromField("fraction_changed")
ROUTE2050.setFromNode("StopTimer")
ROUTE2050.setToField("set_fraction")
ROUTE2050.setToNode("Stop_vl5_RotationInterpolator")

Group1943.addChildren(ROUTE2050)
ROUTE2051 = ROUTE()
ROUTE2051.setFromField("fraction_changed")
ROUTE2051.setFromNode("StopTimer")
ROUTE2051.setToField("set_fraction")
ROUTE2051.setToNode("Stop_vl4_RotationInterpolator")

Group1943.addChildren(ROUTE2051)
ROUTE2052 = ROUTE()
ROUTE2052.setFromField("fraction_changed")
ROUTE2052.setFromNode("StopTimer")
ROUTE2052.setToField("set_fraction")
ROUTE2052.setToNode("Stop_vl3_RotationInterpolator")

Group1943.addChildren(ROUTE2052)
ROUTE2053 = ROUTE()
ROUTE2053.setFromField("fraction_changed")
ROUTE2053.setFromNode("StopTimer")
ROUTE2053.setToField("set_fraction")
ROUTE2053.setToNode("Stop_vl2_RotationInterpolator")

Group1943.addChildren(ROUTE2053)
ROUTE2054 = ROUTE()
ROUTE2054.setFromField("fraction_changed")
ROUTE2054.setFromNode("StopTimer")
ROUTE2054.setToField("set_fraction")
ROUTE2054.setToNode("Stop_vl1_RotationInterpolator")

Group1943.addChildren(ROUTE2054)
ROUTE2055 = ROUTE()
ROUTE2055.setFromField("fraction_changed")
ROUTE2055.setFromNode("StopTimer")
ROUTE2055.setToField("set_fraction")
ROUTE2055.setToNode("Stop_vt12_RotationInterpolator")

Group1943.addChildren(ROUTE2055)
ROUTE2056 = ROUTE()
ROUTE2056.setFromField("fraction_changed")
ROUTE2056.setFromNode("StopTimer")
ROUTE2056.setToField("set_fraction")
ROUTE2056.setToNode("Stop_vt11_RotationInterpolator")

Group1943.addChildren(ROUTE2056)
ROUTE2057 = ROUTE()
ROUTE2057.setFromField("fraction_changed")
ROUTE2057.setFromNode("StopTimer")
ROUTE2057.setToField("set_fraction")
ROUTE2057.setToNode("Stop_vt10_RotationInterpolator")

Group1943.addChildren(ROUTE2057)
ROUTE2058 = ROUTE()
ROUTE2058.setFromField("fraction_changed")
ROUTE2058.setFromNode("StopTimer")
ROUTE2058.setToField("set_fraction")
ROUTE2058.setToNode("Stop_vt9_RotationInterpolator")

Group1943.addChildren(ROUTE2058)
ROUTE2059 = ROUTE()
ROUTE2059.setFromField("fraction_changed")
ROUTE2059.setFromNode("StopTimer")
ROUTE2059.setToField("set_fraction")
ROUTE2059.setToNode("Stop_vt8_RotationInterpolator")

Group1943.addChildren(ROUTE2059)
ROUTE2060 = ROUTE()
ROUTE2060.setFromField("fraction_changed")
ROUTE2060.setFromNode("StopTimer")
ROUTE2060.setToField("set_fraction")
ROUTE2060.setToNode("Stop_vt7_RotationInterpolator")

Group1943.addChildren(ROUTE2060)
ROUTE2061 = ROUTE()
ROUTE2061.setFromField("fraction_changed")
ROUTE2061.setFromNode("StopTimer")
ROUTE2061.setToField("set_fraction")
ROUTE2061.setToNode("Stop_vt6_RotationInterpolator")

Group1943.addChildren(ROUTE2061)
ROUTE2062 = ROUTE()
ROUTE2062.setFromField("fraction_changed")
ROUTE2062.setFromNode("StopTimer")
ROUTE2062.setToField("set_fraction")
ROUTE2062.setToNode("Stop_vt5_RotationInterpolator")

Group1943.addChildren(ROUTE2062)
ROUTE2063 = ROUTE()
ROUTE2063.setFromField("fraction_changed")
ROUTE2063.setFromNode("StopTimer")
ROUTE2063.setToField("set_fraction")
ROUTE2063.setToNode("Stop_vt4_RotationInterpolator")

Group1943.addChildren(ROUTE2063)
ROUTE2064 = ROUTE()
ROUTE2064.setFromField("fraction_changed")
ROUTE2064.setFromNode("StopTimer")
ROUTE2064.setToField("set_fraction")
ROUTE2064.setToNode("Stop_vt3_RotationInterpolator")

Group1943.addChildren(ROUTE2064)
ROUTE2065 = ROUTE()
ROUTE2065.setFromField("fraction_changed")
ROUTE2065.setFromNode("StopTimer")
ROUTE2065.setToField("set_fraction")
ROUTE2065.setToNode("Stop_vt2_RotationInterpolator")

Group1943.addChildren(ROUTE2065)
ROUTE2066 = ROUTE()
ROUTE2066.setFromField("fraction_changed")
ROUTE2066.setFromNode("StopTimer")
ROUTE2066.setToField("set_fraction")
ROUTE2066.setToNode("Stop_vt1_RotationInterpolator")

Group1943.addChildren(ROUTE2066)
ROUTE2067 = ROUTE()
ROUTE2067.setFromField("fraction_changed")
ROUTE2067.setFromNode("StopTimer")
ROUTE2067.setToField("set_fraction")
ROUTE2067.setToNode("Stop_vc7_RotationInterpolator")

Group1943.addChildren(ROUTE2067)
ROUTE2068 = ROUTE()
ROUTE2068.setFromField("fraction_changed")
ROUTE2068.setFromNode("StopTimer")
ROUTE2068.setToField("set_fraction")
ROUTE2068.setToNode("Stop_vc6_RotationInterpolator")

Group1943.addChildren(ROUTE2068)
ROUTE2069 = ROUTE()
ROUTE2069.setFromField("fraction_changed")
ROUTE2069.setFromNode("StopTimer")
ROUTE2069.setToField("set_fraction")
ROUTE2069.setToNode("Stop_vc5_RotationInterpolator")

Group1943.addChildren(ROUTE2069)
ROUTE2070 = ROUTE()
ROUTE2070.setFromField("fraction_changed")
ROUTE2070.setFromNode("StopTimer")
ROUTE2070.setToField("set_fraction")
ROUTE2070.setToNode("Stop_vc4_RotationInterpolator")

Group1943.addChildren(ROUTE2070)
ROUTE2071 = ROUTE()
ROUTE2071.setFromField("fraction_changed")
ROUTE2071.setFromNode("StopTimer")
ROUTE2071.setToField("set_fraction")
ROUTE2071.setToNode("Stop_vc3_RotationInterpolator")

Group1943.addChildren(ROUTE2071)
ROUTE2072 = ROUTE()
ROUTE2072.setFromField("fraction_changed")
ROUTE2072.setFromNode("StopTimer")
ROUTE2072.setToField("set_fraction")
ROUTE2072.setToNode("Stop_vc2_RotationInterpolator")

Group1943.addChildren(ROUTE2072)
ROUTE2073 = ROUTE()
ROUTE2073.setFromField("fraction_changed")
ROUTE2073.setFromNode("StopTimer")
ROUTE2073.setToField("set_fraction")
ROUTE2073.setToNode("Stop_vc1_RotationInterpolator")

Group1943.addChildren(ROUTE2073)
ROUTE2074 = ROUTE()
ROUTE2074.setFromField("fraction_changed")
ROUTE2074.setFromNode("StopTimer")
ROUTE2074.setToField("set_fraction")
ROUTE2074.setToNode("Stop_skullbase_RotationInterpolator")

Group1943.addChildren(ROUTE2074)
ROUTE2075 = ROUTE()
ROUTE2075.setFromField("fraction_changed")
ROUTE2075.setFromNode("StopTimer")
ROUTE2075.setToField("set_fraction")
ROUTE2075.setToNode("Stop_l_eyeball_joint_RotationInterpolator")

Group1943.addChildren(ROUTE2075)
ROUTE2076 = ROUTE()
ROUTE2076.setFromField("fraction_changed")
ROUTE2076.setFromNode("StopTimer")
ROUTE2076.setToField("set_fraction")
ROUTE2076.setToNode("Stop_r_eyeball_joint_RotationInterpolator")

Group1943.addChildren(ROUTE2076)
ROUTE2077 = ROUTE()
ROUTE2077.setFromField("fraction_changed")
ROUTE2077.setFromNode("StopTimer")
ROUTE2077.setToField("set_fraction")
ROUTE2077.setToNode("Stop_l_sternoclavicular_RotationInterpolator")

Group1943.addChildren(ROUTE2077)
ROUTE2078 = ROUTE()
ROUTE2078.setFromField("fraction_changed")
ROUTE2078.setFromNode("StopTimer")
ROUTE2078.setToField("set_fraction")
ROUTE2078.setToNode("Stop_l_acromioclavicular_RotationInterpolator")

Group1943.addChildren(ROUTE2078)
ROUTE2079 = ROUTE()
ROUTE2079.setFromField("fraction_changed")
ROUTE2079.setFromNode("StopTimer")
ROUTE2079.setToField("set_fraction")
ROUTE2079.setToNode("Stop_l_shoulder_RotationInterpolator")

Group1943.addChildren(ROUTE2079)
ROUTE2080 = ROUTE()
ROUTE2080.setFromField("fraction_changed")
ROUTE2080.setFromNode("StopTimer")
ROUTE2080.setToField("set_fraction")
ROUTE2080.setToNode("Stop_l_elbow_RotationInterpolator")

Group1943.addChildren(ROUTE2080)
ROUTE2081 = ROUTE()
ROUTE2081.setFromField("fraction_changed")
ROUTE2081.setFromNode("StopTimer")
ROUTE2081.setToField("set_fraction")
ROUTE2081.setToNode("Stop_l_wrist_RotationInterpolator")

Group1943.addChildren(ROUTE2081)
ROUTE2082 = ROUTE()
ROUTE2082.setFromField("fraction_changed")
ROUTE2082.setFromNode("StopTimer")
ROUTE2082.setToField("set_fraction")
ROUTE2082.setToNode("Stop_l_thumb1_RotationInterpolator")

Group1943.addChildren(ROUTE2082)
ROUTE2083 = ROUTE()
ROUTE2083.setFromField("fraction_changed")
ROUTE2083.setFromNode("StopTimer")
ROUTE2083.setToField("set_fraction")
ROUTE2083.setToNode("Stop_l_thumb2_RotationInterpolator")

Group1943.addChildren(ROUTE2083)
ROUTE2084 = ROUTE()
ROUTE2084.setFromField("fraction_changed")
ROUTE2084.setFromNode("StopTimer")
ROUTE2084.setToField("set_fraction")
ROUTE2084.setToNode("Stop_l_thumb3_RotationInterpolator")

Group1943.addChildren(ROUTE2084)
ROUTE2085 = ROUTE()
ROUTE2085.setFromField("fraction_changed")
ROUTE2085.setFromNode("StopTimer")
ROUTE2085.setToField("set_fraction")
ROUTE2085.setToNode("Stop_l_index0_RotationInterpolator")

Group1943.addChildren(ROUTE2085)
ROUTE2086 = ROUTE()
ROUTE2086.setFromField("fraction_changed")
ROUTE2086.setFromNode("StopTimer")
ROUTE2086.setToField("set_fraction")
ROUTE2086.setToNode("Stop_l_index1_RotationInterpolator")

Group1943.addChildren(ROUTE2086)
ROUTE2087 = ROUTE()
ROUTE2087.setFromField("fraction_changed")
ROUTE2087.setFromNode("StopTimer")
ROUTE2087.setToField("set_fraction")
ROUTE2087.setToNode("Stop_l_index2_RotationInterpolator")

Group1943.addChildren(ROUTE2087)
ROUTE2088 = ROUTE()
ROUTE2088.setFromField("fraction_changed")
ROUTE2088.setFromNode("StopTimer")
ROUTE2088.setToField("set_fraction")
ROUTE2088.setToNode("Stop_l_index3_RotationInterpolator")

Group1943.addChildren(ROUTE2088)
ROUTE2089 = ROUTE()
ROUTE2089.setFromField("fraction_changed")
ROUTE2089.setFromNode("StopTimer")
ROUTE2089.setToField("set_fraction")
ROUTE2089.setToNode("Stop_l_middle0_RotationInterpolator")

Group1943.addChildren(ROUTE2089)
ROUTE2090 = ROUTE()
ROUTE2090.setFromField("fraction_changed")
ROUTE2090.setFromNode("StopTimer")
ROUTE2090.setToField("set_fraction")
ROUTE2090.setToNode("Stop_l_middle1_RotationInterpolator")

Group1943.addChildren(ROUTE2090)
ROUTE2091 = ROUTE()
ROUTE2091.setFromField("fraction_changed")
ROUTE2091.setFromNode("StopTimer")
ROUTE2091.setToField("set_fraction")
ROUTE2091.setToNode("Stop_l_middle2_RotationInterpolator")

Group1943.addChildren(ROUTE2091)
ROUTE2092 = ROUTE()
ROUTE2092.setFromField("fraction_changed")
ROUTE2092.setFromNode("StopTimer")
ROUTE2092.setToField("set_fraction")
ROUTE2092.setToNode("Stop_l_middle3_RotationInterpolator")

Group1943.addChildren(ROUTE2092)
ROUTE2093 = ROUTE()
ROUTE2093.setFromField("fraction_changed")
ROUTE2093.setFromNode("StopTimer")
ROUTE2093.setToField("set_fraction")
ROUTE2093.setToNode("Stop_l_ring0_RotationInterpolator")

Group1943.addChildren(ROUTE2093)
ROUTE2094 = ROUTE()
ROUTE2094.setFromField("fraction_changed")
ROUTE2094.setFromNode("StopTimer")
ROUTE2094.setToField("set_fraction")
ROUTE2094.setToNode("Stop_l_ring1_RotationInterpolator")

Group1943.addChildren(ROUTE2094)
ROUTE2095 = ROUTE()
ROUTE2095.setFromField("fraction_changed")
ROUTE2095.setFromNode("StopTimer")
ROUTE2095.setToField("set_fraction")
ROUTE2095.setToNode("Stop_l_ring2_RotationInterpolator")

Group1943.addChildren(ROUTE2095)
ROUTE2096 = ROUTE()
ROUTE2096.setFromField("fraction_changed")
ROUTE2096.setFromNode("StopTimer")
ROUTE2096.setToField("set_fraction")
ROUTE2096.setToNode("Stop_l_ring3_RotationInterpolator")

Group1943.addChildren(ROUTE2096)
ROUTE2097 = ROUTE()
ROUTE2097.setFromField("fraction_changed")
ROUTE2097.setFromNode("StopTimer")
ROUTE2097.setToField("set_fraction")
ROUTE2097.setToNode("Stop_l_pinky0_RotationInterpolator")

Group1943.addChildren(ROUTE2097)
ROUTE2098 = ROUTE()
ROUTE2098.setFromField("fraction_changed")
ROUTE2098.setFromNode("StopTimer")
ROUTE2098.setToField("set_fraction")
ROUTE2098.setToNode("Stop_l_pinky1_RotationInterpolator")

Group1943.addChildren(ROUTE2098)
ROUTE2099 = ROUTE()
ROUTE2099.setFromField("fraction_changed")
ROUTE2099.setFromNode("StopTimer")
ROUTE2099.setToField("set_fraction")
ROUTE2099.setToNode("Stop_l_pinky2_RotationInterpolator")

Group1943.addChildren(ROUTE2099)
ROUTE2100 = ROUTE()
ROUTE2100.setFromField("fraction_changed")
ROUTE2100.setFromNode("StopTimer")
ROUTE2100.setToField("set_fraction")
ROUTE2100.setToNode("Stop_l_pinky3_RotationInterpolator")

Group1943.addChildren(ROUTE2100)
ROUTE2101 = ROUTE()
ROUTE2101.setFromField("fraction_changed")
ROUTE2101.setFromNode("StopTimer")
ROUTE2101.setToField("set_fraction")
ROUTE2101.setToNode("Stop_r_sternoclavicular_RotationInterpolator")

Group1943.addChildren(ROUTE2101)
ROUTE2102 = ROUTE()
ROUTE2102.setFromField("fraction_changed")
ROUTE2102.setFromNode("StopTimer")
ROUTE2102.setToField("set_fraction")
ROUTE2102.setToNode("Stop_r_acromioclavicular_RotationInterpolator")

Group1943.addChildren(ROUTE2102)
ROUTE2103 = ROUTE()
ROUTE2103.setFromField("fraction_changed")
ROUTE2103.setFromNode("StopTimer")
ROUTE2103.setToField("set_fraction")
ROUTE2103.setToNode("Stop_r_shoulder_RotationInterpolator")

Group1943.addChildren(ROUTE2103)
ROUTE2104 = ROUTE()
ROUTE2104.setFromField("fraction_changed")
ROUTE2104.setFromNode("StopTimer")
ROUTE2104.setToField("set_fraction")
ROUTE2104.setToNode("Stop_r_elbow_RotationInterpolator")

Group1943.addChildren(ROUTE2104)
ROUTE2105 = ROUTE()
ROUTE2105.setFromField("fraction_changed")
ROUTE2105.setFromNode("StopTimer")
ROUTE2105.setToField("set_fraction")
ROUTE2105.setToNode("Stop_r_wrist_RotationInterpolator")

Group1943.addChildren(ROUTE2105)
ROUTE2106 = ROUTE()
ROUTE2106.setFromField("fraction_changed")
ROUTE2106.setFromNode("StopTimer")
ROUTE2106.setToField("set_fraction")
ROUTE2106.setToNode("Stop_r_thumb1_RotationInterpolator")

Group1943.addChildren(ROUTE2106)
ROUTE2107 = ROUTE()
ROUTE2107.setFromField("fraction_changed")
ROUTE2107.setFromNode("StopTimer")
ROUTE2107.setToField("set_fraction")
ROUTE2107.setToNode("Stop_r_thumb2_RotationInterpolator")

Group1943.addChildren(ROUTE2107)
ROUTE2108 = ROUTE()
ROUTE2108.setFromField("fraction_changed")
ROUTE2108.setFromNode("StopTimer")
ROUTE2108.setToField("set_fraction")
ROUTE2108.setToNode("Stop_r_thumb3_RotationInterpolator")

Group1943.addChildren(ROUTE2108)
ROUTE2109 = ROUTE()
ROUTE2109.setFromField("fraction_changed")
ROUTE2109.setFromNode("StopTimer")
ROUTE2109.setToField("set_fraction")
ROUTE2109.setToNode("Stop_r_index0_RotationInterpolator")

Group1943.addChildren(ROUTE2109)
ROUTE2110 = ROUTE()
ROUTE2110.setFromField("fraction_changed")
ROUTE2110.setFromNode("StopTimer")
ROUTE2110.setToField("set_fraction")
ROUTE2110.setToNode("Stop_r_index1_RotationInterpolator")

Group1943.addChildren(ROUTE2110)
ROUTE2111 = ROUTE()
ROUTE2111.setFromField("fraction_changed")
ROUTE2111.setFromNode("StopTimer")
ROUTE2111.setToField("set_fraction")
ROUTE2111.setToNode("Stop_r_index2_RotationInterpolator")

Group1943.addChildren(ROUTE2111)
ROUTE2112 = ROUTE()
ROUTE2112.setFromField("fraction_changed")
ROUTE2112.setFromNode("StopTimer")
ROUTE2112.setToField("set_fraction")
ROUTE2112.setToNode("Stop_r_index3_RotationInterpolator")

Group1943.addChildren(ROUTE2112)
ROUTE2113 = ROUTE()
ROUTE2113.setFromField("fraction_changed")
ROUTE2113.setFromNode("StopTimer")
ROUTE2113.setToField("set_fraction")
ROUTE2113.setToNode("Stop_r_middle0_RotationInterpolator")

Group1943.addChildren(ROUTE2113)
ROUTE2114 = ROUTE()
ROUTE2114.setFromField("fraction_changed")
ROUTE2114.setFromNode("StopTimer")
ROUTE2114.setToField("set_fraction")
ROUTE2114.setToNode("Stop_r_middle1_RotationInterpolator")

Group1943.addChildren(ROUTE2114)
ROUTE2115 = ROUTE()
ROUTE2115.setFromField("fraction_changed")
ROUTE2115.setFromNode("StopTimer")
ROUTE2115.setToField("set_fraction")
ROUTE2115.setToNode("Stop_r_middle2_RotationInterpolator")

Group1943.addChildren(ROUTE2115)
ROUTE2116 = ROUTE()
ROUTE2116.setFromField("fraction_changed")
ROUTE2116.setFromNode("StopTimer")
ROUTE2116.setToField("set_fraction")
ROUTE2116.setToNode("Stop_r_middle3_RotationInterpolator")

Group1943.addChildren(ROUTE2116)
ROUTE2117 = ROUTE()
ROUTE2117.setFromField("fraction_changed")
ROUTE2117.setFromNode("StopTimer")
ROUTE2117.setToField("set_fraction")
ROUTE2117.setToNode("Stop_r_ring0_RotationInterpolator")

Group1943.addChildren(ROUTE2117)
ROUTE2118 = ROUTE()
ROUTE2118.setFromField("fraction_changed")
ROUTE2118.setFromNode("StopTimer")
ROUTE2118.setToField("set_fraction")
ROUTE2118.setToNode("Stop_r_ring1_RotationInterpolator")

Group1943.addChildren(ROUTE2118)
ROUTE2119 = ROUTE()
ROUTE2119.setFromField("fraction_changed")
ROUTE2119.setFromNode("StopTimer")
ROUTE2119.setToField("set_fraction")
ROUTE2119.setToNode("Stop_r_ring2_RotationInterpolator")

Group1943.addChildren(ROUTE2119)
ROUTE2120 = ROUTE()
ROUTE2120.setFromField("fraction_changed")
ROUTE2120.setFromNode("StopTimer")
ROUTE2120.setToField("set_fraction")
ROUTE2120.setToNode("Stop_r_ring3_RotationInterpolator")

Group1943.addChildren(ROUTE2120)
ROUTE2121 = ROUTE()
ROUTE2121.setFromField("fraction_changed")
ROUTE2121.setFromNode("StopTimer")
ROUTE2121.setToField("set_fraction")
ROUTE2121.setToNode("Stop_r_pinky0_RotationInterpolator")

Group1943.addChildren(ROUTE2121)
ROUTE2122 = ROUTE()
ROUTE2122.setFromField("fraction_changed")
ROUTE2122.setFromNode("StopTimer")
ROUTE2122.setToField("set_fraction")
ROUTE2122.setToNode("Stop_r_pinky1_RotationInterpolator")

Group1943.addChildren(ROUTE2122)
ROUTE2123 = ROUTE()
ROUTE2123.setFromField("fraction_changed")
ROUTE2123.setFromNode("StopTimer")
ROUTE2123.setToField("set_fraction")
ROUTE2123.setToNode("Stop_r_pinky2_RotationInterpolator")

Group1943.addChildren(ROUTE2123)
ROUTE2124 = ROUTE()
ROUTE2124.setFromField("fraction_changed")
ROUTE2124.setFromNode("StopTimer")
ROUTE2124.setToField("set_fraction")
ROUTE2124.setToNode("Stop_r_pinky3_RotationInterpolator")

Group1943.addChildren(ROUTE2124)
ROUTE2125 = ROUTE()
ROUTE2125.setFromField("value_changed")
ROUTE2125.setFromNode("Stop_HumanoidRoot_TranslationInterpolator")
ROUTE2125.setToField("translation")
ROUTE2125.setToNode("hanim_humanoid_root")

Group1943.addChildren(ROUTE2125)
ROUTE2126 = ROUTE()
ROUTE2126.setFromField("value_changed")
ROUTE2126.setFromNode("Stop_HumanoidRoot_RotationInterpolator")
ROUTE2126.setToField("rotation")
ROUTE2126.setToNode("hanim_humanoid_root")

Group1943.addChildren(ROUTE2126)
ROUTE2127 = ROUTE()
ROUTE2127.setFromField("value_changed")
ROUTE2127.setFromNode("Stop_sacroiliac_RotationInterpolator")
ROUTE2127.setToField("rotation")
ROUTE2127.setToNode("hanim_sacroiliac")

Group1943.addChildren(ROUTE2127)
ROUTE2128 = ROUTE()
ROUTE2128.setFromField("value_changed")
ROUTE2128.setFromNode("Stop_l_hip_RotationInterpolator")
ROUTE2128.setToField("rotation")
ROUTE2128.setToNode("hanim_l_hip")

Group1943.addChildren(ROUTE2128)
ROUTE2129 = ROUTE()
ROUTE2129.setFromField("value_changed")
ROUTE2129.setFromNode("Stop_l_knee_RotationInterpolator")
ROUTE2129.setToField("rotation")
ROUTE2129.setToNode("hanim_l_knee")

Group1943.addChildren(ROUTE2129)
ROUTE2130 = ROUTE()
ROUTE2130.setFromField("value_changed")
ROUTE2130.setFromNode("Stop_l_ankle_RotationInterpolator")
ROUTE2130.setToField("rotation")
ROUTE2130.setToNode("hanim_l_ankle")

Group1943.addChildren(ROUTE2130)
ROUTE2131 = ROUTE()
ROUTE2131.setFromField("value_changed")
ROUTE2131.setFromNode("Stop_l_subtalar_RotationInterpolator")
ROUTE2131.setToField("rotation")
ROUTE2131.setToNode("hanim_l_subtalar")

Group1943.addChildren(ROUTE2131)
ROUTE2132 = ROUTE()
ROUTE2132.setFromField("value_changed")
ROUTE2132.setFromNode("Stop_l_midtarsal_RotationInterpolator")
ROUTE2132.setToField("rotation")
ROUTE2132.setToNode("hanim_l_midtarsal")

Group1943.addChildren(ROUTE2132)
ROUTE2133 = ROUTE()
ROUTE2133.setFromField("value_changed")
ROUTE2133.setFromNode("Stop_l_metatarsal_RotationInterpolator")
ROUTE2133.setToField("rotation")
ROUTE2133.setToNode("hanim_l_metatarsal")

Group1943.addChildren(ROUTE2133)
ROUTE2134 = ROUTE()
ROUTE2134.setFromField("value_changed")
ROUTE2134.setFromNode("Stop_r_hip_RotationInterpolator")
ROUTE2134.setToField("rotation")
ROUTE2134.setToNode("hanim_r_hip")

Group1943.addChildren(ROUTE2134)
ROUTE2135 = ROUTE()
ROUTE2135.setFromField("value_changed")
ROUTE2135.setFromNode("Stop_r_knee_RotationInterpolator")
ROUTE2135.setToField("rotation")
ROUTE2135.setToNode("hanim_r_knee")

Group1943.addChildren(ROUTE2135)
ROUTE2136 = ROUTE()
ROUTE2136.setFromField("value_changed")
ROUTE2136.setFromNode("Stop_r_ankle_RotationInterpolator")
ROUTE2136.setToField("rotation")
ROUTE2136.setToNode("hanim_r_ankle")

Group1943.addChildren(ROUTE2136)
ROUTE2137 = ROUTE()
ROUTE2137.setFromField("value_changed")
ROUTE2137.setFromNode("Stop_r_subtalar_RotationInterpolator")
ROUTE2137.setToField("rotation")
ROUTE2137.setToNode("hanim_r_subtalar")

Group1943.addChildren(ROUTE2137)
ROUTE2138 = ROUTE()
ROUTE2138.setFromField("value_changed")
ROUTE2138.setFromNode("Stop_r_midtarsal_RotationInterpolator")
ROUTE2138.setToField("rotation")
ROUTE2138.setToNode("hanim_r_midtarsal")

Group1943.addChildren(ROUTE2138)
ROUTE2139 = ROUTE()
ROUTE2139.setFromField("value_changed")
ROUTE2139.setFromNode("Stop_r_metatarsal_RotationInterpolator")
ROUTE2139.setToField("rotation")
ROUTE2139.setToNode("hanim_r_metatarsal")

Group1943.addChildren(ROUTE2139)
ROUTE2140 = ROUTE()
ROUTE2140.setFromField("value_changed")
ROUTE2140.setFromNode("Stop_vl5_RotationInterpolator")
ROUTE2140.setToField("rotation")
ROUTE2140.setToNode("hanim_vl5")

Group1943.addChildren(ROUTE2140)
ROUTE2141 = ROUTE()
ROUTE2141.setFromField("value_changed")
ROUTE2141.setFromNode("Stop_vl4_RotationInterpolator")
ROUTE2141.setToField("rotation")
ROUTE2141.setToNode("hanim_vl4")

Group1943.addChildren(ROUTE2141)
ROUTE2142 = ROUTE()
ROUTE2142.setFromField("value_changed")
ROUTE2142.setFromNode("Stop_vl3_RotationInterpolator")
ROUTE2142.setToField("rotation")
ROUTE2142.setToNode("hanim_vl3")

Group1943.addChildren(ROUTE2142)
ROUTE2143 = ROUTE()
ROUTE2143.setFromField("value_changed")
ROUTE2143.setFromNode("Stop_vl2_RotationInterpolator")
ROUTE2143.setToField("rotation")
ROUTE2143.setToNode("hanim_vl2")

Group1943.addChildren(ROUTE2143)
ROUTE2144 = ROUTE()
ROUTE2144.setFromField("value_changed")
ROUTE2144.setFromNode("Stop_vl1_RotationInterpolator")
ROUTE2144.setToField("rotation")
ROUTE2144.setToNode("hanim_vl1")

Group1943.addChildren(ROUTE2144)
ROUTE2145 = ROUTE()
ROUTE2145.setFromField("value_changed")
ROUTE2145.setFromNode("Stop_vt12_RotationInterpolator")
ROUTE2145.setToField("rotation")
ROUTE2145.setToNode("hanim_vt12")

Group1943.addChildren(ROUTE2145)
ROUTE2146 = ROUTE()
ROUTE2146.setFromField("value_changed")
ROUTE2146.setFromNode("Stop_vt11_RotationInterpolator")
ROUTE2146.setToField("rotation")
ROUTE2146.setToNode("hanim_vt11")

Group1943.addChildren(ROUTE2146)
ROUTE2147 = ROUTE()
ROUTE2147.setFromField("value_changed")
ROUTE2147.setFromNode("Stop_vt10_RotationInterpolator")
ROUTE2147.setToField("rotation")
ROUTE2147.setToNode("hanim_vt10")

Group1943.addChildren(ROUTE2147)
ROUTE2148 = ROUTE()
ROUTE2148.setFromField("value_changed")
ROUTE2148.setFromNode("Stop_vt9_RotationInterpolator")
ROUTE2148.setToField("rotation")
ROUTE2148.setToNode("hanim_vt9")

Group1943.addChildren(ROUTE2148)
ROUTE2149 = ROUTE()
ROUTE2149.setFromField("value_changed")
ROUTE2149.setFromNode("Stop_vt8_RotationInterpolator")
ROUTE2149.setToField("rotation")
ROUTE2149.setToNode("hanim_vt8")

Group1943.addChildren(ROUTE2149)
ROUTE2150 = ROUTE()
ROUTE2150.setFromField("value_changed")
ROUTE2150.setFromNode("Stop_vt7_RotationInterpolator")
ROUTE2150.setToField("rotation")
ROUTE2150.setToNode("hanim_vt7")

Group1943.addChildren(ROUTE2150)
ROUTE2151 = ROUTE()
ROUTE2151.setFromField("value_changed")
ROUTE2151.setFromNode("Stop_vt6_RotationInterpolator")
ROUTE2151.setToField("rotation")
ROUTE2151.setToNode("hanim_vt6")

Group1943.addChildren(ROUTE2151)
ROUTE2152 = ROUTE()
ROUTE2152.setFromField("value_changed")
ROUTE2152.setFromNode("Stop_vt5_RotationInterpolator")
ROUTE2152.setToField("rotation")
ROUTE2152.setToNode("hanim_vt5")

Group1943.addChildren(ROUTE2152)
ROUTE2153 = ROUTE()
ROUTE2153.setFromField("value_changed")
ROUTE2153.setFromNode("Stop_vt4_RotationInterpolator")
ROUTE2153.setToField("rotation")
ROUTE2153.setToNode("hanim_vt4")

Group1943.addChildren(ROUTE2153)
ROUTE2154 = ROUTE()
ROUTE2154.setFromField("value_changed")
ROUTE2154.setFromNode("Stop_vt3_RotationInterpolator")
ROUTE2154.setToField("rotation")
ROUTE2154.setToNode("hanim_vt3")

Group1943.addChildren(ROUTE2154)
ROUTE2155 = ROUTE()
ROUTE2155.setFromField("value_changed")
ROUTE2155.setFromNode("Stop_vt2_RotationInterpolator")
ROUTE2155.setToField("rotation")
ROUTE2155.setToNode("hanim_vt2")

Group1943.addChildren(ROUTE2155)
ROUTE2156 = ROUTE()
ROUTE2156.setFromField("value_changed")
ROUTE2156.setFromNode("Stop_vt1_RotationInterpolator")
ROUTE2156.setToField("rotation")
ROUTE2156.setToNode("hanim_vt1")

Group1943.addChildren(ROUTE2156)
ROUTE2157 = ROUTE()
ROUTE2157.setFromField("value_changed")
ROUTE2157.setFromNode("Stop_vc7_RotationInterpolator")
ROUTE2157.setToField("rotation")
ROUTE2157.setToNode("hanim_vc7")

Group1943.addChildren(ROUTE2157)
ROUTE2158 = ROUTE()
ROUTE2158.setFromField("value_changed")
ROUTE2158.setFromNode("Stop_vc6_RotationInterpolator")
ROUTE2158.setToField("rotation")
ROUTE2158.setToNode("hanim_vc6")

Group1943.addChildren(ROUTE2158)
ROUTE2159 = ROUTE()
ROUTE2159.setFromField("value_changed")
ROUTE2159.setFromNode("Stop_vc5_RotationInterpolator")
ROUTE2159.setToField("rotation")
ROUTE2159.setToNode("hanim_vc5")

Group1943.addChildren(ROUTE2159)
ROUTE2160 = ROUTE()
ROUTE2160.setFromField("value_changed")
ROUTE2160.setFromNode("Stop_vc4_RotationInterpolator")
ROUTE2160.setToField("rotation")
ROUTE2160.setToNode("hanim_vc4")

Group1943.addChildren(ROUTE2160)
ROUTE2161 = ROUTE()
ROUTE2161.setFromField("value_changed")
ROUTE2161.setFromNode("Stop_vc3_RotationInterpolator")
ROUTE2161.setToField("rotation")
ROUTE2161.setToNode("hanim_vc3")

Group1943.addChildren(ROUTE2161)
ROUTE2162 = ROUTE()
ROUTE2162.setFromField("value_changed")
ROUTE2162.setFromNode("Stop_vc2_RotationInterpolator")
ROUTE2162.setToField("rotation")
ROUTE2162.setToNode("hanim_vc2")

Group1943.addChildren(ROUTE2162)
ROUTE2163 = ROUTE()
ROUTE2163.setFromField("value_changed")
ROUTE2163.setFromNode("Stop_vc1_RotationInterpolator")
ROUTE2163.setToField("rotation")
ROUTE2163.setToNode("hanim_vc1")

Group1943.addChildren(ROUTE2163)
ROUTE2164 = ROUTE()
ROUTE2164.setFromField("value_changed")
ROUTE2164.setFromNode("Stop_skullbase_RotationInterpolator")
ROUTE2164.setToField("rotation")
ROUTE2164.setToNode("hanim_skullbase")

Group1943.addChildren(ROUTE2164)
ROUTE2165 = ROUTE()
ROUTE2165.setFromField("value_changed")
ROUTE2165.setFromNode("Stop_l_eyeball_joint_RotationInterpolator")
ROUTE2165.setToField("rotation")
ROUTE2165.setToNode("hanim_l_eyeball_joint")

Group1943.addChildren(ROUTE2165)
ROUTE2166 = ROUTE()
ROUTE2166.setFromField("value_changed")
ROUTE2166.setFromNode("Stop_r_eyeball_joint_RotationInterpolator")
ROUTE2166.setToField("rotation")
ROUTE2166.setToNode("hanim_r_eyeball_joint")

Group1943.addChildren(ROUTE2166)
ROUTE2167 = ROUTE()
ROUTE2167.setFromField("value_changed")
ROUTE2167.setFromNode("Stop_l_sternoclavicular_RotationInterpolator")
ROUTE2167.setToField("rotation")
ROUTE2167.setToNode("hanim_l_sternoclavicular")

Group1943.addChildren(ROUTE2167)
ROUTE2168 = ROUTE()
ROUTE2168.setFromField("value_changed")
ROUTE2168.setFromNode("Stop_l_acromioclavicular_RotationInterpolator")
ROUTE2168.setToField("rotation")
ROUTE2168.setToNode("hanim_l_acromioclavicular")

Group1943.addChildren(ROUTE2168)
ROUTE2169 = ROUTE()
ROUTE2169.setFromField("value_changed")
ROUTE2169.setFromNode("Stop_l_shoulder_RotationInterpolator")
ROUTE2169.setToField("rotation")
ROUTE2169.setToNode("hanim_l_shoulder")

Group1943.addChildren(ROUTE2169)
ROUTE2170 = ROUTE()
ROUTE2170.setFromField("value_changed")
ROUTE2170.setFromNode("Stop_l_elbow_RotationInterpolator")
ROUTE2170.setToField("rotation")
ROUTE2170.setToNode("hanim_l_elbow")

Group1943.addChildren(ROUTE2170)
ROUTE2171 = ROUTE()
ROUTE2171.setFromField("value_changed")
ROUTE2171.setFromNode("Stop_l_wrist_RotationInterpolator")
ROUTE2171.setToField("rotation")
ROUTE2171.setToNode("hanim_l_wrist")

Group1943.addChildren(ROUTE2171)
ROUTE2172 = ROUTE()
ROUTE2172.setFromField("value_changed")
ROUTE2172.setFromNode("Stop_l_thumb1_RotationInterpolator")
ROUTE2172.setToField("rotation")
ROUTE2172.setToNode("hanim_l_thumb1")

Group1943.addChildren(ROUTE2172)
ROUTE2173 = ROUTE()
ROUTE2173.setFromField("value_changed")
ROUTE2173.setFromNode("Stop_l_thumb2_RotationInterpolator")
ROUTE2173.setToField("rotation")
ROUTE2173.setToNode("hanim_l_thumb2")

Group1943.addChildren(ROUTE2173)
ROUTE2174 = ROUTE()
ROUTE2174.setFromField("value_changed")
ROUTE2174.setFromNode("Stop_l_thumb3_RotationInterpolator")
ROUTE2174.setToField("rotation")
ROUTE2174.setToNode("hanim_l_thumb3")

Group1943.addChildren(ROUTE2174)
ROUTE2175 = ROUTE()
ROUTE2175.setFromField("value_changed")
ROUTE2175.setFromNode("Stop_l_index0_RotationInterpolator")
ROUTE2175.setToField("rotation")
ROUTE2175.setToNode("hanim_l_index0")

Group1943.addChildren(ROUTE2175)
ROUTE2176 = ROUTE()
ROUTE2176.setFromField("value_changed")
ROUTE2176.setFromNode("Stop_l_index1_RotationInterpolator")
ROUTE2176.setToField("rotation")
ROUTE2176.setToNode("hanim_l_index1")

Group1943.addChildren(ROUTE2176)
ROUTE2177 = ROUTE()
ROUTE2177.setFromField("value_changed")
ROUTE2177.setFromNode("Stop_l_index2_RotationInterpolator")
ROUTE2177.setToField("rotation")
ROUTE2177.setToNode("hanim_l_index2")

Group1943.addChildren(ROUTE2177)
ROUTE2178 = ROUTE()
ROUTE2178.setFromField("value_changed")
ROUTE2178.setFromNode("Stop_l_index3_RotationInterpolator")
ROUTE2178.setToField("rotation")
ROUTE2178.setToNode("hanim_l_index3")

Group1943.addChildren(ROUTE2178)
ROUTE2179 = ROUTE()
ROUTE2179.setFromField("value_changed")
ROUTE2179.setFromNode("Stop_l_middle0_RotationInterpolator")
ROUTE2179.setToField("rotation")
ROUTE2179.setToNode("hanim_l_middle0")

Group1943.addChildren(ROUTE2179)
ROUTE2180 = ROUTE()
ROUTE2180.setFromField("value_changed")
ROUTE2180.setFromNode("Stop_l_middle1_RotationInterpolator")
ROUTE2180.setToField("rotation")
ROUTE2180.setToNode("hanim_l_middle1")

Group1943.addChildren(ROUTE2180)
ROUTE2181 = ROUTE()
ROUTE2181.setFromField("value_changed")
ROUTE2181.setFromNode("Stop_l_middle2_RotationInterpolator")
ROUTE2181.setToField("rotation")
ROUTE2181.setToNode("hanim_l_middle2")

Group1943.addChildren(ROUTE2181)
ROUTE2182 = ROUTE()
ROUTE2182.setFromField("value_changed")
ROUTE2182.setFromNode("Stop_l_middle3_RotationInterpolator")
ROUTE2182.setToField("rotation")
ROUTE2182.setToNode("hanim_l_middle3")

Group1943.addChildren(ROUTE2182)
ROUTE2183 = ROUTE()
ROUTE2183.setFromField("value_changed")
ROUTE2183.setFromNode("Stop_l_ring0_RotationInterpolator")
ROUTE2183.setToField("rotation")
ROUTE2183.setToNode("hanim_l_ring0")

Group1943.addChildren(ROUTE2183)
ROUTE2184 = ROUTE()
ROUTE2184.setFromField("value_changed")
ROUTE2184.setFromNode("Stop_l_ring1_RotationInterpolator")
ROUTE2184.setToField("rotation")
ROUTE2184.setToNode("hanim_l_ring1")

Group1943.addChildren(ROUTE2184)
ROUTE2185 = ROUTE()
ROUTE2185.setFromField("value_changed")
ROUTE2185.setFromNode("Stop_l_ring2_RotationInterpolator")
ROUTE2185.setToField("rotation")
ROUTE2185.setToNode("hanim_l_ring2")

Group1943.addChildren(ROUTE2185)
ROUTE2186 = ROUTE()
ROUTE2186.setFromField("value_changed")
ROUTE2186.setFromNode("Stop_l_ring3_RotationInterpolator")
ROUTE2186.setToField("rotation")
ROUTE2186.setToNode("hanim_l_ring3")

Group1943.addChildren(ROUTE2186)
ROUTE2187 = ROUTE()
ROUTE2187.setFromField("value_changed")
ROUTE2187.setFromNode("Stop_l_pinky0_RotationInterpolator")
ROUTE2187.setToField("rotation")
ROUTE2187.setToNode("hanim_l_pinky0")

Group1943.addChildren(ROUTE2187)
ROUTE2188 = ROUTE()
ROUTE2188.setFromField("value_changed")
ROUTE2188.setFromNode("Stop_l_pinky1_RotationInterpolator")
ROUTE2188.setToField("rotation")
ROUTE2188.setToNode("hanim_l_pinky1")

Group1943.addChildren(ROUTE2188)
ROUTE2189 = ROUTE()
ROUTE2189.setFromField("value_changed")
ROUTE2189.setFromNode("Stop_l_pinky2_RotationInterpolator")
ROUTE2189.setToField("rotation")
ROUTE2189.setToNode("hanim_l_pinky2")

Group1943.addChildren(ROUTE2189)
ROUTE2190 = ROUTE()
ROUTE2190.setFromField("value_changed")
ROUTE2190.setFromNode("Stop_l_pinky3_RotationInterpolator")
ROUTE2190.setToField("rotation")
ROUTE2190.setToNode("hanim_l_pinky3")

Group1943.addChildren(ROUTE2190)
ROUTE2191 = ROUTE()
ROUTE2191.setFromField("value_changed")
ROUTE2191.setFromNode("Stop_r_sternoclavicular_RotationInterpolator")
ROUTE2191.setToField("rotation")
ROUTE2191.setToNode("hanim_r_sternoclavicular")

Group1943.addChildren(ROUTE2191)
ROUTE2192 = ROUTE()
ROUTE2192.setFromField("value_changed")
ROUTE2192.setFromNode("Stop_r_acromioclavicular_RotationInterpolator")
ROUTE2192.setToField("rotation")
ROUTE2192.setToNode("hanim_r_acromioclavicular")

Group1943.addChildren(ROUTE2192)
ROUTE2193 = ROUTE()
ROUTE2193.setFromField("value_changed")
ROUTE2193.setFromNode("Stop_r_shoulder_RotationInterpolator")
ROUTE2193.setToField("rotation")
ROUTE2193.setToNode("hanim_r_shoulder")

Group1943.addChildren(ROUTE2193)
ROUTE2194 = ROUTE()
ROUTE2194.setFromField("value_changed")
ROUTE2194.setFromNode("Stop_r_elbow_RotationInterpolator")
ROUTE2194.setToField("rotation")
ROUTE2194.setToNode("hanim_r_elbow")

Group1943.addChildren(ROUTE2194)
ROUTE2195 = ROUTE()
ROUTE2195.setFromField("value_changed")
ROUTE2195.setFromNode("Stop_r_wrist_RotationInterpolator")
ROUTE2195.setToField("rotation")
ROUTE2195.setToNode("hanim_r_wrist")

Group1943.addChildren(ROUTE2195)
ROUTE2196 = ROUTE()
ROUTE2196.setFromField("value_changed")
ROUTE2196.setFromNode("Stop_r_thumb1_RotationInterpolator")
ROUTE2196.setToField("rotation")
ROUTE2196.setToNode("hanim_r_thumb1")

Group1943.addChildren(ROUTE2196)
ROUTE2197 = ROUTE()
ROUTE2197.setFromField("value_changed")
ROUTE2197.setFromNode("Stop_r_thumb2_RotationInterpolator")
ROUTE2197.setToField("rotation")
ROUTE2197.setToNode("hanim_r_thumb2")

Group1943.addChildren(ROUTE2197)
ROUTE2198 = ROUTE()
ROUTE2198.setFromField("value_changed")
ROUTE2198.setFromNode("Stop_r_thumb3_RotationInterpolator")
ROUTE2198.setToField("rotation")
ROUTE2198.setToNode("hanim_r_thumb3")

Group1943.addChildren(ROUTE2198)
ROUTE2199 = ROUTE()
ROUTE2199.setFromField("value_changed")
ROUTE2199.setFromNode("Stop_r_index0_RotationInterpolator")
ROUTE2199.setToField("rotation")
ROUTE2199.setToNode("hanim_r_index0")

Group1943.addChildren(ROUTE2199)
ROUTE2200 = ROUTE()
ROUTE2200.setFromField("value_changed")
ROUTE2200.setFromNode("Stop_r_index1_RotationInterpolator")
ROUTE2200.setToField("rotation")
ROUTE2200.setToNode("hanim_r_index1")

Group1943.addChildren(ROUTE2200)
ROUTE2201 = ROUTE()
ROUTE2201.setFromField("value_changed")
ROUTE2201.setFromNode("Stop_r_index2_RotationInterpolator")
ROUTE2201.setToField("rotation")
ROUTE2201.setToNode("hanim_r_index2")

Group1943.addChildren(ROUTE2201)
ROUTE2202 = ROUTE()
ROUTE2202.setFromField("value_changed")
ROUTE2202.setFromNode("Stop_r_index3_RotationInterpolator")
ROUTE2202.setToField("rotation")
ROUTE2202.setToNode("hanim_r_index3")

Group1943.addChildren(ROUTE2202)
ROUTE2203 = ROUTE()
ROUTE2203.setFromField("value_changed")
ROUTE2203.setFromNode("Stop_r_middle0_RotationInterpolator")
ROUTE2203.setToField("rotation")
ROUTE2203.setToNode("hanim_r_middle0")

Group1943.addChildren(ROUTE2203)
ROUTE2204 = ROUTE()
ROUTE2204.setFromField("value_changed")
ROUTE2204.setFromNode("Stop_r_middle1_RotationInterpolator")
ROUTE2204.setToField("rotation")
ROUTE2204.setToNode("hanim_r_middle1")

Group1943.addChildren(ROUTE2204)
ROUTE2205 = ROUTE()
ROUTE2205.setFromField("value_changed")
ROUTE2205.setFromNode("Stop_r_middle2_RotationInterpolator")
ROUTE2205.setToField("rotation")
ROUTE2205.setToNode("hanim_r_middle2")

Group1943.addChildren(ROUTE2205)
ROUTE2206 = ROUTE()
ROUTE2206.setFromField("value_changed")
ROUTE2206.setFromNode("Stop_r_middle3_RotationInterpolator")
ROUTE2206.setToField("rotation")
ROUTE2206.setToNode("hanim_r_middle3")

Group1943.addChildren(ROUTE2206)
ROUTE2207 = ROUTE()
ROUTE2207.setFromField("value_changed")
ROUTE2207.setFromNode("Stop_r_ring0_RotationInterpolator")
ROUTE2207.setToField("rotation")
ROUTE2207.setToNode("hanim_r_ring0")

Group1943.addChildren(ROUTE2207)
ROUTE2208 = ROUTE()
ROUTE2208.setFromField("value_changed")
ROUTE2208.setFromNode("Stop_r_ring1_RotationInterpolator")
ROUTE2208.setToField("rotation")
ROUTE2208.setToNode("hanim_r_ring1")

Group1943.addChildren(ROUTE2208)
ROUTE2209 = ROUTE()
ROUTE2209.setFromField("value_changed")
ROUTE2209.setFromNode("Stop_r_ring2_RotationInterpolator")
ROUTE2209.setToField("rotation")
ROUTE2209.setToNode("hanim_r_ring2")

Group1943.addChildren(ROUTE2209)
ROUTE2210 = ROUTE()
ROUTE2210.setFromField("value_changed")
ROUTE2210.setFromNode("Stop_r_ring3_RotationInterpolator")
ROUTE2210.setToField("rotation")
ROUTE2210.setToNode("hanim_r_ring3")

Group1943.addChildren(ROUTE2210)
ROUTE2211 = ROUTE()
ROUTE2211.setFromField("value_changed")
ROUTE2211.setFromNode("Stop_r_pinky0_RotationInterpolator")
ROUTE2211.setToField("rotation")
ROUTE2211.setToNode("hanim_r_pinky0")

Group1943.addChildren(ROUTE2211)
ROUTE2212 = ROUTE()
ROUTE2212.setFromField("value_changed")
ROUTE2212.setFromNode("Stop_r_pinky1_RotationInterpolator")
ROUTE2212.setToField("rotation")
ROUTE2212.setToNode("hanim_r_pinky1")

Group1943.addChildren(ROUTE2212)
ROUTE2213 = ROUTE()
ROUTE2213.setFromField("value_changed")
ROUTE2213.setFromNode("Stop_r_pinky2_RotationInterpolator")
ROUTE2213.setToField("rotation")
ROUTE2213.setToNode("hanim_r_pinky2")

Group1943.addChildren(ROUTE2213)
ROUTE2214 = ROUTE()
ROUTE2214.setFromField("value_changed")
ROUTE2214.setFromNode("Stop_r_pinky3_RotationInterpolator")
ROUTE2214.setToField("rotation")
ROUTE2214.setToNode("hanim_r_pinky3")

Group1943.addChildren(ROUTE2214)

Scene31.addChildren(Group1943)
Group2215 = Group()
Group2215.setDEF("StandAnimation")
TimeSensor2216 = TimeSensor()
TimeSensor2216.setDEF("StandTimer")
TimeSensor2216.setCycleInterval(5.73)
TimeSensor2216.setLoop(True)

Group2215.addChildren(TimeSensor2216)
OrientationInterpolator2217 = OrientationInterpolator()
OrientationInterpolator2217.setDEF("Stand_r_metatarsal_PitchInterpolator")
OrientationInterpolator2217.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2217.setKeyValue([1,0,0,0,-1,0,0,0.015,1,0,0,0.17,-1,0,0,0.025,1,0,0,0.01,1,0,0,0])

Group2215.addChildren(OrientationInterpolator2217)
OrientationInterpolator2218 = OrientationInterpolator()
OrientationInterpolator2218.setDEF("Stand_r_ankle_RotationInterpolator")
OrientationInterpolator2218.setKey([0,0.5,1])
OrientationInterpolator2218.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2218)
OrientationInterpolator2219 = OrientationInterpolator()
OrientationInterpolator2219.setDEF("Stand_r_knee_RotationInterpolator")
OrientationInterpolator2219.setKey([0,0.5,1])
OrientationInterpolator2219.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2219)
OrientationInterpolator2220 = OrientationInterpolator()
OrientationInterpolator2220.setDEF("Stand_r_hip_RotationInterpolator")
OrientationInterpolator2220.setKey([0,0.5,1])
OrientationInterpolator2220.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2220)
OrientationInterpolator2221 = OrientationInterpolator()
OrientationInterpolator2221.setDEF("Stand_l_ankle_RotationInterpolator")
OrientationInterpolator2221.setKey([0,0.5,1])
OrientationInterpolator2221.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2221)
OrientationInterpolator2222 = OrientationInterpolator()
OrientationInterpolator2222.setDEF("Stand_l_knee_RotationInterpolator")
OrientationInterpolator2222.setKey([0,0.5,1])
OrientationInterpolator2222.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2222)
OrientationInterpolator2223 = OrientationInterpolator()
OrientationInterpolator2223.setDEF("Stand_l_hip_RotationInterpolator")
OrientationInterpolator2223.setKey([0,0.5,1])
OrientationInterpolator2223.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2223)
OrientationInterpolator2224 = OrientationInterpolator()
OrientationInterpolator2224.setDEF("Stand_r_wrist_RotationInterpolator")
OrientationInterpolator2224.setKey([0,0.5,1])
OrientationInterpolator2224.setKeyValue([0,0,1,0,0,0,-1,0.25,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2224)
OrientationInterpolator2225 = OrientationInterpolator()
OrientationInterpolator2225.setDEF("Stand_r_elbow_RotationInterpolator")
OrientationInterpolator2225.setKey([0,0.5,1])
OrientationInterpolator2225.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2225)
OrientationInterpolator2226 = OrientationInterpolator()
OrientationInterpolator2226.setDEF("Stand_r_shoulder_RotationInterpolator")
OrientationInterpolator2226.setKey([0,0.5,1])
OrientationInterpolator2226.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2226)
OrientationInterpolator2227 = OrientationInterpolator()
OrientationInterpolator2227.setDEF("Stand_l_wrist_RotationInterpolator")
OrientationInterpolator2227.setKey([0,0.5,1])
OrientationInterpolator2227.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2227)
OrientationInterpolator2228 = OrientationInterpolator()
OrientationInterpolator2228.setDEF("Stand_l_elbow_RotationInterpolator")
OrientationInterpolator2228.setKey([0,0.5,1])
OrientationInterpolator2228.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2228)
OrientationInterpolator2229 = OrientationInterpolator()
OrientationInterpolator2229.setDEF("Stand_l_shoulder_RotationInterpolator")
OrientationInterpolator2229.setKey([0,0.5,1])
OrientationInterpolator2229.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2229)
OrientationInterpolator2230 = OrientationInterpolator()
OrientationInterpolator2230.setDEF("Stand_head_RotationInterpolator")
OrientationInterpolator2230.setKey([0,0.5,1])
OrientationInterpolator2230.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2230)
OrientationInterpolator2231 = OrientationInterpolator()
OrientationInterpolator2231.setDEF("Stand_neck_RotationInterpolator")
OrientationInterpolator2231.setKey([0,0.5,1])
OrientationInterpolator2231.setKeyValue([0,0,1,0,-1,0,0,0.5,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2231)
OrientationInterpolator2232 = OrientationInterpolator()
OrientationInterpolator2232.setDEF("Stand_l_eyeball_RotationInterpolator")
OrientationInterpolator2232.setKey([0,0.4,0.7,1])
OrientationInterpolator2232.setKeyValue([0,0,1,0,-1,0,0,0.5,1,0,0,0.45,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2232)
OrientationInterpolator2233 = OrientationInterpolator()
OrientationInterpolator2233.setDEF("Stand_r_eyeball_RotationInterpolator")
OrientationInterpolator2233.setKey([0,0.4,0.7,1])
OrientationInterpolator2233.setKeyValue([0,0,1,0,-1,0,0,0.5,1,0,0,0.45,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2233)
OrientationInterpolator2234 = OrientationInterpolator()
OrientationInterpolator2234.setDEF("Stand_lower_body_RotationInterpolator")
OrientationInterpolator2234.setKey([0,0.5,1])
OrientationInterpolator2234.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2234)
OrientationInterpolator2235 = OrientationInterpolator()
OrientationInterpolator2235.setDEF("Stand_upper_body_RotationInterpolator")
OrientationInterpolator2235.setKey([0,0.5,1])
OrientationInterpolator2235.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2235)
OrientationInterpolator2236 = OrientationInterpolator()
OrientationInterpolator2236.setDEF("Stand_whole_body_RotationInterpolator")
OrientationInterpolator2236.setKey([0,0.5,1])
OrientationInterpolator2236.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2236)
PositionInterpolator2237 = PositionInterpolator()
PositionInterpolator2237.setDEF("Stand_whole_body_TranslationInterpolator")
PositionInterpolator2237.setKey([0,0.5,1])
PositionInterpolator2237.setKeyValue([0,0,0,0,0,0,0,0,0])

Group2215.addChildren(PositionInterpolator2237)
OrientationInterpolator2238 = OrientationInterpolator()
OrientationInterpolator2238.setDEF("Stand_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2238.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2238.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2238)
OrientationInterpolator2239 = OrientationInterpolator()
OrientationInterpolator2239.setDEF("Stand_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2239.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2239.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2239)
OrientationInterpolator2240 = OrientationInterpolator()
OrientationInterpolator2240.setDEF("Stand_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2240.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2240.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2240)
OrientationInterpolator2241 = OrientationInterpolator()
OrientationInterpolator2241.setDEF("Stand_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2241.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2241.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2241)
OrientationInterpolator2242 = OrientationInterpolator()
OrientationInterpolator2242.setDEF("Stand_sacroiliac_YawInterpolator")
OrientationInterpolator2242.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2242.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2242)
OrientationInterpolator2243 = OrientationInterpolator()
OrientationInterpolator2243.setDEF("Stand_vl5_YawInterpolator")
OrientationInterpolator2243.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2243.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2243)
OrientationInterpolator2244 = OrientationInterpolator()
OrientationInterpolator2244.setDEF("Stand_vc6_YawInterpolator")
OrientationInterpolator2244.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2244.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,-1,0,0,0,0,-1,0,0,0,1,0,0])

Group2215.addChildren(OrientationInterpolator2244)
OrientationInterpolator2245 = OrientationInterpolator()
OrientationInterpolator2245.setDEF("Stand_l_thumb1_PitchInterpolator")
OrientationInterpolator2245.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2245.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2245)
OrientationInterpolator2246 = OrientationInterpolator()
OrientationInterpolator2246.setDEF("Stand_r_thumb1_PitchInterpolator")
OrientationInterpolator2246.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2246.setKeyValue([1,0,0,0,1,0,0,0.5,1,0,0,0.1,1,0,0,0.27,1,0,0,0.2,1,0,0,0])

Group2215.addChildren(OrientationInterpolator2246)
OrientationInterpolator2247 = OrientationInterpolator()
OrientationInterpolator2247.setDEF("Stand_r_index1_RollInterpolator")
OrientationInterpolator2247.setKey([0,0.2,0.4,0.5,0.8,1])
OrientationInterpolator2247.setKeyValue([0,0,1,0,0,0,1,0.1,0,0,1,0.2,0,0,1,0.3,0,0,1,0,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2247)
OrientationInterpolator2248 = OrientationInterpolator()
OrientationInterpolator2248.setDEF("Stand_r_index2_RollInterpolator")
OrientationInterpolator2248.setKey([0,0.2,0.4,0.5,0.8,1])
OrientationInterpolator2248.setKeyValue([0,0,1,0,0,0,1,0.4,0,0,1,0.32,0,0,1,0.25,0,0,1,0.2,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2248)
OrientationInterpolator2249 = OrientationInterpolator()
OrientationInterpolator2249.setDEF("Stand_r_index3_RollInterpolator")
OrientationInterpolator2249.setKey([0,0.2,0.4,0.5,0.8,1])
OrientationInterpolator2249.setKeyValue([0,0,1,0,0,0,1,0.2,0,0,1,0.3,0,0,1,0.35,0,0,1,0.2,0,0,1,0])

Group2215.addChildren(OrientationInterpolator2249)
ROUTE2250 = ROUTE()
ROUTE2250.setFromField("fraction_changed")
ROUTE2250.setFromNode("StandTimer")
ROUTE2250.setToField("set_fraction")
ROUTE2250.setToNode("Stand_r_ankle_RotationInterpolator")

Group2215.addChildren(ROUTE2250)
ROUTE2251 = ROUTE()
ROUTE2251.setFromField("fraction_changed")
ROUTE2251.setFromNode("StandTimer")
ROUTE2251.setToField("set_fraction")
ROUTE2251.setToNode("Stand_r_knee_RotationInterpolator")

Group2215.addChildren(ROUTE2251)
ROUTE2252 = ROUTE()
ROUTE2252.setFromField("fraction_changed")
ROUTE2252.setFromNode("StandTimer")
ROUTE2252.setToField("set_fraction")
ROUTE2252.setToNode("Stand_r_hip_RotationInterpolator")

Group2215.addChildren(ROUTE2252)
ROUTE2253 = ROUTE()
ROUTE2253.setFromField("fraction_changed")
ROUTE2253.setFromNode("StandTimer")
ROUTE2253.setToField("set_fraction")
ROUTE2253.setToNode("Stand_l_ankle_RotationInterpolator")

Group2215.addChildren(ROUTE2253)
ROUTE2254 = ROUTE()
ROUTE2254.setFromField("fraction_changed")
ROUTE2254.setFromNode("StandTimer")
ROUTE2254.setToField("set_fraction")
ROUTE2254.setToNode("Stand_l_knee_RotationInterpolator")

Group2215.addChildren(ROUTE2254)
ROUTE2255 = ROUTE()
ROUTE2255.setFromField("fraction_changed")
ROUTE2255.setFromNode("StandTimer")
ROUTE2255.setToField("set_fraction")
ROUTE2255.setToNode("Stand_l_hip_RotationInterpolator")

Group2215.addChildren(ROUTE2255)
ROUTE2256 = ROUTE()
ROUTE2256.setFromField("fraction_changed")
ROUTE2256.setFromNode("StandTimer")
ROUTE2256.setToField("set_fraction")
ROUTE2256.setToNode("Stand_lower_body_RotationInterpolator")

Group2215.addChildren(ROUTE2256)
ROUTE2257 = ROUTE()
ROUTE2257.setFromField("fraction_changed")
ROUTE2257.setFromNode("StandTimer")
ROUTE2257.setToField("set_fraction")
ROUTE2257.setToNode("Stand_r_wrist_RotationInterpolator")

Group2215.addChildren(ROUTE2257)
ROUTE2258 = ROUTE()
ROUTE2258.setFromField("fraction_changed")
ROUTE2258.setFromNode("StandTimer")
ROUTE2258.setToField("set_fraction")
ROUTE2258.setToNode("Stand_r_elbow_RotationInterpolator")

Group2215.addChildren(ROUTE2258)
ROUTE2259 = ROUTE()
ROUTE2259.setFromField("fraction_changed")
ROUTE2259.setFromNode("StandTimer")
ROUTE2259.setToField("set_fraction")
ROUTE2259.setToNode("Stand_r_shoulder_RotationInterpolator")

Group2215.addChildren(ROUTE2259)
ROUTE2260 = ROUTE()
ROUTE2260.setFromField("fraction_changed")
ROUTE2260.setFromNode("StandTimer")
ROUTE2260.setToField("set_fraction")
ROUTE2260.setToNode("Stand_l_wrist_RotationInterpolator")

Group2215.addChildren(ROUTE2260)
ROUTE2261 = ROUTE()
ROUTE2261.setFromField("fraction_changed")
ROUTE2261.setFromNode("StandTimer")
ROUTE2261.setToField("set_fraction")
ROUTE2261.setToNode("Stand_l_elbow_RotationInterpolator")

Group2215.addChildren(ROUTE2261)
ROUTE2262 = ROUTE()
ROUTE2262.setFromField("fraction_changed")
ROUTE2262.setFromNode("StandTimer")
ROUTE2262.setToField("set_fraction")
ROUTE2262.setToNode("Stand_l_shoulder_RotationInterpolator")

Group2215.addChildren(ROUTE2262)
ROUTE2263 = ROUTE()
ROUTE2263.setFromField("fraction_changed")
ROUTE2263.setFromNode("StandTimer")
ROUTE2263.setToField("set_fraction")
ROUTE2263.setToNode("Stand_head_RotationInterpolator")

Group2215.addChildren(ROUTE2263)
ROUTE2264 = ROUTE()
ROUTE2264.setFromField("fraction_changed")
ROUTE2264.setFromNode("StandTimer")
ROUTE2264.setToField("set_fraction")
ROUTE2264.setToNode("Stand_neck_RotationInterpolator")

Group2215.addChildren(ROUTE2264)
ROUTE2265 = ROUTE()
ROUTE2265.setFromField("fraction_changed")
ROUTE2265.setFromNode("StandTimer")
ROUTE2265.setToField("set_fraction")
ROUTE2265.setToNode("Stand_l_eyeball_RotationInterpolator")

Group2215.addChildren(ROUTE2265)
ROUTE2266 = ROUTE()
ROUTE2266.setFromField("fraction_changed")
ROUTE2266.setFromNode("StandTimer")
ROUTE2266.setToField("set_fraction")
ROUTE2266.setToNode("Stand_r_eyeball_RotationInterpolator")

Group2215.addChildren(ROUTE2266)
ROUTE2267 = ROUTE()
ROUTE2267.setFromField("fraction_changed")
ROUTE2267.setFromNode("StandTimer")
ROUTE2267.setToField("set_fraction")
ROUTE2267.setToNode("Stand_upper_body_RotationInterpolator")

Group2215.addChildren(ROUTE2267)
ROUTE2268 = ROUTE()
ROUTE2268.setFromField("fraction_changed")
ROUTE2268.setFromNode("StandTimer")
ROUTE2268.setToField("set_fraction")
ROUTE2268.setToNode("Stand_whole_body_RotationInterpolator")

Group2215.addChildren(ROUTE2268)
ROUTE2269 = ROUTE()
ROUTE2269.setFromField("fraction_changed")
ROUTE2269.setFromNode("StandTimer")
ROUTE2269.setToField("set_fraction")
ROUTE2269.setToNode("Stand_whole_body_TranslationInterpolator")

Group2215.addChildren(ROUTE2269)
ROUTE2270 = ROUTE()
ROUTE2270.setFromField("fraction_changed")
ROUTE2270.setFromNode("StandTimer")
ROUTE2270.setToField("set_fraction")
ROUTE2270.setToNode("Stand_l_sternoclavicular_RollInterpolator")

Group2215.addChildren(ROUTE2270)
ROUTE2271 = ROUTE()
ROUTE2271.setFromField("fraction_changed")
ROUTE2271.setFromNode("StandTimer")
ROUTE2271.setToField("set_fraction")
ROUTE2271.setToNode("Stand_l_acromioclavicular_RollInterpolator")

Group2215.addChildren(ROUTE2271)
ROUTE2272 = ROUTE()
ROUTE2272.setFromField("fraction_changed")
ROUTE2272.setFromNode("StandTimer")
ROUTE2272.setToField("set_fraction")
ROUTE2272.setToNode("Stand_r_sternoclavicular_RollInterpolator")

Group2215.addChildren(ROUTE2272)
ROUTE2273 = ROUTE()
ROUTE2273.setFromField("fraction_changed")
ROUTE2273.setFromNode("StandTimer")
ROUTE2273.setToField("set_fraction")
ROUTE2273.setToNode("Stand_r_acromioclavicular_RollInterpolator")

Group2215.addChildren(ROUTE2273)
ROUTE2274 = ROUTE()
ROUTE2274.setFromField("fraction_changed")
ROUTE2274.setFromNode("StandTimer")
ROUTE2274.setToField("set_fraction")
ROUTE2274.setToNode("Stand_r_metatarsal_PitchInterpolator")

Group2215.addChildren(ROUTE2274)
ROUTE2275 = ROUTE()
ROUTE2275.setFromField("fraction_changed")
ROUTE2275.setFromNode("StandTimer")
ROUTE2275.setToField("set_fraction")
ROUTE2275.setToNode("Stand_sacroiliac_YawInterpolator")

Group2215.addChildren(ROUTE2275)
ROUTE2276 = ROUTE()
ROUTE2276.setFromField("fraction_changed")
ROUTE2276.setFromNode("StandTimer")
ROUTE2276.setToField("set_fraction")
ROUTE2276.setToNode("Stand_vl5_YawInterpolator")

Group2215.addChildren(ROUTE2276)
ROUTE2277 = ROUTE()
ROUTE2277.setFromField("fraction_changed")
ROUTE2277.setFromNode("StandTimer")
ROUTE2277.setToField("set_fraction")
ROUTE2277.setToNode("Stand_vc6_YawInterpolator")

Group2215.addChildren(ROUTE2277)
ROUTE2278 = ROUTE()
ROUTE2278.setFromField("fraction_changed")
ROUTE2278.setFromNode("StandTimer")
ROUTE2278.setToField("set_fraction")
ROUTE2278.setToNode("Stand_l_thumb1_PitchInterpolator")

Group2215.addChildren(ROUTE2278)
ROUTE2279 = ROUTE()
ROUTE2279.setFromField("fraction_changed")
ROUTE2279.setFromNode("StandTimer")
ROUTE2279.setToField("set_fraction")
ROUTE2279.setToNode("Stand_r_thumb1_PitchInterpolator")

Group2215.addChildren(ROUTE2279)
ROUTE2280 = ROUTE()
ROUTE2280.setFromField("fraction_changed")
ROUTE2280.setFromNode("StandTimer")
ROUTE2280.setToField("set_fraction")
ROUTE2280.setToNode("Stand_r_index1_RollInterpolator")

Group2215.addChildren(ROUTE2280)
ROUTE2281 = ROUTE()
ROUTE2281.setFromField("fraction_changed")
ROUTE2281.setFromNode("StandTimer")
ROUTE2281.setToField("set_fraction")
ROUTE2281.setToNode("Stand_r_index2_RollInterpolator")

Group2215.addChildren(ROUTE2281)
ROUTE2282 = ROUTE()
ROUTE2282.setFromField("fraction_changed")
ROUTE2282.setFromNode("StandTimer")
ROUTE2282.setToField("set_fraction")
ROUTE2282.setToNode("Stand_r_index3_RollInterpolator")

Group2215.addChildren(ROUTE2282)
ROUTE2283 = ROUTE()
ROUTE2283.setFromField("value_changed")
ROUTE2283.setFromNode("Stand_r_ankle_RotationInterpolator")
ROUTE2283.setToField("rotation")
ROUTE2283.setToNode("hanim_r_ankle")

Group2215.addChildren(ROUTE2283)
ROUTE2284 = ROUTE()
ROUTE2284.setFromField("value_changed")
ROUTE2284.setFromNode("Stand_r_knee_RotationInterpolator")
ROUTE2284.setToField("rotation")
ROUTE2284.setToNode("hanim_r_knee")

Group2215.addChildren(ROUTE2284)
ROUTE2285 = ROUTE()
ROUTE2285.setFromField("value_changed")
ROUTE2285.setFromNode("Stand_r_hip_RotationInterpolator")
ROUTE2285.setToField("rotation")
ROUTE2285.setToNode("hanim_r_hip")

Group2215.addChildren(ROUTE2285)
ROUTE2286 = ROUTE()
ROUTE2286.setFromField("value_changed")
ROUTE2286.setFromNode("Stand_l_ankle_RotationInterpolator")
ROUTE2286.setToField("rotation")
ROUTE2286.setToNode("hanim_l_ankle")

Group2215.addChildren(ROUTE2286)
ROUTE2287 = ROUTE()
ROUTE2287.setFromField("value_changed")
ROUTE2287.setFromNode("Stand_l_knee_RotationInterpolator")
ROUTE2287.setToField("rotation")
ROUTE2287.setToNode("hanim_l_knee")

Group2215.addChildren(ROUTE2287)
ROUTE2288 = ROUTE()
ROUTE2288.setFromField("value_changed")
ROUTE2288.setFromNode("Stand_l_hip_RotationInterpolator")
ROUTE2288.setToField("rotation")
ROUTE2288.setToNode("hanim_l_hip")

Group2215.addChildren(ROUTE2288)
ROUTE2289 = ROUTE()
ROUTE2289.setFromField("value_changed")
ROUTE2289.setFromNode("Stand_r_wrist_RotationInterpolator")
ROUTE2289.setToField("rotation")
ROUTE2289.setToNode("hanim_r_wrist")

Group2215.addChildren(ROUTE2289)
ROUTE2290 = ROUTE()
ROUTE2290.setFromField("value_changed")
ROUTE2290.setFromNode("Stand_r_elbow_RotationInterpolator")
ROUTE2290.setToField("rotation")
ROUTE2290.setToNode("hanim_r_elbow")

Group2215.addChildren(ROUTE2290)
ROUTE2291 = ROUTE()
ROUTE2291.setFromField("value_changed")
ROUTE2291.setFromNode("Stand_r_shoulder_RotationInterpolator")
ROUTE2291.setToField("rotation")
ROUTE2291.setToNode("hanim_r_shoulder")

Group2215.addChildren(ROUTE2291)
ROUTE2292 = ROUTE()
ROUTE2292.setFromField("value_changed")
ROUTE2292.setFromNode("Stand_l_wrist_RotationInterpolator")
ROUTE2292.setToField("rotation")
ROUTE2292.setToNode("hanim_l_wrist")

Group2215.addChildren(ROUTE2292)
ROUTE2293 = ROUTE()
ROUTE2293.setFromField("value_changed")
ROUTE2293.setFromNode("Stand_l_elbow_RotationInterpolator")
ROUTE2293.setToField("rotation")
ROUTE2293.setToNode("hanim_l_elbow")

Group2215.addChildren(ROUTE2293)
ROUTE2294 = ROUTE()
ROUTE2294.setFromField("value_changed")
ROUTE2294.setFromNode("Stand_l_shoulder_RotationInterpolator")
ROUTE2294.setToField("rotation")
ROUTE2294.setToNode("hanim_l_shoulder")

Group2215.addChildren(ROUTE2294)
ROUTE2295 = ROUTE()
ROUTE2295.setFromField("value_changed")
ROUTE2295.setFromNode("Stand_head_RotationInterpolator")
ROUTE2295.setToField("rotation")
ROUTE2295.setToNode("hanim_skullbase")

Group2215.addChildren(ROUTE2295)
ROUTE2296 = ROUTE()
ROUTE2296.setFromField("value_changed")
ROUTE2296.setFromNode("Stand_neck_RotationInterpolator")
ROUTE2296.setToField("rotation")
ROUTE2296.setToNode("hanim_vc7")

Group2215.addChildren(ROUTE2296)
ROUTE2297 = ROUTE()
ROUTE2297.setFromField("value_changed")
ROUTE2297.setFromNode("Stand_l_eyeball_RotationInterpolator")
ROUTE2297.setToField("rotation")
ROUTE2297.setToNode("hanim_l_eyeball_joint")

Group2215.addChildren(ROUTE2297)
ROUTE2298 = ROUTE()
ROUTE2298.setFromField("value_changed")
ROUTE2298.setFromNode("Stand_r_eyeball_RotationInterpolator")
ROUTE2298.setToField("rotation")
ROUTE2298.setToNode("hanim_r_eyeball_joint")

Group2215.addChildren(ROUTE2298)
ROUTE2299 = ROUTE()
ROUTE2299.setFromField("value_changed")
ROUTE2299.setFromNode("Stand_upper_body_RotationInterpolator")
ROUTE2299.setToField("rotation")
ROUTE2299.setToNode("hanim_vl1")

Group2215.addChildren(ROUTE2299)
ROUTE2300 = ROUTE()
ROUTE2300.setFromField("value_changed")
ROUTE2300.setFromNode("Stand_lower_body_RotationInterpolator")
ROUTE2300.setToField("rotation")
ROUTE2300.setToNode("hanim_sacroiliac")

Group2215.addChildren(ROUTE2300)
ROUTE2301 = ROUTE()
ROUTE2301.setFromField("value_changed")
ROUTE2301.setFromNode("Stand_whole_body_RotationInterpolator")
ROUTE2301.setToField("rotation")
ROUTE2301.setToNode("hanim_humanoid_root")

Group2215.addChildren(ROUTE2301)
ROUTE2302 = ROUTE()
ROUTE2302.setFromField("value_changed")
ROUTE2302.setFromNode("Stand_whole_body_TranslationInterpolator")
ROUTE2302.setToField("translation")
ROUTE2302.setToNode("hanim_humanoid_root")

Group2215.addChildren(ROUTE2302)
ROUTE2303 = ROUTE()
ROUTE2303.setFromField("value_changed")
ROUTE2303.setFromNode("Stand_l_sternoclavicular_RollInterpolator")
ROUTE2303.setToField("rotation")
ROUTE2303.setToNode("hanim_l_sternoclavicular")

Group2215.addChildren(ROUTE2303)
ROUTE2304 = ROUTE()
ROUTE2304.setFromField("value_changed")
ROUTE2304.setFromNode("Stand_l_acromioclavicular_RollInterpolator")
ROUTE2304.setToField("rotation")
ROUTE2304.setToNode("hanim_l_acromioclavicular")

Group2215.addChildren(ROUTE2304)
ROUTE2305 = ROUTE()
ROUTE2305.setFromField("value_changed")
ROUTE2305.setFromNode("Stand_r_sternoclavicular_RollInterpolator")
ROUTE2305.setToField("rotation")
ROUTE2305.setToNode("hanim_r_sternoclavicular")

Group2215.addChildren(ROUTE2305)
ROUTE2306 = ROUTE()
ROUTE2306.setFromField("value_changed")
ROUTE2306.setFromNode("Stand_r_acromioclavicular_RollInterpolator")
ROUTE2306.setToField("rotation")
ROUTE2306.setToNode("hanim_r_acromioclavicular")

Group2215.addChildren(ROUTE2306)
ROUTE2307 = ROUTE()
ROUTE2307.setFromField("value_changed")
ROUTE2307.setFromNode("Stand_r_metatarsal_PitchInterpolator")
ROUTE2307.setToField("rotation")
ROUTE2307.setToNode("hanim_l_metatarsal")

Group2215.addChildren(ROUTE2307)
ROUTE2308 = ROUTE()
ROUTE2308.setFromField("value_changed")
ROUTE2308.setFromNode("Stand_r_metatarsal_PitchInterpolator")
ROUTE2308.setToField("rotation")
ROUTE2308.setToNode("hanim_r_metatarsal")

Group2215.addChildren(ROUTE2308)
ROUTE2309 = ROUTE()
ROUTE2309.setFromField("value_changed")
ROUTE2309.setFromNode("Stand_sacroiliac_YawInterpolator")
ROUTE2309.setToField("rotation")
ROUTE2309.setToNode("hanim_sacroiliac")

Group2215.addChildren(ROUTE2309)
ROUTE2310 = ROUTE()
ROUTE2310.setFromField("value_changed")
ROUTE2310.setFromNode("Stand_vl5_YawInterpolator")
ROUTE2310.setToField("rotation")
ROUTE2310.setToNode("hanim_vl5")

Group2215.addChildren(ROUTE2310)
ROUTE2311 = ROUTE()
ROUTE2311.setFromField("value_changed")
ROUTE2311.setFromNode("Stand_vc6_YawInterpolator")
ROUTE2311.setToField("rotation")
ROUTE2311.setToNode("hanim_vc6")

Group2215.addChildren(ROUTE2311)
ROUTE2312 = ROUTE()
ROUTE2312.setFromField("value_changed")
ROUTE2312.setFromNode("Stand_l_thumb1_PitchInterpolator")
ROUTE2312.setToField("rotation")
ROUTE2312.setToNode("hanim_l_thumb1")

Group2215.addChildren(ROUTE2312)
ROUTE2313 = ROUTE()
ROUTE2313.setFromField("value_changed")
ROUTE2313.setFromNode("Stand_r_thumb1_PitchInterpolator")
ROUTE2313.setToField("rotation")
ROUTE2313.setToNode("hanim_r_thumb1")

Group2215.addChildren(ROUTE2313)
ROUTE2314 = ROUTE()
ROUTE2314.setFromField("value_changed")
ROUTE2314.setFromNode("Stand_r_index1_RollInterpolator")
ROUTE2314.setToField("rotation")
ROUTE2314.setToNode("hanim_r_index1")

Group2215.addChildren(ROUTE2314)
ROUTE2315 = ROUTE()
ROUTE2315.setFromField("value_changed")
ROUTE2315.setFromNode("Stand_r_index2_RollInterpolator")
ROUTE2315.setToField("rotation")
ROUTE2315.setToNode("hanim_r_index2")

Group2215.addChildren(ROUTE2315)
ROUTE2316 = ROUTE()
ROUTE2316.setFromField("value_changed")
ROUTE2316.setFromNode("Stand_r_index3_RollInterpolator")
ROUTE2316.setToField("rotation")
ROUTE2316.setToNode("hanim_r_index3")

Group2215.addChildren(ROUTE2316)
ROUTE2317 = ROUTE()
ROUTE2317.setFromField("value_changed")
ROUTE2317.setFromNode("Stand_r_index1_RollInterpolator")
ROUTE2317.setToField("rotation")
ROUTE2317.setToNode("hanim_r_middle1")

Group2215.addChildren(ROUTE2317)
ROUTE2318 = ROUTE()
ROUTE2318.setFromField("value_changed")
ROUTE2318.setFromNode("Stand_r_index2_RollInterpolator")
ROUTE2318.setToField("rotation")
ROUTE2318.setToNode("hanim_r_middle2")

Group2215.addChildren(ROUTE2318)
ROUTE2319 = ROUTE()
ROUTE2319.setFromField("value_changed")
ROUTE2319.setFromNode("Stand_r_index3_RollInterpolator")
ROUTE2319.setToField("rotation")
ROUTE2319.setToNode("hanim_r_middle3")

Group2215.addChildren(ROUTE2319)
ROUTE2320 = ROUTE()
ROUTE2320.setFromField("value_changed")
ROUTE2320.setFromNode("Stand_r_index1_RollInterpolator")
ROUTE2320.setToField("rotation")
ROUTE2320.setToNode("hanim_r_ring1")

Group2215.addChildren(ROUTE2320)
ROUTE2321 = ROUTE()
ROUTE2321.setFromField("value_changed")
ROUTE2321.setFromNode("Stand_r_index2_RollInterpolator")
ROUTE2321.setToField("rotation")
ROUTE2321.setToNode("hanim_r_ring2")

Group2215.addChildren(ROUTE2321)
ROUTE2322 = ROUTE()
ROUTE2322.setFromField("value_changed")
ROUTE2322.setFromNode("Stand_r_index3_RollInterpolator")
ROUTE2322.setToField("rotation")
ROUTE2322.setToNode("hanim_r_ring3")

Group2215.addChildren(ROUTE2322)
ROUTE2323 = ROUTE()
ROUTE2323.setFromField("value_changed")
ROUTE2323.setFromNode("Stand_r_index1_RollInterpolator")
ROUTE2323.setToField("rotation")
ROUTE2323.setToNode("hanim_r_pinky1")

Group2215.addChildren(ROUTE2323)
ROUTE2324 = ROUTE()
ROUTE2324.setFromField("value_changed")
ROUTE2324.setFromNode("Stand_r_index2_RollInterpolator")
ROUTE2324.setToField("rotation")
ROUTE2324.setToNode("hanim_r_pinky2")

Group2215.addChildren(ROUTE2324)
ROUTE2325 = ROUTE()
ROUTE2325.setFromField("value_changed")
ROUTE2325.setFromNode("Stand_r_index3_RollInterpolator")
ROUTE2325.setToField("rotation")
ROUTE2325.setToNode("hanim_r_pinky3")

Group2215.addChildren(ROUTE2325)

Scene31.addChildren(Group2215)
Group2326 = Group()
Group2326.setDEF("PitchesAnimation")
TimeSensor2327 = TimeSensor()
TimeSensor2327.setDEF("PitchTimer")
TimeSensor2327.setCycleInterval(5.73)
TimeSensor2327.setLoop(True)

Group2326.addChildren(TimeSensor2327)
OrientationInterpolator2328 = OrientationInterpolator()
OrientationInterpolator2328.setDEF("Pitch_r_metatarsal_PitchInterpolator")
OrientationInterpolator2328.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2328.setKeyValue([1,0,0,0,-1,0,0,0.5,-1,0,0,0.7,1,0,0,0.75,-1,0,0,0.2,1,0,0,0])

Group2326.addChildren(OrientationInterpolator2328)
OrientationInterpolator2329 = OrientationInterpolator()
OrientationInterpolator2329.setDEF("Pitches_r_ankle_RotationInterpolator")
OrientationInterpolator2329.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2329.setKeyValue([0,0,1,0,1,0,0,1.5,0,0,1,0,-1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2329)
OrientationInterpolator2330 = OrientationInterpolator()
OrientationInterpolator2330.setDEF("Pitches_r_knee_RotationInterpolator")
OrientationInterpolator2330.setKey([0,0.5,1])
OrientationInterpolator2330.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2330)
OrientationInterpolator2331 = OrientationInterpolator()
OrientationInterpolator2331.setDEF("Pitches_r_hip_RotationInterpolator")
OrientationInterpolator2331.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2331.setKeyValue([0,0,1,0,-1,0,0,1.5,0,0,1,0,1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2331)
OrientationInterpolator2332 = OrientationInterpolator()
OrientationInterpolator2332.setDEF("Pitches_l_ankle_RotationInterpolator")
OrientationInterpolator2332.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2332.setKeyValue([0,0,1,0,-1,0,0,1.5,0,0,1,0,1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2332)
OrientationInterpolator2333 = OrientationInterpolator()
OrientationInterpolator2333.setDEF("Pitches_l_knee_RotationInterpolator")
OrientationInterpolator2333.setKey([0,0.5,1])
OrientationInterpolator2333.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2333)
OrientationInterpolator2334 = OrientationInterpolator()
OrientationInterpolator2334.setDEF("Pitches_l_hip_RotationInterpolator")
OrientationInterpolator2334.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2334.setKeyValue([0,0,1,0,1,0,0,1.5,0,0,1,0,-1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2334)
OrientationInterpolator2335 = OrientationInterpolator()
OrientationInterpolator2335.setDEF("Pitches_r_wrist_RotationInterpolator")
OrientationInterpolator2335.setKey([0,0.5,1])
OrientationInterpolator2335.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2335)
OrientationInterpolator2336 = OrientationInterpolator()
OrientationInterpolator2336.setDEF("Pitches_r_elbow_RotationInterpolator")
OrientationInterpolator2336.setKey([0,0.5,1])
OrientationInterpolator2336.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2336)
OrientationInterpolator2337 = OrientationInterpolator()
OrientationInterpolator2337.setDEF("Pitches_r_shoulder_RotationInterpolator")
OrientationInterpolator2337.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2337.setKeyValue([0,0,1,0,1,0,0,1.5,0,0,1,0,-1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2337)
OrientationInterpolator2338 = OrientationInterpolator()
OrientationInterpolator2338.setDEF("Pitches_l_wrist_RotationInterpolator")
OrientationInterpolator2338.setKey([0,0.5,1])
OrientationInterpolator2338.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2338)
OrientationInterpolator2339 = OrientationInterpolator()
OrientationInterpolator2339.setDEF("Pitches_l_elbow_RotationInterpolator")
OrientationInterpolator2339.setKey([0,0.5,1])
OrientationInterpolator2339.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2339)
OrientationInterpolator2340 = OrientationInterpolator()
OrientationInterpolator2340.setDEF("Pitches_l_shoulder_RotationInterpolator")
OrientationInterpolator2340.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2340.setKeyValue([0,0,1,0,-1,0,0,1.5,0,0,1,0,1,0,0,1.5,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2340)
OrientationInterpolator2341 = OrientationInterpolator()
OrientationInterpolator2341.setDEF("Pitches_head_RotationInterpolator")
OrientationInterpolator2341.setKey([0,0.5,1])
OrientationInterpolator2341.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2341)
OrientationInterpolator2342 = OrientationInterpolator()
OrientationInterpolator2342.setDEF("Pitches_neck_RotationInterpolator")
OrientationInterpolator2342.setKey([0,0.25,0.55,1])
OrientationInterpolator2342.setKeyValue([0,0,1,0,1,0,0,0.55,-1,0,0,1.05,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2342)
OrientationInterpolator2343 = OrientationInterpolator()
OrientationInterpolator2343.setDEF("Pitches_lower_body_RotationInterpolator")
OrientationInterpolator2343.setKey([0,0.5,1])
OrientationInterpolator2343.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2343)
OrientationInterpolator2344 = OrientationInterpolator()
OrientationInterpolator2344.setDEF("Pitches_upper_body_RotationInterpolator")
OrientationInterpolator2344.setKey([0,0.5,1])
OrientationInterpolator2344.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2344)
OrientationInterpolator2345 = OrientationInterpolator()
OrientationInterpolator2345.setDEF("Pitches_whole_body_RotationInterpolator")
OrientationInterpolator2345.setKey([0,0.5,1])
OrientationInterpolator2345.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2345)
PositionInterpolator2346 = PositionInterpolator()
PositionInterpolator2346.setDEF("Pitches_whole_body_TranslationInterpolator")
PositionInterpolator2346.setKey([0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1])
PositionInterpolator2346.setKeyValue([0,0,0,0,-0.15,0,0,-0.7,0,0,-0.15,0,0,0,0,0,-0.15,0,0,-0.7,0,0,-0.15,0,0,0,0])

Group2326.addChildren(PositionInterpolator2346)
OrientationInterpolator2347 = OrientationInterpolator()
OrientationInterpolator2347.setDEF("Pitch_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2347.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2347.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2347)
OrientationInterpolator2348 = OrientationInterpolator()
OrientationInterpolator2348.setDEF("Pitch_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2348.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2348.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2348)
OrientationInterpolator2349 = OrientationInterpolator()
OrientationInterpolator2349.setDEF("Pitch_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2349.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2349.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2349)
OrientationInterpolator2350 = OrientationInterpolator()
OrientationInterpolator2350.setDEF("Pitch_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2350.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2350.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2350)
OrientationInterpolator2351 = OrientationInterpolator()
OrientationInterpolator2351.setDEF("Pitch_sacroiliac_YawInterpolator")
OrientationInterpolator2351.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2351.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2351)
OrientationInterpolator2352 = OrientationInterpolator()
OrientationInterpolator2352.setDEF("Pitch_vl5_YawInterpolator")
OrientationInterpolator2352.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2352.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2352)
OrientationInterpolator2353 = OrientationInterpolator()
OrientationInterpolator2353.setDEF("Pitch_vc6_YawInterpolator")
OrientationInterpolator2353.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2353.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2326.addChildren(OrientationInterpolator2353)
OrientationInterpolator2354 = OrientationInterpolator()
OrientationInterpolator2354.setDEF("Pitch_l_thumb1_PitchInterpolator")
OrientationInterpolator2354.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2354.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.3,1,0,0,0.27,1,0,0,0.2,1,0,0,0])

Group2326.addChildren(OrientationInterpolator2354)
OrientationInterpolator2355 = OrientationInterpolator()
OrientationInterpolator2355.setDEF("Pitch_r_thumb1_PitchInterpolator")
OrientationInterpolator2355.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2355.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.3,1,0,0,0.27,1,0,0,0.2,1,0,0,0])

Group2326.addChildren(OrientationInterpolator2355)
ROUTE2356 = ROUTE()
ROUTE2356.setFromField("fraction_changed")
ROUTE2356.setFromNode("PitchTimer")
ROUTE2356.setToField("set_fraction")
ROUTE2356.setToNode("Pitches_r_ankle_RotationInterpolator")

Group2326.addChildren(ROUTE2356)
ROUTE2357 = ROUTE()
ROUTE2357.setFromField("fraction_changed")
ROUTE2357.setFromNode("PitchTimer")
ROUTE2357.setToField("set_fraction")
ROUTE2357.setToNode("Pitches_r_knee_RotationInterpolator")

Group2326.addChildren(ROUTE2357)
ROUTE2358 = ROUTE()
ROUTE2358.setFromField("fraction_changed")
ROUTE2358.setFromNode("PitchTimer")
ROUTE2358.setToField("set_fraction")
ROUTE2358.setToNode("Pitches_r_hip_RotationInterpolator")

Group2326.addChildren(ROUTE2358)
ROUTE2359 = ROUTE()
ROUTE2359.setFromField("fraction_changed")
ROUTE2359.setFromNode("PitchTimer")
ROUTE2359.setToField("set_fraction")
ROUTE2359.setToNode("Pitches_l_ankle_RotationInterpolator")

Group2326.addChildren(ROUTE2359)
ROUTE2360 = ROUTE()
ROUTE2360.setFromField("fraction_changed")
ROUTE2360.setFromNode("PitchTimer")
ROUTE2360.setToField("set_fraction")
ROUTE2360.setToNode("Pitches_l_knee_RotationInterpolator")

Group2326.addChildren(ROUTE2360)
ROUTE2361 = ROUTE()
ROUTE2361.setFromField("fraction_changed")
ROUTE2361.setFromNode("PitchTimer")
ROUTE2361.setToField("set_fraction")
ROUTE2361.setToNode("Pitches_l_hip_RotationInterpolator")

Group2326.addChildren(ROUTE2361)
ROUTE2362 = ROUTE()
ROUTE2362.setFromField("fraction_changed")
ROUTE2362.setFromNode("PitchTimer")
ROUTE2362.setToField("set_fraction")
ROUTE2362.setToNode("Pitches_lower_body_RotationInterpolator")

Group2326.addChildren(ROUTE2362)
ROUTE2363 = ROUTE()
ROUTE2363.setFromField("fraction_changed")
ROUTE2363.setFromNode("PitchTimer")
ROUTE2363.setToField("set_fraction")
ROUTE2363.setToNode("Pitches_r_wrist_RotationInterpolator")

Group2326.addChildren(ROUTE2363)
ROUTE2364 = ROUTE()
ROUTE2364.setFromField("fraction_changed")
ROUTE2364.setFromNode("PitchTimer")
ROUTE2364.setToField("set_fraction")
ROUTE2364.setToNode("Pitches_r_elbow_RotationInterpolator")

Group2326.addChildren(ROUTE2364)
ROUTE2365 = ROUTE()
ROUTE2365.setFromField("fraction_changed")
ROUTE2365.setFromNode("PitchTimer")
ROUTE2365.setToField("set_fraction")
ROUTE2365.setToNode("Pitches_r_shoulder_RotationInterpolator")

Group2326.addChildren(ROUTE2365)
ROUTE2366 = ROUTE()
ROUTE2366.setFromField("fraction_changed")
ROUTE2366.setFromNode("PitchTimer")
ROUTE2366.setToField("set_fraction")
ROUTE2366.setToNode("Pitches_l_wrist_RotationInterpolator")

Group2326.addChildren(ROUTE2366)
ROUTE2367 = ROUTE()
ROUTE2367.setFromField("fraction_changed")
ROUTE2367.setFromNode("PitchTimer")
ROUTE2367.setToField("set_fraction")
ROUTE2367.setToNode("Pitches_l_elbow_RotationInterpolator")

Group2326.addChildren(ROUTE2367)
ROUTE2368 = ROUTE()
ROUTE2368.setFromField("fraction_changed")
ROUTE2368.setFromNode("PitchTimer")
ROUTE2368.setToField("set_fraction")
ROUTE2368.setToNode("Pitches_l_shoulder_RotationInterpolator")

Group2326.addChildren(ROUTE2368)
ROUTE2369 = ROUTE()
ROUTE2369.setFromField("fraction_changed")
ROUTE2369.setFromNode("PitchTimer")
ROUTE2369.setToField("set_fraction")
ROUTE2369.setToNode("Pitches_head_RotationInterpolator")

Group2326.addChildren(ROUTE2369)
ROUTE2370 = ROUTE()
ROUTE2370.setFromField("fraction_changed")
ROUTE2370.setFromNode("PitchTimer")
ROUTE2370.setToField("set_fraction")
ROUTE2370.setToNode("Pitches_neck_RotationInterpolator")

Group2326.addChildren(ROUTE2370)
ROUTE2371 = ROUTE()
ROUTE2371.setFromField("fraction_changed")
ROUTE2371.setFromNode("PitchTimer")
ROUTE2371.setToField("set_fraction")
ROUTE2371.setToNode("Pitches_upper_body_RotationInterpolator")

Group2326.addChildren(ROUTE2371)
ROUTE2372 = ROUTE()
ROUTE2372.setFromField("fraction_changed")
ROUTE2372.setFromNode("PitchTimer")
ROUTE2372.setToField("set_fraction")
ROUTE2372.setToNode("Pitches_whole_body_RotationInterpolator")

Group2326.addChildren(ROUTE2372)
ROUTE2373 = ROUTE()
ROUTE2373.setFromField("fraction_changed")
ROUTE2373.setFromNode("PitchTimer")
ROUTE2373.setToField("set_fraction")
ROUTE2373.setToNode("Pitches_whole_body_TranslationInterpolator")

Group2326.addChildren(ROUTE2373)
ROUTE2374 = ROUTE()
ROUTE2374.setFromField("fraction_changed")
ROUTE2374.setFromNode("PitchTimer")
ROUTE2374.setToField("set_fraction")
ROUTE2374.setToNode("Pitch_l_sternoclavicular_RollInterpolator")

Group2326.addChildren(ROUTE2374)
ROUTE2375 = ROUTE()
ROUTE2375.setFromField("fraction_changed")
ROUTE2375.setFromNode("PitchTimer")
ROUTE2375.setToField("set_fraction")
ROUTE2375.setToNode("Pitch_l_acromioclavicular_RollInterpolator")

Group2326.addChildren(ROUTE2375)
ROUTE2376 = ROUTE()
ROUTE2376.setFromField("fraction_changed")
ROUTE2376.setFromNode("PitchTimer")
ROUTE2376.setToField("set_fraction")
ROUTE2376.setToNode("Pitch_r_sternoclavicular_RollInterpolator")

Group2326.addChildren(ROUTE2376)
ROUTE2377 = ROUTE()
ROUTE2377.setFromField("fraction_changed")
ROUTE2377.setFromNode("PitchTimer")
ROUTE2377.setToField("set_fraction")
ROUTE2377.setToNode("Pitch_r_acromioclavicular_RollInterpolator")

Group2326.addChildren(ROUTE2377)
ROUTE2378 = ROUTE()
ROUTE2378.setFromField("fraction_changed")
ROUTE2378.setFromNode("PitchTimer")
ROUTE2378.setToField("set_fraction")
ROUTE2378.setToNode("Pitch_r_metatarsal_PitchInterpolator")

Group2326.addChildren(ROUTE2378)
ROUTE2379 = ROUTE()
ROUTE2379.setFromField("fraction_changed")
ROUTE2379.setFromNode("PitchTimer")
ROUTE2379.setToField("set_fraction")
ROUTE2379.setToNode("Pitch_sacroiliac_YawInterpolator")

Group2326.addChildren(ROUTE2379)
ROUTE2380 = ROUTE()
ROUTE2380.setFromField("fraction_changed")
ROUTE2380.setFromNode("PitchTimer")
ROUTE2380.setToField("set_fraction")
ROUTE2380.setToNode("Pitch_vl5_YawInterpolator")

Group2326.addChildren(ROUTE2380)
ROUTE2381 = ROUTE()
ROUTE2381.setFromField("fraction_changed")
ROUTE2381.setFromNode("PitchTimer")
ROUTE2381.setToField("set_fraction")
ROUTE2381.setToNode("Pitch_vc6_YawInterpolator")

Group2326.addChildren(ROUTE2381)
ROUTE2382 = ROUTE()
ROUTE2382.setFromField("fraction_changed")
ROUTE2382.setFromNode("PitchTimer")
ROUTE2382.setToField("set_fraction")
ROUTE2382.setToNode("Pitch_l_thumb1_PitchInterpolator")

Group2326.addChildren(ROUTE2382)
ROUTE2383 = ROUTE()
ROUTE2383.setFromField("fraction_changed")
ROUTE2383.setFromNode("PitchTimer")
ROUTE2383.setToField("set_fraction")
ROUTE2383.setToNode("Pitch_r_thumb1_PitchInterpolator")

Group2326.addChildren(ROUTE2383)
ROUTE2384 = ROUTE()
ROUTE2384.setFromField("value_changed")
ROUTE2384.setFromNode("Pitches_r_ankle_RotationInterpolator")
ROUTE2384.setToField("rotation")
ROUTE2384.setToNode("hanim_r_ankle")

Group2326.addChildren(ROUTE2384)
ROUTE2385 = ROUTE()
ROUTE2385.setFromField("value_changed")
ROUTE2385.setFromNode("Pitches_r_knee_RotationInterpolator")
ROUTE2385.setToField("rotation")
ROUTE2385.setToNode("hanim_r_knee")

Group2326.addChildren(ROUTE2385)
ROUTE2386 = ROUTE()
ROUTE2386.setFromField("value_changed")
ROUTE2386.setFromNode("Pitches_r_hip_RotationInterpolator")
ROUTE2386.setToField("rotation")
ROUTE2386.setToNode("hanim_r_hip")

Group2326.addChildren(ROUTE2386)
ROUTE2387 = ROUTE()
ROUTE2387.setFromField("value_changed")
ROUTE2387.setFromNode("Pitches_l_ankle_RotationInterpolator")
ROUTE2387.setToField("rotation")
ROUTE2387.setToNode("hanim_l_ankle")

Group2326.addChildren(ROUTE2387)
ROUTE2388 = ROUTE()
ROUTE2388.setFromField("value_changed")
ROUTE2388.setFromNode("Pitches_l_knee_RotationInterpolator")
ROUTE2388.setToField("rotation")
ROUTE2388.setToNode("hanim_l_knee")

Group2326.addChildren(ROUTE2388)
ROUTE2389 = ROUTE()
ROUTE2389.setFromField("value_changed")
ROUTE2389.setFromNode("Pitches_l_hip_RotationInterpolator")
ROUTE2389.setToField("rotation")
ROUTE2389.setToNode("hanim_l_hip")

Group2326.addChildren(ROUTE2389)
ROUTE2390 = ROUTE()
ROUTE2390.setFromField("value_changed")
ROUTE2390.setFromNode("Pitches_lower_body_RotationInterpolator")
ROUTE2390.setToField("rotation")
ROUTE2390.setToNode("hanim_sacroiliac")

Group2326.addChildren(ROUTE2390)
ROUTE2391 = ROUTE()
ROUTE2391.setFromField("value_changed")
ROUTE2391.setFromNode("Pitches_r_wrist_RotationInterpolator")
ROUTE2391.setToField("rotation")
ROUTE2391.setToNode("hanim_r_wrist")

Group2326.addChildren(ROUTE2391)
ROUTE2392 = ROUTE()
ROUTE2392.setFromField("value_changed")
ROUTE2392.setFromNode("Pitches_r_elbow_RotationInterpolator")
ROUTE2392.setToField("rotation")
ROUTE2392.setToNode("hanim_r_elbow")

Group2326.addChildren(ROUTE2392)
ROUTE2393 = ROUTE()
ROUTE2393.setFromField("value_changed")
ROUTE2393.setFromNode("Pitches_r_shoulder_RotationInterpolator")
ROUTE2393.setToField("rotation")
ROUTE2393.setToNode("hanim_r_shoulder")

Group2326.addChildren(ROUTE2393)
ROUTE2394 = ROUTE()
ROUTE2394.setFromField("value_changed")
ROUTE2394.setFromNode("Pitches_l_wrist_RotationInterpolator")
ROUTE2394.setToField("rotation")
ROUTE2394.setToNode("hanim_l_wrist")

Group2326.addChildren(ROUTE2394)
ROUTE2395 = ROUTE()
ROUTE2395.setFromField("value_changed")
ROUTE2395.setFromNode("Pitches_l_elbow_RotationInterpolator")
ROUTE2395.setToField("rotation")
ROUTE2395.setToNode("hanim_l_elbow")

Group2326.addChildren(ROUTE2395)
ROUTE2396 = ROUTE()
ROUTE2396.setFromField("value_changed")
ROUTE2396.setFromNode("Pitches_l_shoulder_RotationInterpolator")
ROUTE2396.setToField("rotation")
ROUTE2396.setToNode("hanim_l_shoulder")

Group2326.addChildren(ROUTE2396)
ROUTE2397 = ROUTE()
ROUTE2397.setFromField("value_changed")
ROUTE2397.setFromNode("Pitches_head_RotationInterpolator")
ROUTE2397.setToField("rotation")
ROUTE2397.setToNode("hanim_skullbase")

Group2326.addChildren(ROUTE2397)
ROUTE2398 = ROUTE()
ROUTE2398.setFromField("value_changed")
ROUTE2398.setFromNode("Pitches_neck_RotationInterpolator")
ROUTE2398.setToField("rotation")
ROUTE2398.setToNode("hanim_vc4")

Group2326.addChildren(ROUTE2398)
ROUTE2399 = ROUTE()
ROUTE2399.setFromField("value_changed")
ROUTE2399.setFromNode("Pitches_upper_body_RotationInterpolator")
ROUTE2399.setToField("rotation")
ROUTE2399.setToNode("hanim_vl1")

Group2326.addChildren(ROUTE2399)
ROUTE2400 = ROUTE()
ROUTE2400.setFromField("value_changed")
ROUTE2400.setFromNode("Pitches_whole_body_RotationInterpolator")
ROUTE2400.setToField("rotation")
ROUTE2400.setToNode("hanim_humanoid_root")

Group2326.addChildren(ROUTE2400)
ROUTE2401 = ROUTE()
ROUTE2401.setFromField("value_changed")
ROUTE2401.setFromNode("Pitches_whole_body_TranslationInterpolator")
ROUTE2401.setToField("translation")
ROUTE2401.setToNode("hanim_humanoid_root")

Group2326.addChildren(ROUTE2401)
ROUTE2402 = ROUTE()
ROUTE2402.setFromField("value_changed")
ROUTE2402.setFromNode("Pitch_l_sternoclavicular_RollInterpolator")
ROUTE2402.setToField("rotation")
ROUTE2402.setToNode("hanim_l_sternoclavicular")

Group2326.addChildren(ROUTE2402)
ROUTE2403 = ROUTE()
ROUTE2403.setFromField("value_changed")
ROUTE2403.setFromNode("Pitch_l_acromioclavicular_RollInterpolator")
ROUTE2403.setToField("rotation")
ROUTE2403.setToNode("hanim_l_acromioclavicular")

Group2326.addChildren(ROUTE2403)
ROUTE2404 = ROUTE()
ROUTE2404.setFromField("value_changed")
ROUTE2404.setFromNode("Pitch_r_sternoclavicular_RollInterpolator")
ROUTE2404.setToField("rotation")
ROUTE2404.setToNode("hanim_r_sternoclavicular")

Group2326.addChildren(ROUTE2404)
ROUTE2405 = ROUTE()
ROUTE2405.setFromField("value_changed")
ROUTE2405.setFromNode("Pitch_r_acromioclavicular_RollInterpolator")
ROUTE2405.setToField("rotation")
ROUTE2405.setToNode("hanim_r_acromioclavicular")

Group2326.addChildren(ROUTE2405)
ROUTE2406 = ROUTE()
ROUTE2406.setFromField("value_changed")
ROUTE2406.setFromNode("Pitch_r_metatarsal_PitchInterpolator")
ROUTE2406.setToField("rotation")
ROUTE2406.setToNode("hanim_l_metatarsal")

Group2326.addChildren(ROUTE2406)
ROUTE2407 = ROUTE()
ROUTE2407.setFromField("value_changed")
ROUTE2407.setFromNode("Pitch_r_metatarsal_PitchInterpolator")
ROUTE2407.setToField("rotation")
ROUTE2407.setToNode("hanim_r_metatarsal")

Group2326.addChildren(ROUTE2407)
ROUTE2408 = ROUTE()
ROUTE2408.setFromField("value_changed")
ROUTE2408.setFromNode("Pitch_sacroiliac_YawInterpolator")
ROUTE2408.setToField("rotation")
ROUTE2408.setToNode("hanim_sacroiliac")

Group2326.addChildren(ROUTE2408)
ROUTE2409 = ROUTE()
ROUTE2409.setFromField("value_changed")
ROUTE2409.setFromNode("Pitch_vl5_YawInterpolator")
ROUTE2409.setToField("rotation")
ROUTE2409.setToNode("hanim_vl5")

Group2326.addChildren(ROUTE2409)
ROUTE2410 = ROUTE()
ROUTE2410.setFromField("value_changed")
ROUTE2410.setFromNode("Pitch_vc6_YawInterpolator")
ROUTE2410.setToField("rotation")
ROUTE2410.setToNode("hanim_vc6")

Group2326.addChildren(ROUTE2410)
ROUTE2411 = ROUTE()
ROUTE2411.setFromField("value_changed")
ROUTE2411.setFromNode("Pitch_l_thumb1_PitchInterpolator")
ROUTE2411.setToField("rotation")
ROUTE2411.setToNode("hanim_l_thumb1")

Group2326.addChildren(ROUTE2411)
ROUTE2412 = ROUTE()
ROUTE2412.setFromField("value_changed")
ROUTE2412.setFromNode("Pitch_r_thumb1_PitchInterpolator")
ROUTE2412.setToField("rotation")
ROUTE2412.setToNode("hanim_r_thumb1")

Group2326.addChildren(ROUTE2412)

Scene31.addChildren(Group2326)
Group2413 = Group()
Group2413.setDEF("YawsAnimation")
TimeSensor2414 = TimeSensor()
TimeSensor2414.setDEF("YawTimer")
TimeSensor2414.setCycleInterval(5.73)
TimeSensor2414.setLoop(True)

Group2413.addChildren(TimeSensor2414)
OrientationInterpolator2415 = OrientationInterpolator()
OrientationInterpolator2415.setDEF("Yaw_r_metatarsal_PitchInterpolator")
OrientationInterpolator2415.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2415.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2415)
OrientationInterpolator2416 = OrientationInterpolator()
OrientationInterpolator2416.setDEF("Yaws_r_ankle_RotationInterpolator")
OrientationInterpolator2416.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2416.setKeyValue([0,0,1,0,0,-1,0,1.5,0,0,1,0,0,1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2416)
OrientationInterpolator2417 = OrientationInterpolator()
OrientationInterpolator2417.setDEF("Yaws_r_knee_RotationInterpolator")
OrientationInterpolator2417.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2417.setKeyValue([0,0,1,0,0,1,0,1.5,0,0,1,0,0,-1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2417)
OrientationInterpolator2418 = OrientationInterpolator()
OrientationInterpolator2418.setDEF("Yaws_r_hip_RotationInterpolator")
OrientationInterpolator2418.setKey([0,0.5,1])
OrientationInterpolator2418.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2418)
OrientationInterpolator2419 = OrientationInterpolator()
OrientationInterpolator2419.setDEF("Yaws_l_ankle_RotationInterpolator")
OrientationInterpolator2419.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2419.setKeyValue([0,0,1,0,0,1,0,1.5,0,0,1,0,0,-1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2419)
OrientationInterpolator2420 = OrientationInterpolator()
OrientationInterpolator2420.setDEF("Yaws_l_knee_RotationInterpolator")
OrientationInterpolator2420.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2420.setKeyValue([0,0,1,0,0,-1,0,1.5,0,0,1,0,0,1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2420)
OrientationInterpolator2421 = OrientationInterpolator()
OrientationInterpolator2421.setDEF("Yaws_l_hip_RotationInterpolator")
OrientationInterpolator2421.setKey([0,0.5,1])
OrientationInterpolator2421.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2421)
OrientationInterpolator2422 = OrientationInterpolator()
OrientationInterpolator2422.setDEF("Yaws_r_wrist_RotationInterpolator")
OrientationInterpolator2422.setKey([0,0.5,1])
OrientationInterpolator2422.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2422)
OrientationInterpolator2423 = OrientationInterpolator()
OrientationInterpolator2423.setDEF("Yaws_r_elbow_RotationInterpolator")
OrientationInterpolator2423.setKey([0,0.5,1])
OrientationInterpolator2423.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2423)
OrientationInterpolator2424 = OrientationInterpolator()
OrientationInterpolator2424.setDEF("Yaws_r_shoulder_RotationInterpolator")
OrientationInterpolator2424.setKey([0,0.5,1])
OrientationInterpolator2424.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2424)
OrientationInterpolator2425 = OrientationInterpolator()
OrientationInterpolator2425.setDEF("Yaws_l_wrist_RotationInterpolator")
OrientationInterpolator2425.setKey([0,0.5,1])
OrientationInterpolator2425.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2425)
OrientationInterpolator2426 = OrientationInterpolator()
OrientationInterpolator2426.setDEF("Yaws_l_elbow_RotationInterpolator")
OrientationInterpolator2426.setKey([0,0.5,1])
OrientationInterpolator2426.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2426)
OrientationInterpolator2427 = OrientationInterpolator()
OrientationInterpolator2427.setDEF("Yaws_l_shoulder_RotationInterpolator")
OrientationInterpolator2427.setKey([0,0.5,1])
OrientationInterpolator2427.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2427)
OrientationInterpolator2428 = OrientationInterpolator()
OrientationInterpolator2428.setDEF("Yaws_head_RotationInterpolator")
OrientationInterpolator2428.setKey([0,0.5,1])
OrientationInterpolator2428.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2428)
OrientationInterpolator2429 = OrientationInterpolator()
OrientationInterpolator2429.setDEF("Yaws_neck_RotationInterpolator")
OrientationInterpolator2429.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2429.setKeyValue([0,0,1,0,0,1,0,1.5,0,0,1,0,0,-1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2429)
OrientationInterpolator2430 = OrientationInterpolator()
OrientationInterpolator2430.setDEF("Yaws_upper_body_RotationInterpolator")
OrientationInterpolator2430.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2430.setKeyValue([0,0,1,0,0,-1,0,1.5,0,0,1,0,0,1,0,1.5,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2430)
OrientationInterpolator2431 = OrientationInterpolator()
OrientationInterpolator2431.setDEF("Yaws_lower_body_RotationInterpolator")
OrientationInterpolator2431.setKey([0,0.5,1])
OrientationInterpolator2431.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2431)
OrientationInterpolator2432 = OrientationInterpolator()
OrientationInterpolator2432.setDEF("Yaws_whole_body_RotationInterpolator")
OrientationInterpolator2432.setKey([0,0.5,1])
OrientationInterpolator2432.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2432)
PositionInterpolator2433 = PositionInterpolator()
PositionInterpolator2433.setDEF("Yaws_whole_body_TranslationInterpolator")
PositionInterpolator2433.setKey([0,0.5,1])
PositionInterpolator2433.setKeyValue([0,0,0,0,0,0,0,0,0])

Group2413.addChildren(PositionInterpolator2433)
OrientationInterpolator2434 = OrientationInterpolator()
OrientationInterpolator2434.setDEF("Yaw_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2434.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2434.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2434)
OrientationInterpolator2435 = OrientationInterpolator()
OrientationInterpolator2435.setDEF("Yaw_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2435.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2435.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2435)
OrientationInterpolator2436 = OrientationInterpolator()
OrientationInterpolator2436.setDEF("Yaw_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2436.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2436.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2436)
OrientationInterpolator2437 = OrientationInterpolator()
OrientationInterpolator2437.setDEF("Yaw_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2437.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2437.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2437)
OrientationInterpolator2438 = OrientationInterpolator()
OrientationInterpolator2438.setDEF("Yaw_sacroiliac_YawInterpolator")
OrientationInterpolator2438.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2438.setKeyValue([0,1,0,0,0,-1,0,0.1,0,1,0,0,0,1,0,0.24,0,-1,0,0.4,0,1,0,0])

Group2413.addChildren(OrientationInterpolator2438)
OrientationInterpolator2439 = OrientationInterpolator()
OrientationInterpolator2439.setDEF("Yaw_vl5_YawInterpolator")
OrientationInterpolator2439.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2439.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2439)
OrientationInterpolator2440 = OrientationInterpolator()
OrientationInterpolator2440.setDEF("Yaw_vc6_YawInterpolator")
OrientationInterpolator2440.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2440.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2440)
OrientationInterpolator2441 = OrientationInterpolator()
OrientationInterpolator2441.setDEF("Yaw_l_thumb1_PitchInterpolator")
OrientationInterpolator2441.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2441.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2441)
OrientationInterpolator2442 = OrientationInterpolator()
OrientationInterpolator2442.setDEF("Yaw_r_thumb1_PitchInterpolator")
OrientationInterpolator2442.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2442.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2413.addChildren(OrientationInterpolator2442)
ROUTE2443 = ROUTE()
ROUTE2443.setFromField("fraction_changed")
ROUTE2443.setFromNode("YawTimer")
ROUTE2443.setToField("set_fraction")
ROUTE2443.setToNode("Yaws_r_ankle_RotationInterpolator")

Group2413.addChildren(ROUTE2443)
ROUTE2444 = ROUTE()
ROUTE2444.setFromField("fraction_changed")
ROUTE2444.setFromNode("YawTimer")
ROUTE2444.setToField("set_fraction")
ROUTE2444.setToNode("Yaws_r_knee_RotationInterpolator")

Group2413.addChildren(ROUTE2444)
ROUTE2445 = ROUTE()
ROUTE2445.setFromField("fraction_changed")
ROUTE2445.setFromNode("YawTimer")
ROUTE2445.setToField("set_fraction")
ROUTE2445.setToNode("Yaws_r_hip_RotationInterpolator")

Group2413.addChildren(ROUTE2445)
ROUTE2446 = ROUTE()
ROUTE2446.setFromField("fraction_changed")
ROUTE2446.setFromNode("YawTimer")
ROUTE2446.setToField("set_fraction")
ROUTE2446.setToNode("Yaws_l_ankle_RotationInterpolator")

Group2413.addChildren(ROUTE2446)
ROUTE2447 = ROUTE()
ROUTE2447.setFromField("fraction_changed")
ROUTE2447.setFromNode("YawTimer")
ROUTE2447.setToField("set_fraction")
ROUTE2447.setToNode("Yaws_l_knee_RotationInterpolator")

Group2413.addChildren(ROUTE2447)
ROUTE2448 = ROUTE()
ROUTE2448.setFromField("fraction_changed")
ROUTE2448.setFromNode("YawTimer")
ROUTE2448.setToField("set_fraction")
ROUTE2448.setToNode("Yaws_l_hip_RotationInterpolator")

Group2413.addChildren(ROUTE2448)
ROUTE2449 = ROUTE()
ROUTE2449.setFromField("fraction_changed")
ROUTE2449.setFromNode("YawTimer")
ROUTE2449.setToField("set_fraction")
ROUTE2449.setToNode("Yaws_lower_body_RotationInterpolator")

Group2413.addChildren(ROUTE2449)
ROUTE2450 = ROUTE()
ROUTE2450.setFromField("fraction_changed")
ROUTE2450.setFromNode("YawTimer")
ROUTE2450.setToField("set_fraction")
ROUTE2450.setToNode("Yaws_r_wrist_RotationInterpolator")

Group2413.addChildren(ROUTE2450)
ROUTE2451 = ROUTE()
ROUTE2451.setFromField("fraction_changed")
ROUTE2451.setFromNode("YawTimer")
ROUTE2451.setToField("set_fraction")
ROUTE2451.setToNode("Yaws_r_elbow_RotationInterpolator")

Group2413.addChildren(ROUTE2451)
ROUTE2452 = ROUTE()
ROUTE2452.setFromField("fraction_changed")
ROUTE2452.setFromNode("YawTimer")
ROUTE2452.setToField("set_fraction")
ROUTE2452.setToNode("Yaws_r_shoulder_RotationInterpolator")

Group2413.addChildren(ROUTE2452)
ROUTE2453 = ROUTE()
ROUTE2453.setFromField("fraction_changed")
ROUTE2453.setFromNode("YawTimer")
ROUTE2453.setToField("set_fraction")
ROUTE2453.setToNode("Yaws_l_wrist_RotationInterpolator")

Group2413.addChildren(ROUTE2453)
ROUTE2454 = ROUTE()
ROUTE2454.setFromField("fraction_changed")
ROUTE2454.setFromNode("YawTimer")
ROUTE2454.setToField("set_fraction")
ROUTE2454.setToNode("Yaws_l_elbow_RotationInterpolator")

Group2413.addChildren(ROUTE2454)
ROUTE2455 = ROUTE()
ROUTE2455.setFromField("fraction_changed")
ROUTE2455.setFromNode("YawTimer")
ROUTE2455.setToField("set_fraction")
ROUTE2455.setToNode("Yaws_l_shoulder_RotationInterpolator")

Group2413.addChildren(ROUTE2455)
ROUTE2456 = ROUTE()
ROUTE2456.setFromField("fraction_changed")
ROUTE2456.setFromNode("YawTimer")
ROUTE2456.setToField("set_fraction")
ROUTE2456.setToNode("Yaws_head_RotationInterpolator")

Group2413.addChildren(ROUTE2456)
ROUTE2457 = ROUTE()
ROUTE2457.setFromField("fraction_changed")
ROUTE2457.setFromNode("YawTimer")
ROUTE2457.setToField("set_fraction")
ROUTE2457.setToNode("Yaws_neck_RotationInterpolator")

Group2413.addChildren(ROUTE2457)
ROUTE2458 = ROUTE()
ROUTE2458.setFromField("fraction_changed")
ROUTE2458.setFromNode("YawTimer")
ROUTE2458.setToField("set_fraction")
ROUTE2458.setToNode("Yaws_upper_body_RotationInterpolator")

Group2413.addChildren(ROUTE2458)
ROUTE2459 = ROUTE()
ROUTE2459.setFromField("fraction_changed")
ROUTE2459.setFromNode("YawTimer")
ROUTE2459.setToField("set_fraction")
ROUTE2459.setToNode("Yaws_whole_body_RotationInterpolator")

Group2413.addChildren(ROUTE2459)
ROUTE2460 = ROUTE()
ROUTE2460.setFromField("fraction_changed")
ROUTE2460.setFromNode("YawTimer")
ROUTE2460.setToField("set_fraction")
ROUTE2460.setToNode("Yaws_whole_body_TranslationInterpolator")

Group2413.addChildren(ROUTE2460)
ROUTE2461 = ROUTE()
ROUTE2461.setFromField("fraction_changed")
ROUTE2461.setFromNode("YawTimer")
ROUTE2461.setToField("set_fraction")
ROUTE2461.setToNode("Yaw_l_sternoclavicular_RollInterpolator")

Group2413.addChildren(ROUTE2461)
ROUTE2462 = ROUTE()
ROUTE2462.setFromField("fraction_changed")
ROUTE2462.setFromNode("YawTimer")
ROUTE2462.setToField("set_fraction")
ROUTE2462.setToNode("Yaw_l_acromioclavicular_RollInterpolator")

Group2413.addChildren(ROUTE2462)
ROUTE2463 = ROUTE()
ROUTE2463.setFromField("fraction_changed")
ROUTE2463.setFromNode("YawTimer")
ROUTE2463.setToField("set_fraction")
ROUTE2463.setToNode("Yaw_r_sternoclavicular_RollInterpolator")

Group2413.addChildren(ROUTE2463)
ROUTE2464 = ROUTE()
ROUTE2464.setFromField("fraction_changed")
ROUTE2464.setFromNode("YawTimer")
ROUTE2464.setToField("set_fraction")
ROUTE2464.setToNode("Yaw_r_acromioclavicular_RollInterpolator")

Group2413.addChildren(ROUTE2464)
ROUTE2465 = ROUTE()
ROUTE2465.setFromField("fraction_changed")
ROUTE2465.setFromNode("YawTimer")
ROUTE2465.setToField("set_fraction")
ROUTE2465.setToNode("Yaw_r_metatarsal_PitchInterpolator")

Group2413.addChildren(ROUTE2465)
ROUTE2466 = ROUTE()
ROUTE2466.setFromField("fraction_changed")
ROUTE2466.setFromNode("YawTimer")
ROUTE2466.setToField("set_fraction")
ROUTE2466.setToNode("Yaw_sacroiliac_YawInterpolator")

Group2413.addChildren(ROUTE2466)
ROUTE2467 = ROUTE()
ROUTE2467.setFromField("fraction_changed")
ROUTE2467.setFromNode("YawTimer")
ROUTE2467.setToField("set_fraction")
ROUTE2467.setToNode("Yaw_vl5_YawInterpolator")

Group2413.addChildren(ROUTE2467)
ROUTE2468 = ROUTE()
ROUTE2468.setFromField("fraction_changed")
ROUTE2468.setFromNode("YawTimer")
ROUTE2468.setToField("set_fraction")
ROUTE2468.setToNode("Yaw_vc6_YawInterpolator")

Group2413.addChildren(ROUTE2468)
ROUTE2469 = ROUTE()
ROUTE2469.setFromField("fraction_changed")
ROUTE2469.setFromNode("YawTimer")
ROUTE2469.setToField("set_fraction")
ROUTE2469.setToNode("Yaw_l_thumb1_PitchInterpolator")

Group2413.addChildren(ROUTE2469)
ROUTE2470 = ROUTE()
ROUTE2470.setFromField("fraction_changed")
ROUTE2470.setFromNode("YawTimer")
ROUTE2470.setToField("set_fraction")
ROUTE2470.setToNode("Yaw_r_thumb1_PitchInterpolator")

Group2413.addChildren(ROUTE2470)
ROUTE2471 = ROUTE()
ROUTE2471.setFromField("value_changed")
ROUTE2471.setFromNode("Yaws_r_ankle_RotationInterpolator")
ROUTE2471.setToField("rotation")
ROUTE2471.setToNode("hanim_r_ankle")

Group2413.addChildren(ROUTE2471)
ROUTE2472 = ROUTE()
ROUTE2472.setFromField("value_changed")
ROUTE2472.setFromNode("Yaws_r_knee_RotationInterpolator")
ROUTE2472.setToField("rotation")
ROUTE2472.setToNode("hanim_r_knee")

Group2413.addChildren(ROUTE2472)
ROUTE2473 = ROUTE()
ROUTE2473.setFromField("value_changed")
ROUTE2473.setFromNode("Yaws_r_hip_RotationInterpolator")
ROUTE2473.setToField("rotation")
ROUTE2473.setToNode("hanim_r_hip")

Group2413.addChildren(ROUTE2473)
ROUTE2474 = ROUTE()
ROUTE2474.setFromField("value_changed")
ROUTE2474.setFromNode("Yaws_l_ankle_RotationInterpolator")
ROUTE2474.setToField("rotation")
ROUTE2474.setToNode("hanim_l_ankle")

Group2413.addChildren(ROUTE2474)
ROUTE2475 = ROUTE()
ROUTE2475.setFromField("value_changed")
ROUTE2475.setFromNode("Yaws_l_knee_RotationInterpolator")
ROUTE2475.setToField("rotation")
ROUTE2475.setToNode("hanim_l_knee")

Group2413.addChildren(ROUTE2475)
ROUTE2476 = ROUTE()
ROUTE2476.setFromField("value_changed")
ROUTE2476.setFromNode("Yaws_l_hip_RotationInterpolator")
ROUTE2476.setToField("rotation")
ROUTE2476.setToNode("hanim_l_hip")

Group2413.addChildren(ROUTE2476)
ROUTE2477 = ROUTE()
ROUTE2477.setFromField("value_changed")
ROUTE2477.setFromNode("Yaws_lower_body_RotationInterpolator")
ROUTE2477.setToField("rotation")
ROUTE2477.setToNode("hanim_sacroiliac")

Group2413.addChildren(ROUTE2477)
ROUTE2478 = ROUTE()
ROUTE2478.setFromField("value_changed")
ROUTE2478.setFromNode("Yaws_r_wrist_RotationInterpolator")
ROUTE2478.setToField("rotation")
ROUTE2478.setToNode("hanim_r_wrist")

Group2413.addChildren(ROUTE2478)
ROUTE2479 = ROUTE()
ROUTE2479.setFromField("value_changed")
ROUTE2479.setFromNode("Yaws_r_elbow_RotationInterpolator")
ROUTE2479.setToField("rotation")
ROUTE2479.setToNode("hanim_r_elbow")

Group2413.addChildren(ROUTE2479)
ROUTE2480 = ROUTE()
ROUTE2480.setFromField("value_changed")
ROUTE2480.setFromNode("Yaws_r_shoulder_RotationInterpolator")
ROUTE2480.setToField("rotation")
ROUTE2480.setToNode("hanim_r_shoulder")

Group2413.addChildren(ROUTE2480)
ROUTE2481 = ROUTE()
ROUTE2481.setFromField("value_changed")
ROUTE2481.setFromNode("Yaws_l_wrist_RotationInterpolator")
ROUTE2481.setToField("rotation")
ROUTE2481.setToNode("hanim_l_wrist")

Group2413.addChildren(ROUTE2481)
ROUTE2482 = ROUTE()
ROUTE2482.setFromField("value_changed")
ROUTE2482.setFromNode("Yaws_l_elbow_RotationInterpolator")
ROUTE2482.setToField("rotation")
ROUTE2482.setToNode("hanim_l_elbow")

Group2413.addChildren(ROUTE2482)
ROUTE2483 = ROUTE()
ROUTE2483.setFromField("value_changed")
ROUTE2483.setFromNode("Yaws_l_shoulder_RotationInterpolator")
ROUTE2483.setToField("rotation")
ROUTE2483.setToNode("hanim_l_shoulder")

Group2413.addChildren(ROUTE2483)
ROUTE2484 = ROUTE()
ROUTE2484.setFromField("value_changed")
ROUTE2484.setFromNode("Yaws_head_RotationInterpolator")
ROUTE2484.setToField("rotation")
ROUTE2484.setToNode("hanim_skullbase")

Group2413.addChildren(ROUTE2484)
ROUTE2485 = ROUTE()
ROUTE2485.setFromField("value_changed")
ROUTE2485.setFromNode("Yaws_neck_RotationInterpolator")
ROUTE2485.setToField("rotation")
ROUTE2485.setToNode("hanim_vc4")

Group2413.addChildren(ROUTE2485)
ROUTE2486 = ROUTE()
ROUTE2486.setFromField("value_changed")
ROUTE2486.setFromNode("Yaws_upper_body_RotationInterpolator")
ROUTE2486.setToField("rotation")
ROUTE2486.setToNode("hanim_vl1")

Group2413.addChildren(ROUTE2486)
ROUTE2487 = ROUTE()
ROUTE2487.setFromField("value_changed")
ROUTE2487.setFromNode("Yaws_whole_body_RotationInterpolator")
ROUTE2487.setToField("rotation")
ROUTE2487.setToNode("hanim_humanoid_root")

Group2413.addChildren(ROUTE2487)
ROUTE2488 = ROUTE()
ROUTE2488.setFromField("value_changed")
ROUTE2488.setFromNode("Yaws_whole_body_TranslationInterpolator")
ROUTE2488.setToField("translation")
ROUTE2488.setToNode("hanim_humanoid_root")

Group2413.addChildren(ROUTE2488)
ROUTE2489 = ROUTE()
ROUTE2489.setFromField("value_changed")
ROUTE2489.setFromNode("Yaw_l_sternoclavicular_RollInterpolator")
ROUTE2489.setToField("rotation")
ROUTE2489.setToNode("hanim_l_sternoclavicular")

Group2413.addChildren(ROUTE2489)
ROUTE2490 = ROUTE()
ROUTE2490.setFromField("value_changed")
ROUTE2490.setFromNode("Yaw_l_acromioclavicular_RollInterpolator")
ROUTE2490.setToField("rotation")
ROUTE2490.setToNode("hanim_l_acromioclavicular")

Group2413.addChildren(ROUTE2490)
ROUTE2491 = ROUTE()
ROUTE2491.setFromField("value_changed")
ROUTE2491.setFromNode("Yaw_r_sternoclavicular_RollInterpolator")
ROUTE2491.setToField("rotation")
ROUTE2491.setToNode("hanim_r_sternoclavicular")

Group2413.addChildren(ROUTE2491)
ROUTE2492 = ROUTE()
ROUTE2492.setFromField("value_changed")
ROUTE2492.setFromNode("Yaw_r_acromioclavicular_RollInterpolator")
ROUTE2492.setToField("rotation")
ROUTE2492.setToNode("hanim_r_acromioclavicular")

Group2413.addChildren(ROUTE2492)
ROUTE2493 = ROUTE()
ROUTE2493.setFromField("value_changed")
ROUTE2493.setFromNode("Yaw_r_metatarsal_PitchInterpolator")
ROUTE2493.setToField("rotation")
ROUTE2493.setToNode("hanim_l_metatarsal")

Group2413.addChildren(ROUTE2493)
ROUTE2494 = ROUTE()
ROUTE2494.setFromField("value_changed")
ROUTE2494.setFromNode("Yaw_r_metatarsal_PitchInterpolator")
ROUTE2494.setToField("rotation")
ROUTE2494.setToNode("hanim_r_metatarsal")

Group2413.addChildren(ROUTE2494)
ROUTE2495 = ROUTE()
ROUTE2495.setFromField("value_changed")
ROUTE2495.setFromNode("Yaw_sacroiliac_YawInterpolator")
ROUTE2495.setToField("rotation")
ROUTE2495.setToNode("hanim_sacroiliac")

Group2413.addChildren(ROUTE2495)
ROUTE2496 = ROUTE()
ROUTE2496.setFromField("value_changed")
ROUTE2496.setFromNode("Yaw_vl5_YawInterpolator")
ROUTE2496.setToField("rotation")
ROUTE2496.setToNode("hanim_vl5")

Group2413.addChildren(ROUTE2496)
ROUTE2497 = ROUTE()
ROUTE2497.setFromField("value_changed")
ROUTE2497.setFromNode("Yaw_vc6_YawInterpolator")
ROUTE2497.setToField("rotation")
ROUTE2497.setToNode("hanim_vc6")

Group2413.addChildren(ROUTE2497)
ROUTE2498 = ROUTE()
ROUTE2498.setFromField("value_changed")
ROUTE2498.setFromNode("Yaw_l_thumb1_PitchInterpolator")
ROUTE2498.setToField("rotation")
ROUTE2498.setToNode("hanim_l_thumb1")

Group2413.addChildren(ROUTE2498)
ROUTE2499 = ROUTE()
ROUTE2499.setFromField("value_changed")
ROUTE2499.setFromNode("Yaw_r_thumb1_PitchInterpolator")
ROUTE2499.setToField("rotation")
ROUTE2499.setToNode("hanim_r_thumb1")

Group2413.addChildren(ROUTE2499)

Scene31.addChildren(Group2413)
Group2500 = Group()
Group2500.setDEF("RollsAnimation")
TimeSensor2501 = TimeSensor()
TimeSensor2501.setDEF("RollTimer")
TimeSensor2501.setCycleInterval(5.73)
TimeSensor2501.setLoop(True)

Group2500.addChildren(TimeSensor2501)
OrientationInterpolator2502 = OrientationInterpolator()
OrientationInterpolator2502.setDEF("Roll_r_metatarsal_PitchInterpolator")
OrientationInterpolator2502.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2502.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2502)
OrientationInterpolator2503 = OrientationInterpolator()
OrientationInterpolator2503.setDEF("Rolls_r_ankle_RotationInterpolator")
OrientationInterpolator2503.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2503.setKeyValue([0,0,1,0,0,0,1,1.5,0,0,1,0,0,0,1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2503)
OrientationInterpolator2504 = OrientationInterpolator()
OrientationInterpolator2504.setDEF("Rolls_r_knee_RotationInterpolator")
OrientationInterpolator2504.setKey([0,0.5,1])
OrientationInterpolator2504.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2504)
OrientationInterpolator2505 = OrientationInterpolator()
OrientationInterpolator2505.setDEF("Rolls_r_hip_RotationInterpolator")
OrientationInterpolator2505.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2505.setKeyValue([0,0,-1,0,0,0,-1,1.5,0,0,1,0,0,0,-1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2505)
OrientationInterpolator2506 = OrientationInterpolator()
OrientationInterpolator2506.setDEF("Rolls_l_ankle_RotationInterpolator")
OrientationInterpolator2506.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2506.setKeyValue([0,0,1,0,0,0,-1,1.5,0,0,1,0,0,0,-1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2506)
OrientationInterpolator2507 = OrientationInterpolator()
OrientationInterpolator2507.setDEF("Rolls_l_knee_RotationInterpolator")
OrientationInterpolator2507.setKey([0,0.5,1])
OrientationInterpolator2507.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2507)
OrientationInterpolator2508 = OrientationInterpolator()
OrientationInterpolator2508.setDEF("Rolls_l_hip_RotationInterpolator")
OrientationInterpolator2508.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2508.setKeyValue([0,0,1,0,0,0,1,1.5,0,0,1,0,0,0,1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2508)
OrientationInterpolator2509 = OrientationInterpolator()
OrientationInterpolator2509.setDEF("Rolls_r_wrist_RotationInterpolator")
OrientationInterpolator2509.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2509.setKeyValue([0,0,1,0,0,0,-1,1.5,0,0,1,0,0,0,1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2509)
OrientationInterpolator2510 = OrientationInterpolator()
OrientationInterpolator2510.setDEF("Rolls_r_elbow_RotationInterpolator")
OrientationInterpolator2510.setKey([0,0.5,1])
OrientationInterpolator2510.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2510)
OrientationInterpolator2511 = OrientationInterpolator()
OrientationInterpolator2511.setDEF("Rolls_r_shoulder_RotationInterpolator")
OrientationInterpolator2511.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2511.setKeyValue([0,0,1,0,0,0,-1,1.5,0,0,-1,3,0,0,-1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2511)
OrientationInterpolator2512 = OrientationInterpolator()
OrientationInterpolator2512.setDEF("Rolls_l_wrist_RotationInterpolator")
OrientationInterpolator2512.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2512.setKeyValue([0,0,1,0,0,0,1,1.5,0,0,1,0,0,0,-1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2512)
OrientationInterpolator2513 = OrientationInterpolator()
OrientationInterpolator2513.setDEF("Rolls_l_elbow_RotationInterpolator")
OrientationInterpolator2513.setKey([0,0.5,1])
OrientationInterpolator2513.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2513)
OrientationInterpolator2514 = OrientationInterpolator()
OrientationInterpolator2514.setDEF("Rolls_l_shoulder_RotationInterpolator")
OrientationInterpolator2514.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2514.setKeyValue([0,0,1,0,0,0,1,1.5,0,0,1,3,0,0,1,1.5,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2514)
OrientationInterpolator2515 = OrientationInterpolator()
OrientationInterpolator2515.setDEF("Rolls_head_RotationInterpolator")
OrientationInterpolator2515.setKey([0,0.5,1])
OrientationInterpolator2515.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2515)
OrientationInterpolator2516 = OrientationInterpolator()
OrientationInterpolator2516.setDEF("Rolls_neck_RotationInterpolator")
OrientationInterpolator2516.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2516.setKeyValue([0,0,1,0,0,0,1,1.25,0,0,1,0,0,0,-1,1.25,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2516)
OrientationInterpolator2517 = OrientationInterpolator()
OrientationInterpolator2517.setDEF("Rolls_lower_body_RotationInterpolator")
OrientationInterpolator2517.setKey([0,0.5,1])
OrientationInterpolator2517.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2517)
OrientationInterpolator2518 = OrientationInterpolator()
OrientationInterpolator2518.setDEF("Rolls_upper_body_RotationInterpolator")
OrientationInterpolator2518.setKey([0,0.5,1])
OrientationInterpolator2518.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2518)
OrientationInterpolator2519 = OrientationInterpolator()
OrientationInterpolator2519.setDEF("Rolls_whole_body_RotationInterpolator")
OrientationInterpolator2519.setKey([0,0.5,1])
OrientationInterpolator2519.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2519)
PositionInterpolator2520 = PositionInterpolator()
PositionInterpolator2520.setDEF("Rolls_whole_body_TranslationInterpolator")
PositionInterpolator2520.setKey([0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1])
PositionInterpolator2520.setKeyValue([0,0,0,0,-0.25,0,0,-0.8,0,0,-0.25,0,0,0,0,0,-0.25,0,0,-0.8,0,0,-0.25,0,0,0,0])

Group2500.addChildren(PositionInterpolator2520)
OrientationInterpolator2521 = OrientationInterpolator()
OrientationInterpolator2521.setDEF("Roll_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2521.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2521.setKeyValue([0,0,1,0,0,0,1,0.2,0,0,1,0.22,0,0,1,0.2,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2521)
OrientationInterpolator2522 = OrientationInterpolator()
OrientationInterpolator2522.setDEF("Roll_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2522.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2522.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2522)
OrientationInterpolator2523 = OrientationInterpolator()
OrientationInterpolator2523.setDEF("Roll_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2523.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2523.setKeyValue([0,0,1,0,0,0,1,-0.2,0,0,1,-0.22,0,0,1,-0.2,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2523)
OrientationInterpolator2524 = OrientationInterpolator()
OrientationInterpolator2524.setDEF("Roll_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2524.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2524.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,-0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2524)
OrientationInterpolator2525 = OrientationInterpolator()
OrientationInterpolator2525.setDEF("Roll_sacroiliac_YawInterpolator")
OrientationInterpolator2525.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2525.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2525)
OrientationInterpolator2526 = OrientationInterpolator()
OrientationInterpolator2526.setDEF("Roll_vl5_YawInterpolator")
OrientationInterpolator2526.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2526.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2526)
OrientationInterpolator2527 = OrientationInterpolator()
OrientationInterpolator2527.setDEF("Roll_vc6_YawInterpolator")
OrientationInterpolator2527.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2527.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2527)
OrientationInterpolator2528 = OrientationInterpolator()
OrientationInterpolator2528.setDEF("Roll_l_thumb1_PitchInterpolator")
OrientationInterpolator2528.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2528.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2528)
OrientationInterpolator2529 = OrientationInterpolator()
OrientationInterpolator2529.setDEF("Roll_r_thumb1_PitchInterpolator")
OrientationInterpolator2529.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2529.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2500.addChildren(OrientationInterpolator2529)
ROUTE2530 = ROUTE()
ROUTE2530.setFromField("fraction_changed")
ROUTE2530.setFromNode("RollTimer")
ROUTE2530.setToField("set_fraction")
ROUTE2530.setToNode("Rolls_r_ankle_RotationInterpolator")

Group2500.addChildren(ROUTE2530)
ROUTE2531 = ROUTE()
ROUTE2531.setFromField("fraction_changed")
ROUTE2531.setFromNode("RollTimer")
ROUTE2531.setToField("set_fraction")
ROUTE2531.setToNode("Rolls_r_knee_RotationInterpolator")

Group2500.addChildren(ROUTE2531)
ROUTE2532 = ROUTE()
ROUTE2532.setFromField("fraction_changed")
ROUTE2532.setFromNode("RollTimer")
ROUTE2532.setToField("set_fraction")
ROUTE2532.setToNode("Rolls_r_hip_RotationInterpolator")

Group2500.addChildren(ROUTE2532)
ROUTE2533 = ROUTE()
ROUTE2533.setFromField("fraction_changed")
ROUTE2533.setFromNode("RollTimer")
ROUTE2533.setToField("set_fraction")
ROUTE2533.setToNode("Rolls_l_ankle_RotationInterpolator")

Group2500.addChildren(ROUTE2533)
ROUTE2534 = ROUTE()
ROUTE2534.setFromField("fraction_changed")
ROUTE2534.setFromNode("RollTimer")
ROUTE2534.setToField("set_fraction")
ROUTE2534.setToNode("Rolls_l_knee_RotationInterpolator")

Group2500.addChildren(ROUTE2534)
ROUTE2535 = ROUTE()
ROUTE2535.setFromField("fraction_changed")
ROUTE2535.setFromNode("RollTimer")
ROUTE2535.setToField("set_fraction")
ROUTE2535.setToNode("Rolls_l_hip_RotationInterpolator")

Group2500.addChildren(ROUTE2535)
ROUTE2536 = ROUTE()
ROUTE2536.setFromField("fraction_changed")
ROUTE2536.setFromNode("RollTimer")
ROUTE2536.setToField("set_fraction")
ROUTE2536.setToNode("Rolls_lower_body_RotationInterpolator")

Group2500.addChildren(ROUTE2536)
ROUTE2537 = ROUTE()
ROUTE2537.setFromField("fraction_changed")
ROUTE2537.setFromNode("RollTimer")
ROUTE2537.setToField("set_fraction")
ROUTE2537.setToNode("Rolls_r_wrist_RotationInterpolator")

Group2500.addChildren(ROUTE2537)
ROUTE2538 = ROUTE()
ROUTE2538.setFromField("fraction_changed")
ROUTE2538.setFromNode("RollTimer")
ROUTE2538.setToField("set_fraction")
ROUTE2538.setToNode("Rolls_r_elbow_RotationInterpolator")

Group2500.addChildren(ROUTE2538)
ROUTE2539 = ROUTE()
ROUTE2539.setFromField("fraction_changed")
ROUTE2539.setFromNode("RollTimer")
ROUTE2539.setToField("set_fraction")
ROUTE2539.setToNode("Rolls_r_shoulder_RotationInterpolator")

Group2500.addChildren(ROUTE2539)
ROUTE2540 = ROUTE()
ROUTE2540.setFromField("fraction_changed")
ROUTE2540.setFromNode("RollTimer")
ROUTE2540.setToField("set_fraction")
ROUTE2540.setToNode("Rolls_l_wrist_RotationInterpolator")

Group2500.addChildren(ROUTE2540)
ROUTE2541 = ROUTE()
ROUTE2541.setFromField("fraction_changed")
ROUTE2541.setFromNode("RollTimer")
ROUTE2541.setToField("set_fraction")
ROUTE2541.setToNode("Rolls_l_elbow_RotationInterpolator")

Group2500.addChildren(ROUTE2541)
ROUTE2542 = ROUTE()
ROUTE2542.setFromField("fraction_changed")
ROUTE2542.setFromNode("RollTimer")
ROUTE2542.setToField("set_fraction")
ROUTE2542.setToNode("Rolls_l_shoulder_RotationInterpolator")

Group2500.addChildren(ROUTE2542)
ROUTE2543 = ROUTE()
ROUTE2543.setFromField("fraction_changed")
ROUTE2543.setFromNode("RollTimer")
ROUTE2543.setToField("set_fraction")
ROUTE2543.setToNode("Rolls_head_RotationInterpolator")

Group2500.addChildren(ROUTE2543)
ROUTE2544 = ROUTE()
ROUTE2544.setFromField("fraction_changed")
ROUTE2544.setFromNode("RollTimer")
ROUTE2544.setToField("set_fraction")
ROUTE2544.setToNode("Rolls_neck_RotationInterpolator")

Group2500.addChildren(ROUTE2544)
ROUTE2545 = ROUTE()
ROUTE2545.setFromField("fraction_changed")
ROUTE2545.setFromNode("RollTimer")
ROUTE2545.setToField("set_fraction")
ROUTE2545.setToNode("Rolls_upper_body_RotationInterpolator")

Group2500.addChildren(ROUTE2545)
ROUTE2546 = ROUTE()
ROUTE2546.setFromField("fraction_changed")
ROUTE2546.setFromNode("RollTimer")
ROUTE2546.setToField("set_fraction")
ROUTE2546.setToNode("Rolls_whole_body_RotationInterpolator")

Group2500.addChildren(ROUTE2546)
ROUTE2547 = ROUTE()
ROUTE2547.setFromField("fraction_changed")
ROUTE2547.setFromNode("RollTimer")
ROUTE2547.setToField("set_fraction")
ROUTE2547.setToNode("Rolls_whole_body_TranslationInterpolator")

Group2500.addChildren(ROUTE2547)
ROUTE2548 = ROUTE()
ROUTE2548.setFromField("fraction_changed")
ROUTE2548.setFromNode("RollTimer")
ROUTE2548.setToField("set_fraction")
ROUTE2548.setToNode("Roll_l_sternoclavicular_RollInterpolator")

Group2500.addChildren(ROUTE2548)
ROUTE2549 = ROUTE()
ROUTE2549.setFromField("fraction_changed")
ROUTE2549.setFromNode("RollTimer")
ROUTE2549.setToField("set_fraction")
ROUTE2549.setToNode("Roll_l_acromioclavicular_RollInterpolator")

Group2500.addChildren(ROUTE2549)
ROUTE2550 = ROUTE()
ROUTE2550.setFromField("fraction_changed")
ROUTE2550.setFromNode("RollTimer")
ROUTE2550.setToField("set_fraction")
ROUTE2550.setToNode("Roll_r_sternoclavicular_RollInterpolator")

Group2500.addChildren(ROUTE2550)
ROUTE2551 = ROUTE()
ROUTE2551.setFromField("fraction_changed")
ROUTE2551.setFromNode("RollTimer")
ROUTE2551.setToField("set_fraction")
ROUTE2551.setToNode("Roll_r_acromioclavicular_RollInterpolator")

Group2500.addChildren(ROUTE2551)
ROUTE2552 = ROUTE()
ROUTE2552.setFromField("fraction_changed")
ROUTE2552.setFromNode("RollTimer")
ROUTE2552.setToField("set_fraction")
ROUTE2552.setToNode("Roll_r_metatarsal_PitchInterpolator")

Group2500.addChildren(ROUTE2552)
ROUTE2553 = ROUTE()
ROUTE2553.setFromField("fraction_changed")
ROUTE2553.setFromNode("RollTimer")
ROUTE2553.setToField("set_fraction")
ROUTE2553.setToNode("Roll_sacroiliac_YawInterpolator")

Group2500.addChildren(ROUTE2553)
ROUTE2554 = ROUTE()
ROUTE2554.setFromField("fraction_changed")
ROUTE2554.setFromNode("RollTimer")
ROUTE2554.setToField("set_fraction")
ROUTE2554.setToNode("Roll_vl5_YawInterpolator")

Group2500.addChildren(ROUTE2554)
ROUTE2555 = ROUTE()
ROUTE2555.setFromField("fraction_changed")
ROUTE2555.setFromNode("RollTimer")
ROUTE2555.setToField("set_fraction")
ROUTE2555.setToNode("Roll_vc6_YawInterpolator")

Group2500.addChildren(ROUTE2555)
ROUTE2556 = ROUTE()
ROUTE2556.setFromField("fraction_changed")
ROUTE2556.setFromNode("RollTimer")
ROUTE2556.setToField("set_fraction")
ROUTE2556.setToNode("Roll_l_thumb1_PitchInterpolator")

Group2500.addChildren(ROUTE2556)
ROUTE2557 = ROUTE()
ROUTE2557.setFromField("fraction_changed")
ROUTE2557.setFromNode("RollTimer")
ROUTE2557.setToField("set_fraction")
ROUTE2557.setToNode("Roll_r_thumb1_PitchInterpolator")

Group2500.addChildren(ROUTE2557)
ROUTE2558 = ROUTE()
ROUTE2558.setFromField("value_changed")
ROUTE2558.setFromNode("Rolls_r_ankle_RotationInterpolator")
ROUTE2558.setToField("rotation")
ROUTE2558.setToNode("hanim_r_ankle")

Group2500.addChildren(ROUTE2558)
ROUTE2559 = ROUTE()
ROUTE2559.setFromField("value_changed")
ROUTE2559.setFromNode("Rolls_r_knee_RotationInterpolator")
ROUTE2559.setToField("rotation")
ROUTE2559.setToNode("hanim_r_knee")

Group2500.addChildren(ROUTE2559)
ROUTE2560 = ROUTE()
ROUTE2560.setFromField("value_changed")
ROUTE2560.setFromNode("Rolls_r_hip_RotationInterpolator")
ROUTE2560.setToField("rotation")
ROUTE2560.setToNode("hanim_r_hip")

Group2500.addChildren(ROUTE2560)
ROUTE2561 = ROUTE()
ROUTE2561.setFromField("value_changed")
ROUTE2561.setFromNode("Rolls_l_ankle_RotationInterpolator")
ROUTE2561.setToField("rotation")
ROUTE2561.setToNode("hanim_l_ankle")

Group2500.addChildren(ROUTE2561)
ROUTE2562 = ROUTE()
ROUTE2562.setFromField("value_changed")
ROUTE2562.setFromNode("Rolls_l_knee_RotationInterpolator")
ROUTE2562.setToField("rotation")
ROUTE2562.setToNode("hanim_l_knee")

Group2500.addChildren(ROUTE2562)
ROUTE2563 = ROUTE()
ROUTE2563.setFromField("value_changed")
ROUTE2563.setFromNode("Rolls_l_hip_RotationInterpolator")
ROUTE2563.setToField("rotation")
ROUTE2563.setToNode("hanim_l_hip")

Group2500.addChildren(ROUTE2563)
ROUTE2564 = ROUTE()
ROUTE2564.setFromField("value_changed")
ROUTE2564.setFromNode("Rolls_lower_body_RotationInterpolator")
ROUTE2564.setToField("rotation")
ROUTE2564.setToNode("hanim_sacroiliac")

Group2500.addChildren(ROUTE2564)
ROUTE2565 = ROUTE()
ROUTE2565.setFromField("value_changed")
ROUTE2565.setFromNode("Rolls_r_wrist_RotationInterpolator")
ROUTE2565.setToField("rotation")
ROUTE2565.setToNode("hanim_r_wrist")

Group2500.addChildren(ROUTE2565)
ROUTE2566 = ROUTE()
ROUTE2566.setFromField("value_changed")
ROUTE2566.setFromNode("Rolls_r_elbow_RotationInterpolator")
ROUTE2566.setToField("rotation")
ROUTE2566.setToNode("hanim_r_elbow")

Group2500.addChildren(ROUTE2566)
ROUTE2567 = ROUTE()
ROUTE2567.setFromField("value_changed")
ROUTE2567.setFromNode("Rolls_r_shoulder_RotationInterpolator")
ROUTE2567.setToField("rotation")
ROUTE2567.setToNode("hanim_r_shoulder")

Group2500.addChildren(ROUTE2567)
ROUTE2568 = ROUTE()
ROUTE2568.setFromField("value_changed")
ROUTE2568.setFromNode("Rolls_l_wrist_RotationInterpolator")
ROUTE2568.setToField("rotation")
ROUTE2568.setToNode("hanim_l_wrist")

Group2500.addChildren(ROUTE2568)
ROUTE2569 = ROUTE()
ROUTE2569.setFromField("value_changed")
ROUTE2569.setFromNode("Rolls_l_elbow_RotationInterpolator")
ROUTE2569.setToField("rotation")
ROUTE2569.setToNode("hanim_l_elbow")

Group2500.addChildren(ROUTE2569)
ROUTE2570 = ROUTE()
ROUTE2570.setFromField("value_changed")
ROUTE2570.setFromNode("Rolls_l_shoulder_RotationInterpolator")
ROUTE2570.setToField("rotation")
ROUTE2570.setToNode("hanim_l_shoulder")

Group2500.addChildren(ROUTE2570)
ROUTE2571 = ROUTE()
ROUTE2571.setFromField("value_changed")
ROUTE2571.setFromNode("Rolls_head_RotationInterpolator")
ROUTE2571.setToField("rotation")
ROUTE2571.setToNode("hanim_skullbase")

Group2500.addChildren(ROUTE2571)
ROUTE2572 = ROUTE()
ROUTE2572.setFromField("value_changed")
ROUTE2572.setFromNode("Rolls_neck_RotationInterpolator")
ROUTE2572.setToField("rotation")
ROUTE2572.setToNode("hanim_vc4")

Group2500.addChildren(ROUTE2572)
ROUTE2573 = ROUTE()
ROUTE2573.setFromField("value_changed")
ROUTE2573.setFromNode("Rolls_upper_body_RotationInterpolator")
ROUTE2573.setToField("rotation")
ROUTE2573.setToNode("hanim_vl1")

Group2500.addChildren(ROUTE2573)
ROUTE2574 = ROUTE()
ROUTE2574.setFromField("value_changed")
ROUTE2574.setFromNode("Rolls_whole_body_RotationInterpolator")
ROUTE2574.setToField("rotation")
ROUTE2574.setToNode("hanim_humanoid_root")

Group2500.addChildren(ROUTE2574)
ROUTE2575 = ROUTE()
ROUTE2575.setFromField("value_changed")
ROUTE2575.setFromNode("Rolls_whole_body_TranslationInterpolator")
ROUTE2575.setToField("translation")
ROUTE2575.setToNode("hanim_humanoid_root")

Group2500.addChildren(ROUTE2575)
ROUTE2576 = ROUTE()
ROUTE2576.setFromField("value_changed")
ROUTE2576.setFromNode("Roll_l_sternoclavicular_RollInterpolator")
ROUTE2576.setToField("rotation")
ROUTE2576.setToNode("hanim_l_sternoclavicular")

Group2500.addChildren(ROUTE2576)
ROUTE2577 = ROUTE()
ROUTE2577.setFromField("value_changed")
ROUTE2577.setFromNode("Roll_l_acromioclavicular_RollInterpolator")
ROUTE2577.setToField("rotation")
ROUTE2577.setToNode("hanim_l_acromioclavicular")

Group2500.addChildren(ROUTE2577)
ROUTE2578 = ROUTE()
ROUTE2578.setFromField("value_changed")
ROUTE2578.setFromNode("Roll_r_sternoclavicular_RollInterpolator")
ROUTE2578.setToField("rotation")
ROUTE2578.setToNode("hanim_r_sternoclavicular")

Group2500.addChildren(ROUTE2578)
ROUTE2579 = ROUTE()
ROUTE2579.setFromField("value_changed")
ROUTE2579.setFromNode("Roll_r_acromioclavicular_RollInterpolator")
ROUTE2579.setToField("rotation")
ROUTE2579.setToNode("hanim_r_acromioclavicular")

Group2500.addChildren(ROUTE2579)
ROUTE2580 = ROUTE()
ROUTE2580.setFromField("value_changed")
ROUTE2580.setFromNode("Roll_r_metatarsal_PitchInterpolator")
ROUTE2580.setToField("rotation")
ROUTE2580.setToNode("hanim_l_metatarsal")

Group2500.addChildren(ROUTE2580)
ROUTE2581 = ROUTE()
ROUTE2581.setFromField("value_changed")
ROUTE2581.setFromNode("Roll_r_metatarsal_PitchInterpolator")
ROUTE2581.setToField("rotation")
ROUTE2581.setToNode("hanim_r_metatarsal")

Group2500.addChildren(ROUTE2581)
ROUTE2582 = ROUTE()
ROUTE2582.setFromField("value_changed")
ROUTE2582.setFromNode("Roll_sacroiliac_YawInterpolator")
ROUTE2582.setToField("rotation")
ROUTE2582.setToNode("hanim_sacroiliac")

Group2500.addChildren(ROUTE2582)
ROUTE2583 = ROUTE()
ROUTE2583.setFromField("value_changed")
ROUTE2583.setFromNode("Roll_vl5_YawInterpolator")
ROUTE2583.setToField("rotation")
ROUTE2583.setToNode("hanim_vl5")

Group2500.addChildren(ROUTE2583)
ROUTE2584 = ROUTE()
ROUTE2584.setFromField("value_changed")
ROUTE2584.setFromNode("Roll_vc6_YawInterpolator")
ROUTE2584.setToField("rotation")
ROUTE2584.setToNode("hanim_vc6")

Group2500.addChildren(ROUTE2584)
ROUTE2585 = ROUTE()
ROUTE2585.setFromField("value_changed")
ROUTE2585.setFromNode("Roll_l_thumb1_PitchInterpolator")
ROUTE2585.setToField("rotation")
ROUTE2585.setToNode("hanim_l_thumb1")

Group2500.addChildren(ROUTE2585)
ROUTE2586 = ROUTE()
ROUTE2586.setFromField("value_changed")
ROUTE2586.setFromNode("Roll_r_thumb1_PitchInterpolator")
ROUTE2586.setToField("rotation")
ROUTE2586.setToNode("hanim_r_thumb1")

Group2500.addChildren(ROUTE2586)

Scene31.addChildren(Group2500)
Group2587 = Group()
Group2587.setDEF("WalkAnimation")
TimeSensor2588 = TimeSensor()
TimeSensor2588.setDEF("WalkTimer")
TimeSensor2588.setCycleInterval(1.73)
TimeSensor2588.setLoop(True)

Group2587.addChildren(TimeSensor2588)
OrientationInterpolator2589 = OrientationInterpolator()
OrientationInterpolator2589.setDEF("Walk_r_metatarsal_PitchInterpolator")
OrientationInterpolator2589.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2589.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2589)
OrientationInterpolator2590 = OrientationInterpolator()
OrientationInterpolator2590.setDEF("Walk_r_ankle_RotationInterpolator")
OrientationInterpolator2590.setKey([0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1])
OrientationInterpolator2590.setKeyValue([0,0,1,0,-1,0,0,0.3533,-1,0,0,0.1072,1,0,0,0.2612,1,0,0,0.1268,-1,0,0,0.01793,-1,0,0,0.05824,-1,0,0,0.2398,-1,0,0,0.35,-1,0,0,0.3322,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2590)
OrientationInterpolator2591 = OrientationInterpolator()
OrientationInterpolator2591.setDEF("Walk_r_knee_RotationInterpolator")
OrientationInterpolator2591.setKey([0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1])
OrientationInterpolator2591.setKeyValue([1,0,0,0.8573,1,0,0,0.8926,1,0,0,0.5351,1,0,0,0.1756,1,0,0,0.1194,1,0,0,0.3153,1,0,0,0.09354,1,0,0,0.08558,1,0,0,0.2475,1,0,0,0.8573])

Group2587.addChildren(OrientationInterpolator2591)
OrientationInterpolator2592 = OrientationInterpolator()
OrientationInterpolator2592.setDEF("Walk_r_hip_RotationInterpolator")
OrientationInterpolator2592.setKey([0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1])
OrientationInterpolator2592.setKeyValue([-0.5831,0.03511,0.8116,0.1481,-0.995,0.02296,0.09674,0.4683,-1,0.00192,0.007964,0.4732,-0.998,-0.0158,-0.06102,0.5079,-0.9911,-0.03541,-0.1286,0.5419,-0.9131,-0.06243,-0.403,0.3361,-0.4306,-0.07962,-0.899,0.07038,1,0,0,0.2571,0.9891,-0.02805,0.1444,0.3879,-0.5831,0.03511,0.8116,0.1481])

Group2587.addChildren(OrientationInterpolator2592)
OrientationInterpolator2593 = OrientationInterpolator()
OrientationInterpolator2593.setDEF("Walk_l_ankle_RotationInterpolator")
OrientationInterpolator2593.setKey([0,0.125,0.2083,0.375,0.6667,0.9167,1])
OrientationInterpolator2593.setKeyValue([-1,0,0,0.06714,-1,0,0,0.2152,-1,0,0,0.3184,-1,0,0,0.4717,-1,0,0,0.2912,1,0,0,0.1222,-1,0,0,0.06714])

Group2587.addChildren(OrientationInterpolator2593)
OrientationInterpolator2594 = OrientationInterpolator()
OrientationInterpolator2594.setDEF("Walk_l_knee_RotationInterpolator")
OrientationInterpolator2594.setKey([0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1])
OrientationInterpolator2594.setKeyValue([1,0,0,0.3226,1,0,0,0.1556,1,0,0,0.08678,1,0,0,0.8751,1,0,0,1.131,1,0,0,0.09961,1,0,0,0.3942,1,0,0,0.3226])

Group2587.addChildren(OrientationInterpolator2594)
OrientationInterpolator2595 = OrientationInterpolator()
OrientationInterpolator2595.setDEF("Walk_l_hip_RotationInterpolator")
OrientationInterpolator2595.setKey([0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1])
OrientationInterpolator2595.setKeyValue([-0.873,0.06094,0.484,0.2865,0.9963,-0.01057,0.08481,0.2488,0.9965,0.01591,-0.08222,0.3836,-0.7018,-0.03223,-0.7117,0.1289,-1,0,0,0.5518,-0.9964,0.02231,0.0817,0.5351,-0.9809,0.04912,0.1881,0.5204,-0.873,0.06094,0.484,0.2865])

Group2587.addChildren(OrientationInterpolator2595)
OrientationInterpolator2596 = OrientationInterpolator()
OrientationInterpolator2596.setDEF("Walk_lower_body_RotationInterpolator")
OrientationInterpolator2596.setKey([0,0.5,1])
OrientationInterpolator2596.setKeyValue([0,0,-1,0.1056,0,0,1,0.09018,0,0,-1,0.1056])

Group2587.addChildren(OrientationInterpolator2596)
OrientationInterpolator2597 = OrientationInterpolator()
OrientationInterpolator2597.setDEF("Walk_r_wrist_RotationInterpolator")
OrientationInterpolator2597.setKey([0,0.375,0.9167,1])
OrientationInterpolator2597.setKeyValue([-0.8129,0.4759,-0.3357,0.1346,0.1533,-0.9878,0.02582,0.3902,-0.5701,0.7604,-0.311,0.366,-0.8129,0.4759,-0.3357,0.1346])

Group2587.addChildren(OrientationInterpolator2597)
OrientationInterpolator2598 = OrientationInterpolator()
OrientationInterpolator2598.setDEF("Walk_r_elbow_RotationInterpolator")
OrientationInterpolator2598.setKey([0,0.375,0.9167,1])
OrientationInterpolator2598.setKeyValue([-1,0,0,0.411508,-1,0,0,0.0925011,-1,0,0,0.572568,-1,0,0,0.411508])

Group2587.addChildren(OrientationInterpolator2598)
OrientationInterpolator2599 = OrientationInterpolator()
OrientationInterpolator2599.setDEF("Walk_r_shoulder_RotationInterpolator")
OrientationInterpolator2599.setKey([0,0.375,0.9167,1])
OrientationInterpolator2599.setKeyValue([-1,0,0,0.09346,1,0,0,0.3197,-1,0,0,0.1564,-1,0,0,0.09346])

Group2587.addChildren(OrientationInterpolator2599)
OrientationInterpolator2600 = OrientationInterpolator()
OrientationInterpolator2600.setDEF("Walk_l_wrist_RotationInterpolator")
OrientationInterpolator2600.setKey([0,0.375,0.9167,1])
OrientationInterpolator2600.setKeyValue([0,-1,0,0.461076,-0.330195,-0.927451,0.175516,0.538852,0.0327774,-0.999314,-0.0172185,0.492033,0,-1,0,0.461076])

Group2587.addChildren(OrientationInterpolator2600)
OrientationInterpolator2601 = OrientationInterpolator()
OrientationInterpolator2601.setDEF("Walk_l_elbow_RotationInterpolator")
OrientationInterpolator2601.setKey([0,0.375,0.9167,1])
OrientationInterpolator2601.setKeyValue([-1,0,0,0.0659878,-1,0,0,0.488383,-1,0,0,0.0177536,-1,0,0,0.0659878])

Group2587.addChildren(OrientationInterpolator2601)
OrientationInterpolator2602 = OrientationInterpolator()
OrientationInterpolator2602.setDEF("Walk_l_shoulder_RotationInterpolator")
OrientationInterpolator2602.setKey([0,0.375,0.9167,1])
OrientationInterpolator2602.setKeyValue([1,0,0,0.1189,-1,0,0,0.1861,1,0,0,0.3357,1,0,0,0.1189])

Group2587.addChildren(OrientationInterpolator2602)
OrientationInterpolator2603 = OrientationInterpolator()
OrientationInterpolator2603.setDEF("Walk_head_RotationInterpolator")
OrientationInterpolator2603.setKey([0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1])
OrientationInterpolator2603.setKeyValue([0,-1,0,0.08642,0,1,0,0.1825,0,1,0,0.1505,0,1,0,0.1053,0,1,0,0.04391,0,-1,0,0.03119,0,-1,0,0.07936,0,-1,0,0.1616,0,-1,0,0.155,0,-1,0,0.08642])

Group2587.addChildren(OrientationInterpolator2603)
OrientationInterpolator2604 = OrientationInterpolator()
OrientationInterpolator2604.setDEF("Walk_neck_RotationInterpolator")
OrientationInterpolator2604.setKey([0,1])
OrientationInterpolator2604.setKeyValue([0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2604)
OrientationInterpolator2605 = OrientationInterpolator()
OrientationInterpolator2605.setDEF("Walk_upper_body_RotationInterpolator")
OrientationInterpolator2605.setKey([0,0.2083,0.375,0.75,0.8333,1])
OrientationInterpolator2605.setKeyValue([0,1,0,0.0826,-0.01972,-0.5974,0.8017,0.08231,0.009296,-0.9648,0.2627,0.1734,-0.01238,0.9549,-0.2968,0.08732,-0.008125,0.9691,-0.2463,0.158,0,1,0,0.0826])

Group2587.addChildren(OrientationInterpolator2605)
OrientationInterpolator2606 = OrientationInterpolator()
OrientationInterpolator2606.setDEF("Walk_whole_body_RotationInterpolator")
OrientationInterpolator2606.setKey([0,1])
OrientationInterpolator2606.setKeyValue([0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2606)
PositionInterpolator2607 = PositionInterpolator()
PositionInterpolator2607.setDEF("Walk_whole_body_TranslationInterpolator")
PositionInterpolator2607.setKey([0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1])
PositionInterpolator2607.setKeyValue([0,-0.00928,0,0,-0.003858,0,0,-0.008847,0,0,-0.01486,0,0,-0.02641,0,0,-0.03934,0,0,-0.0502,0,0,-0.07469,0,0,-0.02732,0,0,-0.01608,0,0,-0.01129,0,0,-0.005819,0,0,-0.002004,0,0,-0.002579,0,0,-0.0143,0,0,-0.03799,0,0,-0.05648,0,0,-0.045,0,0,-0.00928,0])

Group2587.addChildren(PositionInterpolator2607)
OrientationInterpolator2608 = OrientationInterpolator()
OrientationInterpolator2608.setDEF("Walk_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2608.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2608.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2608)
OrientationInterpolator2609 = OrientationInterpolator()
OrientationInterpolator2609.setDEF("Walk_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2609.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2609.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2609)
OrientationInterpolator2610 = OrientationInterpolator()
OrientationInterpolator2610.setDEF("Walk_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2610.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2610.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2610)
OrientationInterpolator2611 = OrientationInterpolator()
OrientationInterpolator2611.setDEF("Walk_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2611.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2611.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2611)
OrientationInterpolator2612 = OrientationInterpolator()
OrientationInterpolator2612.setDEF("Walk_sacroiliac_YawInterpolator")
OrientationInterpolator2612.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2612.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2612)
OrientationInterpolator2613 = OrientationInterpolator()
OrientationInterpolator2613.setDEF("Walk_vl5_YawInterpolator")
OrientationInterpolator2613.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2613.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2613)
OrientationInterpolator2614 = OrientationInterpolator()
OrientationInterpolator2614.setDEF("Walk_vc6_YawInterpolator")
OrientationInterpolator2614.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2614.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2587.addChildren(OrientationInterpolator2614)
OrientationInterpolator2615 = OrientationInterpolator()
OrientationInterpolator2615.setDEF("Walk_l_thumb1_PitchInterpolator")
OrientationInterpolator2615.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2615.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.5,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2587.addChildren(OrientationInterpolator2615)
OrientationInterpolator2616 = OrientationInterpolator()
OrientationInterpolator2616.setDEF("Walk_r_thumb1_PitchInterpolator")
OrientationInterpolator2616.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2616.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.5,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2587.addChildren(OrientationInterpolator2616)
ROUTE2617 = ROUTE()
ROUTE2617.setFromField("fraction_changed")
ROUTE2617.setFromNode("WalkTimer")
ROUTE2617.setToField("set_fraction")
ROUTE2617.setToNode("Walk_r_ankle_RotationInterpolator")

Group2587.addChildren(ROUTE2617)
ROUTE2618 = ROUTE()
ROUTE2618.setFromField("fraction_changed")
ROUTE2618.setFromNode("WalkTimer")
ROUTE2618.setToField("set_fraction")
ROUTE2618.setToNode("Walk_r_knee_RotationInterpolator")

Group2587.addChildren(ROUTE2618)
ROUTE2619 = ROUTE()
ROUTE2619.setFromField("fraction_changed")
ROUTE2619.setFromNode("WalkTimer")
ROUTE2619.setToField("set_fraction")
ROUTE2619.setToNode("Walk_r_hip_RotationInterpolator")

Group2587.addChildren(ROUTE2619)
ROUTE2620 = ROUTE()
ROUTE2620.setFromField("fraction_changed")
ROUTE2620.setFromNode("WalkTimer")
ROUTE2620.setToField("set_fraction")
ROUTE2620.setToNode("Walk_l_ankle_RotationInterpolator")

Group2587.addChildren(ROUTE2620)
ROUTE2621 = ROUTE()
ROUTE2621.setFromField("fraction_changed")
ROUTE2621.setFromNode("WalkTimer")
ROUTE2621.setToField("set_fraction")
ROUTE2621.setToNode("Walk_l_knee_RotationInterpolator")

Group2587.addChildren(ROUTE2621)
ROUTE2622 = ROUTE()
ROUTE2622.setFromField("fraction_changed")
ROUTE2622.setFromNode("WalkTimer")
ROUTE2622.setToField("set_fraction")
ROUTE2622.setToNode("Walk_l_hip_RotationInterpolator")

Group2587.addChildren(ROUTE2622)
ROUTE2623 = ROUTE()
ROUTE2623.setFromField("fraction_changed")
ROUTE2623.setFromNode("WalkTimer")
ROUTE2623.setToField("set_fraction")
ROUTE2623.setToNode("Walk_lower_body_RotationInterpolator")

Group2587.addChildren(ROUTE2623)
ROUTE2624 = ROUTE()
ROUTE2624.setFromField("fraction_changed")
ROUTE2624.setFromNode("WalkTimer")
ROUTE2624.setToField("set_fraction")
ROUTE2624.setToNode("Walk_r_wrist_RotationInterpolator")

Group2587.addChildren(ROUTE2624)
ROUTE2625 = ROUTE()
ROUTE2625.setFromField("fraction_changed")
ROUTE2625.setFromNode("WalkTimer")
ROUTE2625.setToField("set_fraction")
ROUTE2625.setToNode("Walk_r_elbow_RotationInterpolator")

Group2587.addChildren(ROUTE2625)
ROUTE2626 = ROUTE()
ROUTE2626.setFromField("fraction_changed")
ROUTE2626.setFromNode("WalkTimer")
ROUTE2626.setToField("set_fraction")
ROUTE2626.setToNode("Walk_r_shoulder_RotationInterpolator")

Group2587.addChildren(ROUTE2626)
ROUTE2627 = ROUTE()
ROUTE2627.setFromField("fraction_changed")
ROUTE2627.setFromNode("WalkTimer")
ROUTE2627.setToField("set_fraction")
ROUTE2627.setToNode("Walk_l_wrist_RotationInterpolator")

Group2587.addChildren(ROUTE2627)
ROUTE2628 = ROUTE()
ROUTE2628.setFromField("fraction_changed")
ROUTE2628.setFromNode("WalkTimer")
ROUTE2628.setToField("set_fraction")
ROUTE2628.setToNode("Walk_l_elbow_RotationInterpolator")

Group2587.addChildren(ROUTE2628)
ROUTE2629 = ROUTE()
ROUTE2629.setFromField("fraction_changed")
ROUTE2629.setFromNode("WalkTimer")
ROUTE2629.setToField("set_fraction")
ROUTE2629.setToNode("Walk_l_shoulder_RotationInterpolator")

Group2587.addChildren(ROUTE2629)
ROUTE2630 = ROUTE()
ROUTE2630.setFromField("fraction_changed")
ROUTE2630.setFromNode("WalkTimer")
ROUTE2630.setToField("set_fraction")
ROUTE2630.setToNode("Walk_head_RotationInterpolator")

Group2587.addChildren(ROUTE2630)
ROUTE2631 = ROUTE()
ROUTE2631.setFromField("fraction_changed")
ROUTE2631.setFromNode("WalkTimer")
ROUTE2631.setToField("set_fraction")
ROUTE2631.setToNode("Walk_neck_RotationInterpolator")

Group2587.addChildren(ROUTE2631)
ROUTE2632 = ROUTE()
ROUTE2632.setFromField("fraction_changed")
ROUTE2632.setFromNode("WalkTimer")
ROUTE2632.setToField("set_fraction")
ROUTE2632.setToNode("Walk_upper_body_RotationInterpolator")

Group2587.addChildren(ROUTE2632)
ROUTE2633 = ROUTE()
ROUTE2633.setFromField("fraction_changed")
ROUTE2633.setFromNode("WalkTimer")
ROUTE2633.setToField("set_fraction")
ROUTE2633.setToNode("Walk_whole_body_RotationInterpolator")

Group2587.addChildren(ROUTE2633)
ROUTE2634 = ROUTE()
ROUTE2634.setFromField("fraction_changed")
ROUTE2634.setFromNode("WalkTimer")
ROUTE2634.setToField("set_fraction")
ROUTE2634.setToNode("Walk_whole_body_TranslationInterpolator")

Group2587.addChildren(ROUTE2634)
ROUTE2635 = ROUTE()
ROUTE2635.setFromField("fraction_changed")
ROUTE2635.setFromNode("WalkTimer")
ROUTE2635.setToField("set_fraction")
ROUTE2635.setToNode("Walk_l_sternoclavicular_RollInterpolator")

Group2587.addChildren(ROUTE2635)
ROUTE2636 = ROUTE()
ROUTE2636.setFromField("fraction_changed")
ROUTE2636.setFromNode("WalkTimer")
ROUTE2636.setToField("set_fraction")
ROUTE2636.setToNode("Walk_l_acromioclavicular_RollInterpolator")

Group2587.addChildren(ROUTE2636)
ROUTE2637 = ROUTE()
ROUTE2637.setFromField("fraction_changed")
ROUTE2637.setFromNode("WalkTimer")
ROUTE2637.setToField("set_fraction")
ROUTE2637.setToNode("Walk_r_sternoclavicular_RollInterpolator")

Group2587.addChildren(ROUTE2637)
ROUTE2638 = ROUTE()
ROUTE2638.setFromField("fraction_changed")
ROUTE2638.setFromNode("WalkTimer")
ROUTE2638.setToField("set_fraction")
ROUTE2638.setToNode("Walk_r_acromioclavicular_RollInterpolator")

Group2587.addChildren(ROUTE2638)
ROUTE2639 = ROUTE()
ROUTE2639.setFromField("fraction_changed")
ROUTE2639.setFromNode("WalkTimer")
ROUTE2639.setToField("set_fraction")
ROUTE2639.setToNode("Walk_r_metatarsal_PitchInterpolator")

Group2587.addChildren(ROUTE2639)
ROUTE2640 = ROUTE()
ROUTE2640.setFromField("fraction_changed")
ROUTE2640.setFromNode("WalkTimer")
ROUTE2640.setToField("set_fraction")
ROUTE2640.setToNode("Walk_sacroiliac_YawInterpolator")

Group2587.addChildren(ROUTE2640)
ROUTE2641 = ROUTE()
ROUTE2641.setFromField("fraction_changed")
ROUTE2641.setFromNode("WalkTimer")
ROUTE2641.setToField("set_fraction")
ROUTE2641.setToNode("Walk_vl5_YawInterpolator")

Group2587.addChildren(ROUTE2641)
ROUTE2642 = ROUTE()
ROUTE2642.setFromField("fraction_changed")
ROUTE2642.setFromNode("WalkTimer")
ROUTE2642.setToField("set_fraction")
ROUTE2642.setToNode("Walk_vc6_YawInterpolator")

Group2587.addChildren(ROUTE2642)
ROUTE2643 = ROUTE()
ROUTE2643.setFromField("fraction_changed")
ROUTE2643.setFromNode("WalkTimer")
ROUTE2643.setToField("set_fraction")
ROUTE2643.setToNode("Walk_l_thumb1_PitchInterpolator")

Group2587.addChildren(ROUTE2643)
ROUTE2644 = ROUTE()
ROUTE2644.setFromField("fraction_changed")
ROUTE2644.setFromNode("WalkTimer")
ROUTE2644.setToField("set_fraction")
ROUTE2644.setToNode("Walk_r_thumb1_PitchInterpolator")

Group2587.addChildren(ROUTE2644)
ROUTE2645 = ROUTE()
ROUTE2645.setFromField("value_changed")
ROUTE2645.setFromNode("Walk_r_ankle_RotationInterpolator")
ROUTE2645.setToField("rotation")
ROUTE2645.setToNode("hanim_r_ankle")

Group2587.addChildren(ROUTE2645)
ROUTE2646 = ROUTE()
ROUTE2646.setFromField("value_changed")
ROUTE2646.setFromNode("Walk_r_knee_RotationInterpolator")
ROUTE2646.setToField("rotation")
ROUTE2646.setToNode("hanim_r_knee")

Group2587.addChildren(ROUTE2646)
ROUTE2647 = ROUTE()
ROUTE2647.setFromField("value_changed")
ROUTE2647.setFromNode("Walk_r_hip_RotationInterpolator")
ROUTE2647.setToField("rotation")
ROUTE2647.setToNode("hanim_r_hip")

Group2587.addChildren(ROUTE2647)
ROUTE2648 = ROUTE()
ROUTE2648.setFromField("value_changed")
ROUTE2648.setFromNode("Walk_l_ankle_RotationInterpolator")
ROUTE2648.setToField("rotation")
ROUTE2648.setToNode("hanim_l_ankle")

Group2587.addChildren(ROUTE2648)
ROUTE2649 = ROUTE()
ROUTE2649.setFromField("value_changed")
ROUTE2649.setFromNode("Walk_l_knee_RotationInterpolator")
ROUTE2649.setToField("rotation")
ROUTE2649.setToNode("hanim_l_knee")

Group2587.addChildren(ROUTE2649)
ROUTE2650 = ROUTE()
ROUTE2650.setFromField("value_changed")
ROUTE2650.setFromNode("Walk_l_hip_RotationInterpolator")
ROUTE2650.setToField("rotation")
ROUTE2650.setToNode("hanim_l_hip")

Group2587.addChildren(ROUTE2650)
ROUTE2651 = ROUTE()
ROUTE2651.setFromField("value_changed")
ROUTE2651.setFromNode("Walk_lower_body_RotationInterpolator")
ROUTE2651.setToField("rotation")
ROUTE2651.setToNode("hanim_sacroiliac")

Group2587.addChildren(ROUTE2651)
ROUTE2652 = ROUTE()
ROUTE2652.setFromField("value_changed")
ROUTE2652.setFromNode("Walk_r_wrist_RotationInterpolator")
ROUTE2652.setToField("rotation")
ROUTE2652.setToNode("hanim_r_wrist")

Group2587.addChildren(ROUTE2652)
ROUTE2653 = ROUTE()
ROUTE2653.setFromField("value_changed")
ROUTE2653.setFromNode("Walk_r_elbow_RotationInterpolator")
ROUTE2653.setToField("rotation")
ROUTE2653.setToNode("hanim_r_elbow")

Group2587.addChildren(ROUTE2653)
ROUTE2654 = ROUTE()
ROUTE2654.setFromField("value_changed")
ROUTE2654.setFromNode("Walk_r_shoulder_RotationInterpolator")
ROUTE2654.setToField("rotation")
ROUTE2654.setToNode("hanim_r_shoulder")

Group2587.addChildren(ROUTE2654)
ROUTE2655 = ROUTE()
ROUTE2655.setFromField("value_changed")
ROUTE2655.setFromNode("Walk_l_wrist_RotationInterpolator")
ROUTE2655.setToField("rotation")
ROUTE2655.setToNode("hanim_l_wrist")

Group2587.addChildren(ROUTE2655)
ROUTE2656 = ROUTE()
ROUTE2656.setFromField("value_changed")
ROUTE2656.setFromNode("Walk_l_elbow_RotationInterpolator")
ROUTE2656.setToField("rotation")
ROUTE2656.setToNode("hanim_l_elbow")

Group2587.addChildren(ROUTE2656)
ROUTE2657 = ROUTE()
ROUTE2657.setFromField("value_changed")
ROUTE2657.setFromNode("Walk_l_shoulder_RotationInterpolator")
ROUTE2657.setToField("rotation")
ROUTE2657.setToNode("hanim_l_shoulder")

Group2587.addChildren(ROUTE2657)
ROUTE2658 = ROUTE()
ROUTE2658.setFromField("value_changed")
ROUTE2658.setFromNode("Walk_head_RotationInterpolator")
ROUTE2658.setToField("rotation")
ROUTE2658.setToNode("hanim_skullbase")

Group2587.addChildren(ROUTE2658)
ROUTE2659 = ROUTE()
ROUTE2659.setFromField("value_changed")
ROUTE2659.setFromNode("Walk_neck_RotationInterpolator")
ROUTE2659.setToField("rotation")
ROUTE2659.setToNode("hanim_vc4")

Group2587.addChildren(ROUTE2659)
ROUTE2660 = ROUTE()
ROUTE2660.setFromField("value_changed")
ROUTE2660.setFromNode("Walk_upper_body_RotationInterpolator")
ROUTE2660.setToField("rotation")
ROUTE2660.setToNode("hanim_vl1")

Group2587.addChildren(ROUTE2660)
ROUTE2661 = ROUTE()
ROUTE2661.setFromField("value_changed")
ROUTE2661.setFromNode("Walk_whole_body_RotationInterpolator")
ROUTE2661.setToField("rotation")
ROUTE2661.setToNode("hanim_humanoid_root")

Group2587.addChildren(ROUTE2661)
ROUTE2662 = ROUTE()
ROUTE2662.setFromField("value_changed")
ROUTE2662.setFromNode("Walk_whole_body_TranslationInterpolator")
ROUTE2662.setToField("translation")
ROUTE2662.setToNode("hanim_humanoid_root")

Group2587.addChildren(ROUTE2662)
ROUTE2663 = ROUTE()
ROUTE2663.setFromField("value_changed")
ROUTE2663.setFromNode("Walk_l_sternoclavicular_RollInterpolator")
ROUTE2663.setToField("rotation")
ROUTE2663.setToNode("hanim_l_sternoclavicular")

Group2587.addChildren(ROUTE2663)
ROUTE2664 = ROUTE()
ROUTE2664.setFromField("value_changed")
ROUTE2664.setFromNode("Walk_l_acromioclavicular_RollInterpolator")
ROUTE2664.setToField("rotation")
ROUTE2664.setToNode("hanim_l_acromioclavicular")

Group2587.addChildren(ROUTE2664)
ROUTE2665 = ROUTE()
ROUTE2665.setFromField("value_changed")
ROUTE2665.setFromNode("Walk_r_sternoclavicular_RollInterpolator")
ROUTE2665.setToField("rotation")
ROUTE2665.setToNode("hanim_r_sternoclavicular")

Group2587.addChildren(ROUTE2665)
ROUTE2666 = ROUTE()
ROUTE2666.setFromField("value_changed")
ROUTE2666.setFromNode("Walk_r_acromioclavicular_RollInterpolator")
ROUTE2666.setToField("rotation")
ROUTE2666.setToNode("hanim_r_acromioclavicular")

Group2587.addChildren(ROUTE2666)
ROUTE2667 = ROUTE()
ROUTE2667.setFromField("value_changed")
ROUTE2667.setFromNode("Walk_r_metatarsal_PitchInterpolator")
ROUTE2667.setToField("rotation")
ROUTE2667.setToNode("hanim_l_metatarsal")

Group2587.addChildren(ROUTE2667)
ROUTE2668 = ROUTE()
ROUTE2668.setFromField("value_changed")
ROUTE2668.setFromNode("Walk_r_metatarsal_PitchInterpolator")
ROUTE2668.setToField("rotation")
ROUTE2668.setToNode("hanim_r_metatarsal")

Group2587.addChildren(ROUTE2668)
ROUTE2669 = ROUTE()
ROUTE2669.setFromField("value_changed")
ROUTE2669.setFromNode("Walk_sacroiliac_YawInterpolator")
ROUTE2669.setToField("rotation")
ROUTE2669.setToNode("hanim_sacroiliac")

Group2587.addChildren(ROUTE2669)
ROUTE2670 = ROUTE()
ROUTE2670.setFromField("value_changed")
ROUTE2670.setFromNode("Walk_vl5_YawInterpolator")
ROUTE2670.setToField("rotation")
ROUTE2670.setToNode("hanim_vl5")

Group2587.addChildren(ROUTE2670)
ROUTE2671 = ROUTE()
ROUTE2671.setFromField("value_changed")
ROUTE2671.setFromNode("Walk_vc6_YawInterpolator")
ROUTE2671.setToField("rotation")
ROUTE2671.setToNode("hanim_vc6")

Group2587.addChildren(ROUTE2671)
ROUTE2672 = ROUTE()
ROUTE2672.setFromField("value_changed")
ROUTE2672.setFromNode("Walk_l_thumb1_PitchInterpolator")
ROUTE2672.setToField("rotation")
ROUTE2672.setToNode("hanim_l_thumb1")

Group2587.addChildren(ROUTE2672)
ROUTE2673 = ROUTE()
ROUTE2673.setFromField("value_changed")
ROUTE2673.setFromNode("Walk_r_thumb1_PitchInterpolator")
ROUTE2673.setToField("rotation")
ROUTE2673.setToNode("hanim_r_thumb1")

Group2587.addChildren(ROUTE2673)

Scene31.addChildren(Group2587)
Group2674 = Group()
Group2674.setDEF("RunAnimation")
TimeSensor2675 = TimeSensor()
TimeSensor2675.setDEF("RunTimer")
TimeSensor2675.setCycleInterval(0.9)
TimeSensor2675.setLoop(True)

Group2674.addChildren(TimeSensor2675)
OrientationInterpolator2676 = OrientationInterpolator()
OrientationInterpolator2676.setDEF("Run_r_metatarsal_PitchInterpolator")
OrientationInterpolator2676.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2676.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2676)
OrientationInterpolator2677 = OrientationInterpolator()
OrientationInterpolator2677.setDEF("Run_l_hip_RotationInterpolator_Run")
OrientationInterpolator2677.setKey([0,0.2182,0.4909,0.7455,1])
OrientationInterpolator2677.setKeyValue([-0.99,0.033,0.04,1.42,-0.99,0.1328,0.067,0.42,0.99,0.014,0.009,0.9,-0.99,0.0703,0.05,0.7,-0.99,0.033,0.04,1.42])

Group2674.addChildren(OrientationInterpolator2677)
OrientationInterpolator2678 = OrientationInterpolator()
OrientationInterpolator2678.setDEF("Run_l_knee_RotationInterpolator_Run")
OrientationInterpolator2678.setKey([0,0.2182,0.4909,0.7455,1])
OrientationInterpolator2678.setKeyValue([1,0,0,1.01,1,0,0,0.426,1,0,0,0.705,1,0,0,2.179,1,0,0,1.01])

Group2674.addChildren(OrientationInterpolator2678)
OrientationInterpolator2679 = OrientationInterpolator()
OrientationInterpolator2679.setDEF("Run_l_ankle_RotationInterpolator_Run")
OrientationInterpolator2679.setKey([0,0.22,0.3,0.4,1])
OrientationInterpolator2679.setKeyValue([1,0,0,0.0374,-1,0,0,0.1037,-1,0,0,0.4328,1,0,0,0.1929,1,0,0,0.03574])

Group2674.addChildren(OrientationInterpolator2679)
OrientationInterpolator2680 = OrientationInterpolator()
OrientationInterpolator2680.setDEF("Run_r_hip_RotationInterpolator_Run")
OrientationInterpolator2680.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2680.setKeyValue([0.99,-0.014,0.009,0.9,-0.99,-0.0703,-0.05,0.7,-0.99,-0.033,0.04,1.42,-0.99,-0.1328,-0.067,0.42,0.99,-0.014,0.009,0.9])

Group2674.addChildren(OrientationInterpolator2680)
OrientationInterpolator2681 = OrientationInterpolator()
OrientationInterpolator2681.setDEF("Run_r_knee_RotationInterpolator_Run")
OrientationInterpolator2681.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2681.setKeyValue([1,0,0,0.705,1,0,0,2.179,1,0,0,1.01,1,0,0,0.426,1,0,0,0.705])

Group2674.addChildren(OrientationInterpolator2681)
OrientationInterpolator2682 = OrientationInterpolator()
OrientationInterpolator2682.setDEF("Run_r_ankle_RotationInterpolator_Run")
OrientationInterpolator2682.setKey([0,0.4,0.71,0.8,0.82,1])
OrientationInterpolator2682.setKeyValue([1,0,0,0.2323,-1,0,0,0.07843,-1,0,0,0.32,-1,0,0,0.374,-1,0,0,0.3478,1,0,0,0.2323])

Group2674.addChildren(OrientationInterpolator2682)
OrientationInterpolator2683 = OrientationInterpolator()
OrientationInterpolator2683.setDEF("Run_l_shoulder_RotationInterpolator_Run")
OrientationInterpolator2683.setKey([0,0.2182,0.4909,0.7455,1])
OrientationInterpolator2683.setKeyValue([0.99,-0.074,0.25,1.5,0.99,-0.092,0.44,0.3,-0.99,0.136,0.25,0.85,0.99,-0.081,0.38,0.4,0.99,-0.074,0.25,1.5])

Group2674.addChildren(OrientationInterpolator2683)
OrientationInterpolator2684 = OrientationInterpolator()
OrientationInterpolator2684.setDEF("Run_l_elbow_RotationInterpolator_Run")
OrientationInterpolator2684.setKey([0,0.2182,0.4909,0.7455,1])
OrientationInterpolator2684.setKeyValue([-1,0,0,1.85,-0.99,-0.19,0.18,1.35,-1,0,0,0.975,-0.99,-0.09,-0.02,1.55,-1,0,0,1.85])

Group2674.addChildren(OrientationInterpolator2684)
OrientationInterpolator2685 = OrientationInterpolator()
OrientationInterpolator2685.setDEF("Run_l_wrist_RotationInterpolator_Run")
OrientationInterpolator2685.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2685.setKeyValue([-0.25,-1,0.08,0.14,0.25,1,0.08,0.14,0,0,1,0,-0.25,1,0.08,-0.14,-0.25,1,0.08,0.14])

Group2674.addChildren(OrientationInterpolator2685)
OrientationInterpolator2686 = OrientationInterpolator()
OrientationInterpolator2686.setDEF("Run_r_shoulder_RotationInterpolator_Run")
OrientationInterpolator2686.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2686.setKeyValue([-0.99,-0.136,-0.25,0.85,0.99,0.081,-0.38,0.4,0.99,0.074,-0.25,1.5,0.99,0.081,-0.38,0.4,-0.99,-0.136,-0.25,0.85])

Group2674.addChildren(OrientationInterpolator2686)
OrientationInterpolator2687 = OrientationInterpolator()
OrientationInterpolator2687.setDEF("Run_r_elbow_RotationInterpolator_Run")
OrientationInterpolator2687.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2687.setKeyValue([-1,0,0,0.975,-0.99,0.09,0.02,1.55,-1,0,0,1.85,-0.99,0.19,-0.18,1.35,-1,0,0,0.975])

Group2674.addChildren(OrientationInterpolator2687)
OrientationInterpolator2688 = OrientationInterpolator()
OrientationInterpolator2688.setDEF("Run_r_wrist_RotationInterpolator_Run")
OrientationInterpolator2688.setKey([0,1])
OrientationInterpolator2688.setKeyValue([-0.917742,-0.237244,-0.318536,0.214273,-0.917742,-0.237244,-0.318536,0.214273])

Group2674.addChildren(OrientationInterpolator2688)
OrientationInterpolator2689 = OrientationInterpolator()
OrientationInterpolator2689.setDEF("Run_lower_body_RotationInterpolator_Run")
OrientationInterpolator2689.setKey([0,0.2182,0.4909,0.7455,1])
OrientationInterpolator2689.setKeyValue([0,-1,0,0.125,0,0,1,0,0,1,0,0.125,0,0,1,0,0,-1,0,0.125])

Group2674.addChildren(OrientationInterpolator2689)
OrientationInterpolator2690 = OrientationInterpolator()
OrientationInterpolator2690.setDEF("Run_head_RotationInterpolator_Run")
OrientationInterpolator2690.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2690.setKeyValue([1,0,0,0.08,1,0,0,0.12,1,0,0,0.3,1,0,0,0.3,1,0,0,0.08])

Group2674.addChildren(OrientationInterpolator2690)
OrientationInterpolator2691 = OrientationInterpolator()
OrientationInterpolator2691.setDEF("Run_neck_RotationInterpolator_Run")
OrientationInterpolator2691.setKey([0,0.2545,0.4909,0.7091,1])
OrientationInterpolator2691.setKeyValue([0.7,0,0,0.4,-0.7,-0.7,0,0.4,0,0,0,0.4,-0.7,0.7,0,0.4,0.7,0,0,0.4])

Group2674.addChildren(OrientationInterpolator2691)
OrientationInterpolator2692 = OrientationInterpolator()
OrientationInterpolator2692.setDEF("Run_upper_body_RotationInterpolator_Run")
OrientationInterpolator2692.setKey([0,0.2545,0.4909,0.7636,1])
OrientationInterpolator2692.setKeyValue([0.97,0.65,0.086,0.5,0.9,0.003,-0.02,0.38,0.95,-0.68,-0.086,0.5,0.9,0.004,-0.025,0.4,0.97,0.65,0.086,0.5])

Group2674.addChildren(OrientationInterpolator2692)
OrientationInterpolator2693 = OrientationInterpolator()
OrientationInterpolator2693.setDEF("Run_whole_body_RotationInterpolator_Run")
OrientationInterpolator2693.setKey([0,0.25,0.5,0.75,1])
OrientationInterpolator2693.setKeyValue([1,0,0,0.06,1,0,0,0.167,1,0,0,0.06,1,0,0,0.168,1,0,0,0.06])

Group2674.addChildren(OrientationInterpolator2693)
PositionInterpolator2694 = PositionInterpolator()
PositionInterpolator2694.setDEF("Run_whole_body_TranslationInterpolator_Run")
PositionInterpolator2694.setKey([0,0.22,0.3,0.31,0.5,0.69,0.7,0.78,1])
PositionInterpolator2694.setKeyValue([0,-0.01,0,0,-0.037,0,0,-0.049,0,0,-0.037,0,0,-0.01,0,0,-0.037,0,0,-0.049,0,0,-0.037,0,0,-0.01,0])

Group2674.addChildren(PositionInterpolator2694)
OrientationInterpolator2695 = OrientationInterpolator()
OrientationInterpolator2695.setDEF("Run_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2695.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2695.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2695)
OrientationInterpolator2696 = OrientationInterpolator()
OrientationInterpolator2696.setDEF("Run_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2696.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2696.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2696)
OrientationInterpolator2697 = OrientationInterpolator()
OrientationInterpolator2697.setDEF("Run_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2697.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2697.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2697)
OrientationInterpolator2698 = OrientationInterpolator()
OrientationInterpolator2698.setDEF("Run_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2698.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2698.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2698)
OrientationInterpolator2699 = OrientationInterpolator()
OrientationInterpolator2699.setDEF("Run_sacroiliac_YawInterpolator")
OrientationInterpolator2699.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2699.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2699)
OrientationInterpolator2700 = OrientationInterpolator()
OrientationInterpolator2700.setDEF("Run_vl5_YawInterpolator")
OrientationInterpolator2700.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2700.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2700)
OrientationInterpolator2701 = OrientationInterpolator()
OrientationInterpolator2701.setDEF("Run_vc6_YawInterpolator")
OrientationInterpolator2701.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2701.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2674.addChildren(OrientationInterpolator2701)
OrientationInterpolator2702 = OrientationInterpolator()
OrientationInterpolator2702.setDEF("Run_l_thumb1_PitchInterpolator")
OrientationInterpolator2702.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2702.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.7,1,0,0,0.27,1,0,0,0.2,1,0,0,0])

Group2674.addChildren(OrientationInterpolator2702)
OrientationInterpolator2703 = OrientationInterpolator()
OrientationInterpolator2703.setDEF("Run_r_thumb1_PitchInterpolator")
OrientationInterpolator2703.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2703.setKeyValue([1,0,0,0,1,0,0,0.25,1,0,0,0.7,1,0,0,0.27,1,0,0,0.2,1,0,0,0])

Group2674.addChildren(OrientationInterpolator2703)
ROUTE2704 = ROUTE()
ROUTE2704.setFromField("fraction_changed")
ROUTE2704.setFromNode("RunTimer")
ROUTE2704.setToField("set_fraction")
ROUTE2704.setToNode("Run_r_ankle_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2704)
ROUTE2705 = ROUTE()
ROUTE2705.setFromField("fraction_changed")
ROUTE2705.setFromNode("RunTimer")
ROUTE2705.setToField("set_fraction")
ROUTE2705.setToNode("Run_r_knee_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2705)
ROUTE2706 = ROUTE()
ROUTE2706.setFromField("fraction_changed")
ROUTE2706.setFromNode("RunTimer")
ROUTE2706.setToField("set_fraction")
ROUTE2706.setToNode("Run_r_hip_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2706)
ROUTE2707 = ROUTE()
ROUTE2707.setFromField("fraction_changed")
ROUTE2707.setFromNode("RunTimer")
ROUTE2707.setToField("set_fraction")
ROUTE2707.setToNode("Run_l_ankle_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2707)
ROUTE2708 = ROUTE()
ROUTE2708.setFromField("fraction_changed")
ROUTE2708.setFromNode("RunTimer")
ROUTE2708.setToField("set_fraction")
ROUTE2708.setToNode("Run_l_knee_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2708)
ROUTE2709 = ROUTE()
ROUTE2709.setFromField("fraction_changed")
ROUTE2709.setFromNode("RunTimer")
ROUTE2709.setToField("set_fraction")
ROUTE2709.setToNode("Run_l_hip_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2709)
ROUTE2710 = ROUTE()
ROUTE2710.setFromField("fraction_changed")
ROUTE2710.setFromNode("RunTimer")
ROUTE2710.setToField("set_fraction")
ROUTE2710.setToNode("Run_lower_body_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2710)
ROUTE2711 = ROUTE()
ROUTE2711.setFromField("fraction_changed")
ROUTE2711.setFromNode("RunTimer")
ROUTE2711.setToField("set_fraction")
ROUTE2711.setToNode("Run_r_wrist_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2711)
ROUTE2712 = ROUTE()
ROUTE2712.setFromField("fraction_changed")
ROUTE2712.setFromNode("RunTimer")
ROUTE2712.setToField("set_fraction")
ROUTE2712.setToNode("Run_r_elbow_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2712)
ROUTE2713 = ROUTE()
ROUTE2713.setFromField("fraction_changed")
ROUTE2713.setFromNode("RunTimer")
ROUTE2713.setToField("set_fraction")
ROUTE2713.setToNode("Run_r_shoulder_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2713)
ROUTE2714 = ROUTE()
ROUTE2714.setFromField("fraction_changed")
ROUTE2714.setFromNode("RunTimer")
ROUTE2714.setToField("set_fraction")
ROUTE2714.setToNode("Run_l_wrist_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2714)
ROUTE2715 = ROUTE()
ROUTE2715.setFromField("fraction_changed")
ROUTE2715.setFromNode("RunTimer")
ROUTE2715.setToField("set_fraction")
ROUTE2715.setToNode("Run_l_elbow_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2715)
ROUTE2716 = ROUTE()
ROUTE2716.setFromField("fraction_changed")
ROUTE2716.setFromNode("RunTimer")
ROUTE2716.setToField("set_fraction")
ROUTE2716.setToNode("Run_l_shoulder_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2716)
ROUTE2717 = ROUTE()
ROUTE2717.setFromField("fraction_changed")
ROUTE2717.setFromNode("RunTimer")
ROUTE2717.setToField("set_fraction")
ROUTE2717.setToNode("Run_head_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2717)
ROUTE2718 = ROUTE()
ROUTE2718.setFromField("fraction_changed")
ROUTE2718.setFromNode("RunTimer")
ROUTE2718.setToField("set_fraction")
ROUTE2718.setToNode("Run_neck_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2718)
ROUTE2719 = ROUTE()
ROUTE2719.setFromField("fraction_changed")
ROUTE2719.setFromNode("RunTimer")
ROUTE2719.setToField("set_fraction")
ROUTE2719.setToNode("Run_upper_body_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2719)
ROUTE2720 = ROUTE()
ROUTE2720.setFromField("fraction_changed")
ROUTE2720.setFromNode("RunTimer")
ROUTE2720.setToField("set_fraction")
ROUTE2720.setToNode("Run_whole_body_RotationInterpolator_Run")

Group2674.addChildren(ROUTE2720)
ROUTE2721 = ROUTE()
ROUTE2721.setFromField("fraction_changed")
ROUTE2721.setFromNode("RunTimer")
ROUTE2721.setToField("set_fraction")
ROUTE2721.setToNode("Run_whole_body_TranslationInterpolator_Run")

Group2674.addChildren(ROUTE2721)
ROUTE2722 = ROUTE()
ROUTE2722.setFromField("fraction_changed")
ROUTE2722.setFromNode("RunTimer")
ROUTE2722.setToField("set_fraction")
ROUTE2722.setToNode("Run_l_sternoclavicular_RollInterpolator")

Group2674.addChildren(ROUTE2722)
ROUTE2723 = ROUTE()
ROUTE2723.setFromField("fraction_changed")
ROUTE2723.setFromNode("RunTimer")
ROUTE2723.setToField("set_fraction")
ROUTE2723.setToNode("Run_l_acromioclavicular_RollInterpolator")

Group2674.addChildren(ROUTE2723)
ROUTE2724 = ROUTE()
ROUTE2724.setFromField("fraction_changed")
ROUTE2724.setFromNode("RunTimer")
ROUTE2724.setToField("set_fraction")
ROUTE2724.setToNode("Run_r_sternoclavicular_RollInterpolator")

Group2674.addChildren(ROUTE2724)
ROUTE2725 = ROUTE()
ROUTE2725.setFromField("fraction_changed")
ROUTE2725.setFromNode("RunTimer")
ROUTE2725.setToField("set_fraction")
ROUTE2725.setToNode("Run_r_acromioclavicular_RollInterpolator")

Group2674.addChildren(ROUTE2725)
ROUTE2726 = ROUTE()
ROUTE2726.setFromField("fraction_changed")
ROUTE2726.setFromNode("RunTimer")
ROUTE2726.setToField("set_fraction")
ROUTE2726.setToNode("Run_r_metatarsal_PitchInterpolator")

Group2674.addChildren(ROUTE2726)
ROUTE2727 = ROUTE()
ROUTE2727.setFromField("fraction_changed")
ROUTE2727.setFromNode("RunTimer")
ROUTE2727.setToField("set_fraction")
ROUTE2727.setToNode("Run_sacroiliac_YawInterpolator")

Group2674.addChildren(ROUTE2727)
ROUTE2728 = ROUTE()
ROUTE2728.setFromField("fraction_changed")
ROUTE2728.setFromNode("RunTimer")
ROUTE2728.setToField("set_fraction")
ROUTE2728.setToNode("Run_vl5_YawInterpolator")

Group2674.addChildren(ROUTE2728)
ROUTE2729 = ROUTE()
ROUTE2729.setFromField("fraction_changed")
ROUTE2729.setFromNode("RunTimer")
ROUTE2729.setToField("set_fraction")
ROUTE2729.setToNode("Run_vc6_YawInterpolator")

Group2674.addChildren(ROUTE2729)
ROUTE2730 = ROUTE()
ROUTE2730.setFromField("fraction_changed")
ROUTE2730.setFromNode("RunTimer")
ROUTE2730.setToField("set_fraction")
ROUTE2730.setToNode("Run_l_thumb1_PitchInterpolator")

Group2674.addChildren(ROUTE2730)
ROUTE2731 = ROUTE()
ROUTE2731.setFromField("fraction_changed")
ROUTE2731.setFromNode("RunTimer")
ROUTE2731.setToField("set_fraction")
ROUTE2731.setToNode("Run_r_thumb1_PitchInterpolator")

Group2674.addChildren(ROUTE2731)
ROUTE2732 = ROUTE()
ROUTE2732.setFromField("value_changed")
ROUTE2732.setFromNode("Run_r_ankle_RotationInterpolator_Run")
ROUTE2732.setToField("rotation")
ROUTE2732.setToNode("hanim_r_ankle")

Group2674.addChildren(ROUTE2732)
ROUTE2733 = ROUTE()
ROUTE2733.setFromField("value_changed")
ROUTE2733.setFromNode("Run_r_knee_RotationInterpolator_Run")
ROUTE2733.setToField("rotation")
ROUTE2733.setToNode("hanim_r_knee")

Group2674.addChildren(ROUTE2733)
ROUTE2734 = ROUTE()
ROUTE2734.setFromField("value_changed")
ROUTE2734.setFromNode("Run_r_hip_RotationInterpolator_Run")
ROUTE2734.setToField("rotation")
ROUTE2734.setToNode("hanim_r_hip")

Group2674.addChildren(ROUTE2734)
ROUTE2735 = ROUTE()
ROUTE2735.setFromField("value_changed")
ROUTE2735.setFromNode("Run_l_ankle_RotationInterpolator_Run")
ROUTE2735.setToField("rotation")
ROUTE2735.setToNode("hanim_l_ankle")

Group2674.addChildren(ROUTE2735)
ROUTE2736 = ROUTE()
ROUTE2736.setFromField("value_changed")
ROUTE2736.setFromNode("Run_l_knee_RotationInterpolator_Run")
ROUTE2736.setToField("rotation")
ROUTE2736.setToNode("hanim_l_knee")

Group2674.addChildren(ROUTE2736)
ROUTE2737 = ROUTE()
ROUTE2737.setFromField("value_changed")
ROUTE2737.setFromNode("Run_l_hip_RotationInterpolator_Run")
ROUTE2737.setToField("rotation")
ROUTE2737.setToNode("hanim_l_hip")

Group2674.addChildren(ROUTE2737)
ROUTE2738 = ROUTE()
ROUTE2738.setFromField("value_changed")
ROUTE2738.setFromNode("Run_r_wrist_RotationInterpolator_Run")
ROUTE2738.setToField("rotation")
ROUTE2738.setToNode("hanim_r_wrist")

Group2674.addChildren(ROUTE2738)
ROUTE2739 = ROUTE()
ROUTE2739.setFromField("value_changed")
ROUTE2739.setFromNode("Run_r_elbow_RotationInterpolator_Run")
ROUTE2739.setToField("rotation")
ROUTE2739.setToNode("hanim_r_elbow")

Group2674.addChildren(ROUTE2739)
ROUTE2740 = ROUTE()
ROUTE2740.setFromField("value_changed")
ROUTE2740.setFromNode("Run_r_shoulder_RotationInterpolator_Run")
ROUTE2740.setToField("rotation")
ROUTE2740.setToNode("hanim_r_shoulder")

Group2674.addChildren(ROUTE2740)
ROUTE2741 = ROUTE()
ROUTE2741.setFromField("value_changed")
ROUTE2741.setFromNode("Run_l_wrist_RotationInterpolator_Run")
ROUTE2741.setToField("rotation")
ROUTE2741.setToNode("hanim_l_wrist")

Group2674.addChildren(ROUTE2741)
ROUTE2742 = ROUTE()
ROUTE2742.setFromField("value_changed")
ROUTE2742.setFromNode("Run_l_elbow_RotationInterpolator_Run")
ROUTE2742.setToField("rotation")
ROUTE2742.setToNode("hanim_l_elbow")

Group2674.addChildren(ROUTE2742)
ROUTE2743 = ROUTE()
ROUTE2743.setFromField("value_changed")
ROUTE2743.setFromNode("Run_l_shoulder_RotationInterpolator_Run")
ROUTE2743.setToField("rotation")
ROUTE2743.setToNode("hanim_l_shoulder")

Group2674.addChildren(ROUTE2743)
ROUTE2744 = ROUTE()
ROUTE2744.setFromField("value_changed")
ROUTE2744.setFromNode("Run_lower_body_RotationInterpolator_Run")
ROUTE2744.setToField("rotation")
ROUTE2744.setToNode("hanim_sacroiliac")

Group2674.addChildren(ROUTE2744)
ROUTE2745 = ROUTE()
ROUTE2745.setFromField("value_changed")
ROUTE2745.setFromNode("Run_head_RotationInterpolator_Run")
ROUTE2745.setToField("rotation")
ROUTE2745.setToNode("hanim_skullbase")

Group2674.addChildren(ROUTE2745)
ROUTE2746 = ROUTE()
ROUTE2746.setFromField("value_changed")
ROUTE2746.setFromNode("Run_neck_RotationInterpolator_Run")
ROUTE2746.setToField("rotation")
ROUTE2746.setToNode("hanim_vc4")

Group2674.addChildren(ROUTE2746)
ROUTE2747 = ROUTE()
ROUTE2747.setFromField("value_changed")
ROUTE2747.setFromNode("Run_upper_body_RotationInterpolator_Run")
ROUTE2747.setToField("rotation")
ROUTE2747.setToNode("hanim_vl1")

Group2674.addChildren(ROUTE2747)
ROUTE2748 = ROUTE()
ROUTE2748.setFromField("value_changed")
ROUTE2748.setFromNode("Run_whole_body_RotationInterpolator_Run")
ROUTE2748.setToField("rotation")
ROUTE2748.setToNode("hanim_humanoid_root")

Group2674.addChildren(ROUTE2748)
ROUTE2749 = ROUTE()
ROUTE2749.setFromField("value_changed")
ROUTE2749.setFromNode("Run_whole_body_TranslationInterpolator_Run")
ROUTE2749.setToField("translation")
ROUTE2749.setToNode("hanim_humanoid_root")

Group2674.addChildren(ROUTE2749)
ROUTE2750 = ROUTE()
ROUTE2750.setFromField("value_changed")
ROUTE2750.setFromNode("Run_l_sternoclavicular_RollInterpolator")
ROUTE2750.setToField("rotation")
ROUTE2750.setToNode("hanim_l_sternoclavicular")

Group2674.addChildren(ROUTE2750)
ROUTE2751 = ROUTE()
ROUTE2751.setFromField("value_changed")
ROUTE2751.setFromNode("Run_l_acromioclavicular_RollInterpolator")
ROUTE2751.setToField("rotation")
ROUTE2751.setToNode("hanim_l_acromioclavicular")

Group2674.addChildren(ROUTE2751)
ROUTE2752 = ROUTE()
ROUTE2752.setFromField("value_changed")
ROUTE2752.setFromNode("Run_r_sternoclavicular_RollInterpolator")
ROUTE2752.setToField("rotation")
ROUTE2752.setToNode("hanim_r_sternoclavicular")

Group2674.addChildren(ROUTE2752)
ROUTE2753 = ROUTE()
ROUTE2753.setFromField("value_changed")
ROUTE2753.setFromNode("Run_r_acromioclavicular_RollInterpolator")
ROUTE2753.setToField("rotation")
ROUTE2753.setToNode("hanim_r_acromioclavicular")

Group2674.addChildren(ROUTE2753)
ROUTE2754 = ROUTE()
ROUTE2754.setFromField("value_changed")
ROUTE2754.setFromNode("Run_r_metatarsal_PitchInterpolator")
ROUTE2754.setToField("rotation")
ROUTE2754.setToNode("hanim_l_metatarsal")

Group2674.addChildren(ROUTE2754)
ROUTE2755 = ROUTE()
ROUTE2755.setFromField("value_changed")
ROUTE2755.setFromNode("Run_r_metatarsal_PitchInterpolator")
ROUTE2755.setToField("rotation")
ROUTE2755.setToNode("hanim_r_metatarsal")

Group2674.addChildren(ROUTE2755)
ROUTE2756 = ROUTE()
ROUTE2756.setFromField("value_changed")
ROUTE2756.setFromNode("Run_sacroiliac_YawInterpolator")
ROUTE2756.setToField("rotation")
ROUTE2756.setToNode("hanim_sacroiliac")

Group2674.addChildren(ROUTE2756)
ROUTE2757 = ROUTE()
ROUTE2757.setFromField("value_changed")
ROUTE2757.setFromNode("Run_vl5_YawInterpolator")
ROUTE2757.setToField("rotation")
ROUTE2757.setToNode("hanim_vl5")

Group2674.addChildren(ROUTE2757)
ROUTE2758 = ROUTE()
ROUTE2758.setFromField("value_changed")
ROUTE2758.setFromNode("Run_vc6_YawInterpolator")
ROUTE2758.setToField("rotation")
ROUTE2758.setToNode("hanim_vc6")

Group2674.addChildren(ROUTE2758)
ROUTE2759 = ROUTE()
ROUTE2759.setFromField("value_changed")
ROUTE2759.setFromNode("Run_l_thumb1_PitchInterpolator")
ROUTE2759.setToField("rotation")
ROUTE2759.setToNode("hanim_l_thumb1")

Group2674.addChildren(ROUTE2759)
ROUTE2760 = ROUTE()
ROUTE2760.setFromField("value_changed")
ROUTE2760.setFromNode("Run_r_thumb1_PitchInterpolator")
ROUTE2760.setToField("rotation")
ROUTE2760.setToNode("hanim_r_thumb1")

Group2674.addChildren(ROUTE2760)

Scene31.addChildren(Group2674)
Group2761 = Group()
Group2761.setDEF("JumpAnimation")
TimeSensor2762 = TimeSensor()
TimeSensor2762.setDEF("JumpTimer")
TimeSensor2762.setCycleInterval(3.73)
TimeSensor2762.setLoop(True)

Group2761.addChildren(TimeSensor2762)
OrientationInterpolator2763 = OrientationInterpolator()
OrientationInterpolator2763.setDEF("Jump_r_metatarsal_PitchInterpolator")
OrientationInterpolator2763.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2763.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2763)
OrientationInterpolator2764 = OrientationInterpolator()
OrientationInterpolator2764.setDEF("Jump_r_ankle_RotationInterpolator")
OrientationInterpolator2764.setKey([0,0.1,0.15,0.25,0.28,0.32,0.35,0.64,0.76,0.84,0.88,0.92,0.96,1])
OrientationInterpolator2764.setKeyValue([0,0,1,0,-1,0,0,0.6735,-1,0,0,0.6735,-1,0,0,0.3527,-1,0,0,0.3038,-1,0,0,0.07964,1,0,0,1.3,1,0,0,0.6509,1,0,0,0.3001,-1,0,0,0.2087,-1,0,0,0.3756,-1,0,0,0.3279,-1,0,0,0.1193,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2764)
OrientationInterpolator2765 = OrientationInterpolator()
OrientationInterpolator2765.setDEF("Jump_r_knee_RotationInterpolator")
OrientationInterpolator2765.setKey([0,0.2,0.25,0.3,0.64,0.76,0.88,1])
OrientationInterpolator2765.setKeyValue([0,0,1,0,1,0,0,2.5,1,0,0,1.7,0,0,1,0,1,0,0,0.9507,1,0,0,0.5845,1,0,0,0.9054,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2765)
OrientationInterpolator2766 = OrientationInterpolator()
OrientationInterpolator2766.setDEF("Jump_r_hip_RotationInterpolator")
OrientationInterpolator2766.setKey([0,0.18,0.24,0.26,0.28,0.32,0.48,0.64,0.76,0.88,1])
OrientationInterpolator2766.setKeyValue([0,0,1,0,-1,0,0,1.63,-1,0,0,1.7,-1,0,0,1.55,-1,0,0,0.8943,-1,0,0,0.3698,0,0,1,0,-1,0,0,0.4963,-1,0,0,0.3829,-1,0,0,0.5169,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2766)
OrientationInterpolator2767 = OrientationInterpolator()
OrientationInterpolator2767.setDEF("Jump_l_ankle_RotationInterpolator")
OrientationInterpolator2767.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1])
OrientationInterpolator2767.setKeyValue([0,0,1,0,-1,0,0,0.625,-1,0,0,0.625,-1,0,0,0.3364,-1,0,0,0.2742,-1,0,0,0.05078,1,0,0,0.2833,1,0,0,0.6667,1,0,0,0.2833,-1,0,0,0.2108,-1,0,0,0.375,-1,0,0,0.3146,-1,0,0,0.1174,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2767)
OrientationInterpolator2768 = OrientationInterpolator()
OrientationInterpolator2768.setDEF("Jump_l_knee_RotationInterpolator")
OrientationInterpolator2768.setKey([0,0.28,0.32,0.48,0.64,0.76,0.88,1])
OrientationInterpolator2768.setKeyValue([0,0,1,0,1,0,0,2.047,1,0,0,2.047,0,0,1,0,1,0,0,1.566,1,0,0,0.5913,1,0,0,0.9235,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2768)
OrientationInterpolator2769 = OrientationInterpolator()
OrientationInterpolator2769.setDEF("Jump_l_hip_RotationInterpolator")
OrientationInterpolator2769.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1])
OrientationInterpolator2769.setKeyValue([0,0,1,0,1,0,0,4.349,1,0,0,4.349,1,0,0,4.615,-1,0,0,0.9136,-1,0,0,0.3614,0,0,1,0,-1,0,0,0.7869,-1,0,0,0.3918,-1,0,0,0.5433,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2769)
OrientationInterpolator2770 = OrientationInterpolator()
OrientationInterpolator2770.setDEF("Jump_lower_body_RotationInterpolator")
OrientationInterpolator2770.setKey([0,0.28,0.32,0.48,0.76,1])
OrientationInterpolator2770.setKeyValue([0,0,1,0,1,0,0,0.1892,1,0,0,0.1892,0,0,1,0,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2770)
OrientationInterpolator2771 = OrientationInterpolator()
OrientationInterpolator2771.setDEF("Jump_r_wrist_RotationInterpolator")
OrientationInterpolator2771.setKey([0,0.28,0.32,0.64,0.76,1])
OrientationInterpolator2771.setKeyValue([0,0,1,0,-0.0585279,0.983903,-0.168849,1.85956,-0.0585279,0.983903,-0.168849,1.85956,-0.00222418,0.99801,-0.0630095,1.46072,0,1,0,0.497349,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2771)
OrientationInterpolator2772 = OrientationInterpolator()
OrientationInterpolator2772.setDEF("Jump_r_elbow_RotationInterpolator")
OrientationInterpolator2772.setKey([0,0.28,0.32,0.64,0.76,1])
OrientationInterpolator2772.setKeyValue([0,0,1,0,-1,0,0,0.04151,-1,0,0,0.04151,-1,0,0,0.5855,-1,0,0,0.5852,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2772)
OrientationInterpolator2773 = OrientationInterpolator()
OrientationInterpolator2773.setDEF("Jump_r_shoulder_RotationInterpolator")
OrientationInterpolator2773.setKey([0,0.28,0.32,0.64,0.76,0.88,1])
OrientationInterpolator2773.setKeyValue([0,0,1,0,0.9992,0.02042,0.03558,4.688,0.9992,0.02042,0.03558,4.688,0.9989,-0.04623,0.005159,4.079,-0.8687,-0.2525,-0.4261,1.501,-0.941,-0.2893,-0.1754,0.4788,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2773)
OrientationInterpolator2774 = OrientationInterpolator()
OrientationInterpolator2774.setDEF("Jump_l_wrist_RotationInterpolator")
OrientationInterpolator2774.setKey([0,0.48,0.52,0.64,0.76,0.88,1])
OrientationInterpolator2774.setKeyValue([0,0,1,0,0.0672928,0.989475,-0.128107,4.15574,0.0672928,0.989475,-0.128107,4.15574,0.00364942,0.999901,0.0135896,4.5822,0,-1,0,0.655922,-0.00050618,-0.999999,0.0012782,1.28397,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2774)
OrientationInterpolator2775 = OrientationInterpolator()
OrientationInterpolator2775.setDEF("Jump_l_elbow_RotationInterpolator")
OrientationInterpolator2775.setKey([0,0.28,0.32,0.58,0.72,1])
OrientationInterpolator2775.setKeyValue([0,0,1,0,-1,0,0,1.13,-1,0,0,1.7,-1,0,0,1.7,-1,0,0,0.4,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2775)
OrientationInterpolator2776 = OrientationInterpolator()
OrientationInterpolator2776.setDEF("Jump_l_shoulder_RotationInterpolator")
OrientationInterpolator2776.setKey([0,0.28,0.32,0.64,0.76,0.88,1])
OrientationInterpolator2776.setKeyValue([0,0,1,0,-0.9987,0.02554,0.04498,1.57,-0.9987,0.02554,0.04498,1.57,1,0.0004113,0.003055,4.114,-0.8413,0.3238,0.4329,1.453,-0.877,0.4198,0.2337,0.6009,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2776)
OrientationInterpolator2777 = OrientationInterpolator()
OrientationInterpolator2777.setDEF("Jump_head_RotationInterpolator")
OrientationInterpolator2777.setKey([0,0.28,0.32,0.48,0.76,1])
OrientationInterpolator2777.setKeyValue([0,0,1,0,-1,0,0,0.5989,-1,0,0,0.5989,-1,0,0,0.3216,1,0,0,0.06503,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2777)
OrientationInterpolator2778 = OrientationInterpolator()
OrientationInterpolator2778.setDEF("Jump_neck_RotationInterpolator")
OrientationInterpolator2778.setKey([0,0.28,0.32,0.48,0.76,1])
OrientationInterpolator2778.setKeyValue([0,0,1,0,-1,0,0,0.1942,-1,0,0,0.1942,0,0,1,0,1,0,0,0.2284,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2778)
OrientationInterpolator2779 = OrientationInterpolator()
OrientationInterpolator2779.setDEF("Jump_upper_body_RotationInterpolator")
OrientationInterpolator2779.setKey([0,0.22,0.28,0.34,0.71,0.88,1])
OrientationInterpolator2779.setKeyValue([0,0,1,0,1,0,0,1.05,1,0,0,1.051,-1,0,0,0.257,1,0,0,0.2171,1,0,0,0.3465,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2779)
OrientationInterpolator2780 = OrientationInterpolator()
OrientationInterpolator2780.setDEF("Jump_whole_body_RotationInterpolator")
OrientationInterpolator2780.setKey([0,0.28,0.32,0.48,0.64,0.76,1])
OrientationInterpolator2780.setKeyValue([0,0,1,0,1,0,0,0.3273,1,0,0,0.3273,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2780)
PositionInterpolator2781 = PositionInterpolator()
PositionInterpolator2781.setDEF("Jump_whole_body_TranslationInterpolator")
PositionInterpolator2781.setKey([0,0.04,0.07,0.11,0.15,0.19,0.22,0.25,0.27,0.31,0.33,0.35,0.38,0.53,0.544,0.76,0.8,0.84,0.88,0.92,0.96,1])
PositionInterpolator2781.setKeyValue([0,0,0,0,-0.01264,-0.01289,0,-0.04712,-0.03738,-0.0003345,-0.1049,-0.05353,-0.0005712,-0.1892,-0.06561,-0.0008233,-0.286,-0.06276,-0.0009591,-0.3795,-0.05148,-0.00106,-0.4484,-0.03656,-0.00106,-0.4484,-0.03656,-0.001122,-0.25,-0.1499,-0.0008616,-0.05,-0.06358,-0.0005128,0.15,-0.05488,0.0004779,0.55,0.02732,0.0001728,1.385,0.006873,0.00017,1.395,0.0069,0,0.35,0.02148,0,-0.01299,-0.01057,0,-0.06932,-0.01064,0.0001365,-0.1037,-0.005059,0.0001279,-0.07198,-0.007596,0.000141,-0.01626,-0.004935,0,0,0])

Group2761.addChildren(PositionInterpolator2781)
OrientationInterpolator2782 = OrientationInterpolator()
OrientationInterpolator2782.setDEF("Jump_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2782.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2782.setKeyValue([0,0,1,0,0,0,1,0.2,0,0,1,0.22,0,0,1,0.2,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2782)
OrientationInterpolator2783 = OrientationInterpolator()
OrientationInterpolator2783.setDEF("Jump_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2783.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2783.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2783)
OrientationInterpolator2784 = OrientationInterpolator()
OrientationInterpolator2784.setDEF("Jump_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2784.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2784.setKeyValue([0,0,1,0,0,0,1,-0.2,0,0,1,-0.22,0,0,1,-0.2,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2784)
OrientationInterpolator2785 = OrientationInterpolator()
OrientationInterpolator2785.setDEF("Jump_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2785.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2785.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,-0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2761.addChildren(OrientationInterpolator2785)
OrientationInterpolator2786 = OrientationInterpolator()
OrientationInterpolator2786.setDEF("Jump_sacroiliac_YawInterpolator")
OrientationInterpolator2786.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2786.setKeyValue([0,1,0,0,0,-1,0,0.1,0,1,0,0,0,1,-1,0.24,0,-1,0,0.4,0,1,0,0])

Group2761.addChildren(OrientationInterpolator2786)
OrientationInterpolator2787 = OrientationInterpolator()
OrientationInterpolator2787.setDEF("Jump_vl5_YawInterpolator")
OrientationInterpolator2787.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2787.setKeyValue([0,1,0,0,0,1,0,-0.1,0,1,0,0,0,1,0,0,1,0,0,0.6,0,1,0,0.1,0,1,0,0])

Group2761.addChildren(OrientationInterpolator2787)
OrientationInterpolator2788 = OrientationInterpolator()
OrientationInterpolator2788.setDEF("Jump_vc6_YawInterpolator")
OrientationInterpolator2788.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2788.setKeyValue([0,1,0,0,0,1,0,0.8,0,1,0,0,0,1,0,0,-1,0,0,0.6,0,-1,0,0.8,0,1,0,0])

Group2761.addChildren(OrientationInterpolator2788)
OrientationInterpolator2789 = OrientationInterpolator()
OrientationInterpolator2789.setDEF("Jump_l_thumb1_PitchInterpolator")
OrientationInterpolator2789.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2789.setKeyValue([1,0,0,0,1,0,0,0.5,1,0,0,1.1,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2761.addChildren(OrientationInterpolator2789)
OrientationInterpolator2790 = OrientationInterpolator()
OrientationInterpolator2790.setDEF("Jump_r_thumb1_PitchInterpolator")
OrientationInterpolator2790.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2790.setKeyValue([1,0,0,0,1,0,0,0.5,1,0,0,1.1,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2761.addChildren(OrientationInterpolator2790)
ROUTE2791 = ROUTE()
ROUTE2791.setFromField("fraction_changed")
ROUTE2791.setFromNode("JumpTimer")
ROUTE2791.setToField("set_fraction")
ROUTE2791.setToNode("Jump_r_ankle_RotationInterpolator")

Group2761.addChildren(ROUTE2791)
ROUTE2792 = ROUTE()
ROUTE2792.setFromField("fraction_changed")
ROUTE2792.setFromNode("JumpTimer")
ROUTE2792.setToField("set_fraction")
ROUTE2792.setToNode("Jump_r_knee_RotationInterpolator")

Group2761.addChildren(ROUTE2792)
ROUTE2793 = ROUTE()
ROUTE2793.setFromField("fraction_changed")
ROUTE2793.setFromNode("JumpTimer")
ROUTE2793.setToField("set_fraction")
ROUTE2793.setToNode("Jump_r_hip_RotationInterpolator")

Group2761.addChildren(ROUTE2793)
ROUTE2794 = ROUTE()
ROUTE2794.setFromField("fraction_changed")
ROUTE2794.setFromNode("JumpTimer")
ROUTE2794.setToField("set_fraction")
ROUTE2794.setToNode("Jump_l_ankle_RotationInterpolator")

Group2761.addChildren(ROUTE2794)
ROUTE2795 = ROUTE()
ROUTE2795.setFromField("fraction_changed")
ROUTE2795.setFromNode("JumpTimer")
ROUTE2795.setToField("set_fraction")
ROUTE2795.setToNode("Jump_l_knee_RotationInterpolator")

Group2761.addChildren(ROUTE2795)
ROUTE2796 = ROUTE()
ROUTE2796.setFromField("fraction_changed")
ROUTE2796.setFromNode("JumpTimer")
ROUTE2796.setToField("set_fraction")
ROUTE2796.setToNode("Jump_l_hip_RotationInterpolator")

Group2761.addChildren(ROUTE2796)
ROUTE2797 = ROUTE()
ROUTE2797.setFromField("fraction_changed")
ROUTE2797.setFromNode("JumpTimer")
ROUTE2797.setToField("set_fraction")
ROUTE2797.setToNode("Jump_lower_body_RotationInterpolator")

Group2761.addChildren(ROUTE2797)
ROUTE2798 = ROUTE()
ROUTE2798.setFromField("fraction_changed")
ROUTE2798.setFromNode("JumpTimer")
ROUTE2798.setToField("set_fraction")
ROUTE2798.setToNode("Jump_r_wrist_RotationInterpolator")

Group2761.addChildren(ROUTE2798)
ROUTE2799 = ROUTE()
ROUTE2799.setFromField("fraction_changed")
ROUTE2799.setFromNode("JumpTimer")
ROUTE2799.setToField("set_fraction")
ROUTE2799.setToNode("Jump_r_elbow_RotationInterpolator")

Group2761.addChildren(ROUTE2799)
ROUTE2800 = ROUTE()
ROUTE2800.setFromField("fraction_changed")
ROUTE2800.setFromNode("JumpTimer")
ROUTE2800.setToField("set_fraction")
ROUTE2800.setToNode("Jump_r_shoulder_RotationInterpolator")

Group2761.addChildren(ROUTE2800)
ROUTE2801 = ROUTE()
ROUTE2801.setFromField("fraction_changed")
ROUTE2801.setFromNode("JumpTimer")
ROUTE2801.setToField("set_fraction")
ROUTE2801.setToNode("Jump_l_wrist_RotationInterpolator")

Group2761.addChildren(ROUTE2801)
ROUTE2802 = ROUTE()
ROUTE2802.setFromField("fraction_changed")
ROUTE2802.setFromNode("JumpTimer")
ROUTE2802.setToField("set_fraction")
ROUTE2802.setToNode("Jump_l_elbow_RotationInterpolator")

Group2761.addChildren(ROUTE2802)
ROUTE2803 = ROUTE()
ROUTE2803.setFromField("fraction_changed")
ROUTE2803.setFromNode("JumpTimer")
ROUTE2803.setToField("set_fraction")
ROUTE2803.setToNode("Jump_l_shoulder_RotationInterpolator")

Group2761.addChildren(ROUTE2803)
ROUTE2804 = ROUTE()
ROUTE2804.setFromField("fraction_changed")
ROUTE2804.setFromNode("JumpTimer")
ROUTE2804.setToField("set_fraction")
ROUTE2804.setToNode("Jump_head_RotationInterpolator")

Group2761.addChildren(ROUTE2804)
ROUTE2805 = ROUTE()
ROUTE2805.setFromField("fraction_changed")
ROUTE2805.setFromNode("JumpTimer")
ROUTE2805.setToField("set_fraction")
ROUTE2805.setToNode("Jump_neck_RotationInterpolator")

Group2761.addChildren(ROUTE2805)
ROUTE2806 = ROUTE()
ROUTE2806.setFromField("fraction_changed")
ROUTE2806.setFromNode("JumpTimer")
ROUTE2806.setToField("set_fraction")
ROUTE2806.setToNode("Jump_upper_body_RotationInterpolator")

Group2761.addChildren(ROUTE2806)
ROUTE2807 = ROUTE()
ROUTE2807.setFromField("fraction_changed")
ROUTE2807.setFromNode("JumpTimer")
ROUTE2807.setToField("set_fraction")
ROUTE2807.setToNode("Jump_whole_body_RotationInterpolator")

Group2761.addChildren(ROUTE2807)
ROUTE2808 = ROUTE()
ROUTE2808.setFromField("fraction_changed")
ROUTE2808.setFromNode("JumpTimer")
ROUTE2808.setToField("set_fraction")
ROUTE2808.setToNode("Jump_whole_body_TranslationInterpolator")

Group2761.addChildren(ROUTE2808)
ROUTE2809 = ROUTE()
ROUTE2809.setFromField("fraction_changed")
ROUTE2809.setFromNode("JumpTimer")
ROUTE2809.setToField("set_fraction")
ROUTE2809.setToNode("Jump_l_sternoclavicular_RollInterpolator")

Group2761.addChildren(ROUTE2809)
ROUTE2810 = ROUTE()
ROUTE2810.setFromField("fraction_changed")
ROUTE2810.setFromNode("JumpTimer")
ROUTE2810.setToField("set_fraction")
ROUTE2810.setToNode("Jump_l_acromioclavicular_RollInterpolator")

Group2761.addChildren(ROUTE2810)
ROUTE2811 = ROUTE()
ROUTE2811.setFromField("fraction_changed")
ROUTE2811.setFromNode("JumpTimer")
ROUTE2811.setToField("set_fraction")
ROUTE2811.setToNode("Jump_r_sternoclavicular_RollInterpolator")

Group2761.addChildren(ROUTE2811)
ROUTE2812 = ROUTE()
ROUTE2812.setFromField("fraction_changed")
ROUTE2812.setFromNode("JumpTimer")
ROUTE2812.setToField("set_fraction")
ROUTE2812.setToNode("Jump_r_acromioclavicular_RollInterpolator")

Group2761.addChildren(ROUTE2812)
ROUTE2813 = ROUTE()
ROUTE2813.setFromField("fraction_changed")
ROUTE2813.setFromNode("JumpTimer")
ROUTE2813.setToField("set_fraction")
ROUTE2813.setToNode("Jump_r_metatarsal_PitchInterpolator")

Group2761.addChildren(ROUTE2813)
ROUTE2814 = ROUTE()
ROUTE2814.setFromField("fraction_changed")
ROUTE2814.setFromNode("JumpTimer")
ROUTE2814.setToField("set_fraction")
ROUTE2814.setToNode("Jump_sacroiliac_YawInterpolator")

Group2761.addChildren(ROUTE2814)
ROUTE2815 = ROUTE()
ROUTE2815.setFromField("fraction_changed")
ROUTE2815.setFromNode("JumpTimer")
ROUTE2815.setToField("set_fraction")
ROUTE2815.setToNode("Jump_vl5_YawInterpolator")

Group2761.addChildren(ROUTE2815)
ROUTE2816 = ROUTE()
ROUTE2816.setFromField("fraction_changed")
ROUTE2816.setFromNode("JumpTimer")
ROUTE2816.setToField("set_fraction")
ROUTE2816.setToNode("Jump_vc6_YawInterpolator")

Group2761.addChildren(ROUTE2816)
ROUTE2817 = ROUTE()
ROUTE2817.setFromField("fraction_changed")
ROUTE2817.setFromNode("JumpTimer")
ROUTE2817.setToField("set_fraction")
ROUTE2817.setToNode("Jump_l_thumb1_PitchInterpolator")

Group2761.addChildren(ROUTE2817)
ROUTE2818 = ROUTE()
ROUTE2818.setFromField("fraction_changed")
ROUTE2818.setFromNode("JumpTimer")
ROUTE2818.setToField("set_fraction")
ROUTE2818.setToNode("Jump_r_thumb1_PitchInterpolator")

Group2761.addChildren(ROUTE2818)
ROUTE2819 = ROUTE()
ROUTE2819.setFromField("value_changed")
ROUTE2819.setFromNode("Jump_r_ankle_RotationInterpolator")
ROUTE2819.setToField("rotation")
ROUTE2819.setToNode("hanim_r_ankle")

Group2761.addChildren(ROUTE2819)
ROUTE2820 = ROUTE()
ROUTE2820.setFromField("value_changed")
ROUTE2820.setFromNode("Jump_r_knee_RotationInterpolator")
ROUTE2820.setToField("rotation")
ROUTE2820.setToNode("hanim_r_knee")

Group2761.addChildren(ROUTE2820)
ROUTE2821 = ROUTE()
ROUTE2821.setFromField("value_changed")
ROUTE2821.setFromNode("Jump_r_hip_RotationInterpolator")
ROUTE2821.setToField("rotation")
ROUTE2821.setToNode("hanim_r_hip")

Group2761.addChildren(ROUTE2821)
ROUTE2822 = ROUTE()
ROUTE2822.setFromField("value_changed")
ROUTE2822.setFromNode("Jump_l_ankle_RotationInterpolator")
ROUTE2822.setToField("rotation")
ROUTE2822.setToNode("hanim_l_ankle")

Group2761.addChildren(ROUTE2822)
ROUTE2823 = ROUTE()
ROUTE2823.setFromField("value_changed")
ROUTE2823.setFromNode("Jump_l_knee_RotationInterpolator")
ROUTE2823.setToField("rotation")
ROUTE2823.setToNode("hanim_l_knee")

Group2761.addChildren(ROUTE2823)
ROUTE2824 = ROUTE()
ROUTE2824.setFromField("value_changed")
ROUTE2824.setFromNode("Jump_l_hip_RotationInterpolator")
ROUTE2824.setToField("rotation")
ROUTE2824.setToNode("hanim_l_hip")

Group2761.addChildren(ROUTE2824)
ROUTE2825 = ROUTE()
ROUTE2825.setFromField("value_changed")
ROUTE2825.setFromNode("Jump_lower_body_RotationInterpolator")
ROUTE2825.setToField("rotation")
ROUTE2825.setToNode("hanim_sacroiliac")

Group2761.addChildren(ROUTE2825)
ROUTE2826 = ROUTE()
ROUTE2826.setFromField("value_changed")
ROUTE2826.setFromNode("Jump_r_wrist_RotationInterpolator")
ROUTE2826.setToField("rotation")
ROUTE2826.setToNode("hanim_r_wrist")

Group2761.addChildren(ROUTE2826)
ROUTE2827 = ROUTE()
ROUTE2827.setFromField("value_changed")
ROUTE2827.setFromNode("Jump_r_elbow_RotationInterpolator")
ROUTE2827.setToField("rotation")
ROUTE2827.setToNode("hanim_r_elbow")

Group2761.addChildren(ROUTE2827)
ROUTE2828 = ROUTE()
ROUTE2828.setFromField("value_changed")
ROUTE2828.setFromNode("Jump_r_shoulder_RotationInterpolator")
ROUTE2828.setToField("rotation")
ROUTE2828.setToNode("hanim_r_shoulder")

Group2761.addChildren(ROUTE2828)
ROUTE2829 = ROUTE()
ROUTE2829.setFromField("value_changed")
ROUTE2829.setFromNode("Jump_l_wrist_RotationInterpolator")
ROUTE2829.setToField("rotation")
ROUTE2829.setToNode("hanim_l_wrist")

Group2761.addChildren(ROUTE2829)
ROUTE2830 = ROUTE()
ROUTE2830.setFromField("value_changed")
ROUTE2830.setFromNode("Jump_l_elbow_RotationInterpolator")
ROUTE2830.setToField("rotation")
ROUTE2830.setToNode("hanim_l_elbow")

Group2761.addChildren(ROUTE2830)
ROUTE2831 = ROUTE()
ROUTE2831.setFromField("value_changed")
ROUTE2831.setFromNode("Jump_l_shoulder_RotationInterpolator")
ROUTE2831.setToField("rotation")
ROUTE2831.setToNode("hanim_l_shoulder")

Group2761.addChildren(ROUTE2831)
ROUTE2832 = ROUTE()
ROUTE2832.setFromField("value_changed")
ROUTE2832.setFromNode("Jump_head_RotationInterpolator")
ROUTE2832.setToField("rotation")
ROUTE2832.setToNode("hanim_skullbase")

Group2761.addChildren(ROUTE2832)
ROUTE2833 = ROUTE()
ROUTE2833.setFromField("value_changed")
ROUTE2833.setFromNode("Jump_neck_RotationInterpolator")
ROUTE2833.setToField("rotation")
ROUTE2833.setToNode("hanim_vc4")

Group2761.addChildren(ROUTE2833)
ROUTE2834 = ROUTE()
ROUTE2834.setFromField("value_changed")
ROUTE2834.setFromNode("Jump_upper_body_RotationInterpolator")
ROUTE2834.setToField("rotation")
ROUTE2834.setToNode("hanim_vl1")

Group2761.addChildren(ROUTE2834)
ROUTE2835 = ROUTE()
ROUTE2835.setFromField("value_changed")
ROUTE2835.setFromNode("Jump_whole_body_RotationInterpolator")
ROUTE2835.setToField("rotation")
ROUTE2835.setToNode("hanim_humanoid_root")

Group2761.addChildren(ROUTE2835)
ROUTE2836 = ROUTE()
ROUTE2836.setFromField("value_changed")
ROUTE2836.setFromNode("Jump_whole_body_TranslationInterpolator")
ROUTE2836.setToField("translation")
ROUTE2836.setToNode("hanim_humanoid_root")

Group2761.addChildren(ROUTE2836)
ROUTE2837 = ROUTE()
ROUTE2837.setFromField("value_changed")
ROUTE2837.setFromNode("Jump_l_sternoclavicular_RollInterpolator")
ROUTE2837.setToField("rotation")
ROUTE2837.setToNode("hanim_l_sternoclavicular")

Group2761.addChildren(ROUTE2837)
ROUTE2838 = ROUTE()
ROUTE2838.setFromField("value_changed")
ROUTE2838.setFromNode("Jump_l_acromioclavicular_RollInterpolator")
ROUTE2838.setToField("rotation")
ROUTE2838.setToNode("hanim_l_acromioclavicular")

Group2761.addChildren(ROUTE2838)
ROUTE2839 = ROUTE()
ROUTE2839.setFromField("value_changed")
ROUTE2839.setFromNode("Jump_r_sternoclavicular_RollInterpolator")
ROUTE2839.setToField("rotation")
ROUTE2839.setToNode("hanim_r_sternoclavicular")

Group2761.addChildren(ROUTE2839)
ROUTE2840 = ROUTE()
ROUTE2840.setFromField("value_changed")
ROUTE2840.setFromNode("Jump_r_acromioclavicular_RollInterpolator")
ROUTE2840.setToField("rotation")
ROUTE2840.setToNode("hanim_r_acromioclavicular")

Group2761.addChildren(ROUTE2840)
ROUTE2841 = ROUTE()
ROUTE2841.setFromField("value_changed")
ROUTE2841.setFromNode("Jump_r_metatarsal_PitchInterpolator")
ROUTE2841.setToField("rotation")
ROUTE2841.setToNode("hanim_l_metatarsal")

Group2761.addChildren(ROUTE2841)
ROUTE2842 = ROUTE()
ROUTE2842.setFromField("value_changed")
ROUTE2842.setFromNode("Jump_r_metatarsal_PitchInterpolator")
ROUTE2842.setToField("rotation")
ROUTE2842.setToNode("hanim_r_metatarsal")

Group2761.addChildren(ROUTE2842)
ROUTE2843 = ROUTE()
ROUTE2843.setFromField("value_changed")
ROUTE2843.setFromNode("Jump_sacroiliac_YawInterpolator")
ROUTE2843.setToField("rotation")
ROUTE2843.setToNode("hanim_sacroiliac")

Group2761.addChildren(ROUTE2843)
ROUTE2844 = ROUTE()
ROUTE2844.setFromField("value_changed")
ROUTE2844.setFromNode("Jump_vl5_YawInterpolator")
ROUTE2844.setToField("rotation")
ROUTE2844.setToNode("hanim_vl5")

Group2761.addChildren(ROUTE2844)
ROUTE2845 = ROUTE()
ROUTE2845.setFromField("value_changed")
ROUTE2845.setFromNode("Jump_vc6_YawInterpolator")
ROUTE2845.setToField("rotation")
ROUTE2845.setToNode("hanim_vc6")

Group2761.addChildren(ROUTE2845)
ROUTE2846 = ROUTE()
ROUTE2846.setFromField("value_changed")
ROUTE2846.setFromNode("Jump_l_thumb1_PitchInterpolator")
ROUTE2846.setToField("rotation")
ROUTE2846.setToNode("hanim_l_thumb1")

Group2761.addChildren(ROUTE2846)
ROUTE2847 = ROUTE()
ROUTE2847.setFromField("value_changed")
ROUTE2847.setFromNode("Jump_r_thumb1_PitchInterpolator")
ROUTE2847.setToField("rotation")
ROUTE2847.setToNode("hanim_r_thumb1")

Group2761.addChildren(ROUTE2847)

Scene31.addChildren(Group2761)
Group2848 = Group()
Group2848.setDEF("KickAnimation")
TimeSensor2849 = TimeSensor()
TimeSensor2849.setDEF("KickTimer")
TimeSensor2849.setCycleInterval(3.73)
TimeSensor2849.setLoop(True)

Group2848.addChildren(TimeSensor2849)
OrientationInterpolator2850 = OrientationInterpolator()
OrientationInterpolator2850.setDEF("Kick_l_sternoclavicular_RollInterpolator")
OrientationInterpolator2850.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2850.setKeyValue([0,0,1,0,0,0,1,0.2,0,0,1,0.22,0,0,1,0.2,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2850)
OrientationInterpolator2851 = OrientationInterpolator()
OrientationInterpolator2851.setDEF("Kick_l_acromioclavicular_RollInterpolator")
OrientationInterpolator2851.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2851.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2851)
OrientationInterpolator2852 = OrientationInterpolator()
OrientationInterpolator2852.setDEF("Kick_l_shoulder_RollInterpolator")
OrientationInterpolator2852.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2852.setKeyValue([0,0,1,0,0,0,1,1.76,-0.25,0,1,1.76,0,0,1,1.256,0,0,1,0.05,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2852)
OrientationInterpolator2853 = OrientationInterpolator()
OrientationInterpolator2853.setDEF("Kick_l_ForeArm_PitchInterpolator")
OrientationInterpolator2853.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2853.setKeyValue([1,0,0,0,1,0,0,-0.55,-1,0.25,0,2.55,1,0,0,0,1,0,0,0,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2853)
OrientationInterpolator2854 = OrientationInterpolator()
OrientationInterpolator2854.setDEF("Kick_l_wrist_RollInterpolator")
OrientationInterpolator2854.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2854.setKeyValue([0,0,1,0,0,0,1,0,0,1,0,0.55,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2854)
OrientationInterpolator2855 = OrientationInterpolator()
OrientationInterpolator2855.setDEF("Kick_l_thumb1_PitchInterpolator")
OrientationInterpolator2855.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2855.setKeyValue([1,0,0,0,1,0,0,0.5,1,0,0,1.1,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2855)
OrientationInterpolator2856 = OrientationInterpolator()
OrientationInterpolator2856.setDEF("Kick_r_sternoclavicular_RollInterpolator")
OrientationInterpolator2856.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2856.setKeyValue([0,0,1,0,0,0,1,-0.2,0,0,1,-0.22,0,0,1,-0.2,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2856)
OrientationInterpolator2857 = OrientationInterpolator()
OrientationInterpolator2857.setDEF("Kick_r_acromioclavicular_RollInterpolator")
OrientationInterpolator2857.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2857.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,-0.05,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2857)
OrientationInterpolator2858 = OrientationInterpolator()
OrientationInterpolator2858.setDEF("Kick_r_shoulder_RollInterpolator")
OrientationInterpolator2858.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2858.setKeyValue([0,0,1,0,0,0,1,-1.76,0.25,0,1,-1.76,0,0,1,-1.256,0,0,1,-0.05,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2858)
OrientationInterpolator2859 = OrientationInterpolator()
OrientationInterpolator2859.setDEF("Kick_r_ForeArm_PitchInterpolator")
OrientationInterpolator2859.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2859.setKeyValue([1,0,0,0,1,0,0,-0.55,1,0.25,0,-2.55,1,0,0,0,1,0,0,0,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2859)
OrientationInterpolator2860 = OrientationInterpolator()
OrientationInterpolator2860.setDEF("Kick_r_wrist_RollInterpolator")
OrientationInterpolator2860.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2860.setKeyValue([0,0,1,0,0,0,1,0,0,1,0,-0.55,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2860)
OrientationInterpolator2861 = OrientationInterpolator()
OrientationInterpolator2861.setDEF("Kick_r_thumb1_PitchInterpolator")
OrientationInterpolator2861.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2861.setKeyValue([1,0,0,0,1,0,0,0.5,1,0,0,1.1,1,0,0,0.7,1,0,0,0.2,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2861)
OrientationInterpolator2862 = OrientationInterpolator()
OrientationInterpolator2862.setDEF("Kick_r_hip_PitchInterpolator")
OrientationInterpolator2862.setKey([0,0.2,0.3,0.5,0.6,0.9,1])
OrientationInterpolator2862.setKeyValue([1,0,0,0,1,0,0,0.9,-1,0,0,1.75,-1,0,0,2.25,-1,0,0,2,1,0,0,0,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2862)
OrientationInterpolator2863 = OrientationInterpolator()
OrientationInterpolator2863.setDEF("Kick_r_knee_PitchInterpolator")
OrientationInterpolator2863.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2863.setKeyValue([0,0,1,0,1,0,0,1.95,1,0,0,1.75,-1,0,0,0.28,1,0,0,0,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2863)
OrientationInterpolator2864 = OrientationInterpolator()
OrientationInterpolator2864.setDEF("Kick_l_hip_PitchInterpolator")
OrientationInterpolator2864.setKey([0,0.2,0.3,0.5,0.6,0.9,1])
OrientationInterpolator2864.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2864)
OrientationInterpolator2865 = OrientationInterpolator()
OrientationInterpolator2865.setDEF("Kick_l_knee_PitchInterpolator")
OrientationInterpolator2865.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2865.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2865)
OrientationInterpolator2866 = OrientationInterpolator()
OrientationInterpolator2866.setDEF("Kick_r_ankle_PitchInterpolator")
OrientationInterpolator2866.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2866.setKeyValue([0,0,1,0,-1,0,0,0.9,-1,0,0,0.95,1,0,0,0.75,-1,0,0,0.05,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2866)
OrientationInterpolator2867 = OrientationInterpolator()
OrientationInterpolator2867.setDEF("Kick_r_metatarsal_PitchInterpolator")
OrientationInterpolator2867.setKey([0,0.2,0.4,0.6,0.7,1])
OrientationInterpolator2867.setKeyValue([1,0,0,0,-1,0,0,0.5,-1,0,0,0.7,1,0,0,0.75,-1,0,0,0.2,1,0,0,0])

Group2848.addChildren(OrientationInterpolator2867)
OrientationInterpolator2868 = OrientationInterpolator()
OrientationInterpolator2868.setDEF("Kick_sacroiliac_YawInterpolator")
OrientationInterpolator2868.setKey([0,0.2,0.4,0.6,0.8,1])
OrientationInterpolator2868.setKeyValue([0,1,0,0,0,-1,0,0.1,0,1,0,0,0,1,-1,0.24,0,-1,0,0.4,0,1,0,0])

Group2848.addChildren(OrientationInterpolator2868)
OrientationInterpolator2869 = OrientationInterpolator()
OrientationInterpolator2869.setDEF("Kick_vl5_YawInterpolator")
OrientationInterpolator2869.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2869.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2869)
OrientationInterpolator2870 = OrientationInterpolator()
OrientationInterpolator2870.setDEF("Kick_vc6_YawInterpolator")
OrientationInterpolator2870.setKey([0,0.2,0.4,0.5,0.6,0.8,1])
OrientationInterpolator2870.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2870)
OrientationInterpolator2871 = OrientationInterpolator()
OrientationInterpolator2871.setDEF("Kick_lower_body_RotationInterpolator")
OrientationInterpolator2871.setKey([0,0.5,1])
OrientationInterpolator2871.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2871)
OrientationInterpolator2872 = OrientationInterpolator()
OrientationInterpolator2872.setDEF("Kick_upper_body_RotationInterpolator")
OrientationInterpolator2872.setKey([0,0.5,1])
OrientationInterpolator2872.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2872)
OrientationInterpolator2873 = OrientationInterpolator()
OrientationInterpolator2873.setDEF("Kick_whole_body_RotationInterpolator")
OrientationInterpolator2873.setKey([0,0.5,1])
OrientationInterpolator2873.setKeyValue([0,0,1,0,0,0,1,0,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2873)
PositionInterpolator2874 = PositionInterpolator()
PositionInterpolator2874.setDEF("Kick_whole_body_TranslationInterpolator")
PositionInterpolator2874.setKey([0,0.5,1])
PositionInterpolator2874.setKeyValue([0,0,0,0,0,0,0,0,0])

Group2848.addChildren(PositionInterpolator2874)
OrientationInterpolator2875 = OrientationInterpolator()
OrientationInterpolator2875.setDEF("Kick_neck_RotationInterpolator")
OrientationInterpolator2875.setKey([0,0.25,0.55,1])
OrientationInterpolator2875.setKeyValue([0,0,1,0,1,0,0,0.7,1,0,0,0.5,0,0,1,0])

Group2848.addChildren(OrientationInterpolator2875)
ROUTE2876 = ROUTE()
ROUTE2876.setFromField("fraction_changed")
ROUTE2876.setFromNode("KickTimer")
ROUTE2876.setToField("set_fraction")
ROUTE2876.setToNode("Kick_l_sternoclavicular_RollInterpolator")

Group2848.addChildren(ROUTE2876)
ROUTE2877 = ROUTE()
ROUTE2877.setFromField("fraction_changed")
ROUTE2877.setFromNode("KickTimer")
ROUTE2877.setToField("set_fraction")
ROUTE2877.setToNode("Kick_l_acromioclavicular_RollInterpolator")

Group2848.addChildren(ROUTE2877)
ROUTE2878 = ROUTE()
ROUTE2878.setFromField("fraction_changed")
ROUTE2878.setFromNode("KickTimer")
ROUTE2878.setToField("set_fraction")
ROUTE2878.setToNode("Kick_l_shoulder_RollInterpolator")

Group2848.addChildren(ROUTE2878)
ROUTE2879 = ROUTE()
ROUTE2879.setFromField("fraction_changed")
ROUTE2879.setFromNode("KickTimer")
ROUTE2879.setToField("set_fraction")
ROUTE2879.setToNode("Kick_l_ForeArm_PitchInterpolator")

Group2848.addChildren(ROUTE2879)
ROUTE2880 = ROUTE()
ROUTE2880.setFromField("fraction_changed")
ROUTE2880.setFromNode("KickTimer")
ROUTE2880.setToField("set_fraction")
ROUTE2880.setToNode("Kick_l_wrist_RollInterpolator")

Group2848.addChildren(ROUTE2880)
ROUTE2881 = ROUTE()
ROUTE2881.setFromField("fraction_changed")
ROUTE2881.setFromNode("KickTimer")
ROUTE2881.setToField("set_fraction")
ROUTE2881.setToNode("Kick_l_thumb1_PitchInterpolator")

Group2848.addChildren(ROUTE2881)
ROUTE2882 = ROUTE()
ROUTE2882.setFromField("fraction_changed")
ROUTE2882.setFromNode("KickTimer")
ROUTE2882.setToField("set_fraction")
ROUTE2882.setToNode("Kick_r_sternoclavicular_RollInterpolator")

Group2848.addChildren(ROUTE2882)
ROUTE2883 = ROUTE()
ROUTE2883.setFromField("fraction_changed")
ROUTE2883.setFromNode("KickTimer")
ROUTE2883.setToField("set_fraction")
ROUTE2883.setToNode("Kick_r_acromioclavicular_RollInterpolator")

Group2848.addChildren(ROUTE2883)
ROUTE2884 = ROUTE()
ROUTE2884.setFromField("fraction_changed")
ROUTE2884.setFromNode("KickTimer")
ROUTE2884.setToField("set_fraction")
ROUTE2884.setToNode("Kick_r_shoulder_RollInterpolator")

Group2848.addChildren(ROUTE2884)
ROUTE2885 = ROUTE()
ROUTE2885.setFromField("fraction_changed")
ROUTE2885.setFromNode("KickTimer")
ROUTE2885.setToField("set_fraction")
ROUTE2885.setToNode("Kick_r_ForeArm_PitchInterpolator")

Group2848.addChildren(ROUTE2885)
ROUTE2886 = ROUTE()
ROUTE2886.setFromField("fraction_changed")
ROUTE2886.setFromNode("KickTimer")
ROUTE2886.setToField("set_fraction")
ROUTE2886.setToNode("Kick_r_wrist_RollInterpolator")

Group2848.addChildren(ROUTE2886)
ROUTE2887 = ROUTE()
ROUTE2887.setFromField("fraction_changed")
ROUTE2887.setFromNode("KickTimer")
ROUTE2887.setToField("set_fraction")
ROUTE2887.setToNode("Kick_r_thumb1_PitchInterpolator")

Group2848.addChildren(ROUTE2887)
ROUTE2888 = ROUTE()
ROUTE2888.setFromField("fraction_changed")
ROUTE2888.setFromNode("KickTimer")
ROUTE2888.setToField("set_fraction")
ROUTE2888.setToNode("Kick_r_hip_PitchInterpolator")

Group2848.addChildren(ROUTE2888)
ROUTE2889 = ROUTE()
ROUTE2889.setFromField("fraction_changed")
ROUTE2889.setFromNode("KickTimer")
ROUTE2889.setToField("set_fraction")
ROUTE2889.setToNode("Kick_r_knee_PitchInterpolator")

Group2848.addChildren(ROUTE2889)
ROUTE2890 = ROUTE()
ROUTE2890.setFromField("fraction_changed")
ROUTE2890.setFromNode("KickTimer")
ROUTE2890.setToField("set_fraction")
ROUTE2890.setToNode("Kick_l_hip_PitchInterpolator")

Group2848.addChildren(ROUTE2890)
ROUTE2891 = ROUTE()
ROUTE2891.setFromField("fraction_changed")
ROUTE2891.setFromNode("KickTimer")
ROUTE2891.setToField("set_fraction")
ROUTE2891.setToNode("Kick_l_knee_PitchInterpolator")

Group2848.addChildren(ROUTE2891)
ROUTE2892 = ROUTE()
ROUTE2892.setFromField("fraction_changed")
ROUTE2892.setFromNode("KickTimer")
ROUTE2892.setToField("set_fraction")
ROUTE2892.setToNode("Kick_r_ankle_PitchInterpolator")

Group2848.addChildren(ROUTE2892)
ROUTE2893 = ROUTE()
ROUTE2893.setFromField("fraction_changed")
ROUTE2893.setFromNode("KickTimer")
ROUTE2893.setToField("set_fraction")
ROUTE2893.setToNode("Kick_r_metatarsal_PitchInterpolator")

Group2848.addChildren(ROUTE2893)
ROUTE2894 = ROUTE()
ROUTE2894.setFromField("fraction_changed")
ROUTE2894.setFromNode("KickTimer")
ROUTE2894.setToField("set_fraction")
ROUTE2894.setToNode("Kick_sacroiliac_YawInterpolator")

Group2848.addChildren(ROUTE2894)
ROUTE2895 = ROUTE()
ROUTE2895.setFromField("fraction_changed")
ROUTE2895.setFromNode("KickTimer")
ROUTE2895.setToField("set_fraction")
ROUTE2895.setToNode("Kick_vl5_YawInterpolator")

Group2848.addChildren(ROUTE2895)
ROUTE2896 = ROUTE()
ROUTE2896.setFromField("fraction_changed")
ROUTE2896.setFromNode("KickTimer")
ROUTE2896.setToField("set_fraction")
ROUTE2896.setToNode("Kick_vc6_YawInterpolator")

Group2848.addChildren(ROUTE2896)
ROUTE2897 = ROUTE()
ROUTE2897.setFromField("fraction_changed")
ROUTE2897.setFromNode("KickTimer")
ROUTE2897.setToField("set_fraction")
ROUTE2897.setToNode("Kick_lower_body_RotationInterpolator")

Group2848.addChildren(ROUTE2897)
ROUTE2898 = ROUTE()
ROUTE2898.setFromField("fraction_changed")
ROUTE2898.setFromNode("KickTimer")
ROUTE2898.setToField("set_fraction")
ROUTE2898.setToNode("Kick_upper_body_RotationInterpolator")

Group2848.addChildren(ROUTE2898)
ROUTE2899 = ROUTE()
ROUTE2899.setFromField("fraction_changed")
ROUTE2899.setFromNode("KickTimer")
ROUTE2899.setToField("set_fraction")
ROUTE2899.setToNode("Kick_whole_body_RotationInterpolator")

Group2848.addChildren(ROUTE2899)
ROUTE2900 = ROUTE()
ROUTE2900.setFromField("fraction_changed")
ROUTE2900.setFromNode("KickTimer")
ROUTE2900.setToField("set_fraction")
ROUTE2900.setToNode("Kick_whole_body_TranslationInterpolator")

Group2848.addChildren(ROUTE2900)
ROUTE2901 = ROUTE()
ROUTE2901.setFromField("fraction_changed")
ROUTE2901.setFromNode("KickTimer")
ROUTE2901.setToField("set_fraction")
ROUTE2901.setToNode("Kick_neck_RotationInterpolator")

Group2848.addChildren(ROUTE2901)
ROUTE2902 = ROUTE()
ROUTE2902.setFromField("value_changed")
ROUTE2902.setFromNode("Kick_l_sternoclavicular_RollInterpolator")
ROUTE2902.setToField("rotation")
ROUTE2902.setToNode("hanim_l_sternoclavicular")

Group2848.addChildren(ROUTE2902)
ROUTE2903 = ROUTE()
ROUTE2903.setFromField("value_changed")
ROUTE2903.setFromNode("Kick_l_acromioclavicular_RollInterpolator")
ROUTE2903.setToField("rotation")
ROUTE2903.setToNode("hanim_l_acromioclavicular")

Group2848.addChildren(ROUTE2903)
ROUTE2904 = ROUTE()
ROUTE2904.setFromField("value_changed")
ROUTE2904.setFromNode("Kick_l_shoulder_RollInterpolator")
ROUTE2904.setToField("rotation")
ROUTE2904.setToNode("hanim_l_shoulder")

Group2848.addChildren(ROUTE2904)
ROUTE2905 = ROUTE()
ROUTE2905.setFromField("value_changed")
ROUTE2905.setFromNode("Kick_l_ForeArm_PitchInterpolator")
ROUTE2905.setToField("rotation")
ROUTE2905.setToNode("hanim_l_elbow")

Group2848.addChildren(ROUTE2905)
ROUTE2906 = ROUTE()
ROUTE2906.setFromField("value_changed")
ROUTE2906.setFromNode("Kick_l_wrist_RollInterpolator")
ROUTE2906.setToField("rotation")
ROUTE2906.setToNode("hanim_l_wrist")

Group2848.addChildren(ROUTE2906)
ROUTE2907 = ROUTE()
ROUTE2907.setFromField("value_changed")
ROUTE2907.setFromNode("Kick_l_thumb1_PitchInterpolator")
ROUTE2907.setToField("rotation")
ROUTE2907.setToNode("hanim_l_thumb1")

Group2848.addChildren(ROUTE2907)
ROUTE2908 = ROUTE()
ROUTE2908.setFromField("value_changed")
ROUTE2908.setFromNode("Kick_r_sternoclavicular_RollInterpolator")
ROUTE2908.setToField("rotation")
ROUTE2908.setToNode("hanim_r_sternoclavicular")

Group2848.addChildren(ROUTE2908)
ROUTE2909 = ROUTE()
ROUTE2909.setFromField("value_changed")
ROUTE2909.setFromNode("Kick_r_acromioclavicular_RollInterpolator")
ROUTE2909.setToField("rotation")
ROUTE2909.setToNode("hanim_r_acromioclavicular")

Group2848.addChildren(ROUTE2909)
ROUTE2910 = ROUTE()
ROUTE2910.setFromField("value_changed")
ROUTE2910.setFromNode("Kick_r_shoulder_RollInterpolator")
ROUTE2910.setToField("rotation")
ROUTE2910.setToNode("hanim_r_shoulder")

Group2848.addChildren(ROUTE2910)
ROUTE2911 = ROUTE()
ROUTE2911.setFromField("value_changed")
ROUTE2911.setFromNode("Kick_r_ForeArm_PitchInterpolator")
ROUTE2911.setToField("rotation")
ROUTE2911.setToNode("hanim_r_elbow")

Group2848.addChildren(ROUTE2911)
ROUTE2912 = ROUTE()
ROUTE2912.setFromField("value_changed")
ROUTE2912.setFromNode("Kick_r_wrist_RollInterpolator")
ROUTE2912.setToField("rotation")
ROUTE2912.setToNode("hanim_r_wrist")

Group2848.addChildren(ROUTE2912)
ROUTE2913 = ROUTE()
ROUTE2913.setFromField("value_changed")
ROUTE2913.setFromNode("Kick_r_thumb1_PitchInterpolator")
ROUTE2913.setToField("rotation")
ROUTE2913.setToNode("hanim_r_thumb1")

Group2848.addChildren(ROUTE2913)
ROUTE2914 = ROUTE()
ROUTE2914.setFromField("value_changed")
ROUTE2914.setFromNode("Kick_r_hip_PitchInterpolator")
ROUTE2914.setToField("rotation")
ROUTE2914.setToNode("hanim_r_hip")

Group2848.addChildren(ROUTE2914)
ROUTE2915 = ROUTE()
ROUTE2915.setFromField("value_changed")
ROUTE2915.setFromNode("Kick_r_knee_PitchInterpolator")
ROUTE2915.setToField("rotation")
ROUTE2915.setToNode("hanim_r_knee")

Group2848.addChildren(ROUTE2915)
ROUTE2916 = ROUTE()
ROUTE2916.setFromField("value_changed")
ROUTE2916.setFromNode("Kick_r_ankle_PitchInterpolator")
ROUTE2916.setToField("rotation")
ROUTE2916.setToNode("hanim_r_ankle")

Group2848.addChildren(ROUTE2916)
ROUTE2917 = ROUTE()
ROUTE2917.setFromField("value_changed")
ROUTE2917.setFromNode("Kick_r_metatarsal_PitchInterpolator")
ROUTE2917.setToField("rotation")
ROUTE2917.setToNode("hanim_r_metatarsal")

Group2848.addChildren(ROUTE2917)
ROUTE2918 = ROUTE()
ROUTE2918.setFromField("value_changed")
ROUTE2918.setFromNode("Kick_l_hip_PitchInterpolator")
ROUTE2918.setToField("rotation")
ROUTE2918.setToNode("hanim_l_hip")

Group2848.addChildren(ROUTE2918)
ROUTE2919 = ROUTE()
ROUTE2919.setFromField("value_changed")
ROUTE2919.setFromNode("Kick_l_knee_PitchInterpolator")
ROUTE2919.setToField("rotation")
ROUTE2919.setToNode("hanim_l_knee")

Group2848.addChildren(ROUTE2919)
ROUTE2920 = ROUTE()
ROUTE2920.setFromField("value_changed")
ROUTE2920.setFromNode("Kick_r_ankle_PitchInterpolator")
ROUTE2920.setToField("rotation")
ROUTE2920.setToNode("hanim_l_ankle")

Group2848.addChildren(ROUTE2920)
ROUTE2921 = ROUTE()
ROUTE2921.setFromField("value_changed")
ROUTE2921.setFromNode("Kick_r_metatarsal_PitchInterpolator")
ROUTE2921.setToField("rotation")
ROUTE2921.setToNode("hanim_l_metatarsal")

Group2848.addChildren(ROUTE2921)
ROUTE2922 = ROUTE()
ROUTE2922.setFromField("value_changed")
ROUTE2922.setFromNode("Kick_sacroiliac_YawInterpolator")
ROUTE2922.setToField("rotation")
ROUTE2922.setToNode("hanim_sacroiliac")

Group2848.addChildren(ROUTE2922)
ROUTE2923 = ROUTE()
ROUTE2923.setFromField("value_changed")
ROUTE2923.setFromNode("Kick_vl5_YawInterpolator")
ROUTE2923.setToField("rotation")
ROUTE2923.setToNode("hanim_vl5")

Group2848.addChildren(ROUTE2923)
ROUTE2924 = ROUTE()
ROUTE2924.setFromField("value_changed")
ROUTE2924.setFromNode("Kick_vc6_YawInterpolator")
ROUTE2924.setToField("rotation")
ROUTE2924.setToNode("hanim_vc6")

Group2848.addChildren(ROUTE2924)
ROUTE2925 = ROUTE()
ROUTE2925.setFromField("value_changed")
ROUTE2925.setFromNode("Kick_upper_body_RotationInterpolator")
ROUTE2925.setToField("rotation")
ROUTE2925.setToNode("hanim_vl1")

Group2848.addChildren(ROUTE2925)
ROUTE2926 = ROUTE()
ROUTE2926.setFromField("value_changed")
ROUTE2926.setFromNode("Kick_lower_body_RotationInterpolator")
ROUTE2926.setToField("rotation")
ROUTE2926.setToNode("hanim_sacroiliac")

Group2848.addChildren(ROUTE2926)
ROUTE2927 = ROUTE()
ROUTE2927.setFromField("value_changed")
ROUTE2927.setFromNode("Kick_whole_body_RotationInterpolator")
ROUTE2927.setToField("rotation")
ROUTE2927.setToNode("hanim_humanoid_root")

Group2848.addChildren(ROUTE2927)
ROUTE2928 = ROUTE()
ROUTE2928.setFromField("value_changed")
ROUTE2928.setFromNode("Kick_whole_body_TranslationInterpolator")
ROUTE2928.setToField("translation")
ROUTE2928.setToNode("hanim_humanoid_root")

Group2848.addChildren(ROUTE2928)
ROUTE2929 = ROUTE()
ROUTE2929.setFromField("value_changed")
ROUTE2929.setFromNode("Kick_neck_RotationInterpolator")
ROUTE2929.setToField("rotation")
ROUTE2929.setToNode("hanim_vc4")

Group2848.addChildren(ROUTE2929)

Scene31.addChildren(Group2848)
Group2930 = Group()
Group2930.setDEF("UserInterface")
#Authoring hint: these axes are aligned within local coordinate system
Transform2931 = Transform()
Transform2931.setDEF("CoordinateAxesAdjustedScale")
Transform2931.setScale([0.175,0.175,0.175])
Inline2932 = Inline()
Inline2932.setDEF("CoordinateAxes")
Inline2932.setUrl(["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl"])

Transform2931.addChildren(Inline2932)

Group2930.addChildren(Transform2931)
Transform2933 = Transform()
Transform2933.setDEF("cordsys")
Transform2933.setScale([0.175,0.175,0.175])
#<Inline bboxCenter='0.05143541 0.07883984 0.04731131' bboxSize='2.202872 2.25768 2.194624' url='\"JointCoordinateAxes.x3dv\"'/>

Group2930.addChildren(Transform2933)
ProximitySensor2934 = ProximitySensor()
ProximitySensor2934.setDEF("HudProximitySensor")
ProximitySensor2934.setCenter([0,20,0])
ProximitySensor2934.setSize([500,100,500])

Group2930.addChildren(ProximitySensor2934)
Transform2935 = Transform()
Transform2935.setDEF("Stage")
Transform2935.setScale([1,0.0125,1])
Transform2935.setTranslation([0,-0.0125,0])
Shape2936 = Shape()
Appearance2937 = Appearance()
Material2938 = Material()
Material2938.setTransparency(0.6)

Appearance2937.setMaterial(Material2938)

Shape2936.setAppearance(Appearance2937)
Box2939 = Box()

Shape2936.setGeometry(Box2939)

Transform2935.addChildren(Shape2936)
Transform2940 = Transform()
Transform2940.setDEF("Circle0")
Transform2940.setScale([1.175,1,1.175])
Shape2941 = Shape()
Appearance2942 = Appearance()
Material2943 = Material()
Material2943.setDiffuseColor([0.9,0,0.7])
Material2943.setEmissiveColor([0.424956,0.483976,1])

Appearance2942.setMaterial(Material2943)

Shape2941.setAppearance(Appearance2942)
IndexedLineSet2944 = IndexedLineSet()
IndexedLineSet2944.setDEF("Orbit1")
IndexedLineSet2944.setCoordIndex([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,-1])
Coordinate2945 = Coordinate()
Coordinate2945.setPoint([1,0,0,0.995,0,-0.105,0.979,0,-0.208,0.951,0,-0.309,0.914,0,-0.407,0.866,0,-0.5,0.809,0,-0.588,0.743,0,-0.669,0.669,0,-0.743,0.588,0,-0.809,0.5,0,-0.866,0.407,0,-0.914,0.309,0,-0.951,0.208,0,-0.978,0.105,0,-0.995,0,0,-1,-0.105,0,-0.994522,-0.208,0,-0.978,-0.309,0,-0.951,-0.407,0,-0.914,-0.5,0,-0.866,-0.588,0,-0.809,-0.669,0,-0.743,-0.743,0,-0.669,-0.809,0,-0.588,-0.866,0,-0.5,-0.914,0,-0.407,-0.951,0,-0.309,-0.978,0,-0.208,-0.995,0,-0.105,-1,0,0,-0.995,0,0.105,-0.978,0,0.208,-0.951,0,0.309,-0.914,0,0.407,-0.866,0,0.5,-0.809,0,0.588,-0.743,0,0.669,-0.669,0,0.743,-0.588,0,0.809,-0.5,0,0.866,-0.407,0,0.914,-0.309,0,0.951,-0.208,0,0.978,-0.105,0,0.995,0,0,1,0.105,0,0.995,0.208,0,0.978,0.309,0,0.951,0.407,0,0.914,0.5,0,0.866,0.588,0,0.809,0.669,0,0.743,0.743,0,0.669,0.809,0,0.588,0.866,0,0.5,0.914,0,0.407,0.951,0,0.309,0.978,0,0.208,0.995,0,0.104,1,0,0])

IndexedLineSet2944.setCoord(Coordinate2945)

Shape2941.setGeometry(IndexedLineSet2944)

Transform2940.addChildren(Shape2941)

Transform2935.addChildren(Transform2940)
Transform2946 = Transform()
Transform2946.setDEF("Circle1")
Transform2946.setScale([0.5,1,0.5])
Shape2947 = Shape()
Appearance2948 = Appearance()
Material2949 = Material()
Material2949.setDiffuseColor([0.9,0,0.7])
Material2949.setEmissiveColor([0.424956,0.483976,1])

Appearance2948.setMaterial(Material2949)

Shape2947.setAppearance(Appearance2948)
IndexedLineSet2950 = IndexedLineSet()
IndexedLineSet2950.setUSE("Orbit1")

Shape2947.setGeometry(IndexedLineSet2950)

Transform2946.addChildren(Shape2947)

Transform2935.addChildren(Transform2946)
Transform2951 = Transform()
Transform2951.setDEF("Circle2")
Transform2951.setScale([0.25,1,0.25])
Shape2952 = Shape()
Appearance2953 = Appearance()
Material2954 = Material()
Material2954.setDiffuseColor([0.9,0,0.7])
Material2954.setEmissiveColor([0.424956,0.483976,1])

Appearance2953.setMaterial(Material2954)

Shape2952.setAppearance(Appearance2953)
IndexedLineSet2955 = IndexedLineSet()
IndexedLineSet2955.setUSE("Orbit1")

Shape2952.setGeometry(IndexedLineSet2955)

Transform2951.addChildren(Shape2952)

Transform2935.addChildren(Transform2951)

Group2930.addChildren(Transform2935)
Transform2956 = Transform()
Transform2956.setDEF("HudXform")
Transform2956.setRotation([-0.09996068,0.9942513,0.03837026,0.7131352])
Transform2956.setTranslation([1.705442,1.042139,1.989742])
Transform2957 = Transform()
Transform2957.setScale([0.035,0.035,0.035])
Transform2957.setTranslation([-0.42,-0.2,-0.75])
Transform2958 = Transform()
Transform2958.setDEF("StandTransform")
Transform2958.setTranslation([0,-1,0])
TouchSensor2959 = TouchSensor()
TouchSensor2959.setDEF("Stand_Touch")
TouchSensor2959.setDescription("touch to select")

Transform2958.addChildren(TouchSensor2959)
Shape2960 = Shape()
Shape2960.setDEF("StandTextShape")
Appearance2961 = Appearance()
Material2962 = Material()
Material2962.setDEF("text_color")
Material2962.setAmbientIntensity(1)
Material2962.setDiffuseColor([0.819,0.521,0.169])
Material2962.setEmissiveColor([0.819,0.521,0.169])
Material2962.setSpecularColor([0.819,0.521,0.169])

Appearance2961.setMaterial(Material2962)

Shape2960.setAppearance(Appearance2961)
Text2963 = Text()
Text2963.setString(["Stand"])

Shape2960.setGeometry(Text2963)

Transform2958.addChildren(Shape2960)
Shape2964 = Shape()
Shape2964.setDEF("Stand_Back")
Appearance2965 = Appearance()
Material2966 = Material()
Material2966.setDEF("Clear")
Material2966.setAmbientIntensity(1)
Material2966.setDiffuseColor([0,0.5,0])
Material2966.setEmissiveColor([0,0.5,0])
Material2966.setTransparency(0.8)

Appearance2965.setMaterial(Material2966)

Shape2964.setAppearance(Appearance2965)
IndexedFaceSet2967 = IndexedFaceSet()
IndexedFaceSet2967.setDEF("Backing")
IndexedFaceSet2967.setCoordIndex([0,1,2,3,-1])
Coordinate2968 = Coordinate()
Coordinate2968.setPoint([-0.2,-1.2,-0.01,2.5,-1.2,-0.01,2.5,0.75,-0.01,-0.2,0.75,-0.01])

IndexedFaceSet2967.setCoord(Coordinate2968)

Shape2964.setGeometry(IndexedFaceSet2967)

Transform2958.addChildren(Shape2964)

Transform2957.addChildren(Transform2958)
Transform2969 = Transform()
Transform2969.setDEF("PitchTransform")
Transform2969.setTranslation([3,-1,0])
TouchSensor2970 = TouchSensor()
TouchSensor2970.setDEF("Pitch_Touch")
TouchSensor2970.setDescription("touch to select")

Transform2969.addChildren(TouchSensor2970)
Shape2971 = Shape()
Shape2971.setDEF("PitchTextShape")
Appearance2972 = Appearance()
Material2973 = Material()
Material2973.setUSE("text_color")

Appearance2972.setMaterial(Material2973)

Shape2971.setAppearance(Appearance2972)
Text2974 = Text()
Text2974.setString(["Pitch"])

Shape2971.setGeometry(Text2974)

Transform2969.addChildren(Shape2971)
Shape2975 = Shape()
Shape2975.setDEF("Pitch_Back")
Appearance2976 = Appearance()
Material2977 = Material()
Material2977.setUSE("Clear")

Appearance2976.setMaterial(Material2977)

Shape2975.setAppearance(Appearance2976)
IndexedFaceSet2978 = IndexedFaceSet()
IndexedFaceSet2978.setUSE("Backing")

Shape2975.setGeometry(IndexedFaceSet2978)

Transform2969.addChildren(Shape2975)

Transform2957.addChildren(Transform2969)
Transform2979 = Transform()
Transform2979.setDEF("YawTransform")
Transform2979.setTranslation([6,-1,0])
TouchSensor2980 = TouchSensor()
TouchSensor2980.setDEF("Yaw_Touch")
TouchSensor2980.setDescription("touch to select")

Transform2979.addChildren(TouchSensor2980)
Shape2981 = Shape()
Shape2981.setDEF("YawText")
Appearance2982 = Appearance()
Material2983 = Material()
Material2983.setUSE("text_color")

Appearance2982.setMaterial(Material2983)

Shape2981.setAppearance(Appearance2982)
Text2984 = Text()
Text2984.setString(["Yaw"])

Shape2981.setGeometry(Text2984)

Transform2979.addChildren(Shape2981)
Shape2985 = Shape()
Shape2985.setDEF("Yaw_Back")
Appearance2986 = Appearance()
Material2987 = Material()
Material2987.setUSE("Clear")

Appearance2986.setMaterial(Material2987)

Shape2985.setAppearance(Appearance2986)
IndexedFaceSet2988 = IndexedFaceSet()
IndexedFaceSet2988.setUSE("Backing")

Shape2985.setGeometry(IndexedFaceSet2988)

Transform2979.addChildren(Shape2985)

Transform2957.addChildren(Transform2979)
Transform2989 = Transform()
Transform2989.setDEF("RollTransform")
Transform2989.setTranslation([9,-1,0])
TouchSensor2990 = TouchSensor()
TouchSensor2990.setDEF("Roll_Touch")
TouchSensor2990.setDescription("touch to select")

Transform2989.addChildren(TouchSensor2990)
Shape2991 = Shape()
Shape2991.setDEF("_RollInterpolator")
Appearance2992 = Appearance()
Material2993 = Material()
Material2993.setUSE("text_color")

Appearance2992.setMaterial(Material2993)

Shape2991.setAppearance(Appearance2992)
Text2994 = Text()
Text2994.setString(["Roll"])

Shape2991.setGeometry(Text2994)

Transform2989.addChildren(Shape2991)
Shape2995 = Shape()
Shape2995.setDEF("Roll_Back")
Appearance2996 = Appearance()
Material2997 = Material()
Material2997.setUSE("Clear")

Appearance2996.setMaterial(Material2997)

Shape2995.setAppearance(Appearance2996)
IndexedFaceSet2998 = IndexedFaceSet()
IndexedFaceSet2998.setUSE("Backing")

Shape2995.setGeometry(IndexedFaceSet2998)

Transform2989.addChildren(Shape2995)

Transform2957.addChildren(Transform2989)
Transform2999 = Transform()
Transform2999.setDEF("WalkTransform")
Transform2999.setTranslation([12,-1,0])
TouchSensor3000 = TouchSensor()
TouchSensor3000.setDEF("Walk_Touch")
TouchSensor3000.setDescription("touch to select")

Transform2999.addChildren(TouchSensor3000)
Shape3001 = Shape()
Shape3001.setDEF("WalkText")
Appearance3002 = Appearance()
Material3003 = Material()
Material3003.setUSE("text_color")

Appearance3002.setMaterial(Material3003)

Shape3001.setAppearance(Appearance3002)
Text3004 = Text()
Text3004.setString(["Walk"])

Shape3001.setGeometry(Text3004)

Transform2999.addChildren(Shape3001)
Shape3005 = Shape()
Shape3005.setDEF("Walk_Back")
Appearance3006 = Appearance()
Material3007 = Material()
Material3007.setUSE("Clear")

Appearance3006.setMaterial(Material3007)

Shape3005.setAppearance(Appearance3006)
IndexedFaceSet3008 = IndexedFaceSet()
IndexedFaceSet3008.setUSE("Backing")

Shape3005.setGeometry(IndexedFaceSet3008)

Transform2999.addChildren(Shape3005)

Transform2957.addChildren(Transform2999)
Transform3009 = Transform()
Transform3009.setDEF("RunTransform")
Transform3009.setTranslation([15,-1,0])
TouchSensor3010 = TouchSensor()
TouchSensor3010.setDEF("Run_Touch")
TouchSensor3010.setDescription("touch to select")

Transform3009.addChildren(TouchSensor3010)
Shape3011 = Shape()
Shape3011.setDEF("RunText")
Appearance3012 = Appearance()
Material3013 = Material()
Material3013.setUSE("text_color")

Appearance3012.setMaterial(Material3013)

Shape3011.setAppearance(Appearance3012)
Text3014 = Text()
Text3014.setString(["Run"])

Shape3011.setGeometry(Text3014)

Transform3009.addChildren(Shape3011)
Shape3015 = Shape()
Shape3015.setDEF("Run_Back")
Appearance3016 = Appearance()
Material3017 = Material()
Material3017.setUSE("Clear")

Appearance3016.setMaterial(Material3017)

Shape3015.setAppearance(Appearance3016)
IndexedFaceSet3018 = IndexedFaceSet()
IndexedFaceSet3018.setUSE("Backing")

Shape3015.setGeometry(IndexedFaceSet3018)

Transform3009.addChildren(Shape3015)

Transform2957.addChildren(Transform3009)
Transform3019 = Transform()
Transform3019.setDEF("JumpTransform")
Transform3019.setTranslation([18,-1,0])
TouchSensor3020 = TouchSensor()
TouchSensor3020.setDEF("Jump_Touch")
TouchSensor3020.setDescription("touch to select")

Transform3019.addChildren(TouchSensor3020)
Shape3021 = Shape()
Shape3021.setDEF("Jump")
Appearance3022 = Appearance()
Material3023 = Material()
Material3023.setUSE("text_color")

Appearance3022.setMaterial(Material3023)

Shape3021.setAppearance(Appearance3022)
Text3024 = Text()
Text3024.setString(["Jump"])

Shape3021.setGeometry(Text3024)

Transform3019.addChildren(Shape3021)
Shape3025 = Shape()
Shape3025.setDEF("Jump_Back")
Appearance3026 = Appearance()
Material3027 = Material()
Material3027.setUSE("Clear")

Appearance3026.setMaterial(Material3027)

Shape3025.setAppearance(Appearance3026)
IndexedFaceSet3028 = IndexedFaceSet()
IndexedFaceSet3028.setUSE("Backing")

Shape3025.setGeometry(IndexedFaceSet3028)

Transform3019.addChildren(Shape3025)

Transform2957.addChildren(Transform3019)
Transform3029 = Transform()
Transform3029.setDEF("KickTransform")
Transform3029.setTranslation([21,-1,0])
TouchSensor3030 = TouchSensor()
TouchSensor3030.setDEF("Kick_Touch")
TouchSensor3030.setDescription("touch to select")

Transform3029.addChildren(TouchSensor3030)
Shape3031 = Shape()
Shape3031.setDEF("KickText")
Appearance3032 = Appearance()
Material3033 = Material()
Material3033.setUSE("text_color")

Appearance3032.setMaterial(Material3033)

Shape3031.setAppearance(Appearance3032)
Text3034 = Text()
Text3034.setString(["Kick"])

Shape3031.setGeometry(Text3034)

Transform3029.addChildren(Shape3031)
Shape3035 = Shape()
Shape3035.setDEF("Kick_Back")
Appearance3036 = Appearance()
Material3037 = Material()
Material3037.setUSE("Clear")

Appearance3036.setMaterial(Material3037)

Shape3035.setAppearance(Appearance3036)
IndexedFaceSet3038 = IndexedFaceSet()
IndexedFaceSet3038.setUSE("Backing")

Shape3035.setGeometry(IndexedFaceSet3038)

Transform3029.addChildren(Shape3035)

Transform2957.addChildren(Transform3029)
Transform3039 = Transform()
Transform3039.setDEF("Stop_Text")
Transform3039.setTranslation([0,1.4,0])
TouchSensor3040 = TouchSensor()
TouchSensor3040.setDEF("Stop_Touch")
TouchSensor3040.setDescription("touch to select")

Transform3039.addChildren(TouchSensor3040)
Shape3041 = Shape()
Shape3041.setDEF("StopText")
Appearance3042 = Appearance()
Material3043 = Material()
Material3043.setUSE("text_color")

Appearance3042.setMaterial(Material3043)

Shape3041.setAppearance(Appearance3042)
Text3044 = Text()
Text3044.setString(["Stop","Default Pose"])

Shape3041.setGeometry(Text3044)

Transform3039.addChildren(Shape3041)
Shape3045 = Shape()
Shape3045.setDEF("Stop_Back")
Appearance3046 = Appearance()
Material3047 = Material()
Material3047.setUSE("Clear")

Appearance3046.setMaterial(Material3047)

Shape3045.setAppearance(Appearance3046)
IndexedFaceSet3048 = IndexedFaceSet()
IndexedFaceSet3048.setUSE("Backing")

Shape3045.setGeometry(IndexedFaceSet3048)

Transform3039.addChildren(Shape3045)

Transform2957.addChildren(Transform3039)

Transform2956.addChildren(Transform2957)

Group2930.addChildren(Transform2956)
ROUTE3049 = ROUTE()
ROUTE3049.setFromField("position_changed")
ROUTE3049.setFromNode("HudProximitySensor")
ROUTE3049.setToField("translation")
ROUTE3049.setToNode("HudXform")

Group2930.addChildren(ROUTE3049)
ROUTE3050 = ROUTE()
ROUTE3050.setFromField("orientation_changed")
ROUTE3050.setFromNode("HudProximitySensor")
ROUTE3050.setToField("rotation")
ROUTE3050.setToNode("HudXform")

Group2930.addChildren(ROUTE3050)

Scene31.addChildren(Group2930)
Group3051 = Group()
Group3051.setDEF("BehaviorSynchronization")
ROUTE3052 = ROUTE()
ROUTE3052.setFromField("touchTime")
ROUTE3052.setFromNode("Stand_Touch")
ROUTE3052.setToField("stopTime")
ROUTE3052.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3052)
ROUTE3053 = ROUTE()
ROUTE3053.setFromField("touchTime")
ROUTE3053.setFromNode("Stand_Touch")
ROUTE3053.setToField("stopTime")
ROUTE3053.setToNode("YawTimer")

Group3051.addChildren(ROUTE3053)
ROUTE3054 = ROUTE()
ROUTE3054.setFromField("touchTime")
ROUTE3054.setFromNode("Stand_Touch")
ROUTE3054.setToField("stopTime")
ROUTE3054.setToNode("RollTimer")

Group3051.addChildren(ROUTE3054)
ROUTE3055 = ROUTE()
ROUTE3055.setFromField("touchTime")
ROUTE3055.setFromNode("Stand_Touch")
ROUTE3055.setToField("stopTime")
ROUTE3055.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3055)
ROUTE3056 = ROUTE()
ROUTE3056.setFromField("touchTime")
ROUTE3056.setFromNode("Stand_Touch")
ROUTE3056.setToField("stopTime")
ROUTE3056.setToNode("RunTimer")

Group3051.addChildren(ROUTE3056)
ROUTE3057 = ROUTE()
ROUTE3057.setFromField("touchTime")
ROUTE3057.setFromNode("Stand_Touch")
ROUTE3057.setToField("stopTime")
ROUTE3057.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3057)
ROUTE3058 = ROUTE()
ROUTE3058.setFromField("touchTime")
ROUTE3058.setFromNode("Stand_Touch")
ROUTE3058.setToField("stopTime")
ROUTE3058.setToNode("KickTimer")

Group3051.addChildren(ROUTE3058)
ROUTE3059 = ROUTE()
ROUTE3059.setFromField("touchTime")
ROUTE3059.setFromNode("Stand_Touch")
ROUTE3059.setToField("stopTime")
ROUTE3059.setToNode("StopTimer")

Group3051.addChildren(ROUTE3059)
ROUTE3060 = ROUTE()
ROUTE3060.setFromField("touchTime")
ROUTE3060.setFromNode("Stand_Touch")
ROUTE3060.setToField("startTime")
ROUTE3060.setToNode("StandTimer")

Group3051.addChildren(ROUTE3060)
ROUTE3061 = ROUTE()
ROUTE3061.setFromField("touchTime")
ROUTE3061.setFromNode("Pitch_Touch")
ROUTE3061.setToField("stopTime")
ROUTE3061.setToNode("StandTimer")

Group3051.addChildren(ROUTE3061)
ROUTE3062 = ROUTE()
ROUTE3062.setFromField("touchTime")
ROUTE3062.setFromNode("Pitch_Touch")
ROUTE3062.setToField("stopTime")
ROUTE3062.setToNode("YawTimer")

Group3051.addChildren(ROUTE3062)
ROUTE3063 = ROUTE()
ROUTE3063.setFromField("touchTime")
ROUTE3063.setFromNode("Pitch_Touch")
ROUTE3063.setToField("stopTime")
ROUTE3063.setToNode("RollTimer")

Group3051.addChildren(ROUTE3063)
ROUTE3064 = ROUTE()
ROUTE3064.setFromField("touchTime")
ROUTE3064.setFromNode("Pitch_Touch")
ROUTE3064.setToField("stopTime")
ROUTE3064.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3064)
ROUTE3065 = ROUTE()
ROUTE3065.setFromField("touchTime")
ROUTE3065.setFromNode("Pitch_Touch")
ROUTE3065.setToField("stopTime")
ROUTE3065.setToNode("RunTimer")

Group3051.addChildren(ROUTE3065)
ROUTE3066 = ROUTE()
ROUTE3066.setFromField("touchTime")
ROUTE3066.setFromNode("Pitch_Touch")
ROUTE3066.setToField("stopTime")
ROUTE3066.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3066)
ROUTE3067 = ROUTE()
ROUTE3067.setFromField("touchTime")
ROUTE3067.setFromNode("Pitch_Touch")
ROUTE3067.setToField("stopTime")
ROUTE3067.setToNode("KickTimer")

Group3051.addChildren(ROUTE3067)
ROUTE3068 = ROUTE()
ROUTE3068.setFromField("touchTime")
ROUTE3068.setFromNode("Pitch_Touch")
ROUTE3068.setToField("stopTime")
ROUTE3068.setToNode("StopTimer")

Group3051.addChildren(ROUTE3068)
ROUTE3069 = ROUTE()
ROUTE3069.setFromField("touchTime")
ROUTE3069.setFromNode("Pitch_Touch")
ROUTE3069.setToField("startTime")
ROUTE3069.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3069)
ROUTE3070 = ROUTE()
ROUTE3070.setFromField("touchTime")
ROUTE3070.setFromNode("Yaw_Touch")
ROUTE3070.setToField("stopTime")
ROUTE3070.setToNode("StandTimer")

Group3051.addChildren(ROUTE3070)
ROUTE3071 = ROUTE()
ROUTE3071.setFromField("touchTime")
ROUTE3071.setFromNode("Yaw_Touch")
ROUTE3071.setToField("stopTime")
ROUTE3071.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3071)
ROUTE3072 = ROUTE()
ROUTE3072.setFromField("touchTime")
ROUTE3072.setFromNode("Yaw_Touch")
ROUTE3072.setToField("stopTime")
ROUTE3072.setToNode("RollTimer")

Group3051.addChildren(ROUTE3072)
ROUTE3073 = ROUTE()
ROUTE3073.setFromField("touchTime")
ROUTE3073.setFromNode("Yaw_Touch")
ROUTE3073.setToField("stopTime")
ROUTE3073.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3073)
ROUTE3074 = ROUTE()
ROUTE3074.setFromField("touchTime")
ROUTE3074.setFromNode("Yaw_Touch")
ROUTE3074.setToField("stopTime")
ROUTE3074.setToNode("RunTimer")

Group3051.addChildren(ROUTE3074)
ROUTE3075 = ROUTE()
ROUTE3075.setFromField("touchTime")
ROUTE3075.setFromNode("Yaw_Touch")
ROUTE3075.setToField("stopTime")
ROUTE3075.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3075)
ROUTE3076 = ROUTE()
ROUTE3076.setFromField("touchTime")
ROUTE3076.setFromNode("Yaw_Touch")
ROUTE3076.setToField("stopTime")
ROUTE3076.setToNode("KickTimer")

Group3051.addChildren(ROUTE3076)
ROUTE3077 = ROUTE()
ROUTE3077.setFromField("touchTime")
ROUTE3077.setFromNode("Yaw_Touch")
ROUTE3077.setToField("stopTime")
ROUTE3077.setToNode("StopTimer")

Group3051.addChildren(ROUTE3077)
ROUTE3078 = ROUTE()
ROUTE3078.setFromField("touchTime")
ROUTE3078.setFromNode("Yaw_Touch")
ROUTE3078.setToField("startTime")
ROUTE3078.setToNode("YawTimer")

Group3051.addChildren(ROUTE3078)
ROUTE3079 = ROUTE()
ROUTE3079.setFromField("touchTime")
ROUTE3079.setFromNode("Walk_Touch")
ROUTE3079.setToField("stopTime")
ROUTE3079.setToNode("StandTimer")

Group3051.addChildren(ROUTE3079)
ROUTE3080 = ROUTE()
ROUTE3080.setFromField("touchTime")
ROUTE3080.setFromNode("Walk_Touch")
ROUTE3080.setToField("stopTime")
ROUTE3080.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3080)
ROUTE3081 = ROUTE()
ROUTE3081.setFromField("touchTime")
ROUTE3081.setFromNode("Walk_Touch")
ROUTE3081.setToField("stopTime")
ROUTE3081.setToNode("YawTimer")

Group3051.addChildren(ROUTE3081)
ROUTE3082 = ROUTE()
ROUTE3082.setFromField("touchTime")
ROUTE3082.setFromNode("Walk_Touch")
ROUTE3082.setToField("stopTime")
ROUTE3082.setToNode("RollTimer")

Group3051.addChildren(ROUTE3082)
ROUTE3083 = ROUTE()
ROUTE3083.setFromField("touchTime")
ROUTE3083.setFromNode("Walk_Touch")
ROUTE3083.setToField("stopTime")
ROUTE3083.setToNode("RunTimer")

Group3051.addChildren(ROUTE3083)
ROUTE3084 = ROUTE()
ROUTE3084.setFromField("touchTime")
ROUTE3084.setFromNode("Walk_Touch")
ROUTE3084.setToField("stopTime")
ROUTE3084.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3084)
ROUTE3085 = ROUTE()
ROUTE3085.setFromField("touchTime")
ROUTE3085.setFromNode("Walk_Touch")
ROUTE3085.setToField("stopTime")
ROUTE3085.setToNode("KickTimer")

Group3051.addChildren(ROUTE3085)
ROUTE3086 = ROUTE()
ROUTE3086.setFromField("touchTime")
ROUTE3086.setFromNode("Walk_Touch")
ROUTE3086.setToField("stopTime")
ROUTE3086.setToNode("StopTimer")

Group3051.addChildren(ROUTE3086)
ROUTE3087 = ROUTE()
ROUTE3087.setFromField("touchTime")
ROUTE3087.setFromNode("Walk_Touch")
ROUTE3087.setToField("startTime")
ROUTE3087.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3087)
ROUTE3088 = ROUTE()
ROUTE3088.setFromField("touchTime")
ROUTE3088.setFromNode("Roll_Touch")
ROUTE3088.setToField("stopTime")
ROUTE3088.setToNode("StandTimer")

Group3051.addChildren(ROUTE3088)
ROUTE3089 = ROUTE()
ROUTE3089.setFromField("touchTime")
ROUTE3089.setFromNode("Roll_Touch")
ROUTE3089.setToField("stopTime")
ROUTE3089.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3089)
ROUTE3090 = ROUTE()
ROUTE3090.setFromField("touchTime")
ROUTE3090.setFromNode("Roll_Touch")
ROUTE3090.setToField("stopTime")
ROUTE3090.setToNode("YawTimer")

Group3051.addChildren(ROUTE3090)
ROUTE3091 = ROUTE()
ROUTE3091.setFromField("touchTime")
ROUTE3091.setFromNode("Roll_Touch")
ROUTE3091.setToField("stopTime")
ROUTE3091.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3091)
ROUTE3092 = ROUTE()
ROUTE3092.setFromField("touchTime")
ROUTE3092.setFromNode("Roll_Touch")
ROUTE3092.setToField("stopTime")
ROUTE3092.setToNode("RunTimer")

Group3051.addChildren(ROUTE3092)
ROUTE3093 = ROUTE()
ROUTE3093.setFromField("touchTime")
ROUTE3093.setFromNode("Roll_Touch")
ROUTE3093.setToField("stopTime")
ROUTE3093.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3093)
ROUTE3094 = ROUTE()
ROUTE3094.setFromField("touchTime")
ROUTE3094.setFromNode("Roll_Touch")
ROUTE3094.setToField("stopTime")
ROUTE3094.setToNode("KickTimer")

Group3051.addChildren(ROUTE3094)
ROUTE3095 = ROUTE()
ROUTE3095.setFromField("touchTime")
ROUTE3095.setFromNode("Roll_Touch")
ROUTE3095.setToField("stopTime")
ROUTE3095.setToNode("StopTimer")

Group3051.addChildren(ROUTE3095)
ROUTE3096 = ROUTE()
ROUTE3096.setFromField("touchTime")
ROUTE3096.setFromNode("Roll_Touch")
ROUTE3096.setToField("startTime")
ROUTE3096.setToNode("RollTimer")

Group3051.addChildren(ROUTE3096)
ROUTE3097 = ROUTE()
ROUTE3097.setFromField("touchTime")
ROUTE3097.setFromNode("Run_Touch")
ROUTE3097.setToField("stopTime")
ROUTE3097.setToNode("StandTimer")

Group3051.addChildren(ROUTE3097)
ROUTE3098 = ROUTE()
ROUTE3098.setFromField("touchTime")
ROUTE3098.setFromNode("Run_Touch")
ROUTE3098.setToField("stopTime")
ROUTE3098.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3098)
ROUTE3099 = ROUTE()
ROUTE3099.setFromField("touchTime")
ROUTE3099.setFromNode("Run_Touch")
ROUTE3099.setToField("stopTime")
ROUTE3099.setToNode("YawTimer")

Group3051.addChildren(ROUTE3099)
ROUTE3100 = ROUTE()
ROUTE3100.setFromField("touchTime")
ROUTE3100.setFromNode("Run_Touch")
ROUTE3100.setToField("stopTime")
ROUTE3100.setToNode("RollTimer")

Group3051.addChildren(ROUTE3100)
ROUTE3101 = ROUTE()
ROUTE3101.setFromField("touchTime")
ROUTE3101.setFromNode("Run_Touch")
ROUTE3101.setToField("stopTime")
ROUTE3101.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3101)
ROUTE3102 = ROUTE()
ROUTE3102.setFromField("touchTime")
ROUTE3102.setFromNode("Run_Touch")
ROUTE3102.setToField("stopTime")
ROUTE3102.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3102)
ROUTE3103 = ROUTE()
ROUTE3103.setFromField("touchTime")
ROUTE3103.setFromNode("Run_Touch")
ROUTE3103.setToField("stopTime")
ROUTE3103.setToNode("KickTimer")

Group3051.addChildren(ROUTE3103)
ROUTE3104 = ROUTE()
ROUTE3104.setFromField("touchTime")
ROUTE3104.setFromNode("Run_Touch")
ROUTE3104.setToField("stopTime")
ROUTE3104.setToNode("StopTimer")

Group3051.addChildren(ROUTE3104)
ROUTE3105 = ROUTE()
ROUTE3105.setFromField("touchTime")
ROUTE3105.setFromNode("Run_Touch")
ROUTE3105.setToField("startTime")
ROUTE3105.setToNode("RunTimer")

Group3051.addChildren(ROUTE3105)
ROUTE3106 = ROUTE()
ROUTE3106.setFromField("touchTime")
ROUTE3106.setFromNode("Jump_Touch")
ROUTE3106.setToField("stopTime")
ROUTE3106.setToNode("StandTimer")

Group3051.addChildren(ROUTE3106)
ROUTE3107 = ROUTE()
ROUTE3107.setFromField("touchTime")
ROUTE3107.setFromNode("Jump_Touch")
ROUTE3107.setToField("stopTime")
ROUTE3107.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3107)
ROUTE3108 = ROUTE()
ROUTE3108.setFromField("touchTime")
ROUTE3108.setFromNode("Jump_Touch")
ROUTE3108.setToField("stopTime")
ROUTE3108.setToNode("YawTimer")

Group3051.addChildren(ROUTE3108)
ROUTE3109 = ROUTE()
ROUTE3109.setFromField("touchTime")
ROUTE3109.setFromNode("Jump_Touch")
ROUTE3109.setToField("stopTime")
ROUTE3109.setToNode("RollTimer")

Group3051.addChildren(ROUTE3109)
ROUTE3110 = ROUTE()
ROUTE3110.setFromField("touchTime")
ROUTE3110.setFromNode("Jump_Touch")
ROUTE3110.setToField("stopTime")
ROUTE3110.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3110)
ROUTE3111 = ROUTE()
ROUTE3111.setFromField("touchTime")
ROUTE3111.setFromNode("Jump_Touch")
ROUTE3111.setToField("stopTime")
ROUTE3111.setToNode("RunTimer")

Group3051.addChildren(ROUTE3111)
ROUTE3112 = ROUTE()
ROUTE3112.setFromField("touchTime")
ROUTE3112.setFromNode("Jump_Touch")
ROUTE3112.setToField("stopTime")
ROUTE3112.setToNode("KickTimer")

Group3051.addChildren(ROUTE3112)
ROUTE3113 = ROUTE()
ROUTE3113.setFromField("touchTime")
ROUTE3113.setFromNode("Jump_Touch")
ROUTE3113.setToField("stopTime")
ROUTE3113.setToNode("StopTimer")

Group3051.addChildren(ROUTE3113)
ROUTE3114 = ROUTE()
ROUTE3114.setFromField("touchTime")
ROUTE3114.setFromNode("Jump_Touch")
ROUTE3114.setToField("startTime")
ROUTE3114.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3114)
ROUTE3115 = ROUTE()
ROUTE3115.setFromField("touchTime")
ROUTE3115.setFromNode("Kick_Touch")
ROUTE3115.setToField("stopTime")
ROUTE3115.setToNode("StandTimer")

Group3051.addChildren(ROUTE3115)
ROUTE3116 = ROUTE()
ROUTE3116.setFromField("touchTime")
ROUTE3116.setFromNode("Kick_Touch")
ROUTE3116.setToField("stopTime")
ROUTE3116.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3116)
ROUTE3117 = ROUTE()
ROUTE3117.setFromField("touchTime")
ROUTE3117.setFromNode("Kick_Touch")
ROUTE3117.setToField("stopTime")
ROUTE3117.setToNode("YawTimer")

Group3051.addChildren(ROUTE3117)
ROUTE3118 = ROUTE()
ROUTE3118.setFromField("touchTime")
ROUTE3118.setFromNode("Kick_Touch")
ROUTE3118.setToField("stopTime")
ROUTE3118.setToNode("RollTimer")

Group3051.addChildren(ROUTE3118)
ROUTE3119 = ROUTE()
ROUTE3119.setFromField("touchTime")
ROUTE3119.setFromNode("Kick_Touch")
ROUTE3119.setToField("stopTime")
ROUTE3119.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3119)
ROUTE3120 = ROUTE()
ROUTE3120.setFromField("touchTime")
ROUTE3120.setFromNode("Kick_Touch")
ROUTE3120.setToField("stopTime")
ROUTE3120.setToNode("RunTimer")

Group3051.addChildren(ROUTE3120)
ROUTE3121 = ROUTE()
ROUTE3121.setFromField("touchTime")
ROUTE3121.setFromNode("Kick_Touch")
ROUTE3121.setToField("stopTime")
ROUTE3121.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3121)
ROUTE3122 = ROUTE()
ROUTE3122.setFromField("touchTime")
ROUTE3122.setFromNode("Kick_Touch")
ROUTE3122.setToField("stopTime")
ROUTE3122.setToNode("StopTimer")

Group3051.addChildren(ROUTE3122)
ROUTE3123 = ROUTE()
ROUTE3123.setFromField("touchTime")
ROUTE3123.setFromNode("Kick_Touch")
ROUTE3123.setToField("startTime")
ROUTE3123.setToNode("KickTimer")

Group3051.addChildren(ROUTE3123)
ROUTE3124 = ROUTE()
ROUTE3124.setFromField("touchTime")
ROUTE3124.setFromNode("Stop_Touch")
ROUTE3124.setToField("stopTime")
ROUTE3124.setToNode("StandTimer")

Group3051.addChildren(ROUTE3124)
ROUTE3125 = ROUTE()
ROUTE3125.setFromField("touchTime")
ROUTE3125.setFromNode("Stop_Touch")
ROUTE3125.setToField("stopTime")
ROUTE3125.setToNode("PitchTimer")

Group3051.addChildren(ROUTE3125)
ROUTE3126 = ROUTE()
ROUTE3126.setFromField("touchTime")
ROUTE3126.setFromNode("Stop_Touch")
ROUTE3126.setToField("stopTime")
ROUTE3126.setToNode("YawTimer")

Group3051.addChildren(ROUTE3126)
ROUTE3127 = ROUTE()
ROUTE3127.setFromField("touchTime")
ROUTE3127.setFromNode("Stop_Touch")
ROUTE3127.setToField("stopTime")
ROUTE3127.setToNode("RollTimer")

Group3051.addChildren(ROUTE3127)
ROUTE3128 = ROUTE()
ROUTE3128.setFromField("touchTime")
ROUTE3128.setFromNode("Stop_Touch")
ROUTE3128.setToField("stopTime")
ROUTE3128.setToNode("WalkTimer")

Group3051.addChildren(ROUTE3128)
ROUTE3129 = ROUTE()
ROUTE3129.setFromField("touchTime")
ROUTE3129.setFromNode("Stop_Touch")
ROUTE3129.setToField("stopTime")
ROUTE3129.setToNode("RunTimer")

Group3051.addChildren(ROUTE3129)
ROUTE3130 = ROUTE()
ROUTE3130.setFromField("touchTime")
ROUTE3130.setFromNode("Stop_Touch")
ROUTE3130.setToField("stopTime")
ROUTE3130.setToNode("JumpTimer")

Group3051.addChildren(ROUTE3130)
ROUTE3131 = ROUTE()
ROUTE3131.setFromField("touchTime")
ROUTE3131.setFromNode("Stop_Touch")
ROUTE3131.setToField("stopTime")
ROUTE3131.setToNode("KickTimer")

Group3051.addChildren(ROUTE3131)
ROUTE3132 = ROUTE()
ROUTE3132.setFromField("touchTime")
ROUTE3132.setFromNode("Stop_Touch")
ROUTE3132.setToField("startTime")
ROUTE3132.setToNode("StopTimer")

Group3051.addChildren(ROUTE3132)

Scene31.addChildren(Group3051)

X3D0.setScene(Scene31)
X3D0.toFileX3D("././HAnim1SpecificationLOA3Animation_RoundTrip.x3d")
