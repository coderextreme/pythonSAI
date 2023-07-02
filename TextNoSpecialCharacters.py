print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "TextSpecialCharacters.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "12 July 2008"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "2 April 2017"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "Character entity references in HTML 4"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "http://www.w3.org/TR/REC-html40/sgml/entities.html"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "rights"
meta9.content = "Copyright (c) Don Brutzman and Leonard Daly, 2008"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "identifier"
meta10.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "generator"
meta11.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "license"
meta12.content = "../license.html"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
Background14 = x3d.Background()

Scene13.children.append(Background14)
Viewpoint15 = x3d.Viewpoint()
Viewpoint15.description = "Default View"
Viewpoint15.position = [0,0,15]

Scene13.children.append(Viewpoint15)
Shape16 = x3d.Shape()
#Empty string \"\" means to skip a line
#The ampersand escape characters are based on XML rules
#apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute
#ampersand & is &amp; and needs to be escaped
#quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute
#quotation \" can be used within an X3D string if escaped with backslash \\ as \\\"\"
#backslash \\ is used as escape character for \" (and itself) in X3D
#character entities are listed in HTML specification and are good for any XML
Text17 = x3d.Text()
Text17.DEF = "DefaultText"
Text17.string = ["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe ' is &apos;","ampersand & is &amp;","quote mark \" is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi is pi is pi XML character entity"]
FontStyle18 = x3d.FontStyle()
FontStyle18.DEF = "CenteredFontStyle"
FontStyle18.justify = ["MIDDLE","MIDDLE"]

Text17.fontStyle = FontStyle18

Shape16.geometry = Text17
Appearance19 = x3d.Appearance()
Material20 = x3d.Material()
Material20.DEF = "DefaultMaterial"
Material20.diffuseColor = [0.2,0.2,0.2]

Appearance19.material = Material20

Shape16.appearance = Appearance19

Scene13.children.append(Shape16)

X3D0.Scene = Scene13
f = open("././TextNoSpecialCharacters_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
