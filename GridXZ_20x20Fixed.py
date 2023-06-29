print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "GridXZ_20x20Fixed.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "MV4204 class"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "created"
meta4.content = "3 September 2000"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "modified"
meta5.content = "30 March 2016"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "reference"
meta6.content = "GridXY_20x20Fixed.x3d"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "GridYZ_20x20Fixed.x3d"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "description"
meta8.content = "Line grid authoring tool to enable precise visual measurement of objects in 3D space - fixed position. Oriented along XZ plane, size 20m by 20m, default block size 1m by 1m."

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "identifier"
meta9.content = "https://savage.nps.edu/Savage/Tools/Authoring/GridXZ_20x20Fixed.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "generator"
meta10.content = "X3D-Edit 3.2, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "license"
meta11.content = "../../license.html"

head1.children.append(meta11)

X3D0.head = head1
Scene12 = x3d.Scene()
Viewpoint13 = x3d.Viewpoint()
Viewpoint13.description = "XZ horizontal grid, perpendicular to Y axis (seen from 0 10 25)"
Viewpoint13.orientation = [1,0,0,-0.4]
Viewpoint13.position = [0,10,25]

Scene12.children.append(Viewpoint13)
Transform14 = x3d.Transform()
Transform14.DEF = "GridLocation"
Group15 = x3d.Group()
Shape16 = x3d.Shape()
Shape16.DEF = "LinesAlignedAlongZ"
IndexedLineSet17 = x3d.IndexedLineSet()
IndexedLineSet17.colorIndex = [1,0,0,0,0,2,0,0,0,0,1,0,0,0,0,2,0,0,0,0,1]
IndexedLineSet17.colorPerVertex = False
IndexedLineSet17.coordIndex = [1,22,-1,2,23,-1,3,24,-1,4,25,-1,5,26,-1,6,27,-1,7,28,-1,8,29,-1,9,30,-1,10,31,-1,11,32,-1,12,33,-1,13,34,-1,14,35,-1,15,36,-1,16,37,-1,17,38,-1,18,39,-1,19,40,-1,20,41,-1,21,42,-1]
Coordinate18 = x3d.Coordinate()
Coordinate18.DEF = "EndPoints"
Coordinate18.point = (0.0000,0.0000,0.0000,-10.0000,0.0000,10.0000,-9.0000,0.0000,10.0000,-8.0000,0.0000,10.0000,-7.0000,0.0000,10.0000,-6.0000,0.0000,10.0000,-5.0000,0.0000,10.0000,-4.0000,0.0000,10.0000,-3.0000,0.0000,10.0000,-2.0000,0.0000,10.0000,-1.0000,0.0000,10.0000,0.0000,0.0000,10.0000,1.0000,0.0000,10.0000,2.0000,0.0000,10.0000,3.0000,0.0000,10.0000,4.0000,0.0000,10.0000,5.0000,0.0000,10.0000,6.0000,0.0000,10.0000,7.0000,0.0000,10.0000,8.0000,0.0000,10.0000,9.0000,0.0000,10.0000,10.0000,0.0000,10.0000,-10.0000,0.0000,-10.0000,-9.0000,0.0000,-10.0000,-8.0000,0.0000,-10.0000,-7.0000,0.0000,-10.0000,-6.0000,0.0000,-10.0000,-5.0000,0.0000,-10.0000,-4.0000,0.0000,-10.0000,-3.0000,0.0000,-10.0000,-2.0000,0.0000,-10.0000,-1.0000,0.0000,-10.0000,0.0000,0.0000,-10.0000,1.0000,0.0000,-10.0000,2.0000,0.0000,-10.0000,3.0000,0.0000,-10.0000,4.0000,0.0000,-10.0000,5.0000,0.0000,-10.0000,6.0000,0.0000,-10.0000,7.0000,0.0000,-10.0000,8.0000,0.0000,-10.0000,9.0000,0.0000,-10.0000,10.0000,0.0000,-10.0000)

IndexedLineSet17.coord = Coordinate18
Color19 = x3d.Color()
Color19.color = [0.4,0.4,0.4,0.8,0.2,0,0.4,0.1,0.05]

IndexedLineSet17.color = Color19

Shape16.geometry = IndexedLineSet17

Group15.children.append(Shape16)
Transform20 = x3d.Transform()
Transform20.DEF = "LinesAlignedAlongX"
Transform20.rotation = [0,1,0,1.57079]
Shape21 = x3d.Shape()
Shape21.USE = "LinesAlignedAlongZ"

Transform20.children.append(Shape21)

Group15.children.append(Transform20)
Transform22 = x3d.Transform()
Transform22.translation = [0,-0.5,0]
Billboard23 = x3d.Billboard()
Shape24 = x3d.Shape()
Text25 = x3d.Text()
Text25.DEF = "CenterTextNode"
Text25.string = ["origin"]
FontStyle26 = x3d.FontStyle()
FontStyle26.DEF = "FS4"
FontStyle26.justify = ["MIDDLE","MIDDLE"]
FontStyle26.size = 0.4

Text25.fontStyle = FontStyle26

Shape24.geometry = Text25
Appearance27 = x3d.Appearance()
Appearance27.DEF = "DefaultAppearance"
Material28 = x3d.Material()

Appearance27.material = Material28

Shape24.appearance = Appearance27

Billboard23.children.append(Shape24)

Transform22.children.append(Billboard23)

Group15.children.append(Transform22)
Transform29 = x3d.Transform()
Transform29.translation = [10,-0.5,10]
Billboard30 = x3d.Billboard()
Shape31 = x3d.Shape()
Text32 = x3d.Text()
Text32.string = ["10 0 10"]
FontStyle33 = x3d.FontStyle()
FontStyle33.USE = "FS4"

Text32.fontStyle = FontStyle33

Shape31.geometry = Text32
Appearance34 = x3d.Appearance()
Appearance34.USE = "DefaultAppearance"

Shape31.appearance = Appearance34

Billboard30.children.append(Shape31)

Transform29.children.append(Billboard30)

Group15.children.append(Transform29)
Transform35 = x3d.Transform()
Transform35.translation = [10,-0.5,-10]
Billboard36 = x3d.Billboard()
Shape37 = x3d.Shape()
Text38 = x3d.Text()
Text38.string = ["10 0 -10"]
FontStyle39 = x3d.FontStyle()
FontStyle39.USE = "FS4"

Text38.fontStyle = FontStyle39

Shape37.geometry = Text38
Appearance40 = x3d.Appearance()
Appearance40.USE = "DefaultAppearance"

Shape37.appearance = Appearance40

Billboard36.children.append(Shape37)

Transform35.children.append(Billboard36)

Group15.children.append(Transform35)
Transform41 = x3d.Transform()
Transform41.translation = [-10,-0.5,10]
Billboard42 = x3d.Billboard()
Shape43 = x3d.Shape()
Text44 = x3d.Text()
Text44.string = ["-10 0 10"]
FontStyle45 = x3d.FontStyle()
FontStyle45.USE = "FS4"

Text44.fontStyle = FontStyle45

Shape43.geometry = Text44
Appearance46 = x3d.Appearance()
Appearance46.USE = "DefaultAppearance"

Shape43.appearance = Appearance46

Billboard42.children.append(Shape43)

Transform41.children.append(Billboard42)

Group15.children.append(Transform41)
Transform47 = x3d.Transform()
Transform47.translation = [-10,-0.5,-10]
Billboard48 = x3d.Billboard()
Shape49 = x3d.Shape()
Text50 = x3d.Text()
Text50.string = ["-10 0 -10"]
FontStyle51 = x3d.FontStyle()
FontStyle51.USE = "FS4"

Text50.fontStyle = FontStyle51

Shape49.geometry = Text50
Appearance52 = x3d.Appearance()
Appearance52.USE = "DefaultAppearance"

Shape49.appearance = Appearance52

Billboard48.children.append(Shape49)

Transform47.children.append(Billboard48)

Group15.children.append(Transform47)

Transform14.children.append(Group15)

Scene12.children.append(Transform14)

X3D0.Scene = Scene12
f = open("././GridXZ_20x20Fixed_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
