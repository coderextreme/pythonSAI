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
     .setContent("ArchPrototype.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Michele Foti, Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("15 December 2014") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("27 November 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("ArchModelingDiagrams.pdf") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("https://en.wikipedia.org/wiki/Arch") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d") \
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
    .addChild(ProtoDeclareObject() \
     .setName("ArchPrototype") \
     .setAppinfo("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.") \
     .setProtoInterface(ProtoInterfaceObject() \
.addComments(CommentsBlock("""COLOR OF ARCH""")) \
.addComments(CommentsBlock("""INPUT PARAMETERS""")) \
.addComments(CommentsBlock("""General parameters: measures in meters""")) \
.addComments(CommentsBlock("""Parameters to create to create shapes related to arch: put true to apply""")) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("diffuseColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("color of arch") \
       .setValue("0.2 0.8 0.8") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("emissiveColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("color of arch") \
       .setValue("0.2 0.8 0.8") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("clearSpanWidth") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference") \
       .setValue("4") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("riseHeight") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference") \
       .setValue("2") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("depth") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("depth") \
       .setValue("3") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("topAbutmentHeight") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment") \
       .setValue("0.5") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("pierWidth") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("pierWidth:pierWidtht=0 means no pierWidth") \
       .setValue("0.5") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("pierHeight") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("pierHeight: pierHeight=0 means no pierHeight") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("archHalf") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("archHalfExtensionWidth") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("onlyIntrados") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("archFilled") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("archHalfFilled") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("lintel") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setAppinfo("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
.addComments(CommentsBlock("""First node determines node type of this prototype""")) \
.addComments(CommentsBlock("""IndexedFaceset creates arch""")) \
      .addChild(TransformObject() \
       .setDEF("ArchTransform") \
       .addChild(ShapeObject() \
        .setDEF("Arch") \
.addComments(CommentsBlock("""note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly""")) \
        .setGeometry(IndexedFaceSetObject() \
         .setDEF("ArchIndex") \
         .setConvex(False) \
         .setSolid(False) \
         .setCoord(CoordinateObject() \
          .setDEF("ArchChord") \
         ) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDEF("MaterialNode") \
          .setIS(ISObject() \
           .addConnect(connectObject() \
            .setNodeField("emissiveColor") \
            .setProtoField("emissiveColor") \
           ) \
           .addConnect(connectObject() \
            .setNodeField("diffuseColor") \
            .setProtoField("diffuseColor") \
           ) \
          ) \
         ) \
        ) \
       ) \
      ) \
.addComments(CommentsBlock("""Subsequent nodes do not render, but still must be a valid X3D subgraph""")) \
.addComments(CommentsBlock("""This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs""")) \
      .addChild(ScriptObject() \
       .setDEF("ArchPrototypeScript") \
       .setUrl(["../node/ArchPrototypeScript.js"]) \
.addComments(CommentsBlock("""INPUT PARAMETERS""")) \
.addComments(CommentsBlock("""General parameters""")) \
.addComments(CommentsBlock("""Parameters to create to create shapes related to arch: put true to apply""")) \
.addComments(CommentsBlock("""OUTPUT PARAMETERS""")) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("clearSpanWidth") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for clearSpanWidth parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("riseHeight") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for riseHeight parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("depth") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for depth parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("topAbutmentHeight") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for topAbutmentHeight parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("pierWidth") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for pierWidth parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("pierHeight") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for pierHeight parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("archHalf") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for archHalf parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("archHalfExtensionWidth") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for archHalfExtensionWidth parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("onlyIntrados") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for onlyIntrados parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("archFilled") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for archFilled parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("archHalfFilled") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for archHalfFilled parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("lintel") \
        .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        .setAppinfo("user or default input for lintel parameter") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("computedScale") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
        .setAppinfo("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFVEC3F) \
        .setName("pointOut") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
        .setAppinfo("send computed points to the Coordinate node") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFINT32) \
        .setName("indexOut") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
        .setAppinfo("send computed indices to the IndexedFaceSet node") \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("clearSpanWidth") \
         .setProtoField("clearSpanWidth") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("riseHeight") \
         .setProtoField("riseHeight") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("depth") \
         .setProtoField("depth") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("pierWidth") \
         .setProtoField("pierWidth") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("topAbutmentHeight") \
         .setProtoField("topAbutmentHeight") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("pierHeight") \
         .setProtoField("pierHeight") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("archHalf") \
         .setProtoField("archHalf") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("archHalfExtensionWidth") \
         .setProtoField("archHalfExtensionWidth") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("onlyIntrados") \
         .setProtoField("onlyIntrados") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("archFilled") \
         .setProtoField("archFilled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("archHalfFilled") \
         .setProtoField("archHalfFilled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("lintel") \
         .setProtoField("lintel") \
        ) \
       ) \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("computedScale") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("scale") \
       .setToNode("ArchTransform") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("pointOut") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("point") \
       .setToNode("ArchChord") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("indexOut") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("set_coordIndex") \
       .setToNode("ArchIndex") \
      ) \
     ) \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("ArchPrototype") \
     .setDEF("ArchInstance") \
     .addFieldValue(fieldValueObject() \
      .setName("diffuseColor") \
      .setValue("0.5 0.3 0.6") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("emissiveColor") \
      .setValue("0.5 0.3 0.6") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("clearSpanWidth") \
      .setValue("5") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("riseHeight") \
      .setValue("2.5") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("depth") \
      .setValue("2") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("topAbutmentHeight") \
      .setValue("0.6") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("pierWidth") \
      .setValue("1") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("pierHeight") \
      .setValue("2") \
     ) \
    ) \
.addComments(CommentsBlock("""Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare)""")) \
    .addChild(InlineObject() \
     .setDEF("CoordinateAxes") \
     .setUrl(["../data/CoordinateAxes.x3d"]) \
    ) \
   ) \

X3D0.toFileX3D("./future/./ArchPrototype.newf.x3d")
