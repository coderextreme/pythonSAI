import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setName("title")
meta2.setContent("CameraExamples.x3d")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setName("description")
meta3.setContent("Camera, CameraShot and CameraMove examples that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setName("documentation")
meta4.setContent("Two demos are found in the scene, click the \"red text\" on left or right to start. (a) SimpleShotsTest shows Zoom in/out, Pan left/right, Boom up/down, Tilt left/right, with each is defined by a CameraShot collecting a series of CameraMovements. (b) AimPointTest gradually slews the camera view to look at the sliding cube, then follows it around before returning to original viewpoint.")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setName("creator")
meta5.setContent("Don Brutzman and Jeff Weekley")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setName("created")
meta6.setContent("18 June 2009")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setName("modified")
meta7.setContent("12 January 2014")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setName("TODO")
meta8.setContent("Schematron rules, backed up by initialize() checks")

head1.addMeta(meta8)
meta9 = x3d.meta()
meta9.setName("reference")
meta9.setContent("BeyondViewpointCameraNodesWeb3D2009.pdf")

head1.addMeta(meta9)
meta10 = x3d.meta()
meta10.setName("MovingImage")
meta10.setContent("CameraExamplesDemo.mp4")

head1.addMeta(meta10)
meta11 = x3d.meta()
meta11.setName("reference")
meta11.setContent("http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html")

head1.addMeta(meta11)
meta12 = x3d.meta()
meta12.setName("subject")
meta12.setContent("Camera nodes for Viewpoint navigation control")

head1.addMeta(meta12)
meta13 = x3d.meta()
meta13.setName("reference")
meta13.setContent("CameraPrototypes.x3d")

head1.addMeta(meta13)
meta14 = x3d.meta()
meta14.setName("reference")
meta14.setContent("CameraExamplesConsoleLog.txt")

head1.addMeta(meta14)
meta15 = x3d.meta()
meta15.setName("reference")
meta15.setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.avi")

head1.addMeta(meta15)
meta16 = x3d.meta()
meta16.setName("reference")
meta16.setContent("http://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d")

head1.addMeta(meta16)
meta17 = x3d.meta()
meta17.setName("identifier")
meta17.setContent("http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d")

head1.addMeta(meta17)
meta18 = x3d.meta()
meta18.setName("identifier")
meta18.setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d")

head1.addMeta(meta18)
meta19 = x3d.meta()
meta19.setName("generator")
meta19.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta19)
meta20 = x3d.meta()
meta20.setName("license")
meta20.setContent("../license.html")

head1.addMeta(meta20)
#TODO warn if more than one identifier present

X3D0.setHead(head1)
Scene21 = x3d.Scene()
#=============== Camera ==============
ExternProtoDeclare22 = x3d.ExternProtoDeclare()
ExternProtoDeclare22.setName("Camera")
ExternProtoDeclare22.setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images")
ExternProtoDeclare22.setUrl(["CameraPrototypes.x3d#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#Camera","CameraPrototypes.wrl#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#Camera"])
#Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields
field23 = x3d.field()
field23.setName("description")
field23.setAccessType("inputOutput")
field23.setAppinfo("Text description to be displayed for this Camera")
field23.setType("SFString")

ExternProtoDeclare22.addField(field23)
field24 = x3d.field()
field24.setName("position")
field24.setAccessType("inputOutput")
field24.setAppinfo("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")
field24.setType("SFVec3f")

ExternProtoDeclare22.addField(field24)
field25 = x3d.field()
field25.setName("orientation")
field25.setAccessType("inputOutput")
field25.setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")
field25.setType("SFRotation")

ExternProtoDeclare22.addField(field25)
field26 = x3d.field()
field26.setName("fieldOfView")
field26.setAccessType("inputOutput")
field26.setAppinfo("pi/4")
field26.setType("SFFloat")

ExternProtoDeclare22.addField(field26)
field27 = x3d.field()
field27.setName("set_fraction")
field27.setAccessType("inputOnly")
field27.setAppinfo("input fraction drives interpolators")
field27.setType("SFFloat")

ExternProtoDeclare22.addField(field27)
field28 = x3d.field()
field28.setName("set_bind")
field28.setAccessType("inputOnly")
field28.setAppinfo("input event binds or unbinds this Camera")
field28.setType("SFBool")

ExternProtoDeclare22.addField(field28)
field29 = x3d.field()
field29.setName("bindTime")
field29.setAccessType("outputOnly")
field29.setAppinfo("output event indicates when this Camera is bound")
field29.setType("SFTime")

ExternProtoDeclare22.addField(field29)
field30 = x3d.field()
field30.setName("isBound")
field30.setAccessType("outputOnly")
field30.setAppinfo("output event indicates whether this Camera is bound or unbound")
field30.setType("SFBool")

ExternProtoDeclare22.addField(field30)
field31 = x3d.field()
field31.setName("nearClipPlane")
field31.setAccessType("inputOutput")
field31.setAppinfo("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]")
field31.setType("SFFloat")

ExternProtoDeclare22.addField(field31)
field32 = x3d.field()
field32.setName("farClipPlane")
field32.setAccessType("inputOutput")
field32.setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit")
field32.setType("SFFloat")

ExternProtoDeclare22.addField(field32)
field33 = x3d.field()
field33.setName("shots")
field33.setAccessType("inputOutput")
field33.setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes")
field33.setType("MFNode")

ExternProtoDeclare22.addField(field33)
field34 = x3d.field()
field34.setName("headlight")
field34.setAccessType("inputOutput")
field34.setAppinfo("Whether camera headlight is on or off")
field34.setType("SFBool")

ExternProtoDeclare22.addField(field34)
field35 = x3d.field()
field35.setName("headlightColor")
field35.setAccessType("inputOutput")
field35.setAppinfo("Camera headlight color")
field35.setType("SFColor")

ExternProtoDeclare22.addField(field35)
field36 = x3d.field()
field36.setName("headlightIntensity")
field36.setAccessType("inputOutput")
field36.setAppinfo("Camera headlight intensity")
field36.setType("SFFloat")

ExternProtoDeclare22.addField(field36)
field37 = x3d.field()
field37.setName("filterColor")
field37.setAccessType("inputOutput")
field37.setAppinfo("Camera filter color that modifies virtual lens capture")
field37.setType("SFColor")

ExternProtoDeclare22.addField(field37)
field38 = x3d.field()
field38.setName("filterTransparency")
field38.setAccessType("inputOutput")
field38.setAppinfo("Camera filter transparency that modifies virtual lens capture")
field38.setType("SFFloat")

ExternProtoDeclare22.addField(field38)
field39 = x3d.field()
field39.setName("upVector")
field39.setAccessType("inputOutput")
field39.setAppinfo("upVector changes modify camera orientation (and possibly vice versa)")
field39.setType("SFVec3f")

ExternProtoDeclare22.addField(field39)
field40 = x3d.field()
field40.setName("fStop")
field40.setAccessType("inputOutput")
field40.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field40.setType("SFFloat")

ExternProtoDeclare22.addField(field40)
field41 = x3d.field()
field41.setName("focusDistance")
field41.setAccessType("inputOutput")
field41.setAppinfo("Distance to focal plane of sharpest focus")
field41.setType("SFFloat")

ExternProtoDeclare22.addField(field41)
field42 = x3d.field()
field42.setName("isActive")
field42.setAccessType("outputOnly")
field42.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field42.setType("SFBool")

ExternProtoDeclare22.addField(field42)
field43 = x3d.field()
field43.setName("totalDuration")
field43.setAccessType("outputOnly")
field43.setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations")
field43.setType("SFTime")

ExternProtoDeclare22.addField(field43)
field44 = x3d.field()
field44.setName("offlineRender")
field44.setAccessType("inputOutput")
field44.setAppinfo("OfflineRender node")
field44.setType("SFNode")

ExternProtoDeclare22.addField(field44)
field45 = x3d.field()
field45.setName("traceEnabled")
field45.setAccessType("initializeOnly")
field45.setAppinfo("enable console output to trace script computations and prototype progress")
field45.setType("SFBool")

ExternProtoDeclare22.addField(field45)

Scene21.addChildren(ExternProtoDeclare22)
#=============== CameraShot ==============
ExternProtoDeclare46 = x3d.ExternProtoDeclare()
ExternProtoDeclare46.setName("CameraShot")
ExternProtoDeclare46.setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot")
ExternProtoDeclare46.setUrl(["CameraPrototypes.x3d#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraShot","CameraPrototypes.wrl#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraShot"])
field47 = x3d.field()
field47.setName("description")
field47.setAccessType("inputOutput")
field47.setAppinfo("Text description to be displayed for this CameraShot")
field47.setType("SFString")

ExternProtoDeclare46.addField(field47)
field48 = x3d.field()
field48.setName("enabled")
field48.setAccessType("inputOutput")
field48.setAppinfo("Whether this CameraShot can be activated")
field48.setType("SFBool")

ExternProtoDeclare46.addField(field48)
field49 = x3d.field()
field49.setName("moves")
field49.setAccessType("inputOutput")
field49.setAppinfo("Set of CameraMovement nodes")
field49.setType("MFNode")
#initializing CameraMovement nodes are inserted here by scene author using ProtoInstance

ExternProtoDeclare46.addField(field49)
field50 = x3d.field()
field50.setName("initialPosition")
field50.setAccessType("inputOutput")
field50.setAppinfo("Setup to reinitialize camera position for this shot")
field50.setType("SFVec3f")

ExternProtoDeclare46.addField(field50)
field51 = x3d.field()
field51.setName("initialOrientation")
field51.setAccessType("inputOutput")
field51.setAppinfo("Setup to reinitialize camera rotation for this shot")
field51.setType("SFRotation")

ExternProtoDeclare46.addField(field51)
field52 = x3d.field()
field52.setName("initialAimPoint")
field52.setAccessType("inputOutput")
field52.setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot")
field52.setType("SFVec3f")

ExternProtoDeclare46.addField(field52)
field53 = x3d.field()
field53.setName("initialFieldOfView")
field53.setAccessType("inputOutput")
field53.setAppinfo("pi/4")
field53.setType("SFFloat")

ExternProtoDeclare46.addField(field53)
field54 = x3d.field()
field54.setName("initialFStop")
field54.setAccessType("inputOutput")
field54.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field54.setType("SFFloat")

ExternProtoDeclare46.addField(field54)
field55 = x3d.field()
field55.setName("initialFocusDistance")
field55.setAccessType("inputOutput")
field55.setAppinfo("Distance to focal plane of sharpest focus")
field55.setType("SFFloat")

ExternProtoDeclare46.addField(field55)
field56 = x3d.field()
field56.setName("shotDuration")
field56.setAccessType("outputOnly")
field56.setAppinfo("Subtotal duration of contained CameraMovement move durations")
field56.setType("SFTime")

ExternProtoDeclare46.addField(field56)
field57 = x3d.field()
field57.setName("isActive")
field57.setAccessType("outputOnly")
field57.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field57.setType("SFBool")

ExternProtoDeclare46.addField(field57)
field58 = x3d.field()
field58.setName("traceEnabled")
field58.setAccessType("initializeOnly")
field58.setAppinfo("enable console output to trace script computations and prototype progress")
field58.setType("SFBool")

ExternProtoDeclare46.addField(field58)

Scene21.addChildren(ExternProtoDeclare46)
#=============== CameraMovement ==============
ExternProtoDeclare59 = x3d.ExternProtoDeclare()
ExternProtoDeclare59.setName("CameraMovement")
ExternProtoDeclare59.setAppinfo("CameraMovement defines a single camera movement animation")
ExternProtoDeclare59.setUrl(["CameraPrototypes.x3d#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraMovement","CameraPrototypes.wrl#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraMovement"])
field60 = x3d.field()
field60.setName("description")
field60.setAccessType("inputOutput")
field60.setAppinfo("Text description to be displayed for this CameraMovement")
field60.setType("SFString")

ExternProtoDeclare59.addField(field60)
field61 = x3d.field()
field61.setName("enabled")
field61.setAccessType("inputOutput")
field61.setAppinfo("Whether this CameraMovement can be activated")
field61.setType("SFBool")

ExternProtoDeclare59.addField(field61)
field62 = x3d.field()
field62.setName("duration")
field62.setAccessType("inputOutput")
field62.setAppinfo("Duration in seconds for this move")
field62.setType("SFFloat")

ExternProtoDeclare59.addField(field62)
field63 = x3d.field()
field63.setName("goalPosition")
field63.setAccessType("inputOutput")
field63.setAppinfo("Goal camera position for this move")
field63.setType("SFVec3f")

ExternProtoDeclare59.addField(field63)
field64 = x3d.field()
field64.setName("goalOrientation")
field64.setAccessType("inputOutput")
field64.setAppinfo("Goal camera rotation for this move")
field64.setType("SFRotation")

ExternProtoDeclare59.addField(field64)
field65 = x3d.field()
field65.setName("tracking")
field65.setAccessType("inputOutput")
field65.setAppinfo("Whether or not camera direction is tracking towards the aimPoint")
field65.setType("SFBool")

ExternProtoDeclare59.addField(field65)
field66 = x3d.field()
field66.setName("goalAimPoint")
field66.setAccessType("inputOutput")
field66.setAppinfo("Goal aimPoint for this move, ignored if tracking=false")
field66.setType("SFVec3f")

ExternProtoDeclare59.addField(field66)
field67 = x3d.field()
field67.setName("goalFieldOfView")
field67.setAccessType("inputOutput")
field67.setAppinfo("Goal fieldOfView for this move")
field67.setType("SFFloat")

ExternProtoDeclare59.addField(field67)
field68 = x3d.field()
field68.setName("goalFStop")
field68.setAccessType("inputOutput")
field68.setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane")
field68.setType("SFFloat")

ExternProtoDeclare59.addField(field68)
field69 = x3d.field()
field69.setName("goalFocusDistance")
field69.setAccessType("inputOutput")
field69.setAppinfo("Distance to focal plane of sharpest focus")
field69.setType("SFFloat")

ExternProtoDeclare59.addField(field69)
field70 = x3d.field()
field70.setName("isActive")
field70.setAccessType("outputOnly")
field70.setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations")
field70.setType("SFBool")

ExternProtoDeclare59.addField(field70)
field71 = x3d.field()
field71.setName("traceEnabled")
field71.setAccessType("initializeOnly")
field71.setAppinfo("enable console output to trace script computations and prototype progress")
field71.setType("SFBool")

ExternProtoDeclare59.addField(field71)

Scene21.addChildren(ExternProtoDeclare59)
#=============== OfflineRender ==============
ExternProtoDeclare72 = x3d.ExternProtoDeclare()
ExternProtoDeclare72.setName("OfflineRender")
ExternProtoDeclare72.setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)")
ExternProtoDeclare72.setUrl(["CameraPrototypes.x3d#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#OfflineRender","CameraPrototypes.wrl#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#OfflineRender"])
#TODO non-photorealistic rendering (NPR) parameters
field73 = x3d.field()
field73.setName("description")
field73.setAccessType("inputOutput")
field73.setAppinfo("Text description to be displayed for this OfflineRender")
field73.setType("SFString")

ExternProtoDeclare72.addField(field73)
field74 = x3d.field()
field74.setName("enabled")
field74.setAccessType("inputOutput")
field74.setAppinfo("Whether this OfflineRender can be activated")
field74.setType("SFBool")

ExternProtoDeclare72.addField(field74)
field75 = x3d.field()
field75.setName("frameRate")
field75.setAccessType("inputOutput")
field75.setAppinfo("Frames per second recorded for this rendering")
field75.setType("SFFloat")

ExternProtoDeclare72.addField(field75)
field76 = x3d.field()
field76.setName("frameSize")
field76.setAccessType("inputOutput")
field76.setAppinfo("Size of frame in number of pixels width and height")
field76.setType("SFVec2f")

ExternProtoDeclare72.addField(field76)
field77 = x3d.field()
field77.setName("pixelAspectRatio")
field77.setAccessType("inputOutput")
field77.setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1")
field77.setType("SFFloat")

ExternProtoDeclare72.addField(field77)
field78 = x3d.field()
field78.setName("set_startTime")
field78.setAccessType("inputOnly")
field78.setAppinfo("Begin render operation")
field78.setType("SFTime")

ExternProtoDeclare72.addField(field78)
field79 = x3d.field()
field79.setName("progress")
field79.setAccessType("outputOnly")
field79.setAppinfo("Progress performing render operation (0..1)")
field79.setType("SFFloat")

ExternProtoDeclare72.addField(field79)
field80 = x3d.field()
field80.setName("renderCompleteTime")
field80.setAccessType("outputOnly")
field80.setAppinfo("Render operation complete")
field80.setType("SFTime")

ExternProtoDeclare72.addField(field80)
field81 = x3d.field()
field81.setName("movieFormat")
field81.setAccessType("initializeOnly")
field81.setAppinfo("Format of rendered output movie (mpeg mp4 etc.), use first supported format")
field81.setType("MFString")

ExternProtoDeclare72.addField(field81)
field82 = x3d.field()
field82.setName("imageFormat")
field82.setAccessType("initializeOnly")
field82.setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format")
field82.setType("MFString")

ExternProtoDeclare72.addField(field82)
field83 = x3d.field()
field83.setName("traceEnabled")
field83.setAccessType("initializeOnly")
field83.setAppinfo("enable console output to trace script computations and prototype progress")
field83.setType("SFBool")

ExternProtoDeclare72.addField(field83)

Scene21.addChildren(ExternProtoDeclare72)
#=============== Lights, camera, action! ==============
DirectionalLight84 = x3d.DirectionalLight()
DirectionalLight84.setDirection([0,-1,0])
DirectionalLight84.setGlobal(True)
DirectionalLight84.setIntensity(0.8)

Scene21.addChildren(DirectionalLight84)
NavigationInfo85 = x3d.NavigationInfo()
NavigationInfo85.setType(["EXAMINE","FLY","ANY"])

Scene21.addChildren(NavigationInfo85)
Viewpoint86 = x3d.Viewpoint()
Viewpoint86.setDescription("Camera test scene entry view")
Viewpoint86.setPosition([0,2,12])

Scene21.addChildren(Viewpoint86)
Viewpoint87 = x3d.Viewpoint()
Viewpoint87.setDescription("Camera test scene from above")
Viewpoint87.setOrientation([1,0,0,-1.57079])
Viewpoint87.setPosition([0,150,0])

Scene21.addChildren(Viewpoint87)
#Keep prototype instances in same file while developing, then move later
#We will create examples matching those in the paper
#=============== Camera.SimpleShotsTest ==============
ProtoInstance88 = x3d.ProtoInstance()
ProtoInstance88.setName("Camera")
ProtoInstance88.setDEF("Camera.SimpleShotsTest")
fieldValue89 = x3d.fieldValue()
fieldValue89.setName("description")
fieldValue89.setValue("SimpleShotsTest for camera Zoom Dolly Pan Boom and Tilt")

ProtoInstance88.addFieldValue(fieldValue89)
fieldValue90 = x3d.fieldValue()
fieldValue90.setName("headlight")
fieldValue90.setValue("true")

ProtoInstance88.addFieldValue(fieldValue90)
fieldValue91 = x3d.fieldValue()
fieldValue91.setName("position")
fieldValue91.setValue("-4 4 10")

ProtoInstance88.addFieldValue(fieldValue91)
fieldValue92 = x3d.fieldValue()
fieldValue92.setName("shots")
ProtoInstance93 = x3d.ProtoInstance()
ProtoInstance93.setName("CameraShot")
ProtoInstance93.setDEF("Zoom")
fieldValue94 = x3d.fieldValue()
fieldValue94.setName("description")
fieldValue94.setValue("Simple shot of Camera Zoom")

ProtoInstance93.addFieldValue(fieldValue94)
fieldValue95 = x3d.fieldValue()
fieldValue95.setName("initialPosition")
fieldValue95.setValue("-50 1 -10")

ProtoInstance93.addFieldValue(fieldValue95)
fieldValue96 = x3d.fieldValue()
fieldValue96.setName("initialOrientation")
fieldValue96.setValue("0 1 0 0")

ProtoInstance93.addFieldValue(fieldValue96)
fieldValue97 = x3d.fieldValue()
fieldValue97.setName("moves")
ProtoInstance98 = x3d.ProtoInstance()
ProtoInstance98.setName("CameraMovement")
fieldValue99 = x3d.fieldValue()
fieldValue99.setName("description")
fieldValue99.setValue("Camera Zoom In")

ProtoInstance98.addFieldValue(fieldValue99)
fieldValue100 = x3d.fieldValue()
fieldValue100.setName("duration")
fieldValue100.setValue("3")

ProtoInstance98.addFieldValue(fieldValue100)
fieldValue101 = x3d.fieldValue()
fieldValue101.setName("goalPosition")
fieldValue101.setValue("-50 1 -15")

ProtoInstance98.addFieldValue(fieldValue101)
fieldValue102 = x3d.fieldValue()
fieldValue102.setName("goalOrientation")
fieldValue102.setValue("0 1 0 0")

ProtoInstance98.addFieldValue(fieldValue102)

fieldValue97.addChildren(ProtoInstance98)
ProtoInstance103 = x3d.ProtoInstance()
ProtoInstance103.setName("CameraMovement")
fieldValue104 = x3d.fieldValue()
fieldValue104.setName("description")
fieldValue104.setValue("Camera Zoom Out")

ProtoInstance103.addFieldValue(fieldValue104)
fieldValue105 = x3d.fieldValue()
fieldValue105.setName("duration")
fieldValue105.setValue("3")

ProtoInstance103.addFieldValue(fieldValue105)
fieldValue106 = x3d.fieldValue()
fieldValue106.setName("goalPosition")
fieldValue106.setValue("-50 1 -10")

ProtoInstance103.addFieldValue(fieldValue106)
fieldValue107 = x3d.fieldValue()
fieldValue107.setName("goalOrientation")
fieldValue107.setValue("0 1 0 0")

ProtoInstance103.addFieldValue(fieldValue107)

fieldValue97.addChildren(ProtoInstance103)
ProtoInstance108 = x3d.ProtoInstance()
ProtoInstance108.setName("CameraMovement")
fieldValue109 = x3d.fieldValue()
fieldValue109.setName("description")
fieldValue109.setValue("Camera Pause")

ProtoInstance108.addFieldValue(fieldValue109)
fieldValue110 = x3d.fieldValue()
fieldValue110.setName("duration")
fieldValue110.setValue("1")

ProtoInstance108.addFieldValue(fieldValue110)
fieldValue111 = x3d.fieldValue()
fieldValue111.setName("goalPosition")
fieldValue111.setValue("-50 1 -10")

ProtoInstance108.addFieldValue(fieldValue111)
fieldValue112 = x3d.fieldValue()
fieldValue112.setName("goalOrientation")
fieldValue112.setValue("0 1 0 0")

ProtoInstance108.addFieldValue(fieldValue112)

fieldValue97.addChildren(ProtoInstance108)

ProtoInstance93.addFieldValue(fieldValue97)

fieldValue92.addChildren(ProtoInstance93)
ProtoInstance113 = x3d.ProtoInstance()
ProtoInstance113.setName("CameraShot")
ProtoInstance113.setDEF("Dolly")
fieldValue114 = x3d.fieldValue()
fieldValue114.setName("description")
fieldValue114.setValue("Simple shot of Camera Dolly")

ProtoInstance113.addFieldValue(fieldValue114)
fieldValue115 = x3d.fieldValue()
fieldValue115.setName("initialPosition")
fieldValue115.setValue("-40 1 -10")

ProtoInstance113.addFieldValue(fieldValue115)
fieldValue116 = x3d.fieldValue()
fieldValue116.setName("initialOrientation")
fieldValue116.setValue("0 1 0 0")

ProtoInstance113.addFieldValue(fieldValue116)
fieldValue117 = x3d.fieldValue()
fieldValue117.setName("moves")
ProtoInstance118 = x3d.ProtoInstance()
ProtoInstance118.setName("CameraMovement")
ProtoInstance118.setDEF("DollyMove1")
fieldValue119 = x3d.fieldValue()
fieldValue119.setName("description")
fieldValue119.setValue("Camera Dolly from Right to Left")

ProtoInstance118.addFieldValue(fieldValue119)
fieldValue120 = x3d.fieldValue()
fieldValue120.setName("duration")
fieldValue120.setValue("3")

ProtoInstance118.addFieldValue(fieldValue120)
fieldValue121 = x3d.fieldValue()
fieldValue121.setName("goalPosition")
fieldValue121.setValue("-45 1 -10")

ProtoInstance118.addFieldValue(fieldValue121)
fieldValue122 = x3d.fieldValue()
fieldValue122.setName("goalOrientation")
fieldValue122.setValue("0 1 0 0")

ProtoInstance118.addFieldValue(fieldValue122)

fieldValue117.addChildren(ProtoInstance118)
ProtoInstance123 = x3d.ProtoInstance()
ProtoInstance123.setName("CameraMovement")
fieldValue124 = x3d.fieldValue()
fieldValue124.setName("description")
fieldValue124.setValue("Camera Dolly from Left to Right")

ProtoInstance123.addFieldValue(fieldValue124)
fieldValue125 = x3d.fieldValue()
fieldValue125.setName("duration")
fieldValue125.setValue("3")

ProtoInstance123.addFieldValue(fieldValue125)
fieldValue126 = x3d.fieldValue()
fieldValue126.setName("goalPosition")
fieldValue126.setValue("-40 1 -10")

ProtoInstance123.addFieldValue(fieldValue126)
fieldValue127 = x3d.fieldValue()
fieldValue127.setName("goalOrientation")
fieldValue127.setValue("0 1 0 0")

ProtoInstance123.addFieldValue(fieldValue127)

fieldValue117.addChildren(ProtoInstance123)
ProtoInstance128 = x3d.ProtoInstance()
ProtoInstance128.setName("CameraMovement")
fieldValue129 = x3d.fieldValue()
fieldValue129.setName("description")
fieldValue129.setValue("Camera Pause")

ProtoInstance128.addFieldValue(fieldValue129)
fieldValue130 = x3d.fieldValue()
fieldValue130.setName("duration")
fieldValue130.setValue("1")

ProtoInstance128.addFieldValue(fieldValue130)
fieldValue131 = x3d.fieldValue()
fieldValue131.setName("goalPosition")
fieldValue131.setValue("-40 1 -10")

ProtoInstance128.addFieldValue(fieldValue131)
fieldValue132 = x3d.fieldValue()
fieldValue132.setName("goalOrientation")
fieldValue132.setValue("0 1 0 0")

ProtoInstance128.addFieldValue(fieldValue132)

fieldValue117.addChildren(ProtoInstance128)

ProtoInstance113.addFieldValue(fieldValue117)

fieldValue92.addChildren(ProtoInstance113)
ProtoInstance133 = x3d.ProtoInstance()
ProtoInstance133.setName("CameraShot")
ProtoInstance133.setDEF("Pan")
fieldValue134 = x3d.fieldValue()
fieldValue134.setName("description")
fieldValue134.setValue("Simple shot of Camera Pan left right and back to center")

ProtoInstance133.addFieldValue(fieldValue134)
fieldValue135 = x3d.fieldValue()
fieldValue135.setName("initialPosition")
fieldValue135.setValue("-30 1 -10")

ProtoInstance133.addFieldValue(fieldValue135)
fieldValue136 = x3d.fieldValue()
fieldValue136.setName("initialOrientation")
fieldValue136.setValue("0 1 0 0")

ProtoInstance133.addFieldValue(fieldValue136)
fieldValue137 = x3d.fieldValue()
fieldValue137.setName("moves")
ProtoInstance138 = x3d.ProtoInstance()
ProtoInstance138.setName("CameraMovement")
ProtoInstance138.setDEF("PanLeft")
fieldValue139 = x3d.fieldValue()
fieldValue139.setName("description")
fieldValue139.setValue("Pan Left")

ProtoInstance138.addFieldValue(fieldValue139)
fieldValue140 = x3d.fieldValue()
fieldValue140.setName("duration")
fieldValue140.setValue("2")

ProtoInstance138.addFieldValue(fieldValue140)
fieldValue141 = x3d.fieldValue()
fieldValue141.setName("goalPosition")
fieldValue141.setValue("-30 1 -10")

ProtoInstance138.addFieldValue(fieldValue141)
fieldValue142 = x3d.fieldValue()
fieldValue142.setName("goalOrientation")
fieldValue142.setValue("0 1 0 0.4")

ProtoInstance138.addFieldValue(fieldValue142)

fieldValue137.addChildren(ProtoInstance138)
ProtoInstance143 = x3d.ProtoInstance()
ProtoInstance143.setName("CameraMovement")
ProtoInstance143.setDEF("PanRight")
fieldValue144 = x3d.fieldValue()
fieldValue144.setName("description")
fieldValue144.setValue("Pan Right")

ProtoInstance143.addFieldValue(fieldValue144)
fieldValue145 = x3d.fieldValue()
fieldValue145.setName("duration")
fieldValue145.setValue("3")

ProtoInstance143.addFieldValue(fieldValue145)
fieldValue146 = x3d.fieldValue()
fieldValue146.setName("goalPosition")
fieldValue146.setValue("-30 1 -10")

ProtoInstance143.addFieldValue(fieldValue146)
fieldValue147 = x3d.fieldValue()
fieldValue147.setName("goalOrientation")
fieldValue147.setValue("0 1 0 -0.4")

ProtoInstance143.addFieldValue(fieldValue147)

fieldValue137.addChildren(ProtoInstance143)
ProtoInstance148 = x3d.ProtoInstance()
ProtoInstance148.setName("CameraMovement")
fieldValue149 = x3d.fieldValue()
fieldValue149.setName("description")
fieldValue149.setValue("Camera Pan back to Center")

ProtoInstance148.addFieldValue(fieldValue149)
fieldValue150 = x3d.fieldValue()
fieldValue150.setName("duration")
fieldValue150.setValue("2")

ProtoInstance148.addFieldValue(fieldValue150)
fieldValue151 = x3d.fieldValue()
fieldValue151.setName("goalPosition")
fieldValue151.setValue("-30 1 -10")

ProtoInstance148.addFieldValue(fieldValue151)
fieldValue152 = x3d.fieldValue()
fieldValue152.setName("goalOrientation")
fieldValue152.setValue("0 1 0 0")

ProtoInstance148.addFieldValue(fieldValue152)

fieldValue137.addChildren(ProtoInstance148)
ProtoInstance153 = x3d.ProtoInstance()
ProtoInstance153.setName("CameraMovement")
fieldValue154 = x3d.fieldValue()
fieldValue154.setName("description")
fieldValue154.setValue("Camera Pause")

ProtoInstance153.addFieldValue(fieldValue154)
fieldValue155 = x3d.fieldValue()
fieldValue155.setName("duration")
fieldValue155.setValue("2")

ProtoInstance153.addFieldValue(fieldValue155)
fieldValue156 = x3d.fieldValue()
fieldValue156.setName("goalPosition")
fieldValue156.setValue("-30 1 -10")

ProtoInstance153.addFieldValue(fieldValue156)
fieldValue157 = x3d.fieldValue()
fieldValue157.setName("goalOrientation")
fieldValue157.setValue("0 1 0 0")

ProtoInstance153.addFieldValue(fieldValue157)

fieldValue137.addChildren(ProtoInstance153)

ProtoInstance133.addFieldValue(fieldValue137)

fieldValue92.addChildren(ProtoInstance133)
ProtoInstance158 = x3d.ProtoInstance()
ProtoInstance158.setName("CameraShot")
ProtoInstance158.setDEF("CameraBoom")
fieldValue159 = x3d.fieldValue()
fieldValue159.setName("description")
fieldValue159.setValue("Camera Boom")

ProtoInstance158.addFieldValue(fieldValue159)
fieldValue160 = x3d.fieldValue()
fieldValue160.setName("initialPosition")
fieldValue160.setValue("-20 1 -10")

ProtoInstance158.addFieldValue(fieldValue160)
fieldValue161 = x3d.fieldValue()
fieldValue161.setName("initialOrientation")
fieldValue161.setValue("0 1 0 0")

ProtoInstance158.addFieldValue(fieldValue161)
fieldValue162 = x3d.fieldValue()
fieldValue162.setName("moves")
ProtoInstance163 = x3d.ProtoInstance()
ProtoInstance163.setName("CameraMovement")
ProtoInstance163.setDEF("CameraBoomUp")
fieldValue164 = x3d.fieldValue()
fieldValue164.setName("description")
fieldValue164.setValue("Camera Boom Up")

ProtoInstance163.addFieldValue(fieldValue164)
fieldValue165 = x3d.fieldValue()
fieldValue165.setName("duration")
fieldValue165.setValue("3")

ProtoInstance163.addFieldValue(fieldValue165)
fieldValue166 = x3d.fieldValue()
fieldValue166.setName("goalPosition")
fieldValue166.setValue("-20 5 -10")

ProtoInstance163.addFieldValue(fieldValue166)
fieldValue167 = x3d.fieldValue()
fieldValue167.setName("goalOrientation")
fieldValue167.setValue("0 1 0 0")

ProtoInstance163.addFieldValue(fieldValue167)

fieldValue162.addChildren(ProtoInstance163)
ProtoInstance168 = x3d.ProtoInstance()
ProtoInstance168.setName("CameraMovement")
ProtoInstance168.setDEF("BoomDown")
fieldValue169 = x3d.fieldValue()
fieldValue169.setName("description")
fieldValue169.setValue("Camera Boom Down")

ProtoInstance168.addFieldValue(fieldValue169)
fieldValue170 = x3d.fieldValue()
fieldValue170.setName("duration")
fieldValue170.setValue("3")

ProtoInstance168.addFieldValue(fieldValue170)
fieldValue171 = x3d.fieldValue()
fieldValue171.setName("goalPosition")
fieldValue171.setValue("-20 1 -10")

ProtoInstance168.addFieldValue(fieldValue171)
fieldValue172 = x3d.fieldValue()
fieldValue172.setName("goalOrientation")
fieldValue172.setValue("0 1 0 0")

ProtoInstance168.addFieldValue(fieldValue172)

fieldValue162.addChildren(ProtoInstance168)
ProtoInstance173 = x3d.ProtoInstance()
ProtoInstance173.setName("CameraMovement")
ProtoInstance173.setDEF("BoomPause")
fieldValue174 = x3d.fieldValue()
fieldValue174.setName("description")
fieldValue174.setValue("Camera Pause")

ProtoInstance173.addFieldValue(fieldValue174)
fieldValue175 = x3d.fieldValue()
fieldValue175.setName("duration")
fieldValue175.setValue("2")

ProtoInstance173.addFieldValue(fieldValue175)
fieldValue176 = x3d.fieldValue()
fieldValue176.setName("goalPosition")
fieldValue176.setValue("-20 1 -10")

ProtoInstance173.addFieldValue(fieldValue176)
fieldValue177 = x3d.fieldValue()
fieldValue177.setName("goalOrientation")
fieldValue177.setValue("0 1 0 0")

ProtoInstance173.addFieldValue(fieldValue177)

fieldValue162.addChildren(ProtoInstance173)

ProtoInstance158.addFieldValue(fieldValue162)

fieldValue92.addChildren(ProtoInstance158)
ProtoInstance178 = x3d.ProtoInstance()
ProtoInstance178.setName("CameraShot")
ProtoInstance178.setDEF("CameraTilt")
fieldValue179 = x3d.fieldValue()
fieldValue179.setName("description")
fieldValue179.setValue("Camera Tilt")

ProtoInstance178.addFieldValue(fieldValue179)
fieldValue180 = x3d.fieldValue()
fieldValue180.setName("initialPosition")
fieldValue180.setValue("-10 1 -10")

ProtoInstance178.addFieldValue(fieldValue180)
fieldValue181 = x3d.fieldValue()
fieldValue181.setName("initialOrientation")
fieldValue181.setValue("0 0 1 0")

ProtoInstance178.addFieldValue(fieldValue181)
fieldValue182 = x3d.fieldValue()
fieldValue182.setName("traceEnabled")
fieldValue182.setValue("true")

ProtoInstance178.addFieldValue(fieldValue182)
fieldValue183 = x3d.fieldValue()
fieldValue183.setName("moves")
ProtoInstance184 = x3d.ProtoInstance()
ProtoInstance184.setName("CameraMovement")
fieldValue185 = x3d.fieldValue()
fieldValue185.setName("description")
fieldValue185.setValue("Camera Tilt Pause")

ProtoInstance184.addFieldValue(fieldValue185)
fieldValue186 = x3d.fieldValue()
fieldValue186.setName("duration")
fieldValue186.setValue("1")

ProtoInstance184.addFieldValue(fieldValue186)
fieldValue187 = x3d.fieldValue()
fieldValue187.setName("goalPosition")
fieldValue187.setValue("-10 1 -10")

ProtoInstance184.addFieldValue(fieldValue187)
fieldValue188 = x3d.fieldValue()
fieldValue188.setName("goalOrientation")
fieldValue188.setValue("0 0 1 0")

ProtoInstance184.addFieldValue(fieldValue188)

fieldValue183.addChildren(ProtoInstance184)
ProtoInstance189 = x3d.ProtoInstance()
ProtoInstance189.setName("CameraMovement")
ProtoInstance189.setDEF("TiltDown")
fieldValue190 = x3d.fieldValue()
fieldValue190.setName("description")
fieldValue190.setValue("Camera Tilt Left")

ProtoInstance189.addFieldValue(fieldValue190)
fieldValue191 = x3d.fieldValue()
fieldValue191.setName("duration")
fieldValue191.setValue("3")

ProtoInstance189.addFieldValue(fieldValue191)
fieldValue192 = x3d.fieldValue()
fieldValue192.setName("goalPosition")
fieldValue192.setValue("-10 1 -10")

ProtoInstance189.addFieldValue(fieldValue192)
fieldValue193 = x3d.fieldValue()
fieldValue193.setName("goalOrientation")
fieldValue193.setValue("0 0 1 0.785")

ProtoInstance189.addFieldValue(fieldValue193)

fieldValue183.addChildren(ProtoInstance189)
ProtoInstance194 = x3d.ProtoInstance()
ProtoInstance194.setName("CameraMovement")
ProtoInstance194.setDEF("TiltPause")
fieldValue195 = x3d.fieldValue()
fieldValue195.setName("description")
fieldValue195.setValue("Camera Tilt Pause")

ProtoInstance194.addFieldValue(fieldValue195)
fieldValue196 = x3d.fieldValue()
fieldValue196.setName("duration")
fieldValue196.setValue("1")

ProtoInstance194.addFieldValue(fieldValue196)
fieldValue197 = x3d.fieldValue()
fieldValue197.setName("goalPosition")
fieldValue197.setValue("-10 1 -10")

ProtoInstance194.addFieldValue(fieldValue197)
fieldValue198 = x3d.fieldValue()
fieldValue198.setName("goalOrientation")
fieldValue198.setValue("0 0 1 0.785")

ProtoInstance194.addFieldValue(fieldValue198)

fieldValue183.addChildren(ProtoInstance194)
ProtoInstance199 = x3d.ProtoInstance()
ProtoInstance199.setName("CameraMovement")
fieldValue200 = x3d.fieldValue()
fieldValue200.setName("description")
fieldValue200.setValue("Camera Tilt Right")

ProtoInstance199.addFieldValue(fieldValue200)
fieldValue201 = x3d.fieldValue()
fieldValue201.setName("duration")
fieldValue201.setValue("3")

ProtoInstance199.addFieldValue(fieldValue201)
fieldValue202 = x3d.fieldValue()
fieldValue202.setName("goalPosition")
fieldValue202.setValue("-10 1 -10")

ProtoInstance199.addFieldValue(fieldValue202)
fieldValue203 = x3d.fieldValue()
fieldValue203.setName("goalOrientation")
fieldValue203.setValue("0 0 1 -0.785")

ProtoInstance199.addFieldValue(fieldValue203)

fieldValue183.addChildren(ProtoInstance199)
ProtoInstance204 = x3d.ProtoInstance()
ProtoInstance204.setName("CameraMovement")
fieldValue205 = x3d.fieldValue()
fieldValue205.setName("description")
fieldValue205.setValue("Camera Tilt Pause")

ProtoInstance204.addFieldValue(fieldValue205)
fieldValue206 = x3d.fieldValue()
fieldValue206.setName("duration")
fieldValue206.setValue("1")

ProtoInstance204.addFieldValue(fieldValue206)
fieldValue207 = x3d.fieldValue()
fieldValue207.setName("goalPosition")
fieldValue207.setValue("-10 1 -10")

ProtoInstance204.addFieldValue(fieldValue207)
fieldValue208 = x3d.fieldValue()
fieldValue208.setName("goalOrientation")
fieldValue208.setValue("0 0 1 -0.785")

ProtoInstance204.addFieldValue(fieldValue208)

fieldValue183.addChildren(ProtoInstance204)
ProtoInstance209 = x3d.ProtoInstance()
ProtoInstance209.setName("CameraMovement")
ProtoInstance209.setDEF("TiltReset")
fieldValue210 = x3d.fieldValue()
fieldValue210.setName("description")
fieldValue210.setValue("Camera Tilt Reset")

ProtoInstance209.addFieldValue(fieldValue210)
fieldValue211 = x3d.fieldValue()
fieldValue211.setName("duration")
fieldValue211.setValue("1")

ProtoInstance209.addFieldValue(fieldValue211)
fieldValue212 = x3d.fieldValue()
fieldValue212.setName("goalPosition")
fieldValue212.setValue("-10 1 -10")

ProtoInstance209.addFieldValue(fieldValue212)
fieldValue213 = x3d.fieldValue()
fieldValue213.setName("goalOrientation")
fieldValue213.setValue("0 0 1 0")

ProtoInstance209.addFieldValue(fieldValue213)

fieldValue183.addChildren(ProtoInstance209)
ProtoInstance214 = x3d.ProtoInstance()
ProtoInstance214.setName("CameraMovement")
ProtoInstance214.setDEF("TiltUp")
fieldValue215 = x3d.fieldValue()
fieldValue215.setName("description")
fieldValue215.setValue("Return to home")

ProtoInstance214.addFieldValue(fieldValue215)
fieldValue216 = x3d.fieldValue()
fieldValue216.setName("duration")
fieldValue216.setValue("2")

ProtoInstance214.addFieldValue(fieldValue216)
fieldValue217 = x3d.fieldValue()
fieldValue217.setName("goalPosition")
fieldValue217.setValue("0 2 12")

ProtoInstance214.addFieldValue(fieldValue217)
fieldValue218 = x3d.fieldValue()
fieldValue218.setName("goalOrientation")
fieldValue218.setValue("0 0 1 0")

ProtoInstance214.addFieldValue(fieldValue218)

fieldValue183.addChildren(ProtoInstance214)

ProtoInstance178.addFieldValue(fieldValue183)

fieldValue92.addChildren(ProtoInstance178)

ProtoInstance88.addFieldValue(fieldValue92)

Scene21.addChildren(ProtoInstance88)
Group219 = x3d.Group()
Group219.setDEF("AnimationGroup.SimpleShots")
TimeSensor220 = x3d.TimeSensor()
TimeSensor220.setDEF("CameraTimer.SimpleShots")

Group219.addChildren(TimeSensor220)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE221 = x3d.ROUTE()
ROUTE221.setFromField("totalDuration")
ROUTE221.setFromNode("Camera.SimpleShotsTest")
ROUTE221.setToField("cycleInterval")
ROUTE221.setToNode("CameraTimer.SimpleShots")

Group219.addChildren(ROUTE221)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE222 = x3d.ROUTE()
ROUTE222.setFromField("fraction_changed")
ROUTE222.setFromNode("CameraTimer.SimpleShots")
ROUTE222.setToField("set_fraction")
ROUTE222.setToNode("Camera.SimpleShotsTest")

Group219.addChildren(ROUTE222)
Transform223 = x3d.Transform()
Transform223.setDEF("Trigger.SimpleShots")
Transform223.setTranslation([-4,4,0])
BooleanFilter224 = x3d.BooleanFilter()
BooleanFilter224.setDEF("TextTouchActive.SimpleShotsFilter")

Transform223.addChildren(BooleanFilter224)
TouchSensor225 = x3d.TouchSensor()
TouchSensor225.setDEF("TextTouch.SimpleShots")
TouchSensor225.setDescription("touch to animate Camera SimpleShotsTest")

Transform223.addChildren(TouchSensor225)
ROUTE226 = x3d.ROUTE()
ROUTE226.setFromField("inputTrue")
ROUTE226.setFromNode("TextTouchActive.SimpleShotsFilter")
ROUTE226.setToField("set_bind")
ROUTE226.setToNode("Camera.SimpleShotsTest")

Transform223.addChildren(ROUTE226)
ROUTE227 = x3d.ROUTE()
ROUTE227.setFromField("isActive")
ROUTE227.setFromNode("TextTouch.SimpleShots")
ROUTE227.setToField("set_boolean")
ROUTE227.setToNode("TextTouchActive.SimpleShotsFilter")

Transform223.addChildren(ROUTE227)
ROUTE228 = x3d.ROUTE()
ROUTE228.setFromField("touchTime")
ROUTE228.setFromNode("TextTouch.SimpleShots")
ROUTE228.setToField("startTime")
ROUTE228.setToNode("CameraTimer.SimpleShots")

Transform223.addChildren(ROUTE228)
Shape229 = x3d.Shape()
Text230 = x3d.Text()
Text230.setString(["Click to animate","SimpleShotsTest"])
FontStyle231 = x3d.FontStyle()
FontStyle231.setJustify(["MIDDLE","MIDDLE"])

Text230.setFontStyle(FontStyle231)

Shape229.setGeometry(Text230)
Appearance232 = x3d.Appearance()
Material233 = x3d.Material()
Material233.setDEF("ArtDeco5")
Material233.setAmbientIntensity(0.24)
Material233.setDiffuseColor([0.945455,0.318988,0.321717])
Material233.setShininess(0.01)
Material233.setSpecularColor([0.072727,0.021705,0.010732])
#Universal Media Library: ArtDeco 5

Appearance232.setMaterial(Material233)

Shape229.setAppearance(Appearance232)

Transform223.addChildren(Shape229)
#Simplify intersection test for user selecting text
Shape234 = x3d.Shape()
Shape234.setDEF("TransparentBox")
Appearance235 = x3d.Appearance()
Material236 = x3d.Material()
Material236.setTransparency(1)

Appearance235.setMaterial(Material236)

Shape234.setAppearance(Appearance235)
Box237 = x3d.Box()
Box237.setSize([6,2,0.0001])

Shape234.setGeometry(Box237)

Transform223.addChildren(Shape234)

Group219.addChildren(Transform223)

Scene21.addChildren(Group219)
Group238 = x3d.Group()
Group238.setDEF("SimpleShotsTargets")
Transform239 = x3d.Transform()
Transform239.setDEF("TargetBoxZoom")
Transform239.setTranslation([-50,1,-20])
Shape240 = x3d.Shape()
Box241 = x3d.Box()

Shape240.setGeometry(Box241)
Appearance242 = x3d.Appearance()
Material243 = x3d.Material()

Appearance242.setMaterial(Material243)
ImageTexture244 = x3d.ImageTexture()
ImageTexture244.setUrl(["images/CameraMoveZoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveZoom.png"])

Appearance242.setTexture(ImageTexture244)

Shape240.setAppearance(Appearance242)

Transform239.addChildren(Shape240)
Transform245 = x3d.Transform()
Transform245.setTranslation([0,2,0])
Shape246 = x3d.Shape()
Text247 = x3d.Text()
Text247.setString(["Zoom in, out"])
FontStyle248 = x3d.FontStyle()
FontStyle248.setJustify(["MIDDLE","MIDDLE"])

Text247.setFontStyle(FontStyle248)

Shape246.setGeometry(Text247)
Appearance249 = x3d.Appearance()
Material250 = x3d.Material()

Appearance249.setMaterial(Material250)

Shape246.setAppearance(Appearance249)

Transform245.addChildren(Shape246)

Transform239.addChildren(Transform245)

Group238.addChildren(Transform239)
Transform251 = x3d.Transform()
Transform251.setDEF("TargetBoxDolly")
Transform251.setTranslation([-40,1,-20])
Shape252 = x3d.Shape()
Box253 = x3d.Box()

Shape252.setGeometry(Box253)
Appearance254 = x3d.Appearance()
Material255 = x3d.Material()

Appearance254.setMaterial(Material255)
ImageTexture256 = x3d.ImageTexture()
ImageTexture256.setUrl(["images/CameraMoveDolly.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveDolly.png"])

Appearance254.setTexture(ImageTexture256)

Shape252.setAppearance(Appearance254)

Transform251.addChildren(Shape252)
Transform257 = x3d.Transform()
Transform257.setTranslation([0,2,0])
Shape258 = x3d.Shape()
Text259 = x3d.Text()
Text259.setString(["Dolly left, right"])
FontStyle260 = x3d.FontStyle()
FontStyle260.setJustify(["MIDDLE","MIDDLE"])

Text259.setFontStyle(FontStyle260)

Shape258.setGeometry(Text259)
Appearance261 = x3d.Appearance()
Material262 = x3d.Material()

Appearance261.setMaterial(Material262)

Shape258.setAppearance(Appearance261)

Transform257.addChildren(Shape258)

Transform251.addChildren(Transform257)

Group238.addChildren(Transform251)
Transform263 = x3d.Transform()
Transform263.setDEF("TargetBoxPan")
Transform263.setTranslation([-30,1,-20])
Shape264 = x3d.Shape()
Box265 = x3d.Box()

Shape264.setGeometry(Box265)
Appearance266 = x3d.Appearance()
Material267 = x3d.Material()

Appearance266.setMaterial(Material267)
ImageTexture268 = x3d.ImageTexture()
ImageTexture268.setUrl(["images/CameraMovePan.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMovePan.png"])

Appearance266.setTexture(ImageTexture268)

Shape264.setAppearance(Appearance266)

Transform263.addChildren(Shape264)
Transform269 = x3d.Transform()
Transform269.setTranslation([0,2,0])
Shape270 = x3d.Shape()
Text271 = x3d.Text()
Text271.setString(["Pan left, right"])
FontStyle272 = x3d.FontStyle()
FontStyle272.setJustify(["MIDDLE","MIDDLE"])

Text271.setFontStyle(FontStyle272)

Shape270.setGeometry(Text271)
Appearance273 = x3d.Appearance()
Material274 = x3d.Material()

Appearance273.setMaterial(Material274)

Shape270.setAppearance(Appearance273)

Transform269.addChildren(Shape270)

Transform263.addChildren(Transform269)

Group238.addChildren(Transform263)
Transform275 = x3d.Transform()
Transform275.setDEF("TargetBoxBoom")
Transform275.setTranslation([-20,1,-20])
Shape276 = x3d.Shape()
Box277 = x3d.Box()

Shape276.setGeometry(Box277)
Appearance278 = x3d.Appearance()
Material279 = x3d.Material()

Appearance278.setMaterial(Material279)
ImageTexture280 = x3d.ImageTexture()
ImageTexture280.setUrl(["images/CameraMoveBoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveBoom.png"])

Appearance278.setTexture(ImageTexture280)

Shape276.setAppearance(Appearance278)

Transform275.addChildren(Shape276)
Transform281 = x3d.Transform()
Transform281.setTranslation([0,2,0])
Shape282 = x3d.Shape()
Text283 = x3d.Text()
Text283.setString(["Boom up, down"])
FontStyle284 = x3d.FontStyle()
FontStyle284.setJustify(["MIDDLE","MIDDLE"])

Text283.setFontStyle(FontStyle284)

Shape282.setGeometry(Text283)
Appearance285 = x3d.Appearance()
Material286 = x3d.Material()

Appearance285.setMaterial(Material286)

Shape282.setAppearance(Appearance285)

Transform281.addChildren(Shape282)

Transform275.addChildren(Transform281)

Group238.addChildren(Transform275)
Transform287 = x3d.Transform()
Transform287.setDEF("TargetBoxTilt")
Transform287.setTranslation([-10,1,-20])
Shape288 = x3d.Shape()
Box289 = x3d.Box()

Shape288.setGeometry(Box289)
Appearance290 = x3d.Appearance()
Material291 = x3d.Material()

Appearance290.setMaterial(Material291)
ImageTexture292 = x3d.ImageTexture()
ImageTexture292.setUrl(["images/CameraMoveTilt.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveTilt.png"])

Appearance290.setTexture(ImageTexture292)

Shape288.setAppearance(Appearance290)

Transform287.addChildren(Shape288)
Transform293 = x3d.Transform()
Transform293.setTranslation([0,2,0])
Shape294 = x3d.Shape()
Text295 = x3d.Text()
Text295.setString(["Tilt left, right"])
FontStyle296 = x3d.FontStyle()
FontStyle296.setJustify(["MIDDLE","MIDDLE"])

Text295.setFontStyle(FontStyle296)

Shape294.setGeometry(Text295)
Appearance297 = x3d.Appearance()
Material298 = x3d.Material()

Appearance297.setMaterial(Material298)

Shape294.setAppearance(Appearance297)

Transform293.addChildren(Shape294)

Transform287.addChildren(Transform293)

Group238.addChildren(Transform287)

Scene21.addChildren(Group238)
#=============== Camera.AimPointTest ==============
ProtoInstance299 = x3d.ProtoInstance()
ProtoInstance299.setName("Camera")
ProtoInstance299.setDEF("Camera.AimPointTest")
fieldValue300 = x3d.fieldValue()
fieldValue300.setName("description")
fieldValue300.setValue("AimPointTest for moving camera tracking moving target")

ProtoInstance299.addFieldValue(fieldValue300)
fieldValue301 = x3d.fieldValue()
fieldValue301.setName("position")
fieldValue301.setValue("4 4 10")

ProtoInstance299.addFieldValue(fieldValue301)
fieldValue302 = x3d.fieldValue()
fieldValue302.setName("shots")
ProtoInstance303 = x3d.ProtoInstance()
ProtoInstance303.setName("CameraShot")
ProtoInstance303.setDEF("Shot5")
fieldValue304 = x3d.fieldValue()
fieldValue304.setName("description")
fieldValue304.setValue("#3 Tracking shot")

ProtoInstance303.addFieldValue(fieldValue304)
fieldValue305 = x3d.fieldValue()
fieldValue305.setName("initialPosition")
fieldValue305.setValue("6 6 10")

ProtoInstance303.addFieldValue(fieldValue305)
fieldValue306 = x3d.fieldValue()
fieldValue306.setName("initialOrientation")
fieldValue306.setValue("0 1 0 0")

ProtoInstance303.addFieldValue(fieldValue306)
fieldValue307 = x3d.fieldValue()
fieldValue307.setName("moves")
ProtoInstance308 = x3d.ProtoInstance()
ProtoInstance308.setName("CameraMovement")
ProtoInstance308.setDEF("MoveAimPoint3.1")
fieldValue309 = x3d.fieldValue()
fieldValue309.setName("description")
fieldValue309.setValue("AimPoint 3.1 moving BoxPath")

ProtoInstance308.addFieldValue(fieldValue309)
fieldValue310 = x3d.fieldValue()
fieldValue310.setName("tracking")
fieldValue310.setValue("true")

ProtoInstance308.addFieldValue(fieldValue310)
fieldValue311 = x3d.fieldValue()
fieldValue311.setName("duration")
fieldValue311.setValue("8")

ProtoInstance308.addFieldValue(fieldValue311)
fieldValue312 = x3d.fieldValue()
fieldValue312.setName("goalPosition")
fieldValue312.setValue("6 6 10")

ProtoInstance308.addFieldValue(fieldValue312)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue307.addChildren(ProtoInstance308)
ProtoInstance313 = x3d.ProtoInstance()
ProtoInstance313.setName("CameraMovement")
ProtoInstance313.setDEF("MoveAimPoint3.2")
fieldValue314 = x3d.fieldValue()
fieldValue314.setName("description")
fieldValue314.setValue("AimPoint 3.2 pan right while tracking")

ProtoInstance313.addFieldValue(fieldValue314)
fieldValue315 = x3d.fieldValue()
fieldValue315.setName("tracking")
fieldValue315.setValue("true")

ProtoInstance313.addFieldValue(fieldValue315)
fieldValue316 = x3d.fieldValue()
fieldValue316.setName("duration")
fieldValue316.setValue("8")

ProtoInstance313.addFieldValue(fieldValue316)
fieldValue317 = x3d.fieldValue()
fieldValue317.setName("goalPosition")
fieldValue317.setValue("40 6 12")

ProtoInstance313.addFieldValue(fieldValue317)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue307.addChildren(ProtoInstance313)
ProtoInstance318 = x3d.ProtoInstance()
ProtoInstance318.setName("CameraMovement")
ProtoInstance318.setDEF("MoveAimPoint3.3")
fieldValue319 = x3d.fieldValue()
fieldValue319.setName("description")
fieldValue319.setValue("AimPoint 3.3 boom up while tracking")

ProtoInstance318.addFieldValue(fieldValue319)
fieldValue320 = x3d.fieldValue()
fieldValue320.setName("tracking")
fieldValue320.setValue("true")

ProtoInstance318.addFieldValue(fieldValue320)
fieldValue321 = x3d.fieldValue()
fieldValue321.setName("duration")
fieldValue321.setValue("3")

ProtoInstance318.addFieldValue(fieldValue321)
fieldValue322 = x3d.fieldValue()
fieldValue322.setName("goalPosition")
fieldValue322.setValue("40 20 13")

ProtoInstance318.addFieldValue(fieldValue322)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue307.addChildren(ProtoInstance318)
ProtoInstance323 = x3d.ProtoInstance()
ProtoInstance323.setName("CameraMovement")
ProtoInstance323.setDEF("MoveAimPoint3.4")
fieldValue324 = x3d.fieldValue()
fieldValue324.setName("description")
fieldValue324.setValue("AimPoint 3.4 restore camera back to home")

ProtoInstance323.addFieldValue(fieldValue324)
fieldValue325 = x3d.fieldValue()
fieldValue325.setName("tracking")
fieldValue325.setValue("true")

ProtoInstance323.addFieldValue(fieldValue325)
fieldValue326 = x3d.fieldValue()
fieldValue326.setName("duration")
fieldValue326.setValue("5")

ProtoInstance323.addFieldValue(fieldValue326)
fieldValue327 = x3d.fieldValue()
fieldValue327.setName("goalPosition")
fieldValue327.setValue("4 4 10")

ProtoInstance323.addFieldValue(fieldValue327)
fieldValue328 = x3d.fieldValue()
fieldValue328.setName("goalAimPoint")
fieldValue328.setValue("4 4 0")

ProtoInstance323.addFieldValue(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.setName("goalOrientation")
fieldValue329.setValue("0 1 0 0")

ProtoInstance323.addFieldValue(fieldValue329)
#can test tracking or not using following values

fieldValue307.addChildren(ProtoInstance323)

ProtoInstance303.addFieldValue(fieldValue307)

fieldValue302.addChildren(ProtoInstance303)

ProtoInstance299.addFieldValue(fieldValue302)

Scene21.addChildren(ProtoInstance299)
Group330 = x3d.Group()
Group330.setDEF("AnimationGroup.AimPointTest")
TimeSensor331 = x3d.TimeSensor()
TimeSensor331.setDEF("CameraTimer.AimPointTest")

Group330.addChildren(TimeSensor331)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE332 = x3d.ROUTE()
ROUTE332.setFromField("totalDuration")
ROUTE332.setFromNode("Camera.AimPointTest")
ROUTE332.setToField("cycleInterval")
ROUTE332.setToNode("CameraTimer.AimPointTest")

Group330.addChildren(ROUTE332)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE333 = x3d.ROUTE()
ROUTE333.setFromField("fraction_changed")
ROUTE333.setFromNode("CameraTimer.AimPointTest")
ROUTE333.setToField("set_fraction")
ROUTE333.setToNode("Camera.AimPointTest")

Group330.addChildren(ROUTE333)
Transform334 = x3d.Transform()
Transform334.setDEF("Trigger.AimPointTest")
Transform334.setTranslation([4,4,0])
BooleanFilter335 = x3d.BooleanFilter()
BooleanFilter335.setDEF("TextTouchActive.AimPointFilter")

Transform334.addChildren(BooleanFilter335)
TouchSensor336 = x3d.TouchSensor()
TouchSensor336.setDEF("TextTouch.AimPointTest")
TouchSensor336.setDescription("touch to animate Camera AimPointTest")

Transform334.addChildren(TouchSensor336)
ROUTE337 = x3d.ROUTE()
ROUTE337.setFromField("inputTrue")
ROUTE337.setFromNode("TextTouchActive.AimPointFilter")
ROUTE337.setToField("set_bind")
ROUTE337.setToNode("Camera.AimPointTest")

Transform334.addChildren(ROUTE337)
ROUTE338 = x3d.ROUTE()
ROUTE338.setFromField("isActive")
ROUTE338.setFromNode("TextTouch.AimPointTest")
ROUTE338.setToField("set_boolean")
ROUTE338.setToNode("TextTouchActive.AimPointFilter")

Transform334.addChildren(ROUTE338)
ROUTE339 = x3d.ROUTE()
ROUTE339.setFromField("touchTime")
ROUTE339.setFromNode("TextTouch.AimPointTest")
ROUTE339.setToField("startTime")
ROUTE339.setToNode("CameraTimer.AimPointTest")

Transform334.addChildren(ROUTE339)
Shape340 = x3d.Shape()
Text341 = x3d.Text()
Text341.setString(["Click to animate","AimPointTest"])
FontStyle342 = x3d.FontStyle()
FontStyle342.setJustify(["MIDDLE","MIDDLE"])

Text341.setFontStyle(FontStyle342)

Shape340.setGeometry(Text341)
Appearance343 = x3d.Appearance()
Material344 = x3d.Material()
Material344.setUSE("ArtDeco5")

Appearance343.setMaterial(Material344)

Shape340.setAppearance(Appearance343)

Transform334.addChildren(Shape340)
Shape345 = x3d.Shape()
Shape345.setUSE("TransparentBox")

Transform334.addChildren(Shape345)

Group330.addChildren(Transform334)

Scene21.addChildren(Group330)
#TODO build a test once implemented
ProtoInstance346 = x3d.ProtoInstance()
ProtoInstance346.setName("OfflineRender")

Scene21.addChildren(ProtoInstance346)
#=============== animate a camera shape to visualize view changes ==============
Transform347 = x3d.Transform()
Transform347.setDEF("CameraShapeTransform")
Transform347.setTranslation([0,0.5,0])
#move CameraShape using active Camera
ROUTE348 = x3d.ROUTE()
ROUTE348.setFromField("position_changed")
ROUTE348.setFromNode("Camera.SimpleShotsTest")
ROUTE348.setToField("translation")
ROUTE348.setToNode("CameraShapeTransform")

Transform347.addChildren(ROUTE348)
ROUTE349 = x3d.ROUTE()
ROUTE349.setFromField("orientation_changed")
ROUTE349.setFromNode("Camera.SimpleShotsTest")
ROUTE349.setToField("rotation")
ROUTE349.setToNode("CameraShapeTransform")

Transform347.addChildren(ROUTE349)
ROUTE350 = x3d.ROUTE()
ROUTE350.setFromField("position")
ROUTE350.setFromNode("Camera.AimPointTest")
ROUTE350.setToField("translation")
ROUTE350.setToNode("CameraShapeTransform")

Transform347.addChildren(ROUTE350)
ROUTE351 = x3d.ROUTE()
ROUTE351.setFromField("orientation_changed")
ROUTE351.setFromNode("Camera.AimPointTest")
ROUTE351.setToField("rotation")
ROUTE351.setToNode("CameraShapeTransform")

Transform347.addChildren(ROUTE351)
Transform352 = x3d.Transform()
Transform352.setDEF("CameraOffsetTransform")
Transform352.setTranslation([0,0,0.25])
TouchSensor353 = x3d.TouchSensor()
TouchSensor353.setDEF("CameraShapeTouched")

Transform352.addChildren(TouchSensor353)
Inline354 = x3d.Inline()
Inline354.setDEF("CameraShape")
Inline354.setUrl(["CameraShape.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraShape.x3d"])

Transform352.addChildren(Inline354)
Shape355 = x3d.Shape()
Shape355.setDEF("SightLine")
IndexedLineSet356 = x3d.IndexedLineSet()
IndexedLineSet356.setCoordIndex([0,1])
Coordinate357 = x3d.Coordinate()
Coordinate357.setPoint([0,0,0,0,0,-100])

IndexedLineSet356.setCoord(Coordinate357)

Shape355.setGeometry(IndexedLineSet356)
Appearance358 = x3d.Appearance()
Material359 = x3d.Material()
Material359.setEmissiveColor([0.8,0.8,0.4])

Appearance358.setMaterial(Material359)

Shape355.setAppearance(Appearance358)

Transform352.addChildren(Shape355)

Transform347.addChildren(Transform352)
#Display frustum to show camera view within the scene, toggled by user selecting CameraShape
ExternProtoDeclare360 = x3d.ExternProtoDeclare()
ExternProtoDeclare360.setName("ViewFrustum")
ExternProtoDeclare360.setAppinfo("Display view frustum associated with a given pair of Viewpoint NavigationInfo nodes")
ExternProtoDeclare360.setUrl(["../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum"])
field361 = x3d.field()
field361.setName("ViewpointNode")
field361.setAccessType("initializeOnly")
field361.setAppinfo("required: insert Viewpoint DEF or USE node for view of interest")
field361.setType("SFNode")

ExternProtoDeclare360.addField(field361)
field362 = x3d.field()
field362.setName("NavigationInfoNode")
field362.setAccessType("initializeOnly")
field362.setAppinfo("required: insert NavigationInfo DEF or USE node of interest")
field362.setType("SFNode")

ExternProtoDeclare360.addField(field362)
field363 = x3d.field()
field363.setName("visible")
field363.setAccessType("inputOutput")
field363.setAppinfo("whether or not frustum geometry is rendered")
field363.setType("SFBool")

ExternProtoDeclare360.addField(field363)
field364 = x3d.field()
field364.setName("lineColor")
field364.setAccessType("inputOutput")
field364.setAppinfo("RGB color of ViewFrustum outline, default value 0.9 0.9 0.9")
field364.setType("SFColor")

ExternProtoDeclare360.addField(field364)
field365 = x3d.field()
field365.setName("frustumColor")
field365.setAccessType("inputOutput")
field365.setAppinfo("RGB color of ViewFrustum hull geometry, default value 0.8 0.8 0.8")
field365.setType("SFColor")

ExternProtoDeclare360.addField(field365)
field366 = x3d.field()
field366.setName("transparency")
field366.setAccessType("inputOutput")
field366.setAppinfo("transparency of ViewFrustum hull geometry, default value 0.5")
field366.setType("SFFloat")

ExternProtoDeclare360.addField(field366)
field367 = x3d.field()
field367.setName("aspectRatio")
field367.setAccessType("inputOutput")
field367.setAppinfo("assumed ratio height/width, default value 0.75")
field367.setType("SFFloat")

ExternProtoDeclare360.addField(field367)
field368 = x3d.field()
field368.setName("trace")
field368.setAccessType("initializeOnly")
field368.setAppinfo("debug support, default false")
field368.setType("SFBool")

ExternProtoDeclare360.addField(field368)

Transform347.addChildren(ExternProtoDeclare360)
ProtoInstance369 = x3d.ProtoInstance()
ProtoInstance369.setName("ViewFrustum")
ProtoInstance369.setDEF("ViewFrustumNode")
fieldValue370 = x3d.fieldValue()
fieldValue370.setName("ViewpointNode")
Viewpoint371 = x3d.Viewpoint()
Viewpoint371.setDEF("FrustumViewpoint")
Viewpoint371.setDescription("viewpoint for ViewFrustum")
Viewpoint371.setPosition([0,0,0])

fieldValue370.addChildren(Viewpoint371)

ProtoInstance369.addFieldValue(fieldValue370)
fieldValue372 = x3d.fieldValue()
fieldValue372.setName("NavigationInfoNode")
NavigationInfo373 = x3d.NavigationInfo()
NavigationInfo373.setDEF("TestNavigationInfo")
NavigationInfo373.setTransitionType(["ANIMATE"])
NavigationInfo373.setVisibilityLimit(100)

fieldValue372.addChildren(NavigationInfo373)

ProtoInstance369.addFieldValue(fieldValue372)
fieldValue374 = x3d.fieldValue()
fieldValue374.setName("visible")
fieldValue374.setValue("false")

ProtoInstance369.addFieldValue(fieldValue374)
fieldValue375 = x3d.fieldValue()
fieldValue375.setName("lineColor")
fieldValue375.setValue("0.9 0.9 0.9")

ProtoInstance369.addFieldValue(fieldValue375)
fieldValue376 = x3d.fieldValue()
fieldValue376.setName("frustumColor")
fieldValue376.setValue("0.8 0.8 0.8")

ProtoInstance369.addFieldValue(fieldValue376)
fieldValue377 = x3d.fieldValue()
fieldValue377.setName("transparency")
fieldValue377.setValue("0.95")

ProtoInstance369.addFieldValue(fieldValue377)

Transform347.addChildren(ProtoInstance369)
BooleanToggle378 = x3d.BooleanToggle()
BooleanToggle378.setDEF("ViewFrustumToggle")

Transform347.addChildren(BooleanToggle378)
ROUTE379 = x3d.ROUTE()
ROUTE379.setFromField("isActive")
ROUTE379.setFromNode("CameraShapeTouched")
ROUTE379.setToField("set_boolean")
ROUTE379.setToNode("ViewFrustumToggle")

Transform347.addChildren(ROUTE379)
ROUTE380 = x3d.ROUTE()
ROUTE380.setFromField("toggle")
ROUTE380.setFromNode("ViewFrustumToggle")
ROUTE380.setToField("set_visible")
ROUTE380.setToNode("ViewFrustumNode")

Transform347.addChildren(ROUTE380)

Scene21.addChildren(Transform347)
#=============== add checkerboard, axes and other things to look at while animating ==============
Background381 = x3d.Background()
Background381.setSkyColor([0.282353,0.380392,0.470588])

Scene21.addChildren(Background381)
Transform382 = x3d.Transform()
Transform382.setRotation([1,0,0,-1.57079])
Transform382.setScale([10,10,10])
Shape383 = x3d.Shape()
Appearance384 = x3d.Appearance()
Material385 = x3d.Material()
Material385.setAmbientIntensity(0.01)
Material385.setDiffuseColor([1,1,1])
Material385.setShininess(0.05)

Appearance384.setMaterial(Material385)

Shape383.setAppearance(Appearance384)
IndexedFaceSet386 = x3d.IndexedFaceSet()
IndexedFaceSet386.setColorIndex([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0])
IndexedFaceSet386.setColorPerVertex(False)
IndexedFaceSet386.setCoordIndex([0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1])
IndexedFaceSet386.setNormalPerVertex(False)
IndexedFaceSet386.setSolid(False)
Coordinate387 = x3d.Coordinate()
Coordinate387.setPoint([-5.25,5.25,0,-3.75,5.25,0,-2.25,5.25,0,-0.75,5.25,0,0.75,5.25,0,2.25,5.25,0,3.75,5.25,0,5.25,5.25,0,-5.25,3.75,0,-3.75,3.75,0,-2.25,3.75,0,-0.75,3.75,0,0.75,3.75,0,2.25,3.75,0,3.75,3.75,0,5.25,3.75,0,-5.25,2.25,0,-3.75,2.25,0,-2.25,2.25,0,-0.75,2.25,0,0.75,2.25,0,2.25,2.25,0,3.75,2.25,0,5.25,2.25,0,-5.25,0.75,0,-3.75,0.75,0,-2.25,0.75,0,-0.75,0.75,0,0.75,0.75,0,2.25,0.75,0,3.75,0.75,0,5.25,0.75,0,-5.25,-0.75,0,-3.75,-0.75,0,-2.25,-0.75,0,-0.75,-0.75,0,0.75,-0.75,0,2.25,-0.75,0,3.75,-0.75,0,5.25,-0.75,0,-5.25,-2.25,0,-3.75,-2.25,0,-2.25,-2.25,0,-0.75,-2.25,0,0.75,-2.25,0,2.25,-2.25,0,3.75,-2.25,0,5.25,-2.25,0,-5.25,-3.75,0,-3.75,-3.75,0,-2.25,-3.75,0,-0.75,-3.75,0,0.75,-3.75,0,2.25,-3.75,0,3.75,-3.75,0,5.25,-3.75,0,-5.25,-5.25,0,-3.75,-5.25,0,-2.25,-5.25,0,-0.75,-5.25,0,0.75,-5.25,0,2.25,-5.25,0,3.75,-5.25,0,5.25,-5.25,0])

IndexedFaceSet386.setCoord(Coordinate387)
Color388 = x3d.Color()
Color388.setColor([0.435294,0.741176,0,0,0.560784,0.580392])

IndexedFaceSet386.setColor(Color388)

Shape383.setGeometry(IndexedFaceSet386)

Transform382.addChildren(Shape383)

Scene21.addChildren(Transform382)
Transform389 = x3d.Transform()
Transform389.setScale([3,3,3])
Transform389.setTranslation([0,0.25,0])
Inline390 = x3d.Inline()
Inline390.setDEF("CoordinateAxes")
Inline390.setUrl(["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../Savage/Tools/Authoring/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../Savage/Tools/Authoring/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"])

Transform389.addChildren(Inline390)

Scene21.addChildren(Transform389)
Transform391 = x3d.Transform()
Transform391.setDEF("MovingBoxTransform")
PositionInterpolator392 = x3d.PositionInterpolator()
PositionInterpolator392.setDEF("BoxPath")
PositionInterpolator392.setKey([0,0.25,0.5,0.75,1])
PositionInterpolator392.setKeyValue([-5,1,5,45,1,5,45,1,-45,-5,1,-45,-5,1,5])

Transform391.addChildren(PositionInterpolator392)
TimeSensor393 = x3d.TimeSensor()
TimeSensor393.setDEF("BoxTimer")
TimeSensor393.setCycleInterval(10)
TimeSensor393.setLoop(True)

Transform391.addChildren(TimeSensor393)
ROUTE394 = x3d.ROUTE()
ROUTE394.setFromField("value_changed")
ROUTE394.setFromNode("BoxPath")
ROUTE394.setToField("translation")
ROUTE394.setToNode("MovingBoxTransform")

Transform391.addChildren(ROUTE394)
ROUTE395 = x3d.ROUTE()
ROUTE395.setFromField("value_changed")
ROUTE395.setFromNode("BoxPath")
ROUTE395.setToField("goalAimPoint")
ROUTE395.setToNode("MoveAimPoint3.1")

Transform391.addChildren(ROUTE395)
ROUTE396 = x3d.ROUTE()
ROUTE396.setFromField("value_changed")
ROUTE396.setFromNode("BoxPath")
ROUTE396.setToField("goalAimPoint")
ROUTE396.setToNode("MoveAimPoint3.2")

Transform391.addChildren(ROUTE396)
ROUTE397 = x3d.ROUTE()
ROUTE397.setFromField("value_changed")
ROUTE397.setFromNode("BoxPath")
ROUTE397.setToField("goalAimPoint")
ROUTE397.setToNode("MoveAimPoint3.3")

Transform391.addChildren(ROUTE397)
ROUTE398 = x3d.ROUTE()
ROUTE398.setFromField("fraction_changed")
ROUTE398.setFromNode("BoxTimer")
ROUTE398.setToField("set_fraction")
ROUTE398.setToNode("BoxPath")

Transform391.addChildren(ROUTE398)
Shape399 = x3d.Shape()
Box400 = x3d.Box()

Shape399.setGeometry(Box400)
Appearance401 = x3d.Appearance()
Material402 = x3d.Material()

Appearance401.setMaterial(Material402)
ImageTexture403 = x3d.ImageTexture()
ImageTexture403.setUrl(["../earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png"])

Appearance401.setTexture(ImageTexture403)

Shape399.setAppearance(Appearance401)

Transform391.addChildren(Shape399)

Scene21.addChildren(Transform391)
#================ CrossHair visualization for center of screen ================
ExternProtoDeclare404 = x3d.ExternProtoDeclare()
ExternProtoDeclare404.setName("CrossHair")
ExternProtoDeclare404.setAppinfo("CrossHair prototype provides a heads-up display (HUD) crosshair at the view center, which is useful for assessing NavigationInfo lookAt point")
ExternProtoDeclare404.setUrl(["../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair"])
field405 = x3d.field()
field405.setName("enabled")
field405.setAccessType("initializeOnly")
field405.setAppinfo("whether CrissHair orititype is enabled or not")
field405.setType("SFBool")

ExternProtoDeclare404.addField(field405)
field406 = x3d.field()
field406.setName("set_enabled")
field406.setAccessType("inputOnly")
field406.setAppinfo("control whether enabled/disabled")
field406.setType("SFBool")

ExternProtoDeclare404.addField(field406)
field407 = x3d.field()
field407.setName("markerColor")
field407.setAccessType("inputOutput")
field407.setAppinfo("color of CrossHair marker")
field407.setType("SFColor")

ExternProtoDeclare404.addField(field407)
field408 = x3d.field()
field408.setName("scale")
field408.setAccessType("inputOutput")
field408.setAppinfo("size of CrossHair in meters")
field408.setType("SFVec3f")

ExternProtoDeclare404.addField(field408)
field409 = x3d.field()
field409.setName("positionOffsetFromCamera")
field409.setAccessType("inputOutput")
field409.setAppinfo("distance in front of HUD viewpoint")
field409.setType("SFVec3f")

ExternProtoDeclare404.addField(field409)

Scene21.addChildren(ExternProtoDeclare404)
ProtoInstance410 = x3d.ProtoInstance()
ProtoInstance410.setName("CrossHair")
ProtoInstance410.setDEF("CrossHairInstance")
fieldValue411 = x3d.fieldValue()
fieldValue411.setName("enabled")
fieldValue411.setValue("true")

ProtoInstance410.addFieldValue(fieldValue411)
fieldValue412 = x3d.fieldValue()
fieldValue412.setName("markerColor")
fieldValue412.setValue("1 0.5 0")

ProtoInstance410.addFieldValue(fieldValue412)
fieldValue413 = x3d.fieldValue()
fieldValue413.setName("scale")
fieldValue413.setValue("1 1 1")

ProtoInstance410.addFieldValue(fieldValue413)
fieldValue414 = x3d.fieldValue()
fieldValue414.setName("positionOffsetFromCamera")
fieldValue414.setValue("0 0 -6")

ProtoInstance410.addFieldValue(fieldValue414)

Scene21.addChildren(ProtoInstance410)
#turn on CrossHairInstance when animated camera viewpoints are bound
ROUTE415 = x3d.ROUTE()
ROUTE415.setFromField("isBound")
ROUTE415.setFromNode("Camera.SimpleShotsTest")
ROUTE415.setToField("set_enabled")
ROUTE415.setToNode("CrossHairInstance")

Scene21.addChildren(ROUTE415)
ROUTE416 = x3d.ROUTE()
ROUTE416.setFromField("isBound")
ROUTE416.setFromNode("Camera.AimPointTest")
ROUTE416.setToField("set_enabled")
ROUTE416.setToNode("CrossHairInstance")

Scene21.addChildren(ROUTE416)
#turn off CrossHairInstance when animated camera viewpoints are unbound <BooleanFilter DEF='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.SimpleShotsTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.AimPointTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='inputNegate' fromNode='NegateCrossHair' toField='set_enabled' toNode='CrossHairInstance'/>
#=============== TODO Launch Prototype Example ==============
Anchor417 = x3d.Anchor()
Anchor417.setDescription("launch CameraExample scene")
Anchor417.setParameter(["target=_blank"])
Anchor417.setUrl(["CameraExample.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.x3d","CameraExample.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.wrl"])
Transform418 = x3d.Transform()
Transform418.setTranslation([0,-3,0])
Shape419 = x3d.Shape()
Text420 = x3d.Text()
Text420.setString(["CameraPrototype","defines a prototype","","Click on this text to see","CameraExample scene"])
FontStyle421 = x3d.FontStyle()
FontStyle421.setJustify(["MIDDLE","MIDDLE"])
FontStyle421.setSize(0.5)

Text420.setFontStyle(FontStyle421)

Shape419.setGeometry(Text420)
Appearance422 = x3d.Appearance()
Material423 = x3d.Material()
Material423.setDiffuseColor([1,1,0.2])

Appearance422.setMaterial(Material423)

Shape419.setAppearance(Appearance422)

Transform418.addChildren(Shape419)

Anchor417.addChildren(Transform418)

Scene21.addChildren(Anchor417)

X3D0.setScene(Scene21)
X3D0.toFileX3D("././CameraExamples_RoundTrip.x3d")
