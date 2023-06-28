print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "sphere.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "John Carlson"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "generator"
meta4.content = "manual"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/sphere.x3d"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "description"
meta6.content = "a sphere"

head1.children.append(meta6)

X3D0.head = head1
Scene7 = x3d.Scene()
Group8 = x3d.Group()
Shape9 = x3d.Shape()
Appearance10 = x3d.Appearance()
Material11 = x3d.Material()
Material11.diffuseColor = [1,1,1]

Appearance10.material = Material11

Shape9.appearance = Appearance10
Sphere12 = x3d.Sphere()

Shape9.geometry = Sphere12

Group8.children.append(Shape9)

Scene7.children.append(Group8)

X3D0.Scene = Scene7
f = open("././sphere_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
