import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Interchange") \
   .setVersion("3.0") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("indexedfaceset_pixeltexture_entire.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.nist.gov/vrml.html") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.itl.nist.gov/div897/ctg/vrml/vrml.html") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("http://www.itl.nist.gov/div897/ctg/vrml/members.html") \
    ) \
    .addMeta(metaObject() \
     .setName("disclaimer") \
     .setContent("This file was provided by the National Institute of Standards and Technology, and is part of the X3D Conformance Test Suite, available at http://www.nist.gov/vrml.html The information contained within this file is provided for use in establishing conformance to the ISO VRML97 Specification. Conformance to this test does not imply recommendation or endorsement by the National Institute of Standards and Technology. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.") \
    ) \
    .addMeta(metaObject() \
     .setName("info") \
     .setContent("Correct definition and compliance of this conformance scene is maintained by the X3D Working Group, http://www.web3d.org/working-groups/x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("translator") \
     .setContent("Michael Kass NIST, Don Brutzman NPS") \
    ) \
    .addMeta(metaObject() \
     .setName("translated") \
     .setContent("21 January 2001") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("13 January 2014") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Test browser ability to completely map one PixelTexture onto the surface of an IndexedFaceSet geometry. Four colored squares should map onto each face of the IndexedFaceSet. The PixelTexture consists of red quarter (lower left), green quarter (lower right), white quarter (upper left) and yellow quarter (upper right). PixelTexture should map once onto the surface of the IndexedFaceSet, with the S (horizontal) axis of the texture corresponding to the X axis of the geometry.") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_entire.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ViewpointObject() \
     .setDescription("Front View") \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Rear View") \
     .setOrientation([0,1,0,3.14]) \
     .setPosition([0,0,-10]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Top View") \
     .setOrientation([1,0,0,-1.57]) \
     .setPosition([0,10,0]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Bottom View") \
     .setOrientation([1,0,0,1.57]) \
     .setPosition([0,-10,0]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Right View") \
     .setOrientation([0,1,0,1.57]) \
     .setPosition([10,0,0]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Left View") \
     .setOrientation([0,1,0,-1.57]) \
     .setPosition([-10,0,0]) \
    ) \
    .addChildren(NavigationInfoObject() \
     .setType(["EXAMINE","WALK","FLY","ANY"]) \
    ) \
    .addChildren(ShapeObject() \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
      ) \
      .setTexture(PixelTextureObject(repeatS = False, repeatT = False) \
       .setImage([2,2,4,-16776961,16711935,-1,-65281]) \
      ) \
     ) \
     .setGeometry(IndexedFaceSetObject(coordIndex = [0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1]) \
      .setCoord(CoordinateObject() \
       .setPoint([-2,1.5,1,-2,-1.5,1,2,1.5,1,2,-1.5,1,2,1.5,-1,2,-1.5,-1,-2,1.5,-1,-2,-1.5,-1]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./indexedfaceset_pixeltexture_entire.newf.x3d")
