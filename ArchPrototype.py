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
meta13 = metaObject().setName("translated").setContent("06 May 2017")
head1.addMeta(meta13)
meta14 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta14)
meta15 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta15)
meta16 = metaObject().setName("translated").setContent("6 May 2017")
head1.addMeta(meta16)
meta17 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta17)
X3D0.setHead(head1)
Scene18 = SceneObject()
ProtoDeclare19 = ProtoDeclareObject().setName("ArchPrototype").setAppinfo("Create an arch. Can modify general parameters: clearSpanWidth, riseHeight, depth, topAbutmentHeight, pierWidth, pierHeight. - Possibility to create shapes related to an arch: ArchHalf; IntradosOnly; ArchFilled; ArchHalfFilled; Lintel. See the reference file ArchModelingDiagrams.pdf to find further information. See also ArchPrototypeScript_more_readable.js.js.")
ProtoInterface20 = ProtoInterfaceObject()

ProtoInterface20.addComments(CommentsBlock("COLOR OF ARCH"))

ProtoInterface20.addComments(CommentsBlock("INPUT PARAMETERS"))

ProtoInterface20.addComments(CommentsBlock("General parameters: measures in meters"))

ProtoInterface20.addComments(CommentsBlock("Parameters to create to create shapes related to arch: put true to apply"))
field21 = fieldObject().setName("diffuseColor").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setAppinfo("color of arch").setType(fieldObject.TYPE_SFCOLOR).setValue("0.2 0.8 0.8")
ProtoInterface20.addField(field21)
field22 = fieldObject().setName("emissiveColor").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setAppinfo("color of arch").setType(fieldObject.TYPE_SFCOLOR).setValue("0.2 0.8 0.8")
ProtoInterface20.addField(field22)
field23 = fieldObject().setName("clearSpanWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("clearSpanWidth: clearSpanWidth must be double of riseHeight to obtain an half circumference").setType(fieldObject.TYPE_SFFLOAT).setValue("4")
ProtoInterface20.addField(field23)
field24 = fieldObject().setName("riseHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("riseHeight: riseHeight must be half of clearSpanWidth to obtain an half circumference").setType(fieldObject.TYPE_SFFLOAT).setValue("2")
ProtoInterface20.addField(field24)
field25 = fieldObject().setName("depth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("depth").setType(fieldObject.TYPE_SFFLOAT).setValue("3")
ProtoInterface20.addField(field25)
field26 = fieldObject().setName("topAbutmentHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("topAbutmentHeight:topAbutmentHeight=0 means no topAbutment").setType(fieldObject.TYPE_SFFLOAT).setValue("0.5")
ProtoInterface20.addField(field26)
field27 = fieldObject().setName("pierWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("pierWidth:pierWidtht=0 means no pierWidth").setType(fieldObject.TYPE_SFFLOAT).setValue("0.5")
ProtoInterface20.addField(field27)
field28 = fieldObject().setName("pierHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("pierHeight: pierHeight=0 means no pierHeight").setType(fieldObject.TYPE_SFFLOAT).setValue("1")
ProtoInterface20.addField(field28)
field29 = fieldObject().setName("archHalf").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalf: can modify also clearSpanWidth, riseHeight, depth, pierWidth, pierHeight, topAbutmentHeight, archHalfExtensionWidth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width").setType(fieldObject.TYPE_SFBOOL).setValue("false")
ProtoInterface20.addField(field29)
field30 = fieldObject().setName("archHalfExtensionWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalfExtensionWidth: measure in meters, use only if archHalf=true, it is the width of the etension of the abutment of the archHalf. See the reference file ArchModelingDiagrams.pdf to find further information.").setType(fieldObject.TYPE_SFFLOAT).setValue("0")
ProtoInterface20.addField(field30)
field31 = fieldObject().setName("onlyIntrados").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("onlyIntrados: note it is a flat curved surface, can modify also clearSpanWidth, riseHeight, depth at purpose, if needed apply archHalf=true.").setType(fieldObject.TYPE_SFBOOL).setValue("false")
ProtoInterface20.addField(field31)
field32 = fieldObject().setName("archFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archFilled: note it is an half cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose.").setType(fieldObject.TYPE_SFBOOL).setValue("false")
ProtoInterface20.addField(field32)
field33 = fieldObject().setName("archHalfFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("archHalfFilled: note it is a quarter cylinder, can modify also clearSpanWidth, riseHeight, depth at purpose, clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalfFilled width.").setType(fieldObject.TYPE_SFBOOL).setValue("false")
ProtoInterface20.addField(field33)
field34 = fieldObject().setName("lintel").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("lintel: no arc is rendered, but a lintel: topAbutmentHeight on pierHeight, total height is pierHeight + topAbutmentHeight, if needed apply archHalf=true.").setType(fieldObject.TYPE_SFBOOL).setValue("false")
ProtoInterface20.addField(field34)
ProtoDeclare19.setProtoInterface(ProtoInterface20)
ProtoBody35 = ProtoBodyObject()

ProtoBody35.addComments(CommentsBlock("First node determines node type of this prototype"))

ProtoBody35.addComments(CommentsBlock("IndexedFaceset creates arch"))
Transform36 = TransformObject().setDEF("ArchTransform")
Shape37 = ShapeObject().setDEF("Arch")

Shape37.addComments(CommentsBlock("note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly"))
IndexedFaceSet38 = IndexedFaceSetObject().setDEF("ArchIndex").setConvex(False).setSolid(False)
Coordinate39 = CoordinateObject().setDEF("ArchChord")
IndexedFaceSet38.setCoord(Coordinate39)
Shape37.setGeometry(IndexedFaceSet38)
Appearance40 = AppearanceObject()
Material41 = MaterialObject().setDEF("MaterialNode")
IS42 = ISObject()
connect43 = connectObject().setNodeField("emissiveColor").setProtoField("emissiveColor")
IS42.addConnect(connect43)
connect44 = connectObject().setNodeField("diffuseColor").setProtoField("diffuseColor")
IS42.addConnect(connect44)
Material41.setIS(IS42)
Appearance40.setMaterial(Material41)
Shape37.setAppearance(Appearance40)
Transform36.addChild(Shape37)
ProtoBody35.addChild(Transform36)

ProtoBody35.addComments(CommentsBlock("Subsequent nodes do not render, but still must be a valid X3D subgraph"))

ProtoBody35.addComments(CommentsBlock("This embedded Script provides the X3D author with additional visibility and control over prototype inputs and outputs"))
Script45 = ScriptObject().setDEF("ArchPrototypeScript").setUrl(["ArchPrototypeScript.js"])

Script45.addComments(CommentsBlock("INPUT PARAMETERS"))

Script45.addComments(CommentsBlock("General parameters"))

Script45.addComments(CommentsBlock("Parameters to create to create shapes related to arch: put true to apply"))

Script45.addComments(CommentsBlock("OUTPUT PARAMETERS"))
field46 = fieldObject().setName("clearSpanWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for clearSpanWidth parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field46)
field47 = fieldObject().setName("riseHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for riseHeight parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field47)
field48 = fieldObject().setName("depth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for depth parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field48)
field49 = fieldObject().setName("topAbutmentHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for topAbutmentHeight parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field49)
field50 = fieldObject().setName("pierWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for pierWidth parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field50)
field51 = fieldObject().setName("pierHeight").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for pierHeight parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field51)
field52 = fieldObject().setName("archHalf").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalf parameter").setType(fieldObject.TYPE_SFBOOL)
Script45.addField(field52)
field53 = fieldObject().setName("archHalfExtensionWidth").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalfExtensionWidth parameter").setType(fieldObject.TYPE_SFFLOAT)
Script45.addField(field53)
field54 = fieldObject().setName("onlyIntrados").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for onlyIntrados parameter").setType(fieldObject.TYPE_SFBOOL)
Script45.addField(field54)
field55 = fieldObject().setName("archFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archFilled parameter").setType(fieldObject.TYPE_SFBOOL)
Script45.addField(field55)
field56 = fieldObject().setName("archHalfFilled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for archHalfFilled parameter").setType(fieldObject.TYPE_SFBOOL)
Script45.addField(field56)
field57 = fieldObject().setName("lintel").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setAppinfo("user or default input for lintel parameter").setType(fieldObject.TYPE_SFBOOL)
Script45.addField(field57)
field58 = fieldObject().setName("computedScale").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("computedScale: modify scale field - NOTE it is not used to modify the whole arch, but to modify clearSpanWidth, riseHeight, depth. It does not affect topAbutmentHeight, pierWidth, pierHeight, archHalfExtensionWidth").setType(fieldObject.TYPE_SFVEC3F)
Script45.addField(field58)
field59 = fieldObject().setName("pointOut").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("send computed points to the Coordinate node").setType(fieldObject.TYPE_MFVEC3F)
Script45.addField(field59)
field60 = fieldObject().setName("indexOut").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY).setAppinfo("send computed indices to the IndexedFaceSet node").setType(fieldObject.TYPE_MFINT32)
Script45.addField(field60)
IS61 = ISObject()
connect62 = connectObject().setNodeField("clearSpanWidth").setProtoField("clearSpanWidth")
IS61.addConnect(connect62)
connect63 = connectObject().setNodeField("riseHeight").setProtoField("riseHeight")
IS61.addConnect(connect63)
connect64 = connectObject().setNodeField("depth").setProtoField("depth")
IS61.addConnect(connect64)
connect65 = connectObject().setNodeField("pierWidth").setProtoField("pierWidth")
IS61.addConnect(connect65)
connect66 = connectObject().setNodeField("topAbutmentHeight").setProtoField("topAbutmentHeight")
IS61.addConnect(connect66)
connect67 = connectObject().setNodeField("pierHeight").setProtoField("pierHeight")
IS61.addConnect(connect67)
connect68 = connectObject().setNodeField("archHalf").setProtoField("archHalf")
IS61.addConnect(connect68)
connect69 = connectObject().setNodeField("archHalfExtensionWidth").setProtoField("archHalfExtensionWidth")
IS61.addConnect(connect69)
connect70 = connectObject().setNodeField("onlyIntrados").setProtoField("onlyIntrados")
IS61.addConnect(connect70)
connect71 = connectObject().setNodeField("archFilled").setProtoField("archFilled")
IS61.addConnect(connect71)
connect72 = connectObject().setNodeField("archHalfFilled").setProtoField("archHalfFilled")
IS61.addConnect(connect72)
connect73 = connectObject().setNodeField("lintel").setProtoField("lintel")
IS61.addConnect(connect73)
Script45.setIS(IS61)
ProtoBody35.addChild(Script45)
ROUTE74 = ROUTEObject().setFromField("computedScale").setFromNode("ArchPrototypeScript").setToField("scale").setToNode("ArchTransform")
ProtoBody35.addChild(ROUTE74)
ROUTE75 = ROUTEObject().setFromField("pointOut").setFromNode("ArchPrototypeScript").setToField("point").setToNode("ArchChord")
ProtoBody35.addChild(ROUTE75)
ROUTE76 = ROUTEObject().setFromField("indexOut").setFromNode("ArchPrototypeScript").setToField("set_coordIndex").setToNode("ArchIndex")
ProtoBody35.addChild(ROUTE76)
ProtoDeclare19.setProtoBody(ProtoBody35)
Scene18.addChild(ProtoDeclare19)
ProtoInstance77 = ProtoInstanceObject().setName("ArchPrototype").setDEF("ArchInstance")
fieldValue78 = fieldValueObject().setName("diffuseColor").setValue("0.5 0.3 0.6")
ProtoInstance77.addFieldValue(fieldValue78)
fieldValue79 = fieldValueObject().setName("emissiveColor").setValue("0.5 0.3 0.6")
ProtoInstance77.addFieldValue(fieldValue79)
fieldValue80 = fieldValueObject().setName("clearSpanWidth").setValue("5")
ProtoInstance77.addFieldValue(fieldValue80)
fieldValue81 = fieldValueObject().setName("riseHeight").setValue("2.5")
ProtoInstance77.addFieldValue(fieldValue81)
fieldValue82 = fieldValueObject().setName("depth").setValue("2")
ProtoInstance77.addFieldValue(fieldValue82)
fieldValue83 = fieldValueObject().setName("topAbutmentHeight").setValue("0.6")
ProtoInstance77.addFieldValue(fieldValue83)
fieldValue84 = fieldValueObject().setName("pierWidth").setValue("1")
ProtoInstance77.addFieldValue(fieldValue84)
fieldValue85 = fieldValueObject().setName("pierHeight").setValue("2")
ProtoInstance77.addFieldValue(fieldValue85)
Scene18.addChild(ProtoInstance77)

Scene18.addComments(CommentsBlock("Add any ROUTEs here that connect ProtoInstance to/from prior nodes in Scene (and outside of ProtoDeclare)"))
Inline86 = InlineObject().setDEF("CoordinateAxes").setUrl(["CoordinateAxes.x3d"])
Scene18.addChild(Inline86)
X3D0.setScene(Scene18)

X3D0.toFileX3D("ArchPrototype.new.x3d")
