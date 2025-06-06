print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.level = 1
component2.name = "HAnim"

head1.children.append(component2)
meta3 = x3d.meta()
meta3.content = "JohnBoy.x3d"
meta3.name = "title"

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
meta8.content = "John Carlson"
meta8.name = "creator"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "9 November 2020"
meta9.name = "created"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "../license.html"
meta10.name = "license"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
Transform12 = x3d.Transform()
Transform12.scale = [1,1,1]
""" DEF for markerfor XYZ axes """
Shape13 = x3d.Shape()
Shape13.DEF = "AxisLinesShape"
""" RGB lines showing XYZ axes """
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
""" DEFS for markers of skeleton joints, segments, and sites """
Transform18 = x3d.Transform()
Transform18.translation = [0,0,0]
Transform18.scale = [1,1,1]
Transform19 = x3d.Transform()
Transform19.translation = [0,2,0]
Transform19.scale = [1,1,1]
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
Transform24.scale = [1,1,1]
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
Transform29.scale = [1,1,1]
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
Transform34.scale = [1,1,1]
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
NavigationInfo41.type = ["EXAMINE","ANY"]

Scene11.children.append(NavigationInfo41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,0,0]
Viewpoint42.description = "default"

Scene11.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.DEF = "hanim_HAnim"
HAnimHumanoid43.info = ["humanoidVersion=2.0"]
HAnimHumanoid43.name = "HAnim"
HAnimHumanoid43.scale = [1,1,1]
HAnimHumanoid43.translation = [0,0,0]
HAnimHumanoid43.version = "2.0"
""" <LOD containerField='skin'> (Switch whichChoice='0' and LOD parents each already work in view3dscene) """
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
""" </LOD> """
Coordinate51 = x3d.Coordinate()
Coordinate51.USE = "TheSkinCoord"

HAnimHumanoid43.skinCoord = Coordinate51
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.DEF = "hanim_humanoid_root"
HAnimJoint52.name = "humanoid_root"
HAnimJoint52.center = [0.0000,0.8240,0.0277]
HAnimSegment53 = x3d.HAnimSegment()
HAnimSegment53.DEF = "hanim_sacrum"
HAnimSegment53.name = "sacrum"
Transform54 = x3d.Transform()
Transform54.translation = [0.0000,0.8240,0.0277]
Transform55 = x3d.Transform()
""" Empty Transform """
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
""" from humanoid_root to sacroiliac vertices 2"""
ColorRGBA60 = x3d.ColorRGBA()
ColorRGBA60.USE = "HAnimSegmentLineColorRGBA"

LineSet58.color = ColorRGBA60

Shape57.geometry = LineSet58

HAnimSegment53.children.append(Shape57)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
HAnimSite61.name = "buttocks_standing_wall_contact_point_pt"
TouchSensor62 = x3d.TouchSensor()
TouchSensor62.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite61.children.append(TouchSensor62)
Shape63 = x3d.Shape()
Shape63.USE = "HAnimSiteShape"

HAnimSite61.children.append(Shape63)

HAnimSegment53.children.append(HAnimSite61)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.DEF = "hanim_crotch_pt"
HAnimSite64.name = "crotch_pt"
HAnimSite64.translation = [0.0034,0.8266,0.0257]
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimSite crotch_pt"

HAnimSite64.children.append(TouchSensor65)
Shape66 = x3d.Shape()
Shape66.USE = "HAnimSiteShape"

HAnimSite64.children.append(Shape66)

HAnimSegment53.children.append(HAnimSite64)
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.DEF = "hanim_l_asis_pt"
HAnimSite67.name = "l_asis_pt"
HAnimSite67.translation = [0.0925,0.9983,0.1052]
TouchSensor68 = x3d.TouchSensor()
TouchSensor68.description = "HAnimSite l_asis_pt"

HAnimSite67.children.append(TouchSensor68)
Shape69 = x3d.Shape()
Shape69.USE = "HAnimSiteShape"

HAnimSite67.children.append(Shape69)

HAnimSegment53.children.append(HAnimSite67)
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.DEF = "hanim_l_iliocristale_pt"
HAnimSite70.name = "l_iliocristale_pt"
HAnimSite70.translation = [0.1612,1.0537,0.0008]
TouchSensor71 = x3d.TouchSensor()
TouchSensor71.description = "HAnimSite l_iliocristale_pt"

HAnimSite70.children.append(TouchSensor71)
Shape72 = x3d.Shape()
Shape72.USE = "HAnimSiteShape"

HAnimSite70.children.append(Shape72)

HAnimSegment53.children.append(HAnimSite70)
HAnimSite73 = x3d.HAnimSite()
HAnimSite73.DEF = "hanim_l_psis_pt"
HAnimSite73.name = "l_psis_pt"
HAnimSite73.translation = [0.0774,1.0190,-0.1151]
TouchSensor74 = x3d.TouchSensor()
TouchSensor74.description = "HAnimSite l_psis_pt"

HAnimSite73.children.append(TouchSensor74)
Shape75 = x3d.Shape()
Shape75.USE = "HAnimSiteShape"

HAnimSite73.children.append(Shape75)

HAnimSegment53.children.append(HAnimSite73)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.DEF = "hanim_l_trochanterion_pt"
HAnimSite76.name = "l_trochanterion_pt"
HAnimSite76.translation = [0.1677,0.8336,0.0303]
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite l_trochanterion_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"

HAnimSite76.children.append(Shape78)

HAnimSegment53.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.DEF = "hanim_r_asis_pt"
HAnimSite79.name = "r_asis_pt"
HAnimSite79.translation = [-0.0887,1.0021,0.1112]
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite r_asis_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"

HAnimSite79.children.append(Shape81)

HAnimSegment53.children.append(HAnimSite79)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.DEF = "hanim_r_iliocristale_pt"
HAnimSite82.name = "r_iliocristale_pt"
HAnimSite82.translation = [-0.1525,1.0628,0.0035]
TouchSensor83 = x3d.TouchSensor()
TouchSensor83.description = "HAnimSite r_iliocristale_pt"

HAnimSite82.children.append(TouchSensor83)
Shape84 = x3d.Shape()
Shape84.USE = "HAnimSiteShape"

HAnimSite82.children.append(Shape84)

HAnimSegment53.children.append(HAnimSite82)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.DEF = "hanim_r_psis_pt"
HAnimSite85.name = "r_psis_pt"
HAnimSite85.translation = [-0.0716,1.0190,-0.1138]
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite r_psis_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"

HAnimSite85.children.append(Shape87)

HAnimSegment53.children.append(HAnimSite85)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.DEF = "hanim_r_trochanterion_pt"
HAnimSite88.name = "r_trochanterion_pt"
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
""" from humanoid_root to vl5 vertices 2"""
ColorRGBA94 = x3d.ColorRGBA()
ColorRGBA94.USE = "HAnimSegmentLineColorRGBA"

LineSet92.color = ColorRGBA94

Shape91.geometry = LineSet92

HAnimSegment53.children.append(Shape91)
HAnimSite95 = x3d.HAnimSite()
HAnimSite95.DEF = "hanim_navel_pt"
HAnimSite95.name = "navel_pt"
HAnimSite95.translation = [0.0069,1.0966,0.1017]
TouchSensor96 = x3d.TouchSensor()
TouchSensor96.description = "HAnimSite navel_pt"

HAnimSite95.children.append(TouchSensor96)
Shape97 = x3d.Shape()
Shape97.USE = "HAnimSiteShape"

HAnimSite95.children.append(Shape97)

HAnimSegment53.children.append(HAnimSite95)
HAnimSite98 = x3d.HAnimSite()
HAnimSite98.DEF = "hanim_waist_preferred_anterior_pt"
HAnimSite98.name = "waist_preferred_anterior_pt"
TouchSensor99 = x3d.TouchSensor()
TouchSensor99.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite98.children.append(TouchSensor99)
Shape100 = x3d.Shape()
Shape100.USE = "HAnimSiteShape"

HAnimSite98.children.append(Shape100)

HAnimSegment53.children.append(HAnimSite98)
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite101.name = "waist_preferred_posterior_pt"
HAnimSite101.translation = [0.2900,1.0915,-0.1091]
TouchSensor102 = x3d.TouchSensor()
TouchSensor102.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite101.children.append(TouchSensor102)
Shape103 = x3d.Shape()
Shape103.USE = "HAnimSiteShape"

HAnimSite101.children.append(Shape103)

HAnimSegment53.children.append(HAnimSite101)

HAnimJoint52.children.append(HAnimSegment53)
HAnimJoint104 = x3d.HAnimJoint()
HAnimJoint104.DEF = "hanim_sacroiliac"
HAnimJoint104.name = "sacroiliac"
HAnimJoint104.center = [0.0000,0.9149,0.0016]
HAnimSegment105 = x3d.HAnimSegment()
HAnimSegment105.DEF = "hanim_pelvis"
HAnimSegment105.name = "pelvis"
Transform106 = x3d.Transform()
Transform106.translation = [0.0000,0.9149,0.0016]
Transform107 = x3d.Transform()
""" Empty Transform """
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
""" from sacroiliac to l_hip vertices 2"""
ColorRGBA112 = x3d.ColorRGBA()
ColorRGBA112.USE = "HAnimSegmentLineColorRGBA"

LineSet110.color = ColorRGBA112

Shape109.geometry = LineSet110

HAnimSegment105.children.append(Shape109)
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite113.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite113.translation = [0.1598,0.4967,0.0297]
TouchSensor114 = x3d.TouchSensor()
TouchSensor114.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite113.children.append(TouchSensor114)
Shape115 = x3d.Shape()
Shape115.USE = "HAnimSiteShape"

HAnimSite113.children.append(Shape115)

HAnimSegment105.children.append(HAnimSite113)
HAnimSite116 = x3d.HAnimSite()
HAnimSite116.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite116.name = "l_femoral_medial_epicondyles_pt"
HAnimSite116.translation = [0.0398,0.4946,0.0303]
TouchSensor117 = x3d.TouchSensor()
TouchSensor117.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite116.children.append(TouchSensor117)
Shape118 = x3d.Shape()
Shape118.USE = "HAnimSiteShape"

HAnimSite116.children.append(Shape118)

HAnimSegment105.children.append(HAnimSite116)
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.DEF = "hanim_l_knee_crease_pt"
HAnimSite119.name = "l_knee_crease_pt"
HAnimSite119.translation = [0.0993,0.4881,-0.0309]
TouchSensor120 = x3d.TouchSensor()
TouchSensor120.description = "HAnimSite l_knee_crease_pt"

HAnimSite119.children.append(TouchSensor120)
Shape121 = x3d.Shape()
Shape121.USE = "HAnimSiteShape"

HAnimSite119.children.append(Shape121)

HAnimSegment105.children.append(HAnimSite119)
HAnimSite122 = x3d.HAnimSite()
HAnimSite122.DEF = "hanim_l_suprapatella_pt"
HAnimSite122.name = "l_suprapatella_pt"
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
""" from sacroiliac to r_hip vertices 2"""
ColorRGBA128 = x3d.ColorRGBA()
ColorRGBA128.USE = "HAnimSegmentLineColorRGBA"

LineSet126.color = ColorRGBA128

Shape125.geometry = LineSet126

HAnimSegment105.children.append(Shape125)
HAnimSite129 = x3d.HAnimSite()
HAnimSite129.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite129.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite129.translation = [-0.1421,0.4992,0.0310]
TouchSensor130 = x3d.TouchSensor()
TouchSensor130.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite129.children.append(TouchSensor130)
Shape131 = x3d.Shape()
Shape131.USE = "HAnimSiteShape"

HAnimSite129.children.append(Shape131)

HAnimSegment105.children.append(HAnimSite129)
HAnimSite132 = x3d.HAnimSite()
HAnimSite132.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite132.name = "r_femoral_medial_epicondyles_pt"
HAnimSite132.translation = [-0.0221,0.5014,0.0289]
TouchSensor133 = x3d.TouchSensor()
TouchSensor133.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite132.children.append(TouchSensor133)
Shape134 = x3d.Shape()
Shape134.USE = "HAnimSiteShape"

HAnimSite132.children.append(Shape134)

HAnimSegment105.children.append(HAnimSite132)
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.DEF = "hanim_r_knee_crease_pt"
HAnimSite135.name = "r_knee_crease_pt"
HAnimSite135.translation = [-0.0825,0.4932,-0.0326]
TouchSensor136 = x3d.TouchSensor()
TouchSensor136.description = "HAnimSite r_knee_crease_pt"

HAnimSite135.children.append(TouchSensor136)
Shape137 = x3d.Shape()
Shape137.USE = "HAnimSiteShape"

HAnimSite135.children.append(Shape137)

HAnimSegment105.children.append(HAnimSite135)
HAnimSite138 = x3d.HAnimSite()
HAnimSite138.DEF = "hanim_r_suprapatella_pt"
HAnimSite138.name = "r_suprapatella_pt"
TouchSensor139 = x3d.TouchSensor()
TouchSensor139.description = "HAnimSite r_suprapatella_pt"

HAnimSite138.children.append(TouchSensor139)
Shape140 = x3d.Shape()
Shape140.USE = "HAnimSiteShape"

HAnimSite138.children.append(Shape140)

HAnimSegment105.children.append(HAnimSite138)

HAnimJoint104.children.append(HAnimSegment105)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.DEF = "hanim_l_hip"
HAnimJoint141.name = "l_hip"
HAnimJoint141.center = [0.0961,0.9124,-0.0001]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.DEF = "hanim_l_thigh"
HAnimSegment142.name = "l_thigh"
Transform143 = x3d.Transform()
Transform143.translation = [0.0961,0.9124,-0.0001]
Transform144 = x3d.Transform()
""" Empty Transform """
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
""" from l_hip to l_knee vertices 2"""
ColorRGBA149 = x3d.ColorRGBA()
ColorRGBA149.USE = "HAnimSegmentLineColorRGBA"

LineSet147.color = ColorRGBA149

Shape146.geometry = LineSet147

HAnimSegment142.children.append(Shape146)
HAnimSite150 = x3d.HAnimSite()
HAnimSite150.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite150.name = "l_lateral_malleolus_pt"
HAnimSite150.translation = [0.1308,0.0597,-0.1032]
TouchSensor151 = x3d.TouchSensor()
TouchSensor151.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite150.children.append(TouchSensor151)
Shape152 = x3d.Shape()
Shape152.USE = "HAnimSiteShape"

HAnimSite150.children.append(Shape152)

HAnimSegment142.children.append(HAnimSite150)
HAnimSite153 = x3d.HAnimSite()
HAnimSite153.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite153.name = "l_medial_malleolus_pt"
HAnimSite153.translation = [0.0890,0.0716,-0.0881]
TouchSensor154 = x3d.TouchSensor()
TouchSensor154.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite153.children.append(TouchSensor154)
Shape155 = x3d.Shape()
Shape155.USE = "HAnimSiteShape"

HAnimSite153.children.append(Shape155)

HAnimSegment142.children.append(HAnimSite153)
HAnimSite156 = x3d.HAnimSite()
HAnimSite156.DEF = "hanim_l_tibiale_pt"
HAnimSite156.name = "l_tibiale_pt"
TouchSensor157 = x3d.TouchSensor()
TouchSensor157.description = "HAnimSite l_tibiale_pt"

HAnimSite156.children.append(TouchSensor157)
Shape158 = x3d.Shape()
Shape158.USE = "HAnimSiteShape"

HAnimSite156.children.append(Shape158)

HAnimSegment142.children.append(HAnimSite156)

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.DEF = "hanim_l_knee"
HAnimJoint159.name = "l_knee"
HAnimJoint159.center = [0.1040,0.4867,0.0308]
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.DEF = "hanim_l_calf"
HAnimSegment160.name = "l_calf"
Transform161 = x3d.Transform()
Transform161.translation = [0.1040,0.4867,0.0308]
Transform162 = x3d.Transform()
""" Empty Transform """
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
""" from l_knee to l_talocrural vertices 2"""
ColorRGBA167 = x3d.ColorRGBA()
ColorRGBA167.USE = "HAnimSegmentLineColorRGBA"

LineSet165.color = ColorRGBA167

Shape164.geometry = LineSet165

HAnimSegment160.children.append(Shape164)
HAnimSite168 = x3d.HAnimSite()
HAnimSite168.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite168.name = "l_calcaneus_posterior_pt"
HAnimSite168.translation = [0.0974,0.0259,-0.1171]
TouchSensor169 = x3d.TouchSensor()
TouchSensor169.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite168.children.append(TouchSensor169)
Shape170 = x3d.Shape()
Shape170.USE = "HAnimSiteShape"

HAnimSite168.children.append(Shape170)

HAnimSegment160.children.append(HAnimSite168)
HAnimSite171 = x3d.HAnimSite()
HAnimSite171.DEF = "hanim_l_sphyrion_pt"
HAnimSite171.name = "l_sphyrion_pt"
HAnimSite171.translation = [0.0890,0.0575,-0.0943]
TouchSensor172 = x3d.TouchSensor()
TouchSensor172.description = "HAnimSite l_sphyrion_pt"

HAnimSite171.children.append(TouchSensor172)
Shape173 = x3d.Shape()
Shape173.USE = "HAnimSiteShape"

HAnimSite171.children.append(Shape173)

HAnimSegment160.children.append(HAnimSite171)

HAnimJoint159.children.append(HAnimSegment160)
HAnimJoint174 = x3d.HAnimJoint()
HAnimJoint174.DEF = "hanim_l_talocrural"
HAnimJoint174.name = "l_talocrural"
HAnimJoint174.center = [0.1101,0.0656,-0.0736]
HAnimSegment175 = x3d.HAnimSegment()
HAnimSegment175.DEF = "hanim_l_talus"
HAnimSegment175.name = "l_talus"
Transform176 = x3d.Transform()
Transform176.scale = [0.15,0.15,0.15]
Transform176.translation = [0.08,0.06,-0.025]
Transform176.rotation = [1,0,0,-1.57]
""" Transform left foot """
Transform177 = x3d.Transform()
""" Empty Transform left foot """
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
""" from l_talocrural to l_metatarsophalangeal_2 vertices 2"""
ColorRGBA182 = x3d.ColorRGBA()
ColorRGBA182.USE = "HAnimSegmentLineColorRGBA"

LineSet180.color = ColorRGBA182

Shape179.geometry = LineSet180

HAnimSegment175.children.append(Shape179)

HAnimJoint174.children.append(HAnimSegment175)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint183.name = "l_metatarsophalangeal_2"
HAnimJoint183.center = [0.0824,0.0064,-0.0040]

HAnimJoint174.children.append(HAnimJoint183)

HAnimJoint159.children.append(HAnimJoint174)

HAnimJoint141.children.append(HAnimJoint159)

HAnimJoint104.children.append(HAnimJoint141)
HAnimJoint184 = x3d.HAnimJoint()
HAnimJoint184.DEF = "hanim_r_hip"
HAnimJoint184.name = "r_hip"
HAnimJoint184.center = [-0.0950,0.9171,0.0029]
HAnimSegment185 = x3d.HAnimSegment()
HAnimSegment185.DEF = "hanim_r_thigh"
HAnimSegment185.name = "r_thigh"
Transform186 = x3d.Transform()
Transform186.translation = [-0.0950,0.9171,0.0029]
Transform187 = x3d.Transform()
""" Empty Transform """
Shape188 = x3d.Shape()
Shape188.USE = "HAnimJointShape"

Transform187.children.append(Shape188)

Transform186.children.append(Transform187)

HAnimSegment185.children.append(Transform186)
Shape189 = x3d.Shape()
LineSet190 = x3d.LineSet()
LineSet190.vertexCount = [2]
Coordinate191 = x3d.Coordinate()

LineSet190.coord = Coordinate191
""" from r_hip to r_knee vertices 2"""
ColorRGBA192 = x3d.ColorRGBA()
ColorRGBA192.USE = "HAnimSegmentLineColorRGBA"

LineSet190.color = ColorRGBA192

Shape189.geometry = LineSet190

HAnimSegment185.children.append(Shape189)
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite193.name = "r_lateral_malleolus_pt"
HAnimSite193.translation = [-0.1006,0.0658,-0.1075]
TouchSensor194 = x3d.TouchSensor()
TouchSensor194.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite193.children.append(TouchSensor194)
Shape195 = x3d.Shape()
Shape195.USE = "HAnimSiteShape"

HAnimSite193.children.append(Shape195)

HAnimSegment185.children.append(HAnimSite193)
HAnimSite196 = x3d.HAnimSite()
HAnimSite196.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite196.name = "r_medial_malleolus_pt"
HAnimSite196.translation = [-0.0591,0.0760,-0.0928]
TouchSensor197 = x3d.TouchSensor()
TouchSensor197.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite196.children.append(TouchSensor197)
Shape198 = x3d.Shape()
Shape198.USE = "HAnimSiteShape"

HAnimSite196.children.append(Shape198)

HAnimSegment185.children.append(HAnimSite196)
HAnimSite199 = x3d.HAnimSite()
HAnimSite199.DEF = "hanim_r_tibiale_pt"
HAnimSite199.name = "r_tibiale_pt"
TouchSensor200 = x3d.TouchSensor()
TouchSensor200.description = "HAnimSite r_tibiale_pt"

HAnimSite199.children.append(TouchSensor200)
Shape201 = x3d.Shape()
Shape201.USE = "HAnimSiteShape"

HAnimSite199.children.append(Shape201)

HAnimSegment185.children.append(HAnimSite199)

HAnimJoint184.children.append(HAnimSegment185)
HAnimJoint202 = x3d.HAnimJoint()
HAnimJoint202.DEF = "hanim_r_knee"
HAnimJoint202.name = "r_knee"
HAnimJoint202.center = [-0.0867,0.4913,0.0318]
HAnimSegment203 = x3d.HAnimSegment()
HAnimSegment203.DEF = "hanim_r_calf"
HAnimSegment203.name = "r_calf"
Transform204 = x3d.Transform()
Transform204.translation = [-0.0867,0.4913,0.0318]
Transform205 = x3d.Transform()
""" Empty Transform """
Shape206 = x3d.Shape()
Shape206.USE = "HAnimJointShape"

Transform205.children.append(Shape206)

Transform204.children.append(Transform205)

HAnimSegment203.children.append(Transform204)
Shape207 = x3d.Shape()
LineSet208 = x3d.LineSet()
LineSet208.vertexCount = [2]
Coordinate209 = x3d.Coordinate()

LineSet208.coord = Coordinate209
""" from r_knee to r_talocrural vertices 2"""
ColorRGBA210 = x3d.ColorRGBA()
ColorRGBA210.USE = "HAnimSegmentLineColorRGBA"

LineSet208.color = ColorRGBA210

Shape207.geometry = LineSet208

HAnimSegment203.children.append(Shape207)
HAnimSite211 = x3d.HAnimSite()
HAnimSite211.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite211.name = "r_calcaneus_posterior_pt"
HAnimSite211.translation = [-0.0692,0.0297,-0.1221]
TouchSensor212 = x3d.TouchSensor()
TouchSensor212.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite211.children.append(TouchSensor212)
Shape213 = x3d.Shape()
Shape213.USE = "HAnimSiteShape"

HAnimSite211.children.append(Shape213)

HAnimSegment203.children.append(HAnimSite211)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.DEF = "hanim_r_sphyrion_pt"
HAnimSite214.name = "r_sphyrion_pt"
HAnimSite214.translation = [-0.0603,0.0610,-0.1002]
TouchSensor215 = x3d.TouchSensor()
TouchSensor215.description = "HAnimSite r_sphyrion_pt"

HAnimSite214.children.append(TouchSensor215)
Shape216 = x3d.Shape()
Shape216.USE = "HAnimSiteShape"

HAnimSite214.children.append(Shape216)

HAnimSegment203.children.append(HAnimSite214)

HAnimJoint202.children.append(HAnimSegment203)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.DEF = "hanim_r_talocrural"
HAnimJoint217.name = "r_talocrural"
HAnimJoint217.center = [-0.0801,0.0712,-0.0766]
HAnimSegment218 = x3d.HAnimSegment()
HAnimSegment218.DEF = "hanim_r_talus"
HAnimSegment218.name = "r_talus"
Transform219 = x3d.Transform()
Transform219.scale = [0.15,0.15,0.15]
Transform219.translation = [-0.05,0.06,-0.025]
Transform219.rotation = [1,0,0,-1.57]
""" Transform right foot """
Transform220 = x3d.Transform()
""" Empty Transform right foot """
Shape221 = x3d.Shape()
Shape221.USE = "HAnimJointShape"

Transform220.children.append(Shape221)

Transform219.children.append(Transform220)

HAnimSegment218.children.append(Transform219)
Shape222 = x3d.Shape()
LineSet223 = x3d.LineSet()
LineSet223.vertexCount = [2]
Coordinate224 = x3d.Coordinate()

LineSet223.coord = Coordinate224
""" from r_talocrural to r_metatarsophalangeal_2 vertices 2"""
ColorRGBA225 = x3d.ColorRGBA()
ColorRGBA225.USE = "HAnimSegmentLineColorRGBA"

LineSet223.color = ColorRGBA225

Shape222.geometry = LineSet223

HAnimSegment218.children.append(Shape222)

HAnimJoint217.children.append(HAnimSegment218)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint226.name = "r_metatarsophalangeal_2"
HAnimJoint226.center = [-0.0823,0.0064,-0.0040]

HAnimJoint217.children.append(HAnimJoint226)

HAnimJoint202.children.append(HAnimJoint217)

HAnimJoint184.children.append(HAnimJoint202)

HAnimJoint104.children.append(HAnimJoint184)

HAnimJoint52.children.append(HAnimJoint104)
HAnimJoint227 = x3d.HAnimJoint()
HAnimJoint227.DEF = "hanim_vl5"
HAnimJoint227.name = "vl5"
HAnimJoint227.center = [0.0028,1.0568,-0.0776]
HAnimSegment228 = x3d.HAnimSegment()
HAnimSegment228.DEF = "hanim_l5"
HAnimSegment228.name = "l5"
Transform229 = x3d.Transform()
Transform229.translation = [0.0028,1.0568,-0.0776]
Transform230 = x3d.Transform()
""" Empty Transform """
Shape231 = x3d.Shape()
Shape231.USE = "HAnimJointShape"

Transform230.children.append(Shape231)

Transform229.children.append(Transform230)

HAnimSegment228.children.append(Transform229)
Shape232 = x3d.Shape()
LineSet233 = x3d.LineSet()
LineSet233.vertexCount = [2]
Coordinate234 = x3d.Coordinate()

LineSet233.coord = Coordinate234
""" from vl5 to skullbase vertices 2"""
ColorRGBA235 = x3d.ColorRGBA()
ColorRGBA235.USE = "HAnimSegmentLineColorRGBA"

LineSet233.color = ColorRGBA235

Shape232.geometry = LineSet233

HAnimSegment228.children.append(Shape232)
HAnimSite236 = x3d.HAnimSite()
HAnimSite236.DEF = "hanim_glabella_pt"
HAnimSite236.name = "glabella_pt"
TouchSensor237 = x3d.TouchSensor()
TouchSensor237.description = "HAnimSite glabella_pt"

HAnimSite236.children.append(TouchSensor237)
Shape238 = x3d.Shape()
Shape238.USE = "HAnimSiteShape"

HAnimSite236.children.append(Shape238)

HAnimSegment228.children.append(HAnimSite236)
HAnimSite239 = x3d.HAnimSite()
HAnimSite239.DEF = "hanim_l_ectocanthus_pt"
HAnimSite239.name = "l_ectocanthus_pt"
TouchSensor240 = x3d.TouchSensor()
TouchSensor240.description = "HAnimSite l_ectocanthus_pt"

HAnimSite239.children.append(TouchSensor240)
Shape241 = x3d.Shape()
Shape241.USE = "HAnimSiteShape"

HAnimSite239.children.append(Shape241)

HAnimSegment228.children.append(HAnimSite239)
HAnimSite242 = x3d.HAnimSite()
HAnimSite242.DEF = "hanim_l_infraorbitale_pt"
HAnimSite242.name = "l_infraorbitale_pt"
HAnimSite242.translation = [0.0341,1.6171,0.0752]
TouchSensor243 = x3d.TouchSensor()
TouchSensor243.description = "HAnimSite l_infraorbitale_pt"

HAnimSite242.children.append(TouchSensor243)
Shape244 = x3d.Shape()
Shape244.USE = "HAnimSiteShape"

HAnimSite242.children.append(Shape244)

HAnimSegment228.children.append(HAnimSite242)
HAnimSite245 = x3d.HAnimSite()
HAnimSite245.DEF = "hanim_l_tragion_pt"
HAnimSite245.name = "l_tragion_pt"
HAnimSite245.translation = [0.0739,1.6348,0.0282]
TouchSensor246 = x3d.TouchSensor()
TouchSensor246.description = "HAnimSite l_tragion_pt"

HAnimSite245.children.append(TouchSensor246)
Shape247 = x3d.Shape()
Shape247.USE = "HAnimSiteShape"

HAnimSite245.children.append(Shape247)

HAnimSegment228.children.append(HAnimSite245)
HAnimSite248 = x3d.HAnimSite()
HAnimSite248.DEF = "hanim_nuchale_pt"
HAnimSite248.name = "nuchale_pt"
HAnimSite248.translation = [0.0039,1.5972,-0.0796]
TouchSensor249 = x3d.TouchSensor()
TouchSensor249.description = "HAnimSite nuchale_pt"

HAnimSite248.children.append(TouchSensor249)
Shape250 = x3d.Shape()
Shape250.USE = "HAnimSiteShape"

HAnimSite248.children.append(Shape250)

HAnimSegment228.children.append(HAnimSite248)
HAnimSite251 = x3d.HAnimSite()
HAnimSite251.DEF = "hanim_opisthocranion_pt"
HAnimSite251.name = "opisthocranion_pt"
TouchSensor252 = x3d.TouchSensor()
TouchSensor252.description = "HAnimSite opisthocranion_pt"

HAnimSite251.children.append(TouchSensor252)
Shape253 = x3d.Shape()
Shape253.USE = "HAnimSiteShape"

HAnimSite251.children.append(Shape253)

HAnimSegment228.children.append(HAnimSite251)
HAnimSite254 = x3d.HAnimSite()
HAnimSite254.DEF = "hanim_r_ectocanthus_pt"
HAnimSite254.name = "r_ectocanthus_pt"
TouchSensor255 = x3d.TouchSensor()
TouchSensor255.description = "HAnimSite r_ectocanthus_pt"

HAnimSite254.children.append(TouchSensor255)
Shape256 = x3d.Shape()
Shape256.USE = "HAnimSiteShape"

HAnimSite254.children.append(Shape256)

HAnimSegment228.children.append(HAnimSite254)
HAnimSite257 = x3d.HAnimSite()
HAnimSite257.DEF = "hanim_r_infraorbitale_pt"
HAnimSite257.name = "r_infraorbitale_pt"
HAnimSite257.translation = [-0.0237,1.6171,0.0752]
TouchSensor258 = x3d.TouchSensor()
TouchSensor258.description = "HAnimSite r_infraorbitale_pt"

HAnimSite257.children.append(TouchSensor258)
Shape259 = x3d.Shape()
Shape259.USE = "HAnimSiteShape"

HAnimSite257.children.append(Shape259)

HAnimSegment228.children.append(HAnimSite257)
HAnimSite260 = x3d.HAnimSite()
HAnimSite260.DEF = "hanim_r_tragion_pt"
HAnimSite260.name = "r_tragion_pt"
HAnimSite260.translation = [-0.0646,1.6347,0.0302]
TouchSensor261 = x3d.TouchSensor()
TouchSensor261.description = "HAnimSite r_tragion_pt"

HAnimSite260.children.append(TouchSensor261)
Shape262 = x3d.Shape()
Shape262.USE = "HAnimSiteShape"

HAnimSite260.children.append(Shape262)

HAnimSegment228.children.append(HAnimSite260)
HAnimSite263 = x3d.HAnimSite()
HAnimSite263.DEF = "hanim_sellion_pt"
HAnimSite263.name = "sellion_pt"
HAnimSite263.translation = [0.0058,1.6316,0.0852]
TouchSensor264 = x3d.TouchSensor()
TouchSensor264.description = "HAnimSite sellion_pt"

HAnimSite263.children.append(TouchSensor264)
Shape265 = x3d.Shape()
Shape265.USE = "HAnimSiteShape"

HAnimSite263.children.append(Shape265)

HAnimSegment228.children.append(HAnimSite263)
HAnimSite266 = x3d.HAnimSite()
HAnimSite266.DEF = "hanim_skull_vertex_pt"
HAnimSite266.name = "skull_vertex_pt"
HAnimSite266.translation = [0.0050,1.7504,0.0055]
TouchSensor267 = x3d.TouchSensor()
TouchSensor267.description = "HAnimSite skull_vertex_pt"

HAnimSite266.children.append(TouchSensor267)
Shape268 = x3d.Shape()
Shape268.USE = "HAnimSiteShape"

HAnimSite266.children.append(Shape268)

HAnimSegment228.children.append(HAnimSite266)
Shape269 = x3d.Shape()
LineSet270 = x3d.LineSet()
LineSet270.vertexCount = [2]
Coordinate271 = x3d.Coordinate()

LineSet270.coord = Coordinate271
""" from vl5 to l_shoulder vertices 2"""
ColorRGBA272 = x3d.ColorRGBA()
ColorRGBA272.USE = "HAnimSegmentLineColorRGBA"

LineSet270.color = ColorRGBA272

Shape269.geometry = LineSet270

HAnimSegment228.children.append(Shape269)
HAnimSite273 = x3d.HAnimSite()
HAnimSite273.DEF = "hanim_l_bideltoid_pt"
HAnimSite273.name = "l_bideltoid_pt"
TouchSensor274 = x3d.TouchSensor()
TouchSensor274.description = "HAnimSite l_bideltoid_pt"

HAnimSite273.children.append(TouchSensor274)
Shape275 = x3d.Shape()
Shape275.USE = "HAnimSiteShape"

HAnimSite273.children.append(Shape275)

HAnimSegment228.children.append(HAnimSite273)
HAnimSite276 = x3d.HAnimSite()
HAnimSite276.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite276.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite276.translation = [0.2280,1.1482,-0.1100]
TouchSensor277 = x3d.TouchSensor()
TouchSensor277.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite276.children.append(TouchSensor277)
Shape278 = x3d.Shape()
Shape278.USE = "HAnimSiteShape"

HAnimSite276.children.append(Shape278)

HAnimSegment228.children.append(HAnimSite276)
Shape279 = x3d.Shape()
LineSet280 = x3d.LineSet()
LineSet280.vertexCount = [2]
Coordinate281 = x3d.Coordinate()

LineSet280.coord = Coordinate281
""" from vl5 to r_shoulder vertices 2"""
ColorRGBA282 = x3d.ColorRGBA()
ColorRGBA282.USE = "HAnimSegmentLineColorRGBA"

LineSet280.color = ColorRGBA282

Shape279.geometry = LineSet280

HAnimSegment228.children.append(Shape279)
HAnimSite283 = x3d.HAnimSite()
HAnimSite283.DEF = "hanim_r_bideltoid_pt"
HAnimSite283.name = "r_bideltoid_pt"
TouchSensor284 = x3d.TouchSensor()
TouchSensor284.description = "HAnimSite r_bideltoid_pt"

HAnimSite283.children.append(TouchSensor284)
Shape285 = x3d.Shape()
Shape285.USE = "HAnimSiteShape"

HAnimSite283.children.append(Shape285)

HAnimSegment228.children.append(HAnimSite283)
HAnimSite286 = x3d.HAnimSite()
HAnimSite286.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite286.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite286.translation = [-0.2224,1.1517,-0.1033]
TouchSensor287 = x3d.TouchSensor()
TouchSensor287.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite286.children.append(TouchSensor287)
Shape288 = x3d.Shape()
Shape288.USE = "HAnimSiteShape"

HAnimSite286.children.append(Shape288)

HAnimSegment228.children.append(HAnimSite286)

HAnimJoint227.children.append(HAnimSegment228)
HAnimJoint289 = x3d.HAnimJoint()
HAnimJoint289.DEF = "hanim_skullbase"
HAnimJoint289.name = "skullbase"
HAnimJoint289.center = [0.0044,1.6209,0.0236]

HAnimJoint227.children.append(HAnimJoint289)
HAnimJoint290 = x3d.HAnimJoint()
HAnimJoint290.DEF = "hanim_l_shoulder"
HAnimJoint290.name = "l_shoulder"
HAnimJoint290.center = [0.2029,1.4376,-0.0387]
HAnimSegment291 = x3d.HAnimSegment()
HAnimSegment291.DEF = "hanim_l_upperarm"
HAnimSegment291.name = "l_upperarm"
Transform292 = x3d.Transform()
Transform292.translation = [0.2029,1.4376,-0.0387]
Transform293 = x3d.Transform()
""" Empty Transform """
Shape294 = x3d.Shape()
Shape294.USE = "HAnimJointShape"

Transform293.children.append(Shape294)

Transform292.children.append(Transform293)

HAnimSegment291.children.append(Transform292)
Shape295 = x3d.Shape()
LineSet296 = x3d.LineSet()
LineSet296.vertexCount = [2]
Coordinate297 = x3d.Coordinate()

LineSet296.coord = Coordinate297
""" from l_shoulder to l_elbow vertices 2"""
ColorRGBA298 = x3d.ColorRGBA()
ColorRGBA298.USE = "HAnimSegmentLineColorRGBA"

LineSet296.color = ColorRGBA298

Shape295.geometry = LineSet296

HAnimSegment291.children.append(Shape295)
HAnimSite299 = x3d.HAnimSite()
HAnimSite299.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite299.name = "l_humeral_medial_epicondyles_pt"
HAnimSite299.translation = [0.1735,1.1272,-0.1113]
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite299.children.append(TouchSensor300)
Shape301 = x3d.Shape()
Shape301.USE = "HAnimSiteShape"

HAnimSite299.children.append(Shape301)

HAnimSegment291.children.append(HAnimSite299)
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.DEF = "hanim_l_olecranon_pt"
HAnimSite302.name = "l_olecranon_pt"
HAnimSite302.translation = [-0.1962,1.1375,-0.1123]
TouchSensor303 = x3d.TouchSensor()
TouchSensor303.description = "HAnimSite l_olecranon_pt"

HAnimSite302.children.append(TouchSensor303)
Shape304 = x3d.Shape()
Shape304.USE = "HAnimSiteShape"

HAnimSite302.children.append(Shape304)

HAnimSegment291.children.append(HAnimSite302)
HAnimSite305 = x3d.HAnimSite()
HAnimSite305.DEF = "hanim_l_radial_styloid_pt"
HAnimSite305.name = "l_radial_styloid_pt"
HAnimSite305.translation = [0.1901,0.8645,-0.0415]
TouchSensor306 = x3d.TouchSensor()
TouchSensor306.description = "HAnimSite l_radial_styloid_pt"

HAnimSite305.children.append(TouchSensor306)
Shape307 = x3d.Shape()
Shape307.USE = "HAnimSiteShape"

HAnimSite305.children.append(Shape307)

HAnimSegment291.children.append(HAnimSite305)
HAnimSite308 = x3d.HAnimSite()
HAnimSite308.DEF = "hanim_l_radiale_pt"
HAnimSite308.name = "l_radiale_pt"
HAnimSite308.translation = [0.2182,1.1212,-0.1167]
TouchSensor309 = x3d.TouchSensor()
TouchSensor309.description = "HAnimSite l_radiale_pt"

HAnimSite308.children.append(TouchSensor309)
Shape310 = x3d.Shape()
Shape310.USE = "HAnimSiteShape"

HAnimSite308.children.append(Shape310)

HAnimSegment291.children.append(HAnimSite308)

HAnimJoint290.children.append(HAnimSegment291)
HAnimJoint311 = x3d.HAnimJoint()
HAnimJoint311.DEF = "hanim_l_elbow"
HAnimJoint311.name = "l_elbow"
HAnimJoint311.center = [0.2014,1.1357,-0.0682]
HAnimSegment312 = x3d.HAnimSegment()
HAnimSegment312.DEF = "hanim_l_forearm"
HAnimSegment312.name = "l_forearm"
Transform313 = x3d.Transform()
Transform313.translation = [0.2014,1.1357,-0.0682]
Transform314 = x3d.Transform()
""" Empty Transform """
Shape315 = x3d.Shape()
Shape315.USE = "HAnimJointShape"

Transform314.children.append(Shape315)

Transform313.children.append(Transform314)

HAnimSegment312.children.append(Transform313)
Shape316 = x3d.Shape()
LineSet317 = x3d.LineSet()
LineSet317.vertexCount = [2]
Coordinate318 = x3d.Coordinate()

LineSet317.coord = Coordinate318
""" from l_elbow to l_radiocarpal vertices 2"""
ColorRGBA319 = x3d.ColorRGBA()
ColorRGBA319.USE = "HAnimSegmentLineColorRGBA"

LineSet317.color = ColorRGBA319

Shape316.geometry = LineSet317

HAnimSegment312.children.append(Shape316)
HAnimSite320 = x3d.HAnimSite()
HAnimSite320.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite320.name = "l_ulnar_styloid_pt"
HAnimSite320.translation = [-0.2142,0.8529,-0.0648]
TouchSensor321 = x3d.TouchSensor()
TouchSensor321.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite320.children.append(TouchSensor321)
Shape322 = x3d.Shape()
Shape322.USE = "HAnimSiteShape"

HAnimSite320.children.append(Shape322)

HAnimSegment312.children.append(HAnimSite320)

HAnimJoint311.children.append(HAnimSegment312)
HAnimJoint323 = x3d.HAnimJoint()
HAnimJoint323.DEF = "hanim_l_radiocarpal"
HAnimJoint323.name = "l_radiocarpal"
HAnimJoint323.center = [0.1984,0.8663,-0.0583]

HAnimJoint311.children.append(HAnimJoint323)

HAnimJoint290.children.append(HAnimJoint311)

HAnimJoint227.children.append(HAnimJoint290)
HAnimJoint324 = x3d.HAnimJoint()
HAnimJoint324.DEF = "hanim_r_shoulder"
HAnimJoint324.name = "r_shoulder"
HAnimJoint324.center = [-0.1907,1.4407,-0.0325]
HAnimSegment325 = x3d.HAnimSegment()
HAnimSegment325.DEF = "hanim_r_upperarm"
HAnimSegment325.name = "r_upperarm"
Transform326 = x3d.Transform()
Transform326.translation = [-0.1907,1.4407,-0.0325]
Transform327 = x3d.Transform()
""" Empty Transform """
Shape328 = x3d.Shape()
Shape328.USE = "HAnimJointShape"

Transform327.children.append(Shape328)

Transform326.children.append(Transform327)

HAnimSegment325.children.append(Transform326)
Shape329 = x3d.Shape()
LineSet330 = x3d.LineSet()
LineSet330.vertexCount = [2]
Coordinate331 = x3d.Coordinate()

LineSet330.coord = Coordinate331
""" from r_shoulder to r_elbow vertices 2"""
ColorRGBA332 = x3d.ColorRGBA()
ColorRGBA332.USE = "HAnimSegmentLineColorRGBA"

LineSet330.color = ColorRGBA332

Shape329.geometry = LineSet330

HAnimSegment325.children.append(Shape329)
HAnimSite333 = x3d.HAnimSite()
HAnimSite333.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite333.name = "r_humeral_medial_epicondyles_pt"
HAnimSite333.translation = [-0.1680,1.1298,-0.1062]
TouchSensor334 = x3d.TouchSensor()
TouchSensor334.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite333.children.append(TouchSensor334)
Shape335 = x3d.Shape()
Shape335.USE = "HAnimSiteShape"

HAnimSite333.children.append(Shape335)

HAnimSegment325.children.append(HAnimSite333)
HAnimSite336 = x3d.HAnimSite()
HAnimSite336.DEF = "hanim_r_olecranon_pt"
HAnimSite336.name = "r_olecranon_pt"
HAnimSite336.translation = [-0.1907,1.1405,-0.1065]
TouchSensor337 = x3d.TouchSensor()
TouchSensor337.description = "HAnimSite r_olecranon_pt"

HAnimSite336.children.append(TouchSensor337)
Shape338 = x3d.Shape()
Shape338.USE = "HAnimSiteShape"

HAnimSite336.children.append(Shape338)

HAnimSegment325.children.append(HAnimSite336)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.DEF = "hanim_r_radial_styloid_pt"
HAnimSite339.name = "r_radial_styloid_pt"
HAnimSite339.translation = [-0.1884,0.8676,-0.0360]
TouchSensor340 = x3d.TouchSensor()
TouchSensor340.description = "HAnimSite r_radial_styloid_pt"

HAnimSite339.children.append(TouchSensor340)
Shape341 = x3d.Shape()
Shape341.USE = "HAnimSiteShape"

HAnimSite339.children.append(Shape341)

HAnimSegment325.children.append(HAnimSite339)
HAnimSite342 = x3d.HAnimSite()
HAnimSite342.DEF = "hanim_r_radiale_pt"
HAnimSite342.name = "r_radiale_pt"
HAnimSite342.translation = [-0.2130,1.1305,-0.1091]
TouchSensor343 = x3d.TouchSensor()
TouchSensor343.description = "HAnimSite r_radiale_pt"

HAnimSite342.children.append(TouchSensor343)
Shape344 = x3d.Shape()
Shape344.USE = "HAnimSiteShape"

HAnimSite342.children.append(Shape344)

HAnimSegment325.children.append(HAnimSite342)

HAnimJoint324.children.append(HAnimSegment325)
HAnimJoint345 = x3d.HAnimJoint()
HAnimJoint345.DEF = "hanim_r_elbow"
HAnimJoint345.name = "r_elbow"
HAnimJoint345.center = [-0.1949,1.1388,-0.0620]
HAnimSegment346 = x3d.HAnimSegment()
HAnimSegment346.DEF = "hanim_r_forearm"
HAnimSegment346.name = "r_forearm"
Transform347 = x3d.Transform()
Transform347.translation = [-0.1949,1.1388,-0.0620]
Transform348 = x3d.Transform()
""" Empty Transform """
Shape349 = x3d.Shape()
Shape349.USE = "HAnimJointShape"

Transform348.children.append(Shape349)

Transform347.children.append(Transform348)

HAnimSegment346.children.append(Transform347)
Shape350 = x3d.Shape()
LineSet351 = x3d.LineSet()
LineSet351.vertexCount = [2]
Coordinate352 = x3d.Coordinate()

LineSet351.coord = Coordinate352
""" from r_elbow to r_radiocarpal vertices 2"""
ColorRGBA353 = x3d.ColorRGBA()
ColorRGBA353.USE = "HAnimSegmentLineColorRGBA"

LineSet351.color = ColorRGBA353

Shape350.geometry = LineSet351

HAnimSegment346.children.append(Shape350)
HAnimSite354 = x3d.HAnimSite()
HAnimSite354.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite354.name = "r_ulnar_styloid_pt"
HAnimSite354.translation = [-0.2117,0.8562,-0.0584]
TouchSensor355 = x3d.TouchSensor()
TouchSensor355.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite354.children.append(TouchSensor355)
Shape356 = x3d.Shape()
Shape356.USE = "HAnimSiteShape"

HAnimSite354.children.append(Shape356)

HAnimSegment346.children.append(HAnimSite354)

HAnimJoint345.children.append(HAnimSegment346)
HAnimJoint357 = x3d.HAnimJoint()
HAnimJoint357.DEF = "hanim_r_radiocarpal"
HAnimJoint357.name = "r_radiocarpal"
HAnimJoint357.center = [-0.1959,0.8694,-0.0521]

HAnimJoint345.children.append(HAnimJoint357)

HAnimJoint324.children.append(HAnimJoint345)

HAnimJoint227.children.append(HAnimJoint324)

HAnimJoint52.children.append(HAnimJoint227)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimJoint358 = x3d.HAnimJoint()
HAnimJoint358.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint358)
HAnimJoint359 = x3d.HAnimJoint()
HAnimJoint359.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint359)
HAnimJoint360 = x3d.HAnimJoint()
HAnimJoint360.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint360)
HAnimJoint361 = x3d.HAnimJoint()
HAnimJoint361.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint361)
HAnimJoint362 = x3d.HAnimJoint()
HAnimJoint362.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint362)
HAnimJoint363 = x3d.HAnimJoint()
HAnimJoint363.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint363)
HAnimJoint364 = x3d.HAnimJoint()
HAnimJoint364.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint364)
HAnimJoint365 = x3d.HAnimJoint()
HAnimJoint365.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint365)
HAnimJoint366 = x3d.HAnimJoint()
HAnimJoint366.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint366)
HAnimJoint367 = x3d.HAnimJoint()
HAnimJoint367.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint367)
HAnimJoint368 = x3d.HAnimJoint()
HAnimJoint368.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint368)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint369)
HAnimJoint370 = x3d.HAnimJoint()
HAnimJoint370.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint370)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint371)
HAnimJoint372 = x3d.HAnimJoint()
HAnimJoint372.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint372)
HAnimJoint373 = x3d.HAnimJoint()
HAnimJoint373.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint373)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint374)
HAnimJoint375 = x3d.HAnimJoint()
HAnimJoint375.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint375)
HAnimSegment376 = x3d.HAnimSegment()
HAnimSegment376.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment376)
HAnimSegment377 = x3d.HAnimSegment()
HAnimSegment377.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment377)
HAnimSegment378 = x3d.HAnimSegment()
HAnimSegment378.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment378)
HAnimSegment379 = x3d.HAnimSegment()
HAnimSegment379.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment379)
HAnimSegment380 = x3d.HAnimSegment()
HAnimSegment380.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment380)
HAnimSegment381 = x3d.HAnimSegment()
HAnimSegment381.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment381)
HAnimSegment382 = x3d.HAnimSegment()
HAnimSegment382.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment382)
HAnimSegment383 = x3d.HAnimSegment()
HAnimSegment383.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment383)
HAnimSegment384 = x3d.HAnimSegment()
HAnimSegment384.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment384)
HAnimSegment385 = x3d.HAnimSegment()
HAnimSegment385.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment385)
HAnimSegment386 = x3d.HAnimSegment()
HAnimSegment386.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment386)
HAnimSegment387 = x3d.HAnimSegment()
HAnimSegment387.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment387)
HAnimSegment388 = x3d.HAnimSegment()
HAnimSegment388.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment388)
HAnimSite389 = x3d.HAnimSite()
HAnimSite389.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite389)
HAnimSite390 = x3d.HAnimSite()
HAnimSite390.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite390)
HAnimSite391 = x3d.HAnimSite()
HAnimSite391.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite391)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite392)
HAnimSite393 = x3d.HAnimSite()
HAnimSite393.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite393)
HAnimSite394 = x3d.HAnimSite()
HAnimSite394.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite394)
HAnimSite395 = x3d.HAnimSite()
HAnimSite395.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite395)
HAnimSite396 = x3d.HAnimSite()
HAnimSite396.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite396)
HAnimSite397 = x3d.HAnimSite()
HAnimSite397.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite397)
HAnimSite398 = x3d.HAnimSite()
HAnimSite398.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite398)
HAnimSite399 = x3d.HAnimSite()
HAnimSite399.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite399)
HAnimSite400 = x3d.HAnimSite()
HAnimSite400.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite400)
HAnimSite401 = x3d.HAnimSite()
HAnimSite401.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite401)
HAnimSite402 = x3d.HAnimSite()
HAnimSite402.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite402)
HAnimSite403 = x3d.HAnimSite()
HAnimSite403.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite403)
HAnimSite404 = x3d.HAnimSite()
HAnimSite404.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite404)
HAnimSite405 = x3d.HAnimSite()
HAnimSite405.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite405)
HAnimSite406 = x3d.HAnimSite()
HAnimSite406.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite406)
HAnimSite407 = x3d.HAnimSite()
HAnimSite407.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite407)
HAnimSite408 = x3d.HAnimSite()
HAnimSite408.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite408)
HAnimSite409 = x3d.HAnimSite()
HAnimSite409.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite409)
HAnimSite410 = x3d.HAnimSite()
HAnimSite410.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite410)
HAnimSite411 = x3d.HAnimSite()
HAnimSite411.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite411)
HAnimSite412 = x3d.HAnimSite()
HAnimSite412.USE = "hanim_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite412)
HAnimSite413 = x3d.HAnimSite()
HAnimSite413.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite413)
HAnimSite414 = x3d.HAnimSite()
HAnimSite414.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite414)
HAnimSite415 = x3d.HAnimSite()
HAnimSite415.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite415)
HAnimSite416 = x3d.HAnimSite()
HAnimSite416.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite416)
HAnimSite417 = x3d.HAnimSite()
HAnimSite417.USE = "hanim_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite417)
HAnimSite418 = x3d.HAnimSite()
HAnimSite418.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite418)
HAnimSite419 = x3d.HAnimSite()
HAnimSite419.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite419)
HAnimSite420 = x3d.HAnimSite()
HAnimSite420.USE = "hanim_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite420)
HAnimSite421 = x3d.HAnimSite()
HAnimSite421.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite421)
HAnimSite422 = x3d.HAnimSite()
HAnimSite422.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite422)
HAnimSite423 = x3d.HAnimSite()
HAnimSite423.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite423)
HAnimSite424 = x3d.HAnimSite()
HAnimSite424.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite424)
HAnimSite425 = x3d.HAnimSite()
HAnimSite425.USE = "hanim_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite425)
HAnimSite426 = x3d.HAnimSite()
HAnimSite426.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite426)
HAnimSite427 = x3d.HAnimSite()
HAnimSite427.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite427)
HAnimSite428 = x3d.HAnimSite()
HAnimSite428.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite428)
HAnimSite429 = x3d.HAnimSite()
HAnimSite429.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite429)
HAnimSite430 = x3d.HAnimSite()
HAnimSite430.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite430)
HAnimSite431 = x3d.HAnimSite()
HAnimSite431.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite431)
HAnimSite432 = x3d.HAnimSite()
HAnimSite432.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite432)
HAnimSite433 = x3d.HAnimSite()
HAnimSite433.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite433)
HAnimSite434 = x3d.HAnimSite()
HAnimSite434.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite434)
HAnimSite435 = x3d.HAnimSite()
HAnimSite435.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite435)
HAnimSite436 = x3d.HAnimSite()
HAnimSite436.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite436)
HAnimSite437 = x3d.HAnimSite()
HAnimSite437.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite437)
HAnimSite438 = x3d.HAnimSite()
HAnimSite438.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite438)
HAnimSite439 = x3d.HAnimSite()
HAnimSite439.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite439)
HAnimSite440 = x3d.HAnimSite()
HAnimSite440.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite440)
HAnimSite441 = x3d.HAnimSite()
HAnimSite441.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite441)
HAnimSite442 = x3d.HAnimSite()
HAnimSite442.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite442)
HAnimSite443 = x3d.HAnimSite()
HAnimSite443.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite443)
HAnimSite444 = x3d.HAnimSite()
HAnimSite444.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite444)

Scene11.children.append(HAnimHumanoid43)

X3D0.Scene = Scene11
f = open("Humanoid1_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
