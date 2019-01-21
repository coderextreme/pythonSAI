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
     .setContent("rubik.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/rubik.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a kind of rubik cube with spheres") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
     .setType(["EXAMINE"]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Rubiks Cube") \
     .setPosition([0,0,12]) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("sphere") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("xtranslation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("xtranslation") \
        ) \
       ) \
       .addChild(ShapeObject() \
        .setGeometry(SphereObject() \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([1,1,1]) \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("three") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("ytranslation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ytranslation") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("sphere") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("0 0 0") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("sphere") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("2 0 0") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("sphere") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("-2 0 0") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("nine") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("ztranslation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ztranslation") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 0 0") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 2 0") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 -2 0") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("twentyseven") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("ttranslation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ttranslation") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 0") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 2") \
        ) \
       ) \
       .addChild(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 -2") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("twentyseven") \
     .addFieldValue(fieldValueObject() \
      .setName("ttranslation") \
      .setValue("0 0 0") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./rubik.newf.x3d")
