from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.3")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("TextSpecialCharacters.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("description").setContent("Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities")
head1.addMeta(meta3)
meta4 = metaObject().setName("creator").setContent("Don Brutzman")
head1.addMeta(meta4)
meta5 = metaObject().setName("created").setContent("12 July 2008")
head1.addMeta(meta5)
meta6 = metaObject().setName("modified").setContent("2 April 2017")
head1.addMeta(meta6)
meta7 = metaObject().setName("reference").setContent("Character entity references in HTML 4")
head1.addMeta(meta7)
meta8 = metaObject().setName("reference").setContent("http://www.w3.org/TR/REC-html40/sgml/entities.html")
head1.addMeta(meta8)
meta9 = metaObject().setName("rights").setContent("Copyright (c) Don Brutzman and Leonard Daly, 2008")
head1.addMeta(meta9)
meta10 = metaObject().setName("identifier").setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d")
head1.addMeta(meta10)
meta11 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta11)
meta12 = metaObject().setName("license").setContent("../license.html")
head1.addMeta(meta12)
meta13 = metaObject().setName("translated").setContent("13 May 2017")
head1.addMeta(meta13)
meta14 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta14)
meta15 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta15)
meta16 = metaObject().setName("translated").setContent("13 May 2017")
head1.addMeta(meta16)
meta17 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta17)
X3D0.setHead(head1)
Scene18 = SceneObject()
Background19 = BackgroundObject().setSkyColor([1,1,1])
Scene18.addChild(Background19)
Viewpoint20 = ViewpointObject().setDescription("Default View").setPosition([0,0,15])
Scene18.addChild(Viewpoint20)
Shape21 = ShapeObject()

Shape21.addComments(CommentsBlock("Empty string \"\" means to skip a line"))

Shape21.addComments(CommentsBlock("The ampersand escape characters are based on XML rules"))

Shape21.addComments(CommentsBlock("apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute"))

Shape21.addComments(CommentsBlock("ampersand & is &amp; and needs to be escaped"))

Shape21.addComments(CommentsBlock("quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute"))

Shape21.addComments(CommentsBlock("quotation \" can be used within an X3D string if escaped with backslash \\ as \\\""))

Shape21.addComments(CommentsBlock("backslash \\ is used as escape character for \" (and itself) in X3D"))

Shape21.addComments(CommentsBlock("character entities are listed in HTML specification and are good for any XML"))
Text22 = TextObject().setDEF("DefaultText").setString(["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe ' is &amp;apos;","ampersand &amp; is &amp;amp;","quote mark " is &amp;quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &amp;#928; XML character entity"])
FontStyle23 = FontStyleObject().setDEF("CenteredFontStyle").setJustify(["MIDDLE","MIDDLE"])
Text22.setFontStyle(FontStyle23)
Shape21.setGeometry(Text22)
Appearance24 = AppearanceObject()
Material25 = MaterialObject().setDEF("DefaultMaterial").setDiffuseColor([0.2,0.2,0.2])
Appearance24.setMaterial(Material25)
Shape21.setAppearance(Appearance24)
Scene18.addChild(Shape21)
X3D0.setScene(Scene18)

X3D0.toFileX3D("TextSpecialCharacters.new.x3d")
