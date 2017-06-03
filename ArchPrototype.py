from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.3")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("ArchPrototype.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("description").setContent("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.")
head1.addMeta(meta3)
meta4 = metaObject().setName("description").setContent("Possibility to create shapes related to arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information.")
head1.addMeta(meta4)
meta5 = metaObject().setName("creator").setContent("Michele Foti, Don Brutzman")
head1.addMeta(meta5)
meta6 = metaObject().setName("created").setContent("15 December 2014")
head1.addMeta(meta6)
meta7 = metaObject().setName("modified").setContent("27 November 2015")
head1.addMeta(meta7)
meta8 = metaObject().setName("reference").setContent("ArchModelingDiagrams.pdf")
head1.addMeta(meta8)
meta9 = metaObject().setName("reference").setContent("https://en.wikipedia.org/wiki/Arch")
head1.addMeta(meta9)
meta10 = metaObject().setName("identifier").setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchPrototype.x3d")
head1.addMeta(meta10)
meta11 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta11)
meta12 = metaObject().setName("license").setContent("../license.html")
head1.addMeta(meta12)
X3D0.setHead(head1)
Scene13 = SceneObject()
ProtoDeclare14 = ProtoDeclareObject().setName("ArchPrototype").setAppinfo("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.")
ProtoInterface15 = ProtoInterfaceObject()

ProtoInterface15.addComments(CommentsBlock("COLOR OF ARCH"))

ProtoInterface15.addComments(CommentsBlock("INPUT PARAMETERS"))

ProtoInterface15.addComments(CommentsBlock("General parameters: measures in meters"))

ProtoInterface15.addComments(CommentsBlock("Parameters to create to create shapes related to arch: put true to apply"))
field16 = fieldObject().setType(fieldObject.TYPE_SFCOLOR).setName("diffuseColor").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setAppinfo("color of arch").setValue("0.2 0.8 0.8")
ProtoInterface15.addField(field16)
field17 = fieldObject().setType(fieldObject.TYPE_SFCOLOR).setName("emissiveColor").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setAppinfo("color of arch").setValue("0.2 0.8 0.8")
ProtoInterface15.addField(field17)
field18 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("clearSpanWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference").setValue("4")
ProtoInterface15.addField(field18)
field19 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("riseHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference").setValue("2")
ProtoInterface15.addField(field19)
field20 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("depth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("depth").setValue("3")
ProtoInterface15.addField(field20)
field21 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("topAbutmentHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment").setValue("0.5")
ProtoInterface15.addField(field21)
field22 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("pierWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("pierWidth:pierWidtht=0 means no pierWidth").setValue("0.5")
ProtoInterface15.addField(field22)
field23 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("pierHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("pierHeight: pierHeight=0 means no pierHeight").setValue("1")
ProtoInterface15.addField(field23)
field24 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archHalf").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width").setValue("false")
ProtoInterface15.addField(field24)
field25 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("archHalfExtensionWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.").setValue("0")
ProtoInterface15.addField(field25)
field26 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("onlyIntrados").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.").setValue("false")
ProtoInterface15.addField(field26)
field27 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.").setValue("false")
ProtoInterface15.addField(field27)
field28 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archHalfFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.").setValue("false")
ProtoInterface15.addField(field28)
field29 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("lintel").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.").setValue("false")
ProtoInterface15.addField(field29)
ProtoDeclare14.setProtoInterface(ProtoInterface15)
ProtoBody30 = ProtoBodyObject()

ProtoBody30.addComments(CommentsBlock("First node determines node type of this prototype"))

ProtoBody30.addComments(CommentsBlock("IndexedFaceset creates arch"))
Transform31 = TransformObject().setDEF("ArchTransform")
Shape32 = ShapeObject().setDEF("Arch")

Shape32.addComments(CommentsBlock("note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly"))
IndexedFaceSet33 = IndexedFaceSetObject().setDEF("ArchIndex").setConvex(False).setSolid(False)
Coordinate34 = CoordinateObject().setDEF("ArchChord")
IndexedFaceSet33.setCoord(Coordinate34)
Shape32.setGeometry(IndexedFaceSet33)
Appearance35 = AppearanceObject()
Material36 = MaterialObject().setDEF("MaterialNode")
IS37 = ISObject()
connect38 = connectObject().setNodeField("emissiveColor").setProtoField("emissiveColor")
IS37.addConnect(connect38)
connect39 = connectObject().setNodeField("diffuseColor").setProtoField("diffuseColor")
IS37.addConnect(connect39)
Material36.setIS(IS37)
Appearance35.setMaterial(Material36)
Shape32.setAppearance(Appearance35)
Transform31.addChild(Shape32)
ProtoBody30.addChild(Transform31)

ProtoBody30.addComments(CommentsBlock("Subsequent nodes do not render, but still must be a valid X3D subgraph"))

ProtoBody30.addComments(CommentsBlock("This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs"))
Script40 = ScriptObject().setDEF("ArchPrototypeScript").setUrl(["ArchPrototypeScript.js"])

Script40.addComments(CommentsBlock("INPUT PARAMETERS"))

Script40.addComments(CommentsBlock("General parameters"))

Script40.addComments(CommentsBlock("Parameters to create to create shapes related to arch: put true to apply"))

Script40.addComments(CommentsBlock("OUTPUT PARAMETERS"))
field41 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("clearSpanWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for clearSpanWidth parameter")
Script40.addField(field41)
field42 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("riseHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for riseHeight parameter")
Script40.addField(field42)
field43 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("depth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for depth parameter")
Script40.addField(field43)
field44 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("topAbutmentHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for topAbutmentHeight parameter")
Script40.addField(field44)
field45 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("pierWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for pierWidth parameter")
Script40.addField(field45)
field46 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("pierHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for pierHeight parameter")
Script40.addField(field46)
field47 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archHalf").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalf parameter")
Script40.addField(field47)
field48 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("archHalfExtensionWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalfExtensionWidth parameter")
Script40.addField(field48)
field49 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("onlyIntrados").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for onlyIntrados parameter")
Script40.addField(field49)
field50 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archFilled parameter")
Script40.addField(field50)
field51 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("archHalfFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalfFilled parameter")
Script40.addField(field51)
field52 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("lintel").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for lintel parameter")
Script40.addField(field52)
field53 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("computedScale").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth")
Script40.addField(field53)
field54 = fieldObject().setType(fieldObject.TYPE_MFVEC3F).setName("pointOut").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("send computed points to the Coordinate node")
Script40.addField(field54)
field55 = fieldObject().setType(fieldObject.TYPE_MFINT32).setName("indexOut").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("send computed indices to the IndexedFaceSet node")
Script40.addField(field55)
IS56 = ISObject()
connect57 = connectObject().setNodeField("clearSpanWidth").setProtoField("clearSpanWidth")
IS56.addConnect(connect57)
connect58 = connectObject().setNodeField("riseHeight").setProtoField("riseHeight")
IS56.addConnect(connect58)
connect59 = connectObject().setNodeField("depth").setProtoField("depth")
IS56.addConnect(connect59)
connect60 = connectObject().setNodeField("pierWidth").setProtoField("pierWidth")
IS56.addConnect(connect60)
connect61 = connectObject().setNodeField("topAbutmentHeight").setProtoField("topAbutmentHeight")
IS56.addConnect(connect61)
connect62 = connectObject().setNodeField("pierHeight").setProtoField("pierHeight")
IS56.addConnect(connect62)
connect63 = connectObject().setNodeField("archHalf").setProtoField("archHalf")
IS56.addConnect(connect63)
connect64 = connectObject().setNodeField("archHalfExtensionWidth").setProtoField("archHalfExtensionWidth")
IS56.addConnect(connect64)
connect65 = connectObject().setNodeField("onlyIntrados").setProtoField("onlyIntrados")
IS56.addConnect(connect65)
connect66 = connectObject().setNodeField("archFilled").setProtoField("archFilled")
IS56.addConnect(connect66)
connect67 = connectObject().setNodeField("archHalfFilled").setProtoField("archHalfFilled")
IS56.addConnect(connect67)
connect68 = connectObject().setNodeField("lintel").setProtoField("lintel")
IS56.addConnect(connect68)
Script40.setIS(IS56)
ProtoBody30.addChild(Script40)
ROUTE69 = ROUTEObject().setFromField("computedScale").setFromNode("ArchPrototypeScript").setToField("scale").setToNode("ArchTransform")
ProtoBody30.addChild(ROUTE69)
ROUTE70 = ROUTEObject().setFromField("pointOut").setFromNode("ArchPrototypeScript").setToField("point").setToNode("ArchChord")
ProtoBody30.addChild(ROUTE70)
ROUTE71 = ROUTEObject().setFromField("indexOut").setFromNode("ArchPrototypeScript").setToField("set_coordIndex").setToNode("ArchIndex")
ProtoBody30.addChild(ROUTE71)
ProtoDeclare14.setProtoBody(ProtoBody30)
Scene13.addChild(ProtoDeclare14)
ProtoInstance72 = ProtoInstanceObject().setName("ArchPrototype").setDEF("ArchInstance")
fieldValue73 = fieldValueObject().setName("diffuseColor").setValue("0.5 0.3 0.6")
ProtoInstance72.addFieldValue(fieldValue73)
fieldValue74 = fieldValueObject().setName("emissiveColor").setValue("0.5 0.3 0.6")
ProtoInstance72.addFieldValue(fieldValue74)
fieldValue75 = fieldValueObject().setName("clearSpanWidth").setValue("5")
ProtoInstance72.addFieldValue(fieldValue75)
fieldValue76 = fieldValueObject().setName("riseHeight").setValue("2.5")
ProtoInstance72.addFieldValue(fieldValue76)
fieldValue77 = fieldValueObject().setName("depth").setValue("2")
ProtoInstance72.addFieldValue(fieldValue77)
fieldValue78 = fieldValueObject().setName("topAbutmentHeight").setValue("0.6")
ProtoInstance72.addFieldValue(fieldValue78)
fieldValue79 = fieldValueObject().setName("pierWidth").setValue("1")
ProtoInstance72.addFieldValue(fieldValue79)
fieldValue80 = fieldValueObject().setName("pierHeight").setValue("2")
ProtoInstance72.addFieldValue(fieldValue80)
Scene13.addChild(ProtoInstance72)

Scene13.addComments(CommentsBlock("Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare)"))
Inline81 = InlineObject().setDEF("CoordinateAxes").setUrl(["CoordinateAxes.x3d"])
Scene13.addChild(Inline81)
X3D0.setScene(Scene13)

X3D0.toFileX3D("./ArchPrototype.new.x3d")
