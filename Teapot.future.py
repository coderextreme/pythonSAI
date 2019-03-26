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
     .setContent("MooringBuoy.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("A mooring buoy used in Naval Harbors") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("LT Patrick Sullivan") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("28 July 2006") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("12 January 2014") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://savage.nps.edu/Savage/HarborEquipment/Buoys/MooringBuoy.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("VizX3D, http://www.vivaty.com/downloads/studio") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Wings3D, http://www.wings3d.com") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(TransformObject() \
     .setScale([0.3,0.3,0.3]) \
     .addChildren(GroupObject() \
      .setDEF("MooringBuoyWithHook") \
      .addChildren(TransformObject() \
       .setDEF("Hook") \
       .addChildren(ShapeObject() \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDEF("Black_mat") \
          .setDiffuseColor([0,0,0]) \
         ) \
        ) \
        .setGeometry(IndexedFaceSetObject(coordIndex = [0,1,2,-1,0,2,3,-1,0,4,5,-1,0,5,6,-1,0,3,7,-1,0,7,4,-1,0,6,8,-1,0,8,1,-1,1,9,10,-1,1,10,2,-1,1,8,11,-1,1,11,9,-1,9,12,13,-1,9,13,10,-1,9,11,14,-1,9,14,12,-1,12,15,16,-1,12,16,13,-1,12,14,17,-1,12,17,15,-1,15,18,19,-1,15,19,16,-1,15,17,20,-1,15,20,18,-1,18,21,22,-1,18,22,19,-1,18,20,23,-1,18,23,21,-1,21,24,25,-1,21,25,22,-1,21,23,26,-1,21,26,24,-1,24,27,28,-1,24,28,25,-1,24,26,29,-1,24,29,27,-1,27,30,31,-1,27,31,28,-1,27,29,32,-1,27,32,30,-1,30,33,34,-1,30,34,31,-1,30,32,35,-1,30,35,33,-1,33,36,37,-1,33,37,34,-1,33,35,38,-1,33,38,36,-1,36,39,40,-1,36,40,37,-1,36,38,41,-1,36,41,39,-1,39,42,43,-1,39,43,40,-1,39,41,44,-1,39,44,42,-1,42,45,46,-1,42,46,43,-1,42,44,47,-1,42,47,45,-1,45,4,7,-1,45,7,46,-1,45,47,5,-1,45,5,4,-1,3,2,10,-1,3,10,13,-1,3,13,16,-1,3,16,19,-1,3,19,22,-1,3,22,25,-1,3,25,28,-1,3,28,31,-1,3,31,34,-1,3,34,37,-1,3,37,40,-1,3,40,43,-1,3,43,46,-1,3,46,7,-1,8,6,48,-1,8,48,49,-1,8,49,50,-1,8,50,11,-1,6,5,51,-1,6,51,48,-1,5,47,52,-1,5,52,51,-1,47,44,53,-1,47,53,52,-1,44,41,54,-1,44,54,53,-1,41,38,55,-1,41,55,54,-1,38,35,56,-1,38,56,55,-1,35,32,57,-1,35,57,56,-1,32,29,58,-1,32,58,57,-1,29,26,59,-1,29,59,58,-1,26,23,60,-1,26,60,59,-1,23,20,61,-1,23,61,60,-1,20,17,62,-1,20,62,61,-1,17,14,63,-1,17,63,62,-1,14,11,50,-1,14,50,63,-1,49,48,64,-1,49,64,65,-1,49,65,66,-1,49,66,50,-1,48,51,67,-1,48,67,64,-1,51,52,68,-1,51,68,67,-1,52,53,69,-1,52,69,68,-1,53,54,70,-1,53,70,69,-1,54,55,71,-1,54,71,70,-1,55,56,72,-1,55,72,71,-1,56,57,73,-1,56,73,72,-1,57,58,74,-1,57,74,73,-1,58,59,75,-1,58,75,74,-1,59,60,76,-1,59,76,75,-1,60,61,77,-1,60,77,76,-1,61,62,78,-1,61,78,77,-1,62,63,79,-1,62,79,78,-1,63,50,66,-1,63,66,79,-1,65,64,80,-1,65,80,81,-1,65,81,82,-1,65,82,66,-1,64,67,83,-1,64,83,80,-1,67,68,84,-1,67,84,83,-1,68,69,85,-1,68,85,84,-1,69,70,86,-1,69,86,85,-1,70,71,87,-1,70,87,86,-1,71,72,88,-1,71,88,87,-1,72,73,89,-1,72,89,88,-1,73,74,90,-1,73,90,89,-1,74,75,91,-1,74,91,90,-1,75,76,92,-1,75,92,91,-1,76,77,93,-1,76,93,92,-1,77,78,94,-1,77,94,93,-1,78,79,95,-1,78,95,94,-1,79,66,82,-1,79,82,95,-1,81,80,83,-1,81,83,84,-1,81,84,85,-1,81,85,86,-1,81,86,87,-1,81,87,88,-1,81,88,89,-1,81,89,90,-1,81,90,91,-1,81,91,92,-1,81,92,93,-1,81,93,94,-1,81,94,95,-1,81,95,82,-1,96,97,98,-1,96,98,99,-1,96,100,101,-1,96,101,102,-1,96,102,103,-1,96,103,97,-1,96,99,104,-1,96,104,100,-1,97,105,106,-1,97,106,98,-1,97,103,107,-1,97,107,105,-1,105,108,109,-1,105,109,106,-1,105,107,110,-1,105,110,108,-1,108,111,112,-1,108,112,109,-1,108,110,113,-1,108,113,111,-1,111,114,115,-1,111,115,112,-1,111,113,116,-1,111,116,114,-1,114,117,118,-1,114,118,115,-1,114,116,119,-1,114,119,117,-1,117,120,121,-1,117,121,118,-1,117,119,122,-1,117,122,120,-1,120,123,124,-1,120,124,121,-1,120,122,125,-1,120,125,123,-1,123,126,127,-1,123,127,124,-1,123,125,128,-1,123,128,126,-1,126,129,130,-1,126,130,127,-1,126,128,131,-1,126,131,129,-1,129,132,133,-1,129,133,130,-1,129,131,134,-1,129,134,132,-1,132,135,136,-1,132,136,133,-1,132,134,137,-1,132,137,135,-1,135,138,139,-1,135,139,136,-1,135,137,140,-1,135,140,138,-1,138,141,142,-1,138,142,139,-1,138,140,143,-1,138,143,141,-1,141,100,104,-1,141,104,142,-1,141,143,101,-1,141,101,100,-1,102,101,143,-1,102,143,140,-1,102,140,137,-1,102,137,134,-1,102,134,131,-1,102,131,128,-1,102,128,125,-1,102,125,122,-1,102,122,119,-1,102,119,116,-1,102,116,113,-1,102,113,110,-1,102,110,107,-1,102,107,103,-1,98,106,144,-1,98,144,145,-1,98,145,146,-1,98,146,99,-1,99,146,147,-1,99,147,104,-1,104,147,148,-1,104,148,142,-1,142,148,149,-1,142,149,139,-1,139,149,150,-1,139,150,136,-1,136,150,151,-1,136,151,133,-1,133,151,152,-1,133,152,130,-1,130,152,153,-1,130,153,127,-1,127,153,154,-1,127,154,124,-1,124,154,155,-1,124,155,121,-1,121,155,156,-1,121,156,118,-1,118,156,157,-1,118,157,115,-1,115,157,158,-1,115,158,112,-1,112,158,159,-1,112,159,109,-1,109,159,144,-1,109,144,106,-1,145,144,160,-1,145,160,161,-1,145,161,162,-1,145,162,146,-1,146,162,163,-1,146,163,147,-1,147,163,164,-1,147,164,148,-1,148,164,165,-1,148,165,149,-1,149,165,166,-1,149,166,150,-1,150,166,167,-1,150,167,151,-1,151,167,168,-1,151,168,152,-1,152,168,169,-1,152,169,153,-1,153,169,170,-1,153,170,154,-1,154,170,171,-1,154,171,155,-1,155,171,172,-1,155,172,156,-1,156,172,173,-1,156,173,157,-1,157,173,174,-1,157,174,158,-1,158,174,175,-1,158,175,159,-1,159,175,160,-1,159,160,144,-1,161,160,176,-1,161,176,177,-1,161,177,178,-1,161,178,162,-1,162,178,179,-1,162,179,163,-1,163,179,180,-1,163,180,164,-1,164,180,181,-1,164,181,165,-1,165,181,182,-1,165,182,166,-1,166,182,183,-1,166,183,167,-1,167,183,184,-1,167,184,168,-1,168,184,185,-1,168,185,169,-1,169,185,186,-1,169,186,170,-1,170,186,187,-1,170,187,171,-1,171,187,188,-1,171,188,172,-1,172,188,189,-1,172,189,173,-1,173,189,190,-1,173,190,174,-1,174,190,191,-1,174,191,175,-1,175,191,176,-1,175,176,160,-1,177,176,191,-1,177,191,190,-1,177,190,189,-1,177,189,188,-1,177,188,187,-1,177,187,186,-1,177,186,185,-1,177,185,184,-1,177,184,183,-1,177,183,182,-1,177,182,181,-1,177,181,180,-1,177,180,179,-1,177,179,178,-1], creaseAngle = 0.524) \
         .setCoord(CoordinateObject() \
          .setPoint([-0.07,0.57,0,-0.08,0.57,0.01,-0.08,0.5,0.01,-0.07,0.5,0,-0.08,0.57,-0.01,-0.08,0.6,-0.01,-0.08,0.6,0,-0.08,0.5,-0.01,-0.08,0.6,0.01,-0.08,0.57,0.02,-0.08,0.5,0.02,-0.09,0.6,0.02,-0.09,0.57,0.02,-0.09,0.5,0.02,-0.09,0.6,0.02,-0.1,0.57,0.03,-0.1,0.5,0.03,-0.1,0.61,0.03,-0.11,0.57,0.02,-0.11,0.5,0.02,-0.11,0.61,0.02,-0.12,0.57,0.02,-0.12,0.5,0.02,-0.12,0.62,0.02,-0.12,0.57,0.01,-0.12,0.5,0.01,-0.12,0.62,0.01,-0.13,0.57,0,-0.13,0.5,0,-0.12,0.62,0,-0.12,0.57,-0.01,-0.12,0.5,-0.01,-0.12,0.62,-0.01,-0.12,0.57,-0.02,-0.12,0.5,-0.02,-0.12,0.62,-0.02,-0.11,0.57,-0.02,-0.11,0.5,-0.02,-0.11,0.61,-0.02,-0.1,0.57,-0.03,-0.1,0.5,-0.03,-0.1,0.61,-0.03,-0.09,0.57,-0.02,-0.09,0.5,-0.02,-0.09,0.6,-0.02,-0.08,0.57,-0.02,-0.08,0.5,-0.02,-0.09,0.6,-0.02,-0.06,0.63,0,-0.06,0.63,0.01,-0.07,0.63,0.02,-0.06,0.63,-0.01,-0.07,0.63,-0.02,-0.07,0.64,-0.02,-0.08,0.64,-0.03,-0.09,0.65,-0.02,-0.09,0.66,-0.02,-0.1,0.66,-0.01,-0.1,0.66,0,-0.1,0.66,0.01,-0.09,0.66,0.02,-0.09,0.65,0.02,-0.08,0.64,0.03,-0.07,0.64,0.02,-0.03,0.65,0,-0.03,0.65,0.01,-0.04,0.66,0.02,-0.03,0.65,-0.01,-0.04,0.66,-0.02,-0.04,0.67,-0.02,-0.04,0.68,-0.03,-0.04,0.69,-0.02,-0.04,0.69,-0.02,-0.04,0.7,-0.01,-0.04,0.7,0,-0.04,0.7,0.01,-0.04,0.69,0.02,-0.04,0.69,0.02,-0.04,0.68,0.03,-0.04,0.67,0.02,0,0.65,0,0,0.66,0.01,0,0.66,0.02,0,0.66,-0.01,0,0.66,-0.02,0,0.67,-0.02,0,0.68,-0.03,0,0.69,-0.02,0,0.7,-0.02,0,0.7,-0.01,0,0.71,0,0,0.7,0.01,0,0.7,0.02,0,0.69,0.02,0,0.68,0.03,0,0.67,0.02,0.07,0.57,0,0.07,0.57,0.01,0.07,0.59,0.01,0.07,0.59,0,0.07,0.57,-0.01,0.07,0.5,-0.01,0.07,0.5,0,0.07,0.5,0.01,0.07,0.59,-0.01,0.08,0.57,0.02,0.08,0.6,0.02,0.07,0.5,0.02,0.08,0.57,0.02,0.09,0.6,0.02,0.08,0.5,0.02,0.09,0.57,0.03,0.09,0.61,0.03,0.09,0.5,0.03,0.1,0.57,0.02,0.1,0.61,0.02,0.1,0.5,0.02,0.11,0.57,0.02,0.11,0.62,0.02,0.11,0.5,0.02,0.12,0.57,0.01,0.12,0.62,0.01,0.12,0.5,0.01,0.12,0.57,0,0.12,0.62,0,0.12,0.5,0,0.12,0.57,-0.01,0.12,0.62,-0.01,0.12,0.5,-0.01,0.11,0.57,-0.02,0.11,0.62,-0.02,0.11,0.5,-0.02,0.1,0.57,-0.02,0.1,0.61,-0.02,0.1,0.5,-0.02,0.09,0.57,-0.03,0.09,0.61,-0.03,0.09,0.5,-0.03,0.08,0.57,-0.02,0.09,0.6,-0.02,0.08,0.5,-0.02,0.08,0.57,-0.02,0.08,0.6,-0.02,0.07,0.5,-0.02,0.06,0.63,0.02,0.06,0.63,0.01,0.05,0.63,0,0.06,0.63,-0.01,0.06,0.63,-0.02,0.07,0.64,-0.02,0.07,0.64,-0.03,0.08,0.65,-0.02,0.09,0.65,-0.02,0.09,0.66,-0.01,0.09,0.66,0,0.09,0.66,0.01,0.09,0.65,0.02,0.08,0.65,0.02,0.07,0.64,0.03,0.07,0.64,0.02,0.03,0.66,0.02,0.03,0.65,0.01,0.03,0.65,0,0.03,0.65,-0.01,0.03,0.66,-0.02,0.03,0.67,-0.02,0.03,0.68,-0.03,0.03,0.69,-0.02,0.03,0.69,-0.02,0.04,0.7,-0.01,0.04,0.7,0,0.04,0.7,0.01,0.03,0.69,0.02,0.03,0.69,0.02,0.03,0.68,0.03,0.03,0.67,0.02,0,0.66,0.02,0,0.66,0.01,0,0.65,0,0,0.66,-0.01,0,0.66,-0.02,0,0.67,-0.02,0,0.68,-0.03,0,0.69,-0.02,0,0.7,-0.02,0,0.7,-0.01,0,0.71,0,0,0.7,0.01,0,0.7,0.02,0,0.69,0.02,0,0.68,0.03,0,0.67,0.02]) \
         ) \
        ) \
       ) \
      ) \
      .addChildren(TransformObject() \
       .setDEF("MooringBuoy") \
       .addChildren(ShapeObject() \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDEF("default_mat") \
          .setAmbientIntensity(1) \
          .setDiffuseColor([0.50196,0.50196,0.50196]) \
          .setShininess(1) \
         ) \
         .setTexture(ImageTextureObject() \
          .setUrl(["examples/Savage/HarborEquipment/Buoys/textures/MooringBuoy.jpg"]) \
         ) \
        ) \
        .setGeometry(IndexedFaceSetObject(coordIndex = [0,1,2,-1,0,2,3,-1,0,4,5,-1,0,5,6,-1,0,3,7,-1,0,7,4,-1,0,6,8,-1,0,8,1,-1,1,9,10,-1,1,10,2,-1,1,8,11,-1,1,11,9,-1,9,12,13,-1,9,13,10,-1,9,11,14,-1,9,14,12,-1,12,15,16,-1,12,16,13,-1,12,14,17,-1,12,17,15,-1,15,18,19,-1,15,19,16,-1,15,17,20,-1,15,20,18,-1,18,21,22,-1,18,22,19,-1,18,20,23,-1,18,23,21,-1,21,24,25,-1,21,25,22,-1,21,23,26,-1,21,26,24,-1,24,27,28,-1,24,28,25,-1,24,26,29,-1,24,29,27,-1,27,30,31,-1,27,31,28,-1,27,29,32,-1,27,32,30,-1,30,33,34,-1,30,34,31,-1,30,32,35,-1,30,35,33,-1,33,36,37,-1,33,37,34,-1,33,35,38,-1,33,38,36,-1,36,39,40,-1,36,40,37,-1,36,38,41,-1,36,41,39,-1,39,42,43,-1,39,43,40,-1,39,41,44,-1,39,44,42,-1,42,45,46,-1,42,46,43,-1,42,44,47,-1,42,47,45,-1,45,48,49,-1,45,49,46,-1,45,47,50,-1,45,50,48,-1,48,51,52,-1,48,52,49,-1,48,50,53,-1,48,53,51,-1,51,54,55,-1,51,55,52,-1,51,53,56,-1,51,56,54,-1,54,57,58,-1,54,58,55,-1,54,56,59,-1,54,59,57,-1,57,60,61,-1,57,61,58,-1,57,59,62,-1,57,62,60,-1,60,63,64,-1,60,64,61,-1,60,62,65,-1,60,65,63,-1,63,66,67,-1,63,67,64,-1,63,65,68,-1,63,68,66,-1,66,69,70,-1,66,70,67,-1,66,68,71,-1,66,71,69,-1,69,72,73,-1,69,73,70,-1,69,71,74,-1,69,74,72,-1,72,75,76,-1,72,76,73,-1,72,74,77,-1,72,77,75,-1,75,78,79,-1,75,79,76,-1,75,77,80,-1,75,80,78,-1,78,81,82,-1,78,82,79,-1,78,80,83,-1,78,83,81,-1,81,84,85,-1,81,85,82,-1,81,83,86,-1,81,86,84,-1,84,87,88,-1,84,88,85,-1,84,86,89,-1,84,89,87,-1,87,90,91,-1,87,91,88,-1,87,89,92,-1,87,92,90,-1,90,93,94,-1,90,94,91,-1,90,92,95,-1,90,95,93,-1,93,4,7,-1,93,7,94,-1,93,95,5,-1,93,5,4,-1,3,2,96,-1,3,96,97,-1,3,97,98,-1,3,98,7,-1,2,10,99,-1,2,99,96,-1,10,13,100,-1,10,100,99,-1,13,16,101,-1,13,101,100,-1,16,19,102,-1,16,102,101,-1,19,22,103,-1,19,103,102,-1,22,25,104,-1,22,104,103,-1,25,28,105,-1,25,105,104,-1,28,31,106,-1,28,106,105,-1,31,34,107,-1,31,107,106,-1,34,37,108,-1,34,108,107,-1,37,40,109,-1,37,109,108,-1,40,43,110,-1,40,110,109,-1,43,46,111,-1,43,111,110,-1,46,49,112,-1,46,112,111,-1,49,52,113,-1,49,113,112,-1,52,55,114,-1,52,114,113,-1,55,58,115,-1,55,115,114,-1,58,61,116,-1,58,116,115,-1,61,64,117,-1,61,117,116,-1,64,67,118,-1,64,118,117,-1,67,70,119,-1,67,119,118,-1,70,73,120,-1,70,120,119,-1,73,76,121,-1,73,121,120,-1,76,79,122,-1,76,122,121,-1,79,82,123,-1,79,123,122,-1,82,85,124,-1,82,124,123,-1,85,88,125,-1,85,125,124,-1,88,91,126,-1,88,126,125,-1,91,94,127,-1,91,127,126,-1,94,7,98,-1,94,98,127,-1,8,6,128,-1,8,128,129,-1,8,129,130,-1,8,130,11,-1,6,5,131,-1,6,131,128,-1,5,95,132,-1,5,132,131,-1,95,92,133,-1,95,133,132,-1,92,89,134,-1,92,134,133,-1,89,86,135,-1,89,135,134,-1,86,83,136,-1,86,136,135,-1,83,80,137,-1,83,137,136,-1,80,77,138,-1,80,138,137,-1,77,74,139,-1,77,139,138,-1,74,71,140,-1,74,140,139,-1,71,68,141,-1,71,141,140,-1,68,65,142,-1,68,142,141,-1,65,62,143,-1,65,143,142,-1,62,59,144,-1,62,144,143,-1,59,56,145,-1,59,145,144,-1,56,53,146,-1,56,146,145,-1,53,50,147,-1,53,147,146,-1,50,47,148,-1,50,148,147,-1,47,44,149,-1,47,149,148,-1,44,41,150,-1,44,150,149,-1,41,38,151,-1,41,151,150,-1,38,35,152,-1,38,152,151,-1,35,32,153,-1,35,153,152,-1,32,29,154,-1,32,154,153,-1,29,26,155,-1,29,155,154,-1,26,23,156,-1,26,156,155,-1,23,20,157,-1,23,157,156,-1,20,17,158,-1,20,158,157,-1,17,14,159,-1,17,159,158,-1,14,11,130,-1,14,130,159,-1,129,128,160,-1,129,160,161,-1,129,161,162,-1,129,162,130,-1,128,131,163,-1,128,163,160,-1,131,132,164,-1,131,164,163,-1,132,133,165,-1,132,165,164,-1,133,134,166,-1,133,166,165,-1,134,135,167,-1,134,167,166,-1,135,136,168,-1,135,168,167,-1,136,137,169,-1,136,169,168,-1,137,138,170,-1,137,170,169,-1,138,139,171,-1,138,171,170,-1,139,140,172,-1,139,172,171,-1,140,141,173,-1,140,173,172,-1,141,142,174,-1,141,174,173,-1,142,143,175,-1,142,175,174,-1,143,144,176,-1,143,176,175,-1,144,145,177,-1,144,177,176,-1,145,146,178,-1,145,178,177,-1,146,147,179,-1,146,179,178,-1,147,148,180,-1,147,180,179,-1,148,149,181,-1,148,181,180,-1,149,150,182,-1,149,182,181,-1,150,151,183,-1,150,183,182,-1,151,152,184,-1,151,184,183,-1,152,153,185,-1,152,185,184,-1,153,154,186,-1,153,186,185,-1,154,155,187,-1,154,187,186,-1,155,156,188,-1,155,188,187,-1,156,157,189,-1,156,189,188,-1,157,158,190,-1,157,190,189,-1,158,159,191,-1,158,191,190,-1,159,130,162,-1,159,162,191,-1,161,160,192,-1,161,192,193,-1,161,193,194,-1,161,194,162,-1,160,163,195,-1,160,195,192,-1,163,164,196,-1,163,196,195,-1,164,165,197,-1,164,197,196,-1,165,166,198,-1,165,198,197,-1,166,167,199,-1,166,199,198,-1,167,168,200,-1,167,200,199,-1,168,169,201,-1,168,201,200,-1,169,170,202,-1,169,202,201,-1,170,171,203,-1,170,203,202,-1,171,172,204,-1,171,204,203,-1,172,173,205,-1,172,205,204,-1,173,174,206,-1,173,206,205,-1,174,175,207,-1,174,207,206,-1,175,176,208,-1,175,208,207,-1,176,177,209,-1,176,209,208,-1,177,178,210,-1,177,210,209,-1,178,179,211,-1,178,211,210,-1,179,180,212,-1,179,212,211,-1,180,181,213,-1,180,213,212,-1,181,182,214,-1,181,214,213,-1,182,183,215,-1,182,215,214,-1,183,184,216,-1,183,216,215,-1,184,185,217,-1,184,217,216,-1,185,186,218,-1,185,218,217,-1,186,187,219,-1,186,219,218,-1,187,188,220,-1,187,220,219,-1,188,189,221,-1,188,221,220,-1,189,190,222,-1,189,222,221,-1,190,191,223,-1,190,223,222,-1,191,162,194,-1,191,194,223,-1,97,96,99,-1,97,99,100,-1,97,100,101,-1,97,101,102,-1,97,102,103,-1,97,103,104,-1,97,104,105,-1,97,105,106,-1,97,106,107,-1,97,107,108,-1,97,108,109,-1,97,109,110,-1,97,110,111,-1,97,111,112,-1,97,112,113,-1,97,113,114,-1,97,114,115,-1,97,115,116,-1,97,116,117,-1,97,117,118,-1,97,118,119,-1,97,119,120,-1,97,120,121,-1,97,121,122,-1,97,122,123,-1,97,123,124,-1,97,124,125,-1,97,125,126,-1,97,126,127,-1,97,127,98,-1,193,192,224,-1,193,224,225,-1,193,225,226,-1,193,226,194,-1,192,195,227,-1,192,227,224,-1,195,196,228,-1,195,228,227,-1,196,197,229,-1,196,229,228,-1,197,198,230,-1,197,230,229,-1,198,199,231,-1,198,231,230,-1,199,200,232,-1,199,232,231,-1,200,201,233,-1,200,233,232,-1,201,202,234,-1,201,234,233,-1,202,203,235,-1,202,235,234,-1,203,204,236,-1,203,236,235,-1,204,205,237,-1,204,237,236,-1,205,206,238,-1,205,238,237,-1,206,207,239,-1,206,239,238,-1,207,208,240,-1,207,240,239,-1,208,209,241,-1,208,241,240,-1,209,210,242,-1,209,242,241,-1,210,211,243,-1,210,243,242,-1,211,212,244,-1,211,244,243,-1,212,213,245,-1,212,245,244,-1,213,214,246,-1,213,246,245,-1,214,215,247,-1,214,247,246,-1,215,216,248,-1,215,248,247,-1,216,217,249,-1,216,249,248,-1,217,218,250,-1,217,250,249,-1,218,219,251,-1,218,251,250,-1,219,220,252,-1,219,252,251,-1,220,221,253,-1,220,253,252,-1,221,222,254,-1,221,254,253,-1,222,223,255,-1,222,255,254,-1,223,194,226,-1,223,226,255,-1,225,224,256,-1,225,256,257,-1,225,257,258,-1,225,258,226,-1,224,227,259,-1,224,259,256,-1,227,228,260,-1,227,260,259,-1,228,229,261,-1,228,261,260,-1,229,230,262,-1,229,262,261,-1,230,231,263,-1,230,263,262,-1,231,232,264,-1,231,264,263,-1,232,233,265,-1,232,265,264,-1,233,234,266,-1,233,266,265,-1,234,235,267,-1,234,267,266,-1,235,236,268,-1,235,268,267,-1,236,237,269,-1,236,269,268,-1,237,238,270,-1,237,270,269,-1,238,239,271,-1,238,271,270,-1,239,240,272,-1,239,272,271,-1,240,241,273,-1,240,273,272,-1,241,242,274,-1,241,274,273,-1,242,243,275,-1,242,275,274,-1,243,244,276,-1,243,276,275,-1,244,245,277,-1,244,277,276,-1,245,246,278,-1,245,278,277,-1,246,247,279,-1,246,279,278,-1,247,248,280,-1,247,280,279,-1,248,249,281,-1,248,281,280,-1,249,250,282,-1,249,282,281,-1,250,251,283,-1,250,283,282,-1,251,252,284,-1,251,284,283,-1,252,253,285,-1,252,285,284,-1,253,254,286,-1,253,286,285,-1,254,255,287,-1,254,287,286,-1,255,226,258,-1,255,258,287,-1,257,256,259,-1,257,259,260,-1,257,260,261,-1,257,261,262,-1,257,262,263,-1,257,263,264,-1,257,264,265,-1,257,265,266,-1,257,266,267,-1,257,267,268,-1,257,268,269,-1,257,269,270,-1,257,270,271,-1,257,271,272,-1,257,272,273,-1,257,273,274,-1,257,274,275,-1,257,275,276,-1,257,276,277,-1,257,277,278,-1,257,278,279,-1,257,279,280,-1,257,280,281,-1,257,281,282,-1,257,282,283,-1,257,283,284,-1,257,284,285,-1,257,285,286,-1,257,286,287,-1,257,287,258,-1], creaseAngle = 1.047, texCoordIndex = [0,1,2,-1,0,2,3,-1,0,4,5,-1,0,5,6,-1,0,3,7,-1,0,7,4,-1,0,6,8,-1,0,8,1,-1,1,9,10,-1,1,10,2,-1,1,8,11,-1,1,11,9,-1,9,12,13,-1,9,13,10,-1,9,11,14,-1,9,14,12,-1,12,15,16,-1,12,16,13,-1,12,14,17,-1,12,17,15,-1,15,18,19,-1,15,19,16,-1,15,17,20,-1,15,20,18,-1,18,21,22,-1,18,22,19,-1,18,20,23,-1,18,23,21,-1,21,24,25,-1,21,25,22,-1,21,23,26,-1,21,26,24,-1,24,27,28,-1,24,28,25,-1,24,26,29,-1,24,29,27,-1,27,30,31,-1,27,31,28,-1,27,29,32,-1,27,32,30,-1,30,33,34,-1,30,34,31,-1,30,32,35,-1,30,35,33,-1,33,36,37,-1,33,37,34,-1,33,35,38,-1,33,38,36,-1,36,39,40,-1,36,40,37,-1,36,38,41,-1,36,41,39,-1,39,42,43,-1,39,43,40,-1,39,41,44,-1,39,44,42,-1,42,45,46,-1,42,46,43,-1,42,44,47,-1,42,47,45,-1,45,48,49,-1,45,49,46,-1,45,47,50,-1,45,50,48,-1,48,51,52,-1,48,52,49,-1,48,50,53,-1,48,53,51,-1,51,54,55,-1,51,55,52,-1,51,53,56,-1,51,56,54,-1,54,57,58,-1,54,58,55,-1,54,56,59,-1,54,59,57,-1,57,60,61,-1,57,61,58,-1,57,59,62,-1,57,62,60,-1,60,63,64,-1,60,64,61,-1,60,62,65,-1,60,65,63,-1,63,66,67,-1,63,67,64,-1,63,65,68,-1,63,68,66,-1,66,69,70,-1,66,70,67,-1,66,68,71,-1,66,71,69,-1,69,72,73,-1,69,73,70,-1,69,71,74,-1,69,74,72,-1,72,75,76,-1,72,76,73,-1,72,74,77,-1,72,77,75,-1,78,79,80,-1,78,80,81,-1,78,82,83,-1,78,83,79,-1,79,84,85,-1,79,85,80,-1,79,83,86,-1,79,86,84,-1,84,87,88,-1,84,88,85,-1,84,86,89,-1,84,89,87,-1,87,90,91,-1,87,91,88,-1,87,89,92,-1,87,92,90,-1,90,93,94,-1,90,94,91,-1,90,92,95,-1,90,95,93,-1,93,96,97,-1,93,97,94,-1,93,95,98,-1,93,98,96,-1,96,4,7,-1,96,7,97,-1,96,98,5,-1,96,5,4,-1,3,2,99,-1,3,99,100,-1,3,100,101,-1,3,101,7,-1,2,10,102,-1,2,102,99,-1,10,13,103,-1,10,103,102,-1,13,16,104,-1,13,104,103,-1,16,19,105,-1,16,105,104,-1,19,22,106,-1,19,106,105,-1,22,25,107,-1,22,107,106,-1,25,28,108,-1,25,108,107,-1,28,31,109,-1,28,109,108,-1,31,34,110,-1,31,110,109,-1,34,37,111,-1,34,111,110,-1,37,40,112,-1,37,112,111,-1,40,43,113,-1,40,113,112,-1,43,46,114,-1,43,114,113,-1,46,49,115,-1,46,115,114,-1,49,52,116,-1,49,116,115,-1,52,55,117,-1,52,117,116,-1,55,58,118,-1,55,118,117,-1,58,61,119,-1,58,119,118,-1,61,64,120,-1,61,120,119,-1,64,67,121,-1,64,121,120,-1,67,70,122,-1,67,122,121,-1,70,73,123,-1,70,123,122,-1,73,76,124,-1,73,124,123,-1,81,80,125,-1,81,125,126,-1,80,85,127,-1,80,127,125,-1,85,88,128,-1,85,128,127,-1,88,91,129,-1,88,129,128,-1,91,94,130,-1,91,130,129,-1,94,97,131,-1,94,131,130,-1,97,7,101,-1,97,101,131,-1,8,6,132,-1,8,132,133,-1,8,133,134,-1,8,134,11,-1,6,5,135,-1,6,135,132,-1,5,98,136,-1,5,136,135,-1,98,95,137,-1,98,137,136,-1,95,92,138,-1,95,138,137,-1,92,89,139,-1,92,139,138,-1,89,86,140,-1,89,140,139,-1,86,83,141,-1,86,141,140,-1,83,82,142,-1,83,142,141,-1,77,74,143,-1,77,143,144,-1,74,71,145,-1,74,145,143,-1,71,68,146,-1,71,146,145,-1,68,65,147,-1,68,147,146,-1,65,62,148,-1,65,148,147,-1,62,59,149,-1,62,149,148,-1,59,56,150,-1,59,150,149,-1,56,53,151,-1,56,151,150,-1,53,50,152,-1,53,152,151,-1,50,47,153,-1,50,153,152,-1,47,44,154,-1,47,154,153,-1,44,41,155,-1,44,155,154,-1,41,38,156,-1,41,156,155,-1,38,35,157,-1,38,157,156,-1,35,32,158,-1,35,158,157,-1,32,29,159,-1,32,159,158,-1,29,26,160,-1,29,160,159,-1,26,23,161,-1,26,161,160,-1,23,20,162,-1,23,162,161,-1,20,17,163,-1,20,163,162,-1,17,14,164,-1,17,164,163,-1,14,11,134,-1,14,134,164,-1,133,132,165,-1,133,165,166,-1,133,166,167,-1,133,167,134,-1,132,135,168,-1,132,168,165,-1,135,136,169,-1,135,169,168,-1,136,137,170,-1,136,170,169,-1,137,138,171,-1,137,171,170,-1,138,139,172,-1,138,172,171,-1,139,140,173,-1,139,173,172,-1,140,141,174,-1,140,174,173,-1,141,142,175,-1,141,175,174,-1,144,143,176,-1,144,176,177,-1,143,145,178,-1,143,178,176,-1,145,146,179,-1,145,179,178,-1,146,147,180,-1,146,180,179,-1,147,148,181,-1,147,181,180,-1,148,149,182,-1,148,182,181,-1,149,150,183,-1,149,183,182,-1,150,151,184,-1,150,184,183,-1,151,152,185,-1,151,185,184,-1,152,153,186,-1,152,186,185,-1,153,154,187,-1,153,187,186,-1,154,155,188,-1,154,188,187,-1,155,156,189,-1,155,189,188,-1,156,157,190,-1,156,190,189,-1,157,158,191,-1,157,191,190,-1,158,159,192,-1,158,192,191,-1,159,160,193,-1,159,193,192,-1,160,161,194,-1,160,194,193,-1,161,162,195,-1,161,195,194,-1,162,163,196,-1,162,196,195,-1,163,164,197,-1,163,197,196,-1,164,134,167,-1,164,167,197,-1,166,165,198,-1,166,198,199,-1,166,199,200,-1,166,200,167,-1,165,168,201,-1,165,201,198,-1,168,169,202,-1,168,202,201,-1,169,170,203,-1,169,203,202,-1,170,171,204,-1,170,204,203,-1,171,172,205,-1,171,205,204,-1,172,173,206,-1,172,206,205,-1,173,174,207,-1,173,207,206,-1,174,175,208,-1,174,208,207,-1,177,176,209,-1,177,209,210,-1,176,178,211,-1,176,211,209,-1,178,179,212,-1,178,212,211,-1,179,180,213,-1,179,213,212,-1,180,181,214,-1,180,214,213,-1,181,182,215,-1,181,215,214,-1,182,183,216,-1,182,216,215,-1,183,184,217,-1,183,217,216,-1,184,185,218,-1,184,218,217,-1,185,186,219,-1,185,219,218,-1,186,187,220,-1,186,220,219,-1,187,188,221,-1,187,221,220,-1,188,189,222,-1,188,222,221,-1,189,190,223,-1,189,223,222,-1,190,191,224,-1,190,224,223,-1,191,192,225,-1,191,225,224,-1,192,193,226,-1,192,226,225,-1,193,194,227,-1,193,227,226,-1,194,195,228,-1,194,228,227,-1,195,196,229,-1,195,229,228,-1,196,197,230,-1,196,230,229,-1,197,167,200,-1,197,200,230,-1,100,99,102,-1,100,102,103,-1,100,103,104,-1,100,104,105,-1,100,105,106,-1,100,106,107,-1,100,107,108,-1,100,108,109,-1,100,109,110,-1,100,110,111,-1,100,111,112,-1,100,112,113,-1,100,113,114,-1,100,114,115,-1,100,115,116,-1,100,116,117,-1,100,117,118,-1,100,118,119,-1,100,119,120,-1,100,120,121,-1,100,121,122,-1,100,122,123,-1,100,123,126,-1,100,126,125,-1,100,125,127,-1,100,127,128,-1,100,128,129,-1,100,129,130,-1,100,130,131,-1,100,131,101,-1,199,198,198,-1,199,198,231,-1,199,231,232,-1,199,232,200,-1,198,201,233,-1,198,233,198,-1,201,202,234,-1,201,234,233,-1,202,203,235,-1,202,235,234,-1,203,204,204,-1,203,204,235,-1,204,205,236,-1,204,236,204,-1,205,206,237,-1,205,237,236,-1,206,207,238,-1,206,238,237,-1,207,208,208,-1,207,208,238,-1,210,209,239,-1,210,239,210,-1,209,211,240,-1,209,240,239,-1,211,212,241,-1,211,241,240,-1,212,213,213,-1,212,213,241,-1,213,214,242,-1,213,242,213,-1,214,215,243,-1,214,243,242,-1,215,216,244,-1,215,244,243,-1,216,217,217,-1,216,217,244,-1,217,218,245,-1,217,245,217,-1,218,219,246,-1,218,246,245,-1,219,220,247,-1,219,247,246,-1,220,221,221,-1,220,221,247,-1,221,222,248,-1,221,248,221,-1,222,223,249,-1,222,249,248,-1,223,224,250,-1,223,250,249,-1,224,225,225,-1,224,225,250,-1,225,226,251,-1,225,251,225,-1,226,227,252,-1,226,252,251,-1,227,228,253,-1,227,253,252,-1,228,229,229,-1,228,229,253,-1,229,230,254,-1,229,254,229,-1,230,200,232,-1,230,232,254,-1,231,198,255,-1,231,255,256,-1,231,256,257,-1,231,257,232,-1,198,233,258,-1,198,258,255,-1,233,234,259,-1,233,259,258,-1,234,235,260,-1,234,260,259,-1,235,204,261,-1,235,261,260,-1,204,236,262,-1,204,262,261,-1,236,237,263,-1,236,263,262,-1,237,238,264,-1,237,264,263,-1,238,208,265,-1,238,265,264,-1,210,239,266,-1,210,266,267,-1,239,240,268,-1,239,268,266,-1,240,241,269,-1,240,269,268,-1,241,213,270,-1,241,270,269,-1,213,242,271,-1,213,271,270,-1,242,243,272,-1,242,272,271,-1,243,244,273,-1,243,273,272,-1,244,217,274,-1,244,274,273,-1,217,245,275,-1,217,275,274,-1,245,246,276,-1,245,276,275,-1,246,247,277,-1,246,277,276,-1,247,221,278,-1,247,278,277,-1,221,248,279,-1,221,279,278,-1,248,249,280,-1,248,280,279,-1,249,250,281,-1,249,281,280,-1,250,225,282,-1,250,282,281,-1,225,251,283,-1,225,283,282,-1,251,252,284,-1,251,284,283,-1,252,253,285,-1,252,285,284,-1,253,229,286,-1,253,286,285,-1,229,254,287,-1,229,287,286,-1,254,232,257,-1,254,257,287,-1,256,255,258,-1,256,258,259,-1,256,259,260,-1,256,260,261,-1,256,261,262,-1,256,262,263,-1,256,263,264,-1,256,264,265,-1,256,265,266,-1,256,266,268,-1,256,268,269,-1,256,269,270,-1,256,270,271,-1,256,271,272,-1,256,272,273,-1,256,273,274,-1,256,274,275,-1,256,275,276,-1,256,276,277,-1,256,277,278,-1,256,278,279,-1,256,279,280,-1,256,280,281,-1,256,281,282,-1,256,282,283,-1,256,283,284,-1,256,284,285,-1,256,285,286,-1,256,286,287,-1,256,287,257,-1]) \
         .setCoord(CoordinateObject() \
          .setPoint([1,0.276,0,0.98079,0.276,0.19509,0.98079,-0.6623,0.19509,1,-0.6623,0,0.98079,0.276,-0.19509,0.93371,0.34,-0.18573,0.952,0.34,0,0.98079,-0.6623,-0.19509,0.93371,0.34,0.18573,0.92388,0.276,0.38268,0.92388,-0.6623,0.38268,0.87953,0.34,0.36432,0.83147,0.276,0.55557,0.83147,-0.6623,0.55557,0.79156,0.34,0.5289,0.70711,0.276,0.70711,0.70711,-0.6623,0.70711,0.67317,0.34,0.67317,0.55557,0.276,0.83147,0.55557,-0.6623,0.83147,0.5289,0.34,0.79156,0.38268,0.276,0.92388,0.38268,-0.6623,0.92388,0.36432,0.34,0.87953,0.19509,0.276,0.98079,0.19509,-0.6623,0.98079,0.18573,0.34,0.93371,0,0.276,1,0,-0.6623,1,0,0.34,0.952,-0.19509,0.276,0.98079,-0.19509,-0.6623,0.98079,-0.18573,0.34,0.93371,-0.38268,0.276,0.92388,-0.38268,-0.6623,0.92388,-0.36432,0.34,0.87953,-0.55557,0.276,0.83147,-0.55557,-0.6623,0.83147,-0.5289,0.34,0.79156,-0.70711,0.276,0.70711,-0.70711,-0.6623,0.70711,-0.67317,0.34,0.67317,-0.83147,0.276,0.55557,-0.83147,-0.6623,0.55557,-0.79156,0.34,0.5289,-0.92388,0.276,0.38268,-0.92388,-0.6623,0.38268,-0.87953,0.34,0.36432,-0.98079,0.276,0.19509,-0.98079,-0.6623,0.19509,-0.93371,0.34,0.18573,-1,0.276,0,-1,-0.6623,0,-0.952,0.34,0,-0.98079,0.276,-0.19509,-0.98079,-0.6623,-0.19509,-0.93371,0.34,-0.18573,-0.92388,0.276,-0.38268,-0.92388,-0.6623,-0.38268,-0.87953,0.34,-0.36432,-0.83147,0.276,-0.55557,-0.83147,-0.6623,-0.55557,-0.79156,0.34,-0.5289,-0.70711,0.276,-0.70711,-0.70711,-0.6623,-0.70711,-0.67317,0.34,-0.67317,-0.55557,0.276,-0.83147,-0.55557,-0.6623,-0.83147,-0.5289,0.34,-0.79156,-0.38268,0.276,-0.92388,-0.38268,-0.6623,-0.92388,-0.36432,0.34,-0.87953,-0.19509,0.276,-0.98079,-0.19509,-0.6623,-0.98079,-0.18573,0.34,-0.93371,0,0.276,-1,0,-0.6623,-1,0,0.34,-0.952,0.19509,0.276,-0.98079,0.19509,-0.6623,-0.98079,0.18573,0.34,-0.93371,0.38268,0.276,-0.92388,0.38268,-0.6623,-0.92388,0.36432,0.34,-0.87953,0.55557,0.276,-0.83147,0.55557,-0.6623,-0.83147,0.5289,0.34,-0.79156,0.70711,0.276,-0.70711,0.70711,-0.6623,-0.70711,0.67317,0.34,-0.67317,0.83147,0.276,-0.55557,0.83147,-0.6623,-0.55557,0.79156,0.34,-0.5289,0.92388,0.276,-0.38268,0.92388,-0.6623,-0.38268,0.87953,0.34,-0.36432,0.28009,-1.53955,0.05571,0.28558,-1.53955,0,0.28009,-1.53955,-0.05571,0.26384,-1.53955,0.10929,0.23745,-1.53955,0.15866,0.20194,-1.53955,0.20194,0.15866,-1.53955,0.23745,0.10929,-1.53955,0.26384,0.05571,-1.53955,0.28009,0,-1.53955,0.28558,-0.05571,-1.53955,0.28009,-0.10929,-1.53955,0.26384,-0.15866,-1.53955,0.23745,-0.20194,-1.53955,0.20194,-0.23745,-1.53955,0.15866,-0.26384,-1.53955,0.10929,-0.28009,-1.53955,0.05571,-0.28558,-1.53955,0,-0.28009,-1.53955,-0.05571,-0.26384,-1.53955,-0.10929,-0.23745,-1.53955,-0.15866,-0.20194,-1.53955,-0.20194,-0.15866,-1.53955,-0.23745,-0.10929,-1.53955,-0.26384,-0.05571,-1.53955,-0.28009,0,-1.53955,-0.28558,0.05571,-1.53955,-0.28009,0.10929,-1.53955,-0.26384,0.15866,-1.53955,-0.23745,0.20194,-1.53955,-0.20194,0.23745,-1.53955,-0.15866,0.26384,-1.53955,-0.10929,0.78826,0.43956,0,0.77311,0.43956,0.15378,0.72825,0.43956,0.30165,0.77311,0.43956,-0.15378,0.72825,0.43956,-0.30165,0.65541,0.43956,-0.43793,0.55738,0.43956,-0.55738,0.43793,0.43956,-0.65541,0.30165,0.43956,-0.72825,0.15378,0.43956,-0.77311,0,0.43956,-0.78826,-0.15378,0.43956,-0.77311,-0.30165,0.43956,-0.72825,-0.43793,0.43956,-0.65541,-0.55738,0.43956,-0.55738,-0.65541,0.43956,-0.43793,-0.72825,0.43956,-0.30165,-0.77311,0.43956,-0.15378,-0.78826,0.43956,0,-0.77311,0.43956,0.15378,-0.72825,0.43956,0.30165,-0.65541,0.43956,0.43793,-0.55738,0.43956,0.55738,-0.43793,0.43956,0.65541,-0.30165,0.43956,0.72825,-0.15378,0.43956,0.77311,0,0.43956,0.78826,0.15378,0.43956,0.77311,0.30165,0.43956,0.72825,0.43793,0.43956,0.65541,0.55738,0.43956,0.55738,0.65541,0.43956,0.43793,0.29638,0.50356,0,0.29069,0.50356,0.05782,0.27382,0.50356,0.11342,0.29069,0.50356,-0.05782,0.27382,0.50356,-0.11342,0.24643,0.50356,-0.16466,0.20958,0.50356,-0.20958,0.16466,0.50356,-0.24643,0.11342,0.50356,-0.27382,0.05782,0.50356,-0.29069,0,0.50356,-0.29638,-0.05782,0.50356,-0.29069,-0.11342,0.50356,-0.27382,-0.16466,0.50356,-0.24643,-0.20958,0.50356,-0.20958,-0.24643,0.50356,-0.16466,-0.27382,0.50356,-0.11342,-0.29069,0.50356,-0.05782,-0.29638,0.50356,0,-0.29069,0.50356,0.05782,-0.27382,0.50356,0.11342,-0.24643,0.50356,0.16466,-0.20958,0.50356,0.20958,-0.16466,0.50356,0.24643,-0.11342,0.50356,0.27382,-0.05782,0.50356,0.29069,0,0.50356,0.29638,0.05782,0.50356,0.29069,0.11342,0.50356,0.27382,0.16466,0.50356,0.24643,0.20958,0.50356,0.20958,0.24643,0.50356,0.16466,0.29638,0.5398,0,0.29069,0.5398,0.05782,0.27382,0.5398,0.11342,0.29069,0.5398,-0.05782,0.27382,0.5398,-0.11342,0.24643,0.5398,-0.16466,0.20958,0.5398,-0.20958,0.16466,0.5398,-0.24643,0.11342,0.5398,-0.27382,0.05782,0.5398,-0.29069,0,0.5398,-0.29638,-0.05782,0.5398,-0.29069,-0.11342,0.5398,-0.27382,-0.16466,0.5398,-0.24643,-0.20958,0.5398,-0.20958,-0.24643,0.5398,-0.16466,-0.27382,0.5398,-0.11342,-0.29069,0.5398,-0.05782,-0.29638,0.5398,0,-0.29069,0.5398,0.05782,-0.27382,0.5398,0.11342,-0.24643,0.5398,0.16466,-0.20958,0.5398,0.20958,-0.16466,0.5398,0.24643,-0.11342,0.5398,0.27382,-0.05782,0.5398,0.29069,0,0.5398,0.29638,0.05782,0.5398,0.29069,0.11342,0.5398,0.27382,0.16466,0.5398,0.24643,0.20958,0.5398,0.20958,0.24643,0.5398,0.16466,0.25311,0.5398,0,0.24825,0.5398,0.04938,0.23385,0.5398,0.09686,0.24825,0.5398,-0.04938,0.23385,0.5398,-0.09686,0.21046,0.5398,-0.14062,0.17898,0.5398,-0.17898,0.14062,0.5398,-0.21046,0.09686,0.5398,-0.23385,0.04938,0.5398,-0.24825,0,0.5398,-0.25311,-0.04938,0.5398,-0.24825,-0.09686,0.5398,-0.23385,-0.14062,0.5398,-0.21046,-0.17898,0.5398,-0.17898,-0.21046,0.5398,-0.14062,-0.23385,0.5398,-0.09686,-0.24825,0.5398,-0.04938,-0.25311,0.5398,0,-0.24825,0.5398,0.04938,-0.23385,0.5398,0.09686,-0.21046,0.5398,0.14062,-0.17898,0.5398,0.17898,-0.14062,0.5398,0.21046,-0.09686,0.5398,0.23385,-0.04938,0.5398,0.24825,0,0.5398,0.25311,0.04938,0.5398,0.24825,0.09686,0.5398,0.23385,0.14062,0.5398,0.21046,0.17898,0.5398,0.17898,0.21046,0.5398,0.14062,0.25311,0.51249,0,0.24825,0.51249,0.04938,0.23385,0.51249,0.09686,0.24825,0.51249,-0.04938,0.23385,0.51249,-0.09686,0.21046,0.51249,-0.14062,0.17898,0.51249,-0.17898,0.14062,0.51249,-0.21046,0.09686,0.51249,-0.23385,0.04938,0.51249,-0.24825,0,0.51249,-0.25311,-0.04938,0.51249,-0.24825,-0.09686,0.51249,-0.23385,-0.14062,0.51249,-0.21046,-0.17898,0.51249,-0.17898,-0.21046,0.51249,-0.14062,-0.23385,0.51249,-0.09686,-0.24825,0.51249,-0.04938,-0.25311,0.51249,0,-0.24825,0.51249,0.04938,-0.23385,0.51249,0.09686,-0.21046,0.51249,0.14062,-0.17898,0.51249,0.17898,-0.14062,0.51249,0.21046,-0.09686,0.51249,0.23385,-0.04938,0.51249,0.24825,0,0.51249,0.25311,0.04938,0.51249,0.24825,0.09686,0.51249,0.23385,0.14062,0.51249,0.21046,0.17898,0.51249,0.17898,0.21046,0.51249,0.14062]) \
         ) \
         .setTexCoord(TextureCoordinateObject() \
          .setPoint([0.75,0.873,0.719,0.873,0.719,0.422,0.75,0.422,0.781,0.873,0.781,0.904,0.75,0.904,0.781,0.422,0.719,0.904,0.688,0.873,0.688,0.422,0.687,0.904,0.656,0.873,0.656,0.422,0.656,0.904,0.625,0.873,0.625,0.422,0.625,0.904,0.594,0.873,0.594,0.422,0.594,0.904,0.562,0.873,0.562,0.422,0.563,0.904,0.531,0.873,0.531,0.422,0.531,0.904,0.5,0.873,0.5,0.422,0.5,0.904,0.469,0.873,0.469,0.422,0.469,0.904,0.438,0.873,0.438,0.422,0.437,0.904,0.406,0.873,0.406,0.422,0.406,0.904,0.375,0.873,0.375,0.422,0.375,0.904,0.344,0.873,0.344,0.422,0.344,0.904,0.312,0.873,0.312,0.422,0.313,0.904,0.281,0.873,0.281,0.422,0.281,0.904,0.25,0.873,0.25,0.422,0.25,0.904,0.219,0.873,0.219,0.422,0.219,0.904,0.188,0.873,0.188,0.422,0.187,0.904,0.156,0.873,0.156,0.422,0.156,0.904,0.125,0.873,0.125,0.422,0.125,0.904,0.094,0.873,0.094,0.422,0.094,0.904,0.062,0.873,0.062,0.422,0.063,0.904,0.031,0.873,0.031,0.422,0.031,0.904,0,0.873,0,0.422,0,0.904,1,0.873,0.969,0.873,0.969,0.422,1,0.422,1,0.904,0.969,0.904,0.938,0.873,0.938,0.422,0.937,0.904,0.906,0.873,0.906,0.422,0.906,0.904,0.875,0.873,0.875,0.422,0.875,0.904,0.844,0.873,0.844,0.422,0.844,0.904,0.812,0.873,0.812,0.422,0.813,0.904,0.719,0,0.75,0,0.781,0,0.687,0,0.656,0,0.625,0,0.594,0,0.563,0,0.531,0,0.5,0,0.469,0,0.437,0,0.406,0,0.375,0,0.344,0,0.313,0,0.281,0,0.25,0,0.219,0,0.187,0,0.156,0,0.125,0,0.094,0,0.063,0,0.031,0,0,0,0.969,0,1,0,0.937,0,0.906,0,0.875,0,0.844,0,0.813,0,0.75,0.952,0.719,0.952,0.687,0.952,0.781,0.952,0.813,0.952,0.844,0.952,0.875,0.952,0.906,0.952,0.937,0.952,0.969,0.952,1,0.952,0.031,0.952,0,0.952,0.063,0.952,0.094,0.952,0.125,0.952,0.156,0.952,0.187,0.952,0.219,0.952,0.25,0.952,0.281,0.952,0.313,0.952,0.344,0.952,0.375,0.952,0.406,0.952,0.437,0.952,0.469,0.952,0.5,0.952,0.531,0.952,0.563,0.952,0.594,0.952,0.625,0.952,0.656,0.952,0.75,0.983,0.719,0.983,0.688,0.983,0.781,0.983,0.812,0.983,0.844,0.983,0.875,0.983,0.906,0.983,0.938,0.983,0.969,0.983,1,0.983,0.031,0.983,0,0.983,0.062,0.983,0.094,0.983,0.125,0.983,0.156,0.983,0.188,0.983,0.219,0.983,0.25,0.983,0.281,0.983,0.312,0.983,0.344,0.983,0.375,0.983,0.406,0.983,0.438,0.983,0.469,0.983,0.5,0.983,0.531,0.983,0.562,0.983,0.594,0.983,0.625,0.983,0.656,0.983,0.75,1,0.719,1,0.688,1,0.781,1,0.812,1,0.844,1,0.875,1,0.906,1,0.938,1,0.969,1,1,1,0.031,1,0,1,0.062,1,0.094,1,0.125,1,0.156,1,0.188,1,0.219,1,0.25,1,0.281,1,0.312,1,0.344,1,0.375,1,0.406,1,0.438,1,0.469,1,0.5,1,0.531,1,0.562,1,0.594,1,0.625,1,0.656,1,0.719,1,0.688,1,0.781,1,0.813,1,0.844,1,0.906,1,0.938,1,0.969,1,0.031,1,0.063,1,0.094,1,0.156,1,0.187,1,0.219,1,0.281,1,0.313,1,0.344,1,0.406,1,0.437,1,0.469,1,0.531,1,0.563,1,0.594,1,0.656,1,0.75,0.987,0.719,0.987,0.688,0.987,0.781,0.987,0.813,0.987,0.844,0.987,0.875,0.987,0.906,0.987,0.938,0.987,0.969,0.987,1,0.987,0.031,0.987,0,0.987,0.063,0.987,0.094,0.987,0.125,0.987,0.156,0.987,0.187,0.987,0.219,0.987,0.25,0.987,0.281,0.987,0.313,0.987,0.344,0.987,0.375,0.987,0.406,0.987,0.437,0.987,0.469,0.987,0.5,0.987,0.531,0.987,0.563,0.987,0.594,0.987,0.625,0.987,0.656,0.987]) \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./Teapot.newf.x3d")
