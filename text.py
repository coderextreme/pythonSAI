from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("creator")
meta2.setContent("John W Carlson")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("created")
meta3.setContent("December 13 2015")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("title")
meta4.setContent("text.x3d")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("identifier")
meta5.setContent("http://coderextreme.net/X3DJSONLD/text.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("test text")

head1.addMeta(meta6)
meta7 = metaObject()
meta7.setName("generator")
meta7.setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta7)
X3D0.setHead(head1)
Scene8 = SceneObject()

Transform9 = TransformObject()

Shape10 = ShapeObject()

Text11 = TextObject()
Text11.setString(["Node\"\"\""])

FontStyle12 = FontStyleObject()
FontStyle12.setJustify(["MIDDLE","MIDDLE"])
FontStyle12.setSize(5)

Text11.setFontStyle(FontStyle12)
Shape10.setGeometry(Text11)
Appearance13 = AppearanceObject()

Material14 = MaterialObject()
Material14.setDiffuseColor([0,0,1])

Appearance13.setMaterial(Material14)
Shape10.setAppearance(Appearance13)
Transform9.addChild(Shape10)
Scene8.addChild(Transform9)
X3D0.setScene(Scene8)

X3D0.toFileX3D("./text.new.x3d")
