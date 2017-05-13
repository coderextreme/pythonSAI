from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Interchange").setVersion("3.0")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("rgb_alpha.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("Image").setContent("rgb_alpha-front.jpg")
head1.addMeta(meta3)
meta4 = metaObject().setName("Image").setContent("rgb_alpha-rear.jpg")
head1.addMeta(meta4)
meta5 = metaObject().setName("Image").setContent("rgb_alpha-top.jpg")
head1.addMeta(meta5)
meta6 = metaObject().setName("Image").setContent("rgb_alpha-bottom.jpg")
head1.addMeta(meta6)
meta7 = metaObject().setName("reference").setContent("http://www.nist.gov/vrml.html")
head1.addMeta(meta7)
meta8 = metaObject().setName("reference").setContent("http://www.itl.nist.gov/div897/ctg/vrml/vrml.html")
head1.addMeta(meta8)
meta9 = metaObject().setName("creator").setContent("http://www.itl.nist.gov/div897/ctg/vrml/members.html")
head1.addMeta(meta9)
meta10 = metaObject().setName("disclaimer").setContent("This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.")
head1.addMeta(meta10)
meta11 = metaObject().setName("info").setContent("Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d")
head1.addMeta(meta11)
meta12 = metaObject().setName("translator").setContent("Michael Kass NIST, Don Brutzman NPS")
head1.addMeta(meta12)
meta13 = metaObject().setName("translated").setContent("21 January 2001")
head1.addMeta(meta13)
meta14 = metaObject().setName("modified").setContent("16 January 2011")
head1.addMeta(meta14)
meta15 = metaObject().setName("description").setContent("Test browser ability to map a RGB plus alpha opacity to geometry. A checkerboard of four colored squares: lower left (red), lower right (transparent), uppser left (transparent) and upper right (red) map onto the faces of all geometry. For the sphere, the texture should cover the entire surface, and wrap counterclockwise from the back of the sphere. For the cone, the texture should wrap counterclockwise (from above) starting at the back of the cone. A circle cutout of the texture is applied right side up to the base of the cone when the cone is tilted toward the -z axis. For the cylinder, the texture should wrap counterclockwise (from above) starting at the back of the cylinder. A circle cutout of the texture is applied right side up to the top and bottom caps of the cylinder. For the box, the texture should be applied right side up in its entirety to each face of the box.")
head1.addMeta(meta15)
meta16 = metaObject().setName("identifier").setContent("http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/PixelTexture/rgb_alpha.x3d")
head1.addMeta(meta16)
meta17 = metaObject().setName("generator").setContent("Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html")
head1.addMeta(meta17)
meta18 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta18)
meta19 = metaObject().setName("license").setContent("../../license.html")
head1.addMeta(meta19)
meta20 = metaObject().setName("translated").setContent("13 May 2017")
head1.addMeta(meta20)
meta21 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta21)
meta22 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta22)
meta23 = metaObject().setName("translated").setContent("13 May 2017")
head1.addMeta(meta23)
meta24 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta24)
X3D0.setHead(head1)
Scene25 = SceneObject()
NavigationInfo26 = NavigationInfoObject().setType(["EXAMINE","WALK","FLY","ANY"])
Scene25.addChild(NavigationInfo26)
Group27 = GroupObject()
Transform28 = TransformObject().setTranslation([6.14221,0.0694613,-0.000999451])
Shape29 = ShapeObject()
Appearance30 = AppearanceObject()
Material31 = MaterialObject()
Appearance30.setMaterial(Material31)
PixelTexture32 = PixelTextureObject().setDEF("RgbOpacityCheckerboard").setImage([2,2,4,4278190335,4294901760,4294901760,4278190335])
Appearance30.setTexture(PixelTexture32)
Shape29.setAppearance(Appearance30)
Box33 = BoxObject()
Shape29.setGeometry(Box33)
Transform28.addChild(Shape29)
Group27.addChild(Transform28)
Transform34 = TransformObject().setTranslation([-4.85443,0.0694381,-0.00149918])
Shape35 = ShapeObject()
Appearance36 = AppearanceObject()
Material37 = MaterialObject()
Appearance36.setMaterial(Material37)
PixelTexture38 = PixelTextureObject().setUSE("RgbOpacityCheckerboard")
Appearance36.setTexture(PixelTexture38)
Shape35.setAppearance(Appearance36)
Sphere39 = SphereObject()
Shape35.setGeometry(Sphere39)
Transform34.addChild(Shape35)
Group27.addChild(Transform34)
Transform40 = TransformObject().setTranslation([-1.47341,0.036672,-0.00175095])
Shape41 = ShapeObject()
Appearance42 = AppearanceObject()
Material43 = MaterialObject()
Appearance42.setMaterial(Material43)
PixelTexture44 = PixelTextureObject().setUSE("RgbOpacityCheckerboard")
Appearance42.setTexture(PixelTexture44)
Shape41.setAppearance(Appearance42)
Cone45 = ConeObject()
Shape41.setGeometry(Cone45)
Transform40.addChild(Shape41)
Group27.addChild(Transform40)
Transform46 = TransformObject().setTranslation([2.31094,0.0694206,-0.00187683])
Shape47 = ShapeObject()
Appearance48 = AppearanceObject()
Material49 = MaterialObject()
Appearance48.setMaterial(Material49)
PixelTexture50 = PixelTextureObject().setUSE("RgbOpacityCheckerboard")
Appearance48.setTexture(PixelTexture50)
Shape47.setAppearance(Appearance48)
Cylinder51 = CylinderObject()
Shape47.setGeometry(Cylinder51)
Transform46.addChild(Shape47)
Group27.addChild(Transform46)
Scene25.addChild(Group27)
X3D0.setScene(Scene25)

X3D0.toFileX3D("rgb_alpha.new.x3d")
