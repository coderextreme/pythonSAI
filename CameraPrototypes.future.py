import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.2") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("CameraPrototypes.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Camera, CameraShot and CameraMovement prototypes that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman and Jeff Weekley") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("16 March 2009") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("25 October 2016") \
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
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("Camera nodes for Viewpoint navigation control") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("CameraExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
.addComments(CommentsBlock("""=============== Camera ==============""")) \
    .addChild(ProtoDeclareObject() \
     .setName("Camera") \
     .setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images.") \
     .setProtoInterface(ProtoInterfaceObject() \
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
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFROTATION) \
       .setName("orientation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("fieldOfView") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("pi/4") \
       .setValue("0.7854") \
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
       .setValue("0.25") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("farClipPlane") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFNODE) \
       .setName("shots") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes") \
.addComments(CommentsBlock("""initialization nodes (if any) go here""")) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("headlight") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Whether camera headlight is on or off") \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("headlightColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Camera headlight color") \
       .setValue("1 1 1") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("headlightIntensity") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Camera headlight intensity") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("filterColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Camera filter color that modifies virtual lens capture") \
       .setValue("1 1 1") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("filterTransparency") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Camera filter transparency that modifies virtual lens capture") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("upVector") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("upVector changes modify camera orientation (and possibly vice versa)") \
       .setValue("0 1 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("fStop") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("focusDistance") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setValue("10") \
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
.addComments(CommentsBlock("""initialization node (if any) goes here""")) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("traceEnabled") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(ViewpointObject() \
       .setDEF("CameraViewpoint") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("position") \
         .setProtoField("position") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("orientation") \
         .setProtoField("orientation") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("fieldOfView") \
         .setProtoField("fieldOfView") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("set_bind") \
         .setProtoField("set_bind") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("bindTime") \
         .setProtoField("bindTime") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("isBound") \
         .setProtoField("isBound") \
        ) \
       ) \
      ) \
.addComments(CommentsBlock("""NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation""")) \
      .addChild(NavigationInfoObject() \
       .setType(["EXAMINE","FLY","ANY"]) \
       .setDEF("CameraNavInfo") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("set_bind") \
         .setProtoField("set_bind") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("headlight") \
         .setProtoField("headlight") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("visibilityLimit") \
         .setProtoField("farClipPlane") \
        ) \
.addComments(CommentsBlock("""No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing.""")) \
       ) \
      ) \
.addComments(CommentsBlock("""this DirectionalLight replaces NavigationInfo headlight in order to add color capability""")) \
      .addChild(DirectionalLightObject() \
       .setDEF("CameraDirectionalLight") \
       .setGlobal(True) \
.addComments(CommentsBlock("""TODO confirm other default field values match NavigationInfo spec""")) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("on") \
         .setProtoField("headlight") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("color") \
         .setProtoField("headlightColor") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("intensity") \
         .setProtoField("headlightIntensity") \
        ) \
       ) \
      ) \
      .addChild(PositionInterpolatorObject() \
       .setDEF("CameraPositionInterpolator") \
       .setKey([0,1]) \
       .setKeyValue([0,0,0,0,0,0]) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("set_fraction") \
         .setProtoField("set_fraction") \
        ) \
       ) \
      ) \
      .addChild(OrientationInterpolatorObject() \
       .setDEF("CameraOrientationInterpolator") \
       .setKey([0,1]) \
       .setKeyValue([0,1,0,0,0,1,0,0]) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("set_fraction") \
         .setProtoField("set_fraction") \
        ) \
       ) \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("value_changed") \
       .setFromNode("CameraPositionInterpolator") \
       .setToField("position") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("value_changed") \
       .setFromNode("CameraOrientationInterpolator") \
       .setToField("orientation") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChild(ScriptObject() \
       .setDEF("CameraScript") \
       .setDirectOutput(True) \
       .setMustEvaluate(True) \
.addComments(CommentsBlock("""binding is controlled externally, all camera operations proceed the same regardless of whether bound or not""")) \
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
        .setAppinfo("Camera position in local transformation frame") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFROTATION) \
        .setName("orientation") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("Camera rotation in local transformation frame") \
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
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("fieldOfView") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("pi/4") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("nearClipPlane") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("Vector distance to near clipping plane") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("farClipPlane") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("Vector distance to far clipping plane") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFNODE) \
        .setName("shots") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes") \
.addComments(CommentsBlock("""initialization nodes (if any) go here""")) \
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
.addComments(CommentsBlock("""initialization node (if any) goes here""")) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFNODE) \
        .setName("ViewpointNode") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .addChild(ViewpointObject() \
         .setUSE("CameraViewpoint") \
        ) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFNODE) \
        .setName("NavInfoNode") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .addChild(NavigationInfoObject() \
         .setUSE("CameraNavInfo") \
        ) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFNODE) \
        .setName("CameraPI") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .addChild(PositionInterpolatorObject() \
         .setUSE("CameraPositionInterpolator") \
        ) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFNODE) \
        .setName("CameraOI") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .addChild(OrientationInterpolatorObject() \
         .setUSE("CameraOrientationInterpolator") \
        ) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFFLOAT) \
        .setName("key") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("key array for interpolators") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFVEC3F) \
        .setName("keyValuePosition") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("keyValue array for PositionInterpolator") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFROTATION) \
        .setName("keyValueOrientation") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("keyValue array for OrientationInterpolator") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("animated") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events") \
        .setValue("false") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("initialized") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("perform checkShots() function once immediately after initialization") \
        .setValue("false") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFINT32) \
        .setName("shotCount") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("how many CameraShot nodes are contained in shots array") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFINT32) \
        .setName("movesCount") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("how many CameraMove nodes are contained in moves array") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("frameCount") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("how many frames were created in current loop") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFTIME) \
        .setName("startTime") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("holding variable") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFTIME) \
        .setName("priorTraceTime") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("holding variable") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("traceEnabled") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("position") \
         .setProtoField("position") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("orientation") \
         .setProtoField("orientation") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("set_fraction") \
         .setProtoField("set_fraction") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("set_bind") \
         .setProtoField("set_bind") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("fieldOfView") \
         .setProtoField("fieldOfView") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("nearClipPlane") \
         .setProtoField("nearClipPlane") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("farClipPlane") \
         .setProtoField("farClipPlane") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("shots") \
         .setProtoField("shots") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("filterColor") \
         .setProtoField("filterColor") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("filterTransparency") \
         .setProtoField("filterTransparency") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("upVector") \
         .setProtoField("upVector") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("fStop") \
         .setProtoField("fStop") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("focusDistance") \
         .setProtoField("focusDistance") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("isActive") \
         .setProtoField("isActive") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("totalDuration") \
         .setProtoField("totalDuration") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("offlineRender") \
         .setProtoField("offlineRender") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("traceEnabled") \
         .setProtoField("traceEnabled") \
        ) \
       ) \
.setSourceCode('''ecmascript:\n"+
"function initialize () // CameraScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    NavInfoNode.avatarSize[0]   = nearClipPlane;\n"+
"\n"+
"    // remaining setups deferred to invocation of checkShots() method\n"+
"    // thanks to Yvonne Jung Fraunhofer for diagnosing better approach to function initialization\n"+
"    alwaysPrint ('initialize complete');\n"+
"}\n"+
"\n"+
"function checkShots (eventValue)\n"+
"{\n"+
"    tracePrint ('checkShots() method should only occur after initialize() methods in all other Scripts are complete');\n"+
"\n"+
"    // compute totalDuration by summing durations from contained CameraShot and CameraMovement nodes\n"+
"    totalDuration= 0;\n"+
"    shotCount  = shots.length;\n"+
"    movesCount = 0;\n"+
"    for (i = 0; i < shotCount; i++) // shots index\n"+
"    {\n"+
"       tracePrint ('shots[' + i + '].moves.length=' + shots[i].moves.length);\n"+
"       movesCount   += shots[i].moves.length;\n"+
"       totalDuration = totalDuration + shots[i].shotDuration;\n"+
"       if (shots[i].moves.length == 0)\n"+
"       {\n"+
"          alwaysPrint ('warning: CameraShot[' + i + '][' + shots[i].description + '] has no contained CameraMove nodes');\n"+
"       }\n"+
"    }\n"+
"    // size checks before proceeding\n"+
"    if (shotCount == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: no CameraShot nodes found for the shots, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    else if (movesCount == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: no CameraMove nodes found for the shots, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    else if (totalDuration == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: totalDuration = 0 seconds, nothing to do!');\n"+
"       return;\n"+
"    }\n"+
"    tracePrint ('number of contained CameraShot nodes=' + shotCount);\n"+
"    tracePrint ('number of contained CameraMove nodes=' + movesCount);\n"+
"    tracePrint ('totalDuration=' + totalDuration + ' seconds for all shots and moves');\n"+
"\n"+
"    // compute interpolators\n"+
"    var k = 0; // index for latest key, keyValuePosition, keyValueOrientation\n"+
"    for (i = 0; i < shotCount; i++) // shots index\n"+
"    {\n"+
"        if (i==0) // initial entries\n"+
"        {\n"+
"           key[0]                   = 0.0; // no previous move\n"+
"           keyValuePosition[0]      = shots[i].initialPosition;\n"+
"           keyValueOrientation[0]   = shots[i].initialOrientation;\n"+
"        }\n"+
"        else     // new shot repositions, reorients camera as clean break from preceding shot/move\n"+
"        {\n"+
"           key[k+1]                 = key[k]; // start from end from previous move\n"+
"           keyValuePosition[k+1]    = shots[i].initialPosition;\n"+
"           keyValueOrientation[k+1] = shots[i].initialOrientation;\n"+
"           k++;\n"+
"        }\n"+
"        tracePrint (shots[i].description);\n"+
"        tracePrint ('shots[i].moves.length=' + shots[i].moves.length);\n"+
"\n"+
"        for (j = 0; j < shots[i].moves.length; j++) // moves index\n"+
"        {\n"+
"            var durationFloat =              shots[i].moves[j].duration;  // implicit type conversion from SFTime\n"+
"            //  durationFloat = new SFFloat (shots[i].moves[j].duration); // explicit type conversion from SFTime\n"+
"            //  tracePrint ('durationFloat=' + durationFloat);\n"+
"            key[k+1]               = key[k] + (durationFloat / totalDuration);\n"+
"            keyValuePosition[k+1]  = shots[i].moves[j].goalPosition;\n"+
"            if (!animated)\n"+
"            {\n"+
"                 keyValueOrientation[k+1] = shots[i].moves[j].goalOrientation;\n"+
"            }\n"+
"            else\n"+
"            {\n"+
"                // using constructor SFRotation (SFVec3f fromVector, SFVec3f toVector)\n"+
"                // see X3D ECMAScript binding Table 7.18 — SFRotation instance creation functions\n"+
"\n"+
"                // test if difference vector is zero, if so maintain previous rotation\n"+
"                var shotVector = ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).normalize();\n"+
"                if (shotVector.length() >= 0)\n"+
"                {\n"+
"                    // default view direction is along -Z axis\n"+
"                    shots[i].moves[j].goalOrientation = new SFRotation (new SFVec3f (0, 0, 1), shotVector);\n"+
"                    keyValueOrientation[k+1] = shots[i].moves[j].goalOrientation;\n"+
"                }\n"+
"                else // note (k > 0)\n"+
"                {\n"+
"                    keyValueOrientation[k+1] = keyValueOrientation[k];  // no change\n"+
"                }\n"+
"\n"+
"                tracePrint ('shots[' + i + '].moves[' + j + '].goalAimPoint=' + shots[i].moves[j].goalAimPoint.toString());\n"+
"                tracePrint ('        ViewpointNode.position=' + ViewpointNode.position.toString());\n"+
"                tracePrint ('          shotVector     delta=' + ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).toString());\n"+
"                tracePrint ('          shotVector normalize=' + ViewpointNode.position.subtract(shots[i].moves[j].goalAimPoint).normalize().toString());\n"+
"                tracePrint ('               goalOrientation=' + shots[i].moves[j].goalOrientation.toString());\n"+
"                tracePrint ('      keyValueOrientation[k+1]=' + keyValueOrientation[k+1].toString() + '\\n');\n"+
"            }\n"+
"            k++; // update index to match latest key, keyValuePosition, keyValueOrientation\n"+
"\n"+
"            // check animated parameter:  set true if any of moves are tracking moves\n"+
"            if (!animated)  animated = shots[i].moves[j].tracking; // once true, remains true\n"+
"         // tracePrint ('shots[' + i + '].moves[' + j + '].tracking=' + shots[i].moves[j].tracking + ', animated=' + animated);\n"+
"\n"+
"            // intermediate trace\n"+
"            tracePrint ('                key=' + key);\n"+
"            tracePrint ('   keyValuePosition=' + keyValuePosition);\n"+
"            tracePrint ('keyValueOrientation=' + keyValueOrientation);\n"+
"            tracePrint ('- ' + shots[i].moves[j].description);\n"+
"        }\n"+
"    }\n"+
"    tracePrint ('                key=' + key);\n"+
"    tracePrint ('   keyValuePosition=' + keyValuePosition);\n"+
"    tracePrint ('keyValueOrientation=' + keyValueOrientation);\n"+
"    if (key.length != keyValuePosition.length)\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  'keyValuePosition.length=' + keyValuePosition.length);\n"+
"    }\n"+
"    if (key.length != keyValueOrientation.length)\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  'keyValueOrientation.length=' + keyValueOrientation.length);\n"+
"    }\n"+
"    if (key.length != (shotCount + movesCount))\n"+
"    {\n"+
"      alwaysPrint ('warning: internal error during array construction, ' +\n"+
"                  'key.length=' + key.length + ' must equal ' +\n"+
"                  '(shotCount + movesCount)=' + (shotCount + movesCount));\n"+
"    }\n"+
"    tracePrint ('           animated=' + animated);\n"+
"    // set node values\n"+
"    CameraPI.key      = key;\n"+
"    CameraOI.key      = key;\n"+
"    CameraPI.keyValue = keyValuePosition;\n"+
"    CameraOI.keyValue = keyValueOrientation;\n"+
"\n"+
"    if (!animated) // output results\n"+
"    {\n"+
"        tracePrint ('<PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        tracePrint ('<OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"    }\n"+
"    tracePrint ('checkShots() complete');\n"+
"}\n"+
"\n"+
"function stripBrackets (fieldArray)\n"+
"{\n"+
"    // some browsers add brackets to array output strings, this function strips them\n"+
"    outputString = '';\n"+
"    for (i = 0; i < fieldArray.length; i++)\n"+
"    {\n"+
"       outputString += fieldArray[i].toString();\n"+
"       if (i < fieldArray.length - 1) outputString += ' ';\n"+
"    }\n"+
"    return outputString;\n"+
"}\n"+
"\n"+
"function set_fraction (eventValue, timestamp) // input event received for inputOnly field\n"+
"{\n"+
"   // traceEnabled = false;  // for testing purposes\n"+
"\n"+
"   // if Camera is being animated, immediately recompute interpolator settings\n"+
"   if (animated) checkShots (true);\n"+
"\n"+
"   // trace progress on console with reduced output frequency\n"+
"   if (frameCount == 0)\n"+
"   {\n"+
"      alwaysPrint ('Animation loop commencing, timestamp=' + timestamp);\n"+
"      startTime      = timestamp;\n"+
"      priorTraceTime = timestamp;\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ' seconds, frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"        tracePrint ('  <PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        tracePrint ('  <OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"      }\n"+
"   }\n"+
"   else if ((timestamp - priorTraceTime) >= 1.0) // 1 second trace interval\n"+
"   {\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ' seconds, frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"      priorTraceTime = timestamp;\n"+
"\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"        tracePrint ('  <PositionInterpolator    DEF=\\'CameraPositionInterpolator\\'    key=\\'' + stripBrackets(CameraPI.key) + '\\' keyValue=\\'' + stripBrackets(CameraPI.keyValue) + '\\'/>');\n"+
"        alwaysPrint ('  <OrientationInterpolator DEF=\\'CameraOrientationInterpolator\\' key=\\'' + stripBrackets(CameraOI.key) + '\\' keyValue=\\'' + stripBrackets(CameraOI.keyValue) + '\\'/>');\n"+
"      }\n"+
"   }\n"+
"   if (eventValue == 0)\n"+
"   {\n"+
"      // note that zero value is not necessarily sent first by TimeSensor, so otherwise ignored\n"+
"      frameCount++;\n"+
"   }\n"+
"   else if (eventValue == 1)\n"+
"   {\n"+
"      alwaysPrint ('shotClock=' + (timestamp - startTime) + ', frameCount=' + frameCount + ', fraction=' + eventValue + ', position=' + ViewpointNode.position.toString() + ', orientation=' + ViewpointNode.orientation.toString());\n"+
"      if (animated) // output results\n"+
"      {\n"+
"        // TODO how to report or speed up response?  alwaysPrint ('  aimPoint=' + aimPoint.toString());\n"+
"      }\n"+
"      alwaysPrint ('Animation loop complete.');\n"+
"      // do not unbind the Viewpoint and NavigationInfo nodes, let that be controlled externally\n"+
"   }\n"+
"   else\n"+
"   {\n"+
"      frameCount++;\n"+
"   }\n"+
"}\n"+
"\n"+
"function set_bind (eventValue) // input event received for inputOnly field\n"+
"{\n"+
"   // need to ensure CameraShot nodes are properly initialized\n"+
"   if (initialized == false)\n"+
"   {\n"+
"      checkShots (true);\n"+
"      initialized = true;\n"+
"   }\n"+
"   if (eventValue)\n"+
"   {\n"+
"       tracePrint ('Camera has been bound');\n"+
"   }\n"+
"   else\n"+
"   {\n"+
"       tracePrint ('Camera has been unbound');\n"+
"   }\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_position (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    position = eventValue;\n"+
"}\n"+
"\n"+
"function set_orientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    orientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_fieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    fieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_nearClipPlane (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    nearClipPlane = eventValue;\n"+
"}\n"+
"\n"+
"function set_farClipPlane (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    farClipPlane = eventValue;\n"+
"}\n"+
"\n"+
"function set_shots (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    shots = eventValue;\n"+
"}\n"+
"\n"+
"function set_filterColor (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    filterColor = eventValue;\n"+
"}\n"+
"\n"+
"function set_filterTransparency (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    filterTransparency = eventValue;\n"+
"}\n"+
"\n"+
"function set_upVector (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    upVector = eventValue;\n"+
"}\n"+
"\n"+
"function set_fStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    fStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_focusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    focusDistance = eventValue;\n"+
"}\n"+
"\n"+
"function set_offlineRender (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    offlineRender = eventValue;\n"+
"}\n"+
"\n"+
"function set_key (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    key = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValuePosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValuePosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValueOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValueOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_animated (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    animated = eventValue;\n"+
"}\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"    // try to ensure outputValue is converted to string despite Browser.println idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[Camera: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[Camera] ' + outputString + '\\n');\n"+
"}''')
      ) \
      .addChild(ROUTEObject() \
       .setFromField("position") \
       .setFromNode("CameraScript") \
       .setToField("position") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("orientation") \
       .setFromNode("CameraScript") \
       .setToField("orientation") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("set_bind") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("set_bind") \
       .setToNode("CameraNavInfo") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("on") \
       .setToNode("CameraDirectionalLight") \
      ) \
     ) \
    ) \
.addComments(CommentsBlock("""=============== CameraShot ==============""")) \
    .addChild(ProtoDeclareObject() \
     .setName("CameraShot") \
     .setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot.") \
     .setProtoInterface(ProtoInterfaceObject() \
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
       .setValue("true") \
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
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFROTATION) \
       .setName("initialOrientation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Setup to reinitialize camera rotation for this shot") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("initialAimPoint") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("initialFieldOfView") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("pi/4") \
       .setValue("0.7854") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("initialFStop") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("initialFocusDistance") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setValue("10") \
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
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(ScriptObject() \
       .setDEF("CameraShotScript") \
       .setDirectOutput(True) \
       .setMustEvaluate(True) \
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
.addComments(CommentsBlock("""initialization nodes (if any) go here""")) \
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
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFFLOAT) \
        .setName("key") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("key array for interpolators") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFVEC3F) \
        .setName("keyValuePosition") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("keyValue array for PositionInterpolator") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFROTATION) \
        .setName("keyValueOrientation") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setAppinfo("keyValue array for OrientationInterpolator") \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("enabled") \
         .setProtoField("enabled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("moves") \
         .setProtoField("moves") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialPosition") \
         .setProtoField("initialPosition") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialOrientation") \
         .setProtoField("initialOrientation") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialAimPoint") \
         .setProtoField("initialAimPoint") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialFieldOfView") \
         .setProtoField("initialFieldOfView") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialFStop") \
         .setProtoField("initialFStop") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("initialFocusDistance") \
         .setProtoField("initialFocusDistance") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("shotDuration") \
         .setProtoField("shotDuration") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("isActive") \
         .setProtoField("isActive") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("traceEnabled") \
         .setProtoField("traceEnabled") \
        ) \
       ) \
.setSourceCode('''ecmascript:\n"+
"function initialize () // CameraShotScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    // compute shotDuration by summing durations from contained CameraMovement nodes\n"+
"    shotDuration = 0;\n"+
"    for (i = 0; i < moves.length; i++)\n"+
"    {\n"+
"        shotDuration = shotDuration + moves[i].duration;\n"+
"    }\n"+
"    alwaysPrint ('number of contained CameraMove nodes=' + moves.length + ', shotDuration=' + shotDuration + ' seconds');\n"+
"\n"+
"//  tracePrint ('... initialize() complete');\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_moves (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    moves = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialPosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialPosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialAimPoint (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialAimPoint = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_initialFocusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    initialFocusDistance = eventValue;\n"+
"}\n"+
"\n"+
"function set_key (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    key = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValuePosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValuePosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_keyValueOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    keyValueOrientation = eventValue;\n"+
"}\n"+
"\n"+
"// TODO consider method set_active for constructed Camera node BooleanSequencer to send isActive\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[CameraShot: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[CameraShot] ' + outputString + '\\n');\n"+
"}''')
      ) \
.addComments(CommentsBlock("""Add any ROUTEs here, going from Script to other nodes within ProtoBody""")) \
     ) \
    ) \
.addComments(CommentsBlock("""=============== CameraMovement ==============""")) \
    .addChild(ProtoDeclareObject() \
     .setName("CameraMovement") \
     .setAppinfo("CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView.") \
     .setProtoInterface(ProtoInterfaceObject() \
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
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("duration") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Duration in seconds for this move") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("goalPosition") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Goal camera position for this move") \
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFROTATION) \
       .setName("goalOrientation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Goal camera rotation for this move") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("tracking") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Whether or not camera direction is tracking towards the aimPoint") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("goalAimPoint") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Goal aimPoint for this move, ignored if tracking=false") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("goalFieldOfView") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Goal fieldOfView for this move") \
       .setValue("0.7854") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("goalFStop") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("goalFocusDistance") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setValue("10") \
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
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
.addComments(CommentsBlock("""First node determines node type of this prototype""")) \
.addComments(CommentsBlock("""Subsequent nodes do not render, but still must be a valid X3D subgraph""")) \
.addComments(CommentsBlock("""Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events""")) \
      .addChild(ScriptObject() \
       .setDEF("CameraMovementScript") \
       .setDirectOutput(True) \
       .setMustEvaluate(True) \
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
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("enabled") \
         .setProtoField("enabled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("duration") \
         .setProtoField("duration") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalPosition") \
         .setProtoField("goalPosition") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalOrientation") \
         .setProtoField("goalOrientation") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("tracking") \
         .setProtoField("tracking") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalAimPoint") \
         .setProtoField("goalAimPoint") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalFieldOfView") \
         .setProtoField("goalFieldOfView") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalFStop") \
         .setProtoField("goalFStop") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("goalFocusDistance") \
         .setProtoField("goalFocusDistance") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("isActive") \
         .setProtoField("isActive") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("traceEnabled") \
         .setProtoField("traceEnabled") \
        ) \
       ) \
.setSourceCode('''ecmascript:\n"+
"function initialize () // CameraMovementScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"    alwaysPrint ('initialize goalPosition=' + goalPosition.toString() + ', goalOrientation=' + goalOrientation.toString() +\n"+
"                           ', goalAimPoint=' + goalAimPoint.toString() // + ', tracking=' + tracking.toString()\n"+
"                           );\n"+
"    if (duration < 0)\n"+
"    {\n"+
"       alwaysPrint ('error: negative duration=' + duration + ', reset to 0 and ignored');\n"+
"       duration = 0;\n"+
"    }\n"+
"    else if (duration == 0)\n"+
"    {\n"+
"       alwaysPrint ('warning: duration=0, nothing to do!');\n"+
"    }\n"+
"    tracePrint ('... initialize complete');\n"+
"}\n"+
"\n"+
"function set_goalAimPoint (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalAimPoint_changed = eventValue;\n"+
"    tracePrint ('goalAimPoint=' + goalAimPoint.toString());\n"+
"\n"+
"    // updated goalOrientation tracking is handled by Camera recomputing the OrientationInterpolator\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_duration (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    duration = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalPosition (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalPosition = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalOrientation (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalOrientation = eventValue;\n"+
"}\n"+
"\n"+
"function set_tracking (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    tracking = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFieldOfView (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFieldOfView = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFStop (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFStop = eventValue;\n"+
"}\n"+
"\n"+
"function set_goalFocusDistance (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    goalFocusDistance = eventValue;\n"+
"}\n"+
"\n"+
"// TODO consider method set_active for constructed Camera node BooleanSequencer to send isActive\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[CameraMovement: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[CameraMovement] ' + outputString + '\\n');\n"+
"}''')
      ) \
.addComments(CommentsBlock("""Add any ROUTEs here, going from Script to other nodes within ProtoBody""")) \
     ) \
    ) \
.addComments(CommentsBlock("""=============== OfflineRender ==============""")) \
    .addChild(ProtoDeclareObject() \
     .setName("OfflineRender") \
     .setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot).") \
     .setProtoInterface(ProtoInterfaceObject() \
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
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("frameRate") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Frames per second recorded for this rendering") \
       .setValue("30") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC2F) \
       .setName("frameSize") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Size of frame in number of pixels width and height") \
       .setValue("640 480") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("pixelAspectRatio") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1") \
       .setValue("1.33") \
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
       .setValue("\"mpeg\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("imageFormat") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format") \
       .setValue("\"png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("traceEnabled") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
.addComments(CommentsBlock("""First node determines node type of this prototype""")) \
.addComments(CommentsBlock("""Subsequent nodes do not render, but still must be a valid X3D subgraph""")) \
      .addChild(ScriptObject() \
       .setDEF("OfflineRenderScript") \
       .setMustEvaluate(True) \
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
        .setAppinfo("Format of rendered output movie (mpeg mp4 etc.)") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFSTRING) \
        .setName("imageFormat") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("Format of rendered output images (png jpeg gif tiff etc.)") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("traceEnabled") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("enabled") \
         .setProtoField("enabled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("frameRate") \
         .setProtoField("frameRate") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("frameSize") \
         .setProtoField("frameSize") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("pixelAspectRatio") \
         .setProtoField("pixelAspectRatio") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("set_startTime") \
         .setProtoField("set_startTime") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("progress") \
         .setProtoField("progress") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("renderCompleteTime") \
         .setProtoField("renderCompleteTime") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("movieFormat") \
         .setProtoField("movieFormat") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("imageFormat") \
         .setProtoField("imageFormat") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("traceEnabled") \
         .setProtoField("traceEnabled") \
        ) \
       ) \
.setSourceCode('''ecmascript:\n"+
"function initialize () // OfflineRenderScript\n"+
"{\n"+
"//  tracePrint ('initialize start...');\n"+
"\n"+
"    tracePrint ('... initialize complete');\n"+
"}\n"+
"\n"+
"function set_description (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    description = eventValue;\n"+
"}\n"+
"\n"+
"function set_enabled (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    enabled = eventValue;\n"+
"}\n"+
"\n"+
"function set_frameRate (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    frameRate = eventValue;\n"+
"}\n"+
"\n"+
"function set_frameSize (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    frameSize = eventValue;\n"+
"}\n"+
"\n"+
"function set_pixelAspectRatio (eventValue) // input event received for inputOutput field\n"+
"{\n"+
"    pixelAspectRatio = eventValue;\n"+
"}\n"+
"\n"+
"function set_startTime (eventValue) // input event received for inputOnly field\n"+
"{\n"+
"   // do something with input eventValue;\n"+
"}\n"+
"\n"+
"function tracePrint (outputValue)\n"+
"{\n"+
"	if (traceEnabled) alwaysPrint (outputValue);\n"+
"}\n"+
"\n"+
"function alwaysPrint (outputValue)\n"+
"{\n"+
"	// try to ensure outputValue is converted to string despite browser idiosyncracies\n"+
"    var outputString = outputValue.toString(); // utility function according to spec\n"+
"    if (outputString == null) outputString = outputValue; // direct cast\n"+
"\n"+
"    if  (description.length > 0)\n"+
"         Browser.print ('[OfflineRender: ' + description + '] ' + outputString + '\\n');\n"+
"    else\n"+
"         Browser.print ('[OfflineRender] ' + outputString + '\\n');\n"+
"}''')
      ) \
.addComments(CommentsBlock("""Add any ROUTEs here, going from Script to other nodes within ProtoBody""")) \
     ) \
    ) \
.addComments(CommentsBlock("""=============== Launch Prototype Example ==============""")) \
    .addChild(BackgroundObject() \
     .setSkyColor([0.282353,0.380392,0.470588]) \
    ) \
    .addChild(AnchorObject() \
     .setDescription("launch CameraExample scene") \
     .setUrl(["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"]) \
     .addChild(TransformObject() \
      .addChild(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"]) \
        .setFontStyle(FontStyleObject() \
         .setJustify(["MIDDLE","MIDDLE"]) \
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

X3D0.toFileX3D("./future/./CameraPrototypes.newf.x3d")
