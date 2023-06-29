print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "HAnim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "JohnBoy.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "identifier"
meta4.content = "http://www.web3d.org/x3d/content/examples/HumanoidAnimation/JohnBoy.x3d"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "description"
meta5.content = "An attempt at a standard LOA-4 skeleton"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "generator"
meta6.content = "h.pl"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "creator"
meta7.content = "John Carlson"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "created"
meta8.content = "12 June 2020"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "license"
meta9.content = "../license.html"

head1.children.append(meta9)

X3D0.head = head1
Scene10 = x3d.Scene()
NavigationInfo11 = x3d.NavigationInfo()
NavigationInfo11.speed = 1.5

Scene10.children.append(NavigationInfo11)
Viewpoint12 = x3d.Viewpoint()
Viewpoint12.centerOfRotation = [0,1,0]
Viewpoint12.description = "JohnBoy"
Viewpoint12.position = [0,1,3]

Scene10.children.append(Viewpoint12)

X3D0.Scene = Scene10
f = open("././skeleton_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
