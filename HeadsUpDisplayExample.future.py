import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("HeadsUpDisplayExample.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Leonard Daly and Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("15 July 2006") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("24 October 2016") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HeadsUpDisplayPrototype.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://X3dGraphics.com") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html") \
    ) \
    .addMeta(metaObject() \
     .setName("rights") \
     .setContent("Copyright 2006, Daly Realism and Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addComments(CommentsBlock("""Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n""")) \
    .addChild(ExternProtoDeclareObject() \
     .setName("HeadsUpDisplay") \
     .setAppinfo("Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location") \
     .setUrl(["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"]) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("screenOffset") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("offset position for HUD relative to current view location, default 0 0 -5") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFNODE) \
      .setName("children") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("X3D content positioned at HUD offset") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("position_changed") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("HUD position update (in world coordinates) relative to original location") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFROTATION) \
      .setName("orientation_changed") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setAppinfo("HUD orientation update relative to original location") \
     ) \
    ) \
    .addChild(BackgroundObject() \
     .setDEF("SandyShallowBottom") \
     .setGroundAngle([0.05,1.52,1.56,1.5707]) \
     .setGroundColor([0.2,0.2,0,0.3,0.3,0,0.5,0.5,0.3,0.1,0.3,0.4,0,0.2,0.4]) \
     .setSkyAngle([0.04,0.05,0.1,1.309,1.57]) \
     .setSkyColor([0.8,0.8,0.2,0.8,0.8,0.2,0.1,0.1,0.6,0.1,0.1,0.6,0.1,0.25,0.8,0.6,0.6,0.9]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Heads-up display (HUD)") \
    ) \
    .addComments(CommentsBlock("""ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence""")) \
    .addChild(ProtoInstanceObject() \
     .setName("HeadsUpDisplay") \
     .setDEF("HeadsUpDisplayInstance") \
     .addComments(CommentsBlock("""example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view""")) \
     .addFieldValue(fieldValueObject() \
      .setName("screenOffset") \
      .setValue("-0.75 1 -5") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("children") \
      .addChild(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["HUD text stays fixed","while user navigates"]) \
        .setFontStyle(FontStyleObject() \
         .setJustify(["MIDDLE","MIDDLE"]) \
         .setSize(0.3) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0.894118,0.819608,1]) \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(InlineObject() \
     .setUrl(["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"]) \
    ) \
   ) \

X3D0.toFileX3D("./future/./HeadsUpDisplayExample.newf.x3d")
