import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("ArchPrototype.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Michele Foti, Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("15 December 2014")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("27 November 2015")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("ArchModelingDiagrams.pdf")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("https://en.wikipedia.org/wiki/Arch")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("ArchPrototype")).setAppinfo(x3dpsail.SFString("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js."))
          .setProtoInterface(x3dpsail.ProtoInterface()
            #COLOR OF ARCH

            #INPUT PARAMETERS

            #General parameters: measures in meters

            #Parameters to create to create shapes related to arch: put true to apply

            .addField(x3dpsail.field().setName(x3dpsail.SFString("diffuseColor")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("color of arch")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("0.2 0.8 0.8")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("emissiveColor")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("color of arch")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("0.2 0.8 0.8")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("clearSpanWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("4")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("riseHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("depth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("depth")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("3")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("topAbutmentHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("pierWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("pierWidth:pierWidtht=0 means no pierWidth")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("pierHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("pierHeight: pierHeight=0 means no pierHeight")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("1")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalf")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalfExtensionWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("onlyIntrados")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("archFilled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalfFilled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("lintel")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("false"))))
          .setProtoBody(x3dpsail.ProtoBody()
            #First node determines node type of this prototype

            #IndexedFaceset creates arch

            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("ArchTransform"))
              .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("Arch"))
                #note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly

                .setGeometry(x3dpsail.IndexedFaceSet().setDEF(x3dpsail.SFString("ArchIndex")).setConvex(x3dpsail.SFBool(False)).setSolid(x3dpsail.SFBool(False))
                  .setCoord(x3dpsail.Coordinate().setDEF(x3dpsail.SFString("ArchChord"))))
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDEF(x3dpsail.SFString("MaterialNode"))
                    .setIS(x3dpsail.IS()
                      .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("emissiveColor")).setProtoField(x3dpsail.SFString("emissiveColor")))
                      .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("diffuseColor")).setProtoField(x3dpsail.SFString("diffuseColor"))))))))
            #Subsequent nodes do not render, but still must be a valid X3D subgraph

            #This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs

            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("ArchPrototypeScript")).setUrl(x3dpsail.MFString(["../node/ArchPrototypeScript.js"]))
              #INPUT PARAMETERS

              #General parameters

              #Parameters to create to create shapes related to arch: put true to apply

              #OUTPUT PARAMETERS

              .addField(x3dpsail.field().setName(x3dpsail.SFString("clearSpanWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for clearSpanWidth parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("riseHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for riseHeight parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("depth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for depth parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("topAbutmentHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for topAbutmentHeight parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("pierWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for pierWidth parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("pierHeight")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for pierHeight parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalf")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for archHalf parameter")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalfExtensionWidth")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for archHalfExtensionWidth parameter")).setType(x3dpsail.SFString("SFFloat")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("onlyIntrados")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for onlyIntrados parameter")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("archFilled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for archFilled parameter")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("archHalfFilled")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for archHalfFilled parameter")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("lintel")).setAccessType(x3dpsail.SFString("initializeOnly")).setAppinfo(x3dpsail.SFString("user or default input for lintel parameter")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("computedScale")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("pointOut")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("send computed points to the Coordinate node")).setType(x3dpsail.SFString("MFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("indexOut")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("send computed indices to the IndexedFaceSet node")).setType(x3dpsail.SFString("MFInt32")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("clearSpanWidth")).setProtoField(x3dpsail.SFString("clearSpanWidth")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("riseHeight")).setProtoField(x3dpsail.SFString("riseHeight")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("depth")).setProtoField(x3dpsail.SFString("depth")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("pierWidth")).setProtoField(x3dpsail.SFString("pierWidth")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("topAbutmentHeight")).setProtoField(x3dpsail.SFString("topAbutmentHeight")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("pierHeight")).setProtoField(x3dpsail.SFString("pierHeight")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("archHalf")).setProtoField(x3dpsail.SFString("archHalf")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("archHalfExtensionWidth")).setProtoField(x3dpsail.SFString("archHalfExtensionWidth")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("onlyIntrados")).setProtoField(x3dpsail.SFString("onlyIntrados")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("archFilled")).setProtoField(x3dpsail.SFString("archFilled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("archHalfFilled")).setProtoField(x3dpsail.SFString("archHalfFilled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("lintel")).setProtoField(x3dpsail.SFString("lintel")))))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("computedScale")).setFromNode(x3dpsail.SFString("ArchPrototypeScript")).setToField(x3dpsail.SFString("scale")).setToNode(x3dpsail.SFString("ArchTransform")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("pointOut")).setFromNode(x3dpsail.SFString("ArchPrototypeScript")).setToField(x3dpsail.SFString("point")).setToNode(x3dpsail.SFString("ArchChord")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("indexOut")).setFromNode(x3dpsail.SFString("ArchPrototypeScript")).setToField(x3dpsail.SFString("set_coordIndex")).setToNode(x3dpsail.SFString("ArchIndex")))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("ArchPrototype")).setDEF(x3dpsail.SFString("ArchInstance"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("diffuseColor")).setValue(x3dpsail.SFString("0.5 0.3 0.6")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("emissiveColor")).setValue(x3dpsail.SFString("0.5 0.3 0.6")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("clearSpanWidth")).setValue(x3dpsail.SFString("5")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("riseHeight")).setValue(x3dpsail.SFString("2.5")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("depth")).setValue(x3dpsail.SFString("2")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("topAbutmentHeight")).setValue(x3dpsail.SFString("0.6")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("pierWidth")).setValue(x3dpsail.SFString("1")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("pierHeight")).setValue(x3dpsail.SFString("2"))))
        #Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare)

        .addChild(x3dpsail.Inline().setDEF(x3dpsail.SFString("CoordinateAxes")).setUrl(x3dpsail.MFString(["../data/CoordinateAxes.x3d"])))))

X3D0.toFileX3D("./future/./ArchPrototype_RoundTrip.x3d")
