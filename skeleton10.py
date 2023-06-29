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
meta6.content = "h2.pl"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "creator"
meta7.content = "John Carlson"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "created"
meta8.content = "9 November 2020"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "license"
meta9.content = "../license.html"

head1.children.append(meta9)

X3D0.head = head1
Scene10 = x3d.Scene()
Transform11 = x3d.Transform()
#DEF for markerfor XYZ axes
Shape12 = x3d.Shape()
Shape12.DEF = "AxisLinesShape"
#RGB lines showing XYZ axes
IndexedLineSet13 = x3d.IndexedLineSet()
IndexedLineSet13.colorIndex = [0,1,2]
IndexedLineSet13.colorPerVertex = False
IndexedLineSet13.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate14 = x3d.Coordinate()
Coordinate14.point = (0.0000,0.0000,0.0000,0.1000,0.0000,0.0000,0.0000,0.1000,0.0000,0.0000,0.0000,0.1000)

IndexedLineSet13.coord = Coordinate14
Color15 = x3d.Color()
Color15.color = [1,0,0,0,0.6,0,0,0,1]

IndexedLineSet13.color = Color15

Shape12.geometry = IndexedLineSet13

Transform11.children.append(Shape12)

Scene10.children.append(Transform11)
Group16 = x3d.Group()
#DEFS for markers of skeleton joints, segments, and sites
Transform17 = x3d.Transform()
Transform18 = x3d.Transform()
Transform18.translation = [0,2,0]
Shape19 = x3d.Shape()
Shape19.DEF = "HAnimRootShape"
Sphere20 = x3d.Sphere()
Sphere20.radius = 0.02

Shape19.geometry = Sphere20
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.DEF = "HAnimRootMaterial"
Material22.diffuseColor = [0.8,0,0]
Material22.transparency = 0.3

Appearance21.material = Material22

Shape19.appearance = Appearance21

Transform18.children.append(Shape19)

Transform17.children.append(Transform18)
Transform23 = x3d.Transform()
Transform23.translation = [0,2.1,0]
Shape24 = x3d.Shape()
Shape24.DEF = "HAnimJointShape"
Sphere25 = x3d.Sphere()
Sphere25.radius = 0.02

Shape24.geometry = Sphere25
Appearance26 = x3d.Appearance()
Material27 = x3d.Material()
Material27.DEF = "HAnimJointMaterial"
Material27.diffuseColor = [0,0,0.8]
Material27.transparency = 0.3

Appearance26.material = Material27

Shape24.appearance = Appearance26

Transform23.children.append(Shape24)

Transform17.children.append(Transform23)
Transform28 = x3d.Transform()
Transform28.translation = [0,2.05,0]
Shape29 = x3d.Shape()
Shape29.DEF = "HAnimSegmentLine"
LineSet30 = x3d.LineSet()
LineSet30.vertexCount = [2]
ColorRGBA31 = x3d.ColorRGBA()
ColorRGBA31.DEF = "HAnimSegmentLineColorRGBA"
ColorRGBA31.color = [1,1,0,1,1,1,0,0.1]

LineSet30.color = ColorRGBA31
Coordinate32 = x3d.Coordinate()
Coordinate32.point = (-0.0500,0.0000,0.0000,0.0500,0.0000,0.0000)

LineSet30.coord = Coordinate32

Shape29.geometry = LineSet30

Transform28.children.append(Shape29)

Transform17.children.append(Transform28)
Transform33 = x3d.Transform()
Transform33.translation = [0,2.1,0]
Shape34 = x3d.Shape()
Shape34.DEF = "HAnimSiteShape"
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.DEF = "DiamondIFS"
IndexedFaceSet35.creaseAngle = 0.5
IndexedFaceSet35.solid = False
IndexedFaceSet35.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA36 = x3d.ColorRGBA()
ColorRGBA36.DEF = "HAnimSiteColorRGBA"
ColorRGBA36.color = [1,1,0,1,1,1,0,0.1]

IndexedFaceSet35.color = ColorRGBA36
Coordinate37 = x3d.Coordinate()
Coordinate37.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

IndexedFaceSet35.coord = Coordinate37

Shape34.geometry = IndexedFaceSet35
Appearance38 = x3d.Appearance()
Material39 = x3d.Material()
Material39.diffuseColor = [1,1,0]
Material39.transparency = 0.3

Appearance38.material = Material39

Shape34.appearance = Appearance38

Transform33.children.append(Shape34)

Transform17.children.append(Transform33)

Group16.children.append(Transform17)

Scene10.children.append(Group16)
NavigationInfo40 = x3d.NavigationInfo()
NavigationInfo40.speed = 1.5

Scene10.children.append(NavigationInfo40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.description = "default"

Scene10.children.append(Viewpoint41)

X3D0.Scene = Scene10
f = open("././skeleton10_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
