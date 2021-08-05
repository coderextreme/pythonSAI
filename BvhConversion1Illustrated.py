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
meta3.setContent("BvhConversion1Illustrated.x3d")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("description")
meta4.setContent("BVH file conversion: test case showing current BVH-to-X3D conversion results of \"invisible\" skeleton, with node visualization geometry later applied from X3dToXhtml stylesheet-produced HumanoidRootHAnimHumanoidReport.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("creator")
meta5.setContent("TODO unknown original creator of file 1.bvh, please advise if known")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("translator")
meta6.setContent("Don Brutzman")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("created")
meta7.setContent("1 January 2016")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("translated")
meta8.setContent("1 January 2018")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("modified")
meta9.setContent("20 February 2021")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("warning")
meta10.setContent("under development, TODO fix transcription of HAnimSite nodes. A few further improvements needed in X3dToXhhtml.xslt HAnim report stylesheet")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("Image")
meta11.setContent("BvhConversion1Illustrated.png")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("reference")
meta12.setContent("BvhConversion1Invisible.html#HumanoidRootHAnimHumanoidReport")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("reference")
meta13.setContent("1.bvh")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("reference")
meta14.setContent("1.bvh.txt")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("Image")
meta15.setContent("1.bvhacker.png")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("reference")
meta16.setContent("http://www.bvhacker.com")

head1.addMeta(meta16)
meta17 = meta()
meta17.setName("reference")
meta17.setContent("BvhSeamless3dExport1.x3d")

head1.addMeta(meta17)
meta18 = meta()
meta18.setName("reference")
meta18.setContent("BvhConversion1Index.html")

head1.addMeta(meta18)
meta19 = meta()
meta19.setName("reference")
meta19.setContent("BvhConversion1InvisibleIndex.html")

head1.addMeta(meta19)
meta20 = meta()
meta20.setName("reference")
meta20.setContent("http://www.character-studio.net/bvh_file_specification.htm")

head1.addMeta(meta20)
meta21 = meta()
meta21.setName("reference")
meta21.setContent("https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#MOCAP")

head1.addMeta(meta21)
meta22 = meta()
meta22.setName("generator")
meta22.setContent("Java BVH to X3D Converter, org.web3d.x3d.hanim.bvh package")

head1.addMeta(meta22)
meta23 = meta()
meta23.setName("generator")
meta23.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta23)
meta24 = meta()
meta24.setName("identifier")
meta24.setContent("https://x3dgraphics.com/examples/X3dForAdvancedModeling/MotionAnimation/BvhConversion1Illustrated.x3d")

head1.addMeta(meta24)
meta25 = meta()
meta25.setName("license")
meta25.setContent("license.html")

head1.addMeta(meta25)

X3D0.setHead(head1)
Scene26 = Scene()
#BVH HIERARCHY size computations: minX=0.0, maxX=0.0, width=0.0; minY=-17.78, maxY=10.16, height=27.94; minZ=0.0, maxZ=15.24, depth=15.24
#Estimated rescaling to meters based on height: scaleFactor=0.01 for modified height of 0.279m
NavigationInfo27 = NavigationInfo()

Scene26.addChildren(NavigationInfo27)
Group28 = Group()
Group28.setDEF("Bvh1_ConversionInformation")
#20 BVH JOINT definitions found, following a single HIERARCHY ROOT
#BVH HIERARCHY model size computations: minX=0.0, maxX=0.0, width=0.0; minY=-17.78, maxY=10.16, height=27.94; minZ=0.0, maxZ=15.24, depth=15.24
#Estimated rescaling to meters based on height: scaleFactor=0.0254 for modified height of 0.710m
#Vertical offset to move bottom of BVH figure to ground plane (adjusted in HAnimJoint containerField='skeleton'): heightOffset=0.451612m
MetadataSet29 = MetadataSet()
MetadataSet29.setName("BvhToHAnimConversionNameTable")
#<MetadataString name='bvhName' reference='bvhType' value='\"name\" \"segmentName\"'/>
MetadataString30 = MetadataString()
MetadataString30.setName("Hips")
MetadataString30.setReference("ROOT")
MetadataString30.setValue(["HumanoidRoot","sacrum"])

MetadataSet29.setValue(MetadataString30)
MetadataString31 = MetadataString()
MetadataString31.setName("LeftHip")
MetadataString31.setReference("JOINT")
MetadataString31.setValue(["l_hip","l_thigh"])

MetadataSet29.addValue(MetadataString31)
MetadataString32 = MetadataString()
MetadataString32.setName("LeftKnee")
MetadataString32.setReference("JOINT")
MetadataString32.setValue(["l_knee","l_calf"])

MetadataSet29.addValue(MetadataString32)
MetadataString33 = MetadataString()
MetadataString33.setName("LeftAnkle")
MetadataString33.setReference("JOINT")
MetadataString33.setValue(["l_ankle","l_hindfoot"])

MetadataSet29.addValue(MetadataString33)
MetadataString34 = MetadataString()
MetadataString34.setName("LeftAnkleEnd")
MetadataString34.setReference("JOINT")
MetadataString34.setValue(["l_midtarsal","l_middistal"])

MetadataSet29.addValue(MetadataString34)
MetadataString35 = MetadataString()
MetadataString35.setName("LeftAnkleEndSite")
MetadataString35.setReference("Site")
MetadataString35.setValue(["l_midtarsal_tip"])

MetadataSet29.addValue(MetadataString35)
MetadataString36 = MetadataString()
MetadataString36.setName("RightHip")
MetadataString36.setReference("JOINT")
MetadataString36.setValue(["r_hip","r_thigh"])

MetadataSet29.addValue(MetadataString36)
MetadataString37 = MetadataString()
MetadataString37.setName("RightKnee")
MetadataString37.setReference("JOINT")
MetadataString37.setValue(["r_knee","r_calf"])

MetadataSet29.addValue(MetadataString37)
MetadataString38 = MetadataString()
MetadataString38.setName("RightAnkle")
MetadataString38.setReference("JOINT")
MetadataString38.setValue(["r_ankle","r_hindfoot"])

MetadataSet29.addValue(MetadataString38)
MetadataString39 = MetadataString()
MetadataString39.setName("RightAnkleEnd")
MetadataString39.setReference("JOINT")
MetadataString39.setValue(["r_midtarsal","r_middistal"])

MetadataSet29.addValue(MetadataString39)
MetadataString40 = MetadataString()
MetadataString40.setName("RightAnkleEndSite")
MetadataString40.setReference("Site")
MetadataString40.setValue(["r_midtarsal_tip"])

MetadataSet29.addValue(MetadataString40)
MetadataString41 = MetadataString()
MetadataString41.setName("Chest")
MetadataString41.setReference("JOINT")
MetadataString41.setValue(["vl5","l5"])

MetadataSet29.addValue(MetadataString41)
MetadataString42 = MetadataString()
MetadataString42.setName("Chest2")
MetadataString42.setReference("JOINT")
MetadataString42.setValue(["Chest2","vl5_to_Chest2"])

MetadataSet29.addValue(MetadataString42)
MetadataString43 = MetadataString()
MetadataString43.setName("LeftCollar")
MetadataString43.setReference("JOINT")
MetadataString43.setValue(["LeftCollar","Chest2_to_LeftCollar"])

MetadataSet29.addValue(MetadataString43)
MetadataString44 = MetadataString()
MetadataString44.setName("LeftShoulder")
MetadataString44.setReference("JOINT")
MetadataString44.setValue(["l_shoulder","l_upperarm"])

MetadataSet29.addValue(MetadataString44)
MetadataString45 = MetadataString()
MetadataString45.setName("LeftElbow")
MetadataString45.setReference("JOINT")
MetadataString45.setValue(["l_elbow","l_forearm"])

MetadataSet29.addValue(MetadataString45)
MetadataString46 = MetadataString()
MetadataString46.setName("LeftWrist")
MetadataString46.setReference("JOINT")
MetadataString46.setValue(["l_wrist","l_hand"])

MetadataSet29.addValue(MetadataString46)
MetadataString47 = MetadataString()
MetadataString47.setName("LeftWristSite")
MetadataString47.setReference("Site")
MetadataString47.setValue(["l_wrist_tip"])

MetadataSet29.addValue(MetadataString47)
MetadataString48 = MetadataString()
MetadataString48.setName("RightCollar")
MetadataString48.setReference("JOINT")
MetadataString48.setValue(["RightCollar","Chest2_to_RightCollar"])

MetadataSet29.addValue(MetadataString48)
MetadataString49 = MetadataString()
MetadataString49.setName("RightShoulder")
MetadataString49.setReference("JOINT")
MetadataString49.setValue(["r_shoulder","r_upperarm"])

MetadataSet29.addValue(MetadataString49)
MetadataString50 = MetadataString()
MetadataString50.setName("RightElbow")
MetadataString50.setReference("JOINT")
MetadataString50.setValue(["r_elbow","r_forearm"])

MetadataSet29.addValue(MetadataString50)
MetadataString51 = MetadataString()
MetadataString51.setName("RightWrist")
MetadataString51.setReference("JOINT")
MetadataString51.setValue(["r_wrist","r_hand"])

MetadataSet29.addValue(MetadataString51)
MetadataString52 = MetadataString()
MetadataString52.setName("RightWristSite")
MetadataString52.setReference("Site")
MetadataString52.setValue(["r_wrist_tip"])

MetadataSet29.addValue(MetadataString52)
MetadataString53 = MetadataString()
MetadataString53.setName("Neck")
MetadataString53.setReference("JOINT")
MetadataString53.setValue(["Neck","Chest2_to_Neck"])

MetadataSet29.addValue(MetadataString53)
MetadataString54 = MetadataString()
MetadataString54.setName("Head")
MetadataString54.setReference("JOINT")
MetadataString54.setValue(["skullbase","skull"])

MetadataSet29.addValue(MetadataString54)
MetadataString55 = MetadataString()
MetadataString55.setName("HeadSite")
MetadataString55.setReference("Site")
MetadataString55.setValue(["skullbase_tip"])

MetadataSet29.addValue(MetadataString55)

Group28.setMetadata(MetadataSet29)

Scene26.addChildren(Group28)
#initialPositionOffset computation: 0.000 13.970 7.620, initialPositionScaled computation: 0.000 0.140 0.076
Transform56 = Transform()
Transform56.setDEF("InitialPositionScaled")
Transform56.setTranslation([0,0.806,0.194])
Viewpoint57 = Viewpoint()
Viewpoint57.setDescription("Bvh1 model BVH to X3D conversion, from 8m")
Viewpoint57.setPosition([0,0,8])

Transform56.addChildren(Viewpoint57)
Viewpoint58 = Viewpoint()
Viewpoint58.setDescription("Bvh1 initial motion position")
Viewpoint58.setPosition([0.039,2.423,7.987])

Transform56.addChildren(Viewpoint58)
Viewpoint59 = Viewpoint()
Viewpoint59.setDescription("Bvh1 final motion position")
Viewpoint59.setPosition([2.697,2.404,15.107])

Transform56.addChildren(Viewpoint59)

Scene26.addChildren(Transform56)
HAnimHumanoid60 = HAnimHumanoid()
HAnimHumanoid60.setName("Hips")
HAnimHumanoid60.setDEF("Bvh1_Hips")
HAnimHumanoid60.setVersion("1.0")
#HAnimHumanoid original info='\"authorEmail=*TODO*\" \"authorName=*TODO*\" \"copyright=Copyright 2017\" \"humanoidVersion=*TODO*\" \"usageRestrictions=*TODO*\"'
#Top-level HAnimSite/Viewpoint attached to HAnimHumanoid is unaffected by motion animation
#top-level USE nodes follow DEF declarations and can be employed by inverse-kinematics (IK) engines or other HAnim tools
MetadataSet61 = MetadataSet()
MetadataSet61.setName("HAnimHumanoid.info")
MetadataSet61.setReference("https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid")
MetadataString62 = MetadataString()
MetadataString62.setName("authorEmail")
MetadataString62.setValue(["*TODO*"])

MetadataSet61.setValue(MetadataString62)
MetadataString63 = MetadataString()
MetadataString63.setName("authorName")
MetadataString63.setValue(["*TODO*"])

MetadataSet61.addValue(MetadataString63)
MetadataString64 = MetadataString()
MetadataString64.setName("copyright")
MetadataString64.setValue(["Copyright 2017"])

MetadataSet61.addValue(MetadataString64)
MetadataString65 = MetadataString()
MetadataString65.setName("humanoidVersion")
MetadataString65.setValue(["*TODO*"])

MetadataSet61.addValue(MetadataString65)
MetadataString66 = MetadataString()
MetadataString66.setName("usageRestrictions")
MetadataString66.setValue(["*TODO*"])

MetadataSet61.addValue(MetadataString66)

HAnimHumanoid60.setMetadata(MetadataSet61)
HAnimJoint67 = HAnimJoint()
HAnimJoint67.setName("HumanoidRoot")
HAnimJoint67.setDEF("Bvh1_HumanoidRoot")
HAnimJoint67.setScale([0.0254,0.0254,0.0254])
HAnimJoint67.setTranslation([0,0.806,0.194])
HAnimJoint67.setStiffness([0,0,0])
#BVH ROOT Hips, OFFSET 7.62 0.0 0.0, CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation
HAnimSegment68 = HAnimSegment()
HAnimSegment68.setName("sacrum")
HAnimSegment68.setDEF("Bvh1_sacrum")
#Visualization root shape and hidden DEF geometry for later use
Viewpoint69 = Viewpoint()
Viewpoint69.setDescription("View from (0 0 4) towards HAnimHumanoid center")
Viewpoint69.setPosition([0,0,4])

HAnimSegment68.addChildren(Viewpoint69)
Switch70 = Switch()
Switch70.setWhichChoice(0)
Group71 = Group()
TouchSensor72 = TouchSensor()
TouchSensor72.setDescription("HAnimHumanoid HAnimSegment HumanoidRoot")

Group71.addChildren(TouchSensor72)
Shape73 = Shape()
Shape73.setDEF("HAnimRootShape")
Sphere74 = Sphere()
Sphere74.setDEF("HAnimJointSphere")

Shape73.setGeometry(Sphere74)
Appearance75 = Appearance()
Material76 = Material()
Material76.setDEF("HAnimRootMaterial")
Material76.setDiffuseColor([0.8,0,0])
Material76.setTransparency(0.3)

Appearance75.setMaterial(Material76)

Shape73.setAppearance(Appearance75)

Group71.addChildren(Shape73)

Switch70.addChildren(Group71)
Shape77 = Shape()
Shape77.setDEF("HAnimJointShape")
Sphere78 = Sphere()
Sphere78.setUSE("HAnimJointSphere")

Shape77.setGeometry(Sphere78)
Appearance79 = Appearance()
Material80 = Material()
Material80.setDEF("HAnimJointMaterial")
Material80.setDiffuseColor([0,0,0.8])
Material80.setTransparency(0.3)

Appearance79.setMaterial(Material80)

Shape77.setAppearance(Appearance79)

Switch70.addChildren(Shape77)
Shape81 = Shape()
LineSet82 = LineSet()
LineSet82.setVertexCount([2])
#transparency indicates parent/child relationship of line segment
ColorRGBA83 = ColorRGBA()
ColorRGBA83.setDEF("HAnimSegmentLineColorRGBA")
ColorRGBA83.setColor([1,1,0,1,1,1,0,0.1])

LineSet82.setColor(ColorRGBA83)
Coordinate84 = Coordinate()
Coordinate84.setPoint([0,0,0,0,0,0])

LineSet82.setCoord(Coordinate84)

Shape81.setGeometry(LineSet82)

Switch70.addChildren(Shape81)
Shape85 = Shape()
Shape85.setDEF("HAnimSiteShape")
IndexedFaceSet86 = IndexedFaceSet()
IndexedFaceSet86.setDEF("DiamondIFS")
IndexedFaceSet86.setColorIndex([0,0,0,0,0,0,0,0])
IndexedFaceSet86.setCoordIndex([0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1])
IndexedFaceSet86.setCreaseAngle(0.5)
IndexedFaceSet86.setSolid(False)
ColorRGBA87 = ColorRGBA()
ColorRGBA87.setDEF("HAnimSiteColorRGBA")
ColorRGBA87.setColor([1,1,0,1,1,1,0,0.1])

IndexedFaceSet86.setColor(ColorRGBA87)
Coordinate88 = Coordinate()
Coordinate88.setPoint([0,0.8,0,-0.8,0,0,0,0,0.8,0.8,0,0,0,0,-0.8,0,-0.8,0])

IndexedFaceSet86.setCoord(Coordinate88)

Shape85.setGeometry(IndexedFaceSet86)
Appearance89 = Appearance()
Material90 = Material()
Material90.setDiffuseColor([1,1,0])
Material90.setTransparency(0.3)

Appearance89.setMaterial(Material90)

Shape85.setAppearance(Appearance89)

Switch70.addChildren(Shape85)

HAnimSegment68.addChildren(Switch70)
#HAnimSegment visualization line from current <HAnimJoint name='HumanoidRoot'/> to child <HAnimJoint name='l_hip'/>
Shape91 = Shape()
LineSet92 = LineSet()
LineSet92.setVertexCount([2])
Coordinate93 = Coordinate()
Coordinate93.setPoint([0,0,0,7.62,0,0])

LineSet92.setCoord(Coordinate93)
ColorRGBA94 = ColorRGBA()
ColorRGBA94.setUSE("HAnimSegmentLineColorRGBA")

LineSet92.setColor(ColorRGBA94)

Shape91.setGeometry(LineSet92)

HAnimSegment68.addChildren(Shape91)
#HAnimSegment visualization line from current <HAnimJoint name='HumanoidRoot'/> to child <HAnimJoint name='r_hip'/>
Shape95 = Shape()
LineSet96 = LineSet()
LineSet96.setVertexCount([2])
Coordinate97 = Coordinate()
Coordinate97.setPoint([0,0,0,-7.62,0,0])

LineSet96.setCoord(Coordinate97)
ColorRGBA98 = ColorRGBA()
ColorRGBA98.setUSE("HAnimSegmentLineColorRGBA")

LineSet96.setColor(ColorRGBA98)

Shape95.setGeometry(LineSet96)

HAnimSegment68.addChildren(Shape95)
#HAnimSegment visualization line from current <HAnimJoint name='HumanoidRoot'/> to child <HAnimJoint name='vl5'/>
Shape99 = Shape()
LineSet100 = LineSet()
LineSet100.setVertexCount([2])
Coordinate101 = Coordinate()
Coordinate101.setPoint([0,0,0,0,7.62,-2.54])

LineSet100.setCoord(Coordinate101)
ColorRGBA102 = ColorRGBA()
ColorRGBA102.setUSE("HAnimSegmentLineColorRGBA")

LineSet100.setColor(ColorRGBA102)

Shape99.setGeometry(LineSet100)

HAnimSegment68.addChildren(Shape99)

HAnimJoint67.addChildren(HAnimSegment68)
HAnimJoint103 = HAnimJoint()
HAnimJoint103.setName("l_hip")
HAnimJoint103.setDEF("Bvh1_l_hip")
HAnimJoint103.setCenter([7.62,0,0])
HAnimJoint103.setStiffness([0,0,0])
#BVH JOINT LeftHip, OFFSET 7.62 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment104 = HAnimSegment()
HAnimSegment104.setName("l_thigh")
HAnimSegment104.setDEF("Bvh1_l_thigh")
#Visualization sphere for <HAnimJoint name='l_hip'/> is placed within <HAnimSegment name='l_thigh'/>
TouchSensor105 = TouchSensor()
TouchSensor105.setDescription("HAnimJoint l_hip, HAnimSegment l_thigh")

HAnimSegment104.addChildren(TouchSensor105)
Transform106 = Transform()
Transform106.setTranslation([7.62,0,0])
Shape107 = Shape()
Shape107.setUSE("HAnimJointShape")

Transform106.addChildren(Shape107)

HAnimSegment104.addChildren(Transform106)
#HAnimSegment visualization line from current <HAnimJoint name='l_hip'/> to child <HAnimJoint name='l_knee'/>
Shape108 = Shape()
LineSet109 = LineSet()
LineSet109.setVertexCount([2])
Coordinate110 = Coordinate()
Coordinate110.setPoint([7.62,0,0,7.62,-44.449999,0])

LineSet109.setCoord(Coordinate110)
ColorRGBA111 = ColorRGBA()
ColorRGBA111.setUSE("HAnimSegmentLineColorRGBA")

LineSet109.setColor(ColorRGBA111)

Shape108.setGeometry(LineSet109)

HAnimSegment104.addChildren(Shape108)
Transform112 = Transform()
Transform112.setTranslation([7.62,0,0])
#insert Shape geometry here

HAnimSegment104.addChildren(Transform112)

HAnimJoint103.addChildren(HAnimSegment104)
HAnimJoint113 = HAnimJoint()
HAnimJoint113.setName("l_knee")
HAnimJoint113.setDEF("Bvh1_l_knee")
HAnimJoint113.setCenter([7.62,-44.449999,0])
HAnimJoint113.setStiffness([0,0,0])
#BVH JOINT LeftKnee, OFFSET 0.0 -44.449999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment114 = HAnimSegment()
HAnimSegment114.setName("l_calf")
HAnimSegment114.setDEF("Bvh1_l_calf")
#Visualization sphere for <HAnimJoint name='l_knee'/> is placed within <HAnimSegment name='l_calf'/>
TouchSensor115 = TouchSensor()
TouchSensor115.setDescription("HAnimJoint l_knee, HAnimSegment l_calf")

HAnimSegment114.addChildren(TouchSensor115)
Transform116 = Transform()
Transform116.setTranslation([7.62,-44.449999,0])
Shape117 = Shape()
Shape117.setUSE("HAnimJointShape")

Transform116.addChildren(Shape117)

HAnimSegment114.addChildren(Transform116)
#HAnimSegment visualization line from current <HAnimJoint name='l_knee'/> to child <HAnimJoint name='l_ankle'/>
Shape118 = Shape()
LineSet119 = LineSet()
LineSet119.setVertexCount([2])
Coordinate120 = Coordinate()
Coordinate120.setPoint([7.62,-44.449999,0,7.62,-83.819998,0])

LineSet119.setCoord(Coordinate120)
ColorRGBA121 = ColorRGBA()
ColorRGBA121.setUSE("HAnimSegmentLineColorRGBA")

LineSet119.setColor(ColorRGBA121)

Shape118.setGeometry(LineSet119)

HAnimSegment114.addChildren(Shape118)
Transform122 = Transform()
Transform122.setTranslation([7.62,-44.449999,0])
#insert Shape geometry here

HAnimSegment114.addChildren(Transform122)

HAnimJoint113.addChildren(HAnimSegment114)
HAnimJoint123 = HAnimJoint()
HAnimJoint123.setName("l_ankle")
HAnimJoint123.setDEF("Bvh1_l_ankle")
HAnimJoint123.setCenter([7.62,-83.819998,0])
HAnimJoint123.setStiffness([0,0,0])
#BVH JOINT LeftAnkle, OFFSET 0.0 -39.369999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment124 = HAnimSegment()
HAnimSegment124.setName("l_hindfoot")
HAnimSegment124.setDEF("Bvh1_l_hindfoot")
#Visualization sphere for <HAnimJoint name='l_ankle'/> is placed within <HAnimSegment name='l_hindfoot'/>
TouchSensor125 = TouchSensor()
TouchSensor125.setDescription("HAnimJoint l_ankle, HAnimSegment l_hindfoot")

HAnimSegment124.addChildren(TouchSensor125)
Transform126 = Transform()
Transform126.setTranslation([7.62,-83.819998,0])
Shape127 = Shape()
Shape127.setUSE("HAnimJointShape")

Transform126.addChildren(Shape127)

HAnimSegment124.addChildren(Transform126)
#HAnimSegment visualization line from current <HAnimJoint name='l_ankle'/> to child <HAnimJoint name='l_midtarsal'/>
Shape128 = Shape()
LineSet129 = LineSet()
LineSet129.setVertexCount([2])
Coordinate130 = Coordinate()
Coordinate130.setPoint([7.62,-83.819998,0,7.62,-92.709998,-3.81])

LineSet129.setCoord(Coordinate130)
ColorRGBA131 = ColorRGBA()
ColorRGBA131.setUSE("HAnimSegmentLineColorRGBA")

LineSet129.setColor(ColorRGBA131)

Shape128.setGeometry(LineSet129)

HAnimSegment124.addChildren(Shape128)
Transform132 = Transform()
Transform132.setTranslation([7.62,-83.819998,0])
#insert Shape geometry here

HAnimSegment124.addChildren(Transform132)

HAnimJoint123.addChildren(HAnimSegment124)
HAnimJoint133 = HAnimJoint()
HAnimJoint133.setName("l_midtarsal")
HAnimJoint133.setDEF("Bvh1_l_midtarsal")
HAnimJoint133.setCenter([7.62,-92.709998,-3.81])
HAnimJoint133.setStiffness([0,0,0])
#BVH JOINT LeftAnkleEnd, OFFSET 0.0 -8.89 -3.81, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment134 = HAnimSegment()
HAnimSegment134.setName("l_middistal")
HAnimSegment134.setDEF("Bvh1_l_middistal")
#Visualization sphere for <HAnimJoint name='l_midtarsal'/> is placed within <HAnimSegment name='l_middistal'/>
TouchSensor135 = TouchSensor()
TouchSensor135.setDescription("HAnimJoint l_midtarsal, HAnimSegment l_middistal")

HAnimSegment134.addChildren(TouchSensor135)
Transform136 = Transform()
Transform136.setTranslation([7.62,-92.709998,-3.81])
Shape137 = Shape()
Shape137.setUSE("HAnimJointShape")

Transform136.addChildren(Shape137)

HAnimSegment134.addChildren(Transform136)
Transform138 = Transform()
Transform138.setTranslation([7.62,-92.709998,-3.81])
HAnimSite139 = HAnimSite()
HAnimSite139.setName("l_middistal_tip")
HAnimSite139.setDEF("Bvh1_l_middistal_tip")
HAnimSite139.setTranslation([0,0,15.24])
#BVH End Site OFFSET (0.0, 0.0, 15.24)
#HAnimSite visualization shape
TouchSensor140 = TouchSensor()
TouchSensor140.setDescription("HAnimSite l_middistal_tip")

HAnimSite139.addChildren(TouchSensor140)
Shape141 = Shape()
Shape141.setUSE("HAnimSiteShape")

HAnimSite139.addChildren(Shape141)

Transform138.addChildren(HAnimSite139)

HAnimSegment134.addChildren(Transform138)

HAnimJoint133.addChildren(HAnimSegment134)

HAnimJoint123.addChildren(HAnimJoint133)

HAnimJoint113.addChildren(HAnimJoint123)

HAnimJoint103.addChildren(HAnimJoint113)

HAnimJoint67.addChildren(HAnimJoint103)
HAnimJoint142 = HAnimJoint()
HAnimJoint142.setName("r_hip")
HAnimJoint142.setDEF("Bvh1_r_hip")
HAnimJoint142.setCenter([-7.62,0,0])
HAnimJoint142.setStiffness([0,0,0])
#BVH JOINT RightHip, OFFSET -7.62 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment143 = HAnimSegment()
HAnimSegment143.setName("r_thigh")
HAnimSegment143.setDEF("Bvh1_r_thigh")
#Visualization sphere for <HAnimJoint name='r_hip'/> is placed within <HAnimSegment name='r_thigh'/>
TouchSensor144 = TouchSensor()
TouchSensor144.setDescription("HAnimJoint r_hip, HAnimSegment r_thigh")

HAnimSegment143.addChildren(TouchSensor144)
Transform145 = Transform()
Transform145.setTranslation([-7.62,0,0])
Shape146 = Shape()
Shape146.setUSE("HAnimJointShape")

Transform145.addChildren(Shape146)

HAnimSegment143.addChildren(Transform145)
#HAnimSegment visualization line from current <HAnimJoint name='r_hip'/> to child <HAnimJoint name='r_knee'/>
Shape147 = Shape()
LineSet148 = LineSet()
LineSet148.setVertexCount([2])
Coordinate149 = Coordinate()
Coordinate149.setPoint([-7.62,0,0,-7.62,-44.449999,0])

LineSet148.setCoord(Coordinate149)
ColorRGBA150 = ColorRGBA()
ColorRGBA150.setUSE("HAnimSegmentLineColorRGBA")

LineSet148.setColor(ColorRGBA150)

Shape147.setGeometry(LineSet148)

HAnimSegment143.addChildren(Shape147)
Transform151 = Transform()
Transform151.setTranslation([-7.62,0,0])
#insert Shape geometry here

HAnimSegment143.addChildren(Transform151)

HAnimJoint142.addChildren(HAnimSegment143)
HAnimJoint152 = HAnimJoint()
HAnimJoint152.setName("r_knee")
HAnimJoint152.setDEF("Bvh1_r_knee")
HAnimJoint152.setCenter([-7.62,-44.449999,0])
HAnimJoint152.setStiffness([0,0,0])
#BVH JOINT RightKnee, OFFSET 0.0 -44.449999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment153 = HAnimSegment()
HAnimSegment153.setName("r_calf")
HAnimSegment153.setDEF("Bvh1_r_calf")
#Visualization sphere for <HAnimJoint name='r_knee'/> is placed within <HAnimSegment name='r_calf'/>
TouchSensor154 = TouchSensor()
TouchSensor154.setDescription("HAnimJoint r_knee, HAnimSegment r_calf")

HAnimSegment153.addChildren(TouchSensor154)
Transform155 = Transform()
Transform155.setTranslation([-7.62,-44.449999,0])
Shape156 = Shape()
Shape156.setUSE("HAnimJointShape")

Transform155.addChildren(Shape156)

HAnimSegment153.addChildren(Transform155)
#HAnimSegment visualization line from current <HAnimJoint name='r_knee'/> to child <HAnimJoint name='r_ankle'/>
Shape157 = Shape()
LineSet158 = LineSet()
LineSet158.setVertexCount([2])
Coordinate159 = Coordinate()
Coordinate159.setPoint([-7.62,-44.449999,0,-7.62,-83.819998,0])

LineSet158.setCoord(Coordinate159)
ColorRGBA160 = ColorRGBA()
ColorRGBA160.setUSE("HAnimSegmentLineColorRGBA")

LineSet158.setColor(ColorRGBA160)

Shape157.setGeometry(LineSet158)

HAnimSegment153.addChildren(Shape157)
Transform161 = Transform()
Transform161.setTranslation([-7.62,-44.449999,0])
#insert Shape geometry here

HAnimSegment153.addChildren(Transform161)

HAnimJoint152.addChildren(HAnimSegment153)
HAnimJoint162 = HAnimJoint()
HAnimJoint162.setName("r_ankle")
HAnimJoint162.setDEF("Bvh1_r_ankle")
HAnimJoint162.setCenter([-7.62,-83.819998,0])
HAnimJoint162.setStiffness([0,0,0])
#BVH JOINT RightAnkle, OFFSET 0.0 -39.369999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment163 = HAnimSegment()
HAnimSegment163.setName("r_hindfoot")
HAnimSegment163.setDEF("Bvh1_r_hindfoot")
#Visualization sphere for <HAnimJoint name='r_ankle'/> is placed within <HAnimSegment name='r_hindfoot'/>
TouchSensor164 = TouchSensor()
TouchSensor164.setDescription("HAnimJoint r_ankle, HAnimSegment r_hindfoot")

HAnimSegment163.addChildren(TouchSensor164)
Transform165 = Transform()
Transform165.setTranslation([-7.62,-83.819998,0])
Shape166 = Shape()
Shape166.setUSE("HAnimJointShape")

Transform165.addChildren(Shape166)

HAnimSegment163.addChildren(Transform165)
#HAnimSegment visualization line from current <HAnimJoint name='r_ankle'/> to child <HAnimJoint name='r_midtarsal'/>
Shape167 = Shape()
LineSet168 = LineSet()
LineSet168.setVertexCount([2])
Coordinate169 = Coordinate()
Coordinate169.setPoint([-7.62,-83.819998,0,-7.62,-92.709998,-3.81])

LineSet168.setCoord(Coordinate169)
ColorRGBA170 = ColorRGBA()
ColorRGBA170.setUSE("HAnimSegmentLineColorRGBA")

LineSet168.setColor(ColorRGBA170)

Shape167.setGeometry(LineSet168)

HAnimSegment163.addChildren(Shape167)
Transform171 = Transform()
Transform171.setTranslation([-7.62,-83.819998,0])
#insert Shape geometry here

HAnimSegment163.addChildren(Transform171)

HAnimJoint162.addChildren(HAnimSegment163)
HAnimJoint172 = HAnimJoint()
HAnimJoint172.setName("r_midtarsal")
HAnimJoint172.setDEF("Bvh1_r_midtarsal")
HAnimJoint172.setCenter([-7.62,-92.709998,-3.81])
HAnimJoint172.setStiffness([0,0,0])
#BVH JOINT RightAnkleEnd, OFFSET 0.0 -8.89 -3.81, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment173 = HAnimSegment()
HAnimSegment173.setName("r_middistal")
HAnimSegment173.setDEF("Bvh1_r_middistal")
#Visualization sphere for <HAnimJoint name='r_midtarsal'/> is placed within <HAnimSegment name='r_middistal'/>
TouchSensor174 = TouchSensor()
TouchSensor174.setDescription("HAnimJoint r_midtarsal, HAnimSegment r_middistal")

HAnimSegment173.addChildren(TouchSensor174)
Transform175 = Transform()
Transform175.setTranslation([-7.62,-92.709998,-3.81])
Shape176 = Shape()
Shape176.setUSE("HAnimJointShape")

Transform175.addChildren(Shape176)

HAnimSegment173.addChildren(Transform175)
Transform177 = Transform()
Transform177.setTranslation([-7.62,-92.709998,-3.81])
HAnimSite178 = HAnimSite()
HAnimSite178.setName("r_middistal_tip")
HAnimSite178.setDEF("Bvh1_r_middistal_tip")
HAnimSite178.setTranslation([0,0,15.24])
#BVH End Site OFFSET (0.0, 0.0, 15.24)
#HAnimSite visualization shape
TouchSensor179 = TouchSensor()
TouchSensor179.setDescription("HAnimSite r_middistal_tip")

HAnimSite178.addChildren(TouchSensor179)
Shape180 = Shape()
Shape180.setUSE("HAnimSiteShape")

HAnimSite178.addChildren(Shape180)

Transform177.addChildren(HAnimSite178)

HAnimSegment173.addChildren(Transform177)

HAnimJoint172.addChildren(HAnimSegment173)

HAnimJoint162.addChildren(HAnimJoint172)

HAnimJoint152.addChildren(HAnimJoint162)

HAnimJoint142.addChildren(HAnimJoint152)

HAnimJoint67.addChildren(HAnimJoint142)
HAnimJoint181 = HAnimJoint()
HAnimJoint181.setName("vl5")
HAnimJoint181.setDEF("Bvh1_vl5")
HAnimJoint181.setCenter([0,7.62,-2.54])
HAnimJoint181.setStiffness([0,0,0])
#BVH JOINT Chest, OFFSET 0.0 7.62 -2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment182 = HAnimSegment()
HAnimSegment182.setName("l5")
HAnimSegment182.setDEF("Bvh1_l5")
#Visualization sphere for <HAnimJoint name='vl5'/> is placed within <HAnimSegment name='l5'/>
TouchSensor183 = TouchSensor()
TouchSensor183.setDescription("HAnimJoint vl5, HAnimSegment l5")

HAnimSegment182.addChildren(TouchSensor183)
Transform184 = Transform()
Transform184.setTranslation([0,7.62,-2.54])
Shape185 = Shape()
Shape185.setUSE("HAnimJointShape")

Transform184.addChildren(Shape185)

HAnimSegment182.addChildren(Transform184)
#HAnimSegment visualization line from current <HAnimJoint name='vl5'/> to child <HAnimJoint name='Chest2'/>
Shape186 = Shape()
LineSet187 = LineSet()
LineSet187.setVertexCount([2])
Coordinate188 = Coordinate()
Coordinate188.setPoint([0,7.62,-2.54,0,15.24,-2.54])

LineSet187.setCoord(Coordinate188)
ColorRGBA189 = ColorRGBA()
ColorRGBA189.setUSE("HAnimSegmentLineColorRGBA")

LineSet187.setColor(ColorRGBA189)

Shape186.setGeometry(LineSet187)

HAnimSegment182.addChildren(Shape186)
Transform190 = Transform()
Transform190.setTranslation([0,7.62,-2.54])
#insert Shape geometry here

HAnimSegment182.addChildren(Transform190)

HAnimJoint181.addChildren(HAnimSegment182)
HAnimJoint191 = HAnimJoint()
HAnimJoint191.setName("Chest2")
HAnimJoint191.setDEF("Bvh1_Chest2")
HAnimJoint191.setCenter([0,15.24,-2.54])
HAnimJoint191.setStiffness([0,0,0])
#BVH JOINT Chest2, OFFSET 0.0 7.62 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment192 = HAnimSegment()
HAnimSegment192.setName("vl5_to_Chest2")
HAnimSegment192.setDEF("Bvh1_vl5_to_Chest2")
#Visualization sphere for <HAnimJoint name='Chest2'/> is placed within <HAnimSegment name='vl5_to_Chest2'/>
TouchSensor193 = TouchSensor()
TouchSensor193.setDescription("HAnimJoint Chest2, HAnimSegment vl5_to_Chest2")

HAnimSegment192.addChildren(TouchSensor193)
Transform194 = Transform()
Transform194.setTranslation([0,15.24,-2.54])
Shape195 = Shape()
Shape195.setUSE("HAnimJointShape")

Transform194.addChildren(Shape195)

HAnimSegment192.addChildren(Transform194)
#HAnimSegment visualization line from current <HAnimJoint name='Chest2'/> to child <HAnimJoint name='LeftCollar'/>
Shape196 = Shape()
LineSet197 = LineSet()
LineSet197.setVertexCount([2])
Coordinate198 = Coordinate()
Coordinate198.setPoint([0,15.24,-2.54,7.62,48.260000000000005,0])

LineSet197.setCoord(Coordinate198)
ColorRGBA199 = ColorRGBA()
ColorRGBA199.setUSE("HAnimSegmentLineColorRGBA")

LineSet197.setColor(ColorRGBA199)

Shape196.setGeometry(LineSet197)

HAnimSegment192.addChildren(Shape196)
#HAnimSegment visualization line from current <HAnimJoint name='Chest2'/> to child <HAnimJoint name='RightCollar'/>
Shape200 = Shape()
LineSet201 = LineSet()
LineSet201.setVertexCount([2])
Coordinate202 = Coordinate()
Coordinate202.setPoint([0,15.24,-2.54,-7.62,48.260000000000005,0])

LineSet201.setCoord(Coordinate202)
ColorRGBA203 = ColorRGBA()
ColorRGBA203.setUSE("HAnimSegmentLineColorRGBA")

LineSet201.setColor(ColorRGBA203)

Shape200.setGeometry(LineSet201)

HAnimSegment192.addChildren(Shape200)
#HAnimSegment visualization line from current <HAnimJoint name='Chest2'/> to child <HAnimJoint name='Neck'/>
Shape204 = Shape()
LineSet205 = LineSet()
LineSet205.setVertexCount([2])
Coordinate206 = Coordinate()
Coordinate206.setPoint([0,15.24,-2.54,0,53.339999,0])

LineSet205.setCoord(Coordinate206)
ColorRGBA207 = ColorRGBA()
ColorRGBA207.setUSE("HAnimSegmentLineColorRGBA")

LineSet205.setColor(ColorRGBA207)

Shape204.setGeometry(LineSet205)

HAnimSegment192.addChildren(Shape204)
Transform208 = Transform()
Transform208.setTranslation([0,15.24,-2.54])
#insert Shape geometry here

HAnimSegment192.addChildren(Transform208)

HAnimJoint191.addChildren(HAnimSegment192)
HAnimJoint209 = HAnimJoint()
HAnimJoint209.setName("LeftCollar")
HAnimJoint209.setDEF("Bvh1_LeftCollar")
HAnimJoint209.setCenter([7.62,48.260000000000005,0])
HAnimJoint209.setStiffness([0,0,0])
#BVH JOINT LeftCollar, OFFSET 7.62 33.02 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment210 = HAnimSegment()
HAnimSegment210.setName("Chest2_to_LeftCollar")
HAnimSegment210.setDEF("Bvh1_Chest2_to_LeftCollar")
#Visualization sphere for <HAnimJoint name='LeftCollar'/> is placed within <HAnimSegment name='Chest2_to_LeftCollar'/>
TouchSensor211 = TouchSensor()
TouchSensor211.setDescription("HAnimJoint LeftCollar, HAnimSegment Chest2_to_LeftCollar")

HAnimSegment210.addChildren(TouchSensor211)
Transform212 = Transform()
Transform212.setTranslation([7.62,48.260000000000005,0])
Shape213 = Shape()
Shape213.setUSE("HAnimJointShape")

Transform212.addChildren(Shape213)

HAnimSegment210.addChildren(Transform212)
#HAnimSegment visualization line from current <HAnimJoint name='LeftCollar'/> to child <HAnimJoint name='l_shoulder'/>
Shape214 = Shape()
LineSet215 = LineSet()
LineSet215.setVertexCount([2])
Coordinate216 = Coordinate()
Coordinate216.setPoint([7.62,48.260000000000005,0,20.32,48.260000000000005,0])

LineSet215.setCoord(Coordinate216)
ColorRGBA217 = ColorRGBA()
ColorRGBA217.setUSE("HAnimSegmentLineColorRGBA")

LineSet215.setColor(ColorRGBA217)

Shape214.setGeometry(LineSet215)

HAnimSegment210.addChildren(Shape214)
Transform218 = Transform()
Transform218.setTranslation([7.62,48.260000000000005,0])
#insert Shape geometry here

HAnimSegment210.addChildren(Transform218)

HAnimJoint209.addChildren(HAnimSegment210)
HAnimJoint219 = HAnimJoint()
HAnimJoint219.setName("l_shoulder")
HAnimJoint219.setDEF("Bvh1_l_shoulder")
HAnimJoint219.setCenter([20.32,48.260000000000005,0])
HAnimJoint219.setStiffness([0,0,0])
#BVH JOINT LeftShoulder, OFFSET 12.7 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment220 = HAnimSegment()
HAnimSegment220.setName("l_upperarm")
HAnimSegment220.setDEF("Bvh1_l_upperarm")
#Visualization sphere for <HAnimJoint name='l_shoulder'/> is placed within <HAnimSegment name='l_upperarm'/>
TouchSensor221 = TouchSensor()
TouchSensor221.setDescription("HAnimJoint l_shoulder, HAnimSegment l_upperarm")

HAnimSegment220.addChildren(TouchSensor221)
Transform222 = Transform()
Transform222.setTranslation([20.32,48.260000000000005,0])
Shape223 = Shape()
Shape223.setUSE("HAnimJointShape")

Transform222.addChildren(Shape223)

HAnimSegment220.addChildren(Transform222)
#HAnimSegment visualization line from current <HAnimJoint name='l_shoulder'/> to child <HAnimJoint name='l_elbow'/>
Shape224 = Shape()
LineSet225 = LineSet()
LineSet225.setVertexCount([2])
Coordinate226 = Coordinate()
Coordinate226.setPoint([20.32,48.260000000000005,0,20.32,17.780000000000005,0])

LineSet225.setCoord(Coordinate226)
ColorRGBA227 = ColorRGBA()
ColorRGBA227.setUSE("HAnimSegmentLineColorRGBA")

LineSet225.setColor(ColorRGBA227)

Shape224.setGeometry(LineSet225)

HAnimSegment220.addChildren(Shape224)
Transform228 = Transform()
Transform228.setTranslation([20.32,48.260000000000005,0])
#insert Shape geometry here

HAnimSegment220.addChildren(Transform228)

HAnimJoint219.addChildren(HAnimSegment220)
HAnimJoint229 = HAnimJoint()
HAnimJoint229.setName("l_elbow")
HAnimJoint229.setDEF("Bvh1_l_elbow")
HAnimJoint229.setCenter([20.32,17.780000000000005,0])
HAnimJoint229.setStiffness([0,0,0])
#BVH JOINT LeftElbow, OFFSET 0.0 -30.48 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment230 = HAnimSegment()
HAnimSegment230.setName("l_forearm")
HAnimSegment230.setDEF("Bvh1_l_forearm")
#Visualization sphere for <HAnimJoint name='l_elbow'/> is placed within <HAnimSegment name='l_forearm'/>
TouchSensor231 = TouchSensor()
TouchSensor231.setDescription("HAnimJoint l_elbow, HAnimSegment l_forearm")

HAnimSegment230.addChildren(TouchSensor231)
Transform232 = Transform()
Transform232.setTranslation([20.32,17.780000000000005,0])
Shape233 = Shape()
Shape233.setUSE("HAnimJointShape")

Transform232.addChildren(Shape233)

HAnimSegment230.addChildren(Transform232)
#HAnimSegment visualization line from current <HAnimJoint name='l_elbow'/> to child <HAnimJoint name='l_wrist'/>
Shape234 = Shape()
LineSet235 = LineSet()
LineSet235.setVertexCount([2])
Coordinate236 = Coordinate()
Coordinate236.setPoint([20.32,17.780000000000005,0,20.32,-6.349999999999994,0])

LineSet235.setCoord(Coordinate236)
ColorRGBA237 = ColorRGBA()
ColorRGBA237.setUSE("HAnimSegmentLineColorRGBA")

LineSet235.setColor(ColorRGBA237)

Shape234.setGeometry(LineSet235)

HAnimSegment230.addChildren(Shape234)
Transform238 = Transform()
Transform238.setTranslation([20.32,17.780000000000005,0])
#insert Shape geometry here

HAnimSegment230.addChildren(Transform238)

HAnimJoint229.addChildren(HAnimSegment230)
HAnimJoint239 = HAnimJoint()
HAnimJoint239.setName("l_wrist")
HAnimJoint239.setDEF("Bvh1_l_wrist")
HAnimJoint239.setCenter([20.32,-6.349999999999994,0])
HAnimJoint239.setStiffness([0,0,0])
#BVH JOINT LeftWrist, OFFSET 0.0 -24.13 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment240 = HAnimSegment()
HAnimSegment240.setName("l_hand")
HAnimSegment240.setDEF("Bvh1_l_hand")
#Visualization sphere for <HAnimJoint name='l_wrist'/> is placed within <HAnimSegment name='l_hand'/>
TouchSensor241 = TouchSensor()
TouchSensor241.setDescription("HAnimJoint l_wrist, HAnimSegment l_hand")

HAnimSegment240.addChildren(TouchSensor241)
Transform242 = Transform()
Transform242.setTranslation([20.32,-6.349999999999994,0])
Shape243 = Shape()
Shape243.setUSE("HAnimJointShape")

Transform242.addChildren(Shape243)

HAnimSegment240.addChildren(Transform242)
Transform244 = Transform()
Transform244.setTranslation([20.32,-6.349999999999994,0])
HAnimSite245 = HAnimSite()
HAnimSite245.setName("l_hand_tip")
HAnimSite245.setDEF("Bvh1_l_hand_tip")
HAnimSite245.setTranslation([0,-17.78,0])
#BVH End Site OFFSET (0.0, -17.78, 0.0)
#HAnimSite visualization shape
TouchSensor246 = TouchSensor()
TouchSensor246.setDescription("HAnimSite l_hand_tip")

HAnimSite245.addChildren(TouchSensor246)
Shape247 = Shape()
Shape247.setUSE("HAnimSiteShape")

HAnimSite245.addChildren(Shape247)

Transform244.addChildren(HAnimSite245)

HAnimSegment240.addChildren(Transform244)

HAnimJoint239.addChildren(HAnimSegment240)

HAnimJoint229.addChildren(HAnimJoint239)

HAnimJoint219.addChildren(HAnimJoint229)

HAnimJoint209.addChildren(HAnimJoint219)

HAnimJoint191.addChildren(HAnimJoint209)
HAnimJoint248 = HAnimJoint()
HAnimJoint248.setName("RightCollar")
HAnimJoint248.setDEF("Bvh1_RightCollar")
HAnimJoint248.setCenter([-7.62,48.260000000000005,0])
HAnimJoint248.setStiffness([0,0,0])
#BVH JOINT RightCollar, OFFSET -7.62 33.02 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment249 = HAnimSegment()
HAnimSegment249.setName("Chest2_to_RightCollar")
HAnimSegment249.setDEF("Bvh1_Chest2_to_RightCollar")
#Visualization sphere for <HAnimJoint name='RightCollar'/> is placed within <HAnimSegment name='Chest2_to_RightCollar'/>
TouchSensor250 = TouchSensor()
TouchSensor250.setDescription("HAnimJoint RightCollar, HAnimSegment Chest2_to_RightCollar")

HAnimSegment249.addChildren(TouchSensor250)
Transform251 = Transform()
Transform251.setTranslation([-7.62,48.260000000000005,0])
Shape252 = Shape()
Shape252.setUSE("HAnimJointShape")

Transform251.addChildren(Shape252)

HAnimSegment249.addChildren(Transform251)
#HAnimSegment visualization line from current <HAnimJoint name='RightCollar'/> to child <HAnimJoint name='r_shoulder'/>
Shape253 = Shape()
LineSet254 = LineSet()
LineSet254.setVertexCount([2])
Coordinate255 = Coordinate()
Coordinate255.setPoint([-7.62,48.260000000000005,0,-20.32,48.260000000000005,0])

LineSet254.setCoord(Coordinate255)
ColorRGBA256 = ColorRGBA()
ColorRGBA256.setUSE("HAnimSegmentLineColorRGBA")

LineSet254.setColor(ColorRGBA256)

Shape253.setGeometry(LineSet254)

HAnimSegment249.addChildren(Shape253)
Transform257 = Transform()
Transform257.setTranslation([-7.62,48.260000000000005,0])
#insert Shape geometry here

HAnimSegment249.addChildren(Transform257)

HAnimJoint248.addChildren(HAnimSegment249)
HAnimJoint258 = HAnimJoint()
HAnimJoint258.setName("r_shoulder")
HAnimJoint258.setDEF("Bvh1_r_shoulder")
HAnimJoint258.setCenter([-20.32,48.260000000000005,0])
HAnimJoint258.setStiffness([0,0,0])
#BVH JOINT RightShoulder, OFFSET -12.7 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment259 = HAnimSegment()
HAnimSegment259.setName("r_upperarm")
HAnimSegment259.setDEF("Bvh1_r_upperarm")
#Visualization sphere for <HAnimJoint name='r_shoulder'/> is placed within <HAnimSegment name='r_upperarm'/>
TouchSensor260 = TouchSensor()
TouchSensor260.setDescription("HAnimJoint r_shoulder, HAnimSegment r_upperarm")

HAnimSegment259.addChildren(TouchSensor260)
Transform261 = Transform()
Transform261.setTranslation([-20.32,48.260000000000005,0])
Shape262 = Shape()
Shape262.setUSE("HAnimJointShape")

Transform261.addChildren(Shape262)

HAnimSegment259.addChildren(Transform261)
#HAnimSegment visualization line from current <HAnimJoint name='r_shoulder'/> to child <HAnimJoint name='r_elbow'/>
Shape263 = Shape()
LineSet264 = LineSet()
LineSet264.setVertexCount([2])
Coordinate265 = Coordinate()
Coordinate265.setPoint([-20.32,48.260000000000005,0,-20.32,17.780000000000005,0])

LineSet264.setCoord(Coordinate265)
ColorRGBA266 = ColorRGBA()
ColorRGBA266.setUSE("HAnimSegmentLineColorRGBA")

LineSet264.setColor(ColorRGBA266)

Shape263.setGeometry(LineSet264)

HAnimSegment259.addChildren(Shape263)
Transform267 = Transform()
Transform267.setTranslation([-20.32,48.260000000000005,0])
#insert Shape geometry here

HAnimSegment259.addChildren(Transform267)

HAnimJoint258.addChildren(HAnimSegment259)
HAnimJoint268 = HAnimJoint()
HAnimJoint268.setName("r_elbow")
HAnimJoint268.setDEF("Bvh1_r_elbow")
HAnimJoint268.setCenter([-20.32,17.780000000000005,0])
HAnimJoint268.setStiffness([0,0,0])
#BVH JOINT RightElbow, OFFSET 0.0 -30.48 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment269 = HAnimSegment()
HAnimSegment269.setName("r_forearm")
HAnimSegment269.setDEF("Bvh1_r_forearm")
#Visualization sphere for <HAnimJoint name='r_elbow'/> is placed within <HAnimSegment name='r_forearm'/>
TouchSensor270 = TouchSensor()
TouchSensor270.setDescription("HAnimJoint r_elbow, HAnimSegment r_forearm")

HAnimSegment269.addChildren(TouchSensor270)
Transform271 = Transform()
Transform271.setTranslation([-20.32,17.780000000000005,0])
Shape272 = Shape()
Shape272.setUSE("HAnimJointShape")

Transform271.addChildren(Shape272)

HAnimSegment269.addChildren(Transform271)
#HAnimSegment visualization line from current <HAnimJoint name='r_elbow'/> to child <HAnimJoint name='r_wrist'/>
Shape273 = Shape()
LineSet274 = LineSet()
LineSet274.setVertexCount([2])
Coordinate275 = Coordinate()
Coordinate275.setPoint([-20.32,17.780000000000005,0,-20.32,-6.349999999999994,0])

LineSet274.setCoord(Coordinate275)
ColorRGBA276 = ColorRGBA()
ColorRGBA276.setUSE("HAnimSegmentLineColorRGBA")

LineSet274.setColor(ColorRGBA276)

Shape273.setGeometry(LineSet274)

HAnimSegment269.addChildren(Shape273)
Transform277 = Transform()
Transform277.setTranslation([-20.32,17.780000000000005,0])
#insert Shape geometry here

HAnimSegment269.addChildren(Transform277)

HAnimJoint268.addChildren(HAnimSegment269)
HAnimJoint278 = HAnimJoint()
HAnimJoint278.setName("r_wrist")
HAnimJoint278.setDEF("Bvh1_r_wrist")
HAnimJoint278.setCenter([-20.32,-6.349999999999994,0])
HAnimJoint278.setStiffness([0,0,0])
#BVH JOINT RightWrist, OFFSET 0.0 -24.13 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment279 = HAnimSegment()
HAnimSegment279.setName("r_hand")
HAnimSegment279.setDEF("Bvh1_r_hand")
#Visualization sphere for <HAnimJoint name='r_wrist'/> is placed within <HAnimSegment name='r_hand'/>
TouchSensor280 = TouchSensor()
TouchSensor280.setDescription("HAnimJoint r_wrist, HAnimSegment r_hand")

HAnimSegment279.addChildren(TouchSensor280)
Transform281 = Transform()
Transform281.setTranslation([-20.32,-6.349999999999994,0])
Shape282 = Shape()
Shape282.setUSE("HAnimJointShape")

Transform281.addChildren(Shape282)

HAnimSegment279.addChildren(Transform281)
Transform283 = Transform()
Transform283.setTranslation([-20.32,-6.349999999999994,0])
HAnimSite284 = HAnimSite()
HAnimSite284.setName("r_hand_tip")
HAnimSite284.setDEF("Bvh1_r_hand_tip")
HAnimSite284.setTranslation([0,-17.78,0])
#BVH End Site OFFSET (0.0, -17.78, 0.0)
#HAnimSite visualization shape
TouchSensor285 = TouchSensor()
TouchSensor285.setDescription("HAnimSite r_hand_tip")

HAnimSite284.addChildren(TouchSensor285)
Shape286 = Shape()
Shape286.setUSE("HAnimSiteShape")

HAnimSite284.addChildren(Shape286)

Transform283.addChildren(HAnimSite284)

HAnimSegment279.addChildren(Transform283)

HAnimJoint278.addChildren(HAnimSegment279)

HAnimJoint268.addChildren(HAnimJoint278)

HAnimJoint258.addChildren(HAnimJoint268)

HAnimJoint248.addChildren(HAnimJoint258)

HAnimJoint191.addChildren(HAnimJoint248)
HAnimJoint287 = HAnimJoint()
HAnimJoint287.setName("Neck")
HAnimJoint287.setDEF("Bvh1_Neck")
HAnimJoint287.setCenter([0,53.339999,0])
HAnimJoint287.setStiffness([0,0,0])
#BVH JOINT Neck, OFFSET 0.0 38.099999 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment288 = HAnimSegment()
HAnimSegment288.setName("Chest2_to_Neck")
HAnimSegment288.setDEF("Bvh1_Chest2_to_Neck")
#Visualization sphere for <HAnimJoint name='Neck'/> is placed within <HAnimSegment name='Chest2_to_Neck'/>
TouchSensor289 = TouchSensor()
TouchSensor289.setDescription("HAnimJoint Neck, HAnimSegment Chest2_to_Neck")

HAnimSegment288.addChildren(TouchSensor289)
Transform290 = Transform()
Transform290.setTranslation([0,53.339999,0])
Shape291 = Shape()
Shape291.setUSE("HAnimJointShape")

Transform290.addChildren(Shape291)

HAnimSegment288.addChildren(Transform290)
#HAnimSegment visualization line from current <HAnimJoint name='Neck'/> to child <HAnimJoint name='skullbase'/>
Shape292 = Shape()
LineSet293 = LineSet()
LineSet293.setVertexCount([2])
Coordinate294 = Coordinate()
Coordinate294.setPoint([0,53.339999,0,0,69.849999,0])

LineSet293.setCoord(Coordinate294)
ColorRGBA295 = ColorRGBA()
ColorRGBA295.setUSE("HAnimSegmentLineColorRGBA")

LineSet293.setColor(ColorRGBA295)

Shape292.setGeometry(LineSet293)

HAnimSegment288.addChildren(Shape292)
Transform296 = Transform()
Transform296.setTranslation([0,53.339999,0])
#insert Shape geometry here

HAnimSegment288.addChildren(Transform296)

HAnimJoint287.addChildren(HAnimSegment288)
HAnimJoint297 = HAnimJoint()
HAnimJoint297.setName("skullbase")
HAnimJoint297.setDEF("Bvh1_skullbase")
HAnimJoint297.setCenter([0,69.849999,0])
HAnimJoint297.setStiffness([0,0,0])
#BVH JOINT Head, OFFSET 0.0 16.51 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment298 = HAnimSegment()
HAnimSegment298.setName("skull")
HAnimSegment298.setDEF("Bvh1_skull")
#Visualization sphere for <HAnimJoint name='skullbase'/> is placed within <HAnimSegment name='skull'/>
TouchSensor299 = TouchSensor()
TouchSensor299.setDescription("HAnimJoint skullbase, HAnimSegment skull")

HAnimSegment298.addChildren(TouchSensor299)
Transform300 = Transform()
Transform300.setTranslation([0,69.849999,0])
Shape301 = Shape()
Shape301.setUSE("HAnimJointShape")

Transform300.addChildren(Shape301)

HAnimSegment298.addChildren(Transform300)
Transform302 = Transform()
Transform302.setTranslation([0,69.849999,0])
HAnimSite303 = HAnimSite()
HAnimSite303.setName("skull_tip")
HAnimSite303.setDEF("Bvh1_skull_tip")
HAnimSite303.setTranslation([0,10.16,0])
#BVH End Site OFFSET (0.0, 10.16, 0.0)
#HAnimSite visualization shape
TouchSensor304 = TouchSensor()
TouchSensor304.setDescription("HAnimSite skull_tip")

HAnimSite303.addChildren(TouchSensor304)
Shape305 = Shape()
Shape305.setUSE("HAnimSiteShape")

HAnimSite303.addChildren(Shape305)

Transform302.addChildren(HAnimSite303)

HAnimSegment298.addChildren(Transform302)

HAnimJoint297.addChildren(HAnimSegment298)

HAnimJoint287.addChildren(HAnimJoint297)

HAnimJoint191.addChildren(HAnimJoint287)

HAnimJoint181.addChildren(HAnimJoint191)

HAnimJoint67.addChildren(HAnimJoint181)

HAnimHumanoid60.setSkeleton(HAnimJoint67)
HAnimSite306 = HAnimSite()
HAnimSite306.setName("HumanoidRoot_view")
HAnimSite306.setDEF("Bvh1_HumanoidRoot_view")
#HAnimSite visualization shape
TouchSensor307 = TouchSensor()
TouchSensor307.setDescription("HAnimSite HumanoidRoot_view")

HAnimSite306.addChildren(TouchSensor307)
Shape308 = Shape()
Shape308.setUSE("HAnimSiteShape")

HAnimSite306.addChildren(Shape308)
Viewpoint309 = Viewpoint()
Viewpoint309.setDEF("Bvh1_HumanoidRoot_viewpoint")
Viewpoint309.setDescription("Bvh1 front view towards HAnimHumanoid center")
Viewpoint309.setPosition([0,0,314.96062992125985])

HAnimSite306.addChildren(Viewpoint309)
#HAnimSite/Viewpoint visualization shape
Anchor310 = Anchor()
Anchor310.setDescription("HAnimSite Bvh1_HumanoidRoot_view Viewpoint")
Anchor310.setUrl(["#Bvh1_HumanoidRoot_viewpoint"])
LOD311 = LOD()
LOD311.setForceTransitions(True)
LOD311.setRange([0.04])
WorldInfo312 = WorldInfo()
WorldInfo312.setInfo(["hide diamond when close"])

LOD311.addChildren(WorldInfo312)
Shape313 = Shape()
Shape313.setDEF("HAnimSiteViewpointShape")
IndexedFaceSet314 = IndexedFaceSet()
IndexedFaceSet314.setDEF("SiteViewpointDiamondIFS")
IndexedFaceSet314.setCoordIndex([0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1])
IndexedFaceSet314.setCreaseAngle(0.5)
Coordinate315 = Coordinate()
Coordinate315.setPoint([0,0.01,0,-0.01,0,0,0,0,0.01,0.01,0,0,0,0,-0.01,0,-0.01,0])

IndexedFaceSet314.setCoord(Coordinate315)

Shape313.setGeometry(IndexedFaceSet314)
Appearance316 = Appearance()
Material317 = Material()
Material317.setDiffuseColor([1,1,0])
Material317.setTransparency(0.3)

Appearance316.setMaterial(Material317)

Shape313.setAppearance(Appearance316)

LOD311.addChildren(Shape313)

Anchor310.addChildren(LOD311)

HAnimSite306.addChildren(Anchor310)

HAnimHumanoid60.addViewpoints(HAnimSite306)
HAnimJoint318 = HAnimJoint()
HAnimJoint318.setUSE("Bvh1_HumanoidRoot")

HAnimHumanoid60.addJoints(HAnimJoint318)
HAnimJoint319 = HAnimJoint()
HAnimJoint319.setUSE("Bvh1_vl5")

HAnimHumanoid60.addJoints(HAnimJoint319)
HAnimJoint320 = HAnimJoint()
HAnimJoint320.setUSE("Bvh1_Chest2")

HAnimHumanoid60.addJoints(HAnimJoint320)
HAnimJoint321 = HAnimJoint()
HAnimJoint321.setUSE("Bvh1_LeftCollar")

HAnimHumanoid60.addJoints(HAnimJoint321)
HAnimJoint322 = HAnimJoint()
HAnimJoint322.setUSE("Bvh1_RightCollar")

HAnimHumanoid60.addJoints(HAnimJoint322)
HAnimJoint323 = HAnimJoint()
HAnimJoint323.setUSE("Bvh1_Neck")

HAnimHumanoid60.addJoints(HAnimJoint323)
HAnimJoint324 = HAnimJoint()
HAnimJoint324.setUSE("Bvh1_skullbase")

HAnimHumanoid60.addJoints(HAnimJoint324)
HAnimJoint325 = HAnimJoint()
HAnimJoint325.setUSE("Bvh1_l_ankle")

HAnimHumanoid60.addJoints(HAnimJoint325)
HAnimJoint326 = HAnimJoint()
HAnimJoint326.setUSE("Bvh1_r_ankle")

HAnimHumanoid60.addJoints(HAnimJoint326)
HAnimJoint327 = HAnimJoint()
HAnimJoint327.setUSE("Bvh1_l_elbow")

HAnimHumanoid60.addJoints(HAnimJoint327)
HAnimJoint328 = HAnimJoint()
HAnimJoint328.setUSE("Bvh1_r_elbow")

HAnimHumanoid60.addJoints(HAnimJoint328)
HAnimJoint329 = HAnimJoint()
HAnimJoint329.setUSE("Bvh1_l_hip")

HAnimHumanoid60.addJoints(HAnimJoint329)
HAnimJoint330 = HAnimJoint()
HAnimJoint330.setUSE("Bvh1_r_hip")

HAnimHumanoid60.addJoints(HAnimJoint330)
HAnimJoint331 = HAnimJoint()
HAnimJoint331.setUSE("Bvh1_l_knee")

HAnimHumanoid60.addJoints(HAnimJoint331)
HAnimJoint332 = HAnimJoint()
HAnimJoint332.setUSE("Bvh1_r_knee")

HAnimHumanoid60.addJoints(HAnimJoint332)
HAnimJoint333 = HAnimJoint()
HAnimJoint333.setUSE("Bvh1_l_midtarsal")

HAnimHumanoid60.addJoints(HAnimJoint333)
HAnimJoint334 = HAnimJoint()
HAnimJoint334.setUSE("Bvh1_r_midtarsal")

HAnimHumanoid60.addJoints(HAnimJoint334)
HAnimJoint335 = HAnimJoint()
HAnimJoint335.setUSE("Bvh1_l_shoulder")

HAnimHumanoid60.addJoints(HAnimJoint335)
HAnimJoint336 = HAnimJoint()
HAnimJoint336.setUSE("Bvh1_r_shoulder")

HAnimHumanoid60.addJoints(HAnimJoint336)
HAnimJoint337 = HAnimJoint()
HAnimJoint337.setUSE("Bvh1_l_wrist")

HAnimHumanoid60.addJoints(HAnimJoint337)
HAnimJoint338 = HAnimJoint()
HAnimJoint338.setUSE("Bvh1_r_wrist")

HAnimHumanoid60.addJoints(HAnimJoint338)
HAnimSegment339 = HAnimSegment()
HAnimSegment339.setUSE("Bvh1_sacrum")

HAnimHumanoid60.addSegments(HAnimSegment339)
HAnimSegment340 = HAnimSegment()
HAnimSegment340.setUSE("Bvh1_l5")

HAnimHumanoid60.addSegments(HAnimSegment340)
HAnimSegment341 = HAnimSegment()
HAnimSegment341.setUSE("Bvh1_vl5_to_Chest2")

HAnimHumanoid60.addSegments(HAnimSegment341)
HAnimSegment342 = HAnimSegment()
HAnimSegment342.setUSE("Bvh1_Chest2_to_LeftCollar")

HAnimHumanoid60.addSegments(HAnimSegment342)
HAnimSegment343 = HAnimSegment()
HAnimSegment343.setUSE("Bvh1_Chest2_to_RightCollar")

HAnimHumanoid60.addSegments(HAnimSegment343)
HAnimSegment344 = HAnimSegment()
HAnimSegment344.setUSE("Bvh1_Chest2_to_Neck")

HAnimHumanoid60.addSegments(HAnimSegment344)
HAnimSegment345 = HAnimSegment()
HAnimSegment345.setUSE("Bvh1_skull")

HAnimHumanoid60.addSegments(HAnimSegment345)
HAnimSegment346 = HAnimSegment()
HAnimSegment346.setUSE("Bvh1_l_calf")

HAnimHumanoid60.addSegments(HAnimSegment346)
HAnimSegment347 = HAnimSegment()
HAnimSegment347.setUSE("Bvh1_r_calf")

HAnimHumanoid60.addSegments(HAnimSegment347)
HAnimSegment348 = HAnimSegment()
HAnimSegment348.setUSE("Bvh1_l_forearm")

HAnimHumanoid60.addSegments(HAnimSegment348)
HAnimSegment349 = HAnimSegment()
HAnimSegment349.setUSE("Bvh1_r_forearm")

HAnimHumanoid60.addSegments(HAnimSegment349)
HAnimSegment350 = HAnimSegment()
HAnimSegment350.setUSE("Bvh1_l_hand")

HAnimHumanoid60.addSegments(HAnimSegment350)
HAnimSegment351 = HAnimSegment()
HAnimSegment351.setUSE("Bvh1_r_hand")

HAnimHumanoid60.addSegments(HAnimSegment351)
HAnimSegment352 = HAnimSegment()
HAnimSegment352.setUSE("Bvh1_l_hindfoot")

HAnimHumanoid60.addSegments(HAnimSegment352)
HAnimSegment353 = HAnimSegment()
HAnimSegment353.setUSE("Bvh1_r_hindfoot")

HAnimHumanoid60.addSegments(HAnimSegment353)
HAnimSegment354 = HAnimSegment()
HAnimSegment354.setUSE("Bvh1_l_middistal")

HAnimHumanoid60.addSegments(HAnimSegment354)
HAnimSegment355 = HAnimSegment()
HAnimSegment355.setUSE("Bvh1_r_middistal")

HAnimHumanoid60.addSegments(HAnimSegment355)
HAnimSegment356 = HAnimSegment()
HAnimSegment356.setUSE("Bvh1_l_thigh")

HAnimHumanoid60.addSegments(HAnimSegment356)
HAnimSegment357 = HAnimSegment()
HAnimSegment357.setUSE("Bvh1_r_thigh")

HAnimHumanoid60.addSegments(HAnimSegment357)
HAnimSegment358 = HAnimSegment()
HAnimSegment358.setUSE("Bvh1_l_upperarm")

HAnimHumanoid60.addSegments(HAnimSegment358)
HAnimSegment359 = HAnimSegment()
HAnimSegment359.setUSE("Bvh1_r_upperarm")

HAnimHumanoid60.addSegments(HAnimSegment359)
HAnimSite360 = HAnimSite()
HAnimSite360.setUSE("Bvh1_HumanoidRoot_view")

HAnimHumanoid60.addSites(HAnimSite360)
HAnimSite361 = HAnimSite()
HAnimSite361.setUSE("Bvh1_skull_tip")

HAnimHumanoid60.addSites(HAnimSite361)
HAnimSite362 = HAnimSite()
HAnimSite362.setUSE("Bvh1_l_hand_tip")

HAnimHumanoid60.addSites(HAnimSite362)
HAnimSite363 = HAnimSite()
HAnimSite363.setUSE("Bvh1_r_hand_tip")

HAnimHumanoid60.addSites(HAnimSite363)
HAnimSite364 = HAnimSite()
HAnimSite364.setUSE("Bvh1_l_middistal_tip")

HAnimHumanoid60.addSites(HAnimSite364)
HAnimSite365 = HAnimSite()
HAnimSite365.setUSE("Bvh1_r_middistal_tip")

HAnimHumanoid60.addSites(HAnimSite365)

Scene26.addChildren(HAnimHumanoid60)
#=============================================================
#testAxisAngleRotation() results compared to RotationTests.x3d
#getAxisAngleRotation(-4.40030,-0.38161,-1.82953) = (0.4067064033441406, -0.7164490591980798, -0.566825058596618, 2.6752961450535095), expected rotation: 0.40671 -0.71645 -0.56683 2.6753
#getAxisAngleRotation(5.80115,2.55377,2.83223) = (-0.9645827419506009, 0.07774106101143803, 0.2520643992393143, 2.59673649727989), expected rotation: -0.96458 0.07774 0.25206 2.59674
#getAxisAngleRotation(-3.76620,-3.47408,-3.93998) = (0.4075772844419879, -0.491492223290994, -0.7696207843161272, 1.1286216623422884), expected rotation: 0.40758 -0.49149 -0.76962 1.12862
#=============================================================
Group366 = Group()
Group366.setDEF("Bvh1_MotionGroup")
#BVH MOTION
#BVH Frames: 286
#BVH Frame Time: 0.016667 seconds (60.00 frames per second)
#Expected frame count: 286, actual frame count: 286, animation total duration: 4.767 seconds
#Frame width: 22 triplet values
#Total count: 66 * 286 = 18876 recorded motion values
#Animation playback: enable RealTimer for continuous motion at 60.000 frames/second (fps)
TimeSensor367 = TimeSensor()
TimeSensor367.setDEF("RealTimer")
TimeSensor367.setCycleInterval(4.767)
TimeSensor367.setLoop(True)

Group366.addChildren(TimeSensor367)
#Alternative replay: enable StepTimer for discrete time-step motion at 1 fps
TimeSensor368 = TimeSensor()
TimeSensor368.setDEF("StepTimer")
TimeSensor368.setCycleInterval(286)
TimeSensor368.setEnabled(False)
TimeSensor368.setLoop(True)

Group366.addChildren(TimeSensor368)
ScalarInterpolator369 = ScalarInterpolator()
ScalarInterpolator369.setDEF("FrameStepper")
ScalarInterpolator369.setKey([0,0.0035,0.0035,0.007,0.007,0.0105,0.0105,0.014,0.014,0.0175,0.0175,0.0211,0.0211,0.0246,0.0246,0.0281,0.0281,0.0316,0.0316,0.0351,0.0351,0.0386,0.0386,0.0421,0.0421,0.0456,0.0456,0.0491,0.0491,0.0526,0.0526,0.0561,0.0561,0.0596,0.0596,0.0632,0.0632,0.0667,0.0667,0.0702,0.0702,0.0737,0.0737,0.0772,0.0772,0.0807,0.0807,0.0842,0.0842,0.0877,0.0877,0.0912,0.0912,0.0947,0.0947,0.0982,0.0982,0.1018,0.1018,0.1053,0.1053,0.1088,0.1088,0.1123,0.1123,0.1158,0.1158,0.1193,0.1193,0.1228,0.1228,0.1263,0.1263,0.1298,0.1298,0.1333,0.1333,0.1368,0.1368,0.1404,0.1404,0.1439,0.1439,0.1474,0.1474,0.1509,0.1509,0.1544,0.1544,0.1579,0.1579,0.1614,0.1614,0.1649,0.1649,0.1684,0.1684,0.1719,0.1719,0.1754,0.1754,0.1789,0.1789,0.1825,0.1825,0.186,0.186,0.1895,0.1895,0.193,0.193,0.1965,0.1965,0.2,0.2,0.2035,0.2035,0.207,0.207,0.2105,0.2105,0.214,0.214,0.2175,0.2175,0.2211,0.2211,0.2246,0.2246,0.2281,0.2281,0.2316,0.2316,0.2351,0.2351,0.2386,0.2386,0.2421,0.2421,0.2456,0.2456,0.2491,0.2491,0.2526,0.2526,0.2561,0.2561,0.2596,0.2596,0.2632,0.2632,0.2667,0.2667,0.2702,0.2702,0.2737,0.2737,0.2772,0.2772,0.2807,0.2807,0.2842,0.2842,0.2877,0.2877,0.2912,0.2912,0.2947,0.2947,0.2982,0.2982,0.3018,0.3018,0.3053,0.3053,0.3088,0.3088,0.3123,0.3123,0.3158,0.3158,0.3193,0.3193,0.3228,0.3228,0.3263,0.3263,0.3298,0.3298,0.3333,0.3333,0.3368,0.3368,0.3404,0.3404,0.3439,0.3439,0.3474,0.3474,0.3509,0.3509,0.3544,0.3544,0.3579,0.3579,0.3614,0.3614,0.3649,0.3649,0.3684,0.3684,0.3719,0.3719,0.3754,0.3754,0.3789,0.3789,0.3825,0.3825,0.386,0.386,0.3895,0.3895,0.393,0.393,0.3965,0.3965,0.4,0.4,0.4035,0.4035,0.407,0.407,0.4105,0.4105,0.414,0.414,0.4175,0.4175,0.4211,0.4211,0.4246,0.4246,0.4281,0.4281,0.4316,0.4316,0.4351,0.4351,0.4386,0.4386,0.4421,0.4421,0.4456,0.4456,0.4491,0.4491,0.4526,0.4526,0.4561,0.4561,0.4596,0.4596,0.4632,0.4632,0.4667,0.4667,0.4702,0.4702,0.4737,0.4737,0.4772,0.4772,0.4807,0.4807,0.4842,0.4842,0.4877,0.4877,0.4912,0.4912,0.4947,0.4947,0.4982,0.4982,0.5018,0.5018,0.5053,0.5053,0.5088,0.5088,0.5123,0.5123,0.5158,0.5158,0.5193,0.5193,0.5228,0.5228,0.5263,0.5263,0.5298,0.5298,0.5333,0.5333,0.5368,0.5368,0.5404,0.5404,0.5439,0.5439,0.5474,0.5474,0.5509,0.5509,0.5544,0.5544,0.5579,0.5579,0.5614,0.5614,0.5649,0.5649,0.5684,0.5684,0.5719,0.5719,0.5754,0.5754,0.5789,0.5789,0.5825,0.5825,0.586,0.586,0.5895,0.5895,0.593,0.593,0.5965,0.5965,0.6,0.6,0.6035,0.6035,0.607,0.607,0.6105,0.6105,0.614,0.614,0.6175,0.6175,0.6211,0.6211,0.6246,0.6246,0.6281,0.6281,0.6316,0.6316,0.6351,0.6351,0.6386,0.6386,0.6421,0.6421,0.6456,0.6456,0.6491,0.6491,0.6526,0.6526,0.6561,0.6561,0.6596,0.6596,0.6632,0.6632,0.6667,0.6667,0.6702,0.6702,0.6737,0.6737,0.6772,0.6772,0.6807,0.6807,0.6842,0.6842,0.6877,0.6877,0.6912,0.6912,0.6947,0.6947,0.6982,0.6982,0.7018,0.7018,0.7053,0.7053,0.7088,0.7088,0.7123,0.7123,0.7158,0.7158,0.7193,0.7193,0.7228,0.7228,0.7263,0.7263,0.7298,0.7298,0.7333,0.7333,0.7368,0.7368,0.7404,0.7404,0.7439,0.7439,0.7474,0.7474,0.7509,0.7509,0.7544,0.7544,0.7579,0.7579,0.7614,0.7614,0.7649,0.7649,0.7684,0.7684,0.7719,0.7719,0.7754,0.7754,0.7789,0.7789,0.7825,0.7825,0.786,0.786,0.7895,0.7895,0.793,0.793,0.7965,0.7965,0.8,0.8,0.8035,0.8035,0.807,0.807,0.8105,0.8105,0.814,0.814,0.8175,0.8175,0.8211,0.8211,0.8246,0.8246,0.8281,0.8281,0.8316,0.8316,0.8351,0.8351,0.8386,0.8386,0.8421,0.8421,0.8456,0.8456,0.8491,0.8491,0.8526,0.8526,0.8561,0.8561,0.8596,0.8596,0.8632,0.8632,0.8667,0.8667,0.8702,0.8702,0.8737,0.8737,0.8772,0.8772,0.8807,0.8807,0.8842,0.8842,0.8877,0.8877,0.8912,0.8912,0.8947,0.8947,0.8982,0.8982,0.9018,0.9018,0.9053,0.9053,0.9088,0.9088,0.9123,0.9123,0.9158,0.9158,0.9193,0.9193,0.9228,0.9228,0.9263,0.9263,0.9298,0.9298,0.9333,0.9333,0.9368,0.9368,0.9404,0.9404,0.9439,0.9439,0.9474,0.9474,0.9509,0.9509,0.9544,0.9544,0.9579,0.9579,0.9614,0.9614,0.9649,0.9649,0.9684,0.9684,0.9719,0.9719,0.9754,0.9754,0.9789,0.9789,0.9825,0.9825,0.986,0.986,0.9895,0.9895,0.993,0.993,0.9965,0.9965,1,1])
ScalarInterpolator369.setKeyValue([0,0,0.0035,0.0035,0.007,0.007,0.0105,0.0105,0.014,0.014,0.0175,0.0175,0.0211,0.0211,0.0246,0.0246,0.0281,0.0281,0.0316,0.0316,0.0351,0.0351,0.0386,0.0386,0.0421,0.0421,0.0456,0.0456,0.0491,0.0491,0.0526,0.0526,0.0561,0.0561,0.0596,0.0596,0.0632,0.0632,0.0667,0.0667,0.0702,0.0702,0.0737,0.0737,0.0772,0.0772,0.0807,0.0807,0.0842,0.0842,0.0877,0.0877,0.0912,0.0912,0.0947,0.0947,0.0982,0.0982,0.1018,0.1018,0.1053,0.1053,0.1088,0.1088,0.1123,0.1123,0.1158,0.1158,0.1193,0.1193,0.1228,0.1228,0.1263,0.1263,0.1298,0.1298,0.1333,0.1333,0.1368,0.1368,0.1404,0.1404,0.1439,0.1439,0.1474,0.1474,0.1509,0.1509,0.1544,0.1544,0.1579,0.1579,0.1614,0.1614,0.1649,0.1649,0.1684,0.1684,0.1719,0.1719,0.1754,0.1754,0.1789,0.1789,0.1825,0.1825,0.186,0.186,0.1895,0.1895,0.193,0.193,0.1965,0.1965,0.2,0.2,0.2035,0.2035,0.207,0.207,0.2105,0.2105,0.214,0.214,0.2175,0.2175,0.2211,0.2211,0.2246,0.2246,0.2281,0.2281,0.2316,0.2316,0.2351,0.2351,0.2386,0.2386,0.2421,0.2421,0.2456,0.2456,0.2491,0.2491,0.2526,0.2526,0.2561,0.2561,0.2596,0.2596,0.2632,0.2632,0.2667,0.2667,0.2702,0.2702,0.2737,0.2737,0.2772,0.2772,0.2807,0.2807,0.2842,0.2842,0.2877,0.2877,0.2912,0.2912,0.2947,0.2947,0.2982,0.2982,0.3018,0.3018,0.3053,0.3053,0.3088,0.3088,0.3123,0.3123,0.3158,0.3158,0.3193,0.3193,0.3228,0.3228,0.3263,0.3263,0.3298,0.3298,0.3333,0.3333,0.3368,0.3368,0.3404,0.3404,0.3439,0.3439,0.3474,0.3474,0.3509,0.3509,0.3544,0.3544,0.3579,0.3579,0.3614,0.3614,0.3649,0.3649,0.3684,0.3684,0.3719,0.3719,0.3754,0.3754,0.3789,0.3789,0.3825,0.3825,0.386,0.386,0.3895,0.3895,0.393,0.393,0.3965,0.3965,0.4,0.4,0.4035,0.4035,0.407,0.407,0.4105,0.4105,0.414,0.414,0.4175,0.4175,0.4211,0.4211,0.4246,0.4246,0.4281,0.4281,0.4316,0.4316,0.4351,0.4351,0.4386,0.4386,0.4421,0.4421,0.4456,0.4456,0.4491,0.4491,0.4526,0.4526,0.4561,0.4561,0.4596,0.4596,0.4632,0.4632,0.4667,0.4667,0.4702,0.4702,0.4737,0.4737,0.4772,0.4772,0.4807,0.4807,0.4842,0.4842,0.4877,0.4877,0.4912,0.4912,0.4947,0.4947,0.4982,0.4982,0.5018,0.5018,0.5053,0.5053,0.5088,0.5088,0.5123,0.5123,0.5158,0.5158,0.5193,0.5193,0.5228,0.5228,0.5263,0.5263,0.5298,0.5298,0.5333,0.5333,0.5368,0.5368,0.5404,0.5404,0.5439,0.5439,0.5474,0.5474,0.5509,0.5509,0.5544,0.5544,0.5579,0.5579,0.5614,0.5614,0.5649,0.5649,0.5684,0.5684,0.5719,0.5719,0.5754,0.5754,0.5789,0.5789,0.5825,0.5825,0.586,0.586,0.5895,0.5895,0.593,0.593,0.5965,0.5965,0.6,0.6,0.6035,0.6035,0.607,0.607,0.6105,0.6105,0.614,0.614,0.6175,0.6175,0.6211,0.6211,0.6246,0.6246,0.6281,0.6281,0.6316,0.6316,0.6351,0.6351,0.6386,0.6386,0.6421,0.6421,0.6456,0.6456,0.6491,0.6491,0.6526,0.6526,0.6561,0.6561,0.6596,0.6596,0.6632,0.6632,0.6667,0.6667,0.6702,0.6702,0.6737,0.6737,0.6772,0.6772,0.6807,0.6807,0.6842,0.6842,0.6877,0.6877,0.6912,0.6912,0.6947,0.6947,0.6982,0.6982,0.7018,0.7018,0.7053,0.7053,0.7088,0.7088,0.7123,0.7123,0.7158,0.7158,0.7193,0.7193,0.7228,0.7228,0.7263,0.7263,0.7298,0.7298,0.7333,0.7333,0.7368,0.7368,0.7404,0.7404,0.7439,0.7439,0.7474,0.7474,0.7509,0.7509,0.7544,0.7544,0.7579,0.7579,0.7614,0.7614,0.7649,0.7649,0.7684,0.7684,0.7719,0.7719,0.7754,0.7754,0.7789,0.7789,0.7825,0.7825,0.786,0.786,0.7895,0.7895,0.793,0.793,0.7965,0.7965,0.8,0.8,0.8035,0.8035,0.807,0.807,0.8105,0.8105,0.814,0.814,0.8175,0.8175,0.8211,0.8211,0.8246,0.8246,0.8281,0.8281,0.8316,0.8316,0.8351,0.8351,0.8386,0.8386,0.8421,0.8421,0.8456,0.8456,0.8491,0.8491,0.8526,0.8526,0.8561,0.8561,0.8596,0.8596,0.8632,0.8632,0.8667,0.8667,0.8702,0.8702,0.8737,0.8737,0.8772,0.8772,0.8807,0.8807,0.8842,0.8842,0.8877,0.8877,0.8912,0.8912,0.8947,0.8947,0.8982,0.8982,0.9018,0.9018,0.9053,0.9053,0.9088,0.9088,0.9123,0.9123,0.9158,0.9158,0.9193,0.9193,0.9228,0.9228,0.9263,0.9263,0.9298,0.9298,0.9333,0.9333,0.9368,0.9368,0.9404,0.9404,0.9439,0.9439,0.9474,0.9474,0.9509,0.9509,0.9544,0.9544,0.9579,0.9579,0.9614,0.9614,0.9649,0.9649,0.9684,0.9684,0.9719,0.9719,0.9754,0.9754,0.9789,0.9789,0.9825,0.9825,0.986,0.986,0.9895,0.9895,0.993,0.993,0.9965,0.9965,1])

Group366.addChildren(ScalarInterpolator369)
ROUTE370 = ROUTE()
ROUTE370.setFromField("fraction_changed")
ROUTE370.setFromNode("StepTimer")
ROUTE370.setToField("set_fraction")
ROUTE370.setToNode("FrameStepper")

Group366.addChildren(ROUTE370)
#Interpolator0_HIERARCHY_Hips channels [0..2] sends animation values to BVH JOINT Hips, DEF Bvh1_Hips, <HAnimJoint name=HIERARCHY_Hips/>
PositionInterpolator371 = PositionInterpolator()
PositionInterpolator371.setDEF("Interpolator0_HIERARCHY_Hips")
PositionInterpolator371.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
PositionInterpolator371.setKeyValue([0.0387,2.4231,-0.0129,0.0387,2.4231,-0.0129,0.0389,2.423,-0.0116,0.039,2.4229,-0.009,0.0416,2.423,-0.0107,0.041,2.423,-0.0135,0.0432,2.423,-0.0179,0.043,2.4231,-0.0222,0.0456,2.423,-0.0246,0.0485,2.4232,-0.0267,0.0534,2.4232,-0.0277,0.0561,2.4231,-0.0255,0.0595,2.4233,-0.0251,0.0646,2.4234,-0.0259,0.0678,2.4236,-0.0253,0.0724,2.424,-0.0238,0.0757,2.4242,-0.0207,0.0788,2.4246,-0.0178,0.079,2.4253,-0.0147,0.0778,2.4259,-0.0092,0.0759,2.4263,-0.004,0.0753,2.4269,0.0039,0.0732,2.4267,0.0092,0.071,2.4264,0.0107,0.0695,2.4258,0.0092,0.0681,2.4251,0.0071,0.0683,2.4245,0.0042,0.0693,2.4237,0.0039,0.0698,2.4239,0.0056,0.0698,2.4242,0.0083,0.0712,2.4245,0.0095,0.074,2.4254,0.0158,0.0779,2.4264,0.0196,0.0845,2.4271,0.0264,0.0895,2.4275,0.033,0.0931,2.4275,0.0398,0.0964,2.4273,0.0484,0.0994,2.4267,0.0581,0.1015,2.4285,0.0674,0.1038,2.4304,0.0769,0.1048,2.4317,0.087,0.1074,2.4322,0.097,0.1098,2.432,0.1055,0.119,2.4333,0.1089,0.1277,2.4332,0.112,0.1368,2.4333,0.1153,0.1455,2.4326,0.1194,0.1518,2.432,0.124,0.1548,2.4302,0.1308,0.1584,2.4281,0.1384,0.1623,2.4255,0.1452,0.1661,2.422,0.1524,0.1718,2.4181,0.1596,0.1767,2.4163,0.1699,0.1798,2.4141,0.1791,0.1849,2.4129,0.1893,0.1888,2.4123,0.1973,0.1932,2.4111,0.2067,0.1996,2.4103,0.2168,0.2052,2.4095,0.2299,0.2115,2.4075,0.2456,0.2186,2.4049,0.2628,0.2271,2.4025,0.2809,0.2358,2.4001,0.2976,0.2467,2.3978,0.3174,0.2583,2.395,0.3394,0.2699,2.3924,0.3614,0.2822,2.3906,0.3854,0.2967,2.3885,0.4097,0.3125,2.3872,0.4364,0.3304,2.3867,0.4629,0.3502,2.3863,0.4889,0.3761,2.3858,0.515,0.4041,2.3856,0.5424,0.4328,2.3845,0.5693,0.4605,2.3814,0.5953,0.4883,2.3764,0.6212,0.5163,2.3694,0.6467,0.5343,2.3655,0.6718,0.5316,2.3719,0.6968,0.5334,2.3778,0.7206,0.5339,2.3829,0.7439,0.5356,2.3878,0.7651,0.5368,2.3925,0.7868,0.536,2.3977,0.8098,0.5365,2.403,0.834,0.5373,2.4077,0.8581,0.5378,2.4123,0.8811,0.5385,2.4173,0.9057,0.5375,2.4211,0.9303,0.5369,2.4244,0.9536,0.5363,2.4269,0.9757,0.5368,2.4291,0.9978,0.5364,2.4306,1.0188,0.5361,2.4318,1.0378,0.5364,2.4321,1.0583,0.5386,2.4324,1.0796,0.5396,2.4326,1.0992,0.5434,2.4327,1.1223,0.5483,2.4326,1.1445,0.5521,2.4325,1.1709,0.556,2.4322,1.1983,0.5615,2.4316,1.227,0.5654,2.43,1.2584,0.5726,2.4284,1.2882,0.5804,2.4267,1.3185,0.5887,2.4241,1.3492,0.5935,2.4214,1.3807,0.6013,2.418,1.4142,0.6096,2.4141,1.4506,0.6185,2.4105,1.4854,0.6271,2.4071,1.5215,0.6381,2.4029,1.5598,0.6482,2.3995,1.5987,0.663,2.3975,1.6381,0.6792,2.3959,1.6793,0.6972,2.3938,1.7216,0.7209,2.3909,1.7646,0.7448,2.3872,1.8076,0.7687,2.3818,1.8504,0.7932,2.3743,1.892,0.8098,2.3739,1.9276,0.8197,2.3812,1.9544,0.8287,2.3871,1.9792,0.8396,2.3926,2.0033,0.8512,2.3975,2.0263,0.863,2.4024,2.0486,0.8736,2.4067,2.0714,0.8825,2.4104,2.0936,0.8911,2.4138,2.115,0.8997,2.4168,2.1373,0.9093,2.4197,2.1596,0.9191,2.4227,2.1829,0.9303,2.4252,2.2059,0.9401,2.4278,2.2282,0.9492,2.43,2.2517,0.9588,2.4321,2.2798,0.9673,2.4336,2.3087,0.9769,2.4343,2.3373,0.9853,2.4348,2.3645,0.9926,2.4348,2.395,1.0005,2.4333,2.4281,1.0078,2.4312,2.4626,1.0166,2.4279,2.4989,1.0282,2.4237,2.5371,1.0392,2.4192,2.5716,1.0532,2.4142,2.607,1.0707,2.4081,2.6421,1.0905,2.4006,2.6783,1.11,2.3924,2.7147,1.132,2.3873,2.7541,1.1568,2.3825,2.7948,1.186,2.3783,2.8381,1.2173,2.3736,2.8834,1.2531,2.3696,2.9276,1.2918,2.3649,2.9703,1.3357,2.359,3.0106,1.3793,2.3525,3.0503,1.4218,2.3444,3.0901,1.4637,2.3347,3.1302,1.5053,2.3231,3.1699,1.52,2.3284,3.2145,1.5245,2.338,3.258,1.5298,2.3464,3.3007,1.5344,2.3537,3.3418,1.5393,2.3601,3.382,1.5437,2.3668,3.4154,1.5486,2.3727,3.4473,1.5543,2.378,3.479,1.5587,2.3835,3.5131,1.5631,2.3883,3.5478,1.5663,2.3934,3.5843,1.5686,2.3975,3.6193,1.5704,2.4006,3.6554,1.5721,2.4028,3.6914,1.5736,2.4035,3.7279,1.5755,2.4033,3.765,1.5769,2.403,3.8031,1.5799,2.4027,3.836,1.5817,2.4017,3.8706,1.5862,2.4001,3.9059,1.5906,2.398,3.9418,1.5943,2.3953,3.9783,1.5992,2.3922,4.0159,1.6052,2.3891,4.0566,1.6135,2.3855,4.0997,1.6195,2.3813,4.1435,1.6282,2.3771,4.1859,1.6373,2.373,4.2279,1.6487,2.3683,4.2706,1.6613,2.3637,4.3141,1.6762,2.3591,4.3586,1.6926,2.3549,4.4063,1.7092,2.3506,4.4563,1.7297,2.346,4.5077,1.7537,2.3408,4.5581,1.7777,2.3347,4.6073,1.8014,2.3276,4.6544,1.821,2.3378,4.6865,1.8387,2.3487,4.7217,1.8529,2.3595,4.7582,1.8672,2.3691,4.7939,1.8807,2.378,4.8288,1.8933,2.3853,4.8634,1.905,2.3905,4.8963,1.9168,2.3951,4.928,1.9267,2.4002,4.9512,1.9364,2.4054,4.9764,1.9441,2.4111,5.0035,1.9513,2.4159,5.031,1.9573,2.4202,5.0563,1.9598,2.4236,5.0811,1.9604,2.4273,5.1083,1.9638,2.4299,5.1333,1.9684,2.4318,5.1585,1.9718,2.4333,5.1837,1.9769,2.4343,5.2063,1.9799,2.4352,5.2307,1.9847,2.4355,5.2534,1.9918,2.4349,5.2764,2.0009,2.4343,5.3032,2.0103,2.4328,5.3307,2.023,2.4305,5.3599,2.0376,2.4276,5.3911,2.0533,2.4243,5.4222,2.069,2.4201,5.4538,2.0851,2.4152,5.4849,2.1005,2.4099,5.5148,2.1163,2.4036,5.546,2.1332,2.3987,5.5783,2.1518,2.3939,5.6114,2.169,2.3894,5.6446,2.1864,2.3865,5.6803,2.2073,2.383,5.7189,2.23,2.38,5.7615,2.257,2.378,5.802,2.2859,2.3754,5.8416,2.3176,2.3725,5.8823,2.3513,2.369,5.9194,2.3838,2.3646,5.955,2.416,2.3584,5.9906,2.4485,2.3502,6.0251,2.4805,2.3397,6.0583,2.4856,2.3465,6.0963,2.4886,2.3541,6.1329,2.4912,2.3608,6.1681,2.4941,2.3658,6.2026,2.4971,2.3689,6.2356,2.5001,2.3706,6.2675,2.503,2.3735,6.2952,2.5074,2.3768,6.3139,2.5119,2.3805,6.3338,2.5158,2.3842,6.3573,2.5186,2.3877,6.3844,2.5215,2.3909,6.4121,2.5243,2.3941,6.4401,2.5288,2.3961,6.461,2.5333,2.3979,6.4819,2.534,2.3991,6.5033,2.5346,2.3997,6.525,2.535,2.4002,6.5469,2.5366,2.4,6.568,2.539,2.4,6.59,2.5421,2.3998,6.6136,2.5458,2.3995,6.6376,2.5503,2.3992,6.6625,2.554,2.3985,6.6857,2.5594,2.3973,6.7091,2.5643,2.3959,6.7337,2.5682,2.3945,6.7583,2.5722,2.3923,6.7834,2.5786,2.3901,6.8095,2.5846,2.3875,6.8359,2.5917,2.3853,6.8619,2.5996,2.3844,6.8871,2.607,2.3843,6.9123,2.6141,2.384,6.9371,2.6229,2.3841,6.9606,2.6345,2.3841,6.985,2.6482,2.3837,7.0118,2.6636,2.387,7.0367,2.6706,2.3922,7.0563,2.6774,2.3963,7.0747,2.684,2.3999,7.0899,2.6903,2.4021,7.0997,2.6968,2.4038,7.107])

Group366.addChildren(PositionInterpolator371)
#Position triplet values, CHANNELS Xposition Yposition Zposition Zrotation Xrotation Yrotation, with min/max ranges [1.7976931348623157E308,4.9E-324], [1.7976931348623157E308,4.9E-324], [1.7976931348623157E308,4.9E-324] degrees
#1.524644 95.397761 -0.507247, 1.524644 95.397761 -0.507247, 1.531642 95.392907 -0.455451, 1.536651 95.390310 -0.353990, 1.635970 95.393905 -0.422713, 1.613231 95.393798 -0.530394, 1.701452 95.394980 -0.705016, 1.694725 95.398042 -0.875051, 1.795072 95.393808 -0.967489, 1.911313 95.402179 -1.052076, 2.101843 95.402557 -1.090820, 2.209312 95.398333 -1.003293, 2.343692 95.406375 -0.986640, 2.541407 95.411161 -1.019877, 2.670940 95.416849 -0.996071, 2.849001 95.433108 -0.938466, 2.978657 95.442254 -0.815843, 3.103978 95.456294 -0.699048, 3.108427 95.483947 -0.577880, 3.063617 95.508510 -0.361170, 2.987453 95.525253 -0.159291, 2.963545 95.545291 0.154905, 2.882266 95.537878 0.361733, 2.795358 95.525708 0.423056, 2.736351 95.503927 0.360759, 2.679144 95.474597 0.279759, 2.688164 95.452176 0.164168, 2.726807 95.422614 0.154911, 2.749113 95.427517 0.219507, 2.748040 95.439861 0.325306, 2.801936 95.452806 0.373057, 2.915216 95.488918 0.621190, 3.068299 95.526716 0.772324, 3.326345 95.553778 1.040487, 3.522513 95.570027 1.299668, 3.664174 95.572808 1.566910, 3.794184 95.563700 1.906918, 3.912936 95.538789 2.286155, 3.997214 95.610926 2.653914, 4.086375 95.684856 3.027425, 4.126404 95.736529 3.427126, 4.229044 95.755065 3.817114, 4.324466 95.748495 4.154011, 4.685616 95.797853 4.288347, 5.025683 95.796942 4.410415, 5.385478 95.799200 4.540750, 5.727035 95.773348 4.700784, 5.975542 95.747895 4.883212, 6.094952 95.678141 5.148433, 6.236034 95.595375 5.446863, 6.390408 95.491050 5.716755, 6.537691 95.352502 6.001115, 6.765692 95.202317 6.284258, 6.955140 95.129473 6.687456, 7.076889 95.043509 7.052399, 7.278605 94.997068 7.453431, 7.431958 94.971081 7.766989, 7.607177 94.925135 8.138173, 7.857586 94.893828 8.535513, 8.080230 94.861631 9.050066, 8.325060 94.784833 9.670038, 8.607172 94.679374 10.344639, 8.942562 94.586696 11.057101, 9.283855 94.493184 11.716877, 9.713364 94.400506 12.495485, 10.169141 94.289611 13.364058, 10.624406 94.188145 14.229451, 11.111318 94.118207 15.173661, 11.681664 94.036022 16.128606, 12.302880 93.983206 17.182784, 13.006071 93.963517 18.225621, 13.788966 93.950281 19.249553, 14.805500 93.930380 20.276559, 15.911036 93.921591 21.354990, 17.041059 93.876933 22.414244, 18.130399 93.756873 23.436871, 19.222698 93.559840 24.458042, 20.325261 93.282735 25.461781, 21.036642 93.129440 26.450435, 20.928158 93.380365 27.433180, 21.001634 93.613529 28.371289, 21.021309 93.814243 29.287349, 21.086193 94.007507 30.122560, 21.133509 94.192805 30.975994, 21.103869 94.397415 31.880612, 21.123909 94.606530 32.833766, 21.151792 94.792333 33.781566, 21.173107 94.973901 34.688965, 21.201334 95.168424 35.658380, 21.162395 95.320702 36.627262, 21.139681 95.448552 37.542577, 21.115213 95.546541 38.412398, 21.135054 95.634413 39.284980, 21.117323 95.691764 40.110211, 21.107544 95.740337 40.859327, 21.117960 95.750734 41.664133, 21.206205 95.764812 42.503645, 21.243843 95.771633 43.276529, 21.395620 95.775625 44.184730, 21.586109 95.771372 45.058528, 21.734698 95.766663 46.096924, 21.891381 95.757477 47.177628, 22.107669 95.732866 48.305767, 22.261383 95.667764 49.544436, 22.544295 95.606295 50.717533, 22.850926 95.540223 51.908652, 23.175487 95.438708 53.120013, 23.367919 95.331515 54.358595, 23.673702 95.198432 55.675496, 23.999448 95.041872 57.111009, 24.351037 94.900117 58.480480, 24.688200 94.766753 59.899744, 25.122749 94.601046 61.410548, 25.520191 94.468099 62.941690, 26.100805 94.391582 64.491920, 26.738523 94.326131 66.114452, 27.447161 94.245971 67.778468, 28.380491 94.129505 69.473413, 29.321640 93.984872 71.165447, 30.265720 93.771852 72.849772, 31.229438 93.476677 74.489173, 31.881183 93.461232 75.887930, 32.271680 93.747542 76.946344, 32.625777 93.981200 77.922723, 33.056569 94.198105 78.871541, 33.513404 94.389392 79.776907, 33.977741 94.583964 80.653511, 34.392910 94.753546 81.549818, 34.744267 94.898780 82.425520, 35.083258 95.032260 83.265885, 35.420272 95.149646 84.146413, 35.800377 95.263428 85.025187, 36.184719 95.381793 85.940238, 36.626603 95.480798 86.845851, 37.013360 95.580802 87.726272, 37.368741 95.667638 88.649442, 37.746484 95.753195 89.755634, 38.083375 95.812629 90.894228, 38.461671 95.838635 92.020835, 38.789606 95.859467 93.091564, 39.078145 95.858721 94.293080, 39.389141 95.800236 95.592778, 39.676848 95.717170 96.951038, 40.022724 95.586054 98.383024, 40.480239 95.420424 99.884948, 40.912468 95.245919 101.244594, 41.466184 95.048722 102.638462, 42.153066 94.806867 104.020791, 42.932422 94.512175 105.443378, 43.702133 94.187234 106.878320, 44.565627 93.987295 108.430841, 45.541653 93.798120 110.032119, 46.694310 93.633808 111.735368, 47.923310 93.449159 113.517895, 49.333674 93.291058 115.260831, 50.857239 93.107038 116.942318, 52.586644 92.872925 118.527996, 54.302557 92.617310 120.091912, 55.976258 92.300934 121.657010, 57.625668 91.918952 123.235858, 59.263702 91.462255 124.797875, 59.840872 91.667640 126.553911, 60.018002 92.046502 128.267208, 60.227360 92.378081 129.950438, 60.411336 92.665505 131.565998, 60.602768 92.918620 133.149584, 60.775412 93.182576 134.464416, 60.970129 93.414694 135.720774, 61.192010 93.621222 136.968139, 61.367726 93.837120 138.309899, 61.539712 94.029017 139.678594, 61.665392 94.230245 141.112741, 61.755348 94.388433 142.493907, 61.827257 94.511923 143.913617, 61.893130 94.600203 145.330652, 61.954076 94.627537 146.767929, 62.027841 94.618574 148.228460, 62.081597 94.606259 149.727806, 62.199483 94.595571 151.023338, 62.272022 94.555661 152.386597, 62.448232 94.492487 153.775980, 62.621671 94.410903 155.187473, 62.767616 94.301578 156.624207, 62.960143 94.181294 158.106393, 63.194940 94.059064 159.709522, 63.524130 93.915545 161.406812, 63.760720 93.750575 163.130428, 64.103170 93.586118 164.797671, 64.460144 93.423502 166.453151, 64.911240 93.240800 168.133010, 65.404810 93.058243 169.847072, 65.990642 92.878041 171.598845, 66.639618 92.710745 173.477374, 67.292897 92.545222 175.445761, 68.100009 92.362704 177.468855, 69.042994 92.156980 179.451524, 69.987568 91.917266 181.391542, 70.920089 91.637942 183.244180, 71.693782 92.041173 184.507320, 72.391593 92.468046 185.892100, 72.950062 92.892778 187.329260, 73.512726 93.272949 188.734698, 74.044845 93.622278 190.110777, 74.538380 93.907794 191.473407, 74.998149 94.115785 192.769529, 75.465577 94.295813 194.017476, 75.854594 94.495558 194.927343, 76.236436 94.701524 195.921430, 76.540865 94.924156 196.989969, 76.824026 95.115007 198.069128, 77.060784 95.283533 199.066858, 77.157692 95.417430 200.044608, 77.179488 95.562092 201.112353, 77.314437 95.663597 202.098243, 77.494804 95.741422 203.090081, 77.631108 95.800382 204.082443, 77.830544 95.839207 204.973241, 77.950304 95.873982 205.934869, 78.138383 95.886374 206.825396, 78.416947 95.862442 207.733538, 78.776373 95.838945 208.785877, 79.143947 95.780470 209.869900, 79.643776 95.687675 211.020469, 80.219070 95.574175 212.248786, 80.837497 95.443049 213.473750, 81.456296 95.279251 214.716852, 82.090230 95.088293 215.941661, 82.697742 94.878258 217.119593, 83.319283 94.629048 218.347347, 83.984950 94.436046 219.618103, 84.714634 94.247482 220.920000, 85.395561 94.072725 222.227537, 86.079057 93.955630 223.632044, 86.901216 93.820706 225.154819, 87.796985 93.699841 226.831926, 88.858625 93.620709 228.423767, 89.997451 93.520831 229.985067, 91.245049 93.404685 231.587973, 92.569242 93.269654 233.046392, 93.851189 93.094200 234.450221, 95.116489 92.852035 235.851376, 96.396712 92.528362 237.209122, 97.657526 92.115578 238.517182, 97.858589 92.381346 240.012924, 97.976470 92.682820 241.451557, 98.080252 92.946108 242.837674, 98.192212 93.140922 244.195110, 98.309172 93.263967 245.496659, 98.430802 93.330697 246.751233, 98.545049 93.444179 247.843841, 98.715339 93.575731 248.578951, 98.894699 93.719869 249.364000, 99.048207 93.866188 250.286870, 99.159169 94.005675 251.353666, 99.271991 94.128381 252.443560, 99.383322 94.255253 253.547020, 99.560007 94.335839 254.370206, 99.737951 94.406155 255.193547, 99.764268 94.451249 256.033961, 99.785962 94.477071 256.889200, 99.803558 94.496827 257.753294, 99.867798 94.489347 258.581674, 99.958839 94.487594 259.446970, 100.081060 94.480588 260.376293, 100.230237 94.469416 261.322650, 100.405546 94.454970 262.303365, 100.550159 94.430456 263.218096, 100.763848 94.382910 264.139106, 100.957034 94.325123 265.105152, 101.108604 94.269826 266.073678, 101.267083 94.183242 267.061079, 101.521098 94.099458 268.089369, 101.757809 93.996693 269.130022, 102.035999 93.909460 270.151684, 102.347995 93.875829 271.144356, 102.636001 93.869463 272.136253, 102.917476 93.857293 273.114333, 103.263676 93.861663 274.037649, 103.721972 93.862254 274.998249, 104.259536 93.848166 276.054309, 104.867018 93.976879 277.034249, 105.140926 94.179667 277.807225, 105.410667 94.342225 278.533382, 105.667647 94.485694 279.130768, 105.919260 94.572763 279.516946, 106.171861 94.636160 279.802413
#Interpolator1_HIERARCHY_Hips channels [3..5] sends animation values to BVH JOINT Hips, DEF Bvh1_Hips, <HAnimJoint name=HIERARCHY_Hips/>
OrientationInterpolator372 = OrientationInterpolator()
OrientationInterpolator372.setDEF("Interpolator1_HIERARCHY_Hips")
OrientationInterpolator372.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator372.setKeyValue([-0.9227,-0.0652,-0.3799,0.0833,-0.9227,-0.0652,-0.3799,0.0833,-0.9227,-0.0652,-0.3799,0.0833,-0.9227,-0.0652,-0.3799,0.0833,-0.9227,-0.0652,-0.3799,0.0833,-0.9228,-0.0763,-0.3778,0.0818,-0.9228,-0.0763,-0.3778,0.0818,-0.9228,-0.0763,-0.3778,0.0818,-0.9266,-0.0607,-0.3712,0.0806,-0.9302,-0.0445,-0.3643,0.0795,-0.9267,-0.0153,-0.3754,0.0781,-0.9276,0.0242,-0.3729,0.0774,-0.9238,0.0741,-0.3757,0.0752,-0.9219,0.1354,-0.363,0.0738,-0.9139,0.2048,-0.3505,0.0744,-0.8995,0.2762,-0.3386,0.0772,-0.8739,0.3582,-0.3286,0.0812,-0.8426,0.4254,-0.3303,0.0849,-0.7986,0.4938,-0.3442,0.0894,-0.7501,0.5511,-0.3655,0.0919,-0.7124,0.5953,-0.3717,0.0944,-0.6703,0.6267,-0.3974,0.0978,-0.6332,0.6495,-0.4209,0.0984,-0.5915,0.6736,-0.4432,0.0975,-0.5491,0.6931,-0.467,0.0937,-0.4933,0.7334,-0.4677,0.0892,-0.4543,0.7575,-0.4688,0.0839,-0.4678,0.754,-0.4611,0.0797,-0.4913,0.7284,-0.4776,0.0751,-0.5225,0.6805,-0.5137,0.0702,-0.5398,0.637,-0.5503,0.0655,-0.5324,0.5811,-0.6156,0.0632,-0.5201,0.5167,-0.6801,0.0615,-0.4818,0.4795,-0.7334,0.0624,-0.4374,0.4587,-0.7735,0.065,-0.424,0.4335,-0.7952,0.0681,-0.4076,0.4267,-0.8073,0.0726,-0.411,0.4375,-0.7998,0.0768,-0.3989,0.4524,-0.7976,0.0823,-0.3991,0.4733,-0.7853,0.0878,-0.4054,0.5042,-0.7626,0.0917,-0.3955,0.5481,-0.737,0.094,-0.398,0.5858,-0.706,0.0952,-0.3946,0.6086,-0.6884,0.098,-0.3958,0.629,-0.6691,0.0981,-0.3879,0.6435,-0.6598,0.098,-0.4092,0.6468,-0.6436,0.0971,-0.4306,0.6497,-0.6265,0.0963,-0.4651,0.6494,-0.6017,0.0944,-0.4866,0.651,-0.5826,0.0938,-0.5134,0.6495,-0.5608,0.0949,-0.5259,0.6648,-0.5305,0.0943,-0.5175,0.6794,-0.5202,0.0943,-0.5169,0.683,-0.5161,0.0975,-0.5138,0.6936,-0.5049,0.0992,-0.5133,0.6965,-0.5014,0.1024,-0.4984,0.7089,-0.4991,0.1051,-0.5098,0.7085,-0.4879,0.1073,-0.5068,0.7174,-0.478,0.1091,-0.5065,0.7193,-0.4755,0.1123,-0.5093,0.7297,-0.4563,0.1147,-0.5194,0.7286,-0.4466,0.1169,-0.5194,0.7286,-0.4466,0.1169,-0.5118,0.7393,-0.4376,0.1171,-0.5118,0.7393,-0.4376,0.1171,-0.489,0.7554,-0.4362,0.1166,-0.4782,0.7568,-0.4456,0.1143,-0.4749,0.7472,-0.4649,0.1119,-0.4905,0.7231,-0.4864,0.1084,-0.5196,0.6773,-0.5209,0.1035,-0.5632,0.6132,-0.554,0.0997,-0.5989,0.5556,-0.5767,0.0963,-0.6377,0.5124,-0.5751,0.0954,-0.6566,0.4898,-0.5736,0.095,-0.6574,0.511,-0.5538,0.0951,-0.6577,0.5317,-0.5336,0.0953,-0.6704,0.5457,-0.5028,0.0948,-0.6695,0.5654,-0.4818,0.0952,-0.6554,0.5966,-0.4632,0.0948,-0.6373,0.6298,-0.444,0.0928,-0.6227,0.6512,-0.4338,0.0893,-0.6101,0.6701,-0.4227,0.0876,-0.6108,0.6841,-0.3987,0.0852,-0.6212,0.6824,-0.3852,0.0827,-0.6321,0.6804,-0.3708,0.0803,-0.6552,0.6752,-0.3389,0.0756,-0.6829,0.6638,-0.3051,0.0727,-0.709,0.654,-0.2638,0.0683,-0.7366,0.6409,-0.2161,0.064,-0.7798,0.5982,-0.1847,0.0617,-0.8225,0.5509,-0.1416,0.0579,-0.8632,0.4905,-0.1192,0.0551,-0.9038,0.4231,-0.0649,0.0522,-0.9508,0.3069,-0.041,0.0489,-0.987,0.1604,-0.0002,0.0487,-1,0.0045,-0.0071,0.0496,-0.9897,-0.1423,-0.0135,0.0517,-0.9561,-0.2909,-0.0362,0.056,-0.9246,-0.3775,-0.0508,0.0611,-0.8854,-0.4585,-0.0759,0.068,-0.8541,-0.5133,-0.0844,0.074,-0.8247,-0.5582,-0.0913,0.0802,-0.8064,-0.5849,-0.0873,0.0868,-0.7826,-0.613,-0.1084,0.0922,-0.7644,-0.6336,-0.1189,0.0962,-0.7472,-0.6521,-0.1284,0.1003,-0.7433,-0.655,-0.1361,0.1019,-0.7308,-0.6656,-0.1515,0.1035,-0.7271,-0.668,-0.1586,0.1051,-0.7271,-0.668,-0.1586,0.1051,-0.7271,-0.668,-0.1586,0.1051,-0.7271,-0.668,-0.1586,0.1051,-0.7306,-0.6623,-0.1662,0.1024,-0.7342,-0.6562,-0.1742,0.0998,-0.7516,-0.6383,-0.1667,0.0957,-0.7838,-0.6008,-0.1572,0.0907,-0.812,-0.5627,-0.1548,0.0876,-0.8403,-0.5204,-0.1519,0.0846,-0.8564,-0.4888,-0.1663,0.0848,-0.8633,-0.4672,-0.1908,0.0849,-0.8546,-0.4706,-0.2193,0.0838,-0.8436,-0.4658,-0.2672,0.0819,-0.8252,-0.4838,-0.2915,0.08,-0.8114,-0.4952,-0.3104,0.0766,-0.8075,-0.4961,-0.3191,0.0733,-0.8116,-0.4791,-0.3344,0.0711,-0.8158,-0.4512,-0.3618,0.0715,-0.8343,-0.4223,-0.3545,0.0727,-0.8407,-0.4052,-0.3593,0.0738,-0.8423,-0.3777,-0.3845,0.0744,-0.8375,-0.3666,-0.4052,0.0739,-0.8441,-0.3274,-0.4246,0.0731,-0.8423,-0.2742,-0.4641,0.0722,-0.8472,-0.2076,-0.4891,0.0718,-0.8498,-0.1258,-0.5118,0.0732,-0.851,-0.0179,-0.5249,0.0755,-0.8392,0.112,-0.5322,0.0808,-0.8236,0.2298,-0.5186,0.0878,-0.8119,0.3202,-0.4882,0.0972,-0.7866,0.4006,-0.4699,0.1096,-0.7584,0.4749,-0.4464,0.1223,-0.7297,0.5471,-0.4102,0.1342,-0.699,0.6023,-0.3855,0.1463,-0.6681,0.6566,-0.3501,0.1597,-0.6394,0.6996,-0.3188,0.1739,-0.611,0.7337,-0.2972,0.1877,-0.5881,0.758,-0.2819,0.2,-0.5727,0.7766,-0.2626,0.2118,-0.5659,0.7858,-0.2494,0.222,-0.5592,0.7932,-0.241,0.2315,-0.5513,0.8025,-0.2281,0.2401,-0.5441,0.8089,-0.2229,0.2458,-0.5327,0.8164,-0.2228,0.2522,-0.5263,0.8201,-0.2247,0.255,-0.524,0.8198,-0.2308,0.2573,-0.5322,0.8121,-0.2394,0.2562,-0.5469,0.7985,-0.2517,0.2533,-0.5579,0.7857,-0.2671,0.2482,-0.571,0.7722,-0.2787,0.2439,-0.5842,0.7578,-0.2906,0.2397,-0.5935,0.7475,-0.2982,0.236,-0.5973,0.7436,-0.3004,0.2309,-0.6054,0.7342,-0.3073,0.2255,-0.6164,0.7257,-0.3056,0.2216,-0.6236,0.7169,-0.3119,0.2145,-0.6338,0.7091,-0.309,0.2089,-0.643,0.7025,-0.3049,0.2015,-0.6542,0.6936,-0.3015,0.196,-0.6679,0.6845,-0.2922,0.1913,-0.6801,0.6741,-0.2881,0.1858,-0.6887,0.667,-0.2843,0.1817,-0.6937,0.6652,-0.2762,0.1794,-0.6988,0.6632,-0.2679,0.1772,-0.704,0.6612,-0.2593,0.175,-0.7124,0.6508,-0.2625,0.1719,-0.7227,0.6406,-0.2594,0.1697,-0.7378,0.6249,-0.2551,0.1662,-0.7642,0.5921,-0.2559,0.1637,-0.7841,0.565,-0.257,0.1606,-0.808,0.5269,-0.2637,0.1578,-0.8309,0.4864,-0.2701,0.1553,-0.8526,0.4436,-0.2761,0.1532,-0.8758,0.3919,-0.2818,0.1544,-0.8976,0.3409,-0.2794,0.1549,-0.9145,0.2836,-0.2884,0.1546,-0.9267,0.2217,-0.3034,0.1541,-0.9306,0.1751,-0.3214,0.1533,-0.9341,0.1317,-0.3318,0.1535,-0.9343,0.0934,-0.3441,0.1526,-0.9313,0.0656,-0.3582,0.1522,-0.9307,0.0361,-0.3639,0.1538,-0.9298,0.002,-0.3681,0.154,-0.9339,-0.0334,-0.3559,0.1551,-0.9416,-0.0663,-0.3303,0.1557,-0.9495,-0.0909,-0.3003,0.1554,-0.9564,-0.1104,-0.2705,0.1539,-0.9597,-0.1355,-0.2463,0.152,-0.9618,-0.161,-0.2213,0.1503,-0.9603,-0.1925,-0.2018,0.1483,-0.9535,-0.2394,-0.1831,0.1465,-0.939,-0.301,-0.1662,0.1433,-0.9197,-0.3638,-0.1478,0.1407,-0.906,-0.4027,-0.1304,0.1413,-0.8949,-0.4276,-0.1276,0.1422,-0.8913,-0.4362,-0.1233,0.1411,-0.8872,-0.4428,-0.1295,0.1408,-0.8802,-0.446,-0.1624,0.14,-0.8673,-0.455,-0.2019,0.1391,-0.8557,-0.4496,-0.2561,0.1386,-0.8483,-0.4417,-0.292,0.1395,-0.8398,-0.4333,-0.3271,0.1406,-0.8397,-0.4137,-0.3519,0.1404,-0.8306,-0.3939,-0.3937,0.1398,-0.832,-0.3528,-0.4281,0.1392,-0.8369,-0.3047,-0.4547,0.1391,-0.845,-0.2544,-0.4704,0.1411,-0.8505,-0.2048,-0.4844,0.1435,-0.8596,-0.1442,-0.4902,0.1479,-0.8695,-0.0932,-0.485,0.153,-0.8803,-0.0462,-0.4722,0.1573,-0.8849,-0.0011,-0.4657,0.1631,-0.8916,0.0532,-0.4496,0.1687,-0.8958,0.1122,-0.43,0.1738,-0.8928,0.1698,-0.4173,0.1778,-0.887,0.2241,-0.4038,0.1824,-0.8818,0.2669,-0.3888,0.1868,-0.8771,0.2975,-0.3772,0.1905,-0.8708,0.3228,-0.3709,0.1918,-0.8647,0.3463,-0.3638,0.1915,-0.8559,0.3684,-0.3629,0.1924,-0.8433,0.3967,-0.3625,0.1944,-0.829,0.4342,-0.3525,0.1986,-0.8073,0.4718,-0.3546,0.2045,-0.7804,0.5101,-0.3616,0.2112,-0.7587,0.5416,-0.3621,0.2179,-0.7399,0.5647,-0.3656,0.2231,-0.7343,0.5739,-0.3627,0.2278,-0.7298,0.5761,-0.3682,0.23,-0.7331,0.569,-0.3726,0.232,-0.7436,0.5533,-0.3754,0.2318,-0.7512,0.5438,-0.3743,0.2316,-0.7542,0.54,-0.3737,0.2287,-0.7444,0.5496,-0.3792,0.2246,-0.7374,0.5521,-0.3892,0.2225,-0.737,0.5528,-0.3889,0.2207,-0.737,0.5528,-0.3889,0.2207,-0.737,0.5528,-0.3889,0.2207,-0.743,0.5421,-0.3927,0.2179,-0.7455,0.5391,-0.3919,0.2113,-0.7482,0.5359,-0.391,0.2047,-0.742,0.5444,-0.3912,0.1966,-0.7395,0.5475,-0.3916,0.1891,-0.7327,0.5563,-0.392,0.1828,-0.7296,0.5563,-0.3978,0.1785,-0.7262,0.5564,-0.4038,0.1742,-0.7289,0.5533,-0.4033,0.1676,-0.7361,0.5399,-0.4084,0.163,-0.7503,0.5216,-0.4063,0.1562,-0.7663,0.4888,-0.417,0.1491,-0.7827,0.4519,-0.428,0.1423,-0.8019,0.3989,-0.4448,0.1362,-0.8212,0.3295,-0.466,0.133,-0.8466,0.2554,-0.4669,0.1327,-0.8668,0.1799,-0.465,0.1332,-0.8816,0.1043,-0.4603,0.1344,-0.8923,0.0402,-0.4496,0.1355,-0.8903,-0.0211,-0.4549,0.1365,-0.8843,-0.0752,-0.4608,0.1367,-0.8736,-0.1258,-0.47,0.1357,-0.8551,-0.1825,-0.4852,0.1349,-0.8326,-0.2345,-0.5018,0.1331,-0.817,-0.278,-0.5052,0.1319,-0.7993,-0.3217,-0.5076,0.1309,-0.7824,-0.3524,-0.5135,0.13,-0.7758,-0.3748,-0.5076,0.1291,-0.776,-0.3913,-0.4946,0.1283,-0.787,-0.3921,-0.4763,0.1286,-0.7868,-0.4085,-0.4627,0.1279,-0.7745,-0.441,-0.4535,0.1261,-0.7538,-0.4718,-0.4574,0.1256,-0.7217,-0.5143,-0.4632,0.1228,-0.6809,-0.5688,-0.4613,0.1211,-0.6413,-0.611,-0.4641,0.1191,-0.5983,-0.6522,-0.4654,0.1176,-0.5429,-0.7021,-0.4607,0.1159,-0.4932,-0.7395,-0.4581,0.1153])

Group366.addChildren(OrientationInterpolator372)
#Euler angle triplet values, CHANNELS Xposition Yposition Zposition Zrotation Xrotation Yrotation, with min/max ranges [-4.411866,0.010186], [-10.242768,4.9E-324], [-4.974968,11.925271] degrees
#-1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.788088 -4.320133 -0.425375, -1.788088 -4.320133 -0.425375, -1.788088 -4.320133 -0.425375, -1.728913 -4.276426 -0.345031, -1.669766 -4.232606 -0.264662, -1.685525 -4.145720 -0.129650, -1.652053 -4.113320 0.048212, -1.609415 -3.982305 0.263455, -1.517751 -3.905375 0.521242, -1.467091 -3.908291 0.823506, -1.456708 -3.991359 1.170824, -1.471413 -4.086321 1.614424, -1.535673 -4.127849 2.015931, -1.675475 -4.128628 2.471004, -1.826812 -3.996097 2.839420, -1.902912 -3.905024 3.154643, -2.112926 -3.819734 3.442007, -2.259367 -3.640699 3.590316, -2.367132 -3.380561 3.693366, -2.410912 -3.025221 3.657587, -2.307748 -2.596693 3.696661, -2.184056 -2.253902 3.599807, -2.041469 -2.197795 3.405301, -1.997309 -2.168679 3.097270, -2.016934 -2.150796 2.701221, -2.022475 -2.067209 2.353890, -2.194512 -1.968233 2.067374, -2.366086 -1.868372 1.781071, -2.598501 -1.762160 1.675914, -2.857023 -1.671104 1.667144, -3.080900 -1.700232 1.647672, -3.330402 -1.745331 1.723969, -3.489516 -1.866317 1.869079, -3.724264 -1.948238 2.069781, -3.907512 -2.086627 2.309540, -3.958720 -2.220398 2.574254, -3.912702 -2.228696 2.875660, -3.790715 -2.275653 3.121986, -3.800008 -2.328235 3.342237, -3.692726 -2.338173 3.462473, -3.637202 -2.293115 3.543880, -3.509365 -2.386682 3.527902, -3.381620 -2.480235 3.512142, -3.177843 -2.612885 3.442053, -3.050264 -2.706512 3.426829, -2.962620 -2.881371 3.457208, -2.778823 -2.929527 3.523834, -2.722559 -2.884000 3.605225, -2.786968 -2.979980 3.744315, -2.770202 -3.015797 3.871498, -2.834207 -3.111912 4.010355, -2.893595 -3.108783 4.191570, -2.880861 -3.244102 4.276380, -2.863720 -3.280172 4.404058, -2.926913 -3.376542 4.542418, -2.857359 -3.466013 4.709269, -2.843753 -3.601161 4.794092, -2.843753 -3.601161 4.794092, -2.787526 -3.555302 4.876284, -2.787526 -3.555302 4.876284, -2.769375 -3.388591 4.965569, -2.783012 -3.253494 4.880746, -2.852387 -3.164270 4.713966, -2.901063 -3.159456 4.411880, -2.981556 -3.185251 3.934991, -3.067171 -3.309579 3.415278, -3.097131 -3.388279 2.977283, -3.059598 -3.557727 2.705670, -3.041132 -3.642530 2.569862, -2.932659 -3.651984 2.691736, -2.824239 -3.661196 2.813556, -2.640189 -3.710383 2.881434, -2.531805 -3.719085 3.003250, -2.417602 -3.628699 3.166242, -2.264106 -3.456534 3.283660, -2.128356 -3.248565 3.273570, -2.032154 -3.121779 3.308902, -1.859576 -3.034984 3.290117, -1.743659 -2.994268 3.190140, -1.627707 -2.953763 3.090093, -1.395604 -2.873361 2.889806, -1.202800 -2.874118 2.735520, -0.970309 -2.795164 2.534762, -0.737611 -2.717040 2.333742, -0.601820 -2.765985 2.099027, -0.426459 -2.735801 1.818054, -0.339741 -2.731774 1.541740, -0.164262 -2.703094 1.260876, -0.095080 -2.667067 0.858616, 0.010186 -2.753225 0.447858, -0.019921 -2.842906 0.012374, -0.050695 -2.932342 -0.423079, -0.141199 -3.066584 -0.937309, -0.215214 -3.233839 -1.327795, -0.350017 -3.445031 -1.797627, -0.426700 -3.611152 -2.189156, -0.504572 -3.776845 -2.581229, -0.536385 -3.997451 -2.928499, -0.690760 -4.116915 -3.265727, -0.785166 -4.192702 -3.524448, -0.879977 -4.268097 -3.783478, -0.940760 -4.310611 -3.862243, -1.048757 -4.297316 -3.986858, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.122320 -4.251632 -3.930945, -1.135275 -4.163697 -3.796252, -1.040683 -4.088952 -3.537298, -0.929185 -4.049552 -3.156774, -0.878108 -4.052577 -2.854900, -0.826985 -4.055335 -2.552895, -0.896105 -4.144703 -2.409206, -1.012853 -4.179078 -2.310513, -1.135121 -4.079315 -2.299888, -1.331787 -3.935126 -2.233524, -1.411478 -3.756261 -2.265616, -1.431557 -3.534168 -2.218302, -1.403903 -3.367791 -2.126827, -1.419258 -3.280401 -1.991948, -1.536603 -3.315573 -1.892552, -1.531100 -3.450300 -1.805181, -1.573682 -3.529463 -1.761651, -1.690803 -3.565035 -1.662490, -1.765342 -3.521446 -1.606843, -1.823401 -3.513934 -1.428172, -1.956216 -3.463367 -1.193725, -2.040265 -3.468781 -0.916128, -2.166223 -3.554380 -0.595195, -2.275035 -3.677063 -0.150523, -2.449350 -3.893910 0.435604, -2.570926 -4.166828 1.063031, -2.654828 -4.563269 1.679435, -2.849200 -5.001401 2.393433, -2.980011 -5.397781 3.189302, -2.955989 -5.720922 4.064415, -2.980344 -5.992032 4.899459, -2.889023 -6.269107 5.858841, -2.793034 -6.544525 6.818833, -2.747144 -6.768757 7.740730, -2.720510 -6.954337 8.531729, -2.614780 -7.176875 9.273687, -2.542405 -7.434660 9.844651, -2.512619 -7.664474 10.368456, -2.402983 -7.835724 10.893099, -2.373446 -7.921570 11.246732, -2.420542 -7.970830 11.647726, -2.472330 -7.972330 11.829858, -2.581027 -8.022026 11.925271, -2.694926 -8.117733 11.751631, -2.846250 -8.250303 11.407296, -3.023136 -8.249192 10.977660, -3.143356 -8.293914 10.584957, -3.263840 -8.337790 10.192293, -3.326771 -8.334619 9.886428, -3.298343 -8.199272 9.620469, -3.327093 -8.110147 9.268167, -3.255594 -8.098228 9.000278, -3.249253 -7.923811 8.601842, -3.142641 -7.827216 8.287056, -3.000608 -7.646248 7.925707, -2.892550 -7.550795 7.610201, -2.729043 -7.505020 7.333610, -2.620035 -7.410803 7.017589, -2.531775 -7.327227 6.790732, -2.420496 -7.282453 6.694836, -2.309160 -7.237870 6.598867, -2.197752 -7.193463 6.502812, -2.198766 -7.145436 6.282249, -2.145806 -7.147140 6.101692, -2.070855 -7.139194 5.830737, -2.060396 -7.272480 5.431556, -2.044901 -7.310510 5.075964, -2.089138 -7.393617 4.636014, -2.134027 -7.476377 4.195898, -2.179568 -7.558798 3.755647, -2.270955 -7.818559 3.317973, -2.282360 -8.025312 2.870398, -2.391908 -8.149839 2.345553, -2.555128 -8.222192 1.777455, -2.731162 -8.207470 1.344469, -2.854720 -8.243043 0.955119, -2.969296 -8.184175 0.605681, -3.104194 -8.133051 0.352608, -3.206620 -8.207551 0.089090, -3.268701 -8.199076 -0.216379, -3.206394 -8.286676 -0.530176, -3.010383 -8.377973 -0.813450, -2.752369 -8.429312 -1.013579, -2.474169 -8.406960 -1.157143, -2.247378 -8.333099 -1.346081, -2.020426 -8.259995 -1.535226, -1.843790 -8.135219 -1.770469, -1.687853 -7.971228 -2.130128, -1.539096 -7.674539 -2.577899, -1.388122 -7.379049 -3.026058, -1.270670 -7.298710 -3.344683, -1.267604 -7.252576 -3.567891, -1.225183 -7.172469 -3.609401, -1.273940 -7.118751 -3.656250, -1.530148 -7.013199 -3.675171, -1.834952 -6.853510 -3.740089, -2.254985 -6.727648 -3.708374, -2.553768 -6.702308 -3.684730, -2.852508 -6.677087 -3.660945, -3.039843 -6.666620 -3.510273, -3.348859 -6.556761 -3.349950, -3.590333 -6.543370 -3.022331, -3.781369 -6.586067 -2.649847, -3.943133 -6.755381 -2.292293, -4.103956 -6.925786 -1.934909, -4.254793 -7.233204 -1.493048, -4.331428 -7.585374 -1.105719, -4.311476 -7.908836 -0.714936, -4.383454 -8.261798 -0.327459, -4.338515 -8.627381 0.188131, -4.228634 -8.951911 0.789131, -4.147720 -9.148852 1.402116, -4.064705 -9.344744 2.015155, -3.961312 -9.531525 2.534343, -3.879220 -9.674967 2.926623, -3.812869 -9.683474 3.233868, -3.708647 -9.607100 3.498333, -3.697260 -9.565199 3.763205, -3.704581 -9.531253 4.120766, -3.633227 -9.588596 4.649239, -3.727131 -9.640581 5.229541, -3.894536 -9.653186 5.859632, -3.987679 -9.707486 6.440492, -4.104880 -9.720654 6.890254, -4.133226 -9.857194 7.154995, -4.242627 -9.903733 7.248058, -4.337797 -10.033408 7.204977, -4.383971 -10.159811 6.981487, -4.370337 -10.242768 6.845367, -4.317763 -10.148513 6.712233, -4.316989 -9.845343 6.720018, -4.411866 -9.671497 6.684850, -4.376048 -9.585706 6.640844, -4.376048 -9.585706 6.640844, -4.376048 -9.585706 6.640844, -4.382447 -9.534406 6.420510, -4.256351 -9.268641 6.198946, -4.129318 -9.003385 5.976985, -3.979504 -8.570233 5.846439, -3.846492 -8.212560 5.668837, -3.731894 -7.864828 5.581016, -3.712765 -7.645802 5.451993, -3.693152 -7.426872 5.323010, -3.560992 -7.163845 5.098509, -3.524129 -7.029308 4.833653, -3.374152 -6.851545 4.472998, -3.335311 -6.667322 3.987462, -3.294895 -6.483348 3.501762, -3.311835 -6.343237 2.932606, -3.426060 -6.328801 2.324237, -3.453977 -6.490132 1.748088, -3.483545 -6.651154 1.171740, -3.514741 -6.811846 0.595230, -3.487171 -6.930540 0.101290, -3.585094 -6.952864 -0.382913, -3.662472 -6.902582 -0.811213, -3.729971 -6.757144 -1.200275, -3.847547 -6.556993 -1.633167, -3.942009 -6.285167 -2.007685, -3.945343 -6.097701 -2.314166, -3.947664 -5.910049 -2.620815, -3.970932 -5.733502 -2.827471, -3.905054 -5.641560 -2.968133, -3.788904 -5.605283 -3.064509, -3.666748 -5.705165 -3.075675, -3.550683 -5.669202 -3.172033, -3.440216 -5.497645 -3.353974, -3.462000 -5.322189 -3.560606, -3.427523 -4.970641 -3.772186, -3.368148 -4.607542 -4.085361, -3.330748 -4.256041 -4.297379, -3.292059 -3.904738 -4.509504, -3.206619 -3.474988 -4.762572, -3.165136 -3.124392 -4.974968
#Interpolator2_l_hip channels [6..8] sends animation values to BVH JOINT LeftHip, DEF Bvh1_l_hip, <HAnimJoint name=l_hip/>
OrientationInterpolator373 = OrientationInterpolator()
OrientationInterpolator373.setDEF("Interpolator2_l_hip")
OrientationInterpolator373.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator373.setKeyValue([0.8201,0.3853,0.423,0.1221,0.8201,0.3853,0.423,0.1221,0.8171,0.3886,0.4259,0.1239,0.819,0.3933,0.4178,0.1264,0.8212,0.4001,0.4068,0.1242,0.8132,0.4179,0.4051,0.1209,0.8074,0.4361,0.3975,0.1185,0.8039,0.4427,0.3971,0.1158,0.8151,0.4314,0.3867,0.1104,0.827,0.4188,0.375,0.1051,0.8451,0.384,0.3721,0.0997,0.8673,0.3284,0.374,0.0969,0.8905,0.2731,0.364,0.0905,0.9133,0.214,0.3466,0.0843,0.9327,0.1579,0.3243,0.0809,0.9461,0.1161,0.3023,0.0808,0.9522,0.0918,0.2914,0.0835,0.953,0.0779,0.2927,0.0857,0.9421,0.0794,0.3258,0.088,0.9185,0.1387,0.3704,0.0914,0.8865,0.2072,0.4137,0.0967,0.8449,0.2773,0.4574,0.1061,0.7922,0.3565,0.4953,0.1147,0.7416,0.4165,0.5259,0.1198,0.6975,0.4657,0.5445,0.1209,0.6628,0.49,0.5663,0.1166,0.641,0.5018,0.5808,0.1123,0.6596,0.4904,0.5696,0.1127,0.6684,0.487,0.5622,0.1154,0.6796,0.4806,0.5542,0.1195,0.6788,0.483,0.5531,0.1222,0.6746,0.4875,0.5543,0.1277,0.6634,0.4993,0.5573,0.1312,0.6623,0.4931,0.5642,0.1353,0.6625,0.487,0.5691,0.1393,0.6619,0.4961,0.5619,0.146,0.662,0.5043,0.5544,0.1539,0.6695,0.5151,0.5352,0.1636,0.6603,0.5256,0.5364,0.1727,0.6577,0.5315,0.5338,0.1817,0.6616,0.5318,0.5287,0.1896,0.6662,0.5284,0.5263,0.1924,0.6738,0.5286,0.5164,0.1956,0.6757,0.545,0.4963,0.1944,0.6796,0.5582,0.476,0.1926,0.6862,0.5625,0.4612,0.1893,0.7137,0.549,0.4351,0.1866,0.7441,0.5205,0.4188,0.1838,0.775,0.4886,0.4008,0.1841,0.7979,0.4617,0.3875,0.1865,0.8164,0.438,0.3763,0.1935,0.8234,0.4355,0.3638,0.2018,0.8226,0.4454,0.3534,0.2087,0.8302,0.4324,0.3519,0.2166,0.8401,0.4163,0.3477,0.2219,0.8541,0.39,0.3441,0.2272,0.8637,0.3609,0.3518,0.2274,0.8715,0.3407,0.3527,0.2297,0.8801,0.3262,0.3449,0.2308,0.8806,0.3203,0.3491,0.2361,0.8829,0.3158,0.3474,0.2422,0.8848,0.3163,0.3421,0.2505,0.8814,0.3241,0.3438,0.2565,0.8817,0.3255,0.3415,0.2593,0.8801,0.3306,0.3408,0.2635,0.8827,0.3223,0.3421,0.2638,0.8821,0.3236,0.3423,0.2656,0.8822,0.3235,0.3422,0.2694,0.8835,0.3229,0.3394,0.2739,0.8843,0.3237,0.3365,0.278,0.8829,0.3311,0.3331,0.2804,0.8807,0.337,0.3328,0.2784,0.8798,0.3414,0.3306,0.271,0.8715,0.3589,0.3341,0.2589,0.8491,0.3872,0.3592,0.2423,0.8052,0.4411,0.3962,0.2253,0.7286,0.5271,0.4373,0.2121,0.6048,0.6369,0.4781,0.2061,0.4379,0.7487,0.4976,0.208,0.2506,0.8441,0.474,0.2186,0.0615,0.9026,0.426,0.2343,-0.1093,0.9213,0.3732,0.2533,-0.2647,0.9116,0.3146,0.2758,-0.3921,0.8835,0.2562,0.3026,-0.4906,0.8477,0.202,0.3295,-0.57,0.8081,0.1486,0.359,-0.6288,0.7705,0.1047,0.3838,-0.6736,0.7359,0.0686,0.4071,-0.7117,0.7014,0.038,0.4278,-0.7407,0.6716,0.0185,0.4423,-0.7685,0.6398,0.003,0.4562,-0.7899,0.6132,-0.0046,0.4663,-0.8091,0.5874,-0.0158,0.4745,-0.822,0.5689,-0.0249,0.4826,-0.8281,0.5596,-0.0328,0.4862,-0.8328,0.5525,-0.0344,0.4868,-0.8396,0.5418,-0.039,0.486,-0.8466,0.5307,-0.0404,0.4811,-0.8564,0.5146,-0.0419,0.4732,-0.8653,0.4996,-0.0418,0.4627,-0.8739,0.4843,-0.0423,0.4517,-0.8784,0.4761,-0.0408,0.4393,-0.8783,0.4767,-0.0378,0.427,-0.8767,0.4801,-0.0293,0.4165,-0.8764,0.481,-0.0234,0.4073,-0.8774,0.4794,-0.0189,0.4004,-0.8829,0.4688,-0.0277,0.3957,-0.8927,0.4492,-0.0367,0.3939,-0.9,0.4331,-0.0499,0.3883,-0.9067,0.4169,-0.0639,0.3825,-0.9075,0.4128,-0.0773,0.3772,-0.9004,0.4239,-0.0977,0.371,-0.8871,0.4457,-0.1203,0.3631,-0.8685,0.4763,-0.137,0.3553,-0.8592,0.4877,-0.1548,0.3464,-0.8672,0.4698,-0.1651,0.3302,-0.8834,0.4365,-0.1708,0.3125,-0.9011,0.397,-0.1745,0.2904,-0.9145,0.3657,-0.1732,0.2653,-0.9168,0.361,-0.1707,0.2407,-0.9145,0.371,-0.1612,0.2203,-0.9127,0.38,-0.15,0.1995,-0.9073,0.3939,-0.1474,0.1828,-0.9086,0.39,-0.1491,0.1677,-0.9099,0.3838,-0.1577,0.1517,-0.9154,0.3637,-0.1724,0.1349,-0.9204,0.3478,-0.1789,0.116,-0.9239,0.3249,-0.2022,0.0953,-0.9255,0.2871,-0.2468,0.0775,-0.9336,0.221,-0.2821,0.0615,-0.9238,0.1704,-0.343,0.0472,-0.8959,0.0445,-0.4421,0.0339,-0.8282,-0.1215,-0.5471,0.022,-0.3943,-0.4502,-0.8012,0.0134,0.6233,-0.5809,-0.5235,0.0142,0.9557,-0.2579,-0.1421,0.0253,0.9906,-0.132,0.0357,0.0437,0.9901,-0.0241,0.1384,0.0636,0.9835,0.0518,0.1735,0.0861,0.9697,0.0956,0.2248,0.1098,0.9617,0.108,0.2519,0.1339,0.9565,0.1085,0.2708,0.1582,0.9515,0.1062,0.2887,0.1828,0.9522,0.0962,0.29,0.2078,0.9536,0.0841,0.2892,0.2313,0.9515,0.0764,0.298,0.251,0.952,0.0664,0.2987,0.2683,0.9548,0.0569,0.2919,0.2848,0.9551,0.0565,0.291,0.3013,0.9536,0.0629,0.2946,0.3165,0.9512,0.0713,0.3003,0.3287,0.9477,0.0914,0.3059,0.3393,0.9444,0.0997,0.3134,0.3471,0.9403,0.1148,0.3203,0.3523,0.9363,0.1232,0.329,0.3523,0.9312,0.1366,0.3378,0.349,0.9246,0.1521,0.3492,0.3399,0.9111,0.1735,0.3738,0.3218,0.886,0.2016,0.4175,0.3024,0.8489,0.2419,0.4699,0.2831,0.7916,0.3038,0.5301,0.2643,0.7155,0.3889,0.5803,0.2453,0.6077,0.4963,0.62,0.2298,0.4662,0.6017,0.6486,0.2171,0.2763,0.7127,0.6448,0.2112,0.0702,0.7966,0.6004,0.2118,-0.1402,0.8411,0.5224,0.2195,-0.3197,0.8393,0.4396,0.2339,-0.4655,0.8122,0.3517,0.2525,-0.58,0.7669,0.2748,0.2734,-0.6666,0.7168,0.2045,0.2939,-0.7415,0.6552,0.1448,0.3113,-0.7974,0.5962,0.0935,0.3284,-0.8409,0.5391,0.0467,0.3445,-0.8714,0.4905,0.009,0.3604,-0.8932,0.449,-0.0229,0.3711,-0.9072,0.4179,-0.0478,0.3798,-0.9164,0.3958,-0.06,0.3823,-0.9246,0.3745,-0.0694,0.3805,-0.9302,0.3612,-0.066,0.3777,-0.9339,0.3529,-0.0576,0.3707,-0.9407,0.3363,-0.0453,0.3604,-0.9474,0.3195,-0.0197,0.3468,-0.9526,0.3043,-0.0001,0.3336,-0.9529,0.3022,0.0268,0.3206,-0.9506,0.306,0.0513,0.3085,-0.9484,0.3094,0.0699,0.2985,-0.9464,0.3147,0.0721,0.2929,-0.947,0.3153,0.0623,0.2938,-0.9515,0.3038,0.0479,0.2931,-0.9559,0.292,0.0308,0.2876,-0.957,0.2897,0.0129,0.2794,-0.9552,0.2954,-0.0157,0.2657,-0.9567,0.2872,-0.048,0.2539,-0.9645,0.2504,-0.0844,0.2444,-0.9764,0.1856,-0.1106,0.2381,-0.9862,0.1125,-0.1212,0.2316,-0.9901,0.0577,-0.128,0.2223,-0.9888,0.0288,-0.1463,0.2079,-0.9832,0.0483,-0.176,0.1904,-0.976,0.0926,-0.197,0.173,-0.9658,0.1289,-0.2248,0.1566,-0.9541,0.1503,-0.2591,0.1386,-0.9423,0.1628,-0.2924,0.1193,-0.9351,0.1083,-0.3376,0.1029,-0.9179,-0.0205,-0.3963,0.0876,-0.8855,-0.2438,-0.3957,0.0758,-0.7882,-0.4949,-0.3658,0.0666,-0.5942,-0.7539,-0.2805,0.0591,-0.278,-0.9361,-0.2156,0.0526,0.13,-0.9851,-0.1129,0.0489,0.5284,-0.8489,0.0092,0.051,0.784,-0.5906,0.1909,0.06,0.8827,-0.3907,0.2612,0.0747,0.9216,-0.2693,0.2796,0.0916,0.9432,-0.1783,0.2803,0.1114,0.9501,-0.1274,0.2847,0.1299,0.9501,-0.0902,0.2986,0.152,0.9508,-0.034,0.3081,0.1702,0.952,0.0196,0.3054,0.1876,0.9511,0.0639,0.3022,0.2067,0.9511,0.0858,0.2968,0.2262,0.9537,0.0851,0.2884,0.2447,0.9558,0.0807,0.2829,0.2597,0.9595,0.0689,0.2732,0.2742,0.9621,0.0598,0.2662,0.2894,0.9642,0.0503,0.2603,0.3027,0.9657,0.0396,0.2567,0.3131,0.9672,0.0323,0.252,0.322,0.968,0.0286,0.2492,0.3312,0.9679,0.0238,0.2501,0.3396,0.9672,0.0124,0.2537,0.3474,0.9636,0.0086,0.2673,0.3552,0.9592,0.0073,0.2828,0.3626,0.9555,0.01,0.2949,0.3688,0.9514,0.0209,0.3071,0.3683,0.9476,0.0345,0.3176,0.3666,0.9406,0.0514,0.3357,0.3584,0.9315,0.0709,0.3567,0.3443,0.9167,0.0988,0.3872,0.3236,0.8931,0.1281,0.4313,0.2978,0.8542,0.1692,0.4917,0.2666,0.788,0.2313,0.5706,0.2344,0.6764,0.337,0.655,0.2079,0.5189,0.471,0.7134,0.1888,0.3004,0.6116,0.732,0.1795,0.0478,0.7247,0.6874,0.1795,-0.2045,0.7861,0.5833,0.1935,-0.4119,0.792,0.4507,0.2173,-0.549,0.7663,0.3338,0.247,-0.6551,0.7187,0.2333,0.2791,-0.7227,0.6739,0.1534,0.3095,-0.7707,0.6302,0.0942,0.3366,-0.8038,0.5924,0.0544,0.3584,-0.8275,0.5608,0.0273,0.3765,-0.8462,0.5329,0.0047,0.389,-0.8614,0.5079,-0.0068,0.3969,-0.872,0.4891,-0.0207,0.4016,-0.8787,0.4768,-0.0208,0.4044,-0.8829,0.469,-0.0215,0.4044,-0.8872,0.4611,-0.0168,0.4031,-0.8949,0.4462,-0.0063,0.3961,-0.9027,0.4303,0.0033,0.3838,-0.9138,0.4061,0.012,0.3701,-0.9228,0.3846,0.0204,0.3546,-0.9295,0.3681,0.0234,0.3404,-0.9328,0.3584,0.0369,0.3276,-0.931,0.3614,0.0519,0.3177,-0.9262,0.3716,0.0632,0.3094,-0.9159,0.3951,0.0706,0.3009,-0.9081,0.4113,0.079,0.2911,-0.906,0.4148,0.0844,0.2767,-0.916,0.3913,0.0883,0.2606,-0.9381,0.3328,0.0956,0.2427,-0.9641,0.2489,0.0922,0.2268,-0.9856,0.141,0.0937,0.2125,-0.9947,0.0351,0.0961,0.1972,-0.9946,-0.0356,0.0972,0.1873,-0.9922,-0.0699,0.1032,0.1764,-0.9895,-0.0658,0.1287,0.1627,-0.9882,-0.0483,0.1451,0.1523,-0.987,-0.0171,0.1595,0.1419,-0.9841,-0.0043,0.1774,0.1338,-0.981,-0.0288,0.1921,0.1274,-0.9795,-0.0666,0.1899,0.1257,-0.9765,-0.1138,0.1832,0.1252])

Group366.addChildren(OrientationInterpolator373)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-2.07709,7.74649], [-23.242655,20.162275], [-2.82819,17.87174] degrees
#2.832229 5.801149 2.553770, 2.832229 5.801149 2.553770, 2.893268 5.869187 2.613585, 2.886478 6.000001 2.699244, 2.757954 5.911017 2.707608, 2.671466 5.700300 2.764938, 2.563605 5.546554 2.839046, 2.503336 5.395139 2.820716, 2.329124 5.211887 2.625725, 2.154138 5.029144 2.430089, 2.038072 4.867472 2.109035, 2.004529 4.847241 1.739820, 1.834637 4.641002 1.343288, 1.636777 4.423985 0.970761, 1.479116 4.333948 0.676835, 1.382096 4.387193 0.484949, 1.380085 4.562369 0.384830, 1.424597 4.683239 0.324424, 1.630335 4.756027 0.332913, 1.914505 4.823192 0.646326, 2.249224 4.935641 1.052710, 2.712964 5.176470 1.565353, 3.156771 5.269109 2.200086, 3.490622 5.175544 2.703977, 3.644308 4.934379 3.073523, 3.663468 4.532536 3.132416, 3.625192 4.224030 3.096808, 3.565495 4.356757 3.033947, 3.596890 4.516984 3.079280, 3.666362 4.754819 3.140256, 3.739552 4.861400 3.226387, 3.908872 5.054255 3.397689, 4.034752 5.117296 3.577705, 4.209808 5.269904 3.631968, 4.371542 5.431460 3.683026, 4.510505 5.697347 3.931649, 4.674832 6.015391 4.207866, 4.768012 6.474186 4.567344, 5.027681 6.757952 4.914306, 5.243429 7.094718 5.218116, 5.400640 7.452162 5.436618, 5.450805 7.615705 5.475396, 5.420737 7.827277 5.567975, 5.151124 7.796432 5.733640, 4.869335 7.759462 5.843816, 4.623693 7.687126 5.802298, 4.278740 7.847598 5.586888, 4.055679 8.029014 5.208513, 3.881389 8.347087 4.880706, 3.797085 8.686701 4.655683, 3.815585 9.210081 4.559852, 3.817612 9.684537 4.725433, 3.800367 10.010423 5.008277, 3.921535 10.484694 5.023202, 3.968370 10.863517 4.933724, 4.031518 11.291982 4.696630, 4.170718 11.417600 4.302324, 4.245632 11.631557 4.068994, 4.175780 11.789265 3.899434, 4.328813 12.067161 3.892931, 4.414634 12.410997 3.920547, 4.475957 12.870954 4.057196, 4.586023 13.132854 4.257065, 4.594031 13.283576 4.324063, 4.643834 13.481508 4.468195, 4.681195 13.528196 4.340896, 4.712275 13.617700 4.387710, 4.771180 13.814596 4.441391, 4.799826 14.069101 4.503335, 4.815863 14.292030 4.581263, 4.782811 14.398184 4.745988, 4.736263 14.262715 4.814431, 4.579834 13.863674 4.772534, 4.423285 13.129302 4.841889, 4.490148 11.993941 4.926150, 4.642351 10.621325 5.282381, 4.847876 9.122188 6.035493, 5.190194 7.483083 7.198329, 5.518437 5.651601 8.665732, 5.622439 3.661852 10.405171, 5.590827 1.420251 12.059477, 5.551896 -0.941485 13.426015, 5.449883 -3.511261 14.588489, 5.314196 -6.117500 15.630031, 5.090293 -8.600213 16.428646, 4.768567 -11.103746 17.145111, 4.385863 -13.270555 17.536860, 4.022193 -15.224087 17.812460, 3.644212 -17.029942 17.871740, 3.370986 -18.412497 17.719542, 3.142739 -19.776531 17.444628, 3.043082 -20.817665 17.128246, 2.795460 -21.758997 16.706587, 2.595528 -22.524221 16.455637, 2.386870 -22.896303 16.287270, 2.327955 -23.065458 16.096937, 2.148184 -23.242655 15.742593, 2.013536 -23.215712 15.249210, 1.828479 -23.122025 14.522050, 1.666708 -22.855043 13.759366, 1.487845 -22.553154 12.996436, 1.383245 -22.052752 12.404510, 1.349219 -21.426388 12.054583, 1.480272 -20.850464 11.858182, 1.542556 -20.371794 11.622407, 1.579255 -20.044142 11.391354, 1.299053 -19.956358 10.966695, 1.014279 -20.111464 10.422645, 0.618548 -20.020414 9.844428, 0.211559 -19.896366 9.266111, -0.130370 -19.664928 8.987178, -0.573707 -19.224682 9.000589, -1.024465 -18.575506 9.186677, -1.313609 -17.831934 9.569765, -1.659942 -17.229168 9.501938, -1.885092 -16.578993 8.675566, -2.016473 -15.970876 7.582511, -2.077090 -15.125435 6.370121, -1.991632 -14.001677 5.341220, -1.829999 -12.728888 4.796271, -1.581400 -11.612572 4.537875, -1.331816 -10.487686 4.233605, -1.211003 -9.548136 4.033661, -1.154760 -8.773225 3.667611, -1.146919 -7.944105 3.261767, -1.163624 -7.103045 2.741724, -1.068763 -6.136926 2.255621, -1.028374 -5.058967 1.729463, -1.051783 -4.120789 1.237512, -0.971978 -3.293972 0.750339, -0.917125 -2.499330 0.440429, -0.856614 -1.738582 0.073417, -0.690100 -1.041631 -0.159160, -0.615017 -0.300364 -0.346711, -0.422905 0.507765 -0.469786, -0.201424 1.385306 -0.371191, 0.096753 2.481500 -0.332834, 0.507878 3.608437 -0.103818, 0.846517 4.850883 0.219704, 1.386757 6.104817 0.528019, 1.890013 7.393109 0.708072, 2.399279 8.690373 0.803861, 2.957360 9.991704 0.857054, 3.383058 11.363266 0.813295, 3.770791 12.665697 0.701306, 4.233838 13.711538 0.595547, 4.560273 14.662127 0.440509, 4.754183 15.602407 0.283707, 5.021220 16.509916 0.254737, 5.331733 17.321573 0.337827, 5.629994 17.952202 0.464234, 5.862180 18.480577 0.838351, 6.127396 18.853811 0.985565, 6.310817 19.067993 1.279504, 6.464346 19.000109 1.428744, 6.540294 18.738163 1.678070, 6.547938 18.137476 1.944973, 6.610426 16.947029 2.239718, 6.929051 15.525990 2.573191, 7.287074 13.985853 3.054616, 7.651628 12.261320 3.801455, 7.746490 10.398503 4.782916, 7.745063 8.426219 5.986492, 7.698053 6.292410 7.081097, 7.532519 3.906659 8.382342, 7.183016 1.457888 9.590134, 6.695642 -1.144690 10.657774, 6.280996 -3.672315 11.463290, 5.764982 -6.156411 12.082637, 5.261804 -8.554473 12.435684, 4.655063 -10.765365 12.550171, 3.981673 -12.858058 12.187481, 3.293444 -14.727556 11.709354, 2.534302 -16.409212 11.080534, 1.845000 -17.881065 10.502579, 1.151728 -18.944704 9.829328, 0.566200 -19.739803 9.284315, 0.232276 -20.096167 8.802554, -0.061775 -20.198736 8.240182, -0.039521 -20.163565 7.891159, 0.092465 -19.858990 7.587718, 0.265139 -19.435440 7.057597, 0.686002 -18.805832 6.519338, 0.962674 -18.177488 6.019915, 1.389061 -17.450853 5.808390, 1.753299 -16.732788 5.706532, 2.000497 -16.139769 5.612278, 1.996072 -15.803757 5.593822, 1.837309 -15.866412 5.597595, 1.558683 -15.918087 5.352021, 1.202826 -15.711389 5.008601, 0.850277 -15.296737 4.780139, 0.341709 -14.539001 4.565547, -0.191583 -13.932732 4.175399, -0.780728 -13.533186 3.429988, -1.235455 -13.348140 2.398373, -1.462597 -13.104679 1.330924, -1.575411 -12.620260 0.563556, -1.731100 -11.781775 0.165907, -1.893373 -10.735291 0.351250, -1.893536 -9.689223 0.759807, -1.944445 -8.685539 1.011434, -1.989842 -7.593464 1.062987, -1.943539 -6.456947 1.003845, -1.966106 -5.524487 0.544196, -1.998428 -4.606179 -0.183423, -1.756662 -3.829282 -1.117947, -1.445437 -2.981599 -1.925464, -0.994383 -1.989619 -2.569871, -0.670793 -0.822153 -2.828190, -0.307093 0.371347 -2.756933, 0.060449 1.543605 -2.482729, 0.704931 2.684592 -2.048531, 1.174483 3.760175 -1.710948, 1.531036 4.819514 -1.479337, 1.855846 6.001740 -1.236497, 2.189172 7.054068 -1.084568, 2.675948 8.254451 -0.980543, 3.058443 9.260207 -0.580406, 3.298804 10.233540 -0.083824, 3.550740 11.281109 0.408696, 3.785609 12.353469 0.707212, 3.975314 13.400192 0.731661, 4.145034 14.252640 0.689339, 4.247539 15.102928 0.525763, 4.388748 15.972947 0.382671, 4.514685 16.738729 0.213828, 4.638931 17.333302 0.009449, 4.708764 17.849300 -0.139078, 4.806458 18.371044 -0.229656, 4.970265 18.828703 -0.356659, 5.204412 19.234266 -0.632217, 5.631539 19.589071 -0.796189, 6.095309 19.897947 -0.916614, 6.463166 20.162275 -0.936754, 6.677623 20.058683 -0.735518, 6.820518 19.900309 -0.465742, 6.982131 19.333364 -0.123137, 7.054181 18.417225 0.268508, 7.114507 17.063616 0.778944, 7.238667 15.335371 1.225137, 7.341827 13.178058 1.750551, 7.460561 10.756817 2.417192, 7.564530 8.299118 3.476920, 7.483237 5.932747 4.718340, 7.352686 3.487230 6.076504, 7.019080 0.948082 7.405816, 6.615777 -1.762581 8.827506, 6.037679 -4.611503 10.117277, 5.459861 -7.265746 11.214539, 4.805209 -10.020116 11.951391, 4.101614 -12.426932 12.448965, 3.458267 -14.551555 12.666535, 2.946317 -16.253349 12.670041, 2.560053 -17.649853 12.594315, 2.146204 -18.709940 12.339437, 1.907851 -19.467741 11.992743, 1.576638 -19.979761 11.649097, 1.565475 -20.275463 11.445477, 1.525808 -20.378031 11.259027, 1.602482 -20.403070 11.053254, 1.738583 -20.210068 10.541636, 1.795934 -19.751081 9.871426, 1.787890 -19.277788 8.996215, 1.764751 -18.658545 8.174740, 1.653305 -18.050352 7.502786, 1.781834 -17.426825 7.053306, 1.979575 -16.849291 6.920408, 2.125033 -16.312094 6.936576, 2.213819 -15.674872 7.160229, 2.278126 -15.024364 7.200164, 2.208691 -14.249763 6.886278, 2.055068 -13.580343 6.114401, 1.889059 -12.972301 4.862382, 1.577350 -12.486387 3.420280, 1.340714 -11.979342 1.863340, 1.139961 -11.235892 0.509811, 1.019736 -10.676725 -0.288038, 0.991014 -10.033175 -0.620850, 1.160437 -9.230432 -0.520799, 1.243653 -8.627681 -0.328339, 1.295994 -8.027895 -0.047980, 1.366214 -7.545083 0.056705, 1.396847 -7.164520 -0.122879, 1.345077 -7.058871 -0.397547, 1.270130 -7.010466 -0.739485
#Interpolator3_l_knee channels [9..11] sends animation values to BVH JOINT LeftKnee, DEF Bvh1_l_knee, <HAnimJoint name=l_knee/>
OrientationInterpolator374 = OrientationInterpolator()
OrientationInterpolator374.setDEF("Interpolator3_l_knee")
OrientationInterpolator374.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator374.setKeyValue([-0.6074,-0.5228,-0.5981,0.1116,-0.6074,-0.5228,-0.5981,0.1116,-0.6059,-0.5111,-0.6096,0.1136,-0.614,-0.5151,-0.5981,0.1158,-0.6131,-0.5251,-0.5903,0.1135,-0.6033,-0.5465,-0.5808,0.1116,-0.5905,-0.579,-0.5622,0.112,-0.5797,-0.6117,-0.5383,0.1122,-0.562,-0.6435,-0.5197,0.1118,-0.5432,-0.6744,-0.5001,0.1117,-0.5278,-0.6984,-0.4834,0.1131,-0.5081,-0.7143,-0.4813,0.1158,-0.4818,-0.7499,-0.4533,0.117,-0.4447,-0.7798,-0.4406,0.1187,-0.4122,-0.8118,-0.4136,0.1209,-0.3818,-0.8359,-0.3943,0.1257,-0.3722,-0.8479,-0.3775,0.1328,-0.3695,-0.8529,-0.3687,0.1374,-0.371,-0.8538,-0.3654,0.1404,-0.3815,-0.8487,-0.3663,0.1457,-0.395,-0.829,-0.3959,0.1494,-0.4107,-0.8083,-0.4219,0.1573,-0.4152,-0.7913,-0.4488,0.1696,-0.4134,-0.7891,-0.4544,0.1837,-0.4233,-0.7847,-0.4528,0.1937,-0.4279,-0.777,-0.4617,0.199,-0.44,-0.7626,-0.4741,0.201,-0.47,-0.7342,-0.49,0.2007,-0.4881,-0.7155,-0.4998,0.1997,-0.5176,-0.6902,-0.5057,0.1968,-0.5401,-0.6616,-0.5202,0.1943,-0.5604,-0.6351,-0.5316,0.1908,-0.5737,-0.6125,-0.5438,0.1859,-0.587,-0.5844,-0.5603,0.1842,-0.6082,-0.5564,-0.5661,0.1825,-0.6253,-0.5301,-0.5727,0.1811,-0.6402,-0.5102,-0.5743,0.1816,-0.6523,-0.4905,-0.5779,0.1821,-0.6469,-0.4795,-0.593,0.1839,-0.6371,-0.4804,-0.6027,0.1871,-0.624,-0.4862,-0.6118,0.1921,-0.5996,-0.4997,-0.6251,0.197,-0.5767,-0.5205,-0.6297,0.2042,-0.5486,-0.5661,-0.6153,0.207,-0.5139,-0.6074,-0.6058,0.2135,-0.4869,-0.6353,-0.5995,0.2185,-0.4775,-0.6464,-0.5952,0.2195,-0.4745,-0.6384,-0.6061,0.2185,-0.4757,-0.6165,-0.6273,0.2157,-0.4797,-0.5921,-0.6476,0.2138,-0.4917,-0.562,-0.6651,0.2173,-0.4872,-0.5432,-0.6838,0.2266,-0.4861,-0.5406,-0.6866,0.2356,-0.4876,-0.5363,-0.6889,0.2419,-0.4906,-0.5324,-0.6898,0.2466,-0.4948,-0.5262,-0.6915,0.2508,-0.4852,-0.517,-0.7052,0.2524,-0.4652,-0.5076,-0.7252,0.2538,-0.4475,-0.5037,-0.739,0.2526,-0.4205,-0.5015,-0.7561,0.2551,-0.3886,-0.4952,-0.777,0.2598,-0.3527,-0.4935,-0.795,0.2634,-0.3102,-0.4912,-0.8139,0.2694,-0.269,-0.4844,-0.8325,0.2725,-0.217,-0.4809,-0.8495,0.2771,-0.1644,-0.4674,-0.8686,0.2807,-0.1128,-0.4528,-0.8844,0.2853,-0.0668,-0.4345,-0.8982,0.2902,-0.0162,-0.4045,-0.9144,0.2957,0.0456,-0.3656,-0.9297,0.3016,0.1261,-0.3272,-0.9365,0.3089,0.2154,-0.28,-0.9355,0.321,0.3234,-0.2231,-0.9196,0.3398,0.4329,-0.1699,-0.8853,0.3653,0.5316,-0.1236,-0.8379,0.407,0.6092,-0.0896,-0.788,0.4575,0.6698,-0.077,-0.7385,0.5186,0.7147,-0.088,-0.6938,0.5859,0.7497,-0.1093,-0.6527,0.6559,0.7789,-0.1315,-0.6132,0.7255,0.805,-0.1423,-0.5759,0.7899,0.8293,-0.1417,-0.5406,0.848,0.8537,-0.1291,-0.5044,0.8981,0.8773,-0.1105,-0.467,0.9374,0.8995,-0.0904,-0.4275,0.9639,0.9197,-0.0709,-0.3862,0.9802,0.9367,-0.0543,-0.3458,0.9855,0.9499,-0.0456,-0.3091,0.9776,0.9606,-0.0447,-0.2744,0.959,0.9692,-0.05,-0.2412,0.9288,0.9759,-0.062,-0.2091,0.8931,0.9804,-0.0826,-0.1789,0.8497,0.9836,-0.1083,-0.1442,0.8033,0.984,-0.1455,-0.1031,0.7551,0.9786,-0.1975,-0.0573,0.7055,0.9668,-0.2554,-0.0058,0.6585,0.9485,-0.3115,0.057,0.6146,0.9236,-0.3601,0.1313,0.5707,0.8913,-0.3979,0.2172,0.5289,0.8521,-0.419,0.3135,0.4865,0.8014,-0.423,0.4229,0.4475,0.7358,-0.4161,0.5343,0.4116,0.6471,-0.4048,0.646,0.3847,0.5485,-0.3922,0.7385,0.3675,0.4565,-0.3805,0.8043,0.3569,0.3905,-0.377,0.8399,0.3555,0.3572,-0.3814,0.8526,0.3618,0.3564,-0.3844,0.8516,0.3684,0.3647,-0.3836,0.8484,0.3723,0.3802,-0.3791,0.8437,0.373,0.3894,-0.3676,0.8445,0.3691,0.3933,-0.3541,0.8485,0.3636,0.3886,-0.3568,0.8495,0.3574,0.3828,-0.3788,0.8426,0.3519,0.3951,-0.3953,0.8292,0.3434,0.4181,-0.3946,0.8182,0.3283,0.4455,-0.3919,0.8049,0.3104,0.4649,-0.397,0.7914,0.291,0.4705,-0.407,0.7829,0.2699,0.4493,-0.4417,0.7766,0.2504,0.4197,-0.4756,0.7731,0.23,0.3823,-0.4837,0.7873,0.2077,0.3472,-0.4788,0.8064,0.1863,0.3137,-0.4548,0.8335,0.166,0.268,-0.4516,0.851,0.1463,0.2141,-0.4421,0.871,0.1298,0.1419,-0.4499,0.8817,0.1149,0.0576,-0.4591,0.8865,0.1013,-0.0349,-0.4228,0.9056,0.0923,-0.1355,-0.3787,0.9155,0.0825,-0.2688,-0.3452,0.8992,0.0748,-0.3941,-0.3434,0.8525,0.067,-0.5122,-0.3907,0.7649,0.0608,-0.6215,-0.4549,0.6378,0.0574,-0.7283,-0.5032,0.4652,0.055,-0.7864,-0.5685,0.2417,0.0573,-0.7912,-0.6106,0.0344,0.064,-0.7362,-0.6574,-0.1605,0.0761,-0.6717,-0.6742,-0.3069,0.0929,-0.6128,-0.6816,-0.3999,0.1113,-0.5744,-0.6779,-0.4588,0.1286,-0.5455,-0.6494,-0.5299,0.148,-0.5324,-0.6175,-0.5789,0.1663,-0.5247,-0.5938,-0.61,0.1853,-0.5016,-0.5816,-0.6404,0.2027,-0.4687,-0.5739,-0.6715,0.2187,-0.4331,-0.5655,-0.7019,0.2296,-0.392,-0.5518,-0.7361,0.2387,-0.3335,-0.5348,-0.7764,0.2498,-0.2576,-0.524,-0.8118,0.2611,-0.1644,-0.5102,-0.8442,0.2767,-0.0729,-0.499,-0.8635,0.2937,0.0231,-0.4813,-0.8762,0.312,0.1285,-0.4502,-0.8836,0.3314,0.2436,-0.4071,-0.8803,0.355,0.3536,-0.3562,-0.8649,0.3856,0.4563,-0.3022,-0.8369,0.4259,0.5458,-0.2525,-0.799,0.4765,0.6156,-0.212,-0.759,0.5419,0.6669,-0.1864,-0.7215,0.612,0.7064,-0.1755,-0.6857,0.6873,0.7362,-0.1766,-0.6534,0.7615,0.7624,-0.1781,-0.6221,0.8308,0.7859,-0.1769,-0.5925,0.8966,0.8093,-0.1717,-0.5617,0.9524,0.8333,-0.1622,-0.5285,0.9996,0.8556,-0.1498,-0.4955,1.036,0.8766,-0.1376,-0.4612,1.0637,0.8964,-0.127,-0.4247,1.0796,0.9137,-0.119,-0.3885,1.0833,0.9291,-0.1159,-0.3511,1.0757,0.9433,-0.1132,-0.312,1.0601,0.9562,-0.1154,-0.269,1.0356,0.9674,-0.1208,-0.2228,1.0046,0.9765,-0.1294,-0.1723,0.9671,0.9817,-0.1467,-0.1215,0.9221,0.9827,-0.173,-0.0661,0.8732,0.9783,-0.2071,-0.0093,0.8205,0.9672,-0.2488,0.0506,0.7617,0.9478,-0.2984,0.1119,0.7046,0.9171,-0.3538,0.1835,0.6452,0.8779,-0.3996,0.2638,0.5845,0.8283,-0.4363,0.3516,0.5267,0.7617,-0.4596,0.4566,0.4734,0.6699,-0.4687,0.5758,0.4271,0.5602,-0.4527,0.6938,0.3932,0.4501,-0.4194,0.7884,0.3733,0.3692,-0.3908,0.8432,0.3669,0.3324,-0.3776,0.8643,0.3703,0.3277,-0.3663,0.8709,0.3738,0.3397,-0.3667,0.8661,0.3764,0.342,-0.3774,0.8606,0.3748,0.3443,-0.3913,0.8535,0.3696,0.37,-0.397,0.8399,0.365,0.4183,-0.3879,0.8213,0.3567,0.4853,-0.3645,0.7947,0.3457,0.552,-0.3414,0.7608,0.3307,0.6071,-0.332,0.722,0.3141,0.6348,-0.3425,0.6926,0.2956,0.6429,-0.3593,0.6764,0.2767,0.6504,-0.3532,0.6725,0.2518,0.6672,-0.3134,0.6758,0.2254,0.6854,-0.2739,0.6747,0.1992,0.6979,-0.2389,0.6752,0.1758,0.7131,-0.2148,0.6673,0.1551,0.7223,-0.1705,0.6702,0.1379,0.7448,-0.0464,0.6657,0.1212,0.7441,0.1278,0.6557,0.1056,0.7019,0.3145,0.639,0.0924,0.6106,0.4649,0.6411,0.0789,0.431,0.6096,0.6653,0.0649,0.166,0.6987,0.6959,0.0505,-0.2722,0.7792,0.5645,0.0408,-0.6817,0.6628,0.3097,0.0407,-0.8725,0.4843,0.0648,0.0479,-0.9485,0.3049,-0.0855,0.0585,-0.9534,0.2175,-0.2092,0.0704,-0.9346,0.1396,-0.327,0.0829,-0.8928,0.0237,-0.4499,0.0905,-0.8326,-0.1029,-0.5443,0.1007,-0.7653,-0.2085,-0.6089,0.1106,-0.6941,-0.2708,-0.667,0.1234,-0.6219,-0.2956,-0.7251,0.1376,-0.5452,-0.3145,-0.777,0.1494,-0.4844,-0.3289,-0.8107,0.1595,-0.4291,-0.3336,-0.8394,0.1711,-0.3734,-0.3304,-0.8668,0.1834,-0.3178,-0.3126,-0.8952,0.1935,-0.2604,-0.2973,-0.9186,0.2038,-0.1994,-0.2891,-0.9363,0.2136,-0.1298,-0.2787,-0.9516,0.2256,-0.051,-0.2705,-0.9614,0.2397,0.0285,-0.2701,-0.9624,0.2544,0.1093,-0.2732,-0.9557,0.2727,0.1966,-0.2715,-0.9422,0.2919,0.299,-0.2624,-0.9175,0.3145,0.3955,-0.239,-0.8868,0.3436,0.4929,-0.2036,-0.8459,0.381,0.5854,-0.1602,-0.7948,0.4253,0.664,-0.1104,-0.7395,0.4842,0.7258,-0.0685,-0.6845,0.5535,0.7728,-0.0389,-0.6335,0.6308,0.8058,-0.0262,-0.5917,0.7078,0.8315,-0.0295,-0.5547,0.7839,0.8504,-0.0385,-0.5247,0.8561,0.8675,-0.0482,-0.4951,0.9202,0.8845,-0.0526,-0.4636,0.9727,0.9004,-0.0557,-0.4315,1.0146,0.9142,-0.06,-0.4008,1.0462,0.9269,-0.0651,-0.3697,1.0632,0.9389,-0.0707,-0.3367,1.0676,0.9498,-0.0789,-0.3028,1.0573,0.9587,-0.0913,-0.2693,1.0352,0.9658,-0.1088,-0.2352,1.0031,0.9706,-0.1346,-0.1995,0.9638,0.9729,-0.1617,-0.1652,0.9156,0.9726,-0.1952,-0.1265,0.8619,0.969,-0.2332,-0.0816,0.8041,0.96,-0.2778,-0.0334,0.7465,0.9445,-0.3276,0.026,0.6898,0.924,-0.3716,0.09,0.6378,0.9017,-0.402,0.1595,0.5887,0.8823,-0.4109,0.2296,0.5431,0.864,-0.3995,0.3065,0.5023,0.8449,-0.3718,0.3845,0.4651,0.8202,-0.3397,0.4603,0.4343,0.7939,-0.3107,0.5227,0.4096,0.7732,-0.2925,0.5627,0.3892,0.7504,-0.2909,0.5935,0.3729,0.7178,-0.3203,0.6182,0.3604,0.6807,-0.3645,0.6354,0.3476,0.6436,-0.4082,0.6475,0.3353,0.6221,-0.4227,0.659,0.322,0.6144,-0.4074,0.6757,0.3059,0.6225,-0.3587,0.6956,0.2902,0.6401,-0.2889,0.7119,0.2741,0.6544,-0.218,0.724,0.2563,0.6654,-0.1795,0.7245,0.2424,0.6563,-0.1663,0.736,0.2249,0.6329,-0.1863,0.7515,0.2061,0.5996,-0.1952,0.7761,0.1894,0.5718,-0.1881,0.7985,0.1714,0.538,-0.1638,0.8269,0.1547,0.5143,-0.1182,0.8494,0.1401,0.4883,-0.0564,0.8709,0.1289,0.4629,0.0045,0.8864,0.1215])

Group366.addChildren(OrientationInterpolator374)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-34.92207,19.195293], [-6.526618,57.245258], [-17.028704,12.703618] degrees
#-3.939975 -3.766201 -3.474078, -3.939975 -3.766201 -3.474078, -4.087531 -3.824402 -3.466879, -4.093241 -3.948997 -3.561182, -3.960619 -3.866694 -3.550377, -3.834370 -3.738754 -3.621544, -3.733652 -3.667324 -3.838453, -3.589555 -3.601340 -4.046555, -3.461005 -3.476283 -4.231246, -3.332685 -3.350797 -4.416099, -3.266505 -3.290072 -4.620756, -3.331850 -3.232222 -4.834424, -3.179870 -3.090900 -5.115561, -3.134691 -2.879325 -5.384120, -3.003442 -2.709592 -5.697166, -2.981100 -2.594460 -6.091019, -3.026685 -2.662159 -6.522533, -3.069262 -2.731425 -6.791653, -3.114120 -2.800296 -6.948999, -3.249367 -2.986074 -7.172327, -3.594525 -3.161520 -7.201317, -4.032129 -3.447166 -7.411406, -4.625803 -3.725826 -7.847285, -5.088897 -3.983961 -8.491629, -5.372149 -4.290939 -8.918939, -5.630632 -4.444394 -9.088295, -5.838985 -4.620029 -9.029859, -6.027059 -4.960439 -8.716910, -6.115529 -5.148654 -8.475998, -6.099472 -5.420537 -8.085193, -6.181458 -5.613129 -7.681916, -6.189431 -5.747969 -7.267530, -6.147818 -5.755021 -6.843904, -6.255480 -5.851282 -6.498271, -6.253995 -6.034492 -6.158106, -6.269282 -6.180486 -5.850351, -6.302267 -6.361139 -5.670412, -6.354571 -6.514375 -5.490971, -6.570467 -6.517792 -5.438235, -6.789512 -6.514420 -5.548758, -7.076112 -6.526618 -5.768890, -7.408134 -6.390126 -6.067214, -7.745207 -6.324413 -6.534191, -7.691460 -6.044915 -7.136610, -7.822977 -5.769712 -7.841972, -7.927781 -5.536735 -8.354908, -7.910833 -5.437178 -8.525034, -8.001611 -5.373817 -8.387547, -8.145371 -5.328479 -8.017870, -8.307655 -5.338922 -7.658227, -8.661688 -5.578624 -7.437864, -9.277953 -5.737038 -7.540685, -9.698742 -5.924809 -7.826411, -9.999862 -6.089008 -7.994178, -10.215347 -6.237994 -8.108297, -10.422400 -6.397584 -8.174664, -10.669665 -6.291948 -8.091794, -10.996106 -6.028053 -7.992971, -11.114440 -5.739970 -7.876284, -11.451788 -5.384835 -7.900877, -11.935874 -4.984858 -7.923724, -12.334879 -4.490746 -7.964097, -12.866072 -3.907377 -8.058410, -13.250233 -3.297686 -7.980925, -13.683358 -2.508712 -7.973041, -14.109074 -1.699534 -7.766320, -14.538452 -0.891067 -7.556117, -14.963526 -0.160992 -7.286780, -15.473159 0.648736 -6.808437, -15.991401 1.655376 -6.125971, -16.447624 3.029521 -5.395289, -17.038933 4.665825 -4.491837, -17.731054 6.864288 -3.312119, -18.405849 9.472552 -2.057152, -19.537600 12.644535 -0.736564, -20.874128 16.042168 0.583533, -22.456200 19.847546 1.638013, -24.094213 23.915976 2.136521, -25.612638 28.165661 2.267411, -26.857290 32.484062 2.245345, -27.852926 36.589249 2.581597, -28.684603 40.378040 3.424374, -29.285950 43.810497 4.877421, -29.439875 46.732677 6.548551, -28.858059 49.062382 7.980522, -27.568747 50.896484 8.984966, -25.615826 52.112766 9.347354, -22.959755 52.546753 8.670194, -19.739666 52.333656 7.110879, -16.154879 51.355556 4.934896, -12.590123 49.914364 2.477232, -9.165704 47.850990 -0.204507, -5.829761 45.448902 -2.821702, -2.478240 42.722332 -5.636001, 0.668505 39.589931 -8.559116, 3.421243 36.293816 -11.095500, 5.946341 32.938625 -13.049797, 8.161756 29.437809 -14.208281, 10.127060 25.971972 -14.641338, 11.744483 22.531145 -14.220431, 13.244369 19.216454 -13.247885, 14.416320 16.009758 -11.967554, 15.565923 12.927683 -10.789451, 16.512854 10.238226 -9.828478, 17.148540 8.059446 -9.069825, 17.673113 6.668108 -8.787449, 18.202393 6.049401 -8.952033, 18.523430 6.106709 -9.189127, 18.672489 6.336034 -9.306707, 18.635103 6.692642 -9.283475, 18.458456 6.867680 -8.969679, 18.247967 6.904797 -8.558421, 17.941015 6.707598 -8.434866, 17.530581 6.453153 -8.702065, 16.869535 6.539927 -8.814102, 15.933082 6.751630 -8.424598, 14.835796 6.949809 -7.922245, 13.683020 6.902159 -7.488574, 12.537408 6.541054 -7.044241, 11.512815 5.775104 -6.944696, 10.494855 4.932518 -6.741942, 9.597046 4.051138 -6.111510, 8.769696 3.302735 -5.374659, 8.036599 2.671685 -4.520710, 7.208016 2.004367 -3.917926, 6.521704 1.402388 -3.371747, 5.826421 0.782313 -3.004404, 5.151680 0.214437 -2.676588, 4.781635 -0.277601 -2.224233, 4.315220 -0.707148 -1.763667, 3.841243 -1.201668 -1.440767, 3.258109 -1.550754 -1.275537, 2.642500 -1.814142 -1.318911, 2.071136 -2.070072 -1.458391, 1.434001 -2.313149 -1.556014, 0.751414 -2.592101 -1.848135, 0.069603 -2.905336 -2.239288, -0.780232 -3.189277 -2.887095, -1.745952 -3.519694 -3.642198, -2.699433 -3.805180 -4.438111, -3.567453 -4.077834 -5.126541, -4.718138 -4.397607 -5.694162, -5.781164 -4.773260 -6.134012, -6.787304 -5.190460 -6.622773, -7.787150 -5.356984 -7.135412, -8.788046 -5.308338 -7.619725, -9.602497 -5.056894 -7.885675, -10.416606 -4.655948 -7.997668, -11.415977 -3.987782 -8.081615, -12.382151 -2.985920 -8.195743, -13.527860 -1.635356 -8.322394, -14.570342 -0.151864 -8.462132, -15.578365 1.573353 -8.443415, -16.554119 3.637314 -8.082532, -17.547707 6.141714 -7.404226, -18.659086 8.951082 -6.481070, -19.944935 12.186837 -5.326556, -21.408230 15.832149 -4.006531, -23.359873 19.912144 -2.584796, -25.417456 24.048876 -1.238330, -27.549919 28.392221 -0.089850, -29.532516 32.672783 0.748944, -31.233725 36.807732 1.644393, -32.842697 40.794899 2.780060, -33.995316 44.425201 4.106742, -34.689724 47.764820 5.626235, -34.922070 50.579426 7.149245, -34.554394 53.025978 8.381177, -33.212452 54.976620 8.937463, -30.950056 56.288948 8.655535, -27.633541 57.025135 7.312683, -23.712614 57.245258 5.483645, -18.946463 56.897671 2.810928, -13.842920 55.981941 -0.207533, -8.623897 54.443554 -3.332947, -3.718814 52.122662 -6.514160, 0.891989 49.221615 -9.640932, 4.739643 45.741348 -12.292856, 7.799412 41.610870 -14.347097, 10.126727 37.299500 -15.947546, 12.026262 32.582626 -17.018156, 13.326240 27.836344 -17.028704, 14.227730 23.300753 -16.364185, 15.114910 18.916754 -15.185034, 16.005224 14.669018 -13.681065, 16.886806 10.990486 -11.939180, 17.673098 8.127779 -10.323455, 18.302038 6.345594 -9.318274, 18.836460 5.633483 -9.026444, 19.139187 5.603265 -8.871451, 19.195293 5.889776 -8.987277, 19.009691 5.892982 -9.175154, 18.607635 5.844045 -9.324980, 18.141371 6.322053 -9.389671, 17.422213 7.240291 -9.110630, 16.428471 8.469862 -8.506667, 15.118213 9.506368 -7.784500, 13.686287 10.126665 -7.236768, 12.387758 10.058430 -6.932853, 11.323479 9.579226 -6.680845, 10.188030 8.890215 -5.912348, 9.090088 8.266467 -4.722108, 7.958160 7.584525 -3.664634, 6.981262 6.867752 -2.832175, 6.060039 6.226485 -2.242952, 5.379089 5.635438 -1.614063, 4.650719 5.154063 -0.531760, 3.943882 4.523850 0.618039, 3.331857 3.761120 1.556167, 2.847616 2.809937 2.031168, 2.441680 1.650509 2.231561, 2.003389 0.515210 2.011342, 1.328842 -0.614924 1.827664, 0.743837 -1.580206 1.556455, 0.205530 -2.390968 1.333050, -0.258781 -3.183863 1.015578, -0.815626 -3.852218 0.850361, -1.531057 -4.448983 0.604133, -2.331881 -4.628253 0.028659, -3.171337 -4.783138 -0.726456, -3.922614 -4.799909 -1.486444, -4.809152 -4.822401 -2.119582, -5.829910 -4.778097 -2.577636, -6.770525 -4.496989 -2.962266, -7.535018 -4.217787 -3.289692, -8.358459 -3.955629 -3.567377, -9.234919 -3.629437 -3.773475, -10.033749 -3.202851 -3.756367, -10.818011 -2.696127 -3.736872, -11.533575 -2.069666 -3.760307, -12.346911 -1.279258 -3.754648, -13.215220 -0.267569 -3.761704, -14.002190 0.890158 -3.847023, -14.863503 2.240021 -4.001281, -15.633396 3.864088 -4.039954, -16.351839 5.988516 -3.903659, -17.240421 8.373788 -3.476746, -18.267332 11.282914 -2.678101, -19.286901 14.646504 -1.460235, -20.748188 18.572023 0.305994, -22.487539 22.863523 2.372995, -24.479866 27.420935 4.603004, -26.542624 31.844118 6.589016, -28.492496 36.290810 8.114017, -30.411554 40.487072 9.437781, -31.895235 44.405396 10.568786, -32.737694 47.865753 11.667150, -32.923698 50.899216 12.462738, -32.447273 53.443703 12.703618, -30.887066 55.322247 12.093710, -28.255590 56.602875 10.648288, -24.529251 57.080936 8.205296, -20.146025 56.773754 5.016072, -15.407351 55.705070 1.346170, -10.557292 53.977562 -2.665480, -6.402997 51.430992 -6.025434, -2.563802 48.323372 -9.105699, 0.843890 44.727917 -11.672470, 3.659465 40.875282 -13.782959, 6.260497 36.804825 -15.509439, 8.293514 32.929943 -16.443687, 9.877722 29.331856 -16.485388, 10.979002 26.254133 -15.619828, 11.984180 23.630465 -14.221028, 12.767410 21.333775 -12.479837, 13.453741 19.306690 -10.871564, 13.875176 17.619938 -9.544771, 13.893015 16.324497 -8.601796, 13.862700 15.160343 -8.136711, 13.876287 13.909965 -8.380249, 13.710710 12.594725 -8.844252, 13.426375 11.363462 -9.243920, 13.050978 10.517782 -9.060328, 12.613075 9.918784 -8.286085, 12.201921 9.654469 -7.034683, 11.677664 9.531848 -5.540803, 10.994650 9.251282 -4.110190, 10.348771 8.972024 -3.319894, 9.705316 8.235996 -2.851919, 9.063526 7.269543 -2.784306, 8.576174 6.326198 -2.599717, 7.953456 5.468631 -2.231707, 7.405807 4.662607 -1.756797, 6.864078 4.062303 -1.193797, 6.451123 3.574063 -0.618832, 6.175721 3.217674 -0.142123
#Interpolator4_l_ankle channels [12..14] sends animation values to BVH JOINT LeftAnkle, DEF Bvh1_l_ankle, <HAnimJoint name=l_ankle/>
OrientationInterpolator375 = OrientationInterpolator()
OrientationInterpolator375.setDEF("Interpolator4_l_ankle")
OrientationInterpolator375.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator375.setKeyValue([0.7009,0.2504,0.6678,0.0639,0.7009,0.2504,0.6678,0.0639,0.6943,0.226,0.6833,0.0645,0.6943,0.226,0.6833,0.0645,0.6943,0.226,0.6833,0.0645,0.7009,0.2504,0.6678,0.0639,0.704,0.2862,0.6499,0.0657,0.7104,0.3434,0.6143,0.0671,0.6888,0.4142,0.595,0.0693,0.6805,0.4806,0.5532,0.0715,0.6433,0.565,0.5167,0.0744,0.598,0.6407,0.4816,0.0764,0.5253,0.7393,0.4213,0.0794,0.4586,0.8049,0.3765,0.0822,0.4179,0.847,0.3285,0.0845,0.3595,0.8821,0.3045,0.0854,0.3476,0.8938,0.2833,0.0856,0.3426,0.8984,0.2748,0.0843,0.3554,0.8973,0.2617,0.0788,0.3869,0.8899,0.2417,0.0715,0.435,0.8714,0.2269,0.0598,0.5045,0.825,0.2545,0.0511,0.5689,0.7128,0.4101,0.0496,0.5854,0.6516,0.4825,0.0546,0.6125,0.619,0.4917,0.0615,0.625,0.6092,0.4881,0.0648,0.6158,0.6527,0.4413,0.0672,0.6359,0.6699,0.3831,0.0678,0.6066,0.7513,0.2598,0.0649,0.5889,0.8058,0.0633,0.0619,0.5447,0.821,-0.1708,0.059,0.4476,0.7848,-0.4287,0.0563,0.3165,0.6845,-0.6567,0.0594,0.2166,0.6146,-0.7585,0.0621,0.2197,0.514,-0.8292,0.0631,0.2782,0.3864,-0.8794,0.061,0.3969,0.2595,-0.8804,0.0585,0.5244,0.0452,-0.8503,0.0541,0.6411,-0.1698,-0.7484,0.0521,0.7255,-0.3277,-0.6051,0.0528,0.7868,-0.4185,-0.4537,0.0547,0.832,-0.4848,-0.2697,0.0536,0.8712,-0.4885,-0.0488,0.0535,0.8878,-0.4239,0.1791,0.0566,0.8647,-0.3131,0.3926,0.0595,0.808,-0.2159,0.5482,0.0654,0.7578,-0.1445,0.6363,0.0684,0.7187,-0.0878,0.6898,0.0704,0.6717,-0.0791,0.7366,0.0653,0.6207,-0.12,0.7748,0.0559,0.565,-0.1536,0.8107,0.0483,0.3928,-0.226,0.8914,0.0414,0.2306,-0.2792,0.9321,0.0393,0.0969,-0.2909,0.9519,0.0394,-0.0606,-0.2882,0.9557,0.0395,-0.1106,-0.1943,0.9747,0.0429,-0.1758,-0.1354,0.9751,0.0465,-0.2823,-0.1036,0.9537,0.0499,-0.3634,-0.0963,0.9266,0.0542,-0.4372,-0.1142,0.8921,0.0588,-0.5016,-0.1478,0.8524,0.066,-0.6007,-0.1785,0.7793,0.0749,-0.6512,-0.1931,0.734,0.0834,-0.7125,-0.2207,0.666,0.0902,-0.7601,-0.2443,0.6022,0.098,-0.8031,-0.2667,0.5329,0.106,-0.8296,-0.2865,0.4793,0.1128,-0.8386,-0.3163,0.4435,0.1153,-0.8337,-0.3772,0.4034,0.1177,-0.8215,-0.4465,0.3545,0.1166,-0.7931,-0.5379,0.2859,0.1136,-0.727,-0.6541,0.2087,0.1086,-0.5975,-0.7929,0.1196,0.1036,-0.365,-0.9307,-0.0231,0.0986,-0.0157,-0.9847,-0.1738,0.103,0.3742,-0.878,-0.2985,0.123,0.6174,-0.7033,-0.3524,0.1561,0.7548,-0.5436,-0.367,0.1911,0.8399,-0.42,-0.3438,0.2149,0.9083,-0.313,-0.2775,0.2191,0.9679,-0.1882,-0.1667,0.2132,0.9997,-0.0246,0.0063,0.2007,0.9683,0.1408,0.2065,0.1974,0.8842,0.2732,0.3788,0.2014,0.7828,0.3458,0.5173,0.2003,0.6872,0.3735,0.6231,0.1942,0.5856,0.3588,0.7268,0.1813,0.4963,0.3047,0.8129,0.1681,0.4088,0.245,0.8792,0.1527,0.3203,0.1888,0.9283,0.1363,0.2052,0.1683,0.9641,0.117,0.0426,0.1798,0.9828,0.0997,-0.1799,0.198,0.9635,0.0812,-0.5232,0.2339,0.8195,0.0618,-0.9009,0.2456,0.3579,0.0516,-0.9507,0.179,-0.253,0.063,-0.8103,0.1239,-0.5727,0.0899,-0.6862,0.1067,-0.7195,0.1246,-0.5873,0.1101,-0.8019,0.1631,-0.5169,0.1085,-0.8492,0.2011,-0.4537,0.1039,-0.8851,0.2402,-0.4088,0.1024,-0.9068,0.277,-0.369,0.1022,-0.9238,0.3123,-0.3387,0.1026,-0.9353,0.342,-0.317,0.0943,-0.9437,0.3616,-0.299,0.0852,-0.9504,0.3744,-0.281,0.0844,-0.956,0.3802,-0.2574,0.0847,-0.9626,0.3815,-0.227,0.0865,-0.97,0.3785,-0.1804,0.0984,-0.9787,0.3717,-0.1086,0.0955,-0.9895,0.3596,-0.022,0.0775,-0.9968,0.3456,0.0621,0.0527,-0.9967,0.3361,0.1443,0.0357,-0.9889,0.3315,0.2102,0.0307,-0.9772,0.3241,0.2606,0.0367,-0.9647,0.3181,0.2959,0.064,-0.9531,0.3117,0.3136,0.1046,-0.9438,0.3068,0.3127,0.1481,-0.9382,0.3006,0.316,0.1949,-0.9285,0.2939,0.3361,0.2204,-0.9157,0.2848,0.3603,0.2242,-0.9055,0.2705,0.3877,0.2193,-0.8953,0.254,0.4099,0.2089,-0.8879,0.2409,0.426,0.2157,-0.8786,0.2281,0.4321,0.2302,-0.872,0.2187,0.4266,0.2551,-0.8677,0.2094,0.4112,0.2876,-0.865,0.2012,0.3902,0.308,-0.8677,0.1933,0.3805,0.3213,-0.8672,0.1835,0.3715,0.344,-0.8624,0.1747,0.3415,0.3749,-0.8619,0.1642,0.2895,0.4087,-0.8655,0.1556,0.2195,0.4489,-0.8662,0.1496,0.1287,0.4663,-0.8752,0.1433,0.0307,0.4636,-0.8855,0.137,-0.0793,0.4491,-0.89,0.1336,-0.1805,0.4272,-0.886,0.1306,-0.2824,0.4228,-0.8611,0.1256,-0.3656,0.396,-0.8423,0.1222,-0.4563,0.3566,-0.8153,0.1207,-0.5419,0.3002,-0.785,0.1164,-0.6121,0.2139,-0.7613,0.1123,-0.6811,0.1329,-0.72,0.1073,-0.7622,0.0494,-0.6455,0.1033,-0.8351,-0.0371,-0.5488,0.0989,-0.8985,-0.1097,-0.425,0.0988,-0.9331,-0.1998,-0.2989,0.1023,-0.944,-0.2779,-0.178,0.1091,-0.9399,-0.3299,-0.0881,0.1206,-0.9261,-0.3772,-0.0082,0.1327,-0.9064,-0.4206,0.0395,0.1431,-0.8767,-0.4771,0.0611,0.1479,-0.8285,-0.5575,0.0522,0.1516,-0.7492,-0.6621,0.0191,0.1486,-0.618,-0.7843,-0.0542,0.1401,-0.3739,-0.9088,-0.1851,0.1284,0.04,-0.916,-0.3993,0.1284,0.4286,-0.7366,-0.5232,0.1567,0.6296,-0.5478,-0.5509,0.1999,0.7322,-0.418,-0.5377,0.2344,0.8067,-0.3153,-0.4998,0.2507,0.871,-0.2196,-0.4395,0.2491,0.9332,-0.1066,-0.3433,0.238,0.9796,0.0128,-0.2004,0.2244,0.99,0.1388,-0.0267,0.2075,0.9521,0.2546,0.1696,0.1953,0.8736,0.3275,0.3599,0.185,0.7749,0.3509,0.5257,0.1779,0.6773,0.3299,0.6576,0.167,0.5739,0.2921,0.765,0.1529,0.4371,0.2553,0.8624,0.1328,0.2551,0.2133,0.9431,0.1095,-0.029,0.1643,0.986,0.0902,-0.3813,0.0917,0.9199,0.0771,-0.7194,0.041,0.6933,0.0731,-0.9573,-0.0044,0.289,0.0779,-0.992,0.005,-0.1265,0.0951,-0.9101,0.0253,-0.4137,0.1224,-0.8032,0.0428,-0.5942,0.1586,-0.7018,0.0598,-0.7099,0.2028,-0.6139,0.076,-0.7857,0.2474,-0.5391,0.0974,-0.8366,0.2901,-0.4637,0.1041,-0.8799,0.3273,-0.3945,0.1065,-0.9127,0.3626,-0.3419,0.1101,-0.9333,0.3942,-0.3065,0.1063,-0.9459,0.4185,-0.2745,0.105,-0.9558,0.4282,-0.2359,0.1081,-0.9657,0.4278,-0.1942,0.1077,-0.975,0.4204,-0.1476,0.1171,-0.9821,0.4101,-0.0741,0.1411,-0.9872,0.3943,0.015,0.1676,-0.9857,0.3766,0.0983,0.1895,-0.977,0.3672,0.1679,0.2154,-0.962,0.3559,0.2163,0.2462,-0.9448,0.341,0.2522,0.2905,-0.923,0.3248,0.2776,0.345,-0.8966,0.3056,0.2977,0.4039,-0.865,0.2882,0.3166,0.4516,-0.8342,0.2671,0.3423,0.4678,-0.8149,0.2434,0.3697,0.4777,-0.797,0.2161,0.4033,0.4937,-0.7705,0.1937,0.4235,0.5169,-0.7439,0.1744,0.4409,0.5708,-0.6927,0.161,0.4466,0.6347,-0.6307,0.1535,0.449,0.6822,-0.5771,0.1425,0.4579,0.7108,-0.534,0.1314,0.4534,0.7376,-0.5004,0.1205,0.436,0.766,-0.4723,0.1151,0.4268,0.7697,-0.4748,0.1118,0.4123,0.7711,-0.4852,0.1117,0.3993,0.7674,-0.5017,0.1056,0.3885,0.7534,-0.5305,0.1008,0.3603,0.7574,-0.5446,0.0946,0.3194,0.7535,-0.5747,0.0901,0.2819,0.7548,-0.5923,0.0842,0.2048,0.7383,-0.6426,0.0797,0.0936,0.744,-0.6616,0.0736,-0.012,0.7709,-0.6368,0.0678,-0.1809,0.7724,-0.6088,0.0631,-0.3719,0.7577,-0.5363,0.0588,-0.5922,0.6824,-0.4285,0.0584,-0.7814,0.5549,-0.2856,0.062,-0.8696,0.4515,-0.2001,0.072,-0.9192,0.3582,-0.1638,0.0826,-0.9506,0.2792,-0.1356,0.0934,-0.9688,0.2137,-0.1258,0.1059,-0.9788,0.1507,-0.1385,0.1192,-0.9837,0.0939,-0.1536,0.1317,-0.9867,0.0459,-0.1559,0.1451,-0.9872,-0.0016,-0.1598,0.1557,-0.9822,-0.064,-0.1767,0.1613,-0.974,-0.135,-0.1819,0.1633,-0.9533,-0.2192,-0.2078,0.1615,-0.9145,-0.3224,-0.2445,0.1537,-0.8318,-0.4579,-0.3138,0.1419,-0.6594,-0.6087,-0.4412,0.1284,-0.3007,-0.7138,-0.6325,0.126,0.1264,-0.677,-0.725,0.1493,0.4152,-0.5616,-0.7157,0.1945,0.5692,-0.4595,-0.6818,0.241,0.6689,-0.3784,-0.6399,0.2749,0.7425,-0.3,-0.5989,0.2924,0.8107,-0.2158,-0.5443,0.2883,0.8723,-0.1186,-0.4744,0.2719,0.925,-0.0104,-0.3798,0.2528,0.9546,0.0953,-0.2822,0.2358,0.96,0.2011,-0.1948,0.2135,0.9527,0.2839,-0.1084,0.1858,0.9363,0.3508,-0.0161,0.1554,0.9094,0.4034,0.1018,0.1241,0.8517,0.4533,0.263,0.0981,0.7096,0.5619,0.4251,0.0756,0.3972,0.7534,0.524,0.0575,-0.0841,0.9274,0.3646,0.0472,-0.4818,0.8617,-0.1592,0.0503,-0.5669,0.5994,-0.5651,0.0733,-0.545,0.4145,-0.7288,0.1044,-0.4829,0.323,-0.8139,0.1347,-0.4102,0.2684,-0.8716,0.1629,-0.3214,0.2479,-0.9139,0.1884,-0.2593,0.2222,-0.9399,0.2077,-0.2053,0.209,-0.9561,0.2296,-0.1579,0.1952,-0.968,0.2499,-0.0993,0.1808,-0.9785,0.2686,-0.0594,0.1674,-0.9841,0.288,-0.041,0.1545,-0.9871,0.3026,-0.0285,0.1349,-0.9904,0.3138,-0.0104,0.1332,-0.991,0.3205,0.0328,0.1498,-0.9882,0.3173,0.0976,0.1948,-0.976,0.3057,0.1542,0.2427,-0.9578,0.2923,0.2093,0.2878,-0.9346,0.2798,0.2543,0.3118,-0.9155,0.2687,0.286,0.3303,-0.8995,0.2599,0.3109,0.3457,-0.8854,0.2508,0.3222,0.3716,-0.8707,0.2433,0.3474,0.4066,-0.845,0.2378,0.3623,0.4359,-0.8238,0.2325,0.3805,0.4612,-0.8016,0.2261,0.4073,0.4747,-0.7803,0.2145,0.4327,0.4843,-0.7604,0.2058,0.4506,0.5056,-0.7358,0.1967,0.4709,0.5292,-0.7058,0.1904,0.4862,0.5515,-0.6778,0.1862])

Group366.addChildren(OrientationInterpolator375)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-23.619896,7.722682], [-9.093368,13.668425], [-6.728483,7.403621] degrees
#2.425202 2.584131 0.862019, 2.425202 2.584131 0.862019, 2.507924 2.583092 0.778887, 2.507924 2.583092 0.778887, 2.507924 2.583092 0.778887, 2.425202 2.584131 0.862019, 2.423151 2.672199 1.021105, 2.331845 2.757493 1.264444, 2.324676 2.767895 1.588864, 2.219845 2.825402 1.914622, 2.147104 2.788701 2.358574, 2.043523 2.666124 2.756536, 1.845469 2.442871 3.322897, 1.701275 2.216076 3.758269, 1.516805 2.077536 4.072685, 1.423512 1.814161 4.296466, 1.323453 1.756366 4.364845, 1.263316 1.702997 4.319884, 1.123673 1.644183 4.033422, 0.939131 1.615444 3.632405, 0.738429 1.509712 2.975586, 0.714545 1.493644 2.408378, 1.136336 1.636020 2.008490, 1.476841 1.857568 2.014554, 1.692564 2.191121 2.149876, 1.767853 2.356368 2.227104, 1.647455 2.406780 2.478721, 1.432222 2.502295 2.570813, 0.911024 2.277973 2.775821, 0.172392 2.093017 2.854671, -0.622351 1.828009 2.787702, -1.413738 1.411840 2.547649, -2.256546 1.031254 2.350314, -2.711773 0.718547 2.203094, -3.011640 0.745669 1.879156, -3.086140 0.935855 1.376735, -2.961441 1.307315 0.903848, -2.639648 1.622627 0.177630, -2.228441 1.924794 -0.470068, -1.812047 2.209719 -0.956298, -1.393627 2.480125 -1.280955, -0.796149 2.567468 -1.472320, -0.114666 2.672522 -1.495068, 0.615512 2.869852 -1.389345, 1.367952 2.936934 -1.103553, 2.078010 3.013291 -0.864071, 2.509998 2.955920 -0.631222, 2.795570 2.891051 -0.425056, 2.765944 2.506295 -0.356560, 2.490947 1.980154 -0.427704, 2.250733 1.555493 -0.455848, 2.117086 0.920921 -0.552645, 2.103763 0.508132 -0.638698, 2.148133 0.206115 -0.659964, 2.161341 -0.149437 -0.649195, 2.397282 -0.282166 -0.472345, 2.596385 -0.476399 -0.350118, 2.724742 -0.813723 -0.276890, 2.873708 -1.134987 -0.270375, 3.001080 -1.482456 -0.346130, 3.214745 -1.911450 -0.505587, 3.329103 -2.598218 -0.690572, 3.484975 -3.137272 -0.827606, 3.411432 -3.715842 -1.031346, 3.335580 -4.304617 -1.247071, 3.176093 -4.922218 -1.485297, 3.018499 -5.406498 -1.710445, 2.837440 -5.591376 -1.953514, 2.602935 -5.678675 -2.417490, 2.231601 -5.546670 -2.877692, 1.707146 -5.215414 -3.426120, 1.139465 -4.567967 -4.028709, 0.564360 -3.572576 -4.691836, -0.225312 -2.053906 -5.264689, -1.028463 -0.040582 -5.811797, -1.958845 2.744969 -6.141535, -2.850835 5.680039 -6.153817, -3.607931 8.454725 -5.699182, -3.802645 10.511350 -4.837614, -3.131095 11.508204 -3.628534, -1.823082 11.856555 -2.117942, 0.102901 11.497493 -0.294553, 2.209850 10.980565 1.385456, 4.131631 10.308961 2.789449, 5.669469 9.169767 3.526323, 6.692408 7.875071 3.706229, 7.377176 6.308747 3.329604, 7.722682 4.964311 2.605814, 7.634739 3.709096 1.899904, 7.219032 2.586866 1.312547, 6.452985 1.436670 1.048864, 5.612273 0.293318 1.013939, 4.486987 -0.799598 0.952553, 2.917699 -1.831618 0.875518, 1.076203 -2.657840 0.751543, -0.894876 -3.435911 0.619365, -2.932677 -4.189389 0.531615, -5.114984 -4.925286 0.542316, -7.464610 -5.537964 0.669507, -9.753782 -6.032449 0.739431, -12.152410 -6.349151 0.760042, -14.364840 -6.624610 0.800302, -16.496368 -6.773037 0.861199, -18.291426 -6.841619 0.927909, -19.526117 -6.771546 0.809087, -20.375408 -6.602769 0.660624, -20.807184 -6.318341 0.699890, -21.018391 -5.835792 0.789529, -21.007202 -5.153993 0.942987, -20.804256 -4.134989 1.359953, -20.359850 -2.537633 1.533395, -19.731369 -0.687919 1.430441, -19.205669 1.005236 1.194781, -18.809288 2.581347 1.111985, -18.189281 3.749157 1.174697, -17.647547 4.572639 1.385036, -17.119471 5.037562 1.911568, -16.719404 5.168798 2.613010, -16.316854 4.954871 3.280085, -15.818650 4.806251 3.972400, -15.143521 4.950146 4.278693, -14.231320 5.100270 4.131271, -13.220236 5.228276 3.814876, -12.427890 5.303133 3.474980, -11.648831 5.245377 3.366304, -11.087652 5.104040 3.391272, -10.566739 4.809288 3.516150, -10.124657 4.425951 3.718104, -9.746976 4.012103 3.762206, -9.245358 3.713213 3.687502, -8.749837 3.442718 3.714241, -8.207246 2.950294 3.744063, -7.800241 2.327383 3.809307, -7.486339 1.625862 3.960786, -7.214705 0.813421 3.884326, -6.953074 0.020067 3.644695, -6.792846 -0.809382 3.394863, -6.589338 -1.531509 3.111508, -6.143826 -2.192420 2.928502, -5.839762 -2.698032 2.638642, -5.573421 -3.269875 2.308733, -5.179349 -3.700901 1.837189, -4.860403 -3.993556 1.208354, -4.405800 -4.216228 0.655791, -3.815252 -4.515814 0.142070, -3.124770 -4.722589 -0.338998, -2.439898 -5.072422 -0.729393, -1.812852 -5.448676 -1.257809, -1.206467 -5.883669 -1.801237, -0.741169 -6.482183 -2.324724, -0.239776 -7.038072 -2.887120, 0.100473 -7.436812 -3.447225, 0.256184 -7.443763 -4.033586, 0.149506 -7.206019 -4.838401, -0.152114 -6.377877 -5.652634, -0.708606 -4.925940 -6.329010, -1.519338 -2.663972 -6.721354, -2.913324 0.466047 -6.728483, -4.473157 4.106512 -6.459960, -5.936733 7.529457 -5.898586, -6.797662 10.148153 -5.029838, -6.808119 11.832380 -3.843851, -6.025159 12.574698 -2.484786, -4.594378 12.767045 -0.945567, -2.637407 12.586160 0.456446, -0.494612 11.761012 1.707199, 1.651142 10.696146 2.703041, 3.563990 9.365761 3.189348, 5.143148 8.051891 3.223851, 6.138376 6.639955 2.806978, 6.604680 5.163795 2.265436, 6.513486 3.430048 1.750065, 5.901102 1.666885 1.253722, 5.095525 -0.111966 0.854268, 4.069852 -1.668368 0.464407, 2.910332 -3.006828 0.248049, 1.290655 -4.270497 0.028403, -0.690184 -5.405442 -0.005224, -2.902789 -6.382324 0.015564, -5.405581 -7.307895 0.044292, -8.253334 -8.174847 0.106334, -11.141315 -8.752104 0.227021, -13.891227 -9.068383 0.523654, -16.480547 -8.854589 0.684619, -18.937206 -8.411026 0.832167, -21.042263 -8.001430 1.030714, -22.646334 -7.656353 1.050493, -23.412756 -7.068203 1.150484, -23.619896 -6.158003 1.401605, -23.431641 -5.072293 1.580363, -23.019081 -3.920513 1.990800, -22.257782 -2.244141 2.786906, -21.267128 -0.346976 3.592521, -20.611868 1.314144 4.269357, -19.742203 2.609430 4.890854, -18.638042 3.378566 5.408951, -17.401072 3.810946 6.034092, -15.956229 3.967694 6.639023, -14.562157 4.026348 7.222071, -13.049326 4.025506 7.403621, -11.631183 4.086900 6.964666, -10.105343 4.038039 6.290307, -8.768139 4.044128 5.803460, -7.627457 3.880099 5.434517, -6.577711 3.759186 5.489887, -5.738364 3.645665 5.772319, -4.890085 3.428263 5.722960, -4.180766 3.251988 5.474356, -3.593595 2.971204 5.189721, -3.240815 2.733730 5.132963, -3.157389 2.598490 5.003756, -3.215949 2.499932 5.005891, -3.131891 2.289375 4.707678, -3.147826 2.124732 4.412086, -3.020215 1.844726 4.155404, -3.022264 1.546497 3.932713, -2.898591 1.267551 3.673257, -2.961832 0.848121 3.395640, -2.800933 0.318125 3.147584, -2.471157 -0.111235 2.992525, -2.184409 -0.707181 2.779421, -1.778916 -1.293042 2.533600, -1.395565 -2.011003 2.261255, -0.967401 -2.792706 1.948325, -0.767956 -3.600317 1.839066, -0.711969 -4.358867 1.668260, -0.661366 -5.098137 1.466050, -0.698915 -5.884237 1.261600, -0.889653 -6.692768 0.978101, -1.118983 -7.428358 0.637012, -1.277700 -8.207983 0.290958, -1.437689 -8.805524 -0.125139, -1.694507 -9.067228 -0.726956, -1.818096 -9.093368 -1.410890, -2.095885 -8.785511 -2.193850, -2.368146 -7.995113 -3.009614, -2.782512 -6.673240 -3.890692, -3.440862 -4.718197 -4.625148, -4.660296 -1.960986 -5.237294, -6.136866 1.390005 -5.721274, -7.726320 5.037798 -5.931162, -9.023488 8.331597 -5.711163, -9.628318 10.991716 -5.063140, -9.632290 12.803564 -3.975198, -8.730656 13.609695 -2.543628, -7.308375 13.668425 -0.981103, -5.584240 13.382105 0.504925, -4.025872 12.844546 1.746810, -2.672488 11.682527 2.741932, -1.436343 10.108156 3.157586, -0.373351 8.326473 3.155502, 0.563753 6.481862 2.839645, 1.374276 4.816467 2.490752, 1.776961 3.110854 2.386279, 1.697292 1.344978 2.461921, 0.991262 -0.205933 2.511175, -0.428352 -1.397347 2.476832, -2.320460 -2.429916 2.467374, -4.293278 -3.350758 2.355840, -6.208375 -3.854999 2.287564, -8.063935 -3.993778 2.229733, -9.796467 -3.681733 2.368032, -11.120317 -3.322241 2.329207, -12.517402 -2.978958 2.433282, -13.810494 -2.575547 2.497977, -15.018430 -1.873932 2.550983, -16.212374 -1.355580 2.588228, -17.092428 -1.097446 2.533878, -17.793930 -0.878919 2.308613, -18.191196 -0.572380 2.374650, -17.970158 0.163688 2.772251, -17.135996 1.177077 3.615283, -16.126371 1.980729 4.373848, -15.115627 2.713382 5.001661, -14.258899 3.283153 5.237583, -13.578729 3.640943 5.377181, -12.919566 3.875061 5.428818, -12.343954 3.904756 5.625055, -11.744227 4.137942 5.987854, -11.220801 4.232614 6.244277, -10.642786 4.351938 6.400125, -9.846327 4.484324 6.236682, -9.224895 4.625284 6.098688, -8.549911 4.639210 6.059036, -7.965559 4.725864 6.115324, -7.504282 4.793661 6.211139
#Interpolator5_l_midtarsal channels [15..17] sends animation values to BVH JOINT LeftAnkleEnd, DEF Bvh1_l_midtarsal, <HAnimJoint name=l_midtarsal/>
OrientationInterpolator376 = OrientationInterpolator()
OrientationInterpolator376.setDEF("Interpolator5_l_midtarsal")
OrientationInterpolator376.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator376.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0])

Group366.addChildren(OrientationInterpolator376)
#Unchanging Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.0,4.9E-324], [0.0,4.9E-324], [0.0,4.9E-324] degrees
#0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000
#Interpolator6_r_hip channels [18..20] sends animation values to BVH JOINT RightHip, DEF Bvh1_r_hip, <HAnimJoint name=r_hip/>
OrientationInterpolator377 = OrientationInterpolator()
OrientationInterpolator377.setDEF("Interpolator6_r_hip")
OrientationInterpolator377.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator377.setKeyValue([0.9812,-0.173,-0.086,0.1046,0.9834,-0.1611,-0.0838,0.1056,0.9851,-0.1494,-0.0849,0.1067,0.984,-0.1365,-0.1144,0.108,0.978,-0.1462,-0.1486,0.1074,0.9706,-0.1413,-0.1949,0.1032,0.9619,-0.1416,-0.234,0.1005,0.9563,-0.1442,-0.2544,0.0962,0.9504,-0.1384,-0.2784,0.0913,0.9466,-0.118,-0.2999,0.0875,0.9475,-0.0949,-0.3052,0.0837,0.9457,-0.0485,-0.3213,0.0802,0.931,-0.0364,-0.3632,0.0757,0.9055,-0.0475,-0.4216,0.0741,0.8886,-0.0854,-0.4507,0.0733,0.8764,-0.133,-0.4628,0.0736,0.8675,-0.1899,-0.4598,0.0727,0.845,-0.2498,-0.4729,0.0677,0.8025,-0.3795,-0.4605,0.0614,0.7014,-0.545,-0.4594,0.0537,0.5503,-0.7023,-0.4516,0.0489,0.3409,-0.8621,-0.3749,0.0439,-0.0269,-0.955,-0.2955,0.0453,-0.4341,-0.8887,-0.1477,0.06,-0.6692,-0.7418,-0.0431,0.0878,-0.751,-0.66,0.0181,0.1285,-0.7732,-0.6307,0.0658,0.1727,-0.7757,-0.6248,0.0894,0.2137,-0.7691,-0.6297,0.1096,0.254,-0.7635,-0.6316,0.1349,0.2898,-0.7618,-0.6278,0.1597,0.3225,-0.7674,-0.6134,0.1868,0.3528,-0.7789,-0.5916,0.2082,0.376,-0.7934,-0.5669,0.2218,0.3966,-0.8155,-0.5313,0.2296,0.4115,-0.8417,-0.4854,0.2364,0.4202,-0.8703,-0.429,0.2419,0.4268,-0.896,-0.3688,0.2474,0.4304,-0.9148,-0.3123,0.2561,0.4376,-0.9258,-0.2687,0.2657,0.443,-0.9318,-0.2422,0.2703,0.4476,-0.9349,-0.2333,0.2673,0.4542,-0.9352,-0.2371,0.2631,0.4617,-0.932,-0.2509,0.2615,0.4732,-0.9329,-0.2583,0.2509,0.486,-0.936,-0.2568,0.2405,0.4992,-0.9402,-0.2489,0.2326,0.5053,-0.9442,-0.2396,0.2258,0.5098,-0.949,-0.2297,0.216,0.5114,-0.9525,-0.2219,0.2085,0.5134,-0.9554,-0.2149,0.2025,0.5137,-0.958,-0.2121,0.1928,0.5151,-0.9598,-0.2099,0.1864,0.5188,-0.9611,-0.2106,0.1787,0.5227,-0.9625,-0.2105,0.1713,0.5258,-0.9624,-0.2136,0.168,0.5252,-0.9619,-0.2175,0.1658,0.5259,-0.961,-0.2226,0.1643,0.5213,-0.9595,-0.2299,0.1629,0.5154,-0.9572,-0.2377,0.1651,0.5073,-0.9553,-0.2445,0.1662,0.4967,-0.9532,-0.2498,0.1702,0.4852,-0.9539,-0.2429,0.1765,0.4731,-0.9558,-0.2337,0.1785,0.4598,-0.9571,-0.2207,0.1875,0.4436,-0.9586,-0.2083,0.1941,0.4305,-0.9593,-0.1933,0.2059,0.4184,-0.9561,-0.1828,0.2291,0.4076,-0.9504,-0.1698,0.2608,0.3951,-0.9433,-0.1544,0.2939,0.3825,-0.9352,-0.1401,0.3253,0.3679,-0.9294,-0.129,0.3457,0.3501,-0.926,-0.1184,0.3585,0.33,-0.925,-0.1049,0.3653,0.313,-0.9287,-0.0922,0.3592,0.2948,-0.9315,-0.0698,0.3569,0.2766,-0.9353,-0.0401,0.3515,0.2574,-0.9383,-0.0148,0.3456,0.2408,-0.9404,0.0058,0.3401,0.2263,-0.9411,0.0223,0.3374,0.214,-0.9444,0.0457,0.3257,0.2016,-0.9416,0.0607,0.3311,0.1907,-0.9451,0.0715,0.3187,0.1789,-0.9458,0.0913,0.3117,0.1669,-0.944,0.0992,0.3146,0.1531,-0.9474,0.1151,0.2987,0.1379,-0.9494,0.1283,0.2867,0.1216,-0.9588,0.1207,0.2571,0.1037,-0.9732,0.0832,0.2142,0.085,-0.9808,0.0117,0.1948,0.0651,-0.9846,-0.1185,0.1288,0.0485,-0.9216,-0.386,0.0411,0.0352,-0.6955,-0.6956,-0.1801,0.0286,-0.3358,-0.8563,-0.3924,0.0255,0.1497,-0.8016,-0.5788,0.0265,0.475,-0.6647,-0.5766,0.0321,0.7134,-0.4935,-0.4975,0.0391,0.8507,-0.3159,-0.4201,0.046,0.9179,-0.191,-0.3477,0.0568,0.9509,-0.0832,-0.2981,0.0681,0.9621,-0.0387,-0.2699,0.0819,0.971,-0.019,-0.2383,0.0956,0.9732,-0.0217,-0.229,0.1117,0.9813,-0.0174,-0.1916,0.1256,0.9838,-0.0227,-0.1777,0.1379,0.9845,-0.0193,-0.1744,0.1506,0.9859,-0.0215,-0.1661,0.1627,0.9887,-0.0122,-0.1492,0.1726,0.9892,-0.0206,-0.1452,0.1836,0.9875,-0.0412,-0.152,0.1952,0.9856,-0.0709,-0.1536,0.2056,0.9843,-0.0926,-0.15,0.2149,0.9809,-0.1236,-0.15,0.2219,0.9796,-0.1437,-0.1405,0.2265,0.9736,-0.1727,-0.1494,0.2298,0.966,-0.2001,-0.1636,0.2321,0.9578,-0.2279,-0.1752,0.2303,0.9388,-0.2725,-0.2107,0.2259,0.9135,-0.3231,-0.2471,0.2192,0.8687,-0.3997,-0.2925,0.2087,0.782,-0.5134,-0.3534,0.1995,0.6557,-0.654,-0.3773,0.1962,0.4995,-0.7798,-0.3774,0.1988,0.3211,-0.8799,-0.3502,0.2053,0.1386,-0.9458,-0.2937,0.2176,-0.0211,-0.974,-0.2255,0.2342,-0.1624,-0.9751,-0.151,0.2515,-0.286,-0.954,-0.0902,0.271,-0.3949,-0.9184,-0.025,0.29,-0.4901,-0.8708,0.0397,0.31,-0.5787,-0.8106,0.0891,0.329,-0.6516,-0.7474,0.1293,0.3461,-0.7138,-0.6796,0.1692,0.3626,-0.7664,-0.6107,0.199,0.375,-0.8076,-0.5457,0.2236,0.384,-0.8386,-0.4875,0.2432,0.3917,-0.8588,-0.4422,0.2588,0.397,-0.8728,-0.4054,0.2719,0.3972,-0.8856,-0.3709,0.2795,0.3946,-0.8948,-0.3423,0.2865,0.391,-0.9035,-0.3186,0.2866,0.3884,-0.912,-0.2981,0.2816,0.3871,-0.9185,-0.2798,0.2793,0.389,-0.9215,-0.2782,0.2711,0.3904,-0.9228,-0.2863,0.2577,0.3907,-0.9202,-0.3033,0.2474,0.3902,-0.9163,-0.3224,0.2376,0.391,-0.912,-0.3414,0.2274,0.3918,-0.9071,-0.3601,0.218,0.3916,-0.8994,-0.3799,0.2162,0.3922,-0.889,-0.405,0.2139,0.3928,-0.8763,-0.4283,0.2203,0.3922,-0.8619,-0.4527,0.2286,0.3935,-0.8507,-0.4674,0.2406,0.3923,-0.8475,-0.465,0.2558,0.3877,-0.8587,-0.4401,0.2628,0.378,-0.8751,-0.4024,0.269,0.3657,-0.887,-0.3703,0.2758,0.3516,-0.8859,-0.3603,0.2922,0.3337,-0.8743,-0.3697,0.3147,0.3144,-0.8582,-0.3846,0.34,0.2954,-0.8408,-0.4005,0.3642,0.2775,-0.8233,-0.4079,0.3946,0.2605,-0.8044,-0.4194,0.4208,0.2414,-0.795,-0.4016,0.4546,0.2252,-0.7937,-0.3698,0.4831,0.2056,-0.804,-0.3026,0.5118,0.1847,-0.8079,-0.2038,0.553,0.1636,-0.8,-0.0793,0.5947,0.1437,-0.7563,0.0486,0.6524,0.1261,-0.6787,0.1356,0.7218,0.1109,-0.5486,0.1553,0.8216,0.0938,-0.3617,0.1169,0.9249,0.0799,-0.0925,0.0421,0.9948,0.0719,0.1714,-0.0017,0.9852,0.0711,0.4147,-0.0166,0.9098,0.074,0.5992,0.0185,0.8004,0.0805,0.7343,0.0673,0.6755,0.0928,0.8123,0.0887,0.5764,0.1048,0.8581,0.1038,0.5029,0.1197,0.9005,0.0908,0.4253,0.1347,0.93,0.0625,0.3621,0.1527,0.9479,0.0254,0.3176,0.1735,0.9645,-0.0078,0.2641,0.1929,0.9726,-0.0179,0.2319,0.2121,0.9796,-0.0277,0.1988,0.2302,0.9829,-0.0455,0.1782,0.245,0.9857,-0.0595,0.1579,0.2585,0.9876,-0.0707,0.1405,0.2684,0.9895,-0.0744,0.1238,0.2772,0.9918,-0.0765,0.1019,0.2869,0.9937,-0.0804,0.0786,0.294,0.9945,-0.0912,0.0522,0.3018,0.9936,-0.1111,0.0229,0.3087,0.9907,-0.1356,-0.0111,0.3107,0.9851,-0.1656,-0.0458,0.3051,0.9752,-0.2008,-0.093,0.2915,0.9527,-0.2603,-0.1571,0.2699,0.9042,-0.359,-0.2313,0.2475,0.8144,-0.4941,-0.3044,0.2293,0.6681,-0.6528,-0.3571,0.2181,0.4807,-0.7943,-0.3715,0.2174,0.2855,-0.894,-0.3454,0.231,0.1142,-0.9501,-0.2904,0.2514,-0.0444,-0.9708,-0.2358,0.2767,-0.1847,-0.9661,-0.1805,0.2991,-0.3059,-0.9435,-0.1276,0.319,-0.4156,-0.9063,-0.0769,0.3372,-0.5063,-0.8619,-0.0292,0.356,-0.5848,-0.8112,0.0048,0.3722,-0.6502,-0.7589,0.0356,0.389,-0.6969,-0.7145,0.0617,0.4047,-0.7292,-0.6784,0.0902,0.4211,-0.7411,-0.6608,0.1189,0.4373,-0.7415,-0.6549,0.1463,0.4507,-0.7378,-0.6533,0.1701,0.4576,-0.7349,-0.6516,0.1879,0.4595,-0.7348,-0.6475,0.2021,0.456,-0.7434,-0.6361,0.2066,0.4439,-0.761,-0.6129,0.2125,0.4258,-0.7866,-0.5754,0.2239,0.4034,-0.814,-0.5307,0.2362,0.3793,-0.841,-0.4841,0.2418,0.3576,-0.8641,-0.4406,0.2432,0.3398,-0.8752,-0.4175,0.2442,0.3252,-0.8753,-0.4193,0.241,0.3169,-0.8675,-0.4334,0.2442,0.3142,-0.8577,-0.4453,0.257,0.3183,-0.8521,-0.4493,0.2684,0.3255,-0.8442,-0.4522,0.2878,0.3297,-0.8364,-0.4551,0.3056,0.3324,-0.8283,-0.4636,0.3146,0.3291,-0.8161,-0.475,0.3292,0.3228,-0.8059,-0.4805,0.3459,0.3134,-0.8029,-0.4763,0.3585,0.3026,-0.8113,-0.4519,0.371,0.2941,-0.8233,-0.4137,0.3886,0.283,-0.8366,-0.363,0.4102,0.2714,-0.8466,-0.3148,0.4292,0.2574,-0.8486,-0.269,0.4556,0.2419,-0.8358,-0.2572,0.4852,0.2237,-0.8151,-0.2743,0.5102,0.2067,-0.7843,-0.3296,0.5256,0.1948,-0.732,-0.395,0.5552,0.1843,-0.6647,-0.4704,0.5804,0.1741,-0.5911,-0.5378,0.6012,0.1687,-0.5281,-0.5822,0.6183,0.1649,-0.5007,-0.5696,0.6517,0.1563,-0.5225,-0.51,0.6833,0.1457,-0.5544,-0.4121,0.7231,0.1332,-0.5906,-0.2969,0.7504,0.1245,-0.6018,-0.1896,0.7758,0.1156,-0.5865,-0.1558,0.7948,0.108,-0.5069,-0.1846,0.842,0.1005,-0.4029,-0.2603,0.8775,0.0962,-0.2994,-0.3489,0.888,0.091,-0.1916,-0.4255,0.8844,0.0891,-0.1248,-0.4597,0.8792,0.0866,-0.0561,-0.4392,0.8966,0.0852,-0.0109,-0.3958,0.9183,0.0823,0.0468,-0.3289,0.9432,0.0803,0.1202,-0.2177,0.9686,0.0804,0.2446,-0.127,0.9613,0.0801,0.3852,-0.0505,0.9214,0.0828,0.5052,0.0208,0.8628,0.0874,0.5971,0.0574,0.8001,0.093,0.6573,0.0952,0.7476,0.101,0.7026,0.0909,0.7058,0.1063,0.7401,0.0919,0.6662,0.1115,0.7737,0.0867,0.6276,0.1185,0.7973,0.0673,0.5999,0.1233,0.8335,0.058,0.5495,0.1291,0.8637,0.0493,0.5016,0.1353,0.8881,0.0288,0.4588,0.1422,0.9121,0.0181,0.4095,0.1491,0.9317,0.0116,0.3629,0.1549,0.9458,-0.0254,0.3238,0.1613,0.9566,-0.0574,0.2856,0.1618,0.9627,-0.1099,0.2474,0.158,0.9547,-0.2001,0.2204,0.1539,0.9261,-0.3271,0.1879,0.1443,0.8636,-0.4785,0.1589,0.1336,0.7372,-0.6655,0.1168,0.1272,0.5449,-0.8355,0.0703,0.1258,0.2832,-0.9589,0.0193,0.1313,0.0422,-0.9991,-0.0029,0.1474])

Group366.addChildren(OrientationInterpolator377)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.157261,6.750121], [-29.20495,17.635117], [-17.819462,1.117753] degrees
#-0.463647 5.886320 -1.013938, -0.457973 5.955936 -0.952109, -0.472793 6.027548 -0.889615, -0.665969 6.096365 -0.810241, -0.870313 6.026208 -0.854687, -1.113930 5.745759 -0.780209, -1.311787 5.546465 -0.752326, -1.369681 5.281392 -0.732511, -1.429278 4.982326 -0.662568, -1.482513 4.752792 -0.530477, -1.449486 4.551945 -0.397918, -1.470868 4.347774 -0.167059, -1.571716 4.038394 -0.102584, -1.785921 3.847450 -0.141724, -1.883015 3.735377 -0.297418, -1.936328 3.705180 -0.498352, -1.892994 3.626591 -0.731540, -1.808667 3.292837 -0.917364, -1.588066 2.841102 -1.295890, -1.383252 2.179703 -1.652080, -1.239107 1.563532 -1.951524, -0.925871 0.874250 -2.159603, -0.768206 -0.053329 -2.478601, -0.547427 -1.477904 -3.061992, -0.326667 -3.357264 -3.742706, -0.101292 -5.526819 -4.866435, 0.234320 -7.669518 -6.232724, 0.461297 -9.543160 -7.630078, 0.701795 -11.269773 -9.123387, 1.083134 -12.808705 -10.407759, 1.534882 -14.278560 -11.470045, 2.117400 -15.795771 -12.185031, 2.654253 -17.134100 -12.441459, 3.066722 -18.434092 -12.499436, 3.388619 -19.657310 -12.067257, 3.733262 -20.693235 -11.137940, 4.111614 -21.689083 -9.835261, 4.536672 -22.466307 -8.315687, 5.097023 -23.281029 -6.895510, 5.639353 -23.814924 -5.735267, 5.962579 -24.189854 -5.032736, 6.007799 -24.616217 -4.861295, 5.955014 -25.033178 -5.055720, 5.950693 -25.594276 -5.570896, 5.717373 -26.311792 -5.989933, 5.531695 -27.105438 -6.157423, 5.393551 -27.537914 -6.029875, 5.285458 -27.884010 -5.832609, 5.059349 -28.082926 -5.605918, 4.894954 -28.279188 -5.433496, 4.760615 -28.366486 -5.258080, 4.479827 -28.507729 -5.256432, 4.312781 -28.751268 -5.270215, 4.076246 -28.998310 -5.393849, 3.851585 -29.204950 -5.480572, 3.711441 -29.167879 -5.606119, 3.610655 -29.193022 -5.761967, 3.498630 -28.911566 -5.892942, 3.369718 -28.541307 -6.079056, 3.349475 -28.031677 -6.214269, 3.290246 -27.394953 -6.292204, 3.331900 -26.712570 -6.284389, 3.508061 -26.058996 -5.890000, 3.552973 -25.368921 -5.460135, 3.783094 -24.505535 -4.876289, 3.936068 -23.810205 -4.383720, 4.221247 -23.154421 -3.834478, 4.748349 -22.484440 -3.382954, 5.428765 -21.664371 -2.853463, 6.089560 -20.813793 -2.305517, 6.605723 -19.838264 -1.829423, 6.750121 -18.754608 -1.497699, 6.643376 -17.600946 -1.229919, 6.459007 -16.660398 -0.950322, 6.002895 -15.738651 -0.738355, 5.639166 -14.793545 -0.379958, 5.212533 -13.800171 0.037337, 4.828225 -12.938966 0.342959, 4.485624 -12.178822 0.554227, 4.221767 -11.520246 0.700612, 3.859385 -10.884043 0.897993, 3.716600 -10.258261 0.998645, 3.360383 -9.660075 1.019226, 3.074944 -9.015380 1.117753, 2.841785 -8.254423 1.076442, 2.432330 -7.462487 1.069395, 2.057575 -6.595348 1.012978, 1.568497 -5.686317 0.795890, 1.062052 -4.733721 0.449166, 0.729567 -3.660034 0.066964, 0.350556 -2.739143 -0.321271, 0.070376 -1.860759 -0.778128, -0.306883 -1.138149 -1.144540, -0.579319 -0.484952 -1.255065, -0.876170 0.236495 -1.215063, -1.051389 0.885046 -1.214768, -1.098649 1.607574 -1.089470, -1.090433 2.247508 -0.810580, -1.116042 2.992103 -0.592501, -1.154498 3.714391 -0.287497, -1.262548 4.518425 -0.131846, -1.304290 5.318889 -0.043744, -1.464701 6.231959 -0.059220, -1.377744 7.060910 -0.040106, -1.400815 7.775869 -0.084577, -1.502751 8.493948 -0.054776, -1.544973 9.191073 -0.077002, -1.478779 9.775628 0.005775, -1.523585 10.404763 -0.078392, -1.676420 11.048604 -0.300093, -1.748250 11.621850 -0.659893, -1.752449 12.136559 -0.958755, -1.762879 12.496050 -1.384550, -1.642777 12.736542 -1.688950, -1.741087 12.855229 -2.087424, -1.906742 12.888752 -2.456828, -2.011202 12.690244 -2.796060, -2.385841 12.224241 -3.286139, -2.730122 11.568026 -3.795554, -3.094247 10.518070 -4.509542, -3.604671 9.124733 -5.595598, -3.779162 7.618917 -7.115694, -3.854045 5.994053 -8.691518, -3.761798 4.124072 -10.220773, -3.459478 2.090429 -11.733425, -3.031996 0.062712 -13.071626, -2.441271 -2.050382 -14.098674, -1.959504 -4.211298 -14.893917, -1.286351 -6.429687 -15.350651, -0.478198 -8.695275 -15.534271, 0.211168 -11.004461 -15.309449, 0.881029 -13.107648 -14.785451, 1.690489 -15.108415 -13.977064, 2.416154 -16.807724 -12.861652, 3.116418 -18.144270 -11.610748, 3.756861 -19.212727 -10.412024, 4.301610 -19.933638 -9.409688, 4.747635 -20.257902 -8.480508, 5.030520 -20.392735 -7.575719, 5.270149 -20.394142 -6.807278, 5.331741 -20.421822 -6.210309, 5.278721 -20.516788 -5.732181, 5.322324 -20.744593 -5.334225, 5.150934 -20.877686 -5.348425, 4.804814 -20.917683 -5.597732, 4.487149 -20.833452 -6.033696, 4.186182 -20.793715 -6.538296, 3.877923 -20.742929 -7.041483, 3.581530 -20.618643 -7.518840, 3.468884 -20.488411 -8.005243, 3.327722 -20.296400 -8.617578, 3.399545 -20.007603 -9.128187, 3.522944 -19.775534 -9.696836, 3.757460 -19.497318 -9.966290, 4.097724 -19.225155 -9.738769, 4.263249 -18.969984 -8.910983, 4.412739 -18.665823 -7.784949, 4.520356 -18.166620 -6.803941, 4.689763 -17.215788 -6.234726, 4.863308 -16.027906 -6.022487, 5.024212 -14.800842 -5.896482, 5.129777 -13.647424 -5.788636, 5.308755 -12.560731 -5.532104, 5.314611 -11.384269 -5.292693, 5.453815 -10.494841 -4.698837, 5.378489 -9.542732 -3.919442, 5.213875 -8.641736 -2.815875, 5.087012 -7.648619 -1.574076, 4.879580 -6.605193 -0.371917, 4.746145 -5.445519 0.577225, 4.626693 -4.273258 1.035020, 4.441142 -2.913353 0.948103, 4.241659 -1.634031 0.595797, 4.100333 -0.374560 0.186840, 4.011729 0.697272 -0.031530, 3.860321 1.754820 -0.129542, 3.691031 2.763736 -0.003784, 3.584299 3.912417 0.235801, 3.445764 4.889366 0.385799, 3.424094 5.902555 0.535967, 3.255823 6.966758 0.503870, 3.150817 8.148797 0.323724, 3.165222 9.425735 -0.007766, 2.960749 10.652176 -0.362968, 2.881762 11.807482 -0.516929, 2.709460 12.906066 -0.673665, 2.630348 13.781452 -0.960311, 2.506705 14.577859 -1.207686, 2.360642 15.159471 -1.407366, 2.183453 15.691246 -1.489409, 1.906119 16.279266 -1.539339, 1.568499 16.718784 -1.594183, 1.175865 17.178127 -1.766173, 0.731185 17.562960 -2.092832, 0.182876 17.635117 -2.462072, -0.372652 17.236496 -2.861568, -1.101940 16.325605 -3.219931, -1.950349 14.802380 -3.794124, -2.750351 12.946177 -4.801467, -3.424177 10.895785 -6.184981, -3.881728 8.630133 -7.881871, -4.105083 6.352144 -9.682067, -4.157261 4.218960 -11.689063, -3.948370 2.124501 -13.617095, -3.787050 -0.196837 -15.401984, -3.507659 -2.675207 -16.646437, -3.140734 -5.155109 -17.400879, -2.699046 -7.676798 -17.721062, -2.185551 -10.070715 -17.819462, -1.802923 -12.293236 -17.560360, -1.382921 -14.395090 -17.179588, -0.950256 -16.137039 -16.813040, -0.382363 -17.661182 -16.556826, 0.258302 -18.739738 -16.663462, 0.926987 -19.421955 -16.915390, 1.555242 -19.717329 -17.030552, 2.050861 -19.791441 -16.970638, 2.458752 -19.691887 -16.663542, 2.606148 -19.392775 -15.894265, 2.797546 -19.025570 -14.627461, 3.117550 -18.608395 -12.908180, 3.423256 -18.080263 -11.089259, 3.540972 -17.561430 -9.451152, 3.557288 -17.106382 -8.109180, 3.522011 -16.558163 -7.324380, 3.390974 -16.127211 -7.185462, 3.401210 -15.860987 -7.381222, 3.651670 -15.910362 -7.665988, 3.924821 -16.191498 -7.881756, 4.339554 -16.281445 -7.982944, 4.714711 -16.293037 -8.055700, 4.836370 -15.991734 -8.124286, 5.024116 -15.484343 -8.160383, 5.210375 -14.864449 -8.002171, 5.296193 -14.300697 -7.641986, 5.429678 -14.027777 -6.990834, 5.609048 -13.670386 -6.073062, 5.829651 -13.282688 -4.996759, 5.912680 -12.708654 -4.007614, 6.013404 -11.939031 -3.116405, 5.976576 -10.863632 -2.739347, 5.820282 -9.801188 -2.759179, 5.624299 -8.920067 -3.249668, 5.609976 -7.921388 -3.790775, 5.537173 -6.848904 -4.369917, 5.564547 -5.961347 -4.918029, 5.607047 -5.252285 -5.249875, 5.640219 -4.729235 -4.873546, 5.548913 -4.562819 -4.041572, 5.410915 -4.374331 -2.942324, 5.284744 -4.306036 -1.921776, 5.102231 -4.036222 -1.076814, 4.894138 -3.666281 -0.807980, 4.826862 -2.960758 -0.939140, 4.808983 -2.277413 -1.339410, 4.603314 -1.631924 -1.753800, 4.496749 -1.062432 -2.132121, 4.347103 -0.704714 -2.254283, 4.370907 -0.355380 -2.131359, 4.326640 -0.121804 -1.862022, 4.339124 0.157666 -1.519199, 4.464204 0.513727 -1.022893, 4.420378 1.099448 -0.626069, 4.376482 1.816472 -0.309278, 4.322760 2.532227 0.008877, 4.257355 3.188894 0.187650, 4.316024 3.822310 0.407717, 4.287640 4.297883 0.393731, 4.240575 4.744157 0.411672, 4.245694 5.269475 0.393869, 4.229390 5.646245 0.267282, 4.057909 6.175666 0.210660, 3.884034 6.704000 0.155517, 3.742094 7.236833 -0.001850, 3.509140 7.791162 -0.083761, 3.236142 8.268278 -0.130473, 3.033978 8.731081 -0.466509, 2.711394 8.855350 -0.742982, 2.333648 8.694297 -1.174541, 2.088072 8.384262 -1.920870, 1.744212 7.616653 -2.824636, 1.433588 6.568992 -3.750380, 1.080521 5.328060 -4.902299, 0.713508 3.894096 -6.049717, 0.278969 2.115276 -7.218181, 0.001921 0.356889 -8.438903
#Interpolator7_r_knee channels [21..23] sends animation values to BVH JOINT RightKnee, DEF Bvh1_r_knee, <HAnimJoint name=r_knee/>
OrientationInterpolator378 = OrientationInterpolator()
OrientationInterpolator378.setDEF("Interpolator7_r_knee")
OrientationInterpolator378.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator378.setKeyValue([-0.0545,0.8753,0.4804,0.0725,-0.0529,0.8762,0.479,0.0718,-0.0531,0.8729,0.485,0.0705,-0.0702,0.8478,0.5256,0.0714,-0.0876,0.8233,0.5607,0.0746,-0.082,0.8098,0.581,0.0771,-0.0593,0.8017,0.5947,0.0796,-0.0367,0.801,0.5976,0.0824,-0.0016,0.799,0.6013,0.0831,0.0183,0.7925,0.6096,0.0828,0.0401,0.7824,0.6214,0.0812,0.0825,0.7405,0.667,0.0779,0.143,0.7013,0.6983,0.078,0.1968,0.6785,0.7077,0.0795,0.2577,0.6504,0.7146,0.0794,0.3493,0.6352,0.6889,0.0781,0.4735,0.6056,0.6396,0.0773,0.6408,0.5349,0.5506,0.0787,0.7888,0.4595,0.4082,0.0867,0.8833,0.3959,0.2511,0.1018,0.9413,0.3158,0.1196,0.1214,0.9732,0.2298,-0.0004,0.149,0.9795,0.181,-0.0885,0.1874,0.9739,0.1726,-0.1474,0.237,0.964,0.1875,-0.1887,0.2959,0.9524,0.2131,-0.2178,0.3582,0.9373,0.2502,-0.2425,0.4185,0.9245,0.2818,-0.2567,0.4725,0.9111,0.3154,-0.2652,0.5174,0.8976,0.3444,-0.2752,0.5507,0.886,0.3641,-0.2872,0.5706,0.8798,0.3713,-0.2968,0.5791,0.8771,0.3701,-0.3062,0.576,0.8787,0.3657,-0.3069,0.5614,0.8859,0.3499,-0.3045,0.5379,0.8982,0.323,-0.2983,0.5074,0.9136,0.2826,-0.2924,0.474,0.9289,0.2344,-0.2866,0.4377,0.94,0.1854,-0.2863,0.4048,0.9455,0.146,-0.2909,0.3701,0.9464,0.1287,-0.2963,0.3384,0.9433,0.1308,-0.305,0.3088,0.936,0.1581,-0.3144,0.285,0.9254,0.2062,-0.3181,0.2701,0.9184,0.2419,-0.313,0.2611,0.9124,0.2703,-0.3073,0.2563,0.9095,0.2827,-0.3048,0.2486,0.9068,0.2903,-0.3055,0.2407,0.9063,0.2908,-0.3068,0.2317,0.9089,0.2821,-0.307,0.2229,0.915,0.2549,-0.3128,0.2155,0.9222,0.2242,-0.3151,0.2103,0.9273,0.186,-0.3247,0.2081,0.9391,0.1441,-0.3121,0.2122,0.9437,0.1164,-0.3095,0.218,0.9441,0.097,-0.3149,0.2241,0.9446,0.0855,-0.317,0.2311,0.9435,0.0936,-0.3178,0.2369,0.9409,0.1038,-0.3224,0.2395,0.9398,0.112,-0.3228,0.2423,0.9382,0.1124,-0.3275,0.2415,0.9365,0.1218,-0.3287,0.2424,0.9349,0.1153,-0.3357,0.2398,0.9367,0.0923,-0.3378,0.2354,0.9368,0.0578,-0.345,0.2264,0.9372,0.0108,-0.3485,0.2164,0.9362,-0.0252,-0.3507,0.2123,0.93,-0.0231,-0.3668,0.2093,0.921,0,-0.3895,0.2089,0.9117,0.0429,-0.4087,0.21,0.904,0.0898,-0.4181,0.2106,0.903,0.13,-0.4095,0.2072,0.9025,0.156,-0.4015,0.2004,0.911,0.159,-0.3806,0.1958,0.9331,0.135,-0.3333,0.1883,0.9522,0.1002,-0.2884,0.1797,0.9671,0.0717,-0.2442,0.1719,0.9803,0.0444,-0.1926,0.1645,0.9895,0.0232,-0.1427,0.1579,0.9938,0.0144,-0.1104,0.1522,0.9974,-0.0038,-0.0715,0.1449,0.998,-0.0305,-0.055,0.141,0.9976,-0.066,-0.0204,0.1372,0.9923,-0.1228,0.0141,0.1342,0.9844,-0.17,0.0449,0.128,0.973,-0.2129,0.0897,0.1211,0.958,-0.2594,0.1224,0.1124,0.9333,-0.304,0.1911,0.1012,0.8904,-0.3614,0.2768,0.0905,0.8312,-0.4154,0.3695,0.0805,0.7511,-0.4558,0.4775,0.0726,0.6506,-0.4745,0.593,0.0667,0.5684,-0.4788,0.6691,0.0657,0.4448,-0.4834,0.754,0.0672,0.3486,-0.4894,0.7994,0.0695,0.3169,-0.42,0.8504,0.0721,0.274,-0.3604,0.8916,0.0698,0.256,-0.2977,0.9197,0.0699,0.2575,-0.2592,0.9309,0.0693,0.2699,-0.227,0.9358,0.07,0.2736,-0.1866,0.9436,0.0717,0.3025,-0.1129,0.9464,0.0707,0.3107,-0.0078,0.9505,0.0719,0.3595,0.0899,0.9288,0.072,0.4123,0.2017,0.8884,0.0731,0.4508,0.2887,0.8447,0.076,0.5202,0.3423,0.7825,0.0785,0.6055,0.3449,0.7172,0.0802,0.6898,0.3796,0.6166,0.0851,0.7384,0.4256,0.5231,0.0942,0.7792,0.4799,0.4033,0.1038,0.8159,0.5043,0.2829,0.116,0.8536,0.4938,0.166,0.1325,0.8905,0.4523,0.0486,0.1514,0.9106,0.4106,-0.0464,0.1751,0.9273,0.3567,-0.1135,0.2032,0.9365,0.3071,-0.1691,0.2409,0.9435,0.2725,-0.1885,0.2862,0.9461,0.252,-0.2035,0.3393,0.946,0.2445,-0.2128,0.402,0.9417,0.2533,-0.2213,0.4714,0.9331,0.2708,-0.2366,0.5456,0.9231,0.2905,-0.252,0.6186,0.916,0.3015,-0.2648,0.6881,0.9093,0.3074,-0.2806,0.7527,0.9041,0.3095,-0.2946,0.8081,0.9001,0.3066,-0.3095,0.8557,0.8964,0.304,-0.3226,0.8934,0.893,0.3009,-0.3347,0.9199,0.8891,0.2983,-0.3471,0.9343,0.8868,0.2961,-0.3548,0.9361,0.8847,0.2951,-0.3609,0.9243,0.8828,0.2942,-0.3662,0.9016,0.8816,0.2961,-0.3677,0.8668,0.88,0.3023,-0.3664,0.8216,0.8777,0.3132,-0.3627,0.7688,0.8733,0.3317,-0.3567,0.7104,0.867,0.351,-0.3537,0.6445,0.8612,0.3686,-0.35,0.576,0.8579,0.3765,-0.3497,0.5032,0.8571,0.3771,-0.351,0.4326,0.8621,0.3569,-0.3597,0.3643,0.8759,0.3018,-0.3764,0.3017,0.8885,0.2123,-0.4068,0.2449,0.8996,0.0901,-0.4272,0.1975,0.8891,-0.0644,-0.4531,0.1584,0.8593,-0.2097,-0.4665,0.1288,0.8391,-0.3314,-0.4313,0.1234,0.8346,-0.3951,-0.3838,0.1215,0.8412,-0.4064,-0.3568,0.1261,0.86,-0.3729,-0.3485,0.1343,0.8763,-0.3189,-0.3612,0.1431,0.8905,-0.2652,-0.3696,0.155,0.9009,-0.2175,-0.3757,0.1715,0.9071,-0.1887,-0.3762,0.1925,0.9212,-0.178,-0.346,0.2168,0.9359,-0.1762,-0.305,0.241,0.9538,-0.1538,-0.2582,0.2597,0.9698,-0.1001,-0.2226,0.2666,0.9813,-0.0315,-0.1897,0.2688,0.9857,0.0146,-0.1681,0.2687,0.9869,0.0419,-0.1556,0.2685,0.9881,0.0527,-0.1446,0.269,0.9901,0.0493,-0.1314,0.2693,0.9926,0.0458,-0.1123,0.2692,0.995,0.0383,-0.0921,0.2676,0.9977,0.0265,-0.0631,0.2627,0.9992,-0.005,-0.0386,0.2561,0.9992,-0.0377,-0.0126,0.2498,0.9978,-0.0653,0.0082,0.2394,0.9968,-0.0768,0.0244,0.2288,0.9966,-0.0664,0.0478,0.214,0.9969,-0.0303,0.0729,0.2006,0.9962,0.0124,0.0862,0.1891,0.9942,0.0354,0.1018,0.1823,0.9904,0.0517,0.1284,0.1772,0.9875,0.0615,0.1452,0.1737,0.9836,0.0771,0.1633,0.1706,0.9786,0.0984,0.1809,0.1689,0.9765,0.1078,0.1867,0.1683,0.9689,0.1394,0.2047,0.1678,0.9613,0.1805,0.2081,0.165,0.9541,0.2214,0.2018,0.1669,0.9445,0.2615,0.1989,0.169,0.9435,0.277,0.1818,0.1704,0.9386,0.2989,0.1723,0.1742,0.9356,0.3168,0.1559,0.1832,0.938,0.3239,0.1235,0.1944,0.9385,0.3328,0.0919,0.2094,0.9453,0.3201,0.0634,0.2254,0.9515,0.305,0.0404,0.2436,0.9556,0.2947,0.0076,0.2642,0.9555,0.2929,-0.034,0.2893,0.9534,0.2911,-0.0797,0.3178,0.9521,0.2816,-0.1192,0.3539,0.9547,0.2524,-0.1575,0.3975,0.9595,0.2148,-0.1823,0.4519,0.9625,0.1792,-0.2034,0.519,0.9598,0.1588,-0.2312,0.5952,0.9521,0.1582,-0.2617,0.6777,0.9408,0.1799,-0.2873,0.7615,0.9288,0.2089,-0.3061,0.8424,0.9175,0.2347,-0.3212,0.9174,0.9082,0.2528,-0.3337,0.9839,0.9015,0.2638,-0.343,1.0425,0.8989,0.2675,-0.347,1.0934,0.8994,0.2683,-0.3452,1.1308,0.9017,0.2639,-0.3424,1.1553,0.9054,0.2589,-0.3364,1.1672,0.9101,0.2523,-0.3286,1.1675,0.9147,0.2477,-0.3194,1.1562,0.9183,0.2445,-0.3113,1.1329,0.9202,0.2459,-0.3046,1.0943,0.9189,0.2541,-0.3017,1.0459,0.9146,0.2684,-0.3024,0.9873,0.9094,0.2857,-0.3022,0.9195,0.9041,0.3057,-0.2985,0.8435,0.9003,0.3201,-0.2949,0.7639,0.9005,0.3276,-0.2859,0.6758,0.9043,0.3225,-0.2795,0.5839,0.9158,0.2935,-0.2743,0.4872,0.9338,0.2273,-0.2763,0.3911,0.9562,0.0978,-0.2757,0.3015,0.9527,-0.1376,-0.271,0.2274,0.8464,-0.4721,-0.2465,0.1816,0.6412,-0.7449,-0.1844,0.1675,0.4687,-0.8707,-0.1491,0.1667,0.4024,-0.9017,-0.1581,0.1641,0.438,-0.876,-0.2021,0.1545,0.5183,-0.812,-0.2685,0.1414,0.6162,-0.7078,-0.3453,0.1295,0.6746,-0.633,-0.3797,0.1245,0.7001,-0.6052,-0.3789,0.1274,0.6953,-0.6207,-0.3625,0.138,0.6847,-0.6422,-0.3445,0.1523,0.7044,-0.6364,-0.3143,0.171,0.7312,-0.6131,-0.2991,0.1895,0.7581,-0.5893,-0.2793,0.2041,0.7891,-0.5653,-0.2403,0.2162,0.8146,-0.5426,-0.2049,0.2215,0.8396,-0.5164,-0.1685,0.2181,0.8655,-0.4846,-0.1267,0.2101,0.8925,-0.4431,-0.0845,0.2001,0.9134,-0.4035,-0.0542,0.1915,0.9314,-0.3624,-0.0349,0.1826,0.9485,-0.3162,-0.0211,0.1789,0.9581,-0.2864,-0.0072,0.1785,0.9589,-0.2838,0.0039,0.1837,0.9521,-0.3058,0.0095,0.1914,0.9381,-0.3459,0.0185,0.1971,0.9228,-0.3846,0.0224,0.2022,0.902,-0.4302,0.0375,0.2053,0.8901,-0.4532,0.049,0.2062,0.8831,-0.4658,0.0556,0.2017,0.8837,-0.4655,0.049,0.1956,0.8829,-0.4675,0.0445,0.1868,0.8913,-0.4516,0.0402,0.1798,0.9069,-0.4205,0.0248,0.1779,0.9208,-0.3899,0.0128,0.1767,0.9359,-0.3523,0.0056,0.1789,0.949,-0.3152,-0.0018,0.1813,0.9583,-0.2856,-0.0088,0.1855,0.9685,-0.249,-0.0016,0.1886,0.9773,-0.2117,-0.0029,0.1894,0.9852,-0.1715,0.0023,0.1905,0.9916,-0.129,-0.0052,0.192,0.9958,-0.0896,-0.0207,0.1919,0.9985,-0.0437,-0.034,0.1951,0.9989,-0.0048,-0.0462,0.1975,0.9975,0.0402,-0.0575,0.1953,0.9947,0.0746,-0.0712,0.196,0.992,0.092,-0.0859,0.195,0.9889,0.1093,-0.1008,0.1941,0.9833,0.1337,-0.1231,0.1931,0.9806,0.1323,-0.1444,0.1943,0.9769,0.1272,-0.1716,0.1986,0.9715,0.1233,-0.2025,0.2076,0.9674,0.115,-0.2256,0.221,0.9615,0.1172,-0.2485,0.2411,0.9544,0.1305,-0.2685,0.2677,0.9481,0.1496,-0.2807,0.3021,0.9405,0.1651,-0.2969,0.345,0.9359,0.1778,-0.304,0.3924,0.9322,0.1871,-0.3098,0.4447,0.9289,0.1959,-0.3144,0.5034,0.9245,0.2018,-0.3233,0.5619])

Group366.addChildren(OrientationInterpolator378)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-46.181885,3.916524], [-0.300555,52.181007], [-8.439433,42.513977] degrees
#2.001732 -0.162876 3.639678, 1.974982 -0.155333 3.605519, 1.963410 -0.153872 3.527220, 2.156318 -0.221908 3.470656, 2.407975 -0.300555 3.527844, 2.574924 -0.281542 3.582581, 2.719984 -0.183522 3.662675, 2.825301 -0.080024 3.784698, 2.859258 0.087116 3.800880, 2.888186 0.181490 3.757687, 2.884585 0.278321 3.635533, 2.966480 0.454083 3.295805, 3.100296 0.723090 3.113770, 3.197531 0.982386 3.063685, 3.219869 1.255035 2.924692, 3.042033 1.637554 2.798402, 2.782180 2.160292 2.629052, 2.423636 2.940365 2.350888, 1.952588 3.957536 2.216810, 1.363797 5.177670 2.248248, 0.709036 6.560304 2.158115, -0.147177 8.306978 1.975717, -1.141260 10.495391 2.053399, -2.312393 13.173897 2.620381, -3.755092 16.235859 3.737742, -5.427441 19.328680 5.344125, -7.364349 22.065035 7.519727, -9.183669 24.383806 9.752104, -10.832458 26.083900 12.059031, -12.305082 27.107157 14.091288, -13.444748 27.513578 15.496689, -14.087172 27.611904 16.102276, -14.284027 27.350363 16.004265, -13.783643 26.779451 15.333961, -12.847063 26.030251 13.999450, -11.560117 25.105005 12.156238, -10.216016 24.071886 9.994284, -8.861128 22.791538 7.758323, -7.833241 21.461786 5.844345, -6.995211 19.823187 4.354496, -6.361458 18.178997 3.537765, -5.900111 16.546497 3.190256, -5.609516 15.136958 3.343760, -5.433230 14.156156 3.884638, -5.214726 13.565488 4.260231, -5.065650 13.212629 4.577106, -4.875842 12.773151 4.590578, -4.722577 12.335842 4.532638, -4.541140 11.871283 4.349079, -4.342463 11.465203 4.052843, -4.226254 11.176047 3.573049, -4.109262 11.010650 3.108115, -4.137017 10.970811 2.622897, -4.021383 11.346258 2.157773, -4.071828 11.724965 1.877884, -4.238874 12.067057 1.699150, -4.391355 12.452980 1.616738, -4.529897 12.742439 1.782779, -4.663151 12.840938 1.955540, -4.739670 12.967589 2.101578, -4.788178 12.901465 2.104247, -4.840108 12.921306 2.248766, -4.871541 12.765905 2.137377, -4.771135 12.569151 1.776082, -4.624113 12.111097 1.243305, -4.395478 11.605447 0.581202, -4.291938 11.388247 0.120887, -4.428962 11.153741 0.154855, -4.720733 11.011622 0.454882, -5.028743 10.934873 0.999584, -5.210986 10.845778 1.582379, -5.063566 10.637801 2.019915, -4.823518 10.274761 2.230628, -4.476573 10.143163 2.187402, -3.762183 10.013012 1.790621, -3.088616 9.773967 1.298253, -2.486484 9.504086 0.914024, -1.865461 9.231792 0.569619, -1.318339 8.949812 0.313394, -0.979632 8.664416 0.199851, -0.595666 8.281788 0.011285, -0.429651 8.064204 -0.216372, -0.125844 7.844276 -0.511486, 0.172016 7.626734 -0.956572, 0.410056 7.215672 -1.274670, 0.712747 6.742887 -1.521036, 0.881426 6.155397 -1.719298, 1.194639 5.392572 -1.820056, 1.514584 4.593886 -1.936393, 1.770030 3.802256 -1.974764, 2.039700 3.090366 -1.951738, 2.306379 2.449230 -1.863045, 2.552228 2.098439 -1.849017, 2.928946 1.663244 -1.903092, 3.205907 1.332726 -1.986195, 3.530823 1.254429 -1.773233, 3.581253 1.050651 -1.475416, 3.692049 0.985614 -1.223700, 3.703293 0.987747 -1.060776, 3.761990 1.051775 -0.945427, 3.886820 1.098065 -0.804597, 3.837694 1.208559 -0.497884, 3.916524 1.277627 -0.075999, 3.827524 1.494297 0.320931, 3.708334 1.752540 0.787973, 3.657741 2.001651 1.193619, 3.488535 2.384713 1.467024, 3.261390 2.828017 1.505921, 2.956108 3.411001 1.764432, 2.748426 4.041200 2.202509, 2.287110 4.690989 2.762583, 1.725519 5.473937 3.271918, 1.051802 6.518163 3.693568, 0.157653 7.734126 3.919037, -0.801515 9.112915 4.192769, -1.732773 10.738519 4.328813, -2.859763 12.820394 4.577426, -3.784103 15.321237 5.005706, -4.910165 18.177420 5.728527, -6.274833 21.467522 6.895541, -8.019513 24.934141 8.738546, -10.438185 28.353037 11.308995, -13.268949 31.448097 14.358880, -16.241367 34.301811 17.373274, -19.488073 36.748940 20.380249, -22.573000 38.717522 23.101353, -25.530777 40.309803 25.426582, -28.100498 41.444080 27.388176, -30.117334 42.125404 28.788298, -31.523581 42.299782 29.575430, -31.981863 42.171753 29.635563, -31.598112 41.594021 28.991955, -30.569090 40.655361 27.774494, -28.768600 39.316132 26.071680, -26.439220 37.516926 24.126627, -23.821323 35.332893 22.126793, -21.092897 32.745098 20.290514, -18.360378 29.735144 18.279501, -15.699046 26.631901 16.202709, -13.144069 23.414566 13.789204, -10.873873 20.311642 11.428522, -8.943020 17.383356 8.892623, -7.355667 14.783790 6.208544, -6.126102 12.291492 3.653885, -4.978260 10.125965 1.464131, -4.098389 8.082958 -0.295917, -3.369165 6.381420 -1.361425, -2.938743 5.992514 -2.192422, -2.539734 5.869695 -2.622740, -2.430053 6.139540 -2.809393, -2.526030 6.679293 -2.725214, -2.811104 7.246716 -2.440792, -3.138203 7.967907 -2.140275, -3.554841 8.914914 -1.864912, -4.007148 10.068663 -1.733689, -4.130911 11.514149 -1.802776, -4.003350 12.999018 -1.988013, -3.631406 14.257830 -1.846859, -3.274170 14.849031 -1.111226, -2.926384 15.120211 -0.099571, -2.680452 15.162329 0.583471, -2.539057 15.163374 0.985910, -2.394097 15.206486 1.136488, -2.180790 15.259028 1.056802, -1.872298 15.294940 0.962587, -1.527063 15.245147 0.795224, -1.025722 15.013369 0.536808, -0.569391 14.661027 0.000102, -0.115072 14.300466 -0.527326, 0.224691 13.685206 -0.927246, 0.442070 13.060209 -1.061357, 0.683586 12.215458 -0.890073, 0.885394 11.456342 -0.438846, 0.932354 10.791257 0.046647, 1.040845 10.386720 0.276284, 1.270650 10.061666 0.414335, 1.406082 9.835327 0.492636, 1.547264 9.620447 0.624740, 1.687050 9.481987 0.814276, 1.731036 9.433089 0.899568, 1.875499 9.338115 1.190558, 1.847519 9.115906 1.562926, 1.775944 9.155837 1.980120, 1.738134 9.185627 2.398256, 1.570036 9.248766 2.582848, 1.487954 9.405267 2.867562, 1.363377 9.859189 3.214803, 1.056762 10.480704 3.520538, 0.717987 11.291559 3.935695, 0.382407 12.224399 4.107880, 0.068922 13.286814 4.268035, -0.460080 14.452376 4.542985, -1.270127 15.793427 5.061834, -2.327500 17.259752 5.694455, -3.516834 19.142199 6.359796, -4.917336 21.499426 6.753368, -6.328342 24.523106 7.030566, -8.064460 28.205963 7.477740, -10.604738 32.128986 8.639803, -14.118433 36.001942 10.989956, -18.484821 39.411350 14.908314, -23.323460 42.200218 19.801580, -28.336290 44.340679 24.968285, -33.148495 45.934048 29.804996, -37.560745 47.203293 34.130848, -41.336960 48.439526 37.757168, -43.977448 49.509918 40.417171, -45.637043 50.454739 41.944248, -46.181885 51.239594 42.513977, -45.702866 51.880955 42.097313, -44.222252 52.181007 40.865089, -41.891033 51.981968 38.814335, -38.658604 50.999298 36.037281, -35.297382 49.199417 33.240112, -31.866846 46.623466 30.461588, -28.225664 43.571461 27.579420, -24.387226 40.148876 24.649954, -20.729425 36.624245 21.580458, -16.865290 32.868908 18.140509, -13.371744 28.919968 14.536125, -10.129426 24.792709 10.576402, -7.446207 20.560509 6.508485, -5.149621 16.423386 2.445040, -3.388072 12.458154 -1.430448, -2.201015 8.902619 -4.750215, -1.386421 6.247604 -7.080207, -1.097278 4.564311 -8.277807, -1.203241 3.878125 -8.439433, -1.524437 3.986209 -7.705368, -1.932659 4.313298 -6.508325, -2.353320 4.680636 -5.158072, -2.522150 4.911699 -4.410331, -2.573926 5.211461 -4.305818, -2.634416 5.609536 -4.781474, -2.720031 6.111180 -5.466411, -2.711425 7.052791 -6.076879, -2.796978 8.106204 -6.471006, -2.747562 9.036945 -6.690616, -2.395322 9.928328 -6.812799, -1.994368 10.468567 -6.723036, -1.526165 10.587839 -6.330739, -1.002279 10.477650 -5.757119, -0.518567 10.262691 -5.048285, -0.208833 10.033872 -4.419474, -0.041884 9.748567 -3.797436, 0.059617 9.722675 -3.253833, 0.179499 9.797924 -2.951916, 0.307931 10.088033 -3.022049, 0.415573 10.434112 -3.401065, 0.577896 10.580239 -3.971809, 0.683402 10.668882 -4.532686, 0.919943 10.575810 -5.159387, 1.081762 10.470474 -5.467131, 1.133850 10.160913 -5.499030, 1.009883 9.865846 -5.318605, 0.896696 9.414899 -5.088644, 0.793863 9.154288 -4.725331, 0.604199 9.226269 -4.344578, 0.455389 9.312288 -3.993660, 0.363349 9.584834 -3.650240, 0.266303 9.855857 -3.306264, 0.179131 10.180693 -3.058557, 0.231367 10.460989 -2.718511, 0.184382 10.604227 -2.320899, 0.203327 10.751811 -1.896314, 0.078993 10.906775 -1.430359, -0.135063 10.949221 -0.975157, -0.337028 11.162957 -0.457326, -0.524769 11.305873 -0.002015, -0.696708 11.160870 0.519612, -0.892883 11.165123 0.928230, -1.072793 11.075237 1.135248, -1.253799 10.983347 1.339870, -1.521119 10.859595 1.628786, -1.768602 10.890636 1.645828, -2.119739 11.086560 1.657222, -2.591458 11.519073 1.732975, -3.057875 12.203814 1.788592, -3.687214 13.222310 2.054907, -4.470952 14.550350 2.585019, -5.376544 16.271599 3.378662, -6.627742 18.370691 4.367634, -7.920386 20.717602 5.498173, -9.414497 23.290794 6.790174, -11.190895 26.133850 8.374302, -13.263932 28.851444 10.092083
#Interpolator8_r_ankle channels [24..26] sends animation values to BVH JOINT RightAnkle, DEF Bvh1_r_ankle, <HAnimJoint name=r_ankle/>
OrientationInterpolator379 = OrientationInterpolator()
OrientationInterpolator379.setDEF("Interpolator8_r_ankle")
OrientationInterpolator379.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator379.setKeyValue([-0.6616,-0.3368,-0.67,0.0341,-0.6845,-0.3416,-0.6441,0.035,-0.6699,-0.3227,-0.6686,0.0381,-0.6699,-0.3227,-0.6686,0.0381,-0.6198,-0.3303,-0.7119,0.0368,-0.5627,-0.3833,-0.7324,0.0349,-0.5263,-0.444,-0.7252,0.034,-0.4361,-0.5136,-0.739,0.0344,-0.4126,-0.6001,-0.6853,0.0357,-0.3871,-0.6739,-0.6293,0.0373,-0.4276,-0.7746,-0.4659,0.0389,-0.463,-0.8345,-0.2988,0.0426,-0.515,-0.8524,-0.0905,0.0482,-0.5226,-0.8468,0.099,0.0577,-0.5343,-0.8038,0.2617,0.0629,-0.5587,-0.723,0.4064,0.0725,-0.5572,-0.6517,0.5145,0.0828,-0.5624,-0.5689,0.6,0.0927,-0.5681,-0.4921,0.6596,0.1039,-0.5839,-0.4279,0.6899,0.1172,-0.5935,-0.36,0.7199,0.1322,-0.6041,-0.2859,0.7438,0.1527,-0.6098,-0.2188,0.7618,0.1767,-0.6172,-0.1812,0.7657,0.1935,-0.6352,-0.1518,0.7572,0.2064,-0.6504,-0.1334,0.7478,0.2153,-0.6559,-0.1287,0.7438,0.223,-0.6597,-0.1207,0.7418,0.2299,-0.6601,-0.11,0.7431,0.2333,-0.6433,-0.1047,0.7584,0.2353,-0.622,-0.0916,0.7776,0.2352,-0.6005,-0.0659,0.7969,0.2364,-0.5779,-0.0394,0.8151,0.2404,-0.5481,-0.0355,0.8357,0.2424,-0.5096,-0.0344,0.8597,0.2446,-0.4637,-0.0424,0.885,0.2434,-0.3994,-0.0474,0.9156,0.243,-0.3358,-0.0479,0.9407,0.2434,-0.2776,-0.0385,0.9599,0.2487,-0.2171,-0.0284,0.9757,0.255,-0.1675,-0.0256,0.9855,0.2608,-0.1077,-0.0149,0.9941,0.2662,-0.0387,-0.0126,0.9992,0.27,0.0147,-0.0112,0.9998,0.2752,0.0452,0.0014,0.999,0.2803,0.0677,0.0015,0.9977,0.2855,0.0864,-0.0001,0.9963,0.2889,0.1019,-0.0089,0.9948,0.2917,0.1258,-0.0115,0.992,0.2918,0.162,-0.0145,0.9867,0.2883,0.2085,-0.0149,0.9779,0.2831,0.2591,-0.0079,0.9658,0.2747,0.3143,0.007,0.9493,0.2659,0.3767,0.0131,0.9262,0.254,0.4449,0.0189,0.8954,0.2438,0.5119,0.0244,0.8587,0.2354,0.5829,0.0323,0.8119,0.2298,0.6519,0.0403,0.7572,0.227,0.7028,0.0636,0.7086,0.23,0.7379,0.0893,0.6689,0.2323,0.7705,0.1288,0.6243,0.236,0.7989,0.1545,0.5813,0.2375,0.83,0.1718,0.5307,0.24,0.8597,0.1807,0.4778,0.2418,0.9,0.1766,0.3985,0.2462,0.9388,0.1648,0.3023,0.2507,0.962,0.151,0.2277,0.2475,0.9749,0.1313,0.1796,0.2407,0.9845,0.1011,0.143,0.231,0.991,0.0612,0.1188,0.2194,0.9967,0.0256,0.0772,0.2032,0.9989,-0.0089,0.0453,0.1892,0.9988,-0.0382,0.031,0.1789,0.9961,-0.0744,0.0467,0.169,0.9933,-0.0954,0.0659,0.1583,0.9886,-0.1199,0.0916,0.1506,0.974,-0.1584,0.1619,0.1435,0.9561,-0.1968,0.217,0.1393,0.9348,-0.239,0.2627,0.1323,0.9129,-0.2735,0.303,0.1255,0.8896,-0.2975,0.3466,0.1202,0.8627,-0.3071,0.4017,0.1135,0.8405,-0.2951,0.4545,0.1083,0.8176,-0.2436,0.5218,0.1038,0.7804,-0.1813,0.5985,0.1039,0.7229,-0.1241,0.6798,0.1052,0.6448,-0.0657,0.7615,0.1127,0.5643,0.0176,0.8254,0.123,0.5051,0.1106,0.8559,0.1366,0.4438,0.1797,0.8779,0.1523,0.3919,0.2303,0.8907,0.1677,0.3536,0.2769,0.8935,0.1822,0.306,0.3142,0.8987,0.1955,0.2818,0.3469,0.8946,0.206,0.2515,0.3694,0.8946,0.2172,0.2104,0.3811,0.9003,0.2214,0.1765,0.3757,0.9098,0.2201,0.1473,0.3739,0.9157,0.2169,0.1072,0.3857,0.9164,0.2116,0.0693,0.3988,0.9144,0.2081,0.0246,0.4166,0.9088,0.2044,-0.0248,0.4312,0.9019,0.201,-0.0824,0.4437,0.8924,0.192,-0.1634,0.4593,0.8731,0.1826,-0.2467,0.4644,0.8506,0.1725,-0.3244,0.4688,0.8216,0.1654,-0.4223,0.4568,0.7829,0.1626,-0.5001,0.4576,0.7352,0.1639,-0.5745,0.4462,0.6862,0.1699,-0.6477,0.417,0.6376,0.1756,-0.6914,0.3971,0.6036,0.1829,-0.7258,0.3711,0.5792,0.1882,-0.7419,0.3548,0.5689,0.1985,-0.7373,0.351,0.5773,0.206,-0.6978,0.3612,0.6186,0.2114,-0.6325,0.3929,0.6676,0.2146,-0.5403,0.4383,0.7184,0.2163,-0.4196,0.5033,0.7554,0.2132,-0.2457,0.5688,0.7849,0.2077,-0.0095,0.614,0.7893,0.2065,0.2241,0.6008,0.7673,0.2188,0.359,0.5541,0.751,0.2382,0.4175,0.5173,0.7471,0.2446,0.4299,0.5095,0.7454,0.2344,0.4214,0.51,0.7499,0.2134,0.3856,0.5112,0.7681,0.1853,0.3164,0.5004,0.8059,0.1542,0.1882,0.4491,0.8734,0.1241,-0.0344,0.3305,0.9432,0.0997,-0.3311,0.1309,0.9345,0.0883,-0.5742,-0.083,0.8145,0.0896,-0.7013,-0.2241,0.6768,0.0986,-0.7475,-0.2836,0.6006,0.1068,-0.7425,-0.2952,0.6013,0.1129,-0.7053,-0.2767,0.6527,0.1167,-0.6267,-0.2548,0.7364,0.119,-0.5033,-0.2325,0.8322,0.1222,-0.3609,-0.1857,0.9139,0.1273,-0.1941,-0.1399,0.971,0.1339,-0.0098,-0.0659,0.9978,0.1439,0.1414,-0.0132,0.9899,0.1596,0.2674,0.023,0.9633,0.1787,0.3771,0.0635,0.924,0.1984,0.4655,0.089,0.8805,0.2218,0.5326,0.0996,0.8405,0.2409,0.5801,0.1153,0.8063,0.2587,0.6099,0.114,0.7842,0.2734,0.5927,0.1291,0.795,0.2786,0.5809,0.1405,0.8017,0.2804,0.5707,0.1511,0.8071,0.2761,0.5711,0.1593,0.8053,0.2658,0.5951,0.1376,0.7918,0.2543,0.6513,0.1068,0.7513,0.2417,0.7135,0.092,0.6946,0.2297,0.7675,0.0666,0.6376,0.2247,0.8049,0.0289,0.5927,0.2212,0.8357,-0.0132,0.5491,0.2146,0.8561,-0.0717,0.5118,0.2008,0.873,-0.1725,0.4562,0.1854,0.8742,-0.285,0.3931,0.169,0.8645,-0.3814,0.3274,0.1536,0.8492,-0.4591,0.261,0.1349,0.8204,-0.5442,0.1754,0.1166,0.7666,-0.6384,0.0684,0.0967,0.6568,-0.7471,-0.102,0.0841,0.4839,-0.8359,-0.2591,0.0808,0.2776,-0.88,-0.3855,0.0866,0.1065,-0.8728,-0.4763,0.0939,-0.0502,-0.8367,-0.5453,0.1066,-0.155,-0.8002,-0.5793,0.1159,-0.2436,-0.7672,-0.5933,0.1228,-0.3038,-0.7315,-0.6105,0.1304,-0.3618,-0.7048,-0.6102,0.136,-0.4322,-0.6843,-0.5873,0.1386,-0.5169,-0.6533,-0.5532,0.1421,-0.5888,-0.622,-0.5162,0.1458,-0.6571,-0.5933,-0.4651,0.1507,-0.7138,-0.5652,-0.4135,0.1575,-0.7527,-0.5418,-0.374,0.1644,-0.7963,-0.5055,-0.3323,0.1708,-0.8339,-0.4664,-0.2952,0.1784,-0.8656,-0.4301,-0.2564,0.1865,-0.8949,-0.386,-0.2241,0.195,-0.9244,-0.3329,-0.186,0.2026,-0.9467,-0.2869,-0.1463,0.2088,-0.9644,-0.2442,-0.1015,0.2158,-0.9768,-0.2055,-0.0606,0.2233,-0.9845,-0.1755,-0.0035,0.2303,-0.9859,-0.1575,0.056,0.236,-0.9838,-0.1317,0.1215,0.2404,-0.9775,-0.0999,0.1857,0.2416,-0.9652,-0.0542,0.2558,0.239,-0.9459,-0.01,0.3244,0.2294,-0.9141,0.0536,0.402,0.2137,-0.854,0.1384,0.5016,0.1911,-0.7172,0.295,0.6313,0.1631,-0.4071,0.5191,0.7516,0.1396,0.1204,0.7028,0.7011,0.1461,0.5054,0.6997,0.5049,0.1962,0.6595,0.6568,0.3656,0.257,0.7251,0.6204,0.299,0.2941,0.7642,0.5896,0.2614,0.3014,0.7979,0.5537,0.2382,0.2879,0.8334,0.5109,0.2108,0.2585,0.8733,0.4593,0.1624,0.2228,0.9174,0.3867,0.0942,0.1827,0.962,0.269,0.0461,0.1445,0.9908,0.1317,0.0299,0.1082,0.9969,-0.0411,0.067,0.076,0.9301,-0.2752,0.2433,0.0468,0.4832,-0.5622,0.6712,0.0305,-0.3288,-0.4772,0.8149,0.0367,-0.5344,-0.3278,0.7791,0.0527,-0.5545,-0.2473,0.7946,0.0681,-0.5175,-0.2257,0.8254,0.0821,-0.4573,-0.2014,0.8662,0.0947,-0.3585,-0.1917,0.9136,0.1033,-0.2267,-0.1411,0.9637,0.115,-0.0567,-0.0573,0.9967,0.1295,0.097,0.0223,0.995,0.1499,0.2132,0.0865,0.9732,0.1751,0.2912,0.1178,0.9494,0.2061,0.3497,0.1281,0.9281,0.2392,0.4027,0.1241,0.9069,0.2757,0.4447,0.1353,0.8854,0.3108,0.4685,0.161,0.8686,0.3385,0.476,0.1847,0.8599,0.3563,0.4818,0.1964,0.854,0.3622,0.4867,0.1867,0.8534,0.3566,0.5,0.1664,0.8499,0.3455,0.5229,0.1253,0.8432,0.3325,0.5758,0.0809,0.8136,0.3191,0.6434,0.0516,0.7638,0.3024,0.7168,0.0287,0.6967,0.2846,0.7948,0.0175,0.6067,0.2695,0.8594,-0.0049,0.5112,0.2518,0.9024,-0.0472,0.4284,0.2353,0.9274,-0.1082,0.3579,0.2209,0.938,-0.1829,0.2944,0.2075,0.9353,-0.264,0.2358,0.1957,0.9179,-0.3483,0.1898,0.1834,0.8937,-0.4298,0.1289,0.1702,0.8634,-0.5,0.0667,0.1565,0.828,-0.5605,0.0171,0.1421,0.7884,-0.6142,-0.0355,0.1293,0.7252,-0.683,-0.0872,0.1171,0.6543,-0.7434,-0.1388,0.1081,0.5467,-0.8163,-0.1863,0.0994,0.4356,-0.8698,-0.2315,0.0955,0.3315,-0.9116,-0.2429,0.0955,0.1911,-0.9157,-0.3535,0.0982,0.0914,-0.8953,-0.436,0.0997,-0.0305,-0.8771,-0.4794,0.0992,-0.1424,-0.8575,-0.4944,0.0952,-0.2617,-0.8263,-0.4987,0.0907,-0.3627,-0.7842,-0.5035,0.0851,-0.4581,-0.7414,-0.4904,0.0826,-0.5736,-0.7007,-0.4242,0.0846,-0.6522,-0.6547,-0.3821,0.0897,-0.7121,-0.62,-0.3294,0.0978,-0.755,-0.5863,-0.2937,0.109,-0.781,-0.5594,-0.2778,0.1202,-0.8032,-0.5314,-0.269,0.1314,-0.8268,-0.5186,-0.218,0.141,-0.8483,-0.4967,-0.1835,0.1522,-0.8623,-0.4805,-0.1596,0.1629,-0.8698,-0.4733,-0.1394,0.1753,-0.8854,-0.4478,-0.125,0.1863,-0.8953,-0.4338,-0.1013,0.1979,-0.9038,-0.4199,-0.0827,0.2066,-0.9139,-0.4007,-0.065,0.2126,-0.925,-0.3777,-0.042,0.2178,-0.934,-0.3571,-0.0149,0.2219,-0.9385,-0.3445,0.0225,0.2249,-0.9443,-0.3218,0.0689,0.227,-0.9444,-0.3032,0.1273,0.2268,-0.9411,-0.278,0.1926,0.2269,-0.9322,-0.2365,0.274,0.2248,-0.9136,-0.1793,0.365,0.225,-0.8838,-0.1167,0.4531,0.225,-0.8472,-0.0458,0.5292,0.2261,-0.7959,0.0224,0.6051,0.2254,-0.7353,0.1,0.6703,0.2207,-0.66,0.1713,0.7314,0.2145,-0.5688,0.2535,0.7825,0.2063,-0.4457,0.3487,0.8244,0.1938])

Group366.addChildren(OrientationInterpolator379)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.885964,17.54318], [-13.573542,13.69133], [-5.606315,10.062532] degrees
#-1.317750 -1.286104 -0.673492, -1.301316 -1.366098 -0.701196, -1.470395 -1.454794 -0.724041, -1.470395 -1.454794 -0.724041, -1.509849 -1.297974 -0.713856, -1.472780 -1.115783 -0.781199, -1.419042 -1.013363 -0.876688, -1.461995 -0.845389 -1.021629, -1.409099 -0.827931 -1.236261, -1.356436 -0.810885 -1.451107, -1.051746 -0.936286 -1.733474, -0.749921 -1.117671 -2.045724, -0.279234 -1.417705 -2.359331, 0.285132 -1.735062 -2.795323, 0.894825 -1.949656 -2.883907, 1.626820 -2.362706 -2.969104, 2.369530 -2.706624 -3.036180, 3.110428 -3.068982 -2.940533, 3.842908 -3.478372 -2.814568, 4.538624 -4.029786 -2.715255, 5.354771 -4.616504 -2.513999, 6.407552 -5.413402 -2.201791, 7.620510 -6.301512 -1.799806, 8.407479 -6.964830 -1.502154, 8.889326 -7.622513 -1.208806, 9.170975 -8.122870 -0.999575, 9.449203 -8.477419 -0.949279, 9.726587 -8.784123 -0.848442, 9.900585 -8.907694 -0.704670, 10.197036 -8.752707 -0.635539, 10.463896 -8.448426 -0.464976, 10.804849 -8.169545 -0.122982, 11.260267 -7.960663 0.240736, 11.639968 -7.608035 0.281475, 12.080660 -7.138828 0.272176, 12.360570 -6.480808 0.108157, 12.754566 -5.587594 -0.038693, 13.122949 -4.719154 -0.127954, 13.683297 -3.983242 -0.074007, 14.256371 -3.189939 -0.018042, 14.725115 -2.523887 -0.057812, 15.164227 -1.653351 -0.009166, 15.455572 -0.618176 -0.112255, 15.764572 0.204643 -0.206643, 16.046377 0.719395 -0.078635, 16.320629 1.095314 -0.131712, 16.493528 1.409999 -0.206781, 16.630131 1.658316 -0.391475, 16.595665 2.045549 -0.492775, 16.314447 2.605448 -0.614835, 15.888074 3.305167 -0.704329, 15.231986 4.013544 -0.661347, 14.490420 4.750102 -0.497663, 13.513572 5.455311 -0.455753, 12.540332 6.193209 -0.416238, 11.617925 6.889326 -0.371693, 10.723685 7.668816 -0.293911, 9.883469 8.482862 -0.208570, 9.351080 9.287950 0.080379, 8.889342 9.874573 0.424272, 8.374214 10.506554 0.977674, 7.802840 10.978165 1.361279, 7.154949 11.528626 1.650022, 6.450048 12.024899 1.835587, 5.432131 12.794387 1.894085, 4.139839 13.562000 1.887544, 3.029183 13.691330 1.788305, 2.306018 13.478493 1.546627, 1.770693 13.049044 1.141016, 1.431640 12.465671 0.616305, 0.880265 11.605193 0.209509, 0.505662 10.826180 -0.144145, 0.356421 10.238907 -0.424859, 0.518413 9.644545 -0.766174, 0.671140 9.002534 -0.919672, 0.873507 8.521063 -1.101667, 1.431693 7.992437 -1.404773, 1.847027 7.602446 -1.695277, 2.114698 7.053100 -1.944912, 2.300323 6.522215 -2.099638, 2.504880 6.078806 -2.183403, 2.718434 5.561996 -2.131409, 2.911888 5.168576 -1.964713, 3.172235 4.820767 -1.584038, 3.612932 4.606969 -1.225020, 4.134538 4.327429 -0.905039, 4.940413 4.139500 -0.603500, 5.819566 3.974660 -0.078068, 6.680144 3.994943 0.633699, 7.620382 3.966140 1.306709, 8.498429 3.916367 1.927404, 9.242581 3.907996 2.581699, 9.970401 3.717489 3.205885, 10.444104 3.680554 3.770159, 11.008425 3.552119 4.270124, 11.306034 3.129151 4.542667, 11.378166 2.681438 4.488688, 11.297236 2.275906 4.436393, 11.047242 1.741632 4.522133, 10.858277 1.271034 4.648258, 10.618443 0.737370 4.823961, 10.383893 0.165068 4.963023, 9.844585 -0.483513 4.935708, 9.199865 -1.318277 4.922706, 8.500084 -2.090997 4.754916, 7.904191 -2.760776 4.642013, 7.443771 -3.648649 4.500817, 7.089857 -4.422847 4.579883, 6.903844 -5.319279 4.672275, 6.675500 -6.262482 4.571021, 6.617200 -6.994934 4.576626, 6.552776 -7.585517 4.446744, 6.809133 -8.183872 4.535035, 7.174241 -8.424410 4.684320, 7.861928 -8.131747 4.949130, 8.576159 -7.393561 5.402057, 9.246359 -6.236637 5.954513, 9.507273 -4.599198 6.548679, 9.498481 -2.353955 6.982546, 9.319865 0.478314 7.241063, 9.419635 3.419379 7.271118, 9.925582 5.534717 7.104541, 10.114864 6.466743 6.703916, 9.681649 6.330032 6.330076, 8.896881 5.618188 5.814156, 7.962525 4.458812 5.127316, 7.013669 3.060812 4.241195, 6.171081 1.507370 3.115254, 5.390015 -0.107223 1.894620, 4.740378 -1.646376 0.731115, 4.173450 -2.960495 -0.318324, 3.786493 -4.002096 -1.134783, 3.613938 -4.626791 -1.591173, 3.818410 -4.863667 -1.749537, 4.298348 -4.781960 -1.672569, 4.963531 -4.341569 -1.550394, 5.784306 -3.600552 -1.447909, 6.638031 -2.704159 -1.199341, 7.434775 -1.554422 -0.973503, 8.227912 -0.119353 -0.536070, 9.055745 1.278209 -0.222259, 9.863111 2.744109 -0.000429, 10.498290 4.330005 0.326086, 11.171907 5.988620 0.549250, 11.577847 7.440228 0.626547, 11.914284 8.714038 0.807428, 12.251301 9.672551 0.756265, 12.637959 9.612482 1.007672, 12.809380 9.505831 1.201641, 12.687813 9.219806 1.378329, 12.175011 8.890397 1.490046, 11.471625 8.812018 1.127861, 10.375776 9.104897 0.658446, 9.123167 9.446597 0.460066, 8.215046 9.907144 0.148232, 7.559227 10.196490 -0.306956, 6.838316 10.239646 -0.776556, 6.019483 9.790719 -1.343534, 5.035826 9.180264 -2.242138, 4.039029 8.363939 -3.061777, 3.119660 7.513804 -3.566264, 2.228949 6.495920 -3.679926, 1.349195 5.440307 -3.703081, 0.511199 4.234894 -3.559468, -0.392168 3.177160 -3.589142, -1.123112 2.277934 -3.846636, -1.858735 1.448142 -4.342416, -2.536751 0.676912 -4.681822, -3.339742 -0.157818 -5.116310, -3.890090 -0.848718 -5.345763, -4.251044 -1.513370 -5.458125, -4.664247 -2.046347 -5.551929, -4.885964 -2.584211 -5.606315, -4.823501 -3.201179 -5.572124, -4.700454 -3.988425 -5.487072, -4.538981 -4.710719 -5.387578, -4.278247 -5.482764 -5.334987, -4.028649 -6.260990 -5.327360, -3.853309 -6.919966 -5.345525, -3.606238 -7.637842 -5.197511, -3.393920 -8.385533 -5.027195, -3.133918 -9.123260 -4.855946, -2.908099 -9.890314 -4.576361, -2.549343 -10.644463 -4.113063, -2.116698 -11.262376 -3.652643, -1.593019 -11.886368 -3.196653, -1.079651 -12.473793 -2.757426, -0.315335 -12.986735 -2.361969, 0.517664 -13.344446 -2.078495, 1.485644 -13.573542 -1.645152, 2.452726 -13.558006 -1.097401, 3.479110 -13.230721 -0.342357, 4.316785 -12.424053 0.338495, 5.050070 -11.149442 1.151996, 5.665052 -9.262166 1.979836, 6.085854 -6.545461 3.110768, 6.129504 -3.029195 4.318870, 5.807889 1.305168 5.822650, 5.287465 6.043375 7.598718, 4.585683 10.110108 9.298064, 3.957167 12.598308 10.062532, 3.378385 13.521317 9.831505, 2.914748 13.413976 8.835750, 2.332890 12.508270 7.341935, 1.517504 11.234125 5.733371, 0.651414 9.627780 4.001714, 0.228014 7.971572 2.215487, 0.141780 6.143533 0.809635, 0.299285 4.342711 -0.190321, 0.669612 2.492214 -0.753489, 1.178723 0.833233 -0.989867, 1.706523 -0.705873 -0.992464, 2.337172 -1.632025 -0.955941, 3.083950 -2.188865 -0.906695, 3.861870 -2.467827 -0.978689, 4.679349 -2.523208 -0.990469, 5.387169 -2.171344 -1.033294, 6.339836 -1.542066 -0.845114, 7.396822 -0.447090 -0.396716, 8.545075 0.844467 0.128434, 9.753472 2.202303 0.682547, 11.181789 3.552458 1.048301, 12.674907 4.946613 1.214100, 14.274346 6.537369 1.152441, 15.699834 8.147604 1.303106, 16.742702 9.412205 1.764866, 17.402830 10.136873 2.253747, 17.543180 10.462035 2.499675, 17.277468 10.364061 2.274741, 16.705217 10.234032 1.819370, 16.020954 10.164732 0.974725, 14.906523 10.599236 0.100861, 13.315224 11.150566 -0.404945, 11.470420 11.656442 -0.704190, 9.485150 12.241196 -0.747093, 7.499157 12.358516 -0.883603, 5.932466 12.112839 -1.270013, 4.735602 11.667559 -1.859331, 3.758507 11.074418 -2.547009, 2.947488 10.411109 -3.238325, 2.323493 9.571927 -3.863721, 1.587483 8.659679 -4.319242, 0.906702 7.712152 -4.552758, 0.409680 6.730122 -4.593793, -0.030807 5.844223 -4.552019, -0.390870 4.885818 -4.570259, -0.697199 4.083123 -4.582325, -0.934505 3.153200 -4.624654, -1.167557 2.434355 -4.737428, -1.248823 1.869413 -4.968577, -1.939281 1.163576 -5.135688, -2.463104 0.632156 -5.099645, -2.730061 -0.054328 -4.989577, -2.726495 -0.665604 -4.695340, -2.639529 -1.260933 -4.322954, -2.511816 -1.683985 -3.860152, -2.386370 -2.094701 -3.552798, -2.140466 -2.718519 -3.450499, -2.064105 -3.293092 -3.427168, -1.969081 -3.931649 -3.544216, -1.988227 -4.652641 -3.745245, -2.098744 -5.309823 -3.953784, -2.243910 -5.972004 -4.123403, -2.013474 -6.609069 -4.312143, -1.889931 -7.330645 -4.460405, -1.814851 -7.978594 -4.617666, -1.775134 -8.668216 -4.898819, -1.743260 -9.381310 -4.933229, -1.601035 -10.088511 -5.073495, -1.459099 -10.639513 -5.119811, -1.281313 -11.081793 -5.019835, -1.013646 -11.509042 -4.831505, -0.670544 -11.855889 -4.626600, -0.183342 -12.093885 -4.475757, 0.452800 -12.304103 -4.153394, 1.248503 -12.319628 -3.821081, 2.148047 -12.304000 -3.397958, 3.255216 -12.090082 -2.713717, 4.530641 -11.855759 -1.849761, 5.767203 -11.449569 -0.931998, 6.884411 -10.986089 0.067133, 7.923868 -10.224658 1.000889, 8.651861 -9.168123 1.964750, 9.196260 -7.910711 2.750803, 9.459954 -6.447221 3.540138, 9.337306 -4.615580 4.261023
#Interpolator9_r_midtarsal channels [27..29] sends animation values to BVH JOINT RightAnkleEnd, DEF Bvh1_r_midtarsal, <HAnimJoint name=r_midtarsal/>
OrientationInterpolator380 = OrientationInterpolator()
OrientationInterpolator380.setDEF("Interpolator9_r_midtarsal")
OrientationInterpolator380.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator380.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0])

Group366.addChildren(OrientationInterpolator380)
#Unchanging Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.0,4.9E-324], [0.0,4.9E-324], [0.0,4.9E-324] degrees
#0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000
#Interpolator10_vl5 channels [30..32] sends animation values to BVH JOINT Chest, DEF Bvh1_vl5, <HAnimJoint name=vl5/>
OrientationInterpolator381 = OrientationInterpolator()
OrientationInterpolator381.setDEF("Interpolator10_vl5")
OrientationInterpolator381.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator381.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0])

Group366.addChildren(OrientationInterpolator381)
#Jittery Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-3.0E-6,2.0E-6], [-2.0E-6,1.0E-6], [-2.0E-6,2.0E-6] degrees
#0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 0.000001, 0.000000 0.000000 0.000000, -0.000000 0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, -0.000001 -0.000001 0.000001, 0.000001 -0.000001 -0.000000, -0.000000 -0.000000 0.000000, -0.000000 -0.000001 -0.000000, 0.000000 -0.000000 -0.000000, -0.000000 -0.000000 -0.000000, 0.000002 -0.000000 -0.000000, -0.000002 -0.000000 0.000000, 0.000000 -0.000000 0.000001, -0.000001 -0.000001 0.000000, -0.000000 -0.000000 -0.000001, -0.000002 -0.000001 0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000000 -0.000000, -0.000002 -0.000000 -0.000000, 0.000000 -0.000000 0.000000, 0.000001 -0.000000 0.000001, -0.000003 -0.000001 0.000002, -0.000001 -0.000001 0.000001, 0.000001 -0.000000 0.000000, 0.000001 -0.000001 0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000002 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 0.000000, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 0.000000, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000000, 0.000001 -0.000000 0.000000, 0.000002 -0.000001 -0.000000, 0.000001 -0.000001 -0.000000, -0.000000 -0.000001 -0.000001, -0.000002 -0.000000 -0.000000, -0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000001 -0.000000 -0.000000, -0.000002 -0.000000 -0.000001, -0.000002 0.000000 -0.000001, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000000, 0.000001 -0.000001 -0.000001, -0.000000 -0.000001 0.000001, 0.000001 -0.000001 0.000001, 0.000001 -0.000001 0.000001, -0.000001 -0.000001 -0.000001, -0.000001 -0.000001 -0.000001, 0.000000 0.000000 -0.000001, 0.000001 -0.000000 -0.000001, -0.000000 -0.000001 0.000001, -0.000001 0.000000 -0.000001, 0.000001 -0.000001 0.000001, -0.000001 0.000000 0.000001, 0.000001 0.000000 -0.000000, -0.000002 -0.000001 0.000000, 0.000001 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000001 0.000001, 0.000001 -0.000001 0.000001, -0.000001 -0.000001 0.000000, 0.000001 -0.000000 0.000000, -0.000000 -0.000001 0.000000, -0.000002 -0.000001 0.000000, -0.000001 -0.000000 0.000001, 0.000001 -0.000000 -0.000000, -0.000002 -0.000000 -0.000000, 0.000002 -0.000000 -0.000000, -0.000001 -0.000001 -0.000000, -0.000001 -0.000000 -0.000000, -0.000002 -0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000000, -0.000002 0.000000 -0.000001, 0.000000 -0.000000 -0.000000, -0.000000 -0.000000 0.000000, -0.000001 -0.000001 0.000002, 0.000000 0.000000 -0.000000, 0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 0.000000, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000000, 0.000000 -0.000000 0.000001, -0.000002 -0.000000 -0.000000, 0.000000 -0.000001 0.000001, 0.000000 -0.000000 0.000000, 0.000001 0.000000 -0.000000, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000000 -0.000001 0.000000, 0.000000 -0.000000 -0.000001, 0.000001 -0.000001 -0.000000, -0.000002 0.000000 -0.000001, -0.000002 -0.000001 0.000000, -0.000001 -0.000001 0.000000, 0.000001 0.000000 -0.000001, -0.000000 -0.000001 0.000000, 0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000002, -0.000000 -0.000001 0.000000, 0.000000 -0.000000 0.000000, -0.000002 -0.000001 0.000001, 0.000000 0.000001 -0.000000, -0.000001 -0.000001 0.000001, -0.000000 0.000000 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000000 0.000000, -0.000002 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000000 -0.000000, -0.000000 -0.000001 -0.000001, 0.000001 -0.000000 0.000001, -0.000000 0.000000 0.000001, -0.000003 -0.000000 0.000001, -0.000001 -0.000001 0.000001, 0.000001 -0.000000 0.000000, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 0.000000, 0.000000 0.000000 -0.000001, -0.000000 -0.000001 0.000001, -0.000001 -0.000001 0.000001, -0.000003 -0.000001 0.000000, 0.000000 -0.000001 0.000000, -0.000001 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 -0.000001, -0.000003 -0.000002 0.000001, 0.000001 -0.000002 0.000000, -0.000001 -0.000001 -0.000002, 0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000001 -0.000001 -0.000000, 0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000002 -0.000001 0.000000, 0.000000 0.000001 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 -0.000000 0.000001, 0.000000 0.000000 0.000001, -0.000002 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000001 -0.000001 0.000000, 0.000002 -0.000001 0.000001, -0.000000 0.000000 -0.000001, 0.000000 -0.000001 0.000001, -0.000001 -0.000001 -0.000000, 0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000000, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000001, -0.000002 -0.000001 0.000000, 0.000000 0.000001 0.000000, -0.000001 -0.000001 0.000001, -0.000002 -0.000001 0.000001, -0.000000 -0.000001 0.000001, -0.000000 -0.000000 0.000000, -0.000001 -0.000001 -0.000001, 0.000001 0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000001 -0.000001 0.000001, 0.000000 0.000000 0.000000, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 0.000001, -0.000002 -0.000001 0.000002, -0.000001 -0.000001 0.000001, 0.000001 -0.000001 0.000001, 0.000001 0.000000 0.000001, -0.000002 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, 0.000000 -0.000001 0.000001, -0.000002 -0.000001 -0.000000, 0.000001 0.000000 -0.000000, 0.000001 0.000001 0.000002, 0.000000 -0.000001 -0.000000, -0.000001 -0.000000 0.000001, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000002 -0.000001 0.000001, 0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 -0.000001 -0.000000, 0.000001 0.000001 -0.000002, 0.000001 -0.000001 -0.000000, -0.000002 0.000000 -0.000000, 0.000000 -0.000001 0.000001, -0.000001 0.000001 -0.000000, 0.000001 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 0.000000, -0.000001 -0.000002 0.000002, 0.000001 0.000001 -0.000000, 0.000000 0.000000 -0.000001, 0.000001 0.000000 0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000001 0.000000, 0.000001 -0.000001 -0.000002, -0.000000 -0.000000 0.000000, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000000, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 -0.000000, -0.000001 0.000000 0.000000, -0.000003 -0.000002 -0.000000, -0.000002 -0.000001 0.000001, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000002 -0.000001 -0.000001, 0.000001 -0.000001 0.000001, 0.000002 -0.000000 0.000000, 0.000002 -0.000000 0.000000, 0.000002 -0.000000 0.000000, 0.000000 -0.000001 0.000001, -0.000000 0.000000 0.000001, -0.000000 0.000000 -0.000001, 0.000001 -0.000001 0.000000, -0.000001 -0.000002 -0.000001, -0.000001 -0.000000 0.000000, 0.000001 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000001 0.000002, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, -0.000001 -0.000002 0.000002, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 0.000000, 0.000000 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000000, -0.000001 -0.000001 -0.000000, 0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 0.000001 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000001, -0.000001 -0.000001 0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 0.000000 -0.000000, 0.000001 -0.000000 -0.000000, 0.000000 -0.000002 0.000002, -0.000000 -0.000000 0.000000, 0.000001 -0.000001 0.000001, 0.000001 0.000000 0.000001, -0.000001 -0.000000 -0.000000, -0.000000 -0.000001 -0.000000, -0.000001 0.000000 0.000000
#Interpolator11_Chest2 channels [33..35] sends animation values to BVH JOINT Chest2, DEF Bvh1_Chest2, <HAnimJoint name=Chest2/>
OrientationInterpolator382 = OrientationInterpolator()
OrientationInterpolator382.setDEF("Interpolator11_Chest2")
OrientationInterpolator382.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator382.setKeyValue([-0.0484,0.1749,0.9834,0.0781,-0.0418,0.1877,0.9813,0.0796,-0.028,0.1813,0.983,0.0822,-0.0208,0.1629,0.9864,0.0832,-0.0208,0.1629,0.9864,0.0832,-0.0374,0.1745,0.9839,0.0827,-0.0374,0.1745,0.9839,0.0827,-0.0449,0.1931,0.9801,0.0817,-0.1028,0.1811,0.9781,0.0791,-0.1551,0.1811,0.9712,0.0783,-0.191,0.1547,0.9693,0.0794,-0.2268,0.1402,0.9638,0.0785,-0.2735,0.1193,0.9544,0.0789,-0.3018,0.0855,0.9495,0.0796,-0.3119,0.0735,0.9473,0.0808,-0.3176,0.0553,0.9466,0.0834,-0.3178,0.0292,0.9477,0.0842,-0.3258,0.0238,0.9451,0.0864,-0.3162,0.0166,0.9485,0.0903,-0.347,0.0278,0.9375,0.0928,-0.3729,0.0497,0.9266,0.094,-0.3889,0.0457,0.9201,0.0972,-0.4282,0.0448,0.9026,0.0987,-0.4787,0.0529,0.8764,0.1004,-0.5498,0.0738,0.8321,0.1014,-0.624,0.0623,0.779,0.099,-0.6912,0.0846,0.7177,0.0945,-0.7272,0.1092,0.6777,0.0859,-0.7451,0.1644,0.6464,0.0805,-0.7482,0.2138,0.628,0.0777,-0.7657,0.2215,0.6038,0.0749,-0.7743,0.209,0.5973,0.0755,-0.7662,0.2102,0.6072,0.0753,-0.7574,0.1815,0.6272,0.0756,-0.7446,0.1509,0.6502,0.0761,-0.7195,0.1395,0.6803,0.0751,-0.6958,0.1194,0.7082,0.0724,-0.6697,0.0992,0.736,0.0679,-0.6589,0.0682,0.7491,0.0655,-0.6292,0.0457,0.7759,0.0628,-0.6241,0.0233,0.781,0.0596,-0.6559,-0.0104,0.7548,0.0564,-0.6774,-0.0043,0.7356,0.0526,-0.6422,0.0091,0.7665,0.0519,-0.641,0.0171,0.7673,0.0513,-0.6248,0.0407,0.7797,0.0526,-0.5684,0.073,0.8195,0.0524,-0.5259,0.1312,0.8404,0.0518,-0.4947,0.2139,0.8423,0.0494,-0.4628,0.2541,0.8492,0.0481,-0.4234,0.2334,0.8754,0.0493,-0.4503,0.2361,0.8611,0.0491,-0.4714,0.212,0.8561,0.0525,-0.4722,0.1829,0.8623,0.0588,-0.4952,0.1614,0.8537,0.0623,-0.4695,0.1101,0.876,0.0662,-0.4797,0.0732,0.8744,0.07,-0.4897,0.0601,0.8698,0.0739,-0.5477,0.0334,0.836,0.08,-0.5795,-0.0063,0.8149,0.0868,-0.624,-0.0389,0.7805,0.0933,-0.6369,-0.0457,0.7696,0.0998,-0.6546,-0.0549,0.754,0.1067,-0.6655,-0.0677,0.7433,0.1127,-0.6591,-0.0785,0.7479,0.1198,-0.6698,-0.1129,0.7339,0.1266,-0.6719,-0.1177,0.7312,0.132,-0.6632,-0.117,0.7393,0.1363,-0.648,-0.1193,0.7522,0.1394,-0.6212,-0.1172,0.7748,0.143,-0.593,-0.1134,0.7971,0.1453,-0.5609,-0.1131,0.8201,0.1469,-0.5283,-0.1173,0.8409,0.1431,-0.5029,-0.1246,0.8553,0.1387,-0.488,-0.1494,0.8599,0.1361,-0.4733,-0.1711,0.8641,0.1315,-0.4642,-0.1838,0.8665,0.1263,-0.4562,-0.1864,0.8701,0.1247,-0.458,-0.2016,0.8658,0.1237,-0.4728,-0.201,0.8579,0.1227,-0.4915,-0.182,0.8517,0.1218,-0.4974,-0.179,0.8489,0.121,-0.5112,-0.1728,0.8419,0.1179,-0.51,-0.16,0.8452,0.114,-0.4937,-0.1391,0.8584,0.1097,-0.4873,-0.1144,0.8657,0.1042,-0.4754,-0.0947,0.8747,0.0977,-0.4747,-0.091,0.8754,0.0913,-0.4861,-0.0722,0.8709,0.0838,-0.4556,-0.0608,0.8881,0.0779,-0.4513,-0.0286,0.8919,0.0732,-0.4447,-0.0035,0.8957,0.0706,-0.4373,0.0067,0.8993,0.0678,-0.4326,0.038,0.9008,0.0677,-0.3766,0.0613,0.9244,0.0663,-0.3056,0.0865,0.9482,0.0674,-0.2629,0.1219,0.9571,0.0686,-0.2059,0.1351,0.9692,0.0705,-0.1291,0.1274,0.9834,0.0715,-0.0668,0.1465,0.987,0.0733,-0.0189,0.1495,0.9886,0.0742,0.0352,0.1325,0.9906,0.0763,0.0742,0.1309,0.9886,0.0772,0.0888,0.1227,0.9885,0.0802,0.0979,0.115,0.9885,0.0834,0.1008,0.1254,0.987,0.0855,0.0964,0.1011,0.9902,0.0866,0.0639,0.1186,0.9909,0.0896,0.0571,0.1342,0.9893,0.0914,0.0284,0.1308,0.991,0.0924,-0.0064,0.1437,0.9896,0.0923,-0.0492,0.1704,0.9841,0.0946,-0.1066,0.1716,0.9794,0.0973,-0.1913,0.183,0.9643,0.1007,-0.2718,0.1983,0.9417,0.1013,-0.3566,0.1826,0.9162,0.1004,-0.4278,0.1678,0.8881,0.1005,-0.4956,0.1609,0.8535,0.1016,-0.5283,0.1532,0.8352,0.1046,-0.5672,0.1287,0.8134,0.1099,-0.6029,0.1286,0.7874,0.1182,-0.6366,0.1071,0.7637,0.1257,-0.6624,0.1177,0.7398,0.1323,-0.6866,0.1221,0.7168,0.1363,-0.7122,0.1306,0.6897,0.1372,-0.7273,0.1382,0.6723,0.1365,-0.7224,0.1385,0.6775,0.1358,-0.7195,0.1374,0.6807,0.132,-0.7186,0.1417,0.6808,0.1311,-0.7117,0.147,0.687,0.1337,-0.7032,0.1464,0.6957,0.1357,-0.6984,0.1468,0.7005,0.1354,-0.6927,0.138,0.7079,0.1365,-0.6871,0.1254,0.7157,0.1362,-0.6732,0.1204,0.7296,0.1325,-0.6571,0.1193,0.7443,0.1284,-0.634,0.0991,0.767,0.1254,-0.6075,0.0731,0.7909,0.1213,-0.5673,0.0473,0.8222,0.1158,-0.5315,0.0108,0.847,0.1136,-0.4851,-0.0385,0.8736,0.1131,-0.4785,-0.0946,0.873,0.1106,-0.4736,-0.1451,0.8687,0.1097,-0.4783,-0.2206,0.85,0.1086,-0.4734,-0.2923,0.8309,0.1071,-0.4768,-0.3582,0.8027,0.1081,-0.478,-0.399,0.7825,0.1105,-0.4747,-0.4445,0.7597,0.1115,-0.4591,-0.4731,0.7519,0.113,-0.4468,-0.4922,0.7471,0.1151,-0.4317,-0.5056,0.747,0.1182,-0.4396,-0.5069,0.7415,0.1222,-0.4431,-0.5055,0.7403,0.1291,-0.4454,-0.494,0.7467,0.1362,-0.4396,-0.4822,0.7578,0.1435,-0.4295,-0.468,0.7723,0.1504,-0.4135,-0.4527,0.79,0.1592,-0.4113,-0.4286,0.8044,0.1684,-0.4009,-0.41,0.8192,0.1759,-0.3939,-0.4007,0.8272,0.1829,-0.3938,-0.3874,0.8336,0.1889,-0.4099,-0.3786,0.8298,0.1914,-0.4205,-0.3627,0.8316,0.1918,-0.4207,-0.3603,0.8326,0.1899,-0.4268,-0.3536,0.8323,0.1889,-0.4284,-0.3561,0.8305,0.1841,-0.4386,-0.3537,0.8261,0.1789,-0.4409,-0.3563,0.8238,0.1741,-0.4405,-0.3645,0.8204,0.1684,-0.4454,-0.3603,0.8196,0.1613,-0.4549,-0.3595,0.8148,0.156,-0.4658,-0.3744,0.8018,0.1497,-0.4721,-0.3889,0.7912,0.1447,-0.48,-0.3958,0.7829,0.1389,-0.485,-0.3955,0.78,0.1349,-0.484,-0.4106,0.7728,0.1301,-0.4861,-0.4164,0.7683,0.1267,-0.472,-0.41,0.7805,0.1224,-0.4589,-0.4123,0.787,0.118,-0.4377,-0.4037,0.8034,0.1159,-0.4221,-0.3966,0.8152,0.115,-0.4061,-0.3893,0.8268,0.1141,-0.3635,-0.3854,0.8481,0.1129,-0.3303,-0.3807,0.8637,0.1108,-0.3065,-0.3614,0.8806,0.1126,-0.2885,-0.3344,0.8972,0.1154,-0.2915,-0.3071,0.9059,0.1198,-0.2912,-0.2808,0.9145,0.1234,-0.3096,-0.2625,0.9139,0.1285,-0.3195,-0.2353,0.9179,0.133,-0.3152,-0.2107,0.9253,0.1363,-0.328,-0.1842,0.9265,0.1402,-0.3335,-0.1658,0.9281,0.1399,-0.3653,-0.1415,0.9201,0.1382,-0.3974,-0.1348,0.9077,0.1374,-0.4311,-0.1371,0.8918,0.1359,-0.4672,-0.133,0.8741,0.1358,-0.4977,-0.125,0.8583,0.135,-0.5225,-0.134,0.842,0.1344,-0.5496,-0.1265,0.8258,0.1344,-0.5817,-0.1094,0.806,0.1346,-0.6044,-0.0923,0.7913,0.1326,-0.6038,-0.0919,0.7918,0.1279,-0.5919,-0.1069,0.7989,0.1245,-0.597,-0.1305,0.7916,0.1184,-0.5905,-0.1402,0.7948,0.1152,-0.572,-0.1548,0.8055,0.1154,-0.5457,-0.1719,0.8201,0.1178,-0.5164,-0.1759,0.8381,0.1228,-0.4867,-0.1802,0.8548,0.1252,-0.4576,-0.1839,0.8699,0.1277,-0.4338,-0.2043,0.8775,0.129,-0.416,-0.2028,0.8865,0.1327,-0.392,-0.224,0.8923,0.1352,-0.3727,-0.2467,0.8945,0.138,-0.3494,-0.2621,0.8996,0.1382,-0.3258,-0.2772,0.9039,0.1386,-0.2867,-0.3044,0.9084,0.1386,-0.2443,-0.327,0.9129,0.1373,-0.2142,-0.3535,0.9106,0.1356,-0.1763,-0.368,0.913,0.1387,-0.1504,-0.3938,0.9068,0.1415,-0.1539,-0.4209,0.894,0.1439,-0.1657,-0.4493,0.8779,0.149,-0.1822,-0.4714,0.8629,0.1526,-0.2004,-0.4898,0.8485,0.1577,-0.2243,-0.4897,0.8426,0.1621,-0.2581,-0.4851,0.8355,0.1667,-0.2939,-0.475,0.8294,0.17,-0.3153,-0.4674,0.8259,0.174,-0.329,-0.4656,0.8216,0.1782,-0.3404,-0.4764,0.8106,0.1806,-0.3474,-0.4866,0.8016,0.186,-0.3552,-0.4971,0.7917,0.1933,-0.3552,-0.5099,0.7835,0.1981,-0.3541,-0.5154,0.7804,0.2038,-0.3454,-0.5194,0.7816,0.2046,-0.3367,-0.5166,0.7873,0.2073,-0.3125,-0.5097,0.8016,0.2067,-0.2814,-0.5014,0.8182,0.2018,-0.2571,-0.4957,0.8296,0.1955,-0.2447,-0.4801,0.8424,0.1896,-0.2446,-0.4812,0.8418,0.1852,-0.2336,-0.4734,0.8493,0.1814,-0.213,-0.4744,0.8541,0.1755,-0.1819,-0.4789,0.8588,0.1705,-0.1574,-0.4793,0.8634,0.1662,-0.1323,-0.4638,0.876,0.1621,-0.1299,-0.449,0.884,0.1559,-0.1345,-0.4355,0.8901,0.1505,-0.1523,-0.4263,0.8917,0.1449,-0.1697,-0.4146,0.894,0.1399,-0.2004,-0.4177,0.8862,0.136,-0.2048,-0.42,0.8841,0.1325,-0.2198,-0.4173,0.8818,0.1296,-0.246,-0.4267,0.8703,0.124,-0.2578,-0.4305,0.865,0.1216,-0.2803,-0.4264,0.86,0.1168,-0.2838,-0.4139,0.865,0.1138,-0.2928,-0.4142,0.8618,0.1103,-0.2947,-0.4018,0.867,0.107,-0.2829,-0.3849,0.8785,0.1053,-0.2357,-0.3762,0.8961,0.101,-0.208,-0.3627,0.9084,0.0983,-0.1701,-0.3566,0.9186,0.0973,-0.1651,-0.3621,0.9174,0.0975,-0.1887,-0.3328,0.9239,0.0999,-0.2324,-0.3156,0.92,0.1036,-0.289,-0.2941,0.911,0.1081,-0.3422,-0.2733,0.899,0.1139,-0.3916,-0.2572,0.8834,0.1196,-0.4306,-0.2538,0.8661,0.1238,-0.4623,-0.2437,0.8526,0.125,-0.4893,-0.2465,0.8365,0.127,-0.5011,-0.2468,0.8295,0.1269,-0.5176,-0.2533,0.8173,0.1245,-0.5283,-0.2794,0.8018,0.1208,-0.5477,-0.2788,0.7889,0.1186,-0.5816,-0.2852,0.7618,0.1194,-0.6049,-0.2861,0.7431,0.1221,-0.6366,-0.2846,0.7168,0.1238,-0.6708,-0.2695,0.6909,0.125,-0.6985,-0.2675,0.6637,0.1272,-0.7207,-0.2705,0.6383,0.1282,-0.75,-0.2656,0.6058,0.1298,-0.7709,-0.2757,0.5742,0.1285])

Group366.addChildren(OrientationInterpolator382)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [2.218203,9.295252], [-5.744765,0.519277], [-5.795249,1.398932] degrees
#4.402057 -0.186171 0.790177, 4.478723 -0.156879 0.863166, 4.629217 -0.097192 0.858014, 4.703200 -0.066964 0.779875, 4.703200 -0.066964 0.779875, 4.662544 -0.143323 0.833202, 4.662544 -0.143323 0.833202, 4.588589 -0.173620 0.911243, 4.438109 -0.433936 0.838519, 4.363862 -0.664650 0.838554, 4.414059 -0.840527 0.736381, 4.339954 -0.995229 0.668329, 4.319120 -1.214313 0.585343, 4.334266 -1.359754 0.441576, 4.392553 -1.430067 0.395552, 4.525755 -1.504707 0.323657, 4.572873 -1.525474 0.201755, 4.682803 -1.606527 0.183530, 4.908304 -1.629847 0.155552, 4.988880 -1.836351 0.227820, 4.996583 -1.993829 0.354594, 5.133520 -2.152471 0.351046, 5.114036 -2.407550 0.361169, 5.052392 -2.736780 0.425251, 4.849618 -3.171196 0.563263, 4.434484 -3.521762 0.490232, 3.905134 -3.722769 0.585218, 3.354459 -3.559441 0.641505, 3.009123 -3.417158 0.848907, 2.828121 -3.308028 1.034619, 2.622634 -3.264796 1.026205, 2.612677 -3.327057 0.980406, 2.647847 -3.282472 0.982958, 2.743388 -3.262069 0.865142, 2.855068 -3.226981 0.738408, 2.945652 -3.078419 0.679441, 2.950887 -2.870348 0.569262, 2.874322 -2.595147 0.451221, 2.820196 -2.466802 0.316997, 2.794547 -2.257284 0.219549, 2.668799 -2.128093 0.129003, 2.439979 -2.120088 0.011523, 2.218203 -2.041799 0.026637, 2.282044 -1.909660 0.065231, 2.257226 -1.882756 0.087335, 2.353553 -1.880437 0.161370, 2.463776 -1.701009 0.255761, 2.498967 -1.551251 0.423088, 2.391425 -1.386788 0.634468, 2.348241 -1.260619 0.726233, 2.477405 -1.180052 0.684153, 2.427799 -1.251290 0.690339, 2.582294 -1.402518 0.669298, 2.912531 -1.573686 0.656071, 3.057584 -1.751684 0.623301, 3.329560 -1.767431 0.468958, 3.513710 -1.913962 0.352663, 3.691090 -2.064779 0.321091, 3.838665 -2.503850 0.237199, 4.057460 -2.882351 0.070797, 4.171732 -3.341086 -0.086294, 4.396468 -3.646924 -0.121208, 4.603673 -4.009476 -0.174863, 4.793758 -4.312085 -0.257014, 5.122385 -4.541892 -0.336029, 5.299591 -4.887645 -0.593202, 5.507306 -5.118281 -0.645519, 5.749367 -5.217555 -0.652918, 5.982884 -5.217809 -0.681968, 6.323870 -5.133309 -0.678476, 6.612999 -4.981400 -0.658060, 6.881445 -4.768289 -0.667058, 6.871167 -4.378755 -0.700042, 6.772778 -4.045362 -0.752499, 6.677915 -3.865822 -0.941610, 6.476491 -3.630388 -1.085051, 6.239554 -3.425707 -1.144981, 6.185827 -3.325063 -1.153787, 6.104430 -3.317146 -1.253989, 5.997278 -3.392029 -1.237197, 5.913113 -3.489936 -1.091211, 5.854334 -3.505438 -1.062992, 5.661108 -3.506752 -0.995556, 5.497770 -3.377229 -0.884617, 5.378716 -3.140320 -0.728068, 5.157421 -2.937123 -0.551346, 4.885974 -2.679604 -0.416292, 4.569622 -2.498065 -0.376399, 4.177638 -2.345068 -0.261277, 3.961977 -2.042051 -0.201002, 3.738576 -1.894365 -0.057973, 3.624170 -1.798378 0.042809, 3.495099 -1.697002 0.077933, 3.496558 -1.672023 0.198320, 3.515640 -1.422693 0.276569, 3.667777 -1.169140 0.371975, 3.765724 -1.016806 0.512581, 3.920341 -0.812769 0.573961, 4.030273 -0.510004 0.539783, 4.145746 -0.258177 0.624665, 4.201211 -0.057150 0.637865, 4.329480 0.175448 0.572664, 4.370716 0.350090 0.565730, 4.537511 0.429834 0.546687, 4.721831 0.489953 0.529886, 4.832225 0.519277 0.592507, 4.912196 0.499248 0.480834, 5.082906 0.354567 0.593511, 5.179077 0.330482 0.688141, 5.242682 0.181607 0.684424, 5.233088 0.001126 0.760357, 5.338518 -0.223579 0.934989, 5.462363 -0.547332 0.983271, 5.576736 -1.051315 1.108504, 5.483441 -1.520470 1.224878, 5.289041 -1.999123 1.143354, 5.135651 -2.416131 1.074881, 4.995796 -2.840353 1.061556, 5.033209 -3.120394 1.055494, 5.155205 -3.531426 0.970621, 5.371727 -4.035640 1.061469, 5.542555 -4.540000 0.992469, 5.662943 -4.971137 1.139785, 5.658018 -5.305999 1.217189, 5.488254 -5.541042 1.293880, 5.330250 -5.631423 1.345136, 5.342037 -5.563563 1.339422, 5.212753 -5.387269 1.285955, 5.176992 -5.341320 1.307355, 5.329654 -5.390109 1.378040, 5.478923 -5.404552 1.398802, 5.505744 -5.356523 1.398932, 5.602993 -5.355840 1.342947, 5.646310 -5.305116 1.241658, 5.595007 -5.058480 1.162838, 5.525700 -4.785227 1.109946, 5.550429 -4.513914 0.931911, 5.525831 -4.191284 0.711230, 5.474535 -3.744097 0.493140, 5.520125 -3.449616 0.237017, 5.657898 -3.149689 -0.094114, 5.522863 -3.057105 -0.452485, 5.438924 -3.014384 -0.769541, 5.255813 -3.034200 -1.234387, 5.054962 -2.979579 -1.663094, 4.918183 -3.045109 -2.089749, 4.889932 -3.130440 -2.393942, 4.779879 -3.147252 -2.709745, 4.792907 -3.098903 -2.936939, 4.847289 -3.082189 -3.119649, 4.972471 -3.069002 -3.293398, 5.096990 -3.231999 -3.407823, 5.372615 -3.449912 -3.581756, 5.714266 -3.663921 -3.677143, 6.109418 -3.820156 -3.766061, 6.531622 -3.925422 -3.816352, 7.075651 -4.018960 -3.888094, 7.625281 -4.232808 -3.861474, 8.117542 -4.320102 -3.834175, 8.526807 -4.426292 -3.879082, 8.877321 -4.571868 -3.848541, 8.950728 -4.802744 -3.787304, 8.993618 -4.916131 -3.610522, 8.915234 -4.863470 -3.550111, 8.867402 -4.897415 -3.457015, 8.623735 -4.784697 -3.403749, 8.338463 -4.744702 -3.287909, 8.093285 -4.635686 -3.233956, 7.796551 -4.477564 -3.219040, 7.464719 -4.321651 -3.054358, 7.177411 -4.257331 -2.951286, 6.771517 -4.174781 -2.968420, 6.455653 -4.087351 -2.997811, 6.132526 -3.981930 -2.941145, 5.934195 -3.900283 -2.858441, 5.668583 -3.753207 -2.877625, 5.489099 -3.668459 -2.850046, 5.392918 -3.439897 -2.715072, 5.247714 -3.225771 -2.642065, 5.271165 -3.027111 -2.544789, 5.309134 -2.898151 -2.480929, 5.346152 -2.768960 -2.416963, 5.436082 -2.466350 -2.378137, 5.441107 -2.209118 -2.314255, 5.643582 -2.090184 -2.231609, 5.896869 -2.018351 -2.109601, 6.182817 -2.110676 -1.996040, 6.433427 -2.166632 -1.866282, 6.691852 -2.387234 -1.795649, 6.959707 -2.537551 -1.641164, 7.196839 -2.559272 -1.487007, 7.415610 -2.724001 -1.305868, 7.412840 -2.751299 -1.152641, 7.263327 -2.956017 -0.934682, 7.121138 -3.185543 -0.863880, 6.921338 -3.413514 -0.862911, 6.777133 -3.688155 -0.817894, 6.615073 -3.895984 -0.743125, 6.458181 -4.073265 -0.803296, 6.333712 -4.276905 -0.738781, 6.193375 -4.521794 -0.600074, 5.995072 -4.618899 -0.460037, 5.786554 -4.450161 -0.449080, 5.679955 -4.252769 -0.552148, 5.346255 -4.084150 -0.695206, 5.220811 -3.932833 -0.746891, 5.301045 -3.824624 -0.847871, 5.505827 -3.733725 -0.981913, 5.865232 -3.690484 -1.050060, 6.099125 -3.553282 -1.104480, 6.333254 -3.416208 -1.158672, 6.449774 -3.284521 -1.326833, 6.702696 -3.245079 -1.353850, 6.874091 -3.134524 -1.549652, 7.028601 -3.059713 -1.766010, 7.079490 -2.888471 -1.900556, 7.131717 -2.717318 -2.035092, 7.168347 -2.422119 -2.269503, 7.137736 -2.077061 -2.445766, 7.036667 -1.829638 -2.638465, 7.216371 -1.581371 -2.828041, 7.315426 -1.420081 -3.106580, 7.331500 -1.487704 -3.380696, 7.445872 -1.660243 -3.734898, 7.485161 -1.858811 -4.007570, 7.592699 -2.099391 -4.293893, 7.738723 -2.384583 -4.394373, 7.878698 -2.777434 -4.450738, 7.963329 -3.176705 -4.414506, 8.107144 -3.464062 -4.423725, 8.249045 -3.690606 -4.496744, 8.236495 -3.865059 -4.660498, 8.378910 -4.070444 -4.900025, 8.582920 -4.333920 -5.193913, 8.690132 -4.456332 -5.462017, 8.896700 -4.587132 -5.675740, 8.950214 -4.511830 -5.751550, 9.138797 -4.474470 -5.795249, 9.295252 -4.176188 -5.711937, 9.292179 -3.711156 -5.510511, 9.146390 -3.311964 -5.299591, 9.025323 -3.059313 -4.985888, 8.810046 -2.978467 -4.886987, 8.720442 -2.794694 -4.718201, 8.495645 -2.489004 -4.595787, 8.312654 -2.111255 -4.534008, 8.157905 -1.819558 -4.443178, 8.082167 -1.528365 -4.206567, 7.852209 -1.431674 -3.919532, 7.634152 -1.406958 -3.667405, 7.360437 -1.488465 -3.448609, 7.126264 -1.564124 -3.231678, 6.857116 -1.752551 -3.152920, 6.665640 -1.736408 -3.090013, 6.503744 -1.804815 -2.999997, 6.135383 -1.906622 -2.931878, 5.977570 -1.948863 -2.899751, 5.709022 -2.015229 -2.755878, 5.597874 -1.980319 -2.604991, 5.405196 -1.971581 -2.527001, 5.275399 -1.917414 -2.376544, 5.267339 -1.811810 -2.241513, 5.157399 -1.459494 -2.111982, 5.096413 -1.261243 -1.988797, 5.106020 -1.036104 -1.944117, 5.106460 -1.011206 -1.978775, 5.272214 -1.166571 -1.853562, 5.440166 -1.466968 -1.805965, 5.615829 -1.876326 -1.731301, 5.834872 -2.320533 -1.666905, 6.014890 -2.770764 -1.618493, 6.102346 -3.145177 -1.635248, 6.063274 -3.398108 -1.568036, 6.040443 -3.649932 -1.604125, 5.979887 -3.729775 -1.601091, 5.779100 -3.777425 -1.618032, 5.492800 -3.742582 -1.756076, 5.306452 -3.804505 -1.720576, 5.152643 -4.062173 -1.770902, 5.132722 -4.315338 -1.810155, 5.012444 -4.596441 -1.819182, 4.879487 -4.882478 -1.724971, 4.761608 -5.165064 -1.736394, 4.607664 -5.366444 -1.772395, 4.420866 -5.646972 -1.759458, 4.140108 -5.744765 -1.824507
#Interpolator12_LeftCollar channels [36..38] sends animation values to BVH JOINT LeftCollar, DEF Bvh1_LeftCollar, <HAnimJoint name=LeftCollar/>
OrientationInterpolator383 = OrientationInterpolator()
OrientationInterpolator383.setDEF("Interpolator12_LeftCollar")
OrientationInterpolator383.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator383.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0])

Group366.addChildren(OrientationInterpolator383)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-1.0E-6,4.9E-324], [-2.0E-6,1.0E-6], [-6.0E-6,4.0E-6] degrees
#-0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000004, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000003, -0.000000 0.000000 0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000000 -0.000005, -0.000001 0.000000 -0.000003, -0.000001 0.000000 -0.000000, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 -0.000002, -0.000001 -0.000000 0.000003, -0.000000 0.000001 -0.000005, -0.000000 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000001, -0.000000 0.000000 0.000003, -0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000000, -0.000000 -0.000000 -0.000004, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000000 0.000003, -0.000001 0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000005, -0.000000 0.000001 -0.000003, -0.000001 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000000 -0.000001 -0.000000, -0.000001 0.000001 -0.000002, -0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000001 0.000000 0.000000, 0.000000 0.000001 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000004, -0.000000 0.000000 0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000000, -0.000000 0.000000 -0.000006, -0.000001 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 0.000000 0.000002, -0.000001 0.000000 -0.000003, 0.000000 -0.000000 -0.000002, -0.000000 -0.000000 0.000002, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000000 0.000000 -0.000002, 0.000000 -0.000000 -0.000002, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 0.000001 -0.000002, -0.000001 -0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000001 0.000000 -0.000004, -0.000000 0.000000 -0.000004, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 -0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000002, -0.000000 0.000001 -0.000003, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 0.000000, 0.000000 0.000001 -0.000003, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000001, -0.000001 0.000000 -0.000000, -0.000000 0.000000 -0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, 0.000000 -0.000000 -0.000004, 0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000002, -0.000000 0.000000 -0.000005, 0.000000 -0.000001 0.000002, 0.000000 0.000001 -0.000003, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000001 0.000001 -0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000001, 0.000000 0.000001 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 0.000003, -0.000001 -0.000000 0.000001, 0.000000 -0.000001 -0.000004, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, 0.000000 0.000000 -0.000002, -0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 0.000001 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000001 -0.000001, -0.000001 0.000000 -0.000000, 0.000000 -0.000002 -0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000001 -0.000000 -0.000004, -0.000000 -0.000001 -0.000003, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000000 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000004, -0.000001 0.000000 -0.000001, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000001 -0.000004, 0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 -0.000001 -0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000004, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 0.000001, -0.000001 -0.000002 0.000001, -0.000000 0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000004, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000000 -0.000001 0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000002, 0.000000 -0.000001 -0.000003, 0.000000 -0.000000 0.000001, -0.000001 0.000000 0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 -0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000004, -0.000000 -0.000000 0.000001, -0.000001 0.000000 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000001 -0.000001, 0.000000 0.000000 -0.000001, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000000 -0.000001 -0.000000, -0.000000 -0.000001 0.000003, -0.000001 -0.000001 0.000003, -0.000001 -0.000001 -0.000001, 0.000000 -0.000001 -0.000000, -0.000000 0.000001 -0.000001, -0.000000 0.000000 -0.000001, -0.000001 0.000000 0.000004, -0.000001 0.000001 -0.000001, 0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000001 -0.000002 -0.000003, -0.000000 0.000001 -0.000001, -0.000001 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000001 -0.000003, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000002, 0.000000 -0.000001 -0.000002, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 -0.000001 0.000004, -0.000000 -0.000002 -0.000000, 0.000000 0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000000 -0.000001 -0.000000, -0.000000 0.000000 0.000002, 0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 0.000001 0.000001, 0.000000 -0.000001 -0.000003, 0.000000 0.000001 -0.000002
#Interpolator13_l_shoulder channels [39..41] sends animation values to BVH JOINT LeftShoulder, DEF Bvh1_l_shoulder, <HAnimJoint name=l_shoulder/>
OrientationInterpolator384 = OrientationInterpolator()
OrientationInterpolator384.setDEF("Interpolator13_l_shoulder")
OrientationInterpolator384.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator384.setKeyValue([0.1439,-0.9533,-0.2656,0.2132,0.141,-0.9546,-0.2625,0.215,0.1397,-0.9515,-0.2739,0.2197,0.1429,-0.951,-0.2742,0.2232,0.1419,-0.9527,-0.2687,0.2291,0.1472,-0.9536,-0.2625,0.2336,0.1525,-0.9529,-0.2622,0.235,0.1599,-0.9535,-0.2555,0.2375,0.1815,-0.9528,-0.2435,0.2395,0.2046,-0.9489,-0.2404,0.2415,0.2175,-0.9445,-0.2462,0.2414,0.2304,-0.9428,-0.2408,0.2421,0.2397,-0.9409,-0.2394,0.2433,0.2487,-0.9376,-0.243,0.2417,0.2536,-0.9372,-0.2393,0.2423,0.267,-0.933,-0.2412,0.2414,0.2706,-0.9317,-0.2425,0.2415,0.2758,-0.9302,-0.2424,0.24,0.264,-0.934,-0.2408,0.2397,0.2618,-0.9367,-0.2325,0.2366,0.2594,-0.9395,-0.2239,0.2337,0.2635,-0.9383,-0.224,0.2294,0.2799,-0.9365,-0.2111,0.2219,0.2972,-0.9342,-0.1971,0.2146,0.3246,-0.9292,-0.1769,0.2077,0.3505,-0.9254,-0.1443,0.1999,0.365,-0.9263,-0.0936,0.1941,0.3704,-0.9282,-0.0359,0.1891,0.3684,-0.9296,0.0116,0.1864,0.3717,-0.9275,0.0392,0.185,0.3712,-0.9263,0.0641,0.1821,0.3682,-0.9268,0.0741,0.1802,0.3509,-0.9334,0.0746,0.1809,0.3325,-0.9411,0.0616,0.1851,0.3142,-0.9474,0.0613,0.1933,0.2992,-0.9527,0.0541,0.2025,0.2786,-0.9588,0.0557,0.2118,0.2636,-0.9626,0.0621,0.2204,0.2606,-0.9622,0.079,0.2294,0.262,-0.9602,0.0967,0.2358,0.2634,-0.9588,0.1065,0.2407,0.2615,-0.9574,0.1226,0.2416,0.2622,-0.9554,0.136,0.2426,0.2597,-0.9557,0.1387,0.2395,0.2661,-0.953,0.145,0.2321,0.2699,-0.9517,0.1466,0.2247,0.2665,-0.9536,0.1398,0.2166,0.264,-0.9547,0.1375,0.2101,0.2627,-0.9554,0.1348,0.2063,0.2206,-0.9661,0.1343,0.2004,0.1724,-0.9784,0.114,0.1958,0.1278,-0.9865,0.1023,0.1949,0.0909,-0.9924,0.0825,0.1958,0.0871,-0.9946,0.057,0.1997,0.084,-0.9957,0.0379,0.2061,0.0629,-0.9979,0.0127,0.2115,0.0538,-0.9985,-0.0079,0.2169,0.0542,-0.9982,-0.0276,0.2225,0.065,-0.9966,-0.0511,0.2267,0.0811,-0.994,-0.0741,0.2312,0.0939,-0.9912,-0.0933,0.2352,0.0943,-0.9881,-0.1212,0.2413,0.1015,-0.9842,-0.1452,0.2453,0.1036,-0.981,-0.1639,0.2488,0.1111,-0.9753,-0.1908,0.2498,0.1167,-0.9708,-0.2094,0.2461,0.1174,-0.967,-0.2261,0.2428,0.1123,-0.9624,-0.2473,0.2385,0.108,-0.9563,-0.2717,0.2318,0.107,-0.9488,-0.2972,0.2247,0.1119,-0.9391,-0.325,0.2177,0.1107,-0.9303,-0.3498,0.2155,0.103,-0.9316,-0.3486,0.2177,0.0929,-0.939,-0.331,0.2241,0.0797,-0.9437,-0.321,0.2371,0.0651,-0.9506,-0.3034,0.2504,0.0446,-0.9573,-0.2856,0.2617,0.0277,-0.9614,-0.2736,0.2726,0.0127,-0.9639,-0.2658,0.28,-0.0039,-0.9659,-0.2588,0.2852,-0.0214,-0.9663,-0.2565,0.2874,-0.0403,-0.9666,-0.2532,0.2859,-0.0605,-0.9662,-0.2507,0.2829,-0.0786,-0.966,-0.2464,0.2786,-0.1056,-0.9645,-0.2422,0.2776,-0.129,-0.9632,-0.2358,0.2763,-0.1467,-0.9623,-0.2292,0.2778,-0.1635,-0.9605,-0.2253,0.2795,-0.1705,-0.9624,-0.2113,0.2836,-0.1801,-0.9626,-0.2025,0.2868,-0.1815,-0.9638,-0.1953,0.2886,-0.1791,-0.9652,-0.1905,0.2897,-0.1822,-0.9649,-0.1891,0.2872,-0.1816,-0.9648,-0.19,0.284,-0.1854,-0.9631,-0.1949,0.2832,-0.1859,-0.9622,-0.1989,0.2806,-0.1852,-0.9621,-0.2,0.2774,-0.184,-0.9615,-0.2039,0.2744,-0.1832,-0.9615,-0.2047,0.2702,-0.1749,-0.9634,-0.203,0.2664,-0.1701,-0.9645,-0.202,0.2643,-0.1624,-0.9648,-0.2069,0.2622,-0.1505,-0.9653,-0.2134,0.2607,-0.1373,-0.9656,-0.2208,0.2569,-0.1317,-0.9639,-0.2315,0.2538,-0.1245,-0.9638,-0.2357,0.2491,-0.117,-0.9637,-0.2401,0.2443,-0.1098,-0.9617,-0.2513,0.2411,-0.1054,-0.9586,-0.2647,0.2387,-0.093,-0.9567,-0.2759,0.234,-0.0813,-0.9548,-0.2859,0.2294,-0.0688,-0.9501,-0.3042,0.2265,-0.0605,-0.9428,-0.3278,0.2228,-0.0458,-0.9347,-0.3526,0.2214,-0.0297,-0.9303,-0.3657,0.2218,-0.0117,-0.924,-0.3823,0.2204,0.0067,-0.9197,-0.3925,0.2183,0.0308,-0.9176,-0.3964,0.2181,0.0595,-0.9094,-0.4117,0.218,0.0812,-0.9028,-0.4223,0.2162,0.1055,-0.8945,-0.4344,0.2175,0.1284,-0.8914,-0.4347,0.2166,0.1419,-0.8928,-0.4275,0.2204,0.1358,-0.9012,-0.4117,0.2245,0.1195,-0.9186,-0.3768,0.2299,0.0933,-0.9355,-0.3408,0.2346,0.0602,-0.95,-0.3064,0.2406,0.0197,-0.9614,-0.2743,0.2443,-0.0133,-0.9685,-0.2488,0.2467,-0.0384,-0.9712,-0.235,0.2495,-0.0713,-0.9719,-0.2242,0.251,-0.0979,-0.9713,-0.2167,0.2551,-0.1235,-0.97,-0.2093,0.2594,-0.1413,-0.9702,-0.1969,0.2653,-0.1596,-0.9699,-0.1838,0.2706,-0.1664,-0.9717,-0.1674,0.2827,-0.1653,-0.9734,-0.1589,0.293,-0.1608,-0.9756,-0.1496,0.3017,-0.1553,-0.9772,-0.1445,0.3103,-0.141,-0.9806,-0.1363,0.3197,-0.1301,-0.9826,-0.1326,0.3252,-0.1136,-0.9855,-0.1264,0.3277,-0.1017,-0.9881,-0.1151,0.3298,-0.0995,-0.9895,-0.1044,0.3335,-0.1039,-0.9901,-0.094,0.3395,-0.1159,-0.9893,-0.0884,0.3471,-0.1375,-0.9868,-0.085,0.3553,-0.1591,-0.9839,-0.0814,0.3626,-0.1867,-0.9791,-0.0809,0.3681,-0.218,-0.9727,-0.0799,0.3729,-0.2517,-0.964,-0.0856,0.3782,-0.2765,-0.9568,-0.09,0.3824,-0.3004,-0.9488,-0.0972,0.3872,-0.3288,-0.9383,-0.1076,0.3897,-0.358,-0.9264,-0.1169,0.3914,-0.3918,-0.9111,-0.1277,0.3872,-0.4242,-0.8936,-0.1467,0.3804,-0.4519,-0.8772,-0.1623,0.3751,-0.4719,-0.8644,-0.1736,0.3726,-0.4788,-0.8592,-0.1806,0.3723,-0.4717,-0.8618,-0.1867,0.3713,-0.459,-0.8688,-0.1857,0.3712,-0.4447,-0.878,-0.1769,0.3684,-0.432,-0.8854,-0.1718,0.3633,-0.4171,-0.8938,-0.1646,0.3555,-0.4016,-0.9027,-0.1546,0.3487,-0.3775,-0.9135,-0.1515,0.3446,-0.3526,-0.924,-0.1483,0.3406,-0.3208,-0.9353,-0.1493,0.3375,-0.293,-0.9452,-0.1442,0.3358,-0.2586,-0.9551,-0.1447,0.3323,-0.227,-0.9638,-0.1398,0.3284,-0.1952,-0.9696,-0.1477,0.3241,-0.1624,-0.9745,-0.1546,0.3215,-0.1288,-0.9782,-0.1626,0.3178,-0.0969,-0.9809,-0.1684,0.3107,-0.0619,-0.9805,-0.1863,0.3027,-0.0236,-0.9776,-0.209,0.2953,0.0059,-0.9738,-0.2274,0.2892,0.0404,-0.9653,-0.258,0.2832,0.0852,-0.953,-0.2906,0.276,0.1365,-0.9363,-0.3237,0.2713,0.1886,-0.9149,-0.3568,0.2676,0.2367,-0.8897,-0.3903,0.2636,0.2872,-0.8556,-0.4306,0.2609,0.3395,-0.8146,-0.4703,0.257,0.3889,-0.7688,-0.5077,0.2553,0.4321,-0.7221,-0.5402,0.2538,0.4741,-0.6708,-0.5704,0.2515,0.5025,-0.6327,-0.5892,0.2522,0.5233,-0.5974,-0.6076,0.2541,0.5414,-0.5689,-0.619,0.2563,0.5621,-0.5424,-0.6245,0.2587,0.5829,-0.5196,-0.6247,0.2642,0.6005,-0.495,-0.628,0.2677,0.6176,-0.4622,-0.6364,0.2683,0.6343,-0.4316,-0.6415,0.2682,0.6433,-0.4103,-0.6464,0.2658,0.6496,-0.3907,-0.6523,0.2616,0.6525,-0.3791,-0.6561,0.2572,0.6458,-0.3831,-0.6604,0.2547,0.6271,-0.4082,-0.6634,0.2516,0.599,-0.4576,-0.6571,0.2503,0.5602,-0.5231,-0.6423,0.25,0.5137,-0.6064,-0.607,0.2493,0.4442,-0.69,-0.5715,0.2525,0.3671,-0.7621,-0.5333,0.2566,0.296,-0.8159,-0.4968,0.2593,0.2239,-0.8584,-0.4616,0.2632,0.155,-0.8918,-0.425,0.2638,0.0903,-0.9159,-0.3911,0.2645,0.03,-0.9323,-0.3605,0.2623,-0.0196,-0.9442,-0.3289,0.2611,-0.0696,-0.9527,-0.296,0.2609,-0.1111,-0.9592,-0.2599,0.2602,-0.1478,-0.9636,-0.2226,0.2614,-0.1765,-0.9676,-0.1804,0.2648,-0.2087,-0.967,-0.146,0.27,-0.2393,-0.9644,-0.1128,0.2758,-0.2609,-0.9611,-0.0903,0.2838,-0.2784,-0.9573,-0.0786,0.2906,-0.2917,-0.9535,-0.0754,0.2969,-0.2883,-0.9539,-0.0836,0.3035,-0.2849,-0.9526,-0.1064,0.3064,-0.2799,-0.9517,-0.1259,0.31,-0.2743,-0.9491,-0.1547,0.3118,-0.2588,-0.9483,-0.1835,0.3137,-0.2414,-0.9454,-0.2188,0.3128,-0.2236,-0.9418,-0.251,0.3113,-0.2098,-0.9367,-0.2805,0.3099,-0.1905,-0.9306,-0.3124,0.3083,-0.161,-0.9271,-0.3386,0.3094,-0.1308,-0.9235,-0.3606,0.3136,-0.0999,-0.9175,-0.3849,0.3183,-0.0753,-0.9108,-0.4059,0.3202,-0.0533,-0.8988,-0.4351,0.3215,-0.0298,-0.885,-0.4646,0.3175,-0.0036,-0.8645,-0.5026,0.3112,0.0193,-0.8486,-0.5286,0.306,0.0434,-0.8355,-0.5478,0.3007,0.074,-0.8307,-0.5518,0.2998,0.1053,-0.827,-0.5522,0.3016,0.1269,-0.8296,-0.5438,0.3041,0.1523,-0.8334,-0.5313,0.306,0.1767,-0.8373,-0.5174,0.3037,0.1934,-0.8408,-0.5057,0.2987,0.2153,-0.8387,-0.5003,0.2921,0.2323,-0.8334,-0.5014,0.2834,0.2501,-0.8275,-0.5026,0.2748,0.2607,-0.8272,-0.4978,0.268,0.2688,-0.8265,-0.4946,0.2618,0.272,-0.8291,-0.4885,0.2589,0.2834,-0.8296,-0.481,0.2556,0.2906,-0.8336,-0.4696,0.2544,0.2938,-0.8372,-0.4613,0.2549,0.2916,-0.8451,-0.448,0.2525,0.2849,-0.8474,-0.4481,0.2515,0.2788,-0.8523,-0.4425,0.2505,0.2656,-0.8538,-0.4477,0.2477,0.2559,-0.8553,-0.4505,0.2434,0.2402,-0.8613,-0.4477,0.2404,0.2272,-0.8658,-0.4458,0.2401,0.2016,-0.8764,-0.4374,0.2408,0.1873,-0.8799,-0.4368,0.2428,0.1647,-0.8815,-0.4424,0.2455,0.152,-0.8792,-0.4516,0.249,0.1493,-0.8727,-0.4648,0.2516,0.1519,-0.8633,-0.4813,0.2514,0.1611,-0.8574,-0.4888,0.2477,0.1706,-0.8449,-0.507,0.2436,0.1868,-0.8384,-0.5121,0.2392,0.2025,-0.8279,-0.523,0.235,0.2072,-0.8274,-0.522,0.2323,0.212,-0.8268,-0.521,0.2296,0.1989,-0.8299,-0.5213,0.2292,0.1903,-0.8365,-0.5139,0.2291,0.1825,-0.8444,-0.5037,0.2305,0.1744,-0.8511,-0.4953,0.2314,0.1766,-0.8487,-0.4985,0.2314,0.1811,-0.8485,-0.4972,0.2287,0.1745,-0.8495,-0.4979,0.2251,0.1745,-0.849,-0.4987,0.2202,0.1802,-0.8481,-0.4983,0.2167,0.1745,-0.8544,-0.4894,0.2137,0.1686,-0.8653,-0.4721,0.2136,0.1541,-0.8845,-0.4403,0.2143])

Group366.addChildren(OrientationInterpolator384)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-9.387506,2.305873], [-9.412142,10.268742], [-21.255741,4.9E-324] degrees
#-3.044958 2.073855 -11.594578, -3.034865 2.054907 -11.710495, -3.241454 2.104472 -11.923323, -3.288924 2.183270 -12.103689, -3.298266 2.229691 -12.444087, -3.267601 2.341883 -12.701078, -3.274577 2.428410 -12.766608, -3.203674 2.548425 -12.908639, -3.031522 2.848173 -13.005631, -2.977609 3.184350 -13.051184, -3.037540 3.367566 -12.979206, -2.952636 3.547034 -12.995814, -2.930911 3.691416 -13.027780, -2.951313 3.792785 -12.893161, -2.899162 3.865137 -12.921764, -2.899467 4.035412 -12.812999, -2.912050 4.086954 -12.796653, -2.887900 4.128922 -12.692170, -2.879447 3.962058 -12.732851, -2.738386 3.866985 -12.615643, -2.597700 3.770831 -12.497939, -2.553573 3.751033 -12.255336, -2.299378 3.811129 -11.839067, -2.045170 3.871180 -11.423052, -1.722959 4.040985 -11.003507, -1.275263 4.142782 -10.556090, -0.672923 4.130442 -10.281590, -0.035877 4.026489 -10.057885, 0.464645 3.904207 -9.948834, 0.751247 3.884190 -9.858994, 0.992885 3.797625 -9.700407, 1.080012 3.720547 -9.610147, 1.077539 3.554980 -9.713577, 0.958262 3.452191 -10.013822, 0.993874 3.398245 -10.526814, 0.959401 3.390013 -11.087187, 1.014387 3.290275 -11.670405, 1.131263 3.221537 -12.193494, 1.407624 3.282308 -12.690172, 1.695965 3.361434 -13.027176, 1.874681 3.430093 -13.282827, 2.102483 3.392086 -13.322164, 2.296537 3.392012 -13.351357, 2.295662 3.314781 -13.183971, 2.305873 3.296190 -12.746310, 2.244937 3.246313 -12.317895, 2.064892 3.104784 -11.894423, 1.964205 2.990759 -11.547964, 1.888998 2.928120 -11.343236, 1.777853 2.367349 -11.131145, 1.456911 1.800665 -11.002416, 1.272597 1.309327 -11.032833, 1.018241 0.923514 -11.142959, 0.746404 0.925537 -11.384513, 0.545372 0.938922 -11.764384, 0.233371 0.740976 -12.096395, -0.025197 0.674090 -12.408784, -0.272469 0.724002 -12.724458, -0.562685 0.911360 -12.940438, -0.849568 1.176776 -13.157176, -1.099117 1.400172 -13.343926, -1.505434 1.490325 -13.641071, -1.850734 1.657252 -13.809486, -2.134161 1.745484 -13.953410, -2.512011 1.904995 -13.921693, -2.729796 1.979981 -13.645653, -2.927417 1.985130 -13.407908, -3.175800 1.906740 -13.103116, -3.421330 1.819728 -12.649565, -3.652028 1.773151 -12.165737, -3.884034 1.797017 -11.657226, -4.155064 1.787419 -11.427326, -4.189151 1.713662 -11.562064, -4.094838 1.628316 -12.004236, -4.204506 1.558453 -12.770753, -4.202672 1.440001 -13.593976, -4.155036 1.194428 -14.319252, -4.169705 0.984530 -14.989929, -4.185528 0.773067 -15.442711, -4.184811 0.515612 -15.773163, -4.217707 0.235111 -15.911489, -4.184987 -0.082117 -15.841219, -4.147254 -0.415632 -15.683357, -4.053545 -0.713122 -15.451437, -4.030497 -1.146008 -15.386662, -3.959105 -1.523133 -15.306087, -3.915753 -1.820912 -15.383133, -3.916800 -2.104247 -15.460607, -3.769369 -2.267716 -15.720489, -3.692990 -2.463622 -15.903625, -3.605469 -2.514154 -16.023909, -3.536959 -2.493915 -16.106842, -3.487656 -2.530164 -15.962946, -3.458153 -2.495108 -15.782564, -3.532727 -2.540983 -15.712835, -3.562775 -2.522129 -15.557800, -3.534289 -2.486169 -15.378162, -3.550485 -2.437078 -15.198223, -3.503273 -2.392961 -14.968110, -3.406770 -2.242889 -14.779643, -3.354129 -2.158494 -14.676541, -3.383672 -2.021441 -14.562230, -3.436462 -1.824519 -14.476516, -3.467610 -1.597682 -14.268381, -3.567390 -1.484751 -14.070638, -3.544492 -1.356080 -13.800237, -3.522333 -1.227171 -13.530066, -3.616445 -1.102360 -13.325771, -3.753788 -1.015640 -13.149265, -3.808070 -0.823512 -12.860054, -3.844555 -0.650188 -12.576937, -4.012863 -0.462107 -12.352064, -4.235071 -0.328816 -12.054316, -4.500610 -0.115342 -11.866139, -4.652457 0.103163 -11.822692, -4.809642 0.342403 -11.659942, -4.866854 0.574250 -11.484165, -4.882844 0.875147 -11.437001, -5.035021 1.245404 -11.309993, -5.099963 1.505728 -11.122296, -5.252772 1.829173 -11.071297, -5.209503 2.100334 -10.973913, -5.190055 2.306407 -11.178873, -5.085031 2.265442 -11.499004, -4.762163 2.082603 -12.021273, -4.409181 1.742790 -12.515231, -4.093843 1.302309 -13.056742, -3.773586 0.721607 -13.441149, -3.504803 0.231679 -13.685265, -3.392759 -0.137938 -13.892022, -3.316873 -0.623760 -13.997720, -3.310924 -1.024869 -14.228924, -3.307656 -1.425849 -14.460252, -3.236046 -1.739447 -14.801023, -3.141050 -2.073414 -15.100701, -3.047803 -2.291173 -15.808543, -3.026188 -2.358311 -16.410795, -2.955800 -2.361053 -16.929569, -2.947878 -2.330798 -17.440506, -2.859209 -2.151447 -18.022627, -2.814138 -1.991106 -18.364861, -2.674809 -1.714573 -18.546370, -2.446549 -1.535760 -18.707869, -2.271093 -1.540204 -18.941063, -2.132188 -1.677517 -19.296432, -2.115988 -1.959916 -19.712883, -2.182925 -2.440749 -20.142923, -2.241583 -2.936510 -20.508316, -2.373594 -3.548272 -20.729713, -2.509871 -4.249084 -20.885994, -2.806214 -4.997395 -21.031887, -3.034326 -5.564407 -21.133289, -3.333303 -6.119946 -21.255741, -3.694474 -6.739315 -21.198273, -4.030061 -7.377348 -21.072388, -4.322578 -8.010102 -20.558661, -4.730327 -8.519249 -19.877848, -5.055167 -8.956087 -19.301590, -5.301996 -9.293395 -18.939430, -5.460378 -9.412142 -18.832911, -5.549767 -9.218116 -18.835825, -5.490839 -8.947426 -18.960333, -5.216247 -8.610525 -18.973219, -4.984900 -8.254458 -18.831274, -4.667513 -7.815197 -18.565203, -4.316731 -7.401927 -18.350285, -4.126024 -6.856118 -18.312523, -3.938340 -6.309916 -18.274521, -3.823502 -5.643348 -18.294920, -3.625784 -5.103850 -18.367519, -3.491300 -4.405032 -18.335850, -3.261996 -3.784894 -18.255047, -3.265533 -3.134979 -18.101357, -3.268107 -2.498721 -18.032606, -3.276966 -1.849833 -17.874018, -3.213025 -1.245051 -17.504210, -3.342927 -0.580858 -17.029602, -3.544692 0.113628 -16.540846, -3.705549 0.622723 -16.120468, -4.045189 1.214400 -15.626913, -4.368543 1.931272 -15.008426, -4.712505 2.731411 -14.449440, -5.069759 3.525449 -13.885185, -5.432257 4.224469 -13.252036, -5.919944 4.965570 -12.551833, -6.373174 5.674312 -11.700415, -6.850924 6.365691 -10.890823, -7.271768 6.949390 -10.086547, -7.647027 7.470294 -9.193872, -7.947875 7.884908 -8.621955, -8.289232 8.232164 -8.129413, -8.541259 8.554208 -7.745832, -8.711765 8.921842 -7.391368, -8.901354 9.410193 -7.165750, -9.080611 9.781924 -6.847609, -9.260572 10.032321 -6.323062, -9.368829 10.251036 -5.821846, -9.387506 10.268742 -5.433249, -9.357605 10.174235 -5.048729, -9.277029 10.028883 -4.796269, -9.254098 9.840482 -4.819190, -9.163494 9.475294 -5.148085, -8.986751 9.076620 -5.875787, -8.713162 8.571762 -6.866428, -8.133613 7.938206 -8.123498, -7.704853 7.092192 -9.532252, -7.289905 6.111494 -10.838983, -6.878291 5.130288 -11.833037, -6.532898 4.123590 -12.729178, -6.094930 3.067343 -13.331042, -5.706879 2.067441 -13.792476, -5.309616 1.104420 -13.970418, -4.906435 0.312517 -14.120933, -4.507226 -0.481739 -14.265531, -4.040748 -1.157403 -14.344855, -3.576717 -1.771337 -14.492719, -3.050090 -2.299023 -14.746712, -2.655045 -2.898245 -15.033571, -2.265627 -3.500641 -15.317142, -2.028528 -3.989343 -15.707569, -1.936526 -4.393927 -16.023539, -1.969158 -4.714924 -16.314053, -2.159360 -4.733823 -16.688417, -2.572454 -4.658047 -16.841946, -2.939093 -4.570482 -17.034208, -3.450158 -4.419283 -17.101330, -3.943962 -4.092371 -17.200796, -4.506532 -3.684474 -17.103901, -4.999256 -3.275378 -16.955956, -5.451652 -2.949992 -16.786236, -5.926335 -2.527813 -16.585445, -6.330361 -1.954969 -16.563194, -6.727497 -1.380915 -16.692297, -7.185153 -0.774645 -16.805960, -7.541569 -0.280458 -16.754862, -8.044259 0.183711 -16.571295, -8.418431 0.644117 -16.082649, -8.863223 1.132443 -15.359181, -9.122657 1.527717 -14.789063, -9.250097 1.913360 -14.273238, -9.227627 2.424386 -14.104543, -9.224277 2.974536 -14.083397, -9.106703 3.365515 -14.221620, -8.887671 3.810462 -14.351173, -8.532238 4.167579 -14.294529, -8.165396 4.343503 -14.112166, -7.864990 4.575883 -13.750803, -7.639065 4.682081 -13.248361, -7.416630 4.788873 -12.744734, -7.155435 4.803731 -12.426048, -6.941824 4.789548 -12.130846, -6.774914 4.769210 -12.037991, -6.567299 4.853852 -11.890024, -6.361548 4.918823 -11.897600, -6.244677 4.966275 -11.977062, -5.997178 4.867736 -11.988696, -5.984957 4.751479 -11.977785, -5.889725 4.639770 -12.012531, -5.921333 4.403740 -11.906936, -5.877171 4.188404 -11.728953, -5.789853 3.915028 -11.679750, -5.773612 3.733564 -11.737062, -5.702929 3.389049 -11.933737, -5.758724 3.227769 -12.092546, -5.929702 2.964466 -12.259266, -6.159350 2.848577 -12.402455, -6.415570 2.862462 -12.434653, -6.646872 2.913961 -12.280888, -6.647454 2.996428 -12.009553, -6.787520 3.083948 -11.625485, -6.722947 3.238304 -11.317805, -6.740069 3.385339 -10.962743, -6.648649 3.399617 -10.829926, -6.557105 3.414344 -10.697407, -6.562384 3.237964 -10.725780, -6.471952 3.121385 -10.817434, -6.380458 3.034398 -10.994202, -6.302236 2.937070 -11.136127, -6.342291 2.967563 -11.100213, -6.249361 2.983246 -10.968664, -6.171173 2.843913 -10.813951, -6.054072 2.770585 -10.575155, -5.951966 2.786934 -10.396441, -5.768618 2.666011 -10.338457, -5.557788 2.579636 -10.473218, -5.196756 2.388356 -10.759043
#Interpolator14_l_elbow channels [42..44] sends animation values to BVH JOINT LeftElbow, DEF Bvh1_l_elbow, <HAnimJoint name=l_elbow/>
OrientationInterpolator385 = OrientationInterpolator()
OrientationInterpolator385.setDEF("Interpolator14_l_elbow")
OrientationInterpolator385.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator385.setKeyValue([-0.0235,0.9634,-0.2669,0.2821,-0.0134,0.9602,-0.2791,0.2842,-0.0094,0.9608,-0.2772,0.2868,-0.0118,0.9609,-0.2767,0.2928,-0.0097,0.9603,-0.2789,0.2996,-0.0068,0.9589,-0.2838,0.3051,-0.0074,0.9587,-0.2843,0.3081,-0.007,0.9569,-0.2905,0.31,-0.0076,0.9538,-0.3002,0.3133,-0.0116,0.9527,-0.3038,0.3147,-0.0127,0.9512,-0.3082,0.3168,-0.017,0.9503,-0.3108,0.3199,-0.017,0.9497,-0.3128,0.3234,-0.0199,0.9472,-0.32,0.3243,-0.0175,0.9457,-0.3245,0.3268,-0.0199,0.9434,-0.3311,0.3263,-0.0146,0.9455,-0.3252,0.327,-0.0123,0.9458,-0.3246,0.3252,-0.0058,0.9479,-0.3185,0.3263,-0.0003,0.9512,-0.3086,0.3251,0.0007,0.9542,-0.2991,0.324,0.0009,0.9605,-0.2784,0.3236,-0.0077,0.9649,-0.2625,0.3215,-0.02,0.9675,-0.2521,0.3183,-0.0331,0.9703,-0.2398,0.3165,-0.0509,0.9713,-0.2322,0.3139,-0.0594,0.9699,-0.236,0.3119,-0.0616,0.9679,-0.2438,0.312,-0.0525,0.9623,-0.2669,0.3121,-0.0411,0.9572,-0.2866,0.3132,-0.0205,0.9504,-0.3102,0.3168,0.0086,0.9428,-0.3333,0.3222,0.0319,0.9331,-0.3582,0.3312,0.0502,0.926,-0.3743,0.342,0.0556,0.9179,-0.393,0.3536,0.0598,0.9096,-0.4112,0.3621,0.0626,0.9026,-0.4259,0.3663,0.0641,0.8962,-0.439,0.3676,0.0591,0.8925,-0.4472,0.3676,0.0479,0.8896,-0.4543,0.3652,0.0361,0.8917,-0.4512,0.362,0.0287,0.8953,-0.4445,0.357,0.0165,0.9015,-0.4326,0.354,0.0085,0.9113,-0.4117,0.3493,-0.0033,0.9199,-0.3921,0.3449,-0.0115,0.9284,-0.3714,0.3411,-0.0209,0.9375,-0.3474,0.3384,-0.0307,0.9459,-0.3229,0.336,-0.0415,0.9542,-0.2961,0.3335,-0.0216,0.9622,-0.2715,0.3315,0.002,0.9693,-0.246,0.3312,0.0236,0.9736,-0.2272,0.3318,0.0444,0.9751,-0.2174,0.3323,0.0522,0.9772,-0.2058,0.3319,0.0575,0.979,-0.1958,0.3333,0.0728,0.9791,-0.1898,0.3367,0.0833,0.9795,-0.1835,0.3383,0.0948,0.9785,-0.1833,0.3422,0.1173,0.9767,-0.1798,0.3452,0.1278,0.9751,-0.1814,0.3478,0.1484,0.9712,-0.1862,0.3502,0.1694,0.9679,-0.1855,0.3541,0.1842,0.9641,-0.1911,0.3562,0.2022,0.9589,-0.1992,0.3562,0.2157,0.9537,-0.2097,0.356,0.2305,0.9481,-0.2189,0.3545,0.2454,0.9404,-0.2354,0.354,0.2613,0.9328,-0.2482,0.3529,0.2758,0.9244,-0.2633,0.3536,0.2841,0.9167,-0.2808,0.3561,0.2913,0.9099,-0.2952,0.358,0.2941,0.9041,-0.3101,0.3608,0.2989,0.8969,-0.326,0.3646,0.3018,0.8893,-0.3437,0.3692,0.3072,0.8829,-0.3552,0.3732,0.32,0.8735,-0.367,0.3735,0.3457,0.8582,-0.3795,0.3705,0.3734,0.841,-0.3914,0.3666,0.3945,0.8308,-0.3927,0.3605,0.4129,0.8251,-0.3857,0.355,0.4258,0.8261,-0.3692,0.3511,0.4341,0.8324,-0.3445,0.3476,0.4345,0.8453,-0.311,0.3452,0.4271,0.8612,-0.2756,0.3436,0.4193,0.8749,-0.2424,0.3438,0.4073,0.8878,-0.2142,0.3422,0.402,0.8968,-0.1847,0.3406,0.3948,0.9049,-0.1589,0.3376,0.3889,0.9102,-0.1424,0.3335,0.3869,0.9122,-0.1352,0.3274,0.3832,0.9145,-0.13,0.3196,0.3801,0.9157,-0.1302,0.3114,0.3816,0.9146,-0.1336,0.3006,0.381,0.9138,-0.1407,0.2913,0.3794,0.9124,-0.1533,0.2857,0.3735,0.9114,-0.1728,0.2801,0.3745,0.906,-0.1972,0.2765,0.3739,0.901,-0.2199,0.2772,0.3675,0.895,-0.2527,0.2753,0.3631,0.8862,-0.2876,0.2757,0.3641,0.8756,-0.3175,0.2789,0.3528,0.8684,-0.3483,0.2835,0.3442,0.863,-0.3698,0.2883,0.3377,0.857,-0.3892,0.2938,0.3291,0.8525,-0.4061,0.3011,0.3275,0.8459,-0.4209,0.3074,0.3268,0.8362,-0.4403,0.3134,0.3366,0.8239,-0.4559,0.319,0.3476,0.8133,-0.4666,0.3221,0.3549,0.8024,-0.4798,0.3264,0.3656,0.791,-0.4905,0.3302,0.3785,0.7787,-0.5004,0.3338,0.3926,0.7689,-0.5046,0.3386,0.4006,0.7657,-0.5033,0.3453,0.4059,0.7635,-0.5023,0.3523,0.4145,0.765,-0.4929,0.3566,0.423,0.7654,-0.4851,0.3603,0.4235,0.7684,-0.4799,0.3643,0.4222,0.7745,-0.471,0.3654,0.4319,0.7755,-0.4606,0.3672,0.4365,0.7794,-0.4495,0.3665,0.4414,0.7821,-0.4398,0.3651,0.4433,0.7878,-0.4276,0.3647,0.451,0.7921,-0.4113,0.3631,0.4605,0.7946,-0.3956,0.3633,0.4785,0.7899,-0.3835,0.3614,0.5002,0.7836,-0.3684,0.3614,0.5312,0.7705,-0.3522,0.3622,0.5604,0.7579,-0.334,0.3633,0.5862,0.7498,-0.3068,0.3621,0.6078,0.7443,-0.2768,0.3631,0.6197,0.7478,-0.2383,0.364,0.6261,0.7533,-0.2012,0.3636,0.6269,0.7615,-0.1649,0.3617,0.6251,0.7707,-0.1237,0.3566,0.6147,0.7843,-0.0837,0.3513,0.6017,0.7975,-0.0432,0.3456,0.5888,0.8082,-0.0075,0.3378,0.5681,0.8221,0.0377,0.3306,0.5392,0.8382,0.0821,0.3256,0.499,0.8575,0.1251,0.3215,0.4559,0.8716,0.1805,0.3185,0.4103,0.8826,0.2296,0.3192,0.3779,0.8868,0.266,0.3215,0.3652,0.8802,0.303,0.3231,0.379,0.8612,0.3386,0.3283,0.4095,0.8352,0.3671,0.3318,0.446,0.802,0.3973,0.3365,0.4898,0.7643,0.4195,0.3441,0.5317,0.7227,0.4416,0.3538,0.5622,0.6896,0.4565,0.3664,0.5821,0.664,0.4694,0.3817,0.5947,0.6478,0.4761,0.3999,0.6081,0.6333,0.4787,0.4197,0.6268,0.6167,0.4764,0.4378,0.6485,0.5986,0.4702,0.4547,0.6729,0.5796,0.4597,0.4694,0.7015,0.5588,0.4423,0.4812,0.7278,0.5411,0.4212,0.4904,0.7531,0.5272,0.3935,0.4987,0.7758,0.5145,0.3652,0.4994,0.796,0.5038,0.3355,0.4983,0.815,0.4923,0.3055,0.4925,0.8295,0.4854,0.2762,0.4842,0.8386,0.4838,0.2505,0.4723,0.8443,0.4867,0.2243,0.4588,0.8436,0.4977,0.2016,0.4452,0.8411,0.5117,0.175,0.4325,0.8342,0.5303,0.1511,0.4181,0.8294,0.5447,0.1243,0.4058,0.8225,0.5605,0.0966,0.3913,0.8146,0.5759,0.0694,0.3782,0.8031,0.5941,0.0449,0.3647,0.788,0.6155,0.0153,0.3525,0.7687,0.6394,-0.017,0.3396,0.749,0.6606,-0.052,0.3284,0.7229,0.6852,-0.0891,0.3176,0.6932,0.7094,-0.1274,0.3091,0.6562,0.7347,-0.1723,0.3055,0.6172,0.7572,-0.214,0.302,0.5705,0.7783,-0.2622,0.2996,0.5155,0.8013,-0.3037,0.2985,0.4569,0.822,-0.34,0.3016,0.3915,0.8427,-0.3696,0.3098,0.3204,0.8657,-0.3846,0.3241,0.253,0.8838,-0.3936,0.3409,0.2009,0.8942,-0.4,0.357,0.1717,0.8925,-0.4172,0.3676,0.1617,0.8785,-0.4495,0.3694,0.1651,0.855,-0.4916,0.3635,0.1754,0.8244,-0.5381,0.3551,0.1902,0.7893,-0.5838,0.3473,0.1993,0.7557,-0.6239,0.341,0.2074,0.7297,-0.6515,0.3384,0.2151,0.7083,-0.6724,0.3393,0.2198,0.6947,-0.6849,0.3391,0.223,0.6887,-0.69,0.3399,0.2264,0.6901,-0.6874,0.3421,0.2283,0.6988,-0.6779,0.3445,0.2313,0.7094,-0.6657,0.3475,0.2307,0.7284,-0.6452,0.3511,0.2326,0.7481,-0.6215,0.3528,0.2331,0.7691,-0.5951,0.3542,0.2414,0.7834,-0.5727,0.3548,0.2678,0.7843,-0.5596,0.3536,0.3134,0.7788,-0.5433,0.352,0.3718,0.7654,-0.5253,0.3498,0.4271,0.7524,-0.5014,0.3483,0.4824,0.744,-0.4624,0.3502,0.5277,0.7424,-0.4127,0.3534,0.5592,0.7522,-0.3485,0.3592,0.5795,0.7677,-0.2735,0.3628,0.5915,0.7822,-0.1958,0.364,0.5993,0.7929,-0.1107,0.3654,0.6056,0.7952,-0.0319,0.3644,0.6184,0.7843,0.0489,0.3617,0.6312,0.7659,0.1221,0.3592,0.6509,0.7356,0.1877,0.358,0.6762,0.6935,0.2485,0.3563,0.6977,0.6493,0.3028,0.3601,0.7161,0.609,0.3409,0.3613,0.73,0.5718,0.3742,0.3647,0.7359,0.5432,0.4042,0.3679,0.7374,0.5169,0.4347,0.3726,0.7378,0.5008,0.4526,0.3764,0.7334,0.494,0.4669,0.3801,0.7253,0.5011,0.4721,0.3838,0.7163,0.5121,0.474,0.3856,0.7065,0.5305,0.4684,0.3839,0.6934,0.5565,0.4578,0.382,0.6807,0.5874,0.4377,0.378,0.669,0.6206,0.409,0.3731,0.6575,0.6588,0.3657,0.3687,0.6525,0.6887,0.3162,0.3651,0.6587,0.7091,0.2515,0.3583,0.6679,0.7212,0.1838,0.353,0.6848,0.7203,0.111,0.3453,0.6989,0.7143,0.0371,0.3376,0.7018,0.7111,-0.0424,0.3318,0.6907,0.7141,-0.114,0.329,0.6654,0.725,-0.1776,0.3283,0.6336,0.7369,-0.2358,0.3285,0.6029,0.7446,-0.2864,0.3311,0.5721,0.7489,-0.3345,0.3324,0.5485,0.7453,-0.3791,0.3311,0.5351,0.7347,-0.4169,0.3268,0.5249,0.7222,-0.4504,0.3211,0.5142,0.7129,-0.4768,0.3153,0.4981,0.7116,-0.4955,0.3114,0.4795,0.7165,-0.5066,0.3128,0.456,0.7313,-0.5073,0.3126,0.4334,0.7462,-0.5053,0.3146,0.4133,0.7599,-0.5017,0.315,0.3904,0.7712,-0.5029,0.3127,0.3768,0.7787,-0.5017,0.3081,0.3757,0.7786,-0.5027,0.3044,0.3843,0.7802,-0.4935,0.2999,0.3875,0.7816,-0.4888,0.2958,0.3894,0.788,-0.4769,0.2926,0.3856,0.7997,-0.4602,0.2892,0.3811,0.8119,-0.4423,0.2885,0.3725,0.8281,-0.419,0.2896,0.3688,0.8425,-0.3927,0.2915,0.3681,0.8508,-0.3749,0.2917,0.3766,0.8555,-0.3553,0.2922,0.385,0.8597,-0.3357,0.293,0.4027,0.8578,-0.3195,0.29,0.4194,0.8554,-0.3039,0.2879,0.4303,0.8501,-0.3037,0.2877,0.431,0.8542,-0.2907,0.2894,0.4219,0.8598,-0.2878,0.2914,0.4108,0.8684,-0.2778,0.2948,0.4002,0.8755,-0.2708,0.2996,0.3925,0.8793,-0.2697,0.3035,0.3961,0.8785,-0.267,0.3075,0.401,0.8762,-0.2674,0.3095,0.4068,0.8755,-0.2607,0.3115,0.418,0.8711,-0.2578,0.3125,0.4218,0.8714,-0.2507,0.3123,0.4231,0.8718,-0.2469,0.3108,0.428,0.8733,-0.2326,0.31,0.4228,0.8798,-0.2171,0.3067,0.4119,0.889,-0.2001,0.3038,0.4045,0.8959,-0.1836,0.304,0.3982,0.9015,-0.1693,0.3057,0.392,0.9048,-0.1663,0.3085])

Group366.addChildren(OrientationInterpolator385)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-13.882767,10.133185], [-1.735815,23.780594], [9.550971,19.809969] degrees
#-4.209171 -0.956767 15.542125, -4.459375 -0.830590 15.608989, -4.476139 -0.775092 15.764439, -4.553674 -0.842833 16.093493, -4.698999 -0.847590 16.460310, -4.872755 -0.836375 16.735620, -4.928457 -0.864238 16.899836, -5.065824 -0.881759 16.966072, -5.289596 -0.933467 17.090935, -5.365664 -1.020011 17.140644, -5.475568 -1.062598 17.227947, -5.562577 -1.165336 17.378244, -5.658044 -1.191625 17.550426, -5.797744 -1.269387 17.550930, -5.930939 -1.253531 17.659334, -6.036566 -1.309102 17.586447, -5.955359 -1.202155 17.667650, -5.918179 -1.146635 17.577909, -5.843574 -1.018329 17.685450, -5.656076 -0.885500 17.688231, -5.466358 -0.837841 17.687351, -5.083170 -0.779445 17.787874, -4.735620 -0.882076 17.745825, -4.470139 -1.059863 17.611347, -4.189794 -1.251557 17.556625, -3.975331 -1.531844 17.426308, -3.996085 -1.677718 17.283699, -4.127633 -1.735815 17.245644, -4.561687 -1.634529 17.152985, -4.957360 -1.489763 17.124262, -5.491736 -1.207605 17.209818, -6.082725 -0.769623 17.380705, -6.782347 -0.446813 17.698597, -7.366393 -0.186329 18.156824, -8.003438 -0.175855 18.612537, -8.581265 -0.176606 18.893654, -8.991168 -0.177254 18.966280, -9.300286 -0.185315 18.900526, -9.453194 -0.310359 18.813715, -9.502047 -0.547178 18.612331, -9.315676 -0.761112 18.472830, -9.032214 -0.863056 18.285244, -8.678535 -1.057144 18.238876, -8.127527 -1.132103 18.186089, -7.611537 -1.280606 18.123507, -7.102710 -1.358855 18.081436, -6.561292 -1.456617 18.113340, -6.020236 -1.558718 18.145536, -5.439682 -1.670151 18.168884, -5.005928 -1.216900 18.232254, -4.594167 -0.704705 18.374510, -4.316419 -0.250715 18.509298, -4.201699 0.165169 18.576675, -4.005128 0.345610 18.604012, -3.849675 0.472896 18.715967, -3.824566 0.780989 18.922544, -3.757487 0.999956 19.027016, -3.835992 1.227140 19.232571, -3.877246 1.681101 19.381929, -3.974991 1.889236 19.503635, -4.168779 2.288737 19.581636, -4.277148 2.727554 19.751133, -4.468053 3.019456 19.809969, -4.691412 3.355788 19.723595, -4.941257 3.590881 19.625395, -5.149311 3.846945 19.449001, -5.518249 4.091561 19.295052, -5.802319 4.359990 19.104815, -6.160785 4.613844 19.007309, -6.581861 4.755011 19.007168, -6.930963 4.877897 18.992970, -7.299025 4.919416 19.039633, -7.724164 5.011712 19.116959, -8.203210 5.067221 19.219921, -8.556305 5.187823 19.314568, -8.851434 5.432342 19.165398, -9.114920 5.916742 18.745882, -9.334521 6.428803 18.248915, -9.248812 6.787251 17.767183, -9.004655 7.104473 17.399529, -8.606471 7.344441 17.222944, -8.058151 7.511931 17.159761, -7.354538 7.557034 17.249926, -6.621694 7.469048 17.428129, -5.971743 7.406592 17.660318, -5.369191 7.216309 17.779671, -4.765512 7.167944 17.834131, -4.206584 7.043469 17.790636, -3.818351 6.900747 17.648430, -3.592147 6.769305 17.350552, -3.381538 6.568497 16.964777, -3.267299 6.356989 16.540892, -3.183041 6.171250 15.942126, -3.174823 5.969551 15.434334, -3.299578 5.812798 15.122505, -3.515888 5.571836 14.812185, -3.844260 5.478601 14.555556, -4.207500 5.437722 14.529812, -4.670587 5.243613 14.351428, -5.210903 5.118947 14.253291, -5.745653 5.134905 14.269896, -6.318861 4.968243 14.401862, -6.766427 4.858554 14.567904, -7.213177 4.791287 14.758533, -7.672348 4.704995 15.053877, -8.094817 4.726953 15.266988, -8.603125 4.750376 15.411119, -9.064714 4.968787 15.493136, -9.376055 5.193043 15.480665, -9.764377 5.363197 15.509413, -10.107094 5.598915 15.510505, -10.436650 5.882998 15.484701, -10.709711 6.221446 15.558580, -10.934103 6.479756 15.831849, -11.168912 6.691561 16.134851, -11.154889 6.948442 16.379087, -11.145953 7.195793 16.571669, -11.178375 7.277179 16.821804, -11.037157 7.283193 16.992092, -10.912533 7.540355 17.108328, -10.680483 7.651520 17.153492, -10.454957 7.754982 17.144592, -10.200117 7.813901 17.227530, -9.849169 7.988004 17.236147, -9.566648 8.229592 17.298761, -9.313190 8.604066 17.125658, -9.065071 9.103384 17.016672, -8.835649 9.823728 16.821247, -8.564953 10.524556 16.641405, -8.036058 11.111852 16.411766, -7.498885 11.677749 16.327095, -6.766594 12.060432 16.389269, -6.016947 12.284911 16.419006, -5.242659 12.340746 16.421825, -4.312412 12.253509 16.278143, -3.414839 11.978571 16.208630, -2.516546 11.643206 16.107079, -1.716726 11.233594 15.865287, -0.760790 10.725159 15.688431, 0.146052 10.144019 15.666552, 1.022553 9.391048 15.749197, 2.118312 8.664248 15.774732, 3.112027 7.988774 15.952493, 3.867852 7.557136 16.110594, 4.603578 7.456813 16.028215, 5.315589 7.920386 15.871456, 5.858576 8.633121 15.480124, 6.469305 9.505488 14.978026, 6.985815 10.602186 14.479682, 7.583831 11.768528 13.938344, 8.125725 12.843476 13.643888, 8.710976 13.842742 13.560955, 9.225446 14.825740 13.754625, 9.675375 15.907891 14.007954, 9.969776 17.063601 14.124324, 10.133185 18.265089 14.135760, 10.124131 19.462622 14.038130, 9.859505 20.655910 13.812223, 9.413152 21.695112 13.615335, 8.719193 22.675032 13.541964, 7.891953 23.235268 13.327739, 6.995933 23.638725 13.141107, 6.070464 23.780594 12.829035, 5.155535 23.675032 12.590035, 4.342409 23.249857 12.385584, 3.530252 22.654036 12.259220, 2.836408 21.903408 12.305445, 2.071643 21.147402 12.440242, 1.419769 20.221979 12.586562, 0.751407 19.446598 12.659112, 0.119909 18.526358 12.656977, -0.453634 17.675842 12.651535, -0.919135 16.751354 12.641153, -1.460240 15.819456 12.712205, -1.999994 14.799702 12.770612, -2.550905 13.869830 12.802065, -3.092126 12.864836 12.871896, -3.636950 11.923761 12.995268, -4.333068 11.039539 13.324360, -4.941827 10.150488 13.583951, -5.647548 9.165474 13.851786, -6.237635 8.095215 14.180084, -6.827014 7.072165 14.663619, -7.416586 6.000070 15.378827, -7.899324 4.859103 16.447224, -8.324320 3.703049 17.569603, -8.702048 2.732254 18.537712, -9.223924 2.110599 19.012161, -9.903196 1.819121 18.800875, -10.609579 1.790293 18.027016, -11.314376 1.909543 17.018436, -11.993101 2.133825 15.987415, -12.559577 2.263109 15.073343, -13.008528 2.401032 14.486806, -13.456431 2.547442 14.136783, -13.695181 2.637401 13.881462, -13.830696 2.702403 13.806053, -13.882767 2.777306 13.932421, -13.806030 2.823957 14.205081, -13.698832 2.896905 14.543669, -13.440144 2.903685 15.063564, -13.049117 2.964599 15.532318, -12.582395 3.006806 16.008930, -12.185318 3.206030 16.332266, -11.960507 3.760663 16.347935, -11.710421 4.709547 16.253475, -11.436913 5.916440 15.996597, -11.064242 7.071280 15.768641, -10.506244 8.315563 15.762149, -9.749377 9.422051 15.907364, -8.733082 10.361988 16.348814, -7.377421 11.069993 16.747402, -5.860786 11.568916 16.976484, -4.159358 12.025715 17.107235, -2.522868 12.364349 16.941208, -0.827394 12.787610 16.416218, 0.708919 13.172513 15.752969, 2.089611 13.699724 14.910072, 3.384781 14.281545 13.810833, 4.610054 14.977067 12.873751, 5.498202 15.459451 11.947922, 6.330312 15.931559 11.153659, 7.096742 16.225086 10.530219, 7.918955 16.491299 9.980167, 8.434252 16.680573 9.656838, 8.855320 16.773500 9.550971, 9.033079 16.783869 9.784859, 9.091599 16.693583 10.083716, 8.885856 16.423336 10.489127, 8.547802 16.071053 11.074666, 7.958511 15.628088 11.728759, 7.172847 15.149816 12.406691, 6.094202 14.666093 13.222463, 4.931275 14.318007 13.869642, 3.459772 14.024971 14.209665, 1.996659 13.830787 14.414717, 0.497845 13.680631 14.259167, -0.935290 13.471660 13.990609, -2.414020 13.117090 13.856963, -3.718766 12.638750 13.933881, -4.868982 11.986049 14.207788, -5.913978 11.252207 14.511347, -6.865771 10.626214 14.823124, -7.738748 9.960899 14.996495, -8.476386 9.378256 14.891519, -9.007651 8.950191 14.521791, -9.402910 8.571769 14.049887, -9.650097 8.202990 13.624310, -9.813382 7.796931 13.417549, -10.021760 7.465520 13.545949, -9.987944 7.021313 13.760652, -9.983622 6.638350 14.078608, -9.900344 6.274251 14.307397, -9.797681 5.813008 14.361516, -9.595609 5.500843 14.249359, -9.487720 5.427943 14.069005, -9.201013 5.528785 13.890007, -8.996124 5.529988 13.718266, -8.702696 5.529769 13.667620, -8.320672 5.433749 13.681541, -8.002837 5.370070 13.827699, -7.645149 5.274691 14.121141, -7.266457 5.279308 14.434305, -6.982258 5.300949 14.571355, -6.693873 5.486518 14.673789, -6.407830 5.676010 14.775290, -6.104132 5.952167 14.595583, -5.833138 6.221560 14.453097, -5.844730 6.400421 14.366108, -5.675450 6.469025 14.509668, -5.656924 6.359528 14.694358, -5.547674 6.254079 14.994569, -5.513400 6.174387 15.351606, -5.562623 6.110967 15.613249, -5.607419 6.250768 15.810017, -5.667704 6.372327 15.881334, -5.606840 6.528724 15.977761, -5.599769 6.756353 15.958705, -5.479019 6.836749 15.951333, -5.384267 6.839868 15.876088, -5.131411 6.942599 15.853076, -4.789719 6.819990 15.774738, -4.423537 6.607477 15.751765, -4.131451 6.517969 15.862647, -3.901722 6.475040 16.036787, -3.880312 6.426272 16.235306
#Interpolator15_l_wrist channels [45..47] sends animation values to BVH JOINT LeftWrist, DEF Bvh1_l_wrist, <HAnimJoint name=l_wrist/>
OrientationInterpolator386 = OrientationInterpolator()
OrientationInterpolator386.setDEF("Interpolator15_l_wrist")
OrientationInterpolator386.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator386.setKeyValue([0.8318,0.3043,0.4642,0.1814,0.8133,0.3073,0.494,0.1792,0.7952,0.318,0.5163,0.1771,0.7863,0.3137,0.5323,0.1788,0.7729,0.3061,0.5558,0.181,0.7514,0.3051,0.5851,0.1822,0.7477,0.2945,0.5951,0.184,0.7342,0.2891,0.6143,0.1881,0.7194,0.2864,0.6329,0.1924,0.7101,0.2823,0.6451,0.1945,0.7032,0.2697,0.6579,0.1985,0.699,0.2555,0.6679,0.203,0.7002,0.2479,0.6695,0.2048,0.6987,0.2442,0.6725,0.2081,0.7045,0.2358,0.6694,0.2106,0.7065,0.2328,0.6683,0.2118,0.7099,0.2302,0.6656,0.2096,0.7108,0.2311,0.6644,0.2088,0.7249,0.2304,0.6491,0.2059,0.7384,0.2355,0.6319,0.201,0.758,0.242,0.6056,0.1963,0.7808,0.2509,0.5722,0.1901,0.8086,0.2585,0.5286,0.1852,0.8283,0.2715,0.4902,0.1812,0.8526,0.2753,0.4441,0.1749,0.8691,0.2932,0.3984,0.1691,0.8687,0.3165,0.381,0.162,0.8564,0.3444,0.3846,0.1562,0.8201,0.3697,0.4367,0.1521,0.7712,0.3725,0.5163,0.1509,0.6919,0.3626,0.6244,0.1563,0.5968,0.3424,0.7257,0.1674,0.5046,0.3142,0.8041,0.1869,0.434,0.2798,0.8563,0.2092,0.391,0.2544,0.8845,0.2336,0.3676,0.229,0.9013,0.2556,0.3688,0.2048,0.9067,0.2736,0.3823,0.1812,0.9061,0.287,0.4088,0.1599,0.8985,0.2931,0.4389,0.1437,0.887,0.2954,0.4658,0.1362,0.8743,0.2921,0.4969,0.1367,0.857,0.2853,0.5238,0.1431,0.8397,0.274,0.5452,0.149,0.825,0.2582,0.5653,0.158,0.8096,0.2411,0.579,0.1825,0.7946,0.2236,0.5959,0.2126,0.7744,0.2049,0.6157,0.2543,0.7458,0.1882,0.6304,0.307,0.713,0.1741,0.6472,0.3481,0.6782,0.1611,0.6806,0.3754,0.6291,0.1556,0.7165,0.3882,0.5797,0.1521,0.7477,0.3859,0.5403,0.1513,0.7831,0.373,0.4976,0.1514,0.8083,0.3635,0.4631,0.1553,0.8223,0.3371,0.4585,0.1576,0.8276,0.3213,0.4603,0.1615,0.8307,0.2977,0.4703,0.1654,0.8236,0.2891,0.488,0.1668,0.8098,0.2839,0.5134,0.1699,0.7943,0.2809,0.5388,0.1719,0.7798,0.2708,0.5644,0.1725,0.7538,0.2659,0.6009,0.1737,0.7283,0.2638,0.6324,0.1722,0.7031,0.2542,0.6641,0.1728,0.6831,0.245,0.688,0.173,0.6466,0.2301,0.7273,0.175,0.6033,0.2248,0.7652,0.1794,0.5575,0.2167,0.8014,0.1864,0.5048,0.2188,0.835,0.1934,0.4573,0.2137,0.8632,0.2023,0.4091,0.2096,0.8881,0.2107,0.3589,0.208,0.9099,0.2192,0.3165,0.1986,0.9276,0.2278,0.2698,0.1844,0.9451,0.2346,0.2271,0.1705,0.9588,0.24,0.1842,0.1597,0.9698,0.2416,0.1406,0.1467,0.9792,0.2394,0.1026,0.1369,0.9853,0.2326,0.0616,0.1365,0.9887,0.2212,0.0156,0.1474,0.989,0.2055,-0.0356,0.1824,0.9826,0.1864,-0.0917,0.2328,0.9682,0.162,-0.1695,0.3015,0.9383,0.1398,-0.2653,0.3936,0.8802,0.1203,-0.3485,0.4993,0.7932,0.1049,-0.4341,0.5798,0.6895,0.0955,-0.4863,0.6419,0.5928,0.0874,-0.5173,0.7053,0.4847,0.0806,-0.531,0.7346,0.4223,0.0745,-0.5447,0.7651,0.3434,0.0665,-0.5323,0.7914,0.3006,0.0589,-0.4874,0.8376,0.2468,0.0527,-0.4222,0.8846,0.1979,0.0472,-0.3889,0.8944,0.2211,0.0463,-0.3333,0.8978,0.2879,0.0456,-0.2646,0.8629,0.4305,0.046,-0.1999,0.771,0.6046,0.0469,-0.0843,0.6637,0.7433,0.053,0.0205,0.5311,0.8471,0.0625,0.0958,0.4046,0.9095,0.074,0.1703,0.3029,0.9377,0.0894,0.2467,0.2334,0.9406,0.1046,0.2929,0.1939,0.9363,0.1198,0.3371,0.1583,0.9281,0.1357,0.3443,0.1239,0.9307,0.1492,0.3345,0.1012,0.9369,0.1638,0.3082,0.0821,0.9478,0.1776,0.2717,0.0795,0.9591,0.191,0.2451,0.0705,0.9669,0.2033,0.2124,0.0605,0.9753,0.2178,0.1866,0.0652,0.9803,0.2312,0.168,0.0615,0.9839,0.2436,0.1642,0.0533,0.985,0.2558,0.1683,0.0453,0.9847,0.2681,0.1751,0.0445,0.9835,0.2755,0.1792,0.046,0.9827,0.2827,0.1821,0.0436,0.9823,0.2865,0.1858,0.0422,0.9817,0.2891,0.1832,0.0403,0.9823,0.2868,0.1874,0.0364,0.9816,0.2819,0.183,0.0335,0.9825,0.2748,0.1771,0.0306,0.9837,0.2654,0.1711,0.0339,0.9847,0.2505,0.1502,0.033,0.9881,0.2345,0.1201,0.0339,0.9922,0.2179,0.0706,0.0389,0.9967,0.2001,-0.009,0.0478,0.9988,0.183,-0.1047,0.0532,0.9931,0.1672,-0.2215,0.0685,0.9727,0.1506,-0.3481,0.0936,0.9328,0.134,-0.4861,0.1144,0.8664,0.1194,-0.6338,0.1439,0.76,0.106,-0.7869,0.2005,0.5836,0.0929,-0.9158,0.2542,0.311,0.0846,-0.9468,0.3213,-0.019,0.0815,-0.8828,0.326,-0.3382,0.0859,-0.7554,0.321,-0.5712,0.0953,-0.575,0.3105,-0.757,0.1068,-0.3445,0.2757,-0.8974,0.1219,-0.094,0.213,-0.9725,0.14,0.1387,0.1505,-0.9788,0.1716,0.3171,0.0791,-0.9451,0.2119,0.427,0.0355,-0.9036,0.2547,0.4808,0.0027,-0.8768,0.294,0.4961,-0.0282,-0.8678,0.3266,0.4874,-0.0527,-0.8716,0.3493,0.4605,-0.0644,-0.8853,0.3619,0.4104,-0.0634,-0.9097,0.3676,0.3514,-0.0495,-0.9349,0.3728,0.289,-0.0299,-0.9569,0.379,0.2235,-0.0009,-0.9747,0.3891,0.1568,0.0249,-0.9873,0.4052,0.0885,0.0498,-0.9948,0.4218,0.0204,0.0845,-0.9962,0.4392,-0.053,0.1104,-0.9925,0.4529,-0.1366,0.1395,-0.9807,0.4608,-0.2265,0.1688,-0.9593,0.4624,-0.3178,0.1971,-0.9274,0.4616,-0.4088,0.2166,-0.8865,0.4585,-0.4879,0.2324,-0.8414,0.4531,-0.5579,0.2388,-0.7948,0.4465,-0.6085,0.2386,-0.7568,0.437,-0.6504,0.2348,-0.7224,0.4226,-0.6822,0.2297,-0.6941,0.4052,-0.7055,0.2264,-0.6716,0.3846,-0.729,0.2235,-0.647,0.3628,-0.7526,0.2203,-0.6205,0.3422,-0.776,0.2188,-0.5915,0.3211,-0.8026,0.2153,-0.5564,0.3013,-0.8308,0.2139,-0.5138,0.2793,-0.856,0.2111,-0.4718,0.2548,-0.8852,0.2047,-0.4178,0.2292,-0.9128,0.1995,-0.3565,0.2041,-0.9395,0.207,-0.2728,0.1759,-0.967,0.1928,-0.1667,0.1498,-0.9827,0.1852,0.0009,0.1237,-0.955,0.1586,0.2507,0.1029,-0.8007,0.1117,0.5886,0.0931,-0.5084,0.069,0.8583,0.0982,-0.219,0.0222,0.9755,0.1195,-0.0297,0.0309,0.9991,0.1489,0.0747,0.0441,0.9962,0.1814,0.1401,0.0755,0.9873,0.2168,0.1731,0.1071,0.9791,0.2518,0.1924,0.1294,0.9728,0.2845,0.1906,0.1399,0.9717,0.3155,0.1771,0.132,0.9753,0.3442,0.1672,0.1153,0.9791,0.3729,0.158,0.0989,0.9825,0.3983,0.1544,0.0784,0.9849,0.4261,0.1576,0.0642,0.9854,0.4488,0.1622,0.0524,0.9854,0.4679,0.1686,0.0442,0.9847,0.4844,0.1809,0.0381,0.9828,0.4982,0.1982,0.0309,0.9797,0.5084,0.2144,0.0267,0.9764,0.5144,0.2306,0.0207,0.9728,0.5165,0.2393,0.018,0.9708,0.514,0.2466,0.0159,0.969,0.5079,0.2464,0.0133,0.9691,0.4973,0.2449,0.013,0.9695,0.4809,0.2409,0.0134,0.9705,0.4613,0.2334,0.0088,0.9724,0.4384,0.2127,0.0101,0.9771,0.4135,0.1792,0.0057,0.9838,0.3891,0.1257,0.0001,0.9921,0.3645,0.0631,-0.0104,0.998,0.3385,-0.0103,-0.0156,0.9998,0.3091,-0.0984,-0.0179,0.995,0.2737,-0.2098,-0.0118,0.9777,0.2336,-0.3545,0.0005,0.9351,0.1866,-0.5796,0.034,0.8142,0.1397,-0.8751,0.104,0.4726,0.1066,-0.9784,0.1628,-0.1273,0.1083,-0.8285,0.1809,-0.5299,0.1472,-0.706,0.1793,-0.6852,0.2022,-0.6475,0.1792,-0.7407,0.2577,-0.6171,0.1898,-0.7637,0.3132,-0.6057,0.1952,-0.7714,0.3645,-0.6059,0.2028,-0.7692,0.4094,-0.6068,0.2144,-0.7654,0.4482,-0.6088,0.2279,-0.7599,0.481,-0.6111,0.2452,-0.7526,0.5076,-0.6121,0.2596,-0.7469,0.5242,-0.6101,0.2739,-0.7435,0.5321,-0.608,0.2812,-0.7425,0.5307,-0.6065,0.2904,-0.7402,0.5207,-0.6016,0.2995,-0.7405,0.5022,-0.5939,0.3077,-0.7433,0.4745,-0.5904,0.3169,-0.7423,0.4394,-0.5905,0.3259,-0.7383,0.3988,-0.5949,0.3347,-0.7307,0.351,-0.6115,0.3451,-0.712,0.2993,-0.6502,0.3565,-0.6709,0.2408,-0.7171,0.372,-0.5894,0.181,-0.8402,0.3841,-0.3827,0.1231,-0.9245,0.3487,0.154,0.0828,-0.549,0.1571,0.8209,0.084,-0.1247,-0.0073,0.9922,0.1245,0.071,-0.0605,0.9956,0.1709,0.167,-0.0822,0.9825,0.2166,0.2062,-0.0759,0.9756,0.2545,0.209,-0.0778,0.9748,0.2869,0.2013,-0.0768,0.9765,0.3099,0.1885,-0.0727,0.9794,0.3259,0.1663,-0.0649,0.9839,0.3379,0.1424,-0.0581,0.9881,0.3466,0.1194,-0.0487,0.9916,0.3511,0.0978,-0.0409,0.9944,0.3522,0.0874,-0.0348,0.9956,0.3508,0.0795,-0.0232,0.9966,0.3484,0.08,-0.026,0.9965,0.3436,0.085,-0.0228,0.9961,0.3397,0.0895,-0.023,0.9957,0.3342,0.0905,-0.021,0.9957,0.3284,0.0859,-0.0251,0.996,0.3206,0.0781,-0.0226,0.9967,0.3128,0.066,-0.0263,0.9975,0.3041,0.0582,-0.0223,0.9981,0.2939,0.0499,-0.0178,0.9986,0.2836,0.044,-0.0161,0.9989,0.2725,0.0351,-0.0053,0.9994,0.261,0.023,0.0041,0.9997,0.2528,0.0086,0.0114,0.9999,0.2437,-0.0093,0.0065,0.9999,0.2363,-0.0309,0.0081,0.9995,0.2294,-0.0409,0.0069,0.9991,0.2259,-0.0448,0.0062,0.999,0.2228,-0.039,0.0031,0.9992,0.2179,-0.0373,0.0122,0.9992,0.2139,-0.0307,0.0121,0.9995,0.2085,-0.0101,0.016,0.9998,0.2051,-0.0003,0.0189,0.9998,0.2037,0.0105,0.018,0.9998,0.2034,0.0108,0.0124,0.9999,0.2039,0.0223,0.0047,0.9997,0.2031,0.0116,0.0004,0.9999,0.2013,0.0079,-0.0049,1,0.1998,0.0036,-0.0022,1,0.1939,-0.0136,-0.0035,0.9999,0.1855,-0.0219,0.0035,0.9998,0.175,-0.0313,0.0116,0.9994,0.1645,-0.0361,0.0244,0.999,0.1554,-0.0437,0.0369,0.9984,0.1473,-0.0664,0.0384,0.9971,0.1431])

Group366.addChildren(OrientationInterpolator386)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-25.808823,28.885216], [-19.734434,9.765475], [-1.893683,5.558785] degrees
#4.620726 8.767239 2.816781, 4.875600 8.477571 2.801267, 5.042766 8.200990 2.872262, 5.259824 8.193152 2.844685, 5.576401 8.157900 2.784464, 5.926369 7.997870 2.778819, 6.097806 8.035483 2.684623, 6.445376 8.072772 2.669499, 6.798725 8.099038 2.683844, 7.015496 8.088227 2.659138, 7.312119 8.170278 2.553663, 7.606586 8.303685 2.428225, 7.700098 8.388991 2.353513, 7.861967 8.506024 2.336178, 7.924347 8.672566 2.254587, 7.956888 8.742134 2.226346, 7.844638 8.688625 2.176867, 7.800100 8.666793 2.182888, 7.507773 8.704259 2.154918, 7.127421 8.651467 2.180640, 6.656054 8.664115 2.224817, 6.071107 8.632622 2.281117, 5.442282 8.697379 2.336358, 4.913029 8.711118 2.451399, 4.274776 8.640910 2.442828, 3.676760 8.507605 2.573990, 3.350749 8.146338 2.705052, 3.252988 7.748227 2.866765, 3.622089 7.246763 2.998524, 4.293136 6.781305 2.970351, 5.434257 6.341100 2.950962, 6.816708 5.906898 2.938832, 8.473284 5.633001 2.956011, 10.137950 5.473197 2.880136, 11.711172 5.544520 2.850253, 13.076478 5.718525 2.715529, 14.095562 6.115538 2.472556, 14.793044 6.599702 2.141587, 15.000972 7.136200 1.762866, 14.939879 7.661156 1.443180, 14.566185 7.999672 1.270827, 13.945295 8.314679 1.231654, 13.114498 8.409328 1.293227, 12.128458 8.237076 1.340159, 11.102587 7.969378 1.417113, 10.085241 7.586093 1.677043, 8.980842 7.162271 1.940603, 7.916407 6.806740 2.278299, 6.971710 6.461987 2.676120, 6.113612 6.135380 2.891786, 5.450493 6.220343 3.057244, 4.884509 6.382152 3.116131, 4.510855 6.607057 3.089900, 4.142714 6.907024 2.991646, 3.937205 7.301610 2.989913, 3.963002 7.524080 2.788505, 4.083537 7.757822 2.701741, 4.289783 7.973776 2.528921, 4.500170 7.971835 2.454756, 4.837687 7.993029 2.432399, 5.147330 7.936154 2.414962, 5.428708 7.822081 2.310754, 5.839411 7.625803 2.262836, 6.108890 7.313129 2.219027, 6.452726 7.089595 2.122387, 6.707889 6.899481 2.029534, 7.191120 6.611099 1.896950, 7.767786 6.337697 1.885586, 8.470172 6.105494 1.868444, 9.162922 5.763969 1.969792, 9.916862 5.487909 2.008574, 10.638151 5.145813 2.060763, 11.344402 4.735063 2.151609, 12.031893 4.372763 2.141499, 12.640953 3.870553 2.060377, 13.130677 3.363044 1.968518, 13.384215 2.783679 1.894829, 13.402261 2.145105 1.769360, 13.107335 1.563695 1.652807, 12.517855 0.962207 1.631302, 11.641868 0.358543 1.704922, 10.497449 -0.200647 1.971367, 9.000372 -0.678273 2.218765, 7.542405 -1.195140 2.497348, 6.109685 -1.680728 2.805229, 4.820708 -1.965640 3.085061, 3.837854 -2.267471 3.249453, 3.036231 -2.349053 3.277229, 2.306485 -2.323654 3.305002, 1.863751 -2.214744 3.170766, 1.361109 -2.040790 2.939258, 1.056890 -1.772715 2.688401, 0.777564 -1.454773 2.539138, 0.559147 -1.130816 2.398931, 0.608028 -1.019426 2.378818, 0.769179 -0.854414 2.349063, 1.148162 -0.674673 2.280957, 1.634566 -0.507836 2.079897, 2.260693 -0.216017 2.019564, 3.032943 0.123792 1.899781, 3.849300 0.463458 1.700418, 4.788741 0.935637 1.512582, 5.620234 1.545159 1.324352, 6.403686 2.079957 1.215486, 7.192437 2.691314 1.063133, 7.933629 3.006164 0.852103, 8.775698 3.199569 0.706722, 9.631068 3.191464 0.569163, 10.480242 3.035489 0.593736, 11.252699 2.917785 0.536009, 12.162734 2.710446 0.469593, 12.977405 2.548441 0.578295, 13.721233 2.424192 0.570749, 14.430466 2.479424 0.471995, 15.120250 2.646660 0.349173, 15.520801 2.824703 0.321298, 15.915130 2.969158 0.335698, 16.118317 3.049783 0.288980, 16.258596 3.135296 0.255994, 16.137142 3.063133 0.231835, 15.855867 3.068965 0.165038, 15.468962 2.916501 0.134498, 14.958249 2.723601 0.111103, 14.131956 2.490070 0.180438, 13.272406 2.050380 0.207110, 12.386274 1.533289 0.258710, 11.424575 0.848657 0.362794, 10.471356 -0.048381 0.507190, 9.518579 -0.956222 0.590680, 8.403514 -1.860515 0.729107, 7.182344 -2.620378 0.884132, 5.956905 -3.279521 0.954133, 4.650367 -3.808397 1.029208, 3.149436 -4.155130 1.181871, 1.558625 -4.422453 1.293027, -0.030825 -4.423519 1.500457, -1.606763 -4.367359 1.544098, -3.061541 -4.170847 1.642856, -4.578485 -3.590831 1.757656, -6.229995 -2.506581 1.791688, -7.788054 -0.867184 1.651815, -9.639607 1.233199 1.587350, -11.524076 3.728822 1.340977, -13.265940 6.116955 1.233482, -14.871373 8.002426 1.092433, -16.337273 9.232847 0.795219, -17.525732 9.765475 0.442410, -18.418291 9.598929 0.209807, -19.203876 8.704074 0.125388, -20.015265 7.537626 0.263158, -20.827839 6.254766 0.494169, -21.781200 4.867110 0.917780, -22.966192 3.429062 1.282292, -24.073215 1.826754 1.612325, -25.073244 0.038875 2.168858, -25.717354 -1.963256 2.466931, -25.808823 -4.303303 2.763247, -25.270954 -6.778835 3.029007, -24.322388 -9.246679 3.307162, -23.031250 -11.583159 3.418690, -21.531094 -13.491312 3.554604, -19.992138 -15.041576 3.541208, -18.598125 -15.932427 3.441245, -17.145519 -16.362297 3.283456, -15.781125 -16.371035 3.119052, -14.476338 -16.008780 3.001365, -13.140723 -15.551912 2.893258, -11.872144 -15.099747 2.780610, -10.597892 -14.567264 2.699757, -9.335052 -14.096886 2.587105, -7.964919 -13.491632 2.500794, -6.656513 -12.650269 2.359221, -5.285237 -11.733049 2.156366, -3.996275 -10.745983 1.964187, -2.600123 -9.515615 1.875355, -1.320075 -8.318119 1.561880, 0.086707 -6.965930 1.320131, 1.528474 -5.616585 1.010922, 3.166210 -4.250791 0.713805, 4.845451 -2.842324 0.509039, 6.680282 -1.486946 0.239104, 8.523042 -0.232424 0.281521, 10.349913 0.813008 0.386058, 12.252968 1.827176 0.745127, 14.098040 2.661243 1.223395, 15.813285 3.385173 1.652863, 17.505552 3.774270 1.967399, 19.174446 3.859797 1.976747, 20.867069 3.938329 1.766261, 22.381105 3.951263 1.506327, 24.019802 4.056929 1.080149, 25.322742 4.280541 0.716051, 26.417431 4.514408 0.369701, 27.344090 4.790527 0.086664, 28.079300 5.221510 -0.194938, 28.588633 5.757869 -0.548461, 28.850204 6.249621 -0.804202, 28.885216 6.688611 -1.098673, 28.697378 6.887233 -1.222120, 28.316261 7.000937 -1.296413, 27.726971 6.840428 -1.303107, 26.814863 6.586393 -1.206700, 25.735020 6.233004 -1.063734, 24.495438 5.731321 -1.020283, 23.194256 4.950009 -0.774443, 21.964586 3.922781 -0.633007, 20.733459 2.567836 -0.467455, 19.360138 1.166836 -0.403090, 17.704533 -0.221543 -0.244527, 15.602649 -1.561792 -0.068799, 13.092027 -2.801173 0.162622, 10.011459 -3.770286 0.336201, 6.544158 -4.615162 0.536949, 2.923383 -5.324854 0.771610, -0.739094 -6.078850 0.971988, -4.397464 -7.039455 1.257864, -7.841941 -8.294875 1.514206, -10.816671 -9.753691 1.734054, -13.545111 -11.373587 2.077692, -15.919448 -13.050215 2.286958, -17.825626 -14.720860 2.502021, -19.392822 -16.209805 2.808225, -20.622746 -17.537746 3.182724, -21.483521 -18.683931 3.705218, -21.947649 -19.415085 4.166543, -22.095625 -19.734434 4.647760, -21.967199 -19.660522 4.888289, -21.429985 -19.280357 5.166523, -20.632910 -18.480015 5.393541, -19.543308 -17.256512 5.518304, -18.047758 -15.871251 5.558785, -16.283701 -14.371198 5.470643, -14.186600 -12.677977 5.209732, -11.789869 -11.024081 4.815240, -8.939701 -9.322451 4.210220, -5.892527 -7.625653 3.474303, -2.567857 -5.987220 2.578479, 0.795667 -4.375169 1.685920, 3.973447 -2.615374 0.847807, 7.075397 -0.889950 0.003065, 9.755356 0.641926 -0.648580, 12.215673 1.948186 -1.232310, 14.267735 2.838712 -1.468818, 16.079765 3.212817 -1.741001, 17.399956 3.313691 -1.882475, 18.347416 3.244535 -1.893683, 19.103045 2.953984 -1.766370, 19.661901 2.577345 -1.612315, 19.979565 2.185236 -1.375020, 20.088381 1.791231 -1.151553, 20.024801 1.600054 -0.989127, 19.902586 1.475175 -0.726921, 19.627733 1.458248 -0.768719, 19.397228 1.549124 -0.713304, 19.076544 1.609861 -0.714507, 18.747389 1.609138 -0.665342, 18.302849 1.477974 -0.702418, 17.870676 1.314101 -0.615304, 17.388840 1.062937 -0.623808, 16.809483 0.911922 -0.512228, 16.231375 0.758996 -0.399057, 15.600908 0.644100 -0.341089, 14.944809 0.509224 -0.146401, 14.480840 0.336597 0.016611, 13.964165 0.138066 0.142826, 13.538626 -0.114702 0.102399, 13.140038 -0.390212 0.151931, 12.933104 -0.515529 0.147818, 12.754726 -0.558689 0.141563, 12.476332 -0.478629 0.091232, 12.245532 -0.437340 0.197140, 11.937628 -0.348882 0.181626, 11.747863 -0.099107 0.198749, 11.669934 0.019006 0.219649, 11.648956 0.142596 0.196154, 11.682013 0.140273 0.131031, 11.632658 0.263233 0.027905, 11.530915 0.133038 -0.009244, 11.445556 0.084607 -0.064783, 11.110202 0.037738 -0.027838, 10.630076 -0.146873 -0.023565, 10.025872 -0.215680 0.054052, 9.422285 -0.284748 0.133496, 8.894746 -0.303637 0.241074, 8.429388 -0.345042 0.337556, 8.177369 -0.520231 0.352241
#Interpolator16_RightCollar channels [48..50] sends animation values to BVH JOINT RightCollar, DEF Bvh1_RightCollar, <HAnimJoint name=RightCollar/>
OrientationInterpolator387 = OrientationInterpolator()
OrientationInterpolator387.setDEF("Interpolator16_RightCollar")
OrientationInterpolator387.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator387.setKeyValue([0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0])

Group366.addChildren(OrientationInterpolator387)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-1.0E-6,4.9E-324], [-2.0E-6,1.0E-6], [-6.0E-6,4.0E-6] degrees
#-0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000004, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000003, -0.000000 0.000000 0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000000 -0.000005, -0.000001 0.000000 -0.000003, -0.000001 0.000000 -0.000000, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 -0.000002, -0.000001 -0.000000 0.000003, -0.000000 0.000001 -0.000005, -0.000000 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000001, -0.000000 0.000000 0.000003, -0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000000, -0.000000 -0.000000 -0.000004, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000000 0.000003, -0.000001 0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000005, -0.000000 0.000001 -0.000003, -0.000001 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000000 -0.000001 -0.000000, -0.000001 0.000001 -0.000002, -0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000001 0.000000 0.000000, 0.000000 0.000001 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000004, -0.000000 0.000000 0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000000, -0.000000 0.000000 -0.000006, -0.000001 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 0.000000 0.000002, -0.000001 0.000000 -0.000003, 0.000000 -0.000000 -0.000002, -0.000000 -0.000000 0.000002, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000000 0.000000 -0.000002, 0.000000 -0.000000 -0.000002, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 0.000001 -0.000002, -0.000001 -0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000001 0.000000 -0.000004, -0.000000 0.000000 -0.000004, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 -0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000002, -0.000000 0.000001 -0.000003, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 0.000000, 0.000000 0.000001 -0.000003, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000001, -0.000001 0.000000 -0.000000, -0.000000 0.000000 -0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, 0.000000 -0.000000 -0.000004, 0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000002, -0.000000 0.000000 -0.000005, 0.000000 -0.000001 0.000002, 0.000000 0.000001 -0.000003, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000001 0.000001 -0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000001, 0.000000 0.000001 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 0.000003, -0.000001 -0.000000 0.000001, 0.000000 -0.000001 -0.000004, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, 0.000000 0.000000 -0.000002, -0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 0.000001 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000001 -0.000001, -0.000001 0.000000 -0.000000, 0.000000 -0.000002 -0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000001 -0.000000 -0.000004, -0.000000 -0.000001 -0.000003, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000000 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000004, -0.000001 0.000000 -0.000001, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000001 -0.000004, 0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 -0.000001 -0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000004, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 0.000001, -0.000001 -0.000002 0.000001, -0.000000 0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000004, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000000 -0.000001 0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000002, 0.000000 -0.000001 -0.000003, 0.000000 -0.000000 0.000001, -0.000001 0.000000 0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 -0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000004, -0.000000 -0.000000 0.000001, -0.000001 0.000000 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000001 -0.000001, 0.000000 0.000000 -0.000001, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000000 -0.000001 -0.000000, -0.000000 -0.000001 0.000003, -0.000001 -0.000001 0.000003, -0.000001 -0.000001 -0.000001, 0.000000 -0.000001 -0.000000, -0.000000 0.000001 -0.000001, -0.000000 0.000000 -0.000001, -0.000001 0.000000 0.000004, -0.000001 0.000001 -0.000001, 0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000001 -0.000002 -0.000003, -0.000000 0.000001 -0.000001, -0.000001 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000001 -0.000003, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000002, 0.000000 -0.000001 -0.000002, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 -0.000001 0.000004, -0.000000 -0.000002 -0.000000, 0.000000 0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000000 -0.000001 -0.000000, -0.000000 0.000000 0.000002, 0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 0.000001 0.000001, 0.000000 -0.000001 -0.000003, 0.000000 0.000001 -0.000002
#Interpolator17_r_shoulder channels [51..53] sends animation values to BVH JOINT RightShoulder, DEF Bvh1_r_shoulder, <HAnimJoint name=r_shoulder/>
OrientationInterpolator388 = OrientationInterpolator()
OrientationInterpolator388.setDEF("Interpolator17_r_shoulder")
OrientationInterpolator388.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator388.setKeyValue([0.4344,0.8611,0.2641,0.1105,0.4259,0.8589,0.2845,0.1096,0.4119,0.8677,0.2783,0.1098,0.4112,0.8688,0.276,0.1116,0.4157,0.8631,0.2867,0.112,0.4146,0.8594,0.2993,0.1115,0.3925,0.8631,0.3179,0.1103,0.3767,0.8625,0.3379,0.1091,0.3877,0.8519,0.3521,0.112,0.3859,0.8481,0.363,0.1142,0.3649,0.8607,0.3551,0.119,0.3388,0.8679,0.3633,0.1252,0.3179,0.8763,0.3621,0.1314,0.2974,0.888,0.3507,0.1374,0.2897,0.8931,0.3442,0.1427,0.2972,0.8945,0.334,0.1485,0.2936,0.8938,0.339,0.1531,0.2928,0.8919,0.3445,0.1567,0.2832,0.8939,0.3476,0.1589,0.2777,0.8921,0.3564,0.1625,0.2629,0.8924,0.3667,0.1673,0.2501,0.9006,0.3555,0.1761,0.2361,0.907,0.3487,0.1876,0.2271,0.9146,0.3345,0.197,0.2151,0.9204,0.3265,0.2072,0.1871,0.927,0.3251,0.2185,0.157,0.9282,0.3372,0.2264,0.1275,0.9275,0.3514,0.2344,0.1049,0.9276,0.3587,0.2389,0.095,0.9277,0.3611,0.2437,0.0814,0.929,0.3609,0.2502,0.077,0.9281,0.3642,0.2539,0.0706,0.9264,0.3698,0.2545,0.0704,0.9241,0.3756,0.2527,0.0704,0.9207,0.3838,0.2468,0.0706,0.914,0.3995,0.2368,0.0672,0.9058,0.4183,0.2271,0.0639,0.896,0.4395,0.2193,0.0679,0.8819,0.4665,0.2142,0.071,0.8678,0.4919,0.2075,0.0851,0.8532,0.5147,0.2039,0.0956,0.8419,0.531,0.2025,0.1057,0.8369,0.537,0.2022,0.1086,0.8358,0.5382,0.2025,0.1221,0.8455,0.5199,0.2052,0.1265,0.858,0.4979,0.2086,0.1346,0.8696,0.475,0.211,0.1403,0.8796,0.4545,0.212,0.1408,0.8838,0.4462,0.2121,0.1404,0.8853,0.4434,0.2103,0.1443,0.8877,0.4373,0.2075,0.1533,0.8789,0.4518,0.2018,0.1669,0.875,0.4544,0.1937,0.208,0.8624,0.4615,0.1839,0.2432,0.8492,0.4688,0.1751,0.2741,0.841,0.4664,0.168,0.3059,0.8251,0.4749,0.1598,0.3611,0.8028,0.4744,0.1534,0.4326,0.7682,0.4719,0.1484,0.4938,0.7353,0.4642,0.1468,0.5491,0.7004,0.4559,0.1456,0.5882,0.6682,0.4556,0.1444,0.615,0.6448,0.4539,0.1441,0.644,0.6164,0.4531,0.1388,0.672,0.5893,0.4485,0.1345,0.6885,0.5743,0.4429,0.1317,0.7005,0.5539,0.4499,0.1296,0.6947,0.555,0.4576,0.1273,0.6728,0.5861,0.4515,0.1289,0.6336,0.6394,0.4355,0.1335,0.5937,0.6884,0.4167,0.139,0.5588,0.7246,0.4034,0.1415,0.5373,0.7306,0.4213,0.141,0.5207,0.723,0.454,0.1371,0.5157,0.7212,0.4625,0.1312,0.5027,0.7137,0.4877,0.1251,0.4996,0.6999,0.5104,0.1192,0.5049,0.6934,0.5141,0.1141,0.5108,0.6907,0.5118,0.1116,0.5221,0.6979,0.4903,0.1075,0.5084,0.721,0.4708,0.1067,0.4907,0.754,0.4366,0.1071,0.4589,0.7869,0.4125,0.1094,0.3965,0.8328,0.3864,0.1125,0.326,0.866,0.3792,0.1147,0.2704,0.8971,0.3494,0.1182,0.2167,0.9139,0.3432,0.1221,0.1746,0.9286,0.3275,0.1274,0.1436,0.9316,0.3339,0.1325,0.0979,0.9426,0.3194,0.137,0.0746,0.9509,0.3005,0.1397,0.0748,0.9554,0.2857,0.1417,0.075,0.9631,0.2584,0.1427,0.0791,0.9682,0.2372,0.1431,0.0694,0.9743,0.2142,0.1407,0.0591,0.9799,0.1904,0.1385,0.061,0.9828,0.1742,0.1358,0.0666,0.9842,0.164,0.1357,0.0613,0.9833,0.1713,0.1371,0.0497,0.9805,0.1899,0.1382,0.039,0.9766,0.2116,0.1421,0.0261,0.9748,0.2215,0.147,0.0499,0.9708,0.2347,0.1508,0.0683,0.9687,0.2387,0.1545,0.0754,0.9681,0.2391,0.1582,0.0935,0.9646,0.2465,0.1594,0.103,0.9611,0.2563,0.1621,0.1225,0.9558,0.2672,0.1618,0.1343,0.9503,0.2809,0.1611,0.1538,0.9462,0.2849,0.1642,0.1719,0.9413,0.2906,0.1662,0.1923,0.9349,0.2983,0.1678,0.2096,0.9289,0.3053,0.1661,0.2557,0.9146,0.3133,0.1628,0.2984,0.894,0.3344,0.1577,0.341,0.875,0.3436,0.1556,0.3789,0.8521,0.3611,0.1535,0.4122,0.8312,0.3731,0.1488,0.4394,0.8167,0.3741,0.1456,0.4677,0.8084,0.3574,0.1443,0.4901,0.7999,0.3463,0.1427,0.4865,0.8046,0.3404,0.1431,0.4787,0.8122,0.3334,0.14,0.4383,0.8319,0.3402,0.136,0.3883,0.8474,0.3621,0.1317,0.3261,0.8618,0.3887,0.1272,0.2619,0.8782,0.4003,0.1254,0.1932,0.8967,0.3983,0.1254,0.1457,0.9093,0.3899,0.127,0.12,0.9252,0.36,0.1284,0.0902,0.9437,0.3183,0.13,0.0597,0.9516,0.3016,0.1306,0.0332,0.9587,0.2824,0.1293,0.0206,0.9628,0.2693,0.1267,-0.001,0.9625,0.2713,0.1218,-0.0117,0.9543,0.2987,0.1124,-0.0102,0.9447,0.3277,0.1024,0.0159,0.9325,0.3607,0.0943,0.0531,0.9154,0.399,0.0845,0.1458,0.8712,0.4688,0.0775,0.2294,0.8225,0.5205,0.069,0.3542,0.7036,0.616,0.0632,0.4964,0.496,0.7124,0.0591,0.6056,0.2247,0.7634,0.0583,0.6399,-0.0643,0.7657,0.0634,0.6531,-0.2626,0.7103,0.0742,0.6516,-0.4028,0.6427,0.0861,0.6448,-0.4797,0.5951,0.097,0.6284,-0.5571,0.5428,0.1084,0.6128,-0.619,0.4911,0.1194,0.587,-0.6827,0.4351,0.1301,0.5649,-0.731,0.3827,0.1405,0.5445,-0.7722,0.3274,0.1508,0.5432,-0.7964,0.2659,0.1572,0.5505,-0.8069,0.2143,0.1582,0.5831,-0.7962,0.1613,0.156,0.6304,-0.7702,0.0971,0.1498,0.6942,-0.7196,0.0141,0.148,0.728,-0.6828,-0.0613,0.1459,0.7599,-0.6388,-0.1205,0.1446,0.7721,-0.6099,-0.1788,0.1435,0.7718,-0.5927,-0.2305,0.1418,0.7579,-0.5919,-0.2742,0.1395,0.7388,-0.5894,-0.3269,0.1336,0.7196,-0.5771,-0.3861,0.1241,0.6958,-0.5766,-0.4283,0.1141,0.6784,-0.5706,-0.4628,0.1023,0.6612,-0.5673,-0.491,0.0906,0.656,-0.5342,-0.5332,0.0795,0.6499,-0.5164,-0.5577,0.07,0.6582,-0.4791,-0.5808,0.0625,0.6785,-0.4414,-0.5873,0.0544,0.6849,-0.3686,-0.6285,0.0497,0.7087,-0.323,-0.6273,0.0469,0.7406,-0.2371,-0.6288,0.0442,0.7617,-0.0917,-0.6414,0.0423,0.7655,0.0662,-0.64,0.0424,0.7712,0.2115,-0.6004,0.043,0.7592,0.3816,-0.5272,0.0446,0.745,0.5123,-0.4272,0.0481,0.7216,0.6077,-0.3317,0.0542,0.7128,0.6677,-0.2149,0.0598,0.6997,0.7061,-0.1087,0.0636,0.681,0.7321,-0.0146,0.0682,0.6803,0.7324,0.03,0.0744,0.6823,0.7267,0.0797,0.0792,0.6995,0.7066,0.1066,0.085,0.7209,0.6812,0.1276,0.0903,0.7406,0.6598,0.127,0.0976,0.7666,0.6283,0.1325,0.1019,0.7782,0.611,0.1452,0.1064,0.7758,0.6156,0.1382,0.1141,0.7542,0.6409,0.1428,0.1216,0.7414,0.6532,0.1538,0.1317,0.7331,0.6637,0.1486,0.1412,0.7191,0.6788,0.1486,0.1501,0.7047,0.6957,0.1397,0.1577,0.6899,0.7098,0.1425,0.1637,0.6655,0.7355,0.1271,0.1695,0.6402,0.76,0.1116,0.1736,0.6131,0.7843,0.0947,0.1744,0.5843,0.8071,0.0849,0.1718,0.5485,0.832,0.0836,0.1659,0.5054,0.8591,0.0811,0.1585,0.4601,0.8811,0.1095,0.1488,0.4276,0.8933,0.1387,0.1399,0.4018,0.9006,0.166,0.1306,0.3641,0.9116,0.1907,0.1256,0.3435,0.9165,0.2051,0.12,0.3287,0.9211,0.2088,0.1166,0.3075,0.9299,0.2018,0.1131,0.2937,0.9359,0.1945,0.1113,0.2965,0.9374,0.1825,0.105,0.3031,0.9399,0.1571,0.1003,0.332,0.9334,0.136,0.0956,0.3732,0.9167,0.1427,0.0895,0.4463,0.8835,0.1425,0.0845,0.5313,0.8325,0.1567,0.0803,0.602,0.7815,0.1642,0.0798,0.6704,0.7233,0.1655,0.0802,0.7584,0.6416,0.1146,0.0818,0.8422,0.5347,0.0695,0.0832,0.9347,0.3532,0.04,0.0856,0.9867,0.1615,-0.0164,0.0895,0.997,-0.0664,-0.0393,0.0975,0.9703,-0.2343,-0.0603,0.1107,0.9289,-0.3573,-0.0977,0.1264,0.8879,-0.4429,-0.1246,0.1432,0.8531,-0.4977,-0.1564,0.1602,0.8224,-0.5375,-0.1863,0.1764,0.7965,-0.5657,-0.2137,0.1923,0.7748,-0.5876,-0.2332,0.2076,0.7608,-0.595,-0.2591,0.223,0.7554,-0.591,-0.283,0.237,0.7602,-0.5775,-0.2977,0.2482,0.7665,-0.5596,-0.3151,0.2549,0.7808,-0.535,-0.3227,0.2568,0.7997,-0.496,-0.3382,0.2555,0.8189,-0.4585,-0.3453,0.249,0.8463,-0.4078,-0.3427,0.2367,0.8723,-0.3578,-0.3332,0.2249,0.8899,-0.3143,-0.3307,0.2161,0.9057,-0.2712,-0.326,0.2068,0.9174,-0.2263,-0.3274,0.1983,0.9249,-0.1739,-0.3381,0.1893,0.9263,-0.1259,-0.3552,0.179,0.9305,-0.0747,-0.3585,0.1688,0.9291,-0.0215,-0.3692,0.1571,0.9258,0.0391,-0.3759,0.1436,0.9212,0.0984,-0.3764,0.1324,0.9157,0.1589,-0.369,0.1195,0.9032,0.23,-0.3624,0.1081,0.8961,0.3036,-0.3238,0.1006,0.8641,0.405,-0.2988,0.0935,0.8281,0.4996,-0.2545,0.0888,0.7728,0.6009,-0.2041,0.0869,0.7041,0.6906,-0.1655,0.089,0.6304,0.7668,-0.1213,0.093,0.5331,0.841,-0.0922,0.0979,0.4541,0.8893,-0.0545,0.1056,0.3815,0.9242,-0.0143,0.1126,0.3304,0.9436,0.0212,0.1228,0.314,0.9479,0.0544,0.1323,0.3486,0.9348,0.0675,0.1434,0.3588,0.9304,0.0745,0.1557,0.3816,0.9212,0.0755,0.1641,0.4154,0.9061,0.0798,0.1689,0.4664,0.8811,0.0788,0.1709,0.5268,0.8469,0.0719,0.1722,0.578,0.8136,0.0637,0.1732,0.6299,0.7753,0.0469,0.1749,0.6717,0.74,0.0343,0.1786,0.7046,0.7091,0.0278,0.18,0.7357,0.677,0.0227,0.1836,0.7636,0.6457,0.004,0.1839,0.7928,0.6095,0.0024,0.1857,0.8188,0.574,-0.0019,0.1876,0.8444,0.5356,-0.0113,0.1905,0.8581,0.5122,-0.0352,0.1968,0.8699,0.4899,-0.0577,0.2033,0.8783,0.4717,-0.0773,0.2058,0.8864,0.4522,-0.099,0.2057,0.8966,0.4271,-0.1171,0.2043,0.9043,0.4056,-0.1333,0.2019,0.9115,0.3832,-0.1496,0.1997,0.9197,0.3628,-0.1502,0.1951])

Group366.addChildren(OrientationInterpolator388)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.308793,6.108548], [0.028064,11.981505], [-7.903096,13.444084] degrees
#1.539841 2.825439 5.415902, 1.659198 2.753919 5.354541, 1.625498 2.669958 5.420823, 1.635851 2.710081 5.517717, 1.709246 2.751279 5.498542, 1.784128 2.736570 5.450369, 1.890162 2.572632 5.415076, 1.999269 2.449772 5.348680, 2.139033 2.591124 5.419775, 2.250012 2.633984 5.497386, 2.291157 2.606829 5.817527, 2.470241 2.565995 6.171932, 2.585234 2.544601 6.543992, 2.612884 2.503433 6.936684, 2.656961 2.539271 7.243045, 2.667868 2.709070 7.550754, 2.790483 2.770228 7.776845, 2.902675 2.836037 7.941399, 2.972895 2.791735 8.066810, 3.122263 2.815632 8.233824, 3.317151 2.772131 8.480510, 3.374153 2.794408 9.007363, 3.516791 2.842327 9.666446, 3.527120 2.886672 10.238727, 3.612417 2.904853 10.841058, 3.808820 2.735540 11.519359, 4.130212 2.477762 11.956823, 4.498990 2.207664 12.379446, 4.712445 1.963622 12.622948, 4.852257 1.880785 12.883872, 4.993766 1.753587 13.251352, 5.118576 1.729687 13.432649, 5.223372 1.650766 13.444084, 5.271639 1.639933 13.314195, 5.269379 1.598588 12.955299, 5.275953 1.532345 12.339832, 5.315741 1.423947 11.730162, 5.407961 1.337053 11.200869, 5.612225 1.365543 10.763661, 5.740685 1.362724 10.256515, 5.896593 1.507919 9.897114, 6.039891 1.626244 9.694221, 6.091292 1.741280 9.615250, 6.108548 1.777709 9.611070, 5.960849 1.954654 9.850123, 5.786687 2.032180 10.161457, 5.564275 2.141125 10.419526, 5.331964 2.204646 10.588397, 5.233246 2.204957 10.648883, 5.157654 2.175082 10.578238, 5.015079 2.180710 10.466765, 5.040973 2.221691 10.069785, 4.864235 2.267448 9.620588, 4.673319 2.565467 8.990757, 4.507741 2.776731 8.415347, 4.291955 2.944167 7.990723, 4.156141 3.077573 7.450298, 3.969330 3.421023 6.944750, 3.800106 3.895494 6.407286, 3.680072 4.353392 6.049390, 3.572792 4.765178 5.701854, 3.537423 5.036597 5.377108, 3.516724 5.241601 5.168880, 3.389826 5.267253 4.751217, 3.256528 5.307953 4.394653, 3.151973 5.315391 4.192788, 3.159031 5.312814 3.969057, 3.164854 5.178929 3.908918, 3.151274 5.086535 4.191673, 3.128397 4.980465 4.759638, 3.095225 4.877620 5.355340, 3.038961 4.686393 5.753066, 3.180666 4.505731 5.781435, 3.364690 4.258335 5.559049, 3.294290 4.034218 5.309987, 3.335736 3.753568 5.011118, 3.343917 3.552269 4.680160, 3.231652 3.430023 4.440219, 3.146148 3.385720 4.324314, 2.900862 3.325940 4.218502, 2.759282 3.214887 4.333297, 2.556682 3.114451 4.558411, 2.460793 2.983402 4.870402, 2.367981 2.666538 5.312231, 2.382555 2.262095 5.645256, 2.265176 1.952483 6.037054, 2.311145 1.646034 6.360004, 2.311090 1.413178 6.753007, 2.462139 1.243958 7.049155, 2.449759 0.927281 7.377811, 2.358125 0.754491 7.594779, 2.272150 0.761979 7.744729, 2.063609 0.756198 7.861013, 1.893547 0.781141 7.926217, 1.683758 0.675934 7.847624, 1.474561 0.569533 7.768697, 1.319386 0.562995 7.639850, 1.236512 0.601127 7.645232, 1.309789 0.570698 7.719815, 1.472613 0.493709 7.758840, 1.695318 0.435949 7.943337, 1.843556 0.352589 8.207355, 1.988597 0.577498 8.376950, 2.060283 0.759999 8.563943, 2.105997 0.845526 8.758120, 2.176740 1.023211 8.791803, 2.296736 1.137690 8.905041, 2.380599 1.321913 8.836703, 2.488762 1.432628 8.742267, 2.557031 1.647719 8.864279, 2.629366 1.845502 8.924725, 2.713435 2.065946 8.943919, 2.741401 2.210066 8.790573, 2.736133 2.593024 8.472451, 2.823940 2.898843 8.010077, 2.849713 3.237589 7.724328, 2.952813 3.529531 7.408338, 2.959594 3.700424 6.994677, 2.900391 3.840819 6.719944, 2.726928 4.028975 6.592043, 2.601432 4.159382 6.450484, 2.559361 4.139420 6.508563, 2.454687 3.982234 6.433605, 2.455359 3.556897 6.408954, 2.566662 3.076496 6.329539, 2.697830 2.525296 6.221654, 2.766888 2.034380 6.260426, 2.778461 1.545180 6.406199, 2.769111 1.220695 6.586525, 2.589489 1.037459 6.783438, 2.323725 0.815493 7.013365, 2.223831 0.585443 7.110412, 2.071923 0.374639 7.098576, 1.941470 0.268589 6.987932, 1.888927 0.104129 6.714764, 1.923086 0.028064 6.143245, 1.922718 0.033475 5.543188, 1.943688 0.171336 5.038196, 1.919272 0.331167 4.424983, 2.058617 0.717184 3.856963, 2.031932 0.965127 3.236427, 2.202439 1.331844 2.523175, 2.389669 1.716919 1.645444, 2.538263 2.039088 0.705599, 2.787350 2.317533 -0.289975, 3.047571 2.744570 -1.189415, 3.227982 3.156201 -2.076316, 3.393687 3.502913 -2.771553, 3.492766 3.797110 -3.578935, 3.517079 4.061381 -4.362130, 3.440013 4.223393 -5.219701, 3.315510 4.378778 -6.015869, 3.102353 4.527208 -6.799446, 2.701454 4.728346 -7.290344, 2.261339 4.850821 -7.415062, 1.765894 5.107989 -7.200192, 1.147201 5.350907 -6.669604, 0.433984 5.868917 -6.129395, -0.208987 6.102906 -5.703598, -0.709043 6.334280 -5.260380, -1.195441 6.403401 -4.952821, -1.613637 6.342876 -4.732400, -1.946252 6.139285 -4.630992, -2.284751 5.745710 -4.400836, -2.566453 5.207935 -3.989599, -2.654719 4.636758 -3.665329, -2.598872 4.050777 -3.254033, -2.461914 3.494283 -2.870508, -2.365506 3.036685 -2.370260, -2.190458 2.645703 -2.020924, -2.044405 2.386040 -1.672496, -1.806243 2.136882 -1.342669, -1.772130 1.966045 -1.019295, -1.672569 1.917788 -0.840526, -1.583862 1.884591 -0.574792, -1.552768 1.850197 -0.197349, -1.557191 1.856274 0.185883, -1.489060 1.893858 0.546103, -1.364708 1.929209 0.998751, -1.204258 2.040278 1.434860, -1.066379 2.221556 1.906642, -0.785329 2.426634 2.304550, -0.453607 2.540488 2.584233, -0.123354 2.657879 2.863242, 0.048837 2.903327 3.122849, 0.272679 3.105040 3.291274, 0.416843 3.420251 3.429887, 0.545781 3.749540 3.509463, 0.577116 4.160682 3.669850, 0.630882 4.498604 3.646070, 0.731767 4.768635 3.695891, 0.726295 5.097736 3.993843, 0.790838 5.286163 4.430202, 0.921510 5.635983 4.886602, 0.925345 5.977057 5.325645, 0.963962 6.237135 5.789543, 0.914775 6.424888 6.242757, 0.962084 6.534754 6.611441, 0.831744 6.522065 7.102596, 0.690237 6.423434 7.529771, 0.526641 6.171502 7.815439, 0.435730 5.791489 7.929120, 0.433454 5.251531 7.893014, 0.422588 4.626759 7.790867, 0.675379 3.971329 7.489743, 0.896302 3.488851 7.137039, 1.063474 3.071782 6.710490, 1.220587 2.693421 6.534095, 1.277549 2.433432 6.272878, 1.274875 2.265517 6.127219, 1.201453 2.057799 6.006757, 1.141561 1.935118 5.952320, 1.009097 1.835118 5.625164, 0.819902 1.781654 5.389270, 0.663021 1.849666 5.104369, 0.652524 1.940477 4.688197, 0.608456 2.183239 4.264184, 0.639023 2.465538 3.815193, 0.664872 2.773503 3.557142, 0.671515 3.101393 3.306823, 0.444170 3.566520 2.993821, 0.242243 4.020555 2.541180, 0.127226 4.584747 1.727443, -0.120776 5.057913 0.833752, -0.201914 5.571814 -0.361316, -0.303451 6.159817 -1.471791, -0.557985 6.743077 -2.558703, -0.794591 7.312361 -3.588281, -1.129012 7.881477 -4.498874, -1.496181 8.389862 -5.334077, -1.886650 8.883523 -6.098204, -2.223527 9.358481 -6.822636, -2.681435 9.907380 -7.389225, -3.146455 10.488713 -7.762302, -3.486883 11.070706 -7.903096, -3.837596 11.475283 -7.817317, -3.998698 11.769812 -7.491693, -4.256133 11.981505 -6.845989, -4.308793 11.925361 -6.116582, -4.141274 11.672716 -5.127547, -3.887588 11.394709 -4.239806, -3.763989 11.143174 -3.538801, -3.601629 10.827950 -2.882778, -3.523323 10.494513 -2.254569, -3.536868 10.082382 -1.578667, -3.568114 9.534146 -0.997120, -3.438276 9.013334 -0.452506, -3.333298 8.365539 0.050015, -3.132158 7.603348 0.530259, -2.914954 6.964976 0.925065, -2.596121 6.243224 1.230830, -2.321784 5.565041 1.539007, -1.949505 5.132383 1.838022, -1.691550 4.597380 2.238838, -1.390545 4.183148 2.594195, -1.117559 3.818260 3.029668, -0.954387 3.559994 3.550543, -0.766372 3.332531 4.108601, -0.640401 2.965731 4.735943, -0.458969 2.729020 5.394960, -0.220335 2.451936 5.967710, 0.014559 2.329088 6.641727, 0.262680 2.399180 7.179081, 0.361503 2.891956 7.672117, 0.431204 3.237390 8.289264, 0.436771 3.628849 8.653377, 0.463122 4.061896 8.753965, 0.426688 4.607890 8.616160, 0.328956 5.231747 8.348691, 0.227031 5.761292 8.069072, 0.041215 6.325610 7.776369, -0.104384 6.876001 7.587522, -0.178945 7.263827 7.333302, -0.243991 7.732790 7.148040, -0.438410 8.030734 6.847092, -0.455722 8.418845 6.530881, -0.498692 8.782389 6.220225, -0.598981 9.195501 5.907287, -0.892859 9.639155 5.865096, -1.188982 10.081673 5.826207, -1.429893 10.296177 5.707324, -1.669778 10.373792 5.494705, -1.848853 10.419980 5.182458, -1.991358 10.385781 4.887197, -2.133324 10.352474 4.590765, -2.063855 10.208699 4.250721
#Interpolator18_r_elbow channels [54..56] sends animation values to BVH JOINT RightElbow, DEF Bvh1_r_elbow, <HAnimJoint name=r_elbow/>
OrientationInterpolator389 = OrientationInterpolator()
OrientationInterpolator389.setDEF("Interpolator18_r_elbow")
OrientationInterpolator389.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator389.setKeyValue([-0.1792,-0.9723,-0.1498,0.3045,-0.1802,-0.9708,-0.1581,0.3037,-0.1813,-0.97,-0.1618,0.3035,-0.1881,-0.9684,-0.1637,0.3028,-0.1906,-0.9672,-0.1678,0.3029,-0.1905,-0.9664,-0.1724,0.3023,-0.1818,-0.9668,-0.1794,0.3015,-0.1718,-0.9689,-0.1783,0.2988,-0.1655,-0.9702,-0.177,0.2975,-0.1465,-0.9738,-0.1741,0.2969,-0.1212,-0.9775,-0.1727,0.298,-0.0881,-0.9786,-0.1859,0.2986,-0.0618,-0.9781,-0.1987,0.2962,-0.0279,-0.9761,-0.2156,0.2926,-0.0011,-0.972,-0.2349,0.2902,0.0154,-0.9674,-0.2526,0.2877,0.0358,-0.963,-0.2671,0.2872,0.0519,-0.9604,-0.2739,0.2884,0.0594,-0.9568,-0.2846,0.29,0.0639,-0.9564,-0.2848,0.2925,0.069,-0.9537,-0.2927,0.2968,0.0657,-0.954,-0.2924,0.3004,0.0553,-0.9548,-0.292,0.3028,0.038,-0.9586,-0.2823,0.3015,0.0183,-0.9614,-0.2744,0.3003,-0.0089,-0.9641,-0.2653,0.298,-0.037,-0.9674,-0.2505,0.2958,-0.0743,-0.9678,-0.2403,0.2927,-0.1135,-0.9682,-0.2232,0.2909,-0.157,-0.9669,-0.2011,0.2884,-0.1963,-0.9639,-0.1797,0.2883,-0.243,-0.9572,-0.1574,0.2872,-0.2863,-0.9475,-0.1422,0.2855,-0.3334,-0.9338,-0.1297,0.2847,-0.3802,-0.9189,-0.1051,0.2832,-0.422,-0.903,-0.0808,0.2805,-0.4502,-0.8912,-0.0559,0.2803,-0.4681,-0.8832,-0.0299,0.2814,-0.4735,-0.8805,-0.0202,0.286,-0.4691,-0.8831,-0.0091,0.2869,-0.4564,-0.8898,-0.0035,0.2874,-0.4347,-0.9005,-0.0058,0.2866,-0.4019,-0.9156,-0.009,0.2858,-0.3578,-0.9335,-0.025,0.2864,-0.3177,-0.9477,-0.0304,0.2911,-0.2741,-0.9612,-0.0318,0.2962,-0.2478,-0.968,-0.0408,0.3016,-0.2253,-0.9733,-0.0441,0.3051,-0.2098,-0.9763,-0.0522,0.3059,-0.1994,-0.9779,-0.0632,0.3043,-0.1847,-0.9797,-0.0782,0.3005,-0.1797,-0.9795,-0.0909,0.2964,-0.1802,-0.9794,-0.0908,0.2932,-0.1926,-0.9771,-0.0904,0.2896,-0.2088,-0.9745,-0.0818,0.288,-0.2271,-0.9712,-0.072,0.2851,-0.2513,-0.9656,-0.0674,0.2845,-0.2699,-0.9605,-0.0679,0.2854,-0.2813,-0.9573,-0.0669,0.2845,-0.283,-0.9567,-0.0686,0.287,-0.2733,-0.9589,-0.0763,0.291,-0.2569,-0.9623,-0.0891,0.2952,-0.2379,-0.9662,-0.0989,0.2997,-0.2164,-0.9704,-0.1075,0.2997,-0.2011,-0.972,-0.1214,0.2988,-0.1811,-0.9741,-0.1351,0.299,-0.168,-0.9742,-0.1507,0.2986,-0.1462,-0.9742,-0.1719,0.301,-0.1249,-0.9738,-0.1898,0.307,-0.1056,-0.9716,-0.2115,0.3136,-0.0861,-0.971,-0.2232,0.321,-0.0796,-0.9679,-0.2384,0.3249,-0.0822,-0.9649,-0.2495,0.3261,-0.0919,-0.9617,-0.2583,0.3238,-0.1038,-0.9622,-0.2519,0.3208,-0.1159,-0.9625,-0.2453,0.318,-0.1338,-0.9617,-0.239,0.3133,-0.1507,-0.9604,-0.2345,0.3112,-0.1716,-0.9581,-0.2295,0.3107,-0.1922,-0.9567,-0.2187,0.3085,-0.1984,-0.9574,-0.2099,0.3084,-0.2069,-0.9578,-0.1994,0.3066,-0.2049,-0.9581,-0.2004,0.3055,-0.1916,-0.9605,-0.2019,0.3051,-0.1745,-0.9606,-0.2164,0.3025,-0.1601,-0.962,-0.2213,0.3016,-0.147,-0.9611,-0.2339,0.3027,-0.1398,-0.9609,-0.2391,0.3032,-0.135,-0.9604,-0.2435,0.3025,-0.1282,-0.9619,-0.2415,0.3008,-0.1307,-0.9623,-0.2387,0.2987,-0.1469,-0.9624,-0.2287,0.2957,-0.1666,-0.962,-0.2165,0.2929,-0.1867,-0.9604,-0.2068,0.2901,-0.2009,-0.9599,-0.1953,0.2855,-0.2177,-0.959,-0.1815,0.2843,-0.2302,-0.9582,-0.1702,0.2826,-0.2367,-0.9575,-0.1648,0.2815,-0.2334,-0.9577,-0.1685,0.2826,-0.212,-0.9612,-0.1765,0.2819,-0.1828,-0.9653,-0.1867,0.2858,-0.1512,-0.9673,-0.2038,0.288,-0.1287,-0.9681,-0.2148,0.2915,-0.1022,-0.9694,-0.223,0.2939,-0.0698,-0.9699,-0.2333,0.2961,-0.0492,-0.9704,-0.2365,0.2957,-0.0229,-0.9688,-0.2469,0.2964,0.0034,-0.9664,-0.257,0.2973,0.0294,-0.9633,-0.2669,0.2984,0.048,-0.9607,-0.2736,0.3036,0.0656,-0.9572,-0.2821,0.3062,0.079,-0.9528,-0.2931,0.3107,0.0963,-0.9469,-0.3069,0.3127,0.101,-0.9426,-0.3184,0.3109,0.0981,-0.941,-0.3239,0.3106,0.0907,-0.9436,-0.3185,0.3111,0.0736,-0.9453,-0.3179,0.3101,0.0507,-0.9465,-0.3187,0.3061,0.0273,-0.9473,-0.3192,0.3023,-0.0017,-0.9493,-0.3144,0.2976,-0.0385,-0.9472,-0.3182,0.2952,-0.0771,-0.9435,-0.3223,0.2952,-0.1174,-0.9406,-0.3184,0.2966,-0.1621,-0.9361,-0.3122,0.2989,-0.2027,-0.9312,-0.303,0.3021,-0.2386,-0.9276,-0.2876,0.3053,-0.2758,-0.9205,-0.2769,0.3098,-0.314,-0.9117,-0.2648,0.3133,-0.346,-0.904,-0.251,0.3164,-0.3799,-0.8952,-0.2331,0.3203,-0.4124,-0.8843,-0.2188,0.3202,-0.446,-0.8693,-0.213,0.32,-0.477,-0.8554,-0.2017,0.3174,-0.5117,-0.8379,-0.1901,0.3132,-0.5446,-0.8211,-0.1707,0.3109,-0.5714,-0.8051,-0.1588,0.3086,-0.5913,-0.7938,-0.1423,0.3082,-0.6,-0.7893,-0.1304,0.3094,-0.6041,-0.7877,-0.1205,0.3077,-0.5979,-0.7928,-0.1179,0.3076,-0.5842,-0.8024,-0.122,0.3042,-0.5619,-0.816,-0.1355,0.2986,-0.5319,-0.8334,-0.1503,0.2926,-0.4832,-0.859,-0.1689,0.2832,-0.4238,-0.8857,-0.1894,0.2758,-0.3551,-0.9108,-0.2105,0.2729,-0.2769,-0.9319,-0.2344,0.2758,-0.1973,-0.9462,-0.2563,0.2823,-0.1247,-0.9503,-0.2854,0.2879,-0.0563,-0.9477,-0.3143,0.2926,0.0081,-0.9359,-0.3522,0.2953,0.0697,-0.9172,-0.3923,0.2967,0.1226,-0.8946,-0.4297,0.2985,0.168,-0.8726,-0.4586,0.3021,0.2058,-0.8576,-0.4713,0.3077,0.2333,-0.8457,-0.48,0.3123,0.2536,-0.8358,-0.487,0.3169,0.2553,-0.8343,-0.4886,0.3159,0.2554,-0.834,-0.4891,0.3133,0.2331,-0.8406,-0.4889,0.3097,0.2082,-0.8477,-0.4879,0.3073,0.1746,-0.8631,-0.4739,0.3014,0.1415,-0.8754,-0.4623,0.2947,0.1059,-0.889,-0.4455,0.2887,0.0649,-0.9018,-0.4273,0.284,0.022,-0.9102,-0.4135,0.279,-0.0178,-0.9134,-0.4066,0.2771,-0.0585,-0.9124,-0.4052,0.2748,-0.0997,-0.911,-0.4002,0.2744,-0.1423,-0.9086,-0.3927,0.273,-0.188,-0.9061,-0.379,0.2712,-0.2281,-0.9012,-0.3686,0.2704,-0.2694,-0.8989,-0.3454,0.2667,-0.3121,-0.8922,-0.3263,0.2621,-0.3511,-0.8851,-0.3054,0.2567,-0.3862,-0.8798,-0.2773,0.251,-0.4142,-0.8742,-0.2535,0.2466,-0.4358,-0.8685,-0.2362,0.2426,-0.4529,-0.867,-0.2077,0.2399,-0.4635,-0.8645,-0.1947,0.2407,-0.4613,-0.8698,-0.1752,0.2421,-0.4561,-0.8751,-0.1618,0.2485,-0.438,-0.887,-0.146,0.2547,-0.4201,-0.8982,-0.1297,0.2645,-0.4089,-0.9058,-0.111,0.2736,-0.3939,-0.9136,-0.1007,0.2824,-0.3802,-0.9212,-0.0826,0.2905,-0.3707,-0.9263,-0.0669,0.2966,-0.3608,-0.9309,-0.0574,0.3016,-0.3568,-0.9327,-0.0531,0.3026,-0.3478,-0.9358,-0.057,0.3036,-0.333,-0.9409,-0.0622,0.3055,-0.3077,-0.949,-0.0689,0.3078,-0.2826,-0.9555,-0.0851,0.3108,-0.2657,-0.9586,-0.1027,0.3098,-0.2432,-0.962,-0.1242,0.3069,-0.2238,-0.9638,-0.145,0.3043,-0.2139,-0.9608,-0.1765,0.2998,-0.2131,-0.9566,-0.1986,0.2928,-0.2189,-0.9511,-0.218,0.2873,-0.2258,-0.9456,-0.2343,0.2818,-0.2488,-0.9375,-0.2432,0.2776,-0.273,-0.9298,-0.2471,0.2769,-0.2871,-0.9261,-0.2447,0.279,-0.3033,-0.9223,-0.2395,0.2828,-0.3177,-0.9178,-0.2381,0.2899,-0.3285,-0.9145,-0.2362,0.2962,-0.3379,-0.9106,-0.238,0.3025,-0.3432,-0.908,-0.2401,0.3083,-0.3458,-0.906,-0.2442,0.3109,-0.3414,-0.9071,-0.2463,0.3087,-0.3355,-0.9075,-0.2528,0.3062,-0.3355,-0.905,-0.2615,0.2983,-0.3251,-0.9075,-0.266,0.292,-0.3093,-0.9113,-0.2718,0.2849,-0.289,-0.9138,-0.2856,0.2788,-0.2742,-0.9175,-0.288,0.2742,-0.2534,-0.9226,-0.2909,0.2707,-0.2263,-0.9287,-0.2937,0.2701,-0.196,-0.9345,-0.2971,0.2691,-0.1681,-0.9401,-0.2967,0.2665,-0.1415,-0.9444,-0.2967,0.2639,-0.1096,-0.9449,-0.3085,0.2587,-0.0736,-0.9465,-0.3141,0.2541,-0.0475,-0.9474,-0.3165,0.2515,-0.0279,-0.9447,-0.3268,0.2489,-0.0088,-0.9481,-0.3178,0.2483,0,-0.9499,-0.3124,0.2482,0.0064,-0.9553,-0.2956,0.2496,0.0158,-0.9579,-0.2867,0.2475,0.0145,-0.9629,-0.2695,0.2427,0.0191,-0.9667,-0.255,0.2394,0.0273,-0.9724,-0.2317,0.2348,0.0341,-0.9786,-0.2031,0.2334,0.0441,-0.9819,-0.1842,0.2334,0.0703,-0.9808,-0.1818,0.2359,0.1004,-0.9767,-0.1896,0.2392,0.1353,-0.9699,-0.2023,0.2439,0.1752,-0.9603,-0.2171,0.2509,0.2022,-0.9508,-0.2345,0.2608,0.2198,-0.9434,-0.2485,0.2711,0.2155,-0.9445,-0.248,0.2766,0.2009,-0.9497,-0.2402,0.2762,0.1743,-0.9594,-0.2219,0.2759,0.1472,-0.9689,-0.199,0.2729,0.1186,-0.9763,-0.1809,0.2691,0.0845,-0.9808,-0.1758,0.2673,0.0481,-0.984,-0.1714,0.2655,0.0129,-0.985,-0.172,0.2675,-0.0252,-0.9839,-0.1771,0.2706,-0.0655,-0.9813,-0.181,0.2763,-0.1009,-0.9785,-0.1799,0.2831,-0.1477,-0.9728,-0.1785,0.2904,-0.1887,-0.9675,-0.1687,0.2967,-0.2244,-0.9607,-0.1635,0.3011,-0.2611,-0.9532,-0.1522,0.3028,-0.2945,-0.9446,-0.1445,0.3035,-0.3244,-0.936,-0.1365,0.3043,-0.3487,-0.9279,-0.1318,0.3023,-0.3684,-0.9213,-0.1246,0.3005,-0.3837,-0.9151,-0.1239,0.2984,-0.395,-0.9101,-0.1253,0.296,-0.4137,-0.9015,-0.1274,0.2937,-0.44,-0.8894,-0.1242,0.2937,-0.448,-0.8852,-0.1253,0.2921,-0.4547,-0.881,-0.1305,0.2848,-0.4492,-0.8815,-0.1454,0.2768,-0.4453,-0.8819,-0.155,0.267,-0.4385,-0.8853,-0.155,0.2619,-0.4206,-0.8938,-0.1558,0.2563,-0.4035,-0.9032,-0.1462,0.2536,-0.3741,-0.9175,-0.135,0.2514,-0.3403,-0.9319,-0.1253,0.2484,-0.3072,-0.9435,-0.124,0.2452,-0.2579,-0.9579,-0.1262,0.2387,-0.214,-0.9671,-0.1378,0.2334,-0.1546,-0.9774,-0.1443,0.2296,-0.1131,-0.9819,-0.1518,0.2271,-0.074,-0.9861,-0.149,0.2264,-0.0424,-0.9884,-0.146,0.2241,-0.011,-0.9894,-0.1445,0.2215,0.0114,-0.9897,-0.1428,0.2192,0.0296,-0.9885,-0.1483,0.2165,0.0398,-0.9888,-0.1436,0.2176,0.0338,-0.9904,-0.134,0.2209,0.0281,-0.9924,-0.12,0.2269])

Group366.addChildren(OrientationInterpolator389)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-8.160302,4.9E-324], [-10.282856,5.709675], [-18.069595,4.9E-324] degrees
#-3.038276 -2.695683 -17.044260, -3.173039 -2.685500 -16.975225, -3.236759 -2.694288 -16.951908, -3.278201 -2.801277 -16.891127, -3.354454 -2.836097 -16.877422, -3.425246 -2.816996 -16.831570, -3.513221 -2.645918 -16.790714, -3.435343 -2.459249 -16.666903, -3.381774 -2.348616 -16.614628, -3.279579 -2.031565 -16.627829, -3.207361 -1.611960 -16.738003, -3.355053 -1.024369 -16.777802, -3.476483 -0.548868 -16.622627, -3.632224 0.051148 -16.368502, -3.857817 0.529835 -16.152891, -4.076652 0.825428 -15.927710, -4.259197 1.184264 -15.810665, -4.350909 1.468075 -15.821504, -4.533524 1.624662 -15.840855, -4.563967 1.719429 -15.970753, -4.747699 1.855510 -16.153070, -4.804778 1.829579 -16.352146, -4.859013 1.672150 -16.502810, -4.715123 1.345039 -16.511299, -4.612236 0.987203 -16.513512, -4.488900 0.496315 -16.452084, -4.277091 -0.014433 -16.404318, -4.152136 -0.661875 -16.263243, -3.935186 -1.345443 -16.187069, -3.641361 -2.098724 -16.049826, -3.380809 -2.788617 -16.011442, -3.108384 -3.592112 -15.856604, -2.932581 -4.310992 -15.619919, -2.817217 -5.092356 -15.370347, -2.493457 -5.877699 -15.055402, -2.149905 -6.544142 -14.651957, -1.797365 -7.041009 -14.439983, -1.420419 -7.410280 -14.353994, -1.308529 -7.635469 -14.538056, -1.126749 -7.608803 -14.611930, -1.020082 -7.425097 -14.737721, -1.016794 -7.048173 -14.871422, -1.007247 -6.486712 -15.067690, -1.189975 -5.746553 -15.391425, -1.229824 -5.161088 -15.871852, -1.192246 -4.511606 -16.365561, -1.318885 -4.118335 -16.781076, -1.342288 -3.766446 -17.067190, -1.448619 -3.486931 -17.161886, -1.601565 -3.262657 -17.099051, -1.793190 -2.936534 -16.919312, -1.964202 -2.786063 -16.687321, -1.938324 -2.768300 -16.505754, -1.931621 -2.942194 -16.268528, -1.813756 -3.211833 -16.135675, -1.673150 -3.500592 -15.921735, -1.645820 -3.893785 -15.801250, -1.701528 -4.206222 -15.777701, -1.701863 -4.380197 -15.677043, -1.753378 -4.440660 -15.808029, -1.890803 -4.320504 -16.070265, -2.103883 -4.072744 -16.359219, -2.266168 -3.782611 -16.674627, -2.360082 -3.396589 -16.739115, -2.548197 -3.093726 -16.716755, -2.732032 -2.723082 -16.759661, -2.959556 -2.459800 -16.735064, -3.290191 -2.053090 -16.865265, -3.616567 -1.668126 -17.187088, -4.029756 -1.291964 -17.510679, -4.285402 -0.922668 -17.902458, -4.596975 -0.763990 -18.057606, -4.823849 -0.781917 -18.069595, -4.977468 -0.936215 -17.891865, -4.850467 -1.167652 -17.747738, -4.721468 -1.398168 -17.603384, -4.585950 -1.722516 -17.341312, -4.521121 -2.025128 -17.216402, -4.479328 -2.404128 -17.162111, -4.312415 -2.779205 -17.028156, -4.172729 -2.908540 -17.032942, -3.986545 -3.068475 -16.943409, -3.983059 -3.023073 -16.888325, -3.970985 -2.785855 -16.898561, -4.137971 -2.438227 -16.747780, -4.170830 -2.174591 -16.711040, -4.368653 -1.924734 -16.751036, -4.448112 -1.791273 -16.772465, -4.501572 -1.696519 -16.725254, -4.423375 -1.578365 -16.648880, -4.348835 -1.622044 -16.538143, -4.175269 -1.905891 -16.382244, -3.978975 -2.248515 -16.228172, -3.825432 -2.586305 -16.060329, -3.605387 -2.808180 -15.799911, -3.403504 -3.100324 -15.722653, -3.227839 -3.308984 -15.617292, -3.141369 -3.413703 -15.542647, -3.208451 -3.364660 -15.611465, -3.281017 -2.995975 -15.619033, -3.430947 -2.534379 -15.890022, -3.666496 -1.995761 -16.032291, -3.842694 -1.616750 -16.232506, -3.949810 -1.165554 -16.374557, -4.072503 -0.603533 -16.483177, -4.071422 -0.251453 -16.456547, -4.189995 0.214822 -16.449043, -4.309131 0.681010 -16.441822, -4.428824 1.147060 -16.434889, -4.571921 1.511583 -16.662092, -4.712132 1.853672 -16.728462, -4.936398 2.150735 -16.879774, -5.168016 2.504873 -16.866949, -5.332204 2.595946 -16.686460, -5.432518 2.554886 -16.640411, -5.362354 2.417797 -16.720587, -5.379704 2.108207 -16.712255, -5.384888 1.679484 -16.536917, -5.387121 1.250719 -16.362545, -5.294126 0.722933 -16.162024, -5.403421 0.105981 -16.029760, -5.561680 -0.531403 -15.996744, -5.618670 -1.217334 -16.057964, -5.666011 -1.993023 -16.145769, -5.669467 -2.724350 -16.267532, -5.556999 -3.404562 -16.406202, -5.552644 -4.125546 -16.560493, -5.502465 -4.878236 -16.624048, -5.398194 -5.532483 -16.675850, -5.233820 -6.257142 -16.741028, -5.051181 -6.890786 -16.559603, -5.016611 -7.521632 -16.304754, -4.826764 -8.061856 -15.930412, -4.609095 -8.621869 -15.422084, -4.280745 -9.201862 -15.011819, -4.068963 -9.642343 -14.616755, -3.802355 -10.024055 -14.392312, -3.624519 -10.242434 -14.361278, -3.428979 -10.282856 -14.237968, -3.375526 -10.175319 -14.316247, -3.378019 -9.816749 -14.313488, -3.493426 -9.231596 -14.278891, -3.606248 -8.516576 -14.270102, -3.686031 -7.426723 -14.204406, -3.793452 -6.261422 -14.222913, -3.953795 -5.083272 -14.429641, -4.229689 -3.850737 -14.880258, -4.523220 -2.600339 -15.418481, -4.929790 -1.388736 -15.744285, -5.331033 -0.205299 -15.907869, -5.865220 0.953404 -15.799833, -6.427789 2.067583 -15.492693, -6.989959 3.040758 -15.137938, -7.475790 3.906011 -14.878198, -7.753129 4.665461 -14.837188, -7.961443 5.239381 -14.800323, -8.157948 5.697874 -14.804476, -8.160302 5.709675 -14.729602, -8.108832 5.656813 -14.607107, -8.062877 5.198779 -14.584909, -8.034842 4.724060 -14.626186, -7.714232 4.030589 -14.662586, -7.420038 3.356771 -14.586955, -7.070675 2.668756 -14.563965, -6.743892 1.926469 -14.577709, -6.494870 1.181460 -14.496901, -6.422644 0.533110 -14.489091, -6.426718 -0.114196 -14.384882, -6.421210 -0.766008 -14.378004, -6.354543 -1.441554 -14.305281, -6.190893 -2.166905 -14.214726, -6.088057 -2.799737 -14.126286, -5.726153 -3.441199 -13.923828, -5.409429 -4.067279 -13.604625, -5.049684 -4.605231 -13.237341, -4.578748 -5.064677 -12.871148, -4.197196 -5.418097 -12.566969, -3.908481 -5.663916 -12.281560, -3.492779 -5.881174 -12.112642, -3.342621 -6.064600 -12.115916, -3.096595 -6.094299 -12.246515, -3.001761 -6.191358 -12.638146, -2.843435 -6.094708 -13.110293, -2.709600 -6.070873 -13.768378, -2.523210 -6.127499 -14.351709, -2.439274 -6.092661 -14.929269, -2.208709 -6.068038 -15.467223, -1.990504 -6.064586 -15.863581, -1.855038 -6.013410 -16.197268, -1.783591 -5.973846 -16.280436, -1.838669 -5.828228 -16.386497, -1.912972 -5.591213 -16.574574, -1.989810 -5.171443 -16.839060, -2.240697 -4.734076 -17.119286, -2.496378 -4.375818 -17.120008, -2.784879 -3.893279 -17.021999, -3.065461 -3.477067 -16.907904, -3.520414 -3.188282 -16.612190, -3.789351 -3.061322 -16.158243, -4.036616 -3.067680 -15.773149, -4.225785 -3.099444 -15.394328, -4.342393 -3.408832 -15.052974, -4.437232 -3.776436 -14.908484, -4.466722 -4.032012 -14.975649, -4.482490 -4.350502 -15.127823, -4.617665 -4.686294 -15.451461, -4.723429 -4.960260 -15.743101, -4.888343 -5.210808 -16.024220, -5.044889 -5.385431 -16.297741, -5.171616 -5.461156 -16.407885, -5.156779 -5.346757 -16.308485, -5.206849 -5.190795 -16.181595, -5.198350 -5.056809 -15.717059, -5.127759 -4.783499 -15.418278, -5.050268 -4.413500 -15.087887, -5.106794 -3.983332 -14.792031, -5.023747 -3.691200 -14.591442, -4.959146 -3.324800 -14.465294, -4.937855 -2.893326 -14.507779, -4.913650 -2.414562 -14.523329, -4.806451 -1.972258 -14.448750, -4.706628 -1.560109 -14.355755, -4.725446 -1.050610 -14.058448, -4.656411 -0.513013 -13.806784, -4.599262 -0.136076 -13.666937, -4.663968 0.151719 -13.472824, -4.494621 0.405155 -13.479307, -4.401703 0.521072 -13.494617, -4.177505 0.592830 -13.647253, -3.999979 0.701447 -13.562801, -3.690526 0.635654 -13.375665, -3.436717 0.662739 -13.244077, -3.047838 0.718211 -13.065136, -2.641462 0.760650 -13.071710, -2.374731 0.865120 -13.115138, -2.326155 1.223751 -13.234367, -2.415203 1.665728 -13.355845, -2.579600 2.205733 -13.506387, -2.791139 2.866711 -13.738086, -3.099147 3.421233 -14.122196, -3.388671 3.866669 -14.549656, -3.447136 3.883948 -14.860752, -3.346375 3.636161 -14.930720, -3.106962 3.182895 -15.085898, -2.775019 2.682554 -15.091341, -2.518915 2.171450 -15.007937, -2.492671 1.629894 -14.987034, -2.484140 1.061870 -14.950997, -2.579654 0.540425 -15.085224, -2.765895 -0.022803 -15.259145, -2.969134 -0.637610 -15.553392, -3.107171 -1.212788 -15.910526, -3.275892 -2.007213 -16.246847, -3.288092 -2.752848 -16.533842, -3.341343 -3.410985 -16.683447, -3.259386 -4.085835 -16.663784, -3.216225 -4.691795 -16.574009, -3.157616 -5.238605 -16.477602, -3.105029 -5.639218 -16.239717, -3.001349 -5.962741 -16.035425, -2.996213 -6.189526 -15.828755, -3.010047 -6.329943 -15.621245, -3.048723 -6.594464 -15.363843, -3.045230 -7.045184 -15.178311, -3.054850 -7.142027 -15.029889, -3.050027 -7.072591 -14.585212, -3.163747 -6.768710 -14.185226, -3.161337 -6.466885 -13.685386, -3.077846 -6.248502 -13.467278, -2.983431 -5.858132 -13.291263, -2.783285 -5.565953 -13.269973, -2.552565 -5.115181 -13.338671, -2.331740 -4.594043 -13.368472, -2.228406 -4.076259 -13.343527, -2.114330 -3.298835 -13.166446, -2.150629 -2.629865 -12.988220, -2.111004 -1.804738 -12.894673, -2.122947 -1.239660 -12.800999, -2.024437 -0.737047 -12.807662, -1.919426 -0.333254 -12.696501, -1.834022 0.062192 -12.554565, -1.764251 0.336037 -12.426515, -1.786777 0.560324 -12.253061, -1.723755 0.683519 -12.317791, -1.635900 0.609710 -12.529258, -1.505791 0.536854 -12.893166
#Interpolator19_r_wrist channels [57..59] sends animation values to BVH JOINT RightWrist, DEF Bvh1_r_wrist, <HAnimJoint name=r_wrist/>
OrientationInterpolator390 = OrientationInterpolator()
OrientationInterpolator390.setDEF("Interpolator19_r_wrist")
OrientationInterpolator390.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator390.setKeyValue([0.5547,-0.1919,0.8096,0.056,0.5528,-0.1923,0.8108,0.0556,0.5509,-0.1926,0.812,0.0551,0.5636,-0.2209,0.796,0.0548,0.5636,-0.2209,0.796,0.0548,0.5636,-0.2209,0.796,0.0548,0.5636,-0.2209,0.796,0.0548,0.5834,-0.2363,0.7771,0.0549,0.6077,-0.2101,0.7659,0.0566,0.6084,-0.1859,0.7715,0.0574,0.598,-0.1716,0.7829,0.0586,0.5807,-0.1365,0.8026,0.0612,0.612,-0.0922,0.7854,0.0617,0.6169,-0.0334,0.7864,0.0627,0.6236,0.0192,0.7815,0.0662,0.6518,0.054,0.7565,0.0707,0.675,0.0819,0.7332,0.073,0.6939,0.1138,0.7111,0.0755,0.7086,0.1295,0.6936,0.0798,0.7146,0.1456,0.6842,0.0806,0.714,0.1408,0.6858,0.0834,0.6979,0.1473,0.7009,0.0848,0.6792,0.1462,0.7192,0.085,0.6538,0.1406,0.7435,0.0823,0.6216,0.129,0.7726,0.0803,0.5789,0.1101,0.8079,0.0757,0.5351,0.0905,0.8399,0.0696,0.4736,0.0531,0.8791,0.0671,0.4295,0.0386,0.9023,0.0671,0.4159,0.0122,0.9093,0.0666,0.4137,-0.0047,0.9104,0.0693,0.4307,-0.0125,0.9024,0.0719,0.4376,0.016,0.899,0.0743,0.4296,0.0079,0.903,0.0779,0.4432,0.0119,0.8963,0.0777,0.4526,0.0184,0.8915,0.0757,0.4139,0.0142,0.9102,0.075,0.3997,-0.0065,0.9166,0.0705,0.3794,-0.0259,0.9249,0.0689,0.3224,-0.0397,0.9458,0.0657,0.2935,-0.0678,0.9536,0.0621,0.2965,-0.0867,0.9511,0.0616,0.2959,-0.0924,0.9507,0.0604,0.2346,-0.1068,0.9662,0.0623,0.1501,-0.1093,0.9826,0.0633,-0.0113,-0.1711,0.9852,0.0648,-0.1409,-0.2264,0.9638,0.0674,-0.2654,-0.2667,0.9265,0.0668,-0.3505,-0.2883,0.8911,0.0646,-0.393,-0.2718,0.8785,0.0629,-0.4082,-0.2379,0.8813,0.0626,-0.3943,-0.1993,0.8971,0.0622,-0.3395,-0.18,0.9232,0.0632,-0.2896,-0.168,0.9423,0.0643,-0.2481,-0.1227,0.9609,0.0656,-0.2313,-0.116,0.9659,0.0662,-0.1959,-0.0822,0.9772,0.0668,-0.1616,-0.0196,0.9867,0.069,-0.1411,0.0094,0.9899,0.0705,-0.1409,0.0403,0.9892,0.0708,-0.1032,0.0878,0.9908,0.072,-0.1003,0.077,0.992,0.0729,-0.0799,0.0921,0.9925,0.0738,-0.0483,0.1048,0.9933,0.0744,0.0123,0.1347,0.9908,0.0766,0.071,0.1695,0.983,0.0768,0.1448,0.188,0.9714,0.0772,0.1936,0.2047,0.9595,0.0792,0.2206,0.2079,0.9529,0.0814,0.2214,0.1793,0.9586,0.081,0.2236,0.164,0.9608,0.0782,0.2545,0.1596,0.9538,0.0763,0.254,0.1754,0.9512,0.0729,0.2756,0.2022,0.9398,0.0711,0.3111,0.236,0.9206,0.0705,0.3121,0.2604,0.9136,0.072,0.3359,0.257,0.9062,0.073,0.348,0.2502,0.9035,0.0738,0.356,0.2441,0.902,0.0732,0.354,0.2362,0.9049,0.0733,0.2945,0.2359,0.9261,0.0711,0.2743,0.2429,0.9305,0.0678,0.244,0.2454,0.9382,0.067,0.217,0.2697,0.9382,0.0666,0.1986,0.2637,0.944,0.0656,0.1973,0.2592,0.9454,0.0652,0.2061,0.2782,0.9381,0.067,0.2432,0.2817,0.9282,0.068,0.2809,0.2795,0.9181,0.0671,0.3001,0.2899,0.9088,0.0667,0.2999,0.31,0.9022,0.0679,0.2931,0.321,0.9006,0.0678,0.3112,0.3065,0.8996,0.0691,0.2955,0.2814,0.913,0.0701,0.2451,0.2539,0.9357,0.0681,0.2252,0.248,0.9422,0.0666,0.2236,0.2284,0.9475,0.0646,0.2162,0.2354,0.9476,0.0645,0.2291,0.2121,0.95,0.0631,0.2408,0.1816,0.9534,0.0606,0.2814,0.2003,0.9385,0.06,0.3276,0.2109,0.921,0.0606,0.4114,0.2476,0.8772,0.0638,0.4951,0.2747,0.8243,0.0677,0.5462,0.2943,0.7843,0.0716,0.6212,0.3109,0.7194,0.0751,0.6618,0.3286,0.6738,0.079,0.6865,0.3353,0.6452,0.0822,0.6946,0.3578,0.624,0.0859,0.7074,0.3795,0.5963,0.0911,0.7277,0.3658,0.5802,0.0969,0.7444,0.3784,0.5502,0.1027,0.7486,0.3842,0.5404,0.1084,0.7608,0.3753,0.5295,0.1161,0.7694,0.3749,0.5172,0.1236,0.7674,0.3787,0.5174,0.1284,0.7663,0.3803,0.5179,0.1348,0.7652,0.3632,0.5315,0.1405,0.7522,0.3646,0.5489,0.1398,0.7367,0.363,0.5705,0.1391,0.7197,0.3558,0.5962,0.1353,0.6975,0.3396,0.631,0.1308,0.6736,0.3343,0.6592,0.1244,0.648,0.3035,0.6985,0.1149,0.602,0.2672,0.7524,0.1041,0.5382,0.2306,0.8106,0.0932,0.4594,0.1808,0.8696,0.0847,0.4007,0.1142,0.9091,0.0789,0.3419,0.0863,0.9358,0.0744,0.3166,0.0614,0.9466,0.0709,0.2621,0.0173,0.9649,0.0713,0.2433,0.001,0.97,0.0727,0.2084,0.009,0.978,0.0749,0.1708,-0.0081,0.9853,0.0768,0.1733,-0.0186,0.9847,0.0776,0.141,-0.0243,0.9897,0.0789,0.1252,-0.0245,0.9918,0.079,0.1157,-0.0276,0.9929,0.0785,0.0996,-0.0295,0.9946,0.0794,0.1044,-0.0159,0.9944,0.0804,0.1317,-0.0067,0.9913,0.0798,0.1616,0.0218,0.9866,0.0815,0.2052,0.0695,0.9762,0.0832,0.2401,0.0936,0.9662,0.084,0.3103,0.1392,0.9404,0.0873,0.4153,0.1834,0.891,0.0932,0.4736,0.2146,0.8542,0.1023,0.5031,0.2179,0.8363,0.1115,0.5411,0.259,0.8001,0.1207,0.6135,0.2938,0.733,0.1313,0.6802,0.3271,0.656,0.1447,0.7378,0.3342,0.5865,0.1614,0.778,0.3455,0.5247,0.1747,0.7924,0.3561,0.4953,0.185,0.8075,0.3632,0.4648,0.1867,0.8132,0.3702,0.4491,0.1819,0.8116,0.3784,0.4451,0.1723,0.8075,0.3888,0.4436,0.1589,0.798,0.4044,0.4467,0.1458,0.7934,0.4177,0.4427,0.1363,0.7784,0.42,0.4666,0.1299,0.7711,0.4044,0.4918,0.126,0.7413,0.3963,0.5417,0.1237,0.705,0.3761,0.6012,0.1217,0.6567,0.3607,0.6624,0.1172,0.5985,0.3438,0.7236,0.1092,0.5029,0.3195,0.8031,0.1001,0.3844,0.2813,0.8793,0.0889,0.2446,0.2354,0.9406,0.0809,0.0916,0.1787,0.9796,0.0741,-0.0416,0.1224,0.9916,0.0682,-0.1309,0.0828,0.9879,0.0671,-0.189,0.0476,0.9808,0.0655,-0.248,0.0231,0.9685,0.0676,-0.2695,0.0046,0.963,0.068,-0.2694,-0.0148,0.9629,0.0696,-0.2258,-0.0059,0.9742,0.0706,-0.1723,0.0103,0.985,0.0722,-0.1228,0.0236,0.9922,0.0707,-0.0232,0.0447,0.9987,0.0733,0.0872,0.0497,0.995,0.0748,0.2183,0.0661,0.9736,0.0789,0.3169,0.0758,0.9454,0.0857,0.4174,0.0628,0.9065,0.0929,0.4864,0.0416,0.8727,0.1017,0.5344,0.0346,0.8445,0.1105,0.5673,0.0389,0.8226,0.1164,0.5816,0.0456,0.8122,0.1219,0.595,0.055,0.8019,0.1259,0.5912,0.0586,0.8044,0.1299,0.5922,0.0678,0.803,0.1342,0.5854,0.0834,0.8065,0.1373,0.5792,0.0914,0.8101,0.1373,0.5796,0.0992,0.8088,0.1385,0.5858,0.1075,0.8033,0.1402,0.5812,0.1284,0.8035,0.1413,0.5864,0.163,0.7934,0.1456,0.5939,0.1921,0.7813,0.1514,0.6074,0.2018,0.7683,0.1579,0.6084,0.2147,0.764,0.1621,0.5935,0.2137,0.7759,0.1632,0.5725,0.2006,0.795,0.1576,0.5385,0.1796,0.8232,0.1501,0.4839,0.1501,0.8622,0.138,0.413,0.1057,0.9046,0.1247,0.3169,0.0564,0.9468,0.1124,0.1953,-0.0005,0.9807,0.1017,0.0846,-0.0653,0.9943,0.0931,-0.0113,-0.0992,0.995,0.0884,-0.0847,-0.1209,0.9891,0.0852,-0.136,-0.1368,0.9812,0.0835,-0.1567,-0.1136,0.9811,0.0826,-0.1099,-0.103,0.9886,0.0822,-0.0734,-0.0589,0.9956,0.0828,-0.0414,-0.0103,0.9991,0.0838,0.0034,0.0186,0.9998,0.0843,0.0318,0.0384,0.9988,0.0826,0.0448,0.0715,0.9964,0.0819,0.0811,0.0968,0.992,0.0818,0.1172,0.1221,0.9856,0.0818,0.1279,0.1459,0.981,0.0837,0.167,0.1903,0.9674,0.0861,0.1831,0.2218,0.9578,0.0914,0.2007,0.2538,0.9462,0.0975,0.2488,0.2911,0.9238,0.103,0.3008,0.2944,0.9071,0.1094,0.341,0.3114,0.887,0.1139,0.381,0.3159,0.8689,0.1186,0.4017,0.3481,0.847,0.1207,0.3943,0.3507,0.8495,0.1223,0.4051,0.3571,0.8416,0.1208,0.3974,0.3805,0.8351,0.1187,0.3788,0.3847,0.8417,0.114,0.3702,0.3977,0.8395,0.1097,0.3257,0.4045,0.8546,0.1048,0.2847,0.4138,0.8647,0.1019,0.2837,0.4264,0.8589,0.0989,0.2847,0.4219,0.8608,0.1001,0.3164,0.4345,0.8433,0.1011,0.3642,0.443,0.8192,0.1035,0.412,0.4559,0.7889,0.1089,0.4734,0.4651,0.7481,0.1123,0.4917,0.4673,0.7348,0.1123,0.4889,0.4748,0.7318,0.1127,0.4694,0.4648,0.7508,0.1108,0.4284,0.4559,0.7801,0.1081,0.3557,0.4442,0.8223,0.1054,0.304,0.4251,0.8525,0.1,0.252,0.3988,0.8817,0.0949,0.2026,0.3795,0.9027,0.0909,0.1453,0.3534,0.9241,0.0869,0.0826,0.3229,0.9428,0.0843,0.0295,0.2832,0.9586,0.0836,-0.0174,0.2385,0.971,0.0848,-0.1086,0.1972,0.9743,0.086,-0.1626,0.1639,0.973,0.0872,-0.2084,0.1244,0.9701,0.0902,-0.2397,0.1053,0.9651,0.0919,-0.2579,0.0916,0.9618,0.0935,-0.2763,0.0911,0.9568,0.0953,-0.2622,0.1135,0.9583,0.0958,-0.2487,0.1068,0.9627,0.0942,-0.2301,0.1094,0.967,0.0944,-0.2175,0.1175,0.969,0.0947,-0.2068,0.1363,0.9688,0.0938,-0.1929,0.157,0.9686,0.091,-0.1869,0.1729,0.967,0.091,-0.1932,0.186,0.9634,0.0914,-0.1739,0.2269,0.9583,0.0885,-0.1417,0.2522,0.9573,0.0879,-0.0943,0.2802,0.9553,0.0875,-0.0677,0.3089,0.9487,0.0853,-0.0089,0.348,0.9375,0.0862,0.0763,0.3807,0.9215,0.0857,0.1287,0.4178,0.8994,0.0879,0.2326,0.4526,0.8608,0.0903,0.3075,0.4979,0.8109,0.0946,0.3939,0.5096,0.7649,0.1005,0.4741,0.5201,0.7104,0.1073,0.5279,0.5096,0.6795,0.1134,0.5408,0.5205,0.6608,0.1188,0.551,0.5295,0.645,0.1223,0.5401,0.5412,0.6445,0.1197,0.5115,0.5535,0.6573,0.1133,0.4798,0.5567,0.6781,0.1033,0.4128,0.5701,0.7103,0.0921])

Group366.addChildren(OrientationInterpolator390)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [2.456646,7.178621], [-1.486638,8.788413], [-1.029227,3.571787] degrees
#2.609710 1.766516 -0.656470, 2.591541 1.745618 -0.651706, 2.573301 1.724784 -0.647000, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.456646 1.818346 -0.782432, 2.497362 1.956090 -0.724531, 2.547518 1.985646 -0.655483, 2.638535 1.992728 -0.622024, 2.822679 2.022872 -0.528548, 2.783255 2.154312 -0.378447, 2.827835 2.211573 -0.174673, 2.966454 2.367945 0.011768, 3.061421 2.644875 0.148318, 3.060796 2.831178 0.267117, 3.066253 3.013679 0.411704, 3.159835 3.256714 0.502920, 3.144267 3.317638 0.581686, 3.262764 3.431193 0.575882, 3.389136 3.411379 0.615320, 3.487574 3.329128 0.611571, 3.491598 3.101521 0.568892, 3.541601 2.875596 0.504479, 3.497271 2.524889 0.400633, 3.341896 2.141649 0.298143, 3.375993 1.824663 0.150344, 3.468760 1.655123 0.098415, 3.468958 1.587139 -0.001426, 3.617346 1.641407 -0.070653, 3.721347 1.772506 -0.108926, 3.824912 1.862581 0.006109, 4.032639 1.917917 -0.032100, 3.992694 1.974164 -0.015752, 3.867841 1.964866 0.013598, 3.911627 1.779103 0.000452, 3.702141 1.611857 -0.078364, 3.651941 1.492803 -0.149983, 3.562690 1.208382 -0.187226, 3.394138 1.036159 -0.271922, 3.357769 1.036099 -0.336150, 3.295940 1.015112 -0.349175, 3.449153 0.824696 -0.405887, 3.565457 0.531763 -0.413232, 3.658690 -0.062138 -0.633820, 3.715758 -0.571864 -0.855765, 3.537050 -1.046493 -0.988707, 3.286674 -1.327173 -1.029227, 3.155375 -1.443082 -0.940426, 3.150302 -1.486638 -0.812448, 3.190036 -1.424879 -0.671186, 3.338912 -1.248655 -0.616267, 3.468783 -1.085750 -0.586551, 3.605629 -0.945630 -0.431275, 3.658360 -0.890390 -0.411479, 3.736752 -0.759408 -0.289796, 3.898445 -0.640889 -0.055670, 3.996348 -0.567845 0.057673, 4.015692 -0.565568 0.183632, 4.089818 -0.412534 0.377172, 4.146720 -0.407018 0.336773, 4.198324 -0.323280 0.401580, 4.236970 -0.189247 0.454345, 4.347973 0.076507 0.588716, 4.323826 0.340251 0.733516, 4.292437 0.670870 0.807026, 4.348366 0.913239 0.894975, 4.436174 1.065549 0.928852, 4.440114 1.058259 0.791183, 4.297723 1.028319 0.696289, 4.165938 1.137442 0.656905, 3.966641 1.085614 0.695216, 3.821973 1.149549 0.786012, 3.710192 1.287091 0.912316, 3.758895 1.322547 1.031811, 3.778157 1.439755 1.028016, 3.804880 1.504585 1.007598, 3.772261 1.526406 0.974293, 3.787666 1.518317 0.942191, 3.761770 1.229793 0.920513, 3.607916 1.095199 0.910055, 3.591836 0.965124 0.911397, 3.572788 0.859712 1.002569, 3.543512 0.776950 0.967856, 3.527230 0.766862 0.945530, 3.592711 0.824003 1.042235, 3.606554 0.981228 1.066815, 3.520762 1.112436 1.041098, 3.462283 1.179569 1.072517, 3.498291 1.203131 1.169989, 3.488258 1.176765 1.212472, 3.548696 1.268652 1.174410, 3.653401 1.221396 1.091068, 3.644977 0.987682 0.960030, 3.587633 0.888106 0.918511, 3.502422 0.853340 0.820066, 3.495017 0.824862 0.844745, 3.431740 0.851256 0.741975, 3.304274 0.853369 0.605805, 3.222446 0.986675 0.661551, 3.191320 1.157573 0.700467, 3.194075 1.527976 0.862452, 3.178567 1.947787 1.011074, 3.194157 2.272527 1.143861, 3.067826 2.708904 1.266654, 3.014899 3.034764 1.409054, 2.996991 3.272868 1.494379, 3.020661 3.462350 1.669930, 3.053185 3.744555 1.882853, 3.153502 4.093783 1.918935, 3.157214 4.438551 2.105475, 3.264934 4.713367 2.252724, 3.420915 5.134163 2.346133, 3.546325 5.528796 2.487097, 3.679927 5.731876 2.605094, 3.860155 6.013876 2.737916, 4.136775 6.262952 2.702362, 4.257153 6.128742 2.696179, 4.413658 5.980105 2.667713, 4.498665 5.680610 2.537950, 4.623168 5.323748 2.333003, 4.606783 4.890638 2.187691, 4.532002 4.341436 1.828472, 4.444507 3.650190 1.454080, 4.302584 2.918533 1.123233, 4.202941 2.258538 0.794406, 4.105155 1.829636 0.451094, 3.987128 1.469597 0.317206, 3.845129 1.294009 0.206231, 3.940210 1.071800 0.033911, 4.043222 1.013302 -0.031399, 4.195504 0.894460 0.005893, 4.336459 0.749749 -0.064048, 4.380551 0.767012 -0.111951, 4.476020 0.632756 -0.134787, 4.490328 0.561642 -0.133104, 4.466521 0.515244 -0.144245, 4.527095 0.447300 -0.152167, 4.579456 0.477261 -0.092139, 4.531847 0.600354 -0.054204, 4.605219 0.757764 0.071504, 4.653720 0.991235 0.291282, 4.644312 1.171796 0.403046, 4.692876 1.578039 0.631508, 4.741666 2.256210 0.886786, 4.981188 2.828020 1.136423, 5.307639 3.272872 1.241454, 5.481036 3.821904 1.610268, 5.437832 4.715100 1.989678, 5.322356 5.759709 2.448527, 5.262897 6.956882 2.777122, 5.045299 7.930885 3.116274, 5.007168 8.557764 3.410101, 4.711544 8.788413 3.532429, 4.425086 8.618318 3.533709, 4.157495 8.143188 3.447216, 3.830289 7.465457 3.295743, 3.550007 6.769403 3.173775, 3.292316 6.288131 3.085796, 3.323904 5.881514 2.958260, 3.416953 5.649967 2.753599, 3.718779 5.341076 2.637790, 4.088656 5.006107 2.446630, 4.363964 4.499816 2.253824, 4.461232 3.823933 2.003320, 4.562994 2.954117 1.715938, 4.455107 2.011667 1.355090, 4.348244 1.173957 1.046626, 4.159241 0.416373 0.744220, 3.878191 -0.146459 0.483840, 3.802101 -0.492538 0.335120, 3.681212 -0.702899 0.201115, 3.753507 -0.957291 0.120798, 3.751885 -1.048348 0.052433, 3.838710 -1.075086 -0.023061, 3.941370 -0.913584 0.007368, 4.077155 -0.710841 0.067974, 4.021138 -0.493783 0.113109, 4.192567 -0.090379 0.191119, 4.265887 0.381359 0.199195, 4.396726 0.996866 0.260430, 4.637878 1.569224 0.308649, 4.819003 2.232227 0.240338, 5.083901 2.841405 0.116490, 5.348825 3.389904 0.061128, 5.484107 3.788867 0.078171, 5.671214 4.071801 0.117036, 5.778224 4.302830 0.179695, 5.984050 4.416688 0.206002, 6.164649 4.571058 0.275744, 6.330037 4.630530 0.401026, 6.359154 4.588037 0.465473, 6.399112 4.633233 0.529274, 6.432635 4.745173 0.598181, 6.476054 4.753545 0.771733, 6.575794 4.958569 1.076699, 6.717582 5.236322 1.361264, 6.884017 5.591733 1.493165, 7.019921 5.758934 1.644916, 7.178621 5.659254 1.647058, 7.114531 5.268462 1.486865, 7.033399 4.715368 1.258053, 6.785652 3.886451 0.957835, 6.448216 2.986852 0.587559, 6.095248 2.056996 0.253951, 5.716551 1.136121 -0.059571, 5.303021 0.434514 -0.368557, 5.039319 -0.079251 -0.499075, 4.827057 -0.437709 -0.572066, 4.689123 -0.676466 -0.626956, 4.640162 -0.762470 -0.507007, 4.652785 -0.536442 -0.463485, 4.724301 -0.359404 -0.265021, 4.795363 -0.200408 -0.040887, 4.829113 0.020305 0.089064, 4.727686 0.157978 0.175518, 4.674071 0.223846 0.326485, 4.645977 0.398000 0.437760, 4.615845 0.571808 0.549512, 4.699035 0.641097 0.673296, 4.764174 0.861556 0.903415, 5.006110 1.008186 1.117992, 5.270810 1.184520 1.364237, 5.430277 1.547521 1.645999, 5.655989 1.973009 1.749372, 5.749415 2.323365 1.917190, 5.860627 2.695108 2.011161, 5.802779 2.895799 2.263206, 5.896626 2.884801 2.311376, 5.768037 2.924230 2.327038, 5.622861 2.826566 2.452531, 5.447722 2.591182 2.392977, 5.229531 2.439090 2.391254, 5.089054 2.060736 2.338355, 5.015532 1.766368 2.340999, 4.834675 1.708341 2.346365, 4.901945 1.734669 2.347052, 4.844102 1.936747 2.436603, 4.810528 2.268255 2.534630, 4.860759 2.688789 2.733017, 4.736041 3.166318 2.863721, 4.649082 3.283733 2.877078, 4.645667 3.279725 2.936363, 4.692152 3.098269 2.826031, 4.767061 2.767752 2.709860, 4.918048 2.261921 2.588167, 4.846825 1.842797 2.359103, 4.769948 1.459683 2.109476, 4.684646 1.135207 1.932150, 4.587901 0.793034 1.727886, 4.548129 0.460378 1.542455, 4.592036 0.195497 1.350232, 4.717709 -0.036784 1.160607, 4.805299 -0.493930 0.992772, 4.867844 -0.776893 0.852458, 5.019173 -1.047115 0.689119, 5.088356 -1.235900 0.609737, 5.159803 -1.357874 0.552079, 5.231793 -1.483777 0.565409, 5.267893 -1.408280 0.688241, 5.202056 -1.313708 0.636508, 5.238701 -1.215977 0.647841, 5.264812 -1.149316 0.691081, 5.215518 -1.076591 0.782431, 5.058992 -0.968773 0.861934, 5.050659 -0.933754 0.943135, 5.053639 -0.967311 1.017240, 4.869430 -0.832179 1.186766, 4.826537 -0.658884 1.298053, 4.795041 -0.413694 1.422978, 4.639856 -0.269186 1.521027, 4.628968 0.025500 1.718026, 4.518999 0.448081 1.853044, 4.518989 0.731057 2.077240, 4.426625 1.292210 2.291998, 4.353678 1.767168 2.631521, 4.347259 2.377491 2.846277, 4.288334 3.032555 3.086150, 4.319291 3.552707 3.180204, 4.387262 3.814030 3.399403, 4.399560 4.001153 3.560441, 4.305292 3.842644 3.571787, 4.163692 3.448258 3.469280, 3.931834 2.950572 3.194955, 3.692430 2.274818 2.937333
#Interpolator20_Neck channels [60..62] sends animation values to BVH JOINT Neck, DEF Bvh1_Neck, <HAnimJoint name=Neck/>
OrientationInterpolator391 = OrientationInterpolator()
OrientationInterpolator391.setDEF("Interpolator20_Neck")
OrientationInterpolator391.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator391.setKeyValue([0.7404,-0.5674,0.3603,0.0527,0.743,-0.5847,0.3256,0.0515,0.7528,-0.6008,0.2688,0.0502,0.7658,-0.6017,0.2267,0.0497,0.7779,-0.5939,0.2052,0.0503,0.7893,-0.5858,0.184,0.0508,0.7989,-0.5772,0.1691,0.0522,0.8026,-0.5757,0.1562,0.0549,0.8202,-0.5515,0.1523,0.0579,0.8352,-0.5298,0.1473,0.0611,0.8372,-0.5305,0.1328,0.0624,0.8451,-0.5157,0.1408,0.0647,0.8442,-0.517,0.1419,0.0673,0.8434,-0.5174,0.1445,0.0696,0.8356,-0.5307,0.1417,0.0719,0.8235,-0.5494,0.1411,0.0749,0.8063,-0.5713,0.1533,0.0779,0.793,-0.5895,0.1538,0.0826,0.7684,-0.6196,0.16,0.0855,0.7513,-0.6359,0.1767,0.0899,0.7361,-0.6517,0.1831,0.0941,0.7282,-0.6575,0.1932,0.0983,0.7243,-0.653,0.2212,0.1022,0.7158,-0.6524,0.249,0.1063,0.7145,-0.6418,0.2784,0.1103,0.7114,-0.6278,0.3159,0.1137,0.7008,-0.614,0.3632,0.1169,0.6844,-0.599,0.4157,0.1196,0.6693,-0.5863,0.4565,0.122,0.6583,-0.5672,0.495,0.1235,0.6487,-0.5459,0.5303,0.1234,0.6393,-0.5301,0.557,0.1228,0.6217,-0.5168,0.5886,0.1214,0.6012,-0.5058,0.6187,0.1196,0.5854,-0.4978,0.6399,0.1184,0.5662,-0.4991,0.656,0.1171,0.5475,-0.4911,0.6775,0.1165,0.5225,-0.4896,0.6981,0.1174,0.4936,-0.49,0.7185,0.1191,0.4708,-0.4938,0.7311,0.121,0.4606,-0.5047,0.7302,0.1225,0.4488,-0.5153,0.7301,0.1233,0.4373,-0.5355,0.7225,0.1222,0.4249,-0.5611,0.7104,0.1201,0.4157,-0.5782,0.702,0.1174,0.4092,-0.5966,0.6904,0.1139,0.4015,-0.6117,0.6817,0.11,0.3962,-0.6309,0.6671,0.1075,0.3966,-0.6412,0.657,0.1053,0.3961,-0.6478,0.6507,0.1031,0.4061,-0.6601,0.632,0.1,0.4234,-0.6599,0.6207,0.098,0.4386,-0.6676,0.6016,0.0963,0.4633,-0.6772,0.5716,0.0954,0.4854,-0.6801,0.5494,0.0956,0.5041,-0.6818,0.5301,0.0945,0.5166,-0.6881,0.5095,0.0953,0.5363,-0.6892,0.4872,0.0961,0.5708,-0.6829,0.4559,0.0992,0.6043,-0.665,0.4389,0.1018,0.6297,-0.6491,0.4267,0.1048,0.6429,-0.646,0.4114,0.1073,0.6574,-0.6391,0.3992,0.1088,0.6595,-0.6431,0.3891,0.1092,0.6704,-0.6422,0.3717,0.1086,0.6835,-0.6288,0.3708,0.1085,0.6858,-0.6234,0.3756,0.1076,0.6936,-0.6075,0.3872,0.107,0.7067,-0.5829,0.4011,0.1057,0.724,-0.5513,0.4146,0.1043,0.7373,-0.5128,0.4397,0.1031,0.7484,-0.4721,0.4658,0.1017,0.7394,-0.4456,0.5047,0.1019,0.7184,-0.4216,0.5533,0.1026,0.7015,-0.4074,0.5848,0.1033,0.6819,-0.3978,0.6138,0.1047,0.6659,-0.3883,0.637,0.1058,0.6532,-0.3875,0.6506,0.1069,0.6493,-0.3866,0.655,0.1066,0.6436,-0.3969,0.6544,0.1061,0.6442,-0.4029,0.6501,0.1053,0.6463,-0.3966,0.6519,0.104,0.6543,-0.3908,0.6475,0.1033,0.6611,-0.3854,0.6437,0.1017,0.66,-0.3837,0.6459,0.0999,0.6619,-0.374,0.6496,0.097,0.6541,-0.3673,0.6613,0.0951,0.6498,-0.3478,0.6759,0.0927,0.6414,-0.3314,0.6919,0.0913,0.6348,-0.3177,0.7043,0.0885,0.6331,-0.3056,0.7112,0.086,0.6374,-0.2893,0.7142,0.0838,0.6453,-0.2665,0.7159,0.0808,0.6517,-0.2445,0.718,0.0782,0.6552,-0.2182,0.7233,0.0747,0.6585,-0.189,0.7285,0.0713,0.6645,-0.1516,0.7318,0.0695,0.6741,-0.1034,0.7313,0.0692,0.6743,-0.0524,0.7366,0.068,0.6761,-0.0061,0.7367,0.068,0.6712,0.0178,0.7411,0.0682,0.673,0.059,0.7373,0.0679,0.6838,0.0644,0.7268,0.069,0.6995,0.0696,0.7113,0.0696,0.7121,0.066,0.699,0.0701,0.7131,0.0514,0.6992,0.0705,0.7197,0.0516,0.6923,0.0717,0.7274,0.0303,0.6856,0.0737,0.7326,0.0135,0.6806,0.0755,0.7369,0.0064,0.6759,0.0776,0.7377,-0.0074,0.6751,0.0816,0.7399,-0.0205,0.6724,0.0846,0.7527,-0.0367,0.6573,0.0883,0.7695,-0.0548,0.6363,0.0927,0.7721,-0.0894,0.6292,0.0982,0.7724,-0.1134,0.6249,0.1044,0.7721,-0.1304,0.622,0.1106,0.7716,-0.1498,0.6182,0.1169,0.774,-0.1639,0.6116,0.1218,0.7769,-0.1706,0.6061,0.1263,0.7845,-0.1831,0.5925,0.1296,0.784,-0.1872,0.5919,0.1338,0.7792,-0.2,0.5941,0.1362,0.7713,-0.2136,0.5995,0.1375,0.7559,-0.226,0.6145,0.1388,0.7392,-0.2357,0.6309,0.1383,0.7243,-0.2372,0.6474,0.1376,0.7089,-0.2379,0.664,0.1356,0.7033,-0.2345,0.6711,0.1347,0.701,-0.2434,0.6703,0.1329,0.7025,-0.243,0.6689,0.1299,0.6982,-0.2505,0.6707,0.1282,0.6964,-0.2543,0.6711,0.1266,0.6998,-0.256,0.6669,0.1255,0.6886,-0.268,0.6738,0.1255,0.6773,-0.2928,0.6749,0.1262,0.6692,-0.3187,0.6712,0.1273,0.6611,-0.3452,0.6661,0.1293,0.6605,-0.3697,0.6535,0.1315,0.6581,-0.4033,0.6358,0.1349,0.6638,-0.4371,0.6069,0.1375,0.6647,-0.4691,0.5815,0.1421,0.6626,-0.4964,0.5609,0.1466,0.6641,-0.5254,0.5319,0.1515,0.6564,-0.5508,0.5155,0.1566,0.6519,-0.572,0.4978,0.1621,0.6468,-0.5917,0.4813,0.1666,0.6385,-0.6102,0.4691,0.1712,0.6265,-0.6285,0.4609,0.1741,0.6145,-0.6416,0.4592,0.1767,0.6011,-0.6566,0.4556,0.1779,0.594,-0.6622,0.4568,0.1796,0.5931,-0.6636,0.456,0.1806,0.5947,-0.6628,0.4551,0.1804,0.5988,-0.6564,0.4589,0.18,0.6089,-0.6429,0.4647,0.1792,0.6246,-0.6248,0.4685,0.1766,0.6458,-0.5993,0.4731,0.175,0.6586,-0.581,0.4781,0.1726,0.6768,-0.5551,0.4836,0.171,0.6913,-0.5335,0.4873,0.1695,0.7018,-0.5102,0.4972,0.1689,0.7082,-0.4927,0.5057,0.1689,0.7123,-0.4743,0.5174,0.1684,0.7163,-0.4519,0.5317,0.1681,0.717,-0.4318,0.5473,0.1686,0.713,-0.4185,0.5626,0.169,0.7083,-0.4091,0.5752,0.1689,0.7053,-0.4006,0.5849,0.1685,0.6988,-0.396,0.5957,0.1685,0.6923,-0.3964,0.6029,0.1686,0.6837,-0.4,0.6103,0.169,0.6767,-0.4044,0.6152,0.1687,0.6654,-0.4106,0.6234,0.1684,0.6582,-0.415,0.6282,0.1682,0.6494,-0.4145,0.6376,0.1674,0.6455,-0.4082,0.6456,0.166,0.6416,-0.4026,0.6529,0.1653,0.6346,-0.3948,0.6644,0.1636,0.6367,-0.3839,0.6687,0.1619,0.6378,-0.3741,0.6733,0.1606,0.643,-0.3609,0.6755,0.1591,0.6436,-0.3495,0.6809,0.1571,0.6487,-0.3357,0.683,0.1556,0.6612,-0.3229,0.6772,0.154,0.6714,-0.3071,0.6745,0.1521,0.6803,-0.3032,0.6673,0.1513,0.6867,-0.2998,0.6623,0.1504,0.6966,-0.2917,0.6555,0.1511,0.7006,-0.2919,0.6511,0.1511,0.7047,-0.2936,0.6459,0.1518,0.7118,-0.2894,0.64,0.1533,0.7201,-0.2784,0.6356,0.155,0.7331,-0.2729,0.623,0.1583,0.7419,-0.2656,0.6157,0.1608,0.7479,-0.2571,0.6119,0.1629,0.7537,-0.2489,0.6082,0.1651,0.7551,-0.2399,0.6102,0.1667,0.7579,-0.2229,0.6131,0.1673,0.7586,-0.2052,0.6184,0.1684,0.7532,-0.1877,0.6304,0.1686,0.7465,-0.1719,0.6428,0.1682,0.7366,-0.1547,0.6584,0.1649,0.7261,-0.1388,0.6735,0.1623,0.7141,-0.1273,0.6884,0.161,0.7052,-0.1255,0.6978,0.1587,0.7023,-0.1229,0.7011,0.1565,0.7012,-0.1164,0.7034,0.1535,0.7017,-0.1203,0.7023,0.1509,0.7063,-0.1243,0.6969,0.1475,0.7136,-0.1278,0.6888,0.1449,0.7183,-0.1283,0.6838,0.1422,0.7201,-0.1456,0.6784,0.1398,0.7234,-0.1541,0.673,0.1386,0.7283,-0.1719,0.6633,0.1381,0.7281,-0.1905,0.6584,0.1382,0.7279,-0.211,0.6524,0.139,0.7296,-0.2323,0.6432,0.1394,0.7243,-0.2543,0.6409,0.1398,0.7262,-0.2719,0.6314,0.1411,0.7352,-0.2895,0.6129,0.1417,0.744,-0.3098,0.592,0.142,0.7489,-0.333,0.5729,0.1436,0.7558,-0.3515,0.5525,0.1438,0.7641,-0.3639,0.5326,0.1453,0.771,-0.3771,0.5132,0.1456,0.7788,-0.3906,0.4908,0.1471,0.7848,-0.3993,0.4739,0.1488,0.7845,-0.4092,0.4659,0.1508,0.7822,-0.4182,0.4618,0.1524,0.7769,-0.4299,0.4601,0.1544,0.7659,-0.4425,0.4664,0.1579,0.7551,-0.4546,0.4724,0.1613,0.7483,-0.4629,0.4751,0.1647,0.7404,-0.4664,0.484,0.1679,0.734,-0.4724,0.488,0.1708,0.727,-0.4713,0.4994,0.1733,0.7258,-0.4669,0.5051,0.1742,0.7208,-0.4599,0.5186,0.1749,0.7115,-0.4526,0.5376,0.174,0.6995,-0.4467,0.5578,0.174,0.6864,-0.445,0.5752,0.1738,0.6714,-0.4376,0.5981,0.1735,0.6548,-0.4365,0.617,0.1731,0.6381,-0.4324,0.637,0.1727,0.6206,-0.4273,0.6575,0.1715,0.6091,-0.4252,0.6695,0.1708,0.6008,-0.4225,0.6786,0.1688,0.5923,-0.4198,0.6877,0.1668,0.5903,-0.4169,0.6911,0.1641,0.5872,-0.4179,0.6932,0.1616,0.5807,-0.4178,0.6988,0.1593,0.5795,-0.4209,0.6979,0.1575,0.5726,-0.4203,0.7039,0.1551,0.5696,-0.4166,0.7086,0.1535,0.5658,-0.4096,0.7156,0.1527,0.5635,-0.4042,0.7205,0.1506,0.562,-0.3938,0.7274,0.149,0.5587,-0.3851,0.7345,0.1465,0.5511,-0.3677,0.7491,0.1447,0.548,-0.3525,0.7586,0.1427,0.5465,-0.3351,0.7675,0.1413,0.5435,-0.3139,0.7785,0.14,0.5516,-0.2955,0.78,0.1393,0.5579,-0.2703,0.7846,0.1376,0.5755,-0.2478,0.7794,0.1365,0.6014,-0.2383,0.7626,0.1345,0.6365,-0.2293,0.7363,0.1326,0.6708,-0.2163,0.7094,0.1309,0.7001,-0.205,0.6839,0.1303,0.718,-0.1936,0.6686,0.131,0.7307,-0.1817,0.6581,0.1325,0.7344,-0.1765,0.6553,0.135,0.7337,-0.1713,0.6576,0.1382,0.7279,-0.1744,0.6632,0.1398,0.7184,-0.1808,0.6717,0.143,0.7106,-0.1822,0.6796,0.1459,0.7055,-0.1897,0.6829,0.1477,0.7026,-0.1839,0.6874,0.1494,0.7026,-0.1852,0.6871,0.1507,0.6938,-0.1834,0.6964,0.1512,0.6916,-0.1768,0.7003,0.1524,0.6828,-0.175,0.7093,0.153,0.6736,-0.1707,0.7191,0.1542,0.6615,-0.1672,0.731,0.1546,0.642,-0.1595,0.7499,0.1547])

Group366.addChildren(OrientationInterpolator391)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.525157,6.785662], [2.15166,7.200243], [-7.137212,0.208419] degrees
#1.121967 2.219361 -1.735443, 0.994213 2.177388 -1.744496, 0.805579 2.151660 -1.742254, 0.679111 2.172901 -1.728260, 0.624755 2.231911 -1.723264, 0.570379 2.290937 -1.718213, 0.542117 2.381536 -1.738034, 0.531580 2.517337 -1.823594, 0.549149 2.713147 -1.843520, 0.563941 2.917109 -1.870919, 0.525157 2.987144 -1.912269, 0.574892 3.124177 -1.928076, 0.604275 3.245084 -2.011184, 0.637937 3.354579 -2.084006, 0.650356 3.431784 -2.207296, 0.678749 3.519181 -2.378441, 0.764590 3.580735 -2.573580, 0.820652 3.735475 -2.819216, 0.885168 3.743572 -3.067144, 1.020983 3.839287 -3.309463, 1.110384 3.935837 -3.553521, 1.222308 4.063597 -3.748524, 1.439352 4.196218 -3.880000, 1.669704 4.302683 -4.038571, 1.922543 4.450010 -4.134351, 2.225290 4.554186 -4.179887, 2.604203 4.599705 -4.218820, 3.021413 4.583255 -4.230084, 3.363619 4.558637 -4.236283, 3.669826 4.527610 -4.161393, 3.907995 4.451849 -4.014188, 4.070285 4.363519 -3.887729, 4.232954 4.188039 -3.751403, 4.368740 3.984702 -3.620764, 4.460617 3.835886 -3.528611, 4.516739 3.664460 -3.496188, 4.630396 3.519294 -3.423211, 4.801372 3.374806 -3.438747, 5.005436 3.219751 -3.488132, 5.166541 3.105643 -3.565322, 5.225718 3.067404 -3.685314, 5.258659 2.999334 -3.780756, 5.161829 2.890709 -3.884197, 4.988655 2.753767 -3.984895, 4.815460 2.629791 -4.001894, 4.596022 2.512689 -3.997213, 4.382665 2.382444 -3.950492, 4.189481 2.296196 -3.970605, 4.044883 2.255866 -3.951368, 3.922498 2.209013 -3.906116, 3.697614 2.204157 -3.855239, 3.561283 2.261600 -3.777339, 3.395647 2.309676 -3.752599, 3.206938 2.428936 -3.772364, 3.095091 2.557358 -3.795466, 2.959238 2.634999 -3.762555, 2.875158 2.726652 -3.827821, 2.782374 2.862325 -3.867569, 2.702516 3.153645 -3.958011, 2.679650 3.432902 -3.959859, 2.691986 3.689050 -3.985434, 2.668870 3.861099 -4.064580, 2.633969 4.007509 -4.078988, 2.583006 4.037689 -4.118862, 2.460515 4.086601 -4.086070, 2.451801 4.164371 -3.999287, 2.459995 4.145962 -3.934731, 2.515107 4.171011 -3.818515, 2.565297 4.202494 -3.627770, 2.604961 4.250229 -3.392543, 2.716678 4.283073 -3.132860, 2.822358 4.290907 -2.857396, 3.050277 4.248170 -2.717778, 3.350400 4.151248 -2.602729, 3.554236 4.076006 -2.540025, 3.771785 4.009378 -2.520070, 3.947884 3.951471 -2.490594, 4.072014 3.912941 -2.514076, 4.088645 3.879888 -2.502822, 4.065389 3.823904 -2.550086, 4.008912 3.798303 -2.565249, 3.967706 3.766166 -2.494790, 3.913248 3.789639 -2.443016, 3.831576 3.775483 -2.373734, 3.774690 3.703874 -2.320594, 3.682917 3.611171 -2.197264, 3.669453 3.497859 -2.114641, 3.650600 3.391930 -1.957353, 3.672305 3.296346 -1.839647, 3.619061 3.165519 -1.711801, 3.549732 3.072154 -1.602406, 3.468586 3.015953 -1.480698, 3.347339 2.948084 -1.319930, 3.248112 2.887884 -1.178212, 3.121271 2.778113 -1.010004, 2.995025 2.667553 -0.841937, 2.930910 2.630493 -0.671421, 2.910887 2.660889 -0.477876, 2.878702 2.622730 -0.270328, 2.874407 2.633903 -0.089965, 2.895421 2.622609 0.003438, 2.864997 2.622983 0.163912, 2.870944 2.710242 0.187032, 2.831824 2.795150 0.208419, 2.801772 2.864128 0.195168, 2.823434 2.886235 0.136674, 2.842561 2.962234 0.138566, 2.893312 3.072339 0.050230, 2.945305 3.169060 -0.023143, 3.005831 3.273773 -0.057508, 3.162764 3.448209 -0.129872, 3.265800 3.580472 -0.201568, 3.336217 3.800370 -0.296559, 3.394892 4.075130 -0.411788, 3.566574 4.326088 -0.638243, 3.773851 4.594940 -0.830563, 3.986839 4.861224 -0.996433, 4.196639 5.127308 -1.192622, 4.335627 5.354418 -1.348316, 4.461762 5.569838 -1.453400, 4.484824 5.767971 -1.587985, 4.627941 5.944586 -1.677220, 4.734748 6.008432 -1.811444, 4.828501 5.997575 -1.938207, 5.000063 5.927755 -2.059490, 5.110590 5.765995 -2.127880, 5.214641 5.620038 -2.129691, 5.263880 5.417058 -2.100317, 5.278436 5.336792 -2.058230, 5.205811 5.248875 -2.095545, 5.074884 5.143584 -2.039731, 5.020385 5.041563 -2.063550, 4.958733 4.964071 -2.061371, 4.886445 4.946845 -2.053667, 4.941013 4.864229 -2.140177, 4.982014 4.800811 -2.329307, 5.006756 4.776033 -2.537315, 5.055949 4.781100 -2.772777, 5.054300 4.847237 -3.002801, 5.063600 4.944117 -3.340253, 4.947315 5.075078 -3.666343, 4.926049 5.243894 -4.050424, 4.924683 5.382538 -4.406769, 4.858048 5.568107 -4.803947, 4.891586 5.677371 -5.193464, 4.913520 5.823771 -5.569452, 4.909664 5.931338 -5.912029, 4.939444 6.004642 -6.254594, 4.947734 5.976500 -6.536708, 5.009287 5.936408 -6.765096, 5.009553 5.835185 -6.959681, 5.069421 5.809821 -7.080280, 5.092628 5.831748 -7.137212, 5.076943 5.842960 -7.119306, 5.103021 5.872524 -7.040459, 5.139680 5.954930 -6.879501, 5.099820 6.038476 -6.601801, 5.094427 6.205256 -6.294451, 5.066425 6.255492 -6.031429, 5.067838 6.387685 -5.730882, 5.050860 6.481575 -5.475390, 5.121757 6.567684 -5.240494, 5.195881 6.631392 -5.077236, 5.285515 6.656700 -4.892548, 5.402668 6.687206 -4.676085, 5.560857 6.717559 -4.505943, 5.712650 6.692956 -4.393644, 5.826403 6.645817 -4.305961, 5.899515 6.602479 -4.216831, 5.997004 6.535294 -4.172551, 6.070932 6.477442 -4.181934, 6.153448 6.401458 -4.224249, 6.190146 6.320432 -4.258923, 6.255227 6.193134 -4.307052, 6.292486 6.112446 -4.342071, 6.350712 5.999720 -4.316694, 6.365455 5.913200 -4.218665, 6.404545 5.854970 -4.148852, 6.436221 5.730218 -4.030023, 6.401908 5.696128 -3.885944, 6.388363 5.666929 -3.764602, 6.342019 5.668909 -3.609772, 6.305824 5.610315 -3.460790, 6.259981 5.611590 -3.306132, 6.138210 5.672222 -3.158503, 6.034617 5.702318 -2.982360, 5.939776 5.753873 -2.932646, 5.859556 5.777474 -2.884587, 5.825406 5.891505 -2.828929, 5.788124 5.926635 -2.830882, 5.773235 5.991357 -2.860719, 5.781990 6.116875 -2.856061, 5.803662 6.259250 -2.793832, 5.817612 6.513426 -2.811190, 5.842685 6.699522 -2.793706, 5.884733 6.847353 -2.757272, 5.926550 6.995278 -2.721423, 6.000015 7.078974 -2.667575, 6.041647 7.139030 -2.518409, 6.123828 7.200243 -2.369924, 6.236646 7.164196 -2.208372, 6.330174 7.089306 -2.053289, 6.338223 6.863811 -1.844780, 6.368562 6.668103 -1.664789, 6.445898 6.508529 -1.543903, 6.435922 6.337021 -1.500197, 6.371397 6.223042 -1.450800, 6.266108 6.100069 -1.359976, 6.150122 6.000335 -1.364588, 5.963686 5.903139 -1.359952, 5.792620 5.860641 -1.359650, 5.641956 5.789619 -1.331859, 5.512465 5.705617 -1.443485, 5.425068 5.679785 -1.495452, 5.334359 5.692273 -1.628024, 5.305103 5.686473 -1.774199, 5.298005 5.711830 -1.947498, 5.249020 5.736053 -2.121912, 5.254843 5.702528 -2.302683, 5.235199 5.764686 -2.465753, 5.116291 5.858353 -2.616261, 4.964920 5.936147 -2.781522, 4.877709 6.039678 -3.001555, 4.726244 6.103532 -3.152932, 4.618213 6.233101 -3.285571, 4.473096 6.303749 -3.396552, 4.339934 6.433206 -3.539791, 4.254469 6.558940 -3.652740, 4.251443 6.643472 -3.788367, 4.265951 6.688307 -3.906008, 4.316734 6.727159 -4.063531, 4.478499 6.767388 -4.274158, 4.640405 6.805776 -4.485302, 4.770236 6.874077 -4.661956, 4.955268 6.925325 -4.796188, 5.084912 6.971805 -4.940805, 5.275376 6.998700 -5.012406, 5.358766 7.022005 -4.999310, 5.509097 6.994455 -4.953899, 5.660580 6.862809 -4.860301, 5.853637 6.738662 -4.807108, 6.011951 6.592316 -4.785834, 6.220697 6.429327 -4.709391, 6.386676 6.244808 -4.687921, 6.556545 6.058082 -4.633515, 6.702460 5.843174 -4.550026, 6.784825 5.703144 -4.507080, 6.785296 5.557930 -4.423665, 6.785662 5.412468 -4.340472, 6.703413 5.312208 -4.239413, 6.616308 5.204996 -4.178151, 6.566818 5.072318 -4.111481, 6.482061 5.005240 -4.087447, 6.430917 4.869764 -4.014484, 6.400962 4.795224 -3.936776, 6.425333 4.739654 -3.855288, 6.373913 4.659579 -3.752172, 6.359676 4.602726 -3.622799, 6.308774 4.505087 -3.486145, 6.340040 4.391499 -3.295312, 6.326101 4.314097 -3.125158, 6.327478 4.266879 -2.952693, 6.350692 4.213058 -2.756204, 6.325289 4.263146 -2.597311, 6.278732 4.274085 -2.369063, 6.182423 4.388198 -2.177923, 5.961627 4.530185 -2.075093, 5.679456 4.741871 -1.980013, 5.405350 4.947844 -1.858092, 5.190454 5.152098 -1.766727, 5.100632 5.317797 -1.691794, 5.079194 5.480155 -1.625165, 5.151311 5.610374 -1.619597, 5.292251 5.738371 -1.623514, 5.398982 5.754697 -1.669949, 5.598575 5.805493 -1.768344, 5.779796 5.854524 -1.821636, 5.884558 5.879720 -1.911338, 5.988735 5.923640 -1.887455, 6.037120 5.970644 -1.916898, 6.138525 5.915803 -1.909365, 6.219069 5.944880 -1.870393, 6.320747 5.890897 -1.862698, 6.454471 5.854898 -1.841251, 6.574531 5.764344 -1.815874, 6.738384 5.595616 -1.745892
#Interpolator21_skullbase channels [63..65] sends animation values to BVH JOINT Head, DEF Bvh1_skullbase, <HAnimJoint name=skullbase/>
OrientationInterpolator392 = OrientationInterpolator()
OrientationInterpolator392.setDEF("Interpolator21_skullbase")
OrientationInterpolator392.setKey([0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1])
OrientationInterpolator392.setKeyValue([0.7404,-0.5674,0.3603,0.0527,0.743,-0.5847,0.3256,0.0515,0.7528,-0.6008,0.2688,0.0502,0.7658,-0.6017,0.2267,0.0497,0.7779,-0.5939,0.2052,0.0503,0.7893,-0.5858,0.184,0.0508,0.7989,-0.5772,0.1691,0.0522,0.8026,-0.5757,0.1562,0.0549,0.8202,-0.5515,0.1523,0.0579,0.8352,-0.5298,0.1473,0.0611,0.8372,-0.5305,0.1328,0.0624,0.8451,-0.5157,0.1408,0.0647,0.8442,-0.517,0.1419,0.0673,0.8434,-0.5174,0.1445,0.0696,0.8356,-0.5307,0.1417,0.0719,0.8235,-0.5494,0.1411,0.0749,0.8063,-0.5713,0.1533,0.0779,0.793,-0.5895,0.1538,0.0826,0.7684,-0.6196,0.16,0.0855,0.7513,-0.6359,0.1767,0.0899,0.7361,-0.6517,0.1831,0.0941,0.7282,-0.6575,0.1932,0.0983,0.7243,-0.653,0.2212,0.1022,0.7158,-0.6524,0.249,0.1063,0.7145,-0.6418,0.2784,0.1103,0.7114,-0.6278,0.3159,0.1137,0.7008,-0.614,0.3632,0.1169,0.6844,-0.599,0.4157,0.1196,0.6693,-0.5863,0.4565,0.122,0.6583,-0.5672,0.495,0.1235,0.6487,-0.5459,0.5303,0.1234,0.6393,-0.5301,0.557,0.1228,0.6217,-0.5168,0.5886,0.1214,0.6012,-0.5058,0.6187,0.1196,0.5854,-0.4978,0.6399,0.1184,0.5662,-0.4991,0.656,0.1171,0.5475,-0.4911,0.6775,0.1165,0.5225,-0.4896,0.6981,0.1174,0.4936,-0.49,0.7185,0.1191,0.4708,-0.4938,0.7311,0.121,0.4606,-0.5047,0.7302,0.1225,0.4488,-0.5153,0.7301,0.1233,0.4373,-0.5355,0.7225,0.1222,0.4249,-0.5611,0.7104,0.1201,0.4157,-0.5782,0.702,0.1174,0.4092,-0.5966,0.6904,0.1139,0.4015,-0.6117,0.6817,0.11,0.3962,-0.6309,0.6671,0.1075,0.3966,-0.6412,0.657,0.1053,0.3961,-0.6478,0.6507,0.1031,0.4061,-0.6601,0.632,0.1,0.4234,-0.6599,0.6207,0.098,0.4386,-0.6676,0.6016,0.0963,0.4633,-0.6772,0.5716,0.0954,0.4854,-0.6801,0.5494,0.0956,0.5041,-0.6818,0.5301,0.0945,0.5166,-0.6881,0.5095,0.0953,0.5363,-0.6892,0.4872,0.0961,0.5708,-0.6829,0.4559,0.0992,0.6043,-0.665,0.4389,0.1018,0.6297,-0.6491,0.4267,0.1048,0.6429,-0.646,0.4114,0.1073,0.6574,-0.6391,0.3992,0.1088,0.6595,-0.6431,0.3891,0.1092,0.6704,-0.6422,0.3717,0.1086,0.6835,-0.6288,0.3708,0.1085,0.6858,-0.6234,0.3756,0.1076,0.6936,-0.6075,0.3872,0.107,0.7067,-0.5829,0.4011,0.1057,0.724,-0.5513,0.4146,0.1043,0.7373,-0.5128,0.4397,0.1031,0.7484,-0.4721,0.4658,0.1017,0.7394,-0.4456,0.5047,0.1019,0.7184,-0.4216,0.5533,0.1026,0.7015,-0.4074,0.5848,0.1033,0.6819,-0.3978,0.6138,0.1047,0.6659,-0.3883,0.637,0.1058,0.6532,-0.3875,0.6506,0.1069,0.6493,-0.3866,0.655,0.1066,0.6436,-0.3969,0.6544,0.1061,0.6442,-0.4029,0.6501,0.1053,0.6463,-0.3966,0.6519,0.104,0.6543,-0.3908,0.6475,0.1033,0.6611,-0.3854,0.6437,0.1017,0.66,-0.3837,0.6459,0.0999,0.6619,-0.374,0.6496,0.097,0.6541,-0.3673,0.6613,0.0951,0.6498,-0.3478,0.6759,0.0927,0.6414,-0.3314,0.6919,0.0913,0.6348,-0.3177,0.7043,0.0885,0.6331,-0.3056,0.7112,0.086,0.6374,-0.2893,0.7142,0.0838,0.6453,-0.2665,0.7159,0.0808,0.6517,-0.2445,0.718,0.0782,0.6552,-0.2182,0.7233,0.0747,0.6585,-0.189,0.7285,0.0713,0.6645,-0.1516,0.7318,0.0695,0.6741,-0.1034,0.7313,0.0692,0.6743,-0.0524,0.7366,0.068,0.6761,-0.0061,0.7367,0.068,0.6712,0.0178,0.7411,0.0682,0.673,0.059,0.7373,0.0679,0.6838,0.0644,0.7268,0.069,0.6995,0.0696,0.7113,0.0696,0.7121,0.066,0.699,0.0701,0.7131,0.0514,0.6992,0.0705,0.7197,0.0516,0.6923,0.0717,0.7274,0.0303,0.6856,0.0737,0.7326,0.0135,0.6806,0.0755,0.7369,0.0064,0.6759,0.0776,0.7377,-0.0074,0.6751,0.0816,0.7399,-0.0205,0.6724,0.0846,0.7527,-0.0367,0.6573,0.0883,0.7695,-0.0548,0.6363,0.0927,0.7721,-0.0894,0.6292,0.0982,0.7724,-0.1134,0.6249,0.1044,0.7721,-0.1304,0.622,0.1106,0.7716,-0.1498,0.6182,0.1169,0.774,-0.1639,0.6116,0.1218,0.7769,-0.1706,0.6061,0.1263,0.7845,-0.1831,0.5925,0.1296,0.784,-0.1872,0.5919,0.1338,0.7792,-0.2,0.5941,0.1362,0.7713,-0.2136,0.5995,0.1375,0.7559,-0.226,0.6145,0.1388,0.7392,-0.2357,0.6309,0.1383,0.7243,-0.2372,0.6474,0.1376,0.7089,-0.2379,0.664,0.1356,0.7033,-0.2345,0.6711,0.1347,0.701,-0.2434,0.6703,0.1329,0.7025,-0.243,0.6689,0.1299,0.6982,-0.2505,0.6707,0.1282,0.6964,-0.2543,0.6711,0.1266,0.6998,-0.256,0.6669,0.1255,0.6886,-0.268,0.6738,0.1255,0.6773,-0.2928,0.6749,0.1262,0.6692,-0.3187,0.6712,0.1273,0.6611,-0.3452,0.6661,0.1293,0.6605,-0.3697,0.6535,0.1315,0.6581,-0.4033,0.6358,0.1349,0.6638,-0.4371,0.6069,0.1375,0.6647,-0.4691,0.5815,0.1421,0.6626,-0.4964,0.5609,0.1466,0.6641,-0.5254,0.5319,0.1515,0.6564,-0.5508,0.5155,0.1566,0.6519,-0.572,0.4978,0.1621,0.6468,-0.5917,0.4813,0.1666,0.6385,-0.6102,0.4691,0.1712,0.6265,-0.6285,0.4609,0.1741,0.6145,-0.6416,0.4592,0.1767,0.6011,-0.6566,0.4556,0.1779,0.594,-0.6622,0.4568,0.1796,0.5931,-0.6636,0.456,0.1806,0.5947,-0.6628,0.4551,0.1804,0.5988,-0.6564,0.4589,0.18,0.6089,-0.6429,0.4647,0.1792,0.6246,-0.6248,0.4685,0.1766,0.6458,-0.5993,0.4731,0.175,0.6586,-0.581,0.4781,0.1726,0.6768,-0.5551,0.4836,0.171,0.6913,-0.5335,0.4873,0.1695,0.7018,-0.5102,0.4972,0.1689,0.7082,-0.4927,0.5057,0.1689,0.7123,-0.4743,0.5174,0.1684,0.7163,-0.4519,0.5317,0.1681,0.717,-0.4318,0.5473,0.1686,0.713,-0.4185,0.5626,0.169,0.7083,-0.4091,0.5752,0.1689,0.7053,-0.4006,0.5849,0.1685,0.6988,-0.396,0.5957,0.1685,0.6923,-0.3964,0.6029,0.1686,0.6837,-0.4,0.6103,0.169,0.6767,-0.4044,0.6152,0.1687,0.6654,-0.4106,0.6234,0.1684,0.6582,-0.415,0.6282,0.1682,0.6494,-0.4145,0.6376,0.1674,0.6455,-0.4082,0.6456,0.166,0.6416,-0.4026,0.6529,0.1653,0.6346,-0.3948,0.6644,0.1636,0.6367,-0.3839,0.6687,0.1619,0.6378,-0.3741,0.6733,0.1606,0.643,-0.3609,0.6755,0.1591,0.6436,-0.3495,0.6809,0.1571,0.6487,-0.3357,0.683,0.1556,0.6612,-0.3229,0.6772,0.154,0.6714,-0.3071,0.6745,0.1521,0.6803,-0.3032,0.6673,0.1513,0.6867,-0.2998,0.6623,0.1504,0.6966,-0.2917,0.6555,0.1511,0.7006,-0.2919,0.6511,0.1511,0.7047,-0.2936,0.6459,0.1518,0.7118,-0.2894,0.64,0.1533,0.7201,-0.2784,0.6356,0.155,0.7331,-0.2729,0.623,0.1583,0.7419,-0.2656,0.6157,0.1608,0.7479,-0.2571,0.6119,0.1629,0.7537,-0.2489,0.6082,0.1651,0.7551,-0.2399,0.6102,0.1667,0.7579,-0.2229,0.6131,0.1673,0.7586,-0.2052,0.6184,0.1684,0.7532,-0.1877,0.6304,0.1686,0.7465,-0.1719,0.6428,0.1682,0.7366,-0.1547,0.6584,0.1649,0.7261,-0.1388,0.6735,0.1623,0.7141,-0.1273,0.6884,0.161,0.7052,-0.1255,0.6978,0.1587,0.7023,-0.1229,0.7011,0.1565,0.7012,-0.1164,0.7034,0.1535,0.7017,-0.1203,0.7023,0.1509,0.7063,-0.1243,0.6969,0.1475,0.7136,-0.1278,0.6888,0.1449,0.7183,-0.1283,0.6838,0.1422,0.7201,-0.1456,0.6784,0.1398,0.7234,-0.1541,0.673,0.1386,0.7283,-0.1719,0.6633,0.1381,0.7281,-0.1905,0.6584,0.1382,0.7279,-0.211,0.6524,0.139,0.7296,-0.2323,0.6432,0.1394,0.7243,-0.2543,0.6409,0.1398,0.7262,-0.2719,0.6314,0.1411,0.7352,-0.2895,0.6129,0.1417,0.744,-0.3098,0.592,0.142,0.7489,-0.333,0.5729,0.1436,0.7558,-0.3515,0.5525,0.1438,0.7641,-0.3639,0.5326,0.1453,0.771,-0.3771,0.5132,0.1456,0.7788,-0.3906,0.4908,0.1471,0.7848,-0.3993,0.4739,0.1488,0.7845,-0.4092,0.4659,0.1508,0.7822,-0.4182,0.4618,0.1524,0.7769,-0.4299,0.4601,0.1544,0.7659,-0.4425,0.4664,0.1579,0.7551,-0.4546,0.4724,0.1613,0.7483,-0.4629,0.4751,0.1647,0.7404,-0.4664,0.484,0.1679,0.734,-0.4724,0.488,0.1708,0.727,-0.4713,0.4994,0.1733,0.7258,-0.4669,0.5051,0.1742,0.7208,-0.4599,0.5186,0.1749,0.7115,-0.4526,0.5376,0.174,0.6995,-0.4467,0.5578,0.174,0.6864,-0.445,0.5752,0.1738,0.6714,-0.4376,0.5981,0.1735,0.6548,-0.4365,0.617,0.1731,0.6381,-0.4324,0.637,0.1727,0.6206,-0.4273,0.6575,0.1715,0.6091,-0.4252,0.6695,0.1708,0.6008,-0.4225,0.6786,0.1688,0.5923,-0.4198,0.6877,0.1668,0.5903,-0.4169,0.6911,0.1641,0.5872,-0.4179,0.6932,0.1616,0.5807,-0.4178,0.6988,0.1593,0.5795,-0.4209,0.6979,0.1575,0.5726,-0.4203,0.7039,0.1551,0.5696,-0.4166,0.7086,0.1535,0.5658,-0.4096,0.7156,0.1527,0.5635,-0.4042,0.7205,0.1506,0.562,-0.3938,0.7274,0.149,0.5587,-0.3851,0.7345,0.1465,0.5511,-0.3677,0.7491,0.1447,0.548,-0.3525,0.7586,0.1427,0.5465,-0.3351,0.7675,0.1413,0.5435,-0.3139,0.7785,0.14,0.5516,-0.2955,0.78,0.1393,0.5579,-0.2703,0.7846,0.1376,0.5755,-0.2478,0.7794,0.1365,0.6014,-0.2383,0.7626,0.1345,0.6365,-0.2293,0.7363,0.1326,0.6708,-0.2163,0.7094,0.1309,0.7001,-0.205,0.6839,0.1303,0.718,-0.1936,0.6686,0.131,0.7307,-0.1817,0.6581,0.1325,0.7344,-0.1765,0.6553,0.135,0.7337,-0.1713,0.6576,0.1382,0.7279,-0.1744,0.6632,0.1398,0.7184,-0.1808,0.6717,0.143,0.7106,-0.1822,0.6796,0.1459,0.7055,-0.1897,0.6829,0.1477,0.7026,-0.1839,0.6874,0.1494,0.7026,-0.1852,0.6871,0.1507,0.6938,-0.1834,0.6964,0.1512,0.6916,-0.1768,0.7003,0.1524,0.6828,-0.175,0.7093,0.153,0.6736,-0.1707,0.7191,0.1542,0.6615,-0.1672,0.731,0.1546,0.642,-0.1595,0.7499,0.1547])

Group366.addChildren(OrientationInterpolator392)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.525157,6.785663], [2.151661,7.200242], [-7.137212,0.208419] degrees
#1.121968 2.219362 -1.735443, 0.994214 2.177389 -1.744499, 0.805580 2.151661 -1.742253, 0.679112 2.172901 -1.728257, 0.624756 2.231911 -1.723261, 0.570379 2.290936 -1.718210, 0.542118 2.381536 -1.738031, 0.531580 2.517336 -1.823592, 0.549150 2.713146 -1.843520, 0.563942 2.917109 -1.870919, 0.525157 2.987144 -1.912271, 0.574892 3.124176 -1.928075, 0.604276 3.245085 -2.011183, 0.637938 3.354579 -2.084004, 0.650357 3.431783 -2.207294, 0.678750 3.519181 -2.378441, 0.764591 3.580734 -2.573579, 0.820653 3.735476 -2.819217, 0.885170 3.743571 -3.067142, 1.020983 3.839285 -3.309462, 1.110384 3.935837 -3.553522, 1.222309 4.063596 -3.748522, 1.439353 4.196218 -3.880000, 1.669705 4.302684 -4.038571, 1.922543 4.450009 -4.134351, 2.225290 4.554185 -4.179886, 2.604204 4.599705 -4.218818, 3.021413 4.583254 -4.230084, 3.363620 4.558637 -4.236286, 3.669827 4.527610 -4.161391, 3.907995 4.451848 -4.014190, 4.070286 4.363518 -3.887728, 4.232955 4.188039 -3.751404, 4.368741 3.984702 -3.620764, 4.460616 3.835885 -3.528610, 4.516741 3.664461 -3.496190, 4.630397 3.519294 -3.423210, 4.801373 3.374806 -3.438746, 5.005439 3.219753 -3.488131, 5.166542 3.105644 -3.565322, 5.225718 3.067405 -3.685316, 5.258657 2.999334 -3.780757, 5.161830 2.890710 -3.884197, 4.988657 2.753769 -3.984893, 4.815463 2.629792 -4.001895, 4.596023 2.512689 -3.997211, 4.382665 2.382445 -3.950494, 4.189481 2.296196 -3.970606, 4.044885 2.255867 -3.951368, 3.922498 2.209013 -3.906116, 3.697616 2.204158 -3.855241, 3.561284 2.261600 -3.777339, 3.395648 2.309676 -3.752601, 3.206939 2.428936 -3.772364, 3.095092 2.557358 -3.795466, 2.959238 2.634998 -3.762554, 2.875159 2.726652 -3.827822, 2.782374 2.862324 -3.867569, 2.702517 3.153645 -3.958009, 2.679651 3.432902 -3.959859, 2.691988 3.689050 -3.985434, 2.668869 3.861097 -4.064579, 2.633970 4.007509 -4.078988, 2.583007 4.037688 -4.118861, 2.460516 4.086602 -4.086070, 2.451802 4.164371 -3.999286, 2.459996 4.145961 -3.934731, 2.515108 4.171012 -3.818516, 2.565297 4.202493 -3.627770, 2.604960 4.250229 -3.392541, 2.716679 4.283072 -3.132860, 2.822358 4.290907 -2.857396, 3.050278 4.248169 -2.717778, 3.350401 4.151247 -2.602727, 3.554237 4.076007 -2.540025, 3.771786 4.009379 -2.520070, 3.947884 3.951470 -2.490595, 4.072014 3.912941 -2.514077, 4.088646 3.879889 -2.502821, 4.065391 3.823903 -2.550084, 4.008910 3.798303 -2.565250, 3.967707 3.766166 -2.494788, 3.913249 3.789639 -2.443015, 3.831576 3.775483 -2.373732, 3.774691 3.703875 -2.320593, 3.682918 3.611171 -2.197264, 3.669453 3.497859 -2.114639, 3.650602 3.391930 -1.957353, 3.672305 3.296346 -1.839647, 3.619062 3.165519 -1.711801, 3.549731 3.072154 -1.602406, 3.468588 3.015954 -1.480696, 3.347338 2.948084 -1.319927, 3.248112 2.887884 -1.178211, 3.121273 2.778113 -1.010003, 2.995027 2.667554 -0.841936, 2.930909 2.630492 -0.671422, 2.910887 2.660887 -0.477875, 2.878703 2.622730 -0.270327, 2.874408 2.633903 -0.089965, 2.895421 2.622608 0.003438, 2.864998 2.622983 0.163912, 2.870945 2.710242 0.187034, 2.831825 2.795151 0.208419, 2.801772 2.864126 0.195169, 2.823434 2.886234 0.136675, 2.842562 2.962234 0.138565, 2.893312 3.072339 0.050229, 2.945305 3.169060 -0.023144, 3.005832 3.273774 -0.057507, 3.162763 3.448209 -0.129871, 3.265799 3.580472 -0.201566, 3.336219 3.800371 -0.296558, 3.394891 4.075129 -0.411786, 3.566575 4.326088 -0.638240, 3.773850 4.594939 -0.830561, 3.986840 4.861226 -0.996433, 4.196641 5.127310 -1.192622, 4.335626 5.354416 -1.348315, 4.461763 5.569838 -1.453398, 4.484824 5.767971 -1.587985, 4.627942 5.944585 -1.677220, 4.734749 6.008432 -1.811443, 4.828503 5.997575 -1.938208, 5.000065 5.927756 -2.059492, 5.110590 5.765995 -2.127881, 5.214641 5.620038 -2.129689, 5.263881 5.417058 -2.100316, 5.278437 5.336792 -2.058229, 5.205814 5.248875 -2.095544, 5.074886 5.143584 -2.039730, 5.020388 5.041564 -2.063550, 4.958734 4.964072 -2.061371, 4.886446 4.946846 -2.053668, 4.941012 4.864229 -2.140177, 4.982015 4.800812 -2.329305, 5.006757 4.776033 -2.537314, 5.055951 4.781098 -2.772775, 5.054302 4.847236 -3.002798, 5.063601 4.944117 -3.340254, 4.947315 5.075077 -3.666342, 4.926049 5.243895 -4.050423, 4.924682 5.382537 -4.406768, 4.858049 5.568107 -4.803946, 4.891587 5.677370 -5.193464, 4.913520 5.823771 -5.569451, 4.909666 5.931338 -5.912027, 4.939443 6.004642 -6.254594, 4.947735 5.976501 -6.536708, 5.009288 5.936407 -6.765095, 5.009553 5.835184 -6.959678, 5.069421 5.809823 -7.080284, 5.092631 5.831747 -7.137212, 5.076942 5.842959 -7.119304, 5.103021 5.872524 -7.040458, 5.139678 5.954929 -6.879497, 5.099822 6.038477 -6.601801, 5.094428 6.205256 -6.294448, 5.066426 6.255492 -6.031428, 5.067841 6.387686 -5.730884, 5.050860 6.481573 -5.475389, 5.121757 6.567682 -5.240493, 5.195880 6.631391 -5.077233, 5.285515 6.656700 -4.892548, 5.402668 6.687203 -4.676083, 5.560857 6.717558 -4.505942, 5.712650 6.692956 -4.393645, 5.826404 6.645818 -4.305959, 5.899516 6.602478 -4.216830, 5.997005 6.535293 -4.172551, 6.070933 6.477443 -4.181935, 6.153450 6.401459 -4.224248, 6.190148 6.320433 -4.258923, 6.255226 6.193135 -4.307050, 6.292487 6.112446 -4.342071, 6.350713 5.999720 -4.316694, 6.365457 5.913199 -4.218667, 6.404547 5.854970 -4.148851, 6.436219 5.730216 -4.030024, 6.401911 5.696128 -3.885943, 6.388365 5.666929 -3.764600, 6.342019 5.668908 -3.609772, 6.305825 5.610314 -3.460789, 6.259981 5.611588 -3.306130, 6.138212 5.672223 -3.158502, 6.034620 5.702318 -2.982359, 5.939776 5.753873 -2.932644, 5.859556 5.777474 -2.884586, 5.825408 5.891508 -2.828928, 5.788125 5.926635 -2.830881, 5.773238 5.991358 -2.860720, 5.781990 6.116874 -2.856060, 5.803664 6.259252 -2.793831, 5.817613 6.513426 -2.811190, 5.842687 6.699522 -2.793705, 5.884734 6.847353 -2.757274, 5.926556 6.995281 -2.721422, 6.000017 7.078972 -2.667575, 6.041648 7.139030 -2.518409, 6.123828 7.200242 -2.369922, 6.236650 7.164197 -2.208372, 6.330173 7.089305 -2.053290, 6.338224 6.863811 -1.844779, 6.368562 6.668104 -1.664789, 6.445900 6.508528 -1.543901, 6.435922 6.337022 -1.500195, 6.371398 6.223038 -1.450798, 6.266109 6.100068 -1.359977, 6.150121 6.000334 -1.364586, 5.963688 5.903139 -1.359951, 5.792621 5.860641 -1.359651, 5.641957 5.789619 -1.331858, 5.512467 5.705617 -1.443485, 5.425067 5.679782 -1.495453, 5.334360 5.692272 -1.628023, 5.305102 5.686472 -1.774199, 5.298004 5.711830 -1.947496, 5.249021 5.736053 -2.121910, 5.254845 5.702529 -2.302684, 5.235200 5.764687 -2.465754, 5.116293 5.858355 -2.616260, 4.964920 5.936147 -2.781520, 4.877709 6.039677 -3.001555, 4.726248 6.103535 -3.152933, 4.618215 6.233102 -3.285571, 4.473095 6.303747 -3.396551, 4.339934 6.433202 -3.539787, 4.254471 6.558941 -3.652739, 4.251446 6.643472 -3.788364, 4.265953 6.688306 -3.906005, 4.316737 6.727159 -4.063532, 4.478499 6.767388 -4.274158, 4.640405 6.805777 -4.485301, 4.770237 6.874076 -4.661955, 4.955266 6.925325 -4.796187, 5.084915 6.971806 -4.940806, 5.275376 6.998701 -5.012405, 5.358768 7.022003 -4.999309, 5.509097 6.994456 -4.953900, 5.660579 6.862808 -4.860299, 5.853638 6.738661 -4.807111, 6.011951 6.592316 -4.785834, 6.220698 6.429327 -4.709389, 6.386676 6.244809 -4.687921, 6.556547 6.058082 -4.633515, 6.702461 5.843174 -4.550026, 6.784828 5.703144 -4.507082, 6.785297 5.557929 -4.423664, 6.785663 5.412467 -4.340471, 6.703413 5.312209 -4.239413, 6.616308 5.204994 -4.178151, 6.566821 5.072319 -4.111482, 6.482061 5.005239 -4.087448, 6.430918 4.869767 -4.014484, 6.400961 4.795223 -3.936775, 6.425335 4.739654 -3.855289, 6.373913 4.659577 -3.752170, 6.359679 4.602726 -3.622799, 6.308773 4.505087 -3.486145, 6.340040 4.391499 -3.295312, 6.326103 4.314099 -3.125156, 6.327482 4.266880 -2.952694, 6.350694 4.213058 -2.756203, 6.325289 4.263146 -2.597310, 6.278733 4.274085 -2.369062, 6.182424 4.388197 -2.177922, 5.961628 4.530185 -2.075092, 5.679456 4.741871 -1.980013, 5.405353 4.947844 -1.858091, 5.190453 5.152099 -1.766727, 5.100633 5.317797 -1.691793, 5.079195 5.480154 -1.625164, 5.151312 5.610374 -1.619598, 5.292252 5.738370 -1.623514, 5.398982 5.754696 -1.669947, 5.598574 5.805494 -1.768346, 5.779798 5.854526 -1.821636, 5.884559 5.879719 -1.911337, 5.988737 5.923642 -1.887455, 6.037117 5.970643 -1.916897, 6.138524 5.915802 -1.909366, 6.219070 5.944880 -1.870393, 6.320748 5.890896 -1.862695, 6.454473 5.854898 -1.841251, 6.574532 5.764346 -1.815873, 6.738384 5.595615 -1.745891
#Overall angle min/max range [-46.181885,57.245258] degrees
#Corresponding ROUTE statements to send animation values
ROUTE393 = ROUTE()
ROUTE393.setFromField("fraction_changed")
ROUTE393.setFromNode("RealTimer")
ROUTE393.setToField("set_fraction")
ROUTE393.setToNode("Interpolator0_HIERARCHY_Hips")

Group366.addChildren(ROUTE393)
ROUTE394 = ROUTE()
ROUTE394.setFromField("value_changed")
ROUTE394.setFromNode("FrameStepper")
ROUTE394.setToField("set_fraction")
ROUTE394.setToNode("Interpolator0_HIERARCHY_Hips")

Group366.addChildren(ROUTE394)
ROUTE395 = ROUTE()
ROUTE395.setFromField("value_changed")
ROUTE395.setFromNode("Interpolator0_HIERARCHY_Hips")
ROUTE395.setToField("set_translation")
ROUTE395.setToNode("Bvh1_HumanoidRoot")

Group366.addChildren(ROUTE395)
ROUTE396 = ROUTE()
ROUTE396.setFromField("fraction_changed")
ROUTE396.setFromNode("RealTimer")
ROUTE396.setToField("set_fraction")
ROUTE396.setToNode("Interpolator1_HIERARCHY_Hips")

Group366.addChildren(ROUTE396)
ROUTE397 = ROUTE()
ROUTE397.setFromField("value_changed")
ROUTE397.setFromNode("FrameStepper")
ROUTE397.setToField("set_fraction")
ROUTE397.setToNode("Interpolator1_HIERARCHY_Hips")

Group366.addChildren(ROUTE397)
ROUTE398 = ROUTE()
ROUTE398.setFromField("value_changed")
ROUTE398.setFromNode("Interpolator1_HIERARCHY_Hips")
ROUTE398.setToField("set_rotation")
ROUTE398.setToNode("Bvh1_HumanoidRoot")

Group366.addChildren(ROUTE398)
ROUTE399 = ROUTE()
ROUTE399.setFromField("fraction_changed")
ROUTE399.setFromNode("RealTimer")
ROUTE399.setToField("set_fraction")
ROUTE399.setToNode("Interpolator2_l_hip")

Group366.addChildren(ROUTE399)
ROUTE400 = ROUTE()
ROUTE400.setFromField("value_changed")
ROUTE400.setFromNode("FrameStepper")
ROUTE400.setToField("set_fraction")
ROUTE400.setToNode("Interpolator2_l_hip")

Group366.addChildren(ROUTE400)
ROUTE401 = ROUTE()
ROUTE401.setFromField("value_changed")
ROUTE401.setFromNode("Interpolator2_l_hip")
ROUTE401.setToField("set_rotation")
ROUTE401.setToNode("Bvh1_l_hip")

Group366.addChildren(ROUTE401)
ROUTE402 = ROUTE()
ROUTE402.setFromField("fraction_changed")
ROUTE402.setFromNode("RealTimer")
ROUTE402.setToField("set_fraction")
ROUTE402.setToNode("Interpolator3_l_knee")

Group366.addChildren(ROUTE402)
ROUTE403 = ROUTE()
ROUTE403.setFromField("value_changed")
ROUTE403.setFromNode("FrameStepper")
ROUTE403.setToField("set_fraction")
ROUTE403.setToNode("Interpolator3_l_knee")

Group366.addChildren(ROUTE403)
ROUTE404 = ROUTE()
ROUTE404.setFromField("value_changed")
ROUTE404.setFromNode("Interpolator3_l_knee")
ROUTE404.setToField("set_rotation")
ROUTE404.setToNode("Bvh1_l_knee")

Group366.addChildren(ROUTE404)
ROUTE405 = ROUTE()
ROUTE405.setFromField("fraction_changed")
ROUTE405.setFromNode("RealTimer")
ROUTE405.setToField("set_fraction")
ROUTE405.setToNode("Interpolator4_l_ankle")

Group366.addChildren(ROUTE405)
ROUTE406 = ROUTE()
ROUTE406.setFromField("value_changed")
ROUTE406.setFromNode("FrameStepper")
ROUTE406.setToField("set_fraction")
ROUTE406.setToNode("Interpolator4_l_ankle")

Group366.addChildren(ROUTE406)
ROUTE407 = ROUTE()
ROUTE407.setFromField("value_changed")
ROUTE407.setFromNode("Interpolator4_l_ankle")
ROUTE407.setToField("set_rotation")
ROUTE407.setToNode("Bvh1_l_ankle")

Group366.addChildren(ROUTE407)
ROUTE408 = ROUTE()
ROUTE408.setFromField("fraction_changed")
ROUTE408.setFromNode("RealTimer")
ROUTE408.setToField("set_fraction")
ROUTE408.setToNode("Interpolator5_l_midtarsal")

Group366.addChildren(ROUTE408)
ROUTE409 = ROUTE()
ROUTE409.setFromField("value_changed")
ROUTE409.setFromNode("FrameStepper")
ROUTE409.setToField("set_fraction")
ROUTE409.setToNode("Interpolator5_l_midtarsal")

Group366.addChildren(ROUTE409)
ROUTE410 = ROUTE()
ROUTE410.setFromField("value_changed")
ROUTE410.setFromNode("Interpolator5_l_midtarsal")
ROUTE410.setToField("set_rotation")
ROUTE410.setToNode("Bvh1_l_midtarsal")

Group366.addChildren(ROUTE410)
ROUTE411 = ROUTE()
ROUTE411.setFromField("fraction_changed")
ROUTE411.setFromNode("RealTimer")
ROUTE411.setToField("set_fraction")
ROUTE411.setToNode("Interpolator6_r_hip")

Group366.addChildren(ROUTE411)
ROUTE412 = ROUTE()
ROUTE412.setFromField("value_changed")
ROUTE412.setFromNode("FrameStepper")
ROUTE412.setToField("set_fraction")
ROUTE412.setToNode("Interpolator6_r_hip")

Group366.addChildren(ROUTE412)
ROUTE413 = ROUTE()
ROUTE413.setFromField("value_changed")
ROUTE413.setFromNode("Interpolator6_r_hip")
ROUTE413.setToField("set_rotation")
ROUTE413.setToNode("Bvh1_r_hip")

Group366.addChildren(ROUTE413)
ROUTE414 = ROUTE()
ROUTE414.setFromField("fraction_changed")
ROUTE414.setFromNode("RealTimer")
ROUTE414.setToField("set_fraction")
ROUTE414.setToNode("Interpolator7_r_knee")

Group366.addChildren(ROUTE414)
ROUTE415 = ROUTE()
ROUTE415.setFromField("value_changed")
ROUTE415.setFromNode("FrameStepper")
ROUTE415.setToField("set_fraction")
ROUTE415.setToNode("Interpolator7_r_knee")

Group366.addChildren(ROUTE415)
ROUTE416 = ROUTE()
ROUTE416.setFromField("value_changed")
ROUTE416.setFromNode("Interpolator7_r_knee")
ROUTE416.setToField("set_rotation")
ROUTE416.setToNode("Bvh1_r_knee")

Group366.addChildren(ROUTE416)
ROUTE417 = ROUTE()
ROUTE417.setFromField("fraction_changed")
ROUTE417.setFromNode("RealTimer")
ROUTE417.setToField("set_fraction")
ROUTE417.setToNode("Interpolator8_r_ankle")

Group366.addChildren(ROUTE417)
ROUTE418 = ROUTE()
ROUTE418.setFromField("value_changed")
ROUTE418.setFromNode("FrameStepper")
ROUTE418.setToField("set_fraction")
ROUTE418.setToNode("Interpolator8_r_ankle")

Group366.addChildren(ROUTE418)
ROUTE419 = ROUTE()
ROUTE419.setFromField("value_changed")
ROUTE419.setFromNode("Interpolator8_r_ankle")
ROUTE419.setToField("set_rotation")
ROUTE419.setToNode("Bvh1_r_ankle")

Group366.addChildren(ROUTE419)
ROUTE420 = ROUTE()
ROUTE420.setFromField("fraction_changed")
ROUTE420.setFromNode("RealTimer")
ROUTE420.setToField("set_fraction")
ROUTE420.setToNode("Interpolator9_r_midtarsal")

Group366.addChildren(ROUTE420)
ROUTE421 = ROUTE()
ROUTE421.setFromField("value_changed")
ROUTE421.setFromNode("FrameStepper")
ROUTE421.setToField("set_fraction")
ROUTE421.setToNode("Interpolator9_r_midtarsal")

Group366.addChildren(ROUTE421)
ROUTE422 = ROUTE()
ROUTE422.setFromField("value_changed")
ROUTE422.setFromNode("Interpolator9_r_midtarsal")
ROUTE422.setToField("set_rotation")
ROUTE422.setToNode("Bvh1_r_midtarsal")

Group366.addChildren(ROUTE422)
ROUTE423 = ROUTE()
ROUTE423.setFromField("fraction_changed")
ROUTE423.setFromNode("RealTimer")
ROUTE423.setToField("set_fraction")
ROUTE423.setToNode("Interpolator10_vl5")

Group366.addChildren(ROUTE423)
ROUTE424 = ROUTE()
ROUTE424.setFromField("value_changed")
ROUTE424.setFromNode("FrameStepper")
ROUTE424.setToField("set_fraction")
ROUTE424.setToNode("Interpolator10_vl5")

Group366.addChildren(ROUTE424)
ROUTE425 = ROUTE()
ROUTE425.setFromField("value_changed")
ROUTE425.setFromNode("Interpolator10_vl5")
ROUTE425.setToField("set_rotation")
ROUTE425.setToNode("Bvh1_vl5")

Group366.addChildren(ROUTE425)
ROUTE426 = ROUTE()
ROUTE426.setFromField("fraction_changed")
ROUTE426.setFromNode("RealTimer")
ROUTE426.setToField("set_fraction")
ROUTE426.setToNode("Interpolator11_Chest2")

Group366.addChildren(ROUTE426)
ROUTE427 = ROUTE()
ROUTE427.setFromField("value_changed")
ROUTE427.setFromNode("FrameStepper")
ROUTE427.setToField("set_fraction")
ROUTE427.setToNode("Interpolator11_Chest2")

Group366.addChildren(ROUTE427)
ROUTE428 = ROUTE()
ROUTE428.setFromField("value_changed")
ROUTE428.setFromNode("Interpolator11_Chest2")
ROUTE428.setToField("set_rotation")
ROUTE428.setToNode("Bvh1_Chest2")

Group366.addChildren(ROUTE428)
ROUTE429 = ROUTE()
ROUTE429.setFromField("fraction_changed")
ROUTE429.setFromNode("RealTimer")
ROUTE429.setToField("set_fraction")
ROUTE429.setToNode("Interpolator12_LeftCollar")

Group366.addChildren(ROUTE429)
ROUTE430 = ROUTE()
ROUTE430.setFromField("value_changed")
ROUTE430.setFromNode("FrameStepper")
ROUTE430.setToField("set_fraction")
ROUTE430.setToNode("Interpolator12_LeftCollar")

Group366.addChildren(ROUTE430)
ROUTE431 = ROUTE()
ROUTE431.setFromField("value_changed")
ROUTE431.setFromNode("Interpolator12_LeftCollar")
ROUTE431.setToField("set_rotation")
ROUTE431.setToNode("Bvh1_LeftCollar")

Group366.addChildren(ROUTE431)
ROUTE432 = ROUTE()
ROUTE432.setFromField("fraction_changed")
ROUTE432.setFromNode("RealTimer")
ROUTE432.setToField("set_fraction")
ROUTE432.setToNode("Interpolator13_l_shoulder")

Group366.addChildren(ROUTE432)
ROUTE433 = ROUTE()
ROUTE433.setFromField("value_changed")
ROUTE433.setFromNode("FrameStepper")
ROUTE433.setToField("set_fraction")
ROUTE433.setToNode("Interpolator13_l_shoulder")

Group366.addChildren(ROUTE433)
ROUTE434 = ROUTE()
ROUTE434.setFromField("value_changed")
ROUTE434.setFromNode("Interpolator13_l_shoulder")
ROUTE434.setToField("set_rotation")
ROUTE434.setToNode("Bvh1_l_shoulder")

Group366.addChildren(ROUTE434)
ROUTE435 = ROUTE()
ROUTE435.setFromField("fraction_changed")
ROUTE435.setFromNode("RealTimer")
ROUTE435.setToField("set_fraction")
ROUTE435.setToNode("Interpolator14_l_elbow")

Group366.addChildren(ROUTE435)
ROUTE436 = ROUTE()
ROUTE436.setFromField("value_changed")
ROUTE436.setFromNode("FrameStepper")
ROUTE436.setToField("set_fraction")
ROUTE436.setToNode("Interpolator14_l_elbow")

Group366.addChildren(ROUTE436)
ROUTE437 = ROUTE()
ROUTE437.setFromField("value_changed")
ROUTE437.setFromNode("Interpolator14_l_elbow")
ROUTE437.setToField("set_rotation")
ROUTE437.setToNode("Bvh1_l_elbow")

Group366.addChildren(ROUTE437)
ROUTE438 = ROUTE()
ROUTE438.setFromField("fraction_changed")
ROUTE438.setFromNode("RealTimer")
ROUTE438.setToField("set_fraction")
ROUTE438.setToNode("Interpolator15_l_wrist")

Group366.addChildren(ROUTE438)
ROUTE439 = ROUTE()
ROUTE439.setFromField("value_changed")
ROUTE439.setFromNode("FrameStepper")
ROUTE439.setToField("set_fraction")
ROUTE439.setToNode("Interpolator15_l_wrist")

Group366.addChildren(ROUTE439)
ROUTE440 = ROUTE()
ROUTE440.setFromField("value_changed")
ROUTE440.setFromNode("Interpolator15_l_wrist")
ROUTE440.setToField("set_rotation")
ROUTE440.setToNode("Bvh1_l_wrist")

Group366.addChildren(ROUTE440)
ROUTE441 = ROUTE()
ROUTE441.setFromField("fraction_changed")
ROUTE441.setFromNode("RealTimer")
ROUTE441.setToField("set_fraction")
ROUTE441.setToNode("Interpolator16_RightCollar")

Group366.addChildren(ROUTE441)
ROUTE442 = ROUTE()
ROUTE442.setFromField("value_changed")
ROUTE442.setFromNode("FrameStepper")
ROUTE442.setToField("set_fraction")
ROUTE442.setToNode("Interpolator16_RightCollar")

Group366.addChildren(ROUTE442)
ROUTE443 = ROUTE()
ROUTE443.setFromField("value_changed")
ROUTE443.setFromNode("Interpolator16_RightCollar")
ROUTE443.setToField("set_rotation")
ROUTE443.setToNode("Bvh1_RightCollar")

Group366.addChildren(ROUTE443)
ROUTE444 = ROUTE()
ROUTE444.setFromField("fraction_changed")
ROUTE444.setFromNode("RealTimer")
ROUTE444.setToField("set_fraction")
ROUTE444.setToNode("Interpolator17_r_shoulder")

Group366.addChildren(ROUTE444)
ROUTE445 = ROUTE()
ROUTE445.setFromField("value_changed")
ROUTE445.setFromNode("FrameStepper")
ROUTE445.setToField("set_fraction")
ROUTE445.setToNode("Interpolator17_r_shoulder")

Group366.addChildren(ROUTE445)
ROUTE446 = ROUTE()
ROUTE446.setFromField("value_changed")
ROUTE446.setFromNode("Interpolator17_r_shoulder")
ROUTE446.setToField("set_rotation")
ROUTE446.setToNode("Bvh1_r_shoulder")

Group366.addChildren(ROUTE446)
ROUTE447 = ROUTE()
ROUTE447.setFromField("fraction_changed")
ROUTE447.setFromNode("RealTimer")
ROUTE447.setToField("set_fraction")
ROUTE447.setToNode("Interpolator18_r_elbow")

Group366.addChildren(ROUTE447)
ROUTE448 = ROUTE()
ROUTE448.setFromField("value_changed")
ROUTE448.setFromNode("FrameStepper")
ROUTE448.setToField("set_fraction")
ROUTE448.setToNode("Interpolator18_r_elbow")

Group366.addChildren(ROUTE448)
ROUTE449 = ROUTE()
ROUTE449.setFromField("value_changed")
ROUTE449.setFromNode("Interpolator18_r_elbow")
ROUTE449.setToField("set_rotation")
ROUTE449.setToNode("Bvh1_r_elbow")

Group366.addChildren(ROUTE449)
ROUTE450 = ROUTE()
ROUTE450.setFromField("fraction_changed")
ROUTE450.setFromNode("RealTimer")
ROUTE450.setToField("set_fraction")
ROUTE450.setToNode("Interpolator19_r_wrist")

Group366.addChildren(ROUTE450)
ROUTE451 = ROUTE()
ROUTE451.setFromField("value_changed")
ROUTE451.setFromNode("FrameStepper")
ROUTE451.setToField("set_fraction")
ROUTE451.setToNode("Interpolator19_r_wrist")

Group366.addChildren(ROUTE451)
ROUTE452 = ROUTE()
ROUTE452.setFromField("value_changed")
ROUTE452.setFromNode("Interpolator19_r_wrist")
ROUTE452.setToField("set_rotation")
ROUTE452.setToNode("Bvh1_r_wrist")

Group366.addChildren(ROUTE452)
ROUTE453 = ROUTE()
ROUTE453.setFromField("fraction_changed")
ROUTE453.setFromNode("RealTimer")
ROUTE453.setToField("set_fraction")
ROUTE453.setToNode("Interpolator20_Neck")

Group366.addChildren(ROUTE453)
ROUTE454 = ROUTE()
ROUTE454.setFromField("value_changed")
ROUTE454.setFromNode("FrameStepper")
ROUTE454.setToField("set_fraction")
ROUTE454.setToNode("Interpolator20_Neck")

Group366.addChildren(ROUTE454)
ROUTE455 = ROUTE()
ROUTE455.setFromField("value_changed")
ROUTE455.setFromNode("Interpolator20_Neck")
ROUTE455.setToField("set_rotation")
ROUTE455.setToNode("Bvh1_Neck")

Group366.addChildren(ROUTE455)
ROUTE456 = ROUTE()
ROUTE456.setFromField("fraction_changed")
ROUTE456.setFromNode("RealTimer")
ROUTE456.setToField("set_fraction")
ROUTE456.setToNode("Interpolator21_skullbase")

Group366.addChildren(ROUTE456)
ROUTE457 = ROUTE()
ROUTE457.setFromField("value_changed")
ROUTE457.setFromNode("FrameStepper")
ROUTE457.setToField("set_fraction")
ROUTE457.setToNode("Interpolator21_skullbase")

Group366.addChildren(ROUTE457)
ROUTE458 = ROUTE()
ROUTE458.setFromField("value_changed")
ROUTE458.setFromNode("Interpolator21_skullbase")
ROUTE458.setToField("set_rotation")
ROUTE458.setToNode("Bvh1_skullbase")

Group366.addChildren(ROUTE458)

Scene26.addChildren(Group366)

X3D0.setScene(Scene26)
X3D0.toFileX3D("././BvhConversion1Illustrated_RoundTrip.x3d")
