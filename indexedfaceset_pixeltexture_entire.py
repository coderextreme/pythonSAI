from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Interchange").setVersion("3.0")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("indexedfaceset_pixeltexture_entire.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("reference").setContent("http://www.nist.gov/vrml.html")
head1.addMeta(meta3)
meta4 = metaObject().setName("reference").setContent("http://www.itl.nist.gov/div897/ctg/vrml/vrml.html")
head1.addMeta(meta4)
meta5 = metaObject().setName("creator").setContent("http://www.itl.nist.gov/div897/ctg/vrml/members.html")
head1.addMeta(meta5)
meta6 = metaObject().setName("disclaimer").setContent("This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.")
head1.addMeta(meta6)
meta7 = metaObject().setName("info").setContent("Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d")
head1.addMeta(meta7)
meta8 = metaObject().setName("translator").setContent("Michael Kass NIST, Don Brutzman NPS")
head1.addMeta(meta8)
meta9 = metaObject().setName("translated").setContent("21 January 2001")
head1.addMeta(meta9)
meta10 = metaObject().setName("modified").setContent("13 January 2014")
head1.addMeta(meta10)
meta11 = metaObject().setName("description").setContent("Test browser ability to completely map one PixelTexture onto the surface of an IndexedFaceSet geometry. Four colored squares should map onto each face of the IndexedFaceSet. The PixelTexture consists of red quarter (lower left), green quarter (lower right), white quarter (upper left) and yellow quarter (upper right). PixelTexture should map once onto the surface of the IndexedFaceSet, with the S (horizontal) axis of the texture corresponding to the X axis of the geometry.")
head1.addMeta(meta11)
meta12 = metaObject().setName("identifier").setContent("http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_entire.x3d")
head1.addMeta(meta12)
meta13 = metaObject().setName("generator").setContent("Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html")
head1.addMeta(meta13)
meta14 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta14)
meta15 = metaObject().setName("license").setContent("../../license.html")
head1.addMeta(meta15)
X3D0.setHead(head1)
Scene16 = SceneObject()
Viewpoint17 = ViewpointObject().setDescription("Front View")
Scene16.addChild(Viewpoint17)
Viewpoint18 = ViewpointObject().setDescription("Rear View").setOrientation([0,1,0,3.14]).setPosition([0,0,-10])
Scene16.addChild(Viewpoint18)
Viewpoint19 = ViewpointObject().setDescription("Top View").setOrientation([1,0,0,-1.57]).setPosition([0,10,0])
Scene16.addChild(Viewpoint19)
Viewpoint20 = ViewpointObject().setDescription("Bottom View").setOrientation([1,0,0,1.57]).setPosition([0,-10,0])
Scene16.addChild(Viewpoint20)
Viewpoint21 = ViewpointObject().setDescription("Right View").setOrientation([0,1,0,1.57]).setPosition([10,0,0])
Scene16.addChild(Viewpoint21)
Viewpoint22 = ViewpointObject().setDescription("Left View").setOrientation([0,1,0,-1.57]).setPosition([-10,0,0])
Scene16.addChild(Viewpoint22)
NavigationInfo23 = NavigationInfoObject().setType(["EXAMINE","WALK","FLY","ANY"])
Scene16.addChild(NavigationInfo23)
Shape24 = ShapeObject()
Appearance25 = AppearanceObject()
Material26 = MaterialObject()
Appearance25.setMaterial(Material26)
PixelTexture27 = PixelTextureObject().setImage([2,2,4,4278190335,16711935,4294967295,4294902015]).setRepeatS(False).setRepeatT(False)
Appearance25.setTexture(PixelTexture27)
Shape24.setAppearance(Appearance25)
IndexedFaceSet28 = IndexedFaceSetObject().setCoordIndex([0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1])
Coordinate29 = CoordinateObject().setPoint([-2,1.5,1,-2,-1.5,1,2,1.5,1,2,-1.5,1,2,1.5,-1,2,-1.5,-1,-2,1.5,-1,-2,-1.5,-1])
IndexedFaceSet28.setCoord(Coordinate29)
Shape24.setGeometry(IndexedFaceSet28)
Scene16.addChild(Shape24)
X3D0.setScene(Scene16)

X3D0.toFileX3D("./indexedfaceset_pixeltexture_entire.new.x3d")
