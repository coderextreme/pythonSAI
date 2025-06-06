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
""" from l_talocrural to l_talocalcaneonavicular vertices 2"""
ColorRGBA182 = x3d.ColorRGBA()
ColorRGBA182.USE = "HAnimSegmentLineColorRGBA"

LineSet180.color = ColorRGBA182

Shape179.geometry = LineSet180

HAnimSegment175.children.append(Shape179)
Shape183 = x3d.Shape()
LineSet184 = x3d.LineSet()
LineSet184.vertexCount = [2]
Coordinate185 = x3d.Coordinate()

LineSet184.coord = Coordinate185
""" from l_talocrural to l_calcaneocuboid vertices 2"""
ColorRGBA186 = x3d.ColorRGBA()
ColorRGBA186.USE = "HAnimSegmentLineColorRGBA"

LineSet184.color = ColorRGBA186

Shape183.geometry = LineSet184

HAnimSegment175.children.append(Shape183)

HAnimJoint174.children.append(HAnimSegment175)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.DEF = "hanim_l_talocalcaneonavicular"
HAnimJoint187.name = "l_talocalcaneonavicular"
HAnimJoint187.center = [0.0781,0.0283,-0.0970]
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.DEF = "hanim_l_navicular"
HAnimSegment188.name = "l_navicular"
Transform189 = x3d.Transform()
Transform189.translation = [0.0781,0.0283,-0.0970]
Transform190 = x3d.Transform()
""" Empty Transform """
Shape191 = x3d.Shape()
Shape191.USE = "HAnimJointShape"

Transform190.children.append(Shape191)

Transform189.children.append(Transform190)

HAnimSegment188.children.append(Transform189)
Shape192 = x3d.Shape()
LineSet193 = x3d.LineSet()
LineSet193.vertexCount = [2]
Coordinate194 = x3d.Coordinate()

LineSet193.coord = Coordinate194
""" from l_talocalcaneonavicular to l_cuneonavicular_1 vertices 2"""
ColorRGBA195 = x3d.ColorRGBA()
ColorRGBA195.USE = "HAnimSegmentLineColorRGBA"

LineSet193.color = ColorRGBA195

Shape192.geometry = LineSet193

HAnimSegment188.children.append(Shape192)
Shape196 = x3d.Shape()
LineSet197 = x3d.LineSet()
LineSet197.vertexCount = [2]
Coordinate198 = x3d.Coordinate()

LineSet197.coord = Coordinate198
""" from l_talocalcaneonavicular to l_cuneonavicular_2 vertices 2"""
ColorRGBA199 = x3d.ColorRGBA()
ColorRGBA199.USE = "HAnimSegmentLineColorRGBA"

LineSet197.color = ColorRGBA199

Shape196.geometry = LineSet197

HAnimSegment188.children.append(Shape196)
Shape200 = x3d.Shape()
LineSet201 = x3d.LineSet()
LineSet201.vertexCount = [2]
Coordinate202 = x3d.Coordinate()

LineSet201.coord = Coordinate202
""" from l_talocalcaneonavicular to l_cuneonavicular_3 vertices 2"""
ColorRGBA203 = x3d.ColorRGBA()
ColorRGBA203.USE = "HAnimSegmentLineColorRGBA"

LineSet201.color = ColorRGBA203

Shape200.geometry = LineSet201

HAnimSegment188.children.append(Shape200)

HAnimJoint187.children.append(HAnimSegment188)
HAnimJoint204 = x3d.HAnimJoint()
HAnimJoint204.DEF = "hanim_l_cuneonavicular_1"
HAnimJoint204.name = "l_cuneonavicular_1"
HAnimJoint204.center = [0.0672,0.0235,-0.0835]
HAnimSegment205 = x3d.HAnimSegment()
HAnimSegment205.DEF = "hanim_l_cuneiform_1"
HAnimSegment205.name = "l_cuneiform_1"
Transform206 = x3d.Transform()
Transform206.translation = [0.0672,0.0235,-0.0835]
Transform207 = x3d.Transform()
""" Empty Transform """
Shape208 = x3d.Shape()
Shape208.USE = "HAnimJointShape"

Transform207.children.append(Shape208)

Transform206.children.append(Transform207)

HAnimSegment205.children.append(Transform206)
Shape209 = x3d.Shape()
LineSet210 = x3d.LineSet()
LineSet210.vertexCount = [2]
Coordinate211 = x3d.Coordinate()

LineSet210.coord = Coordinate211
""" from l_cuneonavicular_1 to l_tarsometatarsal_1 vertices 2"""
ColorRGBA212 = x3d.ColorRGBA()
ColorRGBA212.USE = "HAnimSegmentLineColorRGBA"

LineSet210.color = ColorRGBA212

Shape209.geometry = LineSet210

HAnimSegment205.children.append(Shape209)

HAnimJoint204.children.append(HAnimSegment205)
HAnimJoint213 = x3d.HAnimJoint()
HAnimJoint213.DEF = "hanim_l_tarsometatarsal_1"
HAnimJoint213.name = "l_tarsometatarsal_1"
HAnimJoint213.center = [0.0644,0.0147,-0.0577]
HAnimSegment214 = x3d.HAnimSegment()
HAnimSegment214.DEF = "hanim_l_metatarsal_1"
HAnimSegment214.name = "l_metatarsal_1"
Transform215 = x3d.Transform()
Transform215.translation = [0.0644,0.0147,-0.0577]
Transform216 = x3d.Transform()
""" Empty Transform """
Shape217 = x3d.Shape()
Shape217.USE = "HAnimJointShape"

Transform216.children.append(Shape217)

Transform215.children.append(Transform216)

HAnimSegment214.children.append(Transform215)
Shape218 = x3d.Shape()
LineSet219 = x3d.LineSet()
LineSet219.vertexCount = [2]
Coordinate220 = x3d.Coordinate()

LineSet219.coord = Coordinate220
""" from l_tarsometatarsal_1 to l_metatarsophalangeal_1 vertices 2"""
ColorRGBA221 = x3d.ColorRGBA()
ColorRGBA221.USE = "HAnimSegmentLineColorRGBA"

LineSet219.color = ColorRGBA221

Shape218.geometry = LineSet219

HAnimSegment214.children.append(Shape218)
HAnimSite222 = x3d.HAnimSite()
HAnimSite222.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite222.name = "l_metatarsal_phalanx_1_pt"
TouchSensor223 = x3d.TouchSensor()
TouchSensor223.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite222.children.append(TouchSensor223)
Shape224 = x3d.Shape()
Shape224.USE = "HAnimSiteShape"

HAnimSite222.children.append(Shape224)

HAnimSegment214.children.append(HAnimSite222)

HAnimJoint213.children.append(HAnimSegment214)
HAnimJoint225 = x3d.HAnimJoint()
HAnimJoint225.DEF = "hanim_l_metatarsophalangeal_1"
HAnimJoint225.name = "l_metatarsophalangeal_1"
HAnimJoint225.center = [0.0619,0.0059,-0.0083]
HAnimSegment226 = x3d.HAnimSegment()
HAnimSegment226.DEF = "hanim_l_tarsal_proximal_phalanx_1"
HAnimSegment226.name = "l_tarsal_proximal_phalanx_1"
Transform227 = x3d.Transform()
Transform227.translation = [0.0619,0.0059,-0.0083]
Transform228 = x3d.Transform()
""" Empty Transform """
Shape229 = x3d.Shape()
Shape229.USE = "HAnimJointShape"

Transform228.children.append(Shape229)

Transform227.children.append(Transform228)

HAnimSegment226.children.append(Transform227)
Shape230 = x3d.Shape()
LineSet231 = x3d.LineSet()
LineSet231.vertexCount = [2]
Coordinate232 = x3d.Coordinate()

LineSet231.coord = Coordinate232
""" from l_metatarsophalangeal_1 to l_tarsal_interphalangeal_1 vertices 2"""
ColorRGBA233 = x3d.ColorRGBA()
ColorRGBA233.USE = "HAnimSegmentLineColorRGBA"

LineSet231.color = ColorRGBA233

Shape230.geometry = LineSet231

HAnimSegment226.children.append(Shape230)
HAnimSite234 = x3d.HAnimSite()
HAnimSite234.DEF = "hanim_l_tarsal_distal_phalanx_1_tip"
HAnimSite234.name = "l_tarsal_distal_phalanx_1_tip"
TouchSensor235 = x3d.TouchSensor()
TouchSensor235.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite234.children.append(TouchSensor235)
Shape236 = x3d.Shape()
Shape236.USE = "HAnimSiteShape"

HAnimSite234.children.append(Shape236)

HAnimSegment226.children.append(HAnimSite234)

HAnimJoint225.children.append(HAnimSegment226)
HAnimJoint237 = x3d.HAnimJoint()
HAnimJoint237.DEF = "hanim_l_tarsal_interphalangeal_1"
HAnimJoint237.name = "l_tarsal_interphalangeal_1"

HAnimJoint225.children.append(HAnimJoint237)

HAnimJoint213.children.append(HAnimJoint225)

HAnimJoint204.children.append(HAnimJoint213)

HAnimJoint187.children.append(HAnimJoint204)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.DEF = "hanim_l_cuneonavicular_2"
HAnimJoint238.name = "l_cuneonavicular_2"
HAnimJoint238.center = [0.0812,0.0250,-0.0805]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.DEF = "hanim_l_cuneiform_2"
HAnimSegment239.name = "l_cuneiform_2"
Transform240 = x3d.Transform()
Transform240.translation = [0.0812,0.0250,-0.0805]
Transform241 = x3d.Transform()
""" Empty Transform """
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
""" from l_cuneonavicular_2 to l_tarsometatarsal_2 vertices 2"""
ColorRGBA246 = x3d.ColorRGBA()
ColorRGBA246.USE = "HAnimSegmentLineColorRGBA"

LineSet244.color = ColorRGBA246

Shape243.geometry = LineSet244

HAnimSegment239.children.append(Shape243)

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint247 = x3d.HAnimJoint()
HAnimJoint247.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint247.name = "l_tarsometatarsal_2"
HAnimJoint247.center = [0.0800,0.0175,-0.0608]
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.DEF = "hanim_l_metatarsal_2"
HAnimSegment248.name = "l_metatarsal_2"
Transform249 = x3d.Transform()
Transform249.translation = [0.0800,0.0175,-0.0608]
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
""" from l_tarsometatarsal_2 to l_metatarsophalangeal_2 vertices 2"""
ColorRGBA255 = x3d.ColorRGBA()
ColorRGBA255.USE = "HAnimSegmentLineColorRGBA"

LineSet253.color = ColorRGBA255

Shape252.geometry = LineSet253

HAnimSegment248.children.append(Shape252)

HAnimJoint247.children.append(HAnimSegment248)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint256.name = "l_metatarsophalangeal_2"
HAnimJoint256.center = [0.0824,0.0064,-0.0040]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSegment257.name = "l_tarsal_proximal_phalanx_2"
Transform258 = x3d.Transform()
Transform258.translation = [0.0824,0.0064,-0.0040]
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
""" from l_metatarsophalangeal_2 to l_tarsal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA264 = x3d.ColorRGBA()
ColorRGBA264.USE = "HAnimSegmentLineColorRGBA"

LineSet262.color = ColorRGBA264

Shape261.geometry = LineSet262

HAnimSegment257.children.append(Shape261)

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint265 = x3d.HAnimJoint()
HAnimJoint265.DEF = "hanim_l_tarsal_proximal_interphalangeal_2"
HAnimJoint265.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint265.center = [0.0841,0.0041,0.0121]
HAnimSegment266 = x3d.HAnimSegment()
HAnimSegment266.DEF = "hanim_l_tarsal_middle_phalanx_2"
HAnimSegment266.name = "l_tarsal_middle_phalanx_2"
Transform267 = x3d.Transform()
Transform267.translation = [0.0841,0.0041,0.0121]
Transform268 = x3d.Transform()
""" Empty Transform """
Shape269 = x3d.Shape()
Shape269.USE = "HAnimJointShape"

Transform268.children.append(Shape269)

Transform267.children.append(Transform268)

HAnimSegment266.children.append(Transform267)
Shape270 = x3d.Shape()
LineSet271 = x3d.LineSet()
LineSet271.vertexCount = [2]
Coordinate272 = x3d.Coordinate()

LineSet271.coord = Coordinate272
""" from l_tarsal_proximal_interphalangeal_2 to l_tarsal_distal_interphalangeal_2 vertices 2"""
ColorRGBA273 = x3d.ColorRGBA()
ColorRGBA273.USE = "HAnimSegmentLineColorRGBA"

LineSet271.color = ColorRGBA273

Shape270.geometry = LineSet271

HAnimSegment266.children.append(Shape270)
HAnimSite274 = x3d.HAnimSite()
HAnimSite274.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite274.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite274.translation = [0.1195,0.0079,0.1433]
TouchSensor275 = x3d.TouchSensor()
TouchSensor275.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite274.children.append(TouchSensor275)
Shape276 = x3d.Shape()
Shape276.USE = "HAnimSiteShape"

HAnimSite274.children.append(Shape276)

HAnimSegment266.children.append(HAnimSite274)

HAnimJoint265.children.append(HAnimSegment266)
HAnimJoint277 = x3d.HAnimJoint()
HAnimJoint277.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint277.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint277.center = [0.0841,0.0013,0.0216]

HAnimJoint265.children.append(HAnimJoint277)

HAnimJoint256.children.append(HAnimJoint265)

HAnimJoint247.children.append(HAnimJoint256)

HAnimJoint238.children.append(HAnimJoint247)

HAnimJoint187.children.append(HAnimJoint238)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.DEF = "hanim_l_cuneonavicular_3"
HAnimJoint278.name = "l_cuneonavicular_3"
HAnimJoint278.center = [0.0928,0.0248,-0.0821]
HAnimSegment279 = x3d.HAnimSegment()
HAnimSegment279.DEF = "hanim_l_cuneiform_3"
HAnimSegment279.name = "l_cuneiform_3"
Transform280 = x3d.Transform()
Transform280.translation = [0.0928,0.0248,-0.0821]
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
""" from l_cuneonavicular_3 to l_tarsometatarsal_3  vertices 2"""
ColorRGBA286 = x3d.ColorRGBA()
ColorRGBA286.USE = "HAnimSegmentLineColorRGBA"

LineSet284.color = ColorRGBA286

Shape283.geometry = LineSet284

HAnimSegment279.children.append(Shape283)

HAnimJoint278.children.append(HAnimSegment279)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.DEF = "hanim_l_tarsometatarsal_3 "
HAnimJoint287.name = "l_tarsometatarsal_3 "
HAnimSegment288 = x3d.HAnimSegment()
HAnimSegment288.DEF = "hanim_l_metatarsal_3"
HAnimSegment288.name = "l_metatarsal_3"
Transform289 = x3d.Transform()
Transform289.translation = [0.0928,0.0248,-0.0821]
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
""" from l_tarsometatarsal_3  to l_metatarsophalangeal_3 vertices 1"""
ColorRGBA295 = x3d.ColorRGBA()
ColorRGBA295.USE = "HAnimSegmentLineColorRGBA"

LineSet293.color = ColorRGBA295

Shape292.geometry = LineSet293

HAnimSegment288.children.append(Shape292)

HAnimJoint287.children.append(HAnimSegment288)
HAnimJoint296 = x3d.HAnimJoint()
HAnimJoint296.DEF = "hanim_l_metatarsophalangeal_3"
HAnimJoint296.name = "l_metatarsophalangeal_3"
HAnimJoint296.center = [0.0963,0.0065,-0.0065]
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.DEF = "hanim_l_tarsal_proximal_phalanx_3"
HAnimSegment297.name = "l_tarsal_proximal_phalanx_3"
Transform298 = x3d.Transform()
Transform298.translation = [0.0963,0.0065,-0.0065]
Transform299 = x3d.Transform()
""" Empty Transform """
Shape300 = x3d.Shape()
Shape300.USE = "HAnimJointShape"

Transform299.children.append(Shape300)

Transform298.children.append(Transform299)

HAnimSegment297.children.append(Transform298)
Shape301 = x3d.Shape()
LineSet302 = x3d.LineSet()
LineSet302.vertexCount = [2]
Coordinate303 = x3d.Coordinate()

LineSet302.coord = Coordinate303
""" from l_metatarsophalangeal_3 to l_tarsal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA304 = x3d.ColorRGBA()
ColorRGBA304.USE = "HAnimSegmentLineColorRGBA"

LineSet302.color = ColorRGBA304

Shape301.geometry = LineSet302

HAnimSegment297.children.append(Shape301)

HAnimJoint296.children.append(HAnimSegment297)
HAnimJoint305 = x3d.HAnimJoint()
HAnimJoint305.DEF = "hanim_l_tarsal_proximal_interphalangeal_3"
HAnimJoint305.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint305.center = [0.0987,0.0034,0.0086]
HAnimSegment306 = x3d.HAnimSegment()
HAnimSegment306.DEF = "hanim_l_tarsal_middle_phalanx_3"
HAnimSegment306.name = "l_tarsal_middle_phalanx_3"
Transform307 = x3d.Transform()
Transform307.translation = [0.0987,0.0034,0.0086]
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
""" from l_tarsal_proximal_interphalangeal_3 to l_tarsal_distal_interphalangeal_3 vertices 2"""
ColorRGBA313 = x3d.ColorRGBA()
ColorRGBA313.USE = "HAnimSegmentLineColorRGBA"

LineSet311.color = ColorRGBA313

Shape310.geometry = LineSet311

HAnimSegment306.children.append(Shape310)
HAnimSite314 = x3d.HAnimSite()
HAnimSite314.DEF = "hanim_l_tarsal_distal_phalanx_3_tip"
HAnimSite314.name = "l_tarsal_distal_phalanx_3_tip"
TouchSensor315 = x3d.TouchSensor()
TouchSensor315.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite314.children.append(TouchSensor315)
Shape316 = x3d.Shape()
Shape316.USE = "HAnimSiteShape"

HAnimSite314.children.append(Shape316)

HAnimSegment306.children.append(HAnimSite314)

HAnimJoint305.children.append(HAnimSegment306)
HAnimJoint317 = x3d.HAnimJoint()
HAnimJoint317.DEF = "hanim_l_tarsal_distal_interphalangeal_3"
HAnimJoint317.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint317.center = [0.1002,0.0013,0.0178]

HAnimJoint305.children.append(HAnimJoint317)

HAnimJoint296.children.append(HAnimJoint305)

HAnimJoint287.children.append(HAnimJoint296)

HAnimJoint278.children.append(HAnimJoint287)

HAnimJoint187.children.append(HAnimJoint278)

HAnimJoint174.children.append(HAnimJoint187)
HAnimJoint318 = x3d.HAnimJoint()
HAnimJoint318.DEF = "hanim_l_calcaneocuboid"
HAnimJoint318.name = "l_calcaneocuboid"
HAnimJoint318.center = [0.0889,0.0494,-0.1278]
HAnimSegment319 = x3d.HAnimSegment()
HAnimSegment319.DEF = "hanim_l_calcaneus"
HAnimSegment319.name = "l_calcaneus"
Transform320 = x3d.Transform()
Transform320.translation = [0.0889,0.0494,-0.1278]
Transform321 = x3d.Transform()
""" Empty Transform """
Shape322 = x3d.Shape()
Shape322.USE = "HAnimJointShape"

Transform321.children.append(Shape322)

Transform320.children.append(Transform321)

HAnimSegment319.children.append(Transform320)
Shape323 = x3d.Shape()
LineSet324 = x3d.LineSet()
LineSet324.vertexCount = [2]
Coordinate325 = x3d.Coordinate()

LineSet324.coord = Coordinate325
""" from l_calcaneocuboid to l_transversetarsal vertices 2"""
ColorRGBA326 = x3d.ColorRGBA()
ColorRGBA326.USE = "HAnimSegmentLineColorRGBA"

LineSet324.color = ColorRGBA326

Shape323.geometry = LineSet324

HAnimSegment319.children.append(Shape323)

HAnimJoint318.children.append(HAnimSegment319)
HAnimJoint327 = x3d.HAnimJoint()
HAnimJoint327.DEF = "hanim_l_transversetarsal"
HAnimJoint327.name = "l_transversetarsal"
HAnimJoint327.center = [0.1105,0.0267,-0.0998]
HAnimSegment328 = x3d.HAnimSegment()
HAnimSegment328.DEF = "hanim_l_cuboid"
HAnimSegment328.name = "l_cuboid"
Transform329 = x3d.Transform()
Transform329.translation = [0.1105,0.0267,-0.0998]
Transform330 = x3d.Transform()
""" Empty Transform """
Shape331 = x3d.Shape()
Shape331.USE = "HAnimJointShape"

Transform330.children.append(Shape331)

Transform329.children.append(Transform330)

HAnimSegment328.children.append(Transform329)
Shape332 = x3d.Shape()
LineSet333 = x3d.LineSet()
LineSet333.vertexCount = [2]
Coordinate334 = x3d.Coordinate()

LineSet333.coord = Coordinate334
""" from l_transversetarsal to l_tarsometatarsal_4 vertices 2"""
ColorRGBA335 = x3d.ColorRGBA()
ColorRGBA335.USE = "HAnimSegmentLineColorRGBA"

LineSet333.color = ColorRGBA335

Shape332.geometry = LineSet333

HAnimSegment328.children.append(Shape332)
Shape336 = x3d.Shape()
LineSet337 = x3d.LineSet()
LineSet337.vertexCount = [2]
Coordinate338 = x3d.Coordinate()

LineSet337.coord = Coordinate338
""" from l_transversetarsal to l_tarsometatarsal_5 vertices 2"""
ColorRGBA339 = x3d.ColorRGBA()
ColorRGBA339.USE = "HAnimSegmentLineColorRGBA"

LineSet337.color = ColorRGBA339

Shape336.geometry = LineSet337

HAnimSegment328.children.append(Shape336)

HAnimJoint327.children.append(HAnimSegment328)
HAnimJoint340 = x3d.HAnimJoint()
HAnimJoint340.DEF = "hanim_l_tarsometatarsal_4"
HAnimJoint340.name = "l_tarsometatarsal_4"
HAnimJoint340.center = [0.1063,0.0160,-0.0634]
HAnimSegment341 = x3d.HAnimSegment()
HAnimSegment341.DEF = "hanim_l_metatarsal_4"
HAnimSegment341.name = "l_metatarsal_4"
Transform342 = x3d.Transform()
Transform342.translation = [0.1063,0.0160,-0.0634]
Transform343 = x3d.Transform()
""" Empty Transform """
Shape344 = x3d.Shape()
Shape344.USE = "HAnimJointShape"

Transform343.children.append(Shape344)

Transform342.children.append(Transform343)

HAnimSegment341.children.append(Transform342)
Shape345 = x3d.Shape()
LineSet346 = x3d.LineSet()
LineSet346.vertexCount = [2]
Coordinate347 = x3d.Coordinate()

LineSet346.coord = Coordinate347
""" from l_tarsometatarsal_4 to l_metatarsophalangeal_4 vertices 2"""
ColorRGBA348 = x3d.ColorRGBA()
ColorRGBA348.USE = "HAnimSegmentLineColorRGBA"

LineSet346.color = ColorRGBA348

Shape345.geometry = LineSet346

HAnimSegment341.children.append(Shape345)

HAnimJoint340.children.append(HAnimSegment341)
HAnimJoint349 = x3d.HAnimJoint()
HAnimJoint349.DEF = "hanim_l_metatarsophalangeal_4"
HAnimJoint349.name = "l_metatarsophalangeal_4"
HAnimJoint349.center = [0.1097,0.0058,-0.0107]
HAnimSegment350 = x3d.HAnimSegment()
HAnimSegment350.DEF = "hanim_l_tarsal_proximal_phalanx_4"
HAnimSegment350.name = "l_tarsal_proximal_phalanx_4"
Transform351 = x3d.Transform()
Transform351.translation = [0.1097,0.0058,-0.0107]
Transform352 = x3d.Transform()
""" Empty Transform """
Shape353 = x3d.Shape()
Shape353.USE = "HAnimJointShape"

Transform352.children.append(Shape353)

Transform351.children.append(Transform352)

HAnimSegment350.children.append(Transform351)
Shape354 = x3d.Shape()
LineSet355 = x3d.LineSet()
LineSet355.vertexCount = [2]
Coordinate356 = x3d.Coordinate()

LineSet355.coord = Coordinate356
""" from l_metatarsophalangeal_4 to l_tarsal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA357 = x3d.ColorRGBA()
ColorRGBA357.USE = "HAnimSegmentLineColorRGBA"

LineSet355.color = ColorRGBA357

Shape354.geometry = LineSet355

HAnimSegment350.children.append(Shape354)

HAnimJoint349.children.append(HAnimSegment350)
HAnimJoint358 = x3d.HAnimJoint()
HAnimJoint358.DEF = "hanim_l_tarsal_proximal_interphalangeal_4"
HAnimJoint358.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint358.center = [0.1140,0.0037,0.0044]
HAnimSegment359 = x3d.HAnimSegment()
HAnimSegment359.DEF = "hanim_l_tarsal_middle_phalanx_4"
HAnimSegment359.name = "l_tarsal_middle_phalanx_4"
Transform360 = x3d.Transform()
Transform360.translation = [0.1140,0.0037,0.0044]
Transform361 = x3d.Transform()
""" Empty Transform """
Shape362 = x3d.Shape()
Shape362.USE = "HAnimJointShape"

Transform361.children.append(Shape362)

Transform360.children.append(Transform361)

HAnimSegment359.children.append(Transform360)
Shape363 = x3d.Shape()
LineSet364 = x3d.LineSet()
LineSet364.vertexCount = [2]
Coordinate365 = x3d.Coordinate()

LineSet364.coord = Coordinate365
""" from l_tarsal_proximal_interphalangeal_4 to l_tarsal_distal_interphalangeal_4 vertices 2"""
ColorRGBA366 = x3d.ColorRGBA()
ColorRGBA366.USE = "HAnimSegmentLineColorRGBA"

LineSet364.color = ColorRGBA366

Shape363.geometry = LineSet364

HAnimSegment359.children.append(Shape363)
HAnimSite367 = x3d.HAnimSite()
HAnimSite367.DEF = "hanim_l_tarsal_distal_phalanx_4_tip"
HAnimSite367.name = "l_tarsal_distal_phalanx_4_tip"
TouchSensor368 = x3d.TouchSensor()
TouchSensor368.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite367.children.append(TouchSensor368)
Shape369 = x3d.Shape()
Shape369.USE = "HAnimSiteShape"

HAnimSite367.children.append(Shape369)

HAnimSegment359.children.append(HAnimSite367)

HAnimJoint358.children.append(HAnimSegment359)
HAnimJoint370 = x3d.HAnimJoint()
HAnimJoint370.DEF = "hanim_l_tarsal_distal_interphalangeal_4"
HAnimJoint370.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint370.center = [0.1155,0.0008,0.0118]

HAnimJoint358.children.append(HAnimJoint370)

HAnimJoint349.children.append(HAnimJoint358)

HAnimJoint340.children.append(HAnimJoint349)

HAnimJoint327.children.append(HAnimJoint340)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.DEF = "hanim_l_tarsometatarsal_5"
HAnimJoint371.name = "l_tarsometatarsal_5"
HAnimJoint371.center = [0.1206,0.0124,-0.0671]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.DEF = "hanim_l_metatarsal_5"
HAnimSegment372.name = "l_metatarsal_5"
Transform373 = x3d.Transform()
Transform373.translation = [0.1206,0.0124,-0.0671]
Transform374 = x3d.Transform()
""" Empty Transform """
Shape375 = x3d.Shape()
Shape375.USE = "HAnimJointShape"

Transform374.children.append(Shape375)

Transform373.children.append(Transform374)

HAnimSegment372.children.append(Transform373)
Shape376 = x3d.Shape()
LineSet377 = x3d.LineSet()
LineSet377.vertexCount = [2]
Coordinate378 = x3d.Coordinate()

LineSet377.coord = Coordinate378
""" from l_tarsometatarsal_5 to l_metatarsophalangeal_5 vertices 2"""
ColorRGBA379 = x3d.ColorRGBA()
ColorRGBA379.USE = "HAnimSegmentLineColorRGBA"

LineSet377.color = ColorRGBA379

Shape376.geometry = LineSet377

HAnimSegment372.children.append(Shape376)
HAnimSite380 = x3d.HAnimSite()
HAnimSite380.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite380.name = "l_metatarsal_phalanx_5_pt"
TouchSensor381 = x3d.TouchSensor()
TouchSensor381.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite380.children.append(TouchSensor381)
Shape382 = x3d.Shape()
Shape382.USE = "HAnimSiteShape"

HAnimSite380.children.append(Shape382)

HAnimSegment372.children.append(HAnimSite380)

HAnimJoint371.children.append(HAnimSegment372)
HAnimJoint383 = x3d.HAnimJoint()
HAnimJoint383.DEF = "hanim_l_metatarsophalangeal_5"
HAnimJoint383.name = "l_metatarsophalangeal_5"
HAnimJoint383.center = [0.1239,0.0051,-0.0153]
HAnimSegment384 = x3d.HAnimSegment()
HAnimSegment384.DEF = "hanim_l_tarsal_proximal_phalanx_5"
HAnimSegment384.name = "l_tarsal_proximal_phalanx_5"
Transform385 = x3d.Transform()
Transform385.translation = [0.1239,0.0051,-0.0153]
Transform386 = x3d.Transform()
""" Empty Transform """
Shape387 = x3d.Shape()
Shape387.USE = "HAnimJointShape"

Transform386.children.append(Shape387)

Transform385.children.append(Transform386)

HAnimSegment384.children.append(Transform385)
Shape388 = x3d.Shape()
LineSet389 = x3d.LineSet()
LineSet389.vertexCount = [2]
Coordinate390 = x3d.Coordinate()

LineSet389.coord = Coordinate390
""" from l_metatarsophalangeal_5 to l_tarsal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA391 = x3d.ColorRGBA()
ColorRGBA391.USE = "HAnimSegmentLineColorRGBA"

LineSet389.color = ColorRGBA391

Shape388.geometry = LineSet389

HAnimSegment384.children.append(Shape388)

HAnimJoint383.children.append(HAnimSegment384)
HAnimJoint392 = x3d.HAnimJoint()
HAnimJoint392.DEF = "hanim_l_tarsal_proximal_interphalangeal_5"
HAnimJoint392.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint392.center = [0.1262,0.0023,-0.0077]
HAnimSegment393 = x3d.HAnimSegment()
HAnimSegment393.DEF = "hanim_l_tarsal_middle_phalanx_5"
HAnimSegment393.name = "l_tarsal_middle_phalanx_5"
Transform394 = x3d.Transform()
Transform394.translation = [0.1262,0.0023,-0.0077]
Transform395 = x3d.Transform()
""" Empty Transform """
Shape396 = x3d.Shape()
Shape396.USE = "HAnimJointShape"

Transform395.children.append(Shape396)

Transform394.children.append(Transform395)

HAnimSegment393.children.append(Transform394)
Shape397 = x3d.Shape()
LineSet398 = x3d.LineSet()
LineSet398.vertexCount = [2]
Coordinate399 = x3d.Coordinate()

LineSet398.coord = Coordinate399
""" from l_tarsal_proximal_interphalangeal_5 to l_tarsal_distal_interphalangeal_5 vertices 2"""
ColorRGBA400 = x3d.ColorRGBA()
ColorRGBA400.USE = "HAnimSegmentLineColorRGBA"

LineSet398.color = ColorRGBA400

Shape397.geometry = LineSet398

HAnimSegment393.children.append(Shape397)
HAnimSite401 = x3d.HAnimSite()
HAnimSite401.DEF = "hanim_l_tarsal_distal_phalanx_5_tip"
HAnimSite401.name = "l_tarsal_distal_phalanx_5_tip"
TouchSensor402 = x3d.TouchSensor()
TouchSensor402.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite401.children.append(TouchSensor402)
Shape403 = x3d.Shape()
Shape403.USE = "HAnimSiteShape"

HAnimSite401.children.append(Shape403)

HAnimSegment393.children.append(HAnimSite401)

HAnimJoint392.children.append(HAnimSegment393)
HAnimJoint404 = x3d.HAnimJoint()
HAnimJoint404.DEF = "hanim_l_tarsal_distal_interphalangeal_5"
HAnimJoint404.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint404.center = [0.1271,0.0000,0.0000]

HAnimJoint392.children.append(HAnimJoint404)

HAnimJoint383.children.append(HAnimJoint392)

HAnimJoint371.children.append(HAnimJoint383)

HAnimJoint327.children.append(HAnimJoint371)

HAnimJoint318.children.append(HAnimJoint327)

HAnimJoint174.children.append(HAnimJoint318)

HAnimJoint159.children.append(HAnimJoint174)

HAnimJoint141.children.append(HAnimJoint159)

HAnimJoint104.children.append(HAnimJoint141)
HAnimJoint405 = x3d.HAnimJoint()
HAnimJoint405.DEF = "hanim_r_hip"
HAnimJoint405.name = "r_hip"
HAnimJoint405.center = [-0.0950,0.9171,0.0029]
HAnimSegment406 = x3d.HAnimSegment()
HAnimSegment406.DEF = "hanim_r_thigh"
HAnimSegment406.name = "r_thigh"
Transform407 = x3d.Transform()
Transform407.translation = [-0.0950,0.9171,0.0029]
Transform408 = x3d.Transform()
""" Empty Transform """
Shape409 = x3d.Shape()
Shape409.USE = "HAnimJointShape"

Transform408.children.append(Shape409)

Transform407.children.append(Transform408)

HAnimSegment406.children.append(Transform407)
Shape410 = x3d.Shape()
LineSet411 = x3d.LineSet()
LineSet411.vertexCount = [2]
Coordinate412 = x3d.Coordinate()

LineSet411.coord = Coordinate412
""" from r_hip to r_knee vertices 2"""
ColorRGBA413 = x3d.ColorRGBA()
ColorRGBA413.USE = "HAnimSegmentLineColorRGBA"

LineSet411.color = ColorRGBA413

Shape410.geometry = LineSet411

HAnimSegment406.children.append(Shape410)
HAnimSite414 = x3d.HAnimSite()
HAnimSite414.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite414.name = "r_lateral_malleolus_pt"
HAnimSite414.translation = [-0.1006,0.0658,-0.1075]
TouchSensor415 = x3d.TouchSensor()
TouchSensor415.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite414.children.append(TouchSensor415)
Shape416 = x3d.Shape()
Shape416.USE = "HAnimSiteShape"

HAnimSite414.children.append(Shape416)

HAnimSegment406.children.append(HAnimSite414)
HAnimSite417 = x3d.HAnimSite()
HAnimSite417.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite417.name = "r_medial_malleolus_pt"
HAnimSite417.translation = [-0.0591,0.0760,-0.0928]
TouchSensor418 = x3d.TouchSensor()
TouchSensor418.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite417.children.append(TouchSensor418)
Shape419 = x3d.Shape()
Shape419.USE = "HAnimSiteShape"

HAnimSite417.children.append(Shape419)

HAnimSegment406.children.append(HAnimSite417)
HAnimSite420 = x3d.HAnimSite()
HAnimSite420.DEF = "hanim_r_tibiale_pt"
HAnimSite420.name = "r_tibiale_pt"
TouchSensor421 = x3d.TouchSensor()
TouchSensor421.description = "HAnimSite r_tibiale_pt"

HAnimSite420.children.append(TouchSensor421)
Shape422 = x3d.Shape()
Shape422.USE = "HAnimSiteShape"

HAnimSite420.children.append(Shape422)

HAnimSegment406.children.append(HAnimSite420)

HAnimJoint405.children.append(HAnimSegment406)
HAnimJoint423 = x3d.HAnimJoint()
HAnimJoint423.DEF = "hanim_r_knee"
HAnimJoint423.name = "r_knee"
HAnimJoint423.center = [-0.0867,0.4913,0.0318]
HAnimSegment424 = x3d.HAnimSegment()
HAnimSegment424.DEF = "hanim_r_calf"
HAnimSegment424.name = "r_calf"
Transform425 = x3d.Transform()
Transform425.translation = [-0.0867,0.4913,0.0318]
Transform426 = x3d.Transform()
""" Empty Transform """
Shape427 = x3d.Shape()
Shape427.USE = "HAnimJointShape"

Transform426.children.append(Shape427)

Transform425.children.append(Transform426)

HAnimSegment424.children.append(Transform425)
Shape428 = x3d.Shape()
LineSet429 = x3d.LineSet()
LineSet429.vertexCount = [2]
Coordinate430 = x3d.Coordinate()

LineSet429.coord = Coordinate430
""" from r_knee to r_talocrural vertices 2"""
ColorRGBA431 = x3d.ColorRGBA()
ColorRGBA431.USE = "HAnimSegmentLineColorRGBA"

LineSet429.color = ColorRGBA431

Shape428.geometry = LineSet429

HAnimSegment424.children.append(Shape428)
HAnimSite432 = x3d.HAnimSite()
HAnimSite432.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite432.name = "r_calcaneus_posterior_pt"
HAnimSite432.translation = [-0.0692,0.0297,-0.1221]
TouchSensor433 = x3d.TouchSensor()
TouchSensor433.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite432.children.append(TouchSensor433)
Shape434 = x3d.Shape()
Shape434.USE = "HAnimSiteShape"

HAnimSite432.children.append(Shape434)

HAnimSegment424.children.append(HAnimSite432)
HAnimSite435 = x3d.HAnimSite()
HAnimSite435.DEF = "hanim_r_sphyrion_pt"
HAnimSite435.name = "r_sphyrion_pt"
HAnimSite435.translation = [-0.0603,0.0610,-0.1002]
TouchSensor436 = x3d.TouchSensor()
TouchSensor436.description = "HAnimSite r_sphyrion_pt"

HAnimSite435.children.append(TouchSensor436)
Shape437 = x3d.Shape()
Shape437.USE = "HAnimSiteShape"

HAnimSite435.children.append(Shape437)

HAnimSegment424.children.append(HAnimSite435)

HAnimJoint423.children.append(HAnimSegment424)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.DEF = "hanim_r_talocrural"
HAnimJoint438.name = "r_talocrural"
HAnimJoint438.center = [-0.0801,0.0712,-0.0766]
HAnimSegment439 = x3d.HAnimSegment()
HAnimSegment439.DEF = "hanim_r_talus"
HAnimSegment439.name = "r_talus"
Transform440 = x3d.Transform()
Transform440.scale = [0.15,0.15,0.15]
Transform440.translation = [-0.05,0.06,-0.025]
Transform440.rotation = [1,0,0,-1.57]
""" Transform right foot """
Transform441 = x3d.Transform()
""" Empty Transform right foot """
Shape442 = x3d.Shape()
Shape442.USE = "HAnimJointShape"

Transform441.children.append(Shape442)

Transform440.children.append(Transform441)

HAnimSegment439.children.append(Transform440)
Shape443 = x3d.Shape()
LineSet444 = x3d.LineSet()
LineSet444.vertexCount = [2]
Coordinate445 = x3d.Coordinate()

LineSet444.coord = Coordinate445
""" from r_talocrural to r_talocalcaneonavicular vertices 2"""
ColorRGBA446 = x3d.ColorRGBA()
ColorRGBA446.USE = "HAnimSegmentLineColorRGBA"

LineSet444.color = ColorRGBA446

Shape443.geometry = LineSet444

HAnimSegment439.children.append(Shape443)
Shape447 = x3d.Shape()
LineSet448 = x3d.LineSet()
LineSet448.vertexCount = [2]
Coordinate449 = x3d.Coordinate()

LineSet448.coord = Coordinate449
""" from r_talocrural to r_calcaneocuboid vertices 2"""
ColorRGBA450 = x3d.ColorRGBA()
ColorRGBA450.USE = "HAnimSegmentLineColorRGBA"

LineSet448.color = ColorRGBA450

Shape447.geometry = LineSet448

HAnimSegment439.children.append(Shape447)

HAnimJoint438.children.append(HAnimSegment439)
HAnimJoint451 = x3d.HAnimJoint()
HAnimJoint451.DEF = "hanim_r_talocalcaneonavicular"
HAnimJoint451.name = "r_talocalcaneonavicular"
HAnimJoint451.center = [-0.0781,0.0283,-0.0970]
HAnimSegment452 = x3d.HAnimSegment()
HAnimSegment452.DEF = "hanim_r_navicular"
HAnimSegment452.name = "r_navicular"
Transform453 = x3d.Transform()
Transform453.translation = [-0.0781,0.0283,-0.0970]
Transform454 = x3d.Transform()
""" Empty Transform """
Shape455 = x3d.Shape()
Shape455.USE = "HAnimJointShape"

Transform454.children.append(Shape455)

Transform453.children.append(Transform454)

HAnimSegment452.children.append(Transform453)
Shape456 = x3d.Shape()
LineSet457 = x3d.LineSet()
LineSet457.vertexCount = [2]
Coordinate458 = x3d.Coordinate()

LineSet457.coord = Coordinate458
""" from r_talocalcaneonavicular to r_cuneonavicular_1 vertices 2"""
ColorRGBA459 = x3d.ColorRGBA()
ColorRGBA459.USE = "HAnimSegmentLineColorRGBA"

LineSet457.color = ColorRGBA459

Shape456.geometry = LineSet457

HAnimSegment452.children.append(Shape456)
Shape460 = x3d.Shape()
LineSet461 = x3d.LineSet()
LineSet461.vertexCount = [2]
Coordinate462 = x3d.Coordinate()

LineSet461.coord = Coordinate462
""" from r_talocalcaneonavicular to r_cuneonavicular_2 vertices 2"""
ColorRGBA463 = x3d.ColorRGBA()
ColorRGBA463.USE = "HAnimSegmentLineColorRGBA"

LineSet461.color = ColorRGBA463

Shape460.geometry = LineSet461

HAnimSegment452.children.append(Shape460)
Shape464 = x3d.Shape()
LineSet465 = x3d.LineSet()
LineSet465.vertexCount = [2]
Coordinate466 = x3d.Coordinate()

LineSet465.coord = Coordinate466
""" from r_talocalcaneonavicular to r_cuneonavicular_3 vertices 2"""
ColorRGBA467 = x3d.ColorRGBA()
ColorRGBA467.USE = "HAnimSegmentLineColorRGBA"

LineSet465.color = ColorRGBA467

Shape464.geometry = LineSet465

HAnimSegment452.children.append(Shape464)

HAnimJoint451.children.append(HAnimSegment452)
HAnimJoint468 = x3d.HAnimJoint()
HAnimJoint468.DEF = "hanim_r_cuneonavicular_1"
HAnimJoint468.name = "r_cuneonavicular_1"
HAnimJoint468.center = [-0.0672,0.0235,-0.0835]
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.DEF = "hanim_r_cuneiform_1"
HAnimSegment469.name = "r_cuneiform_1"
Transform470 = x3d.Transform()
Transform470.translation = [-0.0672,0.0235,-0.0835]
Transform471 = x3d.Transform()
""" Empty Transform """
Shape472 = x3d.Shape()
Shape472.USE = "HAnimJointShape"

Transform471.children.append(Shape472)

Transform470.children.append(Transform471)

HAnimSegment469.children.append(Transform470)
Shape473 = x3d.Shape()
LineSet474 = x3d.LineSet()
LineSet474.vertexCount = [2]
Coordinate475 = x3d.Coordinate()

LineSet474.coord = Coordinate475
""" from r_cuneonavicular_1 to r_tarsometatarsal_1 vertices 2"""
ColorRGBA476 = x3d.ColorRGBA()
ColorRGBA476.USE = "HAnimSegmentLineColorRGBA"

LineSet474.color = ColorRGBA476

Shape473.geometry = LineSet474

HAnimSegment469.children.append(Shape473)

HAnimJoint468.children.append(HAnimSegment469)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.DEF = "hanim_r_tarsometatarsal_1"
HAnimJoint477.name = "r_tarsometatarsal_1"
HAnimJoint477.center = [-0.0644,0.0147,-0.0577]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.DEF = "hanim_r_metatarsal_1"
HAnimSegment478.name = "r_metatarsal_1"
Transform479 = x3d.Transform()
Transform479.translation = [-0.0644,0.0147,-0.0577]
Transform480 = x3d.Transform()
""" Empty Transform """
Shape481 = x3d.Shape()
Shape481.USE = "HAnimJointShape"

Transform480.children.append(Shape481)

Transform479.children.append(Transform480)

HAnimSegment478.children.append(Transform479)
Shape482 = x3d.Shape()
LineSet483 = x3d.LineSet()
LineSet483.vertexCount = [2]
Coordinate484 = x3d.Coordinate()

LineSet483.coord = Coordinate484
""" from r_tarsometatarsal_1 to r_metatarsophalangeal_1 vertices 2"""
ColorRGBA485 = x3d.ColorRGBA()
ColorRGBA485.USE = "HAnimSegmentLineColorRGBA"

LineSet483.color = ColorRGBA485

Shape482.geometry = LineSet483

HAnimSegment478.children.append(Shape482)
HAnimSite486 = x3d.HAnimSite()
HAnimSite486.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite486.name = "r_metatarsal_phalanx_1_pt"
TouchSensor487 = x3d.TouchSensor()
TouchSensor487.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite486.children.append(TouchSensor487)
Shape488 = x3d.Shape()
Shape488.USE = "HAnimSiteShape"

HAnimSite486.children.append(Shape488)

HAnimSegment478.children.append(HAnimSite486)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint489 = x3d.HAnimJoint()
HAnimJoint489.DEF = "hanim_r_metatarsophalangeal_1"
HAnimJoint489.name = "r_metatarsophalangeal_1"
HAnimJoint489.center = [-0.0619,0.0059,-0.0083]
HAnimSegment490 = x3d.HAnimSegment()
HAnimSegment490.DEF = "hanim_r_tarsal_proximal_phalanx_1"
HAnimSegment490.name = "r_tarsal_proximal_phalanx_1"
Transform491 = x3d.Transform()
Transform491.translation = [-0.0619,0.0059,-0.0083]
Transform492 = x3d.Transform()
""" Empty Transform """
Shape493 = x3d.Shape()
Shape493.USE = "HAnimJointShape"

Transform492.children.append(Shape493)

Transform491.children.append(Transform492)

HAnimSegment490.children.append(Transform491)
Shape494 = x3d.Shape()
LineSet495 = x3d.LineSet()
LineSet495.vertexCount = [2]
Coordinate496 = x3d.Coordinate()

LineSet495.coord = Coordinate496
""" from r_metatarsophalangeal_1 to r_tarsal_interphalangeal_1 vertices 2"""
ColorRGBA497 = x3d.ColorRGBA()
ColorRGBA497.USE = "HAnimSegmentLineColorRGBA"

LineSet495.color = ColorRGBA497

Shape494.geometry = LineSet495

HAnimSegment490.children.append(Shape494)
HAnimSite498 = x3d.HAnimSite()
HAnimSite498.DEF = "hanim_r_tarsal_distal_phalanx_1_tip"
HAnimSite498.name = "r_tarsal_distal_phalanx_1_tip"
TouchSensor499 = x3d.TouchSensor()
TouchSensor499.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite498.children.append(TouchSensor499)
Shape500 = x3d.Shape()
Shape500.USE = "HAnimSiteShape"

HAnimSite498.children.append(Shape500)

HAnimSegment490.children.append(HAnimSite498)

HAnimJoint489.children.append(HAnimSegment490)
HAnimJoint501 = x3d.HAnimJoint()
HAnimJoint501.DEF = "hanim_r_tarsal_interphalangeal_1"
HAnimJoint501.name = "r_tarsal_interphalangeal_1"

HAnimJoint489.children.append(HAnimJoint501)

HAnimJoint477.children.append(HAnimJoint489)

HAnimJoint468.children.append(HAnimJoint477)

HAnimJoint451.children.append(HAnimJoint468)
HAnimJoint502 = x3d.HAnimJoint()
HAnimJoint502.DEF = "hanim_r_cuneonavicular_2"
HAnimJoint502.name = "r_cuneonavicular_2"
HAnimJoint502.center = [-0.0812,0.0250,-0.0805]
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.DEF = "hanim_r_cuneiform_2"
HAnimSegment503.name = "r_cuneiform_2"
Transform504 = x3d.Transform()
Transform504.translation = [-0.0812,0.0250,-0.0805]
Transform505 = x3d.Transform()
""" Empty Transform """
Shape506 = x3d.Shape()
Shape506.USE = "HAnimJointShape"

Transform505.children.append(Shape506)

Transform504.children.append(Transform505)

HAnimSegment503.children.append(Transform504)
Shape507 = x3d.Shape()
LineSet508 = x3d.LineSet()
LineSet508.vertexCount = [2]
Coordinate509 = x3d.Coordinate()

LineSet508.coord = Coordinate509
""" from r_cuneonavicular_2 to r_tarsometatarsal_2 vertices 2"""
ColorRGBA510 = x3d.ColorRGBA()
ColorRGBA510.USE = "HAnimSegmentLineColorRGBA"

LineSet508.color = ColorRGBA510

Shape507.geometry = LineSet508

HAnimSegment503.children.append(Shape507)

HAnimJoint502.children.append(HAnimSegment503)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint511.name = "r_tarsometatarsal_2"
HAnimJoint511.center = [-0.0800,0.0175,-0.0608]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.DEF = "hanim_r_metatarsal_2"
HAnimSegment512.name = "r_metatarsal_2"
Transform513 = x3d.Transform()
Transform513.translation = [-0.0800,0.0175,-0.0608]
Transform514 = x3d.Transform()
""" Empty Transform """
Shape515 = x3d.Shape()
Shape515.USE = "HAnimJointShape"

Transform514.children.append(Shape515)

Transform513.children.append(Transform514)

HAnimSegment512.children.append(Transform513)
Shape516 = x3d.Shape()
LineSet517 = x3d.LineSet()
LineSet517.vertexCount = [2]
Coordinate518 = x3d.Coordinate()

LineSet517.coord = Coordinate518
""" from r_tarsometatarsal_2 to r_metatarsophalangeal_2 vertices 2"""
ColorRGBA519 = x3d.ColorRGBA()
ColorRGBA519.USE = "HAnimSegmentLineColorRGBA"

LineSet517.color = ColorRGBA519

Shape516.geometry = LineSet517

HAnimSegment512.children.append(Shape516)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint520 = x3d.HAnimJoint()
HAnimJoint520.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint520.name = "r_metatarsophalangeal_2"
HAnimJoint520.center = [-0.0823,0.0064,-0.0040]
HAnimSegment521 = x3d.HAnimSegment()
HAnimSegment521.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSegment521.name = "r_tarsal_proximal_phalanx_2"
Transform522 = x3d.Transform()
Transform522.translation = [-0.0823,0.0064,-0.0040]
Transform523 = x3d.Transform()
""" Empty Transform """
Shape524 = x3d.Shape()
Shape524.USE = "HAnimJointShape"

Transform523.children.append(Shape524)

Transform522.children.append(Transform523)

HAnimSegment521.children.append(Transform522)
Shape525 = x3d.Shape()
LineSet526 = x3d.LineSet()
LineSet526.vertexCount = [2]
Coordinate527 = x3d.Coordinate()

LineSet526.coord = Coordinate527
""" from r_metatarsophalangeal_2 to r_tarsal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA528 = x3d.ColorRGBA()
ColorRGBA528.USE = "HAnimSegmentLineColorRGBA"

LineSet526.color = ColorRGBA528

Shape525.geometry = LineSet526

HAnimSegment521.children.append(Shape525)

HAnimJoint520.children.append(HAnimSegment521)
HAnimJoint529 = x3d.HAnimJoint()
HAnimJoint529.DEF = "hanim_r_tarsal_proximal_interphalangeal_2"
HAnimJoint529.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint529.center = [-0.0841,0.0041,0.0121]
HAnimSegment530 = x3d.HAnimSegment()
HAnimSegment530.DEF = "hanim_r_tarsal_middle_phalanx_2"
HAnimSegment530.name = "r_tarsal_middle_phalanx_2"
Transform531 = x3d.Transform()
Transform531.translation = [-0.0841,0.0041,0.0121]
Transform532 = x3d.Transform()
""" Empty Transform """
Shape533 = x3d.Shape()
Shape533.USE = "HAnimJointShape"

Transform532.children.append(Shape533)

Transform531.children.append(Transform532)

HAnimSegment530.children.append(Transform531)
Shape534 = x3d.Shape()
LineSet535 = x3d.LineSet()
LineSet535.vertexCount = [2]
Coordinate536 = x3d.Coordinate()

LineSet535.coord = Coordinate536
""" from r_tarsal_proximal_interphalangeal_2 to r_tarsal_distal_interphalangeal_2 vertices 2"""
ColorRGBA537 = x3d.ColorRGBA()
ColorRGBA537.USE = "HAnimSegmentLineColorRGBA"

LineSet535.color = ColorRGBA537

Shape534.geometry = LineSet535

HAnimSegment530.children.append(Shape534)
HAnimSite538 = x3d.HAnimSite()
HAnimSite538.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite538.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite538.translation = [-0.0883,0.0134,0.1383]
TouchSensor539 = x3d.TouchSensor()
TouchSensor539.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite538.children.append(TouchSensor539)
Shape540 = x3d.Shape()
Shape540.USE = "HAnimSiteShape"

HAnimSite538.children.append(Shape540)

HAnimSegment530.children.append(HAnimSite538)

HAnimJoint529.children.append(HAnimSegment530)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint541.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint541.center = [-0.0841,0.0013,0.0216]

HAnimJoint529.children.append(HAnimJoint541)

HAnimJoint520.children.append(HAnimJoint529)

HAnimJoint511.children.append(HAnimJoint520)

HAnimJoint502.children.append(HAnimJoint511)

HAnimJoint451.children.append(HAnimJoint502)
HAnimJoint542 = x3d.HAnimJoint()
HAnimJoint542.DEF = "hanim_r_cuneonavicular_3"
HAnimJoint542.name = "r_cuneonavicular_3"
HAnimJoint542.center = [-0.0928,0.0248,-0.0821]
HAnimSegment543 = x3d.HAnimSegment()
HAnimSegment543.DEF = "hanim_r_cuneiform_3"
HAnimSegment543.name = "r_cuneiform_3"
Transform544 = x3d.Transform()
Transform544.translation = [-0.0928,0.0248,-0.0821]
Transform545 = x3d.Transform()
""" Empty Transform """
Shape546 = x3d.Shape()
Shape546.USE = "HAnimJointShape"

Transform545.children.append(Shape546)

Transform544.children.append(Transform545)

HAnimSegment543.children.append(Transform544)
Shape547 = x3d.Shape()
LineSet548 = x3d.LineSet()
LineSet548.vertexCount = [2]
Coordinate549 = x3d.Coordinate()

LineSet548.coord = Coordinate549
""" from r_cuneonavicular_3 to r_tarsometatarsal_3  vertices 2"""
ColorRGBA550 = x3d.ColorRGBA()
ColorRGBA550.USE = "HAnimSegmentLineColorRGBA"

LineSet548.color = ColorRGBA550

Shape547.geometry = LineSet548

HAnimSegment543.children.append(Shape547)

HAnimJoint542.children.append(HAnimSegment543)
HAnimJoint551 = x3d.HAnimJoint()
HAnimJoint551.DEF = "hanim_r_tarsometatarsal_3 "
HAnimJoint551.name = "r_tarsometatarsal_3 "
HAnimSegment552 = x3d.HAnimSegment()
HAnimSegment552.DEF = "hanim_r_metatarsal_3"
HAnimSegment552.name = "r_metatarsal_3"
Transform553 = x3d.Transform()
Transform553.translation = [-0.0928,0.0248,-0.0821]
Transform554 = x3d.Transform()
""" Empty Transform """
Shape555 = x3d.Shape()
Shape555.USE = "HAnimJointShape"

Transform554.children.append(Shape555)

Transform553.children.append(Transform554)

HAnimSegment552.children.append(Transform553)
Shape556 = x3d.Shape()
LineSet557 = x3d.LineSet()
LineSet557.vertexCount = [2]
Coordinate558 = x3d.Coordinate()

LineSet557.coord = Coordinate558
""" from r_tarsometatarsal_3  to r_metatarsophalangeal_3 vertices 1"""
ColorRGBA559 = x3d.ColorRGBA()
ColorRGBA559.USE = "HAnimSegmentLineColorRGBA"

LineSet557.color = ColorRGBA559

Shape556.geometry = LineSet557

HAnimSegment552.children.append(Shape556)

HAnimJoint551.children.append(HAnimSegment552)
HAnimJoint560 = x3d.HAnimJoint()
HAnimJoint560.DEF = "hanim_r_metatarsophalangeal_3"
HAnimJoint560.name = "r_metatarsophalangeal_3"
HAnimJoint560.center = [-0.0963,0.0065,-0.0065]
HAnimSegment561 = x3d.HAnimSegment()
HAnimSegment561.DEF = "hanim_r_tarsal_proximal_phalanx_3"
HAnimSegment561.name = "r_tarsal_proximal_phalanx_3"
Transform562 = x3d.Transform()
Transform562.translation = [-0.0963,0.0065,-0.0065]
Transform563 = x3d.Transform()
""" Empty Transform """
Shape564 = x3d.Shape()
Shape564.USE = "HAnimJointShape"

Transform563.children.append(Shape564)

Transform562.children.append(Transform563)

HAnimSegment561.children.append(Transform562)
Shape565 = x3d.Shape()
LineSet566 = x3d.LineSet()
LineSet566.vertexCount = [2]
Coordinate567 = x3d.Coordinate()

LineSet566.coord = Coordinate567
""" from r_metatarsophalangeal_3 to r_tarsal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA568 = x3d.ColorRGBA()
ColorRGBA568.USE = "HAnimSegmentLineColorRGBA"

LineSet566.color = ColorRGBA568

Shape565.geometry = LineSet566

HAnimSegment561.children.append(Shape565)

HAnimJoint560.children.append(HAnimSegment561)
HAnimJoint569 = x3d.HAnimJoint()
HAnimJoint569.DEF = "hanim_r_tarsal_proximal_interphalangeal_3"
HAnimJoint569.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint569.center = [-0.0987,0.0034,0.0086]
HAnimSegment570 = x3d.HAnimSegment()
HAnimSegment570.DEF = "hanim_r_tarsal_middle_phalanx_3"
HAnimSegment570.name = "r_tarsal_middle_phalanx_3"
Transform571 = x3d.Transform()
Transform571.translation = [-0.0987,0.0034,0.0086]
Transform572 = x3d.Transform()
""" Empty Transform """
Shape573 = x3d.Shape()
Shape573.USE = "HAnimJointShape"

Transform572.children.append(Shape573)

Transform571.children.append(Transform572)

HAnimSegment570.children.append(Transform571)
Shape574 = x3d.Shape()
LineSet575 = x3d.LineSet()
LineSet575.vertexCount = [2]
Coordinate576 = x3d.Coordinate()

LineSet575.coord = Coordinate576
""" from r_tarsal_proximal_interphalangeal_3 to r_tarsal_distal_interphalangeal_3 vertices 2"""
ColorRGBA577 = x3d.ColorRGBA()
ColorRGBA577.USE = "HAnimSegmentLineColorRGBA"

LineSet575.color = ColorRGBA577

Shape574.geometry = LineSet575

HAnimSegment570.children.append(Shape574)
HAnimSite578 = x3d.HAnimSite()
HAnimSite578.DEF = "hanim_r_tarsal_distal_phalanx_3_tip"
HAnimSite578.name = "r_tarsal_distal_phalanx_3_tip"
TouchSensor579 = x3d.TouchSensor()
TouchSensor579.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite578.children.append(TouchSensor579)
Shape580 = x3d.Shape()
Shape580.USE = "HAnimSiteShape"

HAnimSite578.children.append(Shape580)

HAnimSegment570.children.append(HAnimSite578)

HAnimJoint569.children.append(HAnimSegment570)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.DEF = "hanim_r_tarsal_distal_interphalangeal_3"
HAnimJoint581.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint581.center = [-0.1002,0.0013,0.0178]

HAnimJoint569.children.append(HAnimJoint581)

HAnimJoint560.children.append(HAnimJoint569)

HAnimJoint551.children.append(HAnimJoint560)

HAnimJoint542.children.append(HAnimJoint551)

HAnimJoint451.children.append(HAnimJoint542)

HAnimJoint438.children.append(HAnimJoint451)
HAnimJoint582 = x3d.HAnimJoint()
HAnimJoint582.DEF = "hanim_r_calcaneocuboid"
HAnimJoint582.name = "r_calcaneocuboid"
HAnimJoint582.center = [-0.0889,0.0494,-0.1278]
HAnimSegment583 = x3d.HAnimSegment()
HAnimSegment583.DEF = "hanim_r_calcaneus"
HAnimSegment583.name = "r_calcaneus"
Transform584 = x3d.Transform()
Transform584.translation = [-0.0889,0.0494,-0.1278]
Transform585 = x3d.Transform()
""" Empty Transform """
Shape586 = x3d.Shape()
Shape586.USE = "HAnimJointShape"

Transform585.children.append(Shape586)

Transform584.children.append(Transform585)

HAnimSegment583.children.append(Transform584)
Shape587 = x3d.Shape()
LineSet588 = x3d.LineSet()
LineSet588.vertexCount = [2]
Coordinate589 = x3d.Coordinate()

LineSet588.coord = Coordinate589
""" from r_calcaneocuboid to r_transversetarsal vertices 2"""
ColorRGBA590 = x3d.ColorRGBA()
ColorRGBA590.USE = "HAnimSegmentLineColorRGBA"

LineSet588.color = ColorRGBA590

Shape587.geometry = LineSet588

HAnimSegment583.children.append(Shape587)

HAnimJoint582.children.append(HAnimSegment583)
HAnimJoint591 = x3d.HAnimJoint()
HAnimJoint591.DEF = "hanim_r_transversetarsal"
HAnimJoint591.name = "r_transversetarsal"
HAnimJoint591.center = [-0.1105,0.0267,-0.0998]
HAnimSegment592 = x3d.HAnimSegment()
HAnimSegment592.DEF = "hanim_r_cuboid"
HAnimSegment592.name = "r_cuboid"
Transform593 = x3d.Transform()
Transform593.translation = [-0.1105,0.0267,-0.0998]
Transform594 = x3d.Transform()
""" Empty Transform """
Shape595 = x3d.Shape()
Shape595.USE = "HAnimJointShape"

Transform594.children.append(Shape595)

Transform593.children.append(Transform594)

HAnimSegment592.children.append(Transform593)
Shape596 = x3d.Shape()
LineSet597 = x3d.LineSet()
LineSet597.vertexCount = [2]
Coordinate598 = x3d.Coordinate()

LineSet597.coord = Coordinate598
""" from r_transversetarsal to r_tarsometatarsal_4 vertices 2"""
ColorRGBA599 = x3d.ColorRGBA()
ColorRGBA599.USE = "HAnimSegmentLineColorRGBA"

LineSet597.color = ColorRGBA599

Shape596.geometry = LineSet597

HAnimSegment592.children.append(Shape596)
Shape600 = x3d.Shape()
LineSet601 = x3d.LineSet()
LineSet601.vertexCount = [2]
Coordinate602 = x3d.Coordinate()

LineSet601.coord = Coordinate602
""" from r_transversetarsal to r_tarsometatarsal_5 vertices 2"""
ColorRGBA603 = x3d.ColorRGBA()
ColorRGBA603.USE = "HAnimSegmentLineColorRGBA"

LineSet601.color = ColorRGBA603

Shape600.geometry = LineSet601

HAnimSegment592.children.append(Shape600)

HAnimJoint591.children.append(HAnimSegment592)
HAnimJoint604 = x3d.HAnimJoint()
HAnimJoint604.DEF = "hanim_r_tarsometatarsal_4"
HAnimJoint604.name = "r_tarsometatarsal_4"
HAnimJoint604.center = [-0.1063,0.0160,-0.0634]
HAnimSegment605 = x3d.HAnimSegment()
HAnimSegment605.DEF = "hanim_r_metatarsal_4"
HAnimSegment605.name = "r_metatarsal_4"
Transform606 = x3d.Transform()
Transform606.translation = [-0.1063,0.0160,-0.0634]
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
""" from r_tarsometatarsal_4 to r_metatarsophalangeal_4 vertices 2"""
ColorRGBA612 = x3d.ColorRGBA()
ColorRGBA612.USE = "HAnimSegmentLineColorRGBA"

LineSet610.color = ColorRGBA612

Shape609.geometry = LineSet610

HAnimSegment605.children.append(Shape609)

HAnimJoint604.children.append(HAnimSegment605)
HAnimJoint613 = x3d.HAnimJoint()
HAnimJoint613.DEF = "hanim_r_metatarsophalangeal_4"
HAnimJoint613.name = "r_metatarsophalangeal_4"
HAnimJoint613.center = [-0.1097,0.0058,-0.0107]
HAnimSegment614 = x3d.HAnimSegment()
HAnimSegment614.DEF = "hanim_r_tarsal_proximal_phalanx_4"
HAnimSegment614.name = "r_tarsal_proximal_phalanx_4"
Transform615 = x3d.Transform()
Transform615.translation = [-0.1097,0.0058,-0.0107]
Transform616 = x3d.Transform()
""" Empty Transform """
Shape617 = x3d.Shape()
Shape617.USE = "HAnimJointShape"

Transform616.children.append(Shape617)

Transform615.children.append(Transform616)

HAnimSegment614.children.append(Transform615)
Shape618 = x3d.Shape()
LineSet619 = x3d.LineSet()
LineSet619.vertexCount = [2]
Coordinate620 = x3d.Coordinate()

LineSet619.coord = Coordinate620
""" from r_metatarsophalangeal_4 to r_tarsal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA621 = x3d.ColorRGBA()
ColorRGBA621.USE = "HAnimSegmentLineColorRGBA"

LineSet619.color = ColorRGBA621

Shape618.geometry = LineSet619

HAnimSegment614.children.append(Shape618)

HAnimJoint613.children.append(HAnimSegment614)
HAnimJoint622 = x3d.HAnimJoint()
HAnimJoint622.DEF = "hanim_r_tarsal_proximal_interphalangeal_4"
HAnimJoint622.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint622.center = [-0.1140,0.0037,0.0044]
HAnimSegment623 = x3d.HAnimSegment()
HAnimSegment623.DEF = "hanim_r_tarsal_middle_phalanx_4"
HAnimSegment623.name = "r_tarsal_middle_phalanx_4"
Transform624 = x3d.Transform()
Transform624.translation = [-0.1140,0.0037,0.0044]
Transform625 = x3d.Transform()
""" Empty Transform """
Shape626 = x3d.Shape()
Shape626.USE = "HAnimJointShape"

Transform625.children.append(Shape626)

Transform624.children.append(Transform625)

HAnimSegment623.children.append(Transform624)
Shape627 = x3d.Shape()
LineSet628 = x3d.LineSet()
LineSet628.vertexCount = [2]
Coordinate629 = x3d.Coordinate()

LineSet628.coord = Coordinate629
""" from r_tarsal_proximal_interphalangeal_4 to r_tarsal_distal_interphalangeal_4 vertices 2"""
ColorRGBA630 = x3d.ColorRGBA()
ColorRGBA630.USE = "HAnimSegmentLineColorRGBA"

LineSet628.color = ColorRGBA630

Shape627.geometry = LineSet628

HAnimSegment623.children.append(Shape627)
HAnimSite631 = x3d.HAnimSite()
HAnimSite631.DEF = "hanim_r_tarsal_distal_phalanx_4_tip"
HAnimSite631.name = "r_tarsal_distal_phalanx_4_tip"
TouchSensor632 = x3d.TouchSensor()
TouchSensor632.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite631.children.append(TouchSensor632)
Shape633 = x3d.Shape()
Shape633.USE = "HAnimSiteShape"

HAnimSite631.children.append(Shape633)

HAnimSegment623.children.append(HAnimSite631)

HAnimJoint622.children.append(HAnimSegment623)
HAnimJoint634 = x3d.HAnimJoint()
HAnimJoint634.DEF = "hanim_r_tarsal_distal_interphalangeal_4"
HAnimJoint634.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint634.center = [-0.1155,0.0008,0.0118]

HAnimJoint622.children.append(HAnimJoint634)

HAnimJoint613.children.append(HAnimJoint622)

HAnimJoint604.children.append(HAnimJoint613)

HAnimJoint591.children.append(HAnimJoint604)
HAnimJoint635 = x3d.HAnimJoint()
HAnimJoint635.DEF = "hanim_r_tarsometatarsal_5"
HAnimJoint635.name = "r_tarsometatarsal_5"
HAnimJoint635.center = [-0.1206,0.0124,-0.0671]
HAnimSegment636 = x3d.HAnimSegment()
HAnimSegment636.DEF = "hanim_r_metatarsal_5"
HAnimSegment636.name = "r_metatarsal_5"
Transform637 = x3d.Transform()
Transform637.translation = [-0.1206,0.0124,-0.0671]
Transform638 = x3d.Transform()
""" Empty Transform """
Shape639 = x3d.Shape()
Shape639.USE = "HAnimJointShape"

Transform638.children.append(Shape639)

Transform637.children.append(Transform638)

HAnimSegment636.children.append(Transform637)
Shape640 = x3d.Shape()
LineSet641 = x3d.LineSet()
LineSet641.vertexCount = [2]
Coordinate642 = x3d.Coordinate()

LineSet641.coord = Coordinate642
""" from r_tarsometatarsal_5 to r_metatarsophalangeal_5 vertices 2"""
ColorRGBA643 = x3d.ColorRGBA()
ColorRGBA643.USE = "HAnimSegmentLineColorRGBA"

LineSet641.color = ColorRGBA643

Shape640.geometry = LineSet641

HAnimSegment636.children.append(Shape640)
HAnimSite644 = x3d.HAnimSite()
HAnimSite644.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite644.name = "r_metatarsal_phalanx_5_pt"
TouchSensor645 = x3d.TouchSensor()
TouchSensor645.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite644.children.append(TouchSensor645)
Shape646 = x3d.Shape()
Shape646.USE = "HAnimSiteShape"

HAnimSite644.children.append(Shape646)

HAnimSegment636.children.append(HAnimSite644)

HAnimJoint635.children.append(HAnimSegment636)
HAnimJoint647 = x3d.HAnimJoint()
HAnimJoint647.DEF = "hanim_r_metatarsophalangeal_5"
HAnimJoint647.name = "r_metatarsophalangeal_5"
HAnimJoint647.center = [-0.1239,0.0051,-0.0153]
HAnimSegment648 = x3d.HAnimSegment()
HAnimSegment648.DEF = "hanim_r_tarsal_proximal_phalanx_5"
HAnimSegment648.name = "r_tarsal_proximal_phalanx_5"
Transform649 = x3d.Transform()
Transform649.translation = [-0.1239,0.0051,-0.0153]
Transform650 = x3d.Transform()
""" Empty Transform """
Shape651 = x3d.Shape()
Shape651.USE = "HAnimJointShape"

Transform650.children.append(Shape651)

Transform649.children.append(Transform650)

HAnimSegment648.children.append(Transform649)
Shape652 = x3d.Shape()
LineSet653 = x3d.LineSet()
LineSet653.vertexCount = [2]
Coordinate654 = x3d.Coordinate()

LineSet653.coord = Coordinate654
""" from r_metatarsophalangeal_5 to r_tarsal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA655 = x3d.ColorRGBA()
ColorRGBA655.USE = "HAnimSegmentLineColorRGBA"

LineSet653.color = ColorRGBA655

Shape652.geometry = LineSet653

HAnimSegment648.children.append(Shape652)

HAnimJoint647.children.append(HAnimSegment648)
HAnimJoint656 = x3d.HAnimJoint()
HAnimJoint656.DEF = "hanim_r_tarsal_proximal_interphalangeal_5"
HAnimJoint656.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint656.center = [-0.1262,0.0023,-0.0077]
HAnimSegment657 = x3d.HAnimSegment()
HAnimSegment657.DEF = "hanim_r_tarsal_middle_phalanx_5"
HAnimSegment657.name = "r_tarsal_middle_phalanx_5"
Transform658 = x3d.Transform()
Transform658.translation = [-0.1262,0.0023,-0.0077]
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
""" from r_tarsal_proximal_interphalangeal_5 to r_tarsal_distal_interphalangeal_5 vertices 2"""
ColorRGBA664 = x3d.ColorRGBA()
ColorRGBA664.USE = "HAnimSegmentLineColorRGBA"

LineSet662.color = ColorRGBA664

Shape661.geometry = LineSet662

HAnimSegment657.children.append(Shape661)
HAnimSite665 = x3d.HAnimSite()
HAnimSite665.DEF = "hanim_r_tarsal_distal_phalanx_5_tip"
HAnimSite665.name = "r_tarsal_distal_phalanx_5_tip"
TouchSensor666 = x3d.TouchSensor()
TouchSensor666.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite665.children.append(TouchSensor666)
Shape667 = x3d.Shape()
Shape667.USE = "HAnimSiteShape"

HAnimSite665.children.append(Shape667)

HAnimSegment657.children.append(HAnimSite665)

HAnimJoint656.children.append(HAnimSegment657)
HAnimJoint668 = x3d.HAnimJoint()
HAnimJoint668.DEF = "hanim_r_tarsal_distal_interphalangeal_5"
HAnimJoint668.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint668.center = [-0.1271,0.0000,0.0000]

HAnimJoint656.children.append(HAnimJoint668)

HAnimJoint647.children.append(HAnimJoint656)

HAnimJoint635.children.append(HAnimJoint647)

HAnimJoint591.children.append(HAnimJoint635)

HAnimJoint582.children.append(HAnimJoint591)

HAnimJoint438.children.append(HAnimJoint582)

HAnimJoint423.children.append(HAnimJoint438)

HAnimJoint405.children.append(HAnimJoint423)

HAnimJoint104.children.append(HAnimJoint405)

HAnimJoint52.children.append(HAnimJoint104)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.DEF = "hanim_vl5"
HAnimJoint669.name = "vl5"
HAnimJoint669.center = [0.0028,1.0568,-0.0776]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.DEF = "hanim_l5"
HAnimSegment670.name = "l5"
Transform671 = x3d.Transform()
Transform671.translation = [0.0028,1.0568,-0.0776]
Transform672 = x3d.Transform()
""" Empty Transform """
Shape673 = x3d.Shape()
Shape673.USE = "HAnimJointShape"

Transform672.children.append(Shape673)

Transform671.children.append(Transform672)

HAnimSegment670.children.append(Transform671)
Shape674 = x3d.Shape()
LineSet675 = x3d.LineSet()
LineSet675.vertexCount = [2]
Coordinate676 = x3d.Coordinate()

LineSet675.coord = Coordinate676
""" from vl5 to vl4 vertices 2"""
ColorRGBA677 = x3d.ColorRGBA()
ColorRGBA677.USE = "HAnimSegmentLineColorRGBA"

LineSet675.color = ColorRGBA677

Shape674.geometry = LineSet675

HAnimSegment670.children.append(Shape674)

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint678 = x3d.HAnimJoint()
HAnimJoint678.DEF = "hanim_vl4"
HAnimJoint678.name = "vl4"
HAnimJoint678.center = [0.0035,1.0925,-0.0787]
HAnimSegment679 = x3d.HAnimSegment()
HAnimSegment679.DEF = "hanim_l4"
HAnimSegment679.name = "l4"
Transform680 = x3d.Transform()
Transform680.translation = [0.0035,1.0925,-0.0787]
Transform681 = x3d.Transform()
""" Empty Transform """
Shape682 = x3d.Shape()
Shape682.USE = "HAnimJointShape"

Transform681.children.append(Shape682)

Transform680.children.append(Transform681)

HAnimSegment679.children.append(Transform680)
Shape683 = x3d.Shape()
LineSet684 = x3d.LineSet()
LineSet684.vertexCount = [2]
Coordinate685 = x3d.Coordinate()

LineSet684.coord = Coordinate685
""" from vl4 to vl3 vertices 2"""
ColorRGBA686 = x3d.ColorRGBA()
ColorRGBA686.USE = "HAnimSegmentLineColorRGBA"

LineSet684.color = ColorRGBA686

Shape683.geometry = LineSet684

HAnimSegment679.children.append(Shape683)

HAnimJoint678.children.append(HAnimSegment679)
HAnimJoint687 = x3d.HAnimJoint()
HAnimJoint687.DEF = "hanim_vl3"
HAnimJoint687.name = "vl3"
HAnimJoint687.center = [0.0041,1.1276,-0.0796]
HAnimSegment688 = x3d.HAnimSegment()
HAnimSegment688.DEF = "hanim_l3"
HAnimSegment688.name = "l3"
Transform689 = x3d.Transform()
Transform689.translation = [0.0041,1.1276,-0.0796]
Transform690 = x3d.Transform()
""" Empty Transform """
Shape691 = x3d.Shape()
Shape691.USE = "HAnimJointShape"

Transform690.children.append(Shape691)

Transform689.children.append(Transform690)

HAnimSegment688.children.append(Transform689)
Shape692 = x3d.Shape()
LineSet693 = x3d.LineSet()
LineSet693.vertexCount = [2]
Coordinate694 = x3d.Coordinate()

LineSet693.coord = Coordinate694
""" from vl3 to vl2 vertices 2"""
ColorRGBA695 = x3d.ColorRGBA()
ColorRGBA695.USE = "HAnimSegmentLineColorRGBA"

LineSet693.color = ColorRGBA695

Shape692.geometry = LineSet693

HAnimSegment688.children.append(Shape692)
HAnimSite696 = x3d.HAnimSite()
HAnimSite696.DEF = "hanim_l_rib10_pt"
HAnimSite696.name = "l_rib10_pt"
HAnimSite696.translation = [0.0871,1.1925,0.0992]
TouchSensor697 = x3d.TouchSensor()
TouchSensor697.description = "HAnimSite l_rib10_pt"

HAnimSite696.children.append(TouchSensor697)
Shape698 = x3d.Shape()
Shape698.USE = "HAnimSiteShape"

HAnimSite696.children.append(Shape698)

HAnimSegment688.children.append(HAnimSite696)
HAnimSite699 = x3d.HAnimSite()
HAnimSite699.DEF = "hanim_r_rib10_pt"
HAnimSite699.name = "r_rib10_pt"
HAnimSite699.translation = [-0.0711,1.1941,0.1016]
TouchSensor700 = x3d.TouchSensor()
TouchSensor700.description = "HAnimSite r_rib10_pt"

HAnimSite699.children.append(TouchSensor700)
Shape701 = x3d.Shape()
Shape701.USE = "HAnimSiteShape"

HAnimSite699.children.append(Shape701)

HAnimSegment688.children.append(HAnimSite699)
HAnimSite702 = x3d.HAnimSite()
HAnimSite702.DEF = "hanim_spine_2_middle_back_pt"
HAnimSite702.name = "spine_2_middle_back_pt"
TouchSensor703 = x3d.TouchSensor()
TouchSensor703.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite702.children.append(TouchSensor703)
Shape704 = x3d.Shape()
Shape704.USE = "HAnimSiteShape"

HAnimSite702.children.append(Shape704)

HAnimSegment688.children.append(HAnimSite702)

HAnimJoint687.children.append(HAnimSegment688)
HAnimJoint705 = x3d.HAnimJoint()
HAnimJoint705.DEF = "hanim_vl2"
HAnimJoint705.name = "vl2"
HAnimJoint705.center = [0.0045,1.1546,-0.0800]
HAnimSegment706 = x3d.HAnimSegment()
HAnimSegment706.DEF = "hanim_l2"
HAnimSegment706.name = "l2"
Transform707 = x3d.Transform()
Transform707.translation = [0.0045,1.1546,-0.0800]
Transform708 = x3d.Transform()
""" Empty Transform """
Shape709 = x3d.Shape()
Shape709.USE = "HAnimJointShape"

Transform708.children.append(Shape709)

Transform707.children.append(Transform708)

HAnimSegment706.children.append(Transform707)
Shape710 = x3d.Shape()
LineSet711 = x3d.LineSet()
LineSet711.vertexCount = [2]
Coordinate712 = x3d.Coordinate()

LineSet711.coord = Coordinate712
""" from vl2 to vl1 vertices 2"""
ColorRGBA713 = x3d.ColorRGBA()
ColorRGBA713.USE = "HAnimSegmentLineColorRGBA"

LineSet711.color = ColorRGBA713

Shape710.geometry = LineSet711

HAnimSegment706.children.append(Shape710)

HAnimJoint705.children.append(HAnimSegment706)
HAnimJoint714 = x3d.HAnimJoint()
HAnimJoint714.DEF = "hanim_vl1"
HAnimJoint714.name = "vl1"
HAnimJoint714.center = [0.0048,1.1912,-0.0805]
HAnimSegment715 = x3d.HAnimSegment()
HAnimSegment715.DEF = "hanim_l1"
HAnimSegment715.name = "l1"
Transform716 = x3d.Transform()
Transform716.translation = [0.0048,1.1912,-0.0805]
Transform717 = x3d.Transform()
""" Empty Transform """
Shape718 = x3d.Shape()
Shape718.USE = "HAnimJointShape"

Transform717.children.append(Shape718)

Transform716.children.append(Transform717)

HAnimSegment715.children.append(Transform716)
Shape719 = x3d.Shape()
LineSet720 = x3d.LineSet()
LineSet720.vertexCount = [2]
Coordinate721 = x3d.Coordinate()

LineSet720.coord = Coordinate721
""" from vl1 to vt12 vertices 2"""
ColorRGBA722 = x3d.ColorRGBA()
ColorRGBA722.USE = "HAnimSegmentLineColorRGBA"

LineSet720.color = ColorRGBA722

Shape719.geometry = LineSet720

HAnimSegment715.children.append(Shape719)

HAnimJoint714.children.append(HAnimSegment715)
HAnimJoint723 = x3d.HAnimJoint()
HAnimJoint723.DEF = "hanim_vt12"
HAnimJoint723.name = "vt12"
HAnimJoint723.center = [0.0051,1.2278,-0.0808]
HAnimSegment724 = x3d.HAnimSegment()
HAnimSegment724.DEF = "hanim_t12"
HAnimSegment724.name = "t12"
Transform725 = x3d.Transform()
Transform725.translation = [0.0051,1.2278,-0.0808]
Transform726 = x3d.Transform()
""" Empty Transform """
Shape727 = x3d.Shape()
Shape727.USE = "HAnimJointShape"

Transform726.children.append(Shape727)

Transform725.children.append(Transform726)

HAnimSegment724.children.append(Transform725)
Shape728 = x3d.Shape()
LineSet729 = x3d.LineSet()
LineSet729.vertexCount = [2]
Coordinate730 = x3d.Coordinate()

LineSet729.coord = Coordinate730
""" from vt12 to vt11 vertices 2"""
ColorRGBA731 = x3d.ColorRGBA()
ColorRGBA731.USE = "HAnimSegmentLineColorRGBA"

LineSet729.color = ColorRGBA731

Shape728.geometry = LineSet729

HAnimSegment724.children.append(Shape728)

HAnimJoint723.children.append(HAnimSegment724)
HAnimJoint732 = x3d.HAnimJoint()
HAnimJoint732.DEF = "hanim_vt11"
HAnimJoint732.name = "vt11"
HAnimJoint732.center = [0.0053,1.2679,-0.0810]
HAnimSegment733 = x3d.HAnimSegment()
HAnimSegment733.DEF = "hanim_t11"
HAnimSegment733.name = "t11"
Transform734 = x3d.Transform()
Transform734.translation = [0.0053,1.2679,-0.0810]
Transform735 = x3d.Transform()
""" Empty Transform """
Shape736 = x3d.Shape()
Shape736.USE = "HAnimJointShape"

Transform735.children.append(Shape736)

Transform734.children.append(Transform735)

HAnimSegment733.children.append(Transform734)
Shape737 = x3d.Shape()
LineSet738 = x3d.LineSet()
LineSet738.vertexCount = [2]
Coordinate739 = x3d.Coordinate()

LineSet738.coord = Coordinate739
""" from vt11 to vt10 vertices 2"""
ColorRGBA740 = x3d.ColorRGBA()
ColorRGBA740.USE = "HAnimSegmentLineColorRGBA"

LineSet738.color = ColorRGBA740

Shape737.geometry = LineSet738

HAnimSegment733.children.append(Shape737)
HAnimSite741 = x3d.HAnimSite()
HAnimSite741.DEF = "hanim_substernale_pt"
HAnimSite741.name = "substernale_pt"
HAnimSite741.translation = [0.0085,1.2995,0.1147]
TouchSensor742 = x3d.TouchSensor()
TouchSensor742.description = "HAnimSite substernale_pt"

HAnimSite741.children.append(TouchSensor742)
Shape743 = x3d.Shape()
Shape743.USE = "HAnimSiteShape"

HAnimSite741.children.append(Shape743)

HAnimSegment733.children.append(HAnimSite741)

HAnimJoint732.children.append(HAnimSegment733)
HAnimJoint744 = x3d.HAnimJoint()
HAnimJoint744.DEF = "hanim_vt10"
HAnimJoint744.name = "vt10"
HAnimJoint744.center = [0.0056,1.2848,-0.0822]
HAnimSegment745 = x3d.HAnimSegment()
HAnimSegment745.DEF = "hanim_t10"
HAnimSegment745.name = "t10"
Transform746 = x3d.Transform()
Transform746.translation = [0.0056,1.2848,-0.0822]
Transform747 = x3d.Transform()
""" Empty Transform """
Shape748 = x3d.Shape()
Shape748.USE = "HAnimJointShape"

Transform747.children.append(Shape748)

Transform746.children.append(Transform747)

HAnimSegment745.children.append(Transform746)
Shape749 = x3d.Shape()
LineSet750 = x3d.LineSet()
LineSet750.vertexCount = [2]
Coordinate751 = x3d.Coordinate()

LineSet750.coord = Coordinate751
""" from vt10 to vt9 vertices 2"""
ColorRGBA752 = x3d.ColorRGBA()
ColorRGBA752.USE = "HAnimSegmentLineColorRGBA"

LineSet750.color = ColorRGBA752

Shape749.geometry = LineSet750

HAnimSegment745.children.append(Shape749)
HAnimSite753 = x3d.HAnimSite()
HAnimSite753.DEF = "hanim_l_thelion_pt"
HAnimSite753.name = "l_thelion_pt"
HAnimSite753.translation = [0.0918,1.3382,0.1192]
TouchSensor754 = x3d.TouchSensor()
TouchSensor754.description = "HAnimSite l_thelion_pt"

HAnimSite753.children.append(TouchSensor754)
Shape755 = x3d.Shape()
Shape755.USE = "HAnimSiteShape"

HAnimSite753.children.append(Shape755)

HAnimSegment745.children.append(HAnimSite753)
HAnimSite756 = x3d.HAnimSite()
HAnimSite756.DEF = "hanim_r_thelion_pt"
HAnimSite756.name = "r_thelion_pt"
HAnimSite756.translation = [-0.0736,1.3385,0.1217]
TouchSensor757 = x3d.TouchSensor()
TouchSensor757.description = "HAnimSite r_thelion_pt"

HAnimSite756.children.append(TouchSensor757)
Shape758 = x3d.Shape()
Shape758.USE = "HAnimSiteShape"

HAnimSite756.children.append(Shape758)

HAnimSegment745.children.append(HAnimSite756)

HAnimJoint744.children.append(HAnimSegment745)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.DEF = "hanim_vt9"
HAnimJoint759.name = "vt9"
HAnimJoint759.center = [0.0057,1.3126,-0.0838]
HAnimSegment760 = x3d.HAnimSegment()
HAnimSegment760.DEF = "hanim_t9"
HAnimSegment760.name = "t9"
Transform761 = x3d.Transform()
Transform761.translation = [0.0057,1.3126,-0.0838]
Transform762 = x3d.Transform()
""" Empty Transform """
Shape763 = x3d.Shape()
Shape763.USE = "HAnimJointShape"

Transform762.children.append(Shape763)

Transform761.children.append(Transform762)

HAnimSegment760.children.append(Transform761)
Shape764 = x3d.Shape()
LineSet765 = x3d.LineSet()
LineSet765.vertexCount = [2]
Coordinate766 = x3d.Coordinate()

LineSet765.coord = Coordinate766
""" from vt9 to vt8 vertices 2"""
ColorRGBA767 = x3d.ColorRGBA()
ColorRGBA767.USE = "HAnimSegmentLineColorRGBA"

LineSet765.color = ColorRGBA767

Shape764.geometry = LineSet765

HAnimSegment760.children.append(Shape764)

HAnimJoint759.children.append(HAnimSegment760)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.DEF = "hanim_vt8"
HAnimJoint768.name = "vt8"
HAnimJoint768.center = [0.0057,1.3382,-0.0845]
HAnimSegment769 = x3d.HAnimSegment()
HAnimSegment769.DEF = "hanim_t8"
HAnimSegment769.name = "t8"
Transform770 = x3d.Transform()
Transform770.translation = [0.0057,1.3382,-0.0845]
Transform771 = x3d.Transform()
""" Empty Transform """
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
""" from vt8 to vt7 vertices 2"""
ColorRGBA776 = x3d.ColorRGBA()
ColorRGBA776.USE = "HAnimSegmentLineColorRGBA"

LineSet774.color = ColorRGBA776

Shape773.geometry = LineSet774

HAnimSegment769.children.append(Shape773)

HAnimJoint768.children.append(HAnimSegment769)
HAnimJoint777 = x3d.HAnimJoint()
HAnimJoint777.DEF = "hanim_vt7"
HAnimJoint777.name = "vt7"
HAnimJoint777.center = [0.0058,1.3625,-0.0833]
HAnimSegment778 = x3d.HAnimSegment()
HAnimSegment778.DEF = "hanim_t7"
HAnimSegment778.name = "t7"
Transform779 = x3d.Transform()
Transform779.translation = [0.0058,1.3625,-0.0833]
Transform780 = x3d.Transform()
""" Empty Transform """
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
""" from vt7 to vt6 vertices 2"""
ColorRGBA785 = x3d.ColorRGBA()
ColorRGBA785.USE = "HAnimSegmentLineColorRGBA"

LineSet783.color = ColorRGBA785

Shape782.geometry = LineSet783

HAnimSegment778.children.append(Shape782)
HAnimSite786 = x3d.HAnimSite()
HAnimSite786.DEF = "hanim_l_chest_midsagittal_plane_pt"
HAnimSite786.name = "l_chest_midsagittal_plane_pt"
TouchSensor787 = x3d.TouchSensor()
TouchSensor787.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite786.children.append(TouchSensor787)
Shape788 = x3d.Shape()
Shape788.USE = "HAnimSiteShape"

HAnimSite786.children.append(Shape788)

HAnimSegment778.children.append(HAnimSite786)
HAnimSite789 = x3d.HAnimSite()
HAnimSite789.DEF = "hanim_mesosternale_pt"
HAnimSite789.name = "mesosternale_pt"
TouchSensor790 = x3d.TouchSensor()
TouchSensor790.description = "HAnimSite mesosternale_pt"

HAnimSite789.children.append(TouchSensor790)
Shape791 = x3d.Shape()
Shape791.USE = "HAnimSiteShape"

HAnimSite789.children.append(Shape791)

HAnimSegment778.children.append(HAnimSite789)
HAnimSite792 = x3d.HAnimSite()
HAnimSite792.DEF = "hanim_r_chest_midsagittal_plane_pt"
HAnimSite792.name = "r_chest_midsagittal_plane_pt"
TouchSensor793 = x3d.TouchSensor()
TouchSensor793.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite792.children.append(TouchSensor793)
Shape794 = x3d.Shape()
Shape794.USE = "HAnimSiteShape"

HAnimSite792.children.append(Shape794)

HAnimSegment778.children.append(HAnimSite792)
HAnimSite795 = x3d.HAnimSite()
HAnimSite795.DEF = "hanim_rear_center_midsagittal_plane_pt"
HAnimSite795.name = "rear_center_midsagittal_plane_pt"
TouchSensor796 = x3d.TouchSensor()
TouchSensor796.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite795.children.append(TouchSensor796)
Shape797 = x3d.Shape()
Shape797.USE = "HAnimSiteShape"

HAnimSite795.children.append(Shape797)

HAnimSegment778.children.append(HAnimSite795)

HAnimJoint777.children.append(HAnimSegment778)
HAnimJoint798 = x3d.HAnimJoint()
HAnimJoint798.DEF = "hanim_vt6"
HAnimJoint798.name = "vt6"
HAnimJoint798.center = [0.0059,1.3866,-0.0800]
HAnimSegment799 = x3d.HAnimSegment()
HAnimSegment799.DEF = "hanim_t6"
HAnimSegment799.name = "t6"
Transform800 = x3d.Transform()
Transform800.translation = [0.0059,1.3866,-0.0800]
Transform801 = x3d.Transform()
""" Empty Transform """
Shape802 = x3d.Shape()
Shape802.USE = "HAnimJointShape"

Transform801.children.append(Shape802)

Transform800.children.append(Transform801)

HAnimSegment799.children.append(Transform800)
Shape803 = x3d.Shape()
LineSet804 = x3d.LineSet()
LineSet804.vertexCount = [2]
Coordinate805 = x3d.Coordinate()

LineSet804.coord = Coordinate805
""" from vt6 to vt5 vertices 2"""
ColorRGBA806 = x3d.ColorRGBA()
ColorRGBA806.USE = "HAnimSegmentLineColorRGBA"

LineSet804.color = ColorRGBA806

Shape803.geometry = LineSet804

HAnimSegment799.children.append(Shape803)
HAnimSite807 = x3d.HAnimSite()
HAnimSite807.DEF = "hanim_spine_1_middle_back_pt"
HAnimSite807.name = "spine_1_middle_back_pt"
TouchSensor808 = x3d.TouchSensor()
TouchSensor808.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite807.children.append(TouchSensor808)
Shape809 = x3d.Shape()
Shape809.USE = "HAnimSiteShape"

HAnimSite807.children.append(Shape809)

HAnimSegment799.children.append(HAnimSite807)

HAnimJoint798.children.append(HAnimSegment799)
HAnimJoint810 = x3d.HAnimJoint()
HAnimJoint810.DEF = "hanim_vt5"
HAnimJoint810.name = "vt5"
HAnimJoint810.center = [0.0060,1.4102,-0.0745]
HAnimSegment811 = x3d.HAnimSegment()
HAnimSegment811.DEF = "hanim_t5"
HAnimSegment811.name = "t5"
Transform812 = x3d.Transform()
Transform812.translation = [0.0060,1.4102,-0.0745]
Transform813 = x3d.Transform()
""" Empty Transform """
Shape814 = x3d.Shape()
Shape814.USE = "HAnimJointShape"

Transform813.children.append(Shape814)

Transform812.children.append(Transform813)

HAnimSegment811.children.append(Transform812)
Shape815 = x3d.Shape()
LineSet816 = x3d.LineSet()
LineSet816.vertexCount = [2]
Coordinate817 = x3d.Coordinate()

LineSet816.coord = Coordinate817
""" from vt5 to vt4 vertices 2"""
ColorRGBA818 = x3d.ColorRGBA()
ColorRGBA818.USE = "HAnimSegmentLineColorRGBA"

LineSet816.color = ColorRGBA818

Shape815.geometry = LineSet816

HAnimSegment811.children.append(Shape815)

HAnimJoint810.children.append(HAnimSegment811)
HAnimJoint819 = x3d.HAnimJoint()
HAnimJoint819.DEF = "hanim_vt4"
HAnimJoint819.name = "vt4"
HAnimJoint819.center = [0.0061,1.4320,-0.0675]
HAnimSegment820 = x3d.HAnimSegment()
HAnimSegment820.DEF = "hanim_t4"
HAnimSegment820.name = "t4"
Transform821 = x3d.Transform()
Transform821.translation = [0.0061,1.4320,-0.0675]
Transform822 = x3d.Transform()
""" Empty Transform """
Shape823 = x3d.Shape()
Shape823.USE = "HAnimJointShape"

Transform822.children.append(Shape823)

Transform821.children.append(Transform822)

HAnimSegment820.children.append(Transform821)
Shape824 = x3d.Shape()
LineSet825 = x3d.LineSet()
LineSet825.vertexCount = [2]
Coordinate826 = x3d.Coordinate()

LineSet825.coord = Coordinate826
""" from vt4 to vt3 vertices 2"""
ColorRGBA827 = x3d.ColorRGBA()
ColorRGBA827.USE = "HAnimSegmentLineColorRGBA"

LineSet825.color = ColorRGBA827

Shape824.geometry = LineSet825

HAnimSegment820.children.append(Shape824)

HAnimJoint819.children.append(HAnimSegment820)
HAnimJoint828 = x3d.HAnimJoint()
HAnimJoint828.DEF = "hanim_vt3"
HAnimJoint828.name = "vt3"
HAnimJoint828.center = [0.0062,1.4583,-0.0570]
HAnimSegment829 = x3d.HAnimSegment()
HAnimSegment829.DEF = "hanim_t3"
HAnimSegment829.name = "t3"
Transform830 = x3d.Transform()
Transform830.translation = [0.0062,1.4583,-0.0570]
Transform831 = x3d.Transform()
""" Empty Transform """
Shape832 = x3d.Shape()
Shape832.USE = "HAnimJointShape"

Transform831.children.append(Shape832)

Transform830.children.append(Transform831)

HAnimSegment829.children.append(Transform830)
Shape833 = x3d.Shape()
LineSet834 = x3d.LineSet()
LineSet834.vertexCount = [2]
Coordinate835 = x3d.Coordinate()

LineSet834.coord = Coordinate835
""" from vt3 to vt2 vertices 2"""
ColorRGBA836 = x3d.ColorRGBA()
ColorRGBA836.USE = "HAnimSegmentLineColorRGBA"

LineSet834.color = ColorRGBA836

Shape833.geometry = LineSet834

HAnimSegment829.children.append(Shape833)

HAnimJoint828.children.append(HAnimSegment829)
HAnimJoint837 = x3d.HAnimJoint()
HAnimJoint837.DEF = "hanim_vt2"
HAnimJoint837.name = "vt2"
HAnimJoint837.center = [0.0063,1.4761,-0.0484]
HAnimSegment838 = x3d.HAnimSegment()
HAnimSegment838.DEF = "hanim_t2"
HAnimSegment838.name = "t2"
Transform839 = x3d.Transform()
Transform839.translation = [0.0063,1.4761,-0.0484]
Transform840 = x3d.Transform()
""" Empty Transform """
Shape841 = x3d.Shape()
Shape841.USE = "HAnimJointShape"

Transform840.children.append(Shape841)

Transform839.children.append(Transform840)

HAnimSegment838.children.append(Transform839)
Shape842 = x3d.Shape()
LineSet843 = x3d.LineSet()
LineSet843.vertexCount = [2]
Coordinate844 = x3d.Coordinate()

LineSet843.coord = Coordinate844
""" from vt2 to vt1 vertices 2"""
ColorRGBA845 = x3d.ColorRGBA()
ColorRGBA845.USE = "HAnimSegmentLineColorRGBA"

LineSet843.color = ColorRGBA845

Shape842.geometry = LineSet843

HAnimSegment838.children.append(Shape842)
HAnimSite846 = x3d.HAnimSite()
HAnimSite846.DEF = "hanim_cervicale_pt"
HAnimSite846.name = "cervicale_pt"
HAnimSite846.translation = [0.0064,1.520,-0.0815]
TouchSensor847 = x3d.TouchSensor()
TouchSensor847.description = "HAnimSite cervicale_pt"

HAnimSite846.children.append(TouchSensor847)
Shape848 = x3d.Shape()
Shape848.USE = "HAnimSiteShape"

HAnimSite846.children.append(Shape848)

HAnimSegment838.children.append(HAnimSite846)
HAnimSite849 = x3d.HAnimSite()
HAnimSite849.DEF = "hanim_suprasternale_pt"
HAnimSite849.name = "suprasternale_pt"
HAnimSite849.translation = [0.0084,1.4714,0.0551]
TouchSensor850 = x3d.TouchSensor()
TouchSensor850.description = "HAnimSite suprasternale_pt"

HAnimSite849.children.append(TouchSensor850)
Shape851 = x3d.Shape()
Shape851.USE = "HAnimSiteShape"

HAnimSite849.children.append(Shape851)

HAnimSegment838.children.append(HAnimSite849)

HAnimJoint837.children.append(HAnimSegment838)
HAnimJoint852 = x3d.HAnimJoint()
HAnimJoint852.DEF = "hanim_vt1"
HAnimJoint852.name = "vt1"
HAnimJoint852.center = [0.0065,1.4951,-0.0387]
HAnimSegment853 = x3d.HAnimSegment()
HAnimSegment853.DEF = "hanim_t1"
HAnimSegment853.name = "t1"
Transform854 = x3d.Transform()
Transform854.translation = [0.0065,1.4951,-0.0387]
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
""" from vt1 to vc7 vertices 2"""
ColorRGBA860 = x3d.ColorRGBA()
ColorRGBA860.USE = "HAnimSegmentLineColorRGBA"

LineSet858.color = ColorRGBA860

Shape857.geometry = LineSet858

HAnimSegment853.children.append(Shape857)
HAnimSite861 = x3d.HAnimSite()
HAnimSite861.DEF = "hanim_l_neck_base_pt"
HAnimSite861.name = "l_neck_base_pt"
HAnimSite861.translation = [0.0646,1.5141,-0.0380]
TouchSensor862 = x3d.TouchSensor()
TouchSensor862.description = "HAnimSite l_neck_base_pt"

HAnimSite861.children.append(TouchSensor862)
Shape863 = x3d.Shape()
Shape863.USE = "HAnimSiteShape"

HAnimSite861.children.append(Shape863)

HAnimSegment853.children.append(HAnimSite861)
HAnimSite864 = x3d.HAnimSite()
HAnimSite864.DEF = "hanim_r_neck_base_pt"
HAnimSite864.name = "r_neck_base_pt"
HAnimSite864.translation = [-0.0419,1.5149,-0.0220]
TouchSensor865 = x3d.TouchSensor()
TouchSensor865.description = "HAnimSite r_neck_base_pt"

HAnimSite864.children.append(TouchSensor865)
Shape866 = x3d.Shape()
Shape866.USE = "HAnimSiteShape"

HAnimSite864.children.append(Shape866)

HAnimSegment853.children.append(HAnimSite864)
Shape867 = x3d.Shape()
LineSet868 = x3d.LineSet()
LineSet868.vertexCount = [2]
Coordinate869 = x3d.Coordinate()

LineSet868.coord = Coordinate869
""" from vt1 to l_sternoclavicular vertices 2"""
ColorRGBA870 = x3d.ColorRGBA()
ColorRGBA870.USE = "HAnimSegmentLineColorRGBA"

LineSet868.color = ColorRGBA870

Shape867.geometry = LineSet868

HAnimSegment853.children.append(Shape867)
HAnimSite871 = x3d.HAnimSite()
HAnimSite871.DEF = "hanim_l_acromion_pt"
HAnimSite871.name = "l_acromion_pt"
HAnimSite871.translation = [0.2032,1.4760,-0.0490]
TouchSensor872 = x3d.TouchSensor()
TouchSensor872.description = "HAnimSite l_acromion_pt"

HAnimSite871.children.append(TouchSensor872)
Shape873 = x3d.Shape()
Shape873.USE = "HAnimSiteShape"

HAnimSite871.children.append(Shape873)

HAnimSegment853.children.append(HAnimSite871)
HAnimSite874 = x3d.HAnimSite()
HAnimSite874.DEF = "hanim_l_axilla_distal_pt"
HAnimSite874.name = "l_axilla_distal_pt"
HAnimSite874.translation = [0.1706,1.4072,-0.0875]
TouchSensor875 = x3d.TouchSensor()
TouchSensor875.description = "HAnimSite l_axilla_distal_pt"

HAnimSite874.children.append(TouchSensor875)
Shape876 = x3d.Shape()
Shape876.USE = "HAnimSiteShape"

HAnimSite874.children.append(Shape876)

HAnimSegment853.children.append(HAnimSite874)
HAnimSite877 = x3d.HAnimSite()
HAnimSite877.DEF = "hanim_l_axilla_posterior_folds_pt"
HAnimSite877.name = "l_axilla_posterior_folds_pt"
TouchSensor878 = x3d.TouchSensor()
TouchSensor878.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite877.children.append(TouchSensor878)
Shape879 = x3d.Shape()
Shape879.USE = "HAnimSiteShape"

HAnimSite877.children.append(Shape879)

HAnimSegment853.children.append(HAnimSite877)
HAnimSite880 = x3d.HAnimSite()
HAnimSite880.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite880.name = "l_axilla_proximal_pt"
HAnimSite880.translation = [0.1777,1.4065,-0.0075]
TouchSensor881 = x3d.TouchSensor()
TouchSensor881.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite880.children.append(TouchSensor881)
Shape882 = x3d.Shape()
Shape882.USE = "HAnimSiteShape"

HAnimSite880.children.append(Shape882)

HAnimSegment853.children.append(HAnimSite880)
HAnimSite883 = x3d.HAnimSite()
HAnimSite883.DEF = "hanim_l_clavicale_pt"
HAnimSite883.name = "l_clavicale_pt"
HAnimSite883.translation = [0.0271,1.4943,0.0394]
TouchSensor884 = x3d.TouchSensor()
TouchSensor884.description = "HAnimSite l_clavicale_pt"

HAnimSite883.children.append(TouchSensor884)
Shape885 = x3d.Shape()
Shape885.USE = "HAnimSiteShape"

HAnimSite883.children.append(Shape885)

HAnimSegment853.children.append(HAnimSite883)
Shape886 = x3d.Shape()
LineSet887 = x3d.LineSet()
LineSet887.vertexCount = [2]
Coordinate888 = x3d.Coordinate()

LineSet887.coord = Coordinate888
""" from vt1 to r_sternoclavicular vertices 2"""
ColorRGBA889 = x3d.ColorRGBA()
ColorRGBA889.USE = "HAnimSegmentLineColorRGBA"

LineSet887.color = ColorRGBA889

Shape886.geometry = LineSet887

HAnimSegment853.children.append(Shape886)
HAnimSite890 = x3d.HAnimSite()
HAnimSite890.DEF = "hanim_r_acromion_pt"
HAnimSite890.name = "r_acromion_pt"
HAnimSite890.translation = [-0.1905,1.4791,-0.0431]
TouchSensor891 = x3d.TouchSensor()
TouchSensor891.description = "HAnimSite r_acromion_pt"

HAnimSite890.children.append(TouchSensor891)
Shape892 = x3d.Shape()
Shape892.USE = "HAnimSiteShape"

HAnimSite890.children.append(Shape892)

HAnimSegment853.children.append(HAnimSite890)
HAnimSite893 = x3d.HAnimSite()
HAnimSite893.DEF = "hanim_r_axilla_distal_pt"
HAnimSite893.name = "r_axilla_distal_pt"
HAnimSite893.translation = [-0.1603,1.4098,-0.0826]
TouchSensor894 = x3d.TouchSensor()
TouchSensor894.description = "HAnimSite r_axilla_distal_pt"

HAnimSite893.children.append(TouchSensor894)
Shape895 = x3d.Shape()
Shape895.USE = "HAnimSiteShape"

HAnimSite893.children.append(Shape895)

HAnimSegment853.children.append(HAnimSite893)
HAnimSite896 = x3d.HAnimSite()
HAnimSite896.DEF = "hanim_r_axilla_posterior_folds_pt"
HAnimSite896.name = "r_axilla_posterior_folds_pt"
TouchSensor897 = x3d.TouchSensor()
TouchSensor897.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite896.children.append(TouchSensor897)
Shape898 = x3d.Shape()
Shape898.USE = "HAnimSiteShape"

HAnimSite896.children.append(Shape898)

HAnimSegment853.children.append(HAnimSite896)
HAnimSite899 = x3d.HAnimSite()
HAnimSite899.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite899.name = "r_axilla_proximal_pt"
HAnimSite899.translation = [-0.1626,1.4072,-0.0031]
TouchSensor900 = x3d.TouchSensor()
TouchSensor900.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite899.children.append(TouchSensor900)
Shape901 = x3d.Shape()
Shape901.USE = "HAnimSiteShape"

HAnimSite899.children.append(Shape901)

HAnimSegment853.children.append(HAnimSite899)
HAnimSite902 = x3d.HAnimSite()
HAnimSite902.DEF = "hanim_r_clavicale_pt"
HAnimSite902.name = "r_clavicale_pt"
HAnimSite902.translation = [-0.0115,1.4943,0.0400]
TouchSensor903 = x3d.TouchSensor()
TouchSensor903.description = "HAnimSite r_clavicale_pt"

HAnimSite902.children.append(TouchSensor903)
Shape904 = x3d.Shape()
Shape904.USE = "HAnimSiteShape"

HAnimSite902.children.append(Shape904)

HAnimSegment853.children.append(HAnimSite902)

HAnimJoint852.children.append(HAnimSegment853)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.DEF = "hanim_vc7"
HAnimJoint905.name = "vc7"
HAnimJoint905.center = [0.0066,1.5132,-0.0301]
HAnimSegment906 = x3d.HAnimSegment()
HAnimSegment906.DEF = "hanim_c7"
HAnimSegment906.name = "c7"
Transform907 = x3d.Transform()
Transform907.translation = [0.0066,1.5132,-0.0301]
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
""" from vc7 to vc6 vertices 2"""
ColorRGBA913 = x3d.ColorRGBA()
ColorRGBA913.USE = "HAnimSegmentLineColorRGBA"

LineSet911.color = ColorRGBA913

Shape910.geometry = LineSet911

HAnimSegment906.children.append(Shape910)

HAnimJoint905.children.append(HAnimSegment906)
HAnimJoint914 = x3d.HAnimJoint()
HAnimJoint914.DEF = "hanim_vc6"
HAnimJoint914.name = "vc6"
HAnimJoint914.center = [0.0066,1.5357,-0.0143]
HAnimSegment915 = x3d.HAnimSegment()
HAnimSegment915.DEF = "hanim_c6"
HAnimSegment915.name = "c6"
Transform916 = x3d.Transform()
Transform916.translation = [0.0066,1.5357,-0.0143]
Transform917 = x3d.Transform()
""" Empty Transform """
Shape918 = x3d.Shape()
Shape918.USE = "HAnimJointShape"

Transform917.children.append(Shape918)

Transform916.children.append(Transform917)

HAnimSegment915.children.append(Transform916)
Shape919 = x3d.Shape()
LineSet920 = x3d.LineSet()
LineSet920.vertexCount = [2]
Coordinate921 = x3d.Coordinate()

LineSet920.coord = Coordinate921
""" from vc6 to vc5 vertices 2"""
ColorRGBA922 = x3d.ColorRGBA()
ColorRGBA922.USE = "HAnimSegmentLineColorRGBA"

LineSet920.color = ColorRGBA922

Shape919.geometry = LineSet920

HAnimSegment915.children.append(Shape919)

HAnimJoint914.children.append(HAnimSegment915)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.DEF = "hanim_vc5"
HAnimJoint923.name = "vc5"
HAnimJoint923.center = [0.0066,1.5520,-0.0082]
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.DEF = "hanim_c5"
HAnimSegment924.name = "c5"
Transform925 = x3d.Transform()
Transform925.translation = [0.0066,1.5520,-0.0082]
Transform926 = x3d.Transform()
""" Empty Transform """
Shape927 = x3d.Shape()
Shape927.USE = "HAnimJointShape"

Transform926.children.append(Shape927)

Transform925.children.append(Transform926)

HAnimSegment924.children.append(Transform925)
Shape928 = x3d.Shape()
LineSet929 = x3d.LineSet()
LineSet929.vertexCount = [2]
Coordinate930 = x3d.Coordinate()

LineSet929.coord = Coordinate930
""" from vc5 to vc4 vertices 2"""
ColorRGBA931 = x3d.ColorRGBA()
ColorRGBA931.USE = "HAnimSegmentLineColorRGBA"

LineSet929.color = ColorRGBA931

Shape928.geometry = LineSet929

HAnimSegment924.children.append(Shape928)

HAnimJoint923.children.append(HAnimSegment924)
HAnimJoint932 = x3d.HAnimJoint()
HAnimJoint932.DEF = "hanim_vc4"
HAnimJoint932.name = "vc4"
HAnimJoint932.center = [0.0066,1.5662,-0.0084]
HAnimSegment933 = x3d.HAnimSegment()
HAnimSegment933.DEF = "hanim_c4"
HAnimSegment933.name = "c4"
Transform934 = x3d.Transform()
Transform934.translation = [0.0066,1.5662,-0.0084]
Transform935 = x3d.Transform()
""" Empty Transform """
Shape936 = x3d.Shape()
Shape936.USE = "HAnimJointShape"

Transform935.children.append(Shape936)

Transform934.children.append(Transform935)

HAnimSegment933.children.append(Transform934)
Shape937 = x3d.Shape()
LineSet938 = x3d.LineSet()
LineSet938.vertexCount = [2]
Coordinate939 = x3d.Coordinate()

LineSet938.coord = Coordinate939
""" from vc4 to vc3 vertices 2"""
ColorRGBA940 = x3d.ColorRGBA()
ColorRGBA940.USE = "HAnimSegmentLineColorRGBA"

LineSet938.color = ColorRGBA940

Shape937.geometry = LineSet938

HAnimSegment933.children.append(Shape937)

HAnimJoint932.children.append(HAnimSegment933)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.DEF = "hanim_vc3"
HAnimJoint941.name = "vc3"
HAnimJoint941.center = [0.0066,1.5800,-0.0103]
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.DEF = "hanim_c3"
HAnimSegment942.name = "c3"
Transform943 = x3d.Transform()
Transform943.translation = [0.0066,1.5800,-0.0103]
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
""" from vc3 to vc2 vertices 2"""
ColorRGBA949 = x3d.ColorRGBA()
ColorRGBA949.USE = "HAnimSegmentLineColorRGBA"

LineSet947.color = ColorRGBA949

Shape946.geometry = LineSet947

HAnimSegment942.children.append(Shape946)
HAnimSite950 = x3d.HAnimSite()
HAnimSite950.DEF = "hanim_adams_apple_pt"
HAnimSite950.name = "adams_apple_pt"
TouchSensor951 = x3d.TouchSensor()
TouchSensor951.description = "HAnimSite adams_apple_pt"

HAnimSite950.children.append(TouchSensor951)
Shape952 = x3d.Shape()
Shape952.USE = "HAnimSiteShape"

HAnimSite950.children.append(Shape952)

HAnimSegment942.children.append(HAnimSite950)

HAnimJoint941.children.append(HAnimSegment942)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.DEF = "hanim_vc2"
HAnimJoint953.name = "vc2"
HAnimJoint953.center = [0.0066,1.5928,-0.0103]
HAnimSegment954 = x3d.HAnimSegment()
HAnimSegment954.DEF = "hanim_c2"
HAnimSegment954.name = "c2"
Transform955 = x3d.Transform()
Transform955.translation = [0.0066,1.5928,-0.0103]
Transform956 = x3d.Transform()
""" Empty Transform """
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
""" from vc2 to vc1 vertices 2"""
ColorRGBA961 = x3d.ColorRGBA()
ColorRGBA961.USE = "HAnimSegmentLineColorRGBA"

LineSet959.color = ColorRGBA961

Shape958.geometry = LineSet959

HAnimSegment954.children.append(Shape958)

HAnimJoint953.children.append(HAnimSegment954)
HAnimJoint962 = x3d.HAnimJoint()
HAnimJoint962.DEF = "hanim_vc1"
HAnimJoint962.name = "vc1"
HAnimJoint962.center = [0.0066,1.6144,-0.0034]
HAnimSegment963 = x3d.HAnimSegment()
HAnimSegment963.DEF = "hanim_c1"
HAnimSegment963.name = "c1"
Transform964 = x3d.Transform()
Transform964.translation = [0.0066,1.6144,-0.0034]
Transform965 = x3d.Transform()
""" Empty Transform """
Shape966 = x3d.Shape()
Shape966.USE = "HAnimJointShape"

Transform965.children.append(Shape966)

Transform964.children.append(Transform965)

HAnimSegment963.children.append(Transform964)
Shape967 = x3d.Shape()
LineSet968 = x3d.LineSet()
LineSet968.vertexCount = [2]
Coordinate969 = x3d.Coordinate()

LineSet968.coord = Coordinate969
""" from vc1 to skullbase vertices 2"""
ColorRGBA970 = x3d.ColorRGBA()
ColorRGBA970.USE = "HAnimSegmentLineColorRGBA"

LineSet968.color = ColorRGBA970

Shape967.geometry = LineSet968

HAnimSegment963.children.append(Shape967)
HAnimSite971 = x3d.HAnimSite()
HAnimSite971.DEF = "hanim_glabella_pt"
HAnimSite971.name = "glabella_pt"
TouchSensor972 = x3d.TouchSensor()
TouchSensor972.description = "HAnimSite glabella_pt"

HAnimSite971.children.append(TouchSensor972)
Shape973 = x3d.Shape()
Shape973.USE = "HAnimSiteShape"

HAnimSite971.children.append(Shape973)

HAnimSegment963.children.append(HAnimSite971)
HAnimSite974 = x3d.HAnimSite()
HAnimSite974.DEF = "hanim_l_ectocanthus_pt"
HAnimSite974.name = "l_ectocanthus_pt"
TouchSensor975 = x3d.TouchSensor()
TouchSensor975.description = "HAnimSite l_ectocanthus_pt"

HAnimSite974.children.append(TouchSensor975)
Shape976 = x3d.Shape()
Shape976.USE = "HAnimSiteShape"

HAnimSite974.children.append(Shape976)

HAnimSegment963.children.append(HAnimSite974)
HAnimSite977 = x3d.HAnimSite()
HAnimSite977.DEF = "hanim_l_infraorbitale_pt"
HAnimSite977.name = "l_infraorbitale_pt"
HAnimSite977.translation = [0.0341,1.6171,0.0752]
TouchSensor978 = x3d.TouchSensor()
TouchSensor978.description = "HAnimSite l_infraorbitale_pt"

HAnimSite977.children.append(TouchSensor978)
Shape979 = x3d.Shape()
Shape979.USE = "HAnimSiteShape"

HAnimSite977.children.append(Shape979)

HAnimSegment963.children.append(HAnimSite977)
HAnimSite980 = x3d.HAnimSite()
HAnimSite980.DEF = "hanim_l_tragion_pt"
HAnimSite980.name = "l_tragion_pt"
HAnimSite980.translation = [0.0739,1.6348,0.0282]
TouchSensor981 = x3d.TouchSensor()
TouchSensor981.description = "HAnimSite l_tragion_pt"

HAnimSite980.children.append(TouchSensor981)
Shape982 = x3d.Shape()
Shape982.USE = "HAnimSiteShape"

HAnimSite980.children.append(Shape982)

HAnimSegment963.children.append(HAnimSite980)
HAnimSite983 = x3d.HAnimSite()
HAnimSite983.DEF = "hanim_nuchale_pt"
HAnimSite983.name = "nuchale_pt"
HAnimSite983.translation = [0.0039,1.5972,-0.0796]
TouchSensor984 = x3d.TouchSensor()
TouchSensor984.description = "HAnimSite nuchale_pt"

HAnimSite983.children.append(TouchSensor984)
Shape985 = x3d.Shape()
Shape985.USE = "HAnimSiteShape"

HAnimSite983.children.append(Shape985)

HAnimSegment963.children.append(HAnimSite983)
HAnimSite986 = x3d.HAnimSite()
HAnimSite986.DEF = "hanim_opisthocranion_pt"
HAnimSite986.name = "opisthocranion_pt"
TouchSensor987 = x3d.TouchSensor()
TouchSensor987.description = "HAnimSite opisthocranion_pt"

HAnimSite986.children.append(TouchSensor987)
Shape988 = x3d.Shape()
Shape988.USE = "HAnimSiteShape"

HAnimSite986.children.append(Shape988)

HAnimSegment963.children.append(HAnimSite986)
HAnimSite989 = x3d.HAnimSite()
HAnimSite989.DEF = "hanim_r_ectocanthus_pt"
HAnimSite989.name = "r_ectocanthus_pt"
TouchSensor990 = x3d.TouchSensor()
TouchSensor990.description = "HAnimSite r_ectocanthus_pt"

HAnimSite989.children.append(TouchSensor990)
Shape991 = x3d.Shape()
Shape991.USE = "HAnimSiteShape"

HAnimSite989.children.append(Shape991)

HAnimSegment963.children.append(HAnimSite989)
HAnimSite992 = x3d.HAnimSite()
HAnimSite992.DEF = "hanim_r_infraorbitale_pt"
HAnimSite992.name = "r_infraorbitale_pt"
HAnimSite992.translation = [-0.0237,1.6171,0.0752]
TouchSensor993 = x3d.TouchSensor()
TouchSensor993.description = "HAnimSite r_infraorbitale_pt"

HAnimSite992.children.append(TouchSensor993)
Shape994 = x3d.Shape()
Shape994.USE = "HAnimSiteShape"

HAnimSite992.children.append(Shape994)

HAnimSegment963.children.append(HAnimSite992)
HAnimSite995 = x3d.HAnimSite()
HAnimSite995.DEF = "hanim_r_tragion_pt"
HAnimSite995.name = "r_tragion_pt"
HAnimSite995.translation = [-0.0646,1.6347,0.0302]
TouchSensor996 = x3d.TouchSensor()
TouchSensor996.description = "HAnimSite r_tragion_pt"

HAnimSite995.children.append(TouchSensor996)
Shape997 = x3d.Shape()
Shape997.USE = "HAnimSiteShape"

HAnimSite995.children.append(Shape997)

HAnimSegment963.children.append(HAnimSite995)
HAnimSite998 = x3d.HAnimSite()
HAnimSite998.DEF = "hanim_sellion_pt"
HAnimSite998.name = "sellion_pt"
HAnimSite998.translation = [0.0058,1.6316,0.0852]
TouchSensor999 = x3d.TouchSensor()
TouchSensor999.description = "HAnimSite sellion_pt"

HAnimSite998.children.append(TouchSensor999)
Shape1000 = x3d.Shape()
Shape1000.USE = "HAnimSiteShape"

HAnimSite998.children.append(Shape1000)

HAnimSegment963.children.append(HAnimSite998)
HAnimSite1001 = x3d.HAnimSite()
HAnimSite1001.DEF = "hanim_skull_vertex_pt"
HAnimSite1001.name = "skull_vertex_pt"
HAnimSite1001.translation = [0.0050,1.7504,0.0055]
TouchSensor1002 = x3d.TouchSensor()
TouchSensor1002.description = "HAnimSite skull_vertex_pt"

HAnimSite1001.children.append(TouchSensor1002)
Shape1003 = x3d.Shape()
Shape1003.USE = "HAnimSiteShape"

HAnimSite1001.children.append(Shape1003)

HAnimSegment963.children.append(HAnimSite1001)

HAnimJoint962.children.append(HAnimSegment963)
HAnimJoint1004 = x3d.HAnimJoint()
HAnimJoint1004.DEF = "hanim_skullbase"
HAnimJoint1004.name = "skullbase"
HAnimJoint1004.center = [0.0044,1.6209,0.0236]
HAnimSegment1005 = x3d.HAnimSegment()
HAnimSegment1005.DEF = "hanim_skull"
HAnimSegment1005.name = "skull"
Transform1006 = x3d.Transform()
Transform1006.translation = [0.0044,1.6209,0.0236]
Transform1007 = x3d.Transform()
""" Empty Transform """
Shape1008 = x3d.Shape()
Shape1008.USE = "HAnimJointShape"

Transform1007.children.append(Shape1008)

Transform1006.children.append(Transform1007)

HAnimSegment1005.children.append(Transform1006)
Shape1009 = x3d.Shape()
LineSet1010 = x3d.LineSet()
LineSet1010.vertexCount = [2]
Coordinate1011 = x3d.Coordinate()

LineSet1010.coord = Coordinate1011
""" from skullbase to l_eyelid_joint vertices 2"""
ColorRGBA1012 = x3d.ColorRGBA()
ColorRGBA1012.USE = "HAnimSegmentLineColorRGBA"

LineSet1010.color = ColorRGBA1012

Shape1009.geometry = LineSet1010

HAnimSegment1005.children.append(Shape1009)
Shape1013 = x3d.Shape()
LineSet1014 = x3d.LineSet()
LineSet1014.vertexCount = [2]
Coordinate1015 = x3d.Coordinate()

LineSet1014.coord = Coordinate1015
""" from skullbase to r_eyelid_joint vertices 2"""
ColorRGBA1016 = x3d.ColorRGBA()
ColorRGBA1016.USE = "HAnimSegmentLineColorRGBA"

LineSet1014.color = ColorRGBA1016

Shape1013.geometry = LineSet1014

HAnimSegment1005.children.append(Shape1013)
Shape1017 = x3d.Shape()
LineSet1018 = x3d.LineSet()
LineSet1018.vertexCount = [2]
Coordinate1019 = x3d.Coordinate()

LineSet1018.coord = Coordinate1019
""" from skullbase to l_eyeball_joint vertices 2"""
ColorRGBA1020 = x3d.ColorRGBA()
ColorRGBA1020.USE = "HAnimSegmentLineColorRGBA"

LineSet1018.color = ColorRGBA1020

Shape1017.geometry = LineSet1018

HAnimSegment1005.children.append(Shape1017)
Shape1021 = x3d.Shape()
LineSet1022 = x3d.LineSet()
LineSet1022.vertexCount = [2]
Coordinate1023 = x3d.Coordinate()

LineSet1022.coord = Coordinate1023
""" from skullbase to r_eyeball_joint vertices 2"""
ColorRGBA1024 = x3d.ColorRGBA()
ColorRGBA1024.USE = "HAnimSegmentLineColorRGBA"

LineSet1022.color = ColorRGBA1024

Shape1021.geometry = LineSet1022

HAnimSegment1005.children.append(Shape1021)
Shape1025 = x3d.Shape()
LineSet1026 = x3d.LineSet()
LineSet1026.vertexCount = [2]
Coordinate1027 = x3d.Coordinate()

LineSet1026.coord = Coordinate1027
""" from skullbase to l_eyebrow_joint vertices 2"""
ColorRGBA1028 = x3d.ColorRGBA()
ColorRGBA1028.USE = "HAnimSegmentLineColorRGBA"

LineSet1026.color = ColorRGBA1028

Shape1025.geometry = LineSet1026

HAnimSegment1005.children.append(Shape1025)
Shape1029 = x3d.Shape()
LineSet1030 = x3d.LineSet()
LineSet1030.vertexCount = [2]
Coordinate1031 = x3d.Coordinate()

LineSet1030.coord = Coordinate1031
""" from skullbase to r_eyebrow_joint vertices 2"""
ColorRGBA1032 = x3d.ColorRGBA()
ColorRGBA1032.USE = "HAnimSegmentLineColorRGBA"

LineSet1030.color = ColorRGBA1032

Shape1029.geometry = LineSet1030

HAnimSegment1005.children.append(Shape1029)
Shape1033 = x3d.Shape()
LineSet1034 = x3d.LineSet()
LineSet1034.vertexCount = [2]
Coordinate1035 = x3d.Coordinate()

LineSet1034.coord = Coordinate1035
""" from skullbase to temporomandibular vertices 2"""
ColorRGBA1036 = x3d.ColorRGBA()
ColorRGBA1036.USE = "HAnimSegmentLineColorRGBA"

LineSet1034.color = ColorRGBA1036

Shape1033.geometry = LineSet1034

HAnimSegment1005.children.append(Shape1033)
HAnimSite1037 = x3d.HAnimSite()
HAnimSite1037.DEF = "hanim_l_gonion_pt"
HAnimSite1037.name = "l_gonion_pt"
HAnimSite1037.translation = [0.0631,1.5530,0.0330]
TouchSensor1038 = x3d.TouchSensor()
TouchSensor1038.description = "HAnimSite l_gonion_pt"

HAnimSite1037.children.append(TouchSensor1038)
Shape1039 = x3d.Shape()
Shape1039.USE = "HAnimSiteShape"

HAnimSite1037.children.append(Shape1039)

HAnimSegment1005.children.append(HAnimSite1037)
HAnimSite1040 = x3d.HAnimSite()
HAnimSite1040.DEF = "hanim_menton_pt"
HAnimSite1040.name = "menton_pt"
TouchSensor1041 = x3d.TouchSensor()
TouchSensor1041.description = "HAnimSite menton_pt"

HAnimSite1040.children.append(TouchSensor1041)
Shape1042 = x3d.Shape()
Shape1042.USE = "HAnimSiteShape"

HAnimSite1040.children.append(Shape1042)

HAnimSegment1005.children.append(HAnimSite1040)
HAnimSite1043 = x3d.HAnimSite()
HAnimSite1043.DEF = "hanim_r_gonion_pt"
HAnimSite1043.name = "r_gonion_pt"
HAnimSite1043.translation = [-0.0520,1.5529,0.0347]
TouchSensor1044 = x3d.TouchSensor()
TouchSensor1044.description = "HAnimSite r_gonion_pt"

HAnimSite1043.children.append(TouchSensor1044)
Shape1045 = x3d.Shape()
Shape1045.USE = "HAnimSiteShape"

HAnimSite1043.children.append(Shape1045)

HAnimSegment1005.children.append(HAnimSite1043)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.DEF = "hanim_supramenton_pt"
HAnimSite1046.name = "supramenton_pt"
HAnimSite1046.translation = [0.0061,1.5410,0.0805]
TouchSensor1047 = x3d.TouchSensor()
TouchSensor1047.description = "HAnimSite supramenton_pt"

HAnimSite1046.children.append(TouchSensor1047)
Shape1048 = x3d.Shape()
Shape1048.USE = "HAnimSiteShape"

HAnimSite1046.children.append(Shape1048)

HAnimSegment1005.children.append(HAnimSite1046)

HAnimJoint1004.children.append(HAnimSegment1005)
HAnimJoint1049 = x3d.HAnimJoint()
HAnimJoint1049.DEF = "hanim_l_eyelid_joint"
HAnimJoint1049.name = "l_eyelid_joint"
HAnimJoint1049.center = [0.0503,1.4157,-0.0689]

HAnimJoint1004.children.append(HAnimJoint1049)
HAnimJoint1050 = x3d.HAnimJoint()
HAnimJoint1050.DEF = "hanim_r_eyelid_joint"
HAnimJoint1050.name = "r_eyelid_joint"
HAnimJoint1050.center = [-0.0507,1.4157,-0.0689]

HAnimJoint1004.children.append(HAnimJoint1050)
HAnimJoint1051 = x3d.HAnimJoint()
HAnimJoint1051.DEF = "hanim_l_eyeball_joint"
HAnimJoint1051.name = "l_eyeball_joint"
HAnimJoint1051.center = [0.0479,1.3963,-0.0188]

HAnimJoint1004.children.append(HAnimJoint1051)
HAnimJoint1052 = x3d.HAnimJoint()
HAnimJoint1052.DEF = "hanim_r_eyeball_joint"
HAnimJoint1052.name = "r_eyeball_joint"
HAnimJoint1052.center = [-0.0483,1.3963,-0.0188]

HAnimJoint1004.children.append(HAnimJoint1052)
HAnimJoint1053 = x3d.HAnimJoint()
HAnimJoint1053.DEF = "hanim_l_eyebrow_joint"
HAnimJoint1053.name = "l_eyebrow_joint"
HAnimJoint1053.center = [0.0216,1.4053,0.0051]

HAnimJoint1004.children.append(HAnimJoint1053)
HAnimJoint1054 = x3d.HAnimJoint()
HAnimJoint1054.DEF = "hanim_r_eyebrow_joint"
HAnimJoint1054.name = "r_eyebrow_joint"
HAnimJoint1054.center = [-0.0219,1.4053,0.0051]

HAnimJoint1004.children.append(HAnimJoint1054)
HAnimJoint1055 = x3d.HAnimJoint()
HAnimJoint1055.DEF = "hanim_temporomandibular"
HAnimJoint1055.name = "temporomandibular"
HAnimJoint1055.center = [-0.0002,1.3043,-0.0865]

HAnimJoint1004.children.append(HAnimJoint1055)

HAnimJoint962.children.append(HAnimJoint1004)

HAnimJoint953.children.append(HAnimJoint962)

HAnimJoint941.children.append(HAnimJoint953)

HAnimJoint932.children.append(HAnimJoint941)

HAnimJoint923.children.append(HAnimJoint932)

HAnimJoint914.children.append(HAnimJoint923)

HAnimJoint905.children.append(HAnimJoint914)

HAnimJoint852.children.append(HAnimJoint905)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.DEF = "hanim_l_sternoclavicular"
HAnimJoint1056.name = "l_sternoclavicular"
HAnimJoint1056.center = [0.0820,1.4488,-0.0353]
HAnimSegment1057 = x3d.HAnimSegment()
HAnimSegment1057.DEF = "hanim_l_clavicle"
HAnimSegment1057.name = "l_clavicle"
Transform1058 = x3d.Transform()
Transform1058.translation = [0.0820,1.4488,-0.0353]
Transform1059 = x3d.Transform()
""" Empty Transform """
Shape1060 = x3d.Shape()
Shape1060.USE = "HAnimJointShape"

Transform1059.children.append(Shape1060)

Transform1058.children.append(Transform1059)

HAnimSegment1057.children.append(Transform1058)
Shape1061 = x3d.Shape()
LineSet1062 = x3d.LineSet()
LineSet1062.vertexCount = [2]
Coordinate1063 = x3d.Coordinate()

LineSet1062.coord = Coordinate1063
""" from l_sternoclavicular to l_acromioclavicular vertices 2"""
ColorRGBA1064 = x3d.ColorRGBA()
ColorRGBA1064.USE = "HAnimSegmentLineColorRGBA"

LineSet1062.color = ColorRGBA1064

Shape1061.geometry = LineSet1062

HAnimSegment1057.children.append(Shape1061)

HAnimJoint1056.children.append(HAnimSegment1057)
HAnimJoint1065 = x3d.HAnimJoint()
HAnimJoint1065.DEF = "hanim_l_acromioclavicular"
HAnimJoint1065.name = "l_acromioclavicular"
HAnimJoint1065.center = [0.0962,1.4269,-0.0424]
HAnimSegment1066 = x3d.HAnimSegment()
HAnimSegment1066.DEF = "hanim_l_scapula"
HAnimSegment1066.name = "l_scapula"
Transform1067 = x3d.Transform()
Transform1067.translation = [0.0962,1.4269,-0.0424]
Transform1068 = x3d.Transform()
""" Empty Transform """
Shape1069 = x3d.Shape()
Shape1069.USE = "HAnimJointShape"

Transform1068.children.append(Shape1069)

Transform1067.children.append(Transform1068)

HAnimSegment1066.children.append(Transform1067)
Shape1070 = x3d.Shape()
LineSet1071 = x3d.LineSet()
LineSet1071.vertexCount = [2]
Coordinate1072 = x3d.Coordinate()

LineSet1071.coord = Coordinate1072
""" from l_acromioclavicular to l_shoulder vertices 2"""
ColorRGBA1073 = x3d.ColorRGBA()
ColorRGBA1073.USE = "HAnimSegmentLineColorRGBA"

LineSet1071.color = ColorRGBA1073

Shape1070.geometry = LineSet1071

HAnimSegment1066.children.append(Shape1070)
HAnimSite1074 = x3d.HAnimSite()
HAnimSite1074.DEF = "hanim_l_bideltoid_pt"
HAnimSite1074.name = "l_bideltoid_pt"
TouchSensor1075 = x3d.TouchSensor()
TouchSensor1075.description = "HAnimSite l_bideltoid_pt"

HAnimSite1074.children.append(TouchSensor1075)
Shape1076 = x3d.Shape()
Shape1076.USE = "HAnimSiteShape"

HAnimSite1074.children.append(Shape1076)

HAnimSegment1066.children.append(HAnimSite1074)
HAnimSite1077 = x3d.HAnimSite()
HAnimSite1077.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite1077.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite1077.translation = [0.2280,1.1482,-0.1100]
TouchSensor1078 = x3d.TouchSensor()
TouchSensor1078.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite1077.children.append(TouchSensor1078)
Shape1079 = x3d.Shape()
Shape1079.USE = "HAnimSiteShape"

HAnimSite1077.children.append(Shape1079)

HAnimSegment1066.children.append(HAnimSite1077)

HAnimJoint1065.children.append(HAnimSegment1066)
HAnimJoint1080 = x3d.HAnimJoint()
HAnimJoint1080.DEF = "hanim_l_shoulder"
HAnimJoint1080.name = "l_shoulder"
HAnimJoint1080.center = [0.2029,1.4376,-0.0387]
HAnimSegment1081 = x3d.HAnimSegment()
HAnimSegment1081.DEF = "hanim_l_upperarm"
HAnimSegment1081.name = "l_upperarm"
Transform1082 = x3d.Transform()
Transform1082.translation = [0.2029,1.4376,-0.0387]
Transform1083 = x3d.Transform()
""" Empty Transform """
Shape1084 = x3d.Shape()
Shape1084.USE = "HAnimJointShape"

Transform1083.children.append(Shape1084)

Transform1082.children.append(Transform1083)

HAnimSegment1081.children.append(Transform1082)
Shape1085 = x3d.Shape()
LineSet1086 = x3d.LineSet()
LineSet1086.vertexCount = [2]
Coordinate1087 = x3d.Coordinate()

LineSet1086.coord = Coordinate1087
""" from l_shoulder to l_elbow vertices 2"""
ColorRGBA1088 = x3d.ColorRGBA()
ColorRGBA1088.USE = "HAnimSegmentLineColorRGBA"

LineSet1086.color = ColorRGBA1088

Shape1085.geometry = LineSet1086

HAnimSegment1081.children.append(Shape1085)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite1089.name = "l_humeral_medial_epicondyles_pt"
HAnimSite1089.translation = [0.1735,1.1272,-0.1113]
TouchSensor1090 = x3d.TouchSensor()
TouchSensor1090.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite1089.children.append(TouchSensor1090)
Shape1091 = x3d.Shape()
Shape1091.USE = "HAnimSiteShape"

HAnimSite1089.children.append(Shape1091)

HAnimSegment1081.children.append(HAnimSite1089)
HAnimSite1092 = x3d.HAnimSite()
HAnimSite1092.DEF = "hanim_l_olecranon_pt"
HAnimSite1092.name = "l_olecranon_pt"
HAnimSite1092.translation = [-0.1962,1.1375,-0.1123]
TouchSensor1093 = x3d.TouchSensor()
TouchSensor1093.description = "HAnimSite l_olecranon_pt"

HAnimSite1092.children.append(TouchSensor1093)
Shape1094 = x3d.Shape()
Shape1094.USE = "HAnimSiteShape"

HAnimSite1092.children.append(Shape1094)

HAnimSegment1081.children.append(HAnimSite1092)
HAnimSite1095 = x3d.HAnimSite()
HAnimSite1095.DEF = "hanim_l_radial_styloid_pt"
HAnimSite1095.name = "l_radial_styloid_pt"
HAnimSite1095.translation = [0.1901,0.8645,-0.0415]
TouchSensor1096 = x3d.TouchSensor()
TouchSensor1096.description = "HAnimSite l_radial_styloid_pt"

HAnimSite1095.children.append(TouchSensor1096)
Shape1097 = x3d.Shape()
Shape1097.USE = "HAnimSiteShape"

HAnimSite1095.children.append(Shape1097)

HAnimSegment1081.children.append(HAnimSite1095)
HAnimSite1098 = x3d.HAnimSite()
HAnimSite1098.DEF = "hanim_l_radiale_pt"
HAnimSite1098.name = "l_radiale_pt"
HAnimSite1098.translation = [0.2182,1.1212,-0.1167]
TouchSensor1099 = x3d.TouchSensor()
TouchSensor1099.description = "HAnimSite l_radiale_pt"

HAnimSite1098.children.append(TouchSensor1099)
Shape1100 = x3d.Shape()
Shape1100.USE = "HAnimSiteShape"

HAnimSite1098.children.append(Shape1100)

HAnimSegment1081.children.append(HAnimSite1098)

HAnimJoint1080.children.append(HAnimSegment1081)
HAnimJoint1101 = x3d.HAnimJoint()
HAnimJoint1101.DEF = "hanim_l_elbow"
HAnimJoint1101.name = "l_elbow"
HAnimJoint1101.center = [0.2014,1.1357,-0.0682]
HAnimSegment1102 = x3d.HAnimSegment()
HAnimSegment1102.DEF = "hanim_l_forearm"
HAnimSegment1102.name = "l_forearm"
Transform1103 = x3d.Transform()
Transform1103.translation = [0.2014,1.1357,-0.0682]
Transform1104 = x3d.Transform()
""" Empty Transform """
Shape1105 = x3d.Shape()
Shape1105.USE = "HAnimJointShape"

Transform1104.children.append(Shape1105)

Transform1103.children.append(Transform1104)

HAnimSegment1102.children.append(Transform1103)
Shape1106 = x3d.Shape()
LineSet1107 = x3d.LineSet()
LineSet1107.vertexCount = [2]
Coordinate1108 = x3d.Coordinate()

LineSet1107.coord = Coordinate1108
""" from l_elbow to l_radiocarpal vertices 2"""
ColorRGBA1109 = x3d.ColorRGBA()
ColorRGBA1109.USE = "HAnimSegmentLineColorRGBA"

LineSet1107.color = ColorRGBA1109

Shape1106.geometry = LineSet1107

HAnimSegment1102.children.append(Shape1106)
HAnimSite1110 = x3d.HAnimSite()
HAnimSite1110.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1110.name = "l_ulnar_styloid_pt"
HAnimSite1110.translation = [-0.2142,0.8529,-0.0648]
TouchSensor1111 = x3d.TouchSensor()
TouchSensor1111.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1110.children.append(TouchSensor1111)
Shape1112 = x3d.Shape()
Shape1112.USE = "HAnimSiteShape"

HAnimSite1110.children.append(Shape1112)

HAnimSegment1102.children.append(HAnimSite1110)

HAnimJoint1101.children.append(HAnimSegment1102)
HAnimJoint1113 = x3d.HAnimJoint()
HAnimJoint1113.DEF = "hanim_l_radiocarpal"
HAnimJoint1113.name = "l_radiocarpal"
HAnimJoint1113.center = [0.1984,0.8663,-0.0583]
HAnimSegment1114 = x3d.HAnimSegment()
HAnimSegment1114.DEF = "hanim_l_carpal"
HAnimSegment1114.name = "l_carpal"
Transform1115 = x3d.Transform()
Transform1115.scale = [0.2,0.2,0.2]
Transform1115.translation = [0.20,0.85,-0.05]
Transform1115.rotation = [0,0,1,-3.14]
""" Transform left hand """
Transform1116 = x3d.Transform()
Transform1116.rotation = [0,1,0,-1.57]
""" Transform left hand """
Shape1117 = x3d.Shape()
Shape1117.USE = "HAnimJointShape"

Transform1116.children.append(Shape1117)

Transform1115.children.append(Transform1116)

HAnimSegment1114.children.append(Transform1115)
Shape1118 = x3d.Shape()
LineSet1119 = x3d.LineSet()
LineSet1119.vertexCount = [2]
Coordinate1120 = x3d.Coordinate()

LineSet1119.coord = Coordinate1120
""" from l_radiocarpal to l_midcarpal_1 vertices 2"""
ColorRGBA1121 = x3d.ColorRGBA()
ColorRGBA1121.USE = "HAnimSegmentLineColorRGBA"

LineSet1119.color = ColorRGBA1121

Shape1118.geometry = LineSet1119

HAnimSegment1114.children.append(Shape1118)
Shape1122 = x3d.Shape()
LineSet1123 = x3d.LineSet()
LineSet1123.vertexCount = [2]
Coordinate1124 = x3d.Coordinate()

LineSet1123.coord = Coordinate1124
""" from l_radiocarpal to l_midcarpal_2 vertices 2"""
ColorRGBA1125 = x3d.ColorRGBA()
ColorRGBA1125.USE = "HAnimSegmentLineColorRGBA"

LineSet1123.color = ColorRGBA1125

Shape1122.geometry = LineSet1123

HAnimSegment1114.children.append(Shape1122)
Shape1126 = x3d.Shape()
LineSet1127 = x3d.LineSet()
LineSet1127.vertexCount = [2]
Coordinate1128 = x3d.Coordinate()

LineSet1127.coord = Coordinate1128
""" from l_radiocarpal to l_midcarpal_3 vertices 2"""
ColorRGBA1129 = x3d.ColorRGBA()
ColorRGBA1129.USE = "HAnimSegmentLineColorRGBA"

LineSet1127.color = ColorRGBA1129

Shape1126.geometry = LineSet1127

HAnimSegment1114.children.append(Shape1126)
Shape1130 = x3d.Shape()
LineSet1131 = x3d.LineSet()
LineSet1131.vertexCount = [2]
Coordinate1132 = x3d.Coordinate()

LineSet1131.coord = Coordinate1132
""" from l_radiocarpal to l_midcarpal_4_5 vertices 2"""
ColorRGBA1133 = x3d.ColorRGBA()
ColorRGBA1133.USE = "HAnimSegmentLineColorRGBA"

LineSet1131.color = ColorRGBA1133

Shape1130.geometry = LineSet1131

HAnimSegment1114.children.append(Shape1130)

HAnimJoint1113.children.append(HAnimSegment1114)
HAnimJoint1134 = x3d.HAnimJoint()
HAnimJoint1134.DEF = "hanim_l_midcarpal_1"
HAnimJoint1134.name = "l_midcarpal_1"
HAnimJoint1134.center = [0.1811,0.6975,-0.0826]
HAnimSegment1135 = x3d.HAnimSegment()
HAnimSegment1135.DEF = "hanim_l_trapezium"
HAnimSegment1135.name = "l_trapezium"
Transform1136 = x3d.Transform()
Transform1136.translation = [0.1811,0.6975,-0.0826]
Transform1137 = x3d.Transform()
""" Empty Transform """
Shape1138 = x3d.Shape()
Shape1138.USE = "HAnimJointShape"

Transform1137.children.append(Shape1138)

Transform1136.children.append(Transform1137)

HAnimSegment1135.children.append(Transform1136)
Shape1139 = x3d.Shape()
LineSet1140 = x3d.LineSet()
LineSet1140.vertexCount = [2]
Coordinate1141 = x3d.Coordinate()

LineSet1140.coord = Coordinate1141
""" from l_midcarpal_1 to l_carpometacarpal_1 vertices 2"""
ColorRGBA1142 = x3d.ColorRGBA()
ColorRGBA1142.USE = "HAnimSegmentLineColorRGBA"

LineSet1140.color = ColorRGBA1142

Shape1139.geometry = LineSet1140

HAnimSegment1135.children.append(Shape1139)

HAnimJoint1134.children.append(HAnimSegment1135)
HAnimJoint1143 = x3d.HAnimJoint()
HAnimJoint1143.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint1143.name = "l_carpometacarpal_1"
HAnimJoint1143.center = [0.1924,0.8472,-0.0534]
HAnimSegment1144 = x3d.HAnimSegment()
HAnimSegment1144.DEF = "hanim_l_metacarpal_1"
HAnimSegment1144.name = "l_metacarpal_1"
Transform1145 = x3d.Transform()
Transform1145.translation = [0.1924,0.8472,-0.0534]
Transform1146 = x3d.Transform()
""" Empty Transform """
Shape1147 = x3d.Shape()
Shape1147.USE = "HAnimJointShape"

Transform1146.children.append(Shape1147)

Transform1145.children.append(Transform1146)

HAnimSegment1144.children.append(Transform1145)
Shape1148 = x3d.Shape()
LineSet1149 = x3d.LineSet()
LineSet1149.vertexCount = [2]
Coordinate1150 = x3d.Coordinate()

LineSet1149.coord = Coordinate1150
""" from l_carpometacarpal_1 to l_metacarpophalangeal_1 vertices 2"""
ColorRGBA1151 = x3d.ColorRGBA()
ColorRGBA1151.USE = "HAnimSegmentLineColorRGBA"

LineSet1149.color = ColorRGBA1151

Shape1148.geometry = LineSet1149

HAnimSegment1144.children.append(Shape1148)

HAnimJoint1143.children.append(HAnimSegment1144)
HAnimJoint1152 = x3d.HAnimJoint()
HAnimJoint1152.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint1152.name = "l_metacarpophalangeal_1"
HAnimJoint1152.center = [0.1951,0.8226,0.0246]
HAnimSegment1153 = x3d.HAnimSegment()
HAnimSegment1153.DEF = "hanim_l_carpal_proximal_phalanx_1"
HAnimSegment1153.name = "l_carpal_proximal_phalanx_1"
Transform1154 = x3d.Transform()
Transform1154.translation = [0.1951,0.8226,0.0246]
Transform1155 = x3d.Transform()
""" Empty Transform """
Shape1156 = x3d.Shape()
Shape1156.USE = "HAnimJointShape"

Transform1155.children.append(Shape1156)

Transform1154.children.append(Transform1155)

HAnimSegment1153.children.append(Transform1154)
Shape1157 = x3d.Shape()
LineSet1158 = x3d.LineSet()
LineSet1158.vertexCount = [2]
Coordinate1159 = x3d.Coordinate()

LineSet1158.coord = Coordinate1159
""" from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 vertices 2"""
ColorRGBA1160 = x3d.ColorRGBA()
ColorRGBA1160.USE = "HAnimSegmentLineColorRGBA"

LineSet1158.color = ColorRGBA1160

Shape1157.geometry = LineSet1158

HAnimSegment1153.children.append(Shape1157)
HAnimSite1161 = x3d.HAnimSite()
HAnimSite1161.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite1161.name = "l_carpal_distal_phalanx_1_tip"
TouchSensor1162 = x3d.TouchSensor()
TouchSensor1162.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite1161.children.append(TouchSensor1162)
Shape1163 = x3d.Shape()
Shape1163.USE = "HAnimSiteShape"

HAnimSite1161.children.append(Shape1163)

HAnimSegment1153.children.append(HAnimSite1161)

HAnimJoint1152.children.append(HAnimSegment1153)
HAnimJoint1164 = x3d.HAnimJoint()
HAnimJoint1164.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint1164.name = "l_carpal_interphalangeal_1"
HAnimJoint1164.center = [0.1955,0.8159,0.0464]

HAnimJoint1152.children.append(HAnimJoint1164)

HAnimJoint1143.children.append(HAnimJoint1152)

HAnimJoint1134.children.append(HAnimJoint1143)

HAnimJoint1113.children.append(HAnimJoint1134)
HAnimJoint1165 = x3d.HAnimJoint()
HAnimJoint1165.DEF = "hanim_l_midcarpal_2"
HAnimJoint1165.name = "l_midcarpal_2"
HAnimJoint1165.center = [0.1811,0.6984,-0.0935]
HAnimSegment1166 = x3d.HAnimSegment()
HAnimSegment1166.DEF = "hanim_l_trapezoid"
HAnimSegment1166.name = "l_trapezoid"
Transform1167 = x3d.Transform()
Transform1167.translation = [0.1811,0.6984,-0.0935]
Transform1168 = x3d.Transform()
""" Empty Transform """
Shape1169 = x3d.Shape()
Shape1169.USE = "HAnimJointShape"

Transform1168.children.append(Shape1169)

Transform1167.children.append(Transform1168)

HAnimSegment1166.children.append(Transform1167)
Shape1170 = x3d.Shape()
LineSet1171 = x3d.LineSet()
LineSet1171.vertexCount = [2]
Coordinate1172 = x3d.Coordinate()

LineSet1171.coord = Coordinate1172
""" from l_midcarpal_2 to l_carpometacarpal_2 vertices 2"""
ColorRGBA1173 = x3d.ColorRGBA()
ColorRGBA1173.USE = "HAnimSegmentLineColorRGBA"

LineSet1171.color = ColorRGBA1173

Shape1170.geometry = LineSet1171

HAnimSegment1166.children.append(Shape1170)
HAnimSite1174 = x3d.HAnimSite()
HAnimSite1174.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite1174.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1174.translation = [0.2009,0.8139,-0.0237]
TouchSensor1175 = x3d.TouchSensor()
TouchSensor1175.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite1174.children.append(TouchSensor1175)
Shape1176 = x3d.Shape()
Shape1176.USE = "HAnimSiteShape"

HAnimSite1174.children.append(Shape1176)

HAnimSegment1166.children.append(HAnimSite1174)

HAnimJoint1165.children.append(HAnimSegment1166)
HAnimJoint1177 = x3d.HAnimJoint()
HAnimJoint1177.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint1177.name = "l_carpometacarpal_2"
HAnimJoint1177.center = [0.1983,0.8024,-0.0280]
HAnimSegment1178 = x3d.HAnimSegment()
HAnimSegment1178.DEF = "hanim_l_metacarpal_2"
HAnimSegment1178.name = "l_metacarpal_2"
Transform1179 = x3d.Transform()
Transform1179.translation = [0.1983,0.8024,-0.0280]
Transform1180 = x3d.Transform()
""" Empty Transform """
Shape1181 = x3d.Shape()
Shape1181.USE = "HAnimJointShape"

Transform1180.children.append(Shape1181)

Transform1179.children.append(Transform1180)

HAnimSegment1178.children.append(Transform1179)
Shape1182 = x3d.Shape()
LineSet1183 = x3d.LineSet()
LineSet1183.vertexCount = [2]
Coordinate1184 = x3d.Coordinate()

LineSet1183.coord = Coordinate1184
""" from l_carpometacarpal_2 to l_metacarpophalangeal_2 vertices 2"""
ColorRGBA1185 = x3d.ColorRGBA()
ColorRGBA1185.USE = "HAnimSegmentLineColorRGBA"

LineSet1183.color = ColorRGBA1185

Shape1182.geometry = LineSet1183

HAnimSegment1178.children.append(Shape1182)

HAnimJoint1177.children.append(HAnimSegment1178)
HAnimJoint1186 = x3d.HAnimJoint()
HAnimJoint1186.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint1186.name = "l_metacarpophalangeal_2"
HAnimJoint1186.center = [0.1983,0.7815,-0.0280]
HAnimSegment1187 = x3d.HAnimSegment()
HAnimSegment1187.DEF = "hanim_l_carpal_proximal_phalanx_2 "
HAnimSegment1187.name = "l_carpal_proximal_phalanx_2 "
Transform1188 = x3d.Transform()
Transform1188.translation = [0.1983,0.7815,-0.0280]
Transform1189 = x3d.Transform()
""" Empty Transform """
Shape1190 = x3d.Shape()
Shape1190.USE = "HAnimJointShape"

Transform1189.children.append(Shape1190)

Transform1188.children.append(Transform1189)

HAnimSegment1187.children.append(Transform1188)
Shape1191 = x3d.Shape()
LineSet1192 = x3d.LineSet()
LineSet1192.vertexCount = [2]
Coordinate1193 = x3d.Coordinate()

LineSet1192.coord = Coordinate1193
""" from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA1194 = x3d.ColorRGBA()
ColorRGBA1194.USE = "HAnimSegmentLineColorRGBA"

LineSet1192.color = ColorRGBA1194

Shape1191.geometry = LineSet1192

HAnimSegment1187.children.append(Shape1191)

HAnimJoint1186.children.append(HAnimSegment1187)
HAnimJoint1195 = x3d.HAnimJoint()
HAnimJoint1195.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint1195.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1195.center = [0.2017,0.7363,-0.0248]
HAnimSegment1196 = x3d.HAnimSegment()
HAnimSegment1196.DEF = "hanim_l_carpal_middle_phalanx_2"
HAnimSegment1196.name = "l_carpal_middle_phalanx_2"
Transform1197 = x3d.Transform()
Transform1197.translation = [0.2017,0.7363,-0.0248]
Transform1198 = x3d.Transform()
""" Empty Transform """
Shape1199 = x3d.Shape()
Shape1199.USE = "HAnimJointShape"

Transform1198.children.append(Shape1199)

Transform1197.children.append(Transform1198)

HAnimSegment1196.children.append(Transform1197)
Shape1200 = x3d.Shape()
LineSet1201 = x3d.LineSet()
LineSet1201.vertexCount = [2]
Coordinate1202 = x3d.Coordinate()

LineSet1201.coord = Coordinate1202
""" from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 vertices 2"""
ColorRGBA1203 = x3d.ColorRGBA()
ColorRGBA1203.USE = "HAnimSegmentLineColorRGBA"

LineSet1201.color = ColorRGBA1203

Shape1200.geometry = LineSet1201

HAnimSegment1196.children.append(Shape1200)
HAnimSite1204 = x3d.HAnimSite()
HAnimSite1204.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite1204.name = "l_carpal_distal_phalanx_2_tip"
TouchSensor1205 = x3d.TouchSensor()
TouchSensor1205.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite1204.children.append(TouchSensor1205)
Shape1206 = x3d.Shape()
Shape1206.USE = "HAnimSiteShape"

HAnimSite1204.children.append(Shape1206)

HAnimSegment1196.children.append(HAnimSite1204)
HAnimSite1207 = x3d.HAnimSite()
HAnimSite1207.DEF = "hanim_l_dactylion_pt"
HAnimSite1207.name = "l_dactylion_pt"
HAnimSite1207.translation = [0.2056,0.6743,-0.0482]
TouchSensor1208 = x3d.TouchSensor()
TouchSensor1208.description = "HAnimSite l_dactylion_pt"

HAnimSite1207.children.append(TouchSensor1208)
Shape1209 = x3d.Shape()
Shape1209.USE = "HAnimSiteShape"

HAnimSite1207.children.append(Shape1209)

HAnimSegment1196.children.append(HAnimSite1207)

HAnimJoint1195.children.append(HAnimSegment1196)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint1210.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1210.center = [0.2028,0.7139,-0.0236]

HAnimJoint1195.children.append(HAnimJoint1210)

HAnimJoint1186.children.append(HAnimJoint1195)

HAnimJoint1177.children.append(HAnimJoint1186)

HAnimJoint1165.children.append(HAnimJoint1177)

HAnimJoint1113.children.append(HAnimJoint1165)
HAnimJoint1211 = x3d.HAnimJoint()
HAnimJoint1211.DEF = "hanim_l_midcarpal_3"
HAnimJoint1211.name = "l_midcarpal_3"
HAnimJoint1211.center = [0.1809,0.7000,-0.1067]
HAnimSegment1212 = x3d.HAnimSegment()
HAnimSegment1212.DEF = "hanim_l_capitate"
HAnimSegment1212.name = "l_capitate"
Transform1213 = x3d.Transform()
Transform1213.translation = [0.1809,0.7000,-0.1067]
Transform1214 = x3d.Transform()
""" Empty Transform """
Shape1215 = x3d.Shape()
Shape1215.USE = "HAnimJointShape"

Transform1214.children.append(Shape1215)

Transform1213.children.append(Transform1214)

HAnimSegment1212.children.append(Transform1213)
Shape1216 = x3d.Shape()
LineSet1217 = x3d.LineSet()
LineSet1217.vertexCount = [2]
Coordinate1218 = x3d.Coordinate()

LineSet1217.coord = Coordinate1218
""" from l_midcarpal_3 to l_carpometacarpal_3 vertices 2"""
ColorRGBA1219 = x3d.ColorRGBA()
ColorRGBA1219.USE = "HAnimSegmentLineColorRGBA"

LineSet1217.color = ColorRGBA1219

Shape1216.geometry = LineSet1217

HAnimSegment1212.children.append(Shape1216)
HAnimSite1220 = x3d.HAnimSite()
HAnimSite1220.DEF = "hanim_l_metacarpal_phalanx_3_pt"
HAnimSite1220.name = "l_metacarpal_phalanx_3_pt"
TouchSensor1221 = x3d.TouchSensor()
TouchSensor1221.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite1220.children.append(TouchSensor1221)
Shape1222 = x3d.Shape()
Shape1222.USE = "HAnimSiteShape"

HAnimSite1220.children.append(Shape1222)

HAnimSegment1212.children.append(HAnimSite1220)

HAnimJoint1211.children.append(HAnimSegment1212)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint1223.name = "l_carpometacarpal_3"
HAnimJoint1223.center = [0.1987,0.8029,-0.0530]
HAnimSegment1224 = x3d.HAnimSegment()
HAnimSegment1224.DEF = "hanim_l_metacarpal_3"
HAnimSegment1224.name = "l_metacarpal_3"
Transform1225 = x3d.Transform()
Transform1225.translation = [0.1987,0.8029,-0.0530]
Transform1226 = x3d.Transform()
""" Empty Transform """
Shape1227 = x3d.Shape()
Shape1227.USE = "HAnimJointShape"

Transform1226.children.append(Shape1227)

Transform1225.children.append(Transform1226)

HAnimSegment1224.children.append(Transform1225)
Shape1228 = x3d.Shape()
LineSet1229 = x3d.LineSet()
LineSet1229.vertexCount = [2]
Coordinate1230 = x3d.Coordinate()

LineSet1229.coord = Coordinate1230
""" from l_carpometacarpal_3 to l_metacarpophalangeal_3 vertices 2"""
ColorRGBA1231 = x3d.ColorRGBA()
ColorRGBA1231.USE = "HAnimSegmentLineColorRGBA"

LineSet1229.color = ColorRGBA1231

Shape1228.geometry = LineSet1229

HAnimSegment1224.children.append(Shape1228)

HAnimJoint1223.children.append(HAnimSegment1224)
HAnimJoint1232 = x3d.HAnimJoint()
HAnimJoint1232.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint1232.name = "l_metacarpophalangeal_3"
HAnimJoint1232.center = [0.1987,0.7818,-0.0530]
HAnimSegment1233 = x3d.HAnimSegment()
HAnimSegment1233.DEF = "hanim_l_carpal_proximal_phalanx_3"
HAnimSegment1233.name = "l_carpal_proximal_phalanx_3"
Transform1234 = x3d.Transform()
Transform1234.translation = [0.1987,0.7818,-0.0530]
Transform1235 = x3d.Transform()
""" Empty Transform """
Shape1236 = x3d.Shape()
Shape1236.USE = "HAnimJointShape"

Transform1235.children.append(Shape1236)

Transform1234.children.append(Transform1235)

HAnimSegment1233.children.append(Transform1234)
Shape1237 = x3d.Shape()
LineSet1238 = x3d.LineSet()
LineSet1238.vertexCount = [2]
Coordinate1239 = x3d.Coordinate()

LineSet1238.coord = Coordinate1239
""" from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA1240 = x3d.ColorRGBA()
ColorRGBA1240.USE = "HAnimSegmentLineColorRGBA"

LineSet1238.color = ColorRGBA1240

Shape1237.geometry = LineSet1238

HAnimSegment1233.children.append(Shape1237)

HAnimJoint1232.children.append(HAnimSegment1233)
HAnimJoint1241 = x3d.HAnimJoint()
HAnimJoint1241.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint1241.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1241.center = [0.2013,0.7273,-0.0503]
HAnimSegment1242 = x3d.HAnimSegment()
HAnimSegment1242.DEF = "hanim_l_carpal_middle_phalanx_3"
HAnimSegment1242.name = "l_carpal_middle_phalanx_3"
Transform1243 = x3d.Transform()
Transform1243.translation = [0.2013,0.7273,-0.0503]
Transform1244 = x3d.Transform()
""" Empty Transform """
Shape1245 = x3d.Shape()
Shape1245.USE = "HAnimJointShape"

Transform1244.children.append(Shape1245)

Transform1243.children.append(Transform1244)

HAnimSegment1242.children.append(Transform1243)
Shape1246 = x3d.Shape()
LineSet1247 = x3d.LineSet()
LineSet1247.vertexCount = [2]
Coordinate1248 = x3d.Coordinate()

LineSet1247.coord = Coordinate1248
""" from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 vertices 2"""
ColorRGBA1249 = x3d.ColorRGBA()
ColorRGBA1249.USE = "HAnimSegmentLineColorRGBA"

LineSet1247.color = ColorRGBA1249

Shape1246.geometry = LineSet1247

HAnimSegment1242.children.append(Shape1246)
HAnimSite1250 = x3d.HAnimSite()
HAnimSite1250.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite1250.name = "l_carpal_distal_phalanx_3_tip"
TouchSensor1251 = x3d.TouchSensor()
TouchSensor1251.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite1250.children.append(TouchSensor1251)
Shape1252 = x3d.Shape()
Shape1252.USE = "HAnimSiteShape"

HAnimSite1250.children.append(Shape1252)

HAnimSegment1242.children.append(HAnimSite1250)

HAnimJoint1241.children.append(HAnimSegment1242)
HAnimJoint1253 = x3d.HAnimJoint()
HAnimJoint1253.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint1253.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1253.center = [0.2026,0.7011,-0.0494]

HAnimJoint1241.children.append(HAnimJoint1253)

HAnimJoint1232.children.append(HAnimJoint1241)

HAnimJoint1223.children.append(HAnimJoint1232)

HAnimJoint1211.children.append(HAnimJoint1223)

HAnimJoint1113.children.append(HAnimJoint1211)
HAnimJoint1254 = x3d.HAnimJoint()
HAnimJoint1254.DEF = "hanim_l_midcarpal_4_5"
HAnimJoint1254.name = "l_midcarpal_4_5"
HAnimJoint1254.center = [0.1809,0.6973,-0.1276]
HAnimSegment1255 = x3d.HAnimSegment()
HAnimSegment1255.DEF = "hanim_l_hamate"
HAnimSegment1255.name = "l_hamate"
Transform1256 = x3d.Transform()
Transform1256.translation = [0.1809,0.6973,-0.1276]
Transform1257 = x3d.Transform()
""" Empty Transform """
Shape1258 = x3d.Shape()
Shape1258.USE = "HAnimJointShape"

Transform1257.children.append(Shape1258)

Transform1256.children.append(Transform1257)

HAnimSegment1255.children.append(Transform1256)
Shape1259 = x3d.Shape()
LineSet1260 = x3d.LineSet()
LineSet1260.vertexCount = [2]
Coordinate1261 = x3d.Coordinate()

LineSet1260.coord = Coordinate1261
""" from l_midcarpal_4_5 to l_carpometacarpal_4 vertices 2"""
ColorRGBA1262 = x3d.ColorRGBA()
ColorRGBA1262.USE = "HAnimSegmentLineColorRGBA"

LineSet1260.color = ColorRGBA1262

Shape1259.geometry = LineSet1260

HAnimSegment1255.children.append(Shape1259)
Shape1263 = x3d.Shape()
LineSet1264 = x3d.LineSet()
LineSet1264.vertexCount = [2]
Coordinate1265 = x3d.Coordinate()

LineSet1264.coord = Coordinate1265
""" from l_midcarpal_4_5 to l_carpometacarpal_5 vertices 2"""
ColorRGBA1266 = x3d.ColorRGBA()
ColorRGBA1266.USE = "HAnimSegmentLineColorRGBA"

LineSet1264.color = ColorRGBA1266

Shape1263.geometry = LineSet1264

HAnimSegment1255.children.append(Shape1263)
HAnimSite1267 = x3d.HAnimSite()
HAnimSite1267.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite1267.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1267.translation = [0.1929,0.7860,-0.1122]
TouchSensor1268 = x3d.TouchSensor()
TouchSensor1268.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite1267.children.append(TouchSensor1268)
Shape1269 = x3d.Shape()
Shape1269.USE = "HAnimSiteShape"

HAnimSite1267.children.append(Shape1269)

HAnimSegment1255.children.append(HAnimSite1267)

HAnimJoint1254.children.append(HAnimSegment1255)
HAnimJoint1270 = x3d.HAnimJoint()
HAnimJoint1270.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint1270.name = "l_carpometacarpal_4"
HAnimJoint1270.center = [0.1956,0.8019,-0.0794]
HAnimSegment1271 = x3d.HAnimSegment()
HAnimSegment1271.DEF = "hanim_l_metacarpal_4"
HAnimSegment1271.name = "l_metacarpal_4"
Transform1272 = x3d.Transform()
Transform1272.translation = [0.1956,0.8019,-0.0794]
Transform1273 = x3d.Transform()
""" Empty Transform """
Shape1274 = x3d.Shape()
Shape1274.USE = "HAnimJointShape"

Transform1273.children.append(Shape1274)

Transform1272.children.append(Transform1273)

HAnimSegment1271.children.append(Transform1272)
Shape1275 = x3d.Shape()
LineSet1276 = x3d.LineSet()
LineSet1276.vertexCount = [2]
Coordinate1277 = x3d.Coordinate()

LineSet1276.coord = Coordinate1277
""" from l_carpometacarpal_4 to l_metacarpophalangeal_4 vertices 2"""
ColorRGBA1278 = x3d.ColorRGBA()
ColorRGBA1278.USE = "HAnimSegmentLineColorRGBA"

LineSet1276.color = ColorRGBA1278

Shape1275.geometry = LineSet1276

HAnimSegment1271.children.append(Shape1275)

HAnimJoint1270.children.append(HAnimSegment1271)
HAnimJoint1279 = x3d.HAnimJoint()
HAnimJoint1279.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint1279.name = "l_metacarpophalangeal_4"
HAnimJoint1279.center = [0.1956,0.7815,-0.0794]
HAnimSegment1280 = x3d.HAnimSegment()
HAnimSegment1280.DEF = "hanim_l_carpal_proximal_phalanx_4"
HAnimSegment1280.name = "l_carpal_proximal_phalanx_4"
Transform1281 = x3d.Transform()
Transform1281.translation = [0.1956,0.7815,-0.0794]
Transform1282 = x3d.Transform()
""" Empty Transform """
Shape1283 = x3d.Shape()
Shape1283.USE = "HAnimJointShape"

Transform1282.children.append(Shape1283)

Transform1281.children.append(Transform1282)

HAnimSegment1280.children.append(Transform1281)
Shape1284 = x3d.Shape()
LineSet1285 = x3d.LineSet()
LineSet1285.vertexCount = [2]
Coordinate1286 = x3d.Coordinate()

LineSet1285.coord = Coordinate1286
""" from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA1287 = x3d.ColorRGBA()
ColorRGBA1287.USE = "HAnimSegmentLineColorRGBA"

LineSet1285.color = ColorRGBA1287

Shape1284.geometry = LineSet1285

HAnimSegment1280.children.append(Shape1284)

HAnimJoint1279.children.append(HAnimSegment1280)
HAnimJoint1288 = x3d.HAnimJoint()
HAnimJoint1288.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint1288.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1288.center = [0.1973,0.7287,-0.0777]
HAnimSegment1289 = x3d.HAnimSegment()
HAnimSegment1289.DEF = "hanim_l_carpal_middle_phalanx_4"
HAnimSegment1289.name = "l_carpal_middle_phalanx_4"
Transform1290 = x3d.Transform()
Transform1290.translation = [0.1973,0.7287,-0.0777]
Transform1291 = x3d.Transform()
""" Empty Transform """
Shape1292 = x3d.Shape()
Shape1292.USE = "HAnimJointShape"

Transform1291.children.append(Shape1292)

Transform1290.children.append(Transform1291)

HAnimSegment1289.children.append(Transform1290)
Shape1293 = x3d.Shape()
LineSet1294 = x3d.LineSet()
LineSet1294.vertexCount = [2]
Coordinate1295 = x3d.Coordinate()

LineSet1294.coord = Coordinate1295
""" from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 vertices 2"""
ColorRGBA1296 = x3d.ColorRGBA()
ColorRGBA1296.USE = "HAnimSegmentLineColorRGBA"

LineSet1294.color = ColorRGBA1296

Shape1293.geometry = LineSet1294

HAnimSegment1289.children.append(Shape1293)
HAnimSite1297 = x3d.HAnimSite()
HAnimSite1297.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite1297.name = "l_carpal_distal_phalanx_4_tip"
TouchSensor1298 = x3d.TouchSensor()
TouchSensor1298.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite1297.children.append(TouchSensor1298)
Shape1299 = x3d.Shape()
Shape1299.USE = "HAnimSiteShape"

HAnimSite1297.children.append(Shape1299)

HAnimSegment1289.children.append(HAnimSite1297)

HAnimJoint1288.children.append(HAnimSegment1289)
HAnimJoint1300 = x3d.HAnimJoint()
HAnimJoint1300.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint1300.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1300.center = [0.1983,0.7045,-0.0767]

HAnimJoint1288.children.append(HAnimJoint1300)

HAnimJoint1279.children.append(HAnimJoint1288)

HAnimJoint1270.children.append(HAnimJoint1279)

HAnimJoint1254.children.append(HAnimJoint1270)
HAnimJoint1301 = x3d.HAnimJoint()
HAnimJoint1301.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint1301.name = "l_carpometacarpal_5"
HAnimJoint1301.center = [0.1925,0.8066,-0.1036]
HAnimSegment1302 = x3d.HAnimSegment()
HAnimSegment1302.DEF = "hanim_l_metacarpal_5"
HAnimSegment1302.name = "l_metacarpal_5"
Transform1303 = x3d.Transform()
Transform1303.translation = [0.1925,0.8066,-0.1036]
Transform1304 = x3d.Transform()
""" Empty Transform """
Shape1305 = x3d.Shape()
Shape1305.USE = "HAnimJointShape"

Transform1304.children.append(Shape1305)

Transform1303.children.append(Transform1304)

HAnimSegment1302.children.append(Transform1303)
Shape1306 = x3d.Shape()
LineSet1307 = x3d.LineSet()
LineSet1307.vertexCount = [2]
Coordinate1308 = x3d.Coordinate()

LineSet1307.coord = Coordinate1308
""" from l_carpometacarpal_5 to l_metacarpophalangeal_5 vertices 2"""
ColorRGBA1309 = x3d.ColorRGBA()
ColorRGBA1309.USE = "HAnimSegmentLineColorRGBA"

LineSet1307.color = ColorRGBA1309

Shape1306.geometry = LineSet1307

HAnimSegment1302.children.append(Shape1306)

HAnimJoint1301.children.append(HAnimSegment1302)
HAnimJoint1310 = x3d.HAnimJoint()
HAnimJoint1310.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint1310.name = "l_metacarpophalangeal_5"
HAnimJoint1310.center = [0.1925,0.7866,-0.1036]
HAnimSegment1311 = x3d.HAnimSegment()
HAnimSegment1311.DEF = "hanim_l_carpal_proximal_phalanx_5"
HAnimSegment1311.name = "l_carpal_proximal_phalanx_5"
Transform1312 = x3d.Transform()
Transform1312.translation = [0.1925,0.7866,-0.1036]
Transform1313 = x3d.Transform()
""" Empty Transform """
Shape1314 = x3d.Shape()
Shape1314.USE = "HAnimJointShape"

Transform1313.children.append(Shape1314)

Transform1312.children.append(Transform1313)

HAnimSegment1311.children.append(Transform1312)
Shape1315 = x3d.Shape()
LineSet1316 = x3d.LineSet()
LineSet1316.vertexCount = [2]
Coordinate1317 = x3d.Coordinate()

LineSet1316.coord = Coordinate1317
""" from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA1318 = x3d.ColorRGBA()
ColorRGBA1318.USE = "HAnimSegmentLineColorRGBA"

LineSet1316.color = ColorRGBA1318

Shape1315.geometry = LineSet1316

HAnimSegment1311.children.append(Shape1315)

HAnimJoint1310.children.append(HAnimSegment1311)
HAnimJoint1319 = x3d.HAnimJoint()
HAnimJoint1319.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint1319.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1319.center = [0.1938,0.7452,-0.1024]
HAnimSegment1320 = x3d.HAnimSegment()
HAnimSegment1320.DEF = "hanim_l_carpal_middle_phalanx_5"
HAnimSegment1320.name = "l_carpal_middle_phalanx_5"
Transform1321 = x3d.Transform()
Transform1321.translation = [0.1938,0.7452,-0.1024]
Transform1322 = x3d.Transform()
""" Empty Transform """
Shape1323 = x3d.Shape()
Shape1323.USE = "HAnimJointShape"

Transform1322.children.append(Shape1323)

Transform1321.children.append(Transform1322)

HAnimSegment1320.children.append(Transform1321)
Shape1324 = x3d.Shape()
LineSet1325 = x3d.LineSet()
LineSet1325.vertexCount = [2]
Coordinate1326 = x3d.Coordinate()

LineSet1325.coord = Coordinate1326
""" from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 vertices 2"""
ColorRGBA1327 = x3d.ColorRGBA()
ColorRGBA1327.USE = "HAnimSegmentLineColorRGBA"

LineSet1325.color = ColorRGBA1327

Shape1324.geometry = LineSet1325

HAnimSegment1320.children.append(Shape1324)
HAnimSite1328 = x3d.HAnimSite()
HAnimSite1328.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite1328.name = "l_carpal_distal_phalanx_5_tip"
TouchSensor1329 = x3d.TouchSensor()
TouchSensor1329.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite1328.children.append(TouchSensor1329)
Shape1330 = x3d.Shape()
Shape1330.USE = "HAnimSiteShape"

HAnimSite1328.children.append(Shape1330)

HAnimSegment1320.children.append(HAnimSite1328)

HAnimJoint1319.children.append(HAnimSegment1320)
HAnimJoint1331 = x3d.HAnimJoint()
HAnimJoint1331.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint1331.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1331.center = [0.1948,0.7277,-0.1017]

HAnimJoint1319.children.append(HAnimJoint1331)

HAnimJoint1310.children.append(HAnimJoint1319)

HAnimJoint1301.children.append(HAnimJoint1310)

HAnimJoint1254.children.append(HAnimJoint1301)

HAnimJoint1113.children.append(HAnimJoint1254)

HAnimJoint1101.children.append(HAnimJoint1113)

HAnimJoint1080.children.append(HAnimJoint1101)

HAnimJoint1065.children.append(HAnimJoint1080)

HAnimJoint1056.children.append(HAnimJoint1065)

HAnimJoint852.children.append(HAnimJoint1056)
HAnimJoint1332 = x3d.HAnimJoint()
HAnimJoint1332.DEF = "hanim_r_sternoclavicular"
HAnimJoint1332.name = "r_sternoclavicular"
HAnimJoint1332.center = [-0.0694,1.4600,-0.0330]
HAnimSegment1333 = x3d.HAnimSegment()
HAnimSegment1333.DEF = "hanim_r_clavicle"
HAnimSegment1333.name = "r_clavicle"
Transform1334 = x3d.Transform()
Transform1334.translation = [-0.0694,1.4600,-0.0330]
Transform1335 = x3d.Transform()
""" Empty Transform """
Shape1336 = x3d.Shape()
Shape1336.USE = "HAnimJointShape"

Transform1335.children.append(Shape1336)

Transform1334.children.append(Transform1335)

HAnimSegment1333.children.append(Transform1334)
Shape1337 = x3d.Shape()
LineSet1338 = x3d.LineSet()
LineSet1338.vertexCount = [2]
Coordinate1339 = x3d.Coordinate()

LineSet1338.coord = Coordinate1339
""" from r_sternoclavicular to r_acromioclavicular vertices 2"""
ColorRGBA1340 = x3d.ColorRGBA()
ColorRGBA1340.USE = "HAnimSegmentLineColorRGBA"

LineSet1338.color = ColorRGBA1340

Shape1337.geometry = LineSet1338

HAnimSegment1333.children.append(Shape1337)

HAnimJoint1332.children.append(HAnimSegment1333)
HAnimJoint1341 = x3d.HAnimJoint()
HAnimJoint1341.DEF = "hanim_r_acromioclavicular"
HAnimJoint1341.name = "r_acromioclavicular"
HAnimJoint1341.center = [-0.0836,1.4281,-0.0401]
HAnimSegment1342 = x3d.HAnimSegment()
HAnimSegment1342.DEF = "hanim_r_scapula"
HAnimSegment1342.name = "r_scapula"
Transform1343 = x3d.Transform()
Transform1343.translation = [-0.0836,1.4281,-0.0401]
Transform1344 = x3d.Transform()
""" Empty Transform """
Shape1345 = x3d.Shape()
Shape1345.USE = "HAnimJointShape"

Transform1344.children.append(Shape1345)

Transform1343.children.append(Transform1344)

HAnimSegment1342.children.append(Transform1343)
Shape1346 = x3d.Shape()
LineSet1347 = x3d.LineSet()
LineSet1347.vertexCount = [2]
Coordinate1348 = x3d.Coordinate()

LineSet1347.coord = Coordinate1348
""" from r_acromioclavicular to r_shoulder vertices 2"""
ColorRGBA1349 = x3d.ColorRGBA()
ColorRGBA1349.USE = "HAnimSegmentLineColorRGBA"

LineSet1347.color = ColorRGBA1349

Shape1346.geometry = LineSet1347

HAnimSegment1342.children.append(Shape1346)
HAnimSite1350 = x3d.HAnimSite()
HAnimSite1350.DEF = "hanim_r_bideltoid_pt"
HAnimSite1350.name = "r_bideltoid_pt"
TouchSensor1351 = x3d.TouchSensor()
TouchSensor1351.description = "HAnimSite r_bideltoid_pt"

HAnimSite1350.children.append(TouchSensor1351)
Shape1352 = x3d.Shape()
Shape1352.USE = "HAnimSiteShape"

HAnimSite1350.children.append(Shape1352)

HAnimSegment1342.children.append(HAnimSite1350)
HAnimSite1353 = x3d.HAnimSite()
HAnimSite1353.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite1353.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1353.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1354 = x3d.TouchSensor()
TouchSensor1354.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1353.children.append(TouchSensor1354)
Shape1355 = x3d.Shape()
Shape1355.USE = "HAnimSiteShape"

HAnimSite1353.children.append(Shape1355)

HAnimSegment1342.children.append(HAnimSite1353)

HAnimJoint1341.children.append(HAnimSegment1342)
HAnimJoint1356 = x3d.HAnimJoint()
HAnimJoint1356.DEF = "hanim_r_shoulder"
HAnimJoint1356.name = "r_shoulder"
HAnimJoint1356.center = [-0.1907,1.4407,-0.0325]
HAnimSegment1357 = x3d.HAnimSegment()
HAnimSegment1357.DEF = "hanim_r_upperarm"
HAnimSegment1357.name = "r_upperarm"
Transform1358 = x3d.Transform()
Transform1358.translation = [-0.1907,1.4407,-0.0325]
Transform1359 = x3d.Transform()
""" Empty Transform """
Shape1360 = x3d.Shape()
Shape1360.USE = "HAnimJointShape"

Transform1359.children.append(Shape1360)

Transform1358.children.append(Transform1359)

HAnimSegment1357.children.append(Transform1358)
Shape1361 = x3d.Shape()
LineSet1362 = x3d.LineSet()
LineSet1362.vertexCount = [2]
Coordinate1363 = x3d.Coordinate()

LineSet1362.coord = Coordinate1363
""" from r_shoulder to r_elbow vertices 2"""
ColorRGBA1364 = x3d.ColorRGBA()
ColorRGBA1364.USE = "HAnimSegmentLineColorRGBA"

LineSet1362.color = ColorRGBA1364

Shape1361.geometry = LineSet1362

HAnimSegment1357.children.append(Shape1361)
HAnimSite1365 = x3d.HAnimSite()
HAnimSite1365.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite1365.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1365.translation = [-0.1680,1.1298,-0.1062]
TouchSensor1366 = x3d.TouchSensor()
TouchSensor1366.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1365.children.append(TouchSensor1366)
Shape1367 = x3d.Shape()
Shape1367.USE = "HAnimSiteShape"

HAnimSite1365.children.append(Shape1367)

HAnimSegment1357.children.append(HAnimSite1365)
HAnimSite1368 = x3d.HAnimSite()
HAnimSite1368.DEF = "hanim_r_olecranon_pt"
HAnimSite1368.name = "r_olecranon_pt"
HAnimSite1368.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1369 = x3d.TouchSensor()
TouchSensor1369.description = "HAnimSite r_olecranon_pt"

HAnimSite1368.children.append(TouchSensor1369)
Shape1370 = x3d.Shape()
Shape1370.USE = "HAnimSiteShape"

HAnimSite1368.children.append(Shape1370)

HAnimSegment1357.children.append(HAnimSite1368)
HAnimSite1371 = x3d.HAnimSite()
HAnimSite1371.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1371.name = "r_radial_styloid_pt"
HAnimSite1371.translation = [-0.1884,0.8676,-0.0360]
TouchSensor1372 = x3d.TouchSensor()
TouchSensor1372.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1371.children.append(TouchSensor1372)
Shape1373 = x3d.Shape()
Shape1373.USE = "HAnimSiteShape"

HAnimSite1371.children.append(Shape1373)

HAnimSegment1357.children.append(HAnimSite1371)
HAnimSite1374 = x3d.HAnimSite()
HAnimSite1374.DEF = "hanim_r_radiale_pt"
HAnimSite1374.name = "r_radiale_pt"
HAnimSite1374.translation = [-0.2130,1.1305,-0.1091]
TouchSensor1375 = x3d.TouchSensor()
TouchSensor1375.description = "HAnimSite r_radiale_pt"

HAnimSite1374.children.append(TouchSensor1375)
Shape1376 = x3d.Shape()
Shape1376.USE = "HAnimSiteShape"

HAnimSite1374.children.append(Shape1376)

HAnimSegment1357.children.append(HAnimSite1374)

HAnimJoint1356.children.append(HAnimSegment1357)
HAnimJoint1377 = x3d.HAnimJoint()
HAnimJoint1377.DEF = "hanim_r_elbow"
HAnimJoint1377.name = "r_elbow"
HAnimJoint1377.center = [-0.1949,1.1388,-0.0620]
HAnimSegment1378 = x3d.HAnimSegment()
HAnimSegment1378.DEF = "hanim_r_forearm"
HAnimSegment1378.name = "r_forearm"
Transform1379 = x3d.Transform()
Transform1379.translation = [-0.1949,1.1388,-0.0620]
Transform1380 = x3d.Transform()
""" Empty Transform """
Shape1381 = x3d.Shape()
Shape1381.USE = "HAnimJointShape"

Transform1380.children.append(Shape1381)

Transform1379.children.append(Transform1380)

HAnimSegment1378.children.append(Transform1379)
Shape1382 = x3d.Shape()
LineSet1383 = x3d.LineSet()
LineSet1383.vertexCount = [2]
Coordinate1384 = x3d.Coordinate()

LineSet1383.coord = Coordinate1384
""" from r_elbow to r_radiocarpal vertices 2"""
ColorRGBA1385 = x3d.ColorRGBA()
ColorRGBA1385.USE = "HAnimSegmentLineColorRGBA"

LineSet1383.color = ColorRGBA1385

Shape1382.geometry = LineSet1383

HAnimSegment1378.children.append(Shape1382)
HAnimSite1386 = x3d.HAnimSite()
HAnimSite1386.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1386.name = "r_ulnar_styloid_pt"
HAnimSite1386.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1387 = x3d.TouchSensor()
TouchSensor1387.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1386.children.append(TouchSensor1387)
Shape1388 = x3d.Shape()
Shape1388.USE = "HAnimSiteShape"

HAnimSite1386.children.append(Shape1388)

HAnimSegment1378.children.append(HAnimSite1386)

HAnimJoint1377.children.append(HAnimSegment1378)
HAnimJoint1389 = x3d.HAnimJoint()
HAnimJoint1389.DEF = "hanim_r_radiocarpal"
HAnimJoint1389.name = "r_radiocarpal"
HAnimJoint1389.center = [-0.1959,0.8694,-0.0521]
HAnimSegment1390 = x3d.HAnimSegment()
HAnimSegment1390.DEF = "hanim_r_carpal"
HAnimSegment1390.name = "r_carpal"
Transform1391 = x3d.Transform()
Transform1391.scale = [0.2,0.2,0.2]
Transform1391.translation = [-0.20,0.85,-0.05]
Transform1391.rotation = [0,0,1,-3.14]
""" Transform right hand """
Transform1392 = x3d.Transform()
Transform1392.rotation = [0,1,0,1.57]
""" Transform right hand """
Shape1393 = x3d.Shape()
Shape1393.USE = "HAnimJointShape"

Transform1392.children.append(Shape1393)

Transform1391.children.append(Transform1392)

HAnimSegment1390.children.append(Transform1391)
Shape1394 = x3d.Shape()
LineSet1395 = x3d.LineSet()
LineSet1395.vertexCount = [2]
Coordinate1396 = x3d.Coordinate()

LineSet1395.coord = Coordinate1396
""" from r_radiocarpal to r_midcarpal_1 vertices 2"""
ColorRGBA1397 = x3d.ColorRGBA()
ColorRGBA1397.USE = "HAnimSegmentLineColorRGBA"

LineSet1395.color = ColorRGBA1397

Shape1394.geometry = LineSet1395

HAnimSegment1390.children.append(Shape1394)
Shape1398 = x3d.Shape()
LineSet1399 = x3d.LineSet()
LineSet1399.vertexCount = [2]
Coordinate1400 = x3d.Coordinate()

LineSet1399.coord = Coordinate1400
""" from r_radiocarpal to r_midcarpal_2 vertices 2"""
ColorRGBA1401 = x3d.ColorRGBA()
ColorRGBA1401.USE = "HAnimSegmentLineColorRGBA"

LineSet1399.color = ColorRGBA1401

Shape1398.geometry = LineSet1399

HAnimSegment1390.children.append(Shape1398)
Shape1402 = x3d.Shape()
LineSet1403 = x3d.LineSet()
LineSet1403.vertexCount = [2]
Coordinate1404 = x3d.Coordinate()

LineSet1403.coord = Coordinate1404
""" from r_radiocarpal to r_midcarpal_3 vertices 2"""
ColorRGBA1405 = x3d.ColorRGBA()
ColorRGBA1405.USE = "HAnimSegmentLineColorRGBA"

LineSet1403.color = ColorRGBA1405

Shape1402.geometry = LineSet1403

HAnimSegment1390.children.append(Shape1402)
Shape1406 = x3d.Shape()
LineSet1407 = x3d.LineSet()
LineSet1407.vertexCount = [2]
Coordinate1408 = x3d.Coordinate()

LineSet1407.coord = Coordinate1408
""" from r_radiocarpal to r_midcarpal_4_5 vertices 2"""
ColorRGBA1409 = x3d.ColorRGBA()
ColorRGBA1409.USE = "HAnimSegmentLineColorRGBA"

LineSet1407.color = ColorRGBA1409

Shape1406.geometry = LineSet1407

HAnimSegment1390.children.append(Shape1406)

HAnimJoint1389.children.append(HAnimSegment1390)
HAnimJoint1410 = x3d.HAnimJoint()
HAnimJoint1410.DEF = "hanim_r_midcarpal_1"
HAnimJoint1410.name = "r_midcarpal_1"
HAnimJoint1410.center = [-0.1811,0.6975,-0.0826]
HAnimSegment1411 = x3d.HAnimSegment()
HAnimSegment1411.DEF = "hanim_r_trapezium"
HAnimSegment1411.name = "r_trapezium"
Transform1412 = x3d.Transform()
Transform1412.translation = [-0.1811,0.6975,-0.0826]
Transform1413 = x3d.Transform()
""" Empty Transform """
Shape1414 = x3d.Shape()
Shape1414.USE = "HAnimJointShape"

Transform1413.children.append(Shape1414)

Transform1412.children.append(Transform1413)

HAnimSegment1411.children.append(Transform1412)
Shape1415 = x3d.Shape()
LineSet1416 = x3d.LineSet()
LineSet1416.vertexCount = [2]
Coordinate1417 = x3d.Coordinate()

LineSet1416.coord = Coordinate1417
""" from r_midcarpal_1 to r_carpometacarpal_1 vertices 2"""
ColorRGBA1418 = x3d.ColorRGBA()
ColorRGBA1418.USE = "HAnimSegmentLineColorRGBA"

LineSet1416.color = ColorRGBA1418

Shape1415.geometry = LineSet1416

HAnimSegment1411.children.append(Shape1415)

HAnimJoint1410.children.append(HAnimSegment1411)
HAnimJoint1419 = x3d.HAnimJoint()
HAnimJoint1419.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint1419.name = "r_carpometacarpal_1"
HAnimJoint1419.center = [-0.1899,0.8502,-0.0473]
HAnimSegment1420 = x3d.HAnimSegment()
HAnimSegment1420.DEF = "hanim_r_metacarpal_1"
HAnimSegment1420.name = "r_metacarpal_1"
Transform1421 = x3d.Transform()
Transform1421.translation = [-0.1899,0.8502,-0.0473]
Transform1422 = x3d.Transform()
""" Empty Transform """
Shape1423 = x3d.Shape()
Shape1423.USE = "HAnimJointShape"

Transform1422.children.append(Shape1423)

Transform1421.children.append(Transform1422)

HAnimSegment1420.children.append(Transform1421)
Shape1424 = x3d.Shape()
LineSet1425 = x3d.LineSet()
LineSet1425.vertexCount = [2]
Coordinate1426 = x3d.Coordinate()

LineSet1425.coord = Coordinate1426
""" from r_carpometacarpal_1 to r_metacarpophalangeal_1 vertices 2"""
ColorRGBA1427 = x3d.ColorRGBA()
ColorRGBA1427.USE = "HAnimSegmentLineColorRGBA"

LineSet1425.color = ColorRGBA1427

Shape1424.geometry = LineSet1425

HAnimSegment1420.children.append(Shape1424)

HAnimJoint1419.children.append(HAnimSegment1420)
HAnimJoint1428 = x3d.HAnimJoint()
HAnimJoint1428.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint1428.name = "r_metacarpophalangeal_1"
HAnimJoint1428.center = [-0.1874,0.8256,0.0306]
HAnimSegment1429 = x3d.HAnimSegment()
HAnimSegment1429.DEF = "hanim_r_carpal_proximal_phalanx_1"
HAnimSegment1429.name = "r_carpal_proximal_phalanx_1"
Transform1430 = x3d.Transform()
Transform1430.translation = [-0.1874,0.8256,0.0306]
Transform1431 = x3d.Transform()
""" Empty Transform """
Shape1432 = x3d.Shape()
Shape1432.USE = "HAnimJointShape"

Transform1431.children.append(Shape1432)

Transform1430.children.append(Transform1431)

HAnimSegment1429.children.append(Transform1430)
Shape1433 = x3d.Shape()
LineSet1434 = x3d.LineSet()
LineSet1434.vertexCount = [2]
Coordinate1435 = x3d.Coordinate()

LineSet1434.coord = Coordinate1435
""" from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 vertices 2"""
ColorRGBA1436 = x3d.ColorRGBA()
ColorRGBA1436.USE = "HAnimSegmentLineColorRGBA"

LineSet1434.color = ColorRGBA1436

Shape1433.geometry = LineSet1434

HAnimSegment1429.children.append(Shape1433)
HAnimSite1437 = x3d.HAnimSite()
HAnimSite1437.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite1437.name = "r_carpal_distal_phalanx_1_tip"
TouchSensor1438 = x3d.TouchSensor()
TouchSensor1438.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1437.children.append(TouchSensor1438)
Shape1439 = x3d.Shape()
Shape1439.USE = "HAnimSiteShape"

HAnimSite1437.children.append(Shape1439)

HAnimSegment1429.children.append(HAnimSite1437)

HAnimJoint1428.children.append(HAnimSegment1429)
HAnimJoint1440 = x3d.HAnimJoint()
HAnimJoint1440.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1440.name = "r_carpal_interphalangeal_1"
HAnimJoint1440.center = [-0.1864,0.8190,0.0506]

HAnimJoint1428.children.append(HAnimJoint1440)

HAnimJoint1419.children.append(HAnimJoint1428)

HAnimJoint1410.children.append(HAnimJoint1419)

HAnimJoint1389.children.append(HAnimJoint1410)
HAnimJoint1441 = x3d.HAnimJoint()
HAnimJoint1441.DEF = "hanim_r_midcarpal_2"
HAnimJoint1441.name = "r_midcarpal_2"
HAnimJoint1441.center = [-0.1811,0.6984,-0.0935]
HAnimSegment1442 = x3d.HAnimSegment()
HAnimSegment1442.DEF = "hanim_r_trapezoid"
HAnimSegment1442.name = "r_trapezoid"
Transform1443 = x3d.Transform()
Transform1443.translation = [-0.1811,0.6984,-0.0935]
Transform1444 = x3d.Transform()
""" Empty Transform """
Shape1445 = x3d.Shape()
Shape1445.USE = "HAnimJointShape"

Transform1444.children.append(Shape1445)

Transform1443.children.append(Transform1444)

HAnimSegment1442.children.append(Transform1443)
Shape1446 = x3d.Shape()
LineSet1447 = x3d.LineSet()
LineSet1447.vertexCount = [2]
Coordinate1448 = x3d.Coordinate()

LineSet1447.coord = Coordinate1448
""" from r_midcarpal_2 to r_carpometacarpal_2 vertices 2"""
ColorRGBA1449 = x3d.ColorRGBA()
ColorRGBA1449.USE = "HAnimSegmentLineColorRGBA"

LineSet1447.color = ColorRGBA1449

Shape1446.geometry = LineSet1447

HAnimSegment1442.children.append(Shape1446)
HAnimSite1450 = x3d.HAnimSite()
HAnimSite1450.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1450.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1450.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1451 = x3d.TouchSensor()
TouchSensor1451.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1450.children.append(TouchSensor1451)
Shape1452 = x3d.Shape()
Shape1452.USE = "HAnimSiteShape"

HAnimSite1450.children.append(Shape1452)

HAnimSegment1442.children.append(HAnimSite1450)

HAnimJoint1441.children.append(HAnimSegment1442)
HAnimJoint1453 = x3d.HAnimJoint()
HAnimJoint1453.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1453.name = "r_carpometacarpal_2"
HAnimJoint1453.center = [-0.1961,0.8055,-0.0218]
HAnimSegment1454 = x3d.HAnimSegment()
HAnimSegment1454.DEF = "hanim_r_metacarpal_2"
HAnimSegment1454.name = "r_metacarpal_2"
Transform1455 = x3d.Transform()
Transform1455.translation = [-0.1961,0.8055,-0.0218]
Transform1456 = x3d.Transform()
""" Empty Transform """
Shape1457 = x3d.Shape()
Shape1457.USE = "HAnimJointShape"

Transform1456.children.append(Shape1457)

Transform1455.children.append(Transform1456)

HAnimSegment1454.children.append(Transform1455)
Shape1458 = x3d.Shape()
LineSet1459 = x3d.LineSet()
LineSet1459.vertexCount = [2]
Coordinate1460 = x3d.Coordinate()

LineSet1459.coord = Coordinate1460
""" from r_carpometacarpal_2 to r_metacarpophalangeal_2 vertices 2"""
ColorRGBA1461 = x3d.ColorRGBA()
ColorRGBA1461.USE = "HAnimSegmentLineColorRGBA"

LineSet1459.color = ColorRGBA1461

Shape1458.geometry = LineSet1459

HAnimSegment1454.children.append(Shape1458)

HAnimJoint1453.children.append(HAnimSegment1454)
HAnimJoint1462 = x3d.HAnimJoint()
HAnimJoint1462.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1462.name = "r_metacarpophalangeal_2"
HAnimJoint1462.center = [-0.1961,0.7846,-0.0218]
HAnimSegment1463 = x3d.HAnimSegment()
HAnimSegment1463.DEF = "hanim_r_carpal_proximal_phalanx_2 "
HAnimSegment1463.name = "r_carpal_proximal_phalanx_2 "
Transform1464 = x3d.Transform()
Transform1464.translation = [-0.1961,0.7846,-0.0218]
Transform1465 = x3d.Transform()
""" Empty Transform """
Shape1466 = x3d.Shape()
Shape1466.USE = "HAnimJointShape"

Transform1465.children.append(Shape1466)

Transform1464.children.append(Transform1465)

HAnimSegment1463.children.append(Transform1464)
Shape1467 = x3d.Shape()
LineSet1468 = x3d.LineSet()
LineSet1468.vertexCount = [2]
Coordinate1469 = x3d.Coordinate()

LineSet1468.coord = Coordinate1469
""" from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 vertices 2"""
ColorRGBA1470 = x3d.ColorRGBA()
ColorRGBA1470.USE = "HAnimSegmentLineColorRGBA"

LineSet1468.color = ColorRGBA1470

Shape1467.geometry = LineSet1468

HAnimSegment1463.children.append(Shape1467)

HAnimJoint1462.children.append(HAnimSegment1463)
HAnimJoint1471 = x3d.HAnimJoint()
HAnimJoint1471.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1471.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1471.center = [-0.1954,0.7393,-0.0185]
HAnimSegment1472 = x3d.HAnimSegment()
HAnimSegment1472.DEF = "hanim_r_carpal_middle_phalanx_2"
HAnimSegment1472.name = "r_carpal_middle_phalanx_2"
Transform1473 = x3d.Transform()
Transform1473.translation = [-0.1954,0.7393,-0.0185]
Transform1474 = x3d.Transform()
""" Empty Transform """
Shape1475 = x3d.Shape()
Shape1475.USE = "HAnimJointShape"

Transform1474.children.append(Shape1475)

Transform1473.children.append(Transform1474)

HAnimSegment1472.children.append(Transform1473)
Shape1476 = x3d.Shape()
LineSet1477 = x3d.LineSet()
LineSet1477.vertexCount = [2]
Coordinate1478 = x3d.Coordinate()

LineSet1477.coord = Coordinate1478
""" from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 vertices 2"""
ColorRGBA1479 = x3d.ColorRGBA()
ColorRGBA1479.USE = "HAnimSegmentLineColorRGBA"

LineSet1477.color = ColorRGBA1479

Shape1476.geometry = LineSet1477

HAnimSegment1472.children.append(Shape1476)
HAnimSite1480 = x3d.HAnimSite()
HAnimSite1480.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite1480.name = "r_carpal_distal_phalanx_2_tip"
TouchSensor1481 = x3d.TouchSensor()
TouchSensor1481.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1480.children.append(TouchSensor1481)
Shape1482 = x3d.Shape()
Shape1482.USE = "HAnimSiteShape"

HAnimSite1480.children.append(Shape1482)

HAnimSegment1472.children.append(HAnimSite1480)
HAnimSite1483 = x3d.HAnimSite()
HAnimSite1483.DEF = "hanim_r_dactylion_pt"
HAnimSite1483.name = "r_dactylion_pt"
HAnimSite1483.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1484 = x3d.TouchSensor()
TouchSensor1484.description = "HAnimSite r_dactylion_pt"

HAnimSite1483.children.append(TouchSensor1484)
Shape1485 = x3d.Shape()
Shape1485.USE = "HAnimSiteShape"

HAnimSite1483.children.append(Shape1485)

HAnimSegment1472.children.append(HAnimSite1483)

HAnimJoint1471.children.append(HAnimSegment1472)
HAnimJoint1486 = x3d.HAnimJoint()
HAnimJoint1486.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1486.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1486.center = [-0.1945,0.7169,-0.0173]

HAnimJoint1471.children.append(HAnimJoint1486)

HAnimJoint1462.children.append(HAnimJoint1471)

HAnimJoint1453.children.append(HAnimJoint1462)

HAnimJoint1441.children.append(HAnimJoint1453)

HAnimJoint1389.children.append(HAnimJoint1441)
HAnimJoint1487 = x3d.HAnimJoint()
HAnimJoint1487.DEF = "hanim_r_midcarpal_3"
HAnimJoint1487.name = "r_midcarpal_3"
HAnimJoint1487.center = [-0.1809,0.7000,-0.1067]
HAnimSegment1488 = x3d.HAnimSegment()
HAnimSegment1488.DEF = "hanim_r_capitate"
HAnimSegment1488.name = "r_capitate"
Transform1489 = x3d.Transform()
Transform1489.translation = [-0.1809,0.7000,-0.1067]
Transform1490 = x3d.Transform()
""" Empty Transform """
Shape1491 = x3d.Shape()
Shape1491.USE = "HAnimJointShape"

Transform1490.children.append(Shape1491)

Transform1489.children.append(Transform1490)

HAnimSegment1488.children.append(Transform1489)
Shape1492 = x3d.Shape()
LineSet1493 = x3d.LineSet()
LineSet1493.vertexCount = [2]
Coordinate1494 = x3d.Coordinate()

LineSet1493.coord = Coordinate1494
""" from r_midcarpal_3 to r_carpometacarpal_3 vertices 2"""
ColorRGBA1495 = x3d.ColorRGBA()
ColorRGBA1495.USE = "HAnimSegmentLineColorRGBA"

LineSet1493.color = ColorRGBA1495

Shape1492.geometry = LineSet1493

HAnimSegment1488.children.append(Shape1492)
HAnimSite1496 = x3d.HAnimSite()
HAnimSite1496.DEF = "hanim_r_metacarpal_phalanx_3_pt"
HAnimSite1496.name = "r_metacarpal_phalanx_3_pt"
TouchSensor1497 = x3d.TouchSensor()
TouchSensor1497.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1496.children.append(TouchSensor1497)
Shape1498 = x3d.Shape()
Shape1498.USE = "HAnimSiteShape"

HAnimSite1496.children.append(Shape1498)

HAnimSegment1488.children.append(HAnimSite1496)

HAnimJoint1487.children.append(HAnimSegment1488)
HAnimJoint1499 = x3d.HAnimJoint()
HAnimJoint1499.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1499.name = "r_carpometacarpal_3"
HAnimJoint1499.center = [-0.1972,0.8060,-0.0468]
HAnimSegment1500 = x3d.HAnimSegment()
HAnimSegment1500.DEF = "hanim_r_metacarpal_3"
HAnimSegment1500.name = "r_metacarpal_3"
Transform1501 = x3d.Transform()
Transform1501.translation = [-0.1972,0.8060,-0.0468]
Transform1502 = x3d.Transform()
""" Empty Transform """
Shape1503 = x3d.Shape()
Shape1503.USE = "HAnimJointShape"

Transform1502.children.append(Shape1503)

Transform1501.children.append(Transform1502)

HAnimSegment1500.children.append(Transform1501)
Shape1504 = x3d.Shape()
LineSet1505 = x3d.LineSet()
LineSet1505.vertexCount = [2]
Coordinate1506 = x3d.Coordinate()

LineSet1505.coord = Coordinate1506
""" from r_carpometacarpal_3 to r_metacarpophalangeal_3 vertices 2"""
ColorRGBA1507 = x3d.ColorRGBA()
ColorRGBA1507.USE = "HAnimSegmentLineColorRGBA"

LineSet1505.color = ColorRGBA1507

Shape1504.geometry = LineSet1505

HAnimSegment1500.children.append(Shape1504)

HAnimJoint1499.children.append(HAnimSegment1500)
HAnimJoint1508 = x3d.HAnimJoint()
HAnimJoint1508.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1508.name = "r_metacarpophalangeal_3"
HAnimJoint1508.center = [-0.1972,0.7849,-0.0468]
HAnimSegment1509 = x3d.HAnimSegment()
HAnimSegment1509.DEF = "hanim_r_carpal_proximal_phalanx_3"
HAnimSegment1509.name = "r_carpal_proximal_phalanx_3"
Transform1510 = x3d.Transform()
Transform1510.translation = [-0.1972,0.7849,-0.0468]
Transform1511 = x3d.Transform()
""" Empty Transform """
Shape1512 = x3d.Shape()
Shape1512.USE = "HAnimJointShape"

Transform1511.children.append(Shape1512)

Transform1510.children.append(Transform1511)

HAnimSegment1509.children.append(Transform1510)
Shape1513 = x3d.Shape()
LineSet1514 = x3d.LineSet()
LineSet1514.vertexCount = [2]
Coordinate1515 = x3d.Coordinate()

LineSet1514.coord = Coordinate1515
""" from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 vertices 2"""
ColorRGBA1516 = x3d.ColorRGBA()
ColorRGBA1516.USE = "HAnimSegmentLineColorRGBA"

LineSet1514.color = ColorRGBA1516

Shape1513.geometry = LineSet1514

HAnimSegment1509.children.append(Shape1513)

HAnimJoint1508.children.append(HAnimSegment1509)
HAnimJoint1517 = x3d.HAnimJoint()
HAnimJoint1517.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1517.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1517.center = [-0.1950,0.7304,-0.0441]
HAnimSegment1518 = x3d.HAnimSegment()
HAnimSegment1518.DEF = "hanim_r_carpal_middle_phalanx_3"
HAnimSegment1518.name = "r_carpal_middle_phalanx_3"
Transform1519 = x3d.Transform()
Transform1519.translation = [-0.1950,0.7304,-0.0441]
Transform1520 = x3d.Transform()
""" Empty Transform """
Shape1521 = x3d.Shape()
Shape1521.USE = "HAnimJointShape"

Transform1520.children.append(Shape1521)

Transform1519.children.append(Transform1520)

HAnimSegment1518.children.append(Transform1519)
Shape1522 = x3d.Shape()
LineSet1523 = x3d.LineSet()
LineSet1523.vertexCount = [2]
Coordinate1524 = x3d.Coordinate()

LineSet1523.coord = Coordinate1524
""" from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 vertices 2"""
ColorRGBA1525 = x3d.ColorRGBA()
ColorRGBA1525.USE = "HAnimSegmentLineColorRGBA"

LineSet1523.color = ColorRGBA1525

Shape1522.geometry = LineSet1523

HAnimSegment1518.children.append(Shape1522)
HAnimSite1526 = x3d.HAnimSite()
HAnimSite1526.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite1526.name = "r_carpal_distal_phalanx_3_tip"
TouchSensor1527 = x3d.TouchSensor()
TouchSensor1527.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1526.children.append(TouchSensor1527)
Shape1528 = x3d.Shape()
Shape1528.USE = "HAnimSiteShape"

HAnimSite1526.children.append(Shape1528)

HAnimSegment1518.children.append(HAnimSite1526)

HAnimJoint1517.children.append(HAnimSegment1518)
HAnimJoint1529 = x3d.HAnimJoint()
HAnimJoint1529.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1529.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1529.center = [-0.1939,0.7042,-0.0432]

HAnimJoint1517.children.append(HAnimJoint1529)

HAnimJoint1508.children.append(HAnimJoint1517)

HAnimJoint1499.children.append(HAnimJoint1508)

HAnimJoint1487.children.append(HAnimJoint1499)

HAnimJoint1389.children.append(HAnimJoint1487)
HAnimJoint1530 = x3d.HAnimJoint()
HAnimJoint1530.DEF = "hanim_r_midcarpal_4_5"
HAnimJoint1530.name = "r_midcarpal_4_5"
HAnimJoint1530.center = [-0.1809,0.6973,-0.1276]
HAnimSegment1531 = x3d.HAnimSegment()
HAnimSegment1531.DEF = "hanim_r_hamate"
HAnimSegment1531.name = "r_hamate"
Transform1532 = x3d.Transform()
Transform1532.translation = [-0.1809,0.6973,-0.1276]
Transform1533 = x3d.Transform()
""" Empty Transform """
Shape1534 = x3d.Shape()
Shape1534.USE = "HAnimJointShape"

Transform1533.children.append(Shape1534)

Transform1532.children.append(Transform1533)

HAnimSegment1531.children.append(Transform1532)
Shape1535 = x3d.Shape()
LineSet1536 = x3d.LineSet()
LineSet1536.vertexCount = [2]
Coordinate1537 = x3d.Coordinate()

LineSet1536.coord = Coordinate1537
""" from r_midcarpal_4_5 to r_carpometacarpal_4 vertices 2"""
ColorRGBA1538 = x3d.ColorRGBA()
ColorRGBA1538.USE = "HAnimSegmentLineColorRGBA"

LineSet1536.color = ColorRGBA1538

Shape1535.geometry = LineSet1536

HAnimSegment1531.children.append(Shape1535)
Shape1539 = x3d.Shape()
LineSet1540 = x3d.LineSet()
LineSet1540.vertexCount = [2]
Coordinate1541 = x3d.Coordinate()

LineSet1540.coord = Coordinate1541
""" from r_midcarpal_4_5 to r_carpometacarpal_5 vertices 2"""
ColorRGBA1542 = x3d.ColorRGBA()
ColorRGBA1542.USE = "HAnimSegmentLineColorRGBA"

LineSet1540.color = ColorRGBA1542

Shape1539.geometry = LineSet1540

HAnimSegment1531.children.append(Shape1539)
HAnimSite1543 = x3d.HAnimSite()
HAnimSite1543.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1543.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1543.translation = [-0.1929,0.7890,-0.1064]
TouchSensor1544 = x3d.TouchSensor()
TouchSensor1544.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1543.children.append(TouchSensor1544)
Shape1545 = x3d.Shape()
Shape1545.USE = "HAnimSiteShape"

HAnimSite1543.children.append(Shape1545)

HAnimSegment1531.children.append(HAnimSite1543)

HAnimJoint1530.children.append(HAnimSegment1531)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1546.name = "r_carpometacarpal_4"
HAnimJoint1546.center = [-0.1951,0.8049,-0.0732]
HAnimSegment1547 = x3d.HAnimSegment()
HAnimSegment1547.DEF = "hanim_r_metacarpal_4"
HAnimSegment1547.name = "r_metacarpal_4"
Transform1548 = x3d.Transform()
Transform1548.translation = [-0.1951,0.8049,-0.0732]
Transform1549 = x3d.Transform()
""" Empty Transform """
Shape1550 = x3d.Shape()
Shape1550.USE = "HAnimJointShape"

Transform1549.children.append(Shape1550)

Transform1548.children.append(Transform1549)

HAnimSegment1547.children.append(Transform1548)
Shape1551 = x3d.Shape()
LineSet1552 = x3d.LineSet()
LineSet1552.vertexCount = [2]
Coordinate1553 = x3d.Coordinate()

LineSet1552.coord = Coordinate1553
""" from r_carpometacarpal_4 to r_metacarpophalangeal_4 vertices 2"""
ColorRGBA1554 = x3d.ColorRGBA()
ColorRGBA1554.USE = "HAnimSegmentLineColorRGBA"

LineSet1552.color = ColorRGBA1554

Shape1551.geometry = LineSet1552

HAnimSegment1547.children.append(Shape1551)

HAnimJoint1546.children.append(HAnimSegment1547)
HAnimJoint1555 = x3d.HAnimJoint()
HAnimJoint1555.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1555.name = "r_metacarpophalangeal_4"
HAnimJoint1555.center = [-0.1951,0.7845,-0.0732]
HAnimSegment1556 = x3d.HAnimSegment()
HAnimSegment1556.DEF = "hanim_r_carpal_proximal_phalanx_4"
HAnimSegment1556.name = "r_carpal_proximal_phalanx_4"
Transform1557 = x3d.Transform()
Transform1557.translation = [-0.1951,0.7845,-0.0732]
Transform1558 = x3d.Transform()
""" Empty Transform """
Shape1559 = x3d.Shape()
Shape1559.USE = "HAnimJointShape"

Transform1558.children.append(Shape1559)

Transform1557.children.append(Transform1558)

HAnimSegment1556.children.append(Transform1557)
Shape1560 = x3d.Shape()
LineSet1561 = x3d.LineSet()
LineSet1561.vertexCount = [2]
Coordinate1562 = x3d.Coordinate()

LineSet1561.coord = Coordinate1562
""" from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 vertices 2"""
ColorRGBA1563 = x3d.ColorRGBA()
ColorRGBA1563.USE = "HAnimSegmentLineColorRGBA"

LineSet1561.color = ColorRGBA1563

Shape1560.geometry = LineSet1561

HAnimSegment1556.children.append(Shape1560)

HAnimJoint1555.children.append(HAnimSegment1556)
HAnimJoint1564 = x3d.HAnimJoint()
HAnimJoint1564.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1564.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1564.center = [-0.1920,0.7318,-0.0716]
HAnimSegment1565 = x3d.HAnimSegment()
HAnimSegment1565.DEF = "hanim_r_carpal_middle_phalanx_4"
HAnimSegment1565.name = "r_carpal_middle_phalanx_4"
Transform1566 = x3d.Transform()
Transform1566.translation = [-0.1920,0.7318,-0.0716]
Transform1567 = x3d.Transform()
""" Empty Transform """
Shape1568 = x3d.Shape()
Shape1568.USE = "HAnimJointShape"

Transform1567.children.append(Shape1568)

Transform1566.children.append(Transform1567)

HAnimSegment1565.children.append(Transform1566)
Shape1569 = x3d.Shape()
LineSet1570 = x3d.LineSet()
LineSet1570.vertexCount = [2]
Coordinate1571 = x3d.Coordinate()

LineSet1570.coord = Coordinate1571
""" from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 vertices 2"""
ColorRGBA1572 = x3d.ColorRGBA()
ColorRGBA1572.USE = "HAnimSegmentLineColorRGBA"

LineSet1570.color = ColorRGBA1572

Shape1569.geometry = LineSet1570

HAnimSegment1565.children.append(Shape1569)
HAnimSite1573 = x3d.HAnimSite()
HAnimSite1573.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite1573.name = "r_carpal_distal_phalanx_4_tip"
TouchSensor1574 = x3d.TouchSensor()
TouchSensor1574.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1573.children.append(TouchSensor1574)
Shape1575 = x3d.Shape()
Shape1575.USE = "HAnimSiteShape"

HAnimSite1573.children.append(Shape1575)

HAnimSegment1565.children.append(HAnimSite1573)

HAnimJoint1564.children.append(HAnimSegment1565)
HAnimJoint1576 = x3d.HAnimJoint()
HAnimJoint1576.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1576.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1576.center = [-0.1908,0.7077,-0.0706]

HAnimJoint1564.children.append(HAnimJoint1576)

HAnimJoint1555.children.append(HAnimJoint1564)

HAnimJoint1546.children.append(HAnimJoint1555)

HAnimJoint1530.children.append(HAnimJoint1546)
HAnimJoint1577 = x3d.HAnimJoint()
HAnimJoint1577.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1577.name = "r_carpometacarpal_5"
HAnimJoint1577.center = [-0.1926,0.8096,-0.0975]
HAnimSegment1578 = x3d.HAnimSegment()
HAnimSegment1578.DEF = "hanim_r_metacarpal_5"
HAnimSegment1578.name = "r_metacarpal_5"
Transform1579 = x3d.Transform()
Transform1579.translation = [-0.1926,0.8096,-0.0975]
Transform1580 = x3d.Transform()
""" Empty Transform """
Shape1581 = x3d.Shape()
Shape1581.USE = "HAnimJointShape"

Transform1580.children.append(Shape1581)

Transform1579.children.append(Transform1580)

HAnimSegment1578.children.append(Transform1579)
Shape1582 = x3d.Shape()
LineSet1583 = x3d.LineSet()
LineSet1583.vertexCount = [2]
Coordinate1584 = x3d.Coordinate()

LineSet1583.coord = Coordinate1584
""" from r_carpometacarpal_5 to r_metacarpophalangeal_5 vertices 2"""
ColorRGBA1585 = x3d.ColorRGBA()
ColorRGBA1585.USE = "HAnimSegmentLineColorRGBA"

LineSet1583.color = ColorRGBA1585

Shape1582.geometry = LineSet1583

HAnimSegment1578.children.append(Shape1582)

HAnimJoint1577.children.append(HAnimSegment1578)
HAnimJoint1586 = x3d.HAnimJoint()
HAnimJoint1586.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1586.name = "r_metacarpophalangeal_5"
HAnimJoint1586.center = [-0.1926,0.7896,-0.0975]
HAnimSegment1587 = x3d.HAnimSegment()
HAnimSegment1587.DEF = "hanim_r_carpal_proximal_phalanx_5"
HAnimSegment1587.name = "r_carpal_proximal_phalanx_5"
Transform1588 = x3d.Transform()
Transform1588.translation = [-0.1926,0.7896,-0.0975]
Transform1589 = x3d.Transform()
""" Empty Transform """
Shape1590 = x3d.Shape()
Shape1590.USE = "HAnimJointShape"

Transform1589.children.append(Shape1590)

Transform1588.children.append(Transform1589)

HAnimSegment1587.children.append(Transform1588)
Shape1591 = x3d.Shape()
LineSet1592 = x3d.LineSet()
LineSet1592.vertexCount = [2]
Coordinate1593 = x3d.Coordinate()

LineSet1592.coord = Coordinate1593
""" from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 vertices 2"""
ColorRGBA1594 = x3d.ColorRGBA()
ColorRGBA1594.USE = "HAnimSegmentLineColorRGBA"

LineSet1592.color = ColorRGBA1594

Shape1591.geometry = LineSet1592

HAnimSegment1587.children.append(Shape1591)

HAnimJoint1586.children.append(HAnimSegment1587)
HAnimJoint1595 = x3d.HAnimJoint()
HAnimJoint1595.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1595.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1595.center = [-0.1902,0.7483,-0.0963]
HAnimSegment1596 = x3d.HAnimSegment()
HAnimSegment1596.DEF = "hanim_r_carpal_middle_phalanx_5"
HAnimSegment1596.name = "r_carpal_middle_phalanx_5"
Transform1597 = x3d.Transform()
Transform1597.translation = [-0.1902,0.7483,-0.0963]
Transform1598 = x3d.Transform()
""" Empty Transform """
Shape1599 = x3d.Shape()
Shape1599.USE = "HAnimJointShape"

Transform1598.children.append(Shape1599)

Transform1597.children.append(Transform1598)

HAnimSegment1596.children.append(Transform1597)
Shape1600 = x3d.Shape()
LineSet1601 = x3d.LineSet()
LineSet1601.vertexCount = [2]
Coordinate1602 = x3d.Coordinate()

LineSet1601.coord = Coordinate1602
""" from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 vertices 2"""
ColorRGBA1603 = x3d.ColorRGBA()
ColorRGBA1603.USE = "HAnimSegmentLineColorRGBA"

LineSet1601.color = ColorRGBA1603

Shape1600.geometry = LineSet1601

HAnimSegment1596.children.append(Shape1600)
HAnimSite1604 = x3d.HAnimSite()
HAnimSite1604.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite1604.name = "r_carpal_distal_phalanx_5_tip"
TouchSensor1605 = x3d.TouchSensor()
TouchSensor1605.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1604.children.append(TouchSensor1605)
Shape1606 = x3d.Shape()
Shape1606.USE = "HAnimSiteShape"

HAnimSite1604.children.append(Shape1606)

HAnimSegment1596.children.append(HAnimSite1604)

HAnimJoint1595.children.append(HAnimSegment1596)
HAnimJoint1607 = x3d.HAnimJoint()
HAnimJoint1607.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1607.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1607.center = [-0.1908,0.7540,-0.0960]

HAnimJoint1595.children.append(HAnimJoint1607)

HAnimJoint1586.children.append(HAnimJoint1595)

HAnimJoint1577.children.append(HAnimJoint1586)

HAnimJoint1530.children.append(HAnimJoint1577)

HAnimJoint1389.children.append(HAnimJoint1530)

HAnimJoint1377.children.append(HAnimJoint1389)

HAnimJoint1356.children.append(HAnimJoint1377)

HAnimJoint1341.children.append(HAnimJoint1356)

HAnimJoint1332.children.append(HAnimJoint1341)

HAnimJoint852.children.append(HAnimJoint1332)

HAnimJoint837.children.append(HAnimJoint852)

HAnimJoint828.children.append(HAnimJoint837)

HAnimJoint819.children.append(HAnimJoint828)

HAnimJoint810.children.append(HAnimJoint819)

HAnimJoint798.children.append(HAnimJoint810)

HAnimJoint777.children.append(HAnimJoint798)

HAnimJoint768.children.append(HAnimJoint777)

HAnimJoint759.children.append(HAnimJoint768)

HAnimJoint744.children.append(HAnimJoint759)

HAnimJoint732.children.append(HAnimJoint744)

HAnimJoint723.children.append(HAnimJoint732)

HAnimJoint714.children.append(HAnimJoint723)

HAnimJoint705.children.append(HAnimJoint714)

HAnimJoint687.children.append(HAnimJoint705)

HAnimJoint678.children.append(HAnimJoint687)

HAnimJoint669.children.append(HAnimJoint678)

HAnimJoint52.children.append(HAnimJoint669)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimJoint1608 = x3d.HAnimJoint()
HAnimJoint1608.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint1608)
HAnimJoint1609 = x3d.HAnimJoint()
HAnimJoint1609.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint1609)
HAnimJoint1610 = x3d.HAnimJoint()
HAnimJoint1610.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint1610)
HAnimJoint1611 = x3d.HAnimJoint()
HAnimJoint1611.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint1611)
HAnimJoint1612 = x3d.HAnimJoint()
HAnimJoint1612.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1612)
HAnimJoint1613 = x3d.HAnimJoint()
HAnimJoint1613.USE = "hanim_l_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint1613)
HAnimJoint1614 = x3d.HAnimJoint()
HAnimJoint1614.USE = "hanim_l_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint1614)
HAnimJoint1615 = x3d.HAnimJoint()
HAnimJoint1615.USE = "hanim_l_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint1615)
HAnimJoint1616 = x3d.HAnimJoint()
HAnimJoint1616.USE = "hanim_l_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1616)
HAnimJoint1617 = x3d.HAnimJoint()
HAnimJoint1617.USE = "hanim_l_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1617)
HAnimJoint1618 = x3d.HAnimJoint()
HAnimJoint1618.USE = "hanim_l_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint1618)
HAnimJoint1619 = x3d.HAnimJoint()
HAnimJoint1619.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1619)
HAnimJoint1620 = x3d.HAnimJoint()
HAnimJoint1620.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1620)
HAnimJoint1621 = x3d.HAnimJoint()
HAnimJoint1621.USE = "hanim_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1621)
HAnimJoint1622 = x3d.HAnimJoint()
HAnimJoint1622.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1622)
HAnimJoint1623 = x3d.HAnimJoint()
HAnimJoint1623.USE = "hanim_l_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint1623)
HAnimJoint1624 = x3d.HAnimJoint()
HAnimJoint1624.USE = "hanim_l_tarsometatarsal_3 "

HAnimHumanoid43.joints.append(HAnimJoint1624)
HAnimJoint1625 = x3d.HAnimJoint()
HAnimJoint1625.USE = "hanim_l_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1625)
HAnimJoint1626 = x3d.HAnimJoint()
HAnimJoint1626.USE = "hanim_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1626)
HAnimJoint1627 = x3d.HAnimJoint()
HAnimJoint1627.USE = "hanim_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1627)
HAnimJoint1628 = x3d.HAnimJoint()
HAnimJoint1628.USE = "hanim_l_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint1628)
HAnimJoint1629 = x3d.HAnimJoint()
HAnimJoint1629.USE = "hanim_l_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint1629)
HAnimJoint1630 = x3d.HAnimJoint()
HAnimJoint1630.USE = "hanim_l_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint1630)
HAnimJoint1631 = x3d.HAnimJoint()
HAnimJoint1631.USE = "hanim_l_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1631)
HAnimJoint1632 = x3d.HAnimJoint()
HAnimJoint1632.USE = "hanim_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1632)
HAnimJoint1633 = x3d.HAnimJoint()
HAnimJoint1633.USE = "hanim_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1633)
HAnimJoint1634 = x3d.HAnimJoint()
HAnimJoint1634.USE = "hanim_l_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint1634)
HAnimJoint1635 = x3d.HAnimJoint()
HAnimJoint1635.USE = "hanim_l_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1635)
HAnimJoint1636 = x3d.HAnimJoint()
HAnimJoint1636.USE = "hanim_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1636)
HAnimJoint1637 = x3d.HAnimJoint()
HAnimJoint1637.USE = "hanim_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1637)
HAnimJoint1638 = x3d.HAnimJoint()
HAnimJoint1638.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint1638)
HAnimJoint1639 = x3d.HAnimJoint()
HAnimJoint1639.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint1639)
HAnimJoint1640 = x3d.HAnimJoint()
HAnimJoint1640.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1640)
HAnimJoint1641 = x3d.HAnimJoint()
HAnimJoint1641.USE = "hanim_r_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint1641)
HAnimJoint1642 = x3d.HAnimJoint()
HAnimJoint1642.USE = "hanim_r_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint1642)
HAnimJoint1643 = x3d.HAnimJoint()
HAnimJoint1643.USE = "hanim_r_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint1643)
HAnimJoint1644 = x3d.HAnimJoint()
HAnimJoint1644.USE = "hanim_r_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1644)
HAnimJoint1645 = x3d.HAnimJoint()
HAnimJoint1645.USE = "hanim_r_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1645)
HAnimJoint1646 = x3d.HAnimJoint()
HAnimJoint1646.USE = "hanim_r_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint1646)
HAnimJoint1647 = x3d.HAnimJoint()
HAnimJoint1647.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1647)
HAnimJoint1648 = x3d.HAnimJoint()
HAnimJoint1648.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1648)
HAnimJoint1649 = x3d.HAnimJoint()
HAnimJoint1649.USE = "hanim_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1649)
HAnimJoint1650 = x3d.HAnimJoint()
HAnimJoint1650.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1650)
HAnimJoint1651 = x3d.HAnimJoint()
HAnimJoint1651.USE = "hanim_r_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint1651)
HAnimJoint1652 = x3d.HAnimJoint()
HAnimJoint1652.USE = "hanim_r_tarsometatarsal_3 "

HAnimHumanoid43.joints.append(HAnimJoint1652)
HAnimJoint1653 = x3d.HAnimJoint()
HAnimJoint1653.USE = "hanim_r_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1653)
HAnimJoint1654 = x3d.HAnimJoint()
HAnimJoint1654.USE = "hanim_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1654)
HAnimJoint1655 = x3d.HAnimJoint()
HAnimJoint1655.USE = "hanim_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1655)
HAnimJoint1656 = x3d.HAnimJoint()
HAnimJoint1656.USE = "hanim_r_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint1656)
HAnimJoint1657 = x3d.HAnimJoint()
HAnimJoint1657.USE = "hanim_r_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint1657)
HAnimJoint1658 = x3d.HAnimJoint()
HAnimJoint1658.USE = "hanim_r_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint1658)
HAnimJoint1659 = x3d.HAnimJoint()
HAnimJoint1659.USE = "hanim_r_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1659)
HAnimJoint1660 = x3d.HAnimJoint()
HAnimJoint1660.USE = "hanim_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1660)
HAnimJoint1661 = x3d.HAnimJoint()
HAnimJoint1661.USE = "hanim_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1661)
HAnimJoint1662 = x3d.HAnimJoint()
HAnimJoint1662.USE = "hanim_r_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint1662)
HAnimJoint1663 = x3d.HAnimJoint()
HAnimJoint1663.USE = "hanim_r_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1663)
HAnimJoint1664 = x3d.HAnimJoint()
HAnimJoint1664.USE = "hanim_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1664)
HAnimJoint1665 = x3d.HAnimJoint()
HAnimJoint1665.USE = "hanim_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1665)
HAnimJoint1666 = x3d.HAnimJoint()
HAnimJoint1666.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint1666)
HAnimJoint1667 = x3d.HAnimJoint()
HAnimJoint1667.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint1667)
HAnimJoint1668 = x3d.HAnimJoint()
HAnimJoint1668.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint1668)
HAnimJoint1669 = x3d.HAnimJoint()
HAnimJoint1669.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint1670)
HAnimJoint1671 = x3d.HAnimJoint()
HAnimJoint1671.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint1672)
HAnimJoint1673 = x3d.HAnimJoint()
HAnimJoint1673.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint1673)
HAnimJoint1674 = x3d.HAnimJoint()
HAnimJoint1674.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint1674)
HAnimJoint1675 = x3d.HAnimJoint()
HAnimJoint1675.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint1675)
HAnimJoint1676 = x3d.HAnimJoint()
HAnimJoint1676.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint1676)
HAnimJoint1677 = x3d.HAnimJoint()
HAnimJoint1677.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint1677)
HAnimJoint1678 = x3d.HAnimJoint()
HAnimJoint1678.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint1678)
HAnimJoint1679 = x3d.HAnimJoint()
HAnimJoint1679.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint1679)
HAnimJoint1680 = x3d.HAnimJoint()
HAnimJoint1680.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint1680)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint1681)
HAnimJoint1682 = x3d.HAnimJoint()
HAnimJoint1682.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint1682)
HAnimJoint1683 = x3d.HAnimJoint()
HAnimJoint1683.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint1683)
HAnimJoint1684 = x3d.HAnimJoint()
HAnimJoint1684.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint1684)
HAnimJoint1685 = x3d.HAnimJoint()
HAnimJoint1685.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint1685)
HAnimJoint1686 = x3d.HAnimJoint()
HAnimJoint1686.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint1686)
HAnimJoint1687 = x3d.HAnimJoint()
HAnimJoint1687.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint1687)
HAnimJoint1688 = x3d.HAnimJoint()
HAnimJoint1688.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint1688)
HAnimJoint1689 = x3d.HAnimJoint()
HAnimJoint1689.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint1689)
HAnimJoint1690 = x3d.HAnimJoint()
HAnimJoint1690.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint1690)
HAnimJoint1691 = x3d.HAnimJoint()
HAnimJoint1691.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1691)
HAnimJoint1692 = x3d.HAnimJoint()
HAnimJoint1692.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1692)
HAnimJoint1693 = x3d.HAnimJoint()
HAnimJoint1693.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1693)
HAnimJoint1694 = x3d.HAnimJoint()
HAnimJoint1694.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1694)
HAnimJoint1695 = x3d.HAnimJoint()
HAnimJoint1695.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1695)
HAnimJoint1696 = x3d.HAnimJoint()
HAnimJoint1696.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1696)
HAnimJoint1697 = x3d.HAnimJoint()
HAnimJoint1697.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint1697)
HAnimJoint1698 = x3d.HAnimJoint()
HAnimJoint1698.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1698)
HAnimJoint1699 = x3d.HAnimJoint()
HAnimJoint1699.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1699)
HAnimJoint1700 = x3d.HAnimJoint()
HAnimJoint1700.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1700)
HAnimJoint1701 = x3d.HAnimJoint()
HAnimJoint1701.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1701)
HAnimJoint1702 = x3d.HAnimJoint()
HAnimJoint1702.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1702)
HAnimJoint1703 = x3d.HAnimJoint()
HAnimJoint1703.USE = "hanim_l_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1703)
HAnimJoint1704 = x3d.HAnimJoint()
HAnimJoint1704.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1704)
HAnimJoint1705 = x3d.HAnimJoint()
HAnimJoint1705.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1705)
HAnimJoint1706 = x3d.HAnimJoint()
HAnimJoint1706.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1706)
HAnimJoint1707 = x3d.HAnimJoint()
HAnimJoint1707.USE = "hanim_l_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1709)
HAnimJoint1710 = x3d.HAnimJoint()
HAnimJoint1710.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1711)
HAnimJoint1712 = x3d.HAnimJoint()
HAnimJoint1712.USE = "hanim_l_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1713)
HAnimJoint1714 = x3d.HAnimJoint()
HAnimJoint1714.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1716)
HAnimJoint1717 = x3d.HAnimJoint()
HAnimJoint1717.USE = "hanim_l_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1719)
HAnimJoint1720 = x3d.HAnimJoint()
HAnimJoint1720.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1729)
HAnimJoint1730 = x3d.HAnimJoint()
HAnimJoint1730.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_r_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1731)
HAnimJoint1732 = x3d.HAnimJoint()
HAnimJoint1732.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1733)
HAnimJoint1734 = x3d.HAnimJoint()
HAnimJoint1734.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_r_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1737)
HAnimJoint1738 = x3d.HAnimJoint()
HAnimJoint1738.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1738)
HAnimJoint1739 = x3d.HAnimJoint()
HAnimJoint1739.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_r_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1742)
HAnimJoint1743 = x3d.HAnimJoint()
HAnimJoint1743.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1744)
HAnimJoint1745 = x3d.HAnimJoint()
HAnimJoint1745.USE = "hanim_r_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1746)
HAnimJoint1747 = x3d.HAnimJoint()
HAnimJoint1747.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1747)
HAnimJoint1748 = x3d.HAnimJoint()
HAnimJoint1748.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1750)
HAnimJoint1751 = x3d.HAnimJoint()
HAnimJoint1751.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1752)
HAnimJoint1753 = x3d.HAnimJoint()
HAnimJoint1753.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1753)
HAnimSegment1754 = x3d.HAnimSegment()
HAnimSegment1754.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment1754)
HAnimSegment1755 = x3d.HAnimSegment()
HAnimSegment1755.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment1755)
HAnimSegment1756 = x3d.HAnimSegment()
HAnimSegment1756.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1756)
HAnimSegment1757 = x3d.HAnimSegment()
HAnimSegment1757.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment1757)
HAnimSegment1758 = x3d.HAnimSegment()
HAnimSegment1758.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment1758)
HAnimSegment1759 = x3d.HAnimSegment()
HAnimSegment1759.USE = "hanim_l_navicular"

HAnimHumanoid43.segments.append(HAnimSegment1759)
HAnimSegment1760 = x3d.HAnimSegment()
HAnimSegment1760.USE = "hanim_l_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment1760)
HAnimSegment1761 = x3d.HAnimSegment()
HAnimSegment1761.USE = "hanim_l_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "hanim_l_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1762)
HAnimSegment1763 = x3d.HAnimSegment()
HAnimSegment1763.USE = "hanim_l_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment1763)
HAnimSegment1764 = x3d.HAnimSegment()
HAnimSegment1764.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1764)
HAnimSegment1765 = x3d.HAnimSegment()
HAnimSegment1765.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1765)
HAnimSegment1766 = x3d.HAnimSegment()
HAnimSegment1766.USE = "hanim_l_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1766)
HAnimSegment1767 = x3d.HAnimSegment()
HAnimSegment1767.USE = "hanim_l_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment1767)
HAnimSegment1768 = x3d.HAnimSegment()
HAnimSegment1768.USE = "hanim_l_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment1768)
HAnimSegment1769 = x3d.HAnimSegment()
HAnimSegment1769.USE = "hanim_l_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1769)
HAnimSegment1770 = x3d.HAnimSegment()
HAnimSegment1770.USE = "hanim_l_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1770)
HAnimSegment1771 = x3d.HAnimSegment()
HAnimSegment1771.USE = "hanim_l_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment1771)
HAnimSegment1772 = x3d.HAnimSegment()
HAnimSegment1772.USE = "hanim_l_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment1772)
HAnimSegment1773 = x3d.HAnimSegment()
HAnimSegment1773.USE = "hanim_l_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment1773)
HAnimSegment1774 = x3d.HAnimSegment()
HAnimSegment1774.USE = "hanim_l_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1774)
HAnimSegment1775 = x3d.HAnimSegment()
HAnimSegment1775.USE = "hanim_l_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1775)
HAnimSegment1776 = x3d.HAnimSegment()
HAnimSegment1776.USE = "hanim_l_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment1776)
HAnimSegment1777 = x3d.HAnimSegment()
HAnimSegment1777.USE = "hanim_l_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1777)
HAnimSegment1778 = x3d.HAnimSegment()
HAnimSegment1778.USE = "hanim_l_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1778)
HAnimSegment1779 = x3d.HAnimSegment()
HAnimSegment1779.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1779)
HAnimSegment1780 = x3d.HAnimSegment()
HAnimSegment1780.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment1780)
HAnimSegment1781 = x3d.HAnimSegment()
HAnimSegment1781.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment1781)
HAnimSegment1782 = x3d.HAnimSegment()
HAnimSegment1782.USE = "hanim_r_navicular"

HAnimHumanoid43.segments.append(HAnimSegment1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "hanim_r_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment1783)
HAnimSegment1784 = x3d.HAnimSegment()
HAnimSegment1784.USE = "hanim_r_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment1784)
HAnimSegment1785 = x3d.HAnimSegment()
HAnimSegment1785.USE = "hanim_r_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1785)
HAnimSegment1786 = x3d.HAnimSegment()
HAnimSegment1786.USE = "hanim_r_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment1786)
HAnimSegment1787 = x3d.HAnimSegment()
HAnimSegment1787.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1787)
HAnimSegment1788 = x3d.HAnimSegment()
HAnimSegment1788.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1788)
HAnimSegment1789 = x3d.HAnimSegment()
HAnimSegment1789.USE = "hanim_r_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1789)
HAnimSegment1790 = x3d.HAnimSegment()
HAnimSegment1790.USE = "hanim_r_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment1790)
HAnimSegment1791 = x3d.HAnimSegment()
HAnimSegment1791.USE = "hanim_r_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment1791)
HAnimSegment1792 = x3d.HAnimSegment()
HAnimSegment1792.USE = "hanim_r_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1792)
HAnimSegment1793 = x3d.HAnimSegment()
HAnimSegment1793.USE = "hanim_r_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1793)
HAnimSegment1794 = x3d.HAnimSegment()
HAnimSegment1794.USE = "hanim_r_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment1794)
HAnimSegment1795 = x3d.HAnimSegment()
HAnimSegment1795.USE = "hanim_r_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "hanim_r_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment1796)
HAnimSegment1797 = x3d.HAnimSegment()
HAnimSegment1797.USE = "hanim_r_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1797)
HAnimSegment1798 = x3d.HAnimSegment()
HAnimSegment1798.USE = "hanim_r_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1798)
HAnimSegment1799 = x3d.HAnimSegment()
HAnimSegment1799.USE = "hanim_r_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment1799)
HAnimSegment1800 = x3d.HAnimSegment()
HAnimSegment1800.USE = "hanim_r_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1800)
HAnimSegment1801 = x3d.HAnimSegment()
HAnimSegment1801.USE = "hanim_r_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment1803)
HAnimSegment1804 = x3d.HAnimSegment()
HAnimSegment1804.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment1804)
HAnimSegment1805 = x3d.HAnimSegment()
HAnimSegment1805.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment1805)
HAnimSegment1806 = x3d.HAnimSegment()
HAnimSegment1806.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment1807)
HAnimSegment1808 = x3d.HAnimSegment()
HAnimSegment1808.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment1818)
HAnimSegment1819 = x3d.HAnimSegment()
HAnimSegment1819.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment1823)
HAnimSegment1824 = x3d.HAnimSegment()
HAnimSegment1824.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment1825)
HAnimSegment1826 = x3d.HAnimSegment()
HAnimSegment1826.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1827)
HAnimSegment1828 = x3d.HAnimSegment()
HAnimSegment1828.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1829)
HAnimSegment1830 = x3d.HAnimSegment()
HAnimSegment1830.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1831)
HAnimSegment1832 = x3d.HAnimSegment()
HAnimSegment1832.USE = "hanim_l_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment1832)
HAnimSegment1833 = x3d.HAnimSegment()
HAnimSegment1833.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1834)
HAnimSegment1835 = x3d.HAnimSegment()
HAnimSegment1835.USE = "hanim_l_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_l_carpal_proximal_phalanx_2 "

HAnimHumanoid43.segments.append(HAnimSegment1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_l_capitate"

HAnimHumanoid43.segments.append(HAnimSegment1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1842)
HAnimSegment1843 = x3d.HAnimSegment()
HAnimSegment1843.USE = "hanim_l_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1843)
HAnimSegment1844 = x3d.HAnimSegment()
HAnimSegment1844.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1845)
HAnimSegment1846 = x3d.HAnimSegment()
HAnimSegment1846.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1851)
HAnimSegment1852 = x3d.HAnimSegment()
HAnimSegment1852.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1852)
HAnimSegment1853 = x3d.HAnimSegment()
HAnimSegment1853.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1853)
HAnimSegment1854 = x3d.HAnimSegment()
HAnimSegment1854.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "hanim_r_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment1855)
HAnimSegment1856 = x3d.HAnimSegment()
HAnimSegment1856.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1856)
HAnimSegment1857 = x3d.HAnimSegment()
HAnimSegment1857.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "hanim_r_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment1858)
HAnimSegment1859 = x3d.HAnimSegment()
HAnimSegment1859.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "hanim_r_carpal_proximal_phalanx_2 "

HAnimHumanoid43.segments.append(HAnimSegment1860)
HAnimSegment1861 = x3d.HAnimSegment()
HAnimSegment1861.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1861)
HAnimSegment1862 = x3d.HAnimSegment()
HAnimSegment1862.USE = "hanim_r_capitate"

HAnimHumanoid43.segments.append(HAnimSegment1862)
HAnimSegment1863 = x3d.HAnimSegment()
HAnimSegment1863.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1863)
HAnimSegment1864 = x3d.HAnimSegment()
HAnimSegment1864.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1864)
HAnimSegment1865 = x3d.HAnimSegment()
HAnimSegment1865.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1865)
HAnimSegment1866 = x3d.HAnimSegment()
HAnimSegment1866.USE = "hanim_r_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1866)
HAnimSegment1867 = x3d.HAnimSegment()
HAnimSegment1867.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1867)
HAnimSegment1868 = x3d.HAnimSegment()
HAnimSegment1868.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1868)
HAnimSegment1869 = x3d.HAnimSegment()
HAnimSegment1869.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1869)
HAnimSegment1870 = x3d.HAnimSegment()
HAnimSegment1870.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1870)
HAnimSegment1871 = x3d.HAnimSegment()
HAnimSegment1871.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1871)
HAnimSegment1872 = x3d.HAnimSegment()
HAnimSegment1872.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1872)
HAnimSite1873 = x3d.HAnimSite()
HAnimSite1873.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite1873)
HAnimSite1874 = x3d.HAnimSite()
HAnimSite1874.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite1874)
HAnimSite1875 = x3d.HAnimSite()
HAnimSite1875.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1875)
HAnimSite1876 = x3d.HAnimSite()
HAnimSite1876.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1876)
HAnimSite1877 = x3d.HAnimSite()
HAnimSite1877.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1877)
HAnimSite1878 = x3d.HAnimSite()
HAnimSite1878.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1878)
HAnimSite1879 = x3d.HAnimSite()
HAnimSite1879.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1879)
HAnimSite1880 = x3d.HAnimSite()
HAnimSite1880.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1880)
HAnimSite1881 = x3d.HAnimSite()
HAnimSite1881.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1881)
HAnimSite1882 = x3d.HAnimSite()
HAnimSite1882.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1882)
HAnimSite1883 = x3d.HAnimSite()
HAnimSite1883.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite1883)
HAnimSite1884 = x3d.HAnimSite()
HAnimSite1884.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1884)
HAnimSite1885 = x3d.HAnimSite()
HAnimSite1885.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1885)
HAnimSite1886 = x3d.HAnimSite()
HAnimSite1886.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1886)
HAnimSite1887 = x3d.HAnimSite()
HAnimSite1887.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1887)
HAnimSite1888 = x3d.HAnimSite()
HAnimSite1888.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1888)
HAnimSite1889 = x3d.HAnimSite()
HAnimSite1889.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1889)
HAnimSite1890 = x3d.HAnimSite()
HAnimSite1890.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1890)
HAnimSite1891 = x3d.HAnimSite()
HAnimSite1891.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1891)
HAnimSite1892 = x3d.HAnimSite()
HAnimSite1892.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1892)
HAnimSite1893 = x3d.HAnimSite()
HAnimSite1893.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1894)
HAnimSite1895 = x3d.HAnimSite()
HAnimSite1895.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1895)
HAnimSite1896 = x3d.HAnimSite()
HAnimSite1896.USE = "hanim_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1896)
HAnimSite1897 = x3d.HAnimSite()
HAnimSite1897.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1898)
HAnimSite1899 = x3d.HAnimSite()
HAnimSite1899.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1899)
HAnimSite1900 = x3d.HAnimSite()
HAnimSite1900.USE = "hanim_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "hanim_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "hanim_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1905)
HAnimSite1906 = x3d.HAnimSite()
HAnimSite1906.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1907)
HAnimSite1908 = x3d.HAnimSite()
HAnimSite1908.USE = "hanim_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1908)
HAnimSite1909 = x3d.HAnimSite()
HAnimSite1909.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1909)
HAnimSite1910 = x3d.HAnimSite()
HAnimSite1910.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1910)
HAnimSite1911 = x3d.HAnimSite()
HAnimSite1911.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1911)
HAnimSite1912 = x3d.HAnimSite()
HAnimSite1912.USE = "hanim_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1913)
HAnimSite1914 = x3d.HAnimSite()
HAnimSite1914.USE = "hanim_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1914)
HAnimSite1915 = x3d.HAnimSite()
HAnimSite1915.USE = "hanim_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "hanim_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1917)
HAnimSite1918 = x3d.HAnimSite()
HAnimSite1918.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite1921)
HAnimSite1922 = x3d.HAnimSite()
HAnimSite1922.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_mesosternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1926)
HAnimSite1927 = x3d.HAnimSite()
HAnimSite1927.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1927)
HAnimSite1928 = x3d.HAnimSite()
HAnimSite1928.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1929)
HAnimSite1930 = x3d.HAnimSite()
HAnimSite1930.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1930)
HAnimSite1931 = x3d.HAnimSite()
HAnimSite1931.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1932)
HAnimSite1933 = x3d.HAnimSite()
HAnimSite1933.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1933)
HAnimSite1934 = x3d.HAnimSite()
HAnimSite1934.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1934)
HAnimSite1935 = x3d.HAnimSite()
HAnimSite1935.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1935)
HAnimSite1936 = x3d.HAnimSite()
HAnimSite1936.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "hanim_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "hanim_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1942)
HAnimSite1943 = x3d.HAnimSite()
HAnimSite1943.USE = "hanim_adams_apple_pt"

HAnimHumanoid43.sites.append(HAnimSite1943)
HAnimSite1944 = x3d.HAnimSite()
HAnimSite1944.USE = "hanim_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite1944)
HAnimSite1945 = x3d.HAnimSite()
HAnimSite1945.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1945)
HAnimSite1946 = x3d.HAnimSite()
HAnimSite1946.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1946)
HAnimSite1947 = x3d.HAnimSite()
HAnimSite1947.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1947)
HAnimSite1948 = x3d.HAnimSite()
HAnimSite1948.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite1948)
HAnimSite1949 = x3d.HAnimSite()
HAnimSite1949.USE = "hanim_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite1949)
HAnimSite1950 = x3d.HAnimSite()
HAnimSite1950.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1950)
HAnimSite1951 = x3d.HAnimSite()
HAnimSite1951.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1951)
HAnimSite1952 = x3d.HAnimSite()
HAnimSite1952.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1952)
HAnimSite1953 = x3d.HAnimSite()
HAnimSite1953.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite1953)
HAnimSite1954 = x3d.HAnimSite()
HAnimSite1954.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite1954)
HAnimSite1955 = x3d.HAnimSite()
HAnimSite1955.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1955)
HAnimSite1956 = x3d.HAnimSite()
HAnimSite1956.USE = "hanim_menton_pt"

HAnimHumanoid43.sites.append(HAnimSite1956)
HAnimSite1957 = x3d.HAnimSite()
HAnimSite1957.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1957)
HAnimSite1958 = x3d.HAnimSite()
HAnimSite1958.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite1958)
HAnimSite1959 = x3d.HAnimSite()
HAnimSite1959.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1959)
HAnimSite1960 = x3d.HAnimSite()
HAnimSite1960.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1960)
HAnimSite1961 = x3d.HAnimSite()
HAnimSite1961.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1961)
HAnimSite1962 = x3d.HAnimSite()
HAnimSite1962.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1962)
HAnimSite1963 = x3d.HAnimSite()
HAnimSite1963.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1963)
HAnimSite1964 = x3d.HAnimSite()
HAnimSite1964.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1965)
HAnimSite1966 = x3d.HAnimSite()
HAnimSite1966.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1966)
HAnimSite1967 = x3d.HAnimSite()
HAnimSite1967.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1967)
HAnimSite1968 = x3d.HAnimSite()
HAnimSite1968.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1968)
HAnimSite1969 = x3d.HAnimSite()
HAnimSite1969.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1969)
HAnimSite1970 = x3d.HAnimSite()
HAnimSite1970.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1970)
HAnimSite1971 = x3d.HAnimSite()
HAnimSite1971.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1972)
HAnimSite1973 = x3d.HAnimSite()
HAnimSite1973.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1973)
HAnimSite1974 = x3d.HAnimSite()
HAnimSite1974.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1974)
HAnimSite1975 = x3d.HAnimSite()
HAnimSite1975.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1975)
HAnimSite1976 = x3d.HAnimSite()
HAnimSite1976.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1976)
HAnimSite1977 = x3d.HAnimSite()
HAnimSite1977.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1977)
HAnimSite1978 = x3d.HAnimSite()
HAnimSite1978.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1978)
HAnimSite1979 = x3d.HAnimSite()
HAnimSite1979.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1979)
HAnimSite1980 = x3d.HAnimSite()
HAnimSite1980.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1980)
HAnimSite1981 = x3d.HAnimSite()
HAnimSite1981.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1981)
HAnimSite1982 = x3d.HAnimSite()
HAnimSite1982.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1982)
HAnimSite1983 = x3d.HAnimSite()
HAnimSite1983.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1983)
HAnimSite1984 = x3d.HAnimSite()
HAnimSite1984.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1984)
HAnimSite1985 = x3d.HAnimSite()
HAnimSite1985.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1985)
HAnimSite1986 = x3d.HAnimSite()
HAnimSite1986.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1986)
HAnimSite1987 = x3d.HAnimSite()
HAnimSite1987.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1987)
HAnimSite1988 = x3d.HAnimSite()
HAnimSite1988.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1988)
HAnimSite1989 = x3d.HAnimSite()
HAnimSite1989.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1989)
HAnimSite1990 = x3d.HAnimSite()
HAnimSite1990.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1990)

Scene11.children.append(HAnimHumanoid43)

X3D0.Scene = Scene11
f = open("Humanoid4_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
