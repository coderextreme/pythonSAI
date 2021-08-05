from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
meta2 = meta()
meta2.setName("title")
meta2.setContent("CameraExamples.x3d")

head1.addMeta(meta2)
meta3 = meta()
meta3.setName("description")
meta3.setContent("Camera, CameraShot and CameraMove examples that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("documentation")
meta4.setContent("Two demos are found in the scene, click the \"red text\" on left or right to start. (a) SimpleShotsTest shows Zoom in/out, Pan left/right, Boom up/down, Tilt left/right, with each is defined by a CameraShot collecting a series of CameraMovements. (b) AimPointTest gradually slews the camera view to look at the sliding cube, then follows it around before returning to original viewpoint.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("creator")
meta5.setContent("Don Brutzman and Jeff Weekley")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("created")
meta6.setContent("18 June 2009")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("modified")
meta7.setContent("20 January 2020")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("TODO")
meta8.setContent("Schematron rules, backed up by initialize() checks")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("reference")
meta9.setContent("BeyondViewpointCameraNodesWeb3D2009.pdf")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("MovingImage")
meta10.setContent("CameraExamplesDemo.mp4")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("reference")
meta11.setContent("https://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("subject")
meta12.setContent("Camera nodes for Viewpoint navigation control")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("reference")
meta13.setContent("CameraPrototypes.x3d")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("reference")
meta14.setContent("CameraExamplesConsoleLog.txt")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("reference")
meta15.setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.avi")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("reference")
meta16.setContent("https://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d")

head1.addMeta(meta16)
meta17 = meta()
meta17.setName("identifier")
meta17.setContent("https://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d")

head1.addMeta(meta17)
meta18 = meta()
meta18.setName("reference")
meta18.setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d")

head1.addMeta(meta18)
meta19 = meta()
meta19.setName("generator")
meta19.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta19)
meta20 = meta()
meta20.setName("license")
meta20.setContent("../license.html")

head1.addMeta(meta20)

X3D0.setHead(head1)
Scene21 = Scene()
#=============== Camera ==============
WorldInfo22 = WorldInfo()
WorldInfo22.setTitle("CameraExamples.x3d")

Scene21.addChildren(WorldInfo22)
ExternProtoDeclare23 = ExternProtoDeclare()
ExternProtoDeclare23.setName("Camera")
ExternProtoDeclare23.setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images")
ExternProtoDeclare23.setUrl(["CameraPrototypes.x3d#Camera","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#Camera","CameraPrototypes.wrl#Camera","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#Camera"])
field24 = field()
field24.setName("description")
field24.setAccessType("inputOutput")
field24.setAppinfo("Text description to be displayed for this Camera")
field24.setType("SFString")

ExternProtoDeclare23.addField(field24)
field25 = field()
field25.setName("position")
field25.setAccessType("inputOutput")
field25.setAppinfo("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")
field25.setType("SFVec3f")

ExternProtoDeclare23.addField(field25)
field26 = field()
field26.setName("orientation")
field26.setAccessType("inputOutput")
field26.setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")
field26.setType("SFRotation")

ExternProtoDeclare23.addField(field26)
field27 = field()
field27.setName("fieldOfView")
field27.setAccessType("inputOutput")
field27.setAppinfo("pi/4")
field27.setType("SFFloat")

ExternProtoDeclare23.addField(field27)
field28 = field()
field28.setName("set_fraction")
field28.setAccessType("inputOnly")
field28.setAppinfo("input fraction drives interpolators")
field28.setType("SFFloat")

ExternProtoDeclare23.addField(field28)
field29 = field()
field29.setName("set_bind")
field29.setAccessType("inputOnly")
field29.setAppinfo("input event binds or unbinds this Camera")
field29.setType("SFBool")

ExternProtoDeclare23.addField(field29)
field30 = field()
field30.setName("bindTime")
field30.setAccessType("outputOnly")
field30.setAppinfo("output event indicates when this Camera is bound")
field30.setType("SFTime")

ExternProtoDeclare23.addField(field30)
field31 = field()
field31.setName("isBound")
field31.setAccessType("outputOnly")
field31.setAppinfo("output event indicates whether this Camera is bound or unbound")
field31.setType("SFBool")

ExternProtoDeclare23.addField(field31)
field32 = field()
field32.setName("nearClipPlane")
field32.setAccessType("inputOutput")
field32.setAppinfo("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]")
field32.setType("SFFloat")

ExternProtoDeclare23.addField(field32)
field33 = field()
field33.setName("farClipPlane")
field33.setAccessType("inputOutput")
field33.setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit")
field33.setType("SFFloat")

ExternProtoDeclare23.addField(field33)
field34 = field()
field34.setName("shots")
field34.setAccessType("inputOutput")
field34.setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes")
field34.setType("MFNode")

ExternProtoDeclare23.addField(field34)
field35 = field()
field35.setName("headlight")
field35.setAccessType("inputOutput")
field35.setAppinfo("Whether camera headlight is on or off")
field35.setType("SFBool")

ExternProtoDeclare23.addField(field35)
field36 = field()
field36.setName("headlightColor")
field36.setAccessType("inputOutput")
field36.setAppinfo("Camera headlight color")
field36.setType("SFColor")

ExternProtoDeclare23.addField(field36)
field37 = field()
field37.setName("headlightIntensity")
field37.setAccessType("inputOutput")
field37.setAppinfo("Camera headlight intensity")
field37.setType("SFFloat")

ExternProtoDeclare23.addField(field37)
field38 = field()
field38.setName("filterColor")
field38.setAccessType("inputOutput")
field38.setAppinfo("Camera filter color that modifies virtual lens capture")
field38.setType("SFColor")

ExternProtoDeclare23.addField(field38)
field39 = field()
field39.setName("filterTransparency")
field39.setAccessType("inputOutput")
field39.setAppinfo("Camera filter transparency that modifies virtual lens capture")
field39.setType("SFFloat")

ExternProtoDeclare23.addField(field39)
field40 = field()
field40.setName("upVector")
field40.setAccessType("inputOutput")
field40.setAppinfo("upVector changes modify camera orientation (and possibly vice versa)")
field40.setType("SFVec3f")

ExternProtoDeclare23.addField(field40)
field41 = field()
field41.setName("fStop")
field41.setAccessType("inputOutput")
field41.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field41.setType("SFFloat")

ExternProtoDeclare23.addField(field41)
field42 = field()
field42.setName("focusDistance")
field42.setAccessType("inputOutput")
field42.setAppinfo("Distance to focal plane of sharpest focus")
field42.setType("SFFloat")

ExternProtoDeclare23.addField(field42)
field43 = field()
field43.setName("isActive")
field43.setAccessType("outputOnly")
field43.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field43.setType("SFBool")

ExternProtoDeclare23.addField(field43)
field44 = field()
field44.setName("totalDuration")
field44.setAccessType("outputOnly")
field44.setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations")
field44.setType("SFTime")

ExternProtoDeclare23.addField(field44)
field45 = field()
field45.setName("offlineRender")
field45.setAccessType("inputOutput")
field45.setAppinfo("OfflineRender node")
field45.setType("SFNode")

ExternProtoDeclare23.addField(field45)
field46 = field()
field46.setName("traceEnabled")
field46.setAccessType("initializeOnly")
field46.setAppinfo("enable console output to trace script computations and prototype progress")
field46.setType("SFBool")

ExternProtoDeclare23.addField(field46)
#Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields

Scene21.addChildren(ExternProtoDeclare23)
#=============== CameraShot ==============
ExternProtoDeclare47 = ExternProtoDeclare()
ExternProtoDeclare47.setName("CameraShot")
ExternProtoDeclare47.setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot")
ExternProtoDeclare47.setUrl(["CameraPrototypes.x3d#CameraShot","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraShot","CameraPrototypes.wrl#CameraShot","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraShot"])
field48 = field()
field48.setName("description")
field48.setAccessType("inputOutput")
field48.setAppinfo("Text description to be displayed for this CameraShot")
field48.setType("SFString")

ExternProtoDeclare47.addField(field48)
field49 = field()
field49.setName("enabled")
field49.setAccessType("inputOutput")
field49.setAppinfo("Whether this CameraShot can be activated")
field49.setType("SFBool")

ExternProtoDeclare47.addField(field49)
field50 = field()
field50.setName("moves")
field50.setAccessType("inputOutput")
field50.setAppinfo("Set of CameraMovement nodes")
field50.setType("MFNode")
#initializing CameraMovement nodes are inserted here by scene author using ProtoInstance

ExternProtoDeclare47.addField(field50)
field51 = field()
field51.setName("initialPosition")
field51.setAccessType("inputOutput")
field51.setAppinfo("Setup to reinitialize camera position for this shot")
field51.setType("SFVec3f")

ExternProtoDeclare47.addField(field51)
field52 = field()
field52.setName("initialOrientation")
field52.setAccessType("inputOutput")
field52.setAppinfo("Setup to reinitialize camera rotation for this shot")
field52.setType("SFRotation")

ExternProtoDeclare47.addField(field52)
field53 = field()
field53.setName("initialAimPoint")
field53.setAccessType("inputOutput")
field53.setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot")
field53.setType("SFVec3f")

ExternProtoDeclare47.addField(field53)
field54 = field()
field54.setName("initialFieldOfView")
field54.setAccessType("inputOutput")
field54.setAppinfo("pi/4")
field54.setType("SFFloat")

ExternProtoDeclare47.addField(field54)
field55 = field()
field55.setName("initialFStop")
field55.setAccessType("inputOutput")
field55.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field55.setType("SFFloat")

ExternProtoDeclare47.addField(field55)
field56 = field()
field56.setName("initialFocusDistance")
field56.setAccessType("inputOutput")
field56.setAppinfo("Distance to focal plane of sharpest focus")
field56.setType("SFFloat")

ExternProtoDeclare47.addField(field56)
field57 = field()
field57.setName("shotDuration")
field57.setAccessType("outputOnly")
field57.setAppinfo("Subtotal duration of contained CameraMovement move durations")
field57.setType("SFTime")

ExternProtoDeclare47.addField(field57)
field58 = field()
field58.setName("isActive")
field58.setAccessType("outputOnly")
field58.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field58.setType("SFBool")

ExternProtoDeclare47.addField(field58)
field59 = field()
field59.setName("traceEnabled")
field59.setAccessType("initializeOnly")
field59.setAppinfo("enable console output to trace script computations and prototype progress")
field59.setType("SFBool")

ExternProtoDeclare47.addField(field59)

Scene21.addChildren(ExternProtoDeclare47)
#=============== CameraMovement ==============
ExternProtoDeclare60 = ExternProtoDeclare()
ExternProtoDeclare60.setName("CameraMovement")
ExternProtoDeclare60.setAppinfo("CameraMovement defines a single camera movement animation")
ExternProtoDeclare60.setUrl(["CameraPrototypes.x3d#CameraMovement","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraMovement","CameraPrototypes.wrl#CameraMovement","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraMovement"])
field61 = field()
field61.setName("description")
field61.setAccessType("inputOutput")
field61.setAppinfo("Text description to be displayed for this CameraMovement")
field61.setType("SFString")

ExternProtoDeclare60.addField(field61)
field62 = field()
field62.setName("enabled")
field62.setAccessType("inputOutput")
field62.setAppinfo("Whether this CameraMovement can be activated")
field62.setType("SFBool")

ExternProtoDeclare60.addField(field62)
field63 = field()
field63.setName("duration")
field63.setAccessType("inputOutput")
field63.setAppinfo("Duration in seconds for this move")
field63.setType("SFFloat")

ExternProtoDeclare60.addField(field63)
field64 = field()
field64.setName("goalPosition")
field64.setAccessType("inputOutput")
field64.setAppinfo("Goal camera position for this move")
field64.setType("SFVec3f")

ExternProtoDeclare60.addField(field64)
field65 = field()
field65.setName("goalOrientation")
field65.setAccessType("inputOutput")
field65.setAppinfo("Goal camera rotation for this move")
field65.setType("SFRotation")

ExternProtoDeclare60.addField(field65)
field66 = field()
field66.setName("tracking")
field66.setAccessType("inputOutput")
field66.setAppinfo("Whether or not camera direction is tracking towards the aimPoint")
field66.setType("SFBool")

ExternProtoDeclare60.addField(field66)
field67 = field()
field67.setName("goalAimPoint")
field67.setAccessType("inputOutput")
field67.setAppinfo("Goal aimPoint for this move, ignored if tracking=false")
field67.setType("SFVec3f")

ExternProtoDeclare60.addField(field67)
field68 = field()
field68.setName("goalFieldOfView")
field68.setAccessType("inputOutput")
field68.setAppinfo("Goal fieldOfView for this move")
field68.setType("SFFloat")

ExternProtoDeclare60.addField(field68)
field69 = field()
field69.setName("goalFStop")
field69.setAccessType("inputOutput")
field69.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field69.setType("SFFloat")

ExternProtoDeclare60.addField(field69)
field70 = field()
field70.setName("goalFocusDistance")
field70.setAccessType("inputOutput")
field70.setAppinfo("Distance to focal plane of sharpest focus")
field70.setType("SFFloat")

ExternProtoDeclare60.addField(field70)
field71 = field()
field71.setName("isActive")
field71.setAccessType("outputOnly")
field71.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field71.setType("SFBool")

ExternProtoDeclare60.addField(field71)
field72 = field()
field72.setName("traceEnabled")
field72.setAccessType("initializeOnly")
field72.setAppinfo("enable console output to trace script computations and prototype progress")
field72.setType("SFBool")

ExternProtoDeclare60.addField(field72)

Scene21.addChildren(ExternProtoDeclare60)
#=============== OfflineRender ==============
ExternProtoDeclare73 = ExternProtoDeclare()
ExternProtoDeclare73.setName("OfflineRender")
ExternProtoDeclare73.setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)")
ExternProtoDeclare73.setUrl(["CameraPrototypes.x3d#OfflineRender","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#OfflineRender","CameraPrototypes.wrl#OfflineRender","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#OfflineRender"])
field74 = field()
field74.setName("description")
field74.setAccessType("inputOutput")
field74.setAppinfo("Text description to be displayed for this OfflineRender")
field74.setType("SFString")

ExternProtoDeclare73.addField(field74)
field75 = field()
field75.setName("enabled")
field75.setAccessType("inputOutput")
field75.setAppinfo("Whether this OfflineRender can be activated")
field75.setType("SFBool")

ExternProtoDeclare73.addField(field75)
field76 = field()
field76.setName("frameRate")
field76.setAccessType("inputOutput")
field76.setAppinfo("Frames per second recorded for this rendering")
field76.setType("SFFloat")

ExternProtoDeclare73.addField(field76)
field77 = field()
field77.setName("frameSize")
field77.setAccessType("inputOutput")
field77.setAppinfo("Size of frame in number of pixels width and height")
field77.setType("SFVec2f")

ExternProtoDeclare73.addField(field77)
field78 = field()
field78.setName("pixelAspectRatio")
field78.setAccessType("inputOutput")
field78.setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1")
field78.setType("SFFloat")

ExternProtoDeclare73.addField(field78)
field79 = field()
field79.setName("set_startTime")
field79.setAccessType("inputOnly")
field79.setAppinfo("Begin render operation")
field79.setType("SFTime")

ExternProtoDeclare73.addField(field79)
field80 = field()
field80.setName("progress")
field80.setAccessType("outputOnly")
field80.setAppinfo("Progress performing render operation (0..1)")
field80.setType("SFFloat")

ExternProtoDeclare73.addField(field80)
field81 = field()
field81.setName("renderCompleteTime")
field81.setAccessType("outputOnly")
field81.setAppinfo("Render operation complete")
field81.setType("SFTime")

ExternProtoDeclare73.addField(field81)
field82 = field()
field82.setName("movieFormat")
field82.setAccessType("initializeOnly")
field82.setAppinfo("Format of rendered output movie (mpeg mp4 etc.), use first supported format")
field82.setType("MFString")

ExternProtoDeclare73.addField(field82)
field83 = field()
field83.setName("imageFormat")
field83.setAccessType("initializeOnly")
field83.setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format")
field83.setType("MFString")

ExternProtoDeclare73.addField(field83)
field84 = field()
field84.setName("traceEnabled")
field84.setAccessType("initializeOnly")
field84.setAppinfo("enable console output to trace script computations and prototype progress")
field84.setType("SFBool")

ExternProtoDeclare73.addField(field84)
#TODO non-photorealistic rendering (NPR) parameters

Scene21.addChildren(ExternProtoDeclare73)
#=============== Lights, camera, action! ==============
DirectionalLight85 = DirectionalLight()
DirectionalLight85.setDirection([0,-1,0])
DirectionalLight85.setGlobal(True)
DirectionalLight85.setIntensity(0.8)

Scene21.addChildren(DirectionalLight85)
NavigationInfo86 = NavigationInfo()
NavigationInfo86.setType(["EXAMINE","FLY","ANY"])

Scene21.addChildren(NavigationInfo86)
Viewpoint87 = Viewpoint()
Viewpoint87.setDescription("Camera test scene entry view")
Viewpoint87.setPosition([0,2,12])

Scene21.addChildren(Viewpoint87)
Viewpoint88 = Viewpoint()
Viewpoint88.setDescription("Camera test scene from above")
Viewpoint88.setOrientation([1,0,0,-1.57079])
Viewpoint88.setPosition([0,150,0])

Scene21.addChildren(Viewpoint88)
#Keep prototype instances in same file while developing, then move later
#We will create examples matching those in the paper
#=============== Camera.SimpleShotsTest ==============
ProtoInstance89 = ProtoInstance()
ProtoInstance89.setName("Camera")
ProtoInstance89.setDEF("Camera.SimpleShotsTest")
fieldValue90 = fieldValue()
fieldValue90.setName("description")
fieldValue90.setValue("SimpleShotsTest for camera Zoom Dolly Pan Boom and Tilt")

ProtoInstance89.addFieldValue(fieldValue90)
fieldValue91 = fieldValue()
fieldValue91.setName("headlight")
fieldValue91.setValue("true")

ProtoInstance89.addFieldValue(fieldValue91)
fieldValue92 = fieldValue()
fieldValue92.setName("position")
fieldValue92.setValue("-4 4 10")

ProtoInstance89.addFieldValue(fieldValue92)
fieldValue93 = fieldValue()
fieldValue93.setName("shots")
ProtoInstance94 = ProtoInstance()
ProtoInstance94.setName("CameraShot")
ProtoInstance94.setDEF("Zoom")
fieldValue95 = fieldValue()
fieldValue95.setName("description")
fieldValue95.setValue("Simple shot of Camera Zoom")

ProtoInstance94.addFieldValue(fieldValue95)
fieldValue96 = fieldValue()
fieldValue96.setName("initialPosition")
fieldValue96.setValue("-50 1 -10")

ProtoInstance94.addFieldValue(fieldValue96)
fieldValue97 = fieldValue()
fieldValue97.setName("initialOrientation")
fieldValue97.setValue("0 1 0 0")

ProtoInstance94.addFieldValue(fieldValue97)
fieldValue98 = fieldValue()
fieldValue98.setName("moves")
ProtoInstance99 = ProtoInstance()
ProtoInstance99.setName("CameraMovement")
fieldValue100 = fieldValue()
fieldValue100.setName("description")
fieldValue100.setValue("Camera Zoom In")

ProtoInstance99.addFieldValue(fieldValue100)
fieldValue101 = fieldValue()
fieldValue101.setName("duration")
fieldValue101.setValue("3")

ProtoInstance99.addFieldValue(fieldValue101)
fieldValue102 = fieldValue()
fieldValue102.setName("goalPosition")
fieldValue102.setValue("-50 1 -15")

ProtoInstance99.addFieldValue(fieldValue102)
fieldValue103 = fieldValue()
fieldValue103.setName("goalOrientation")
fieldValue103.setValue("0 1 0 0")

ProtoInstance99.addFieldValue(fieldValue103)

fieldValue98.addChildren(ProtoInstance99)
ProtoInstance104 = ProtoInstance()
ProtoInstance104.setName("CameraMovement")
fieldValue105 = fieldValue()
fieldValue105.setName("description")
fieldValue105.setValue("Camera Zoom Out")

ProtoInstance104.addFieldValue(fieldValue105)
fieldValue106 = fieldValue()
fieldValue106.setName("duration")
fieldValue106.setValue("3")

ProtoInstance104.addFieldValue(fieldValue106)
fieldValue107 = fieldValue()
fieldValue107.setName("goalPosition")
fieldValue107.setValue("-50 1 -10")

ProtoInstance104.addFieldValue(fieldValue107)
fieldValue108 = fieldValue()
fieldValue108.setName("goalOrientation")
fieldValue108.setValue("0 1 0 0")

ProtoInstance104.addFieldValue(fieldValue108)

fieldValue98.addChildren(ProtoInstance104)
ProtoInstance109 = ProtoInstance()
ProtoInstance109.setName("CameraMovement")
fieldValue110 = fieldValue()
fieldValue110.setName("description")
fieldValue110.setValue("Camera Pause")

ProtoInstance109.addFieldValue(fieldValue110)
fieldValue111 = fieldValue()
fieldValue111.setName("duration")
fieldValue111.setValue("1")

ProtoInstance109.addFieldValue(fieldValue111)
fieldValue112 = fieldValue()
fieldValue112.setName("goalPosition")
fieldValue112.setValue("-50 1 -10")

ProtoInstance109.addFieldValue(fieldValue112)
fieldValue113 = fieldValue()
fieldValue113.setName("goalOrientation")
fieldValue113.setValue("0 1 0 0")

ProtoInstance109.addFieldValue(fieldValue113)

fieldValue98.addChildren(ProtoInstance109)

ProtoInstance94.addFieldValue(fieldValue98)

fieldValue93.addChildren(ProtoInstance94)
ProtoInstance114 = ProtoInstance()
ProtoInstance114.setName("CameraShot")
ProtoInstance114.setDEF("Dolly")
fieldValue115 = fieldValue()
fieldValue115.setName("description")
fieldValue115.setValue("Simple shot of Camera Dolly")

ProtoInstance114.addFieldValue(fieldValue115)
fieldValue116 = fieldValue()
fieldValue116.setName("initialPosition")
fieldValue116.setValue("-40 1 -10")

ProtoInstance114.addFieldValue(fieldValue116)
fieldValue117 = fieldValue()
fieldValue117.setName("initialOrientation")
fieldValue117.setValue("0 1 0 0")

ProtoInstance114.addFieldValue(fieldValue117)
fieldValue118 = fieldValue()
fieldValue118.setName("moves")
ProtoInstance119 = ProtoInstance()
ProtoInstance119.setName("CameraMovement")
ProtoInstance119.setDEF("DollyMove1")
fieldValue120 = fieldValue()
fieldValue120.setName("description")
fieldValue120.setValue("Camera Dolly from Right to Left")

ProtoInstance119.addFieldValue(fieldValue120)
fieldValue121 = fieldValue()
fieldValue121.setName("duration")
fieldValue121.setValue("3")

ProtoInstance119.addFieldValue(fieldValue121)
fieldValue122 = fieldValue()
fieldValue122.setName("goalPosition")
fieldValue122.setValue("-45 1 -10")

ProtoInstance119.addFieldValue(fieldValue122)
fieldValue123 = fieldValue()
fieldValue123.setName("goalOrientation")
fieldValue123.setValue("0 1 0 0")

ProtoInstance119.addFieldValue(fieldValue123)

fieldValue118.addChildren(ProtoInstance119)
ProtoInstance124 = ProtoInstance()
ProtoInstance124.setName("CameraMovement")
fieldValue125 = fieldValue()
fieldValue125.setName("description")
fieldValue125.setValue("Camera Dolly from Left to Right")

ProtoInstance124.addFieldValue(fieldValue125)
fieldValue126 = fieldValue()
fieldValue126.setName("duration")
fieldValue126.setValue("3")

ProtoInstance124.addFieldValue(fieldValue126)
fieldValue127 = fieldValue()
fieldValue127.setName("goalPosition")
fieldValue127.setValue("-40 1 -10")

ProtoInstance124.addFieldValue(fieldValue127)
fieldValue128 = fieldValue()
fieldValue128.setName("goalOrientation")
fieldValue128.setValue("0 1 0 0")

ProtoInstance124.addFieldValue(fieldValue128)

fieldValue118.addChildren(ProtoInstance124)
ProtoInstance129 = ProtoInstance()
ProtoInstance129.setName("CameraMovement")
fieldValue130 = fieldValue()
fieldValue130.setName("description")
fieldValue130.setValue("Camera Pause")

ProtoInstance129.addFieldValue(fieldValue130)
fieldValue131 = fieldValue()
fieldValue131.setName("duration")
fieldValue131.setValue("1")

ProtoInstance129.addFieldValue(fieldValue131)
fieldValue132 = fieldValue()
fieldValue132.setName("goalPosition")
fieldValue132.setValue("-40 1 -10")

ProtoInstance129.addFieldValue(fieldValue132)
fieldValue133 = fieldValue()
fieldValue133.setName("goalOrientation")
fieldValue133.setValue("0 1 0 0")

ProtoInstance129.addFieldValue(fieldValue133)

fieldValue118.addChildren(ProtoInstance129)

ProtoInstance114.addFieldValue(fieldValue118)

fieldValue93.addChildren(ProtoInstance114)
ProtoInstance134 = ProtoInstance()
ProtoInstance134.setName("CameraShot")
ProtoInstance134.setDEF("Pan")
fieldValue135 = fieldValue()
fieldValue135.setName("description")
fieldValue135.setValue("Simple shot of Camera Pan left right and back to center")

ProtoInstance134.addFieldValue(fieldValue135)
fieldValue136 = fieldValue()
fieldValue136.setName("initialPosition")
fieldValue136.setValue("-30 1 -10")

ProtoInstance134.addFieldValue(fieldValue136)
fieldValue137 = fieldValue()
fieldValue137.setName("initialOrientation")
fieldValue137.setValue("0 1 0 0")

ProtoInstance134.addFieldValue(fieldValue137)
fieldValue138 = fieldValue()
fieldValue138.setName("moves")
ProtoInstance139 = ProtoInstance()
ProtoInstance139.setName("CameraMovement")
ProtoInstance139.setDEF("PanLeft")
fieldValue140 = fieldValue()
fieldValue140.setName("description")
fieldValue140.setValue("Pan Left")

ProtoInstance139.addFieldValue(fieldValue140)
fieldValue141 = fieldValue()
fieldValue141.setName("duration")
fieldValue141.setValue("2")

ProtoInstance139.addFieldValue(fieldValue141)
fieldValue142 = fieldValue()
fieldValue142.setName("goalPosition")
fieldValue142.setValue("-30 1 -10")

ProtoInstance139.addFieldValue(fieldValue142)
fieldValue143 = fieldValue()
fieldValue143.setName("goalOrientation")
fieldValue143.setValue("0 1 0 0.4")

ProtoInstance139.addFieldValue(fieldValue143)

fieldValue138.addChildren(ProtoInstance139)
ProtoInstance144 = ProtoInstance()
ProtoInstance144.setName("CameraMovement")
ProtoInstance144.setDEF("PanRight")
fieldValue145 = fieldValue()
fieldValue145.setName("description")
fieldValue145.setValue("Pan Right")

ProtoInstance144.addFieldValue(fieldValue145)
fieldValue146 = fieldValue()
fieldValue146.setName("duration")
fieldValue146.setValue("3")

ProtoInstance144.addFieldValue(fieldValue146)
fieldValue147 = fieldValue()
fieldValue147.setName("goalPosition")
fieldValue147.setValue("-30 1 -10")

ProtoInstance144.addFieldValue(fieldValue147)
fieldValue148 = fieldValue()
fieldValue148.setName("goalOrientation")
fieldValue148.setValue("0 1 0 -0.4")

ProtoInstance144.addFieldValue(fieldValue148)

fieldValue138.addChildren(ProtoInstance144)
ProtoInstance149 = ProtoInstance()
ProtoInstance149.setName("CameraMovement")
fieldValue150 = fieldValue()
fieldValue150.setName("description")
fieldValue150.setValue("Camera Pan back to Center")

ProtoInstance149.addFieldValue(fieldValue150)
fieldValue151 = fieldValue()
fieldValue151.setName("duration")
fieldValue151.setValue("2")

ProtoInstance149.addFieldValue(fieldValue151)
fieldValue152 = fieldValue()
fieldValue152.setName("goalPosition")
fieldValue152.setValue("-30 1 -10")

ProtoInstance149.addFieldValue(fieldValue152)
fieldValue153 = fieldValue()
fieldValue153.setName("goalOrientation")
fieldValue153.setValue("0 1 0 0")

ProtoInstance149.addFieldValue(fieldValue153)

fieldValue138.addChildren(ProtoInstance149)
ProtoInstance154 = ProtoInstance()
ProtoInstance154.setName("CameraMovement")
fieldValue155 = fieldValue()
fieldValue155.setName("description")
fieldValue155.setValue("Camera Pause")

ProtoInstance154.addFieldValue(fieldValue155)
fieldValue156 = fieldValue()
fieldValue156.setName("duration")
fieldValue156.setValue("2")

ProtoInstance154.addFieldValue(fieldValue156)
fieldValue157 = fieldValue()
fieldValue157.setName("goalPosition")
fieldValue157.setValue("-30 1 -10")

ProtoInstance154.addFieldValue(fieldValue157)
fieldValue158 = fieldValue()
fieldValue158.setName("goalOrientation")
fieldValue158.setValue("0 1 0 0")

ProtoInstance154.addFieldValue(fieldValue158)

fieldValue138.addChildren(ProtoInstance154)

ProtoInstance134.addFieldValue(fieldValue138)

fieldValue93.addChildren(ProtoInstance134)
ProtoInstance159 = ProtoInstance()
ProtoInstance159.setName("CameraShot")
ProtoInstance159.setDEF("CameraBoom")
fieldValue160 = fieldValue()
fieldValue160.setName("description")
fieldValue160.setValue("Camera Boom")

ProtoInstance159.addFieldValue(fieldValue160)
fieldValue161 = fieldValue()
fieldValue161.setName("initialPosition")
fieldValue161.setValue("-20 1 -10")

ProtoInstance159.addFieldValue(fieldValue161)
fieldValue162 = fieldValue()
fieldValue162.setName("initialOrientation")
fieldValue162.setValue("0 1 0 0")

ProtoInstance159.addFieldValue(fieldValue162)
fieldValue163 = fieldValue()
fieldValue163.setName("moves")
ProtoInstance164 = ProtoInstance()
ProtoInstance164.setName("CameraMovement")
ProtoInstance164.setDEF("CameraBoomUp")
fieldValue165 = fieldValue()
fieldValue165.setName("description")
fieldValue165.setValue("Camera Boom Up")

ProtoInstance164.addFieldValue(fieldValue165)
fieldValue166 = fieldValue()
fieldValue166.setName("duration")
fieldValue166.setValue("3")

ProtoInstance164.addFieldValue(fieldValue166)
fieldValue167 = fieldValue()
fieldValue167.setName("goalPosition")
fieldValue167.setValue("-20 5 -10")

ProtoInstance164.addFieldValue(fieldValue167)
fieldValue168 = fieldValue()
fieldValue168.setName("goalOrientation")
fieldValue168.setValue("0 1 0 0")

ProtoInstance164.addFieldValue(fieldValue168)

fieldValue163.addChildren(ProtoInstance164)
ProtoInstance169 = ProtoInstance()
ProtoInstance169.setName("CameraMovement")
ProtoInstance169.setDEF("BoomDown")
fieldValue170 = fieldValue()
fieldValue170.setName("description")
fieldValue170.setValue("Camera Boom Down")

ProtoInstance169.addFieldValue(fieldValue170)
fieldValue171 = fieldValue()
fieldValue171.setName("duration")
fieldValue171.setValue("3")

ProtoInstance169.addFieldValue(fieldValue171)
fieldValue172 = fieldValue()
fieldValue172.setName("goalPosition")
fieldValue172.setValue("-20 1 -10")

ProtoInstance169.addFieldValue(fieldValue172)
fieldValue173 = fieldValue()
fieldValue173.setName("goalOrientation")
fieldValue173.setValue("0 1 0 0")

ProtoInstance169.addFieldValue(fieldValue173)

fieldValue163.addChildren(ProtoInstance169)
ProtoInstance174 = ProtoInstance()
ProtoInstance174.setName("CameraMovement")
ProtoInstance174.setDEF("BoomPause")
fieldValue175 = fieldValue()
fieldValue175.setName("description")
fieldValue175.setValue("Camera Pause")

ProtoInstance174.addFieldValue(fieldValue175)
fieldValue176 = fieldValue()
fieldValue176.setName("duration")
fieldValue176.setValue("2")

ProtoInstance174.addFieldValue(fieldValue176)
fieldValue177 = fieldValue()
fieldValue177.setName("goalPosition")
fieldValue177.setValue("-20 1 -10")

ProtoInstance174.addFieldValue(fieldValue177)
fieldValue178 = fieldValue()
fieldValue178.setName("goalOrientation")
fieldValue178.setValue("0 1 0 0")

ProtoInstance174.addFieldValue(fieldValue178)

fieldValue163.addChildren(ProtoInstance174)

ProtoInstance159.addFieldValue(fieldValue163)

fieldValue93.addChildren(ProtoInstance159)
ProtoInstance179 = ProtoInstance()
ProtoInstance179.setName("CameraShot")
ProtoInstance179.setDEF("CameraTilt")
fieldValue180 = fieldValue()
fieldValue180.setName("description")
fieldValue180.setValue("Camera Tilt")

ProtoInstance179.addFieldValue(fieldValue180)
fieldValue181 = fieldValue()
fieldValue181.setName("initialPosition")
fieldValue181.setValue("-10 1 -10")

ProtoInstance179.addFieldValue(fieldValue181)
fieldValue182 = fieldValue()
fieldValue182.setName("initialOrientation")
fieldValue182.setValue("0 0 1 0")

ProtoInstance179.addFieldValue(fieldValue182)
fieldValue183 = fieldValue()
fieldValue183.setName("traceEnabled")
fieldValue183.setValue("true")

ProtoInstance179.addFieldValue(fieldValue183)
fieldValue184 = fieldValue()
fieldValue184.setName("moves")
ProtoInstance185 = ProtoInstance()
ProtoInstance185.setName("CameraMovement")
fieldValue186 = fieldValue()
fieldValue186.setName("description")
fieldValue186.setValue("Camera Tilt Pause")

ProtoInstance185.addFieldValue(fieldValue186)
fieldValue187 = fieldValue()
fieldValue187.setName("duration")
fieldValue187.setValue("1")

ProtoInstance185.addFieldValue(fieldValue187)
fieldValue188 = fieldValue()
fieldValue188.setName("goalPosition")
fieldValue188.setValue("-10 1 -10")

ProtoInstance185.addFieldValue(fieldValue188)
fieldValue189 = fieldValue()
fieldValue189.setName("goalOrientation")
fieldValue189.setValue("0 0 1 0")

ProtoInstance185.addFieldValue(fieldValue189)

fieldValue184.addChildren(ProtoInstance185)
ProtoInstance190 = ProtoInstance()
ProtoInstance190.setName("CameraMovement")
ProtoInstance190.setDEF("TiltDown")
fieldValue191 = fieldValue()
fieldValue191.setName("description")
fieldValue191.setValue("Camera Tilt Left")

ProtoInstance190.addFieldValue(fieldValue191)
fieldValue192 = fieldValue()
fieldValue192.setName("duration")
fieldValue192.setValue("3")

ProtoInstance190.addFieldValue(fieldValue192)
fieldValue193 = fieldValue()
fieldValue193.setName("goalPosition")
fieldValue193.setValue("-10 1 -10")

ProtoInstance190.addFieldValue(fieldValue193)
fieldValue194 = fieldValue()
fieldValue194.setName("goalOrientation")
fieldValue194.setValue("0 0 1 0.785")

ProtoInstance190.addFieldValue(fieldValue194)

fieldValue184.addChildren(ProtoInstance190)
ProtoInstance195 = ProtoInstance()
ProtoInstance195.setName("CameraMovement")
ProtoInstance195.setDEF("TiltPause")
fieldValue196 = fieldValue()
fieldValue196.setName("description")
fieldValue196.setValue("Camera Tilt Pause")

ProtoInstance195.addFieldValue(fieldValue196)
fieldValue197 = fieldValue()
fieldValue197.setName("duration")
fieldValue197.setValue("1")

ProtoInstance195.addFieldValue(fieldValue197)
fieldValue198 = fieldValue()
fieldValue198.setName("goalPosition")
fieldValue198.setValue("-10 1 -10")

ProtoInstance195.addFieldValue(fieldValue198)
fieldValue199 = fieldValue()
fieldValue199.setName("goalOrientation")
fieldValue199.setValue("0 0 1 0.785")

ProtoInstance195.addFieldValue(fieldValue199)

fieldValue184.addChildren(ProtoInstance195)
ProtoInstance200 = ProtoInstance()
ProtoInstance200.setName("CameraMovement")
fieldValue201 = fieldValue()
fieldValue201.setName("description")
fieldValue201.setValue("Camera Tilt Right")

ProtoInstance200.addFieldValue(fieldValue201)
fieldValue202 = fieldValue()
fieldValue202.setName("duration")
fieldValue202.setValue("3")

ProtoInstance200.addFieldValue(fieldValue202)
fieldValue203 = fieldValue()
fieldValue203.setName("goalPosition")
fieldValue203.setValue("-10 1 -10")

ProtoInstance200.addFieldValue(fieldValue203)
fieldValue204 = fieldValue()
fieldValue204.setName("goalOrientation")
fieldValue204.setValue("0 0 1 -0.785")

ProtoInstance200.addFieldValue(fieldValue204)

fieldValue184.addChildren(ProtoInstance200)
ProtoInstance205 = ProtoInstance()
ProtoInstance205.setName("CameraMovement")
fieldValue206 = fieldValue()
fieldValue206.setName("description")
fieldValue206.setValue("Camera Tilt Pause")

ProtoInstance205.addFieldValue(fieldValue206)
fieldValue207 = fieldValue()
fieldValue207.setName("duration")
fieldValue207.setValue("1")

ProtoInstance205.addFieldValue(fieldValue207)
fieldValue208 = fieldValue()
fieldValue208.setName("goalPosition")
fieldValue208.setValue("-10 1 -10")

ProtoInstance205.addFieldValue(fieldValue208)
fieldValue209 = fieldValue()
fieldValue209.setName("goalOrientation")
fieldValue209.setValue("0 0 1 -0.785")

ProtoInstance205.addFieldValue(fieldValue209)

fieldValue184.addChildren(ProtoInstance205)
ProtoInstance210 = ProtoInstance()
ProtoInstance210.setName("CameraMovement")
ProtoInstance210.setDEF("TiltReset")
fieldValue211 = fieldValue()
fieldValue211.setName("description")
fieldValue211.setValue("Camera Tilt Reset")

ProtoInstance210.addFieldValue(fieldValue211)
fieldValue212 = fieldValue()
fieldValue212.setName("duration")
fieldValue212.setValue("1")

ProtoInstance210.addFieldValue(fieldValue212)
fieldValue213 = fieldValue()
fieldValue213.setName("goalPosition")
fieldValue213.setValue("-10 1 -10")

ProtoInstance210.addFieldValue(fieldValue213)
fieldValue214 = fieldValue()
fieldValue214.setName("goalOrientation")
fieldValue214.setValue("0 0 1 0")

ProtoInstance210.addFieldValue(fieldValue214)

fieldValue184.addChildren(ProtoInstance210)
ProtoInstance215 = ProtoInstance()
ProtoInstance215.setName("CameraMovement")
ProtoInstance215.setDEF("TiltUp")
fieldValue216 = fieldValue()
fieldValue216.setName("description")
fieldValue216.setValue("Return to home")

ProtoInstance215.addFieldValue(fieldValue216)
fieldValue217 = fieldValue()
fieldValue217.setName("duration")
fieldValue217.setValue("2")

ProtoInstance215.addFieldValue(fieldValue217)
fieldValue218 = fieldValue()
fieldValue218.setName("goalPosition")
fieldValue218.setValue("0 2 12")

ProtoInstance215.addFieldValue(fieldValue218)
fieldValue219 = fieldValue()
fieldValue219.setName("goalOrientation")
fieldValue219.setValue("0 0 1 0")

ProtoInstance215.addFieldValue(fieldValue219)

fieldValue184.addChildren(ProtoInstance215)

ProtoInstance179.addFieldValue(fieldValue184)

fieldValue93.addChildren(ProtoInstance179)

ProtoInstance89.addFieldValue(fieldValue93)

Scene21.addChildren(ProtoInstance89)
Group220 = Group()
Group220.setDEF("AnimationGroup.SimpleShots")
TimeSensor221 = TimeSensor()
TimeSensor221.setDEF("CameraTimer.SimpleShots")

Group220.addChildren(TimeSensor221)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE222 = ROUTE()
ROUTE222.setFromField("totalDuration")
ROUTE222.setFromNode("Camera.SimpleShotsTest")
ROUTE222.setToField("cycleInterval")
ROUTE222.setToNode("CameraTimer.SimpleShots")

Group220.addChildren(ROUTE222)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE223 = ROUTE()
ROUTE223.setFromField("fraction_changed")
ROUTE223.setFromNode("CameraTimer.SimpleShots")
ROUTE223.setToField("set_fraction")
ROUTE223.setToNode("Camera.SimpleShotsTest")

Group220.addChildren(ROUTE223)
Transform224 = Transform()
Transform224.setDEF("Trigger.SimpleShots")
Transform224.setTranslation([-4,4,0])
BooleanFilter225 = BooleanFilter()
BooleanFilter225.setDEF("TextTouchActive.SimpleShotsFilter")

Transform224.addChildren(BooleanFilter225)
TouchSensor226 = TouchSensor()
TouchSensor226.setDEF("TextTouch.SimpleShots")
TouchSensor226.setDescription("touch to animate Camera SimpleShotsTest")

Transform224.addChildren(TouchSensor226)
ROUTE227 = ROUTE()
ROUTE227.setFromField("inputTrue")
ROUTE227.setFromNode("TextTouchActive.SimpleShotsFilter")
ROUTE227.setToField("set_bind")
ROUTE227.setToNode("Camera.SimpleShotsTest")

Transform224.addChildren(ROUTE227)
ROUTE228 = ROUTE()
ROUTE228.setFromField("isActive")
ROUTE228.setFromNode("TextTouch.SimpleShots")
ROUTE228.setToField("set_boolean")
ROUTE228.setToNode("TextTouchActive.SimpleShotsFilter")

Transform224.addChildren(ROUTE228)
ROUTE229 = ROUTE()
ROUTE229.setFromField("touchTime")
ROUTE229.setFromNode("TextTouch.SimpleShots")
ROUTE229.setToField("startTime")
ROUTE229.setToNode("CameraTimer.SimpleShots")

Transform224.addChildren(ROUTE229)
Shape230 = Shape()
Text231 = Text()
Text231.setString(["Click to animate","SimpleShotsTest"])
FontStyle232 = FontStyle()
FontStyle232.setJustify(["MIDDLE","MIDDLE"])

Text231.setFontStyle(FontStyle232)

Shape230.setGeometry(Text231)
Appearance233 = Appearance()
Material234 = Material()
Material234.setDEF("ArtDeco5")
Material234.setAmbientIntensity(0.24)
Material234.setDiffuseColor([0.945455,0.318988,0.321717])
Material234.setShininess(0.01)
Material234.setSpecularColor([0.072727,0.021705,0.010732])
#Universal Media Library: ArtDeco 5

Appearance233.setMaterial(Material234)

Shape230.setAppearance(Appearance233)

Transform224.addChildren(Shape230)
#Simplify intersection test for user selecting text
Shape235 = Shape()
Shape235.setDEF("TransparentBox")
Appearance236 = Appearance()
Material237 = Material()
Material237.setTransparency(1)

Appearance236.setMaterial(Material237)

Shape235.setAppearance(Appearance236)
Box238 = Box()
Box238.setSize([6,2,0.0001])

Shape235.setGeometry(Box238)

Transform224.addChildren(Shape235)

Group220.addChildren(Transform224)

Scene21.addChildren(Group220)
Group239 = Group()
Group239.setDEF("SimpleShotsTargets")
Transform240 = Transform()
Transform240.setDEF("TargetBoxZoom")
Transform240.setTranslation([-50,1,-20])
Shape241 = Shape()
Box242 = Box()

Shape241.setGeometry(Box242)
Appearance243 = Appearance()
Material244 = Material()

Appearance243.setMaterial(Material244)
ImageTexture245 = ImageTexture()
ImageTexture245.setUrl(["images/CameraMoveZoom.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveZoom.png"])

Appearance243.setTexture(ImageTexture245)

Shape241.setAppearance(Appearance243)

Transform240.addChildren(Shape241)
Transform246 = Transform()
Transform246.setTranslation([0,2,0])
Shape247 = Shape()
Text248 = Text()
Text248.setString(["Zoom in, out"])
FontStyle249 = FontStyle()
FontStyle249.setJustify(["MIDDLE","MIDDLE"])

Text248.setFontStyle(FontStyle249)

Shape247.setGeometry(Text248)
Appearance250 = Appearance()
Material251 = Material()

Appearance250.setMaterial(Material251)

Shape247.setAppearance(Appearance250)

Transform246.addChildren(Shape247)

Transform240.addChildren(Transform246)

Group239.addChildren(Transform240)
Transform252 = Transform()
Transform252.setDEF("TargetBoxDolly")
Transform252.setTranslation([-40,1,-20])
Shape253 = Shape()
Box254 = Box()

Shape253.setGeometry(Box254)
Appearance255 = Appearance()
Material256 = Material()

Appearance255.setMaterial(Material256)
ImageTexture257 = ImageTexture()
ImageTexture257.setUrl(["images/CameraMoveDolly.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveDolly.png"])

Appearance255.setTexture(ImageTexture257)

Shape253.setAppearance(Appearance255)

Transform252.addChildren(Shape253)
Transform258 = Transform()
Transform258.setTranslation([0,2,0])
Shape259 = Shape()
Text260 = Text()
Text260.setString(["Dolly left, right"])
FontStyle261 = FontStyle()
FontStyle261.setJustify(["MIDDLE","MIDDLE"])

Text260.setFontStyle(FontStyle261)

Shape259.setGeometry(Text260)
Appearance262 = Appearance()
Material263 = Material()

Appearance262.setMaterial(Material263)

Shape259.setAppearance(Appearance262)

Transform258.addChildren(Shape259)

Transform252.addChildren(Transform258)

Group239.addChildren(Transform252)
Transform264 = Transform()
Transform264.setDEF("TargetBoxPan")
Transform264.setTranslation([-30,1,-20])
Shape265 = Shape()
Box266 = Box()

Shape265.setGeometry(Box266)
Appearance267 = Appearance()
Material268 = Material()

Appearance267.setMaterial(Material268)
ImageTexture269 = ImageTexture()
ImageTexture269.setUrl(["images/CameraMovePan.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMovePan.png"])

Appearance267.setTexture(ImageTexture269)

Shape265.setAppearance(Appearance267)

Transform264.addChildren(Shape265)
Transform270 = Transform()
Transform270.setTranslation([0,2,0])
Shape271 = Shape()
Text272 = Text()
Text272.setString(["Pan left, right"])
FontStyle273 = FontStyle()
FontStyle273.setJustify(["MIDDLE","MIDDLE"])

Text272.setFontStyle(FontStyle273)

Shape271.setGeometry(Text272)
Appearance274 = Appearance()
Material275 = Material()

Appearance274.setMaterial(Material275)

Shape271.setAppearance(Appearance274)

Transform270.addChildren(Shape271)

Transform264.addChildren(Transform270)

Group239.addChildren(Transform264)
Transform276 = Transform()
Transform276.setDEF("TargetBoxBoom")
Transform276.setTranslation([-20,1,-20])
Shape277 = Shape()
Box278 = Box()

Shape277.setGeometry(Box278)
Appearance279 = Appearance()
Material280 = Material()

Appearance279.setMaterial(Material280)
ImageTexture281 = ImageTexture()
ImageTexture281.setUrl(["images/CameraMoveBoom.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveBoom.png"])

Appearance279.setTexture(ImageTexture281)

Shape277.setAppearance(Appearance279)

Transform276.addChildren(Shape277)
Transform282 = Transform()
Transform282.setTranslation([0,2,0])
Shape283 = Shape()
Text284 = Text()
Text284.setString(["Boom up, down"])
FontStyle285 = FontStyle()
FontStyle285.setJustify(["MIDDLE","MIDDLE"])

Text284.setFontStyle(FontStyle285)

Shape283.setGeometry(Text284)
Appearance286 = Appearance()
Material287 = Material()

Appearance286.setMaterial(Material287)

Shape283.setAppearance(Appearance286)

Transform282.addChildren(Shape283)

Transform276.addChildren(Transform282)

Group239.addChildren(Transform276)
Transform288 = Transform()
Transform288.setDEF("TargetBoxTilt")
Transform288.setTranslation([-10,1,-20])
Shape289 = Shape()
Box290 = Box()

Shape289.setGeometry(Box290)
Appearance291 = Appearance()
Material292 = Material()

Appearance291.setMaterial(Material292)
ImageTexture293 = ImageTexture()
ImageTexture293.setUrl(["images/CameraMoveTilt.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveTilt.png"])

Appearance291.setTexture(ImageTexture293)

Shape289.setAppearance(Appearance291)

Transform288.addChildren(Shape289)
Transform294 = Transform()
Transform294.setTranslation([0,2,0])
Shape295 = Shape()
Text296 = Text()
Text296.setString(["Tilt left, right"])
FontStyle297 = FontStyle()
FontStyle297.setJustify(["MIDDLE","MIDDLE"])

Text296.setFontStyle(FontStyle297)

Shape295.setGeometry(Text296)
Appearance298 = Appearance()
Material299 = Material()

Appearance298.setMaterial(Material299)

Shape295.setAppearance(Appearance298)

Transform294.addChildren(Shape295)

Transform288.addChildren(Transform294)

Group239.addChildren(Transform288)

Scene21.addChildren(Group239)
#=============== Camera.AimPointTest ==============
ProtoInstance300 = ProtoInstance()
ProtoInstance300.setName("Camera")
ProtoInstance300.setDEF("Camera.AimPointTest")
fieldValue301 = fieldValue()
fieldValue301.setName("description")
fieldValue301.setValue("AimPointTest for moving camera tracking moving target")

ProtoInstance300.addFieldValue(fieldValue301)
fieldValue302 = fieldValue()
fieldValue302.setName("position")
fieldValue302.setValue("4 4 10")

ProtoInstance300.addFieldValue(fieldValue302)
fieldValue303 = fieldValue()
fieldValue303.setName("shots")
ProtoInstance304 = ProtoInstance()
ProtoInstance304.setName("CameraShot")
ProtoInstance304.setDEF("Shot5")
fieldValue305 = fieldValue()
fieldValue305.setName("description")
fieldValue305.setValue("#3 Tracking shot")

ProtoInstance304.addFieldValue(fieldValue305)
fieldValue306 = fieldValue()
fieldValue306.setName("initialPosition")
fieldValue306.setValue("6 6 10")

ProtoInstance304.addFieldValue(fieldValue306)
fieldValue307 = fieldValue()
fieldValue307.setName("initialOrientation")
fieldValue307.setValue("0 1 0 0")

ProtoInstance304.addFieldValue(fieldValue307)
fieldValue308 = fieldValue()
fieldValue308.setName("moves")
ProtoInstance309 = ProtoInstance()
ProtoInstance309.setName("CameraMovement")
ProtoInstance309.setDEF("MoveAimPoint3.1")
fieldValue310 = fieldValue()
fieldValue310.setName("description")
fieldValue310.setValue("AimPoint 3.1 moving BoxPath")

ProtoInstance309.addFieldValue(fieldValue310)
fieldValue311 = fieldValue()
fieldValue311.setName("tracking")
fieldValue311.setValue("true")

ProtoInstance309.addFieldValue(fieldValue311)
fieldValue312 = fieldValue()
fieldValue312.setName("duration")
fieldValue312.setValue("8")

ProtoInstance309.addFieldValue(fieldValue312)
fieldValue313 = fieldValue()
fieldValue313.setName("goalPosition")
fieldValue313.setValue("6 6 10")

ProtoInstance309.addFieldValue(fieldValue313)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.addChildren(ProtoInstance309)
ProtoInstance314 = ProtoInstance()
ProtoInstance314.setName("CameraMovement")
ProtoInstance314.setDEF("MoveAimPoint3.2")
fieldValue315 = fieldValue()
fieldValue315.setName("description")
fieldValue315.setValue("AimPoint 3.2 pan right while tracking")

ProtoInstance314.addFieldValue(fieldValue315)
fieldValue316 = fieldValue()
fieldValue316.setName("tracking")
fieldValue316.setValue("true")

ProtoInstance314.addFieldValue(fieldValue316)
fieldValue317 = fieldValue()
fieldValue317.setName("duration")
fieldValue317.setValue("8")

ProtoInstance314.addFieldValue(fieldValue317)
fieldValue318 = fieldValue()
fieldValue318.setName("goalPosition")
fieldValue318.setValue("40 6 12")

ProtoInstance314.addFieldValue(fieldValue318)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.addChildren(ProtoInstance314)
ProtoInstance319 = ProtoInstance()
ProtoInstance319.setName("CameraMovement")
ProtoInstance319.setDEF("MoveAimPoint3.3")
fieldValue320 = fieldValue()
fieldValue320.setName("description")
fieldValue320.setValue("AimPoint 3.3 boom up while tracking")

ProtoInstance319.addFieldValue(fieldValue320)
fieldValue321 = fieldValue()
fieldValue321.setName("tracking")
fieldValue321.setValue("true")

ProtoInstance319.addFieldValue(fieldValue321)
fieldValue322 = fieldValue()
fieldValue322.setName("duration")
fieldValue322.setValue("3")

ProtoInstance319.addFieldValue(fieldValue322)
fieldValue323 = fieldValue()
fieldValue323.setName("goalPosition")
fieldValue323.setValue("40 20 13")

ProtoInstance319.addFieldValue(fieldValue323)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.addChildren(ProtoInstance319)
ProtoInstance324 = ProtoInstance()
ProtoInstance324.setName("CameraMovement")
ProtoInstance324.setDEF("MoveAimPoint3.4")
fieldValue325 = fieldValue()
fieldValue325.setName("description")
fieldValue325.setValue("AimPoint 3.4 restore camera back to home")

ProtoInstance324.addFieldValue(fieldValue325)
fieldValue326 = fieldValue()
fieldValue326.setName("tracking")
fieldValue326.setValue("true")

ProtoInstance324.addFieldValue(fieldValue326)
fieldValue327 = fieldValue()
fieldValue327.setName("duration")
fieldValue327.setValue("5")

ProtoInstance324.addFieldValue(fieldValue327)
fieldValue328 = fieldValue()
fieldValue328.setName("goalPosition")
fieldValue328.setValue("4 4 10")

ProtoInstance324.addFieldValue(fieldValue328)
fieldValue329 = fieldValue()
fieldValue329.setName("goalAimPoint")
fieldValue329.setValue("4 4 0")

ProtoInstance324.addFieldValue(fieldValue329)
fieldValue330 = fieldValue()
fieldValue330.setName("goalOrientation")
fieldValue330.setValue("0 1 0 0")

ProtoInstance324.addFieldValue(fieldValue330)
#can test tracking or not using these values

fieldValue308.addChildren(ProtoInstance324)

ProtoInstance304.addFieldValue(fieldValue308)

fieldValue303.addChildren(ProtoInstance304)

ProtoInstance300.addFieldValue(fieldValue303)

Scene21.addChildren(ProtoInstance300)
Group331 = Group()
Group331.setDEF("AnimationGroup.AimPointTest")
TimeSensor332 = TimeSensor()
TimeSensor332.setDEF("CameraTimer.AimPointTest")

Group331.addChildren(TimeSensor332)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE333 = ROUTE()
ROUTE333.setFromField("totalDuration")
ROUTE333.setFromNode("Camera.AimPointTest")
ROUTE333.setToField("cycleInterval")
ROUTE333.setToNode("CameraTimer.AimPointTest")

Group331.addChildren(ROUTE333)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE334 = ROUTE()
ROUTE334.setFromField("fraction_changed")
ROUTE334.setFromNode("CameraTimer.AimPointTest")
ROUTE334.setToField("set_fraction")
ROUTE334.setToNode("Camera.AimPointTest")

Group331.addChildren(ROUTE334)
Transform335 = Transform()
Transform335.setDEF("Trigger.AimPointTest")
Transform335.setTranslation([4,4,0])
BooleanFilter336 = BooleanFilter()
BooleanFilter336.setDEF("TextTouchActive.AimPointFilter")

Transform335.addChildren(BooleanFilter336)
TouchSensor337 = TouchSensor()
TouchSensor337.setDEF("TextTouch.AimPointTest")
TouchSensor337.setDescription("touch to animate Camera AimPointTest")

Transform335.addChildren(TouchSensor337)
ROUTE338 = ROUTE()
ROUTE338.setFromField("inputTrue")
ROUTE338.setFromNode("TextTouchActive.AimPointFilter")
ROUTE338.setToField("set_bind")
ROUTE338.setToNode("Camera.AimPointTest")

Transform335.addChildren(ROUTE338)
ROUTE339 = ROUTE()
ROUTE339.setFromField("isActive")
ROUTE339.setFromNode("TextTouch.AimPointTest")
ROUTE339.setToField("set_boolean")
ROUTE339.setToNode("TextTouchActive.AimPointFilter")

Transform335.addChildren(ROUTE339)
ROUTE340 = ROUTE()
ROUTE340.setFromField("touchTime")
ROUTE340.setFromNode("TextTouch.AimPointTest")
ROUTE340.setToField("startTime")
ROUTE340.setToNode("CameraTimer.AimPointTest")

Transform335.addChildren(ROUTE340)
Shape341 = Shape()
Text342 = Text()
Text342.setString(["Click to animate","AimPointTest"])
FontStyle343 = FontStyle()
FontStyle343.setJustify(["MIDDLE","MIDDLE"])

Text342.setFontStyle(FontStyle343)

Shape341.setGeometry(Text342)
Appearance344 = Appearance()
Material345 = Material()
Material345.setUSE("ArtDeco5")

Appearance344.setMaterial(Material345)

Shape341.setAppearance(Appearance344)

Transform335.addChildren(Shape341)
Shape346 = Shape()
Shape346.setUSE("TransparentBox")

Transform335.addChildren(Shape346)

Group331.addChildren(Transform335)

Scene21.addChildren(Group331)
#TODO build a test once implemented
ProtoInstance347 = ProtoInstance()
ProtoInstance347.setName("OfflineRender")

Scene21.addChildren(ProtoInstance347)
#=============== animate a camera shape to visualize view changes ==============
Transform348 = Transform()
Transform348.setDEF("CameraShapeTransform")
Transform348.setTranslation([0,0.5,0])
#move CameraShape using active Camera
ROUTE349 = ROUTE()
ROUTE349.setFromField("position_changed")
ROUTE349.setFromNode("Camera.SimpleShotsTest")
ROUTE349.setToField("translation")
ROUTE349.setToNode("CameraShapeTransform")

Transform348.addChildren(ROUTE349)
ROUTE350 = ROUTE()
ROUTE350.setFromField("orientation_changed")
ROUTE350.setFromNode("Camera.SimpleShotsTest")
ROUTE350.setToField("rotation")
ROUTE350.setToNode("CameraShapeTransform")

Transform348.addChildren(ROUTE350)
ROUTE351 = ROUTE()
ROUTE351.setFromField("position")
ROUTE351.setFromNode("Camera.AimPointTest")
ROUTE351.setToField("translation")
ROUTE351.setToNode("CameraShapeTransform")

Transform348.addChildren(ROUTE351)
ROUTE352 = ROUTE()
ROUTE352.setFromField("orientation_changed")
ROUTE352.setFromNode("Camera.AimPointTest")
ROUTE352.setToField("rotation")
ROUTE352.setToNode("CameraShapeTransform")

Transform348.addChildren(ROUTE352)
Transform353 = Transform()
Transform353.setDEF("CameraOffsetTransform")
Transform353.setTranslation([0,0,0.25])
TouchSensor354 = TouchSensor()
TouchSensor354.setDEF("CameraShapeTouched")

Transform353.addChildren(TouchSensor354)
Inline355 = Inline()
Inline355.setDEF("CameraShape")
Inline355.setUrl(["CameraShape.x3d","https://www.web3d.org/x3d/content/examples/Basic/development/CameraShape.x3d"])

Transform353.addChildren(Inline355)
Shape356 = Shape()
Shape356.setDEF("SightLine")
IndexedLineSet357 = IndexedLineSet()
IndexedLineSet357.setCoordIndex([0,1])
Coordinate358 = Coordinate()
Coordinate358.setPoint([0,0,0,0,0,-100])

IndexedLineSet357.setCoord(Coordinate358)

Shape356.setGeometry(IndexedLineSet357)
Appearance359 = Appearance()
Material360 = Material()
Material360.setEmissiveColor([0.8,0.8,0.4])

Appearance359.setMaterial(Material360)

Shape356.setAppearance(Appearance359)

Transform353.addChildren(Shape356)

Transform348.addChildren(Transform353)
#Display frustum to show camera view within the scene, toggled by user selecting CameraShape
ExternProtoDeclare361 = ExternProtoDeclare()
ExternProtoDeclare361.setName("ViewFrustum")
ExternProtoDeclare361.setAppinfo("Display view frustum associated with a given pair of Viewpoint NavigationInfo nodes")
ExternProtoDeclare361.setUrl(["../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum"])
field362 = field()
field362.setName("ViewpointNode")
field362.setAccessType("initializeOnly")
field362.setAppinfo("required: insert Viewpoint DEF or USE node for view of interest")
field362.setType("SFNode")

ExternProtoDeclare361.addField(field362)
field363 = field()
field363.setName("NavigationInfoNode")
field363.setAccessType("initializeOnly")
field363.setAppinfo("required: insert NavigationInfo DEF or USE node of interest")
field363.setType("SFNode")

ExternProtoDeclare361.addField(field363)
field364 = field()
field364.setName("visible")
field364.setAccessType("inputOutput")
field364.setAppinfo("whether or not frustum geometry is rendered")
field364.setType("SFBool")

ExternProtoDeclare361.addField(field364)
field365 = field()
field365.setName("lineColor")
field365.setAccessType("inputOutput")
field365.setAppinfo("RGB color of ViewFrustum outline, default value 0.9 0.9 0.9")
field365.setType("SFColor")

ExternProtoDeclare361.addField(field365)
field366 = field()
field366.setName("frustumColor")
field366.setAccessType("inputOutput")
field366.setAppinfo("RGB color of ViewFrustum hull geometry, default value 0.8 0.8 0.8")
field366.setType("SFColor")

ExternProtoDeclare361.addField(field366)
field367 = field()
field367.setName("transparency")
field367.setAccessType("inputOutput")
field367.setAppinfo("transparency of ViewFrustum hull geometry, default value 0.5")
field367.setType("SFFloat")

ExternProtoDeclare361.addField(field367)
field368 = field()
field368.setName("aspectRatio")
field368.setAccessType("inputOutput")
field368.setAppinfo("assumed ratio height/width, default value 0.75")
field368.setType("SFFloat")

ExternProtoDeclare361.addField(field368)
field369 = field()
field369.setName("trace")
field369.setAccessType("initializeOnly")
field369.setAppinfo("debug support, default false")
field369.setType("SFBool")

ExternProtoDeclare361.addField(field369)

Transform348.addChildren(ExternProtoDeclare361)
ProtoInstance370 = ProtoInstance()
ProtoInstance370.setName("ViewFrustum")
ProtoInstance370.setDEF("ViewFrustumNode")
fieldValue371 = fieldValue()
fieldValue371.setName("ViewpointNode")
Viewpoint372 = Viewpoint()
Viewpoint372.setDEF("FrustumViewpoint")
Viewpoint372.setDescription("viewpoint for ViewFrustum")
Viewpoint372.setPosition([0,0,0])

fieldValue371.addChildren(Viewpoint372)

ProtoInstance370.addFieldValue(fieldValue371)
fieldValue373 = fieldValue()
fieldValue373.setName("NavigationInfoNode")
NavigationInfo374 = NavigationInfo()
NavigationInfo374.setDEF("TestNavigationInfo")
NavigationInfo374.setTransitionType(["ANIMATE"])
NavigationInfo374.setVisibilityLimit(100)

fieldValue373.addChildren(NavigationInfo374)

ProtoInstance370.addFieldValue(fieldValue373)
fieldValue375 = fieldValue()
fieldValue375.setName("visible")
fieldValue375.setValue("false")

ProtoInstance370.addFieldValue(fieldValue375)
fieldValue376 = fieldValue()
fieldValue376.setName("lineColor")
fieldValue376.setValue("0.9 0.9 0.9")

ProtoInstance370.addFieldValue(fieldValue376)
fieldValue377 = fieldValue()
fieldValue377.setName("frustumColor")
fieldValue377.setValue("0.8 0.8 0.8")

ProtoInstance370.addFieldValue(fieldValue377)
fieldValue378 = fieldValue()
fieldValue378.setName("transparency")
fieldValue378.setValue("0.95")

ProtoInstance370.addFieldValue(fieldValue378)

Transform348.addChildren(ProtoInstance370)
BooleanToggle379 = BooleanToggle()
BooleanToggle379.setDEF("ViewFrustumToggle")

Transform348.addChildren(BooleanToggle379)
ROUTE380 = ROUTE()
ROUTE380.setFromField("isActive")
ROUTE380.setFromNode("CameraShapeTouched")
ROUTE380.setToField("set_boolean")
ROUTE380.setToNode("ViewFrustumToggle")

Transform348.addChildren(ROUTE380)
ROUTE381 = ROUTE()
ROUTE381.setFromField("toggle")
ROUTE381.setFromNode("ViewFrustumToggle")
ROUTE381.setToField("set_visible")
ROUTE381.setToNode("ViewFrustumNode")

Transform348.addChildren(ROUTE381)

Scene21.addChildren(Transform348)
#=============== add checkerboard, axes and other things to look at while animating ==============
Background382 = Background()
Background382.setSkyColor([0.282353,0.380392,0.470588])

Scene21.addChildren(Background382)
Transform383 = Transform()
Transform383.setRotation([1,0,0,-1.57079])
Transform383.setScale([10,10,10])
Shape384 = Shape()
Appearance385 = Appearance()
Material386 = Material()
Material386.setAmbientIntensity(0.01)
Material386.setDiffuseColor([1,1,1])
Material386.setShininess(0.05)

Appearance385.setMaterial(Material386)

Shape384.setAppearance(Appearance385)
IndexedFaceSet387 = IndexedFaceSet()
IndexedFaceSet387.setColorIndex([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0])
IndexedFaceSet387.setColorPerVertex(False)
IndexedFaceSet387.setCoordIndex([0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1])
IndexedFaceSet387.setNormalPerVertex(False)
IndexedFaceSet387.setSolid(False)
Coordinate388 = Coordinate()
Coordinate388.setPoint([-5.25,5.25,0,-3.75,5.25,0,-2.25,5.25,0,-0.75,5.25,0,0.75,5.25,0,2.25,5.25,0,3.75,5.25,0,5.25,5.25,0,-5.25,3.75,0,-3.75,3.75,0,-2.25,3.75,0,-0.75,3.75,0,0.75,3.75,0,2.25,3.75,0,3.75,3.75,0,5.25,3.75,0,-5.25,2.25,0,-3.75,2.25,0,-2.25,2.25,0,-0.75,2.25,0,0.75,2.25,0,2.25,2.25,0,3.75,2.25,0,5.25,2.25,0,-5.25,0.75,0,-3.75,0.75,0,-2.25,0.75,0,-0.75,0.75,0,0.75,0.75,0,2.25,0.75,0,3.75,0.75,0,5.25,0.75,0,-5.25,-0.75,0,-3.75,-0.75,0,-2.25,-0.75,0,-0.75,-0.75,0,0.75,-0.75,0,2.25,-0.75,0,3.75,-0.75,0,5.25,-0.75,0,-5.25,-2.25,0,-3.75,-2.25,0,-2.25,-2.25,0,-0.75,-2.25,0,0.75,-2.25,0,2.25,-2.25,0,3.75,-2.25,0,5.25,-2.25,0,-5.25,-3.75,0,-3.75,-3.75,0,-2.25,-3.75,0,-0.75,-3.75,0,0.75,-3.75,0,2.25,-3.75,0,3.75,-3.75,0,5.25,-3.75,0,-5.25,-5.25,0,-3.75,-5.25,0,-2.25,-5.25,0,-0.75,-5.25,0,0.75,-5.25,0,2.25,-5.25,0,3.75,-5.25,0,5.25,-5.25,0])

IndexedFaceSet387.setCoord(Coordinate388)
Color389 = Color()
Color389.setColor([0.435294,0.741176,0,0,0.560784,0.580392])

IndexedFaceSet387.setColor(Color389)

Shape384.setGeometry(IndexedFaceSet387)

Transform383.addChildren(Shape384)

Scene21.addChildren(Transform383)
Transform390 = Transform()
Transform390.setScale([3,3,3])
Transform390.setTranslation([0,0.25,0])
Inline391 = Inline()
Inline391.setDEF("CoordinateAxes")
Inline391.setUrl(["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../Savage/Tools/Authoring/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../Savage/Tools/Authoring/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"])

Transform390.addChildren(Inline391)

Scene21.addChildren(Transform390)
Transform392 = Transform()
Transform392.setDEF("MovingBoxTransform")
PositionInterpolator393 = PositionInterpolator()
PositionInterpolator393.setDEF("BoxPath")
PositionInterpolator393.setKey([0,0.25,0.5,0.75,1])
PositionInterpolator393.setKeyValue([-5,1,5,45,1,5,45,1,-45,-5,1,-45,-5,1,5])

Transform392.addChildren(PositionInterpolator393)
TimeSensor394 = TimeSensor()
TimeSensor394.setDEF("BoxTimer")
TimeSensor394.setCycleInterval(10)
TimeSensor394.setLoop(True)

Transform392.addChildren(TimeSensor394)
ROUTE395 = ROUTE()
ROUTE395.setFromField("value_changed")
ROUTE395.setFromNode("BoxPath")
ROUTE395.setToField("translation")
ROUTE395.setToNode("MovingBoxTransform")

Transform392.addChildren(ROUTE395)
ROUTE396 = ROUTE()
ROUTE396.setFromField("value_changed")
ROUTE396.setFromNode("BoxPath")
ROUTE396.setToField("goalAimPoint")
ROUTE396.setToNode("MoveAimPoint3.1")

Transform392.addChildren(ROUTE396)
ROUTE397 = ROUTE()
ROUTE397.setFromField("value_changed")
ROUTE397.setFromNode("BoxPath")
ROUTE397.setToField("goalAimPoint")
ROUTE397.setToNode("MoveAimPoint3.2")

Transform392.addChildren(ROUTE397)
ROUTE398 = ROUTE()
ROUTE398.setFromField("value_changed")
ROUTE398.setFromNode("BoxPath")
ROUTE398.setToField("goalAimPoint")
ROUTE398.setToNode("MoveAimPoint3.3")

Transform392.addChildren(ROUTE398)
ROUTE399 = ROUTE()
ROUTE399.setFromField("fraction_changed")
ROUTE399.setFromNode("BoxTimer")
ROUTE399.setToField("set_fraction")
ROUTE399.setToNode("BoxPath")

Transform392.addChildren(ROUTE399)
Shape400 = Shape()
Box401 = Box()

Shape400.setGeometry(Box401)
Appearance402 = Appearance()
Material403 = Material()

Appearance402.setMaterial(Material403)
ImageTexture404 = ImageTexture()
ImageTexture404.setUrl(["../earth-topo.png","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.png"])

Appearance402.setTexture(ImageTexture404)

Shape400.setAppearance(Appearance402)

Transform392.addChildren(Shape400)

Scene21.addChildren(Transform392)
#================ CrossHair visualization for center of screen ================
ExternProtoDeclare405 = ExternProtoDeclare()
ExternProtoDeclare405.setName("CrossHair")
ExternProtoDeclare405.setAppinfo("CrossHair prototype provides a heads-up display (HUD) crosshair at the view center, which is useful for assessing NavigationInfo lookAt point")
ExternProtoDeclare405.setUrl(["../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair"])
field406 = field()
field406.setName("enabled")
field406.setAccessType("initializeOnly")
field406.setAppinfo("whether CrissHair orititype is enabled or not")
field406.setType("SFBool")

ExternProtoDeclare405.addField(field406)
field407 = field()
field407.setName("set_enabled")
field407.setAccessType("inputOnly")
field407.setAppinfo("control whether enabled/disabled")
field407.setType("SFBool")

ExternProtoDeclare405.addField(field407)
field408 = field()
field408.setName("markerColor")
field408.setAccessType("inputOutput")
field408.setAppinfo("color of CrossHair marker")
field408.setType("SFColor")

ExternProtoDeclare405.addField(field408)
field409 = field()
field409.setName("scale")
field409.setAccessType("inputOutput")
field409.setAppinfo("size of CrossHair in meters")
field409.setType("SFVec3f")

ExternProtoDeclare405.addField(field409)
field410 = field()
field410.setName("positionOffsetFromCamera")
field410.setAccessType("inputOutput")
field410.setAppinfo("distance in front of HUD viewpoint")
field410.setType("SFVec3f")

ExternProtoDeclare405.addField(field410)

Scene21.addChildren(ExternProtoDeclare405)
ProtoInstance411 = ProtoInstance()
ProtoInstance411.setName("CrossHair")
ProtoInstance411.setDEF("CrossHairInstance")
fieldValue412 = fieldValue()
fieldValue412.setName("enabled")
fieldValue412.setValue("true")

ProtoInstance411.addFieldValue(fieldValue412)
fieldValue413 = fieldValue()
fieldValue413.setName("markerColor")
fieldValue413.setValue("1 0.5 0")

ProtoInstance411.addFieldValue(fieldValue413)
fieldValue414 = fieldValue()
fieldValue414.setName("scale")
fieldValue414.setValue("1 1 1")

ProtoInstance411.addFieldValue(fieldValue414)
fieldValue415 = fieldValue()
fieldValue415.setName("positionOffsetFromCamera")
fieldValue415.setValue("0 0 -6")

ProtoInstance411.addFieldValue(fieldValue415)

Scene21.addChildren(ProtoInstance411)
#turn on CrossHairInstance when animated camera viewpoints are bound
ROUTE416 = ROUTE()
ROUTE416.setFromField("isBound")
ROUTE416.setFromNode("Camera.SimpleShotsTest")
ROUTE416.setToField("set_enabled")
ROUTE416.setToNode("CrossHairInstance")

Scene21.addChildren(ROUTE416)
ROUTE417 = ROUTE()
ROUTE417.setFromField("isBound")
ROUTE417.setFromNode("Camera.AimPointTest")
ROUTE417.setToField("set_enabled")
ROUTE417.setToNode("CrossHairInstance")

Scene21.addChildren(ROUTE417)
#turn off CrossHairInstance when animated camera viewpoints are unbound <BooleanFilter DEF='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.SimpleShotsTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.AimPointTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='inputNegate' fromNode='NegateCrossHair' toField='set_enabled' toNode='CrossHairInstance'/>
#=============== TODO Launch Prototype Example ==============
Anchor418 = Anchor()
Anchor418.setDescription("launch CameraExample scene")
Anchor418.setParameter(["target=_blank"])
Anchor418.setUrl(["CameraExample.x3d","https://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.x3d","CameraExample.wrl","https://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.wrl"])
Transform419 = Transform()
Transform419.setTranslation([0,-3,0])
Shape420 = Shape()
Text421 = Text()
Text421.setString(["CameraPrototype","defines a prototype","","Click on this text to see","CameraExample scene"])
FontStyle422 = FontStyle()
FontStyle422.setJustify(["MIDDLE","MIDDLE"])
FontStyle422.setSize(0.5)

Text421.setFontStyle(FontStyle422)

Shape420.setGeometry(Text421)
Appearance423 = Appearance()
Material424 = Material()
Material424.setDiffuseColor([1,1,0.2])

Appearance423.setMaterial(Material424)

Shape420.setAppearance(Appearance423)

Transform419.addChildren(Shape420)

Anchor418.addChildren(Transform419)

Scene21.addChildren(Anchor418)

X3D0.setScene(Scene21)
X3D0.toFileX3D("././CameraExamples_RoundTrip.x3d")
