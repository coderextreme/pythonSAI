print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "creator"
meta2.content = "Carlson, I"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "Carlson, II"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Carlson, III"

head1.children.append(meta4)

X3D0.head = head1
Scene5 = x3d.Scene()
Group6 = x3d.Group()
Shape7 = x3d.Shape()
Appearance8 = x3d.Appearance()
Material9 = x3d.Material()
Material9.diffuseColor = [1,0,0]

Appearance8.material = Material9

Shape7.appearance = Appearance8
Box10 = x3d.Box()

Shape7.geometry = Box10

Group6.children.append(Shape7)

Scene5.children.append(Group6)
Transform11 = x3d.Transform()
Transform11.rotation = [7,8,9,3.14]
Transform11.scale = [4,5,6]
Transform11.translation = [1,2,3]

Scene5.children.append(Transform11)

X3D0.Scene = Scene5
f = open("././app_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
