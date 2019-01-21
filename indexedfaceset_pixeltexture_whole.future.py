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
     .setContent("indexedfaceset_pixeltexture_whole.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("warning") \
     .setContent("file did not transform to vrml97") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-front.jpg") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-rear.jpg") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-top.jpg") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-bottom.jpg") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-left.jpg") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("indexedfaceset_pixeltexture_whole-right.jpg") \
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
     .setContent("Test of browser ability to map the entire portion of an PixelTexture onto an IndexedFaceSet geometry. Four equal sized red (bottom left), green (bottom right) yellow (top left) and white (top right) squares in the pixel texture map all the faces of the cube.") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/ConformanceNist/GeometricProperties/TextureCoordinate/indexedfaceset_pixeltexture_whole.x3d") \
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
    .addChild(ViewpointObject() \
     .setDescription("Front View") \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Rear View") \
     .setOrientation([0,1,0,3.14]) \
     .setPosition([0,0,-10]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Top View") \
     .setOrientation([1,0,0,-1.57]) \
     .setPosition([0,10,0]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Bottom View") \
     .setOrientation([1,0,0,1.57]) \
     .setPosition([0,-10,0]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Right View") \
     .setOrientation([0,1,0,1.57]) \
     .setPosition([10,0,0]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Left View") \
     .setOrientation([0,1,0,-1.57]) \
     .setPosition([-10,0,0]) \
    ) \
    .addChild(NavigationInfoObject() \
     .setType(["EXAMINE"]) \
    ) \
    .addChild(ShapeObject() \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
      ) \
      .setTexture(PixelTextureObject() \
       .setImage([2,2,4,-16776961,16711935,-1,-65281]) \
      ) \
     ) \
     .setGeometry(IndexedFaceSetObject() \
      .setColorPerVertex(False) \
      .setCoordIndex([0,1,3,2,-1,4,5,7,6,-1,6,7,1,0,-1,2,3,5,4,-1,6,0,2,4,-1,1,7,5,3,-1]) \
      .setCreaseAngle(0.5) \
      .setTexCoordIndex([0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1,0,1,3,2,-1]) \
      .setColor(ColorObject() \
       .setColor([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0]) \
      ) \
      .setCoord(CoordinateObject() \
       .setPoint([-2,1,1,-2,-1,1,2,1,1,2,-1,1,2,1,-1,2,-1,-1,-2,1,-1,-2,-1,-1]) \
      ) \
      .setTexCoord(TextureCoordinateObject() \
       .setPoint([0,1,0,0,1,1,1,0]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./indexedfaceset_pixeltexture_whole.newf.x3d")
