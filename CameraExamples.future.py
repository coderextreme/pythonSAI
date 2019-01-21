import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("CameraExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Camera, CameraShot and CameraMove examples that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.") \
    ) \
    .addMeta(metaObject() \
     .setName("documentation") \
     .setContent("Two demos are found in the scene, click the \"red text\" on left or right to start. (a) SimpleShotsTest shows Zoom in/out, Pan left/right, Boom up/down, Tilt left/right, with each is defined by a CameraShot collecting a series of CameraMovements. (b) AimPointTest gradually slews the camera view to look at the sliding cube, then follows it around before returning to original viewpoint.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman and Jeff Weekley") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("18 June 2009") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("12 January 2014") \
    ) \
    .addMeta(metaObject() \
     .setName("TODO") \
     .setContent("Schematron rules, backed up by initialize() checks") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("BeyondViewpointCameraNodesWeb3D2009.pdf") \
    ) \
    .addMeta(metaObject() \
     .setName("MovingImage") \
     .setContent("CameraExamplesDemo.mp4") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("Camera nodes for Viewpoint navigation control") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("CameraPrototypes.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("CameraExamplesConsoleLog.txt") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.avi") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
.addComments(CommentsBlock("""TODO warn if more than one identifier present""")) \
   ) \
   .setScene(SceneObject() \
.addComments(CommentsBlock("""=============== Camera ==============""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("Camera") \
     .setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images") \
     .setUrl(["CameraPrototypes.x3d#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#Camera","CameraPrototypes.wrl#Camera","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#Camera"]) \
.addComments(CommentsBlock("""Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields""")) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFSTRING) \
      .setName("description") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Text description to be displayed for this Camera") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("position") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFROTATION) \
      .setName("orientation") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("fieldOfView") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("pi/4") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("set_fraction") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setAppinfo("input fraction drives interpolators") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("set_bind") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setAppinfo("input event binds or unbinds this Camera") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("bindTime") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("output event indicates when this Camera is bound") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("isBound") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("output event indicates whether this Camera is bound or unbound") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("nearClipPlane") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("farClipPlane") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFNODE) \
      .setName("shots") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("headlight") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Whether camera headlight is on or off") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFCOLOR) \
      .setName("headlightColor") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera headlight color") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("headlightIntensity") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera headlight intensity") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFCOLOR) \
      .setName("filterColor") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera filter color that modifies virtual lens capture") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("filterTransparency") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Camera filter transparency that modifies virtual lens capture") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("upVector") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("upVector changes modify camera orientation (and possibly vice versa)") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("fStop") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("focusDistance") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Distance to focal plane of sharpest focus") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("isActive") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("totalDuration") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFNODE) \
      .setName("offlineRender") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("OfflineRender node") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("traceEnabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("enable console output to trace script computations and prototype progress") \
     ) \
    ) \
.addComments(CommentsBlock("""=============== CameraShot ==============""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("CameraShot") \
     .setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot") \
     .setUrl(["CameraPrototypes.x3d#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraShot","CameraPrototypes.wrl#CameraShot","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraShot"]) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFSTRING) \
      .setName("description") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Text description to be displayed for this CameraShot") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("enabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Whether this CameraShot can be activated") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFNODE) \
      .setName("moves") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Set of CameraMovement nodes") \
.addComments(CommentsBlock("""initializing CameraMovement nodes are inserted here by scene author using ProtoInstance""")) \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("initialPosition") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Setup to reinitialize camera position for this shot") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFROTATION) \
      .setName("initialOrientation") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Setup to reinitialize camera rotation for this shot") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("initialAimPoint") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("initialFieldOfView") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("pi/4") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("initialFStop") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("initialFocusDistance") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Distance to focal plane of sharpest focus") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("shotDuration") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Subtotal duration of contained CameraMovement move durations") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("isActive") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("traceEnabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("enable console output to trace script computations and prototype progress") \
     ) \
    ) \
.addComments(CommentsBlock("""=============== CameraMovement ==============""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("CameraMovement") \
     .setAppinfo("CameraMovement defines a single camera movement animation") \
     .setUrl(["CameraPrototypes.x3d#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#CameraMovement","CameraPrototypes.wrl#CameraMovement","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#CameraMovement"]) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFSTRING) \
      .setName("description") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Text description to be displayed for this CameraMovement") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("enabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Whether this CameraMovement can be activated") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("duration") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Duration in seconds for this move") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("goalPosition") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Goal camera position for this move") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFROTATION) \
      .setName("goalOrientation") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Goal camera rotation for this move") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("tracking") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Whether or not camera direction is tracking towards the aimPoint") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("goalAimPoint") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Goal aimPoint for this move, ignored if tracking=false") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("goalFieldOfView") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Goal fieldOfView for this move") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("goalFStop") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("goalFocusDistance") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Distance to focal plane of sharpest focus") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("isActive") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("traceEnabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("enable console output to trace script computations and prototype progress") \
     ) \
    ) \
.addComments(CommentsBlock("""=============== OfflineRender ==============""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("OfflineRender") \
     .setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)") \
     .setUrl(["CameraPrototypes.x3d#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d#OfflineRender","CameraPrototypes.wrl#OfflineRender","http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.wrl#OfflineRender"]) \
.addComments(CommentsBlock("""TODO non-photorealistic rendering (NPR) parameters""")) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFSTRING) \
      .setName("description") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Text description to be displayed for this OfflineRender") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("enabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Whether this OfflineRender can be activated") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("frameRate") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Frames per second recorded for this rendering") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC2F) \
      .setName("frameSize") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Size of frame in number of pixels width and height") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("pixelAspectRatio") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("set_startTime") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setAppinfo("Begin render operation") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("progress") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Progress performing render operation (0..1)") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("renderCompleteTime") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("Render operation complete") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFSTRING) \
      .setName("movieFormat") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("Format of rendered output movie (mpeg mp4 etc.), use first supported format") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFSTRING) \
      .setName("imageFormat") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("traceEnabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("enable console output to trace script computations and prototype progress") \
     ) \
    ) \
.addComments(CommentsBlock("""=============== Lights, camera, action! ==============""")) \
    .addChild(DirectionalLightObject() \
     .setDirection([0,-1,0]) \
     .setGlobal(True) \
     .setIntensity(0.8) \
    ) \
    .addChild(NavigationInfoObject() \
     .setType(["EXAMINE","FLY","ANY"]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Camera test scene entry view") \
     .setPosition([0,2,12]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Camera test scene from above") \
     .setOrientation([1,0,0,-1.57079]) \
     .setPosition([0,150,0]) \
    ) \
.addComments(CommentsBlock("""Keep prototype instances in same file while developing, then move later""")) \
.addComments(CommentsBlock("""We will create examples matching those in the paper""")) \
.addComments(CommentsBlock("""=============== Camera.SimpleShotsTest ==============""")) \
    .addChild(ProtoInstanceObject() \
     .setName("Camera") \
     .setDEF("Camera.SimpleShotsTest") \
     .addFieldValue(fieldValueObject() \
      .setName("description") \
      .setValue("SimpleShotsTest for camera Zoom Dolly Pan Boom and Tilt") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("headlight") \
      .setValue("true") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("position") \
      .setValue("-4 4 10") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("shots") \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("Zoom") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("Simple shot of Camera Zoom") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("-50 1 -10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 1 0 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Zoom In") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-50 1 -15") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Zoom Out") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-50 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-50 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
       ) \
      ) \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("Dolly") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("Simple shot of Camera Dolly") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("-40 1 -10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 1 0 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("DollyMove1") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Dolly from Right to Left") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-45 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Dolly from Left to Right") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-40 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-40 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
       ) \
      ) \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("Pan") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("Simple shot of Camera Pan left right and back to center") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("-30 1 -10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 1 0 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("PanLeft") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Pan Left") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("2") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-30 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0.4") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("PanRight") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Pan Right") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-30 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 -0.4") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Pan back to Center") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("2") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-30 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("2") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-30 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
       ) \
      ) \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("CameraBoom") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("Camera Boom") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("-20 1 -10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 1 0 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("CameraBoomUp") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Boom Up") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-20 5 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("BoomDown") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Boom Down") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-20 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("BoomPause") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("2") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-20 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
        ) \
       ) \
      ) \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("CameraTilt") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("Camera Tilt") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("-10 1 -10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 0 1 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("traceEnabled") \
        .setValue("true") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("TiltDown") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Left") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 0.785") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("TiltPause") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 0.785") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Right") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 -0.785") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Pause") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 -0.785") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("TiltReset") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Camera Tilt Reset") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("1") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("-10 1 -10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 0") \
         ) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("TiltUp") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("Return to home") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("2") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("0 2 12") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 0 1 0") \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(GroupObject() \
     .setDEF("AnimationGroup.SimpleShots") \
     .addChild(TimeSensorObject() \
      .setDEF("CameraTimer.SimpleShots") \
     ) \
.addComments(CommentsBlock("""initialize clock to match totalDuration of combined Shot Moves""")) \
     .addChild(ROUTEObject() \
      .setFromField("totalDuration") \
      .setFromNode("Camera.SimpleShotsTest") \
      .setToField("cycleInterval") \
      .setToNode("CameraTimer.SimpleShots") \
     ) \
.addComments(CommentsBlock("""TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator""")) \
     .addChild(ROUTEObject() \
      .setFromField("fraction_changed") \
      .setFromNode("CameraTimer.SimpleShots") \
      .setToField("set_fraction") \
      .setToNode("Camera.SimpleShotsTest") \
     ) \
     .addChild(TransformObject() \
      .setDEF("Trigger.SimpleShots") \
      .setTranslation([-4,4,0]) \
      .addChild(BooleanFilterObject() \
       .setDEF("TextTouchActive.SimpleShotsFilter") \
      ) \
      .addChild(TouchSensorObject() \
       .setDEF("TextTouch.SimpleShots") \
       .setDescription("touch to animate Camera SimpleShotsTest") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("inputTrue") \
       .setFromNode("TextTouchActive.SimpleShotsFilter") \
       .setToField("set_bind") \
       .setToNode("Camera.SimpleShotsTest") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("TextTouch.SimpleShots") \
       .setToField("set_boolean") \
       .setToNode("TextTouchActive.SimpleShotsFilter") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("touchTime") \
       .setFromNode("TextTouch.SimpleShots") \
       .setToField("startTime") \
       .setToNode("CameraTimer.SimpleShots") \
      ) \
      .addChild(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["Click to animate","SimpleShotsTest"]) \
        .setFontStyle(FontStyleObject() \
         .setJustify(["MIDDLE","MIDDLE"]) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDEF("ArtDeco5") \
         .setAmbientIntensity(0.24) \
         .setDiffuseColor([0.945455,0.318988,0.321717]) \
         .setShininess(0.01) \
         .setSpecularColor([0.072727,0.021705,0.010732]) \
.addComments(CommentsBlock("""Universal Media Library: ArtDeco 5""")) \
        ) \
       ) \
      ) \
.addComments(CommentsBlock("""Simplify intersection test for user selecting text""")) \
      .addChild(ShapeObject() \
       .setDEF("TransparentBox") \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setTransparency(1) \
        ) \
       ) \
       .setGeometry(BoxObject() \
        .setSize([6,2,0.0001]) \
       ) \
      ) \
     ) \
    ) \
    .addChild(GroupObject() \
     .setDEF("SimpleShotsTargets") \
     .addChild(TransformObject() \
      .setDEF("TargetBoxZoom") \
      .setTranslation([-50,1,-20]) \
      .addChild(ShapeObject() \
       .setGeometry(BoxObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/CameraMoveZoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveZoom.png"]) \
        ) \
       ) \
      ) \
      .addChild(TransformObject() \
       .setTranslation([0,2,0]) \
       .addChild(ShapeObject() \
        .setGeometry(TextObject() \
         .setString(["Zoom in, out"]) \
         .setFontStyle(FontStyleObject() \
          .setJustify(["MIDDLE","MIDDLE"]) \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
         ) \
        ) \
       ) \
      ) \
     ) \
     .addChild(TransformObject() \
      .setDEF("TargetBoxDolly") \
      .setTranslation([-40,1,-20]) \
      .addChild(ShapeObject() \
       .setGeometry(BoxObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/CameraMoveDolly.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveDolly.png"]) \
        ) \
       ) \
      ) \
      .addChild(TransformObject() \
       .setTranslation([0,2,0]) \
       .addChild(ShapeObject() \
        .setGeometry(TextObject() \
         .setString(["Dolly left, right"]) \
         .setFontStyle(FontStyleObject() \
          .setJustify(["MIDDLE","MIDDLE"]) \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
         ) \
        ) \
       ) \
      ) \
     ) \
     .addChild(TransformObject() \
      .setDEF("TargetBoxPan") \
      .setTranslation([-30,1,-20]) \
      .addChild(ShapeObject() \
       .setGeometry(BoxObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/CameraMovePan.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMovePan.png"]) \
        ) \
       ) \
      ) \
      .addChild(TransformObject() \
       .setTranslation([0,2,0]) \
       .addChild(ShapeObject() \
        .setGeometry(TextObject() \
         .setString(["Pan left, right"]) \
         .setFontStyle(FontStyleObject() \
          .setJustify(["MIDDLE","MIDDLE"]) \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
         ) \
        ) \
       ) \
      ) \
     ) \
     .addChild(TransformObject() \
      .setDEF("TargetBoxBoom") \
      .setTranslation([-20,1,-20]) \
      .addChild(ShapeObject() \
       .setGeometry(BoxObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/CameraMoveBoom.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveBoom.png"]) \
        ) \
       ) \
      ) \
      .addChild(TransformObject() \
       .setTranslation([0,2,0]) \
       .addChild(ShapeObject() \
        .setGeometry(TextObject() \
         .setString(["Boom up, down"]) \
         .setFontStyle(FontStyleObject() \
          .setJustify(["MIDDLE","MIDDLE"]) \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
         ) \
        ) \
       ) \
      ) \
     ) \
     .addChild(TransformObject() \
      .setDEF("TargetBoxTilt") \
      .setTranslation([-10,1,-20]) \
      .addChild(ShapeObject() \
       .setGeometry(BoxObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/CameraMoveTilt.png","http://www.web3d.org/x3d/content/examples/Basic/development/images/CameraMoveTilt.png"]) \
        ) \
       ) \
      ) \
      .addChild(TransformObject() \
       .setTranslation([0,2,0]) \
       .addChild(ShapeObject() \
        .setGeometry(TextObject() \
         .setString(["Tilt left, right"]) \
         .setFontStyle(FontStyleObject() \
          .setJustify(["MIDDLE","MIDDLE"]) \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
.addComments(CommentsBlock("""=============== Camera.AimPointTest ==============""")) \
    .addChild(ProtoInstanceObject() \
     .setName("Camera") \
     .setDEF("Camera.AimPointTest") \
     .addFieldValue(fieldValueObject() \
      .setName("description") \
      .setValue("AimPointTest for moving camera tracking moving target") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("position") \
      .setValue("4 4 10") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("shots") \
      .addChild(ProtoInstanceObject() \
       .setName("CameraShot") \
       .setDEF("Shot5") \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("#3 Tracking shot") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialPosition") \
        .setValue("6 6 10") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("initialOrientation") \
        .setValue("0 1 0 0") \
       ) \
       .addFieldValue(fieldValueObject() \
        .setName("moves") \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("MoveAimPoint3.1") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("AimPoint 3.1 moving BoxPath") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("tracking") \
          .setValue("true") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("8") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("6 6 10") \
         ) \
.addComments(CommentsBlock("""goalAimPoint modified by ROUTE to match moving Box""")) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("MoveAimPoint3.2") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("AimPoint 3.2 pan right while tracking") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("tracking") \
          .setValue("true") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("8") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("40 6 12") \
         ) \
.addComments(CommentsBlock("""goalAimPoint modified by ROUTE to match moving Box""")) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("MoveAimPoint3.3") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("AimPoint 3.3 boom up while tracking") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("tracking") \
          .setValue("true") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("3") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("40 20 13") \
         ) \
.addComments(CommentsBlock("""goalAimPoint modified by ROUTE to match moving Box""")) \
        ) \
        .addChild(ProtoInstanceObject() \
         .setName("CameraMovement") \
         .setDEF("MoveAimPoint3.4") \
         .addFieldValue(fieldValueObject() \
          .setName("description") \
          .setValue("AimPoint 3.4 restore camera back to home") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("tracking") \
          .setValue("true") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("duration") \
          .setValue("5") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalPosition") \
          .setValue("4 4 10") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalAimPoint") \
          .setValue("4 4 0") \
         ) \
         .addFieldValue(fieldValueObject() \
          .setName("goalOrientation") \
          .setValue("0 1 0 0") \
         ) \
.addComments(CommentsBlock("""can test tracking or not using following values""")) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(GroupObject() \
     .setDEF("AnimationGroup.AimPointTest") \
     .addChild(TimeSensorObject() \
      .setDEF("CameraTimer.AimPointTest") \
     ) \
.addComments(CommentsBlock("""initialize clock to match totalDuration of combined Shot Moves""")) \
     .addChild(ROUTEObject() \
      .setFromField("totalDuration") \
      .setFromNode("Camera.AimPointTest") \
      .setToField("cycleInterval") \
      .setToNode("CameraTimer.AimPointTest") \
     ) \
.addComments(CommentsBlock("""TimeSensor animates the CameraClock since that maintains the computed PositionInterpolator and OrientationInterpolator""")) \
     .addChild(ROUTEObject() \
      .setFromField("fraction_changed") \
      .setFromNode("CameraTimer.AimPointTest") \
      .setToField("set_fraction") \
      .setToNode("Camera.AimPointTest") \
     ) \
     .addChild(TransformObject() \
      .setDEF("Trigger.AimPointTest") \
      .setTranslation([4,4,0]) \
      .addChild(BooleanFilterObject() \
       .setDEF("TextTouchActive.AimPointFilter") \
      ) \
      .addChild(TouchSensorObject() \
       .setDEF("TextTouch.AimPointTest") \
       .setDescription("touch to animate Camera AimPointTest") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("inputTrue") \
       .setFromNode("TextTouchActive.AimPointFilter") \
       .setToField("set_bind") \
       .setToNode("Camera.AimPointTest") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("TextTouch.AimPointTest") \
       .setToField("set_boolean") \
       .setToNode("TextTouchActive.AimPointFilter") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("touchTime") \
       .setFromNode("TextTouch.AimPointTest") \
       .setToField("startTime") \
       .setToNode("CameraTimer.AimPointTest") \
      ) \
      .addChild(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["Click to animate","AimPointTest"]) \
        .setFontStyle(FontStyleObject() \
         .setJustify(["MIDDLE","MIDDLE"]) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setUSE("ArtDeco5") \
        ) \
       ) \
      ) \
      .addChild(ShapeObject() \
       .setUSE("TransparentBox") \
      ) \
     ) \
    ) \
.addComments(CommentsBlock("""TODO build a test once implemented""")) \
    .addChild(ProtoInstanceObject() \
     .setName("OfflineRender") \
    ) \
.addComments(CommentsBlock("""=============== animate a camera shape to visualize view changes ==============""")) \
    .addChild(TransformObject() \
     .setDEF("CameraShapeTransform") \
     .setTranslation([0,0.5,0]) \
.addComments(CommentsBlock("""move CameraShape using active Camera""")) \
     .addChild(ROUTEObject() \
      .setFromField("position_changed") \
      .setFromNode("Camera.SimpleShotsTest") \
      .setToField("translation") \
      .setToNode("CameraShapeTransform") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("orientation_changed") \
      .setFromNode("Camera.SimpleShotsTest") \
      .setToField("rotation") \
      .setToNode("CameraShapeTransform") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("position") \
      .setFromNode("Camera.AimPointTest") \
      .setToField("translation") \
      .setToNode("CameraShapeTransform") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("orientation_changed") \
      .setFromNode("Camera.AimPointTest") \
      .setToField("rotation") \
      .setToNode("CameraShapeTransform") \
     ) \
     .addChild(TransformObject() \
      .setDEF("CameraOffsetTransform") \
      .setTranslation([0,0,0.25]) \
      .addChild(TouchSensorObject() \
       .setDEF("CameraShapeTouched") \
      ) \
      .addChild(InlineObject() \
       .setDEF("CameraShape") \
       .setUrl(["CameraShape.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraShape.x3d"]) \
      ) \
      .addChild(ShapeObject() \
       .setDEF("SightLine") \
       .setGeometry(IndexedLineSetObject() \
        .setCoordIndex([0,1]) \
        .setCoord(CoordinateObject() \
         .setPoint([0,0,0,0,0,-100]) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setEmissiveColor([0.8,0.8,0.4]) \
        ) \
       ) \
      ) \
     ) \
.addComments(CommentsBlock("""Display frustum to show camera view within the scene, toggled by user selecting CameraShape""")) \
     .addChild(ExternProtoDeclareObject() \
      .setName("ViewFrustum") \
      .setAppinfo("Display view frustum associated with a given pair of Viewpoint NavigationInfo nodes") \
      .setUrl(["../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.x3d#ViewFrustum","../../X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ViewFrustumPrototype.wrl#ViewFrustum"]) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFNODE) \
       .setName("ViewpointNode") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("required: insert Viewpoint DEF or USE node for view of interest") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFNODE) \
       .setName("NavigationInfoNode") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("required: insert NavigationInfo DEF or USE node of interest") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("visible") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("whether or not frustum geometry is rendered") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("lineColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("RGB color of ViewFrustum outline, default value 0.9 0.9 0.9") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("frustumColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("RGB color of ViewFrustum hull geometry, default value 0.8 0.8 0.8") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("transparency") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("transparency of ViewFrustum hull geometry, default value 0.5") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("aspectRatio") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("assumed ratio height/width, default value 0.75") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("trace") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("debug support, default false") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("ViewFrustum") \
      .setDEF("ViewFrustumNode") \
      .addFieldValue(fieldValueObject() \
       .setName("ViewpointNode") \
       .addChild(ViewpointObject() \
        .setDEF("FrustumViewpoint") \
        .setDescription("viewpoint for ViewFrustum") \
        .setPosition([0,0,0]) \
       ) \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("NavigationInfoNode") \
       .addChild(NavigationInfoObject() \
        .setDEF("TestNavigationInfo") \
        .setTransitionType(["ANIMATE"]) \
        .setVisibilityLimit(100) \
       ) \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("visible") \
       .setValue("false") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("lineColor") \
       .setValue("0.9 0.9 0.9") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("frustumColor") \
       .setValue("0.8 0.8 0.8") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("transparency") \
       .setValue("0.95") \
      ) \
     ) \
     .addChild(BooleanToggleObject() \
      .setDEF("ViewFrustumToggle") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("isActive") \
      .setFromNode("CameraShapeTouched") \
      .setToField("set_boolean") \
      .setToNode("ViewFrustumToggle") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("toggle") \
      .setFromNode("ViewFrustumToggle") \
      .setToField("set_visible") \
      .setToNode("ViewFrustumNode") \
     ) \
    ) \
.addComments(CommentsBlock("""=============== add checkerboard, axes and other things to look at while animating ==============""")) \
    .addChild(BackgroundObject() \
     .setSkyColor([0.282353,0.380392,0.470588]) \
    ) \
    .addChild(TransformObject() \
     .setRotation([1,0,0,-1.57079]) \
     .setScale([10,10,10]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setAmbientIntensity(0.01) \
        .setDiffuseColor([1,1,1]) \
        .setShininess(0.05) \
       ) \
      ) \
      .setGeometry(IndexedFaceSetObject() \
       .setColorIndex([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]) \
       .setColorPerVertex(False) \
       .setCoordIndex([0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1]) \
       .setNormalPerVertex(False) \
       .setSolid(False) \
       .setCoord(CoordinateObject() \
        .setPoint([-5.25,5.25,0,-3.75,5.25,0,-2.25,5.25,0,-0.75,5.25,0,0.75,5.25,0,2.25,5.25,0,3.75,5.25,0,5.25,5.25,0,-5.25,3.75,0,-3.75,3.75,0,-2.25,3.75,0,-0.75,3.75,0,0.75,3.75,0,2.25,3.75,0,3.75,3.75,0,5.25,3.75,0,-5.25,2.25,0,-3.75,2.25,0,-2.25,2.25,0,-0.75,2.25,0,0.75,2.25,0,2.25,2.25,0,3.75,2.25,0,5.25,2.25,0,-5.25,0.75,0,-3.75,0.75,0,-2.25,0.75,0,-0.75,0.75,0,0.75,0.75,0,2.25,0.75,0,3.75,0.75,0,5.25,0.75,0,-5.25,-0.75,0,-3.75,-0.75,0,-2.25,-0.75,0,-0.75,-0.75,0,0.75,-0.75,0,2.25,-0.75,0,3.75,-0.75,0,5.25,-0.75,0,-5.25,-2.25,0,-3.75,-2.25,0,-2.25,-2.25,0,-0.75,-2.25,0,0.75,-2.25,0,2.25,-2.25,0,3.75,-2.25,0,5.25,-2.25,0,-5.25,-3.75,0,-3.75,-3.75,0,-2.25,-3.75,0,-0.75,-3.75,0,0.75,-3.75,0,2.25,-3.75,0,3.75,-3.75,0,5.25,-3.75,0,-5.25,-5.25,0,-3.75,-5.25,0,-2.25,-5.25,0,-0.75,-5.25,0,0.75,-5.25,0,2.25,-5.25,0,3.75,-5.25,0,5.25,-5.25,0]) \
       ) \
       .setColor(ColorObject() \
        .setColor([0.435294,0.741176,0,0,0.560784,0.580392]) \
       ) \
      ) \
     ) \
    ) \
    .addChild(TransformObject() \
     .setScale([3,3,3]) \
     .setTranslation([0,0.25,0]) \
     .addChild(InlineObject() \
      .setDEF("CoordinateAxes") \
      .setUrl(["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../Savage/Tools/Authoring/CoordinateAxes.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../Savage/Tools/Authoring/CoordinateAxes.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"]) \
     ) \
    ) \
    .addChild(TransformObject() \
     .setDEF("MovingBoxTransform") \
     .addChild(PositionInterpolatorObject() \
      .setDEF("BoxPath") \
      .setKey([0,0.25,0.5,0.75,1]) \
      .setKeyValue([-5,1,5,45,1,5,45,1,-45,-5,1,-45,-5,1,5]) \
     ) \
     .addChild(TimeSensorObject() \
      .setDEF("BoxTimer") \
      .setCycleInterval(10) \
      .setLoop(True) \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("BoxPath") \
      .setToField("translation") \
      .setToNode("MovingBoxTransform") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("BoxPath") \
      .setToField("goalAimPoint") \
      .setToNode("MoveAimPoint3.1") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("BoxPath") \
      .setToField("goalAimPoint") \
      .setToNode("MoveAimPoint3.2") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("BoxPath") \
      .setToField("goalAimPoint") \
      .setToNode("MoveAimPoint3.3") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("fraction_changed") \
      .setFromNode("BoxTimer") \
      .setToField("set_fraction") \
      .setToNode("BoxPath") \
     ) \
     .addChild(ShapeObject() \
      .setGeometry(BoxObject() \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
       ) \
       .setTexture(ImageTextureObject() \
        .setUrl(["../earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png"]) \
       ) \
      ) \
     ) \
    ) \
.addComments(CommentsBlock("""================ CrossHair visualization for center of screen ================""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("CrossHair") \
     .setAppinfo("CrossHair prototype provides a heads-up display (HUD) crosshair at the view center, which is useful for assessing NavigationInfo lookAt point") \
     .setUrl(["../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.x3d#CrossHair","../../Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/CrossHairPrototype.wrl#CrossHair"]) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("enabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      .setAppinfo("whether CrissHair orititype is enabled or not") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("set_enabled") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setAppinfo("control whether enabled/disabled") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFCOLOR) \
      .setName("markerColor") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("color of CrossHair marker") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("scale") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("size of CrossHair in meters") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("positionOffsetFromCamera") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("distance in front of HUD viewpoint") \
     ) \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("CrossHair") \
     .setDEF("CrossHairInstance") \
     .addFieldValue(fieldValueObject() \
      .setName("enabled") \
      .setValue("true") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("markerColor") \
      .setValue("1 0.5 0") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("scale") \
      .setValue("1 1 1") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("positionOffsetFromCamera") \
      .setValue("0 0 -6") \
     ) \
    ) \
.addComments(CommentsBlock("""turn on CrossHairInstance when animated camera viewpoints are bound""")) \
    .addChild(ROUTEObject() \
     .setFromField("isBound") \
     .setFromNode("Camera.SimpleShotsTest") \
     .setToField("set_enabled") \
     .setToNode("CrossHairInstance") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("isBound") \
     .setFromNode("Camera.AimPointTest") \
     .setToField("set_enabled") \
     .setToNode("CrossHairInstance") \
    ) \
.addComments(CommentsBlock("""turn off CrossHairInstance when animated camera viewpoints are unbound <BooleanFilter DEF='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.SimpleShotsTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='isBound' fromNode='Camera.AimPointTest' toField='set_boolean' toNode='NegateCrossHair'/> <ROUTE fromField='inputNegate' fromNode='NegateCrossHair' toField='set_enabled' toNode='CrossHairInstance'/>""")) \
.addComments(CommentsBlock("""=============== TODO Launch Prototype Example ==============""")) \
    .addChild(AnchorObject() \
     .setDescription("launch CameraExample scene") \
     .setParameter(["target=_blank"]) \
     .setUrl(["CameraExample.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.x3d","CameraExample.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExample.wrl"]) \
     .addChild(TransformObject() \
      .setTranslation([0,-3,0]) \
      .addChild(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["CameraPrototype","defines a prototype","","Click on this text to see","CameraExample scene"]) \
        .setFontStyle(FontStyleObject() \
         .setJustify(["MIDDLE","MIDDLE"]) \
         .setSize(0.5) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([1,1,0.2]) \
        ) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./CameraExamples.newf.x3d")
