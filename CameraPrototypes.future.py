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
#=============== Camera ==============
    .addChildren(ProtoDeclareObject() \
     .setName("Camera") \
     .setAppinfo("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images.") \
     .setProtoInterface(ProtoInterfaceObject() \
#Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields
      .addField(fieldObject() \
       .setName("description") \
       .setAccessType("inputOutput") \
       .setAppinfo("Text description to be displayed for this Camera") \
       .setType("SFString") \
      ) \
      .addField(fieldObject() \
       .setName("position") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated") \
       .setType("SFVec3f") \
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setName("orientation") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated") \
       .setType("SFRotation") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setName("fieldOfView") \
       .setAccessType("inputOutput") \
       .setAppinfo("pi/4") \
       .setType("SFFloat") \
       .setValue("0.7854") \
      ) \
      .addField(fieldObject() \
       .setName("set_fraction") \
       .setAccessType("inputOnly") \
       .setAppinfo("input fraction drives interpolators") \
       .setType("SFFloat") \
      ) \
      .addField(fieldObject() \
       .setName("set_bind") \
       .setAccessType("inputOnly") \
       .setAppinfo("input event binds or unbinds this Camera") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("bindTime") \
       .setAccessType("outputOnly") \
       .setAppinfo("output event indicates when this Camera is bound") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("isBound") \
       .setAccessType("outputOnly") \
       .setAppinfo("output event indicates whether this Camera is bound or unbound") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("nearClipPlane") \
       .setAccessType("inputOutput") \
       .setAppinfo("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]") \
       .setType("SFFloat") \
       .setValue("0.25") \
      ) \
      .addField(fieldObject() \
       .setName("farClipPlane") \
       .setAccessType("inputOutput") \
       .setAppinfo("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit") \
       .setType("SFFloat") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setName("shots") \
       .setAccessType("inputOutput") \
       .setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes") \
       .setType("MFNode") \
#initialization nodes (if any) go here
      ) \
      .addField(fieldObject() \
       .setName("headlight") \
       .setAccessType("inputOutput") \
       .setAppinfo("Whether camera headlight is on or off") \
       .setType("SFBool") \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setName("headlightColor") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera headlight color") \
       .setType("SFColor") \
       .setValue("1 1 1") \
      ) \
      .addField(fieldObject() \
       .setName("headlightIntensity") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera headlight intensity") \
       .setType("SFFloat") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setName("filterColor") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera filter color that modifies virtual lens capture") \
       .setType("SFColor") \
       .setValue("1 1 1") \
      ) \
      .addField(fieldObject() \
       .setName("filterTransparency") \
       .setAccessType("inputOutput") \
       .setAppinfo("Camera filter transparency that modifies virtual lens capture") \
       .setType("SFFloat") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setName("upVector") \
       .setAccessType("inputOutput") \
       .setAppinfo("upVector changes modify camera orientation (and possibly vice versa)") \
       .setType("SFVec3f") \
       .setValue("0 1 0") \
      ) \
      .addField(fieldObject() \
       .setName("fStop") \
       .setAccessType("inputOutput") \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setType("SFFloat") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setName("focusDistance") \
       .setAccessType("inputOutput") \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setType("SFFloat") \
       .setValue("10") \
      ) \
      .addField(fieldObject() \
       .setName("isActive") \
       .setAccessType("outputOnly") \
       .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("totalDuration") \
       .setAccessType("outputOnly") \
       .setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("offlineRender") \
       .setAccessType("inputOutput") \
       .setAppinfo("OfflineRender node") \
       .setType("SFNode") \
#initialization node (if any) goes here
      ) \
      .addField(fieldObject() \
       .setName("traceEnabled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(ViewpointObject() \
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
#NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation
      .addChildren(NavigationInfoObject() \
       .setDEF("CameraNavInfo") \
       .setType(["EXAMINE","FLY","ANY"]) \
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
#No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing.
       ) \
      ) \
#this DirectionalLight replaces NavigationInfo headlight in order to add color capability
      .addChildren(DirectionalLightObject() \
       .setDEF("CameraDirectionalLight") \
       .setGlobal(True) \
#TODO confirm other default field values match NavigationInfo spec
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
      .addChildren(PositionInterpolatorObject() \
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
      .addChildren(OrientationInterpolatorObject() \
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
      .addChildren(ROUTEObject() \
       .setFromField("value_changed") \
       .setFromNode("CameraPositionInterpolator") \
       .setToField("position") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("value_changed") \
       .setFromNode("CameraOrientationInterpolator") \
       .setToField("orientation") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChildren(ScriptObject(directOutput = True, mustEvaluate = True) \
       .setDEF("CameraScript") \
#binding is controlled externally, all camera operations proceed the same regardless of whether bound or not
       .addField(fieldObject() \
        .setName("description") \
        .setAccessType("inputOutput") \
        .setAppinfo("Text description to be displayed for this Camera") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("position") \
        .setAccessType("inputOutput") \
        .setAppinfo("Camera position in local transformation frame") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("orientation") \
        .setAccessType("inputOutput") \
        .setAppinfo("Camera rotation in local transformation frame") \
        .setType("SFRotation") \
       ) \
       .addField(fieldObject() \
        .setName("set_fraction") \
        .setAccessType("inputOnly") \
        .setAppinfo("input fraction drives interpolators") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("set_bind") \
        .setAccessType("inputOnly") \
        .setAppinfo("input event binds or unbinds this Camera") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("fieldOfView") \
        .setAccessType("inputOutput") \
        .setAppinfo("pi/4") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("nearClipPlane") \
        .setAccessType("inputOutput") \
        .setAppinfo("Vector distance to near clipping plane") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("farClipPlane") \
        .setAccessType("inputOutput") \
        .setAppinfo("Vector distance to far clipping plane") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("shots") \
        .setAccessType("inputOutput") \
        .setAppinfo("Array of CameraShot nodes which in turn contain CameraMovement nodes") \
        .setType("MFNode") \
#initialization nodes (if any) go here
       ) \
       .addField(fieldObject() \
        .setName("filterColor") \
        .setAccessType("inputOutput") \
        .setAppinfo("Camera filter color that modifies virtual lens capture") \
        .setType("SFColor") \
       ) \
       .addField(fieldObject() \
        .setName("filterTransparency") \
        .setAccessType("inputOutput") \
        .setAppinfo("Camera filter transparency that modifies virtual lens capture") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("upVector") \
        .setAccessType("inputOutput") \
        .setAppinfo("upVector changes modify camera orientation (and possibly vice versa)") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("fStop") \
        .setAccessType("inputOutput") \
        .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("focusDistance") \
        .setAccessType("inputOutput") \
        .setAppinfo("Distance to focal plane of sharpest focus") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("isActive") \
        .setAccessType("outputOnly") \
        .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("totalDuration") \
        .setAccessType("outputOnly") \
        .setAppinfo("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations") \
        .setType("SFTime") \
       ) \
       .addField(fieldObject() \
        .setName("offlineRender") \
        .setAccessType("inputOutput") \
        .setAppinfo("OfflineRender node") \
        .setType("SFNode") \
#initialization node (if any) goes here
       ) \
       .addField(fieldObject() \
        .setName("ViewpointNode") \
        .setAccessType("initializeOnly") \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .setType("SFNode") \
        .addChildren(ViewpointObject() \
         .setUSE("CameraViewpoint") \
        ) \
       ) \
       .addField(fieldObject() \
        .setName("NavInfoNode") \
        .setAccessType("initializeOnly") \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .setType("SFNode") \
        .addChildren(NavigationInfoObject() \
         .setUSE("CameraNavInfo") \
        ) \
       ) \
       .addField(fieldObject() \
        .setName("CameraPI") \
        .setAccessType("initializeOnly") \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .setType("SFNode") \
        .addChildren(PositionInterpolatorObject() \
         .setUSE("CameraPositionInterpolator") \
        ) \
       ) \
       .addField(fieldObject() \
        .setName("CameraOI") \
        .setAccessType("initializeOnly") \
        .setAppinfo("node reference to permit getting setting fields from within Script") \
        .setType("SFNode") \
        .addChildren(OrientationInterpolatorObject() \
         .setUSE("CameraOrientationInterpolator") \
        ) \
       ) \
       .addField(fieldObject() \
        .setName("key") \
        .setAccessType("inputOutput") \
        .setAppinfo("key array for interpolators") \
        .setType("MFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("keyValuePosition") \
        .setAccessType("inputOutput") \
        .setAppinfo("keyValue array for PositionInterpolator") \
        .setType("MFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("keyValueOrientation") \
        .setAccessType("inputOutput") \
        .setAppinfo("keyValue array for OrientationInterpolator") \
        .setType("MFRotation") \
       ) \
       .addField(fieldObject() \
        .setName("animated") \
        .setAccessType("inputOutput") \
        .setAppinfo("whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events") \
        .setType("SFBool") \
        .setValue("false") \
       ) \
       .addField(fieldObject() \
        .setName("initialized") \
        .setAccessType("initializeOnly") \
        .setAppinfo("perform checkShots() function once immediately after initialization") \
        .setType("SFBool") \
        .setValue("false") \
       ) \
       .addField(fieldObject() \
        .setName("shotCount") \
        .setAccessType("initializeOnly") \
        .setAppinfo("how many CameraShot nodes are contained in shots array") \
        .setType("SFInt32") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setName("movesCount") \
        .setAccessType("initializeOnly") \
        .setAppinfo("how many CameraMove nodes are contained in moves array") \
        .setType("SFInt32") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setName("frameCount") \
        .setAccessType("initializeOnly") \
        .setAppinfo("how many frames were created in current loop") \
        .setType("SFFloat") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setName("startTime") \
        .setAccessType("initializeOnly") \
        .setAppinfo("holding variable") \
        .setType("SFTime") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setName("priorTraceTime") \
        .setAccessType("initializeOnly") \
        .setAppinfo("holding variable") \
        .setType("SFTime") \
        .setValue("0") \
       ) \
       .addField(fieldObject() \
        .setName("traceEnabled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
        .setType("SFBool") \
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
      .addChildren(ROUTEObject() \
       .setFromField("position") \
       .setFromNode("CameraScript") \
       .setToField("position") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("orientation") \
       .setFromNode("CameraScript") \
       .setToField("orientation") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("set_bind") \
       .setToNode("CameraViewpoint") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("set_bind") \
       .setToNode("CameraNavInfo") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isActive") \
       .setFromNode("CameraScript") \
       .setToField("on") \
       .setToNode("CameraDirectionalLight") \
      ) \
     ) \
    ) \
#=============== CameraShot ==============
    .addChildren(ProtoDeclareObject() \
     .setName("CameraShot") \
     .setAppinfo("CameraShot collects a specific set of CameraMovement animations that make up an individual shot.") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("description") \
       .setAccessType("inputOutput") \
       .setAppinfo("Text description to be displayed for this CameraShot") \
       .setType("SFString") \
      ) \
      .addField(fieldObject() \
       .setName("enabled") \
       .setAccessType("inputOutput") \
       .setAppinfo("Whether this CameraShot can be activated") \
       .setType("SFBool") \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setName("moves") \
       .setAccessType("inputOutput") \
       .setAppinfo("Set of CameraMovement nodes") \
       .setType("MFNode") \
#initializing CameraMovement nodes are inserted here by scene author using ProtoInstance
      ) \
      .addField(fieldObject() \
       .setName("initialPosition") \
       .setAccessType("inputOutput") \
       .setAppinfo("Setup to reinitialize camera position for this shot") \
       .setType("SFVec3f") \
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setName("initialOrientation") \
       .setAccessType("inputOutput") \
       .setAppinfo("Setup to reinitialize camera rotation for this shot") \
       .setType("SFRotation") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setName("initialAimPoint") \
       .setAccessType("inputOutput") \
       .setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("initialFieldOfView") \
       .setAccessType("inputOutput") \
       .setAppinfo("pi/4") \
       .setType("SFFloat") \
       .setValue("0.7854") \
      ) \
      .addField(fieldObject() \
       .setName("initialFStop") \
       .setAccessType("inputOutput") \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setType("SFFloat") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setName("initialFocusDistance") \
       .setAccessType("inputOutput") \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setType("SFFloat") \
       .setValue("10") \
      ) \
      .addField(fieldObject() \
       .setName("shotDuration") \
       .setAccessType("outputOnly") \
       .setAppinfo("Subtotal duration of contained CameraMovement move durations") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("isActive") \
       .setAccessType("outputOnly") \
       .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("traceEnabled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(ScriptObject(directOutput = True, mustEvaluate = True) \
       .setDEF("CameraShotScript") \
       .addField(fieldObject() \
        .setName("description") \
        .setAccessType("inputOutput") \
        .setAppinfo("Text description to be displayed for this CameraShot") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("enabled") \
        .setAccessType("inputOutput") \
        .setAppinfo("Whether this CameraShot can be activated") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("moves") \
        .setAccessType("inputOutput") \
        .setAppinfo("Set of CameraMovement nodes") \
        .setType("MFNode") \
#initialization nodes (if any) go here
       ) \
       .addField(fieldObject() \
        .setName("initialPosition") \
        .setAccessType("inputOutput") \
        .setAppinfo("Setup to reinitialize camera position for this shot") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("initialOrientation") \
        .setAccessType("inputOutput") \
        .setAppinfo("Setup to reinitialize camera rotation for this shot") \
        .setType("SFRotation") \
       ) \
       .addField(fieldObject() \
        .setName("initialAimPoint") \
        .setAccessType("inputOutput") \
        .setAppinfo("Setup to reinitialize aimpoint (relative location for camera direction) for this shot") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("initialFieldOfView") \
        .setAccessType("inputOutput") \
        .setAppinfo("pi/4") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("initialFStop") \
        .setAccessType("inputOutput") \
        .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("initialFocusDistance") \
        .setAccessType("inputOutput") \
        .setAppinfo("Distance to focal plane of sharpest focus") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("shotDuration") \
        .setAccessType("outputOnly") \
        .setAppinfo("Subtotal duration of contained CameraMovement move durations") \
        .setType("SFTime") \
       ) \
       .addField(fieldObject() \
        .setName("isActive") \
        .setAccessType("outputOnly") \
        .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("traceEnabled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("key") \
        .setAccessType("inputOutput") \
        .setAppinfo("key array for interpolators") \
        .setType("MFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("keyValuePosition") \
        .setAccessType("inputOutput") \
        .setAppinfo("keyValue array for PositionInterpolator") \
        .setType("MFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("keyValueOrientation") \
        .setAccessType("inputOutput") \
        .setAppinfo("keyValue array for OrientationInterpolator") \
        .setType("MFRotation") \
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
#Add any ROUTEs here, going from Script to other nodes within ProtoBody
     ) \
    ) \
#=============== CameraMovement ==============
    .addChildren(ProtoDeclareObject() \
     .setName("CameraMovement") \
     .setAppinfo("CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView.") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("description") \
       .setAccessType("inputOutput") \
       .setAppinfo("Text description to be displayed for this CameraMovement") \
       .setType("SFString") \
      ) \
      .addField(fieldObject() \
       .setName("enabled") \
       .setAccessType("inputOutput") \
       .setAppinfo("Whether this CameraMovement can be activated") \
       .setType("SFBool") \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setName("duration") \
       .setAccessType("inputOutput") \
       .setAppinfo("Duration in seconds for this move") \
       .setType("SFFloat") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setName("goalPosition") \
       .setAccessType("inputOutput") \
       .setAppinfo("Goal camera position for this move") \
       .setType("SFVec3f") \
       .setValue("0 0 10") \
      ) \
      .addField(fieldObject() \
       .setName("goalOrientation") \
       .setAccessType("inputOutput") \
       .setAppinfo("Goal camera rotation for this move") \
       .setType("SFRotation") \
       .setValue("0 0 1 0") \
      ) \
      .addField(fieldObject() \
       .setName("tracking") \
       .setAccessType("inputOutput") \
       .setAppinfo("Whether or not camera direction is tracking towards the aimPoint") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setName("goalAimPoint") \
       .setAccessType("inputOutput") \
       .setAppinfo("Goal aimPoint for this move, ignored if tracking=false") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("goalFieldOfView") \
       .setAccessType("inputOutput") \
       .setAppinfo("Goal fieldOfView for this move") \
       .setType("SFFloat") \
       .setValue("0.7854") \
      ) \
      .addField(fieldObject() \
       .setName("goalFStop") \
       .setAccessType("inputOutput") \
       .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
       .setType("SFFloat") \
       .setValue("5.6") \
      ) \
      .addField(fieldObject() \
       .setName("goalFocusDistance") \
       .setAccessType("inputOutput") \
       .setAppinfo("Distance to focal plane of sharpest focus") \
       .setType("SFFloat") \
       .setValue("10") \
      ) \
      .addField(fieldObject() \
       .setName("isActive") \
       .setAccessType("outputOnly") \
       .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("traceEnabled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
#First node determines node type of this prototype
#Subsequent nodes do not render, but still must be a valid X3D subgraph
#Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events
      .addChildren(ScriptObject(directOutput = True, mustEvaluate = True) \
       .setDEF("CameraMovementScript") \
       .addField(fieldObject() \
        .setName("description") \
        .setAccessType("inputOutput") \
        .setAppinfo("Text description to be displayed for this CameraMovement") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("enabled") \
        .setAccessType("inputOutput") \
        .setAppinfo("Whether this CameraMovement can be activated") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("duration") \
        .setAccessType("inputOutput") \
        .setAppinfo("Duration in seconds for this move") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("goalPosition") \
        .setAccessType("inputOutput") \
        .setAppinfo("Goal camera position for this move") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("goalOrientation") \
        .setAccessType("inputOutput") \
        .setAppinfo("Goal camera rotation for this move") \
        .setType("SFRotation") \
       ) \
       .addField(fieldObject() \
        .setName("tracking") \
        .setAccessType("inputOutput") \
        .setAppinfo("Whether or not camera direction is tracking towards the aimPoint") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("goalAimPoint") \
        .setAccessType("inputOutput") \
        .setAppinfo("Goal aimPoint for this move, ignored if tracking=false") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("goalFieldOfView") \
        .setAccessType("inputOutput") \
        .setAppinfo("Goal fieldOfView for this move") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("goalFStop") \
        .setAccessType("inputOutput") \
        .setAppinfo("Focal length divided effective aperture diameter indicating width of focal plane") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("goalFocusDistance") \
        .setAccessType("inputOutput") \
        .setAppinfo("Distance to focal plane of sharpest focus") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("isActive") \
        .setAccessType("outputOnly") \
        .setAppinfo("Mark start/stop with true/false output respectively useful to trigger external animations") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("traceEnabled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
        .setType("SFBool") \
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
#Add any ROUTEs here, going from Script to other nodes within ProtoBody
     ) \
    ) \
#=============== OfflineRender ==============
    .addChildren(ProtoDeclareObject() \
     .setName("OfflineRender") \
     .setAppinfo("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot).") \
     .setProtoInterface(ProtoInterfaceObject() \
#TODO non-photorealistic rendering (NPR) parameters
      .addField(fieldObject() \
       .setName("description") \
       .setAccessType("inputOutput") \
       .setAppinfo("Text description to be displayed for this OfflineRender") \
       .setType("SFString") \
      ) \
      .addField(fieldObject() \
       .setName("enabled") \
       .setAccessType("inputOutput") \
       .setAppinfo("Whether this OfflineRender can be activated") \
       .setType("SFBool") \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setName("frameRate") \
       .setAccessType("inputOutput") \
       .setAppinfo("Frames per second recorded for this rendering") \
       .setType("SFFloat") \
       .setValue("30") \
      ) \
      .addField(fieldObject() \
       .setName("frameSize") \
       .setAccessType("inputOutput") \
       .setAppinfo("Size of frame in number of pixels width and height") \
       .setType("SFVec2f") \
       .setValue("640 480") \
      ) \
      .addField(fieldObject() \
       .setName("pixelAspectRatio") \
       .setAccessType("inputOutput") \
       .setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1") \
       .setType("SFFloat") \
       .setValue("1.33") \
      ) \
      .addField(fieldObject() \
       .setName("set_startTime") \
       .setAccessType("inputOnly") \
       .setAppinfo("Begin render operation") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("progress") \
       .setAccessType("outputOnly") \
       .setAppinfo("Progress performing render operation (0..1)") \
       .setType("SFFloat") \
      ) \
      .addField(fieldObject() \
       .setName("renderCompleteTime") \
       .setAccessType("outputOnly") \
       .setAppinfo("Render operation complete") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("movieFormat") \
       .setAccessType("initializeOnly") \
       .setAppinfo("Format of rendered output movie (mpeg mp4 etc.), use first supported format") \
       .setType("MFString") \
       .setValue("\"mpeg\"") \
      ) \
      .addField(fieldObject() \
       .setName("imageFormat") \
       .setAccessType("initializeOnly") \
       .setAppinfo("Format of rendered output images (png jpeg gif tiff etc.) use first supported format") \
       .setType("MFString") \
       .setValue("\"png\"") \
      ) \
      .addField(fieldObject() \
       .setName("traceEnabled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("enable console output to trace script computations and prototype progress") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
#First node determines node type of this prototype
#Subsequent nodes do not render, but still must be a valid X3D subgraph
      .addChildren(ScriptObject(mustEvaluate = True) \
       .setDEF("OfflineRenderScript") \
       .addField(fieldObject() \
        .setName("description") \
        .setAccessType("inputOutput") \
        .setAppinfo("Text description to be displayed for this OfflineRender") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("enabled") \
        .setAccessType("inputOutput") \
        .setAppinfo("Whether this OfflineRender can be activated") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("frameRate") \
        .setAccessType("inputOutput") \
        .setAppinfo("Frames per second recorded for this rendering") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("frameSize") \
        .setAccessType("inputOutput") \
        .setAppinfo("Size of frame in number of pixels width and height") \
        .setType("SFVec2f") \
       ) \
       .addField(fieldObject() \
        .setName("pixelAspectRatio") \
        .setAccessType("inputOutput") \
        .setAppinfo("Relative dimensions of pixel height/width typically 1.33 or 1") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("set_startTime") \
        .setAccessType("inputOnly") \
        .setAppinfo("Begin render operation") \
        .setType("SFTime") \
       ) \
       .addField(fieldObject() \
        .setName("progress") \
        .setAccessType("outputOnly") \
        .setAppinfo("Progress performing render operation (0..1)") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("renderCompleteTime") \
        .setAccessType("outputOnly") \
        .setAppinfo("Render operation complete") \
        .setType("SFTime") \
       ) \
       .addField(fieldObject() \
        .setName("movieFormat") \
        .setAccessType("initializeOnly") \
        .setAppinfo("Format of rendered output movie (mpeg mp4 etc.)") \
        .setType("MFString") \
       ) \
       .addField(fieldObject() \
        .setName("imageFormat") \
        .setAccessType("initializeOnly") \
        .setAppinfo("Format of rendered output images (png jpeg gif tiff etc.)") \
        .setType("MFString") \
       ) \
       .addField(fieldObject() \
        .setName("traceEnabled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("enable console output to trace script computations and prototype progress") \
        .setType("SFBool") \
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
#Add any ROUTEs here, going from Script to other nodes within ProtoBody
     ) \
    ) \
#=============== Launch Prototype Example ==============
    .addChildren(BackgroundObject() \
     .setSkyColor([0.282353,0.380392,0.470588]) \
    ) \
    .addChildren(AnchorObject() \
     .setDescription("launch CameraExample scene") \
     .setUrl(["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"]) \
     .addChildren(TransformObject() \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"]) \
        .setFontStyle(FontStyleObject(justify = ["MIDDLE","MIDDLE"]) \
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
