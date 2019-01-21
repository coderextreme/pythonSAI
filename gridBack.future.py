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
     .setContent("gridBack.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Checkerboard grid background for X3D/VRML materials selection.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("David Roussel") \
    ) \
    .addMeta(metaObject() \
     .setName("translator") \
     .setContent("James Harney, Don Brutzman NPS") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("8 April 2002") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("12 January 2014") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://vrmlstuff.free.fr/materials") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("Universal Media Material Library") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ShapeObject() \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
       .setAmbientIntensity(0.01) \
       .setDiffuseColor([1,1,1]) \
       .setShininess(0.05) \
      ) \
     ) \
     .setGeometry(IndexedFaceSetObject() \
      .setColorIndex([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]) \
      .setColorPerVertex(False) \
      .setCoordIndex([0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1]) \
      .setNormalPerVertex(False) \
      .setCoord(CoordinateObject() \
       .setPoint([-5.25,5.25,0,-3.75,5.25,0,-2.25,5.25,0,-0.75,5.25,0,0.75,5.25,0,2.25,5.25,0,3.75,5.25,0,5.25,5.25,0,-5.25,3.75,0,-3.75,3.75,0,-2.25,3.75,0,-0.75,3.75,0,0.75,3.75,0,2.25,3.75,0,3.75,3.75,0,5.25,3.75,0,-5.25,2.25,0,-3.75,2.25,0,-2.25,2.25,0,-0.75,2.25,0,0.75,2.25,0,2.25,2.25,0,3.75,2.25,0,5.25,2.25,0,-5.25,0.75,0,-3.75,0.75,0,-2.25,0.75,0,-0.75,0.75,0,0.75,0.75,0,2.25,0.75,0,3.75,0.75,0,5.25,0.75,0,-5.25,-0.75,0,-3.75,-0.75,0,-2.25,-0.75,0,-0.75,-0.75,0,0.75,-0.75,0,2.25,-0.75,0,3.75,-0.75,0,5.25,-0.75,0,-5.25,-2.25,0,-3.75,-2.25,0,-2.25,-2.25,0,-0.75,-2.25,0,0.75,-2.25,0,2.25,-2.25,0,3.75,-2.25,0,5.25,-2.25,0,-5.25,-3.75,0,-3.75,-3.75,0,-2.25,-3.75,0,-0.75,-3.75,0,0.75,-3.75,0,2.25,-3.75,0,3.75,-3.75,0,5.25,-3.75,0,-5.25,-5.25,0,-3.75,-5.25,0,-2.25,-5.25,0,-0.75,-5.25,0,0.75,-5.25,0,2.25,-5.25,0,3.75,-5.25,0,5.25,-5.25,0]) \
      ) \
      .setColor(ColorObject() \
       .setColor([0.5,0.5,0.5,0.75,0.75,0.75]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./gridBack.newf.x3d")
