import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("TextSpecialCharacters.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("12 July 2008")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("2 April 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("Character entity references in HTML 4")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://www.w3.org/TR/REC-html40/sgml/entities.html")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("rights")).setContent(x3dpsail.SFString("Copyright (c) Don Brutzman and Leonard Daly, 2008")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([1,1,1])))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Default View")).setPosition(x3dpsail.SFVec3f(0,0,15)))
        .addChild(x3dpsail.Shape()
          #Empty string \"\" means to skip a line

          #The ampersand escape characters are based on XML rules

          #apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute

          #ampersand & is &amp; and needs to be escaped

          #quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute

          #quotation \" can be used within an X3D string if escaped with backslash \\ as \\\"\"

          #backslash \\ is used as escape character for \" (and itself) in X3D

          #character entities are listed in HTML specification and are good for any XML

          .setGeometry(x3dpsail.Text().setDEF(x3dpsail.SFString("DefaultText")).setString(x3dpsail.MFString(["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe ' is &apos;","ampersand & is &amp;","quote mark \" is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &#928; XML character entity"]))
            .setFontStyle(x3dpsail.FontStyle().setDEF(x3dpsail.SFString("CenteredFontStyle")).setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"]))))
          .setAppearance(x3dpsail.Appearance()
            .setMaterial(x3dpsail.Material().setDEF(x3dpsail.SFString("DefaultMaterial")).setDiffuseColor(x3dpsail.SFColor(0.2,0.2,0.2)))))))

X3D0.toFileX3D("./future/./TextSpecialCharacters_RoundTrip.x3d")
