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
meta7.name = "modified"
meta7.content = "14 Jan 2023"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "creator"
meta8.content = "John Carlson"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "created"
meta9.content = "9 November 2020"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "license"
meta10.content = "../license.html"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
Transform12 = x3d.Transform()
#DEF for markerfor XYZ axes
Shape13 = x3d.Shape()
Shape13.DEF = "AxisLinesShape"
#RGB lines showing XYZ axes
IndexedLineSet14 = x3d.IndexedLineSet()
IndexedLineSet14.colorIndex = [0,1,2]
IndexedLineSet14.colorPerVertex = False
IndexedLineSet14.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate15 = x3d.Coordinate()

IndexedLineSet14.coord = Coordinate15
Color16 = x3d.Color()

IndexedLineSet14.color = Color16

Shape13.geometry = IndexedLineSet14

Transform12.children.append(Shape13)

Scene11.children.append(Transform12)
Group17 = x3d.Group()
#DEFS for markers of skeleton joints, segments, and sites
Transform18 = x3d.Transform()
Transform19 = x3d.Transform()
Transform19.translation = [0,2,0]
Shape20 = x3d.Shape()
Shape20.DEF = "HAnimRootShape"
Sphere21 = x3d.Sphere()
Sphere21.radius = 0.02

Shape20.geometry = Sphere21
Appearance22 = x3d.Appearance()
Material23 = x3d.Material()
Material23.DEF = "HAnimRootMaterial"
Material23.diffuseColor = [0.8,0,0]
Material23.transparency = 0.3

Appearance22.material = Material23

Shape20.appearance = Appearance22

Transform19.children.append(Shape20)

Transform18.children.append(Transform19)
Transform24 = x3d.Transform()
Transform24.translation = [0,2.1,0]
Shape25 = x3d.Shape()
Shape25.DEF = "HAnimJointShape"
Sphere26 = x3d.Sphere()
Sphere26.radius = 0.02

Shape25.geometry = Sphere26
Appearance27 = x3d.Appearance()
Material28 = x3d.Material()
Material28.DEF = "HAnimJointMaterial"
Material28.diffuseColor = [0,0,0.8]
Material28.transparency = 0.3

Appearance27.material = Material28

Shape25.appearance = Appearance27

Transform24.children.append(Shape25)

Transform18.children.append(Transform24)
Transform29 = x3d.Transform()
Transform29.translation = [0,2.05,0]
Shape30 = x3d.Shape()
Shape30.DEF = "HAnimSegmentLine"
LineSet31 = x3d.LineSet()
LineSet31.vertexCount = [2]
ColorRGBA32 = x3d.ColorRGBA()
ColorRGBA32.DEF = "HAnimSegmentLineColorRGBA"

LineSet31.color = ColorRGBA32
Coordinate33 = x3d.Coordinate()

LineSet31.coord = Coordinate33

Shape30.geometry = LineSet31

Transform29.children.append(Shape30)

Transform18.children.append(Transform29)
Transform34 = x3d.Transform()
Transform34.translation = [0,2.1,0]
Shape35 = x3d.Shape()
Shape35.DEF = "HAnimSiteShape"
IndexedFaceSet36 = x3d.IndexedFaceSet()
IndexedFaceSet36.DEF = "DiamondIFS"
IndexedFaceSet36.creaseAngle = 0.5
IndexedFaceSet36.solid = False
IndexedFaceSet36.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA37 = x3d.ColorRGBA()
ColorRGBA37.DEF = "HAnimSiteColorRGBA"

IndexedFaceSet36.color = ColorRGBA37
Coordinate38 = x3d.Coordinate()

IndexedFaceSet36.coord = Coordinate38

Shape35.geometry = IndexedFaceSet36
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.diffuseColor = [1,1,0]
Material40.transparency = 0.3

Appearance39.material = Material40

Shape35.appearance = Appearance39

Transform34.children.append(Shape35)

Transform18.children.append(Transform34)

Group17.children.append(Transform18)

Scene11.children.append(Group17)
NavigationInfo41 = x3d.NavigationInfo()
NavigationInfo41.speed = 1.5

Scene11.children.append(NavigationInfo41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.description = "default"

Scene11.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.name = "HAnim"
HAnimHumanoid43.DEF = "hanim_HAnim"
HAnimHumanoid43.info = ["humanoidVersion=2.0"]
HAnimHumanoid43.version = "2.0"
#<LOD containerField='skin'> (Switch whichChoice='0' and LOD parents each already work in view3dscene)
#</LOD>
Shape44 = x3d.Shape()
Shape44.DEF = "SkinShape"
IndexedFaceSet45 = x3d.IndexedFaceSet()
IndexedFaceSet45.coordIndex = [0,9,5,-1,0,7,9,-1,0,5,1,-1,1,5,2,-1,1,3,7,-1,2,4,3,-1,0,1,7,-1,1,2,3,-1,5,6,2,-1,7,3,8,-1,6,4,2,-1,3,4,8,-1,9,6,5,-1,9,7,8,-1,4,6,10,-1,4,10,12,-1,4,12,8,-1,10,11,12,-1,9,75,24,-1,9,24,74,-1,9,8,75,-1,9,74,6,-1,10,6,74,-1,12,75,8,-1,74,24,29,-1,24,77,29,-1,10,74,29,-1,77,32,29,-1,32,78,29,-1,78,30,29,-1,30,10,29,-1,41,24,75,-1,41,75,12,-1,41,12,42,-1,41,42,80,-1,41,80,44,-1,41,44,79,-1,41,79,24,-1,81,24,79,-1,81,77,24,-1,81,25,77,-1,81,79,25,-1,25,79,44,-1,25,32,77,-1,25,83,32,-1,25,26,83,-1,25,27,26,-1,25,84,27,-1,25,44,84,-1,11,10,30,-1,11,30,13,-1,11,13,15,-1,11,15,14,-1,11,14,42,-1,11,42,12,-1,15,13,16,-1,15,18,14,-1,15,16,76,-1,15,76,18,-1,76,16,17,-1,76,17,82,-1,76,82,19,-1,76,19,18,-1,22,18,19,-1,22,87,18,-1,22,27,84,-1,22,84,87,-1,87,84,85,-1,85,84,44,-1,85,42,14,-1,87,14,18,-1,87,85,14,-1,20,83,26,-1,20,17,16,-1,20,16,88,-1,20,88,83,-1,88,16,13,-1,88,13,86,-1,88,86,83,-1,86,13,30,-1,86,32,83,-1,23,89,22,-1,89,27,22,-1,89,91,27,-1,91,26,27,-1,91,20,26,-1,21,20,91,-1,21,17,20,-1,21,92,17,-1,82,17,92,-1,82,90,19,-1,23,22,19,-1,23,19,90,-1,82,92,101,-1,82,101,99,-1,82,99,93,-1,82,93,95,-1,82,95,97,-1,82,97,90,-1,23,90,97,-1,23,97,94,-1,23,94,89,-1,89,94,96,-1,89,96,95,-1,89,95,93,-1,89,93,91,-1,91,93,99,-1,91,99,100,-1,91,100,98,-1,21,91,98,-1,21,98,101,-1,21,101,92,-1,85,105,42,-1,85,103,105,-1,85,44,103,-1,103,44,104,-1,80,42,105,-1,80,105,102,-1,80,102,104,-1,80,104,44,-1,105,109,102,-1,102,109,47,-1,47,104,102,-1,104,47,45,-1,104,45,103,-1,103,45,46,-1,103,46,109,-1,103,109,105,-1,109,112,110,-1,109,110,47,-1,47,110,111,-1,47,111,45,-1,45,111,113,-1,113,46,45,-1,46,113,112,-1,112,109,46,-1,112,118,110,-1,110,118,115,-1,110,115,111,-1,111,115,117,-1,111,117,113,-1,113,117,116,-1,113,116,112,-1,112,116,118,-1,115,118,119,-1,119,118,122,-1,118,116,122,-1,122,116,120,-1,116,117,120,-1,120,117,121,-1,117,115,121,-1,115,119,121,-1,119,127,123,-1,119,122,127,-1,122,126,127,-1,122,128,126,-1,122,120,128,-1,120,124,128,-1,120,121,124,-1,121,125,124,-1,121,119,125,-1,119,123,125,-1,127,129,123,-1,127,126,129,-1,129,126,141,-1,141,126,143,-1,126,142,143,-1,126,128,142,-1,128,124,130,-1,142,128,130,-1,124,132,130,-1,124,134,132,-1,125,134,124,-1,125,136,134,-1,125,137,136,-1,125,135,137,-1,125,133,135,-1,125,123,133,-1,123,131,133,-1,123,129,131,-1,131,129,138,-1,129,141,138,-1,138,141,144,-1,141,143,144,-1,143,146,144,-1,142,146,143,-1,142,145,146,-1,139,145,142,-1,130,139,142,-1,139,130,132,-1,139,132,154,-1,132,157,154,-1,132,159,157,-1,132,134,159,-1,134,136,159,-1,136,161,159,-1,136,137,161,-1,137,162,161,-1,160,162,137,-1,135,160,137,-1,133,160,135,-1,133,158,160,-1,131,158,133,-1,156,158,131,-1,153,156,131,-1,131,138,153,-1,138,155,153,-1,140,155,138,-1,138,144,140,-1,144,147,140,-1,140,147,145,-1,140,145,139,-1,139,155,140,-1,154,155,139,-1,146,149,144,-1,146,151,149,-1,145,151,146,-1,150,151,145,-1,145,152,150,-1,147,152,145,-1,147,149,152,-1,147,144,149,-1,148,149,151,-1,148,152,149,-1,148,150,152,-1,148,151,150,-1,160,207,162,-1,160,205,207,-1,165,208,205,-1,160,165,205,-1,158,165,160,-1,161,162,207,-1,161,207,206,-1,165,206,208,-1,206,165,161,-1,161,165,159,-1,207,209,211,-1,205,209,207,-1,205,212,209,-1,205,208,212,-1,206,212,208,-1,206,210,212,-1,206,207,210,-1,207,211,210,-1,209,212,213,-1,212,216,213,-1,212,214,216,-1,210,214,212,-1,210,215,214,-1,210,211,215,-1,209,215,211,-1,209,213,215,-1,217,213,216,-1,217,215,213,-1,217,214,215,-1,217,216,214,-1,158,194,165,-1,192,194,158,-1,164,195,192,-1,158,164,192,-1,156,164,158,-1,159,194,165,-1,159,194,193,-1,159,193,195,-1,159,195,164,-1,159,164,157,-1,157,164,180,-1,192,198,194,-1,192,196,198,-1,192,195,196,-1,195,199,196,-1,196,199,200,-1,199,203,200,-1,193,199,195,-1,193,197,199,-1,193,198,197,-1,193,194,198,-1,199,201,203,-1,197,201,199,-1,197,198,201,-1,198,202,201,-1,196,202,198,-1,200,202,196,-1,204,202,200,-1,204,201,202,-1,204,203,201,-1,204,200,203,-1,156,181,164,-1,156,179,181,-1,156,182,179,-1,156,163,182,-1,163,180,182,-1,157,180,163,-1,164,181,180,-1,179,182,183,-1,182,186,183,-1,182,184,186,-1,180,184,182,-1,180,181,184,-1,181,185,184,-1,179,185,181,-1,183,185,179,-1,183,186,187,-1,186,190,187,-1,184,190,186,-1,184,188,190,-1,184,185,188,-1,185,189,188,-1,185,183,189,-1,183,187,189,-1,191,189,187,-1,191,188,189,-1,191,190,188,-1,191,187,190,-1,153,163,156,-1,153,168,163,-1,153,166,168,-1,153,169,166,-1,155,169,153,-1,155,167,169,-1,154,167,155,-1,154,163,167,-1,154,157,163,-1,163,168,167,-1,166,169,170,-1,169,173,170,-1,169,171,173,-1,169,167,171,-1,167,168,171,-1,168,172,171,-1,168,170,172,-1,170,168,166,-1,170,173,174,-1,173,177,174,-1,173,175,177,-1,173,171,175,-1,171,172,175,-1,172,176,175,-1,172,174,176,-1,170,174,172,-1,178,176,174,-1,178,175,176,-1,178,177,175,-1,178,174,177,-1,86,30,221,-1,86,221,219,-1,86,219,32,-1,32,219,220,-1,78,32,220,-1,78,220,218,-1,78,218,221,-1,78,221,30,-1,221,225,219,-1,219,225,35,-1,35,33,219,-1,33,220,219,-1,33,34,220,-1,220,34,218,-1,221,218,34,-1,34,225,221,-1,225,226,228,-1,225,228,35,-1,35,228,229,-1,35,229,33,-1,33,229,227,-1,33,227,34,-1,34,227,226,-1,34,226,225,-1,226,234,228,-1,228,234,232,-1,232,229,228,-1,232,233,229,-1,229,233,227,-1,227,233,231,-1,227,231,226,-1,226,231,234,-1,231,235,234,-1,235,238,234,-1,234,238,232,-1,238,236,232,-1,232,236,233,-1,236,237,233,-1,233,237,231,-1,231,237,235,-1,235,239,243,-1,235,243,238,-1,238,243,242,-1,238,242,244,-1,238,244,236,-1,236,244,240,-1,236,240,237,-1,237,240,241,-1,237,241,235,-1,235,241,239,-1,243,239,245,-1,243,245,242,-1,245,257,242,-1,257,259,242,-1,242,259,258,-1,242,258,244,-1,244,246,240,-1,258,246,244,-1,240,246,248,-1,240,248,250,-1,241,240,250,-1,241,250,252,-1,241,252,253,-1,241,253,251,-1,241,251,249,-1,241,249,239,-1,239,249,247,-1,239,247,245,-1,247,254,245,-1,245,254,257,-1,254,260,257,-1,257,260,259,-1,259,260,262,-1,258,259,262,-1,258,262,261,-1,255,258,261,-1,246,258,255,-1,255,248,246,-1,255,270,248,-1,248,270,273,-1,248,273,275,-1,248,275,250,-1,250,275,252,-1,252,275,277,-1,252,277,253,-1,253,277,278,-1,276,253,278,-1,251,253,276,-1,249,251,276,-1,249,276,274,-1,247,249,274,-1,272,247,274,-1,269,247,272,-1,247,269,254,-1,254,269,271,-1,256,254,271,-1,254,256,260,-1,260,256,263,-1,256,261,263,-1,256,255,261,-1,255,256,271,-1,270,255,271,-1,262,260,265,-1,262,265,267,-1,261,262,267,-1,266,261,267,-1,261,266,268,-1,263,261,268,-1,263,268,265,-1,263,265,260,-1,264,267,265,-1,264,265,268,-1,264,268,266,-1,264,266,267,-1,276,278,323,-1,276,323,321,-1,281,321,324,-1,276,321,281,-1,274,276,281,-1,277,323,278,-1,277,322,323,-1,281,324,322,-1,322,277,281,-1,277,275,281,-1,323,327,325,-1,321,323,325,-1,321,325,328,-1,321,328,324,-1,322,324,328,-1,322,328,326,-1,322,326,323,-1,323,326,327,-1,325,329,328,-1,328,329,332,-1,328,332,330,-1,326,328,330,-1,326,330,331,-1,326,331,327,-1,325,327,331,-1,325,331,329,-1,333,332,329,-1,333,329,331,-1,333,331,330,-1,333,330,332,-1,274,281,310,-1,308,274,310,-1,280,308,311,-1,274,308,280,-1,272,274,280,-1,275,310,281,-1,275,309,310,-1,275,311,309,-1,275,280,311,-1,275,273,280,-1,273,296,280,-1,308,310,314,-1,308,314,312,-1,308,312,311,-1,311,312,315,-1,312,316,315,-1,315,316,319,-1,309,311,315,-1,309,315,313,-1,309,313,314,-1,309,314,310,-1,315,319,317,-1,313,315,317,-1,313,317,314,-1,314,317,318,-1,312,314,318,-1,316,312,318,-1,320,316,318,-1,320,318,317,-1,320,317,319,-1,320,319,316,-1,272,280,297,-1,272,297,295,-1,272,295,298,-1,272,298,279,-1,279,298,296,-1,273,279,296,-1,280,296,297,-1,295,299,298,-1,298,299,302,-1,298,302,300,-1,296,298,300,-1,296,300,297,-1,297,300,301,-1,295,297,301,-1,299,295,301,-1,299,303,302,-1,302,303,306,-1,300,302,306,-1,300,306,304,-1,300,304,301,-1,301,304,305,-1,301,305,299,-1,299,305,303,-1,307,303,305,-1,307,305,304,-1,307,304,306,-1,307,306,303,-1,269,272,279,-1,269,279,284,-1,269,284,282,-1,269,282,285,-1,271,269,285,-1,271,285,283,-1,270,271,283,-1,270,283,279,-1,270,279,273,-1,279,283,284,-1,282,286,285,-1,285,286,289,-1,285,289,287,-1,285,287,283,-1,283,287,284,-1,284,287,288,-1,284,288,286,-1,286,282,284,-1,286,290,289,-1,289,290,293,-1,289,293,291,-1,289,291,287,-1,287,291,288,-1,288,291,292,-1,288,292,290,-1,286,288,290,-1,294,290,292,-1,294,292,291,-1,294,291,293,-1,294,293,290,-1,97,334,336,-1,97,336,94,-1,94,336,96,-1,336,335,96,-1,96,335,95,-1,95,335,337,-1,95,337,334,-1,95,334,97,-1,334,341,336,-1,336,341,338,-1,336,338,335,-1,335,338,340,-1,335,340,337,-1,337,340,339,-1,337,339,334,-1,334,339,341,-1,341,345,342,-1,341,342,338,-1,338,342,340,-1,340,342,344,-1,340,344,339,-1,339,344,343,-1,339,343,345,-1,339,345,341,-1,345,349,342,-1,342,349,351,-1,342,351,346,-1,342,346,344,-1,71,346,348,-1,71,344,346,-1,71,348,347,-1,71,347,344,-1,344,347,343,-1,343,347,352,-1,343,352,349,-1,343,349,345,-1,349,352,356,-1,349,356,353,-1,349,353,355,-1,349,355,351,-1,354,356,352,-1,354,352,350,-1,354,350,351,-1,354,351,355,-1,353,356,357,-1,353,357,358,-1,353,358,359,-1,353,359,360,-1,353,360,361,-1,353,361,355,-1,354,357,356,-1,350,346,351,-1,348,346,347,-1,350,347,346,-1,350,352,347,-1,354,358,357,-1,354,359,358,-1,354,360,359,-1,354,361,360,-1,354,355,361,-1,101,362,365,-1,101,365,99,-1,99,365,100,-1,100,365,363,-1,100,363,98,-1,98,363,364,-1,98,364,101,-1,101,364,362,-1,362,369,367,-1,362,367,365,-1,365,367,363,-1,363,367,368,-1,363,367,368,-1,363,368,366,-1,363,366,364,-1,364,366,362,-1,362,366,369,-1,369,373,371,-1,369,371,367,-1,367,371,368,-1,368,371,372,-1,368,372,366,-1,366,372,370,-1,366,370,369,-1,369,370,373,-1,373,377,380,-1,373,380,375,-1,373,375,371,-1,371,375,372,-1,372,375,376,-1,372,376,374,-1,372,374,370,-1,370,374,379,-1,373,370,379,-1,373,379,377,-1,377,379,383,-1,377,383,381,-1,377,381,384,-1,377,384,380,-1,381,383,389,-1,381,389,388,-1,381,388,387,-1,381,387,386,-1,381,386,385,-1,381,385,384,-1,376,375,374,-1,378,379,374,-1,378,374,375,-1,378,375,380,-1,382,386,387,-1,382,387,388,-1,382,388,389,-1,382,389,383,-1,382,383,379,-1,382,379,378,-1,382,378,380,-1,382,380,384,-1,382,384,385,-1,382,385,386,-1]
IndexedFaceSet45.creaseAngle = 3.1
Coordinate46 = x3d.Coordinate()
Coordinate46.DEF = "TheSkinCoord"

IndexedFaceSet45.coord = Coordinate46
Color47 = x3d.Color()

IndexedFaceSet45.color = Color47

Shape44.geometry = IndexedFaceSet45
Appearance48 = x3d.Appearance()
Appearance48.DEF = "SkinAppearance"
ImageTexture49 = x3d.ImageTexture()
ImageTexture49.DEF = "zBlueSpiralBkg2"
ImageTexture49.description = "Blue Spiral Pattern"
ImageTexture49.url = ["zBlueSpiralBkg2.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Skin/zBlueSpiralBkg2.gif"]

Appearance48.texture = ImageTexture49
Material50 = x3d.Material()
Material50.DEF = "SkinMaterial"
Material50.ambientIntensity = 0.6
Material50.diffuseColor = [1,1,1]
Material50.shininess = 0.6
Material50.transparency = 0.2

Appearance48.material = Material50

Shape44.appearance = Appearance48

HAnimHumanoid43.skin.append(Shape44)
Coordinate51 = x3d.Coordinate()
Coordinate51.USE = "TheSkinCoord"

HAnimHumanoid43.skinCoord = Coordinate51
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.name = "humanoid_root"
HAnimJoint52.DEF = "hanim_humanoid_root"
HAnimJoint52.center = [0,0.824,0.0277]
HAnimJoint52.ulimit = [0,0,0]
HAnimJoint52.llimit = [0,0,0]
HAnimSegment53 = x3d.HAnimSegment()
HAnimSegment53.name = "sacrum"
HAnimSegment53.DEF = "hanim_sacrum"
Transform54 = x3d.Transform()
Transform54.translation = [0,0.824,0.0277]
Transform55 = x3d.Transform()
#Empty Transform
Shape56 = x3d.Shape()
Shape56.USE = "HAnimJointShape"

Transform55.children.append(Shape56)

Transform54.children.append(Transform55)

HAnimSegment53.children.append(Transform54)
Shape57 = x3d.Shape()
LineSet58 = x3d.LineSet()
LineSet58.vertexCount = [2]
Coordinate59 = x3d.Coordinate()

LineSet58.coord = Coordinate59
#from humanoid_root to sacroiliac vertices 2
ColorRGBA60 = x3d.ColorRGBA()
ColorRGBA60.USE = "HAnimSegmentLineColorRGBA"

LineSet58.color = ColorRGBA60

Shape57.geometry = LineSet58

HAnimSegment53.children.append(Shape57)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite61.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
TouchSensor62 = x3d.TouchSensor()
TouchSensor62.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite61.children.append(TouchSensor62)
Shape63 = x3d.Shape()
Shape63.USE = "HAnimSiteShape"

HAnimSite61.children.append(Shape63)

HAnimSegment53.children.append(HAnimSite61)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.name = "crotch_pt"
HAnimSite64.DEF = "hanim_crotch_pt"
HAnimSite64.translation = [0.0034,0.8266,0.0257]
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimSite crotch_pt"

HAnimSite64.children.append(TouchSensor65)
Shape66 = x3d.Shape()
Shape66.USE = "HAnimSiteShape"

HAnimSite64.children.append(Shape66)

HAnimSegment53.children.append(HAnimSite64)
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.name = "l_asis_pt"
HAnimSite67.DEF = "hanim_l_asis_pt"
HAnimSite67.translation = [0.0925,0.9983,0.1052]
TouchSensor68 = x3d.TouchSensor()
TouchSensor68.description = "HAnimSite l_asis_pt"

HAnimSite67.children.append(TouchSensor68)
Shape69 = x3d.Shape()
Shape69.USE = "HAnimSiteShape"

HAnimSite67.children.append(Shape69)

HAnimSegment53.children.append(HAnimSite67)
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.name = "l_iliocristale_pt"
HAnimSite70.DEF = "hanim_l_iliocristale_pt"
HAnimSite70.translation = [0.1612,1.0537,0.0008]
TouchSensor71 = x3d.TouchSensor()
TouchSensor71.description = "HAnimSite l_iliocristale_pt"

HAnimSite70.children.append(TouchSensor71)
Shape72 = x3d.Shape()
Shape72.USE = "HAnimSiteShape"

HAnimSite70.children.append(Shape72)

HAnimSegment53.children.append(HAnimSite70)
HAnimSite73 = x3d.HAnimSite()
HAnimSite73.name = "l_psis_pt"
HAnimSite73.DEF = "hanim_l_psis_pt"
HAnimSite73.translation = [0.0774,1.019,-0.1151]
TouchSensor74 = x3d.TouchSensor()
TouchSensor74.description = "HAnimSite l_psis_pt"

HAnimSite73.children.append(TouchSensor74)
Shape75 = x3d.Shape()
Shape75.USE = "HAnimSiteShape"

HAnimSite73.children.append(Shape75)

HAnimSegment53.children.append(HAnimSite73)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.name = "l_trochanterion_pt"
HAnimSite76.DEF = "hanim_l_trochanterion_pt"
HAnimSite76.translation = [0.1677,0.8336,0.0303]
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite l_trochanterion_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"

HAnimSite76.children.append(Shape78)

HAnimSegment53.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.name = "r_asis_pt"
HAnimSite79.DEF = "hanim_r_asis_pt"
HAnimSite79.translation = [-0.0887,1.0021,0.1112]
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite r_asis_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"

HAnimSite79.children.append(Shape81)

HAnimSegment53.children.append(HAnimSite79)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.name = "r_iliocristale_pt"
HAnimSite82.DEF = "hanim_r_iliocristale_pt"
HAnimSite82.translation = [-0.1525,1.0628,0.0035]
TouchSensor83 = x3d.TouchSensor()
TouchSensor83.description = "HAnimSite r_iliocristale_pt"

HAnimSite82.children.append(TouchSensor83)
Shape84 = x3d.Shape()
Shape84.USE = "HAnimSiteShape"

HAnimSite82.children.append(Shape84)

HAnimSegment53.children.append(HAnimSite82)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.name = "r_psis_pt"
HAnimSite85.DEF = "hanim_r_psis_pt"
HAnimSite85.translation = [-0.0716,1.019,-0.1138]
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite r_psis_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"

HAnimSite85.children.append(Shape87)

HAnimSegment53.children.append(HAnimSite85)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.name = "r_trochanterion_pt"
HAnimSite88.DEF = "hanim_r_trochanterion_pt"
HAnimSite88.translation = [-0.1689,0.8419,0.0352]
TouchSensor89 = x3d.TouchSensor()
TouchSensor89.description = "HAnimSite r_trochanterion_pt"

HAnimSite88.children.append(TouchSensor89)
Shape90 = x3d.Shape()
Shape90.USE = "HAnimSiteShape"

HAnimSite88.children.append(Shape90)

HAnimSegment53.children.append(HAnimSite88)
Shape91 = x3d.Shape()
LineSet92 = x3d.LineSet()
LineSet92.vertexCount = [2]
Coordinate93 = x3d.Coordinate()

LineSet92.coord = Coordinate93
#from humanoid_root to vl5 vertices 2
ColorRGBA94 = x3d.ColorRGBA()
ColorRGBA94.USE = "HAnimSegmentLineColorRGBA"

LineSet92.color = ColorRGBA94

Shape91.geometry = LineSet92

HAnimSegment53.children.append(Shape91)
HAnimSite95 = x3d.HAnimSite()
HAnimSite95.name = "navel_pt"
HAnimSite95.DEF = "hanim_navel_pt"
HAnimSite95.translation = [0.0069,1.0966,0.1017]
TouchSensor96 = x3d.TouchSensor()
TouchSensor96.description = "HAnimSite navel_pt"

HAnimSite95.children.append(TouchSensor96)
Shape97 = x3d.Shape()
Shape97.USE = "HAnimSiteShape"

HAnimSite95.children.append(Shape97)

HAnimSegment53.children.append(HAnimSite95)
HAnimSite98 = x3d.HAnimSite()
HAnimSite98.name = "waist_preferred_anterior_pt"
HAnimSite98.DEF = "hanim_waist_preferred_anterior_pt"
TouchSensor99 = x3d.TouchSensor()
TouchSensor99.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite98.children.append(TouchSensor99)
Shape100 = x3d.Shape()
Shape100.USE = "HAnimSiteShape"

HAnimSite98.children.append(Shape100)

HAnimSegment53.children.append(HAnimSite98)
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.name = "waist_preferred_posterior_pt"
HAnimSite101.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite101.translation = [0.29,1.0915,-0.1091]
TouchSensor102 = x3d.TouchSensor()
TouchSensor102.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite101.children.append(TouchSensor102)
Shape103 = x3d.Shape()
Shape103.USE = "HAnimSiteShape"

HAnimSite101.children.append(Shape103)

HAnimSegment53.children.append(HAnimSite101)

HAnimJoint52.children.append(HAnimSegment53)
HAnimJoint104 = x3d.HAnimJoint()
HAnimJoint104.name = "sacroiliac"
HAnimJoint104.DEF = "hanim_sacroiliac"
HAnimJoint104.center = [0,0.9149,0.0016]
HAnimJoint104.ulimit = [0,0,0]
HAnimJoint104.llimit = [0,0,0]
HAnimSegment105 = x3d.HAnimSegment()
HAnimSegment105.name = "pelvis"
HAnimSegment105.DEF = "hanim_pelvis"
Transform106 = x3d.Transform()
Transform106.translation = [0,0.9149,0.0016]
Transform107 = x3d.Transform()
#Empty Transform
Shape108 = x3d.Shape()
Shape108.USE = "HAnimJointShape"

Transform107.children.append(Shape108)

Transform106.children.append(Transform107)

HAnimSegment105.children.append(Transform106)
Shape109 = x3d.Shape()
LineSet110 = x3d.LineSet()
LineSet110.vertexCount = [2]
Coordinate111 = x3d.Coordinate()

LineSet110.coord = Coordinate111
#from sacroiliac to l_hip vertices 2
ColorRGBA112 = x3d.ColorRGBA()
ColorRGBA112.USE = "HAnimSegmentLineColorRGBA"

LineSet110.color = ColorRGBA112

Shape109.geometry = LineSet110

HAnimSegment105.children.append(Shape109)
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite113.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite113.translation = [0.1598,0.4967,0.0297]
TouchSensor114 = x3d.TouchSensor()
TouchSensor114.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite113.children.append(TouchSensor114)
Shape115 = x3d.Shape()
Shape115.USE = "HAnimSiteShape"

HAnimSite113.children.append(Shape115)

HAnimSegment105.children.append(HAnimSite113)
HAnimSite116 = x3d.HAnimSite()
HAnimSite116.name = "l_femoral_medial_epicondyles_pt"
HAnimSite116.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite116.translation = [0.0398,0.4946,0.0303]
TouchSensor117 = x3d.TouchSensor()
TouchSensor117.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite116.children.append(TouchSensor117)
Shape118 = x3d.Shape()
Shape118.USE = "HAnimSiteShape"

HAnimSite116.children.append(Shape118)

HAnimSegment105.children.append(HAnimSite116)
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.name = "l_knee_crease_pt"
HAnimSite119.DEF = "hanim_l_knee_crease_pt"
HAnimSite119.translation = [0.0993,0.4881,-0.0309]
TouchSensor120 = x3d.TouchSensor()
TouchSensor120.description = "HAnimSite l_knee_crease_pt"

HAnimSite119.children.append(TouchSensor120)
Shape121 = x3d.Shape()
Shape121.USE = "HAnimSiteShape"

HAnimSite119.children.append(Shape121)

HAnimSegment105.children.append(HAnimSite119)
HAnimSite122 = x3d.HAnimSite()
HAnimSite122.name = "l_suprapatella_pt"
HAnimSite122.DEF = "hanim_l_suprapatella_pt"
TouchSensor123 = x3d.TouchSensor()
TouchSensor123.description = "HAnimSite l_suprapatella_pt"

HAnimSite122.children.append(TouchSensor123)
Shape124 = x3d.Shape()
Shape124.USE = "HAnimSiteShape"

HAnimSite122.children.append(Shape124)

HAnimSegment105.children.append(HAnimSite122)
Shape125 = x3d.Shape()
LineSet126 = x3d.LineSet()
LineSet126.vertexCount = [2]
Coordinate127 = x3d.Coordinate()

LineSet126.coord = Coordinate127
#from sacroiliac to r_hip vertices 2
ColorRGBA128 = x3d.ColorRGBA()
ColorRGBA128.USE = "HAnimSegmentLineColorRGBA"

LineSet126.color = ColorRGBA128

Shape125.geometry = LineSet126

HAnimSegment105.children.append(Shape125)
HAnimSite129 = x3d.HAnimSite()
HAnimSite129.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite129.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite129.translation = [-0.1421,0.4992,0.031]
TouchSensor130 = x3d.TouchSensor()
TouchSensor130.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite129.children.append(TouchSensor130)
Shape131 = x3d.Shape()
Shape131.USE = "HAnimSiteShape"

HAnimSite129.children.append(Shape131)

HAnimSegment105.children.append(HAnimSite129)
HAnimSite132 = x3d.HAnimSite()
HAnimSite132.name = "r_femoral_medial_epicondyles_pt"
HAnimSite132.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite132.translation = [-0.0221,0.5014,0.0289]
TouchSensor133 = x3d.TouchSensor()
TouchSensor133.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite132.children.append(TouchSensor133)
Shape134 = x3d.Shape()
Shape134.USE = "HAnimSiteShape"

HAnimSite132.children.append(Shape134)

HAnimSegment105.children.append(HAnimSite132)
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.name = "r_knee_crease_pt"
HAnimSite135.DEF = "hanim_r_knee_crease_pt"
HAnimSite135.translation = [-0.0825,0.4932,-0.0326]
TouchSensor136 = x3d.TouchSensor()
TouchSensor136.description = "HAnimSite r_knee_crease_pt"

HAnimSite135.children.append(TouchSensor136)
Shape137 = x3d.Shape()
Shape137.USE = "HAnimSiteShape"

HAnimSite135.children.append(Shape137)

HAnimSegment105.children.append(HAnimSite135)
HAnimSite138 = x3d.HAnimSite()
HAnimSite138.name = "r_suprapatella_pt"
HAnimSite138.DEF = "hanim_r_suprapatella_pt"
TouchSensor139 = x3d.TouchSensor()
TouchSensor139.description = "HAnimSite r_suprapatella_pt"

HAnimSite138.children.append(TouchSensor139)
Shape140 = x3d.Shape()
Shape140.USE = "HAnimSiteShape"

HAnimSite138.children.append(Shape140)

HAnimSegment105.children.append(HAnimSite138)

HAnimJoint104.children.append(HAnimSegment105)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "l_hip"
HAnimJoint141.DEF = "hanim_l_hip"
HAnimJoint141.center = [0.0961,0.9124,-0.0001]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "l_thigh"
HAnimSegment142.DEF = "hanim_l_thigh"
Transform143 = x3d.Transform()
Transform143.translation = [0.0961,0.9124,-0.0001]
Transform144 = x3d.Transform()
#Empty Transform
Shape145 = x3d.Shape()
Shape145.USE = "HAnimJointShape"

Transform144.children.append(Shape145)

Transform143.children.append(Transform144)

HAnimSegment142.children.append(Transform143)
Shape146 = x3d.Shape()
LineSet147 = x3d.LineSet()
LineSet147.vertexCount = [2]
Coordinate148 = x3d.Coordinate()

LineSet147.coord = Coordinate148
#from l_hip to l_knee vertices 2
ColorRGBA149 = x3d.ColorRGBA()
ColorRGBA149.USE = "HAnimSegmentLineColorRGBA"

LineSet147.color = ColorRGBA149

Shape146.geometry = LineSet147

HAnimSegment142.children.append(Shape146)
HAnimSite150 = x3d.HAnimSite()
HAnimSite150.name = "l_lateral_malleolus_pt"
HAnimSite150.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite150.translation = [0.1308,0.0597,-0.1032]
TouchSensor151 = x3d.TouchSensor()
TouchSensor151.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite150.children.append(TouchSensor151)
Shape152 = x3d.Shape()
Shape152.USE = "HAnimSiteShape"

HAnimSite150.children.append(Shape152)

HAnimSegment142.children.append(HAnimSite150)
HAnimSite153 = x3d.HAnimSite()
HAnimSite153.name = "l_medial_malleolus_pt"
HAnimSite153.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite153.translation = [0.089,0.0716,-0.0881]
TouchSensor154 = x3d.TouchSensor()
TouchSensor154.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite153.children.append(TouchSensor154)
Shape155 = x3d.Shape()
Shape155.USE = "HAnimSiteShape"

HAnimSite153.children.append(Shape155)

HAnimSegment142.children.append(HAnimSite153)
HAnimSite156 = x3d.HAnimSite()
HAnimSite156.name = "l_tibiale_pt"
HAnimSite156.DEF = "hanim_l_tibiale_pt"
TouchSensor157 = x3d.TouchSensor()
TouchSensor157.description = "HAnimSite l_tibiale_pt"

HAnimSite156.children.append(TouchSensor157)
Shape158 = x3d.Shape()
Shape158.USE = "HAnimSiteShape"

HAnimSite156.children.append(Shape158)

HAnimSegment142.children.append(HAnimSite156)

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.name = "l_knee"
HAnimJoint159.DEF = "hanim_l_knee"
HAnimJoint159.center = [0.104,0.4867,0.0308]
HAnimJoint159.ulimit = [0,0,0]
HAnimJoint159.llimit = [0,0,0]
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.name = "l_calf"
HAnimSegment160.DEF = "hanim_l_calf"
Transform161 = x3d.Transform()
Transform161.translation = [0.104,0.4867,0.0308]
Transform162 = x3d.Transform()
#Empty Transform
Shape163 = x3d.Shape()
Shape163.USE = "HAnimJointShape"

Transform162.children.append(Shape163)

Transform161.children.append(Transform162)

HAnimSegment160.children.append(Transform161)
Shape164 = x3d.Shape()
LineSet165 = x3d.LineSet()
LineSet165.vertexCount = [2]
Coordinate166 = x3d.Coordinate()

LineSet165.coord = Coordinate166
#from l_knee to l_talocrural vertices 2
ColorRGBA167 = x3d.ColorRGBA()
ColorRGBA167.USE = "HAnimSegmentLineColorRGBA"

LineSet165.color = ColorRGBA167

Shape164.geometry = LineSet165

HAnimSegment160.children.append(Shape164)
HAnimSite168 = x3d.HAnimSite()
HAnimSite168.name = "l_calcaneus_posterior_pt"
HAnimSite168.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite168.translation = [0.0974,0.0259,-0.1171]
TouchSensor169 = x3d.TouchSensor()
TouchSensor169.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite168.children.append(TouchSensor169)
Shape170 = x3d.Shape()
Shape170.USE = "HAnimSiteShape"

HAnimSite168.children.append(Shape170)

HAnimSegment160.children.append(HAnimSite168)
HAnimSite171 = x3d.HAnimSite()
HAnimSite171.name = "l_sphyrion_pt"
HAnimSite171.DEF = "hanim_l_sphyrion_pt"
HAnimSite171.translation = [0.089,0.0575,-0.0943]
TouchSensor172 = x3d.TouchSensor()
TouchSensor172.description = "HAnimSite l_sphyrion_pt"

HAnimSite171.children.append(TouchSensor172)
Shape173 = x3d.Shape()
Shape173.USE = "HAnimSiteShape"

HAnimSite171.children.append(Shape173)

HAnimSegment160.children.append(HAnimSite171)

HAnimJoint159.children.append(HAnimSegment160)
HAnimJoint174 = x3d.HAnimJoint()
HAnimJoint174.name = "l_talocrural"
HAnimJoint174.DEF = "hanim_l_talocrural"
HAnimJoint174.center = [0.1101,0.0656,-0.0736]
HAnimJoint174.ulimit = [0,0,0]
HAnimJoint174.llimit = [0,0,0]
HAnimSegment175 = x3d.HAnimSegment()
HAnimSegment175.name = "l_talus"
HAnimSegment175.DEF = "hanim_l_talus"
Transform176 = x3d.Transform()
Transform176.scale = [0.15,0.15,0.15]
Transform176.translation = [0.08,0.06,-0.025]
Transform176.rotation = [1,0,0,-1.57]
#Transform left foot
Transform177 = x3d.Transform()
#Empty Transform left foot
Shape178 = x3d.Shape()
Shape178.USE = "HAnimJointShape"

Transform177.children.append(Shape178)

Transform176.children.append(Transform177)

HAnimSegment175.children.append(Transform176)
Shape179 = x3d.Shape()
LineSet180 = x3d.LineSet()
LineSet180.vertexCount = [2]
Coordinate181 = x3d.Coordinate()

LineSet180.coord = Coordinate181
#from l_talocrural to l_tarsometatarsal_2 vertices 2
ColorRGBA182 = x3d.ColorRGBA()
ColorRGBA182.USE = "HAnimSegmentLineColorRGBA"

LineSet180.color = ColorRGBA182

Shape179.geometry = LineSet180

HAnimSegment175.children.append(Shape179)

HAnimJoint174.children.append(HAnimSegment175)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.name = "l_tarsometatarsal_2"
HAnimJoint183.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint183.center = [0.08,0.0175,-0.0608]
HAnimJoint183.ulimit = [0,0,0]
HAnimJoint183.llimit = [0,0,0]
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.name = "l_metatarsal_2"
HAnimSegment184.DEF = "hanim_l_metatarsal_2"
Transform185 = x3d.Transform()
Transform185.translation = [0.08,0.0175,-0.0608]
Transform186 = x3d.Transform()
#Empty Transform
Shape187 = x3d.Shape()
Shape187.USE = "HAnimJointShape"

Transform186.children.append(Shape187)

Transform185.children.append(Transform186)

HAnimSegment184.children.append(Transform185)
Shape188 = x3d.Shape()
LineSet189 = x3d.LineSet()
LineSet189.vertexCount = [2]
Coordinate190 = x3d.Coordinate()

LineSet189.coord = Coordinate190
#from l_tarsometatarsal_2 to l_metatarsophalangeal_2 vertices 2
ColorRGBA191 = x3d.ColorRGBA()
ColorRGBA191.USE = "HAnimSegmentLineColorRGBA"

LineSet189.color = ColorRGBA191

Shape188.geometry = LineSet189

HAnimSegment184.children.append(Shape188)

HAnimJoint183.children.append(HAnimSegment184)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.name = "l_metatarsophalangeal_2"
HAnimJoint192.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint192.center = [0.0824,0.0064,-0.004]
HAnimJoint192.ulimit = [0,0,0]
HAnimJoint192.llimit = [0,0,0]
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment193.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform194 = x3d.Transform()
Transform194.translation = [0.0824,0.0064,-0.004]
Transform195 = x3d.Transform()
#Empty Transform
Shape196 = x3d.Shape()
Shape196.USE = "HAnimJointShape"

Transform195.children.append(Shape196)

Transform194.children.append(Transform195)

HAnimSegment193.children.append(Transform194)
Shape197 = x3d.Shape()
LineSet198 = x3d.LineSet()
LineSet198.vertexCount = [2]
Coordinate199 = x3d.Coordinate()

LineSet198.coord = Coordinate199
#from l_metatarsophalangeal_2 to l_tarsal_distal_interphalangeal_2 vertices 2
ColorRGBA200 = x3d.ColorRGBA()
ColorRGBA200.USE = "HAnimSegmentLineColorRGBA"

LineSet198.color = ColorRGBA200

Shape197.geometry = LineSet198

HAnimSegment193.children.append(Shape197)
HAnimSite201 = x3d.HAnimSite()
HAnimSite201.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite201.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite201.translation = [0.1195,0.0079,0.1433]
TouchSensor202 = x3d.TouchSensor()
TouchSensor202.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite201.children.append(TouchSensor202)
Shape203 = x3d.Shape()
Shape203.USE = "HAnimSiteShape"

HAnimSite201.children.append(Shape203)

HAnimSegment193.children.append(HAnimSite201)

HAnimJoint192.children.append(HAnimSegment193)
HAnimJoint204 = x3d.HAnimJoint()
HAnimJoint204.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint204.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint204.center = [0.0841,0.0013,0.0216]
HAnimJoint204.ulimit = [0,0,0]
HAnimJoint204.llimit = [0,0,0]

HAnimJoint192.children.append(HAnimJoint204)

HAnimJoint183.children.append(HAnimJoint192)

HAnimJoint174.children.append(HAnimJoint183)

HAnimJoint159.children.append(HAnimJoint174)

HAnimJoint141.children.append(HAnimJoint159)

HAnimJoint104.children.append(HAnimJoint141)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.name = "r_hip"
HAnimJoint205.DEF = "hanim_r_hip"
HAnimJoint205.center = [-0.095,0.9171,0.0029]
HAnimJoint205.ulimit = [0,0,0]
HAnimJoint205.llimit = [0,0,0]
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.name = "r_thigh"
HAnimSegment206.DEF = "hanim_r_thigh"
Transform207 = x3d.Transform()
Transform207.translation = [-0.095,0.9171,0.0029]
Transform208 = x3d.Transform()
#Empty Transform
Shape209 = x3d.Shape()
Shape209.USE = "HAnimJointShape"

Transform208.children.append(Shape209)

Transform207.children.append(Transform208)

HAnimSegment206.children.append(Transform207)
Shape210 = x3d.Shape()
LineSet211 = x3d.LineSet()
LineSet211.vertexCount = [2]
Coordinate212 = x3d.Coordinate()

LineSet211.coord = Coordinate212
#from r_hip to r_knee vertices 2
ColorRGBA213 = x3d.ColorRGBA()
ColorRGBA213.USE = "HAnimSegmentLineColorRGBA"

LineSet211.color = ColorRGBA213

Shape210.geometry = LineSet211

HAnimSegment206.children.append(Shape210)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.name = "r_lateral_malleolus_pt"
HAnimSite214.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite214.translation = [-0.1006,0.0658,-0.1075]
TouchSensor215 = x3d.TouchSensor()
TouchSensor215.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite214.children.append(TouchSensor215)
Shape216 = x3d.Shape()
Shape216.USE = "HAnimSiteShape"

HAnimSite214.children.append(Shape216)

HAnimSegment206.children.append(HAnimSite214)
HAnimSite217 = x3d.HAnimSite()
HAnimSite217.name = "r_medial_malleolus_pt"
HAnimSite217.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite217.translation = [-0.0591,0.076,-0.0928]
TouchSensor218 = x3d.TouchSensor()
TouchSensor218.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite217.children.append(TouchSensor218)
Shape219 = x3d.Shape()
Shape219.USE = "HAnimSiteShape"

HAnimSite217.children.append(Shape219)

HAnimSegment206.children.append(HAnimSite217)
HAnimSite220 = x3d.HAnimSite()
HAnimSite220.name = "r_tibiale_pt"
HAnimSite220.DEF = "hanim_r_tibiale_pt"
TouchSensor221 = x3d.TouchSensor()
TouchSensor221.description = "HAnimSite r_tibiale_pt"

HAnimSite220.children.append(TouchSensor221)
Shape222 = x3d.Shape()
Shape222.USE = "HAnimSiteShape"

HAnimSite220.children.append(Shape222)

HAnimSegment206.children.append(HAnimSite220)

HAnimJoint205.children.append(HAnimSegment206)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.name = "r_knee"
HAnimJoint223.DEF = "hanim_r_knee"
HAnimJoint223.center = [-0.0867,0.4913,0.0318]
HAnimJoint223.ulimit = [0,0,0]
HAnimJoint223.llimit = [0,0,0]
HAnimSegment224 = x3d.HAnimSegment()
HAnimSegment224.name = "r_calf"
HAnimSegment224.DEF = "hanim_r_calf"
Transform225 = x3d.Transform()
Transform225.translation = [-0.0867,0.4913,0.0318]
Transform226 = x3d.Transform()
#Empty Transform
Shape227 = x3d.Shape()
Shape227.USE = "HAnimJointShape"

Transform226.children.append(Shape227)

Transform225.children.append(Transform226)

HAnimSegment224.children.append(Transform225)
Shape228 = x3d.Shape()
LineSet229 = x3d.LineSet()
LineSet229.vertexCount = [2]
Coordinate230 = x3d.Coordinate()

LineSet229.coord = Coordinate230
#from r_knee to r_talocrural vertices 2
ColorRGBA231 = x3d.ColorRGBA()
ColorRGBA231.USE = "HAnimSegmentLineColorRGBA"

LineSet229.color = ColorRGBA231

Shape228.geometry = LineSet229

HAnimSegment224.children.append(Shape228)
HAnimSite232 = x3d.HAnimSite()
HAnimSite232.name = "r_calcaneus_posterior_pt"
HAnimSite232.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite232.translation = [-0.0692,0.0297,-0.1221]
TouchSensor233 = x3d.TouchSensor()
TouchSensor233.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite232.children.append(TouchSensor233)
Shape234 = x3d.Shape()
Shape234.USE = "HAnimSiteShape"

HAnimSite232.children.append(Shape234)

HAnimSegment224.children.append(HAnimSite232)
HAnimSite235 = x3d.HAnimSite()
HAnimSite235.name = "r_sphyrion_pt"
HAnimSite235.DEF = "hanim_r_sphyrion_pt"
HAnimSite235.translation = [-0.0603,0.061,-0.1002]
TouchSensor236 = x3d.TouchSensor()
TouchSensor236.description = "HAnimSite r_sphyrion_pt"

HAnimSite235.children.append(TouchSensor236)
Shape237 = x3d.Shape()
Shape237.USE = "HAnimSiteShape"

HAnimSite235.children.append(Shape237)

HAnimSegment224.children.append(HAnimSite235)

HAnimJoint223.children.append(HAnimSegment224)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.name = "r_talocrural"
HAnimJoint238.DEF = "hanim_r_talocrural"
HAnimJoint238.center = [-0.0801,0.0712,-0.0766]
HAnimJoint238.ulimit = [0,0,0]
HAnimJoint238.llimit = [0,0,0]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.name = "r_talus"
HAnimSegment239.DEF = "hanim_r_talus"
Transform240 = x3d.Transform()
Transform240.scale = [0.15,0.15,0.15]
Transform240.translation = [-0.05,0.06,-0.025]
Transform240.rotation = [1,0,0,-1.57]
#Transform right foot
Transform241 = x3d.Transform()
#Empty Transform right foot
Shape242 = x3d.Shape()
Shape242.USE = "HAnimJointShape"

Transform241.children.append(Shape242)

Transform240.children.append(Transform241)

HAnimSegment239.children.append(Transform240)
Shape243 = x3d.Shape()
LineSet244 = x3d.LineSet()
LineSet244.vertexCount = [2]
Coordinate245 = x3d.Coordinate()

LineSet244.coord = Coordinate245
#from r_talocrural to r_tarsometatarsal_2 vertices 2
ColorRGBA246 = x3d.ColorRGBA()
ColorRGBA246.USE = "HAnimSegmentLineColorRGBA"

LineSet244.color = ColorRGBA246

Shape243.geometry = LineSet244

HAnimSegment239.children.append(Shape243)

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint247 = x3d.HAnimJoint()
HAnimJoint247.name = "r_tarsometatarsal_2"
HAnimJoint247.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint247.center = [-0.08,0.0175,-0.0608]
HAnimJoint247.ulimit = [0,0,0]
HAnimJoint247.llimit = [0,0,0]
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.name = "r_metatarsal_2"
HAnimSegment248.DEF = "hanim_r_metatarsal_2"
Transform249 = x3d.Transform()
Transform249.translation = [-0.08,0.0175,-0.0608]
Transform250 = x3d.Transform()
#Empty Transform
Shape251 = x3d.Shape()
Shape251.USE = "HAnimJointShape"

Transform250.children.append(Shape251)

Transform249.children.append(Transform250)

HAnimSegment248.children.append(Transform249)
Shape252 = x3d.Shape()
LineSet253 = x3d.LineSet()
LineSet253.vertexCount = [2]
Coordinate254 = x3d.Coordinate()

LineSet253.coord = Coordinate254
#from r_tarsometatarsal_2 to r_metatarsophalangeal_2 vertices 2
ColorRGBA255 = x3d.ColorRGBA()
ColorRGBA255.USE = "HAnimSegmentLineColorRGBA"

LineSet253.color = ColorRGBA255

Shape252.geometry = LineSet253

HAnimSegment248.children.append(Shape252)

HAnimJoint247.children.append(HAnimSegment248)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.name = "r_metatarsophalangeal_2"
HAnimJoint256.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint256.center = [-0.0823,0.0064,-0.004]
HAnimJoint256.ulimit = [0,0,0]
HAnimJoint256.llimit = [0,0,0]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment257.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform258 = x3d.Transform()
Transform258.translation = [-0.0823,0.0064,-0.004]
Transform259 = x3d.Transform()
#Empty Transform
Shape260 = x3d.Shape()
Shape260.USE = "HAnimJointShape"

Transform259.children.append(Shape260)

Transform258.children.append(Transform259)

HAnimSegment257.children.append(Transform258)
Shape261 = x3d.Shape()
LineSet262 = x3d.LineSet()
LineSet262.vertexCount = [2]
Coordinate263 = x3d.Coordinate()

LineSet262.coord = Coordinate263
#from r_metatarsophalangeal_2 to r_tarsal_distal_interphalangeal_2 vertices 2
ColorRGBA264 = x3d.ColorRGBA()
ColorRGBA264.USE = "HAnimSegmentLineColorRGBA"

LineSet262.color = ColorRGBA264

Shape261.geometry = LineSet262

HAnimSegment257.children.append(Shape261)
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite265.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite265.translation = [-0.0883,0.0134,0.1383]
TouchSensor266 = x3d.TouchSensor()
TouchSensor266.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite265.children.append(TouchSensor266)
Shape267 = x3d.Shape()
Shape267.USE = "HAnimSiteShape"

HAnimSite265.children.append(Shape267)

HAnimSegment257.children.append(HAnimSite265)

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint268.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint268.center = [-0.0841,0.0013,0.0216]
HAnimJoint268.ulimit = [0,0,0]
HAnimJoint268.llimit = [0,0,0]

HAnimJoint256.children.append(HAnimJoint268)

HAnimJoint247.children.append(HAnimJoint256)

HAnimJoint238.children.append(HAnimJoint247)

HAnimJoint223.children.append(HAnimJoint238)

HAnimJoint205.children.append(HAnimJoint223)

HAnimJoint104.children.append(HAnimJoint205)

HAnimJoint52.children.append(HAnimJoint104)
HAnimJoint269 = x3d.HAnimJoint()
HAnimJoint269.name = "vl5"
HAnimJoint269.DEF = "hanim_vl5"
HAnimJoint269.center = [0.0028,1.0568,-0.0776]
HAnimJoint269.ulimit = [0,0,0]
HAnimJoint269.llimit = [0,0,0]
HAnimSegment270 = x3d.HAnimSegment()
HAnimSegment270.name = "l5"
HAnimSegment270.DEF = "hanim_l5"
Transform271 = x3d.Transform()
Transform271.translation = [0.0028,1.0568,-0.0776]
Transform272 = x3d.Transform()
#Empty Transform
Shape273 = x3d.Shape()
Shape273.USE = "HAnimJointShape"

Transform272.children.append(Shape273)

Transform271.children.append(Transform272)

HAnimSegment270.children.append(Transform271)
Shape274 = x3d.Shape()
LineSet275 = x3d.LineSet()
LineSet275.vertexCount = [2]
Coordinate276 = x3d.Coordinate()

LineSet275.coord = Coordinate276
#from vl5 to vl3 vertices 2
ColorRGBA277 = x3d.ColorRGBA()
ColorRGBA277.USE = "HAnimSegmentLineColorRGBA"

LineSet275.color = ColorRGBA277

Shape274.geometry = LineSet275

HAnimSegment270.children.append(Shape274)

HAnimJoint269.children.append(HAnimSegment270)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.name = "vl3"
HAnimJoint278.DEF = "hanim_vl3"
HAnimJoint278.center = [0.0041,1.1276,-0.0796]
HAnimJoint278.ulimit = [0,0,0]
HAnimJoint278.llimit = [0,0,0]
HAnimSegment279 = x3d.HAnimSegment()
HAnimSegment279.name = "l3"
HAnimSegment279.DEF = "hanim_l3"
Transform280 = x3d.Transform()
Transform280.translation = [0.0041,1.1276,-0.0796]
Transform281 = x3d.Transform()
#Empty Transform
Shape282 = x3d.Shape()
Shape282.USE = "HAnimJointShape"

Transform281.children.append(Shape282)

Transform280.children.append(Transform281)

HAnimSegment279.children.append(Transform280)
Shape283 = x3d.Shape()
LineSet284 = x3d.LineSet()
LineSet284.vertexCount = [2]
Coordinate285 = x3d.Coordinate()

LineSet284.coord = Coordinate285
#from vl3 to vl1 vertices 2
ColorRGBA286 = x3d.ColorRGBA()
ColorRGBA286.USE = "HAnimSegmentLineColorRGBA"

LineSet284.color = ColorRGBA286

Shape283.geometry = LineSet284

HAnimSegment279.children.append(Shape283)

HAnimJoint278.children.append(HAnimSegment279)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.name = "vl1"
HAnimJoint287.DEF = "hanim_vl1"
HAnimJoint287.center = [0.0048,1.1912,-0.0805]
HAnimJoint287.ulimit = [0,0,0]
HAnimJoint287.llimit = [0,0,0]
HAnimSegment288 = x3d.HAnimSegment()
HAnimSegment288.name = "l1"
HAnimSegment288.DEF = "hanim_l1"
Transform289 = x3d.Transform()
Transform289.translation = [0.0048,1.1912,-0.0805]
Transform290 = x3d.Transform()
#Empty Transform
Shape291 = x3d.Shape()
Shape291.USE = "HAnimJointShape"

Transform290.children.append(Shape291)

Transform289.children.append(Transform290)

HAnimSegment288.children.append(Transform289)
Shape292 = x3d.Shape()
LineSet293 = x3d.LineSet()
LineSet293.vertexCount = [2]
Coordinate294 = x3d.Coordinate()

LineSet293.coord = Coordinate294
#from vl1 to vt10 vertices 2
ColorRGBA295 = x3d.ColorRGBA()
ColorRGBA295.USE = "HAnimSegmentLineColorRGBA"

LineSet293.color = ColorRGBA295

Shape292.geometry = LineSet293

HAnimSegment288.children.append(Shape292)
HAnimSite296 = x3d.HAnimSite()
HAnimSite296.name = "substernale_pt"
HAnimSite296.DEF = "hanim_substernale_pt"
HAnimSite296.translation = [0.0085,1.2995,0.1147]
TouchSensor297 = x3d.TouchSensor()
TouchSensor297.description = "HAnimSite substernale_pt"

HAnimSite296.children.append(TouchSensor297)
Shape298 = x3d.Shape()
Shape298.USE = "HAnimSiteShape"

HAnimSite296.children.append(Shape298)

HAnimSegment288.children.append(HAnimSite296)

HAnimJoint287.children.append(HAnimSegment288)
HAnimJoint299 = x3d.HAnimJoint()
HAnimJoint299.name = "vt10"
HAnimJoint299.DEF = "hanim_vt10"
HAnimJoint299.center = [0.0056,1.2848,-0.0822]
HAnimJoint299.ulimit = [0,0,0]
HAnimJoint299.llimit = [0,0,0]
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.name = "t10"
HAnimSegment300.DEF = "hanim_t10"
Transform301 = x3d.Transform()
Transform301.translation = [0.0056,1.2848,-0.0822]
Transform302 = x3d.Transform()
#Empty Transform
Shape303 = x3d.Shape()
Shape303.USE = "HAnimJointShape"

Transform302.children.append(Shape303)

Transform301.children.append(Transform302)

HAnimSegment300.children.append(Transform301)
Shape304 = x3d.Shape()
LineSet305 = x3d.LineSet()
LineSet305.vertexCount = [2]
Coordinate306 = x3d.Coordinate()

LineSet305.coord = Coordinate306
#from vt10 to vt6 vertices 2
ColorRGBA307 = x3d.ColorRGBA()
ColorRGBA307.USE = "HAnimSegmentLineColorRGBA"

LineSet305.color = ColorRGBA307

Shape304.geometry = LineSet305

HAnimSegment300.children.append(Shape304)
HAnimSite308 = x3d.HAnimSite()
HAnimSite308.name = "l_chest_midsagittal_plane_pt"
HAnimSite308.DEF = "hanim_l_chest_midsagittal_plane_pt"
TouchSensor309 = x3d.TouchSensor()
TouchSensor309.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite308.children.append(TouchSensor309)
Shape310 = x3d.Shape()
Shape310.USE = "HAnimSiteShape"

HAnimSite308.children.append(Shape310)

HAnimSegment300.children.append(HAnimSite308)
HAnimSite311 = x3d.HAnimSite()
HAnimSite311.name = "mesosternale_pt"
HAnimSite311.DEF = "hanim_mesosternale_pt"
TouchSensor312 = x3d.TouchSensor()
TouchSensor312.description = "HAnimSite mesosternale_pt"

HAnimSite311.children.append(TouchSensor312)
Shape313 = x3d.Shape()
Shape313.USE = "HAnimSiteShape"

HAnimSite311.children.append(Shape313)

HAnimSegment300.children.append(HAnimSite311)
HAnimSite314 = x3d.HAnimSite()
HAnimSite314.name = "r_chest_midsagittal_plane_pt"
HAnimSite314.DEF = "hanim_r_chest_midsagittal_plane_pt"
TouchSensor315 = x3d.TouchSensor()
TouchSensor315.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite314.children.append(TouchSensor315)
Shape316 = x3d.Shape()
Shape316.USE = "HAnimSiteShape"

HAnimSite314.children.append(Shape316)

HAnimSegment300.children.append(HAnimSite314)
HAnimSite317 = x3d.HAnimSite()
HAnimSite317.name = "rear_center_midsagittal_plane_pt"
HAnimSite317.DEF = "hanim_rear_center_midsagittal_plane_pt"
TouchSensor318 = x3d.TouchSensor()
TouchSensor318.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite317.children.append(TouchSensor318)
Shape319 = x3d.Shape()
Shape319.USE = "HAnimSiteShape"

HAnimSite317.children.append(Shape319)

HAnimSegment300.children.append(HAnimSite317)

HAnimJoint299.children.append(HAnimSegment300)
HAnimJoint320 = x3d.HAnimJoint()
HAnimJoint320.name = "vt6"
HAnimJoint320.DEF = "hanim_vt6"
HAnimJoint320.center = [0.0059,1.3866,-0.08]
HAnimJoint320.ulimit = [0,0,0]
HAnimJoint320.llimit = [0,0,0]
HAnimSegment321 = x3d.HAnimSegment()
HAnimSegment321.name = "t6"
HAnimSegment321.DEF = "hanim_t6"
Transform322 = x3d.Transform()
Transform322.translation = [0.0059,1.3866,-0.08]
Transform323 = x3d.Transform()
#Empty Transform
Shape324 = x3d.Shape()
Shape324.USE = "HAnimJointShape"

Transform323.children.append(Shape324)

Transform322.children.append(Transform323)

HAnimSegment321.children.append(Transform322)
Shape325 = x3d.Shape()
LineSet326 = x3d.LineSet()
LineSet326.vertexCount = [2]
Coordinate327 = x3d.Coordinate()

LineSet326.coord = Coordinate327
#from vt6 to vt1 vertices 2
ColorRGBA328 = x3d.ColorRGBA()
ColorRGBA328.USE = "HAnimSegmentLineColorRGBA"

LineSet326.color = ColorRGBA328

Shape325.geometry = LineSet326

HAnimSegment321.children.append(Shape325)
HAnimSite329 = x3d.HAnimSite()
HAnimSite329.name = "cervicale_pt"
HAnimSite329.DEF = "hanim_cervicale_pt"
HAnimSite329.translation = [0.0064,1.52,-0.0815]
TouchSensor330 = x3d.TouchSensor()
TouchSensor330.description = "HAnimSite cervicale_pt"

HAnimSite329.children.append(TouchSensor330)
Shape331 = x3d.Shape()
Shape331.USE = "HAnimSiteShape"

HAnimSite329.children.append(Shape331)

HAnimSegment321.children.append(HAnimSite329)
HAnimSite332 = x3d.HAnimSite()
HAnimSite332.name = "suprasternale_pt"
HAnimSite332.DEF = "hanim_suprasternale_pt"
HAnimSite332.translation = [0.0084,1.4714,0.0551]
TouchSensor333 = x3d.TouchSensor()
TouchSensor333.description = "HAnimSite suprasternale_pt"

HAnimSite332.children.append(TouchSensor333)
Shape334 = x3d.Shape()
Shape334.USE = "HAnimSiteShape"

HAnimSite332.children.append(Shape334)

HAnimSegment321.children.append(HAnimSite332)

HAnimJoint320.children.append(HAnimSegment321)
HAnimJoint335 = x3d.HAnimJoint()
HAnimJoint335.name = "vt1"
HAnimJoint335.DEF = "hanim_vt1"
HAnimJoint335.center = [0.0065,1.4951,-0.0387]
HAnimJoint335.ulimit = [0,0,0]
HAnimJoint335.llimit = [0,0,0]
HAnimSegment336 = x3d.HAnimSegment()
HAnimSegment336.name = "t1"
HAnimSegment336.DEF = "hanim_t1"
Transform337 = x3d.Transform()
Transform337.translation = [0.0065,1.4951,-0.0387]
Transform338 = x3d.Transform()
#Empty Transform
Shape339 = x3d.Shape()
Shape339.USE = "HAnimJointShape"

Transform338.children.append(Shape339)

Transform337.children.append(Transform338)

HAnimSegment336.children.append(Transform337)
Shape340 = x3d.Shape()
LineSet341 = x3d.LineSet()
LineSet341.vertexCount = [2]
Coordinate342 = x3d.Coordinate()

LineSet341.coord = Coordinate342
#from vt1 to vc4 vertices 2
ColorRGBA343 = x3d.ColorRGBA()
ColorRGBA343.USE = "HAnimSegmentLineColorRGBA"

LineSet341.color = ColorRGBA343

Shape340.geometry = LineSet341

HAnimSegment336.children.append(Shape340)
Shape344 = x3d.Shape()
LineSet345 = x3d.LineSet()
LineSet345.vertexCount = [2]
Coordinate346 = x3d.Coordinate()

LineSet345.coord = Coordinate346
#from vt1 to l_sternoclavicular vertices 2
ColorRGBA347 = x3d.ColorRGBA()
ColorRGBA347.USE = "HAnimSegmentLineColorRGBA"

LineSet345.color = ColorRGBA347

Shape344.geometry = LineSet345

HAnimSegment336.children.append(Shape344)
HAnimSite348 = x3d.HAnimSite()
HAnimSite348.name = "l_acromion_pt"
HAnimSite348.DEF = "hanim_l_acromion_pt"
HAnimSite348.translation = [0.2032,1.476,-0.049]
TouchSensor349 = x3d.TouchSensor()
TouchSensor349.description = "HAnimSite l_acromion_pt"

HAnimSite348.children.append(TouchSensor349)
Shape350 = x3d.Shape()
Shape350.USE = "HAnimSiteShape"

HAnimSite348.children.append(Shape350)

HAnimSegment336.children.append(HAnimSite348)
HAnimSite351 = x3d.HAnimSite()
HAnimSite351.name = "l_axilla_distal_pt"
HAnimSite351.DEF = "hanim_l_axilla_distal_pt"
HAnimSite351.translation = [0.1706,1.4072,-0.0875]
TouchSensor352 = x3d.TouchSensor()
TouchSensor352.description = "HAnimSite l_axilla_distal_pt"

HAnimSite351.children.append(TouchSensor352)
Shape353 = x3d.Shape()
Shape353.USE = "HAnimSiteShape"

HAnimSite351.children.append(Shape353)

HAnimSegment336.children.append(HAnimSite351)
HAnimSite354 = x3d.HAnimSite()
HAnimSite354.name = "l_axilla_posterior_folds_pt"
HAnimSite354.DEF = "hanim_l_axilla_posterior_folds_pt"
TouchSensor355 = x3d.TouchSensor()
TouchSensor355.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite354.children.append(TouchSensor355)
Shape356 = x3d.Shape()
Shape356.USE = "HAnimSiteShape"

HAnimSite354.children.append(Shape356)

HAnimSegment336.children.append(HAnimSite354)
HAnimSite357 = x3d.HAnimSite()
HAnimSite357.name = "l_axilla_proximal_pt"
HAnimSite357.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite357.translation = [0.1777,1.4065,-0.0075]
TouchSensor358 = x3d.TouchSensor()
TouchSensor358.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite357.children.append(TouchSensor358)
Shape359 = x3d.Shape()
Shape359.USE = "HAnimSiteShape"

HAnimSite357.children.append(Shape359)

HAnimSegment336.children.append(HAnimSite357)
HAnimSite360 = x3d.HAnimSite()
HAnimSite360.name = "l_clavicale_pt"
HAnimSite360.DEF = "hanim_l_clavicale_pt"
HAnimSite360.translation = [0.0271,1.4943,0.0394]
TouchSensor361 = x3d.TouchSensor()
TouchSensor361.description = "HAnimSite l_clavicale_pt"

HAnimSite360.children.append(TouchSensor361)
Shape362 = x3d.Shape()
Shape362.USE = "HAnimSiteShape"

HAnimSite360.children.append(Shape362)

HAnimSegment336.children.append(HAnimSite360)
Shape363 = x3d.Shape()
LineSet364 = x3d.LineSet()
LineSet364.vertexCount = [2]
Coordinate365 = x3d.Coordinate()

LineSet364.coord = Coordinate365
#from vt1 to r_sternoclavicular vertices 2
ColorRGBA366 = x3d.ColorRGBA()
ColorRGBA366.USE = "HAnimSegmentLineColorRGBA"

LineSet364.color = ColorRGBA366

Shape363.geometry = LineSet364

HAnimSegment336.children.append(Shape363)
HAnimSite367 = x3d.HAnimSite()
HAnimSite367.name = "r_acromion_pt"
HAnimSite367.DEF = "hanim_r_acromion_pt"
HAnimSite367.translation = [-0.1905,1.4791,-0.0431]
TouchSensor368 = x3d.TouchSensor()
TouchSensor368.description = "HAnimSite r_acromion_pt"

HAnimSite367.children.append(TouchSensor368)
Shape369 = x3d.Shape()
Shape369.USE = "HAnimSiteShape"

HAnimSite367.children.append(Shape369)

HAnimSegment336.children.append(HAnimSite367)
HAnimSite370 = x3d.HAnimSite()
HAnimSite370.name = "r_axilla_distal_pt"
HAnimSite370.DEF = "hanim_r_axilla_distal_pt"
HAnimSite370.translation = [-0.1603,1.4098,-0.0826]
TouchSensor371 = x3d.TouchSensor()
TouchSensor371.description = "HAnimSite r_axilla_distal_pt"

HAnimSite370.children.append(TouchSensor371)
Shape372 = x3d.Shape()
Shape372.USE = "HAnimSiteShape"

HAnimSite370.children.append(Shape372)

HAnimSegment336.children.append(HAnimSite370)
HAnimSite373 = x3d.HAnimSite()
HAnimSite373.name = "r_axilla_posterior_folds_pt"
HAnimSite373.DEF = "hanim_r_axilla_posterior_folds_pt"
TouchSensor374 = x3d.TouchSensor()
TouchSensor374.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite373.children.append(TouchSensor374)
Shape375 = x3d.Shape()
Shape375.USE = "HAnimSiteShape"

HAnimSite373.children.append(Shape375)

HAnimSegment336.children.append(HAnimSite373)
HAnimSite376 = x3d.HAnimSite()
HAnimSite376.name = "r_axilla_proximal_pt"
HAnimSite376.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite376.translation = [-0.1626,1.4072,-0.0031]
TouchSensor377 = x3d.TouchSensor()
TouchSensor377.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite376.children.append(TouchSensor377)
Shape378 = x3d.Shape()
Shape378.USE = "HAnimSiteShape"

HAnimSite376.children.append(Shape378)

HAnimSegment336.children.append(HAnimSite376)
HAnimSite379 = x3d.HAnimSite()
HAnimSite379.name = "r_clavicale_pt"
HAnimSite379.DEF = "hanim_r_clavicale_pt"
HAnimSite379.translation = [-0.0115,1.4943,0.04]
TouchSensor380 = x3d.TouchSensor()
TouchSensor380.description = "HAnimSite r_clavicale_pt"

HAnimSite379.children.append(TouchSensor380)
Shape381 = x3d.Shape()
Shape381.USE = "HAnimSiteShape"

HAnimSite379.children.append(Shape381)

HAnimSegment336.children.append(HAnimSite379)

HAnimJoint335.children.append(HAnimSegment336)
HAnimJoint382 = x3d.HAnimJoint()
HAnimJoint382.name = "vc4"
HAnimJoint382.DEF = "hanim_vc4"
HAnimJoint382.center = [0.0066,1.5662,-0.0084]
HAnimJoint382.ulimit = [0,0,0]
HAnimJoint382.llimit = [0,0,0]
HAnimSegment383 = x3d.HAnimSegment()
HAnimSegment383.name = "c4"
HAnimSegment383.DEF = "hanim_c4"
Transform384 = x3d.Transform()
Transform384.translation = [0.0066,1.5662,-0.0084]
Transform385 = x3d.Transform()
#Empty Transform
Shape386 = x3d.Shape()
Shape386.USE = "HAnimJointShape"

Transform385.children.append(Shape386)

Transform384.children.append(Transform385)

HAnimSegment383.children.append(Transform384)
Shape387 = x3d.Shape()
LineSet388 = x3d.LineSet()
LineSet388.vertexCount = [2]
Coordinate389 = x3d.Coordinate()

LineSet388.coord = Coordinate389
#from vc4 to vc2 vertices 2
ColorRGBA390 = x3d.ColorRGBA()
ColorRGBA390.USE = "HAnimSegmentLineColorRGBA"

LineSet388.color = ColorRGBA390

Shape387.geometry = LineSet388

HAnimSegment383.children.append(Shape387)
HAnimSite391 = x3d.HAnimSite()
HAnimSite391.name = "adams_apple_pt"
HAnimSite391.DEF = "hanim_adams_apple_pt"
TouchSensor392 = x3d.TouchSensor()
TouchSensor392.description = "HAnimSite adams_apple_pt"

HAnimSite391.children.append(TouchSensor392)
Shape393 = x3d.Shape()
Shape393.USE = "HAnimSiteShape"

HAnimSite391.children.append(Shape393)

HAnimSegment383.children.append(HAnimSite391)

HAnimJoint382.children.append(HAnimSegment383)
HAnimJoint394 = x3d.HAnimJoint()
HAnimJoint394.name = "vc2"
HAnimJoint394.DEF = "hanim_vc2"
HAnimJoint394.center = [0.0066,1.5928,-0.0103]
HAnimJoint394.ulimit = [0,0,0]
HAnimJoint394.llimit = [0,0,0]
HAnimSegment395 = x3d.HAnimSegment()
HAnimSegment395.name = "c2"
HAnimSegment395.DEF = "hanim_c2"
Transform396 = x3d.Transform()
Transform396.translation = [0.0066,1.5928,-0.0103]
Transform397 = x3d.Transform()
#Empty Transform
Shape398 = x3d.Shape()
Shape398.USE = "HAnimJointShape"

Transform397.children.append(Shape398)

Transform396.children.append(Transform397)

HAnimSegment395.children.append(Transform396)
Shape399 = x3d.Shape()
LineSet400 = x3d.LineSet()
LineSet400.vertexCount = [2]
Coordinate401 = x3d.Coordinate()

LineSet400.coord = Coordinate401
#from vc2 to skullbase vertices 2
ColorRGBA402 = x3d.ColorRGBA()
ColorRGBA402.USE = "HAnimSegmentLineColorRGBA"

LineSet400.color = ColorRGBA402

Shape399.geometry = LineSet400

HAnimSegment395.children.append(Shape399)
HAnimSite403 = x3d.HAnimSite()
HAnimSite403.name = "glabella_pt"
HAnimSite403.DEF = "hanim_glabella_pt"
TouchSensor404 = x3d.TouchSensor()
TouchSensor404.description = "HAnimSite glabella_pt"

HAnimSite403.children.append(TouchSensor404)
Shape405 = x3d.Shape()
Shape405.USE = "HAnimSiteShape"

HAnimSite403.children.append(Shape405)

HAnimSegment395.children.append(HAnimSite403)
HAnimSite406 = x3d.HAnimSite()
HAnimSite406.name = "l_ectocanthus_pt"
HAnimSite406.DEF = "hanim_l_ectocanthus_pt"
TouchSensor407 = x3d.TouchSensor()
TouchSensor407.description = "HAnimSite l_ectocanthus_pt"

HAnimSite406.children.append(TouchSensor407)
Shape408 = x3d.Shape()
Shape408.USE = "HAnimSiteShape"

HAnimSite406.children.append(Shape408)

HAnimSegment395.children.append(HAnimSite406)
HAnimSite409 = x3d.HAnimSite()
HAnimSite409.name = "l_infraorbitale_pt"
HAnimSite409.DEF = "hanim_l_infraorbitale_pt"
HAnimSite409.translation = [0.0341,1.6171,0.0752]
TouchSensor410 = x3d.TouchSensor()
TouchSensor410.description = "HAnimSite l_infraorbitale_pt"

HAnimSite409.children.append(TouchSensor410)
Shape411 = x3d.Shape()
Shape411.USE = "HAnimSiteShape"

HAnimSite409.children.append(Shape411)

HAnimSegment395.children.append(HAnimSite409)
HAnimSite412 = x3d.HAnimSite()
HAnimSite412.name = "l_tragion_pt"
HAnimSite412.DEF = "hanim_l_tragion_pt"
HAnimSite412.translation = [0.0739,1.6348,0.0282]
TouchSensor413 = x3d.TouchSensor()
TouchSensor413.description = "HAnimSite l_tragion_pt"

HAnimSite412.children.append(TouchSensor413)
Shape414 = x3d.Shape()
Shape414.USE = "HAnimSiteShape"

HAnimSite412.children.append(Shape414)

HAnimSegment395.children.append(HAnimSite412)
HAnimSite415 = x3d.HAnimSite()
HAnimSite415.name = "nuchale_pt"
HAnimSite415.DEF = "hanim_nuchale_pt"
HAnimSite415.translation = [0.0039,1.5972,-0.0796]
TouchSensor416 = x3d.TouchSensor()
TouchSensor416.description = "HAnimSite nuchale_pt"

HAnimSite415.children.append(TouchSensor416)
Shape417 = x3d.Shape()
Shape417.USE = "HAnimSiteShape"

HAnimSite415.children.append(Shape417)

HAnimSegment395.children.append(HAnimSite415)
HAnimSite418 = x3d.HAnimSite()
HAnimSite418.name = "opisthocranion_pt"
HAnimSite418.DEF = "hanim_opisthocranion_pt"
TouchSensor419 = x3d.TouchSensor()
TouchSensor419.description = "HAnimSite opisthocranion_pt"

HAnimSite418.children.append(TouchSensor419)
Shape420 = x3d.Shape()
Shape420.USE = "HAnimSiteShape"

HAnimSite418.children.append(Shape420)

HAnimSegment395.children.append(HAnimSite418)
HAnimSite421 = x3d.HAnimSite()
HAnimSite421.name = "r_ectocanthus_pt"
HAnimSite421.DEF = "hanim_r_ectocanthus_pt"
TouchSensor422 = x3d.TouchSensor()
TouchSensor422.description = "HAnimSite r_ectocanthus_pt"

HAnimSite421.children.append(TouchSensor422)
Shape423 = x3d.Shape()
Shape423.USE = "HAnimSiteShape"

HAnimSite421.children.append(Shape423)

HAnimSegment395.children.append(HAnimSite421)
HAnimSite424 = x3d.HAnimSite()
HAnimSite424.name = "r_infraorbitale_pt"
HAnimSite424.DEF = "hanim_r_infraorbitale_pt"
HAnimSite424.translation = [-0.0237,1.6171,0.0752]
TouchSensor425 = x3d.TouchSensor()
TouchSensor425.description = "HAnimSite r_infraorbitale_pt"

HAnimSite424.children.append(TouchSensor425)
Shape426 = x3d.Shape()
Shape426.USE = "HAnimSiteShape"

HAnimSite424.children.append(Shape426)

HAnimSegment395.children.append(HAnimSite424)
HAnimSite427 = x3d.HAnimSite()
HAnimSite427.name = "r_tragion_pt"
HAnimSite427.DEF = "hanim_r_tragion_pt"
HAnimSite427.translation = [-0.0646,1.6347,0.0302]
TouchSensor428 = x3d.TouchSensor()
TouchSensor428.description = "HAnimSite r_tragion_pt"

HAnimSite427.children.append(TouchSensor428)
Shape429 = x3d.Shape()
Shape429.USE = "HAnimSiteShape"

HAnimSite427.children.append(Shape429)

HAnimSegment395.children.append(HAnimSite427)
HAnimSite430 = x3d.HAnimSite()
HAnimSite430.name = "sellion_pt"
HAnimSite430.DEF = "hanim_sellion_pt"
HAnimSite430.translation = [0.0058,1.6316,0.0852]
TouchSensor431 = x3d.TouchSensor()
TouchSensor431.description = "HAnimSite sellion_pt"

HAnimSite430.children.append(TouchSensor431)
Shape432 = x3d.Shape()
Shape432.USE = "HAnimSiteShape"

HAnimSite430.children.append(Shape432)

HAnimSegment395.children.append(HAnimSite430)
HAnimSite433 = x3d.HAnimSite()
HAnimSite433.name = "skull_vertex_pt"
HAnimSite433.DEF = "hanim_skull_vertex_pt"
HAnimSite433.translation = [0.005,1.7504,0.0055]
TouchSensor434 = x3d.TouchSensor()
TouchSensor434.description = "HAnimSite skull_vertex_pt"

HAnimSite433.children.append(TouchSensor434)
Shape435 = x3d.Shape()
Shape435.USE = "HAnimSiteShape"

HAnimSite433.children.append(Shape435)

HAnimSegment395.children.append(HAnimSite433)

HAnimJoint394.children.append(HAnimSegment395)
HAnimJoint436 = x3d.HAnimJoint()
HAnimJoint436.name = "skullbase"
HAnimJoint436.DEF = "hanim_skullbase"
HAnimJoint436.center = [0.0044,1.6209,0.0236]
HAnimJoint436.ulimit = [0,0,0]
HAnimJoint436.llimit = [0,0,0]

HAnimJoint394.children.append(HAnimJoint436)

HAnimJoint382.children.append(HAnimJoint394)

HAnimJoint335.children.append(HAnimJoint382)
HAnimJoint437 = x3d.HAnimJoint()
HAnimJoint437.name = "l_sternoclavicular"
HAnimJoint437.DEF = "hanim_l_sternoclavicular"
HAnimJoint437.center = [0.082,1.4488,-0.0353]
HAnimJoint437.ulimit = [0,0,0]
HAnimJoint437.llimit = [0,0,0]
HAnimSegment438 = x3d.HAnimSegment()
HAnimSegment438.name = "l_clavicle"
HAnimSegment438.DEF = "hanim_l_clavicle"
Transform439 = x3d.Transform()
Transform439.translation = [0.082,1.4488,-0.0353]
Transform440 = x3d.Transform()
#Empty Transform
Shape441 = x3d.Shape()
Shape441.USE = "HAnimJointShape"

Transform440.children.append(Shape441)

Transform439.children.append(Transform440)

HAnimSegment438.children.append(Transform439)
Shape442 = x3d.Shape()
LineSet443 = x3d.LineSet()
LineSet443.vertexCount = [2]
Coordinate444 = x3d.Coordinate()

LineSet443.coord = Coordinate444
#from l_sternoclavicular to l_acromioclavicular vertices 2
ColorRGBA445 = x3d.ColorRGBA()
ColorRGBA445.USE = "HAnimSegmentLineColorRGBA"

LineSet443.color = ColorRGBA445

Shape442.geometry = LineSet443

HAnimSegment438.children.append(Shape442)

HAnimJoint437.children.append(HAnimSegment438)
HAnimJoint446 = x3d.HAnimJoint()
HAnimJoint446.name = "l_acromioclavicular"
HAnimJoint446.DEF = "hanim_l_acromioclavicular"
HAnimJoint446.center = [0.0962,1.4269,-0.0424]
HAnimJoint446.ulimit = [0,0,0]
HAnimJoint446.llimit = [0,0,0]
HAnimSegment447 = x3d.HAnimSegment()
HAnimSegment447.name = "l_scapula"
HAnimSegment447.DEF = "hanim_l_scapula"
Transform448 = x3d.Transform()
Transform448.translation = [0.0962,1.4269,-0.0424]
Transform449 = x3d.Transform()
#Empty Transform
Shape450 = x3d.Shape()
Shape450.USE = "HAnimJointShape"

Transform449.children.append(Shape450)

Transform448.children.append(Transform449)

HAnimSegment447.children.append(Transform448)
Shape451 = x3d.Shape()
LineSet452 = x3d.LineSet()
LineSet452.vertexCount = [2]
Coordinate453 = x3d.Coordinate()

LineSet452.coord = Coordinate453
#from l_acromioclavicular to l_shoulder vertices 2
ColorRGBA454 = x3d.ColorRGBA()
ColorRGBA454.USE = "HAnimSegmentLineColorRGBA"

LineSet452.color = ColorRGBA454

Shape451.geometry = LineSet452

HAnimSegment447.children.append(Shape451)
HAnimSite455 = x3d.HAnimSite()
HAnimSite455.name = "l_bideltoid_pt"
HAnimSite455.DEF = "hanim_l_bideltoid_pt"
TouchSensor456 = x3d.TouchSensor()
TouchSensor456.description = "HAnimSite l_bideltoid_pt"

HAnimSite455.children.append(TouchSensor456)
Shape457 = x3d.Shape()
Shape457.USE = "HAnimSiteShape"

HAnimSite455.children.append(Shape457)

HAnimSegment447.children.append(HAnimSite455)
HAnimSite458 = x3d.HAnimSite()
HAnimSite458.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite458.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite458.translation = [0.228,1.1482,-0.11]
TouchSensor459 = x3d.TouchSensor()
TouchSensor459.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite458.children.append(TouchSensor459)
Shape460 = x3d.Shape()
Shape460.USE = "HAnimSiteShape"

HAnimSite458.children.append(Shape460)

HAnimSegment447.children.append(HAnimSite458)

HAnimJoint446.children.append(HAnimSegment447)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.name = "l_shoulder"
HAnimJoint461.DEF = "hanim_l_shoulder"
HAnimJoint461.center = [0.2029,1.4376,-0.0387]
HAnimJoint461.ulimit = [0,0,0]
HAnimJoint461.llimit = [0,0,0]
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.name = "l_upperarm"
HAnimSegment462.DEF = "hanim_l_upperarm"
Transform463 = x3d.Transform()
Transform463.translation = [0.2029,1.4376,-0.0387]
Transform464 = x3d.Transform()
#Empty Transform
Shape465 = x3d.Shape()
Shape465.USE = "HAnimJointShape"

Transform464.children.append(Shape465)

Transform463.children.append(Transform464)

HAnimSegment462.children.append(Transform463)
Shape466 = x3d.Shape()
LineSet467 = x3d.LineSet()
LineSet467.vertexCount = [2]
Coordinate468 = x3d.Coordinate()

LineSet467.coord = Coordinate468
#from l_shoulder to l_elbow vertices 2
ColorRGBA469 = x3d.ColorRGBA()
ColorRGBA469.USE = "HAnimSegmentLineColorRGBA"

LineSet467.color = ColorRGBA469

Shape466.geometry = LineSet467

HAnimSegment462.children.append(Shape466)
HAnimSite470 = x3d.HAnimSite()
HAnimSite470.name = "l_humeral_medial_epicondyles_pt"
HAnimSite470.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite470.translation = [0.1735,1.1272,-0.1113]
TouchSensor471 = x3d.TouchSensor()
TouchSensor471.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite470.children.append(TouchSensor471)
Shape472 = x3d.Shape()
Shape472.USE = "HAnimSiteShape"

HAnimSite470.children.append(Shape472)

HAnimSegment462.children.append(HAnimSite470)
HAnimSite473 = x3d.HAnimSite()
HAnimSite473.name = "l_olecranon_pt"
HAnimSite473.DEF = "hanim_l_olecranon_pt"
HAnimSite473.translation = [-0.1962,1.1375,-0.1123]
TouchSensor474 = x3d.TouchSensor()
TouchSensor474.description = "HAnimSite l_olecranon_pt"

HAnimSite473.children.append(TouchSensor474)
Shape475 = x3d.Shape()
Shape475.USE = "HAnimSiteShape"

HAnimSite473.children.append(Shape475)

HAnimSegment462.children.append(HAnimSite473)
HAnimSite476 = x3d.HAnimSite()
HAnimSite476.name = "l_radial_styloid_pt"
HAnimSite476.DEF = "hanim_l_radial_styloid_pt"
HAnimSite476.translation = [0.1901,0.8645,-0.0415]
TouchSensor477 = x3d.TouchSensor()
TouchSensor477.description = "HAnimSite l_radial_styloid_pt"

HAnimSite476.children.append(TouchSensor477)
Shape478 = x3d.Shape()
Shape478.USE = "HAnimSiteShape"

HAnimSite476.children.append(Shape478)

HAnimSegment462.children.append(HAnimSite476)
HAnimSite479 = x3d.HAnimSite()
HAnimSite479.name = "l_radiale_pt"
HAnimSite479.DEF = "hanim_l_radiale_pt"
HAnimSite479.translation = [0.2182,1.1212,-0.1167]
TouchSensor480 = x3d.TouchSensor()
TouchSensor480.description = "HAnimSite l_radiale_pt"

HAnimSite479.children.append(TouchSensor480)
Shape481 = x3d.Shape()
Shape481.USE = "HAnimSiteShape"

HAnimSite479.children.append(Shape481)

HAnimSegment462.children.append(HAnimSite479)

HAnimJoint461.children.append(HAnimSegment462)
HAnimJoint482 = x3d.HAnimJoint()
HAnimJoint482.name = "l_elbow"
HAnimJoint482.DEF = "hanim_l_elbow"
HAnimJoint482.center = [0.2014,1.1357,-0.0682]
HAnimJoint482.ulimit = [0,0,0]
HAnimJoint482.llimit = [0,0,0]
HAnimSegment483 = x3d.HAnimSegment()
HAnimSegment483.name = "l_forearm"
HAnimSegment483.DEF = "hanim_l_forearm"
Transform484 = x3d.Transform()
Transform484.translation = [0.2014,1.1357,-0.0682]
Transform485 = x3d.Transform()
#Empty Transform
Shape486 = x3d.Shape()
Shape486.USE = "HAnimJointShape"

Transform485.children.append(Shape486)

Transform484.children.append(Transform485)

HAnimSegment483.children.append(Transform484)
Shape487 = x3d.Shape()
LineSet488 = x3d.LineSet()
LineSet488.vertexCount = [2]
Coordinate489 = x3d.Coordinate()

LineSet488.coord = Coordinate489
#from l_elbow to l_radiocarpal vertices 2
ColorRGBA490 = x3d.ColorRGBA()
ColorRGBA490.USE = "HAnimSegmentLineColorRGBA"

LineSet488.color = ColorRGBA490

Shape487.geometry = LineSet488

HAnimSegment483.children.append(Shape487)
HAnimSite491 = x3d.HAnimSite()
HAnimSite491.name = "l_ulnar_styloid_pt"
HAnimSite491.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite491.translation = [-0.2142,0.8529,-0.0648]
TouchSensor492 = x3d.TouchSensor()
TouchSensor492.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite491.children.append(TouchSensor492)
Shape493 = x3d.Shape()
Shape493.USE = "HAnimSiteShape"

HAnimSite491.children.append(Shape493)

HAnimSegment483.children.append(HAnimSite491)

HAnimJoint482.children.append(HAnimSegment483)
HAnimJoint494 = x3d.HAnimJoint()
HAnimJoint494.name = "l_radiocarpal"
HAnimJoint494.DEF = "hanim_l_radiocarpal"
HAnimJoint494.center = [0.1984,0.8663,-0.0583]
HAnimJoint494.ulimit = [0,0,0]
HAnimJoint494.llimit = [0,0,0]
HAnimSegment495 = x3d.HAnimSegment()
HAnimSegment495.name = "l_carpal"
HAnimSegment495.DEF = "hanim_l_carpal"
Transform496 = x3d.Transform()
Transform496.scale = [0.2,0.2,0.2]
Transform496.translation = [0.2,0.85,-0.05]
Transform496.rotation = [0,0,1,-3.14]
#Transform left hand
Transform497 = x3d.Transform()
Transform497.rotation = [0,1,0,-1.57]
#Transform left hand
Shape498 = x3d.Shape()
Shape498.USE = "HAnimJointShape"

Transform497.children.append(Shape498)

Transform496.children.append(Transform497)

HAnimSegment495.children.append(Transform496)
Shape499 = x3d.Shape()
LineSet500 = x3d.LineSet()
LineSet500.vertexCount = [2]
Coordinate501 = x3d.Coordinate()

LineSet500.coord = Coordinate501
#from l_radiocarpal to l_carpometacarpal_1 vertices 2
ColorRGBA502 = x3d.ColorRGBA()
ColorRGBA502.USE = "HAnimSegmentLineColorRGBA"

LineSet500.color = ColorRGBA502

Shape499.geometry = LineSet500

HAnimSegment495.children.append(Shape499)
Shape503 = x3d.Shape()
LineSet504 = x3d.LineSet()
LineSet504.vertexCount = [2]
Coordinate505 = x3d.Coordinate()

LineSet504.coord = Coordinate505
#from l_radiocarpal to l_carpometacarpal_2 vertices 2
ColorRGBA506 = x3d.ColorRGBA()
ColorRGBA506.USE = "HAnimSegmentLineColorRGBA"

LineSet504.color = ColorRGBA506

Shape503.geometry = LineSet504

HAnimSegment495.children.append(Shape503)
HAnimSite507 = x3d.HAnimSite()
HAnimSite507.name = "l_metacarpal_phalanx_2_pt"
HAnimSite507.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite507.translation = [0.2009,0.8139,-0.0237]
TouchSensor508 = x3d.TouchSensor()
TouchSensor508.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite507.children.append(TouchSensor508)
Shape509 = x3d.Shape()
Shape509.USE = "HAnimSiteShape"

HAnimSite507.children.append(Shape509)

HAnimSegment495.children.append(HAnimSite507)
Shape510 = x3d.Shape()
LineSet511 = x3d.LineSet()
LineSet511.vertexCount = [2]
Coordinate512 = x3d.Coordinate()

LineSet511.coord = Coordinate512
#from l_radiocarpal to l_carpometacarpal_3 vertices 2
ColorRGBA513 = x3d.ColorRGBA()
ColorRGBA513.USE = "HAnimSegmentLineColorRGBA"

LineSet511.color = ColorRGBA513

Shape510.geometry = LineSet511

HAnimSegment495.children.append(Shape510)
HAnimSite514 = x3d.HAnimSite()
HAnimSite514.name = "l_metacarpal_phalanx_3_pt"
HAnimSite514.DEF = "hanim_l_metacarpal_phalanx_3_pt"
TouchSensor515 = x3d.TouchSensor()
TouchSensor515.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite514.children.append(TouchSensor515)
Shape516 = x3d.Shape()
Shape516.USE = "HAnimSiteShape"

HAnimSite514.children.append(Shape516)

HAnimSegment495.children.append(HAnimSite514)
Shape517 = x3d.Shape()
LineSet518 = x3d.LineSet()
LineSet518.vertexCount = [2]
Coordinate519 = x3d.Coordinate()

LineSet518.coord = Coordinate519
#from l_radiocarpal to l_carpometacarpal_4 vertices 2
ColorRGBA520 = x3d.ColorRGBA()
ColorRGBA520.USE = "HAnimSegmentLineColorRGBA"

LineSet518.color = ColorRGBA520

Shape517.geometry = LineSet518

HAnimSegment495.children.append(Shape517)
Shape521 = x3d.Shape()
LineSet522 = x3d.LineSet()
LineSet522.vertexCount = [2]
Coordinate523 = x3d.Coordinate()

LineSet522.coord = Coordinate523
#from l_radiocarpal to l_carpometacarpal_5 vertices 2
ColorRGBA524 = x3d.ColorRGBA()
ColorRGBA524.USE = "HAnimSegmentLineColorRGBA"

LineSet522.color = ColorRGBA524

Shape521.geometry = LineSet522

HAnimSegment495.children.append(Shape521)
HAnimSite525 = x3d.HAnimSite()
HAnimSite525.name = "l_metacarpal_phalanx_5_pt"
HAnimSite525.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite525.translation = [0.1929,0.786,-0.1122]
TouchSensor526 = x3d.TouchSensor()
TouchSensor526.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite525.children.append(TouchSensor526)
Shape527 = x3d.Shape()
Shape527.USE = "HAnimSiteShape"

HAnimSite525.children.append(Shape527)

HAnimSegment495.children.append(HAnimSite525)

HAnimJoint494.children.append(HAnimSegment495)
HAnimJoint528 = x3d.HAnimJoint()
HAnimJoint528.name = "l_carpometacarpal_1"
HAnimJoint528.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint528.center = [0.1924,0.8472,-0.0534]
HAnimJoint528.ulimit = [0,0,0]
HAnimJoint528.llimit = [0,0,0]
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.name = "l_metacarpal_1"
HAnimSegment529.DEF = "hanim_l_metacarpal_1"
Transform530 = x3d.Transform()
Transform530.translation = [0.1924,0.8472,-0.0534]
Transform531 = x3d.Transform()
#Empty Transform
Shape532 = x3d.Shape()
Shape532.USE = "HAnimJointShape"

Transform531.children.append(Shape532)

Transform530.children.append(Transform531)

HAnimSegment529.children.append(Transform530)
Shape533 = x3d.Shape()
LineSet534 = x3d.LineSet()
LineSet534.vertexCount = [2]
Coordinate535 = x3d.Coordinate()

LineSet534.coord = Coordinate535
#from l_carpometacarpal_1 to l_metacarpophalangeal_1 vertices 2
ColorRGBA536 = x3d.ColorRGBA()
ColorRGBA536.USE = "HAnimSegmentLineColorRGBA"

LineSet534.color = ColorRGBA536

Shape533.geometry = LineSet534

HAnimSegment529.children.append(Shape533)

HAnimJoint528.children.append(HAnimSegment529)
HAnimJoint537 = x3d.HAnimJoint()
HAnimJoint537.name = "l_metacarpophalangeal_1"
HAnimJoint537.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint537.center = [0.1951,0.8226,0.0246]
HAnimJoint537.ulimit = [0,0,0]
HAnimJoint537.llimit = [0,0,0]
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.name = "l_carpal_proximal_phalanx_1"
HAnimSegment538.DEF = "hanim_l_carpal_proximal_phalanx_1"
Transform539 = x3d.Transform()
Transform539.translation = [0.1951,0.8226,0.0246]
Transform540 = x3d.Transform()
#Empty Transform
Shape541 = x3d.Shape()
Shape541.USE = "HAnimJointShape"

Transform540.children.append(Shape541)

Transform539.children.append(Transform540)

HAnimSegment538.children.append(Transform539)
Shape542 = x3d.Shape()
LineSet543 = x3d.LineSet()
LineSet543.vertexCount = [2]
Coordinate544 = x3d.Coordinate()

LineSet543.coord = Coordinate544
#from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 vertices 2
ColorRGBA545 = x3d.ColorRGBA()
ColorRGBA545.USE = "HAnimSegmentLineColorRGBA"

LineSet543.color = ColorRGBA545

Shape542.geometry = LineSet543

HAnimSegment538.children.append(Shape542)
HAnimSite546 = x3d.HAnimSite()
HAnimSite546.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite546.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
TouchSensor547 = x3d.TouchSensor()
TouchSensor547.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite546.children.append(TouchSensor547)
Shape548 = x3d.Shape()
Shape548.USE = "HAnimSiteShape"

HAnimSite546.children.append(Shape548)

HAnimSegment538.children.append(HAnimSite546)

HAnimJoint537.children.append(HAnimSegment538)
HAnimJoint549 = x3d.HAnimJoint()
HAnimJoint549.name = "l_carpal_interphalangeal_1"
HAnimJoint549.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint549.center = [0.1955,0.8159,0.0464]
HAnimJoint549.ulimit = [0,0,0]
HAnimJoint549.llimit = [0,0,0]

HAnimJoint537.children.append(HAnimJoint549)

HAnimJoint528.children.append(HAnimJoint537)

HAnimJoint494.children.append(HAnimJoint528)
HAnimJoint550 = x3d.HAnimJoint()
HAnimJoint550.name = "l_carpometacarpal_2"
HAnimJoint550.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint550.center = [0.1983,0.8024,-0.028]
HAnimJoint550.ulimit = [0,0,0]
HAnimJoint550.llimit = [0,0,0]
HAnimSegment551 = x3d.HAnimSegment()
HAnimSegment551.name = "l_metacarpal_2"
HAnimSegment551.DEF = "hanim_l_metacarpal_2"
Transform552 = x3d.Transform()
Transform552.translation = [0.1983,0.8024,-0.028]
Transform553 = x3d.Transform()
#Empty Transform
Shape554 = x3d.Shape()
Shape554.USE = "HAnimJointShape"

Transform553.children.append(Shape554)

Transform552.children.append(Transform553)

HAnimSegment551.children.append(Transform552)
Shape555 = x3d.Shape()
LineSet556 = x3d.LineSet()
LineSet556.vertexCount = [2]
Coordinate557 = x3d.Coordinate()

LineSet556.coord = Coordinate557
#from l_carpometacarpal_2 to l_metacarpophalangeal_2 vertices 2
ColorRGBA558 = x3d.ColorRGBA()
ColorRGBA558.USE = "HAnimSegmentLineColorRGBA"

LineSet556.color = ColorRGBA558

Shape555.geometry = LineSet556

HAnimSegment551.children.append(Shape555)

HAnimJoint550.children.append(HAnimSegment551)
HAnimJoint559 = x3d.HAnimJoint()
HAnimJoint559.name = "l_metacarpophalangeal_2"
HAnimJoint559.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint559.center = [0.1983,0.7815,-0.028]
HAnimJoint559.ulimit = [0,0,0]
HAnimJoint559.llimit = [0,0,0]
HAnimSegment560 = x3d.HAnimSegment()
HAnimSegment560.name = "l_carpal_proximal_phalanx_2"
HAnimSegment560.DEF = "hanim_l_carpal_proximal_phalanx_2"
Transform561 = x3d.Transform()
Transform561.translation = [0.1983,0.7815,-0.028]
Transform562 = x3d.Transform()
#Empty Transform
Shape563 = x3d.Shape()
Shape563.USE = "HAnimJointShape"

Transform562.children.append(Shape563)

Transform561.children.append(Transform562)

HAnimSegment560.children.append(Transform561)
Shape564 = x3d.Shape()
LineSet565 = x3d.LineSet()
LineSet565.vertexCount = [2]
Coordinate566 = x3d.Coordinate()

LineSet565.coord = Coordinate566
#from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 vertices 2
ColorRGBA567 = x3d.ColorRGBA()
ColorRGBA567.USE = "HAnimSegmentLineColorRGBA"

LineSet565.color = ColorRGBA567

Shape564.geometry = LineSet565

HAnimSegment560.children.append(Shape564)

HAnimJoint559.children.append(HAnimSegment560)
HAnimJoint568 = x3d.HAnimJoint()
HAnimJoint568.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint568.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint568.center = [0.2017,0.7363,-0.0248]
HAnimJoint568.ulimit = [0,0,0]
HAnimJoint568.llimit = [0,0,0]
HAnimSegment569 = x3d.HAnimSegment()
HAnimSegment569.name = "l_carpal_middle_phalanx_2"
HAnimSegment569.DEF = "hanim_l_carpal_middle_phalanx_2"
Transform570 = x3d.Transform()
Transform570.translation = [0.2017,0.7363,-0.0248]
Transform571 = x3d.Transform()
#Empty Transform
Shape572 = x3d.Shape()
Shape572.USE = "HAnimJointShape"

Transform571.children.append(Shape572)

Transform570.children.append(Transform571)

HAnimSegment569.children.append(Transform570)
Shape573 = x3d.Shape()
LineSet574 = x3d.LineSet()
LineSet574.vertexCount = [2]
Coordinate575 = x3d.Coordinate()

LineSet574.coord = Coordinate575
#from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 vertices 2
ColorRGBA576 = x3d.ColorRGBA()
ColorRGBA576.USE = "HAnimSegmentLineColorRGBA"

LineSet574.color = ColorRGBA576

Shape573.geometry = LineSet574

HAnimSegment569.children.append(Shape573)
HAnimSite577 = x3d.HAnimSite()
HAnimSite577.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite577.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
TouchSensor578 = x3d.TouchSensor()
TouchSensor578.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite577.children.append(TouchSensor578)
Shape579 = x3d.Shape()
Shape579.USE = "HAnimSiteShape"

HAnimSite577.children.append(Shape579)

HAnimSegment569.children.append(HAnimSite577)
HAnimSite580 = x3d.HAnimSite()
HAnimSite580.name = "l_dactylion_pt"
HAnimSite580.DEF = "hanim_l_dactylion_pt"
HAnimSite580.translation = [0.2056,0.6743,-0.0482]
TouchSensor581 = x3d.TouchSensor()
TouchSensor581.description = "HAnimSite l_dactylion_pt"

HAnimSite580.children.append(TouchSensor581)
Shape582 = x3d.Shape()
Shape582.USE = "HAnimSiteShape"

HAnimSite580.children.append(Shape582)

HAnimSegment569.children.append(HAnimSite580)

HAnimJoint568.children.append(HAnimSegment569)
HAnimJoint583 = x3d.HAnimJoint()
HAnimJoint583.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint583.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint583.center = [0.2028,0.7139,-0.0236]
HAnimJoint583.ulimit = [0,0,0]
HAnimJoint583.llimit = [0,0,0]

HAnimJoint568.children.append(HAnimJoint583)

HAnimJoint559.children.append(HAnimJoint568)

HAnimJoint550.children.append(HAnimJoint559)

HAnimJoint494.children.append(HAnimJoint550)
HAnimJoint584 = x3d.HAnimJoint()
HAnimJoint584.name = "l_carpometacarpal_3"
HAnimJoint584.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint584.center = [0.1987,0.8029,-0.053]
HAnimJoint584.ulimit = [0,0,0]
HAnimJoint584.llimit = [0,0,0]
HAnimSegment585 = x3d.HAnimSegment()
HAnimSegment585.name = "l_metacarpal_3"
HAnimSegment585.DEF = "hanim_l_metacarpal_3"
Transform586 = x3d.Transform()
Transform586.translation = [0.1987,0.8029,-0.053]
Transform587 = x3d.Transform()
#Empty Transform
Shape588 = x3d.Shape()
Shape588.USE = "HAnimJointShape"

Transform587.children.append(Shape588)

Transform586.children.append(Transform587)

HAnimSegment585.children.append(Transform586)
Shape589 = x3d.Shape()
LineSet590 = x3d.LineSet()
LineSet590.vertexCount = [2]
Coordinate591 = x3d.Coordinate()

LineSet590.coord = Coordinate591
#from l_carpometacarpal_3 to l_metacarpophalangeal_3 vertices 2
ColorRGBA592 = x3d.ColorRGBA()
ColorRGBA592.USE = "HAnimSegmentLineColorRGBA"

LineSet590.color = ColorRGBA592

Shape589.geometry = LineSet590

HAnimSegment585.children.append(Shape589)

HAnimJoint584.children.append(HAnimSegment585)
HAnimJoint593 = x3d.HAnimJoint()
HAnimJoint593.name = "l_metacarpophalangeal_3"
HAnimJoint593.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint593.center = [0.1987,0.7818,-0.053]
HAnimJoint593.ulimit = [0,0,0]
HAnimJoint593.llimit = [0,0,0]
HAnimSegment594 = x3d.HAnimSegment()
HAnimSegment594.name = "l_carpal_proximal_phalanx_3"
HAnimSegment594.DEF = "hanim_l_carpal_proximal_phalanx_3"
Transform595 = x3d.Transform()
Transform595.translation = [0.1987,0.7818,-0.053]
Transform596 = x3d.Transform()
#Empty Transform
Shape597 = x3d.Shape()
Shape597.USE = "HAnimJointShape"

Transform596.children.append(Shape597)

Transform595.children.append(Transform596)

HAnimSegment594.children.append(Transform595)
Shape598 = x3d.Shape()
LineSet599 = x3d.LineSet()
LineSet599.vertexCount = [2]
Coordinate600 = x3d.Coordinate()

LineSet599.coord = Coordinate600
#from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 vertices 2
ColorRGBA601 = x3d.ColorRGBA()
ColorRGBA601.USE = "HAnimSegmentLineColorRGBA"

LineSet599.color = ColorRGBA601

Shape598.geometry = LineSet599

HAnimSegment594.children.append(Shape598)

HAnimJoint593.children.append(HAnimSegment594)
HAnimJoint602 = x3d.HAnimJoint()
HAnimJoint602.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint602.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint602.center = [0.2013,0.7273,-0.0503]
HAnimJoint602.ulimit = [0,0,0]
HAnimJoint602.llimit = [0,0,0]
HAnimSegment603 = x3d.HAnimSegment()
HAnimSegment603.name = "l_carpal_middle_phalanx_3"
HAnimSegment603.DEF = "hanim_l_carpal_middle_phalanx_3"
Transform604 = x3d.Transform()
Transform604.translation = [0.2013,0.7273,-0.0503]
Transform605 = x3d.Transform()
#Empty Transform
Shape606 = x3d.Shape()
Shape606.USE = "HAnimJointShape"

Transform605.children.append(Shape606)

Transform604.children.append(Transform605)

HAnimSegment603.children.append(Transform604)
Shape607 = x3d.Shape()
LineSet608 = x3d.LineSet()
LineSet608.vertexCount = [2]
Coordinate609 = x3d.Coordinate()

LineSet608.coord = Coordinate609
#from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 vertices 2
ColorRGBA610 = x3d.ColorRGBA()
ColorRGBA610.USE = "HAnimSegmentLineColorRGBA"

LineSet608.color = ColorRGBA610

Shape607.geometry = LineSet608

HAnimSegment603.children.append(Shape607)
HAnimSite611 = x3d.HAnimSite()
HAnimSite611.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite611.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
TouchSensor612 = x3d.TouchSensor()
TouchSensor612.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite611.children.append(TouchSensor612)
Shape613 = x3d.Shape()
Shape613.USE = "HAnimSiteShape"

HAnimSite611.children.append(Shape613)

HAnimSegment603.children.append(HAnimSite611)

HAnimJoint602.children.append(HAnimSegment603)
HAnimJoint614 = x3d.HAnimJoint()
HAnimJoint614.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint614.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint614.center = [0.2026,0.7011,-0.0494]
HAnimJoint614.ulimit = [0,0,0]
HAnimJoint614.llimit = [0,0,0]

HAnimJoint602.children.append(HAnimJoint614)

HAnimJoint593.children.append(HAnimJoint602)

HAnimJoint584.children.append(HAnimJoint593)

HAnimJoint494.children.append(HAnimJoint584)
HAnimJoint615 = x3d.HAnimJoint()
HAnimJoint615.name = "l_carpometacarpal_4"
HAnimJoint615.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint615.center = [0.1956,0.8019,-0.0794]
HAnimJoint615.ulimit = [0,0,0]
HAnimJoint615.llimit = [0,0,0]
HAnimSegment616 = x3d.HAnimSegment()
HAnimSegment616.name = "l_metacarpal_4"
HAnimSegment616.DEF = "hanim_l_metacarpal_4"
Transform617 = x3d.Transform()
Transform617.translation = [0.1956,0.8019,-0.0794]
Transform618 = x3d.Transform()
#Empty Transform
Shape619 = x3d.Shape()
Shape619.USE = "HAnimJointShape"

Transform618.children.append(Shape619)

Transform617.children.append(Transform618)

HAnimSegment616.children.append(Transform617)
Shape620 = x3d.Shape()
LineSet621 = x3d.LineSet()
LineSet621.vertexCount = [2]
Coordinate622 = x3d.Coordinate()

LineSet621.coord = Coordinate622
#from l_carpometacarpal_4 to l_metacarpophalangeal_4 vertices 2
ColorRGBA623 = x3d.ColorRGBA()
ColorRGBA623.USE = "HAnimSegmentLineColorRGBA"

LineSet621.color = ColorRGBA623

Shape620.geometry = LineSet621

HAnimSegment616.children.append(Shape620)

HAnimJoint615.children.append(HAnimSegment616)
HAnimJoint624 = x3d.HAnimJoint()
HAnimJoint624.name = "l_metacarpophalangeal_4"
HAnimJoint624.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint624.center = [0.1956,0.7815,-0.0794]
HAnimJoint624.ulimit = [0,0,0]
HAnimJoint624.llimit = [0,0,0]
HAnimSegment625 = x3d.HAnimSegment()
HAnimSegment625.name = "l_carpal_proximal_phalanx_4"
HAnimSegment625.DEF = "hanim_l_carpal_proximal_phalanx_4"
Transform626 = x3d.Transform()
Transform626.translation = [0.1956,0.7815,-0.0794]
Transform627 = x3d.Transform()
#Empty Transform
Shape628 = x3d.Shape()
Shape628.USE = "HAnimJointShape"

Transform627.children.append(Shape628)

Transform626.children.append(Transform627)

HAnimSegment625.children.append(Transform626)
Shape629 = x3d.Shape()
LineSet630 = x3d.LineSet()
LineSet630.vertexCount = [2]
Coordinate631 = x3d.Coordinate()

LineSet630.coord = Coordinate631
#from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 vertices 2
ColorRGBA632 = x3d.ColorRGBA()
ColorRGBA632.USE = "HAnimSegmentLineColorRGBA"

LineSet630.color = ColorRGBA632

Shape629.geometry = LineSet630

HAnimSegment625.children.append(Shape629)

HAnimJoint624.children.append(HAnimSegment625)
HAnimJoint633 = x3d.HAnimJoint()
HAnimJoint633.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint633.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint633.center = [0.1973,0.7287,-0.0777]
HAnimJoint633.ulimit = [0,0,0]
HAnimJoint633.llimit = [0,0,0]
HAnimSegment634 = x3d.HAnimSegment()
HAnimSegment634.name = "l_carpal_middle_phalanx_4"
HAnimSegment634.DEF = "hanim_l_carpal_middle_phalanx_4"
Transform635 = x3d.Transform()
Transform635.translation = [0.1973,0.7287,-0.0777]
Transform636 = x3d.Transform()
#Empty Transform
Shape637 = x3d.Shape()
Shape637.USE = "HAnimJointShape"

Transform636.children.append(Shape637)

Transform635.children.append(Transform636)

HAnimSegment634.children.append(Transform635)
Shape638 = x3d.Shape()
LineSet639 = x3d.LineSet()
LineSet639.vertexCount = [2]
Coordinate640 = x3d.Coordinate()

LineSet639.coord = Coordinate640
#from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 vertices 2
ColorRGBA641 = x3d.ColorRGBA()
ColorRGBA641.USE = "HAnimSegmentLineColorRGBA"

LineSet639.color = ColorRGBA641

Shape638.geometry = LineSet639

HAnimSegment634.children.append(Shape638)
HAnimSite642 = x3d.HAnimSite()
HAnimSite642.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite642.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
TouchSensor643 = x3d.TouchSensor()
TouchSensor643.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite642.children.append(TouchSensor643)
Shape644 = x3d.Shape()
Shape644.USE = "HAnimSiteShape"

HAnimSite642.children.append(Shape644)

HAnimSegment634.children.append(HAnimSite642)

HAnimJoint633.children.append(HAnimSegment634)
HAnimJoint645 = x3d.HAnimJoint()
HAnimJoint645.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint645.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint645.center = [0.1983,0.7045,-0.0767]
HAnimJoint645.ulimit = [0,0,0]
HAnimJoint645.llimit = [0,0,0]

HAnimJoint633.children.append(HAnimJoint645)

HAnimJoint624.children.append(HAnimJoint633)

HAnimJoint615.children.append(HAnimJoint624)

HAnimJoint494.children.append(HAnimJoint615)
HAnimJoint646 = x3d.HAnimJoint()
HAnimJoint646.name = "l_carpometacarpal_5"
HAnimJoint646.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint646.center = [0.1925,0.8066,-0.1036]
HAnimJoint646.ulimit = [0,0,0]
HAnimJoint646.llimit = [0,0,0]
HAnimSegment647 = x3d.HAnimSegment()
HAnimSegment647.name = "l_metacarpal_5"
HAnimSegment647.DEF = "hanim_l_metacarpal_5"
Transform648 = x3d.Transform()
Transform648.translation = [0.1925,0.8066,-0.1036]
Transform649 = x3d.Transform()
#Empty Transform
Shape650 = x3d.Shape()
Shape650.USE = "HAnimJointShape"

Transform649.children.append(Shape650)

Transform648.children.append(Transform649)

HAnimSegment647.children.append(Transform648)
Shape651 = x3d.Shape()
LineSet652 = x3d.LineSet()
LineSet652.vertexCount = [2]
Coordinate653 = x3d.Coordinate()

LineSet652.coord = Coordinate653
#from l_carpometacarpal_5 to l_metacarpophalangeal_5 vertices 2
ColorRGBA654 = x3d.ColorRGBA()
ColorRGBA654.USE = "HAnimSegmentLineColorRGBA"

LineSet652.color = ColorRGBA654

Shape651.geometry = LineSet652

HAnimSegment647.children.append(Shape651)

HAnimJoint646.children.append(HAnimSegment647)
HAnimJoint655 = x3d.HAnimJoint()
HAnimJoint655.name = "l_metacarpophalangeal_5"
HAnimJoint655.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint655.center = [0.1925,0.7866,-0.1036]
HAnimJoint655.ulimit = [0,0,0]
HAnimJoint655.llimit = [0,0,0]
HAnimSegment656 = x3d.HAnimSegment()
HAnimSegment656.name = "l_carpal_proximal_phalanx_5"
HAnimSegment656.DEF = "hanim_l_carpal_proximal_phalanx_5"
Transform657 = x3d.Transform()
Transform657.translation = [0.1925,0.7866,-0.1036]
Transform658 = x3d.Transform()
#Empty Transform
Shape659 = x3d.Shape()
Shape659.USE = "HAnimJointShape"

Transform658.children.append(Shape659)

Transform657.children.append(Transform658)

HAnimSegment656.children.append(Transform657)
Shape660 = x3d.Shape()
LineSet661 = x3d.LineSet()
LineSet661.vertexCount = [2]
Coordinate662 = x3d.Coordinate()

LineSet661.coord = Coordinate662
#from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 vertices 2
ColorRGBA663 = x3d.ColorRGBA()
ColorRGBA663.USE = "HAnimSegmentLineColorRGBA"

LineSet661.color = ColorRGBA663

Shape660.geometry = LineSet661

HAnimSegment656.children.append(Shape660)

HAnimJoint655.children.append(HAnimSegment656)
HAnimJoint664 = x3d.HAnimJoint()
HAnimJoint664.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint664.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint664.center = [0.1938,0.7452,-0.1024]
HAnimJoint664.ulimit = [0,0,0]
HAnimJoint664.llimit = [0,0,0]
HAnimSegment665 = x3d.HAnimSegment()
HAnimSegment665.name = "l_carpal_middle_phalanx_5"
HAnimSegment665.DEF = "hanim_l_carpal_middle_phalanx_5"
Transform666 = x3d.Transform()
Transform666.translation = [0.1938,0.7452,-0.1024]
Transform667 = x3d.Transform()
#Empty Transform
Shape668 = x3d.Shape()
Shape668.USE = "HAnimJointShape"

Transform667.children.append(Shape668)

Transform666.children.append(Transform667)

HAnimSegment665.children.append(Transform666)
Shape669 = x3d.Shape()
LineSet670 = x3d.LineSet()
LineSet670.vertexCount = [2]
Coordinate671 = x3d.Coordinate()

LineSet670.coord = Coordinate671
#from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 vertices 2
ColorRGBA672 = x3d.ColorRGBA()
ColorRGBA672.USE = "HAnimSegmentLineColorRGBA"

LineSet670.color = ColorRGBA672

Shape669.geometry = LineSet670

HAnimSegment665.children.append(Shape669)
HAnimSite673 = x3d.HAnimSite()
HAnimSite673.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite673.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
TouchSensor674 = x3d.TouchSensor()
TouchSensor674.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite673.children.append(TouchSensor674)
Shape675 = x3d.Shape()
Shape675.USE = "HAnimSiteShape"

HAnimSite673.children.append(Shape675)

HAnimSegment665.children.append(HAnimSite673)

HAnimJoint664.children.append(HAnimSegment665)
HAnimJoint676 = x3d.HAnimJoint()
HAnimJoint676.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint676.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint676.center = [0.1948,0.7277,-0.1017]
HAnimJoint676.ulimit = [0,0,0]
HAnimJoint676.llimit = [0,0,0]

HAnimJoint664.children.append(HAnimJoint676)

HAnimJoint655.children.append(HAnimJoint664)

HAnimJoint646.children.append(HAnimJoint655)

HAnimJoint494.children.append(HAnimJoint646)

HAnimJoint482.children.append(HAnimJoint494)

HAnimJoint461.children.append(HAnimJoint482)

HAnimJoint446.children.append(HAnimJoint461)

HAnimJoint437.children.append(HAnimJoint446)

HAnimJoint335.children.append(HAnimJoint437)
HAnimJoint677 = x3d.HAnimJoint()
HAnimJoint677.name = "r_sternoclavicular"
HAnimJoint677.DEF = "hanim_r_sternoclavicular"
HAnimJoint677.center = [-0.0694,1.46,-0.033]
HAnimJoint677.ulimit = [0,0,0]
HAnimJoint677.llimit = [0,0,0]
HAnimSegment678 = x3d.HAnimSegment()
HAnimSegment678.name = "r_clavicle"
HAnimSegment678.DEF = "hanim_r_clavicle"
Transform679 = x3d.Transform()
Transform679.translation = [-0.0694,1.46,-0.033]
Transform680 = x3d.Transform()
#Empty Transform
Shape681 = x3d.Shape()
Shape681.USE = "HAnimJointShape"

Transform680.children.append(Shape681)

Transform679.children.append(Transform680)

HAnimSegment678.children.append(Transform679)
Shape682 = x3d.Shape()
LineSet683 = x3d.LineSet()
LineSet683.vertexCount = [2]
Coordinate684 = x3d.Coordinate()

LineSet683.coord = Coordinate684
#from r_sternoclavicular to r_acromioclavicular vertices 2
ColorRGBA685 = x3d.ColorRGBA()
ColorRGBA685.USE = "HAnimSegmentLineColorRGBA"

LineSet683.color = ColorRGBA685

Shape682.geometry = LineSet683

HAnimSegment678.children.append(Shape682)

HAnimJoint677.children.append(HAnimSegment678)
HAnimJoint686 = x3d.HAnimJoint()
HAnimJoint686.name = "r_acromioclavicular"
HAnimJoint686.DEF = "hanim_r_acromioclavicular"
HAnimJoint686.center = [-0.0836,1.4281,-0.0401]
HAnimJoint686.ulimit = [0,0,0]
HAnimJoint686.llimit = [0,0,0]
HAnimSegment687 = x3d.HAnimSegment()
HAnimSegment687.name = "r_scapula"
HAnimSegment687.DEF = "hanim_r_scapula"
Transform688 = x3d.Transform()
Transform688.translation = [-0.0836,1.4281,-0.0401]
Transform689 = x3d.Transform()
#Empty Transform
Shape690 = x3d.Shape()
Shape690.USE = "HAnimJointShape"

Transform689.children.append(Shape690)

Transform688.children.append(Transform689)

HAnimSegment687.children.append(Transform688)
Shape691 = x3d.Shape()
LineSet692 = x3d.LineSet()
LineSet692.vertexCount = [2]
Coordinate693 = x3d.Coordinate()

LineSet692.coord = Coordinate693
#from r_acromioclavicular to r_shoulder vertices 2
ColorRGBA694 = x3d.ColorRGBA()
ColorRGBA694.USE = "HAnimSegmentLineColorRGBA"

LineSet692.color = ColorRGBA694

Shape691.geometry = LineSet692

HAnimSegment687.children.append(Shape691)
HAnimSite695 = x3d.HAnimSite()
HAnimSite695.name = "r_bideltoid_pt"
HAnimSite695.DEF = "hanim_r_bideltoid_pt"
TouchSensor696 = x3d.TouchSensor()
TouchSensor696.description = "HAnimSite r_bideltoid_pt"

HAnimSite695.children.append(TouchSensor696)
Shape697 = x3d.Shape()
Shape697.USE = "HAnimSiteShape"

HAnimSite695.children.append(Shape697)

HAnimSegment687.children.append(HAnimSite695)
HAnimSite698 = x3d.HAnimSite()
HAnimSite698.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite698.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite698.translation = [-0.2224,1.1517,-0.1033]
TouchSensor699 = x3d.TouchSensor()
TouchSensor699.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite698.children.append(TouchSensor699)
Shape700 = x3d.Shape()
Shape700.USE = "HAnimSiteShape"

HAnimSite698.children.append(Shape700)

HAnimSegment687.children.append(HAnimSite698)

HAnimJoint686.children.append(HAnimSegment687)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.name = "r_shoulder"
HAnimJoint701.DEF = "hanim_r_shoulder"
HAnimJoint701.center = [-0.1907,1.4407,-0.0325]
HAnimJoint701.ulimit = [0,0,0]
HAnimJoint701.llimit = [0,0,0]
HAnimSegment702 = x3d.HAnimSegment()
HAnimSegment702.name = "r_upperarm"
HAnimSegment702.DEF = "hanim_r_upperarm"
Transform703 = x3d.Transform()
Transform703.translation = [-0.1907,1.4407,-0.0325]
Transform704 = x3d.Transform()
#Empty Transform
Shape705 = x3d.Shape()
Shape705.USE = "HAnimJointShape"

Transform704.children.append(Shape705)

Transform703.children.append(Transform704)

HAnimSegment702.children.append(Transform703)
Shape706 = x3d.Shape()
LineSet707 = x3d.LineSet()
LineSet707.vertexCount = [2]
Coordinate708 = x3d.Coordinate()

LineSet707.coord = Coordinate708
#from r_shoulder to r_elbow vertices 2
ColorRGBA709 = x3d.ColorRGBA()
ColorRGBA709.USE = "HAnimSegmentLineColorRGBA"

LineSet707.color = ColorRGBA709

Shape706.geometry = LineSet707

HAnimSegment702.children.append(Shape706)
HAnimSite710 = x3d.HAnimSite()
HAnimSite710.name = "r_humeral_medial_epicondyles_pt"
HAnimSite710.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite710.translation = [-0.168,1.1298,-0.1062]
TouchSensor711 = x3d.TouchSensor()
TouchSensor711.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite710.children.append(TouchSensor711)
Shape712 = x3d.Shape()
Shape712.USE = "HAnimSiteShape"

HAnimSite710.children.append(Shape712)

HAnimSegment702.children.append(HAnimSite710)
HAnimSite713 = x3d.HAnimSite()
HAnimSite713.name = "r_olecranon_pt"
HAnimSite713.DEF = "hanim_r_olecranon_pt"
HAnimSite713.translation = [-0.1907,1.1405,-0.1065]
TouchSensor714 = x3d.TouchSensor()
TouchSensor714.description = "HAnimSite r_olecranon_pt"

HAnimSite713.children.append(TouchSensor714)
Shape715 = x3d.Shape()
Shape715.USE = "HAnimSiteShape"

HAnimSite713.children.append(Shape715)

HAnimSegment702.children.append(HAnimSite713)
HAnimSite716 = x3d.HAnimSite()
HAnimSite716.name = "r_radial_styloid_pt"
HAnimSite716.DEF = "hanim_r_radial_styloid_pt"
HAnimSite716.translation = [-0.1884,0.8676,-0.036]
TouchSensor717 = x3d.TouchSensor()
TouchSensor717.description = "HAnimSite r_radial_styloid_pt"

HAnimSite716.children.append(TouchSensor717)
Shape718 = x3d.Shape()
Shape718.USE = "HAnimSiteShape"

HAnimSite716.children.append(Shape718)

HAnimSegment702.children.append(HAnimSite716)
HAnimSite719 = x3d.HAnimSite()
HAnimSite719.name = "r_radiale_pt"
HAnimSite719.DEF = "hanim_r_radiale_pt"
HAnimSite719.translation = [-0.213,1.1305,-0.1091]
TouchSensor720 = x3d.TouchSensor()
TouchSensor720.description = "HAnimSite r_radiale_pt"

HAnimSite719.children.append(TouchSensor720)
Shape721 = x3d.Shape()
Shape721.USE = "HAnimSiteShape"

HAnimSite719.children.append(Shape721)

HAnimSegment702.children.append(HAnimSite719)

HAnimJoint701.children.append(HAnimSegment702)
HAnimJoint722 = x3d.HAnimJoint()
HAnimJoint722.name = "r_elbow"
HAnimJoint722.DEF = "hanim_r_elbow"
HAnimJoint722.center = [-0.1949,1.1388,-0.062]
HAnimJoint722.ulimit = [0,0,0]
HAnimJoint722.llimit = [0,0,0]
HAnimSegment723 = x3d.HAnimSegment()
HAnimSegment723.name = "r_forearm"
HAnimSegment723.DEF = "hanim_r_forearm"
Transform724 = x3d.Transform()
Transform724.translation = [-0.1949,1.1388,-0.062]
Transform725 = x3d.Transform()
#Empty Transform
Shape726 = x3d.Shape()
Shape726.USE = "HAnimJointShape"

Transform725.children.append(Shape726)

Transform724.children.append(Transform725)

HAnimSegment723.children.append(Transform724)
Shape727 = x3d.Shape()
LineSet728 = x3d.LineSet()
LineSet728.vertexCount = [2]
Coordinate729 = x3d.Coordinate()

LineSet728.coord = Coordinate729
#from r_elbow to r_radiocarpal vertices 2
ColorRGBA730 = x3d.ColorRGBA()
ColorRGBA730.USE = "HAnimSegmentLineColorRGBA"

LineSet728.color = ColorRGBA730

Shape727.geometry = LineSet728

HAnimSegment723.children.append(Shape727)
HAnimSite731 = x3d.HAnimSite()
HAnimSite731.name = "r_ulnar_styloid_pt"
HAnimSite731.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite731.translation = [-0.2117,0.8562,-0.0584]
TouchSensor732 = x3d.TouchSensor()
TouchSensor732.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite731.children.append(TouchSensor732)
Shape733 = x3d.Shape()
Shape733.USE = "HAnimSiteShape"

HAnimSite731.children.append(Shape733)

HAnimSegment723.children.append(HAnimSite731)

HAnimJoint722.children.append(HAnimSegment723)
HAnimJoint734 = x3d.HAnimJoint()
HAnimJoint734.name = "r_radiocarpal"
HAnimJoint734.DEF = "hanim_r_radiocarpal"
HAnimJoint734.center = [-0.1959,0.8694,-0.0521]
HAnimJoint734.ulimit = [0,0,0]
HAnimJoint734.llimit = [0,0,0]
HAnimSegment735 = x3d.HAnimSegment()
HAnimSegment735.name = "r_carpal"
HAnimSegment735.DEF = "hanim_r_carpal"
Transform736 = x3d.Transform()
Transform736.scale = [0.2,0.2,0.2]
Transform736.translation = [-0.2,0.85,-0.05]
Transform736.rotation = [0,0,1,-3.14]
#Transform right hand
Transform737 = x3d.Transform()
Transform737.rotation = [0,1,0,1.57]
#Transform right hand
Shape738 = x3d.Shape()
Shape738.USE = "HAnimJointShape"

Transform737.children.append(Shape738)

Transform736.children.append(Transform737)

HAnimSegment735.children.append(Transform736)
Shape739 = x3d.Shape()
LineSet740 = x3d.LineSet()
LineSet740.vertexCount = [2]
Coordinate741 = x3d.Coordinate()

LineSet740.coord = Coordinate741
#from r_radiocarpal to r_carpometacarpal_1 vertices 2
ColorRGBA742 = x3d.ColorRGBA()
ColorRGBA742.USE = "HAnimSegmentLineColorRGBA"

LineSet740.color = ColorRGBA742

Shape739.geometry = LineSet740

HAnimSegment735.children.append(Shape739)
Shape743 = x3d.Shape()
LineSet744 = x3d.LineSet()
LineSet744.vertexCount = [2]
Coordinate745 = x3d.Coordinate()

LineSet744.coord = Coordinate745
#from r_radiocarpal to r_carpometacarpal_2 vertices 2
ColorRGBA746 = x3d.ColorRGBA()
ColorRGBA746.USE = "HAnimSegmentLineColorRGBA"

LineSet744.color = ColorRGBA746

Shape743.geometry = LineSet744

HAnimSegment735.children.append(Shape743)
HAnimSite747 = x3d.HAnimSite()
HAnimSite747.name = "r_metacarpal_phalanx_2_pt"
HAnimSite747.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite747.translation = [-0.1977,0.8169,-0.0177]
TouchSensor748 = x3d.TouchSensor()
TouchSensor748.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite747.children.append(TouchSensor748)
Shape749 = x3d.Shape()
Shape749.USE = "HAnimSiteShape"

HAnimSite747.children.append(Shape749)

HAnimSegment735.children.append(HAnimSite747)
Shape750 = x3d.Shape()
LineSet751 = x3d.LineSet()
LineSet751.vertexCount = [2]
Coordinate752 = x3d.Coordinate()

LineSet751.coord = Coordinate752
#from r_radiocarpal to r_carpometacarpal_3 vertices 2
ColorRGBA753 = x3d.ColorRGBA()
ColorRGBA753.USE = "HAnimSegmentLineColorRGBA"

LineSet751.color = ColorRGBA753

Shape750.geometry = LineSet751

HAnimSegment735.children.append(Shape750)
HAnimSite754 = x3d.HAnimSite()
HAnimSite754.name = "r_metacarpal_phalanx_3_pt"
HAnimSite754.DEF = "hanim_r_metacarpal_phalanx_3_pt"
TouchSensor755 = x3d.TouchSensor()
TouchSensor755.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite754.children.append(TouchSensor755)
Shape756 = x3d.Shape()
Shape756.USE = "HAnimSiteShape"

HAnimSite754.children.append(Shape756)

HAnimSegment735.children.append(HAnimSite754)
Shape757 = x3d.Shape()
LineSet758 = x3d.LineSet()
LineSet758.vertexCount = [2]
Coordinate759 = x3d.Coordinate()

LineSet758.coord = Coordinate759
#from r_radiocarpal to r_carpometacarpal_4 vertices 2
ColorRGBA760 = x3d.ColorRGBA()
ColorRGBA760.USE = "HAnimSegmentLineColorRGBA"

LineSet758.color = ColorRGBA760

Shape757.geometry = LineSet758

HAnimSegment735.children.append(Shape757)
Shape761 = x3d.Shape()
LineSet762 = x3d.LineSet()
LineSet762.vertexCount = [2]
Coordinate763 = x3d.Coordinate()

LineSet762.coord = Coordinate763
#from r_radiocarpal to r_carpometacarpal_5 vertices 2
ColorRGBA764 = x3d.ColorRGBA()
ColorRGBA764.USE = "HAnimSegmentLineColorRGBA"

LineSet762.color = ColorRGBA764

Shape761.geometry = LineSet762

HAnimSegment735.children.append(Shape761)
HAnimSite765 = x3d.HAnimSite()
HAnimSite765.name = "r_metacarpal_phalanx_5_pt"
HAnimSite765.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite765.translation = [-0.1929,0.789,-0.1064]
TouchSensor766 = x3d.TouchSensor()
TouchSensor766.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite765.children.append(TouchSensor766)
Shape767 = x3d.Shape()
Shape767.USE = "HAnimSiteShape"

HAnimSite765.children.append(Shape767)

HAnimSegment735.children.append(HAnimSite765)

HAnimJoint734.children.append(HAnimSegment735)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.name = "r_carpometacarpal_1"
HAnimJoint768.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint768.center = [-0.1899,0.8502,-0.0473]
HAnimJoint768.ulimit = [0,0,0]
HAnimJoint768.llimit = [0,0,0]
HAnimSegment769 = x3d.HAnimSegment()
HAnimSegment769.name = "r_metacarpal_1"
HAnimSegment769.DEF = "hanim_r_metacarpal_1"
Transform770 = x3d.Transform()
Transform770.translation = [-0.1899,0.8502,-0.0473]
Transform771 = x3d.Transform()
#Empty Transform
Shape772 = x3d.Shape()
Shape772.USE = "HAnimJointShape"

Transform771.children.append(Shape772)

Transform770.children.append(Transform771)

HAnimSegment769.children.append(Transform770)
Shape773 = x3d.Shape()
LineSet774 = x3d.LineSet()
LineSet774.vertexCount = [2]
Coordinate775 = x3d.Coordinate()

LineSet774.coord = Coordinate775
#from r_carpometacarpal_1 to r_metacarpophalangeal_1 vertices 2
ColorRGBA776 = x3d.ColorRGBA()
ColorRGBA776.USE = "HAnimSegmentLineColorRGBA"

LineSet774.color = ColorRGBA776

Shape773.geometry = LineSet774

HAnimSegment769.children.append(Shape773)

HAnimJoint768.children.append(HAnimSegment769)
HAnimJoint777 = x3d.HAnimJoint()
HAnimJoint777.name = "r_metacarpophalangeal_1"
HAnimJoint777.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint777.center = [-0.1874,0.8256,0.0306]
HAnimJoint777.ulimit = [0,0,0]
HAnimJoint777.llimit = [0,0,0]
HAnimSegment778 = x3d.HAnimSegment()
HAnimSegment778.name = "r_carpal_proximal_phalanx_1"
HAnimSegment778.DEF = "hanim_r_carpal_proximal_phalanx_1"
Transform779 = x3d.Transform()
Transform779.translation = [-0.1874,0.8256,0.0306]
Transform780 = x3d.Transform()
#Empty Transform
Shape781 = x3d.Shape()
Shape781.USE = "HAnimJointShape"

Transform780.children.append(Shape781)

Transform779.children.append(Transform780)

HAnimSegment778.children.append(Transform779)
Shape782 = x3d.Shape()
LineSet783 = x3d.LineSet()
LineSet783.vertexCount = [2]
Coordinate784 = x3d.Coordinate()

LineSet783.coord = Coordinate784
#from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 vertices 2
ColorRGBA785 = x3d.ColorRGBA()
ColorRGBA785.USE = "HAnimSegmentLineColorRGBA"

LineSet783.color = ColorRGBA785

Shape782.geometry = LineSet783

HAnimSegment778.children.append(Shape782)
HAnimSite786 = x3d.HAnimSite()
HAnimSite786.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite786.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
TouchSensor787 = x3d.TouchSensor()
TouchSensor787.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite786.children.append(TouchSensor787)
Shape788 = x3d.Shape()
Shape788.USE = "HAnimSiteShape"

HAnimSite786.children.append(Shape788)

HAnimSegment778.children.append(HAnimSite786)

HAnimJoint777.children.append(HAnimSegment778)
HAnimJoint789 = x3d.HAnimJoint()
HAnimJoint789.name = "r_carpal_interphalangeal_1"
HAnimJoint789.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint789.center = [-0.1864,0.819,0.0506]
HAnimJoint789.ulimit = [0,0,0]
HAnimJoint789.llimit = [0,0,0]

HAnimJoint777.children.append(HAnimJoint789)

HAnimJoint768.children.append(HAnimJoint777)

HAnimJoint734.children.append(HAnimJoint768)
HAnimJoint790 = x3d.HAnimJoint()
HAnimJoint790.name = "r_carpometacarpal_2"
HAnimJoint790.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint790.center = [-0.1961,0.8055,-0.0218]
HAnimJoint790.ulimit = [0,0,0]
HAnimJoint790.llimit = [0,0,0]
HAnimSegment791 = x3d.HAnimSegment()
HAnimSegment791.name = "r_metacarpal_2"
HAnimSegment791.DEF = "hanim_r_metacarpal_2"
Transform792 = x3d.Transform()
Transform792.translation = [-0.1961,0.8055,-0.0218]
Transform793 = x3d.Transform()
#Empty Transform
Shape794 = x3d.Shape()
Shape794.USE = "HAnimJointShape"

Transform793.children.append(Shape794)

Transform792.children.append(Transform793)

HAnimSegment791.children.append(Transform792)
Shape795 = x3d.Shape()
LineSet796 = x3d.LineSet()
LineSet796.vertexCount = [2]
Coordinate797 = x3d.Coordinate()

LineSet796.coord = Coordinate797
#from r_carpometacarpal_2 to r_metacarpophalangeal_2 vertices 2
ColorRGBA798 = x3d.ColorRGBA()
ColorRGBA798.USE = "HAnimSegmentLineColorRGBA"

LineSet796.color = ColorRGBA798

Shape795.geometry = LineSet796

HAnimSegment791.children.append(Shape795)

HAnimJoint790.children.append(HAnimSegment791)
HAnimJoint799 = x3d.HAnimJoint()
HAnimJoint799.name = "r_metacarpophalangeal_2"
HAnimJoint799.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint799.center = [-0.1961,0.7846,-0.0218]
HAnimJoint799.ulimit = [0,0,0]
HAnimJoint799.llimit = [0,0,0]
HAnimSegment800 = x3d.HAnimSegment()
HAnimSegment800.name = "r_carpal_proximal_phalanx_2"
HAnimSegment800.DEF = "hanim_r_carpal_proximal_phalanx_2"
Transform801 = x3d.Transform()
Transform801.translation = [-0.1961,0.7846,-0.0218]
Transform802 = x3d.Transform()
#Empty Transform
Shape803 = x3d.Shape()
Shape803.USE = "HAnimJointShape"

Transform802.children.append(Shape803)

Transform801.children.append(Transform802)

HAnimSegment800.children.append(Transform801)
Shape804 = x3d.Shape()
LineSet805 = x3d.LineSet()
LineSet805.vertexCount = [2]
Coordinate806 = x3d.Coordinate()

LineSet805.coord = Coordinate806
#from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 vertices 2
ColorRGBA807 = x3d.ColorRGBA()
ColorRGBA807.USE = "HAnimSegmentLineColorRGBA"

LineSet805.color = ColorRGBA807

Shape804.geometry = LineSet805

HAnimSegment800.children.append(Shape804)

HAnimJoint799.children.append(HAnimSegment800)
HAnimJoint808 = x3d.HAnimJoint()
HAnimJoint808.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint808.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint808.center = [-0.1954,0.7393,-0.0185]
HAnimJoint808.ulimit = [0,0,0]
HAnimJoint808.llimit = [0,0,0]
HAnimSegment809 = x3d.HAnimSegment()
HAnimSegment809.name = "r_carpal_middle_phalanx_2"
HAnimSegment809.DEF = "hanim_r_carpal_middle_phalanx_2"
Transform810 = x3d.Transform()
Transform810.translation = [-0.1954,0.7393,-0.0185]
Transform811 = x3d.Transform()
#Empty Transform
Shape812 = x3d.Shape()
Shape812.USE = "HAnimJointShape"

Transform811.children.append(Shape812)

Transform810.children.append(Transform811)

HAnimSegment809.children.append(Transform810)
Shape813 = x3d.Shape()
LineSet814 = x3d.LineSet()
LineSet814.vertexCount = [2]
Coordinate815 = x3d.Coordinate()

LineSet814.coord = Coordinate815
#from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 vertices 2
ColorRGBA816 = x3d.ColorRGBA()
ColorRGBA816.USE = "HAnimSegmentLineColorRGBA"

LineSet814.color = ColorRGBA816

Shape813.geometry = LineSet814

HAnimSegment809.children.append(Shape813)
HAnimSite817 = x3d.HAnimSite()
HAnimSite817.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite817.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
TouchSensor818 = x3d.TouchSensor()
TouchSensor818.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite817.children.append(TouchSensor818)
Shape819 = x3d.Shape()
Shape819.USE = "HAnimSiteShape"

HAnimSite817.children.append(Shape819)

HAnimSegment809.children.append(HAnimSite817)
HAnimSite820 = x3d.HAnimSite()
HAnimSite820.name = "r_dactylion_pt"
HAnimSite820.DEF = "hanim_r_dactylion_pt"
HAnimSite820.translation = [-0.1941,0.6772,-0.0423]
TouchSensor821 = x3d.TouchSensor()
TouchSensor821.description = "HAnimSite r_dactylion_pt"

HAnimSite820.children.append(TouchSensor821)
Shape822 = x3d.Shape()
Shape822.USE = "HAnimSiteShape"

HAnimSite820.children.append(Shape822)

HAnimSegment809.children.append(HAnimSite820)

HAnimJoint808.children.append(HAnimSegment809)
HAnimJoint823 = x3d.HAnimJoint()
HAnimJoint823.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint823.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint823.center = [-0.1945,0.7169,-0.0173]
HAnimJoint823.ulimit = [0,0,0]
HAnimJoint823.llimit = [0,0,0]

HAnimJoint808.children.append(HAnimJoint823)

HAnimJoint799.children.append(HAnimJoint808)

HAnimJoint790.children.append(HAnimJoint799)

HAnimJoint734.children.append(HAnimJoint790)
HAnimJoint824 = x3d.HAnimJoint()
HAnimJoint824.name = "r_carpometacarpal_3"
HAnimJoint824.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint824.center = [-0.1972,0.806,-0.0468]
HAnimJoint824.ulimit = [0,0,0]
HAnimJoint824.llimit = [0,0,0]
HAnimSegment825 = x3d.HAnimSegment()
HAnimSegment825.name = "r_metacarpal_3"
HAnimSegment825.DEF = "hanim_r_metacarpal_3"
Transform826 = x3d.Transform()
Transform826.translation = [-0.1972,0.806,-0.0468]
Transform827 = x3d.Transform()
#Empty Transform
Shape828 = x3d.Shape()
Shape828.USE = "HAnimJointShape"

Transform827.children.append(Shape828)

Transform826.children.append(Transform827)

HAnimSegment825.children.append(Transform826)
Shape829 = x3d.Shape()
LineSet830 = x3d.LineSet()
LineSet830.vertexCount = [2]
Coordinate831 = x3d.Coordinate()

LineSet830.coord = Coordinate831
#from r_carpometacarpal_3 to r_metacarpophalangeal_3 vertices 2
ColorRGBA832 = x3d.ColorRGBA()
ColorRGBA832.USE = "HAnimSegmentLineColorRGBA"

LineSet830.color = ColorRGBA832

Shape829.geometry = LineSet830

HAnimSegment825.children.append(Shape829)

HAnimJoint824.children.append(HAnimSegment825)
HAnimJoint833 = x3d.HAnimJoint()
HAnimJoint833.name = "r_metacarpophalangeal_3"
HAnimJoint833.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint833.center = [-0.1972,0.7849,-0.0468]
HAnimJoint833.ulimit = [0,0,0]
HAnimJoint833.llimit = [0,0,0]
HAnimSegment834 = x3d.HAnimSegment()
HAnimSegment834.name = "r_carpal_proximal_phalanx_3"
HAnimSegment834.DEF = "hanim_r_carpal_proximal_phalanx_3"
Transform835 = x3d.Transform()
Transform835.translation = [-0.1972,0.7849,-0.0468]
Transform836 = x3d.Transform()
#Empty Transform
Shape837 = x3d.Shape()
Shape837.USE = "HAnimJointShape"

Transform836.children.append(Shape837)

Transform835.children.append(Transform836)

HAnimSegment834.children.append(Transform835)
Shape838 = x3d.Shape()
LineSet839 = x3d.LineSet()
LineSet839.vertexCount = [2]
Coordinate840 = x3d.Coordinate()

LineSet839.coord = Coordinate840
#from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 vertices 2
ColorRGBA841 = x3d.ColorRGBA()
ColorRGBA841.USE = "HAnimSegmentLineColorRGBA"

LineSet839.color = ColorRGBA841

Shape838.geometry = LineSet839

HAnimSegment834.children.append(Shape838)

HAnimJoint833.children.append(HAnimSegment834)
HAnimJoint842 = x3d.HAnimJoint()
HAnimJoint842.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint842.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint842.center = [-0.195,0.7304,-0.0441]
HAnimJoint842.ulimit = [0,0,0]
HAnimJoint842.llimit = [0,0,0]
HAnimSegment843 = x3d.HAnimSegment()
HAnimSegment843.name = "r_carpal_middle_phalanx_3"
HAnimSegment843.DEF = "hanim_r_carpal_middle_phalanx_3"
Transform844 = x3d.Transform()
Transform844.translation = [-0.195,0.7304,-0.0441]
Transform845 = x3d.Transform()
#Empty Transform
Shape846 = x3d.Shape()
Shape846.USE = "HAnimJointShape"

Transform845.children.append(Shape846)

Transform844.children.append(Transform845)

HAnimSegment843.children.append(Transform844)
Shape847 = x3d.Shape()
LineSet848 = x3d.LineSet()
LineSet848.vertexCount = [2]
Coordinate849 = x3d.Coordinate()

LineSet848.coord = Coordinate849
#from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 vertices 2
ColorRGBA850 = x3d.ColorRGBA()
ColorRGBA850.USE = "HAnimSegmentLineColorRGBA"

LineSet848.color = ColorRGBA850

Shape847.geometry = LineSet848

HAnimSegment843.children.append(Shape847)
HAnimSite851 = x3d.HAnimSite()
HAnimSite851.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite851.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
TouchSensor852 = x3d.TouchSensor()
TouchSensor852.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite851.children.append(TouchSensor852)
Shape853 = x3d.Shape()
Shape853.USE = "HAnimSiteShape"

HAnimSite851.children.append(Shape853)

HAnimSegment843.children.append(HAnimSite851)

HAnimJoint842.children.append(HAnimSegment843)
HAnimJoint854 = x3d.HAnimJoint()
HAnimJoint854.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint854.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint854.center = [-0.1939,0.7042,-0.0432]
HAnimJoint854.ulimit = [0,0,0]
HAnimJoint854.llimit = [0,0,0]

HAnimJoint842.children.append(HAnimJoint854)

HAnimJoint833.children.append(HAnimJoint842)

HAnimJoint824.children.append(HAnimJoint833)

HAnimJoint734.children.append(HAnimJoint824)
HAnimJoint855 = x3d.HAnimJoint()
HAnimJoint855.name = "r_carpometacarpal_4"
HAnimJoint855.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint855.center = [-0.1951,0.8049,-0.0732]
HAnimJoint855.ulimit = [0,0,0]
HAnimJoint855.llimit = [0,0,0]
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.name = "r_metacarpal_4"
HAnimSegment856.DEF = "hanim_r_metacarpal_4"
Transform857 = x3d.Transform()
Transform857.translation = [-0.1951,0.8049,-0.0732]
Transform858 = x3d.Transform()
#Empty Transform
Shape859 = x3d.Shape()
Shape859.USE = "HAnimJointShape"

Transform858.children.append(Shape859)

Transform857.children.append(Transform858)

HAnimSegment856.children.append(Transform857)
Shape860 = x3d.Shape()
LineSet861 = x3d.LineSet()
LineSet861.vertexCount = [2]
Coordinate862 = x3d.Coordinate()

LineSet861.coord = Coordinate862
#from r_carpometacarpal_4 to r_metacarpophalangeal_4 vertices 2
ColorRGBA863 = x3d.ColorRGBA()
ColorRGBA863.USE = "HAnimSegmentLineColorRGBA"

LineSet861.color = ColorRGBA863

Shape860.geometry = LineSet861

HAnimSegment856.children.append(Shape860)

HAnimJoint855.children.append(HAnimSegment856)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.name = "r_metacarpophalangeal_4"
HAnimJoint864.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint864.center = [-0.1951,0.7845,-0.0732]
HAnimJoint864.ulimit = [0,0,0]
HAnimJoint864.llimit = [0,0,0]
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.name = "r_carpal_proximal_phalanx_4"
HAnimSegment865.DEF = "hanim_r_carpal_proximal_phalanx_4"
Transform866 = x3d.Transform()
Transform866.translation = [-0.1951,0.7845,-0.0732]
Transform867 = x3d.Transform()
#Empty Transform
Shape868 = x3d.Shape()
Shape868.USE = "HAnimJointShape"

Transform867.children.append(Shape868)

Transform866.children.append(Transform867)

HAnimSegment865.children.append(Transform866)
Shape869 = x3d.Shape()
LineSet870 = x3d.LineSet()
LineSet870.vertexCount = [2]
Coordinate871 = x3d.Coordinate()

LineSet870.coord = Coordinate871
#from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 vertices 2
ColorRGBA872 = x3d.ColorRGBA()
ColorRGBA872.USE = "HAnimSegmentLineColorRGBA"

LineSet870.color = ColorRGBA872

Shape869.geometry = LineSet870

HAnimSegment865.children.append(Shape869)

HAnimJoint864.children.append(HAnimSegment865)
HAnimJoint873 = x3d.HAnimJoint()
HAnimJoint873.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint873.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint873.center = [-0.192,0.7318,-0.0716]
HAnimJoint873.ulimit = [0,0,0]
HAnimJoint873.llimit = [0,0,0]
HAnimSegment874 = x3d.HAnimSegment()
HAnimSegment874.name = "r_carpal_middle_phalanx_4"
HAnimSegment874.DEF = "hanim_r_carpal_middle_phalanx_4"
Transform875 = x3d.Transform()
Transform875.translation = [-0.192,0.7318,-0.0716]
Transform876 = x3d.Transform()
#Empty Transform
Shape877 = x3d.Shape()
Shape877.USE = "HAnimJointShape"

Transform876.children.append(Shape877)

Transform875.children.append(Transform876)

HAnimSegment874.children.append(Transform875)
Shape878 = x3d.Shape()
LineSet879 = x3d.LineSet()
LineSet879.vertexCount = [2]
Coordinate880 = x3d.Coordinate()

LineSet879.coord = Coordinate880
#from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 vertices 2
ColorRGBA881 = x3d.ColorRGBA()
ColorRGBA881.USE = "HAnimSegmentLineColorRGBA"

LineSet879.color = ColorRGBA881

Shape878.geometry = LineSet879

HAnimSegment874.children.append(Shape878)
HAnimSite882 = x3d.HAnimSite()
HAnimSite882.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite882.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
TouchSensor883 = x3d.TouchSensor()
TouchSensor883.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite882.children.append(TouchSensor883)
Shape884 = x3d.Shape()
Shape884.USE = "HAnimSiteShape"

HAnimSite882.children.append(Shape884)

HAnimSegment874.children.append(HAnimSite882)

HAnimJoint873.children.append(HAnimSegment874)
HAnimJoint885 = x3d.HAnimJoint()
HAnimJoint885.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint885.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint885.center = [-0.1908,0.7077,-0.0706]
HAnimJoint885.ulimit = [0,0,0]
HAnimJoint885.llimit = [0,0,0]

HAnimJoint873.children.append(HAnimJoint885)

HAnimJoint864.children.append(HAnimJoint873)

HAnimJoint855.children.append(HAnimJoint864)

HAnimJoint734.children.append(HAnimJoint855)
HAnimJoint886 = x3d.HAnimJoint()
HAnimJoint886.name = "r_carpometacarpal_5"
HAnimJoint886.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint886.center = [-0.1926,0.8096,-0.0975]
HAnimJoint886.ulimit = [0,0,0]
HAnimJoint886.llimit = [0,0,0]
HAnimSegment887 = x3d.HAnimSegment()
HAnimSegment887.name = "r_metacarpal_5"
HAnimSegment887.DEF = "hanim_r_metacarpal_5"
Transform888 = x3d.Transform()
Transform888.translation = [-0.1926,0.8096,-0.0975]
Transform889 = x3d.Transform()
#Empty Transform
Shape890 = x3d.Shape()
Shape890.USE = "HAnimJointShape"

Transform889.children.append(Shape890)

Transform888.children.append(Transform889)

HAnimSegment887.children.append(Transform888)
Shape891 = x3d.Shape()
LineSet892 = x3d.LineSet()
LineSet892.vertexCount = [2]
Coordinate893 = x3d.Coordinate()

LineSet892.coord = Coordinate893
#from r_carpometacarpal_5 to r_metacarpophalangeal_5 vertices 2
ColorRGBA894 = x3d.ColorRGBA()
ColorRGBA894.USE = "HAnimSegmentLineColorRGBA"

LineSet892.color = ColorRGBA894

Shape891.geometry = LineSet892

HAnimSegment887.children.append(Shape891)

HAnimJoint886.children.append(HAnimSegment887)
HAnimJoint895 = x3d.HAnimJoint()
HAnimJoint895.name = "r_metacarpophalangeal_5"
HAnimJoint895.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint895.center = [-0.1926,0.7896,-0.0975]
HAnimJoint895.ulimit = [0,0,0]
HAnimJoint895.llimit = [0,0,0]
HAnimSegment896 = x3d.HAnimSegment()
HAnimSegment896.name = "r_carpal_proximal_phalanx_5"
HAnimSegment896.DEF = "hanim_r_carpal_proximal_phalanx_5"
Transform897 = x3d.Transform()
Transform897.translation = [-0.1926,0.7896,-0.0975]
Transform898 = x3d.Transform()
#Empty Transform
Shape899 = x3d.Shape()
Shape899.USE = "HAnimJointShape"

Transform898.children.append(Shape899)

Transform897.children.append(Transform898)

HAnimSegment896.children.append(Transform897)
Shape900 = x3d.Shape()
LineSet901 = x3d.LineSet()
LineSet901.vertexCount = [2]
Coordinate902 = x3d.Coordinate()

LineSet901.coord = Coordinate902
#from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 vertices 2
ColorRGBA903 = x3d.ColorRGBA()
ColorRGBA903.USE = "HAnimSegmentLineColorRGBA"

LineSet901.color = ColorRGBA903

Shape900.geometry = LineSet901

HAnimSegment896.children.append(Shape900)

HAnimJoint895.children.append(HAnimSegment896)
HAnimJoint904 = x3d.HAnimJoint()
HAnimJoint904.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint904.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint904.center = [-0.1902,0.7483,-0.0963]
HAnimJoint904.ulimit = [0,0,0]
HAnimJoint904.llimit = [0,0,0]
HAnimSegment905 = x3d.HAnimSegment()
HAnimSegment905.name = "r_carpal_middle_phalanx_5"
HAnimSegment905.DEF = "hanim_r_carpal_middle_phalanx_5"
Transform906 = x3d.Transform()
Transform906.translation = [-0.1902,0.7483,-0.0963]
Transform907 = x3d.Transform()
#Empty Transform
Shape908 = x3d.Shape()
Shape908.USE = "HAnimJointShape"

Transform907.children.append(Shape908)

Transform906.children.append(Transform907)

HAnimSegment905.children.append(Transform906)
Shape909 = x3d.Shape()
LineSet910 = x3d.LineSet()
LineSet910.vertexCount = [2]
Coordinate911 = x3d.Coordinate()

LineSet910.coord = Coordinate911
#from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 vertices 2
ColorRGBA912 = x3d.ColorRGBA()
ColorRGBA912.USE = "HAnimSegmentLineColorRGBA"

LineSet910.color = ColorRGBA912

Shape909.geometry = LineSet910

HAnimSegment905.children.append(Shape909)
HAnimSite913 = x3d.HAnimSite()
HAnimSite913.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite913.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
TouchSensor914 = x3d.TouchSensor()
TouchSensor914.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite913.children.append(TouchSensor914)
Shape915 = x3d.Shape()
Shape915.USE = "HAnimSiteShape"

HAnimSite913.children.append(Shape915)

HAnimSegment905.children.append(HAnimSite913)

HAnimJoint904.children.append(HAnimSegment905)
HAnimJoint916 = x3d.HAnimJoint()
HAnimJoint916.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint916.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint916.center = [-0.1908,0.754,-0.096]
HAnimJoint916.ulimit = [0,0,0]
HAnimJoint916.llimit = [0,0,0]

HAnimJoint904.children.append(HAnimJoint916)

HAnimJoint895.children.append(HAnimJoint904)

HAnimJoint886.children.append(HAnimJoint895)

HAnimJoint734.children.append(HAnimJoint886)

HAnimJoint722.children.append(HAnimJoint734)

HAnimJoint701.children.append(HAnimJoint722)

HAnimJoint686.children.append(HAnimJoint701)

HAnimJoint677.children.append(HAnimJoint686)

HAnimJoint335.children.append(HAnimJoint677)

HAnimJoint320.children.append(HAnimJoint335)

HAnimJoint299.children.append(HAnimJoint320)

HAnimJoint287.children.append(HAnimJoint299)

HAnimJoint278.children.append(HAnimJoint287)

HAnimJoint269.children.append(HAnimJoint278)

HAnimJoint52.children.append(HAnimJoint269)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimJoint917 = x3d.HAnimJoint()
HAnimJoint917.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint917)
HAnimJoint918 = x3d.HAnimJoint()
HAnimJoint918.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint918)
HAnimJoint919 = x3d.HAnimJoint()
HAnimJoint919.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint919)
HAnimJoint920 = x3d.HAnimJoint()
HAnimJoint920.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint920)
HAnimJoint921 = x3d.HAnimJoint()
HAnimJoint921.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint921)
HAnimJoint922 = x3d.HAnimJoint()
HAnimJoint922.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint922)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint923)
HAnimJoint924 = x3d.HAnimJoint()
HAnimJoint924.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint924)
HAnimJoint925 = x3d.HAnimJoint()
HAnimJoint925.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint925)
HAnimJoint926 = x3d.HAnimJoint()
HAnimJoint926.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint926)
HAnimJoint927 = x3d.HAnimJoint()
HAnimJoint927.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint927)
HAnimJoint928 = x3d.HAnimJoint()
HAnimJoint928.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint928)
HAnimJoint929 = x3d.HAnimJoint()
HAnimJoint929.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint929)
HAnimJoint930 = x3d.HAnimJoint()
HAnimJoint930.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint930)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint931)
HAnimJoint932 = x3d.HAnimJoint()
HAnimJoint932.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint932)
HAnimJoint933 = x3d.HAnimJoint()
HAnimJoint933.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint933)
HAnimJoint934 = x3d.HAnimJoint()
HAnimJoint934.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint934)
HAnimJoint935 = x3d.HAnimJoint()
HAnimJoint935.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint935)
HAnimJoint936 = x3d.HAnimJoint()
HAnimJoint936.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint936)
HAnimJoint937 = x3d.HAnimJoint()
HAnimJoint937.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint937)
HAnimJoint938 = x3d.HAnimJoint()
HAnimJoint938.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint938)
HAnimJoint939 = x3d.HAnimJoint()
HAnimJoint939.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint939)
HAnimJoint940 = x3d.HAnimJoint()
HAnimJoint940.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint940)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint941)
HAnimJoint942 = x3d.HAnimJoint()
HAnimJoint942.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint942)
HAnimJoint943 = x3d.HAnimJoint()
HAnimJoint943.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint943)
HAnimJoint944 = x3d.HAnimJoint()
HAnimJoint944.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint944)
HAnimJoint945 = x3d.HAnimJoint()
HAnimJoint945.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint945)
HAnimJoint946 = x3d.HAnimJoint()
HAnimJoint946.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint946)
HAnimJoint947 = x3d.HAnimJoint()
HAnimJoint947.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint947)
HAnimJoint948 = x3d.HAnimJoint()
HAnimJoint948.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint948)
HAnimJoint949 = x3d.HAnimJoint()
HAnimJoint949.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint949)
HAnimJoint950 = x3d.HAnimJoint()
HAnimJoint950.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint950)
HAnimJoint951 = x3d.HAnimJoint()
HAnimJoint951.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint951)
HAnimJoint952 = x3d.HAnimJoint()
HAnimJoint952.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint952)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint953)
HAnimJoint954 = x3d.HAnimJoint()
HAnimJoint954.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint954)
HAnimJoint955 = x3d.HAnimJoint()
HAnimJoint955.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint955)
HAnimJoint956 = x3d.HAnimJoint()
HAnimJoint956.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint956)
HAnimJoint957 = x3d.HAnimJoint()
HAnimJoint957.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint957)
HAnimJoint958 = x3d.HAnimJoint()
HAnimJoint958.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint958)
HAnimJoint959 = x3d.HAnimJoint()
HAnimJoint959.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint959)
HAnimJoint960 = x3d.HAnimJoint()
HAnimJoint960.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint960)
HAnimJoint961 = x3d.HAnimJoint()
HAnimJoint961.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint961)
HAnimJoint962 = x3d.HAnimJoint()
HAnimJoint962.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint962)
HAnimJoint963 = x3d.HAnimJoint()
HAnimJoint963.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint963)
HAnimJoint964 = x3d.HAnimJoint()
HAnimJoint964.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint964)
HAnimJoint965 = x3d.HAnimJoint()
HAnimJoint965.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint965)
HAnimJoint966 = x3d.HAnimJoint()
HAnimJoint966.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint966)
HAnimJoint967 = x3d.HAnimJoint()
HAnimJoint967.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint967)
HAnimJoint968 = x3d.HAnimJoint()
HAnimJoint968.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint968)
HAnimJoint969 = x3d.HAnimJoint()
HAnimJoint969.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint969)
HAnimJoint970 = x3d.HAnimJoint()
HAnimJoint970.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint970)
HAnimJoint971 = x3d.HAnimJoint()
HAnimJoint971.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint971)
HAnimJoint972 = x3d.HAnimJoint()
HAnimJoint972.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint972)
HAnimJoint973 = x3d.HAnimJoint()
HAnimJoint973.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint973)
HAnimJoint974 = x3d.HAnimJoint()
HAnimJoint974.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint974)
HAnimJoint975 = x3d.HAnimJoint()
HAnimJoint975.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint975)
HAnimJoint976 = x3d.HAnimJoint()
HAnimJoint976.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint976)
HAnimJoint977 = x3d.HAnimJoint()
HAnimJoint977.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint977)
HAnimJoint978 = x3d.HAnimJoint()
HAnimJoint978.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint978)
HAnimJoint979 = x3d.HAnimJoint()
HAnimJoint979.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint979)
HAnimJoint980 = x3d.HAnimJoint()
HAnimJoint980.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint980)
HAnimJoint981 = x3d.HAnimJoint()
HAnimJoint981.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint981)
HAnimJoint982 = x3d.HAnimJoint()
HAnimJoint982.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint982)
HAnimJoint983 = x3d.HAnimJoint()
HAnimJoint983.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint983)
HAnimJoint984 = x3d.HAnimJoint()
HAnimJoint984.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint984)
HAnimJoint985 = x3d.HAnimJoint()
HAnimJoint985.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint985)
HAnimJoint986 = x3d.HAnimJoint()
HAnimJoint986.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint986)
HAnimJoint987 = x3d.HAnimJoint()
HAnimJoint987.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint987)
HAnimSegment988 = x3d.HAnimSegment()
HAnimSegment988.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment988)
HAnimSegment989 = x3d.HAnimSegment()
HAnimSegment989.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment989)
HAnimSegment990 = x3d.HAnimSegment()
HAnimSegment990.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment990)
HAnimSegment991 = x3d.HAnimSegment()
HAnimSegment991.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment991)
HAnimSegment992 = x3d.HAnimSegment()
HAnimSegment992.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment992)
HAnimSegment993 = x3d.HAnimSegment()
HAnimSegment993.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment993)
HAnimSegment994 = x3d.HAnimSegment()
HAnimSegment994.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment994)
HAnimSegment995 = x3d.HAnimSegment()
HAnimSegment995.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment995)
HAnimSegment996 = x3d.HAnimSegment()
HAnimSegment996.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment996)
HAnimSegment997 = x3d.HAnimSegment()
HAnimSegment997.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment997)
HAnimSegment998 = x3d.HAnimSegment()
HAnimSegment998.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment998)
HAnimSegment999 = x3d.HAnimSegment()
HAnimSegment999.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment999)
HAnimSegment1000 = x3d.HAnimSegment()
HAnimSegment1000.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment1000)
HAnimSegment1001 = x3d.HAnimSegment()
HAnimSegment1001.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment1001)
HAnimSegment1002 = x3d.HAnimSegment()
HAnimSegment1002.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment1002)
HAnimSegment1003 = x3d.HAnimSegment()
HAnimSegment1003.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment1003)
HAnimSegment1004 = x3d.HAnimSegment()
HAnimSegment1004.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment1004)
HAnimSegment1005 = x3d.HAnimSegment()
HAnimSegment1005.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment1005)
HAnimSegment1006 = x3d.HAnimSegment()
HAnimSegment1006.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment1006)
HAnimSegment1007 = x3d.HAnimSegment()
HAnimSegment1007.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment1007)
HAnimSegment1008 = x3d.HAnimSegment()
HAnimSegment1008.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1008)
HAnimSegment1009 = x3d.HAnimSegment()
HAnimSegment1009.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1009)
HAnimSegment1010 = x3d.HAnimSegment()
HAnimSegment1010.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1010)
HAnimSegment1011 = x3d.HAnimSegment()
HAnimSegment1011.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1011)
HAnimSegment1012 = x3d.HAnimSegment()
HAnimSegment1012.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1012)
HAnimSegment1013 = x3d.HAnimSegment()
HAnimSegment1013.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1013)
HAnimSegment1014 = x3d.HAnimSegment()
HAnimSegment1014.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1014)
HAnimSegment1015 = x3d.HAnimSegment()
HAnimSegment1015.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1015)
HAnimSegment1016 = x3d.HAnimSegment()
HAnimSegment1016.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1016)
HAnimSegment1017 = x3d.HAnimSegment()
HAnimSegment1017.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1017)
HAnimSegment1018 = x3d.HAnimSegment()
HAnimSegment1018.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1018)
HAnimSegment1019 = x3d.HAnimSegment()
HAnimSegment1019.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1019)
HAnimSegment1020 = x3d.HAnimSegment()
HAnimSegment1020.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1020)
HAnimSegment1021 = x3d.HAnimSegment()
HAnimSegment1021.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1021)
HAnimSegment1022 = x3d.HAnimSegment()
HAnimSegment1022.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1022)
HAnimSegment1023 = x3d.HAnimSegment()
HAnimSegment1023.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1023)
HAnimSegment1024 = x3d.HAnimSegment()
HAnimSegment1024.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1024)
HAnimSegment1025 = x3d.HAnimSegment()
HAnimSegment1025.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1025)
HAnimSegment1026 = x3d.HAnimSegment()
HAnimSegment1026.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1026)
HAnimSegment1027 = x3d.HAnimSegment()
HAnimSegment1027.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1027)
HAnimSegment1028 = x3d.HAnimSegment()
HAnimSegment1028.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1028)
HAnimSegment1029 = x3d.HAnimSegment()
HAnimSegment1029.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1029)
HAnimSegment1030 = x3d.HAnimSegment()
HAnimSegment1030.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1030)
HAnimSegment1031 = x3d.HAnimSegment()
HAnimSegment1031.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1031)
HAnimSegment1032 = x3d.HAnimSegment()
HAnimSegment1032.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1032)
HAnimSegment1033 = x3d.HAnimSegment()
HAnimSegment1033.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1033)
HAnimSegment1034 = x3d.HAnimSegment()
HAnimSegment1034.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1034)
HAnimSegment1035 = x3d.HAnimSegment()
HAnimSegment1035.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1035)
HAnimSegment1036 = x3d.HAnimSegment()
HAnimSegment1036.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1036)
HAnimSegment1037 = x3d.HAnimSegment()
HAnimSegment1037.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1037)
HAnimSegment1038 = x3d.HAnimSegment()
HAnimSegment1038.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1038)
HAnimSegment1039 = x3d.HAnimSegment()
HAnimSegment1039.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1039)
HAnimSegment1040 = x3d.HAnimSegment()
HAnimSegment1040.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1040)
HAnimSegment1041 = x3d.HAnimSegment()
HAnimSegment1041.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1041)
HAnimSegment1042 = x3d.HAnimSegment()
HAnimSegment1042.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1042)
HAnimSegment1043 = x3d.HAnimSegment()
HAnimSegment1043.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1043)
HAnimSegment1044 = x3d.HAnimSegment()
HAnimSegment1044.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1044)
HAnimSegment1045 = x3d.HAnimSegment()
HAnimSegment1045.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1045)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite1046)
HAnimSite1047 = x3d.HAnimSite()
HAnimSite1047.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite1047)
HAnimSite1048 = x3d.HAnimSite()
HAnimSite1048.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1048)
HAnimSite1049 = x3d.HAnimSite()
HAnimSite1049.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1049)
HAnimSite1050 = x3d.HAnimSite()
HAnimSite1050.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1050)
HAnimSite1051 = x3d.HAnimSite()
HAnimSite1051.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1051)
HAnimSite1052 = x3d.HAnimSite()
HAnimSite1052.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1052)
HAnimSite1053 = x3d.HAnimSite()
HAnimSite1053.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1053)
HAnimSite1054 = x3d.HAnimSite()
HAnimSite1054.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1054)
HAnimSite1055 = x3d.HAnimSite()
HAnimSite1055.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1055)
HAnimSite1056 = x3d.HAnimSite()
HAnimSite1056.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite1056)
HAnimSite1057 = x3d.HAnimSite()
HAnimSite1057.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1057)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1058)
HAnimSite1059 = x3d.HAnimSite()
HAnimSite1059.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1059)
HAnimSite1060 = x3d.HAnimSite()
HAnimSite1060.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1060)
HAnimSite1061 = x3d.HAnimSite()
HAnimSite1061.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1061)
HAnimSite1062 = x3d.HAnimSite()
HAnimSite1062.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1062)
HAnimSite1063 = x3d.HAnimSite()
HAnimSite1063.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1063)
HAnimSite1064 = x3d.HAnimSite()
HAnimSite1064.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1064)
HAnimSite1065 = x3d.HAnimSite()
HAnimSite1065.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1065)
HAnimSite1066 = x3d.HAnimSite()
HAnimSite1066.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1066)
HAnimSite1067 = x3d.HAnimSite()
HAnimSite1067.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1067)
HAnimSite1068 = x3d.HAnimSite()
HAnimSite1068.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1068)
HAnimSite1069 = x3d.HAnimSite()
HAnimSite1069.USE = "hanim_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1069)
HAnimSite1070 = x3d.HAnimSite()
HAnimSite1070.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1070)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1071)
HAnimSite1072 = x3d.HAnimSite()
HAnimSite1072.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1072)
HAnimSite1073 = x3d.HAnimSite()
HAnimSite1073.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1073)
HAnimSite1074 = x3d.HAnimSite()
HAnimSite1074.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1074)
HAnimSite1075 = x3d.HAnimSite()
HAnimSite1075.USE = "hanim_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1075)
HAnimSite1076 = x3d.HAnimSite()
HAnimSite1076.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1076)
HAnimSite1077 = x3d.HAnimSite()
HAnimSite1077.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1077)
HAnimSite1078 = x3d.HAnimSite()
HAnimSite1078.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1078)
HAnimSite1079 = x3d.HAnimSite()
HAnimSite1079.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite1079)
HAnimSite1080 = x3d.HAnimSite()
HAnimSite1080.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1080)
HAnimSite1081 = x3d.HAnimSite()
HAnimSite1081.USE = "hanim_mesosternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1081)
HAnimSite1082 = x3d.HAnimSite()
HAnimSite1082.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1082)
HAnimSite1083 = x3d.HAnimSite()
HAnimSite1083.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1083)
HAnimSite1084 = x3d.HAnimSite()
HAnimSite1084.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1084)
HAnimSite1085 = x3d.HAnimSite()
HAnimSite1085.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1085)
HAnimSite1086 = x3d.HAnimSite()
HAnimSite1086.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1086)
HAnimSite1087 = x3d.HAnimSite()
HAnimSite1087.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1087)
HAnimSite1088 = x3d.HAnimSite()
HAnimSite1088.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1088)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1089)
HAnimSite1090 = x3d.HAnimSite()
HAnimSite1090.USE = "hanim_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1090)
HAnimSite1091 = x3d.HAnimSite()
HAnimSite1091.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1091)
HAnimSite1092 = x3d.HAnimSite()
HAnimSite1092.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1092)
HAnimSite1093 = x3d.HAnimSite()
HAnimSite1093.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1093)
HAnimSite1094 = x3d.HAnimSite()
HAnimSite1094.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1094)
HAnimSite1095 = x3d.HAnimSite()
HAnimSite1095.USE = "hanim_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1095)
HAnimSite1096 = x3d.HAnimSite()
HAnimSite1096.USE = "hanim_adams_apple_pt"

HAnimHumanoid43.sites.append(HAnimSite1096)
HAnimSite1097 = x3d.HAnimSite()
HAnimSite1097.USE = "hanim_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite1097)
HAnimSite1098 = x3d.HAnimSite()
HAnimSite1098.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1098)
HAnimSite1099 = x3d.HAnimSite()
HAnimSite1099.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1099)
HAnimSite1100 = x3d.HAnimSite()
HAnimSite1100.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1100)
HAnimSite1101 = x3d.HAnimSite()
HAnimSite1101.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite1101)
HAnimSite1102 = x3d.HAnimSite()
HAnimSite1102.USE = "hanim_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite1102)
HAnimSite1103 = x3d.HAnimSite()
HAnimSite1103.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1103)
HAnimSite1104 = x3d.HAnimSite()
HAnimSite1104.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1104)
HAnimSite1105 = x3d.HAnimSite()
HAnimSite1105.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1105)
HAnimSite1106 = x3d.HAnimSite()
HAnimSite1106.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite1106)
HAnimSite1107 = x3d.HAnimSite()
HAnimSite1107.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite1107)
HAnimSite1108 = x3d.HAnimSite()
HAnimSite1108.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1108)
HAnimSite1109 = x3d.HAnimSite()
HAnimSite1109.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1109)
HAnimSite1110 = x3d.HAnimSite()
HAnimSite1110.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1110)
HAnimSite1111 = x3d.HAnimSite()
HAnimSite1111.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1111)
HAnimSite1112 = x3d.HAnimSite()
HAnimSite1112.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1112)
HAnimSite1113 = x3d.HAnimSite()
HAnimSite1113.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1113)
HAnimSite1114 = x3d.HAnimSite()
HAnimSite1114.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1114)
HAnimSite1115 = x3d.HAnimSite()
HAnimSite1115.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1115)
HAnimSite1116 = x3d.HAnimSite()
HAnimSite1116.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1116)
HAnimSite1117 = x3d.HAnimSite()
HAnimSite1117.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1117)
HAnimSite1118 = x3d.HAnimSite()
HAnimSite1118.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1118)
HAnimSite1119 = x3d.HAnimSite()
HAnimSite1119.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1119)
HAnimSite1120 = x3d.HAnimSite()
HAnimSite1120.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1120)
HAnimSite1121 = x3d.HAnimSite()
HAnimSite1121.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1121)
HAnimSite1122 = x3d.HAnimSite()
HAnimSite1122.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1122)
HAnimSite1123 = x3d.HAnimSite()
HAnimSite1123.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1123)
HAnimSite1124 = x3d.HAnimSite()
HAnimSite1124.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1124)
HAnimSite1125 = x3d.HAnimSite()
HAnimSite1125.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1125)
HAnimSite1126 = x3d.HAnimSite()
HAnimSite1126.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1126)
HAnimSite1127 = x3d.HAnimSite()
HAnimSite1127.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1127)
HAnimSite1128 = x3d.HAnimSite()
HAnimSite1128.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1128)
HAnimSite1129 = x3d.HAnimSite()
HAnimSite1129.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1129)
HAnimSite1130 = x3d.HAnimSite()
HAnimSite1130.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1130)
HAnimSite1131 = x3d.HAnimSite()
HAnimSite1131.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1131)
HAnimSite1132 = x3d.HAnimSite()
HAnimSite1132.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1132)
HAnimSite1133 = x3d.HAnimSite()
HAnimSite1133.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1133)
HAnimSite1134 = x3d.HAnimSite()
HAnimSite1134.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1134)
HAnimSite1135 = x3d.HAnimSite()
HAnimSite1135.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1135)
HAnimSite1136 = x3d.HAnimSite()
HAnimSite1136.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1136)
HAnimSite1137 = x3d.HAnimSite()
HAnimSite1137.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1137)
HAnimSite1138 = x3d.HAnimSite()
HAnimSite1138.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1138)
HAnimSite1139 = x3d.HAnimSite()
HAnimSite1139.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1139)

Scene11.children.append(HAnimHumanoid43)

X3D0.Scene = Scene11
f = open("././Humanoid2_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
