from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.3")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("sphereflowers.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("creator").setContent("John Carlson")
head1.addMeta(meta3)
meta4 = metaObject().setName("description").setContent("5 or more prismatic flowers")
head1.addMeta(meta4)
meta5 = metaObject().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta5)
meta6 = metaObject().setName("identifier").setContent("http://coderextreme.net/X3DJSONLD/sphereflowers.x3d")
head1.addMeta(meta6)
meta7 = metaObject().setName("translated").setContent("17 May 2017")
head1.addMeta(meta7)
meta8 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta8)
meta9 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta9)
meta10 = metaObject().setName("translated").setContent("17 May 2017")
head1.addMeta(meta10)
meta11 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta11)
X3D0.setHead(head1)
Scene12 = SceneObject()
NavigationInfo13 = NavigationInfoObject()
Scene12.addChild(NavigationInfo13)
Background14 = BackgroundObject().setBackUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"]).setBottomUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"]).setFrontUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"]).setLeftUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"]).setRightUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"]).setTopUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])
Scene12.addChild(Background14)
Group15 = GroupObject()
ExternProtoDeclare16 = ExternProtoDeclareObject().setName("FlowerProto").setUrl(["flowerproto.x3d#FlowerProto"])
field17 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("vertex").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
ExternProtoDeclare16.addField(field17)
field18 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("fragment").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
ExternProtoDeclare16.addField(field18)
Group15.addChild(ExternProtoDeclare16)
ProtoDeclare19 = ProtoDeclareObject().setName("flower")
ProtoBody20 = ProtoBodyObject()
Group21 = GroupObject()
ProtoInstance22 = ProtoInstanceObject().setName("FlowerProto")
fieldValue23 = fieldValueObject().setName("vertex").setValue("\"freewrl_flowers_chromatic.vs\"")
ProtoInstance22.addFieldValue(fieldValue23)
fieldValue24 = fieldValueObject().setName("fragment").setValue("\"freewrl.fs\"")
ProtoInstance22.addFieldValue(fieldValue24)
Group21.addChild(ProtoInstance22)
ProtoBody20.addChild(Group21)
ProtoDeclare19.setProtoBody(ProtoBody20)
Group15.addChild(ProtoDeclare19)
ProtoInstance25 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance25)
ProtoInstance26 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance26)
ProtoInstance27 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance27)
ProtoInstance28 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance28)
ProtoInstance29 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance29)
ProtoInstance30 = ProtoInstanceObject().setName("flower")
Group15.addChild(ProtoInstance30)
Scene12.addChild(Group15)
X3D0.setScene(Scene12)

X3D0.toFileX3D("freewrlflowers.new.x3d")
