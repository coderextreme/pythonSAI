print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.content = "ArchHalf.x3d"
meta2.name = "title"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.content = "Create a half arch with parameters clearSpanWidth=4; riseHeight=2; depth=3; topAbutmentHeight=0.5; pierWidth=0.5; pierHeight=1. Parameter clearSpanWidth measure refers to a full arc, consider clearSpanWidth/2 for the archHalf width. Modify them with Transform > scale or editing the IndexedFileSet node. See the reference file ArchModelingDiagrams.pdf and the ArchScript_more_readable.js script to find further information."
meta3.name = "description"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "Michele Foti, Don Brutzman"
meta4.name = "creator"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "15 December 2014"
meta5.name = "created"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "16 February 2016"
meta6.name = "modified"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "ArchModelingDiagrams.pdf"
meta7.name = "reference"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "https://en.wikipedia.org/wiki/Arch"
meta8.name = "reference"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "http://X3dGraphics.com/examples/X3dForAdvancedModeling/Buildings/ArchHalf.x3d"
meta9.name = "identifier"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta10.name = "generator"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.content = "../license.html"
meta11.name = "license"

head1.children.append(meta11)

X3D0.head = head1
Scene12 = x3d.Scene()
Shape13 = x3d.Shape()
Shape13.DEF = "Arch"
""" note that convex='false' (meaning concave geometry) is crucial for this IFS of a geometric chord to render properly """
IndexedFaceSet14 = x3d.IndexedFaceSet()
IndexedFaceSet14.DEF = "ArchIndex"
IndexedFaceSet14.convex = False
IndexedFaceSet14.coordIndex = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,144,-1,149,31,144,147,-1,134,147,144,145,-1,145,144,62,141,-1,132,133,141,62,-1,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,143,-1,148,94,143,146,-1,142,128,146,143,-1,140,125,143,142,-1,125,126,127,140,-1,31,94,95,32,-1,32,95,96,33,-1,33,96,97,34,-1,34,97,98,35,-1,35,98,99,36,-1,36,99,100,37,-1,37,100,101,38,-1,38,101,102,39,-1,39,102,103,40,-1,40,103,104,41,-1,41,104,105,42,-1,42,105,106,43,-1,43,106,107,44,-1,44,107,108,45,-1,45,108,109,46,-1,46,109,110,47,-1,47,110,111,48,-1,48,111,112,49,-1,49,112,113,50,-1,50,113,114,51,-1,51,114,115,52,-1,52,115,116,53,-1,53,116,117,54,-1,54,117,118,55,-1,55,118,119,56,-1,56,119,120,57,-1,57,120,121,58,-1,58,121,122,59,-1,59,122,123,60,-1,60,123,124,61,-1,61,124,125,62,-1,148,149,147,146,-1,146,147,134,128,-1,128,134,145,142,-1,140,141,145,142,-1,127,133,141,140,-1,127,126,132,133,-1,126,132,62,125,-1,31,94,143,144,-1,142,143,144,145,-1,140,125,62,141,-1,31,94,148,149,-1]
IndexedFaceSet14.creaseAngle = 0
IndexedFaceSet14.solid = False
Coordinate15 = x3d.Coordinate()
Coordinate15.DEF = "ArchChord"

IndexedFaceSet14.coord = Coordinate15

Shape13.geometry = IndexedFaceSet14
Appearance16 = x3d.Appearance()
Material17 = x3d.Material()
Material17.DEF = "MaterialNode"
Material17.diffuseColor = [1,0.75,0.25]

Appearance16.material = Material17

Shape13.appearance = Appearance16

Scene12.children.append(Shape13)

X3D0.Scene = Scene12
f = open("ArchHalf_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
