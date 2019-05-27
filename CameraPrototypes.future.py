import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.2"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("CameraPrototypes.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Camera, CameraShot and CameraMovement prototypes that demonstrate storyboard capabilities and precise camera operation. This is a developmental effort for potential X3D Specification improvement.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Don Brutzman and Jeff Weekley")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("16 March 2009")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("25 October 2016")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("TODO")).setContent(x3dpsail.SFString("Schematron rules, backed up by initialize() checks")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("BeyondViewpointCameraNodesWeb3D2009.pdf")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/specifications/ISO-IEC-FDIS-19775-1.2-X3D-AbstractSpecification/Part01/components/navigation.html")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("subject")).setContent(x3dpsail.SFString("Camera nodes for Viewpoint navigation control")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("CameraExamples.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/content/examples/Basic/development/CameraPrototypes.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        #=============== Camera ==============

        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("Camera")).setAppinfo(x3dpsail.SFString("Camera node provides direct control of scene view to enable cinematic camera animation shot by shot and move by move along with still digital-photography settings for offline rendering of camera images."))
          .setProtoInterface(x3dpsail.ProtoInterface()
            #Viewpoint-related fields, NavigationInfo-related fields and Camera-unique fields

            .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this Camera")).setType(x3dpsail.SFString("SFString")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("position")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera position in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("orientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera rotation in local transformation frame, which is default prior to first CameraShot initialPosition getting activated")).setType(x3dpsail.SFString("SFRotation")).setValue(x3dpsail.SFString("0 0 1 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("fieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("pi/4")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.7854")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("input fraction drives interpolators")).setType(x3dpsail.SFString("SFFloat")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_bind")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("input event binds or unbinds this Camera")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindTime")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("output event indicates when this Camera is bound")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("isBound")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("output event indicates whether this Camera is bound or unbound")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("nearClipPlane")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Vector distance to near clipping plane corresponds to NavigationInfo.avatarSize[0]")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.25")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("farClipPlane")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Vector distance to far clipping plane corresponds to NavigationInfo.visibilityLimit")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("shots")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Array of CameraShot nodes which in turn contain CameraMovement nodes")).setType(x3dpsail.SFString("MFNode"))
              #initialization nodes (if any) go here

              )
            .addField(x3dpsail.field().setName(x3dpsail.SFString("headlight")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether camera headlight is on or off")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("headlightColor")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera headlight color")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("1 1 1")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("headlightIntensity")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera headlight intensity")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("1")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("filterColor")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera filter color that modifies virtual lens capture")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("1 1 1")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("filterTransparency")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera filter transparency that modifies virtual lens capture")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("1")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("upVector")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("upVector changes modify camera orientation (and possibly vice versa)")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 1 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("fStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("5.6")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("focusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("totalDuration")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("offlineRender")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("OfflineRender node")).setType(x3dpsail.SFString("SFNode"))
              #initialization node (if any) goes here

              )
            .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("CameraViewpoint"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("position")).setProtoField(x3dpsail.SFString("position")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("orientation")).setProtoField(x3dpsail.SFString("orientation")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("fieldOfView")).setProtoField(x3dpsail.SFString("fieldOfView")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_bind")).setProtoField(x3dpsail.SFString("set_bind")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("bindTime")).setProtoField(x3dpsail.SFString("bindTime")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("isBound")).setProtoField(x3dpsail.SFString("isBound")))))
            #NavInfo EXAMINE used since some browsers (InstantReality) try to lock view to vertical when flying to avoid disorientation

            .addChild(x3dpsail.NavigationInfo().setDEF(x3dpsail.SFString("CameraNavInfo")).setType(x3dpsail.MFString(["EXAMINE","FLY","ANY"]))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_bind")).setProtoField(x3dpsail.SFString("set_bind")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("headlight")).setProtoField(x3dpsail.SFString("headlight")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("visibilityLimit")).setProtoField(x3dpsail.SFString("farClipPlane")))
                #No need to bind outputs bindTime, isBound from NavigationInfo since Viewpoint outputs will suffice. TODO inform BitManagement that bindTime field is missing.

                ))
            #this DirectionalLight replaces NavigationInfo headlight in order to add color capability

            .addChild(x3dpsail.DirectionalLight().setDEF(x3dpsail.SFString("CameraDirectionalLight")).setGlobal(x3dpsail.SFBool(True))
              #TODO confirm other default field values match NavigationInfo spec

              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("on")).setProtoField(x3dpsail.SFString("headlight")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("color")).setProtoField(x3dpsail.SFString("headlightColor")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("intensity")).setProtoField(x3dpsail.SFString("headlightIntensity")))))
            .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("CameraPositionInterpolator")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFVec3f([0,0,0,0,0,0]))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_fraction")).setProtoField(x3dpsail.SFString("set_fraction")))))
            .addChild(x3dpsail.OrientationInterpolator().setDEF(x3dpsail.SFString("CameraOrientationInterpolator")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFRotation([0,1,0,0,0,1,0,0]))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_fraction")).setProtoField(x3dpsail.SFString("set_fraction")))))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("CameraPositionInterpolator")).setToField(x3dpsail.SFString("position")).setToNode(x3dpsail.SFString("CameraViewpoint")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("CameraOrientationInterpolator")).setToField(x3dpsail.SFString("orientation")).setToNode(x3dpsail.SFString("CameraViewpoint")))
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("CameraScript")).setDirectOutput(x3dpsail.SFBool(True)).setMustEvaluate(x3dpsail.SFBool(True))
              #binding is controlled externally, all camera operations proceed the same regardless of whether bound or not

              .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this Camera")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("position")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera position in local transformation frame")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("orientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera rotation in local transformation frame")).setType(x3dpsail.SFString("SFRotation")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("input fraction drives interpolators")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_bind")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("input event binds or unbinds this Camera")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("fieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("pi/4")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("nearClipPlane")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Vector distance to near clipping plane")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("farClipPlane")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Vector distance to far clipping plane")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("shots")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Array of CameraShot nodes which in turn contain CameraMovement nodes")).setType(x3dpsail.SFString("MFNode"))
                #initialization nodes (if any) go here

                )
              .addField(x3dpsail.field().setName(x3dpsail.SFString("filterColor")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera filter color that modifies virtual lens capture")).setType(x3dpsail.SFString("SFColor")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("filterTransparency")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Camera filter transparency that modifies virtual lens capture")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("upVector")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("upVector changes modify camera orientation (and possibly vice versa)")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("fStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("focusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("totalDuration")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Total duration of contained enabled CameraShot (and thus CameraMovement) move durations")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("offlineRender")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("OfflineRender node")).setType(x3dpsail.SFString("SFNode"))
                #initialization node (if any) goes here

                )
              .addField(x3dpsail.field().setName(x3dpsail.SFString("ViewpointNode")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("node reference to permit getting setting fields from within Script")).setType(x3dpsail.SFString("SFNode"))
                .addChild(x3dpsail.Viewpoint().setUSE(x3dpsail.SFString("CameraViewpoint"))))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("NavInfoNode")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("node reference to permit getting setting fields from within Script")).setType(x3dpsail.SFString("SFNode"))
                .addChild(x3dpsail.NavigationInfo().setUSE(x3dpsail.SFString("CameraNavInfo"))))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("CameraPI")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("node reference to permit getting setting fields from within Script")).setType(x3dpsail.SFString("SFNode"))
                .addChild(x3dpsail.PositionInterpolator().setUSE(x3dpsail.SFString("CameraPositionInterpolator"))))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("CameraOI")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("node reference to permit getting setting fields from within Script")).setType(x3dpsail.SFString("SFNode"))
                .addChild(x3dpsail.OrientationInterpolator().setUSE(x3dpsail.SFString("CameraOrientationInterpolator"))))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("key")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("key array for interpolators")).setType(x3dpsail.SFString("MFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValuePosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("keyValue array for PositionInterpolator")).setType(x3dpsail.SFString("MFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValueOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("keyValue array for OrientationInterpolator")).setType(x3dpsail.SFString("MFRotation")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("animated")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("whether internal CameraShot and CameraMove nodes are tracking or changed via ROUTE events")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialized")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("perform checkShots() function once immediately after initialization")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("shotCount")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("how many CameraShot nodes are contained in shots array")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("movesCount")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("how many CameraMove nodes are contained in moves array")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("frameCount")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("how many frames were created in current loop")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("startTime")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("holding variable")).setType(x3dpsail.SFString("SFTime")).setValue(x3dpsail.SFString("0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("priorTraceTime")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("holding variable")).setType(x3dpsail.SFString("SFTime")).setValue(x3dpsail.SFString("0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("position")).setProtoField(x3dpsail.SFString("position")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("orientation")).setProtoField(x3dpsail.SFString("orientation")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_fraction")).setProtoField(x3dpsail.SFString("set_fraction")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_bind")).setProtoField(x3dpsail.SFString("set_bind")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("fieldOfView")).setProtoField(x3dpsail.SFString("fieldOfView")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("nearClipPlane")).setProtoField(x3dpsail.SFString("nearClipPlane")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("farClipPlane")).setProtoField(x3dpsail.SFString("farClipPlane")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("shots")).setProtoField(x3dpsail.SFString("shots")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("filterColor")).setProtoField(x3dpsail.SFString("filterColor")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("filterTransparency")).setProtoField(x3dpsail.SFString("filterTransparency")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("upVector")).setProtoField(x3dpsail.SFString("upVector")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("fStop")).setProtoField(x3dpsail.SFString("fStop")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("focusDistance")).setProtoField(x3dpsail.SFString("focusDistance")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("isActive")).setProtoField(x3dpsail.SFString("isActive")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("totalDuration")).setProtoField(x3dpsail.SFString("totalDuration")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("offlineRender")).setProtoField(x3dpsail.SFString("offlineRender")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("traceEnabled")).setProtoField(x3dpsail.SFString("traceEnabled")))).setSourceCode('''ecmascript:\n"+
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
)
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("position")).setFromNode(x3dpsail.SFString("CameraScript")).setToField(x3dpsail.SFString("position")).setToNode(x3dpsail.SFString("CameraViewpoint")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("orientation")).setFromNode(x3dpsail.SFString("CameraScript")).setToField(x3dpsail.SFString("orientation")).setToNode(x3dpsail.SFString("CameraViewpoint")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isActive")).setFromNode(x3dpsail.SFString("CameraScript")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("CameraViewpoint")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isActive")).setFromNode(x3dpsail.SFString("CameraScript")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("CameraNavInfo")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isActive")).setFromNode(x3dpsail.SFString("CameraScript")).setToField(x3dpsail.SFString("on")).setToNode(x3dpsail.SFString("CameraDirectionalLight")))))
        #=============== CameraShot ==============

        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("CameraShot")).setAppinfo(x3dpsail.SFString("CameraShot collects a specific set of CameraMovement animations that make up an individual shot."))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this CameraShot")).setType(x3dpsail.SFString("SFString")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this CameraShot can be activated")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("moves")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Set of CameraMovement nodes")).setType(x3dpsail.SFString("MFNode"))
              #initializing CameraMovement nodes are inserted here by scene author using ProtoInstance

              )
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialPosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize camera position for this shot")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize camera rotation for this shot")).setType(x3dpsail.SFString("SFRotation")).setValue(x3dpsail.SFString("0 0 1 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialAimPoint")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize aimpoint (relative location for camera direction) for this shot")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("pi/4")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.7854")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("5.6")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFocusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("shotDuration")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Subtotal duration of contained CameraMovement move durations")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("CameraShotScript")).setDirectOutput(x3dpsail.SFBool(True)).setMustEvaluate(x3dpsail.SFBool(True))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this CameraShot")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this CameraShot can be activated")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("moves")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Set of CameraMovement nodes")).setType(x3dpsail.SFString("MFNode"))
                #initialization nodes (if any) go here

                )
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialPosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize camera position for this shot")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize camera rotation for this shot")).setType(x3dpsail.SFString("SFRotation")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialAimPoint")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Setup to reinitialize aimpoint (relative location for camera direction) for this shot")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("pi/4")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("initialFocusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("shotDuration")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Subtotal duration of contained CameraMovement move durations")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("key")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("key array for interpolators")).setType(x3dpsail.SFString("MFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValuePosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("keyValue array for PositionInterpolator")).setType(x3dpsail.SFString("MFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValueOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("keyValue array for OrientationInterpolator")).setType(x3dpsail.SFString("MFRotation")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("moves")).setProtoField(x3dpsail.SFString("moves")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialPosition")).setProtoField(x3dpsail.SFString("initialPosition")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialOrientation")).setProtoField(x3dpsail.SFString("initialOrientation")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialAimPoint")).setProtoField(x3dpsail.SFString("initialAimPoint")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialFieldOfView")).setProtoField(x3dpsail.SFString("initialFieldOfView")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialFStop")).setProtoField(x3dpsail.SFString("initialFStop")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("initialFocusDistance")).setProtoField(x3dpsail.SFString("initialFocusDistance")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("shotDuration")).setProtoField(x3dpsail.SFString("shotDuration")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("isActive")).setProtoField(x3dpsail.SFString("isActive")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("traceEnabled")).setProtoField(x3dpsail.SFString("traceEnabled")))).setSourceCode('''ecmascript:\n"+
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
)
            #Add any ROUTEs here, going from Script to other nodes within ProtoBody

            ))
        #=============== CameraMovement ==============

        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("CameraMovement")).setAppinfo(x3dpsail.SFString("CameraMovement node defines a single camera movement animation including goalPosition, goalOrientation, goalAimPoint and goalFieldOfView."))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this CameraMovement")).setType(x3dpsail.SFString("SFString")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this CameraMovement can be activated")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("duration")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Duration in seconds for this move")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalPosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal camera position for this move")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal camera rotation for this move")).setType(x3dpsail.SFString("SFRotation")).setValue(x3dpsail.SFString("0 0 1 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("tracking")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether or not camera direction is tracking towards the aimPoint")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalAimPoint")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal aimPoint for this move, ignored if tracking=false")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal fieldOfView for this move")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.7854")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("5.6")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFocusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("10")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false"))))
          .setProtoBody(x3dpsail.ProtoBody()
            #First node determines node type of this prototype

            #Subsequent nodes do not render, but still must be a valid X3D subgraph

            #Script holds CameraMovement initialization values for query by parent CameraShot, and also permits changing values via events

            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("CameraMovementScript")).setDirectOutput(x3dpsail.SFBool(True)).setMustEvaluate(x3dpsail.SFBool(True))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this CameraMovement")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this CameraMovement can be activated")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("duration")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Duration in seconds for this move")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalPosition")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal camera position for this move")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalOrientation")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal camera rotation for this move")).setType(x3dpsail.SFString("SFRotation")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("tracking")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether or not camera direction is tracking towards the aimPoint")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalAimPoint")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal aimPoint for this move, ignored if tracking=false")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFieldOfView")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Goal fieldOfView for this move")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFStop")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Focal length divided effective aperture diameter indicating width of focal plane")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("goalFocusDistance")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Distance to focal plane of sharpest focus")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("isActive")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Mark start/stop with true/false output respectively useful to trigger external animations")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("duration")).setProtoField(x3dpsail.SFString("duration")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalPosition")).setProtoField(x3dpsail.SFString("goalPosition")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalOrientation")).setProtoField(x3dpsail.SFString("goalOrientation")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("tracking")).setProtoField(x3dpsail.SFString("tracking")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalAimPoint")).setProtoField(x3dpsail.SFString("goalAimPoint")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalFieldOfView")).setProtoField(x3dpsail.SFString("goalFieldOfView")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalFStop")).setProtoField(x3dpsail.SFString("goalFStop")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("goalFocusDistance")).setProtoField(x3dpsail.SFString("goalFocusDistance")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("isActive")).setProtoField(x3dpsail.SFString("isActive")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("traceEnabled")).setProtoField(x3dpsail.SFString("traceEnabled")))).setSourceCode('''ecmascript:\n"+
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
)
            #Add any ROUTEs here, going from Script to other nodes within ProtoBody

            ))
        #=============== OfflineRender ==============

        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("OfflineRender")).setAppinfo(x3dpsail.SFString("OfflineRender defines a parameters for offline rendering of Camera animation output to a movie file (or possibly a still shot)."))
          .setProtoInterface(x3dpsail.ProtoInterface()
            #TODO non-photorealistic rendering (NPR) parameters

            .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this OfflineRender")).setType(x3dpsail.SFString("SFString")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this OfflineRender can be activated")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("frameRate")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Frames per second recorded for this rendering")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("30")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("frameSize")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Size of frame in number of pixels width and height")).setType(x3dpsail.SFString("SFVec2f")).setValue(x3dpsail.SFString("640 480")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("pixelAspectRatio")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Relative dimensions of pixel height/width typically 1.33 or 1")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("1.33")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startTime")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("Begin render operation")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("progress")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Progress performing render operation (0..1)")).setType(x3dpsail.SFString("SFFloat")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("renderCompleteTime")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Render operation complete")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("movieFormat")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("Format of rendered output movie (mpeg mp4 etc.), use first supported format")).setType(x3dpsail.SFString("MFString")).setValue(x3dpsail.SFString("\"mpeg\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("imageFormat")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("Format of rendered output images (png jpeg gif tiff etc.) use first supported format")).setType(x3dpsail.SFString("MFString")).setValue(x3dpsail.SFString("\"png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false"))))
          .setProtoBody(x3dpsail.ProtoBody()
            #First node determines node type of this prototype

            #Subsequent nodes do not render, but still must be a valid X3D subgraph

            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("OfflineRenderScript")).setMustEvaluate(x3dpsail.SFBool(True))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("description")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Text description to be displayed for this OfflineRender")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("enabled")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Whether this OfflineRender can be activated")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("frameRate")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Frames per second recorded for this rendering")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("frameSize")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Size of frame in number of pixels width and height")).setType(x3dpsail.SFString("SFVec2f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("pixelAspectRatio")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("Relative dimensions of pixel height/width typically 1.33 or 1")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startTime")).setAccessType(x3dpsail.SFString("inputOnly")).setAppinfo(x3dpsail.SFString("Begin render operation")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("progress")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Progress performing render operation (0..1)")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("renderCompleteTime")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("Render operation complete")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("movieFormat")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("Format of rendered output movie (mpeg mp4 etc.)")).setType(x3dpsail.SFString("MFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("imageFormat")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("Format of rendered output images (png jpeg gif tiff etc.)")).setType(x3dpsail.SFString("MFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("traceEnabled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("enable console output to trace script computations and prototype progress")).setType(x3dpsail.SFString("SFBool")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("frameRate")).setProtoField(x3dpsail.SFString("frameRate")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("frameSize")).setProtoField(x3dpsail.SFString("frameSize")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("pixelAspectRatio")).setProtoField(x3dpsail.SFString("pixelAspectRatio")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_startTime")).setProtoField(x3dpsail.SFString("set_startTime")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("progress")).setProtoField(x3dpsail.SFString("progress")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("renderCompleteTime")).setProtoField(x3dpsail.SFString("renderCompleteTime")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("movieFormat")).setProtoField(x3dpsail.SFString("movieFormat")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("imageFormat")).setProtoField(x3dpsail.SFString("imageFormat")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("traceEnabled")).setProtoField(x3dpsail.SFString("traceEnabled")))).setSourceCode('''ecmascript:\n"+
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
)
            #Add any ROUTEs here, going from Script to other nodes within ProtoBody

            ))
        #=============== Launch Prototype Example ==============

        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([0.282353,0.380392,0.470588])))
        .addChild(x3dpsail.Anchor().setDescription(x3dpsail.SFString("launch CameraExample scene")).setUrl(x3dpsail.MFString(["CameraExamples.x3d","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.x3d","CameraExamples.wrl","http://www.web3d.org/x3d/content/examples/Basic/development/CameraExamples.wrl"]))
          .addChild(x3dpsail.Transform()
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["CameraPrototypes.x3d","defines multiple prototype nodes","","Click on this text to see","CameraExamples.x3d scene"]))
                .setFontStyle(x3dpsail.FontStyle().setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"]))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,1,0.2)))))))))

X3D0.toFileX3D("./future/./CameraPrototypes_RoundTrip.x3d")
