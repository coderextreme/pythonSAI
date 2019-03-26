import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John W Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("December 13 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("force.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/force.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("beginnings of a force directed graph in 3D") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(GroupObject() \
     .addChildren(ShapeObject() \
      .setGeometry(ExtrusionObject(spine = [-50,-50,0,50,50,0], creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
       .setDEF("extrusion") \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0,1,0]) \
       ) \
      ) \
     ) \
     .addChildren(TimeSensorObject() \
      .setDEF("TourTime") \
      .setLoop(True) \
     ) \
     .addChildren(ScriptObject() \
      .setDEF("MoveCylinder") \
      .addField(fieldObject() \
       .setName("set_cycle") \
       .setAccessType("inputOnly") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("spine") \
       .setAccessType("inputOutput") \
       .setType("MFVec3f") \
       .setValue("-50 -50 0 50 50 0") \
      ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"                function set_cycle(value) {\n"+
"                        Browser.print(value);\n"+
"                        var endA = new SFVec3f(spine[0].x*Math.random()*2, spine[0].y*Math.random()*2, spine[0].z*Math.random()*2);\n"+
"                        var endB = new SFVec3f(spine[1].x*Math.random()*2, spine[1].y*Math.random()*2, spine[1].z*Math.random()*2);\n"+
"		        spine = new MFVec3f([endA, endB]);\n"+
"                }''')
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("TourTime") \
      .setFromField("cycleTime") \
      .setToNode("MoveCylinder") \
      .setToField("set_cycle") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("MoveCylinder") \
      .setFromField("spine_changed") \
      .setToNode("extrusion") \
      .setToField("spine") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./extrusion.newf.x3d")
