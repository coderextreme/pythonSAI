# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.0")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("MFString.x3d")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("created")
meta3.setContent("21 April 20017")

head1.addMeta(meta3)
X3D0.setHead(head1)
Scene4 = SceneObject()

Group5 = GroupObject()

Shape6 = ShapeObject()

Text7 = TextObject()
Text7.setString(["Locked","","FIRE!..FIRE!"])

Shape6.setGeometry(Text7)
Appearance8 = AppearanceObject()

Material9 = MaterialObject()
Material9.setDiffuseColor([0,0.75,0.18])

Appearance8.setMaterial(Material9)
Shape6.setAppearance(Appearance8)
Group5.addChild(Shape6)
Scene4.addChild(Group5)
X3D0.setScene(Scene4)

X3D0.toFileX3D("./MFString.new.x3d")
