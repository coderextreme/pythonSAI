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
    .addChildren(ProtoDeclareObject() \
     .setName("ArchPrototype") \
     .setAppinfo("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.") \
     .setProtoInterface(ProtoInterfaceObject() \
#COLOR OF ARCH
#INPUT PARAMETERS
#General parameters: measures in meters
#Parameters to create to create shapes related to arch: put true to apply
      .addField(fieldObject() \
       .setName("diffuseColor") \
       .setAccessType("inputOutput") \
       .setAppinfo("color of arch") \
       .setType("SFColor") \
       .setValue("0.2 0.8 0.8") \
      ) \
      .addField(fieldObject() \
       .setName("emissiveColor") \
       .setAccessType("inputOutput") \
       .setAppinfo("color of arch") \
       .setType("SFColor") \
       .setValue("0.2 0.8 0.8") \
      ) \
      .addField(fieldObject() \
       .setName("clearSpanWidth") \
       .setAccessType("initializeOnly") \
       .setAppinfo("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference") \
       .setType("SFFloat") \
       .setValue("4") \
      ) \
      .addField(fieldObject() \
       .setName("riseHeight") \
       .setAccessType("initializeOnly") \
       .setAppinfo("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference") \
       .setType("SFFloat") \
       .setValue("2") \
      ) \
      .addField(fieldObject() \
       .setName("depth") \
       .setAccessType("initializeOnly") \
       .setAppinfo("depth") \
       .setType("SFFloat") \
       .setValue("3") \
      ) \
      .addField(fieldObject() \
       .setName("topAbutmentHeight") \
       .setAccessType("initializeOnly") \
       .setAppinfo("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment") \
       .setType("SFFloat") \
       .setValue("0.5") \
      ) \
      .addField(fieldObject() \
       .setName("pierWidth") \
       .setAccessType("initializeOnly") \
       .setAppinfo("pierWidth:pierWidtht=0 means no pierWidth") \
       .setType("SFFloat") \
       .setValue("0.5") \
      ) \
      .addField(fieldObject() \
       .setName("pierHeight") \
       .setAccessType("initializeOnly") \
       .setAppinfo("pierHeight: pierHeight=0 means no pierHeight") \
       .setType("SFFloat") \
       .setValue("1") \
      ) \
      .addField(fieldObject() \
       .setName("archHalf") \
       .setAccessType("initializeOnly") \
       .setAppinfo("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setName("archHalfExtensionWidth") \
       .setAccessType("initializeOnly") \
       .setAppinfo("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.") \
       .setType("SFFloat") \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setName("onlyIntrados") \
       .setAccessType("initializeOnly") \
       .setAppinfo("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setName("archFilled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setName("archHalfFilled") \
       .setAccessType("initializeOnly") \
       .setAppinfo("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
      .addField(fieldObject() \
       .setName("lintel") \
       .setAccessType("initializeOnly") \
       .setAppinfo("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.") \
       .setType("SFBool") \
       .setValue("false") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
#First node determines node type of this prototype
#IndexedFaceset creates arch
      .addChildren(TransformObject() \
       .setDEF("ArchTransform") \
       .addChildren(ShapeObject() \
        .setDEF("Arch") \
#note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly
        .setGeometry(IndexedFaceSetObject(convex = False, solid = False) \
         .setDEF("ArchIndex") \
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
#Subsequent nodes do not render, but still must be a valid X3D subgraph
#This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs
      .addChildren(ScriptObject() \
       .setDEF("ArchPrototypeScript") \
       .setUrl(["../node/ArchPrototypeScript.js"]) \
#INPUT PARAMETERS
#General parameters
#Parameters to create to create shapes related to arch: put true to apply
#OUTPUT PARAMETERS
       .addField(fieldObject() \
        .setName("clearSpanWidth") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for clearSpanWidth parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("riseHeight") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for riseHeight parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("depth") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for depth parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("topAbutmentHeight") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for topAbutmentHeight parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("pierWidth") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for pierWidth parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("pierHeight") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for pierHeight parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("archHalf") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for archHalf parameter") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("archHalfExtensionWidth") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for archHalfExtensionWidth parameter") \
        .setType("SFFloat") \
       ) \
       .addField(fieldObject() \
        .setName("onlyIntrados") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for onlyIntrados parameter") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("archFilled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for archFilled parameter") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("archHalfFilled") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for archHalfFilled parameter") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("lintel") \
        .setAccessType("initializeOnly") \
        .setAppinfo("user or default input for lintel parameter") \
        .setType("SFBool") \
       ) \
       .addField(fieldObject() \
        .setName("computedScale") \
        .setAccessType("outputOnly") \
        .setAppinfo("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth") \
        .setType("SFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("pointOut") \
        .setAccessType("outputOnly") \
        .setAppinfo("send computed points to the Coordinate node") \
        .setType("MFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("indexOut") \
        .setAccessType("outputOnly") \
        .setAppinfo("send computed indices to the IndexedFaceSet node") \
        .setType("MFInt32") \
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
      .addChildren(ROUTEObject() \
       .setFromField("computedScale") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("scale") \
       .setToNode("ArchTransform") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("pointOut") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("point") \
       .setToNode("ArchChord") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("indexOut") \
       .setFromNode("ArchPrototypeScript") \
       .setToField("set_coordIndex") \
       .setToNode("ArchIndex") \
      ) \
     ) \
    ) \
    .addChildren(ProtoInstanceObject() \
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
#Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare)
    .addChildren(InlineObject() \
     .setDEF("CoordinateAxes") \
     .setUrl(["../data/CoordinateAxes.x3d"]) \
    ) \
   ) \

X3D0.toFileX3D("./future/./ArchPrototype.newf.x3d")
