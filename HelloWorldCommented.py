print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.content = "HelloWorldCommented.x3d"
meta2.name = "title"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.content = "Numerous comments added to simple X3D scene example for testing JSON encoding alternatives."
meta3.name = "description"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "19 December 2015"
meta4.name = "created"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "20 October 2019"
meta5.name = "modified"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "Don Brutzman"
meta6.name = "creator"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "HelloWorldCommented.json is most current, HelloWorldCommentedOriginalEncoding.json and HelloWorldCommentedAlternativeEncoding.json were experimental."
meta7.name = "info"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "HelloWorldCommented.json"
meta8.name = "reference"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "HelloWorldCommentedOriginalEncoding.json"
meta9.name = "reference"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "HelloWorldCommentedAlternativeEncoding.json"
meta10.name = "reference"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes/HelloWorldCommented.x3d"
meta11.name = "identifier"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.content = "https://www.web3d.org/x3d/content/examples/license.html"
meta12.name = "license"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta13.name = "generator"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
""" Example scene to illustrate comments interspersed among X3D nodes and fields (XML elements and attributes) """
""" WorldInfo begin """
WorldInfo15 = x3d.WorldInfo()
WorldInfo15.title = "Hello world!"

Scene14.children.append(WorldInfo15)
""" WorldInfo complete, Group begin """
Group16 = x3d.Group()
""" Viewpoint begin """
Viewpoint17 = x3d.Viewpoint()
Viewpoint17.DEF = "ViewUpClose"
Viewpoint17.centerOfRotation = [0,-1,0]
Viewpoint17.description = "Hello world!"
Viewpoint17.position = [0,-1,7]

Group16.children.append(Viewpoint17)
""" Viewpoint complete, Transform begin """
Transform18 = x3d.Transform()
Transform18.rotation = [0,1,0,3]
""" Shape begin """
Shape19 = x3d.Shape()
""" Sphere begin """
Sphere20 = x3d.Sphere()

Shape19.geometry = Sphere20
""" Sphere complete, Appearance begin """
Appearance21 = x3d.Appearance()
""" Material begin """
Material22 = x3d.Material()
Material22.DEF = "MaterialLightBlue"
Material22.diffuseColor = [0.1,0.5,1]

Appearance21.material = Material22
""" Material complete, ImageTexture begin """
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.DEF = "ImageCloudlessEarth"
ImageTexture23.url = ["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","https://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","https://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"]

Appearance21.texture = ImageTexture23
""" ImageTexture complete """

Shape19.appearance = Appearance21
""" Appearance complete """

Transform18.children.append(Shape19)
""" Shape complete """

Group16.children.append(Transform18)
""" Transform complete, Transform begin """
Transform24 = x3d.Transform()
Transform24.translation = [0,-2,0]
""" Shape begin """
Shape25 = x3d.Shape()
""" Text begin """
Text26 = x3d.Text()
Text26.DEF = "TextMessage"
Text26.string = ["Hello","world!"]
""" FontStyle begin """
FontStyle27 = x3d.FontStyle()
FontStyle27.justify = ["MIDDLE","MIDDLE"]

Text26.fontStyle = FontStyle27
""" FontStyle complete """

Shape25.geometry = Text26
""" Text complete, Appearance begin """
Appearance28 = x3d.Appearance()
""" Material begin """
Material29 = x3d.Material()
Material29.USE = "MaterialLightBlue"

Appearance28.material = Material29
""" Material complete """

Shape25.appearance = Appearance28
""" Appearance complete """

Transform24.children.append(Shape25)
""" Shape complete """

Group16.children.append(Transform24)
""" Transform complete """

Scene14.children.append(Group16)
""" Group complete """

X3D0.Scene = Scene14
f = open("HelloWorldCommented_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
