print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.content = "Carlson, I"
meta2.name = "creator"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.content = "Carlson, II"
meta3.name = "creator"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "Carlson, III"
meta4.name = "creator"

head1.children.append(meta4)

X3D0.head = head1
Scene5 = x3d.Scene()
Group6 = x3d.Group()
Group6.bboxCenter = [0,0,0]
Group6.bboxSize = [-1,-1,-1]
Group6.visible = True
Shape7 = x3d.Shape()
Shape7.bboxCenter = [0,0,0]
Shape7.bboxSize = [-1,-1,-1]
Shape7.visible = True
Appearance8 = x3d.Appearance()
Material9 = x3d.Material()
Material9.ambientIntensity = 0.2
Material9.diffuseColor = [1,0,0]
Material9.emissiveColor = [0,0,0]
Material9.shininess = 0.2
Material9.specularColor = [0,0,0]
Material9.transparency = 0

Appearance8.material = Material9

Shape7.appearance = Appearance8
Box10 = x3d.Box()
Box10.size = [2,2,2]
Box10.solid = True

Shape7.geometry = Box10

Group6.children.append(Shape7)

Scene5.children.append(Group6)
Transform11 = x3d.Transform()
Transform11.bboxCenter = [0,0,0]
Transform11.bboxSize = [-1,-1,-1]
Transform11.center = [0,0,0]
Transform11.rotation = [7,8,9,3.14]
Transform11.scale = [4,5,6]
Transform11.scaleOrientation = [0,0,1,0]
Transform11.translation = [1,2,3]
Transform11.visible = True

Scene5.children.append(Transform11)

X3D0.Scene = Scene5
f = open("app_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
