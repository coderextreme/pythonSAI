from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("4.0")
head1 = head()
component2 = component()
component2.setName("HAnim")
component2.setLevel(1)

head1.addComponent(component2)
meta3 = meta()
meta3.setName("title")
meta3.setContent("DiamondManLOA1.x3d")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("description")
meta4.setContent("HAnim skeletal structure for Level of Action (LOA) one, with diamonds at the Joint centers. LOA-1 is typical low-end real-time 3D hierarchy.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("creator")
meta5.setContent("Matthew T. Beitler")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("translator")
meta6.setContent("Joel S. Pawloski")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("created")
meta7.setContent("12 November 2001")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("modified")
meta8.setContent("13 March 2021")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("Image")
meta9.setContent("images/BonesAllSkeletonFrontViewLOA1.png")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("motto")
meta10.setContent("(a) \"Diamonds are a girl's best friend.\" (b) \"Gosh, it sure is chilly in here.\"")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("warning")
meta11.setContent("Still needs comments on CAESAR feature points inserted")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("reference")
meta12.setContent("HAnim 1.1 specification, Appendix A: Suggested Body Dimensions and Levels of Articulation, Level of Articulation Two")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("reference")
meta13.setContent("http://HAnim.org/Specifications/HAnim1.1/appendices.html#appendixa")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("reference")
meta14.setContent("http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA1.wrl")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("reference")
meta15.setContent("http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA1-diamond.wrl")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("reference")
meta16.setContent("http://ece.uwaterloo.ca/~HAnim")

head1.addMeta(meta16)
meta17 = meta()
meta17.setName("reference")
meta17.setContent("http://www.cis.upenn.edu/~badler/anthro/89-71.pdf")

head1.addMeta(meta17)
meta18 = meta()
meta18.setName("reference")
meta18.setContent("http://www.cis.upenn.edu/~badler/anthro/89-71.ps")

head1.addMeta(meta18)
meta19 = meta()
meta19.setName("reference")
meta19.setContent("http://www.cis.upenn.edu/~beitler")

head1.addMeta(meta19)
meta20 = meta()
meta20.setName("Image")
meta20.setContent("humanoid_landmark_locations.gif")

head1.addMeta(meta20)
meta21 = meta()
meta21.setName("Image")
meta21.setContent("http://HAnim.org/Specifications/HAnim1.1/humanoid_landmark_locations.gif")

head1.addMeta(meta21)
meta22 = meta()
meta22.setName("identifier")
meta22.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Templates/DiamondManLOA1.x3d")

head1.addMeta(meta22)
meta23 = meta()
meta23.setName("generator")
meta23.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta23)
meta24 = meta()
meta24.setName("generator")
meta24.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta24)
meta25 = meta()
meta25.setName("license")
meta25.setContent("../license.html")

head1.addMeta(meta25)

X3D0.setHead(head1)
Scene26 = Scene()
WorldInfo27 = WorldInfo()
WorldInfo27.setInfo(["HAnim 2.0 Default Joint Centers, Level Of Articulation (LOA) 1 -------------------------------------------------------- HANIM 1.1 (VRML 2.0) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 1.1 (VRML 2.0) Author email: beitler@graphics.cis.upenn.edu or beitler@acm.org HANIM 1.1 (VRML 2.0) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 1.1 (VRML 2.0) Compliance Date: May 12, 1999 HANIM 1.1 Compliance Information: http://ece.uwaterloo.ca/~HAnim/ Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps, .pdf"])
WorldInfo27.setTitle("HANIM 1.1 Default Joint Centers, LOA1")

Scene26.addChildren(WorldInfo27)
NavigationInfo28 = NavigationInfo()
NavigationInfo28.setSpeed(1.5)

Scene26.addChildren(NavigationInfo28)
Viewpoint29 = Viewpoint()
Viewpoint29.setCenterOfRotation([0,1,0])
Viewpoint29.setDescription("Diamond Man, LOA 1")
Viewpoint29.setPosition([0,1,3])

Scene26.addChildren(Viewpoint29)
HAnimHumanoid30 = HAnimHumanoid()
HAnimHumanoid30.setName("humanoid")
HAnimHumanoid30.setDEF("hanim_humanoid")
HAnimHumanoid30.setLoa(1)
HAnimHumanoid30.setVersion("2.0")
#HAnimHumanoid original info='\"authorEmail=beitler@graphics.cis.upenn.edu beitler@acm.org\" \"authorName=Matthew T. Beitler\" \"copyright=Copyright 1999 Matthew T. Beitler\" \"humanoidVersion=JointCenters 1.1 LOA1\" \"usageRestrictions=PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose.\"'
MetadataSet31 = MetadataSet()
MetadataSet31.setName("HAnimHumanoid.info")
MetadataSet31.setReference("https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid")
MetadataString32 = MetadataString()
MetadataString32.setName("authorEmail")
MetadataString32.setValue(["beitler@graphics.cis.upenn.edu beitler@acm.org"])

MetadataSet31.setValue(MetadataString32)
MetadataString33 = MetadataString()
MetadataString33.setName("authorName")
MetadataString33.setValue(["Matthew T. Beitler"])

MetadataSet31.addValue(MetadataString33)
MetadataString34 = MetadataString()
MetadataString34.setName("copyright")
MetadataString34.setValue(["Copyright 1999 Matthew T. Beitler"])

MetadataSet31.addValue(MetadataString34)
MetadataString35 = MetadataString()
MetadataString35.setName("humanoidVersion")
MetadataString35.setValue(["JointCenters 1.1 LOA1"])

MetadataSet31.addValue(MetadataString35)
MetadataString36 = MetadataString()
MetadataString36.setName("usageRestrictions")
MetadataString36.setValue(["PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose."])

MetadataSet31.addValue(MetadataString36)

HAnimHumanoid30.setMetadata(MetadataSet31)
HAnimJoint37 = HAnimJoint()
HAnimJoint37.setName("humanoid_root")
HAnimJoint37.setDEF("hanim_humanoid_root")
HAnimJoint37.setCenter([0,0.824,0.0277])
HAnimJoint37.setStiffness([0,0,0])
HAnimJoint38 = HAnimJoint()
HAnimJoint38.setName("sacroiliac")
HAnimJoint38.setDEF("hanim_sacroiliac")
HAnimJoint38.setCenter([0,0.9149,0.0016])
HAnimJoint38.setStiffness([0,0,0])
HAnimSegment39 = HAnimSegment()
HAnimSegment39.setName("pelvis")
HAnimSegment39.setDEF("hanim_pelvis")
Transform40 = Transform()
Transform40.setTranslation([0,0.9149,0.0016])
Shape41 = Shape()
Shape41.setDEF("DiamondShape")
IndexedFaceSet42 = IndexedFaceSet()
IndexedFaceSet42.setCoordIndex([0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1])
IndexedFaceSet42.setCreaseAngle(0.5)
Coordinate43 = Coordinate()
Coordinate43.setDEF("points")
Coordinate43.setPoint([0,0.01,0,-0.01,0,0,0,0,0.01,0.01,0,0,0,0,-0.01,0,-0.01,0])

IndexedFaceSet42.setCoord(Coordinate43)

Shape41.setGeometry(IndexedFaceSet42)
Appearance44 = Appearance()
Material45 = Material()
Material45.setDiffuseColor([1,1,0])

Appearance44.setMaterial(Material45)

Shape41.setAppearance(Appearance44)

Transform40.addChildren(Shape41)

HAnimSegment39.addChildren(Transform40)

HAnimJoint38.addChildren(HAnimSegment39)
HAnimJoint46 = HAnimJoint()
HAnimJoint46.setName("l_hip")
HAnimJoint46.setDEF("hanim_l_hip")
HAnimJoint46.setCenter([0.0961,0.9124,-0.0001])
HAnimJoint46.setStiffness([0,0,0])
HAnimSegment47 = HAnimSegment()
HAnimSegment47.setName("l_thigh")
HAnimSegment47.setDEF("hanim_l_thigh")
Transform48 = Transform()
Transform48.setTranslation([0.0961,0.9124,-0.0001])
Shape49 = Shape()
Shape49.setUSE("DiamondShape")

Transform48.addChildren(Shape49)

HAnimSegment47.addChildren(Transform48)
HAnimSite50 = HAnimSite()
HAnimSite50.setName("l_knee_crease_pt")
HAnimSite50.setDEF("hanim_l_knee_crease_pt")
HAnimSite50.setTranslation([0.0993,0.4881,-0.0309])

HAnimSegment47.addChildren(HAnimSite50)
HAnimSite51 = HAnimSite()
HAnimSite51.setName("l_femoral_lateral_epicondyle_pt")
HAnimSite51.setDEF("hanim_l_femoral_lateral_epicondyle_pt")
HAnimSite51.setTranslation([0.1598,0.4967,0.0297])

HAnimSegment47.addChildren(HAnimSite51)
HAnimSite52 = HAnimSite()
HAnimSite52.setName("l_femoral_medial_epicondyle_pt")
HAnimSite52.setDEF("hanim_l_femoral_medial_epicondyle_pt")
HAnimSite52.setTranslation([0.0398,0.4946,0.0303])

HAnimSegment47.addChildren(HAnimSite52)

HAnimJoint46.addChildren(HAnimSegment47)
HAnimJoint53 = HAnimJoint()
HAnimJoint53.setName("l_knee")
HAnimJoint53.setDEF("hanim_l_knee")
HAnimJoint53.setCenter([0.104,0.4867,0.0308])
HAnimJoint53.setStiffness([0,0,0])
HAnimSegment54 = HAnimSegment()
HAnimSegment54.setName("l_calf")
HAnimSegment54.setDEF("hanim_l_calf")
Transform55 = Transform()
Transform55.setTranslation([0.104,0.4867,0.0308])
Shape56 = Shape()
Shape56.setUSE("DiamondShape")

Transform55.addChildren(Shape56)

HAnimSegment54.addChildren(Transform55)

HAnimJoint53.addChildren(HAnimSegment54)
HAnimJoint57 = HAnimJoint()
HAnimJoint57.setName("l_talocrural")
HAnimJoint57.setDEF("hanim_l_talocrural")
HAnimJoint57.setCenter([0.1101,0.0656,-0.0736])
HAnimJoint57.setStiffness([0,0,0])
HAnimSegment58 = HAnimSegment()
HAnimSegment58.setName("l_talus")
HAnimSegment58.setDEF("hanim_l_talus")
Transform59 = Transform()
Transform59.setTranslation([0.1101,0.0656,-0.0736])
Shape60 = Shape()
Shape60.setUSE("DiamondShape")

Transform59.addChildren(Shape60)

HAnimSegment58.addChildren(Transform59)
HAnimSite61 = HAnimSite()
HAnimSite61.setName("l_lateral_malleolus_pt")
HAnimSite61.setDEF("hanim_l_lateral_malleolus_pt")
HAnimSite61.setTranslation([0.1308,0.0597,-0.1032])

HAnimSegment58.addChildren(HAnimSite61)
HAnimSite62 = HAnimSite()
HAnimSite62.setName("l_medial_malleolus_pt")
HAnimSite62.setDEF("hanim_l_medial_malleolus_pt")
HAnimSite62.setTranslation([0.089,0.0716,-0.0881])

HAnimSegment58.addChildren(HAnimSite62)
HAnimSite63 = HAnimSite()
HAnimSite63.setName("l_sphyrion_pt")
HAnimSite63.setDEF("hanim_l_sphyrion_pt")
HAnimSite63.setTranslation([0.089,0.0575,-0.0943])

HAnimSegment58.addChildren(HAnimSite63)
HAnimSite64 = HAnimSite()
HAnimSite64.setName("l_calcaneus_posterior_pt")
HAnimSite64.setDEF("hanim_l_calcaneus_posterior_pt")
HAnimSite64.setTranslation([0.0974,0.0259,-0.1171])

HAnimSegment58.addChildren(HAnimSite64)

HAnimJoint57.addChildren(HAnimSegment58)
HAnimJoint65 = HAnimJoint()
HAnimJoint65.setName("l_metatarsophalangeal_2")
HAnimJoint65.setDEF("hanim_l_metatarsophalangeal_2")
HAnimJoint65.setCenter([0.1086,0.0001,0.0368])
HAnimJoint65.setStiffness([0,0,0])
HAnimSegment66 = HAnimSegment()
HAnimSegment66.setName("l_tarsal_proximal_phalanx_2")
HAnimSegment66.setDEF("hanim_l_tarsal_proximal_phalanx_2")
HAnimSite67 = HAnimSite()
HAnimSite67.setName("l_middistal_tip")
HAnimSite67.setDEF("hanim_l_middistal_tip")
HAnimSite67.setTranslation([0.1354,0.0016,0.1476])

HAnimSegment66.addChildren(HAnimSite67)
HAnimSite68 = HAnimSite()
HAnimSite68.setName("l_metatarsal_phalanx_5_pt")
HAnimSite68.setDEF("hanim_l_metatarsal_phalanx_5_pt")
HAnimSite68.setTranslation([0.1825,0.007,0.0928])

HAnimSegment66.addChildren(HAnimSite68)
HAnimSite69 = HAnimSite()
HAnimSite69.setName("l_metatarsal_phalanx_1_pt")
HAnimSite69.setDEF("hanim_l_metatarsal_phalanx_1_pt")
HAnimSite69.setTranslation([0.0816,0.0232,0.0106])

HAnimSegment66.addChildren(HAnimSite69)
HAnimSite70 = HAnimSite()
HAnimSite70.setName("l_tarsal_distal_phalanx_2_pt")
HAnimSite70.setDEF("hanim_l_tarsal_distal_phalanx_2_pt")
HAnimSite70.setTranslation([0.1195,0.0079,0.1433])

HAnimSegment66.addChildren(HAnimSite70)

HAnimJoint65.addChildren(HAnimSegment66)

HAnimJoint57.addChildren(HAnimJoint65)

HAnimJoint53.addChildren(HAnimJoint57)

HAnimJoint46.addChildren(HAnimJoint53)

HAnimJoint38.addChildren(HAnimJoint46)
HAnimJoint71 = HAnimJoint()
HAnimJoint71.setName("r_hip")
HAnimJoint71.setDEF("hanim_r_hip")
HAnimJoint71.setCenter([-0.095,0.9171,0.0029])
HAnimJoint71.setStiffness([0,0,0])
HAnimSegment72 = HAnimSegment()
HAnimSegment72.setName("r_thigh")
HAnimSegment72.setDEF("hanim_r_thigh")
Transform73 = Transform()
Transform73.setTranslation([-0.095,0.9171,0.0029])
Shape74 = Shape()
Shape74.setUSE("DiamondShape")

Transform73.addChildren(Shape74)

HAnimSegment72.addChildren(Transform73)
HAnimSite75 = HAnimSite()
HAnimSite75.setName("r_knee_crease_pt")
HAnimSite75.setDEF("hanim_r_knee_crease_pt")
HAnimSite75.setTranslation([-0.0825,0.4932,-0.0326])

HAnimSegment72.addChildren(HAnimSite75)
HAnimSite76 = HAnimSite()
HAnimSite76.setName("r_femoral_lateral_epicondyle_pt")
HAnimSite76.setDEF("hanim_r_femoral_lateral_epicondyle_pt")
HAnimSite76.setTranslation([-0.1421,0.4992,0.031])

HAnimSegment72.addChildren(HAnimSite76)
HAnimSite77 = HAnimSite()
HAnimSite77.setName("r_femoral_medial_epicondyle_pt")
HAnimSite77.setDEF("hanim_r_femoral_medial_epicondyle_pt")
HAnimSite77.setTranslation([-0.0221,0.5014,0.0289])

HAnimSegment72.addChildren(HAnimSite77)

HAnimJoint71.addChildren(HAnimSegment72)
HAnimJoint78 = HAnimJoint()
HAnimJoint78.setName("r_knee")
HAnimJoint78.setDEF("hanim_r_knee")
HAnimJoint78.setCenter([-0.0867,0.4913,0.0318])
HAnimJoint78.setStiffness([0,0,0])
HAnimSegment79 = HAnimSegment()
HAnimSegment79.setName("r_calf")
HAnimSegment79.setDEF("hanim_r_calf")
Transform80 = Transform()
Transform80.setTranslation([-0.0867,0.4913,0.0318])
Shape81 = Shape()
Shape81.setUSE("DiamondShape")

Transform80.addChildren(Shape81)

HAnimSegment79.addChildren(Transform80)

HAnimJoint78.addChildren(HAnimSegment79)
HAnimJoint82 = HAnimJoint()
HAnimJoint82.setName("r_talocrural")
HAnimJoint82.setDEF("hanim_r_talocrural")
HAnimJoint82.setCenter([-0.0801,0.0712,-0.0766])
HAnimJoint82.setStiffness([0,0,0])
HAnimSegment83 = HAnimSegment()
HAnimSegment83.setName("r_talus")
HAnimSegment83.setDEF("hanim_r_talus")
Transform84 = Transform()
Transform84.setTranslation([-0.0801,0.0712,-0.0766])
Shape85 = Shape()
Shape85.setUSE("DiamondShape")

Transform84.addChildren(Shape85)

HAnimSegment83.addChildren(Transform84)
HAnimSite86 = HAnimSite()
HAnimSite86.setName("r_lateral_malleolus_pt")
HAnimSite86.setDEF("hanim_r_lateral_malleolus_pt")
HAnimSite86.setTranslation([-0.1006,0.0658,-0.1075])

HAnimSegment83.addChildren(HAnimSite86)
HAnimSite87 = HAnimSite()
HAnimSite87.setName("r_medial_malleolus_pt")
HAnimSite87.setDEF("hanim_r_medial_malleolus_pt")
HAnimSite87.setTranslation([-0.0591,0.076,-0.0928])

HAnimSegment83.addChildren(HAnimSite87)
HAnimSite88 = HAnimSite()
HAnimSite88.setName("r_sphyrion_pt")
HAnimSite88.setDEF("hanim_r_sphyrion_pt")
HAnimSite88.setTranslation([-0.0603,0.061,-0.1002])

HAnimSegment83.addChildren(HAnimSite88)
HAnimSite89 = HAnimSite()
HAnimSite89.setName("r_calcaneus_posterior_pt")
HAnimSite89.setDEF("hanim_r_calcaneus_posterior_pt")
HAnimSite89.setTranslation([-0.0692,0.0297,-0.1221])

HAnimSegment83.addChildren(HAnimSite89)

HAnimJoint82.addChildren(HAnimSegment83)
HAnimJoint90 = HAnimJoint()
HAnimJoint90.setName("r_metatarsophalangeal_2")
HAnimJoint90.setDEF("hanim_r_metatarsophalangeal_2")
HAnimJoint90.setCenter([-0.0801,0,0.0368])
HAnimJoint90.setStiffness([0,0,0])
HAnimSegment91 = HAnimSegment()
HAnimSegment91.setName("r_tarsal_proximal_phalanx_2")
HAnimSegment91.setDEF("hanim_r_tarsal_proximal_phalanx_2")
HAnimSite92 = HAnimSite()
HAnimSite92.setName("r_middistal_tip")
HAnimSite92.setDEF("hanim_r_middistal_tip")
HAnimSite92.setTranslation([-0.1043,-0.0227,0.145])

HAnimSegment91.addChildren(HAnimSite92)
HAnimSite93 = HAnimSite()
HAnimSite93.setName("r_metatarsal_phalanx_5_pt")
HAnimSite93.setDEF("hanim_r_metatarsal_phalanx_5_pt")
HAnimSite93.setTranslation([-0.1523,0.0166,0.0895])

HAnimSegment91.addChildren(HAnimSite93)
HAnimSite94 = HAnimSite()
HAnimSite94.setName("r_metatarsal_phalanx_1_pt")
HAnimSite94.setDEF("hanim_r_metatarsal_phalanx_1_pt")
HAnimSite94.setTranslation([-0.0521,0.026,0.0127])

HAnimSegment91.addChildren(HAnimSite94)
HAnimSite95 = HAnimSite()
HAnimSite95.setName("r_tarsal_distal_phalanx_2_pt")
HAnimSite95.setDEF("hanim_r_tarsal_distal_phalanx_2_pt")
HAnimSite95.setTranslation([-0.0883,0.0134,0.1383])

HAnimSegment91.addChildren(HAnimSite95)

HAnimJoint90.addChildren(HAnimSegment91)

HAnimJoint82.addChildren(HAnimJoint90)

HAnimJoint78.addChildren(HAnimJoint82)

HAnimJoint71.addChildren(HAnimJoint78)

HAnimJoint38.addChildren(HAnimJoint71)

HAnimJoint37.addChildren(HAnimJoint38)
HAnimJoint96 = HAnimJoint()
HAnimJoint96.setName("vl1")
HAnimJoint96.setDEF("hanim_vl1")
HAnimJoint96.setCenter([-0.00405,1.07,-0.0275])
HAnimJoint96.setStiffness([0,0,0])
HAnimSegment97 = HAnimSegment()
HAnimSegment97.setName("l1")
HAnimSegment97.setDEF("hanim_l1")

HAnimJoint96.addChildren(HAnimSegment97)
HAnimJoint98 = HAnimJoint()
HAnimJoint98.setName("l_shoulder")
HAnimJoint98.setDEF("hanim_l_shoulder")
HAnimJoint98.setCenter([0.2029,1.4376,-0.0387])
HAnimJoint98.setStiffness([0,0,0])
HAnimSegment99 = HAnimSegment()
HAnimSegment99.setName("l_upperarm")
HAnimSegment99.setDEF("hanim_l_upperarm")
Transform100 = Transform()
Transform100.setTranslation([0.2029,1.4376,-0.0387])
Shape101 = Shape()
Shape101.setUSE("DiamondShape")

Transform100.addChildren(Shape101)

HAnimSegment99.addChildren(Transform100)
Transform102 = Transform()
Transform102.setDEF("l_upperarm_adjust")
Transform102.setCenter([0.182,1.22,-0.047])
Transform102.setRotation([1,0,0,0.119])
Transform102.setTranslation([0.2029,1.4376,-0.0387])

HAnimSegment99.addChildren(Transform102)
HAnimSite103 = HAnimSite()
HAnimSite103.setName("l_humeral_lateral_epicondyle_pt")
HAnimSite103.setDEF("hanim_l_humeral_lateral_epicondyle_pt")
HAnimSite103.setTranslation([0.228,1.1482,-0.11])

HAnimSegment99.addChildren(HAnimSite103)

HAnimJoint98.addChildren(HAnimSegment99)
HAnimJoint104 = HAnimJoint()
HAnimJoint104.setName("l_elbow")
HAnimJoint104.setDEF("hanim_l_elbow")
HAnimJoint104.setCenter([0.2014,1.1357,-0.0682])
HAnimJoint104.setStiffness([0,0,0])
HAnimSegment105 = HAnimSegment()
HAnimSegment105.setName("l_forearm")
HAnimSegment105.setDEF("hanim_l_forearm")
Transform106 = Transform()
Transform106.setTranslation([0.2014,1.1357,-0.0682])
Shape107 = Shape()
Shape107.setUSE("DiamondShape")

Transform106.addChildren(Shape107)

HAnimSegment105.addChildren(Transform106)
Transform108 = Transform()
Transform108.setDEF("l_forearm_adjust")
Transform108.setCenter([0.198,0.961,-0.0405])
Transform108.setRotation([-1,0,0,0.1])
Transform108.setTranslation([0.2014,1.1357,-0.0682])

HAnimSegment105.addChildren(Transform108)
HAnimSite109 = HAnimSite()
HAnimSite109.setName("l_radial_styloid_pt")
HAnimSite109.setDEF("hanim_l_radial_styloid_pt")
HAnimSite109.setTranslation([0.1901,0.8645,-0.0415])

HAnimSegment105.addChildren(HAnimSite109)
HAnimSite110 = HAnimSite()
HAnimSite110.setName("l_olecranon_pt")
HAnimSite110.setDEF("hanim_l_olecranon_pt")
HAnimSite110.setTranslation([-0.1962,1.1375,-0.1123])

HAnimSegment105.addChildren(HAnimSite110)
HAnimSite111 = HAnimSite()
HAnimSite111.setName("l_humeral_medial_epicondyle_pt")
HAnimSite111.setDEF("hanim_l_humeral_medial_epicondyle_pt")
HAnimSite111.setTranslation([0.1735,1.1272,-0.1113])

HAnimSegment105.addChildren(HAnimSite111)
HAnimSite112 = HAnimSite()
HAnimSite112.setName("l_radiale_pt")
HAnimSite112.setDEF("hanim_l_radiale_pt")
HAnimSite112.setTranslation([0.2182,1.1212,-0.1167])

HAnimSegment105.addChildren(HAnimSite112)

HAnimJoint104.addChildren(HAnimSegment105)
HAnimJoint113 = HAnimJoint()
HAnimJoint113.setName("l_radiocarpal")
HAnimJoint113.setDEF("hanim_l_radiocarpal")
HAnimJoint113.setCenter([0.1984,0.8663,-0.0583])
HAnimJoint113.setStiffness([0,0,0])
HAnimSegment114 = HAnimSegment()
HAnimSegment114.setName("l_carpal")
HAnimSegment114.setDEF("hanim_l_carpal")
Transform115 = Transform()
Transform115.setTranslation([0.1984,0.8663,-0.0583])
Shape116 = Shape()
Shape116.setUSE("DiamondShape")

Transform115.addChildren(Shape116)

HAnimSegment114.addChildren(Transform115)
Transform117 = Transform()
Transform117.setDEF("l_hand_adjust")
Transform117.setCenter([0.213,0.811,-0.0338])
Transform117.setRotation([-0.06361,-0.9967,0.04988,1.333])
Transform117.setTranslation([0.1984,0.8663,-0.0583])

HAnimSegment114.addChildren(Transform117)
HAnimSite118 = HAnimSite()
HAnimSite118.setName("l_hand_tip")
HAnimSite118.setDEF("hanim_l_hand_tip")
HAnimSite118.setTranslation([0.208,0.6731,-0.0491])

HAnimSegment114.addChildren(HAnimSite118)
HAnimSite119 = HAnimSite()
HAnimSite119.setName("l_metacarpal_phalanx_2_pt")
HAnimSite119.setDEF("hanim_l_metacarpal_phalanx_2_pt")
HAnimSite119.setTranslation([0.2009,0.8139,-0.0237])

HAnimSegment114.addChildren(HAnimSite119)
HAnimSite120 = HAnimSite()
HAnimSite120.setName("l_dactylion_pt")
HAnimSite120.setDEF("hanim_l_dactylion_pt")
HAnimSite120.setTranslation([0.2056,0.6743,-0.0482])

HAnimSegment114.addChildren(HAnimSite120)
HAnimSite121 = HAnimSite()
HAnimSite121.setName("l_ulnar_styloid_pt")
HAnimSite121.setDEF("hanim_l_ulnar_styloid_pt")
HAnimSite121.setTranslation([-0.2142,0.8529,-0.0648])

HAnimSegment114.addChildren(HAnimSite121)
HAnimSite122 = HAnimSite()
HAnimSite122.setName("l_metacarpal_phalanx_5_pt")
HAnimSite122.setDEF("hanim_l_metacarpal_phalanx_5_pt")
HAnimSite122.setTranslation([0.1929,0.786,-0.1122])

HAnimSegment114.addChildren(HAnimSite122)

HAnimJoint113.addChildren(HAnimSegment114)

HAnimJoint104.addChildren(HAnimJoint113)

HAnimJoint98.addChildren(HAnimJoint104)

HAnimJoint96.addChildren(HAnimJoint98)
HAnimJoint123 = HAnimJoint()
HAnimJoint123.setName("r_shoulder")
HAnimJoint123.setDEF("hanim_r_shoulder")
HAnimJoint123.setCenter([-0.1907,1.4407,-0.0325])
HAnimJoint123.setStiffness([0,0,0])
HAnimSegment124 = HAnimSegment()
HAnimSegment124.setName("r_upperarm")
HAnimSegment124.setDEF("hanim_r_upperarm")
Transform125 = Transform()
Transform125.setTranslation([-0.1907,1.4407,-0.0325])
Shape126 = Shape()
Shape126.setUSE("DiamondShape")

Transform125.addChildren(Shape126)

HAnimSegment124.addChildren(Transform125)
Transform127 = Transform()
Transform127.setDEF("r_upperarm_adjust")
Transform127.setCenter([-0.182,1.22,-0.047])
Transform127.setRotation([1,0,0,0.0836])
Transform127.setTranslation([-0.1907,1.4407,-0.0325])

HAnimSegment124.addChildren(Transform127)
HAnimSite128 = HAnimSite()
HAnimSite128.setName("r_humeral_lateral_epicondyle_pt")
HAnimSite128.setDEF("hanim_r_humeral_lateral_epicondyle_pt")
HAnimSite128.setTranslation([-0.2224,1.1517,-0.1033])

HAnimSegment124.addChildren(HAnimSite128)

HAnimJoint123.addChildren(HAnimSegment124)
HAnimJoint129 = HAnimJoint()
HAnimJoint129.setName("r_elbow")
HAnimJoint129.setDEF("hanim_r_elbow")
HAnimJoint129.setCenter([-0.1949,1.1388,-0.062])
HAnimJoint129.setStiffness([0,0,0])
HAnimSegment130 = HAnimSegment()
HAnimSegment130.setName("r_forearm")
HAnimSegment130.setDEF("hanim_r_forearm")
Transform131 = Transform()
Transform131.setTranslation([-0.1949,1.1388,-0.062])
Shape132 = Shape()
Shape132.setUSE("DiamondShape")

Transform131.addChildren(Shape132)

HAnimSegment130.addChildren(Transform131)
Transform133 = Transform()
Transform133.setDEF("r_forearm_adjust")
Transform133.setCenter([-0.198,0.961,-0.0397])
Transform133.setRotation([-1,0,0,0.1254])
Transform133.setTranslation([-0.1949,1.1388,-0.062])

HAnimSegment130.addChildren(Transform133)
HAnimSite134 = HAnimSite()
HAnimSite134.setName("r_radial_styloid_pt")
HAnimSite134.setDEF("hanim_r_radial_styloid_pt")
HAnimSite134.setTranslation([-0.1884,0.8676,-0.036])

HAnimSegment130.addChildren(HAnimSite134)
HAnimSite135 = HAnimSite()
HAnimSite135.setName("r_olecranon_pt")
HAnimSite135.setDEF("hanim_r_olecranon_pt")
HAnimSite135.setTranslation([-0.1907,1.1405,-0.1065])

HAnimSegment130.addChildren(HAnimSite135)
HAnimSite136 = HAnimSite()
HAnimSite136.setName("r_humeral_medial_epicondyle_pt")
HAnimSite136.setDEF("hanim_r_humeral_medial_epicondyle_pt")
HAnimSite136.setTranslation([-0.168,1.1298,-0.1062])

HAnimSegment130.addChildren(HAnimSite136)
HAnimSite137 = HAnimSite()
HAnimSite137.setName("r_radiale_pt")
HAnimSite137.setDEF("hanim_r_radiale_pt")
HAnimSite137.setTranslation([-0.213,1.1305,-0.1091])

HAnimSegment130.addChildren(HAnimSite137)

HAnimJoint129.addChildren(HAnimSegment130)
HAnimJoint138 = HAnimJoint()
HAnimJoint138.setName("r_radiocarpal")
HAnimJoint138.setDEF("hanim_r_radiocarpal")
HAnimJoint138.setCenter([-0.1959,0.8694,-0.0521])
HAnimJoint138.setStiffness([0,0,0])
HAnimSegment139 = HAnimSegment()
HAnimSegment139.setName("r_carpal")
HAnimSegment139.setDEF("hanim_r_carpal")
Transform140 = Transform()
Transform140.setTranslation([-0.1959,0.8694,-0.0521])
Shape141 = Shape()
Shape141.setUSE("DiamondShape")

Transform140.addChildren(Shape141)

HAnimSegment139.addChildren(Transform140)
Transform142 = Transform()
Transform142.setDEF("r_hand_adjust")
Transform142.setCenter([-0.217,0.811,-0.0338])
Transform142.setRotation([-0.09024,0.994,-0.0624,1.216])

HAnimSegment139.addChildren(Transform142)
HAnimSite143 = HAnimSite()
HAnimSite143.setName("r_hand_tip")
HAnimSite143.setDEF("hanim_r_hand_tip")
HAnimSite143.setTranslation([-0.1969,0.6758,-0.0427])

HAnimSegment139.addChildren(HAnimSite143)
HAnimSite144 = HAnimSite()
HAnimSite144.setName("r_metacarpal_phalanx_2_pt")
HAnimSite144.setDEF("hanim_r_metacarpal_phalanx_2_pt")
HAnimSite144.setTranslation([-0.1977,0.8169,-0.0177])

HAnimSegment139.addChildren(HAnimSite144)
HAnimSite145 = HAnimSite()
HAnimSite145.setName("r_dactylion_pt")
HAnimSite145.setDEF("hanim_r_dactylion_pt")
HAnimSite145.setTranslation([-0.1941,0.6772,-0.0423])

HAnimSegment139.addChildren(HAnimSite145)
HAnimSite146 = HAnimSite()
HAnimSite146.setName("r_ulnar_styloid_pt")
HAnimSite146.setDEF("hanim_r_ulnar_styloid_pt")
HAnimSite146.setTranslation([-0.2117,0.8562,-0.0584])

HAnimSegment139.addChildren(HAnimSite146)
HAnimSite147 = HAnimSite()
HAnimSite147.setName("r_metacarpal_phalanx_5_pt")
HAnimSite147.setDEF("hanim_r_metacarpal_phalanx_5_pt")
HAnimSite147.setTranslation([-0.1929,0.789,-0.1064])

HAnimSegment139.addChildren(HAnimSite147)

HAnimJoint138.addChildren(HAnimSegment139)

HAnimJoint129.addChildren(HAnimJoint138)

HAnimJoint123.addChildren(HAnimJoint129)

HAnimJoint96.addChildren(HAnimJoint123)
HAnimJoint148 = HAnimJoint()
HAnimJoint148.setName("vc4")
HAnimJoint148.setDEF("hanim_vc4")
HAnimJoint148.setCenter([0,1.43,-0.0458])
HAnimJoint148.setStiffness([0,0,0])
HAnimSegment149 = HAnimSegment()
HAnimSegment149.setName("c4")
HAnimSegment149.setDEF("hanim_c4")

HAnimJoint148.addChildren(HAnimSegment149)

HAnimJoint96.addChildren(HAnimJoint148)

HAnimJoint37.addChildren(HAnimJoint96)
HAnimJoint150 = HAnimJoint()
HAnimJoint150.setName("vl5")
HAnimJoint150.setDEF("hanim_vl5")
HAnimJoint150.setCenter([0.0028,1.0568,-0.0776])
HAnimJoint150.setStiffness([0,0,0])
HAnimJoint151 = HAnimJoint()
HAnimJoint151.setName("skullbase")
HAnimJoint151.setDEF("hanim_skullbase")
HAnimJoint151.setCenter([0.0044,1.6209,0.0236])
HAnimJoint151.setStiffness([0,0,0])
HAnimSegment152 = HAnimSegment()
HAnimSegment152.setName("skull")
HAnimSegment152.setDEF("hanim_skull")
Transform153 = Transform()
Transform153.setTranslation([0.0044,1.6209,0.0236])
Shape154 = Shape()
Shape154.setUSE("DiamondShape")

Transform153.addChildren(Shape154)

HAnimSegment152.addChildren(Transform153)
HAnimSite155 = HAnimSite()
HAnimSite155.setName("skull_vertex_tip")
HAnimSite155.setDEF("hanim_skull_vertex_tip")
HAnimSite155.setTranslation([0.005,1.7504,0.0055])

HAnimSegment152.addChildren(HAnimSite155)
HAnimSite156 = HAnimSite()
HAnimSite156.setName("sellion_pt")
HAnimSite156.setDEF("hanim_sellion_pt")
HAnimSite156.setTranslation([0.0058,1.6316,0.0852])

HAnimSegment152.addChildren(HAnimSite156)
HAnimSite157 = HAnimSite()
HAnimSite157.setName("r_infraorbitale_pt")
HAnimSite157.setDEF("hanim_r_infraorbitale_pt")
HAnimSite157.setTranslation([-0.0237,1.6171,0.0752])

HAnimSegment152.addChildren(HAnimSite157)
HAnimSite158 = HAnimSite()
HAnimSite158.setName("l_infraorbitale_pt")
HAnimSite158.setDEF("hanim_l_infraorbitale_pt")
HAnimSite158.setTranslation([0.0341,1.6171,0.0752])

HAnimSegment152.addChildren(HAnimSite158)
HAnimSite159 = HAnimSite()
HAnimSite159.setName("supramenton_pt")
HAnimSite159.setDEF("hanim_supramenton_pt")
HAnimSite159.setTranslation([0.0061,1.541,0.0805])

HAnimSegment152.addChildren(HAnimSite159)
HAnimSite160 = HAnimSite()
HAnimSite160.setName("r_tragion_pt")
HAnimSite160.setDEF("hanim_r_tragion_pt")
HAnimSite160.setTranslation([-0.0646,1.6347,0.0302])

HAnimSegment152.addChildren(HAnimSite160)
HAnimSite161 = HAnimSite()
HAnimSite161.setName("r_gonion_pt")
HAnimSite161.setDEF("hanim_r_gonion_pt")
HAnimSite161.setTranslation([-0.052,1.5529,0.0347])

HAnimSegment152.addChildren(HAnimSite161)
HAnimSite162 = HAnimSite()
HAnimSite162.setName("l_tragion_pt")
HAnimSite162.setDEF("hanim_l_tragion_pt")
HAnimSite162.setTranslation([0.0739,1.6348,0.0282])

HAnimSegment152.addChildren(HAnimSite162)
HAnimSite163 = HAnimSite()
HAnimSite163.setName("l_gonion_pt")
HAnimSite163.setDEF("hanim_l_gonion_pt")
HAnimSite163.setTranslation([0.0631,1.553,0.033])

HAnimSegment152.addChildren(HAnimSite163)
HAnimSite164 = HAnimSite()
HAnimSite164.setName("nuchale_pt")
HAnimSite164.setDEF("hanim_nuchale_pt")
HAnimSite164.setTranslation([0.0039,1.5972,-0.0796])

HAnimSegment152.addChildren(HAnimSite164)

HAnimJoint151.addChildren(HAnimSegment152)

HAnimJoint150.addChildren(HAnimJoint151)

HAnimJoint37.addChildren(HAnimJoint150)

HAnimHumanoid30.setSkeleton(HAnimJoint37)
HAnimSite165 = HAnimSite()
HAnimSite165.setName("DiamondManLOA1_view")
HAnimSite165.setDEF("hanim_DiamondManLOA1_view")
Viewpoint166 = Viewpoint()
Viewpoint166.setDEF("InclinedView")
Viewpoint166.setDescription("Inclined View")
Viewpoint166.setOrientation([-0.113,0.993,0.0347,0.671])
Viewpoint166.setPosition([1.62,1.05,2.06])

HAnimSite165.addChildren(Viewpoint166)
Viewpoint167 = Viewpoint()
Viewpoint167.setDEF("FrontView")
Viewpoint167.setDescription("Front View")
Viewpoint167.setPosition([0,0.854,2.57665])

HAnimSite165.addChildren(Viewpoint167)
Viewpoint168 = Viewpoint()
Viewpoint168.setDEF("SideView")
Viewpoint168.setDescription("Side View")
Viewpoint168.setOrientation([0,1,0,1.57079])
Viewpoint168.setPosition([2.5929,0.854,0])

HAnimSite165.addChildren(Viewpoint168)
Viewpoint169 = Viewpoint()
Viewpoint169.setDEF("TopView")
Viewpoint169.setDescription("Top View")
Viewpoint169.setOrientation([1,0,0,-1.57079])
Viewpoint169.setPosition([0,3.4495,0])

HAnimSite165.addChildren(Viewpoint169)

HAnimHumanoid30.addViewpoints(HAnimSite165)
HAnimJoint170 = HAnimJoint()
HAnimJoint170.setUSE("hanim_humanoid_root")

HAnimHumanoid30.addJoints(HAnimJoint170)
HAnimJoint171 = HAnimJoint()
HAnimJoint171.setUSE("hanim_sacroiliac")

HAnimHumanoid30.addJoints(HAnimJoint171)
HAnimJoint172 = HAnimJoint()
HAnimJoint172.setUSE("hanim_vl1")

HAnimHumanoid30.addJoints(HAnimJoint172)
HAnimJoint173 = HAnimJoint()
HAnimJoint173.setUSE("hanim_vc4")

HAnimHumanoid30.addJoints(HAnimJoint173)
HAnimJoint174 = HAnimJoint()
HAnimJoint174.setUSE("hanim_skullbase")

HAnimHumanoid30.addJoints(HAnimJoint174)
HAnimJoint175 = HAnimJoint()
HAnimJoint175.setUSE("hanim_vl5")

HAnimHumanoid30.addJoints(HAnimJoint175)
HAnimJoint176 = HAnimJoint()
HAnimJoint176.setUSE("hanim_l_elbow")

HAnimHumanoid30.addJoints(HAnimJoint176)
HAnimJoint177 = HAnimJoint()
HAnimJoint177.setUSE("hanim_r_elbow")

HAnimHumanoid30.addJoints(HAnimJoint177)
HAnimJoint178 = HAnimJoint()
HAnimJoint178.setUSE("hanim_l_hip")

HAnimHumanoid30.addJoints(HAnimJoint178)
HAnimJoint179 = HAnimJoint()
HAnimJoint179.setUSE("hanim_r_hip")

HAnimHumanoid30.addJoints(HAnimJoint179)
HAnimJoint180 = HAnimJoint()
HAnimJoint180.setUSE("hanim_l_knee")

HAnimHumanoid30.addJoints(HAnimJoint180)
HAnimJoint181 = HAnimJoint()
HAnimJoint181.setUSE("hanim_r_knee")

HAnimHumanoid30.addJoints(HAnimJoint181)
HAnimJoint182 = HAnimJoint()
HAnimJoint182.setUSE("hanim_l_metatarsophalangeal_2")

HAnimHumanoid30.addJoints(HAnimJoint182)
HAnimJoint183 = HAnimJoint()
HAnimJoint183.setUSE("hanim_r_metatarsophalangeal_2")

HAnimHumanoid30.addJoints(HAnimJoint183)
HAnimJoint184 = HAnimJoint()
HAnimJoint184.setUSE("hanim_l_radiocarpal")

HAnimHumanoid30.addJoints(HAnimJoint184)
HAnimJoint185 = HAnimJoint()
HAnimJoint185.setUSE("hanim_r_radiocarpal")

HAnimHumanoid30.addJoints(HAnimJoint185)
HAnimJoint186 = HAnimJoint()
HAnimJoint186.setUSE("hanim_l_shoulder")

HAnimHumanoid30.addJoints(HAnimJoint186)
HAnimJoint187 = HAnimJoint()
HAnimJoint187.setUSE("hanim_r_shoulder")

HAnimHumanoid30.addJoints(HAnimJoint187)
HAnimJoint188 = HAnimJoint()
HAnimJoint188.setUSE("hanim_l_talocrural")

HAnimHumanoid30.addJoints(HAnimJoint188)
HAnimJoint189 = HAnimJoint()
HAnimJoint189.setUSE("hanim_r_talocrural")

HAnimHumanoid30.addJoints(HAnimJoint189)
HAnimSegment190 = HAnimSegment()
HAnimSegment190.setUSE("hanim_pelvis")

HAnimHumanoid30.addSegments(HAnimSegment190)
HAnimSegment191 = HAnimSegment()
HAnimSegment191.setUSE("hanim_l1")

HAnimHumanoid30.addSegments(HAnimSegment191)
HAnimSegment192 = HAnimSegment()
HAnimSegment192.setUSE("hanim_c4")

HAnimHumanoid30.addSegments(HAnimSegment192)
HAnimSegment193 = HAnimSegment()
HAnimSegment193.setUSE("hanim_skull")

HAnimHumanoid30.addSegments(HAnimSegment193)
HAnimSegment194 = HAnimSegment()
HAnimSegment194.setUSE("hanim_l_calf")

HAnimHumanoid30.addSegments(HAnimSegment194)
HAnimSegment195 = HAnimSegment()
HAnimSegment195.setUSE("hanim_r_calf")

HAnimHumanoid30.addSegments(HAnimSegment195)
HAnimSegment196 = HAnimSegment()
HAnimSegment196.setUSE("hanim_l_carpal")

HAnimHumanoid30.addSegments(HAnimSegment196)
HAnimSegment197 = HAnimSegment()
HAnimSegment197.setUSE("hanim_r_carpal")

HAnimHumanoid30.addSegments(HAnimSegment197)
HAnimSegment198 = HAnimSegment()
HAnimSegment198.setUSE("hanim_l_forearm")

HAnimHumanoid30.addSegments(HAnimSegment198)
HAnimSegment199 = HAnimSegment()
HAnimSegment199.setUSE("hanim_r_forearm")

HAnimHumanoid30.addSegments(HAnimSegment199)
HAnimSegment200 = HAnimSegment()
HAnimSegment200.setUSE("hanim_l_talus")

HAnimHumanoid30.addSegments(HAnimSegment200)
HAnimSegment201 = HAnimSegment()
HAnimSegment201.setUSE("hanim_r_talus")

HAnimHumanoid30.addSegments(HAnimSegment201)
HAnimSegment202 = HAnimSegment()
HAnimSegment202.setUSE("hanim_l_tarsal_proximal_phalanx_2")

HAnimHumanoid30.addSegments(HAnimSegment202)
HAnimSegment203 = HAnimSegment()
HAnimSegment203.setUSE("hanim_r_tarsal_proximal_phalanx_2")

HAnimHumanoid30.addSegments(HAnimSegment203)
HAnimSegment204 = HAnimSegment()
HAnimSegment204.setUSE("hanim_l_thigh")

HAnimHumanoid30.addSegments(HAnimSegment204)
HAnimSegment205 = HAnimSegment()
HAnimSegment205.setUSE("hanim_r_thigh")

HAnimHumanoid30.addSegments(HAnimSegment205)
HAnimSegment206 = HAnimSegment()
HAnimSegment206.setUSE("hanim_l_upperarm")

HAnimHumanoid30.addSegments(HAnimSegment206)
HAnimSegment207 = HAnimSegment()
HAnimSegment207.setUSE("hanim_r_upperarm")

HAnimHumanoid30.addSegments(HAnimSegment207)
HAnimSite208 = HAnimSite()
HAnimSite208.setUSE("hanim_skull_vertex_tip")

HAnimHumanoid30.addSites(HAnimSite208)
HAnimSite209 = HAnimSite()
HAnimSite209.setUSE("hanim_sellion_pt")

HAnimHumanoid30.addSites(HAnimSite209)
HAnimSite210 = HAnimSite()
HAnimSite210.setUSE("hanim_supramenton_pt")

HAnimHumanoid30.addSites(HAnimSite210)
HAnimSite211 = HAnimSite()
HAnimSite211.setUSE("hanim_nuchale_pt")

HAnimHumanoid30.addSites(HAnimSite211)
HAnimSite212 = HAnimSite()
HAnimSite212.setUSE("hanim_l_calcaneus_posterior_pt")

HAnimHumanoid30.addSites(HAnimSite212)
HAnimSite213 = HAnimSite()
HAnimSite213.setUSE("hanim_r_calcaneus_posterior_pt")

HAnimHumanoid30.addSites(HAnimSite213)
HAnimSite214 = HAnimSite()
HAnimSite214.setUSE("hanim_l_dactylion_pt")

HAnimHumanoid30.addSites(HAnimSite214)
HAnimSite215 = HAnimSite()
HAnimSite215.setUSE("hanim_r_dactylion_pt")

HAnimHumanoid30.addSites(HAnimSite215)
HAnimSite216 = HAnimSite()
HAnimSite216.setUSE("hanim_l_femoral_lateral_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite216)
HAnimSite217 = HAnimSite()
HAnimSite217.setUSE("hanim_r_femoral_lateral_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite217)
HAnimSite218 = HAnimSite()
HAnimSite218.setUSE("hanim_l_femoral_medial_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite218)
HAnimSite219 = HAnimSite()
HAnimSite219.setUSE("hanim_r_femoral_medial_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite219)
HAnimSite220 = HAnimSite()
HAnimSite220.setUSE("hanim_r_gonion_pt")

HAnimHumanoid30.addSites(HAnimSite220)
HAnimSite221 = HAnimSite()
HAnimSite221.setUSE("hanim_l_gonion_pt")

HAnimHumanoid30.addSites(HAnimSite221)
HAnimSite222 = HAnimSite()
HAnimSite222.setUSE("hanim_l_hand_tip")

HAnimHumanoid30.addSites(HAnimSite222)
HAnimSite223 = HAnimSite()
HAnimSite223.setUSE("hanim_r_hand_tip")

HAnimHumanoid30.addSites(HAnimSite223)
HAnimSite224 = HAnimSite()
HAnimSite224.setUSE("hanim_l_humeral_lateral_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite224)
HAnimSite225 = HAnimSite()
HAnimSite225.setUSE("hanim_r_humeral_lateral_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite225)
HAnimSite226 = HAnimSite()
HAnimSite226.setUSE("hanim_l_humeral_medial_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite226)
HAnimSite227 = HAnimSite()
HAnimSite227.setUSE("hanim_r_humeral_medial_epicondyle_pt")

HAnimHumanoid30.addSites(HAnimSite227)
HAnimSite228 = HAnimSite()
HAnimSite228.setUSE("hanim_r_infraorbitale_pt")

HAnimHumanoid30.addSites(HAnimSite228)
HAnimSite229 = HAnimSite()
HAnimSite229.setUSE("hanim_l_infraorbitale_pt")

HAnimHumanoid30.addSites(HAnimSite229)
HAnimSite230 = HAnimSite()
HAnimSite230.setUSE("hanim_l_knee_crease_pt")

HAnimHumanoid30.addSites(HAnimSite230)
HAnimSite231 = HAnimSite()
HAnimSite231.setUSE("hanim_r_knee_crease_pt")

HAnimHumanoid30.addSites(HAnimSite231)
HAnimSite232 = HAnimSite()
HAnimSite232.setUSE("hanim_l_lateral_malleolus_pt")

HAnimHumanoid30.addSites(HAnimSite232)
HAnimSite233 = HAnimSite()
HAnimSite233.setUSE("hanim_r_lateral_malleolus_pt")

HAnimHumanoid30.addSites(HAnimSite233)
HAnimSite234 = HAnimSite()
HAnimSite234.setUSE("hanim_l_medial_malleolus_pt")

HAnimHumanoid30.addSites(HAnimSite234)
HAnimSite235 = HAnimSite()
HAnimSite235.setUSE("hanim_r_medial_malleolus_pt")

HAnimHumanoid30.addSites(HAnimSite235)
HAnimSite236 = HAnimSite()
HAnimSite236.setUSE("hanim_l_metacarpal_phalanx_2_pt")

HAnimHumanoid30.addSites(HAnimSite236)
HAnimSite237 = HAnimSite()
HAnimSite237.setUSE("hanim_r_metacarpal_phalanx_2_pt")

HAnimHumanoid30.addSites(HAnimSite237)
HAnimSite238 = HAnimSite()
HAnimSite238.setUSE("hanim_l_metacarpal_phalanx_5_pt")

HAnimHumanoid30.addSites(HAnimSite238)
HAnimSite239 = HAnimSite()
HAnimSite239.setUSE("hanim_r_metacarpal_phalanx_5_pt")

HAnimHumanoid30.addSites(HAnimSite239)
HAnimSite240 = HAnimSite()
HAnimSite240.setUSE("hanim_l_metatarsal_phalanx_1_pt")

HAnimHumanoid30.addSites(HAnimSite240)
HAnimSite241 = HAnimSite()
HAnimSite241.setUSE("hanim_r_metatarsal_phalanx_1_pt")

HAnimHumanoid30.addSites(HAnimSite241)
HAnimSite242 = HAnimSite()
HAnimSite242.setUSE("hanim_l_metatarsal_phalanx_5_pt")

HAnimHumanoid30.addSites(HAnimSite242)
HAnimSite243 = HAnimSite()
HAnimSite243.setUSE("hanim_r_metatarsal_phalanx_5_pt")

HAnimHumanoid30.addSites(HAnimSite243)
HAnimSite244 = HAnimSite()
HAnimSite244.setUSE("hanim_l_middistal_tip")

HAnimHumanoid30.addSites(HAnimSite244)
HAnimSite245 = HAnimSite()
HAnimSite245.setUSE("hanim_r_middistal_tip")

HAnimHumanoid30.addSites(HAnimSite245)
HAnimSite246 = HAnimSite()
HAnimSite246.setUSE("hanim_l_olecranon_pt")

HAnimHumanoid30.addSites(HAnimSite246)
HAnimSite247 = HAnimSite()
HAnimSite247.setUSE("hanim_r_olecranon_pt")

HAnimHumanoid30.addSites(HAnimSite247)
HAnimSite248 = HAnimSite()
HAnimSite248.setUSE("hanim_l_radial_styloid_pt")

HAnimHumanoid30.addSites(HAnimSite248)
HAnimSite249 = HAnimSite()
HAnimSite249.setUSE("hanim_r_radial_styloid_pt")

HAnimHumanoid30.addSites(HAnimSite249)
HAnimSite250 = HAnimSite()
HAnimSite250.setUSE("hanim_l_radiale_pt")

HAnimHumanoid30.addSites(HAnimSite250)
HAnimSite251 = HAnimSite()
HAnimSite251.setUSE("hanim_r_radiale_pt")

HAnimHumanoid30.addSites(HAnimSite251)
HAnimSite252 = HAnimSite()
HAnimSite252.setUSE("hanim_l_sphyrion_pt")

HAnimHumanoid30.addSites(HAnimSite252)
HAnimSite253 = HAnimSite()
HAnimSite253.setUSE("hanim_r_sphyrion_pt")

HAnimHumanoid30.addSites(HAnimSite253)
HAnimSite254 = HAnimSite()
HAnimSite254.setUSE("hanim_l_tarsal_distal_phalanx_2_pt")

HAnimHumanoid30.addSites(HAnimSite254)
HAnimSite255 = HAnimSite()
HAnimSite255.setUSE("hanim_r_tarsal_distal_phalanx_2_pt")

HAnimHumanoid30.addSites(HAnimSite255)
HAnimSite256 = HAnimSite()
HAnimSite256.setUSE("hanim_r_tragion_pt")

HAnimHumanoid30.addSites(HAnimSite256)
HAnimSite257 = HAnimSite()
HAnimSite257.setUSE("hanim_l_tragion_pt")

HAnimHumanoid30.addSites(HAnimSite257)
HAnimSite258 = HAnimSite()
HAnimSite258.setUSE("hanim_l_ulnar_styloid_pt")

HAnimHumanoid30.addSites(HAnimSite258)
HAnimSite259 = HAnimSite()
HAnimSite259.setUSE("hanim_r_ulnar_styloid_pt")

HAnimHumanoid30.addSites(HAnimSite259)

Scene26.addChildren(HAnimHumanoid30)

X3D0.setScene(Scene26)
X3D0.toFileX3D("././DiamondManLOA1_RoundTrip.x3d")
