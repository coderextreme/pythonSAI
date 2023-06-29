print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "CameraExamples.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Camera, CameraShot and CameraMove examples that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "documentation"
meta4.content = "Two demos are found in the scene, click the \"red text\" on left or right to start. (a) SimpleShotsTest shows Zoom in/out, Pan left/right, Boom up/down, Tilt left/right, with each is defined by a CameraShot collecting a series of CameraMovements. (b) AimPointTest gradually slews the camera view to look at the sliding cube, then follows it around before returning to original viewpoint."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Don Brutzman and Jeff Weekley"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "18 June 2009"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "20 January 2020"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "TODO"
meta8.content = "Schematron rules, backed up by initialize() checks"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "BeyondViewpointCameraNodesWeb3D2009.pdf"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "MovingImage"
meta10.content = "CameraExamplesDemo.mp4"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "https://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "subject"
meta12.content = "Camera nodes for Viewpoint navigation control"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "CameraPrototypes.x3d"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "CameraExamplesConsoleLog.txt"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.avi"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "https://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "identifier"
meta17.content = "https://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "generator"
meta19.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "license"
meta20.content = "../license.html"

head1.children.append(meta20)

X3D0.head = head1
Scene21 = x3d.Scene()
#=============== Camera ==============
WorldInfo22 = x3d.WorldInfo()
WorldInfo22.title = "CameraExamples.x3d"

Scene21.children.append(WorldInfo22)
ExternProtoDeclare23 = x3d.ExternProtoDeclare()
ExternProtoDeclare23.name = "Camera"
ExternProtoDeclare23.appinfo = "Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images"
ExternProtoDeclare23.url = ["CameraPrototypes.x3d#Camera","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#Camera","CameraPrototypes.wrl#Camera","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#Camera"]
field24 = x3d.field()
field24.name = "description"
field24.accessType = "inputOutput"
field24.appinfo = "Text description to be displayed for this Camera"
field24.type = "SFString"

ExternProtoDeclare23.field.append(field24)
field25 = x3d.field()
field25.name = "position"
field25.accessType = "inputOutput"
field25.appinfo = "Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field25.type = "SFVec3f"

ExternProtoDeclare23.field.append(field25)
field26 = x3d.field()
field26.name = "orientation"
field26.accessType = "inputOutput"
field26.appinfo = "Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated"
field26.type = "SFRotation"

ExternProtoDeclare23.field.append(field26)
field27 = x3d.field()
field27.name = "fieldOfView"
field27.accessType = "inputOutput"
field27.appinfo = "pi/4"
field27.type = "SFFloat"

ExternProtoDeclare23.field.append(field27)
field28 = x3d.field()
field28.name = "set_fraction"
field28.accessType = "inputOnly"
field28.appinfo = "input fraction drives interpolators"
field28.type = "SFFloat"

ExternProtoDeclare23.field.append(field28)
field29 = x3d.field()
field29.name = "set_bind"
field29.accessType = "inputOnly"
field29.appinfo = "input event binds or unbinds this Camera"
field29.type = "SFBool"

ExternProtoDeclare23.field.append(field29)
field30 = x3d.field()
field30.name = "bindTime"
field30.accessType = "outputOnly"
field30.appinfo = "output event indicates when this Camera is bound"
field30.type = "SFTime"

ExternProtoDeclare23.field.append(field30)
field31 = x3d.field()
field31.name = "isBound"
field31.accessType = "outputOnly"
field31.appinfo = "output event indicates whether this Camera is bound or unbound"
field31.type = "SFBool"

ExternProtoDeclare23.field.append(field31)
field32 = x3d.field()
field32.name = "nearClipPlane"
field32.accessType = "inputOutput"
field32.appinfo = "Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]"
field32.type = "SFFloat"

ExternProtoDeclare23.field.append(field32)
field33 = x3d.field()
field33.name = "farClipPlane"
field33.accessType = "inputOutput"
field33.appinfo = "Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit"
field33.type = "SFFloat"

ExternProtoDeclare23.field.append(field33)
field34 = x3d.field()
field34.name = "shots"
field34.accessType = "inputOutput"
field34.appinfo = "Array of CameraShot nodes which in turn contain CameraMovement nodes"
field34.type = "MFNode"

ExternProtoDeclare23.field.append(field34)
field35 = x3d.field()
field35.name = "headlight"
field35.accessType = "inputOutput"
field35.appinfo = "Whether camera headlight is on or off"
field35.type = "SFBool"

ExternProtoDeclare23.field.append(field35)
field36 = x3d.field()
field36.name = "headlightColor"
field36.accessType = "inputOutput"
field36.appinfo = "Camera headlight color"
field36.type = "SFColor"

ExternProtoDeclare23.field.append(field36)
field37 = x3d.field()
field37.name = "headlightIntensity"
field37.accessType = "inputOutput"
field37.appinfo = "Camera headlight intensity"
field37.type = "SFFloat"

ExternProtoDeclare23.field.append(field37)
field38 = x3d.field()
field38.name = "filterColor"
field38.accessType = "inputOutput"
field38.appinfo = "Camera filter color that modifies virtual lens capture"
field38.type = "SFColor"

ExternProtoDeclare23.field.append(field38)
field39 = x3d.field()
field39.name = "filterTransparency"
field39.accessType = "inputOutput"
field39.appinfo = "Camera filter transparency that modifies virtual lens capture"
field39.type = "SFFloat"

ExternProtoDeclare23.field.append(field39)
field40 = x3d.field()
field40.name = "upVector"
field40.accessType = "inputOutput"
field40.appinfo = "upVector changes modify camera orientation (and possibly vice versa)"
field40.type = "SFVec3f"

ExternProtoDeclare23.field.append(field40)
field41 = x3d.field()
field41.name = "fStop"
field41.accessType = "inputOutput"
field41.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field41.type = "SFFloat"

ExternProtoDeclare23.field.append(field41)
field42 = x3d.field()
field42.name = "focusDistance"
field42.accessType = "inputOutput"
field42.appinfo = "Distance to focal plane of sharpest focus"
field42.type = "SFFloat"

ExternProtoDeclare23.field.append(field42)
field43 = x3d.field()
field43.name = "isActive"
field43.accessType = "outputOnly"
field43.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field43.type = "SFBool"

ExternProtoDeclare23.field.append(field43)
field44 = x3d.field()
field44.name = "totalDuration"
field44.accessType = "outputOnly"
field44.appinfo = "Total duration of contained enabled CameraShot (and thus CameraMovement) move durations"
field44.type = "SFTime"

ExternProtoDeclare23.field.append(field44)
field45 = x3d.field()
field45.name = "offlineRender"
field45.accessType = "inputOutput"
field45.appinfo = "OfflineRender node"
field45.type = "SFNode"

ExternProtoDeclare23.field.append(field45)
field46 = x3d.field()
field46.name = "traceEnabled"
field46.accessType = "initializeOnly"
field46.appinfo = "enable console output to trace script computations and prototype progress"
field46.type = "SFBool"

ExternProtoDeclare23.field.append(field46)
#Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields

Scene21.children.append(ExternProtoDeclare23)
#=============== CameraShot ==============
ExternProtoDeclare47 = x3d.ExternProtoDeclare()
ExternProtoDeclare47.name = "CameraShot"
ExternProtoDeclare47.appinfo = "CameraShot collects a specific set of CameraMovement animations that make up an individual shot"
ExternProtoDeclare47.url = ["CameraPrototypes.x3d#CameraShot","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraShot","CameraPrototypes.wrl#CameraShot","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraShot"]
field48 = x3d.field()
field48.name = "description"
field48.accessType = "inputOutput"
field48.appinfo = "Text description to be displayed for this CameraShot"
field48.type = "SFString"

ExternProtoDeclare47.field.append(field48)
field49 = x3d.field()
field49.name = "enabled"
field49.accessType = "inputOutput"
field49.appinfo = "Whether this CameraShot can be activated"
field49.type = "SFBool"

ExternProtoDeclare47.field.append(field49)
field50 = x3d.field()
field50.name = "moves"
field50.accessType = "inputOutput"
field50.appinfo = "Set of CameraMovement nodes"
field50.type = "MFNode"
#initializing CameraMovement nodes are inserted here by scene author using ProtoInstance

ExternProtoDeclare47.field.append(field50)
field51 = x3d.field()
field51.name = "initialPosition"
field51.accessType = "inputOutput"
field51.appinfo = "Setup to reinitialize camera position for this shot"
field51.type = "SFVec3f"

ExternProtoDeclare47.field.append(field51)
field52 = x3d.field()
field52.name = "initialOrientation"
field52.accessType = "inputOutput"
field52.appinfo = "Setup to reinitialize camera rotation for this shot"
field52.type = "SFRotation"

ExternProtoDeclare47.field.append(field52)
field53 = x3d.field()
field53.name = "initialAimPoint"
field53.accessType = "inputOutput"
field53.appinfo = "Setup to reinitialize aimpoint (relative location for camera direction) for this shot"
field53.type = "SFVec3f"

ExternProtoDeclare47.field.append(field53)
field54 = x3d.field()
field54.name = "initialFieldOfView"
field54.accessType = "inputOutput"
field54.appinfo = "pi/4"
field54.type = "SFFloat"

ExternProtoDeclare47.field.append(field54)
field55 = x3d.field()
field55.name = "initialFStop"
field55.accessType = "inputOutput"
field55.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field55.type = "SFFloat"

ExternProtoDeclare47.field.append(field55)
field56 = x3d.field()
field56.name = "initialFocusDistance"
field56.accessType = "inputOutput"
field56.appinfo = "Distance to focal plane of sharpest focus"
field56.type = "SFFloat"

ExternProtoDeclare47.field.append(field56)
field57 = x3d.field()
field57.name = "shotDuration"
field57.accessType = "outputOnly"
field57.appinfo = "Subtotal duration of contained CameraMovement move durations"
field57.type = "SFTime"

ExternProtoDeclare47.field.append(field57)
field58 = x3d.field()
field58.name = "isActive"
field58.accessType = "outputOnly"
field58.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field58.type = "SFBool"

ExternProtoDeclare47.field.append(field58)
field59 = x3d.field()
field59.name = "traceEnabled"
field59.accessType = "initializeOnly"
field59.appinfo = "enable console output to trace script computations and prototype progress"
field59.type = "SFBool"

ExternProtoDeclare47.field.append(field59)

Scene21.children.append(ExternProtoDeclare47)
#=============== CameraMovement ==============
ExternProtoDeclare60 = x3d.ExternProtoDeclare()
ExternProtoDeclare60.name = "CameraMovement"
ExternProtoDeclare60.appinfo = "CameraMovement defines a single camera movement animation"
ExternProtoDeclare60.url = ["CameraPrototypes.x3d#CameraMovement","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraMovement","CameraPrototypes.wrl#CameraMovement","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraMovement"]
field61 = x3d.field()
field61.name = "description"
field61.accessType = "inputOutput"
field61.appinfo = "Text description to be displayed for this CameraMovement"
field61.type = "SFString"

ExternProtoDeclare60.field.append(field61)
field62 = x3d.field()
field62.name = "enabled"
field62.accessType = "inputOutput"
field62.appinfo = "Whether this CameraMovement can be activated"
field62.type = "SFBool"

ExternProtoDeclare60.field.append(field62)
field63 = x3d.field()
field63.name = "duration"
field63.accessType = "inputOutput"
field63.appinfo = "Duration in seconds for this move"
field63.type = "SFFloat"

ExternProtoDeclare60.field.append(field63)
field64 = x3d.field()
field64.name = "goalPosition"
field64.accessType = "inputOutput"
field64.appinfo = "Goal camera position for this move"
field64.type = "SFVec3f"

ExternProtoDeclare60.field.append(field64)
field65 = x3d.field()
field65.name = "goalOrientation"
field65.accessType = "inputOutput"
field65.appinfo = "Goal camera rotation for this move"
field65.type = "SFRotation"

ExternProtoDeclare60.field.append(field65)
field66 = x3d.field()
field66.name = "tracking"
field66.accessType = "inputOutput"
field66.appinfo = "Whether or not camera direction is tracking towards the aimPoint"
field66.type = "SFBool"

ExternProtoDeclare60.field.append(field66)
field67 = x3d.field()
field67.name = "goalAimPoint"
field67.accessType = "inputOutput"
field67.appinfo = "Goal aimPoint for this move, ignored if tracking=false"
field67.type = "SFVec3f"

ExternProtoDeclare60.field.append(field67)
field68 = x3d.field()
field68.name = "goalFieldOfView"
field68.accessType = "inputOutput"
field68.appinfo = "Goal fieldOfView for this move"
field68.type = "SFFloat"

ExternProtoDeclare60.field.append(field68)
field69 = x3d.field()
field69.name = "goalFStop"
field69.accessType = "inputOutput"
field69.appinfo = "Focal length divided effective aperture diameter indicating width of focal plane"
field69.type = "SFFloat"

ExternProtoDeclare60.field.append(field69)
field70 = x3d.field()
field70.name = "goalFocusDistance"
field70.accessType = "inputOutput"
field70.appinfo = "Distance to focal plane of sharpest focus"
field70.type = "SFFloat"

ExternProtoDeclare60.field.append(field70)
field71 = x3d.field()
field71.name = "isActive"
field71.accessType = "outputOnly"
field71.appinfo = "Mark start/stop with true/false output respectively useful to trigger external animations"
field71.type = "SFBool"

ExternProtoDeclare60.field.append(field71)
field72 = x3d.field()
field72.name = "traceEnabled"
field72.accessType = "initializeOnly"
field72.appinfo = "enable console output to trace script computations and prototype progress"
field72.type = "SFBool"

ExternProtoDeclare60.field.append(field72)

Scene21.children.append(ExternProtoDeclare60)
#=============== OfflineRender ==============
ExternProtoDeclare73 = x3d.ExternProtoDeclare()
ExternProtoDeclare73.name = "OfflineRender"
ExternProtoDeclare73.appinfo = "OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)"
ExternProtoDeclare73.url = ["CameraPrototypes.x3d#OfflineRender","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#OfflineRender","CameraPrototypes.wrl#OfflineRender","https://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#OfflineRender"]
field74 = x3d.field()
field74.name = "description"
field74.accessType = "inputOutput"
field74.appinfo = "Text description to be displayed for this OfflineRender"
field74.type = "SFString"

ExternProtoDeclare73.field.append(field74)
field75 = x3d.field()
field75.name = "enabled"
field75.accessType = "inputOutput"
field75.appinfo = "Whether this OfflineRender can be activated"
field75.type = "SFBool"

ExternProtoDeclare73.field.append(field75)
field76 = x3d.field()
field76.name = "frameRate"
field76.accessType = "inputOutput"
field76.appinfo = "Frames per second recorded for this rendering"
field76.type = "SFFloat"

ExternProtoDeclare73.field.append(field76)
field77 = x3d.field()
field77.name = "frameSize"
field77.accessType = "inputOutput"
field77.appinfo = "Size of frame in number of pixels width and height"
field77.type = "SFVec2f"

ExternProtoDeclare73.field.append(field77)
field78 = x3d.field()
field78.name = "pixelAspectRatio"
field78.accessType = "inputOutput"
field78.appinfo = "Relative dimensions of pixel height/width typically 1.33 or 1"
field78.type = "SFFloat"

ExternProtoDeclare73.field.append(field78)
field79 = x3d.field()
field79.name = "set_startTime"
field79.accessType = "inputOnly"
field79.appinfo = "Begin render operation"
field79.type = "SFTime"

ExternProtoDeclare73.field.append(field79)
field80 = x3d.field()
field80.name = "progress"
field80.accessType = "outputOnly"
field80.appinfo = "Progress performing render operation (0..1)"
field80.type = "SFFloat"

ExternProtoDeclare73.field.append(field80)
field81 = x3d.field()
field81.name = "renderCompleteTime"
field81.accessType = "outputOnly"
field81.appinfo = "Render operation complete"
field81.type = "SFTime"

ExternProtoDeclare73.field.append(field81)
field82 = x3d.field()
field82.name = "movieFormat"
field82.accessType = "initializeOnly"
field82.appinfo = "Format of rendered output movie (mpeg mp4 etc.), use first supported format"
field82.type = "MFString"

ExternProtoDeclare73.field.append(field82)
field83 = x3d.field()
field83.name = "imageFormat"
field83.accessType = "initializeOnly"
field83.appinfo = "Format of rendered output images (png jpeg gif tiff etc.) use first supported format"
field83.type = "MFString"

ExternProtoDeclare73.field.append(field83)
field84 = x3d.field()
field84.name = "traceEnabled"
field84.accessType = "initializeOnly"
field84.appinfo = "enable console output to trace script computations and prototype progress"
field84.type = "SFBool"

ExternProtoDeclare73.field.append(field84)
#TODO non-photorealistic rendering (NPR) parameters

Scene21.children.append(ExternProtoDeclare73)
#=============== Lights, camera, action! ==============
DirectionalLight85 = x3d.DirectionalLight()
DirectionalLight85.direction = [0,-1,0]
DirectionalLight85.global = True
DirectionalLight85.intensity = 0.8

Scene21.children.append(DirectionalLight85)
NavigationInfo86 = x3d.NavigationInfo()
NavigationInfo86.type = ["EXAMINE","FLY","ANY"]

Scene21.children.append(NavigationInfo86)
Viewpoint87 = x3d.Viewpoint()
Viewpoint87.description = "Camera test scene entry view"
Viewpoint87.position = [0,2,12]

Scene21.children.append(Viewpoint87)
Viewpoint88 = x3d.Viewpoint()
Viewpoint88.description = "Camera test scene from above"
Viewpoint88.orientation = [1,0,0,-1.57079]
Viewpoint88.position = [0,150,0]

Scene21.children.append(Viewpoint88)
#Keep prototype instances in same file while developing, then move later
#We will create examples matching those in the paper
#=============== Camera.SimpleShotsTest ==============
ProtoInstance89 = x3d.ProtoInstance()
ProtoInstance89.name = "Camera"
ProtoInstance89.DEF = "Camera.SimpleShotsTest"
fieldValue90 = x3d.fieldValue()
fieldValue90.name = "description"
fieldValue90.value = "SimpleShotsTest for camera Zoom Dolly Pan Boom and Tilt"

ProtoInstance89.fieldValue.append(fieldValue90)
fieldValue91 = x3d.fieldValue()
fieldValue91.name = "headlight"
fieldValue91.value = "true"

ProtoInstance89.fieldValue.append(fieldValue91)
fieldValue92 = x3d.fieldValue()
fieldValue92.name = "position"
fieldValue92.value = "-4 4 10"

ProtoInstance89.fieldValue.append(fieldValue92)
fieldValue93 = x3d.fieldValue()
fieldValue93.name = "shots"
ProtoInstance94 = x3d.ProtoInstance()
ProtoInstance94.name = "CameraShot"
ProtoInstance94.DEF = "Zoom"
fieldValue95 = x3d.fieldValue()
fieldValue95.name = "description"
fieldValue95.value = "Simple shot of Camera Zoom"

ProtoInstance94.fieldValue.append(fieldValue95)
fieldValue96 = x3d.fieldValue()
fieldValue96.name = "initialPosition"
fieldValue96.value = "-50 1 -10"

ProtoInstance94.fieldValue.append(fieldValue96)
fieldValue97 = x3d.fieldValue()
fieldValue97.name = "initialOrientation"
fieldValue97.value = "0 1 0 0"

ProtoInstance94.fieldValue.append(fieldValue97)
fieldValue98 = x3d.fieldValue()
fieldValue98.name = "moves"
ProtoInstance99 = x3d.ProtoInstance()
ProtoInstance99.name = "CameraMovement"
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "description"
fieldValue100.value = "Camera Zoom In"

ProtoInstance99.fieldValue.append(fieldValue100)
fieldValue101 = x3d.fieldValue()
fieldValue101.name = "duration"
fieldValue101.value = "3"

ProtoInstance99.fieldValue.append(fieldValue101)
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "goalPosition"
fieldValue102.value = "-50 1 -15"

ProtoInstance99.fieldValue.append(fieldValue102)
fieldValue103 = x3d.fieldValue()
fieldValue103.name = "goalOrientation"
fieldValue103.value = "0 1 0 0"

ProtoInstance99.fieldValue.append(fieldValue103)

fieldValue98.children.append(ProtoInstance99)
ProtoInstance104 = x3d.ProtoInstance()
ProtoInstance104.name = "CameraMovement"
fieldValue105 = x3d.fieldValue()
fieldValue105.name = "description"
fieldValue105.value = "Camera Zoom Out"

ProtoInstance104.fieldValue.append(fieldValue105)
fieldValue106 = x3d.fieldValue()
fieldValue106.name = "duration"
fieldValue106.value = "3"

ProtoInstance104.fieldValue.append(fieldValue106)
fieldValue107 = x3d.fieldValue()
fieldValue107.name = "goalPosition"
fieldValue107.value = "-50 1 -10"

ProtoInstance104.fieldValue.append(fieldValue107)
fieldValue108 = x3d.fieldValue()
fieldValue108.name = "goalOrientation"
fieldValue108.value = "0 1 0 0"

ProtoInstance104.fieldValue.append(fieldValue108)

fieldValue98.children.append(ProtoInstance104)
ProtoInstance109 = x3d.ProtoInstance()
ProtoInstance109.name = "CameraMovement"
fieldValue110 = x3d.fieldValue()
fieldValue110.name = "description"
fieldValue110.value = "Camera Pause"

ProtoInstance109.fieldValue.append(fieldValue110)
fieldValue111 = x3d.fieldValue()
fieldValue111.name = "duration"
fieldValue111.value = "1"

ProtoInstance109.fieldValue.append(fieldValue111)
fieldValue112 = x3d.fieldValue()
fieldValue112.name = "goalPosition"
fieldValue112.value = "-50 1 -10"

ProtoInstance109.fieldValue.append(fieldValue112)
fieldValue113 = x3d.fieldValue()
fieldValue113.name = "goalOrientation"
fieldValue113.value = "0 1 0 0"

ProtoInstance109.fieldValue.append(fieldValue113)

fieldValue98.children.append(ProtoInstance109)

ProtoInstance94.fieldValue.append(fieldValue98)

fieldValue93.children.append(ProtoInstance94)
ProtoInstance114 = x3d.ProtoInstance()
ProtoInstance114.name = "CameraShot"
ProtoInstance114.DEF = "Dolly"
fieldValue115 = x3d.fieldValue()
fieldValue115.name = "description"
fieldValue115.value = "Simple shot of Camera Dolly"

ProtoInstance114.fieldValue.append(fieldValue115)
fieldValue116 = x3d.fieldValue()
fieldValue116.name = "initialPosition"
fieldValue116.value = "-40 1 -10"

ProtoInstance114.fieldValue.append(fieldValue116)
fieldValue117 = x3d.fieldValue()
fieldValue117.name = "initialOrientation"
fieldValue117.value = "0 1 0 0"

ProtoInstance114.fieldValue.append(fieldValue117)
fieldValue118 = x3d.fieldValue()
fieldValue118.name = "moves"
ProtoInstance119 = x3d.ProtoInstance()
ProtoInstance119.name = "CameraMovement"
ProtoInstance119.DEF = "DollyMove1"
fieldValue120 = x3d.fieldValue()
fieldValue120.name = "description"
fieldValue120.value = "Camera Dolly from Right to Left"

ProtoInstance119.fieldValue.append(fieldValue120)
fieldValue121 = x3d.fieldValue()
fieldValue121.name = "duration"
fieldValue121.value = "3"

ProtoInstance119.fieldValue.append(fieldValue121)
fieldValue122 = x3d.fieldValue()
fieldValue122.name = "goalPosition"
fieldValue122.value = "-45 1 -10"

ProtoInstance119.fieldValue.append(fieldValue122)
fieldValue123 = x3d.fieldValue()
fieldValue123.name = "goalOrientation"
fieldValue123.value = "0 1 0 0"

ProtoInstance119.fieldValue.append(fieldValue123)

fieldValue118.children.append(ProtoInstance119)
ProtoInstance124 = x3d.ProtoInstance()
ProtoInstance124.name = "CameraMovement"
fieldValue125 = x3d.fieldValue()
fieldValue125.name = "description"
fieldValue125.value = "Camera Dolly from Left to Right"

ProtoInstance124.fieldValue.append(fieldValue125)
fieldValue126 = x3d.fieldValue()
fieldValue126.name = "duration"
fieldValue126.value = "3"

ProtoInstance124.fieldValue.append(fieldValue126)
fieldValue127 = x3d.fieldValue()
fieldValue127.name = "goalPosition"
fieldValue127.value = "-40 1 -10"

ProtoInstance124.fieldValue.append(fieldValue127)
fieldValue128 = x3d.fieldValue()
fieldValue128.name = "goalOrientation"
fieldValue128.value = "0 1 0 0"

ProtoInstance124.fieldValue.append(fieldValue128)

fieldValue118.children.append(ProtoInstance124)
ProtoInstance129 = x3d.ProtoInstance()
ProtoInstance129.name = "CameraMovement"
fieldValue130 = x3d.fieldValue()
fieldValue130.name = "description"
fieldValue130.value = "Camera Pause"

ProtoInstance129.fieldValue.append(fieldValue130)
fieldValue131 = x3d.fieldValue()
fieldValue131.name = "duration"
fieldValue131.value = "1"

ProtoInstance129.fieldValue.append(fieldValue131)
fieldValue132 = x3d.fieldValue()
fieldValue132.name = "goalPosition"
fieldValue132.value = "-40 1 -10"

ProtoInstance129.fieldValue.append(fieldValue132)
fieldValue133 = x3d.fieldValue()
fieldValue133.name = "goalOrientation"
fieldValue133.value = "0 1 0 0"

ProtoInstance129.fieldValue.append(fieldValue133)

fieldValue118.children.append(ProtoInstance129)

ProtoInstance114.fieldValue.append(fieldValue118)

fieldValue93.children.append(ProtoInstance114)
ProtoInstance134 = x3d.ProtoInstance()
ProtoInstance134.name = "CameraShot"
ProtoInstance134.DEF = "Pan"
fieldValue135 = x3d.fieldValue()
fieldValue135.name = "description"
fieldValue135.value = "Simple shot of Camera Pan left right and back to center"

ProtoInstance134.fieldValue.append(fieldValue135)
fieldValue136 = x3d.fieldValue()
fieldValue136.name = "initialPosition"
fieldValue136.value = "-30 1 -10"

ProtoInstance134.fieldValue.append(fieldValue136)
fieldValue137 = x3d.fieldValue()
fieldValue137.name = "initialOrientation"
fieldValue137.value = "0 1 0 0"

ProtoInstance134.fieldValue.append(fieldValue137)
fieldValue138 = x3d.fieldValue()
fieldValue138.name = "moves"
ProtoInstance139 = x3d.ProtoInstance()
ProtoInstance139.name = "CameraMovement"
ProtoInstance139.DEF = "PanLeft"
fieldValue140 = x3d.fieldValue()
fieldValue140.name = "description"
fieldValue140.value = "Pan Left"

ProtoInstance139.fieldValue.append(fieldValue140)
fieldValue141 = x3d.fieldValue()
fieldValue141.name = "duration"
fieldValue141.value = "2"

ProtoInstance139.fieldValue.append(fieldValue141)
fieldValue142 = x3d.fieldValue()
fieldValue142.name = "goalPosition"
fieldValue142.value = "-30 1 -10"

ProtoInstance139.fieldValue.append(fieldValue142)
fieldValue143 = x3d.fieldValue()
fieldValue143.name = "goalOrientation"
fieldValue143.value = "0 1 0 0.4"

ProtoInstance139.fieldValue.append(fieldValue143)

fieldValue138.children.append(ProtoInstance139)
ProtoInstance144 = x3d.ProtoInstance()
ProtoInstance144.name = "CameraMovement"
ProtoInstance144.DEF = "PanRight"
fieldValue145 = x3d.fieldValue()
fieldValue145.name = "description"
fieldValue145.value = "Pan Right"

ProtoInstance144.fieldValue.append(fieldValue145)
fieldValue146 = x3d.fieldValue()
fieldValue146.name = "duration"
fieldValue146.value = "3"

ProtoInstance144.fieldValue.append(fieldValue146)
fieldValue147 = x3d.fieldValue()
fieldValue147.name = "goalPosition"
fieldValue147.value = "-30 1 -10"

ProtoInstance144.fieldValue.append(fieldValue147)
fieldValue148 = x3d.fieldValue()
fieldValue148.name = "goalOrientation"
fieldValue148.value = "0 1 0 -0.4"

ProtoInstance144.fieldValue.append(fieldValue148)

fieldValue138.children.append(ProtoInstance144)
ProtoInstance149 = x3d.ProtoInstance()
ProtoInstance149.name = "CameraMovement"
fieldValue150 = x3d.fieldValue()
fieldValue150.name = "description"
fieldValue150.value = "Camera Pan back to Center"

ProtoInstance149.fieldValue.append(fieldValue150)
fieldValue151 = x3d.fieldValue()
fieldValue151.name = "duration"
fieldValue151.value = "2"

ProtoInstance149.fieldValue.append(fieldValue151)
fieldValue152 = x3d.fieldValue()
fieldValue152.name = "goalPosition"
fieldValue152.value = "-30 1 -10"

ProtoInstance149.fieldValue.append(fieldValue152)
fieldValue153 = x3d.fieldValue()
fieldValue153.name = "goalOrientation"
fieldValue153.value = "0 1 0 0"

ProtoInstance149.fieldValue.append(fieldValue153)

fieldValue138.children.append(ProtoInstance149)
ProtoInstance154 = x3d.ProtoInstance()
ProtoInstance154.name = "CameraMovement"
fieldValue155 = x3d.fieldValue()
fieldValue155.name = "description"
fieldValue155.value = "Camera Pause"

ProtoInstance154.fieldValue.append(fieldValue155)
fieldValue156 = x3d.fieldValue()
fieldValue156.name = "duration"
fieldValue156.value = "2"

ProtoInstance154.fieldValue.append(fieldValue156)
fieldValue157 = x3d.fieldValue()
fieldValue157.name = "goalPosition"
fieldValue157.value = "-30 1 -10"

ProtoInstance154.fieldValue.append(fieldValue157)
fieldValue158 = x3d.fieldValue()
fieldValue158.name = "goalOrientation"
fieldValue158.value = "0 1 0 0"

ProtoInstance154.fieldValue.append(fieldValue158)

fieldValue138.children.append(ProtoInstance154)

ProtoInstance134.fieldValue.append(fieldValue138)

fieldValue93.children.append(ProtoInstance134)
ProtoInstance159 = x3d.ProtoInstance()
ProtoInstance159.name = "CameraShot"
ProtoInstance159.DEF = "CameraBoom"
fieldValue160 = x3d.fieldValue()
fieldValue160.name = "description"
fieldValue160.value = "Camera Boom"

ProtoInstance159.fieldValue.append(fieldValue160)
fieldValue161 = x3d.fieldValue()
fieldValue161.name = "initialPosition"
fieldValue161.value = "-20 1 -10"

ProtoInstance159.fieldValue.append(fieldValue161)
fieldValue162 = x3d.fieldValue()
fieldValue162.name = "initialOrientation"
fieldValue162.value = "0 1 0 0"

ProtoInstance159.fieldValue.append(fieldValue162)
fieldValue163 = x3d.fieldValue()
fieldValue163.name = "moves"
ProtoInstance164 = x3d.ProtoInstance()
ProtoInstance164.name = "CameraMovement"
ProtoInstance164.DEF = "CameraBoomUp"
fieldValue165 = x3d.fieldValue()
fieldValue165.name = "description"
fieldValue165.value = "Camera Boom Up"

ProtoInstance164.fieldValue.append(fieldValue165)
fieldValue166 = x3d.fieldValue()
fieldValue166.name = "duration"
fieldValue166.value = "3"

ProtoInstance164.fieldValue.append(fieldValue166)
fieldValue167 = x3d.fieldValue()
fieldValue167.name = "goalPosition"
fieldValue167.value = "-20 5 -10"

ProtoInstance164.fieldValue.append(fieldValue167)
fieldValue168 = x3d.fieldValue()
fieldValue168.name = "goalOrientation"
fieldValue168.value = "0 1 0 0"

ProtoInstance164.fieldValue.append(fieldValue168)

fieldValue163.children.append(ProtoInstance164)
ProtoInstance169 = x3d.ProtoInstance()
ProtoInstance169.name = "CameraMovement"
ProtoInstance169.DEF = "BoomDown"
fieldValue170 = x3d.fieldValue()
fieldValue170.name = "description"
fieldValue170.value = "Camera Boom Down"

ProtoInstance169.fieldValue.append(fieldValue170)
fieldValue171 = x3d.fieldValue()
fieldValue171.name = "duration"
fieldValue171.value = "3"

ProtoInstance169.fieldValue.append(fieldValue171)
fieldValue172 = x3d.fieldValue()
fieldValue172.name = "goalPosition"
fieldValue172.value = "-20 1 -10"

ProtoInstance169.fieldValue.append(fieldValue172)
fieldValue173 = x3d.fieldValue()
fieldValue173.name = "goalOrientation"
fieldValue173.value = "0 1 0 0"

ProtoInstance169.fieldValue.append(fieldValue173)

fieldValue163.children.append(ProtoInstance169)
ProtoInstance174 = x3d.ProtoInstance()
ProtoInstance174.name = "CameraMovement"
ProtoInstance174.DEF = "BoomPause"
fieldValue175 = x3d.fieldValue()
fieldValue175.name = "description"
fieldValue175.value = "Camera Pause"

ProtoInstance174.fieldValue.append(fieldValue175)
fieldValue176 = x3d.fieldValue()
fieldValue176.name = "duration"
fieldValue176.value = "2"

ProtoInstance174.fieldValue.append(fieldValue176)
fieldValue177 = x3d.fieldValue()
fieldValue177.name = "goalPosition"
fieldValue177.value = "-20 1 -10"

ProtoInstance174.fieldValue.append(fieldValue177)
fieldValue178 = x3d.fieldValue()
fieldValue178.name = "goalOrientation"
fieldValue178.value = "0 1 0 0"

ProtoInstance174.fieldValue.append(fieldValue178)

fieldValue163.children.append(ProtoInstance174)

ProtoInstance159.fieldValue.append(fieldValue163)

fieldValue93.children.append(ProtoInstance159)
ProtoInstance179 = x3d.ProtoInstance()
ProtoInstance179.name = "CameraShot"
ProtoInstance179.DEF = "CameraTilt"
fieldValue180 = x3d.fieldValue()
fieldValue180.name = "description"
fieldValue180.value = "Camera Tilt"

ProtoInstance179.fieldValue.append(fieldValue180)
fieldValue181 = x3d.fieldValue()
fieldValue181.name = "initialPosition"
fieldValue181.value = "-10 1 -10"

ProtoInstance179.fieldValue.append(fieldValue181)
fieldValue182 = x3d.fieldValue()
fieldValue182.name = "initialOrientation"
fieldValue182.value = "0 0 1 0"

ProtoInstance179.fieldValue.append(fieldValue182)
fieldValue183 = x3d.fieldValue()
fieldValue183.name = "traceEnabled"
fieldValue183.value = "true"

ProtoInstance179.fieldValue.append(fieldValue183)
fieldValue184 = x3d.fieldValue()
fieldValue184.name = "moves"
ProtoInstance185 = x3d.ProtoInstance()
ProtoInstance185.name = "CameraMovement"
fieldValue186 = x3d.fieldValue()
fieldValue186.name = "description"
fieldValue186.value = "Camera Tilt Pause"

ProtoInstance185.fieldValue.append(fieldValue186)
fieldValue187 = x3d.fieldValue()
fieldValue187.name = "duration"
fieldValue187.value = "1"

ProtoInstance185.fieldValue.append(fieldValue187)
fieldValue188 = x3d.fieldValue()
fieldValue188.name = "goalPosition"
fieldValue188.value = "-10 1 -10"

ProtoInstance185.fieldValue.append(fieldValue188)
fieldValue189 = x3d.fieldValue()
fieldValue189.name = "goalOrientation"
fieldValue189.value = "0 0 1 0"

ProtoInstance185.fieldValue.append(fieldValue189)

fieldValue184.children.append(ProtoInstance185)
ProtoInstance190 = x3d.ProtoInstance()
ProtoInstance190.name = "CameraMovement"
ProtoInstance190.DEF = "TiltDown"
fieldValue191 = x3d.fieldValue()
fieldValue191.name = "description"
fieldValue191.value = "Camera Tilt Left"

ProtoInstance190.fieldValue.append(fieldValue191)
fieldValue192 = x3d.fieldValue()
fieldValue192.name = "duration"
fieldValue192.value = "3"

ProtoInstance190.fieldValue.append(fieldValue192)
fieldValue193 = x3d.fieldValue()
fieldValue193.name = "goalPosition"
fieldValue193.value = "-10 1 -10"

ProtoInstance190.fieldValue.append(fieldValue193)
fieldValue194 = x3d.fieldValue()
fieldValue194.name = "goalOrientation"
fieldValue194.value = "0 0 1 0.785"

ProtoInstance190.fieldValue.append(fieldValue194)

fieldValue184.children.append(ProtoInstance190)
ProtoInstance195 = x3d.ProtoInstance()
ProtoInstance195.name = "CameraMovement"
ProtoInstance195.DEF = "TiltPause"
fieldValue196 = x3d.fieldValue()
fieldValue196.name = "description"
fieldValue196.value = "Camera Tilt Pause"

ProtoInstance195.fieldValue.append(fieldValue196)
fieldValue197 = x3d.fieldValue()
fieldValue197.name = "duration"
fieldValue197.value = "1"

ProtoInstance195.fieldValue.append(fieldValue197)
fieldValue198 = x3d.fieldValue()
fieldValue198.name = "goalPosition"
fieldValue198.value = "-10 1 -10"

ProtoInstance195.fieldValue.append(fieldValue198)
fieldValue199 = x3d.fieldValue()
fieldValue199.name = "goalOrientation"
fieldValue199.value = "0 0 1 0.785"

ProtoInstance195.fieldValue.append(fieldValue199)

fieldValue184.children.append(ProtoInstance195)
ProtoInstance200 = x3d.ProtoInstance()
ProtoInstance200.name = "CameraMovement"
fieldValue201 = x3d.fieldValue()
fieldValue201.name = "description"
fieldValue201.value = "Camera Tilt Right"

ProtoInstance200.fieldValue.append(fieldValue201)
fieldValue202 = x3d.fieldValue()
fieldValue202.name = "duration"
fieldValue202.value = "3"

ProtoInstance200.fieldValue.append(fieldValue202)
fieldValue203 = x3d.fieldValue()
fieldValue203.name = "goalPosition"
fieldValue203.value = "-10 1 -10"

ProtoInstance200.fieldValue.append(fieldValue203)
fieldValue204 = x3d.fieldValue()
fieldValue204.name = "goalOrientation"
fieldValue204.value = "0 0 1 -0.785"

ProtoInstance200.fieldValue.append(fieldValue204)

fieldValue184.children.append(ProtoInstance200)
ProtoInstance205 = x3d.ProtoInstance()
ProtoInstance205.name = "CameraMovement"
fieldValue206 = x3d.fieldValue()
fieldValue206.name = "description"
fieldValue206.value = "Camera Tilt Pause"

ProtoInstance205.fieldValue.append(fieldValue206)
fieldValue207 = x3d.fieldValue()
fieldValue207.name = "duration"
fieldValue207.value = "1"

ProtoInstance205.fieldValue.append(fieldValue207)
fieldValue208 = x3d.fieldValue()
fieldValue208.name = "goalPosition"
fieldValue208.value = "-10 1 -10"

ProtoInstance205.fieldValue.append(fieldValue208)
fieldValue209 = x3d.fieldValue()
fieldValue209.name = "goalOrientation"
fieldValue209.value = "0 0 1 -0.785"

ProtoInstance205.fieldValue.append(fieldValue209)

fieldValue184.children.append(ProtoInstance205)
ProtoInstance210 = x3d.ProtoInstance()
ProtoInstance210.name = "CameraMovement"
ProtoInstance210.DEF = "TiltReset"
fieldValue211 = x3d.fieldValue()
fieldValue211.name = "description"
fieldValue211.value = "Camera Tilt Reset"

ProtoInstance210.fieldValue.append(fieldValue211)
fieldValue212 = x3d.fieldValue()
fieldValue212.name = "duration"
fieldValue212.value = "1"

ProtoInstance210.fieldValue.append(fieldValue212)
fieldValue213 = x3d.fieldValue()
fieldValue213.name = "goalPosition"
fieldValue213.value = "-10 1 -10"

ProtoInstance210.fieldValue.append(fieldValue213)
fieldValue214 = x3d.fieldValue()
fieldValue214.name = "goalOrientation"
fieldValue214.value = "0 0 1 0"

ProtoInstance210.fieldValue.append(fieldValue214)

fieldValue184.children.append(ProtoInstance210)
ProtoInstance215 = x3d.ProtoInstance()
ProtoInstance215.name = "CameraMovement"
ProtoInstance215.DEF = "TiltUp"
fieldValue216 = x3d.fieldValue()
fieldValue216.name = "description"
fieldValue216.value = "Return to home"

ProtoInstance215.fieldValue.append(fieldValue216)
fieldValue217 = x3d.fieldValue()
fieldValue217.name = "duration"
fieldValue217.value = "2"

ProtoInstance215.fieldValue.append(fieldValue217)
fieldValue218 = x3d.fieldValue()
fieldValue218.name = "goalPosition"
fieldValue218.value = "0 2 12"

ProtoInstance215.fieldValue.append(fieldValue218)
fieldValue219 = x3d.fieldValue()
fieldValue219.name = "goalOrientation"
fieldValue219.value = "0 0 1 0"

ProtoInstance215.fieldValue.append(fieldValue219)

fieldValue184.children.append(ProtoInstance215)

ProtoInstance179.fieldValue.append(fieldValue184)

fieldValue93.children.append(ProtoInstance179)

ProtoInstance89.fieldValue.append(fieldValue93)

Scene21.children.append(ProtoInstance89)
Group220 = x3d.Group()
Group220.DEF = "AnimationGroup.SimpleShots"
TimeSensor221 = x3d.TimeSensor()
TimeSensor221.DEF = "CameraTimer.SimpleShots"

Group220.children.append(TimeSensor221)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE222 = x3d.ROUTE()
ROUTE222.fromField = "totalDuration"
ROUTE222.fromNode = "Camera.SimpleShotsTest"
ROUTE222.toField = "cycleInterval"
ROUTE222.toNode = "CameraTimer.SimpleShots"

Group220.children.append(ROUTE222)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE223 = x3d.ROUTE()
ROUTE223.fromField = "fraction_changed"
ROUTE223.fromNode = "CameraTimer.SimpleShots"
ROUTE223.toField = "set_fraction"
ROUTE223.toNode = "Camera.SimpleShotsTest"

Group220.children.append(ROUTE223)
Transform224 = x3d.Transform()
Transform224.DEF = "Trigger.SimpleShots"
Transform224.translation = [-4,4,0]
BooleanFilter225 = x3d.BooleanFilter()
BooleanFilter225.DEF = "TextTouchActive.SimpleShotsFilter"

Transform224.children.append(BooleanFilter225)
TouchSensor226 = x3d.TouchSensor()
TouchSensor226.DEF = "TextTouch.SimpleShots"
TouchSensor226.description = "touch to animate Camera SimpleShotsTest"

Transform224.children.append(TouchSensor226)
ROUTE227 = x3d.ROUTE()
ROUTE227.fromField = "inputTrue"
ROUTE227.fromNode = "TextTouchActive.SimpleShotsFilter"
ROUTE227.toField = "set_bind"
ROUTE227.toNode = "Camera.SimpleShotsTest"

Transform224.children.append(ROUTE227)
ROUTE228 = x3d.ROUTE()
ROUTE228.fromField = "isActive"
ROUTE228.fromNode = "TextTouch.SimpleShots"
ROUTE228.toField = "set_boolean"
ROUTE228.toNode = "TextTouchActive.SimpleShotsFilter"

Transform224.children.append(ROUTE228)
ROUTE229 = x3d.ROUTE()
ROUTE229.fromField = "touchTime"
ROUTE229.fromNode = "TextTouch.SimpleShots"
ROUTE229.toField = "startTime"
ROUTE229.toNode = "CameraTimer.SimpleShots"

Transform224.children.append(ROUTE229)
Shape230 = x3d.Shape()
Text231 = x3d.Text()
Text231.string = ["Click to animate","SimpleShotsTest"]
FontStyle232 = x3d.FontStyle()
FontStyle232.justify = ["MIDDLE","MIDDLE"]

Text231.fontStyle = FontStyle232

Shape230.geometry = Text231
Appearance233 = x3d.Appearance()
Material234 = x3d.Material()
Material234.DEF = "ArtDeco5"
Material234.ambientIntensity = 0.24
Material234.diffuseColor = [0.945455,0.318988,0.321717]
Material234.shininess = 0.01
Material234.specularColor = [0.072727,0.021705,0.010732]
#Universal Media Library: ArtDeco 5

Appearance233.material = Material234

Shape230.appearance = Appearance233

Transform224.children.append(Shape230)
#Simplify intersection test for user selecting text
Shape235 = x3d.Shape()
Shape235.DEF = "TransparentBox"
Appearance236 = x3d.Appearance()
Material237 = x3d.Material()
Material237.transparency = 1

Appearance236.material = Material237

Shape235.appearance = Appearance236
Box238 = x3d.Box()
Box238.size = [6,2,0.0001]

Shape235.geometry = Box238

Transform224.children.append(Shape235)

Group220.children.append(Transform224)

Scene21.children.append(Group220)
Group239 = x3d.Group()
Group239.DEF = "SimpleShotsTargets"
Transform240 = x3d.Transform()
Transform240.DEF = "TargetBoxZoom"
Transform240.translation = [-50,1,-20]
Shape241 = x3d.Shape()
Box242 = x3d.Box()

Shape241.geometry = Box242
Appearance243 = x3d.Appearance()
Material244 = x3d.Material()

Appearance243.material = Material244
ImageTexture245 = x3d.ImageTexture()
ImageTexture245.url = ["images/CameraMoveZoom.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveZoom.png"]

Appearance243.texture = ImageTexture245

Shape241.appearance = Appearance243

Transform240.children.append(Shape241)
Transform246 = x3d.Transform()
Transform246.translation = [0,2,0]
Shape247 = x3d.Shape()
Text248 = x3d.Text()
Text248.string = ["Zoom in, out"]
FontStyle249 = x3d.FontStyle()
FontStyle249.justify = ["MIDDLE","MIDDLE"]

Text248.fontStyle = FontStyle249

Shape247.geometry = Text248
Appearance250 = x3d.Appearance()
Material251 = x3d.Material()

Appearance250.material = Material251

Shape247.appearance = Appearance250

Transform246.children.append(Shape247)

Transform240.children.append(Transform246)

Group239.children.append(Transform240)
Transform252 = x3d.Transform()
Transform252.DEF = "TargetBoxDolly"
Transform252.translation = [-40,1,-20]
Shape253 = x3d.Shape()
Box254 = x3d.Box()

Shape253.geometry = Box254
Appearance255 = x3d.Appearance()
Material256 = x3d.Material()

Appearance255.material = Material256
ImageTexture257 = x3d.ImageTexture()
ImageTexture257.url = ["images/CameraMoveDolly.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveDolly.png"]

Appearance255.texture = ImageTexture257

Shape253.appearance = Appearance255

Transform252.children.append(Shape253)
Transform258 = x3d.Transform()
Transform258.translation = [0,2,0]
Shape259 = x3d.Shape()
Text260 = x3d.Text()
Text260.string = ["Dolly left, right"]
FontStyle261 = x3d.FontStyle()
FontStyle261.justify = ["MIDDLE","MIDDLE"]

Text260.fontStyle = FontStyle261

Shape259.geometry = Text260
Appearance262 = x3d.Appearance()
Material263 = x3d.Material()

Appearance262.material = Material263

Shape259.appearance = Appearance262

Transform258.children.append(Shape259)

Transform252.children.append(Transform258)

Group239.children.append(Transform252)
Transform264 = x3d.Transform()
Transform264.DEF = "TargetBoxPan"
Transform264.translation = [-30,1,-20]
Shape265 = x3d.Shape()
Box266 = x3d.Box()

Shape265.geometry = Box266
Appearance267 = x3d.Appearance()
Material268 = x3d.Material()

Appearance267.material = Material268
ImageTexture269 = x3d.ImageTexture()
ImageTexture269.url = ["images/CameraMovePan.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMovePan.png"]

Appearance267.texture = ImageTexture269

Shape265.appearance = Appearance267

Transform264.children.append(Shape265)
Transform270 = x3d.Transform()
Transform270.translation = [0,2,0]
Shape271 = x3d.Shape()
Text272 = x3d.Text()
Text272.string = ["Pan left, right"]
FontStyle273 = x3d.FontStyle()
FontStyle273.justify = ["MIDDLE","MIDDLE"]

Text272.fontStyle = FontStyle273

Shape271.geometry = Text272
Appearance274 = x3d.Appearance()
Material275 = x3d.Material()

Appearance274.material = Material275

Shape271.appearance = Appearance274

Transform270.children.append(Shape271)

Transform264.children.append(Transform270)

Group239.children.append(Transform264)
Transform276 = x3d.Transform()
Transform276.DEF = "TargetBoxBoom"
Transform276.translation = [-20,1,-20]
Shape277 = x3d.Shape()
Box278 = x3d.Box()

Shape277.geometry = Box278
Appearance279 = x3d.Appearance()
Material280 = x3d.Material()

Appearance279.material = Material280
ImageTexture281 = x3d.ImageTexture()
ImageTexture281.url = ["images/CameraMoveBoom.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveBoom.png"]

Appearance279.texture = ImageTexture281

Shape277.appearance = Appearance279

Transform276.children.append(Shape277)
Transform282 = x3d.Transform()
Transform282.translation = [0,2,0]
Shape283 = x3d.Shape()
Text284 = x3d.Text()
Text284.string = ["Boom up, down"]
FontStyle285 = x3d.FontStyle()
FontStyle285.justify = ["MIDDLE","MIDDLE"]

Text284.fontStyle = FontStyle285

Shape283.geometry = Text284
Appearance286 = x3d.Appearance()
Material287 = x3d.Material()

Appearance286.material = Material287

Shape283.appearance = Appearance286

Transform282.children.append(Shape283)

Transform276.children.append(Transform282)

Group239.children.append(Transform276)
Transform288 = x3d.Transform()
Transform288.DEF = "TargetBoxTilt"
Transform288.translation = [-10,1,-20]
Shape289 = x3d.Shape()
Box290 = x3d.Box()

Shape289.geometry = Box290
Appearance291 = x3d.Appearance()
Material292 = x3d.Material()

Appearance291.material = Material292
ImageTexture293 = x3d.ImageTexture()
ImageTexture293.url = ["images/CameraMoveTilt.png","https://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveTilt.png"]

Appearance291.texture = ImageTexture293

Shape289.appearance = Appearance291

Transform288.children.append(Shape289)
Transform294 = x3d.Transform()
Transform294.translation = [0,2,0]
Shape295 = x3d.Shape()
Text296 = x3d.Text()
Text296.string = ["Tilt left, right"]
FontStyle297 = x3d.FontStyle()
FontStyle297.justify = ["MIDDLE","MIDDLE"]

Text296.fontStyle = FontStyle297

Shape295.geometry = Text296
Appearance298 = x3d.Appearance()
Material299 = x3d.Material()

Appearance298.material = Material299

Shape295.appearance = Appearance298

Transform294.children.append(Shape295)

Transform288.children.append(Transform294)

Group239.children.append(Transform288)

Scene21.children.append(Group239)
#=============== Camera.AimPointTest ==============
ProtoInstance300 = x3d.ProtoInstance()
ProtoInstance300.name = "Camera"
ProtoInstance300.DEF = "Camera.AimPointTest"
fieldValue301 = x3d.fieldValue()
fieldValue301.name = "description"
fieldValue301.value = "AimPointTest for moving camera tracking moving target"

ProtoInstance300.fieldValue.append(fieldValue301)
fieldValue302 = x3d.fieldValue()
fieldValue302.name = "position"
fieldValue302.value = "4 4 10"

ProtoInstance300.fieldValue.append(fieldValue302)
fieldValue303 = x3d.fieldValue()
fieldValue303.name = "shots"
ProtoInstance304 = x3d.ProtoInstance()
ProtoInstance304.name = "CameraShot"
ProtoInstance304.DEF = "Shot5"
fieldValue305 = x3d.fieldValue()
fieldValue305.name = "description"
fieldValue305.value = "#3 Tracking shot"

ProtoInstance304.fieldValue.append(fieldValue305)
fieldValue306 = x3d.fieldValue()
fieldValue306.name = "initialPosition"
fieldValue306.value = "6 6 10"

ProtoInstance304.fieldValue.append(fieldValue306)
fieldValue307 = x3d.fieldValue()
fieldValue307.name = "initialOrientation"
fieldValue307.value = "0 1 0 0"

ProtoInstance304.fieldValue.append(fieldValue307)
fieldValue308 = x3d.fieldValue()
fieldValue308.name = "moves"
ProtoInstance309 = x3d.ProtoInstance()
ProtoInstance309.name = "CameraMovement"
ProtoInstance309.DEF = "MoveAimPoint3.1"
fieldValue310 = x3d.fieldValue()
fieldValue310.name = "description"
fieldValue310.value = "AimPoint 3.1 moving BoxPath"

ProtoInstance309.fieldValue.append(fieldValue310)
fieldValue311 = x3d.fieldValue()
fieldValue311.name = "tracking"
fieldValue311.value = "true"

ProtoInstance309.fieldValue.append(fieldValue311)
fieldValue312 = x3d.fieldValue()
fieldValue312.name = "duration"
fieldValue312.value = "8"

ProtoInstance309.fieldValue.append(fieldValue312)
fieldValue313 = x3d.fieldValue()
fieldValue313.name = "goalPosition"
fieldValue313.value = "6 6 10"

ProtoInstance309.fieldValue.append(fieldValue313)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.children.append(ProtoInstance309)
ProtoInstance314 = x3d.ProtoInstance()
ProtoInstance314.name = "CameraMovement"
ProtoInstance314.DEF = "MoveAimPoint3.2"
fieldValue315 = x3d.fieldValue()
fieldValue315.name = "description"
fieldValue315.value = "AimPoint 3.2 pan right while tracking"

ProtoInstance314.fieldValue.append(fieldValue315)
fieldValue316 = x3d.fieldValue()
fieldValue316.name = "tracking"
fieldValue316.value = "true"

ProtoInstance314.fieldValue.append(fieldValue316)
fieldValue317 = x3d.fieldValue()
fieldValue317.name = "duration"
fieldValue317.value = "8"

ProtoInstance314.fieldValue.append(fieldValue317)
fieldValue318 = x3d.fieldValue()
fieldValue318.name = "goalPosition"
fieldValue318.value = "40 6 12"

ProtoInstance314.fieldValue.append(fieldValue318)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.children.append(ProtoInstance314)
ProtoInstance319 = x3d.ProtoInstance()
ProtoInstance319.name = "CameraMovement"
ProtoInstance319.DEF = "MoveAimPoint3.3"
fieldValue320 = x3d.fieldValue()
fieldValue320.name = "description"
fieldValue320.value = "AimPoint 3.3 boom up while tracking"

ProtoInstance319.fieldValue.append(fieldValue320)
fieldValue321 = x3d.fieldValue()
fieldValue321.name = "tracking"
fieldValue321.value = "true"

ProtoInstance319.fieldValue.append(fieldValue321)
fieldValue322 = x3d.fieldValue()
fieldValue322.name = "duration"
fieldValue322.value = "3"

ProtoInstance319.fieldValue.append(fieldValue322)
fieldValue323 = x3d.fieldValue()
fieldValue323.name = "goalPosition"
fieldValue323.value = "40 20 13"

ProtoInstance319.fieldValue.append(fieldValue323)
#goalAimPoint modified by ROUTE to match moving Box

fieldValue308.children.append(ProtoInstance319)
ProtoInstance324 = x3d.ProtoInstance()
ProtoInstance324.name = "CameraMovement"
ProtoInstance324.DEF = "MoveAimPoint3.4"
fieldValue325 = x3d.fieldValue()
fieldValue325.name = "description"
fieldValue325.value = "AimPoint 3.4 restore camera back to home"

ProtoInstance324.fieldValue.append(fieldValue325)
fieldValue326 = x3d.fieldValue()
fieldValue326.name = "tracking"
fieldValue326.value = "true"

ProtoInstance324.fieldValue.append(fieldValue326)
fieldValue327 = x3d.fieldValue()
fieldValue327.name = "duration"
fieldValue327.value = "5"

ProtoInstance324.fieldValue.append(fieldValue327)
fieldValue328 = x3d.fieldValue()
fieldValue328.name = "goalPosition"
fieldValue328.value = "4 4 10"

ProtoInstance324.fieldValue.append(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.name = "goalAimPoint"
fieldValue329.value = "4 4 0"

ProtoInstance324.fieldValue.append(fieldValue329)
fieldValue330 = x3d.fieldValue()
fieldValue330.name = "goalOrientation"
fieldValue330.value = "0 1 0 0"

ProtoInstance324.fieldValue.append(fieldValue330)
#can test tracking or not using these values

fieldValue308.children.append(ProtoInstance324)

ProtoInstance304.fieldValue.append(fieldValue308)

fieldValue303.children.append(ProtoInstance304)

ProtoInstance300.fieldValue.append(fieldValue303)

Scene21.children.append(ProtoInstance300)
Group331 = x3d.Group()
Group331.DEF = "AnimationGroup.AimPointTest"
TimeSensor332 = x3d.TimeSensor()
TimeSensor332.DEF = "CameraTimer.AimPointTest"

Group331.children.append(TimeSensor332)
#initialize clock to match totalDuration of combined Shot Moves
ROUTE333 = x3d.ROUTE()
ROUTE333.fromField = "totalDuration"
ROUTE333.fromNode = "Camera.AimPointTest"
ROUTE333.toField = "cycleInterval"
ROUTE333.toNode = "CameraTimer.AimPointTest"

Group331.children.append(ROUTE333)
#TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator
ROUTE334 = x3d.ROUTE()
ROUTE334.fromField = "fraction_changed"
ROUTE334.fromNode = "CameraTimer.AimPointTest"
ROUTE334.toField = "set_fraction"
ROUTE334.toNode = "Camera.AimPointTest"

Group331.children.append(ROUTE334)
Transform335 = x3d.Transform()
Transform335.DEF = "Trigger.AimPointTest"
Transform335.translation = [4,4,0]
BooleanFilter336 = x3d.BooleanFilter()
BooleanFilter336.DEF = "TextTouchActive.AimPointFilter"

Transform335.children.append(BooleanFilter336)
TouchSensor337 = x3d.TouchSensor()
TouchSensor337.DEF = "TextTouch.AimPointTest"
TouchSensor337.description = "touch to animate Camera AimPointTest"

Transform335.children.append(TouchSensor337)
ROUTE338 = x3d.ROUTE()
ROUTE338.fromField = "inputTrue"
ROUTE338.fromNode = "TextTouchActive.AimPointFilter"
ROUTE338.toField = "set_bind"
ROUTE338.toNode = "Camera.AimPointTest"

Transform335.children.append(ROUTE338)
ROUTE339 = x3d.ROUTE()
ROUTE339.fromField = "isActive"
ROUTE339.fromNode = "TextTouch.AimPointTest"
ROUTE339.toField = "set_boolean"
ROUTE339.toNode = "TextTouchActive.AimPointFilter"

Transform335.children.append(ROUTE339)
ROUTE340 = x3d.ROUTE()
ROUTE340.fromField = "touchTime"
ROUTE340.fromNode = "TextTouch.AimPointTest"
ROUTE340.toField = "startTime"
ROUTE340.toNode = "CameraTimer.AimPointTest"

Transform335.children.append(ROUTE340)
Shape341 = x3d.Shape()
Text342 = x3d.Text()
Text342.string = ["Click to animate","AimPointTest"]
FontStyle343 = x3d.FontStyle()
FontStyle343.justify = ["MIDDLE","MIDDLE"]

Text342.fontStyle = FontStyle343

Shape341.geometry = Text342
Appearance344 = x3d.Appearance()
Material345 = x3d.Material()
Material345.USE = "ArtDeco5"

Appearance344.material = Material345

Shape341.appearance = Appearance344

Transform335.children.append(Shape341)
Shape346 = x3d.Shape()
Shape346.USE = "TransparentBox"

Transform335.children.append(Shape346)

Group331.children.append(Transform335)

Scene21.children.append(Group331)
#TODO build a test once implemented
ProtoInstance347 = x3d.ProtoInstance()
ProtoInstance347.name = "OfflineRender"

Scene21.children.append(ProtoInstance347)
#=============== animate a camera shape to visualize view changes ==============
Transform348 = x3d.Transform()
Transform348.DEF = "CameraShapeTransform"
Transform348.translation = [0,0.5,0]
#move CameraShape using active Camera
ROUTE349 = x3d.ROUTE()
ROUTE349.fromField = "position_changed"
ROUTE349.fromNode = "Camera.SimpleShotsTest"
ROUTE349.toField = "translation"
ROUTE349.toNode = "CameraShapeTransform"

Transform348.children.append(ROUTE349)
ROUTE350 = x3d.ROUTE()
ROUTE350.fromField = "orientation_changed"
ROUTE350.fromNode = "Camera.SimpleShotsTest"
ROUTE350.toField = "rotation"
ROUTE350.toNode = "CameraShapeTransform"

Transform348.children.append(ROUTE350)
ROUTE351 = x3d.ROUTE()
ROUTE351.fromField = "position"
ROUTE351.fromNode = "Camera.AimPointTest"
ROUTE351.toField = "translation"
ROUTE351.toNode = "CameraShapeTransform"

Transform348.children.append(ROUTE351)
ROUTE352 = x3d.ROUTE()
ROUTE352.fromField = "orientation_changed"
ROUTE352.fromNode = "Camera.AimPointTest"
ROUTE352.toField = "rotation"
ROUTE352.toNode = "CameraShapeTransform"

Transform348.children.append(ROUTE352)
Transform353 = x3d.Transform()
Transform353.DEF = "CameraOffsetTransform"
Transform353.translation = [0,0,0.25]
TouchSensor354 = x3d.TouchSensor()
TouchSensor354.DEF = "CameraShapeTouched"

Transform353.children.append(TouchSensor354)
Inline355 = x3d.Inline()
Inline355.DEF = "CameraShape"
Inline355.url = ["CameraShape.x3d","https://www.web3d.org/x3d/content/examples/Basic/development/CameraShape.x3d"]

Transform353.children.append(Inline355)
Shape356 = x3d.Shape()
Shape356.DEF = "SightLine"
IndexedLineSet357 = x3d.IndexedLineSet()
IndexedLineSet357.coordIndex = [0,1]
Coordinate358 = x3d.Coordinate()
Coordinate358.point = (0.0000,0.0000,0.0000,0.0000,0.0000,-100.0000)

IndexedLineSet357.coord = Coordinate358

Shape356.geometry = IndexedLineSet357
Appearance359 = x3d.Appearance()
Material360 = x3d.Material()
Material360.emissiveColor = [0.8,0.8,0.4]

Appearance359.material = Material360

Shape356.appearance = Appearance359

Transform353.children.append(Shape356)

Transform348.children.append(Transform353)
#Display frustum to show camera view within the scene, toggled by user selecting CameraShape
ExternProtoDeclare361 = x3d.ExternProtoDeclare()
ExternProtoDeclare361.name = "ViewFrustum"
ExternProtoDeclare361.appinfo = "Display view frustum associated with a given pair of Viewpoint NavigationInfo nodes"
ExternProtoDeclare361.url = ["../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum"]
field362 = x3d.field()
field362.name = "ViewpointNode"
field362.accessType = "initializeOnly"
field362.appinfo = "required: insert Viewpoint DEF or USE node for view of interest"
field362.type = "SFNode"

ExternProtoDeclare361.field.append(field362)
field363 = x3d.field()
field363.name = "NavigationInfoNode"
field363.accessType = "initializeOnly"
field363.appinfo = "required: insert NavigationInfo DEF or USE node of interest"
field363.type = "SFNode"

ExternProtoDeclare361.field.append(field363)
field364 = x3d.field()
field364.name = "visible"
field364.accessType = "inputOutput"
field364.appinfo = "whether or not frustum geometry is rendered"
field364.type = "SFBool"

ExternProtoDeclare361.field.append(field364)
field365 = x3d.field()
field365.name = "lineColor"
field365.accessType = "inputOutput"
field365.appinfo = "RGB color of ViewFrustum outline, default value 0.9 0.9 0.9"
field365.type = "SFColor"

ExternProtoDeclare361.field.append(field365)
field366 = x3d.field()
field366.name = "frustumColor"
field366.accessType = "inputOutput"
field366.appinfo = "RGB color of ViewFrustum hull geometry, default value 0.8 0.8 0.8"
field366.type = "SFColor"

ExternProtoDeclare361.field.append(field366)
field367 = x3d.field()
field367.name = "transparency"
field367.accessType = "inputOutput"
field367.appinfo = "transparency of ViewFrustum hull geometry, default value 0.5"
field367.type = "SFFloat"

ExternProtoDeclare361.field.append(field367)
field368 = x3d.field()
field368.name = "aspectRatio"
field368.accessType = "inputOutput"
field368.appinfo = "assumed ratio height/width, default value 0.75"
field368.type = "SFFloat"

ExternProtoDeclare361.field.append(field368)
field369 = x3d.field()
field369.name = "trace"
field369.accessType = "initializeOnly"
field369.appinfo = "debug support, default false"
field369.type = "SFBool"

ExternProtoDeclare361.field.append(field369)

Transform348.children.append(ExternProtoDeclare361)
ProtoInstance370 = x3d.ProtoInstance()
ProtoInstance370.name = "ViewFrustum"
ProtoInstance370.DEF = "ViewFrustumNode"
fieldValue371 = x3d.fieldValue()
fieldValue371.name = "ViewpointNode"
Viewpoint372 = x3d.Viewpoint()
Viewpoint372.DEF = "FrustumViewpoint"
Viewpoint372.description = "viewpoint for ViewFrustum"
Viewpoint372.position = [0,0,0]

fieldValue371.children.append(Viewpoint372)

ProtoInstance370.fieldValue.append(fieldValue371)
fieldValue373 = x3d.fieldValue()
fieldValue373.name = "NavigationInfoNode"
NavigationInfo374 = x3d.NavigationInfo()
NavigationInfo374.DEF = "TestNavigationInfo"
NavigationInfo374.transitionType = ["ANIMATE"]
NavigationInfo374.visibilityLimit = 100

fieldValue373.children.append(NavigationInfo374)

ProtoInstance370.fieldValue.append(fieldValue373)
fieldValue375 = x3d.fieldValue()
fieldValue375.name = "visible"
fieldValue375.value = "false"

ProtoInstance370.fieldValue.append(fieldValue375)
fieldValue376 = x3d.fieldValue()
fieldValue376.name = "lineColor"
fieldValue376.value = "0.9 0.9 0.9"

ProtoInstance370.fieldValue.append(fieldValue376)
fieldValue377 = x3d.fieldValue()
fieldValue377.name = "frustumColor"
fieldValue377.value = "0.8 0.8 0.8"

ProtoInstance370.fieldValue.append(fieldValue377)
fieldValue378 = x3d.fieldValue()
fieldValue378.name = "transparency"
fieldValue378.value = "0.95"

ProtoInstance370.fieldValue.append(fieldValue378)

Transform348.children.append(ProtoInstance370)
BooleanToggle379 = x3d.BooleanToggle()
BooleanToggle379.DEF = "ViewFrustumToggle"

Transform348.children.append(BooleanToggle379)
ROUTE380 = x3d.ROUTE()
ROUTE380.fromField = "isActive"
ROUTE380.fromNode = "CameraShapeTouched"
ROUTE380.toField = "set_boolean"
ROUTE380.toNode = "ViewFrustumToggle"

Transform348.children.append(ROUTE380)
ROUTE381 = x3d.ROUTE()
ROUTE381.fromField = "toggle"
ROUTE381.fromNode = "ViewFrustumToggle"
ROUTE381.toField = "set_visible"
ROUTE381.toNode = "ViewFrustumNode"

Transform348.children.append(ROUTE381)

Scene21.children.append(Transform348)
#=============== add checkerboard, axes and other things to look at while animating ==============
Background382 = x3d.Background()
Background382.skyColor = [0.282353,0.380392,0.470588]

Scene21.children.append(Background382)
Transform383 = x3d.Transform()
Transform383.rotation = [1,0,0,-1.57079]
Transform383.scale = [10,10,10]
Shape384 = x3d.Shape()
Appearance385 = x3d.Appearance()
Material386 = x3d.Material()
Material386.ambientIntensity = 0.01
Material386.diffuseColor = [1,1,1]
Material386.shininess = 0.05

Appearance385.material = Material386

Shape384.appearance = Appearance385
IndexedFaceSet387 = x3d.IndexedFaceSet()
IndexedFaceSet387.colorIndex = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
IndexedFaceSet387.colorPerVertex = False
IndexedFaceSet387.coordIndex = [0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1]
IndexedFaceSet387.normalPerVertex = False
IndexedFaceSet387.solid = False
Coordinate388 = x3d.Coordinate()
Coordinate388.point = (-5.2500,5.2500,0.0000,-3.7500,5.2500,0.0000,-2.2500,5.2500,0.0000,-0.7500,5.2500,0.0000,0.7500,5.2500,0.0000,2.2500,5.2500,0.0000,3.7500,5.2500,0.0000,5.2500,5.2500,0.0000,-5.2500,3.7500,0.0000,-3.7500,3.7500,0.0000,-2.2500,3.7500,0.0000,-0.7500,3.7500,0.0000,0.7500,3.7500,0.0000,2.2500,3.7500,0.0000,3.7500,3.7500,0.0000,5.2500,3.7500,0.0000,-5.2500,2.2500,0.0000,-3.7500,2.2500,0.0000,-2.2500,2.2500,0.0000,-0.7500,2.2500,0.0000,0.7500,2.2500,0.0000,2.2500,2.2500,0.0000,3.7500,2.2500,0.0000,5.2500,2.2500,0.0000,-5.2500,0.7500,0.0000,-3.7500,0.7500,0.0000,-2.2500,0.7500,0.0000,-0.7500,0.7500,0.0000,0.7500,0.7500,0.0000,2.2500,0.7500,0.0000,3.7500,0.7500,0.0000,5.2500,0.7500,0.0000,-5.2500,-0.7500,0.0000,-3.7500,-0.7500,0.0000,-2.2500,-0.7500,0.0000,-0.7500,-0.7500,0.0000,0.7500,-0.7500,0.0000,2.2500,-0.7500,0.0000,3.7500,-0.7500,0.0000,5.2500,-0.7500,0.0000,-5.2500,-2.2500,0.0000,-3.7500,-2.2500,0.0000,-2.2500,-2.2500,0.0000,-0.7500,-2.2500,0.0000,0.7500,-2.2500,0.0000,2.2500,-2.2500,0.0000,3.7500,-2.2500,0.0000,5.2500,-2.2500,0.0000,-5.2500,-3.7500,0.0000,-3.7500,-3.7500,0.0000,-2.2500,-3.7500,0.0000,-0.7500,-3.7500,0.0000,0.7500,-3.7500,0.0000,2.2500,-3.7500,0.0000,3.7500,-3.7500,0.0000,5.2500,-3.7500,0.0000,-5.2500,-5.2500,0.0000,-3.7500,-5.2500,0.0000,-2.2500,-5.2500,0.0000,-0.7500,-5.2500,0.0000,0.7500,-5.2500,0.0000,2.2500,-5.2500,0.0000,3.7500,-5.2500,0.0000,5.2500,-5.2500,0.0000)

IndexedFaceSet387.coord = Coordinate388
Color389 = x3d.Color()
Color389.color = [0.435294,0.741176,0,0,0.560784,0.580392]

IndexedFaceSet387.color = Color389

Shape384.geometry = IndexedFaceSet387

Transform383.children.append(Shape384)

Scene21.children.append(Transform383)
Transform390 = x3d.Transform()
Transform390.scale = [3,3,3]
Transform390.translation = [0,0.25,0]
Inline391 = x3d.Inline()
Inline391.DEF = "CoordinateAxes"
Inline391.url = ["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../Savage/Tools/Authoring/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../Savage/Tools/Authoring/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"]

Transform390.children.append(Inline391)

Scene21.children.append(Transform390)
Transform392 = x3d.Transform()
Transform392.DEF = "MovingBoxTransform"
PositionInterpolator393 = x3d.PositionInterpolator()
PositionInterpolator393.DEF = "BoxPath"
PositionInterpolator393.key = [0,0.25,0.5,0.75,1]
PositionInterpolator393.keyValue = (-5.0000,1.0000,5.0000,45.0000,1.0000,5.0000,45.0000,1.0000,-45.0000,-5.0000,1.0000,-45.0000,-5.0000,1.0000,5.0000)

Transform392.children.append(PositionInterpolator393)
TimeSensor394 = x3d.TimeSensor()
TimeSensor394.DEF = "BoxTimer"
TimeSensor394.cycleInterval = 10
TimeSensor394.loop = True

Transform392.children.append(TimeSensor394)
ROUTE395 = x3d.ROUTE()
ROUTE395.fromField = "value_changed"
ROUTE395.fromNode = "BoxPath"
ROUTE395.toField = "translation"
ROUTE395.toNode = "MovingBoxTransform"

Transform392.children.append(ROUTE395)
ROUTE396 = x3d.ROUTE()
ROUTE396.fromField = "value_changed"
ROUTE396.fromNode = "BoxPath"
ROUTE396.toField = "goalAimPoint"
ROUTE396.toNode = "MoveAimPoint3.1"

Transform392.children.append(ROUTE396)
ROUTE397 = x3d.ROUTE()
ROUTE397.fromField = "value_changed"
ROUTE397.fromNode = "BoxPath"
ROUTE397.toField = "goalAimPoint"
ROUTE397.toNode = "MoveAimPoint3.2"

Transform392.children.append(ROUTE397)
ROUTE398 = x3d.ROUTE()
ROUTE398.fromField = "value_changed"
ROUTE398.fromNode = "BoxPath"
ROUTE398.toField = "goalAimPoint"
ROUTE398.toNode = "MoveAimPoint3.3"

Transform392.children.append(ROUTE398)
ROUTE399 = x3d.ROUTE()
ROUTE399.fromField = "fraction_changed"
ROUTE399.fromNode = "BoxTimer"
ROUTE399.toField = "set_fraction"
ROUTE399.toNode = "BoxPath"

Transform392.children.append(ROUTE399)
Shape400 = x3d.Shape()
Box401 = x3d.Box()

Shape400.geometry = Box401
Appearance402 = x3d.Appearance()
Material403 = x3d.Material()

Appearance402.material = Material403
ImageTexture404 = x3d.ImageTexture()
ImageTexture404.url = ["../earth-topo.png","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.png"]

Appearance402.texture = ImageTexture404

Shape400.appearance = Appearance402

Transform392.children.append(Shape400)

Scene21.children.append(Transform392)
#================ CrossHair visualization for center of screen ================
ExternProtoDeclare405 = x3d.ExternProtoDeclare()
ExternProtoDeclare405.name = "CrossHair"
ExternProtoDeclare405.appinfo = "CrossHair prototype provides a heads-up display (HUD) crosshair at the view center, which is useful for assessing NavigationInfo lookAt point"
ExternProtoDeclare405.url = ["../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair"]
field406 = x3d.field()
field406.name = "enabled"
field406.accessType = "initializeOnly"
field406.appinfo = "whether CrissHair orititype is enabled or not"
field406.type = "SFBool"

ExternProtoDeclare405.field.append(field406)
field407 = x3d.field()
field407.name = "set_enabled"
field407.accessType = "inputOnly"
field407.appinfo = "control whether enabled/disabled"
field407.type = "SFBool"

ExternProtoDeclare405.field.append(field407)
field408 = x3d.field()
field408.name = "markerColor"
field408.accessType = "inputOutput"
field408.appinfo = "color of CrossHair marker"
field408.type = "SFColor"

ExternProtoDeclare405.field.append(field408)
field409 = x3d.field()
field409.name = "scale"
field409.accessType = "inputOutput"
field409.appinfo = "size of CrossHair in meters"
field409.type = "SFVec3f"

ExternProtoDeclare405.field.append(field409)
field410 = x3d.field()
field410.name = "positionOffsetFromCamera"
field410.accessType = "inputOutput"
field410.appinfo = "distance in front of HUD viewpoint"
field410.type = "SFVec3f"

ExternProtoDeclare405.field.append(field410)

Scene21.children.append(ExternProtoDeclare405)
ProtoInstance411 = x3d.ProtoInstance()
ProtoInstance411.name = "CrossHair"
ProtoInstance411.DEF = "CrossHairInstance"
fieldValue412 = x3d.fieldValue()
fieldValue412.name = "enabled"
fieldValue412.value = "true"

ProtoInstance411.fieldValue.append(fieldValue412)
fieldValue413 = x3d.fieldValue()
fieldValue413.name = "markerColor"
fieldValue413.value = "1 0.5 0"

ProtoInstance411.fieldValue.append(fieldValue413)
fieldValue414 = x3d.fieldValue()
fieldValue414.name = "scale"
fieldValue414.value = "1 1 1"

ProtoInstance411.fieldValue.append(fieldValue414)
fieldValue415 = x3d.fieldValue()
fieldValue415.name = "positionOffsetFromCamera"
fieldValue415.value = "0 0 -6"

ProtoInstance411.fieldValue.append(fieldValue415)

Scene21.children.append(ProtoInstance411)
#turn on CrossHairInstance when animated camera viewpoints are bound
ROUTE416 = x3d.ROUTE()
ROUTE416.fromField = "isBound"
ROUTE416.fromNode = "Camera.SimpleShotsTest"
ROUTE416.toField = "set_enabled"
ROUTE416.toNode = "CrossHairInstance"

Scene21.children.append(ROUTE416)
ROUTE417 = x3d.ROUTE()
ROUTE417.fromField = "isBound"
ROUTE417.fromNode = "Camera.AimPointTest"
ROUTE417.toField = "set_enabled"
ROUTE417.toNode = "CrossHairInstance"

Scene21.children.append(ROUTE417)
#turn off CrossHairInstance when animated camera viewpoints are unbound <BooleanFilter DEF='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.SimpleShotsTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.AimPointTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='inputNegate' fromNode='NegateCrossHair' toField='set_enabled' toNode='CrossHairInstance'/>
#=============== TODO Launch Prototype Example ==============
Anchor418 = x3d.Anchor()
Anchor418.description = "launch CameraExample scene"
Anchor418.parameter = ["target=_blank"]
Anchor418.url = ["CameraExample.x3d","https://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.x3d","CameraExample.wrl","https://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.wrl"]
Transform419 = x3d.Transform()
Transform419.translation = [0,-3,0]
Shape420 = x3d.Shape()
Text421 = x3d.Text()
Text421.string = ["CameraPrototype","defines a prototype","","Click on this text to see","CameraExample scene"]
FontStyle422 = x3d.FontStyle()
FontStyle422.justify = ["MIDDLE","MIDDLE"]
FontStyle422.size = 0.5

Text421.fontStyle = FontStyle422

Shape420.geometry = Text421
Appearance423 = x3d.Appearance()
Material424 = x3d.Material()
Material424.diffuseColor = [1,1,0.2]

Appearance423.material = Material424

Shape420.appearance = Appearance423

Transform419.children.append(Shape420)

Anchor418.children.append(Transform419)

Scene21.children.append(Anchor418)

X3D0.Scene = Scene21
f = open("././CameraExamples_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
