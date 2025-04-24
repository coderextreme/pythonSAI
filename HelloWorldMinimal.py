print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
""" All head/meta tags are optional, WorldInfo is also optional """
""" Text node not supported by X3D Interchange profile, use Immersive profile or Text component level 1 """
head1 = x3d.head()
meta2 = x3d.meta()
meta2.content = "HelloWorldMinimal.x3d"
meta2.name = "title"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.content = "Hello World minimal example scene."
meta3.name = "description"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "Don Brutzman"
meta4.name = "creator"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "19 January 2020"
meta5.name = "created"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "24 January 2020"
meta6.name = "modified"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "https://helloworldcollection.de"
meta7.name = "reference"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "https://en.wiktionary.org/wiki/Hello_World"
meta8.name = "reference"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "https://en.wikipedia.org/wiki/%22Hello,%20World!%22_program"
meta9.name = "reference"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "https://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world"
meta10.name = "reference"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.content = "https://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world#X3D_(Extensible_3D)"
meta11.name = "reference"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes"
meta12.name = "reference"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes/HelloWorldMinimalIndex.html"
meta13.name = "reference"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes/HelloWorldMinimal.x3d"
meta14.name = "identifier"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta15.name = "generator"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.content = "../license.html"
meta16.name = "license"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
WorldInfo18 = x3d.WorldInfo()
WorldInfo18.title = "HelloWorldMinimal.x3d"

Scene17.children.append(WorldInfo18)
Shape19 = x3d.Shape()
Text20 = x3d.Text()
Text20.string = ["hello, world"]

Shape19.geometry = Text20

Scene17.children.append(Shape19)

X3D0.Scene = Scene17
f = open("HelloWorldMinimal_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
