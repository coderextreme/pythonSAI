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
     .setContent("rubikOnFire.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/rubikOnFire.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a white rubik cube") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(NavigationInfoObject() \
     .setType(["EXAMINE"]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Rubiks Cube on Fire") \
     .setPosition([0,0,12]) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("anyShape") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("xtranslation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("myShape") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(SphereObject() \
       ) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("xtranslation") \
        ) \
       ) \
       .addChildren(ShapeObject() \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("geometry") \
          .setProtoField("myShape") \
         ) \
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
    .addChildren(ProtoDeclareObject() \
     .setName("three") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("ytranslation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("myShape") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(SphereObject() \
       ) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ytranslation") \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("anyShape") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("0 0 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("anyShape") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("2 0 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("anyShape") \
        .addFieldValue(fieldValueObject() \
         .setName("xtranslation") \
         .setValue("-2 0 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("nine") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("ztranslation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("myShape") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(SphereObject() \
       ) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ztranslation") \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 0 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 2 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("three") \
        .addFieldValue(fieldValueObject() \
         .setName("ytranslation") \
         .setValue("0 -2 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("twentyseven") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("ttranslation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("myShape") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(SphereObject() \
       ) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("ttranslation") \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 0") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 2") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
       .addChildren(ProtoInstanceObject() \
        .setName("nine") \
        .addFieldValue(fieldValueObject() \
         .setName("ztranslation") \
         .setValue("0 0 -2") \
        ) \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("myShape") \
          .setProtoField("myShape") \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("twentyseven") \
     .addFieldValue(fieldValueObject() \
      .setName("ttranslation") \
      .setValue("0 0 0") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("myShape") \
      .addChildren(BoxObject(size = [1,1,1]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./rubikOnFire.newf.x3d")
