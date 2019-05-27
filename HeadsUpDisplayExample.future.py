import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("HeadsUpDisplayExample.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Leonard Daly and Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("15 July 2006")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("24 October 2016")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("HeadsUpDisplayPrototype.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://X3dGraphics.com")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/X3dResources.html")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("rights")).setContent(x3dpsail.SFString("Copyright 2006, Daly Realism and Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("subject")).setContent(x3dpsail.SFString("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        #Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n

        .addChild(x3dpsail.ExternProtoDeclare().setName(x3dpsail.SFString("HeadsUpDisplay")).setAppinfo(x3dpsail.SFString("Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location")).setUrl(x3dpsail.MFString(["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"]))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("screenOffset")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("offset position for HUD relative to current view location, default 0 0 -5")).setType(x3dpsail.SFString("SFVec3f")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("children")).setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("X3D content positioned at HUD offset")).setType(x3dpsail.SFString("MFNode")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("position_changed")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("HUD position update (in world coordinates) relative to original location")).setType(x3dpsail.SFString("SFVec3f")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("orientation_changed")).setAccessType(x3dpsail.SFString("outputOnly")).setAppinfo(x3dpsail.SFString("HUD orientation update relative to original location")).setType(x3dpsail.SFString("SFRotation"))))
        .addChild(x3dpsail.Background().setDEF(x3dpsail.SFString("SandyShallowBottom")).setGroundAngle(x3dpsail.MFFloat([0.05,1.52,1.56,1.5707])).setGroundColor(x3dpsail.MFColor([0.2,0.2,0,0.3,0.3,0,0.5,0.5,0.3,0.1,0.3,0.4,0,0.2,0.4])).setSkyAngle(x3dpsail.MFFloat([0.04,0.05,0.1,1.309,1.57])).setSkyColor(x3dpsail.MFColor([0.8,0.8,0.2,0.8,0.8,0.2,0.1,0.1,0.6,0.1,0.1,0.6,0.1,0.25,0.8,0.6,0.6,0.9])))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Heads-up display (HUD)")))
        #ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence

        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("HeadsUpDisplay")).setDEF(x3dpsail.SFString("HeadsUpDisplayInstance"))
          #example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view

          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("screenOffset")).setValue(x3dpsail.SFString("-0.75 1 -5")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("children"))
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["HUD text stays fixed","while user navigates"]))
                .setFontStyle(x3dpsail.FontStyle().setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"])).setSize(x3dpsail.SFFloat(0.3))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.894118,0.819608,1)))))))
        .addChild(x3dpsail.Inline().setUrl(x3dpsail.MFString(["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"])))))

X3D0.toFileX3D("./future/./HeadsUpDisplayExample_RoundTrip.x3d")
