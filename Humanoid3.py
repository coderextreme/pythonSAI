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
""" from l_talocrural to l_tarsometatarsal_2 vertices 2"""
ColorRGBA182 = x3d.ColorRGBA()
ColorRGBA182.USE = "HAnimSegmentLineColorRGBA"

LineSet180.color = ColorRGBA182

Shape179.geometry = LineSet180

HAnimSegment175.children.append(Shape179)

HAnimJoint174.children.append(HAnimSegment175)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint183.name = "l_tarsometatarsal_2"
HAnimJoint183.center = [0.0800,0.0175,-0.0608]
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.DEF = "hanim_l_metatarsal_2"
HAnimSegment184.name = "l_metatarsal_2"
Transform185 = x3d.Transform()
Transform185.translation = [0.0800,0.0175,-0.0608]
Transform186 = x3d.Transform()
""" Empty Transform """
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
""" from l_tarsometatarsal_2 to l_metatarsophalangeal_2 vertices 2"""
ColorRGBA191 = x3d.ColorRGBA()
ColorRGBA191.USE = "HAnimSegmentLineColorRGBA"

LineSet189.color = ColorRGBA191

Shape188.geometry = LineSet189

HAnimSegment184.children.append(Shape188)

HAnimJoint183.children.append(HAnimSegment184)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint192.name = "l_metatarsophalangeal_2"
HAnimJoint192.center = [0.0824,0.0064,-0.0040]
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSegment193.name = "l_tarsal_proximal_phalanx_2"
Transform194 = x3d.Transform()
Transform194.translation = [0.0824,0.0064,-0.0040]
Transform195 = x3d.Transform()
""" Empty Transform """
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
""" from l_metatarsophalangeal_2 to l_tarsal_distal_interphalangeal_2 vertices 2"""
ColorRGBA200 = x3d.ColorRGBA()
ColorRGBA200.USE = "HAnimSegmentLineColorRGBA"

LineSet198.color = ColorRGBA200

Shape197.geometry = LineSet198

HAnimSegment193.children.append(Shape197)
HAnimSite201 = x3d.HAnimSite()
HAnimSite201.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite201.name = "l_tarsal_distal_phalanx_2_tip"
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
HAnimJoint204.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint204.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint204.center = [0.0841,0.0013,0.0216]

HAnimJoint192.children.append(HAnimJoint204)

HAnimJoint183.children.append(HAnimJoint192)

HAnimJoint174.children.append(HAnimJoint183)

HAnimJoint159.children.append(HAnimJoint174)

HAnimJoint141.children.append(HAnimJoint159)

HAnimJoint104.children.append(HAnimJoint141)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.DEF = "hanim_r_hip"
HAnimJoint205.name = "r_hip"
HAnimJoint205.center = [-0.0950,0.9171,0.0029]
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.DEF = "hanim_r_thigh"
HAnimSegment206.name = "r_thigh"
Transform207 = x3d.Transform()
Transform207.translation = [-0.0950,0.9171,0.0029]
Transform208 = x3d.Transform()
""" Empty Transform """
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
""" from r_hip to r_knee vertices 2"""
ColorRGBA213 = x3d.ColorRGBA()
ColorRGBA213.USE = "HAnimSegmentLineColorRGBA"

LineSet211.color = ColorRGBA213

Shape210.geometry = LineSet211

HAnimSegment206.children.append(Shape210)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite214.name = "r_lateral_malleolus_pt"
HAnimSite214.translation = [-0.1006,0.0658,-0.1075]
TouchSensor215 = x3d.TouchSensor()
TouchSensor215.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite214.children.append(TouchSensor215)
Shape216 = x3d.Shape()
Shape216.USE = "HAnimSiteShape"

HAnimSite214.children.append(Shape216)

HAnimSegment206.children.append(HAnimSite214)
HAnimSite217 = x3d.HAnimSite()
HAnimSite217.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite217.name = "r_medial_malleolus_pt"
HAnimSite217.translation = [-0.0591,0.0760,-0.0928]
TouchSensor218 = x3d.TouchSensor()
TouchSensor218.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite217.children.append(TouchSensor218)
Shape219 = x3d.Shape()
Shape219.USE = "HAnimSiteShape"

HAnimSite217.children.append(Shape219)

HAnimSegment206.children.append(HAnimSite217)
HAnimSite220 = x3d.HAnimSite()
HAnimSite220.DEF = "hanim_r_tibiale_pt"
HAnimSite220.name = "r_tibiale_pt"
TouchSensor221 = x3d.TouchSensor()
TouchSensor221.description = "HAnimSite r_tibiale_pt"

HAnimSite220.children.append(TouchSensor221)
Shape222 = x3d.Shape()
Shape222.USE = "HAnimSiteShape"

HAnimSite220.children.append(Shape222)

HAnimSegment206.children.append(HAnimSite220)

HAnimJoint205.children.append(HAnimSegment206)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.DEF = "hanim_r_knee"
HAnimJoint223.name = "r_knee"
HAnimJoint223.center = [-0.0867,0.4913,0.0318]
HAnimSegment224 = x3d.HAnimSegment()
HAnimSegment224.DEF = "hanim_r_calf"
HAnimSegment224.name = "r_calf"
Transform225 = x3d.Transform()
Transform225.translation = [-0.0867,0.4913,0.0318]
Transform226 = x3d.Transform()
""" Empty Transform """
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
""" from r_knee to r_talocrural vertices 2"""
ColorRGBA231 = x3d.ColorRGBA()
ColorRGBA231.USE = "HAnimSegmentLineColorRGBA"

LineSet229.color = ColorRGBA231

Shape228.geometry = LineSet229

HAnimSegment224.children.append(Shape228)
HAnimSite232 = x3d.HAnimSite()
HAnimSite232.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite232.name = "r_calcaneus_posterior_pt"
HAnimSite232.translation = [-0.0692,0.0297,-0.1221]
TouchSensor233 = x3d.TouchSensor()
TouchSensor233.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite232.children.append(TouchSensor233)
Shape234 = x3d.Shape()
Shape234.USE = "HAnimSiteShape"

HAnimSite232.children.append(Shape234)

HAnimSegment224.children.append(HAnimSite232)
HAnimSite235 = x3d.HAnimSite()
HAnimSite235.DEF = "hanim_r_sphyrion_pt"
HAnimSite235.name = "r_sphyrion_pt"
HAnimSite235.translation = [-0.0603,0.0610,-0.1002]
TouchSensor236 = x3d.TouchSensor()
TouchSensor236.description = "HAnimSite r_sphyrion_pt"

HAnimSite235.children.append(TouchSensor236)
Shape237 = x3d.Shape()
Shape237.USE = "HAnimSiteShape"

HAnimSite235.children.append(Shape237)

HAnimSegment224.children.append(HAnimSite235)

HAnimJoint223.children.append(HAnimSegment224)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.DEF = "hanim_r_talocrural"
HAnimJoint238.name = "r_talocrural"
HAnimJoint238.center = [-0.0801,0.0712,-0.0766]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.DEF = "hanim_r_talus"
HAnimSegment239.name = "r_talus"
Transform240 = x3d.Transform()
Transform240.scale = [0.15,0.15,0.15]
Transform240.translation = [-0.05,0.06,-0.025]
Transform240.rotation = [1,0,0,-1.57]
""" Transform right foot """
Transform241 = x3d.Transform()
""" Empty Transform right foot """
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
""" from r_talocrural to r_tarsometatarsal_2 vertices 2"""
ColorRGBA246 = x3d.ColorRGBA()
ColorRGBA246.USE = "HAnimSegmentLineColorRGBA"

LineSet244.color = ColorRGBA246

Shape243.geometry = LineSet244

HAnimSegment239.children.append(Shape243)

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint247 = x3d.HAnimJoint()
HAnimJoint247.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint247.name = "r_tarsometatarsal_2"
HAnimJoint247.center = [-0.0800,0.0175,-0.0608]
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.DEF = "hanim_r_metatarsal_2"
HAnimSegment248.name = "r_metatarsal_2"
Transform249 = x3d.Transform()
Transform249.translation = [-0.0800,0.0175,-0.0608]
Transform250 = x3d.Transform()
""" Empty Transform """
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
""" from r_tarsometatarsal_2 to r_metatarsophalangeal_2 vertices 2"""
ColorRGBA255 = x3d.ColorRGBA()
ColorRGBA255.USE = "HAnimSegmentLineColorRGBA"

LineSet253.color = ColorRGBA255

Shape252.geometry = LineSet253

HAnimSegment248.children.append(Shape252)

HAnimJoint247.children.append(HAnimSegment248)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint256.name = "r_metatarsophalangeal_2"
HAnimJoint256.center = [-0.0823,0.0064,-0.0040]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSegment257.name = "r_tarsal_proximal_phalanx_2"
Transform258 = x3d.Transform()
Transform258.translation = [-0.0823,0.0064,-0.0040]
Transform259 = x3d.Transform()
""" Empty Transform """
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
""" from r_metatarsophalangeal_2 to r_tarsal_distal_interphalangeal_2 vertices 2"""
ColorRGBA264 = x3d.ColorRGBA()
ColorRGBA264.USE = "HAnimSegmentLineColorRGBA"

LineSet262.color = ColorRGBA264

Shape261.geometry = LineSet262

HAnimSegment257.children.append(Shape261)
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite265.name = "r_tarsal_distal_phalanx_2_tip"
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
HAnimJoint268.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint268.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint268.center = [-0.0841,0.0013,0.0216]

HAnimJoint256.children.append(HAnimJoint268)

HAnimJoint247.children.append(HAnimJoint256)

HAnimJoint238.children.append(HAnimJoint247)

HAnimJoint223.children.append(HAnimJoint238)

HAnimJoint205.children.append(HAnimJoint223)

HAnimJoint104.children.append(HAnimJoint205)

HAnimJoint52.children.append(HAnimJoint104)
HAnimJoint269 = x3d.HAnimJoint()
HAnimJoint269.DEF = "hanim_vl5"
HAnimJoint269.name = "vl5"
HAnimJoint269.center = [0.0028,1.0568,-0.0776]
HAnimSegment270 = x3d.HAnimSegment()
HAnimSegment270.DEF = "hanim_l5"
HAnimSegment270.name = "l5"
Transform271 = x3d.Transform()
Transform271.translation = [0.0028,1.0568,-0.0776]
Transform272 = x3d.Transform()
""" Empty Transform """
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
""" from vl5 to vl4 vertices 2"""
ColorRGBA277 = x3d.ColorRGBA()
ColorRGBA277.USE = "HAnimSegmentLineColorRGBA"

LineSet275.color = ColorRGBA277

Shape274.geometry = LineSet275

HAnimSegment270.children.append(Shape274)

HAnimJoint269.children.append(HAnimSegment270)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.DEF = "hanim_vl4"
HAnimJoint278.name = "vl4"
HAnimJoint278.center = [0.0035,1.0925,-0.0787]
HAnimSegment279 = x3d.HAnimSegment()
HAnimSegment279.DEF = "hanim_l4"
HAnimSegment279.name = "l4"
Transform280 = x3d.Transform()
Transform280.translation = [0.0035,1.0925,-0.0787]
Transform281 = x3d.Transform()
""" Empty Transform """
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
""" from vl4 to vl3 vertices 2"""
ColorRGBA286 = x3d.ColorRGBA()
ColorRGBA286.USE = "HAnimSegmentLineColorRGBA"

LineSet284.color = ColorRGBA286

Shape283.geometry = LineSet284

HAnimSegment279.children.append(Shape283)

HAnimJoint278.children.append(HAnimSegment279)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.DEF = "hanim_vl3"
HAnimJoint287.name = "vl3"
HAnimJoint287.center = [0.0041,1.1276,-0.0796]
HAnimSegment288 = x3d.HAnimSegment()
HAnimSegment288.DEF = "hanim_l3"
HAnimSegment288.name = "l3"
Transform289 = x3d.Transform()
Transform289.translation = [0.0041,1.1276,-0.0796]
Transform290 = x3d.Transform()
""" Empty Transform """
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
""" from vl3 to vl2 vertices 2"""
ColorRGBA295 = x3d.ColorRGBA()
ColorRGBA295.USE = "HAnimSegmentLineColorRGBA"

LineSet293.color = ColorRGBA295

Shape292.geometry = LineSet293

HAnimSegment288.children.append(Shape292)
HAnimSite296 = x3d.HAnimSite()
HAnimSite296.DEF = "hanim_l_rib10_pt"
HAnimSite296.name = "l_rib10_pt"
HAnimSite296.translation = [0.0871,1.1925,0.0992]
TouchSensor297 = x3d.TouchSensor()
TouchSensor297.description = "HAnimSite l_rib10_pt"

HAnimSite296.children.append(TouchSensor297)
Shape298 = x3d.Shape()
Shape298.USE = "HAnimSiteShape"

HAnimSite296.children.append(Shape298)

HAnimSegment288.children.append(HAnimSite296)
HAnimSite299 = x3d.HAnimSite()
HAnimSite299.DEF = "hanim_r_rib10_pt"
HAnimSite299.name = "r_rib10_pt"
HAnimSite299.translation = [-0.0711,1.1941,0.1016]
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimSite r_rib10_pt"

HAnimSite299.children.append(TouchSensor300)
Shape301 = x3d.Shape()
Shape301.USE = "HAnimSiteShape"

HAnimSite299.children.append(Shape301)

HAnimSegment288.children.append(HAnimSite299)
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.DEF = "hanim_spine_2_middle_back_pt"
HAnimSite302.name = "spine_2_middle_back_pt"
TouchSensor303 = x3d.TouchSensor()
TouchSensor303.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite302.children.append(TouchSensor303)
Shape304 = x3d.Shape()
Shape304.USE = "HAnimSiteShape"

HAnimSite302.children.append(Shape304)

HAnimSegment288.children.append(HAnimSite302)

HAnimJoint287.children.append(HAnimSegment288)
HAnimJoint305 = x3d.HAnimJoint()
HAnimJoint305.DEF = "hanim_vl2"
HAnimJoint305.name = "vl2"
HAnimJoint305.center = [0.0045,1.1546,-0.0800]
HAnimSegment306 = x3d.HAnimSegment()
HAnimSegment306.DEF = "hanim_l2"
HAnimSegment306.name = "l2"
Transform307 = x3d.Transform()
Transform307.translation = [0.0045,1.1546,-0.0800]
Transform308 = x3d.Transform()
""" Empty Transform """
Shape309 = x3d.Shape()
Shape309.USE = "HAnimJointShape"

Transform308.children.append(Shape309)

Transform307.children.append(Transform308)

HAnimSegment306.children.append(Transform307)
Shape310 = x3d.Shape()
LineSet311 = x3d.LineSet()
LineSet311.vertexCount = [2]
Coordinate312 = x3d.Coordinate()

LineSet311.coord = Coordinate312
""" from vl2 to vl1 vertices 2"""
ColorRGBA313 = x3d.ColorRGBA()
ColorRGBA313.USE = "HAnimSegmentLineColorRGBA"

LineSet311.color = ColorRGBA313

Shape310.geometry = LineSet311

HAnimSegment306.children.append(Shape310)

HAnimJoint305.children.append(HAnimSegment306)
HAnimJoint314 = x3d.HAnimJoint()
HAnimJoint314.DEF = "hanim_vl1"
HAnimJoint314.name = "vl1"
HAnimJoint314.center = [0.0048,1.1912,-0.0805]
HAnimSegment315 = x3d.HAnimSegment()
HAnimSegment315.DEF = "hanim_l1"
HAnimSegment315.name = "l1"
Transform316 = x3d.Transform()
Transform316.translation = [0.0048,1.1912,-0.0805]
Transform317 = x3d.Transform()
""" Empty Transform """
Shape318 = x3d.Shape()
Shape318.USE = "HAnimJointShape"

Transform317.children.append(Shape318)

Transform316.children.append(Transform317)

HAnimSegment315.children.append(Transform316)
Shape319 = x3d.Shape()
LineSet320 = x3d.LineSet()
LineSet320.vertexCount = [2]
Coordinate321 = x3d.Coordinate()

LineSet320.coord = Coordinate321
""" from vl1 to vt12 vertices 2"""
ColorRGBA322 = x3d.ColorRGBA()
ColorRGBA322.USE = "HAnimSegmentLineColorRGBA"

LineSet320.color = ColorRGBA322

Shape319.geometry = LineSet320

HAnimSegment315.children.append(Shape319)

HAnimJoint314.children.append(HAnimSegment315)
HAnimJoint323 = x3d.HAnimJoint()
HAnimJoint323.DEF = "hanim_vt12"
HAnimJoint323.name = "vt12"
HAnimJoint323.center = [0.0051,1.2278,-0.0808]
HAnimSegment324 = x3d.HAnimSegment()
HAnimSegment324.DEF = "hanim_t12"
HAnimSegment324.name = "t12"
Transform325 = x3d.Transform()
Transform325.translation = [0.0051,1.2278,-0.0808]
Transform326 = x3d.Transform()
""" Empty Transform """
Shape327 = x3d.Shape()
Shape327.USE = "HAnimJointShape"

Transform326.children.append(Shape327)

Transform325.children.append(Transform326)

HAnimSegment324.children.append(Transform325)
Shape328 = x3d.Shape()
LineSet329 = x3d.LineSet()
LineSet329.vertexCount = [2]
Coordinate330 = x3d.Coordinate()

LineSet329.coord = Coordinate330
""" from vt12 to vt11 vertices 2"""
ColorRGBA331 = x3d.ColorRGBA()
ColorRGBA331.USE = "HAnimSegmentLineColorRGBA"

LineSet329.color = ColorRGBA331

Shape328.geometry = LineSet329

HAnimSegment324.children.append(Shape328)

HAnimJoint323.children.append(HAnimSegment324)
HAnimJoint332 = x3d.HAnimJoint()
HAnimJoint332.DEF = "hanim_vt11"
HAnimJoint332.name = "vt11"
HAnimJoint332.center = [0.0053,1.2679,-0.0810]
HAnimSegment333 = x3d.HAnimSegment()
HAnimSegment333.DEF = "hanim_t11"
HAnimSegment333.name = "t11"
Transform334 = x3d.Transform()
Transform334.translation = [0.0053,1.2679,-0.0810]
Transform335 = x3d.Transform()
""" Empty Transform """
Shape336 = x3d.Shape()
Shape336.USE = "HAnimJointShape"

Transform335.children.append(Shape336)

Transform334.children.append(Transform335)

HAnimSegment333.children.append(Transform334)
Shape337 = x3d.Shape()
LineSet338 = x3d.LineSet()
LineSet338.vertexCount = [2]
Coordinate339 = x3d.Coordinate()

LineSet338.coord = Coordinate339
""" from vt11 to vt10 vertices 2"""
ColorRGBA340 = x3d.ColorRGBA()
ColorRGBA340.USE = "HAnimSegmentLineColorRGBA"

LineSet338.color = ColorRGBA340

Shape337.geometry = LineSet338

HAnimSegment333.children.append(Shape337)
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.DEF = "hanim_substernale_pt"
HAnimSite341.name = "substernale_pt"
HAnimSite341.translation = [0.0085,1.2995,0.1147]
TouchSensor342 = x3d.TouchSensor()
TouchSensor342.description = "HAnimSite substernale_pt"

HAnimSite341.children.append(TouchSensor342)
Shape343 = x3d.Shape()
Shape343.USE = "HAnimSiteShape"

HAnimSite341.children.append(Shape343)

HAnimSegment333.children.append(HAnimSite341)

HAnimJoint332.children.append(HAnimSegment333)
HAnimJoint344 = x3d.HAnimJoint()
HAnimJoint344.DEF = "hanim_vt10"
HAnimJoint344.name = "vt10"
HAnimJoint344.center = [0.0056,1.2848,-0.0822]
HAnimSegment345 = x3d.HAnimSegment()
HAnimSegment345.DEF = "hanim_t10"
HAnimSegment345.name = "t10"
Transform346 = x3d.Transform()
Transform346.translation = [0.0056,1.2848,-0.0822]
Transform347 = x3d.Transform()
""" Empty Transform """
Shape348 = x3d.Shape()
Shape348.USE = "HAnimJointShape"

Transform347.children.append(Shape348)

Transform346.children.append(Transform347)

HAnimSegment345.children.append(Transform346)
Shape349 = x3d.Shape()
LineSet350 = x3d.LineSet()
LineSet350.vertexCount = [2]
Coordinate351 = x3d.Coordinate()

LineSet350.coord = Coordinate351
""" from vt10 to vt9 vertices 2"""
ColorRGBA352 = x3d.ColorRGBA()
ColorRGBA352.USE = "HAnimSegmentLineColorRGBA"

LineSet350.color = ColorRGBA352

Shape349.geometry = LineSet350

HAnimSegment345.children.append(Shape349)
HAnimSite353 = x3d.HAnimSite()
HAnimSite353.DEF = "hanim_l_thelion_pt"
HAnimSite353.name = "l_thelion_pt"
HAnimSite353.translation = [0.0918,1.3382,0.1192]
TouchSensor354 = x3d.TouchSensor()
TouchSensor354.description = "HAnimSite l_thelion_pt"

HAnimSite353.children.append(TouchSensor354)
Shape355 = x3d.Shape()
Shape355.USE = "HAnimSiteShape"

HAnimSite353.children.append(Shape355)

HAnimSegment345.children.append(HAnimSite353)
HAnimSite356 = x3d.HAnimSite()
HAnimSite356.DEF = "hanim_r_thelion_pt"
HAnimSite356.name = "r_thelion_pt"
HAnimSite356.translation = [-0.0736,1.3385,0.1217]
TouchSensor357 = x3d.TouchSensor()
TouchSensor357.description = "HAnimSite r_thelion_pt"

HAnimSite356.children.append(TouchSensor357)
Shape358 = x3d.Shape()
Shape358.USE = "HAnimSiteShape"

HAnimSite356.children.append(Shape358)

HAnimSegment345.children.append(HAnimSite356)

HAnimJoint344.children.append(HAnimSegment345)
HAnimJoint359 = x3d.HAnimJoint()
HAnimJoint359.DEF = "hanim_vt9"
HAnimJoint359.name = "vt9"
HAnimJoint359.center = [0.0057,1.3126,-0.0838]
HAnimSegment360 = x3d.HAnimSegment()
HAnimSegment360.DEF = "hanim_t9"
HAnimSegment360.name = "t9"
Transform361 = x3d.Transform()
Transform361.translation = [0.0057,1.3126,-0.0838]
Transform362 = x3d.Transform()
""" Empty Transform """
Shape363 = x3d.Shape()
Shape363.USE = "HAnimJointShape"

Transform362.children.append(Shape363)

Transform361.children.append(Transform362)

HAnimSegment360.children.append(Transform361)
Shape364 = x3d.Shape()
LineSet365 = x3d.LineSet()
LineSet365.vertexCount = [2]
Coordinate366 = x3d.Coordinate()

LineSet365.coord = Coordinate366
""" from vt9 to vt8 vertices 2"""
ColorRGBA367 = x3d.ColorRGBA()
ColorRGBA367.USE = "HAnimSegmentLineColorRGBA"

LineSet365.color = ColorRGBA367

Shape364.geometry = LineSet365

HAnimSegment360.children.append(Shape364)

HAnimJoint359.children.append(HAnimSegment360)
HAnimJoint368 = x3d.HAnimJoint()
HAnimJoint368.DEF = "hanim_vt8"
HAnimJoint368.name = "vt8"
HAnimJoint368.center = [0.0057,1.3382,-0.0845]
HAnimSegment369 = x3d.HAnimSegment()
HAnimSegment369.DEF = "hanim_t8"
HAnimSegment369.name = "t8"
Transform370 = x3d.Transform()
Transform370.translation = [0.0057,1.3382,-0.0845]
Transform371 = x3d.Transform()
""" Empty Transform """
Shape372 = x3d.Shape()
Shape372.USE = "HAnimJointShape"

Transform371.children.append(Shape372)

Transform370.children.append(Transform371)

HAnimSegment369.children.append(Transform370)
Shape373 = x3d.Shape()
LineSet374 = x3d.LineSet()
LineSet374.vertexCount = [2]
Coordinate375 = x3d.Coordinate()

LineSet374.coord = Coordinate375
""" from vt8 to vt7 vertices 2"""
ColorRGBA376 = x3d.ColorRGBA()
ColorRGBA376.USE = "HAnimSegmentLineColorRGBA"

LineSet374.color = ColorRGBA376

Shape373.geometry = LineSet374

HAnimSegment369.children.append(Shape373)

HAnimJoint368.children.append(HAnimSegment369)
HAnimJoint377 = x3d.HAnimJoint()
HAnimJoint377.DEF = "hanim_vt7"
HAnimJoint377.name = "vt7"
HAnimJoint377.center = [0.0058,1.3625,-0.0833]
HAnimSegment378 = x3d.HAnimSegment()
HAnimSegment378.DEF = "hanim_t7"
HAnimSegment378.name = "t7"
Transform379 = x3d.Transform()
Transform379.translation = [0.0058,1.3625,-0.0833]
Transform380 = x3d.Transform()
""" Empty Transform """
Shape381 = x3d.Shape()
Shape381.USE = "HAnimJointShape"

Transform380.children.append(Shape381)

Transform379.children.append(Transform380)

HAnimSegment378.children.append(Transform379)
Shape382 = x3d.Shape()
LineSet383 = x3d.LineSet()
LineSet383.vertexCount = [2]
Coordinate384 = x3d.Coordinate()

LineSet383.coord = Coordinate384
""" from vt7 to vt6 vertices 2"""
ColorRGBA385 = x3d.ColorRGBA()
ColorRGBA385.USE = "HAnimSegmentLineColorRGBA"

LineSet383.color = ColorRGBA385

Shape382.geometry = LineSet383

HAnimSegment378.children.append(Shape382)
HAnimSite386 = x3d.HAnimSite()
HAnimSite386.DEF = "hanim_l_chest_midsagittal_plane_pt"
HAnimSite386.name = "l_chest_midsagittal_plane_pt"
TouchSensor387 = x3d.TouchSensor()
TouchSensor387.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite386.children.append(TouchSensor387)
Shape388 = x3d.Shape()
Shape388.USE = "HAnimSiteShape"

HAnimSite386.children.append(Shape388)

HAnimSegment378.children.append(HAnimSite386)
HAnimSite389 = x3d.HAnimSite()
HAnimSite389.DEF = "hanim_mesosternale_pt"
HAnimSite389.name = "mesosternale_pt"
TouchSensor390 = x3d.TouchSensor()
TouchSensor390.description = "HAnimSite mesosternale_pt"

HAnimSite389.children.append(TouchSensor390)
Shape391 = x3d.Shape()
Shape391.USE = "HAnimSiteShape"

HAnimSite389.children.append(Shape391)

HAnimSegment378.children.append(HAnimSite389)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.DEF = "hanim_r_chest_midsagittal_plane_pt"
HAnimSite392.name = "r_chest_midsagittal_plane_pt"
TouchSensor393 = x3d.TouchSensor()
TouchSensor393.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite392.children.append(TouchSensor393)
Shape394 = x3d.Shape()
Shape394.USE = "HAnimSiteShape"

HAnimSite392.children.append(Shape394)

HAnimSegment378.children.append(HAnimSite392)
HAnimSite395 = x3d.HAnimSite()
HAnimSite395.DEF = "hanim_rear_center_midsagittal_plane_pt"
HAnimSite395.name = "rear_center_midsagittal_plane_pt"
TouchSensor396 = x3d.TouchSensor()
TouchSensor396.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite395.children.append(TouchSensor396)
Shape397 = x3d.Shape()
Shape397.USE = "HAnimSiteShape"

HAnimSite395.children.append(Shape397)

HAnimSegment378.children.append(HAnimSite395)

HAnimJoint377.children.append(HAnimSegment378)
HAnimJoint398 = x3d.HAnimJoint()
HAnimJoint398.DEF = "hanim_vt6"
HAnimJoint398.name = "vt6"
HAnimJoint398.center = [0.0059,1.3866,-0.0800]
HAnimSegment399 = x3d.HAnimSegment()
HAnimSegment399.DEF = "hanim_t6"
HAnimSegment399.name = "t6"
Transform400 = x3d.Transform()
Transform400.translation = [0.0059,1.3866,-0.0800]
Transform401 = x3d.Transform()
""" Empty Transform """
Shape402 = x3d.Shape()
Shape402.USE = "HAnimJointShape"

Transform401.children.append(Shape402)

Transform400.children.append(Transform401)

HAnimSegment399.children.append(Transform400)
Shape403 = x3d.Shape()
LineSet404 = x3d.LineSet()
LineSet404.vertexCount = [2]
Coordinate405 = x3d.Coordinate()

LineSet404.coord = Coordinate405
""" from vt6 to vt5 vertices 2"""
ColorRGBA406 = x3d.ColorRGBA()
ColorRGBA406.USE = "HAnimSegmentLineColorRGBA"

LineSet404.color = ColorRGBA406

Shape403.geometry = LineSet404

HAnimSegment399.children.append(Shape403)
HAnimSite407 = x3d.HAnimSite()
HAnimSite407.DEF = "hanim_spine_1_middle_back_pt"
HAnimSite407.name = "spine_1_middle_back_pt"
TouchSensor408 = x3d.TouchSensor()
TouchSensor408.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite407.children.append(TouchSensor408)
Shape409 = x3d.Shape()
Shape409.USE = "HAnimSiteShape"

HAnimSite407.children.append(Shape409)

HAnimSegment399.children.append(HAnimSite407)

HAnimJoint398.children.append(HAnimSegment399)
HAnimJoint410 = x3d.HAnimJoint()
HAnimJoint410.DEF = "hanim_vt5"
HAnimJoint410.name = "vt5"
HAnimJoint410.center = [0.0060,1.4102,-0.0745]
HAnimSegment411 = x3d.HAnimSegment()
HAnimSegment411.DEF = "hanim_t5"
HAnimSegment411.name = "t5"
Transform412 = x3d.Transform()
Transform412.translation = [0.0060,1.4102,-0.0745]
Transform413 = x3d.Transform()
""" Empty Transform """
Shape414 = x3d.Shape()
Shape414.USE = "HAnimJointShape"

Transform413.children.append(Shape414)

Transform412.children.append(Transform413)

HAnimSegment411.children.append(Transform412)
Shape415 = x3d.Shape()
LineSet416 = x3d.LineSet()
LineSet416.vertexCount = [2]
Coordinate417 = x3d.Coordinate()

LineSet416.coord = Coordinate417
""" from vt5 to vt4 vertices 2"""
ColorRGBA418 = x3d.ColorRGBA()
ColorRGBA418.USE = "HAnimSegmentLineColorRGBA"

LineSet416.color = ColorRGBA418

Shape415.geometry = LineSet416

HAnimSegment411.children.append(Shape415)

HAnimJoint410.children.append(HAnimSegment411)
HAnimJoint419 = x3d.HAnimJoint()
HAnimJoint419.DEF = "hanim_vt4"
HAnimJoint419.name = "vt4"
HAnimJoint419.center = [0.0061,1.4320,-0.0675]
HAnimSegment420 = x3d.HAnimSegment()
HAnimSegment420.DEF = "hanim_t4"
HAnimSegment420.name = "t4"
Transform421 = x3d.Transform()
Transform421.translation = [0.0061,1.4320,-0.0675]
Transform422 = x3d.Transform()
""" Empty Transform """
Shape423 = x3d.Shape()
Shape423.USE = "HAnimJointShape"

Transform422.children.append(Shape423)

Transform421.children.append(Transform422)

HAnimSegment420.children.append(Transform421)
Shape424 = x3d.Shape()
LineSet425 = x3d.LineSet()
LineSet425.vertexCount = [2]
Coordinate426 = x3d.Coordinate()

LineSet425.coord = Coordinate426
""" from vt4 to vt3 vertices 2"""
ColorRGBA427 = x3d.ColorRGBA()
ColorRGBA427.USE = "HAnimSegmentLineColorRGBA"

LineSet425.color = ColorRGBA427

Shape424.geometry = LineSet425

HAnimSegment420.children.append(Shape424)

HAnimJoint419.children.append(HAnimSegment420)
HAnimJoint428 = x3d.HAnimJoint()
HAnimJoint428.DEF = "hanim_vt3"
HAnimJoint428.name = "vt3"
HAnimJoint428.center = [0.0062,1.4583,-0.0570]
HAnimSegment429 = x3d.HAnimSegment()
HAnimSegment429.DEF = "hanim_t3"
HAnimSegment429.name = "t3"
Transform430 = x3d.Transform()
Transform430.translation = [0.0062,1.4583,-0.0570]
Transform431 = x3d.Transform()
""" Empty Transform """
Shape432 = x3d.Shape()
Shape432.USE = "HAnimJointShape"

Transform431.children.append(Shape432)

Transform430.children.append(Transform431)

HAnimSegment429.children.append(Transform430)
Shape433 = x3d.Shape()
LineSet434 = x3d.LineSet()
LineSet434.vertexCount = [2]
Coordinate435 = x3d.Coordinate()

LineSet434.coord = Coordinate435
""" from vt3 to vt2 vertices 2"""
ColorRGBA436 = x3d.ColorRGBA()
ColorRGBA436.USE = "HAnimSegmentLineColorRGBA"

LineSet434.color = ColorRGBA436

Shape433.geometry = LineSet434

HAnimSegment429.children.append(Shape433)

HAnimJoint428.children.append(HAnimSegment429)
HAnimJoint437 = x3d.HAnimJoint()
HAnimJoint437.DEF = "hanim_vt2"
HAnimJoint437.name = "vt2"
HAnimJoint437.center = [0.0063,1.4761,-0.0484]
HAnimSegment438 = x3d.HAnimSegment()
HAnimSegment438.DEF = "hanim_t2"
HAnimSegment438.name = "t2"
Transform439 = x3d.Transform()
Transform439.translation = [0.0063,1.4761,-0.0484]
Transform440 = x3d.Transform()
""" Empty Transform """
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
""" from vt2 to vt1 vertices 2"""
ColorRGBA445 = x3d.ColorRGBA()
ColorRGBA445.USE = "HAnimSegmentLineColorRGBA"

LineSet443.color = ColorRGBA445

Shape442.geometry = LineSet443

HAnimSegment438.children.append(Shape442)
HAnimSite446 = x3d.HAnimSite()
HAnimSite446.DEF = "hanim_cervicale_pt"
HAnimSite446.name = "cervicale_pt"
HAnimSite446.translation = [0.0064,1.520,-0.0815]
TouchSensor447 = x3d.TouchSensor()
TouchSensor447.description = "HAnimSite cervicale_pt"

HAnimSite446.children.append(TouchSensor447)
Shape448 = x3d.Shape()
Shape448.USE = "HAnimSiteShape"

HAnimSite446.children.append(Shape448)

HAnimSegment438.children.append(HAnimSite446)
HAnimSite449 = x3d.HAnimSite()
HAnimSite449.DEF = "hanim_suprasternale_pt"
HAnimSite449.name = "suprasternale_pt"
HAnimSite449.translation = [0.0084,1.4714,0.0551]
TouchSensor450 = x3d.TouchSensor()
TouchSensor450.description = "HAnimSite suprasternale_pt"

HAnimSite449.children.append(TouchSensor450)
Shape451 = x3d.Shape()
Shape451.USE = "HAnimSiteShape"

HAnimSite449.children.append(Shape451)

HAnimSegment438.children.append(HAnimSite449)

HAnimJoint437.children.append(HAnimSegment438)
HAnimJoint452 = x3d.HAnimJoint()
HAnimJoint452.DEF = "hanim_vt1"
HAnimJoint452.name = "vt1"
HAnimJoint452.center = [0.0065,1.4951,-0.0387]
HAnimSegment453 = x3d.HAnimSegment()
HAnimSegment453.DEF = "hanim_t1"
HAnimSegment453.name = "t1"
Transform454 = x3d.Transform()
Transform454.translation = [0.0065,1.4951,-0.0387]
Transform455 = x3d.Transform()
""" Empty Transform """
Shape456 = x3d.Shape()
Shape456.USE = "HAnimJointShape"

Transform455.children.append(Shape456)

Transform454.children.append(Transform455)

HAnimSegment453.children.append(Transform454)
Shape457 = x3d.Shape()
LineSet458 = x3d.LineSet()
LineSet458.vertexCount = [2]
Coordinate459 = x3d.Coordinate()

LineSet458.coord = Coordinate459
""" from vt1 to vc7 vertices 2"""
ColorRGBA460 = x3d.ColorRGBA()
ColorRGBA460.USE = "HAnimSegmentLineColorRGBA"

LineSet458.color = ColorRGBA460

Shape457.geometry = LineSet458

HAnimSegment453.children.append(Shape457)
HAnimSite461 = x3d.HAnimSite()
HAnimSite461.DEF = "hanim_l_neck_base_pt"
HAnimSite461.name = "l_neck_base_pt"
HAnimSite461.translation = [0.0646,1.5141,-0.0380]
TouchSensor462 = x3d.TouchSensor()
TouchSensor462.description = "HAnimSite l_neck_base_pt"

HAnimSite461.children.append(TouchSensor462)
Shape463 = x3d.Shape()
Shape463.USE = "HAnimSiteShape"

HAnimSite461.children.append(Shape463)

HAnimSegment453.children.append(HAnimSite461)
HAnimSite464 = x3d.HAnimSite()
HAnimSite464.DEF = "hanim_r_neck_base_pt"
HAnimSite464.name = "r_neck_base_pt"
HAnimSite464.translation = [-0.0419,1.5149,-0.0220]
TouchSensor465 = x3d.TouchSensor()
TouchSensor465.description = "HAnimSite r_neck_base_pt"

HAnimSite464.children.append(TouchSensor465)
Shape466 = x3d.Shape()
Shape466.USE = "HAnimSiteShape"

HAnimSite464.children.append(Shape466)

HAnimSegment453.children.append(HAnimSite464)
Shape467 = x3d.Shape()
LineSet468 = x3d.LineSet()
LineSet468.vertexCount = [2]
Coordinate469 = x3d.Coordinate()

LineSet468.coord = Coordinate469
""" from vt1 to l_sternoclavicular vertices 2"""
ColorRGBA470 = x3d.ColorRGBA()
ColorRGBA470.USE = "HAnimSegmentLineColorRGBA"

LineSet468.color = ColorRGBA470

Shape467.geometry = LineSet468

HAnimSegment453.children.append(Shape467)
HAnimSite471 = x3d.HAnimSite()
HAnimSite471.DEF = "hanim_l_acromion_pt"
HAnimSite471.name = "l_acromion_pt"
HAnimSite471.translation = [0.2032,1.4760,-0.0490]
TouchSensor472 = x3d.TouchSensor()
TouchSensor472.description = "HAnimSite l_acromion_pt"

HAnimSite471.children.append(TouchSensor472)
Shape473 = x3d.Shape()
Shape473.USE = "HAnimSiteShape"

HAnimSite471.children.append(Shape473)

HAnimSegment453.children.append(HAnimSite471)
HAnimSite474 = x3d.HAnimSite()
HAnimSite474.DEF = "hanim_l_axilla_distal_pt"
HAnimSite474.name = "l_axilla_distal_pt"
HAnimSite474.translation = [0.1706,1.4072,-0.0875]
TouchSensor475 = x3d.TouchSensor()
TouchSensor475.description = "HAnimSite l_axilla_distal_pt"

HAnimSite474.children.append(TouchSensor475)
Shape476 = x3d.Shape()
Shape476.USE = "HAnimSiteShape"

HAnimSite474.children.append(Shape476)

HAnimSegment453.children.append(HAnimSite474)
HAnimSite477 = x3d.HAnimSite()
HAnimSite477.DEF = "hanim_l_axilla_posterior_folds_pt"
HAnimSite477.name = "l_axilla_posterior_folds_pt"
TouchSensor478 = x3d.TouchSensor()
TouchSensor478.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite477.children.append(TouchSensor478)
Shape479 = x3d.Shape()
Shape479.USE = "HAnimSiteShape"

HAnimSite477.children.append(Shape479)

HAnimSegment453.children.append(HAnimSite477)
HAnimSite480 = x3d.HAnimSite()
HAnimSite480.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite480.name = "l_axilla_proximal_pt"
HAnimSite480.translation = [0.1777,1.4065,-0.0075]
TouchSensor481 = x3d.TouchSensor()
TouchSensor481.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite480.children.append(TouchSensor481)
Shape482 = x3d.Shape()
Shape482.USE = "HAnimSiteShape"

HAnimSite480.children.append(Shape482)

HAnimSegment453.children.append(HAnimSite480)
HAnimSite483 = x3d.HAnimSite()
HAnimSite483.DEF = "hanim_l_clavicale_pt"
HAnimSite483.name = "l_clavicale_pt"
HAnimSite483.translation = [0.0271,1.4943,0.0394]
TouchSensor484 = x3d.TouchSensor()
TouchSensor484.description = "HAnimSite l_clavicale_pt"

HAnimSite483.children.append(TouchSensor484)
Shape485 = x3d.Shape()
Shape485.USE = "HAnimSiteShape"

HAnimSite483.children.append(Shape485)

HAnimSegment453.children.append(HAnimSite483)
Shape486 = x3d.Shape()
LineSet487 = x3d.LineSet()
LineSet487.vertexCount = [2]
Coordinate488 = x3d.Coordinate()

LineSet487.coord = Coordinate488
""" from vt1 to r_sternoclavicular vertices 2"""
ColorRGBA489 = x3d.ColorRGBA()
ColorRGBA489.USE = "HAnimSegmentLineColorRGBA"

LineSet487.color = ColorRGBA489

Shape486.geometry = LineSet487

HAnimSegment453.children.append(Shape486)
HAnimSite490 = x3d.HAnimSite()
HAnimSite490.DEF = "hanim_r_acromion_pt"
HAnimSite490.name = "r_acromion_pt"
HAnimSite490.translation = [-0.1905,1.4791,-0.0431]
TouchSensor491 = x3d.TouchSensor()
TouchSensor491.description = "HAnimSite r_acromion_pt"

HAnimSite490.children.append(TouchSensor491)
Shape492 = x3d.Shape()
Shape492.USE = "HAnimSiteShape"

HAnimSite490.children.append(Shape492)

HAnimSegment453.children.append(HAnimSite490)
HAnimSite493 = x3d.HAnimSite()
HAnimSite493.DEF = "hanim_r_axilla_distal_pt"
HAnimSite493.name = "r_axilla_distal_pt"
HAnimSite493.translation = [-0.1603,1.4098,-0.0826]
TouchSensor494 = x3d.TouchSensor()
TouchSensor494.description = "HAnimSite r_axilla_distal_pt"

HAnimSite493.children.append(TouchSensor494)
Shape495 = x3d.Shape()
Shape495.USE = "HAnimSiteShape"

HAnimSite493.children.append(Shape495)

HAnimSegment453.children.append(HAnimSite493)
HAnimSite496 = x3d.HAnimSite()
HAnimSite496.DEF = "hanim_r_axilla_posterior_folds_pt"
HAnimSite496.name = "r_axilla_posterior_folds_pt"
TouchSensor497 = x3d.TouchSensor()
TouchSensor497.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite496.children.append(TouchSensor497)
Shape498 = x3d.Shape()
Shape498.USE = "HAnimSiteShape"

HAnimSite496.children.append(Shape498)

HAnimSegment453.children.append(HAnimSite496)
HAnimSite499 = x3d.HAnimSite()
HAnimSite499.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite499.name = "r_axilla_proximal_pt"
HAnimSite499.translation = [-0.1626,1.4072,-0.0031]
TouchSensor500 = x3d.TouchSensor()
TouchSensor500.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite499.children.append(TouchSensor500)
Shape501 = x3d.Shape()
Shape501.USE = "HAnimSiteShape"

HAnimSite499.children.append(Shape501)

HAnimSegment453.children.append(HAnimSite499)
HAnimSite502 = x3d.HAnimSite()
HAnimSite502.DEF = "hanim_r_clavicale_pt"
HAnimSite502.name = "r_clavicale_pt"
HAnimSite502.translation = [-0.0115,1.4943,0.0400]
TouchSensor503 = x3d.TouchSensor()
TouchSensor503.description = "HAnimSite r_clavicale_pt"

HAnimSite502.children.append(TouchSensor503)
Shape504 = x3d.Shape()
Shape504.USE = "HAnimSiteShape"

HAnimSite502.children.append(Shape504)

HAnimSegment453.children.append(HAnimSite502)

HAnimJoint452.children.append(HAnimSegment453)
HAnimJoint505 = x3d.HAnimJoint()
HAnimJoint505.DEF = "hanim_vc7"
HAnimJoint505.name = "vc7"
HAnimJoint505.center = [0.0066,1.5132,-0.0301]
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.DEF = "hanim_c7"
HAnimSegment506.name = "c7"
Transform507 = x3d.Transform()
Transform507.translation = [0.0066,1.5132,-0.0301]
Transform508 = x3d.Transform()
""" Empty Transform """
Shape509 = x3d.Shape()
Shape509.USE = "HAnimJointShape"

Transform508.children.append(Shape509)

Transform507.children.append(Transform508)

HAnimSegment506.children.append(Transform507)
Shape510 = x3d.Shape()
LineSet511 = x3d.LineSet()
LineSet511.vertexCount = [2]
Coordinate512 = x3d.Coordinate()

LineSet511.coord = Coordinate512
""" from vc7 to vc6 vertices 2"""
ColorRGBA513 = x3d.ColorRGBA()
ColorRGBA513.USE = "HAnimSegmentLineColorRGBA"

LineSet511.color = ColorRGBA513

Shape510.geometry = LineSet511

HAnimSegment506.children.append(Shape510)

HAnimJoint505.children.append(HAnimSegment506)
HAnimJoint514 = x3d.HAnimJoint()
HAnimJoint514.DEF = "hanim_vc6"
HAnimJoint514.name = "vc6"
HAnimJoint514.center = [0.0066,1.5357,-0.0143]
HAnimSegment515 = x3d.HAnimSegment()
HAnimSegment515.DEF = "hanim_c6"
HAnimSegment515.name = "c6"
Transform516 = x3d.Transform()
Transform516.translation = [0.0066,1.5357,-0.0143]
Transform517 = x3d.Transform()
""" Empty Transform """
Shape518 = x3d.Shape()
Shape518.USE = "HAnimJointShape"

Transform517.children.append(Shape518)

Transform516.children.append(Transform517)

HAnimSegment515.children.append(Transform516)
Shape519 = x3d.Shape()
LineSet520 = x3d.LineSet()
LineSet520.vertexCount = [2]
Coordinate521 = x3d.Coordinate()

LineSet520.coord = Coordinate521
""" from vc6 to vc5 vertices 2"""
ColorRGBA522 = x3d.ColorRGBA()
ColorRGBA522.USE = "HAnimSegmentLineColorRGBA"

LineSet520.color = ColorRGBA522

Shape519.geometry = LineSet520

HAnimSegment515.children.append(Shape519)

HAnimJoint514.children.append(HAnimSegment515)
HAnimJoint523 = x3d.HAnimJoint()
HAnimJoint523.DEF = "hanim_vc5"
HAnimJoint523.name = "vc5"
HAnimJoint523.center = [0.0066,1.5520,-0.0082]
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.DEF = "hanim_c5"
HAnimSegment524.name = "c5"
Transform525 = x3d.Transform()
Transform525.translation = [0.0066,1.5520,-0.0082]
Transform526 = x3d.Transform()
""" Empty Transform """
Shape527 = x3d.Shape()
Shape527.USE = "HAnimJointShape"

Transform526.children.append(Shape527)

Transform525.children.append(Transform526)

HAnimSegment524.children.append(Transform525)
Shape528 = x3d.Shape()
LineSet529 = x3d.LineSet()
LineSet529.vertexCount = [2]
Coordinate530 = x3d.Coordinate()

LineSet529.coord = Coordinate530
""" from vc5 to vc4 vertices 2"""
ColorRGBA531 = x3d.ColorRGBA()
ColorRGBA531.USE = "HAnimSegmentLineColorRGBA"

LineSet529.color = ColorRGBA531

Shape528.geometry = LineSet529

HAnimSegment524.children.append(Shape528)

HAnimJoint523.children.append(HAnimSegment524)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.DEF = "hanim_vc4"
HAnimJoint532.name = "vc4"
HAnimJoint532.center = [0.0066,1.5662,-0.0084]
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.DEF = "hanim_c4"
HAnimSegment533.name = "c4"
Transform534 = x3d.Transform()
Transform534.translation = [0.0066,1.5662,-0.0084]
Transform535 = x3d.Transform()
""" Empty Transform """
Shape536 = x3d.Shape()
Shape536.USE = "HAnimJointShape"

Transform535.children.append(Shape536)

Transform534.children.append(Transform535)

HAnimSegment533.children.append(Transform534)
Shape537 = x3d.Shape()
LineSet538 = x3d.LineSet()
LineSet538.vertexCount = [2]
Coordinate539 = x3d.Coordinate()

LineSet538.coord = Coordinate539
""" from vc4 to vc3 vertices 2"""
ColorRGBA540 = x3d.ColorRGBA()
ColorRGBA540.USE = "HAnimSegmentLineColorRGBA"

LineSet538.color = ColorRGBA540

Shape537.geometry = LineSet538

HAnimSegment533.children.append(Shape537)

HAnimJoint532.children.append(HAnimSegment533)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.DEF = "hanim_vc3"
HAnimJoint541.name = "vc3"
HAnimJoint541.center = [0.0066,1.5800,-0.0103]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.DEF = "hanim_c3"
HAnimSegment542.name = "c3"
Transform543 = x3d.Transform()
Transform543.translation = [0.0066,1.5800,-0.0103]
Transform544 = x3d.Transform()
""" Empty Transform """
Shape545 = x3d.Shape()
Shape545.USE = "HAnimJointShape"

Transform544.children.append(Shape545)

Transform543.children.append(Transform544)

HAnimSegment542.children.append(Transform543)
Shape546 = x3d.Shape()
LineSet547 = x3d.LineSet()
LineSet547.vertexCount = [2]
Coordinate548 = x3d.Coordinate()

LineSet547.coord = Coordinate548
""" from vc3 to vc2 vertices 2"""
ColorRGBA549 = x3d.ColorRGBA()
ColorRGBA549.USE = "HAnimSegmentLineColorRGBA"

LineSet547.color = ColorRGBA549

Shape546.geometry = LineSet547

HAnimSegment542.children.append(Shape546)
HAnimSite550 = x3d.HAnimSite()
HAnimSite550.DEF = "hanim_adams_apple_pt"
HAnimSite550.name = "adams_apple_pt"
TouchSensor551 = x3d.TouchSensor()
TouchSensor551.description = "HAnimSite adams_apple_pt"

HAnimSite550.children.append(TouchSensor551)
Shape552 = x3d.Shape()
Shape552.USE = "HAnimSiteShape"

HAnimSite550.children.append(Shape552)

HAnimSegment542.children.append(HAnimSite550)

HAnimJoint541.children.append(HAnimSegment542)
HAnimJoint553 = x3d.HAnimJoint()
HAnimJoint553.DEF = "hanim_vc2"
HAnimJoint553.name = "vc2"
HAnimJoint553.center = [0.0066,1.5928,-0.0103]
HAnimSegment554 = x3d.HAnimSegment()
HAnimSegment554.DEF = "hanim_c2"
HAnimSegment554.name = "c2"
Transform555 = x3d.Transform()
Transform555.translation = [0.0066,1.5928,-0.0103]
Transform556 = x3d.Transform()
""" Empty Transform """
Shape557 = x3d.Shape()
Shape557.USE = "HAnimJointShape"

Transform556.children.append(Shape557)

Transform555.children.append(Transform556)

HAnimSegment554.children.append(Transform555)
Shape558 = x3d.Shape()
LineSet559 = x3d.LineSet()
LineSet559.vertexCount = [2]
Coordinate560 = x3d.Coordinate()

LineSet559.coord = Coordinate560
""" from vc2 to vc1 vertices 2"""
ColorRGBA561 = x3d.ColorRGBA()
ColorRGBA561.USE = "HAnimSegmentLineColorRGBA"

LineSet559.color = ColorRGBA561

Shape558.geometry = LineSet559

HAnimSegment554.children.append(Shape558)

HAnimJoint553.children.append(HAnimSegment554)
HAnimJoint562 = x3d.HAnimJoint()
HAnimJoint562.DEF = "hanim_vc1"
HAnimJoint562.name = "vc1"
HAnimJoint562.center = [0.0066,1.6144,-0.0034]
HAnimSegment563 = x3d.HAnimSegment()
HAnimSegment563.DEF = "hanim_c1"
HAnimSegment563.name = "c1"
Transform564 = x3d.Transform()
Transform564.translation = [0.0066,1.6144,-0.0034]
Transform565 = x3d.Transform()
""" Empty Transform """
Shape566 = x3d.Shape()
Shape566.USE = "HAnimJointShape"

Transform565.children.append(Shape566)

Transform564.children.append(Transform565)

HAnimSegment563.children.append(Transform564)
Shape567 = x3d.Shape()
LineSet568 = x3d.LineSet()
LineSet568.vertexCount = [2]
Coordinate569 = x3d.Coordinate()

LineSet568.coord = Coordinate569
""" from vc1 to skullbase vertices 2"""
ColorRGBA570 = x3d.ColorRGBA()
ColorRGBA570.USE = "HAnimSegmentLineColorRGBA"

LineSet568.color = ColorRGBA570

Shape567.geometry = LineSet568

HAnimSegment563.children.append(Shape567)
HAnimSite571 = x3d.HAnimSite()
HAnimSite571.DEF = "hanim_glabella_pt"
HAnimSite571.name = "glabella_pt"
TouchSensor572 = x3d.TouchSensor()
TouchSensor572.description = "HAnimSite glabella_pt"

HAnimSite571.children.append(TouchSensor572)
Shape573 = x3d.Shape()
Shape573.USE = "HAnimSiteShape"

HAnimSite571.children.append(Shape573)

HAnimSegment563.children.append(HAnimSite571)
HAnimSite574 = x3d.HAnimSite()
HAnimSite574.DEF = "hanim_l_ectocanthus_pt"
HAnimSite574.name = "l_ectocanthus_pt"
TouchSensor575 = x3d.TouchSensor()
TouchSensor575.description = "HAnimSite l_ectocanthus_pt"

HAnimSite574.children.append(TouchSensor575)
Shape576 = x3d.Shape()
Shape576.USE = "HAnimSiteShape"

HAnimSite574.children.append(Shape576)

HAnimSegment563.children.append(HAnimSite574)
HAnimSite577 = x3d.HAnimSite()
HAnimSite577.DEF = "hanim_l_infraorbitale_pt"
HAnimSite577.name = "l_infraorbitale_pt"
HAnimSite577.translation = [0.0341,1.6171,0.0752]
TouchSensor578 = x3d.TouchSensor()
TouchSensor578.description = "HAnimSite l_infraorbitale_pt"

HAnimSite577.children.append(TouchSensor578)
Shape579 = x3d.Shape()
Shape579.USE = "HAnimSiteShape"

HAnimSite577.children.append(Shape579)

HAnimSegment563.children.append(HAnimSite577)
HAnimSite580 = x3d.HAnimSite()
HAnimSite580.DEF = "hanim_l_tragion_pt"
HAnimSite580.name = "l_tragion_pt"
HAnimSite580.translation = [0.0739,1.6348,0.0282]
TouchSensor581 = x3d.TouchSensor()
TouchSensor581.description = "HAnimSite l_tragion_pt"

HAnimSite580.children.append(TouchSensor581)
Shape582 = x3d.Shape()
Shape582.USE = "HAnimSiteShape"

HAnimSite580.children.append(Shape582)

HAnimSegment563.children.append(HAnimSite580)
HAnimSite583 = x3d.HAnimSite()
HAnimSite583.DEF = "hanim_nuchale_pt"
HAnimSite583.name = "nuchale_pt"
HAnimSite583.translation = [0.0039,1.5972,-0.0796]
TouchSensor584 = x3d.TouchSensor()
TouchSensor584.description = "HAnimSite nuchale_pt"

HAnimSite583.children.append(TouchSensor584)
Shape585 = x3d.Shape()
Shape585.USE = "HAnimSiteShape"

HAnimSite583.children.append(Shape585)

HAnimSegment563.children.append(HAnimSite583)
HAnimSite586 = x3d.HAnimSite()
HAnimSite586.DEF = "hanim_opisthocranion_pt"
HAnimSite586.name = "opisthocranion_pt"
TouchSensor587 = x3d.TouchSensor()
TouchSensor587.description = "HAnimSite opisthocranion_pt"

HAnimSite586.children.append(TouchSensor587)
Shape588 = x3d.Shape()
Shape588.USE = "HAnimSiteShape"

HAnimSite586.children.append(Shape588)

HAnimSegment563.children.append(HAnimSite586)
HAnimSite589 = x3d.HAnimSite()
HAnimSite589.DEF = "hanim_r_ectocanthus_pt"
HAnimSite589.name = "r_ectocanthus_pt"
TouchSensor590 = x3d.TouchSensor()
TouchSensor590.description = "HAnimSite r_ectocanthus_pt"

HAnimSite589.children.append(TouchSensor590)
Shape591 = x3d.Shape()
Shape591.USE = "HAnimSiteShape"

HAnimSite589.children.append(Shape591)

HAnimSegment563.children.append(HAnimSite589)
HAnimSite592 = x3d.HAnimSite()
HAnimSite592.DEF = "hanim_r_infraorbitale_pt"
HAnimSite592.name = "r_infraorbitale_pt"
HAnimSite592.translation = [-0.0237,1.6171,0.0752]
TouchSensor593 = x3d.TouchSensor()
TouchSensor593.description = "HAnimSite r_infraorbitale_pt"

HAnimSite592.children.append(TouchSensor593)
Shape594 = x3d.Shape()
Shape594.USE = "HAnimSiteShape"

HAnimSite592.children.append(Shape594)

HAnimSegment563.children.append(HAnimSite592)
HAnimSite595 = x3d.HAnimSite()
HAnimSite595.DEF = "hanim_r_tragion_pt"
HAnimSite595.name = "r_tragion_pt"
HAnimSite595.translation = [-0.0646,1.6347,0.0302]
TouchSensor596 = x3d.TouchSensor()
TouchSensor596.description = "HAnimSite r_tragion_pt"

HAnimSite595.children.append(TouchSensor596)
Shape597 = x3d.Shape()
Shape597.USE = "HAnimSiteShape"

HAnimSite595.children.append(Shape597)

HAnimSegment563.children.append(HAnimSite595)
HAnimSite598 = x3d.HAnimSite()
HAnimSite598.DEF = "hanim_sellion_pt"
HAnimSite598.name = "sellion_pt"
HAnimSite598.translation = [0.0058,1.6316,0.0852]
TouchSensor599 = x3d.TouchSensor()
TouchSensor599.description = "HAnimSite sellion_pt"

HAnimSite598.children.append(TouchSensor599)
Shape600 = x3d.Shape()
Shape600.USE = "HAnimSiteShape"

HAnimSite598.children.append(Shape600)

HAnimSegment563.children.append(HAnimSite598)
HAnimSite601 = x3d.HAnimSite()
HAnimSite601.DEF = "hanim_skull_vertex_pt"
HAnimSite601.name = "skull_vertex_pt"
HAnimSite601.translation = [0.0050,1.7504,0.0055]
TouchSensor602 = x3d.TouchSensor()
TouchSensor602.description = "HAnimSite skull_vertex_pt"

HAnimSite601.children.append(TouchSensor602)
Shape603 = x3d.Shape()
Shape603.USE = "HAnimSiteShape"

HAnimSite601.children.append(Shape603)

HAnimSegment563.children.append(HAnimSite601)

HAnimJoint562.children.append(HAnimSegment563)
HAnimJoint604 = x3d.HAnimJoint()
HAnimJoint604.DEF = "hanim_skullbase"
HAnimJoint604.name = "skullbase"
HAnimJoint604.center = [0.0044,1.6209,0.0236]
HAnimSegment605 = x3d.HAnimSegment()
HAnimSegment605.DEF = "hanim_skull"
HAnimSegment605.name = "skull"
Transform606 = x3d.Transform()
Transform606.translation = [0.0044,1.6209,0.0236]
Transform607 = x3d.Transform()
""" Empty Transform """
Shape608 = x3d.Shape()
Shape608.USE = "HAnimJointShape"

Transform607.children.append(Shape608)

Transform606.children.append(Transform607)

HAnimSegment605.children.append(Transform606)
Shape609 = x3d.Shape()
LineSet610 = x3d.LineSet()
LineSet610.vertexCount = [2]
Coordinate611 = x3d.Coordinate()

LineSet610.coord = Coordinate611
""" from skullbase to l_eyelid_joint vertices 2"""
ColorRGBA612 = x3d.ColorRGBA()
ColorRGBA612.USE = "HAnimSegmentLineColorRGBA"

LineSet610.color = ColorRGBA612

Shape609.geometry = LineSet610

HAnimSegment605.children.append(Shape609)
Shape613 = x3d.Shape()
LineSet614 = x3d.LineSet()
LineSet614.vertexCount = [2]
Coordinate615 = x3d.Coordinate()

LineSet614.coord = Coordinate615
""" from skullbase to r_eyelid_joint vertices 2"""
ColorRGBA616 = x3d.ColorRGBA()
ColorRGBA616.USE = "HAnimSegmentLineColorRGBA"

LineSet614.color = ColorRGBA616

Shape613.geometry = LineSet614

HAnimSegment605.children.append(Shape613)
Shape617 = x3d.Shape()
LineSet618 = x3d.LineSet()
LineSet618.vertexCount = [2]
Coordinate619 = x3d.Coordinate()

LineSet618.coord = Coordinate619
""" from skullbase to l_eyeball_joint vertices 2"""
ColorRGBA620 = x3d.ColorRGBA()
ColorRGBA620.USE = "HAnimSegmentLineColorRGBA"

LineSet618.color = ColorRGBA620

Shape617.geometry = LineSet618

HAnimSegment605.children.append(Shape617)
Shape621 = x3d.Shape()
LineSet622 = x3d.LineSet()
LineSet622.vertexCount = [2]
Coordinate623 = x3d.Coordinate()

LineSet622.coord = Coordinate623
""" from skullbase to r_eyeball_joint vertices 2"""
ColorRGBA624 = x3d.ColorRGBA()
ColorRGBA624.USE = "HAnimSegmentLineColorRGBA"

LineSet622.color = ColorRGBA624

Shape621.geometry = LineSet622

HAnimSegment605.children.append(Shape621)
Shape625 = x3d.Shape()
LineSet626 = x3d.LineSet()
LineSet626.vertexCount = [2]
Coordinate627 = x3d.Coordinate()

LineSet626.coord = Coordinate627
""" from skullbase to l_eyebrow_joint vertices 2"""
ColorRGBA628 = x3d.ColorRGBA()
ColorRGBA628.USE = "HAnimSegmentLineColorRGBA"

LineSet626.color = ColorRGBA628

Shape625.geometry = LineSet626

HAnimSegment605.children.append(Shape625)
Shape629 = x3d.Shape()
LineSet630 = x3d.LineSet()
LineSet630.vertexCount = [2]
Coordinate631 = x3d.Coordinate()

LineSet630.coord = Coordinate631
""" from skullbase to r_eyebrow_joint vertices 2"""
ColorRGBA632 = x3d.ColorRGBA()
ColorRGBA632.USE = "HAnimSegmentLineColorRGBA"

LineSet630.color = ColorRGBA632

Shape629.geometry = LineSet630

HAnimSegment605.children.append(Shape629)
Shape633 = x3d.Shape()
LineSet634 = x3d.LineSet()
LineSet634.vertexCount = [2]
Coordinate635 = x3d.Coordinate()

LineSet634.coord = Coordinate635
""" from skullbase to temporomandibular vertices 2"""
ColorRGBA636 = x3d.ColorRGBA()
ColorRGBA636.USE = "HAnimSegmentLineColorRGBA"

LineSet634.color = ColorRGBA636

Shape633.geometry = LineSet634

HAnimSegment605.children.append(Shape633)
HAnimSite637 = x3d.HAnimSite()
HAnimSite637.DEF = "hanim_l_gonion_pt"
HAnimSite637.name = "l_gonion_pt"
HAnimSite637.translation = [0.0631,1.5530,0.0330]
TouchSensor638 = x3d.TouchSensor()
TouchSensor638.description = "HAnimSite l_gonion_pt"

HAnimSite637.children.append(TouchSensor638)
Shape639 = x3d.Shape()
Shape639.USE = "HAnimSiteShape"

HAnimSite637.children.append(Shape639)

HAnimSegment605.children.append(HAnimSite637)
HAnimSite640 = x3d.HAnimSite()
HAnimSite640.DEF = "hanim_menton_pt"
HAnimSite640.name = "menton_pt"
TouchSensor641 = x3d.TouchSensor()
TouchSensor641.description = "HAnimSite menton_pt"

HAnimSite640.children.append(TouchSensor641)
Shape642 = x3d.Shape()
Shape642.USE = "HAnimSiteShape"

HAnimSite640.children.append(Shape642)

HAnimSegment605.children.append(HAnimSite640)
HAnimSite643 = x3d.HAnimSite()
HAnimSite643.DEF = "hanim_r_gonion_pt"
HAnimSite643.name = "r_gonion_pt"
HAnimSite643.translation = [-0.0520,1.5529,0.0347]
TouchSensor644 = x3d.TouchSensor()
TouchSensor644.description = "HAnimSite r_gonion_pt"

HAnimSite643.children.append(TouchSensor644)
Shape645 = x3d.Shape()
Shape645.USE = "HAnimSiteShape"

HAnimSite643.children.append(Shape645)

HAnimSegment605.children.append(HAnimSite643)
HAnimSite646 = x3d.HAnimSite()
HAnimSite646.DEF = "hanim_supramenton_pt"
HAnimSite646.name = "supramenton_pt"
HAnimSite646.translation = [0.0061,1.5410,0.0805]
TouchSensor647 = x3d.TouchSensor()
TouchSensor647.description = "HAnimSite supramenton_pt"

HAnimSite646.children.append(TouchSensor647)
Shape648 = x3d.Shape()
Shape648.USE = "HAnimSiteShape"

HAnimSite646.children.append(Shape648)

HAnimSegment605.children.append(HAnimSite646)

HAnimJoint604.children.append(HAnimSegment605)
HAnimJoint649 = x3d.HAnimJoint()
HAnimJoint649.DEF = "hanim_l_eyelid_joint"
HAnimJoint649.name = "l_eyelid_joint"
HAnimJoint649.center = [0.0503,1.4157,-0.0689]

HAnimJoint604.children.append(HAnimJoint649)
HAnimJoint650 = x3d.HAnimJoint()
HAnimJoint650.DEF = "hanim_r_eyelid_joint"
HAnimJoint650.name = "r_eyelid_joint"
HAnimJoint650.center = [-0.0507,1.4157,-0.0689]

HAnimJoint604.children.append(HAnimJoint650)
HAnimJoint651 = x3d.HAnimJoint()
HAnimJoint651.DEF = "hanim_l_eyeball_joint"
HAnimJoint651.name = "l_eyeball_joint"
HAnimJoint651.center = [0.0479,1.3963,-0.0188]

HAnimJoint604.children.append(HAnimJoint651)
HAnimJoint652 = x3d.HAnimJoint()
HAnimJoint652.DEF = "hanim_r_eyeball_joint"
HAnimJoint652.name = "r_eyeball_joint"
HAnimJoint652.center = [-0.0483,1.3963,-0.0188]

HAnimJoint604.children.append(HAnimJoint652)
HAnimJoint653 = x3d.HAnimJoint()
HAnimJoint653.DEF = "hanim_l_eyebrow_joint"
HAnimJoint653.name = "l_eyebrow_joint"
HAnimJoint653.center = [0.0216,1.4053,0.0051]

HAnimJoint604.children.append(HAnimJoint653)
HAnimJoint654 = x3d.HAnimJoint()
HAnimJoint654.DEF = "hanim_r_eyebrow_joint"
HAnimJoint654.name = "r_eyebrow_joint"
HAnimJoint654.center = [-0.0219,1.4053,0.0051]

HAnimJoint604.children.append(HAnimJoint654)
HAnimJoint655 = x3d.HAnimJoint()
HAnimJoint655.DEF = "hanim_temporomandibular"
HAnimJoint655.name = "temporomandibular"
HAnimJoint655.center = [-0.0002,1.3043,-0.0865]

HAnimJoint604.children.append(HAnimJoint655)

HAnimJoint562.children.append(HAnimJoint604)

HAnimJoint553.children.append(HAnimJoint562)

HAnimJoint541.children.append(HAnimJoint553)

HAnimJoint532.children.append(HAnimJoint541)

HAnimJoint523.children.append(HAnimJoint532)

HAnimJoint514.children.append(HAnimJoint523)

HAnimJoint505.children.append(HAnimJoint514)

HAnimJoint452.children.append(HAnimJoint505)
HAnimJoint656 = x3d.HAnimJoint()
HAnimJoint656.DEF = "hanim_l_sternoclavicular"
HAnimJoint656.name = "l_sternoclavicular"
HAnimJoint656.center = [0.0820,1.4488,-0.0353]
HAnimSegment657 = x3d.HAnimSegment()
HAnimSegment657.DEF = "hanim_l_clavicle"
HAnimSegment657.name = "l_clavicle"
Transform658 = x3d.Transform()
Transform658.translation = [0.0820,1.4488,-0.0353]
Transform659 = x3d.Transform()
""" Empty Transform """
Shape660 = x3d.Shape()
Shape660.USE = "HAnimJointShape"

Transform659.children.append(Shape660)

Transform658.children.append(Transform659)

HAnimSegment657.children.append(Transform658)
Shape661 = x3d.Shape()
LineSet662 = x3d.LineSet()
LineSet662.vertexCount = [2]
Coordinate663 = x3d.Coordinate()

LineSet662.coord = Coordinate663
""" from l_sternoclavicular to l_acromioclavicular vertices 2"""
ColorRGBA664 = x3d.ColorRGBA()
ColorRGBA664.USE = "HAnimSegmentLineColorRGBA"

LineSet662.color = ColorRGBA664

Shape661.geometry = LineSet662

HAnimSegment657.children.append(Shape661)

HAnimJoint656.children.append(HAnimSegment657)
HAnimJoint665 = x3d.HAnimJoint()
HAnimJoint665.DEF = "hanim_l_acromioclavicular"
HAnimJoint665.name = "l_acromioclavicular"
HAnimJoint665.center = [0.0962,1.4269,-0.0424]
HAnimSegment666 = x3d.HAnimSegment()
HAnimSegment666.DEF = "hanim_l_scapula"
HAnimSegment666.name = "l_scapula"
Transform667 = x3d.Transform()
Transform667.translation = [0.0962,1.4269,-0.0424]
Transform668 = x3d.Transform()
""" Empty Transform """
Shape669 = x3d.Shape()
Shape669.USE = "HAnimJointShape"

Transform668.children.append(Shape669)

Transform667.children.append(Transform668)

HAnimSegment666.children.append(Transform667)
Shape670 = x3d.Shape()
LineSet671 = x3d.LineSet()
LineSet671.vertexCount = [2]
Coordinate672 = x3d.Coordinate()

LineSet671.coord = Coordinate672
""" from l_acromioclavicular to l_shoulder vertices 2"""
ColorRGBA673 = x3d.ColorRGBA()
ColorRGBA673.USE = "HAnimSegmentLineColorRGBA"

LineSet671.color = ColorRGBA673

Shape670.geometry = LineSet671

HAnimSegment666.children.append(Shape670)
HAnimSite674 = x3d.HAnimSite()
HAnimSite674.DEF = "hanim_l_bideltoid_pt"
HAnimSite674.name = "l_bideltoid_pt"
TouchSensor675 = x3d.TouchSensor()
TouchSensor675.description = "HAnimSite l_bideltoid_pt"

HAnimSite674.children.append(TouchSensor675)
Shape676 = x3d.Shape()
Shape676.USE = "HAnimSiteShape"

HAnimSite674.children.append(Shape676)

HAnimSegment666.children.append(HAnimSite674)
HAnimSite677 = x3d.HAnimSite()
HAnimSite677.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite677.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite677.translation = [0.2280,1.1482,-0.1100]
TouchSensor678 = x3d.TouchSensor()
TouchSensor678.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite677.children.append(TouchSensor678)
Shape679 = x3d.Shape()
Shape679.USE = "HAnimSiteShape"

HAnimSite677.children.append(Shape679)

HAnimSegment666.children.append(HAnimSite677)

HAnimJoint665.children.append(HAnimSegment666)
HAnimJoint680 = x3d.HAnimJoint()
HAnimJoint680.DEF = "hanim_l_shoulder"
HAnimJoint680.name = "l_shoulder"
HAnimJoint680.center = [0.2029,1.4376,-0.0387]
HAnimSegment681 = x3d.HAnimSegment()
HAnimSegment681.DEF = "hanim_l_upperarm"
HAnimSegment681.name = "l_upperarm"
Transform682 = x3d.Transform()
Transform682.translation = [0.2029,1.4376,-0.0387]
Transform683 = x3d.Transform()
""" Empty Transform """
Shape684 = x3d.Shape()
Shape684.USE = "HAnimJointShape"

Transform683.children.append(Shape684)

Transform682.children.append(Transform683)

HAnimSegment681.children.append(Transform682)
Shape685 = x3d.Shape()
LineSet686 = x3d.LineSet()
LineSet686.vertexCount = [2]
Coordinate687 = x3d.Coordinate()

LineSet686.coord = Coordinate687
""" from l_shoulder to l_elbow vertices 2"""
ColorRGBA688 = x3d.ColorRGBA()
ColorRGBA688.USE = "HAnimSegmentLineColorRGBA"

LineSet686.color = ColorRGBA688

Shape685.geometry = LineSet686

HAnimSegment681.children.append(Shape685)
HAnimSite689 = x3d.HAnimSite()
HAnimSite689.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite689.name = "l_humeral_medial_epicondyles_pt"
HAnimSite689.translation = [0.1735,1.1272,-0.1113]
TouchSensor690 = x3d.TouchSensor()
TouchSensor690.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite689.children.append(TouchSensor690)
Shape691 = x3d.Shape()
Shape691.USE = "HAnimSiteShape"

HAnimSite689.children.append(Shape691)

HAnimSegment681.children.append(HAnimSite689)
HAnimSite692 = x3d.HAnimSite()
HAnimSite692.DEF = "hanim_l_olecranon_pt"
HAnimSite692.name = "l_olecranon_pt"
HAnimSite692.translation = [-0.1962,1.1375,-0.1123]
TouchSensor693 = x3d.TouchSensor()
TouchSensor693.description = "HAnimSite l_olecranon_pt"

HAnimSite692.children.append(TouchSensor693)
Shape694 = x3d.Shape()
Shape694.USE = "HAnimSiteShape"

HAnimSite692.children.append(Shape694)

HAnimSegment681.children.append(HAnimSite692)
HAnimSite695 = x3d.HAnimSite()
HAnimSite695.DEF = "hanim_l_radial_styloid_pt"
HAnimSite695.name = "l_radial_styloid_pt"
HAnimSite695.translation = [0.1901,0.8645,-0.0415]
TouchSensor696 = x3d.TouchSensor()
TouchSensor696.description = "HAnimSite l_radial_styloid_pt"

HAnimSite695.children.append(TouchSensor696)
Shape697 = x3d.Shape()
Shape697.USE = "HAnimSiteShape"

HAnimSite695.children.append(Shape697)

HAnimSegment681.children.append(HAnimSite695)
HAnimSite698 = x3d.HAnimSite()
HAnimSite698.DEF = "hanim_l_radiale_pt"
HAnimSite698.name = "l_radiale_pt"
HAnimSite698.translation = [0.2182,1.1212,-0.1167]
TouchSensor699 = x3d.TouchSensor()
TouchSensor699.description = "HAnimSite l_radiale_pt"

HAnimSite698.children.append(TouchSensor699)
Shape700 = x3d.Shape()
Shape700.USE = "HAnimSiteShape"

HAnimSite698.children.append(Shape700)

HAnimSegment681.children.append(HAnimSite698)

HAnimJoint680.children.append(HAnimSegment681)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.DEF = "hanim_l_elbow"
HAnimJoint701.name = "l_elbow"
HAnimJoint701.center = [0.2014,1.1357,-0.0682]
HAnimSegment702 = x3d.HAnimSegment()
HAnimSegment702.DEF = "hanim_l_forearm"
HAnimSegment702.name = "l_forearm"
Transform703 = x3d.Transform()
Transform703.translation = [0.2014,1.1357,-0.0682]
Transform704 = x3d.Transform()
""" Empty Transform """
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
""" from l_elbow to l_radiocarpal vertices 2"""
ColorRGBA709 = x3d.ColorRGBA()
ColorRGBA709.USE = "HAnimSegmentLineColorRGBA"

LineSet707.color = ColorRGBA709

Shape706.geometry = LineSet707

HAnimSegment702.children.append(Shape706)
HAnimSite710 = x3d.HAnimSite()
HAnimSite710.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite710.name = "l_ulnar_styloid_pt"
HAnimSite710.translation = [-0.2142,0.8529,-0.0648]
TouchSensor711 = x3d.TouchSensor()
TouchSensor711.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite710.children.append(TouchSensor711)
Shape712 = x3d.Shape()
Shape712.USE = "HAnimSiteShape"

HAnimSite710.children.append(Shape712)

HAnimSegment702.children.append(HAnimSite710)

HAnimJoint701.children.append(HAnimSegment702)
HAnimJoint713 = x3d.HAnimJoint()
HAnimJoint713.DEF = "hanim_l_radiocarpal"
HAnimJoint713.name = "l_radiocarpal"
HAnimJoint713.center = [0.1984,0.8663,-0.0583]
HAnimSegment714 = x3d.HAnimSegment()
HAnimSegment714.DEF = "hanim_l_carpal"
HAnimSegment714.name = "l_carpal"
Transform715 = x3d.Transform()
Transform715.scale = [0.2,0.2,0.2]
Transform715.translation = [0.20,0.85,-0.05]
Transform715.rotation = [0,0,1,-3.14]
""" Transform left hand """
Transform716 = x3d.Transform()
Transform716.rotation = [0,1,0,-1.57]
""" Transform left hand """
Shape717 = x3d.Shape()
Shape717.USE = "HAnimJointShape"

Transform716.children.append(Shape717)

Transform715.children.append(Transform716)

HAnimSegment714.children.append(Transform715)
Shape718 = x3d.Shape()
LineSet719 = x3d.LineSet()
LineSet719.vertexCount = [2]
Coordinate720 = x3d.Coordinate()

LineSet719.coord = Coordinate720
""" from l_radiocarpal to l_carpometacarpal_1 vertices 2"""
ColorRGBA721 = x3d.ColorRGBA()
ColorRGBA721.USE = "HAnimSegmentLineColorRGBA"

LineSet719.color = ColorRGBA721

Shape718.geometry = LineSet719

HAnimSegment714.children.append(Shape718)
Shape722 = x3d.Shape()
LineSet723 = x3d.LineSet()
LineSet723.vertexCount = [2]
Coordinate724 = x3d.Coordinate()

LineSet723.coord = Coordinate724
""" from l_radiocarpal to l_carpometacarpal_2 vertices 2"""
ColorRGBA725 = x3d.ColorRGBA()
ColorRGBA725.USE = "HAnimSegmentLineColorRGBA"

LineSet723.color = ColorRGBA725

Shape722.geometry = LineSet723

HAnimSegment714.children.append(Shape722)
HAnimSite726 = x3d.HAnimSite()
HAnimSite726.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite726.name = "l_metacarpal_phalanx_2_pt"
HAnimSite726.translation = [0.2009,0.8139,-0.0237]
TouchSensor727 = x3d.TouchSensor()
TouchSensor727.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite726.children.append(TouchSensor727)
Shape728 = x3d.Shape()
Shape728.USE = "HAnimSiteShape"

HAnimSite726.children.append(Shape728)

HAnimSegment714.children.append(HAnimSite726)
Shape729 = x3d.Shape()
LineSet730 = x3d.LineSet()
LineSet730.vertexCount = [2]
Coordinate731 = x3d.Coordinate()

LineSet730.coord = Coordinate731
""" from l_radiocarpal to l_carpometacarpal_3 vertices 2"""
ColorRGBA732 = x3d.ColorRGBA()
ColorRGBA732.USE = "HAnimSegmentLineColorRGBA"

LineSet730.color = ColorRGBA732

Shape729.geometry = LineSet730

HAnimSegment714.children.append(Shape729)
HAnimSite733 = x3d.HAnimSite()
HAnimSite733.DEF = "hanim_l_metacarpal_phalanx_3_pt"
HAnimSite733.name = "l_metacarpal_phalanx_3_pt"
TouchSensor734 = x3d.TouchSensor()
TouchSensor734.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite733.children.append(TouchSensor734)
Shape735 = x3d.Shape()
Shape735.USE = "HAnimSiteShape"

HAnimSite733.children.append(Shape735)

HAnimSegment714.children.append(HAnimSite733)
Shape736 = x3d.Shape()
LineSet737 = x3d.LineSet()
LineSet737.vertexCount = [2]
Coordinate738 = x3d.Coordinate()

LineSet737.coord = Coordinate738
""" from l_radiocarpal to l_carpometacarpal_4 vertices 2"""
ColorRGBA739 = x3d.ColorRGBA()
ColorRGBA739.USE = "HAnimSegmentLineColorRGBA"

LineSet737.color = ColorRGBA739

Shape736.geometry = LineSet737

HAnimSegment714.children.append(Shape736)
Shape740 = x3d.Shape()
LineSet741 = x3d.LineSet()
LineSet741.vertexCount = [2]
Coordinate742 = x3d.Coordinate()

LineSet741.coord = Coordinate742
""" from l_radiocarpal to l_carpometacarpal_5 vertices 2"""
ColorRGBA743 = x3d.ColorRGBA()
ColorRGBA743.USE = "HAnimSegmentLineColorRGBA"

LineSet741.color = ColorRGBA743

Shape740.geometry = LineSet741

HAnimSegment714.children.append(Shape740)
HAnimSite744 = x3d.HAnimSite()
HAnimSite744.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite744.name = "l_metacarpal_phalanx_5_pt"
HAnimSite744.translation = [0.1929,0.7860,-0.1122]
TouchSensor745 = x3d.TouchSensor()
TouchSensor745.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite744.children.append(TouchSensor745)
Shape746 = x3d.Shape()
Shape746.USE = "HAnimSiteShape"

HAnimSite744.children.append(Shape746)

HAnimSegment714.children.append(HAnimSite744)

HAnimJoint713.children.append(HAnimSegment714)
HAnimJoint747 = x3d.HAnimJoint()
HAnimJoint747.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint747.name = "l_carpometacarpal_1"
HAnimJoint747.center = [0.1924,0.8472,-0.0534]
HAnimSegment748 = x3d.HAnimSegment()
HAnimSegment748.DEF = "hanim_l_metacarpal_1"
HAnimSegment748.name = "l_metacarpal_1"
Transform749 = x3d.Transform()
Transform749.translation = [0.1924,0.8472,-0.0534]
Transform750 = x3d.Transform()
""" Empty Transform """
Shape751 = x3d.Shape()
Shape751.USE = "HAnimJointShape"

Transform750.children.append(Shape751)

Transform749.children.append(Transform750)

HAnimSegment748.children.append(Transform749)
Shape752 = x3d.Shape()
LineSet753 = x3d.LineSet()
LineSet753.vertexCount = [2]
Coordinate754 = x3d.Coordinate()

LineSet753.coord = Coordinate754
""" from l_carpometacarpal_1 to l_metacarpophalangeal_1 vertices 2"""
ColorRGBA755 = x3d.ColorRGBA()
ColorRGBA755.USE = "HAnimSegmentLineColorRGBA"

LineSet753.color = ColorRGBA755

Shape752.geometry = LineSet753

HAnimSegment748.children.append(Shape752)

HAnimJoint747.children.append(HAnimSegment748)
HAnimJoint756 = x3d.HAnimJoint()
HAnimJoint756.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint756.name = "l_metacarpophalangeal_1"
HAnimJoint756.center = [0.1951,0.8226,0.0246]
HAnimSegment757 = x3d.HAnimSegment()
HAnimSegment757.DEF = "hanim_l_carpal_proximal_phalanx_1"
HAnimSegment757.name = "l_carpal_proximal_phalanx_1"
Transform758 = x3d.Transform()
Transform758.translation = [0.1951,0.8226,0.0246]
Transform759 = x3d.Transform()
""" Empty Transform """
Shape760 = x3d.Shape()
Shape760.USE = "HAnimJointShape"

Transform759.children.append(Shape760)

Transform758.children.append(Transform759)

HAnimSegment757.children.append(Transform758)
Shape761 = x3d.Shape()
LineSet762 = x3d.LineSet()
LineSet762.vertexCount = [2]
Coordinate763 = x3d.Coordinate()

LineSet762.coord = Coordinate763
""" from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 vertices 2"""
ColorRGBA764 = x3d.ColorRGBA()
ColorRGBA764.USE = "HAnimSegmentLineColorRGBA"

LineSet762.color = ColorRGBA764

Shape761.geometry = LineSet762

HAnimSegment757.children.append(Shape761)
HAnimSite765 = x3d.HAnimSite()
HAnimSite765.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite765.name = "l_carpal_distal_phalanx_1_tip"
TouchSensor766 = x3d.TouchSensor()
TouchSensor766.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite765.children.append(TouchSensor766)
Shape767 = x3d.Shape()
Shape767.USE = "HAnimSiteShape"

HAnimSite765.children.append(Shape767)

HAnimSegment757.children.append(HAnimSite765)

HAnimJoint756.children.append(HAnimSegment757)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint768.name = "l_carpal_interphalangeal_1"
HAnimJoint768.center = [0.1955,0.8159,0.0464]

HAnimJoint756.children.append(HAnimJoint768)

HAnimJoint747.children.append(HAnimJoint756)

HAnimJoint713.children.append(HAnimJoint747)
HAnimJoint769 = x3d.HAnimJoint()
HAnimJoint769.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint769.name = "l_carpometacarpal_2"
HAnimJoint769.center = [0.1983,0.8024,-0.0280]
HAnimSegment770 = x3d.HAnimSegment()
HAnimSegment770.DEF = "hanim_l_metacarpal_2"
HAnimSegment770.name = "l_metacarpal_2"
Transform771 = x3d.Transform()
Transform771.translation = [0.1983,0.8024,-0.0280]
Transform772 = x3d.Transform()
""" Empty Transform """
Shape773 = x3d.Shape()
Shape773.USE = "HAnimJointShape"

Transform772.children.append(Shape773)

Transform771.children.append(Transform772)

HAnimSegment770.children.append(Transform771)
Shape774 = x3d.Shape()
LineSet775 = x3d.LineSet()
LineSet775.vertexCount = [2]
Coordinate776 = x3d.Coordinate()

LineSet775.coord = Coordinate776
""" from l_carpometacarpal_2 to l_metacarpophalangeal_2 vertices 2"""
ColorRGBA777 = x3d.ColorRGBA()
ColorRGBA777.USE = "HAnimSegmentLineColorRGBA"

LineSet775.color = ColorRGBA777

Shape774.geometry = LineSet775

HAnimSegment770.children.append(Shape774)

HAnimJoint769.children.append(HAnimSegment770)
HAnimJoint778 = x3d.HAnimJoint()
HAnimJoint778.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint778.name = "l_metacarpophalangeal_2"
HAnimJoint778.center = [0.1983,0.7815,-0.0280]
HAnimSegment779 = x3d.HAnimSegment()
HAnimSegment779.DEF = "hanim_l_carpal_proximal_phalanx_2"
HAnimSegment779.name = "l_carpal_proximal_phalanx_2"
Transform780 = x3d.Transform()
Transform780.translation = [0.1983,0.7815,-0.0280]
Transform781 = x3d.Transform()
""" Empty Transform """
Shape782 = x3d.Shape()
Shape782.USE = "HAnimJointShape"

Transform781.children.append(Shape782)

Transform780.children.append(Transform781)

HAnimSegment779.children.append(Transform780)
Shape783 = x3d.Shape()
LineSet784 = x3d.LineSet()
LineSet784.vertexCount = [2]
Coordinate785 = x3d.Coordinate()

LineSet784.coord = Coordinate785
""" from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA786 = x3d.ColorRGBA()
ColorRGBA786.USE = "HAnimSegmentLineColorRGBA"

LineSet784.color = ColorRGBA786

Shape783.geometry = LineSet784

HAnimSegment779.children.append(Shape783)

HAnimJoint778.children.append(HAnimSegment779)
HAnimJoint787 = x3d.HAnimJoint()
HAnimJoint787.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint787.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint787.center = [0.2017,0.7363,-0.0248]
HAnimSegment788 = x3d.HAnimSegment()
HAnimSegment788.DEF = "hanim_l_carpal_middle_phalanx_2"
HAnimSegment788.name = "l_carpal_middle_phalanx_2"
Transform789 = x3d.Transform()
Transform789.translation = [0.2017,0.7363,-0.0248]
Transform790 = x3d.Transform()
""" Empty Transform """
Shape791 = x3d.Shape()
Shape791.USE = "HAnimJointShape"

Transform790.children.append(Shape791)

Transform789.children.append(Transform790)

HAnimSegment788.children.append(Transform789)
Shape792 = x3d.Shape()
LineSet793 = x3d.LineSet()
LineSet793.vertexCount = [2]
Coordinate794 = x3d.Coordinate()

LineSet793.coord = Coordinate794
""" from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 vertices 2"""
ColorRGBA795 = x3d.ColorRGBA()
ColorRGBA795.USE = "HAnimSegmentLineColorRGBA"

LineSet793.color = ColorRGBA795

Shape792.geometry = LineSet793

HAnimSegment788.children.append(Shape792)
HAnimSite796 = x3d.HAnimSite()
HAnimSite796.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite796.name = "l_carpal_distal_phalanx_2_tip"
TouchSensor797 = x3d.TouchSensor()
TouchSensor797.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite796.children.append(TouchSensor797)
Shape798 = x3d.Shape()
Shape798.USE = "HAnimSiteShape"

HAnimSite796.children.append(Shape798)

HAnimSegment788.children.append(HAnimSite796)
HAnimSite799 = x3d.HAnimSite()
HAnimSite799.DEF = "hanim_l_dactylion_pt"
HAnimSite799.name = "l_dactylion_pt"
HAnimSite799.translation = [0.2056,0.6743,-0.0482]
TouchSensor800 = x3d.TouchSensor()
TouchSensor800.description = "HAnimSite l_dactylion_pt"

HAnimSite799.children.append(TouchSensor800)
Shape801 = x3d.Shape()
Shape801.USE = "HAnimSiteShape"

HAnimSite799.children.append(Shape801)

HAnimSegment788.children.append(HAnimSite799)

HAnimJoint787.children.append(HAnimSegment788)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint802.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint802.center = [0.2028,0.7139,-0.0236]

HAnimJoint787.children.append(HAnimJoint802)

HAnimJoint778.children.append(HAnimJoint787)

HAnimJoint769.children.append(HAnimJoint778)

HAnimJoint713.children.append(HAnimJoint769)
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint803.name = "l_carpometacarpal_3"
HAnimJoint803.center = [0.1987,0.8029,-0.0530]
HAnimSegment804 = x3d.HAnimSegment()
HAnimSegment804.DEF = "hanim_l_metacarpal_3"
HAnimSegment804.name = "l_metacarpal_3"
Transform805 = x3d.Transform()
Transform805.translation = [0.1987,0.8029,-0.0530]
Transform806 = x3d.Transform()
""" Empty Transform """
Shape807 = x3d.Shape()
Shape807.USE = "HAnimJointShape"

Transform806.children.append(Shape807)

Transform805.children.append(Transform806)

HAnimSegment804.children.append(Transform805)
Shape808 = x3d.Shape()
LineSet809 = x3d.LineSet()
LineSet809.vertexCount = [2]
Coordinate810 = x3d.Coordinate()

LineSet809.coord = Coordinate810
""" from l_carpometacarpal_3 to l_metacarpophalangeal_3 vertices 2"""
ColorRGBA811 = x3d.ColorRGBA()
ColorRGBA811.USE = "HAnimSegmentLineColorRGBA"

LineSet809.color = ColorRGBA811

Shape808.geometry = LineSet809

HAnimSegment804.children.append(Shape808)

HAnimJoint803.children.append(HAnimSegment804)
HAnimJoint812 = x3d.HAnimJoint()
HAnimJoint812.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint812.name = "l_metacarpophalangeal_3"
HAnimJoint812.center = [0.1987,0.7818,-0.0530]
HAnimSegment813 = x3d.HAnimSegment()
HAnimSegment813.DEF = "hanim_l_carpal_proximal_phalanx_3"
HAnimSegment813.name = "l_carpal_proximal_phalanx_3"
Transform814 = x3d.Transform()
Transform814.translation = [0.1987,0.7818,-0.0530]
Transform815 = x3d.Transform()
""" Empty Transform """
Shape816 = x3d.Shape()
Shape816.USE = "HAnimJointShape"

Transform815.children.append(Shape816)

Transform814.children.append(Transform815)

HAnimSegment813.children.append(Transform814)
Shape817 = x3d.Shape()
LineSet818 = x3d.LineSet()
LineSet818.vertexCount = [2]
Coordinate819 = x3d.Coordinate()

LineSet818.coord = Coordinate819
""" from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA820 = x3d.ColorRGBA()
ColorRGBA820.USE = "HAnimSegmentLineColorRGBA"

LineSet818.color = ColorRGBA820

Shape817.geometry = LineSet818

HAnimSegment813.children.append(Shape817)

HAnimJoint812.children.append(HAnimSegment813)
HAnimJoint821 = x3d.HAnimJoint()
HAnimJoint821.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint821.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint821.center = [0.2013,0.7273,-0.0503]
HAnimSegment822 = x3d.HAnimSegment()
HAnimSegment822.DEF = "hanim_l_carpal_middle_phalanx_3"
HAnimSegment822.name = "l_carpal_middle_phalanx_3"
Transform823 = x3d.Transform()
Transform823.translation = [0.2013,0.7273,-0.0503]
Transform824 = x3d.Transform()
""" Empty Transform """
Shape825 = x3d.Shape()
Shape825.USE = "HAnimJointShape"

Transform824.children.append(Shape825)

Transform823.children.append(Transform824)

HAnimSegment822.children.append(Transform823)
Shape826 = x3d.Shape()
LineSet827 = x3d.LineSet()
LineSet827.vertexCount = [2]
Coordinate828 = x3d.Coordinate()

LineSet827.coord = Coordinate828
""" from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 vertices 2"""
ColorRGBA829 = x3d.ColorRGBA()
ColorRGBA829.USE = "HAnimSegmentLineColorRGBA"

LineSet827.color = ColorRGBA829

Shape826.geometry = LineSet827

HAnimSegment822.children.append(Shape826)
HAnimSite830 = x3d.HAnimSite()
HAnimSite830.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite830.name = "l_carpal_distal_phalanx_3_tip"
TouchSensor831 = x3d.TouchSensor()
TouchSensor831.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite830.children.append(TouchSensor831)
Shape832 = x3d.Shape()
Shape832.USE = "HAnimSiteShape"

HAnimSite830.children.append(Shape832)

HAnimSegment822.children.append(HAnimSite830)

HAnimJoint821.children.append(HAnimSegment822)
HAnimJoint833 = x3d.HAnimJoint()
HAnimJoint833.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint833.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint833.center = [0.2026,0.7011,-0.0494]

HAnimJoint821.children.append(HAnimJoint833)

HAnimJoint812.children.append(HAnimJoint821)

HAnimJoint803.children.append(HAnimJoint812)

HAnimJoint713.children.append(HAnimJoint803)
HAnimJoint834 = x3d.HAnimJoint()
HAnimJoint834.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint834.name = "l_carpometacarpal_4"
HAnimJoint834.center = [0.1956,0.8019,-0.0794]
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.DEF = "hanim_l_metacarpal_4"
HAnimSegment835.name = "l_metacarpal_4"
Transform836 = x3d.Transform()
Transform836.translation = [0.1956,0.8019,-0.0794]
Transform837 = x3d.Transform()
""" Empty Transform """
Shape838 = x3d.Shape()
Shape838.USE = "HAnimJointShape"

Transform837.children.append(Shape838)

Transform836.children.append(Transform837)

HAnimSegment835.children.append(Transform836)
Shape839 = x3d.Shape()
LineSet840 = x3d.LineSet()
LineSet840.vertexCount = [2]
Coordinate841 = x3d.Coordinate()

LineSet840.coord = Coordinate841
""" from l_carpometacarpal_4 to l_metacarpophalangeal_4 vertices 2"""
ColorRGBA842 = x3d.ColorRGBA()
ColorRGBA842.USE = "HAnimSegmentLineColorRGBA"

LineSet840.color = ColorRGBA842

Shape839.geometry = LineSet840

HAnimSegment835.children.append(Shape839)

HAnimJoint834.children.append(HAnimSegment835)
HAnimJoint843 = x3d.HAnimJoint()
HAnimJoint843.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint843.name = "l_metacarpophalangeal_4"
HAnimJoint843.center = [0.1956,0.7815,-0.0794]
HAnimSegment844 = x3d.HAnimSegment()
HAnimSegment844.DEF = "hanim_l_carpal_proximal_phalanx_4"
HAnimSegment844.name = "l_carpal_proximal_phalanx_4"
Transform845 = x3d.Transform()
Transform845.translation = [0.1956,0.7815,-0.0794]
Transform846 = x3d.Transform()
""" Empty Transform """
Shape847 = x3d.Shape()
Shape847.USE = "HAnimJointShape"

Transform846.children.append(Shape847)

Transform845.children.append(Transform846)

HAnimSegment844.children.append(Transform845)
Shape848 = x3d.Shape()
LineSet849 = x3d.LineSet()
LineSet849.vertexCount = [2]
Coordinate850 = x3d.Coordinate()

LineSet849.coord = Coordinate850
""" from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA851 = x3d.ColorRGBA()
ColorRGBA851.USE = "HAnimSegmentLineColorRGBA"

LineSet849.color = ColorRGBA851

Shape848.geometry = LineSet849

HAnimSegment844.children.append(Shape848)

HAnimJoint843.children.append(HAnimSegment844)
HAnimJoint852 = x3d.HAnimJoint()
HAnimJoint852.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint852.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint852.center = [0.1973,0.7287,-0.0777]
HAnimSegment853 = x3d.HAnimSegment()
HAnimSegment853.DEF = "hanim_l_carpal_middle_phalanx_4"
HAnimSegment853.name = "l_carpal_middle_phalanx_4"
Transform854 = x3d.Transform()
Transform854.translation = [0.1973,0.7287,-0.0777]
Transform855 = x3d.Transform()
""" Empty Transform """
Shape856 = x3d.Shape()
Shape856.USE = "HAnimJointShape"

Transform855.children.append(Shape856)

Transform854.children.append(Transform855)

HAnimSegment853.children.append(Transform854)
Shape857 = x3d.Shape()
LineSet858 = x3d.LineSet()
LineSet858.vertexCount = [2]
Coordinate859 = x3d.Coordinate()

LineSet858.coord = Coordinate859
""" from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 vertices 2"""
ColorRGBA860 = x3d.ColorRGBA()
ColorRGBA860.USE = "HAnimSegmentLineColorRGBA"

LineSet858.color = ColorRGBA860

Shape857.geometry = LineSet858

HAnimSegment853.children.append(Shape857)
HAnimSite861 = x3d.HAnimSite()
HAnimSite861.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite861.name = "l_carpal_distal_phalanx_4_tip"
TouchSensor862 = x3d.TouchSensor()
TouchSensor862.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite861.children.append(TouchSensor862)
Shape863 = x3d.Shape()
Shape863.USE = "HAnimSiteShape"

HAnimSite861.children.append(Shape863)

HAnimSegment853.children.append(HAnimSite861)

HAnimJoint852.children.append(HAnimSegment853)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint864.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint864.center = [0.1983,0.7045,-0.0767]

HAnimJoint852.children.append(HAnimJoint864)

HAnimJoint843.children.append(HAnimJoint852)

HAnimJoint834.children.append(HAnimJoint843)

HAnimJoint713.children.append(HAnimJoint834)
HAnimJoint865 = x3d.HAnimJoint()
HAnimJoint865.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint865.name = "l_carpometacarpal_5"
HAnimJoint865.center = [0.1925,0.8066,-0.1036]
HAnimSegment866 = x3d.HAnimSegment()
HAnimSegment866.DEF = "hanim_l_metacarpal_5"
HAnimSegment866.name = "l_metacarpal_5"
Transform867 = x3d.Transform()
Transform867.translation = [0.1925,0.8066,-0.1036]
Transform868 = x3d.Transform()
""" Empty Transform """
Shape869 = x3d.Shape()
Shape869.USE = "HAnimJointShape"

Transform868.children.append(Shape869)

Transform867.children.append(Transform868)

HAnimSegment866.children.append(Transform867)
Shape870 = x3d.Shape()
LineSet871 = x3d.LineSet()
LineSet871.vertexCount = [2]
Coordinate872 = x3d.Coordinate()

LineSet871.coord = Coordinate872
""" from l_carpometacarpal_5 to l_metacarpophalangeal_5 vertices 2"""
ColorRGBA873 = x3d.ColorRGBA()
ColorRGBA873.USE = "HAnimSegmentLineColorRGBA"

LineSet871.color = ColorRGBA873

Shape870.geometry = LineSet871

HAnimSegment866.children.append(Shape870)

HAnimJoint865.children.append(HAnimSegment866)
HAnimJoint874 = x3d.HAnimJoint()
HAnimJoint874.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint874.name = "l_metacarpophalangeal_5"
HAnimJoint874.center = [0.1925,0.7866,-0.1036]
HAnimSegment875 = x3d.HAnimSegment()
HAnimSegment875.DEF = "hanim_l_carpal_proximal_phalanx_5"
HAnimSegment875.name = "l_carpal_proximal_phalanx_5"
Transform876 = x3d.Transform()
Transform876.translation = [0.1925,0.7866,-0.1036]
Transform877 = x3d.Transform()
""" Empty Transform """
Shape878 = x3d.Shape()
Shape878.USE = "HAnimJointShape"

Transform877.children.append(Shape878)

Transform876.children.append(Transform877)

HAnimSegment875.children.append(Transform876)
Shape879 = x3d.Shape()
LineSet880 = x3d.LineSet()
LineSet880.vertexCount = [2]
Coordinate881 = x3d.Coordinate()

LineSet880.coord = Coordinate881
""" from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA882 = x3d.ColorRGBA()
ColorRGBA882.USE = "HAnimSegmentLineColorRGBA"

LineSet880.color = ColorRGBA882

Shape879.geometry = LineSet880

HAnimSegment875.children.append(Shape879)

HAnimJoint874.children.append(HAnimSegment875)
HAnimJoint883 = x3d.HAnimJoint()
HAnimJoint883.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint883.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint883.center = [0.1938,0.7452,-0.1024]
HAnimSegment884 = x3d.HAnimSegment()
HAnimSegment884.DEF = "hanim_l_carpal_middle_phalanx_5"
HAnimSegment884.name = "l_carpal_middle_phalanx_5"
Transform885 = x3d.Transform()
Transform885.translation = [0.1938,0.7452,-0.1024]
Transform886 = x3d.Transform()
""" Empty Transform """
Shape887 = x3d.Shape()
Shape887.USE = "HAnimJointShape"

Transform886.children.append(Shape887)

Transform885.children.append(Transform886)

HAnimSegment884.children.append(Transform885)
Shape888 = x3d.Shape()
LineSet889 = x3d.LineSet()
LineSet889.vertexCount = [2]
Coordinate890 = x3d.Coordinate()

LineSet889.coord = Coordinate890
""" from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 vertices 2"""
ColorRGBA891 = x3d.ColorRGBA()
ColorRGBA891.USE = "HAnimSegmentLineColorRGBA"

LineSet889.color = ColorRGBA891

Shape888.geometry = LineSet889

HAnimSegment884.children.append(Shape888)
HAnimSite892 = x3d.HAnimSite()
HAnimSite892.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite892.name = "l_carpal_distal_phalanx_5_tip"
TouchSensor893 = x3d.TouchSensor()
TouchSensor893.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite892.children.append(TouchSensor893)
Shape894 = x3d.Shape()
Shape894.USE = "HAnimSiteShape"

HAnimSite892.children.append(Shape894)

HAnimSegment884.children.append(HAnimSite892)

HAnimJoint883.children.append(HAnimSegment884)
HAnimJoint895 = x3d.HAnimJoint()
HAnimJoint895.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint895.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint895.center = [0.1948,0.7277,-0.1017]

HAnimJoint883.children.append(HAnimJoint895)

HAnimJoint874.children.append(HAnimJoint883)

HAnimJoint865.children.append(HAnimJoint874)

HAnimJoint713.children.append(HAnimJoint865)

HAnimJoint701.children.append(HAnimJoint713)

HAnimJoint680.children.append(HAnimJoint701)

HAnimJoint665.children.append(HAnimJoint680)

HAnimJoint656.children.append(HAnimJoint665)

HAnimJoint452.children.append(HAnimJoint656)
HAnimJoint896 = x3d.HAnimJoint()
HAnimJoint896.DEF = "hanim_r_sternoclavicular"
HAnimJoint896.name = "r_sternoclavicular"
HAnimJoint896.center = [-0.0694,1.4600,-0.0330]
HAnimSegment897 = x3d.HAnimSegment()
HAnimSegment897.DEF = "hanim_r_clavicle"
HAnimSegment897.name = "r_clavicle"
Transform898 = x3d.Transform()
Transform898.translation = [-0.0694,1.4600,-0.0330]
Transform899 = x3d.Transform()
""" Empty Transform """
Shape900 = x3d.Shape()
Shape900.USE = "HAnimJointShape"

Transform899.children.append(Shape900)

Transform898.children.append(Transform899)

HAnimSegment897.children.append(Transform898)
Shape901 = x3d.Shape()
LineSet902 = x3d.LineSet()
LineSet902.vertexCount = [2]
Coordinate903 = x3d.Coordinate()

LineSet902.coord = Coordinate903
""" from r_sternoclavicular to r_acromioclavicular vertices 2"""
ColorRGBA904 = x3d.ColorRGBA()
ColorRGBA904.USE = "HAnimSegmentLineColorRGBA"

LineSet902.color = ColorRGBA904

Shape901.geometry = LineSet902

HAnimSegment897.children.append(Shape901)

HAnimJoint896.children.append(HAnimSegment897)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.DEF = "hanim_r_acromioclavicular"
HAnimJoint905.name = "r_acromioclavicular"
HAnimJoint905.center = [-0.0836,1.4281,-0.0401]
HAnimSegment906 = x3d.HAnimSegment()
HAnimSegment906.DEF = "hanim_r_scapula"
HAnimSegment906.name = "r_scapula"
Transform907 = x3d.Transform()
Transform907.translation = [-0.0836,1.4281,-0.0401]
Transform908 = x3d.Transform()
""" Empty Transform """
Shape909 = x3d.Shape()
Shape909.USE = "HAnimJointShape"

Transform908.children.append(Shape909)

Transform907.children.append(Transform908)

HAnimSegment906.children.append(Transform907)
Shape910 = x3d.Shape()
LineSet911 = x3d.LineSet()
LineSet911.vertexCount = [2]
Coordinate912 = x3d.Coordinate()

LineSet911.coord = Coordinate912
""" from r_acromioclavicular to r_shoulder vertices 2"""
ColorRGBA913 = x3d.ColorRGBA()
ColorRGBA913.USE = "HAnimSegmentLineColorRGBA"

LineSet911.color = ColorRGBA913

Shape910.geometry = LineSet911

HAnimSegment906.children.append(Shape910)
HAnimSite914 = x3d.HAnimSite()
HAnimSite914.DEF = "hanim_r_bideltoid_pt"
HAnimSite914.name = "r_bideltoid_pt"
TouchSensor915 = x3d.TouchSensor()
TouchSensor915.description = "HAnimSite r_bideltoid_pt"

HAnimSite914.children.append(TouchSensor915)
Shape916 = x3d.Shape()
Shape916.USE = "HAnimSiteShape"

HAnimSite914.children.append(Shape916)

HAnimSegment906.children.append(HAnimSite914)
HAnimSite917 = x3d.HAnimSite()
HAnimSite917.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite917.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite917.translation = [-0.2224,1.1517,-0.1033]
TouchSensor918 = x3d.TouchSensor()
TouchSensor918.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite917.children.append(TouchSensor918)
Shape919 = x3d.Shape()
Shape919.USE = "HAnimSiteShape"

HAnimSite917.children.append(Shape919)

HAnimSegment906.children.append(HAnimSite917)

HAnimJoint905.children.append(HAnimSegment906)
HAnimJoint920 = x3d.HAnimJoint()
HAnimJoint920.DEF = "hanim_r_shoulder"
HAnimJoint920.name = "r_shoulder"
HAnimJoint920.center = [-0.1907,1.4407,-0.0325]
HAnimSegment921 = x3d.HAnimSegment()
HAnimSegment921.DEF = "hanim_r_upperarm"
HAnimSegment921.name = "r_upperarm"
Transform922 = x3d.Transform()
Transform922.translation = [-0.1907,1.4407,-0.0325]
Transform923 = x3d.Transform()
""" Empty Transform """
Shape924 = x3d.Shape()
Shape924.USE = "HAnimJointShape"

Transform923.children.append(Shape924)

Transform922.children.append(Transform923)

HAnimSegment921.children.append(Transform922)
Shape925 = x3d.Shape()
LineSet926 = x3d.LineSet()
LineSet926.vertexCount = [2]
Coordinate927 = x3d.Coordinate()

LineSet926.coord = Coordinate927
""" from r_shoulder to r_elbow vertices 2"""
ColorRGBA928 = x3d.ColorRGBA()
ColorRGBA928.USE = "HAnimSegmentLineColorRGBA"

LineSet926.color = ColorRGBA928

Shape925.geometry = LineSet926

HAnimSegment921.children.append(Shape925)
HAnimSite929 = x3d.HAnimSite()
HAnimSite929.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite929.name = "r_humeral_medial_epicondyles_pt"
HAnimSite929.translation = [-0.1680,1.1298,-0.1062]
TouchSensor930 = x3d.TouchSensor()
TouchSensor930.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite929.children.append(TouchSensor930)
Shape931 = x3d.Shape()
Shape931.USE = "HAnimSiteShape"

HAnimSite929.children.append(Shape931)

HAnimSegment921.children.append(HAnimSite929)
HAnimSite932 = x3d.HAnimSite()
HAnimSite932.DEF = "hanim_r_olecranon_pt"
HAnimSite932.name = "r_olecranon_pt"
HAnimSite932.translation = [-0.1907,1.1405,-0.1065]
TouchSensor933 = x3d.TouchSensor()
TouchSensor933.description = "HAnimSite r_olecranon_pt"

HAnimSite932.children.append(TouchSensor933)
Shape934 = x3d.Shape()
Shape934.USE = "HAnimSiteShape"

HAnimSite932.children.append(Shape934)

HAnimSegment921.children.append(HAnimSite932)
HAnimSite935 = x3d.HAnimSite()
HAnimSite935.DEF = "hanim_r_radial_styloid_pt"
HAnimSite935.name = "r_radial_styloid_pt"
HAnimSite935.translation = [-0.1884,0.8676,-0.0360]
TouchSensor936 = x3d.TouchSensor()
TouchSensor936.description = "HAnimSite r_radial_styloid_pt"

HAnimSite935.children.append(TouchSensor936)
Shape937 = x3d.Shape()
Shape937.USE = "HAnimSiteShape"

HAnimSite935.children.append(Shape937)

HAnimSegment921.children.append(HAnimSite935)
HAnimSite938 = x3d.HAnimSite()
HAnimSite938.DEF = "hanim_r_radiale_pt"
HAnimSite938.name = "r_radiale_pt"
HAnimSite938.translation = [-0.2130,1.1305,-0.1091]
TouchSensor939 = x3d.TouchSensor()
TouchSensor939.description = "HAnimSite r_radiale_pt"

HAnimSite938.children.append(TouchSensor939)
Shape940 = x3d.Shape()
Shape940.USE = "HAnimSiteShape"

HAnimSite938.children.append(Shape940)

HAnimSegment921.children.append(HAnimSite938)

HAnimJoint920.children.append(HAnimSegment921)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.DEF = "hanim_r_elbow"
HAnimJoint941.name = "r_elbow"
HAnimJoint941.center = [-0.1949,1.1388,-0.0620]
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.DEF = "hanim_r_forearm"
HAnimSegment942.name = "r_forearm"
Transform943 = x3d.Transform()
Transform943.translation = [-0.1949,1.1388,-0.0620]
Transform944 = x3d.Transform()
""" Empty Transform """
Shape945 = x3d.Shape()
Shape945.USE = "HAnimJointShape"

Transform944.children.append(Shape945)

Transform943.children.append(Transform944)

HAnimSegment942.children.append(Transform943)
Shape946 = x3d.Shape()
LineSet947 = x3d.LineSet()
LineSet947.vertexCount = [2]
Coordinate948 = x3d.Coordinate()

LineSet947.coord = Coordinate948
""" from r_elbow to r_radiocarpal vertices 2"""
ColorRGBA949 = x3d.ColorRGBA()
ColorRGBA949.USE = "HAnimSegmentLineColorRGBA"

LineSet947.color = ColorRGBA949

Shape946.geometry = LineSet947

HAnimSegment942.children.append(Shape946)
HAnimSite950 = x3d.HAnimSite()
HAnimSite950.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite950.name = "r_ulnar_styloid_pt"
HAnimSite950.translation = [-0.2117,0.8562,-0.0584]
TouchSensor951 = x3d.TouchSensor()
TouchSensor951.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite950.children.append(TouchSensor951)
Shape952 = x3d.Shape()
Shape952.USE = "HAnimSiteShape"

HAnimSite950.children.append(Shape952)

HAnimSegment942.children.append(HAnimSite950)

HAnimJoint941.children.append(HAnimSegment942)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.DEF = "hanim_r_radiocarpal"
HAnimJoint953.name = "r_radiocarpal"
HAnimJoint953.center = [-0.1959,0.8694,-0.0521]
HAnimSegment954 = x3d.HAnimSegment()
HAnimSegment954.DEF = "hanim_r_carpal"
HAnimSegment954.name = "r_carpal"
Transform955 = x3d.Transform()
Transform955.scale = [0.2,0.2,0.2]
Transform955.translation = [-0.20,0.85,-0.05]
Transform955.rotation = [0,0,1,-3.14]
""" Transform right hand """
Transform956 = x3d.Transform()
Transform956.rotation = [0,1,0,1.57]
""" Transform right hand """
Shape957 = x3d.Shape()
Shape957.USE = "HAnimJointShape"

Transform956.children.append(Shape957)

Transform955.children.append(Transform956)

HAnimSegment954.children.append(Transform955)
Shape958 = x3d.Shape()
LineSet959 = x3d.LineSet()
LineSet959.vertexCount = [2]
Coordinate960 = x3d.Coordinate()

LineSet959.coord = Coordinate960
""" from r_radiocarpal to r_carpometacarpal_1 vertices 2"""
ColorRGBA961 = x3d.ColorRGBA()
ColorRGBA961.USE = "HAnimSegmentLineColorRGBA"

LineSet959.color = ColorRGBA961

Shape958.geometry = LineSet959

HAnimSegment954.children.append(Shape958)
Shape962 = x3d.Shape()
LineSet963 = x3d.LineSet()
LineSet963.vertexCount = [2]
Coordinate964 = x3d.Coordinate()

LineSet963.coord = Coordinate964
""" from r_radiocarpal to r_carpometacarpal_2 vertices 2"""
ColorRGBA965 = x3d.ColorRGBA()
ColorRGBA965.USE = "HAnimSegmentLineColorRGBA"

LineSet963.color = ColorRGBA965

Shape962.geometry = LineSet963

HAnimSegment954.children.append(Shape962)
HAnimSite966 = x3d.HAnimSite()
HAnimSite966.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite966.name = "r_metacarpal_phalanx_2_pt"
HAnimSite966.translation = [-0.1977,0.8169,-0.0177]
TouchSensor967 = x3d.TouchSensor()
TouchSensor967.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite966.children.append(TouchSensor967)
Shape968 = x3d.Shape()
Shape968.USE = "HAnimSiteShape"

HAnimSite966.children.append(Shape968)

HAnimSegment954.children.append(HAnimSite966)
Shape969 = x3d.Shape()
LineSet970 = x3d.LineSet()
LineSet970.vertexCount = [2]
Coordinate971 = x3d.Coordinate()

LineSet970.coord = Coordinate971
""" from r_radiocarpal to r_carpometacarpal_3 vertices 2"""
ColorRGBA972 = x3d.ColorRGBA()
ColorRGBA972.USE = "HAnimSegmentLineColorRGBA"

LineSet970.color = ColorRGBA972

Shape969.geometry = LineSet970

HAnimSegment954.children.append(Shape969)
HAnimSite973 = x3d.HAnimSite()
HAnimSite973.DEF = "hanim_r_metacarpal_phalanx_3_pt"
HAnimSite973.name = "r_metacarpal_phalanx_3_pt"
TouchSensor974 = x3d.TouchSensor()
TouchSensor974.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite973.children.append(TouchSensor974)
Shape975 = x3d.Shape()
Shape975.USE = "HAnimSiteShape"

HAnimSite973.children.append(Shape975)

HAnimSegment954.children.append(HAnimSite973)
Shape976 = x3d.Shape()
LineSet977 = x3d.LineSet()
LineSet977.vertexCount = [2]
Coordinate978 = x3d.Coordinate()

LineSet977.coord = Coordinate978
""" from r_radiocarpal to r_carpometacarpal_4 vertices 2"""
ColorRGBA979 = x3d.ColorRGBA()
ColorRGBA979.USE = "HAnimSegmentLineColorRGBA"

LineSet977.color = ColorRGBA979

Shape976.geometry = LineSet977

HAnimSegment954.children.append(Shape976)
Shape980 = x3d.Shape()
LineSet981 = x3d.LineSet()
LineSet981.vertexCount = [2]
Coordinate982 = x3d.Coordinate()

LineSet981.coord = Coordinate982
""" from r_radiocarpal to r_carpometacarpal_5 vertices 2"""
ColorRGBA983 = x3d.ColorRGBA()
ColorRGBA983.USE = "HAnimSegmentLineColorRGBA"

LineSet981.color = ColorRGBA983

Shape980.geometry = LineSet981

HAnimSegment954.children.append(Shape980)
HAnimSite984 = x3d.HAnimSite()
HAnimSite984.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite984.name = "r_metacarpal_phalanx_5_pt"
HAnimSite984.translation = [-0.1929,0.7890,-0.1064]
TouchSensor985 = x3d.TouchSensor()
TouchSensor985.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite984.children.append(TouchSensor985)
Shape986 = x3d.Shape()
Shape986.USE = "HAnimSiteShape"

HAnimSite984.children.append(Shape986)

HAnimSegment954.children.append(HAnimSite984)

HAnimJoint953.children.append(HAnimSegment954)
HAnimJoint987 = x3d.HAnimJoint()
HAnimJoint987.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint987.name = "r_carpometacarpal_1"
HAnimJoint987.center = [-0.1899,0.8502,-0.0473]
HAnimSegment988 = x3d.HAnimSegment()
HAnimSegment988.DEF = "hanim_r_metacarpal_1"
HAnimSegment988.name = "r_metacarpal_1"
Transform989 = x3d.Transform()
Transform989.translation = [-0.1899,0.8502,-0.0473]
Transform990 = x3d.Transform()
""" Empty Transform """
Shape991 = x3d.Shape()
Shape991.USE = "HAnimJointShape"

Transform990.children.append(Shape991)

Transform989.children.append(Transform990)

HAnimSegment988.children.append(Transform989)
Shape992 = x3d.Shape()
LineSet993 = x3d.LineSet()
LineSet993.vertexCount = [2]
Coordinate994 = x3d.Coordinate()

LineSet993.coord = Coordinate994
""" from r_carpometacarpal_1 to r_metacarpophalangeal_1 vertices 2"""
ColorRGBA995 = x3d.ColorRGBA()
ColorRGBA995.USE = "HAnimSegmentLineColorRGBA"

LineSet993.color = ColorRGBA995

Shape992.geometry = LineSet993

HAnimSegment988.children.append(Shape992)

HAnimJoint987.children.append(HAnimSegment988)
HAnimJoint996 = x3d.HAnimJoint()
HAnimJoint996.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint996.name = "r_metacarpophalangeal_1"
HAnimJoint996.center = [-0.1874,0.8256,0.0306]
HAnimSegment997 = x3d.HAnimSegment()
HAnimSegment997.DEF = "hanim_r_carpal_proximal_phalanx_1"
HAnimSegment997.name = "r_carpal_proximal_phalanx_1"
Transform998 = x3d.Transform()
Transform998.translation = [-0.1874,0.8256,0.0306]
Transform999 = x3d.Transform()
""" Empty Transform """
Shape1000 = x3d.Shape()
Shape1000.USE = "HAnimJointShape"

Transform999.children.append(Shape1000)

Transform998.children.append(Transform999)

HAnimSegment997.children.append(Transform998)
Shape1001 = x3d.Shape()
LineSet1002 = x3d.LineSet()
LineSet1002.vertexCount = [2]
Coordinate1003 = x3d.Coordinate()

LineSet1002.coord = Coordinate1003
""" from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 vertices 2"""
ColorRGBA1004 = x3d.ColorRGBA()
ColorRGBA1004.USE = "HAnimSegmentLineColorRGBA"

LineSet1002.color = ColorRGBA1004

Shape1001.geometry = LineSet1002

HAnimSegment997.children.append(Shape1001)
HAnimSite1005 = x3d.HAnimSite()
HAnimSite1005.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite1005.name = "r_carpal_distal_phalanx_1_tip"
TouchSensor1006 = x3d.TouchSensor()
TouchSensor1006.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1005.children.append(TouchSensor1006)
Shape1007 = x3d.Shape()
Shape1007.USE = "HAnimSiteShape"

HAnimSite1005.children.append(Shape1007)

HAnimSegment997.children.append(HAnimSite1005)

HAnimJoint996.children.append(HAnimSegment997)
HAnimJoint1008 = x3d.HAnimJoint()
HAnimJoint1008.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1008.name = "r_carpal_interphalangeal_1"
HAnimJoint1008.center = [-0.1864,0.8190,0.0506]

HAnimJoint996.children.append(HAnimJoint1008)

HAnimJoint987.children.append(HAnimJoint996)

HAnimJoint953.children.append(HAnimJoint987)
HAnimJoint1009 = x3d.HAnimJoint()
HAnimJoint1009.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1009.name = "r_carpometacarpal_2"
HAnimJoint1009.center = [-0.1961,0.8055,-0.0218]
HAnimSegment1010 = x3d.HAnimSegment()
HAnimSegment1010.DEF = "hanim_r_metacarpal_2"
HAnimSegment1010.name = "r_metacarpal_2"
Transform1011 = x3d.Transform()
Transform1011.translation = [-0.1961,0.8055,-0.0218]
Transform1012 = x3d.Transform()
""" Empty Transform """
Shape1013 = x3d.Shape()
Shape1013.USE = "HAnimJointShape"

Transform1012.children.append(Shape1013)

Transform1011.children.append(Transform1012)

HAnimSegment1010.children.append(Transform1011)
Shape1014 = x3d.Shape()
LineSet1015 = x3d.LineSet()
LineSet1015.vertexCount = [2]
Coordinate1016 = x3d.Coordinate()

LineSet1015.coord = Coordinate1016
""" from r_carpometacarpal_2 to r_metacarpophalangeal_2 vertices 2"""
ColorRGBA1017 = x3d.ColorRGBA()
ColorRGBA1017.USE = "HAnimSegmentLineColorRGBA"

LineSet1015.color = ColorRGBA1017

Shape1014.geometry = LineSet1015

HAnimSegment1010.children.append(Shape1014)

HAnimJoint1009.children.append(HAnimSegment1010)
HAnimJoint1018 = x3d.HAnimJoint()
HAnimJoint1018.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1018.name = "r_metacarpophalangeal_2"
HAnimJoint1018.center = [-0.1961,0.7846,-0.0218]
HAnimSegment1019 = x3d.HAnimSegment()
HAnimSegment1019.DEF = "hanim_r_carpal_proximal_phalanx_2"
HAnimSegment1019.name = "r_carpal_proximal_phalanx_2"
Transform1020 = x3d.Transform()
Transform1020.translation = [-0.1961,0.7846,-0.0218]
Transform1021 = x3d.Transform()
""" Empty Transform """
Shape1022 = x3d.Shape()
Shape1022.USE = "HAnimJointShape"

Transform1021.children.append(Shape1022)

Transform1020.children.append(Transform1021)

HAnimSegment1019.children.append(Transform1020)
Shape1023 = x3d.Shape()
LineSet1024 = x3d.LineSet()
LineSet1024.vertexCount = [2]
Coordinate1025 = x3d.Coordinate()

LineSet1024.coord = Coordinate1025
""" from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA1026 = x3d.ColorRGBA()
ColorRGBA1026.USE = "HAnimSegmentLineColorRGBA"

LineSet1024.color = ColorRGBA1026

Shape1023.geometry = LineSet1024

HAnimSegment1019.children.append(Shape1023)

HAnimJoint1018.children.append(HAnimSegment1019)
HAnimJoint1027 = x3d.HAnimJoint()
HAnimJoint1027.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1027.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1027.center = [-0.1954,0.7393,-0.0185]
HAnimSegment1028 = x3d.HAnimSegment()
HAnimSegment1028.DEF = "hanim_r_carpal_middle_phalanx_2"
HAnimSegment1028.name = "r_carpal_middle_phalanx_2"
Transform1029 = x3d.Transform()
Transform1029.translation = [-0.1954,0.7393,-0.0185]
Transform1030 = x3d.Transform()
""" Empty Transform """
Shape1031 = x3d.Shape()
Shape1031.USE = "HAnimJointShape"

Transform1030.children.append(Shape1031)

Transform1029.children.append(Transform1030)

HAnimSegment1028.children.append(Transform1029)
Shape1032 = x3d.Shape()
LineSet1033 = x3d.LineSet()
LineSet1033.vertexCount = [2]
Coordinate1034 = x3d.Coordinate()

LineSet1033.coord = Coordinate1034
""" from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 vertices 2"""
ColorRGBA1035 = x3d.ColorRGBA()
ColorRGBA1035.USE = "HAnimSegmentLineColorRGBA"

LineSet1033.color = ColorRGBA1035

Shape1032.geometry = LineSet1033

HAnimSegment1028.children.append(Shape1032)
HAnimSite1036 = x3d.HAnimSite()
HAnimSite1036.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite1036.name = "r_carpal_distal_phalanx_2_tip"
TouchSensor1037 = x3d.TouchSensor()
TouchSensor1037.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1036.children.append(TouchSensor1037)
Shape1038 = x3d.Shape()
Shape1038.USE = "HAnimSiteShape"

HAnimSite1036.children.append(Shape1038)

HAnimSegment1028.children.append(HAnimSite1036)
HAnimSite1039 = x3d.HAnimSite()
HAnimSite1039.DEF = "hanim_r_dactylion_pt"
HAnimSite1039.name = "r_dactylion_pt"
HAnimSite1039.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1040 = x3d.TouchSensor()
TouchSensor1040.description = "HAnimSite r_dactylion_pt"

HAnimSite1039.children.append(TouchSensor1040)
Shape1041 = x3d.Shape()
Shape1041.USE = "HAnimSiteShape"

HAnimSite1039.children.append(Shape1041)

HAnimSegment1028.children.append(HAnimSite1039)

HAnimJoint1027.children.append(HAnimSegment1028)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1042.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1042.center = [-0.1945,0.7169,-0.0173]

HAnimJoint1027.children.append(HAnimJoint1042)

HAnimJoint1018.children.append(HAnimJoint1027)

HAnimJoint1009.children.append(HAnimJoint1018)

HAnimJoint953.children.append(HAnimJoint1009)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1043.name = "r_carpometacarpal_3"
HAnimJoint1043.center = [-0.1972,0.8060,-0.0468]
HAnimSegment1044 = x3d.HAnimSegment()
HAnimSegment1044.DEF = "hanim_r_metacarpal_3"
HAnimSegment1044.name = "r_metacarpal_3"
Transform1045 = x3d.Transform()
Transform1045.translation = [-0.1972,0.8060,-0.0468]
Transform1046 = x3d.Transform()
""" Empty Transform """
Shape1047 = x3d.Shape()
Shape1047.USE = "HAnimJointShape"

Transform1046.children.append(Shape1047)

Transform1045.children.append(Transform1046)

HAnimSegment1044.children.append(Transform1045)
Shape1048 = x3d.Shape()
LineSet1049 = x3d.LineSet()
LineSet1049.vertexCount = [2]
Coordinate1050 = x3d.Coordinate()

LineSet1049.coord = Coordinate1050
""" from r_carpometacarpal_3 to r_metacarpophalangeal_3 vertices 2"""
ColorRGBA1051 = x3d.ColorRGBA()
ColorRGBA1051.USE = "HAnimSegmentLineColorRGBA"

LineSet1049.color = ColorRGBA1051

Shape1048.geometry = LineSet1049

HAnimSegment1044.children.append(Shape1048)

HAnimJoint1043.children.append(HAnimSegment1044)
HAnimJoint1052 = x3d.HAnimJoint()
HAnimJoint1052.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1052.name = "r_metacarpophalangeal_3"
HAnimJoint1052.center = [-0.1972,0.7849,-0.0468]
HAnimSegment1053 = x3d.HAnimSegment()
HAnimSegment1053.DEF = "hanim_r_carpal_proximal_phalanx_3"
HAnimSegment1053.name = "r_carpal_proximal_phalanx_3"
Transform1054 = x3d.Transform()
Transform1054.translation = [-0.1972,0.7849,-0.0468]
Transform1055 = x3d.Transform()
""" Empty Transform """
Shape1056 = x3d.Shape()
Shape1056.USE = "HAnimJointShape"

Transform1055.children.append(Shape1056)

Transform1054.children.append(Transform1055)

HAnimSegment1053.children.append(Transform1054)
Shape1057 = x3d.Shape()
LineSet1058 = x3d.LineSet()
LineSet1058.vertexCount = [2]
Coordinate1059 = x3d.Coordinate()

LineSet1058.coord = Coordinate1059
""" from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA1060 = x3d.ColorRGBA()
ColorRGBA1060.USE = "HAnimSegmentLineColorRGBA"

LineSet1058.color = ColorRGBA1060

Shape1057.geometry = LineSet1058

HAnimSegment1053.children.append(Shape1057)

HAnimJoint1052.children.append(HAnimSegment1053)
HAnimJoint1061 = x3d.HAnimJoint()
HAnimJoint1061.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1061.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1061.center = [-0.1950,0.7304,-0.0441]
HAnimSegment1062 = x3d.HAnimSegment()
HAnimSegment1062.DEF = "hanim_r_carpal_middle_phalanx_3"
HAnimSegment1062.name = "r_carpal_middle_phalanx_3"
Transform1063 = x3d.Transform()
Transform1063.translation = [-0.1950,0.7304,-0.0441]
Transform1064 = x3d.Transform()
""" Empty Transform """
Shape1065 = x3d.Shape()
Shape1065.USE = "HAnimJointShape"

Transform1064.children.append(Shape1065)

Transform1063.children.append(Transform1064)

HAnimSegment1062.children.append(Transform1063)
Shape1066 = x3d.Shape()
LineSet1067 = x3d.LineSet()
LineSet1067.vertexCount = [2]
Coordinate1068 = x3d.Coordinate()

LineSet1067.coord = Coordinate1068
""" from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 vertices 2"""
ColorRGBA1069 = x3d.ColorRGBA()
ColorRGBA1069.USE = "HAnimSegmentLineColorRGBA"

LineSet1067.color = ColorRGBA1069

Shape1066.geometry = LineSet1067

HAnimSegment1062.children.append(Shape1066)
HAnimSite1070 = x3d.HAnimSite()
HAnimSite1070.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite1070.name = "r_carpal_distal_phalanx_3_tip"
TouchSensor1071 = x3d.TouchSensor()
TouchSensor1071.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1070.children.append(TouchSensor1071)
Shape1072 = x3d.Shape()
Shape1072.USE = "HAnimSiteShape"

HAnimSite1070.children.append(Shape1072)

HAnimSegment1062.children.append(HAnimSite1070)

HAnimJoint1061.children.append(HAnimSegment1062)
HAnimJoint1073 = x3d.HAnimJoint()
HAnimJoint1073.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1073.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1073.center = [-0.1939,0.7042,-0.0432]

HAnimJoint1061.children.append(HAnimJoint1073)

HAnimJoint1052.children.append(HAnimJoint1061)

HAnimJoint1043.children.append(HAnimJoint1052)

HAnimJoint953.children.append(HAnimJoint1043)
HAnimJoint1074 = x3d.HAnimJoint()
HAnimJoint1074.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1074.name = "r_carpometacarpal_4"
HAnimJoint1074.center = [-0.1951,0.8049,-0.0732]
HAnimSegment1075 = x3d.HAnimSegment()
HAnimSegment1075.DEF = "hanim_r_metacarpal_4"
HAnimSegment1075.name = "r_metacarpal_4"
Transform1076 = x3d.Transform()
Transform1076.translation = [-0.1951,0.8049,-0.0732]
Transform1077 = x3d.Transform()
""" Empty Transform """
Shape1078 = x3d.Shape()
Shape1078.USE = "HAnimJointShape"

Transform1077.children.append(Shape1078)

Transform1076.children.append(Transform1077)

HAnimSegment1075.children.append(Transform1076)
Shape1079 = x3d.Shape()
LineSet1080 = x3d.LineSet()
LineSet1080.vertexCount = [2]
Coordinate1081 = x3d.Coordinate()

LineSet1080.coord = Coordinate1081
""" from r_carpometacarpal_4 to r_metacarpophalangeal_4 vertices 2"""
ColorRGBA1082 = x3d.ColorRGBA()
ColorRGBA1082.USE = "HAnimSegmentLineColorRGBA"

LineSet1080.color = ColorRGBA1082

Shape1079.geometry = LineSet1080

HAnimSegment1075.children.append(Shape1079)

HAnimJoint1074.children.append(HAnimSegment1075)
HAnimJoint1083 = x3d.HAnimJoint()
HAnimJoint1083.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1083.name = "r_metacarpophalangeal_4"
HAnimJoint1083.center = [-0.1951,0.7845,-0.0732]
HAnimSegment1084 = x3d.HAnimSegment()
HAnimSegment1084.DEF = "hanim_r_carpal_proximal_phalanx_4"
HAnimSegment1084.name = "r_carpal_proximal_phalanx_4"
Transform1085 = x3d.Transform()
Transform1085.translation = [-0.1951,0.7845,-0.0732]
Transform1086 = x3d.Transform()
""" Empty Transform """
Shape1087 = x3d.Shape()
Shape1087.USE = "HAnimJointShape"

Transform1086.children.append(Shape1087)

Transform1085.children.append(Transform1086)

HAnimSegment1084.children.append(Transform1085)
Shape1088 = x3d.Shape()
LineSet1089 = x3d.LineSet()
LineSet1089.vertexCount = [2]
Coordinate1090 = x3d.Coordinate()

LineSet1089.coord = Coordinate1090
""" from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA1091 = x3d.ColorRGBA()
ColorRGBA1091.USE = "HAnimSegmentLineColorRGBA"

LineSet1089.color = ColorRGBA1091

Shape1088.geometry = LineSet1089

HAnimSegment1084.children.append(Shape1088)

HAnimJoint1083.children.append(HAnimSegment1084)
HAnimJoint1092 = x3d.HAnimJoint()
HAnimJoint1092.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1092.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1092.center = [-0.1920,0.7318,-0.0716]
HAnimSegment1093 = x3d.HAnimSegment()
HAnimSegment1093.DEF = "hanim_r_carpal_middle_phalanx_4"
HAnimSegment1093.name = "r_carpal_middle_phalanx_4"
Transform1094 = x3d.Transform()
Transform1094.translation = [-0.1920,0.7318,-0.0716]
Transform1095 = x3d.Transform()
""" Empty Transform """
Shape1096 = x3d.Shape()
Shape1096.USE = "HAnimJointShape"

Transform1095.children.append(Shape1096)

Transform1094.children.append(Transform1095)

HAnimSegment1093.children.append(Transform1094)
Shape1097 = x3d.Shape()
LineSet1098 = x3d.LineSet()
LineSet1098.vertexCount = [2]
Coordinate1099 = x3d.Coordinate()

LineSet1098.coord = Coordinate1099
""" from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 vertices 2"""
ColorRGBA1100 = x3d.ColorRGBA()
ColorRGBA1100.USE = "HAnimSegmentLineColorRGBA"

LineSet1098.color = ColorRGBA1100

Shape1097.geometry = LineSet1098

HAnimSegment1093.children.append(Shape1097)
HAnimSite1101 = x3d.HAnimSite()
HAnimSite1101.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite1101.name = "r_carpal_distal_phalanx_4_tip"
TouchSensor1102 = x3d.TouchSensor()
TouchSensor1102.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1101.children.append(TouchSensor1102)
Shape1103 = x3d.Shape()
Shape1103.USE = "HAnimSiteShape"

HAnimSite1101.children.append(Shape1103)

HAnimSegment1093.children.append(HAnimSite1101)

HAnimJoint1092.children.append(HAnimSegment1093)
HAnimJoint1104 = x3d.HAnimJoint()
HAnimJoint1104.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1104.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1104.center = [-0.1908,0.7077,-0.0706]

HAnimJoint1092.children.append(HAnimJoint1104)

HAnimJoint1083.children.append(HAnimJoint1092)

HAnimJoint1074.children.append(HAnimJoint1083)

HAnimJoint953.children.append(HAnimJoint1074)
HAnimJoint1105 = x3d.HAnimJoint()
HAnimJoint1105.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1105.name = "r_carpometacarpal_5"
HAnimJoint1105.center = [-0.1926,0.8096,-0.0975]
HAnimSegment1106 = x3d.HAnimSegment()
HAnimSegment1106.DEF = "hanim_r_metacarpal_5"
HAnimSegment1106.name = "r_metacarpal_5"
Transform1107 = x3d.Transform()
Transform1107.translation = [-0.1926,0.8096,-0.0975]
Transform1108 = x3d.Transform()
""" Empty Transform """
Shape1109 = x3d.Shape()
Shape1109.USE = "HAnimJointShape"

Transform1108.children.append(Shape1109)

Transform1107.children.append(Transform1108)

HAnimSegment1106.children.append(Transform1107)
Shape1110 = x3d.Shape()
LineSet1111 = x3d.LineSet()
LineSet1111.vertexCount = [2]
Coordinate1112 = x3d.Coordinate()

LineSet1111.coord = Coordinate1112
""" from r_carpometacarpal_5 to r_metacarpophalangeal_5 vertices 2"""
ColorRGBA1113 = x3d.ColorRGBA()
ColorRGBA1113.USE = "HAnimSegmentLineColorRGBA"

LineSet1111.color = ColorRGBA1113

Shape1110.geometry = LineSet1111

HAnimSegment1106.children.append(Shape1110)

HAnimJoint1105.children.append(HAnimSegment1106)
HAnimJoint1114 = x3d.HAnimJoint()
HAnimJoint1114.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1114.name = "r_metacarpophalangeal_5"
HAnimJoint1114.center = [-0.1926,0.7896,-0.0975]
HAnimSegment1115 = x3d.HAnimSegment()
HAnimSegment1115.DEF = "hanim_r_carpal_proximal_phalanx_5"
HAnimSegment1115.name = "r_carpal_proximal_phalanx_5"
Transform1116 = x3d.Transform()
Transform1116.translation = [-0.1926,0.7896,-0.0975]
Transform1117 = x3d.Transform()
""" Empty Transform """
Shape1118 = x3d.Shape()
Shape1118.USE = "HAnimJointShape"

Transform1117.children.append(Shape1118)

Transform1116.children.append(Transform1117)

HAnimSegment1115.children.append(Transform1116)
Shape1119 = x3d.Shape()
LineSet1120 = x3d.LineSet()
LineSet1120.vertexCount = [2]
Coordinate1121 = x3d.Coordinate()

LineSet1120.coord = Coordinate1121
""" from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA1122 = x3d.ColorRGBA()
ColorRGBA1122.USE = "HAnimSegmentLineColorRGBA"

LineSet1120.color = ColorRGBA1122

Shape1119.geometry = LineSet1120

HAnimSegment1115.children.append(Shape1119)

HAnimJoint1114.children.append(HAnimSegment1115)
HAnimJoint1123 = x3d.HAnimJoint()
HAnimJoint1123.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1123.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1123.center = [-0.1902,0.7483,-0.0963]
HAnimSegment1124 = x3d.HAnimSegment()
HAnimSegment1124.DEF = "hanim_r_carpal_middle_phalanx_5"
HAnimSegment1124.name = "r_carpal_middle_phalanx_5"
Transform1125 = x3d.Transform()
Transform1125.translation = [-0.1902,0.7483,-0.0963]
Transform1126 = x3d.Transform()
""" Empty Transform """
Shape1127 = x3d.Shape()
Shape1127.USE = "HAnimJointShape"

Transform1126.children.append(Shape1127)

Transform1125.children.append(Transform1126)

HAnimSegment1124.children.append(Transform1125)
Shape1128 = x3d.Shape()
LineSet1129 = x3d.LineSet()
LineSet1129.vertexCount = [2]
Coordinate1130 = x3d.Coordinate()

LineSet1129.coord = Coordinate1130
""" from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 vertices 2"""
ColorRGBA1131 = x3d.ColorRGBA()
ColorRGBA1131.USE = "HAnimSegmentLineColorRGBA"

LineSet1129.color = ColorRGBA1131

Shape1128.geometry = LineSet1129

HAnimSegment1124.children.append(Shape1128)
HAnimSite1132 = x3d.HAnimSite()
HAnimSite1132.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite1132.name = "r_carpal_distal_phalanx_5_tip"
TouchSensor1133 = x3d.TouchSensor()
TouchSensor1133.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1132.children.append(TouchSensor1133)
Shape1134 = x3d.Shape()
Shape1134.USE = "HAnimSiteShape"

HAnimSite1132.children.append(Shape1134)

HAnimSegment1124.children.append(HAnimSite1132)

HAnimJoint1123.children.append(HAnimSegment1124)
HAnimJoint1135 = x3d.HAnimJoint()
HAnimJoint1135.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1135.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1135.center = [-0.1908,0.7540,-0.0960]

HAnimJoint1123.children.append(HAnimJoint1135)

HAnimJoint1114.children.append(HAnimJoint1123)

HAnimJoint1105.children.append(HAnimJoint1114)

HAnimJoint953.children.append(HAnimJoint1105)

HAnimJoint941.children.append(HAnimJoint953)

HAnimJoint920.children.append(HAnimJoint941)

HAnimJoint905.children.append(HAnimJoint920)

HAnimJoint896.children.append(HAnimJoint905)

HAnimJoint452.children.append(HAnimJoint896)

HAnimJoint437.children.append(HAnimJoint452)

HAnimJoint428.children.append(HAnimJoint437)

HAnimJoint419.children.append(HAnimJoint428)

HAnimJoint410.children.append(HAnimJoint419)

HAnimJoint398.children.append(HAnimJoint410)

HAnimJoint377.children.append(HAnimJoint398)

HAnimJoint368.children.append(HAnimJoint377)

HAnimJoint359.children.append(HAnimJoint368)

HAnimJoint344.children.append(HAnimJoint359)

HAnimJoint332.children.append(HAnimJoint344)

HAnimJoint323.children.append(HAnimJoint332)

HAnimJoint314.children.append(HAnimJoint323)

HAnimJoint305.children.append(HAnimJoint314)

HAnimJoint287.children.append(HAnimJoint305)

HAnimJoint278.children.append(HAnimJoint287)

HAnimJoint269.children.append(HAnimJoint278)

HAnimJoint52.children.append(HAnimJoint269)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimJoint1136 = x3d.HAnimJoint()
HAnimJoint1136.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint1136)
HAnimJoint1137 = x3d.HAnimJoint()
HAnimJoint1137.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint1137)
HAnimJoint1138 = x3d.HAnimJoint()
HAnimJoint1138.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint1138)
HAnimJoint1139 = x3d.HAnimJoint()
HAnimJoint1139.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint1139)
HAnimJoint1140 = x3d.HAnimJoint()
HAnimJoint1140.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1140)
HAnimJoint1141 = x3d.HAnimJoint()
HAnimJoint1141.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1141)
HAnimJoint1142 = x3d.HAnimJoint()
HAnimJoint1142.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1142)
HAnimJoint1143 = x3d.HAnimJoint()
HAnimJoint1143.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1143)
HAnimJoint1144 = x3d.HAnimJoint()
HAnimJoint1144.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint1144)
HAnimJoint1145 = x3d.HAnimJoint()
HAnimJoint1145.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint1145)
HAnimJoint1146 = x3d.HAnimJoint()
HAnimJoint1146.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1146)
HAnimJoint1147 = x3d.HAnimJoint()
HAnimJoint1147.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1147)
HAnimJoint1148 = x3d.HAnimJoint()
HAnimJoint1148.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1148)
HAnimJoint1149 = x3d.HAnimJoint()
HAnimJoint1149.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1149)
HAnimJoint1150 = x3d.HAnimJoint()
HAnimJoint1150.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint1150)
HAnimJoint1151 = x3d.HAnimJoint()
HAnimJoint1151.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint1151)
HAnimJoint1152 = x3d.HAnimJoint()
HAnimJoint1152.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint1152)
HAnimJoint1153 = x3d.HAnimJoint()
HAnimJoint1153.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint1153)
HAnimJoint1154 = x3d.HAnimJoint()
HAnimJoint1154.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint1154)
HAnimJoint1155 = x3d.HAnimJoint()
HAnimJoint1155.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint1155)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint1156)
HAnimJoint1157 = x3d.HAnimJoint()
HAnimJoint1157.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint1157)
HAnimJoint1158 = x3d.HAnimJoint()
HAnimJoint1158.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint1158)
HAnimJoint1159 = x3d.HAnimJoint()
HAnimJoint1159.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint1159)
HAnimJoint1160 = x3d.HAnimJoint()
HAnimJoint1160.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint1160)
HAnimJoint1161 = x3d.HAnimJoint()
HAnimJoint1161.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint1161)
HAnimJoint1162 = x3d.HAnimJoint()
HAnimJoint1162.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint1162)
HAnimJoint1163 = x3d.HAnimJoint()
HAnimJoint1163.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint1163)
HAnimJoint1164 = x3d.HAnimJoint()
HAnimJoint1164.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint1164)
HAnimJoint1165 = x3d.HAnimJoint()
HAnimJoint1165.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint1165)
HAnimJoint1166 = x3d.HAnimJoint()
HAnimJoint1166.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint1166)
HAnimJoint1167 = x3d.HAnimJoint()
HAnimJoint1167.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint1167)
HAnimJoint1168 = x3d.HAnimJoint()
HAnimJoint1168.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint1168)
HAnimJoint1169 = x3d.HAnimJoint()
HAnimJoint1169.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint1169)
HAnimJoint1170 = x3d.HAnimJoint()
HAnimJoint1170.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint1170)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint1171)
HAnimJoint1172 = x3d.HAnimJoint()
HAnimJoint1172.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint1172)
HAnimJoint1173 = x3d.HAnimJoint()
HAnimJoint1173.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint1173)
HAnimJoint1174 = x3d.HAnimJoint()
HAnimJoint1174.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint1174)
HAnimJoint1175 = x3d.HAnimJoint()
HAnimJoint1175.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1175)
HAnimJoint1176 = x3d.HAnimJoint()
HAnimJoint1176.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1176)
HAnimJoint1177 = x3d.HAnimJoint()
HAnimJoint1177.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1177)
HAnimJoint1178 = x3d.HAnimJoint()
HAnimJoint1178.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1178)
HAnimJoint1179 = x3d.HAnimJoint()
HAnimJoint1179.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1179)
HAnimJoint1180 = x3d.HAnimJoint()
HAnimJoint1180.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1180)
HAnimJoint1181 = x3d.HAnimJoint()
HAnimJoint1181.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint1181)
HAnimJoint1182 = x3d.HAnimJoint()
HAnimJoint1182.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1182)
HAnimJoint1183 = x3d.HAnimJoint()
HAnimJoint1183.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1183)
HAnimJoint1184 = x3d.HAnimJoint()
HAnimJoint1184.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1184)
HAnimJoint1185 = x3d.HAnimJoint()
HAnimJoint1185.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1185)
HAnimJoint1186 = x3d.HAnimJoint()
HAnimJoint1186.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1186)
HAnimJoint1187 = x3d.HAnimJoint()
HAnimJoint1187.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1187)
HAnimJoint1188 = x3d.HAnimJoint()
HAnimJoint1188.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1188)
HAnimJoint1189 = x3d.HAnimJoint()
HAnimJoint1189.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1189)
HAnimJoint1190 = x3d.HAnimJoint()
HAnimJoint1190.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1190)
HAnimJoint1191 = x3d.HAnimJoint()
HAnimJoint1191.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1191)
HAnimJoint1192 = x3d.HAnimJoint()
HAnimJoint1192.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1192)
HAnimJoint1193 = x3d.HAnimJoint()
HAnimJoint1193.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1193)
HAnimJoint1194 = x3d.HAnimJoint()
HAnimJoint1194.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1194)
HAnimJoint1195 = x3d.HAnimJoint()
HAnimJoint1195.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1195)
HAnimJoint1196 = x3d.HAnimJoint()
HAnimJoint1196.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1196)
HAnimJoint1197 = x3d.HAnimJoint()
HAnimJoint1197.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1197)
HAnimJoint1198 = x3d.HAnimJoint()
HAnimJoint1198.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1198)
HAnimJoint1199 = x3d.HAnimJoint()
HAnimJoint1199.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1199)
HAnimJoint1200 = x3d.HAnimJoint()
HAnimJoint1200.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1200)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1201)
HAnimJoint1202 = x3d.HAnimJoint()
HAnimJoint1202.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1202)
HAnimJoint1203 = x3d.HAnimJoint()
HAnimJoint1203.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1203)
HAnimJoint1204 = x3d.HAnimJoint()
HAnimJoint1204.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1204)
HAnimJoint1205 = x3d.HAnimJoint()
HAnimJoint1205.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1205)
HAnimJoint1206 = x3d.HAnimJoint()
HAnimJoint1206.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1206)
HAnimJoint1207 = x3d.HAnimJoint()
HAnimJoint1207.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1207)
HAnimJoint1208 = x3d.HAnimJoint()
HAnimJoint1208.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1208)
HAnimJoint1209 = x3d.HAnimJoint()
HAnimJoint1209.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1209)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1210)
HAnimJoint1211 = x3d.HAnimJoint()
HAnimJoint1211.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1211)
HAnimJoint1212 = x3d.HAnimJoint()
HAnimJoint1212.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1212)
HAnimJoint1213 = x3d.HAnimJoint()
HAnimJoint1213.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1213)
HAnimJoint1214 = x3d.HAnimJoint()
HAnimJoint1214.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1214)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1215)
HAnimJoint1216 = x3d.HAnimJoint()
HAnimJoint1216.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1216)
HAnimJoint1217 = x3d.HAnimJoint()
HAnimJoint1217.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1217)
HAnimJoint1218 = x3d.HAnimJoint()
HAnimJoint1218.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1218)
HAnimJoint1219 = x3d.HAnimJoint()
HAnimJoint1219.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1219)
HAnimJoint1220 = x3d.HAnimJoint()
HAnimJoint1220.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1220)
HAnimJoint1221 = x3d.HAnimJoint()
HAnimJoint1221.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1221)
HAnimJoint1222 = x3d.HAnimJoint()
HAnimJoint1222.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1222)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1223)
HAnimJoint1224 = x3d.HAnimJoint()
HAnimJoint1224.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1224)
HAnimJoint1225 = x3d.HAnimJoint()
HAnimJoint1225.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1225)
HAnimJoint1226 = x3d.HAnimJoint()
HAnimJoint1226.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1226)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1227)
HAnimJoint1228 = x3d.HAnimJoint()
HAnimJoint1228.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1228)
HAnimJoint1229 = x3d.HAnimJoint()
HAnimJoint1229.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1229)
HAnimSegment1230 = x3d.HAnimSegment()
HAnimSegment1230.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment1230)
HAnimSegment1231 = x3d.HAnimSegment()
HAnimSegment1231.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment1231)
HAnimSegment1232 = x3d.HAnimSegment()
HAnimSegment1232.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1232)
HAnimSegment1233 = x3d.HAnimSegment()
HAnimSegment1233.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment1233)
HAnimSegment1234 = x3d.HAnimSegment()
HAnimSegment1234.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment1234)
HAnimSegment1235 = x3d.HAnimSegment()
HAnimSegment1235.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1235)
HAnimSegment1236 = x3d.HAnimSegment()
HAnimSegment1236.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1236)
HAnimSegment1237 = x3d.HAnimSegment()
HAnimSegment1237.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1237)
HAnimSegment1238 = x3d.HAnimSegment()
HAnimSegment1238.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment1238)
HAnimSegment1239 = x3d.HAnimSegment()
HAnimSegment1239.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment1239)
HAnimSegment1240 = x3d.HAnimSegment()
HAnimSegment1240.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1240)
HAnimSegment1241 = x3d.HAnimSegment()
HAnimSegment1241.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1241)
HAnimSegment1242 = x3d.HAnimSegment()
HAnimSegment1242.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment1242)
HAnimSegment1243 = x3d.HAnimSegment()
HAnimSegment1243.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment1243)
HAnimSegment1244 = x3d.HAnimSegment()
HAnimSegment1244.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment1244)
HAnimSegment1245 = x3d.HAnimSegment()
HAnimSegment1245.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment1245)
HAnimSegment1246 = x3d.HAnimSegment()
HAnimSegment1246.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment1246)
HAnimSegment1247 = x3d.HAnimSegment()
HAnimSegment1247.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment1247)
HAnimSegment1248 = x3d.HAnimSegment()
HAnimSegment1248.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment1248)
HAnimSegment1249 = x3d.HAnimSegment()
HAnimSegment1249.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment1249)
HAnimSegment1250 = x3d.HAnimSegment()
HAnimSegment1250.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment1250)
HAnimSegment1251 = x3d.HAnimSegment()
HAnimSegment1251.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment1251)
HAnimSegment1252 = x3d.HAnimSegment()
HAnimSegment1252.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment1252)
HAnimSegment1253 = x3d.HAnimSegment()
HAnimSegment1253.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment1253)
HAnimSegment1254 = x3d.HAnimSegment()
HAnimSegment1254.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment1254)
HAnimSegment1255 = x3d.HAnimSegment()
HAnimSegment1255.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment1255)
HAnimSegment1256 = x3d.HAnimSegment()
HAnimSegment1256.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment1256)
HAnimSegment1257 = x3d.HAnimSegment()
HAnimSegment1257.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment1257)
HAnimSegment1258 = x3d.HAnimSegment()
HAnimSegment1258.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment1258)
HAnimSegment1259 = x3d.HAnimSegment()
HAnimSegment1259.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment1259)
HAnimSegment1260 = x3d.HAnimSegment()
HAnimSegment1260.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment1260)
HAnimSegment1261 = x3d.HAnimSegment()
HAnimSegment1261.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment1261)
HAnimSegment1262 = x3d.HAnimSegment()
HAnimSegment1262.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment1262)
HAnimSegment1263 = x3d.HAnimSegment()
HAnimSegment1263.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment1263)
HAnimSegment1264 = x3d.HAnimSegment()
HAnimSegment1264.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment1264)
HAnimSegment1265 = x3d.HAnimSegment()
HAnimSegment1265.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment1265)
HAnimSegment1266 = x3d.HAnimSegment()
HAnimSegment1266.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment1266)
HAnimSegment1267 = x3d.HAnimSegment()
HAnimSegment1267.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1267)
HAnimSegment1268 = x3d.HAnimSegment()
HAnimSegment1268.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1268)
HAnimSegment1269 = x3d.HAnimSegment()
HAnimSegment1269.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1269)
HAnimSegment1270 = x3d.HAnimSegment()
HAnimSegment1270.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1270)
HAnimSegment1271 = x3d.HAnimSegment()
HAnimSegment1271.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1271)
HAnimSegment1272 = x3d.HAnimSegment()
HAnimSegment1272.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1272)
HAnimSegment1273 = x3d.HAnimSegment()
HAnimSegment1273.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1273)
HAnimSegment1274 = x3d.HAnimSegment()
HAnimSegment1274.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1274)
HAnimSegment1275 = x3d.HAnimSegment()
HAnimSegment1275.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1275)
HAnimSegment1276 = x3d.HAnimSegment()
HAnimSegment1276.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1276)
HAnimSegment1277 = x3d.HAnimSegment()
HAnimSegment1277.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1277)
HAnimSegment1278 = x3d.HAnimSegment()
HAnimSegment1278.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1278)
HAnimSegment1279 = x3d.HAnimSegment()
HAnimSegment1279.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1279)
HAnimSegment1280 = x3d.HAnimSegment()
HAnimSegment1280.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1280)
HAnimSegment1281 = x3d.HAnimSegment()
HAnimSegment1281.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1281)
HAnimSegment1282 = x3d.HAnimSegment()
HAnimSegment1282.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1282)
HAnimSegment1283 = x3d.HAnimSegment()
HAnimSegment1283.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1283)
HAnimSegment1284 = x3d.HAnimSegment()
HAnimSegment1284.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1284)
HAnimSegment1285 = x3d.HAnimSegment()
HAnimSegment1285.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1285)
HAnimSegment1286 = x3d.HAnimSegment()
HAnimSegment1286.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1286)
HAnimSegment1287 = x3d.HAnimSegment()
HAnimSegment1287.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1287)
HAnimSegment1288 = x3d.HAnimSegment()
HAnimSegment1288.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1288)
HAnimSegment1289 = x3d.HAnimSegment()
HAnimSegment1289.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1289)
HAnimSegment1290 = x3d.HAnimSegment()
HAnimSegment1290.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1290)
HAnimSegment1291 = x3d.HAnimSegment()
HAnimSegment1291.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1291)
HAnimSegment1292 = x3d.HAnimSegment()
HAnimSegment1292.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1292)
HAnimSegment1293 = x3d.HAnimSegment()
HAnimSegment1293.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1293)
HAnimSegment1294 = x3d.HAnimSegment()
HAnimSegment1294.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1294)
HAnimSegment1295 = x3d.HAnimSegment()
HAnimSegment1295.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1295)
HAnimSegment1296 = x3d.HAnimSegment()
HAnimSegment1296.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1296)
HAnimSegment1297 = x3d.HAnimSegment()
HAnimSegment1297.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1297)
HAnimSegment1298 = x3d.HAnimSegment()
HAnimSegment1298.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1298)
HAnimSegment1299 = x3d.HAnimSegment()
HAnimSegment1299.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1299)
HAnimSegment1300 = x3d.HAnimSegment()
HAnimSegment1300.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1300)
HAnimSegment1301 = x3d.HAnimSegment()
HAnimSegment1301.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1301)
HAnimSegment1302 = x3d.HAnimSegment()
HAnimSegment1302.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1302)
HAnimSegment1303 = x3d.HAnimSegment()
HAnimSegment1303.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1303)
HAnimSegment1304 = x3d.HAnimSegment()
HAnimSegment1304.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1304)
HAnimSite1305 = x3d.HAnimSite()
HAnimSite1305.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite1305)
HAnimSite1306 = x3d.HAnimSite()
HAnimSite1306.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite1306)
HAnimSite1307 = x3d.HAnimSite()
HAnimSite1307.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1307)
HAnimSite1308 = x3d.HAnimSite()
HAnimSite1308.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1308)
HAnimSite1309 = x3d.HAnimSite()
HAnimSite1309.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1309)
HAnimSite1310 = x3d.HAnimSite()
HAnimSite1310.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1310)
HAnimSite1311 = x3d.HAnimSite()
HAnimSite1311.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1311)
HAnimSite1312 = x3d.HAnimSite()
HAnimSite1312.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1312)
HAnimSite1313 = x3d.HAnimSite()
HAnimSite1313.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1313)
HAnimSite1314 = x3d.HAnimSite()
HAnimSite1314.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1314)
HAnimSite1315 = x3d.HAnimSite()
HAnimSite1315.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite1315)
HAnimSite1316 = x3d.HAnimSite()
HAnimSite1316.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1316)
HAnimSite1317 = x3d.HAnimSite()
HAnimSite1317.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1317)
HAnimSite1318 = x3d.HAnimSite()
HAnimSite1318.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1318)
HAnimSite1319 = x3d.HAnimSite()
HAnimSite1319.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1319)
HAnimSite1320 = x3d.HAnimSite()
HAnimSite1320.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1320)
HAnimSite1321 = x3d.HAnimSite()
HAnimSite1321.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1321)
HAnimSite1322 = x3d.HAnimSite()
HAnimSite1322.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1322)
HAnimSite1323 = x3d.HAnimSite()
HAnimSite1323.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1323)
HAnimSite1324 = x3d.HAnimSite()
HAnimSite1324.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1324)
HAnimSite1325 = x3d.HAnimSite()
HAnimSite1325.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1325)
HAnimSite1326 = x3d.HAnimSite()
HAnimSite1326.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1326)
HAnimSite1327 = x3d.HAnimSite()
HAnimSite1327.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1327)
HAnimSite1328 = x3d.HAnimSite()
HAnimSite1328.USE = "hanim_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1328)
HAnimSite1329 = x3d.HAnimSite()
HAnimSite1329.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1329)
HAnimSite1330 = x3d.HAnimSite()
HAnimSite1330.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1330)
HAnimSite1331 = x3d.HAnimSite()
HAnimSite1331.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1331)
HAnimSite1332 = x3d.HAnimSite()
HAnimSite1332.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1332)
HAnimSite1333 = x3d.HAnimSite()
HAnimSite1333.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1333)
HAnimSite1334 = x3d.HAnimSite()
HAnimSite1334.USE = "hanim_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1334)
HAnimSite1335 = x3d.HAnimSite()
HAnimSite1335.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1335)
HAnimSite1336 = x3d.HAnimSite()
HAnimSite1336.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1336)
HAnimSite1337 = x3d.HAnimSite()
HAnimSite1337.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1337)
HAnimSite1338 = x3d.HAnimSite()
HAnimSite1338.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1338)
HAnimSite1339 = x3d.HAnimSite()
HAnimSite1339.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1339)
HAnimSite1340 = x3d.HAnimSite()
HAnimSite1340.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1340)
HAnimSite1341 = x3d.HAnimSite()
HAnimSite1341.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite1341)
HAnimSite1342 = x3d.HAnimSite()
HAnimSite1342.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1342)
HAnimSite1343 = x3d.HAnimSite()
HAnimSite1343.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1343)
HAnimSite1344 = x3d.HAnimSite()
HAnimSite1344.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1344)
HAnimSite1345 = x3d.HAnimSite()
HAnimSite1345.USE = "hanim_mesosternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1345)
HAnimSite1346 = x3d.HAnimSite()
HAnimSite1346.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1346)
HAnimSite1347 = x3d.HAnimSite()
HAnimSite1347.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1347)
HAnimSite1348 = x3d.HAnimSite()
HAnimSite1348.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1348)
HAnimSite1349 = x3d.HAnimSite()
HAnimSite1349.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1349)
HAnimSite1350 = x3d.HAnimSite()
HAnimSite1350.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1350)
HAnimSite1351 = x3d.HAnimSite()
HAnimSite1351.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1351)
HAnimSite1352 = x3d.HAnimSite()
HAnimSite1352.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1352)
HAnimSite1353 = x3d.HAnimSite()
HAnimSite1353.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1353)
HAnimSite1354 = x3d.HAnimSite()
HAnimSite1354.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1354)
HAnimSite1355 = x3d.HAnimSite()
HAnimSite1355.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1355)
HAnimSite1356 = x3d.HAnimSite()
HAnimSite1356.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1356)
HAnimSite1357 = x3d.HAnimSite()
HAnimSite1357.USE = "hanim_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1357)
HAnimSite1358 = x3d.HAnimSite()
HAnimSite1358.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1358)
HAnimSite1359 = x3d.HAnimSite()
HAnimSite1359.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1359)
HAnimSite1360 = x3d.HAnimSite()
HAnimSite1360.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1360)
HAnimSite1361 = x3d.HAnimSite()
HAnimSite1361.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1361)
HAnimSite1362 = x3d.HAnimSite()
HAnimSite1362.USE = "hanim_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1362)
HAnimSite1363 = x3d.HAnimSite()
HAnimSite1363.USE = "hanim_adams_apple_pt"

HAnimHumanoid43.sites.append(HAnimSite1363)
HAnimSite1364 = x3d.HAnimSite()
HAnimSite1364.USE = "hanim_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite1364)
HAnimSite1365 = x3d.HAnimSite()
HAnimSite1365.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1365)
HAnimSite1366 = x3d.HAnimSite()
HAnimSite1366.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1366)
HAnimSite1367 = x3d.HAnimSite()
HAnimSite1367.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1367)
HAnimSite1368 = x3d.HAnimSite()
HAnimSite1368.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite1368)
HAnimSite1369 = x3d.HAnimSite()
HAnimSite1369.USE = "hanim_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite1369)
HAnimSite1370 = x3d.HAnimSite()
HAnimSite1370.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1370)
HAnimSite1371 = x3d.HAnimSite()
HAnimSite1371.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1371)
HAnimSite1372 = x3d.HAnimSite()
HAnimSite1372.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1372)
HAnimSite1373 = x3d.HAnimSite()
HAnimSite1373.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite1373)
HAnimSite1374 = x3d.HAnimSite()
HAnimSite1374.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite1374)
HAnimSite1375 = x3d.HAnimSite()
HAnimSite1375.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1375)
HAnimSite1376 = x3d.HAnimSite()
HAnimSite1376.USE = "hanim_menton_pt"

HAnimHumanoid43.sites.append(HAnimSite1376)
HAnimSite1377 = x3d.HAnimSite()
HAnimSite1377.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1377)
HAnimSite1378 = x3d.HAnimSite()
HAnimSite1378.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite1378)
HAnimSite1379 = x3d.HAnimSite()
HAnimSite1379.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1379)
HAnimSite1380 = x3d.HAnimSite()
HAnimSite1380.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1380)
HAnimSite1381 = x3d.HAnimSite()
HAnimSite1381.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1381)
HAnimSite1382 = x3d.HAnimSite()
HAnimSite1382.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1382)
HAnimSite1383 = x3d.HAnimSite()
HAnimSite1383.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1383)
HAnimSite1384 = x3d.HAnimSite()
HAnimSite1384.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1384)
HAnimSite1385 = x3d.HAnimSite()
HAnimSite1385.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1385)
HAnimSite1386 = x3d.HAnimSite()
HAnimSite1386.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1386)
HAnimSite1387 = x3d.HAnimSite()
HAnimSite1387.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1387)
HAnimSite1388 = x3d.HAnimSite()
HAnimSite1388.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1388)
HAnimSite1389 = x3d.HAnimSite()
HAnimSite1389.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1389)
HAnimSite1390 = x3d.HAnimSite()
HAnimSite1390.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1390)
HAnimSite1391 = x3d.HAnimSite()
HAnimSite1391.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1391)
HAnimSite1392 = x3d.HAnimSite()
HAnimSite1392.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1392)
HAnimSite1393 = x3d.HAnimSite()
HAnimSite1393.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1393)
HAnimSite1394 = x3d.HAnimSite()
HAnimSite1394.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1394)
HAnimSite1395 = x3d.HAnimSite()
HAnimSite1395.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1395)
HAnimSite1396 = x3d.HAnimSite()
HAnimSite1396.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1396)
HAnimSite1397 = x3d.HAnimSite()
HAnimSite1397.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1397)
HAnimSite1398 = x3d.HAnimSite()
HAnimSite1398.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1398)
HAnimSite1399 = x3d.HAnimSite()
HAnimSite1399.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1399)
HAnimSite1400 = x3d.HAnimSite()
HAnimSite1400.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1400)
HAnimSite1401 = x3d.HAnimSite()
HAnimSite1401.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1401)
HAnimSite1402 = x3d.HAnimSite()
HAnimSite1402.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1402)
HAnimSite1403 = x3d.HAnimSite()
HAnimSite1403.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1403)
HAnimSite1404 = x3d.HAnimSite()
HAnimSite1404.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1404)
HAnimSite1405 = x3d.HAnimSite()
HAnimSite1405.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1405)
HAnimSite1406 = x3d.HAnimSite()
HAnimSite1406.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1406)
HAnimSite1407 = x3d.HAnimSite()
HAnimSite1407.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1407)
HAnimSite1408 = x3d.HAnimSite()
HAnimSite1408.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1408)
HAnimSite1409 = x3d.HAnimSite()
HAnimSite1409.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1409)
HAnimSite1410 = x3d.HAnimSite()
HAnimSite1410.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1410)

Scene11.children.append(HAnimHumanoid43)

X3D0.Scene = Scene11
f = open("Humanoid3_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
