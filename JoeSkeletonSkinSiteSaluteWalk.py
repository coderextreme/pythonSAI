print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.level = 2
component2.name = "H-Anim"

head1.children.append(component2)
meta3 = x3d.meta()
meta3.content = "JoeSkeletonSkinSaluteSiteWalk.x3d"
meta3.name = "title"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "Comprehensive example showing skeleton, skin, sites and interpolator animation together."
meta4.name = "description"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "Joe D. Williams"
meta5.name = "creator"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "9 January 2004"
meta6.name = "created"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "4 December 2022"
meta7.name = "translated"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "27 January 2023"
meta8.name = "modified"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "Under development, numerous errors and warnings"
meta9.name = "warning"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "This is an HAnimV1 loa model, might need to convert to X3D4 to note loa value"
meta10.name = "TODO"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.content = "Provide feedback to tovrmlx3d converter"
meta11.name = "TODO"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.content = "HAnimJoint cannot contain X3DChildNode elements, only HAnimJoint HAnimSegmet HAnimSite - improve diagnostics."
meta12.name = "TODO"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.content = "ensure name prefix \"Joe_\" applied to all contained DEF values (not name field), perhaps correction automatically applied by X3DTidy"
meta13.name = "TODO"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.content = "JoeSkeletonSkinSaluteSiteWalk.original.x3dv"
meta14.name = "reference"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.content = "JoeSkeletonSkinSaluteSiteWalk.modified1.x3dv"
meta15.name = "reference"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.content = "JoeSkeletonSkinSaluteSiteWalk.modified2.x3dv"
meta16.name = "reference"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.content = "JoeSkeletonSkinSiteSaluteWalk_X3D-Edit.png"
meta17.name = "Image"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.content = "JoeSkeletonSkinSiteSaluteWalk_composite.vsdx"
meta18.name = "reference"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.content = "JoeSkeletonSkinSiteSaluteWalk_composite.2023JAN2.png"
meta19.name = "Image"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.content = "JoeSkeletonSkinSiteSaluteWalk_view3dscene.png"
meta20.name = "Image"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.content = "JoeSkeletonSkinSiteSaluteWalk_X_ITE.png"
meta21.name = "Image"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.content = "JoeSkeletonSkinSiteSaluteWalk_X3DOM.png"
meta22.name = "Image"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.content = "JoeSkeletonSkinSiteSaluteWalk_H3DViewer.png"
meta23.name = "Image"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.content = "JoeSkeletonSkinSiteSaluteWalk_freeWrl.png"
meta24.name = "Image"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.content = "JoeSkeletonSkinSiteSaluteWalk_Octaga.png"
meta25.name = "Image"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.content = "JoeSkeletonSkinSiteSaluteWalk_vivaty.png"
meta26.name = "Image"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.content = "tovrmlx3d, https://castle-engine.io/convert.php"
meta27.name = "generator"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.content = "https://castle-engine.io/view3dscene.php#section_converting"
meta28.name = "reference"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.content = "Michalis Kamburelis"
meta29.name = "translator"

head1.children.append(meta29)
meta30 = x3d.meta()
meta30.content = "Don Brutzman"
meta30.name = "translator"

head1.children.append(meta30)
meta31 = x3d.meta()
meta31.content = "Joe D. Williams"
meta31.name = "translator"

head1.children.append(meta31)
meta32 = x3d.meta()
meta32.content = "X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit"
meta32.name = "generator"

head1.children.append(meta32)
meta33 = x3d.meta()
meta33.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Skin/JoeSkeletonSkinSaluteSiteWalk.x3d"
meta33.name = "identifier"

head1.children.append(meta33)
meta34 = x3d.meta()
meta34.content = "../license.html"
meta34.name = "license"

head1.children.append(meta34)

X3D0.head = head1
Scene35 = x3d.Scene()
WorldInfo36 = x3d.WorldInfo()
WorldInfo36.info = ["By Joe for Joe"]
WorldInfo36.title = "HAnim V1 LOA3 Skeleton Joint centers and Site translations Adapted for approximatrion of ManGLoss Site Location Example and HANIM 200x Default Joint Centers, LOA3"

Scene35.children.append(WorldInfo36)
WorldInfo37 = x3d.WorldInfo()
WorldInfo37.info = ["By Joe for Joe"]
WorldInfo37.title = "HAnim V1 LOA3 Skeleton Joint centers Adapted for approximatrion of ManGLoss Site Location Example and ANIM 200x Default Joint Centers, LOA3"

Scene35.children.append(WorldInfo37)
NavigationInfo38 = x3d.NavigationInfo()
NavigationInfo38.DEF = "HeadlightOnRevealsSkinTextureAndColors"

Scene35.children.append(NavigationInfo38)
Background39 = x3d.Background()
Background39.groundAngle = [1.57]

Scene35.children.append(Background39)
Transform40 = x3d.Transform()
Transform40.DEF = "cordsysfloor"
Transform40.scale = [0.175,0.175,0.175]
Inline41 = x3d.Inline()
Inline41.DEF = "CoordinateAxes"
Inline41.url = ["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../../Savage/Tools/Authoring/CoordinateAxes.x3d","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","../../../Savage/Tools/Authoring/CoordinateAxes.wrl","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://savage.nps.edu/Savage/Tools/Authoring/CoordinateAxes.wrl"]

Transform40.children.append(Inline41)

Scene35.children.append(Transform40)
""" Authoring hint: these axes are aligned within local coordinate system """
Group42 = x3d.Group()
Group42.DEF = "ViewpointGroup"
Viewpoint43 = x3d.Viewpoint()
Viewpoint43.description = "Front Up View"
Viewpoint43.orientation = [-1,-1,0,0.55]
Viewpoint43.position = [-1,2,2.5]

Group42.children.append(Viewpoint43)
Viewpoint44 = x3d.Viewpoint()
Viewpoint44.description = "From Left View"
Viewpoint44.orientation = [0.3,1,0,-1.57]
Viewpoint44.position = [-2.5,1.5,0]

Group42.children.append(Viewpoint44)
Viewpoint45 = x3d.Viewpoint()
Viewpoint45.description = "Front Mid View"
Viewpoint45.orientation = [0,1,0,0]
Viewpoint45.position = [0,0.5,1.25]

Group42.children.append(Viewpoint45)
Viewpoint46 = x3d.Viewpoint()
Viewpoint46.description = "Front Feet View"
Viewpoint46.orientation = [0,1,0,0]
Viewpoint46.position = [0,0,0.75]

Group42.children.append(Viewpoint46)
Viewpoint47 = x3d.Viewpoint()
Viewpoint47.description = "From Right View"
Viewpoint47.orientation = [0,1,0,1.57]
Viewpoint47.position = [1,1,0]

Group42.children.append(Viewpoint47)
Viewpoint48 = x3d.Viewpoint()
Viewpoint48.centerOfRotation = [0,1.65,0]
Viewpoint48.description = "Front Head View"
Viewpoint48.position = [0,1.65,0.75]

Group42.children.append(Viewpoint48)
Viewpoint49 = x3d.Viewpoint()
Viewpoint49.description = "Front Mid View"
Viewpoint49.orientation = [0,1,0,0]
Viewpoint49.position = [0,1,1.75]

Group42.children.append(Viewpoint49)
Viewpoint50 = x3d.Viewpoint()
Viewpoint50.description = "Rear View"
Viewpoint50.orientation = [0,1,0,3.14]
Viewpoint50.position = [0,1.5,-4]

Group42.children.append(Viewpoint50)
Viewpoint51 = x3d.Viewpoint()
Viewpoint51.description = "Top View"
Viewpoint51.orientation = [1,0,0,-1.57]
Viewpoint51.position = [0,4,0]

Group42.children.append(Viewpoint51)
Viewpoint52 = x3d.Viewpoint()
Viewpoint52.description = "Bottom View"
Viewpoint52.orientation = [1,0,0,1.57]
Viewpoint52.position = [0,-4,0]

Group42.children.append(Viewpoint52)
Viewpoint53 = x3d.Viewpoint()
Viewpoint53.description = "Right View"
Viewpoint53.orientation = [0,1,0,1.57]
Viewpoint53.position = [4,1.5,0]

Group42.children.append(Viewpoint53)

Scene35.children.append(Group42)
Group54 = x3d.Group()
Group54.DEF = "VisualizationShapes"
Transform55 = x3d.Transform()
Transform55.scale = [5,5,5]
Transform55.translation = [0,2.1,0]
Shape56 = x3d.Shape()
Shape56.DEF = "jointbox"
IndexedFaceSet57 = x3d.IndexedFaceSet()
IndexedFaceSet57.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet57.creaseAngle = 0.10000000149011612
Coordinate58 = x3d.Coordinate()
Coordinate58.DEF = "boxCoords"

IndexedFaceSet57.coord = Coordinate58
Color59 = x3d.Color()

IndexedFaceSet57.color = Color59

Shape56.geometry = IndexedFaceSet57
Appearance60 = x3d.Appearance()
Material61 = x3d.Material()
Material61.ambientIntensity = 0.5
Material61.diffuseColor = [0,0,0]
Material61.shininess = 1

Appearance60.material = Material61

Shape56.appearance = Appearance60

Transform55.children.append(Shape56)

Group54.children.append(Transform55)
Transform62 = x3d.Transform()
Transform62.scale = [0.1,0.1,0.1]
Transform62.translation = [-0.2,0.773,-0.016]
Shape63 = x3d.Shape()
Shape63.DEF = "sitebox"
IndexedFaceSet64 = x3d.IndexedFaceSet()
IndexedFaceSet64.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet64.creaseAngle = 0.10000000149011612
Coordinate65 = x3d.Coordinate()
Coordinate65.USE = "boxCoords"

IndexedFaceSet64.coord = Coordinate65

Shape63.geometry = IndexedFaceSet64
Appearance66 = x3d.Appearance()
Material67 = x3d.Material()
Material67.ambientIntensity = 1
Material67.diffuseColor = [1,0,0]
Material67.emissiveColor = [1,0,0]
Material67.shininess = 0.7
Material67.specularColor = [1,0,0]

Appearance66.material = Material67

Shape63.appearance = Appearance66

Transform62.children.append(Shape63)

Group54.children.append(Transform62)
Transform68 = x3d.Transform()
Transform68.scale = [0.1,0.1,0.1]
Transform68.translation = [0,0.2,0]
Shape69 = x3d.Shape()
IndexedLineSet70 = x3d.IndexedLineSet()
IndexedLineSet70.coordIndex = [0,1,-1]
Coordinate71 = x3d.Coordinate()

IndexedLineSet70.coord = Coordinate71

Shape69.geometry = IndexedLineSet70
Appearance72 = x3d.Appearance()
Appearance72.DEF = "SegmentLine"
Material73 = x3d.Material()
Material73.diffuseColor = [0,1,0]
Material73.emissiveColor = [0,1,0]
Material73.specularColor = [0,1,0]

Appearance72.material = Material73

Shape69.appearance = Appearance72

Transform68.children.append(Shape69)

Group54.children.append(Transform68)
Transform74 = x3d.Transform()
Transform74.scale = [0.1,0.1,0.1]
Transform74.translation = [-0.2,0.773,-0.016]
Shape75 = x3d.Shape()
Shape75.DEF = "skinsphere"
Sphere76 = x3d.Sphere()
Sphere76.radius = 0.005

Shape75.geometry = Sphere76
Appearance77 = x3d.Appearance()
Material78 = x3d.Material()
Material78.ambientIntensity = 0.5
Material78.diffuseColor = [0,1,0]
Material78.emissiveColor = [0,1,0]
Material78.shininess = 1
Material78.specularColor = [0,1,0]

Appearance77.material = Material78

Shape75.appearance = Appearance77

Transform74.children.append(Shape75)

Group54.children.append(Transform74)

Scene35.children.append(Group54)
Group79 = x3d.Group()
Group79.DEF = "SpecHumanoid"
Group80 = x3d.Group()
Group80.DEF = "JoeISOHumanoid"
HAnimHumanoid81 = x3d.HAnimHumanoid()
HAnimHumanoid81.DEF = "Joe_Human"
HAnimHumanoid81.info = ["humanoidVersion=2.0"]
HAnimHumanoid81.loa = -1
HAnimHumanoid81.name = "Human"
HAnimHumanoid81.version = "2.0"
""" <LOD containerField='skin'> (Switch whichChoice='0' and LOD parents each already work in view3dscene) """
Shape82 = x3d.Shape()
Shape82.DEF = "SkinShape"
IndexedFaceSet83 = x3d.IndexedFaceSet()
IndexedFaceSet83.coordIndex = [0,9,5,-1,0,7,9,-1,0,5,1,-1,1,5,2,-1,1,3,7,-1,2,4,3,-1,0,1,7,-1,1,2,3,-1,5,6,2,-1,7,3,8,-1,6,4,2,-1,3,4,8,-1,9,6,5,-1,9,7,8,-1,4,6,10,-1,4,10,12,-1,4,12,8,-1,10,11,12,-1,9,75,24,-1,9,24,74,-1,9,8,75,-1,9,74,6,-1,10,6,74,-1,12,75,8,-1,74,24,29,-1,24,77,29,-1,10,74,29,-1,77,32,29,-1,32,78,29,-1,78,30,29,-1,30,10,29,-1,41,24,75,-1,41,75,12,-1,41,12,42,-1,41,42,80,-1,41,80,44,-1,41,44,79,-1,41,79,24,-1,81,24,79,-1,81,77,24,-1,81,25,77,-1,81,79,25,-1,25,79,44,-1,25,32,77,-1,25,83,32,-1,25,26,83,-1,25,27,26,-1,25,84,27,-1,25,44,84,-1,11,10,30,-1,11,30,13,-1,11,13,15,-1,11,15,14,-1,11,14,42,-1,11,42,12,-1,15,13,16,-1,15,18,14,-1,15,16,76,-1,15,76,18,-1,76,16,17,-1,76,17,82,-1,76,82,19,-1,76,19,18,-1,22,18,19,-1,22,87,18,-1,22,27,84,-1,22,84,87,-1,87,84,85,-1,85,84,44,-1,85,42,14,-1,87,14,18,-1,87,85,14,-1,20,83,26,-1,20,17,16,-1,20,16,88,-1,20,88,83,-1,88,16,13,-1,88,13,86,-1,88,86,83,-1,86,13,30,-1,86,32,83,-1,23,89,22,-1,89,27,22,-1,89,91,27,-1,91,26,27,-1,91,20,26,-1,21,20,91,-1,21,17,20,-1,21,92,17,-1,82,17,92,-1,82,90,19,-1,23,22,19,-1,23,19,90,-1,82,92,101,-1,82,101,99,-1,82,99,93,-1,82,93,95,-1,82,95,97,-1,82,97,90,-1,23,90,97,-1,23,97,94,-1,23,94,89,-1,89,94,96,-1,89,96,95,-1,89,95,93,-1,89,93,91,-1,91,93,99,-1,91,99,100,-1,91,100,98,-1,21,91,98,-1,21,98,101,-1,21,101,92,-1,85,105,42,-1,85,103,105,-1,85,44,103,-1,103,44,104,-1,80,42,105,-1,80,105,102,-1,80,102,104,-1,80,104,44,-1,105,109,102,-1,102,109,47,-1,47,104,102,-1,104,47,45,-1,104,45,103,-1,103,45,46,-1,103,46,109,-1,103,109,105,-1,109,112,110,-1,109,110,47,-1,47,110,111,-1,47,111,45,-1,45,111,113,-1,113,46,45,-1,46,113,112,-1,112,109,46,-1,112,118,110,-1,110,118,115,-1,110,115,111,-1,111,115,117,-1,111,117,113,-1,113,117,116,-1,113,116,112,-1,112,116,118,-1,115,118,119,-1,119,118,122,-1,118,116,122,-1,122,116,120,-1,116,117,120,-1,120,117,121,-1,117,115,121,-1,115,119,121,-1,119,127,123,-1,119,122,127,-1,122,126,127,-1,122,128,126,-1,122,120,128,-1,120,124,128,-1,120,121,124,-1,121,125,124,-1,121,119,125,-1,119,123,125,-1,127,129,123,-1,127,126,129,-1,129,126,141,-1,141,126,143,-1,126,142,143,-1,126,128,142,-1,128,124,130,-1,142,128,130,-1,124,132,130,-1,124,134,132,-1,125,134,124,-1,125,136,134,-1,125,137,136,-1,125,135,137,-1,125,133,135,-1,125,123,133,-1,123,131,133,-1,123,129,131,-1,131,129,138,-1,129,141,138,-1,138,141,144,-1,141,143,144,-1,143,146,144,-1,142,146,143,-1,142,145,146,-1,139,145,142,-1,130,139,142,-1,139,130,132,-1,139,132,154,-1,132,157,154,-1,132,159,157,-1,132,134,159,-1,134,136,159,-1,136,161,159,-1,136,137,161,-1,137,162,161,-1,160,162,137,-1,135,160,137,-1,133,160,135,-1,133,158,160,-1,131,158,133,-1,156,158,131,-1,153,156,131,-1,131,138,153,-1,138,155,153,-1,140,155,138,-1,138,144,140,-1,144,147,140,-1,140,147,145,-1,140,145,139,-1,139,155,140,-1,154,155,139,-1,146,149,144,-1,146,151,149,-1,145,151,146,-1,150,151,145,-1,145,152,150,-1,147,152,145,-1,147,149,152,-1,147,144,149,-1,148,149,151,-1,148,152,149,-1,148,150,152,-1,148,151,150,-1,160,207,162,-1,160,205,207,-1,165,208,205,-1,160,165,205,-1,158,165,160,-1,161,162,207,-1,161,207,206,-1,165,206,208,-1,206,165,161,-1,161,165,159,-1,207,209,211,-1,205,209,207,-1,205,212,209,-1,205,208,212,-1,206,212,208,-1,206,210,212,-1,206,207,210,-1,207,211,210,-1,209,212,213,-1,212,216,213,-1,212,214,216,-1,210,214,212,-1,210,215,214,-1,210,211,215,-1,209,215,211,-1,209,213,215,-1,217,213,216,-1,217,215,213,-1,217,214,215,-1,217,216,214,-1,158,194,165,-1,192,194,158,-1,164,195,192,-1,158,164,192,-1,156,164,158,-1,159,194,165,-1,159,194,193,-1,159,193,195,-1,159,195,164,-1,159,164,157,-1,157,164,180,-1,192,198,194,-1,192,196,198,-1,192,195,196,-1,195,199,196,-1,196,199,200,-1,199,203,200,-1,193,199,195,-1,193,197,199,-1,193,198,197,-1,193,194,198,-1,199,201,203,-1,197,201,199,-1,197,198,201,-1,198,202,201,-1,196,202,198,-1,200,202,196,-1,204,202,200,-1,204,201,202,-1,204,203,201,-1,204,200,203,-1,156,181,164,-1,156,179,181,-1,156,182,179,-1,156,163,182,-1,163,180,182,-1,157,180,163,-1,164,181,180,-1,179,182,183,-1,182,186,183,-1,182,184,186,-1,180,184,182,-1,180,181,184,-1,181,185,184,-1,179,185,181,-1,183,185,179,-1,183,186,187,-1,186,190,187,-1,184,190,186,-1,184,188,190,-1,184,185,188,-1,185,189,188,-1,185,183,189,-1,183,187,189,-1,191,189,187,-1,191,188,189,-1,191,190,188,-1,191,187,190,-1,153,163,156,-1,153,168,163,-1,153,166,168,-1,153,169,166,-1,155,169,153,-1,155,167,169,-1,154,167,155,-1,154,163,167,-1,154,157,163,-1,163,168,167,-1,166,169,170,-1,169,173,170,-1,169,171,173,-1,169,167,171,-1,167,168,171,-1,168,172,171,-1,168,170,172,-1,170,168,166,-1,170,173,174,-1,173,177,174,-1,173,175,177,-1,173,171,175,-1,171,172,175,-1,172,176,175,-1,172,174,176,-1,170,174,172,-1,178,176,174,-1,178,175,176,-1,178,177,175,-1,178,174,177,-1,86,30,221,-1,86,221,219,-1,86,219,32,-1,32,219,220,-1,78,32,220,-1,78,220,218,-1,78,218,221,-1,78,221,30,-1,221,225,219,-1,219,225,35,-1,35,33,219,-1,33,220,219,-1,33,34,220,-1,220,34,218,-1,221,218,34,-1,34,225,221,-1,225,226,228,-1,225,228,35,-1,35,228,229,-1,35,229,33,-1,33,229,227,-1,33,227,34,-1,34,227,226,-1,34,226,225,-1,226,234,228,-1,228,234,232,-1,232,229,228,-1,232,233,229,-1,229,233,227,-1,227,233,231,-1,227,231,226,-1,226,231,234,-1,231,235,234,-1,235,238,234,-1,234,238,232,-1,238,236,232,-1,232,236,233,-1,236,237,233,-1,233,237,231,-1,231,237,235,-1,235,239,243,-1,235,243,238,-1,238,243,242,-1,238,242,244,-1,238,244,236,-1,236,244,240,-1,236,240,237,-1,237,240,241,-1,237,241,235,-1,235,241,239,-1,243,239,245,-1,243,245,242,-1,245,257,242,-1,257,259,242,-1,242,259,258,-1,242,258,244,-1,244,246,240,-1,258,246,244,-1,240,246,248,-1,240,248,250,-1,241,240,250,-1,241,250,252,-1,241,252,253,-1,241,253,251,-1,241,251,249,-1,241,249,239,-1,239,249,247,-1,239,247,245,-1,247,254,245,-1,245,254,257,-1,254,260,257,-1,257,260,259,-1,259,260,262,-1,258,259,262,-1,258,262,261,-1,255,258,261,-1,246,258,255,-1,255,248,246,-1,255,270,248,-1,248,270,273,-1,248,273,275,-1,248,275,250,-1,250,275,252,-1,252,275,277,-1,252,277,253,-1,253,277,278,-1,276,253,278,-1,251,253,276,-1,249,251,276,-1,249,276,274,-1,247,249,274,-1,272,247,274,-1,269,247,272,-1,247,269,254,-1,254,269,271,-1,256,254,271,-1,254,256,260,-1,260,256,263,-1,256,261,263,-1,256,255,261,-1,255,256,271,-1,270,255,271,-1,262,260,265,-1,262,265,267,-1,261,262,267,-1,266,261,267,-1,261,266,268,-1,263,261,268,-1,263,268,265,-1,263,265,260,-1,264,267,265,-1,264,265,268,-1,264,268,266,-1,264,266,267,-1,276,278,323,-1,276,323,321,-1,281,321,324,-1,276,321,281,-1,274,276,281,-1,277,323,278,-1,277,322,323,-1,281,324,322,-1,322,277,281,-1,277,275,281,-1,323,327,325,-1,321,323,325,-1,321,325,328,-1,321,328,324,-1,322,324,328,-1,322,328,326,-1,322,326,323,-1,323,326,327,-1,325,329,328,-1,328,329,332,-1,328,332,330,-1,326,328,330,-1,326,330,331,-1,326,331,327,-1,325,327,331,-1,325,331,329,-1,333,332,329,-1,333,329,331,-1,333,331,330,-1,333,330,332,-1,274,281,310,-1,308,274,310,-1,280,308,311,-1,274,308,280,-1,272,274,280,-1,275,310,281,-1,275,309,310,-1,275,311,309,-1,275,280,311,-1,275,273,280,-1,273,296,280,-1,308,310,314,-1,308,314,312,-1,308,312,311,-1,311,312,315,-1,312,316,315,-1,315,316,319,-1,309,311,315,-1,309,315,313,-1,309,313,314,-1,309,314,310,-1,315,319,317,-1,313,315,317,-1,313,317,314,-1,314,317,318,-1,312,314,318,-1,316,312,318,-1,320,316,318,-1,320,318,317,-1,320,317,319,-1,320,319,316,-1,272,280,297,-1,272,297,295,-1,272,295,298,-1,272,298,279,-1,279,298,296,-1,273,279,296,-1,280,296,297,-1,295,299,298,-1,298,299,302,-1,298,302,300,-1,296,298,300,-1,296,300,297,-1,297,300,301,-1,295,297,301,-1,299,295,301,-1,299,303,302,-1,302,303,306,-1,300,302,306,-1,300,306,304,-1,300,304,301,-1,301,304,305,-1,301,305,299,-1,299,305,303,-1,307,303,305,-1,307,305,304,-1,307,304,306,-1,307,306,303,-1,269,272,279,-1,269,279,284,-1,269,284,282,-1,269,282,285,-1,271,269,285,-1,271,285,283,-1,270,271,283,-1,270,283,279,-1,270,279,273,-1,279,283,284,-1,282,286,285,-1,285,286,289,-1,285,289,287,-1,285,287,283,-1,283,287,284,-1,284,287,288,-1,284,288,286,-1,286,282,284,-1,286,290,289,-1,289,290,293,-1,289,293,291,-1,289,291,287,-1,287,291,288,-1,288,291,292,-1,288,292,290,-1,286,288,290,-1,294,290,292,-1,294,292,291,-1,294,291,293,-1,294,293,290,-1,97,334,336,-1,97,336,94,-1,94,336,96,-1,336,335,96,-1,96,335,95,-1,95,335,337,-1,95,337,334,-1,95,334,97,-1,334,341,336,-1,336,341,338,-1,336,338,335,-1,335,338,340,-1,335,340,337,-1,337,340,339,-1,337,339,334,-1,334,339,341,-1,341,345,342,-1,341,342,338,-1,338,342,340,-1,340,342,344,-1,340,344,339,-1,339,344,343,-1,339,343,345,-1,339,345,341,-1,345,349,342,-1,342,349,351,-1,342,351,346,-1,342,346,344,-1,71,346,348,-1,71,344,346,-1,71,348,347,-1,71,347,344,-1,344,347,343,-1,343,347,352,-1,343,352,349,-1,343,349,345,-1,349,352,356,-1,349,356,353,-1,349,353,355,-1,349,355,351,-1,354,356,352,-1,354,352,350,-1,354,350,351,-1,354,351,355,-1,353,356,357,-1,353,357,358,-1,353,358,359,-1,353,359,360,-1,353,360,361,-1,353,361,355,-1,354,357,356,-1,350,346,351,-1,348,346,347,-1,350,347,346,-1,350,352,347,-1,354,358,357,-1,354,359,358,-1,354,360,359,-1,354,361,360,-1,354,355,361,-1,101,362,365,-1,101,365,99,-1,99,365,100,-1,100,365,363,-1,100,363,98,-1,98,363,364,-1,98,364,101,-1,101,364,362,-1,362,369,367,-1,362,367,365,-1,365,367,363,-1,363,367,368,-1,363,367,368,-1,363,368,366,-1,363,366,364,-1,364,366,362,-1,362,366,369,-1,369,373,371,-1,369,371,367,-1,367,371,368,-1,368,371,372,-1,368,372,366,-1,366,372,370,-1,366,370,369,-1,369,370,373,-1,373,377,380,-1,373,380,375,-1,373,375,371,-1,371,375,372,-1,372,375,376,-1,372,376,374,-1,372,374,370,-1,370,374,379,-1,373,370,379,-1,373,379,377,-1,377,379,383,-1,377,383,381,-1,377,381,384,-1,377,384,380,-1,381,383,389,-1,381,389,388,-1,381,388,387,-1,381,387,386,-1,381,386,385,-1,381,385,384,-1,376,375,374,-1,378,379,374,-1,378,374,375,-1,378,375,380,-1,382,386,387,-1,382,387,388,-1,382,388,389,-1,382,389,383,-1,382,383,379,-1,382,379,378,-1,382,378,380,-1,382,380,384,-1,382,384,385,-1,382,385,386,-1]
IndexedFaceSet83.creaseAngle = 3.1
Coordinate84 = x3d.Coordinate()
Coordinate84.DEF = "TheSkinCoord"

IndexedFaceSet83.coord = Coordinate84
Color85 = x3d.Color()

IndexedFaceSet83.color = Color85

Shape82.geometry = IndexedFaceSet83
Appearance86 = x3d.Appearance()
Appearance86.DEF = "SkinAppearance"
ImageTexture87 = x3d.ImageTexture()
ImageTexture87.DEF = "zBlueSpiralBkg2"
ImageTexture87.description = "Blue Spiral Pattern"
ImageTexture87.url = ["zBlueSpiralBkg2.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Skin/zBlueSpiralBkg2.gif"]

Appearance86.texture = ImageTexture87
Material88 = x3d.Material()
Material88.DEF = "SkinMaterial"
Material88.ambientIntensity = 0.6
Material88.diffuseColor = [1,1,1]
Material88.shininess = 0.6
Material88.transparency = 0.2

Appearance86.material = Material88

Shape82.appearance = Appearance86

HAnimHumanoid81.skin.append(Shape82)
""" </LOD> """
Coordinate89 = x3d.Coordinate()
Coordinate89.USE = "TheSkinCoord"

HAnimHumanoid81.skinCoord = Coordinate89
HAnimJoint90 = x3d.HAnimJoint()
HAnimJoint90.DEF = "Joe_HumanoidRoot"
HAnimJoint90.center = [0,0.875,0]
HAnimJoint90.name = "HumanoidRoot"
HAnimJoint90.stiffness = [0,0,0]
HAnimSegment91 = x3d.HAnimSegment()
HAnimSegment91.DEF = "Joe_sacrum"
HAnimSegment91.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment91.name = "sacrum"
Transform92 = x3d.Transform()
Transform92.translation = [0,0.875,0]
Shape93 = x3d.Shape()
Shape93.USE = "jointbox"

Transform92.children.append(Shape93)

HAnimSegment91.children.append(Transform92)
Shape94 = x3d.Shape()
IndexedLineSet95 = x3d.IndexedLineSet()
IndexedLineSet95.coordIndex = [0,1,-1]
Coordinate96 = x3d.Coordinate()

IndexedLineSet95.coord = Coordinate96

Shape94.geometry = IndexedLineSet95
Appearance97 = x3d.Appearance()
Appearance97.USE = "SegmentLine"

Shape94.appearance = Appearance97

HAnimSegment91.children.append(Shape94)
Transform98 = x3d.Transform()
Transform98.translation = [0,0.92,0.08]
Shape99 = x3d.Shape()
Shape99.USE = "skinsphere"

Transform98.children.append(Shape99)

HAnimSegment91.children.append(Transform98)
Transform100 = x3d.Transform()
Transform100.translation = [0,0.87,-0.022]
Shape101 = x3d.Shape()
Shape101.USE = "skinsphere"

Transform100.children.append(Shape101)

HAnimSegment91.children.append(Transform100)

HAnimJoint90.children.append(HAnimSegment91)
HAnimJoint102 = x3d.HAnimJoint()
HAnimJoint102.DEF = "Joe_sacroiliac"
HAnimJoint102.center = [0,0.92,0]
HAnimJoint102.name = "sacroiliac"
HAnimJoint102.skinCoordIndex = [17,19,20,21,22,23,26,27,73,82,89,91,93]
HAnimJoint102.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,0.35,0.35,1]
HAnimSegment103 = x3d.HAnimSegment()
HAnimSegment103.DEF = "Joe_pelvis"
HAnimSegment103.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment103.name = "pelvis"
Transform104 = x3d.Transform()
Transform104.translation = [0,0.9149,0.0016]
Transform105 = x3d.Transform()
Shape106 = x3d.Shape()
Shape106.USE = "jointbox"

Transform105.children.append(Shape106)

Transform104.children.append(Transform105)

HAnimSegment103.children.append(Transform104)
Shape107 = x3d.Shape()
IndexedLineSet108 = x3d.IndexedLineSet()
IndexedLineSet108.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate109 = x3d.Coordinate()

IndexedLineSet108.coord = Coordinate109

Shape107.geometry = IndexedLineSet108
Appearance110 = x3d.Appearance()
Appearance110.USE = "SegmentLine"

Shape107.appearance = Appearance110

HAnimSegment103.children.append(Shape107)
HAnimSite111 = x3d.HAnimSite()
HAnimSite111.DEF = "Joe_l_iliocristale"
HAnimSite111.name = "l_iliocristale"
HAnimSite111.translation = [0.1425,1.065,0.0033]
Shape112 = x3d.Shape()
Shape112.USE = "sitebox"

HAnimSite111.children.append(Shape112)

HAnimSegment103.children.append(HAnimSite111)
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.DEF = "Joe_l_trochanterion"
HAnimSite113.name = "l_trochanterion"
HAnimSite113.translation = [0.15,0.9,-0.01]
Shape114 = x3d.Shape()
Shape114.USE = "sitebox"

HAnimSite113.children.append(Shape114)

HAnimSegment103.children.append(HAnimSite113)
HAnimSite115 = x3d.HAnimSite()
HAnimSite115.DEF = "Joe_r_iliocristale"
HAnimSite115.name = "r_iliocristale"
HAnimSite115.translation = [-0.1425,1.065,0.0033]
Shape116 = x3d.Shape()
Shape116.USE = "sitebox"

HAnimSite115.children.append(Shape116)

HAnimSegment103.children.append(HAnimSite115)
HAnimSite117 = x3d.HAnimSite()
HAnimSite117.DEF = "Joe_r_trochanterion"
HAnimSite117.name = "r_trochanterion"
HAnimSite117.translation = [-0.15,0.9,-0.01]
Shape118 = x3d.Shape()
Shape118.USE = "sitebox"

HAnimSite117.children.append(Shape118)

HAnimSegment103.children.append(HAnimSite117)
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.DEF = "Joe_l_asis"
HAnimSite119.name = "l_asis"
HAnimSite119.translation = [0.0935,1.03,0.075]
Shape120 = x3d.Shape()
Shape120.USE = "sitebox"

HAnimSite119.children.append(Shape120)

HAnimSegment103.children.append(HAnimSite119)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.DEF = "Joe_r_asis"
HAnimSite121.name = "r_asis"
HAnimSite121.translation = [-0.0935,1.03,0.075]
Shape122 = x3d.Shape()
Shape122.USE = "sitebox"

HAnimSite121.children.append(Shape122)

HAnimSegment103.children.append(HAnimSite121)
HAnimSite123 = x3d.HAnimSite()
HAnimSite123.DEF = "Joe_l_psis"
HAnimSite123.name = "l_psis"
HAnimSite123.translation = [0.0773,1.019,-0.12]
Shape124 = x3d.Shape()
Shape124.USE = "sitebox"

HAnimSite123.children.append(Shape124)

HAnimSegment103.children.append(HAnimSite123)
HAnimSite125 = x3d.HAnimSite()
HAnimSite125.DEF = "Joe_r_psis"
HAnimSite125.name = "r_psis"
HAnimSite125.translation = [-0.0773,1.019,-0.12]
Shape126 = x3d.Shape()
Shape126.USE = "sitebox"

HAnimSite125.children.append(Shape126)

HAnimSegment103.children.append(HAnimSite125)
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.DEF = "Joe_floormarker"
HAnimSite127.name = "floormarker"
Transform128 = x3d.Transform()
Transform128.scale = [3,3,3]
Shape129 = x3d.Shape()
Shape129.USE = "sitebox"

Transform128.children.append(Shape129)

HAnimSite127.children.append(Transform128)

HAnimSegment103.children.append(HAnimSite127)
HAnimSite130 = x3d.HAnimSite()
HAnimSite130.DEF = "Joe_crotch"
HAnimSite130.name = "crotch"
HAnimSite130.translation = [0,0.87,-0.022]
Shape131 = x3d.Shape()
Shape131.USE = "sitebox"

HAnimSite130.children.append(Shape131)

HAnimSegment103.children.append(HAnimSite130)

HAnimJoint102.children.append(HAnimSegment103)
HAnimJoint132 = x3d.HAnimJoint()
HAnimJoint132.DEF = "Joe_l_hip"
HAnimJoint132.center = [0.1,0.92,0]
HAnimJoint132.name = "l_hip"
HAnimJoint132.skinCoordIndex = [89,90,94,95,96,97]
HAnimJoint132.skinCoordWeight = [0.65,1,1,1,1,1]
HAnimSegment133 = x3d.HAnimSegment()
HAnimSegment133.DEF = "Joe_l_thigh"
HAnimSegment133.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment133.name = "l_thigh"
Transform134 = x3d.Transform()
Transform134.translation = [0.1,0.92,0]
Shape135 = x3d.Shape()
Shape135.USE = "jointbox"

Transform134.children.append(Shape135)

HAnimSegment133.children.append(Transform134)
Shape136 = x3d.Shape()
IndexedLineSet137 = x3d.IndexedLineSet()
IndexedLineSet137.coordIndex = [0,1,-1]
Coordinate138 = x3d.Coordinate()

IndexedLineSet137.coord = Coordinate138

Shape136.geometry = IndexedLineSet137
Appearance139 = x3d.Appearance()
Appearance139.USE = "SegmentLine"

Shape136.appearance = Appearance139

HAnimSegment133.children.append(Shape136)
Transform140 = x3d.Transform()
Transform140.translation = [0.1,0.9,0.0775]
Shape141 = x3d.Shape()
Shape141.USE = "skinsphere"

Transform140.children.append(Shape141)

HAnimSegment133.children.append(Transform140)
Transform142 = x3d.Transform()
Transform142.translation = [0.079,0.92,-0.14]
Shape143 = x3d.Shape()
Shape143.USE = "skinsphere"

Transform142.children.append(Shape143)

HAnimSegment133.children.append(Transform142)
Transform144 = x3d.Transform()
Transform144.translation = [0.171,0.65,0]
Shape145 = x3d.Shape()
Shape145.USE = "skinsphere"

Transform144.children.append(Shape145)

HAnimSegment133.children.append(Transform144)
Transform146 = x3d.Transform()
Transform146.translation = [0.02,0.65,0]
Shape147 = x3d.Shape()
Shape147.USE = "skinsphere"

Transform146.children.append(Shape147)

HAnimSegment133.children.append(Transform146)
Transform148 = x3d.Transform()
Transform148.translation = [0.1,0.65,-0.08]
Shape149 = x3d.Shape()
Shape149.USE = "skinsphere"

Transform148.children.append(Shape149)

HAnimSegment133.children.append(Transform148)
Transform150 = x3d.Transform()
Transform150.translation = [0.1,0.65,0.07]
Shape151 = x3d.Shape()
Shape151.USE = "skinsphere"

Transform150.children.append(Shape151)

HAnimSegment133.children.append(Transform150)
HAnimSite152 = x3d.HAnimSite()
HAnimSite152.DEF = "Joe_l_knee_crease"
HAnimSite152.name = "l_knee_crease"
HAnimSite152.translation = [0.115,0.466,-0.055]
Shape153 = x3d.Shape()
Shape153.USE = "sitebox"

HAnimSite152.children.append(Shape153)

HAnimSegment133.children.append(HAnimSite152)
HAnimSite154 = x3d.HAnimSite()
HAnimSite154.DEF = "Joe_l_femoral_lateral_epicn"
HAnimSite154.name = "l_femoral_lateral_epicn"
HAnimSite154.translation = [0.17,0.466,0]
Shape155 = x3d.Shape()
Shape155.USE = "sitebox"

HAnimSite154.children.append(Shape155)

HAnimSegment133.children.append(HAnimSite154)
HAnimSite156 = x3d.HAnimSite()
HAnimSite156.DEF = "Joe_l_femoral_medial_epicn"
HAnimSite156.name = "l_femoral_medial_epicn"
HAnimSite156.translation = [0.05,0.466,0]
Shape157 = x3d.Shape()
Shape157.USE = "sitebox"

HAnimSite156.children.append(Shape157)

HAnimSegment133.children.append(HAnimSite156)

HAnimJoint132.children.append(HAnimSegment133)
HAnimJoint158 = x3d.HAnimJoint()
HAnimJoint158.DEF = "Joe_l_knee"
HAnimJoint158.center = [0.11500000208616257,0.46599999070167542,0]
HAnimJoint158.name = "l_knee"
HAnimJoint158.skinCoordIndex = [334,335,336,337,338,339,340,341]
HAnimJoint158.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint158.stiffness = [0,0,0]
HAnimSegment159 = x3d.HAnimSegment()
HAnimSegment159.DEF = "Joe_l_calf"
HAnimSegment159.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment159.name = "l_calf"
Transform160 = x3d.Transform()
Transform160.translation = [0.11500000208616257,0.46599999070167542,0]
Shape161 = x3d.Shape()
Shape161.USE = "jointbox"

Transform160.children.append(Shape161)

HAnimSegment159.children.append(Transform160)
Shape162 = x3d.Shape()
IndexedLineSet163 = x3d.IndexedLineSet()
IndexedLineSet163.coordIndex = [0,1,-1]
Coordinate164 = x3d.Coordinate()

IndexedLineSet163.coord = Coordinate164

Shape162.geometry = IndexedLineSet163
Appearance165 = x3d.Appearance()
Appearance165.USE = "SegmentLine"

Shape162.appearance = Appearance165

HAnimSegment159.children.append(Shape162)
Transform166 = x3d.Transform()
Transform166.translation = [0.115,0.466,0.06]
Shape167 = x3d.Shape()
Shape167.USE = "skinsphere"

Transform166.children.append(Shape167)

HAnimSegment159.children.append(Transform166)
Transform168 = x3d.Transform()
Transform168.translation = [0.115,0.466,-0.055]
Shape169 = x3d.Shape()
Shape169.USE = "skinsphere"

Transform168.children.append(Shape169)

HAnimSegment159.children.append(Transform168)
Transform170 = x3d.Transform()
Transform170.translation = [0.17,0.466,0]
Shape171 = x3d.Shape()
Shape171.USE = "skinsphere"

Transform170.children.append(Shape171)

HAnimSegment159.children.append(Transform170)
Transform172 = x3d.Transform()
Transform172.translation = [0.05,0.466,0]
Shape173 = x3d.Shape()
Shape173.USE = "skinsphere"

Transform172.children.append(Shape173)

HAnimSegment159.children.append(Transform172)
Transform174 = x3d.Transform()
Transform174.translation = [0.17,0.3,0]
Shape175 = x3d.Shape()
Shape175.USE = "skinsphere"

Transform174.children.append(Shape175)

HAnimSegment159.children.append(Transform174)
Transform176 = x3d.Transform()
Transform176.translation = [0.06,0.3,0]
Shape177 = x3d.Shape()
Shape177.USE = "skinsphere"

Transform176.children.append(Shape177)

HAnimSegment159.children.append(Transform176)
Transform178 = x3d.Transform()
Transform178.translation = [0.1,0.3,-0.05]
Shape179 = x3d.Shape()
Shape179.USE = "skinsphere"

Transform178.children.append(Shape179)

HAnimSegment159.children.append(Transform178)
Transform180 = x3d.Transform()
Transform180.translation = [0.1,0.3,0.05]
Shape181 = x3d.Shape()
Shape181.USE = "skinsphere"

Transform180.children.append(Shape181)

HAnimSegment159.children.append(Transform180)
HAnimSite182 = x3d.HAnimSite()
HAnimSite182.DEF = "Joe_l_lateral_malleolus"
HAnimSite182.name = "l_lateral_malleolus"
HAnimSite182.translation = [0.15,0.07,0]
Shape183 = x3d.Shape()
Shape183.USE = "sitebox"

HAnimSite182.children.append(Shape183)

HAnimSegment159.children.append(HAnimSite182)
HAnimSite184 = x3d.HAnimSite()
HAnimSite184.DEF = "Joe_l_medial_malleolus"
HAnimSite184.name = "l_medial_malleolus"
HAnimSite184.translation = [0.085,0.086,0.0125]
Shape185 = x3d.Shape()
Shape185.USE = "sitebox"

HAnimSite184.children.append(Shape185)

HAnimSegment159.children.append(HAnimSite184)

HAnimJoint158.children.append(HAnimSegment159)
HAnimJoint186 = x3d.HAnimJoint()
HAnimJoint186.DEF = "Joe_l_ankle"
HAnimJoint186.center = [0.115,0.069,0]
HAnimJoint186.name = "l_ankle"
HAnimJoint186.skinCoordIndex = [342,343,344,345]
HAnimJoint186.skinCoordWeight = [1,1,1,1]
HAnimSegment187 = x3d.HAnimSegment()
HAnimSegment187.DEF = "Joe_l_hindfoot"
HAnimSegment187.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment187.name = "l_hindfoot"
Transform188 = x3d.Transform()
Transform188.translation = [0.115,0.069,0]
Shape189 = x3d.Shape()
Shape189.USE = "jointbox"

Transform188.children.append(Shape189)

HAnimSegment187.children.append(Transform188)
Shape190 = x3d.Shape()
IndexedLineSet191 = x3d.IndexedLineSet()
IndexedLineSet191.coordIndex = [0,1,-1]
Coordinate192 = x3d.Coordinate()

IndexedLineSet191.coord = Coordinate192

Shape190.geometry = IndexedLineSet191
Appearance193 = x3d.Appearance()
Appearance193.USE = "SegmentLine"

Shape190.appearance = Appearance193

HAnimSegment187.children.append(Shape190)
Transform194 = x3d.Transform()
Transform194.translation = [0.15,0.07,0]
Shape195 = x3d.Shape()
Shape195.USE = "skinsphere"

Transform194.children.append(Shape195)

HAnimSegment187.children.append(Transform194)
Transform196 = x3d.Transform()
Transform196.translation = [0.085,0.086,0.0125]
Shape197 = x3d.Shape()
Shape197.USE = "skinsphere"

Transform196.children.append(Shape197)

HAnimSegment187.children.append(Transform196)
Transform198 = x3d.Transform()
Transform198.translation = [0.115,0.069,-0.045]
Shape199 = x3d.Shape()
Shape199.USE = "skinsphere"

Transform198.children.append(Shape199)

HAnimSegment187.children.append(Transform198)
Transform200 = x3d.Transform()
Transform200.translation = [0.117,0.0975,0.0615]
Shape201 = x3d.Shape()
Shape201.USE = "skinsphere"

Transform200.children.append(Shape201)

HAnimSegment187.children.append(Transform200)
HAnimSite202 = x3d.HAnimSite()
HAnimSite202.DEF = "Joe_l_sphyrion"
HAnimSite202.name = "l_sphyrion"
HAnimSite202.translation = [0.09,0.056,0.0125]
Shape203 = x3d.Shape()
Shape203.USE = "sitebox"

HAnimSite202.children.append(Shape203)

HAnimSegment187.children.append(HAnimSite202)
HAnimSite204 = x3d.HAnimSite()
HAnimSite204.DEF = "Joe_l_calcaneous_post"
HAnimSite204.name = "l_calcaneous_post"
HAnimSite204.translation = [0.115,0.04,-0.055]
Shape205 = x3d.Shape()
Shape205.USE = "sitebox"

HAnimSite204.children.append(Shape205)

HAnimSegment187.children.append(HAnimSite204)

HAnimJoint186.children.append(HAnimSegment187)
HAnimJoint206 = x3d.HAnimJoint()
HAnimJoint206.DEF = "Joe_l_subtalar"
HAnimJoint206.center = [0.115,0.031,0.03]
HAnimJoint206.name = "l_subtalar"
HAnimJoint206.skinCoordIndex = [346,347,348,71]
HAnimJoint206.skinCoordWeight = [1,1,1,1]
HAnimSegment207 = x3d.HAnimSegment()
HAnimSegment207.DEF = "Joe_l_midproximal"
HAnimSegment207.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment207.name = "l_midproximal"
Transform208 = x3d.Transform()
Transform208.translation = [0.115,0.031,0.03]
Shape209 = x3d.Shape()
Shape209.USE = "jointbox"

Transform208.children.append(Shape209)

HAnimSegment207.children.append(Transform208)
Shape210 = x3d.Shape()
IndexedLineSet211 = x3d.IndexedLineSet()
IndexedLineSet211.coordIndex = [0,1,-1]
Coordinate212 = x3d.Coordinate()

IndexedLineSet211.coord = Coordinate212

Shape210.geometry = IndexedLineSet211
Appearance213 = x3d.Appearance()
Appearance213.USE = "SegmentLine"

Shape210.appearance = Appearance213

HAnimSegment207.children.append(Shape210)
Transform214 = x3d.Transform()
Transform214.translation = [0.1375,0.006,-0.03]
Shape215 = x3d.Shape()
Shape215.USE = "skinsphere"

Transform214.children.append(Shape215)

HAnimSegment207.children.append(Transform214)
Transform216 = x3d.Transform()
Transform216.translation = [0.095,0.006,-0.03]
Shape217 = x3d.Shape()
Shape217.USE = "skinsphere"

Transform216.children.append(Shape217)

HAnimSegment207.children.append(Transform216)
Transform218 = x3d.Transform()
Transform218.translation = [0.115,0.015,-0.045]
Shape219 = x3d.Shape()
Shape219.USE = "skinsphere"

Transform218.children.append(Shape219)

HAnimSegment207.children.append(Transform218)

HAnimJoint206.children.append(HAnimSegment207)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.DEF = "Joe_l_midtarsal"
HAnimJoint220.center = [0.115,0.037,0.09]
HAnimJoint220.name = "l_midtarsal"
HAnimJoint220.skinCoordIndex = [349,350,351,352]
HAnimJoint220.skinCoordWeight = [1,1,1,1]
HAnimSegment221 = x3d.HAnimSegment()
HAnimSegment221.DEF = "Joe_l_middistal"
HAnimSegment221.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment221.name = "l_middistal"
Transform222 = x3d.Transform()
Transform222.translation = [0.115,0.037,0.09]
Shape223 = x3d.Shape()
Shape223.USE = "jointbox"

Transform222.children.append(Shape223)

HAnimSegment221.children.append(Transform222)
Shape224 = x3d.Shape()
IndexedLineSet225 = x3d.IndexedLineSet()
IndexedLineSet225.coordIndex = [0,1,-1]
Coordinate226 = x3d.Coordinate()

IndexedLineSet225.coord = Coordinate226

Shape224.geometry = IndexedLineSet225
Appearance227 = x3d.Appearance()
Appearance227.USE = "SegmentLine"

Shape224.appearance = Appearance227

HAnimSegment221.children.append(Shape224)
Transform228 = x3d.Transform()
Transform228.translation = [0.11500000208616257,0.059999998658895493,0.10000000149011612]
Shape229 = x3d.Shape()
Shape229.USE = "skinsphere"

Transform228.children.append(Shape229)

HAnimSegment221.children.append(Transform228)
Transform230 = x3d.Transform()
Transform230.translation = [0.11500000208616257,0,0.070000000298023224]
Shape231 = x3d.Shape()
Shape231.USE = "skinsphere"

Transform230.children.append(Shape231)

HAnimSegment221.children.append(Transform230)
Transform232 = x3d.Transform()
Transform232.translation = [0.16500000655651093,0,0.070000000298023224]
Shape233 = x3d.Shape()
Shape233.USE = "skinsphere"

Transform232.children.append(Shape233)

HAnimSegment221.children.append(Transform232)
Transform234 = x3d.Transform()
Transform234.translation = [0.094999998807907104,0,0.070000000298023224]
Shape235 = x3d.Shape()
Shape235.USE = "skinsphere"

Transform234.children.append(Shape235)

HAnimSegment221.children.append(Transform234)
HAnimSite236 = x3d.HAnimSite()
HAnimSite236.DEF = "Joe_l_metatarsal_pha1"
HAnimSite236.name = "l_metatarsal_pha1"
HAnimSite236.translation = [0.086999997496604919,0.0099999997764825821,0.12200000137090683]
Shape237 = x3d.Shape()
Shape237.USE = "sitebox"

HAnimSite236.children.append(Shape237)

HAnimSegment221.children.append(HAnimSite236)

HAnimJoint220.children.append(HAnimSegment221)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.DEF = "Joe_l_metatarsal"
HAnimJoint238.center = [0.11500000208616257,0.019999999552965164,0.12200000137090683]
HAnimJoint238.name = "l_metatarsal"
HAnimJoint238.skinCoordIndex = [353,354,355,356,357,358,359,360,361]
HAnimJoint238.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint238.stiffness = [0,0,0]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.DEF = "Joe_l_forefoot"
HAnimSegment239.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment239.name = "l_forefoot"
Transform240 = x3d.Transform()
Transform240.translation = [0.11500000208616257,0.019999999552965164,0.12999999523162842]
Shape241 = x3d.Shape()
Shape241.USE = "jointbox"

Transform240.children.append(Shape241)

HAnimSegment239.children.append(Transform240)
Shape242 = x3d.Shape()
IndexedLineSet243 = x3d.IndexedLineSet()
IndexedLineSet243.coordIndex = [0,1,-1]
Coordinate244 = x3d.Coordinate()

IndexedLineSet243.coord = Coordinate244

Shape242.geometry = IndexedLineSet243
Appearance245 = x3d.Appearance()
Appearance245.USE = "SegmentLine"

Shape242.appearance = Appearance245

HAnimSegment239.children.append(Shape242)
Transform246 = x3d.Transform()
Transform246.translation = [0.11500000208616257,0.039999999105930328,0.12999999523162842]
Shape247 = x3d.Shape()
Shape247.USE = "skinsphere"

Transform246.children.append(Shape247)

HAnimSegment239.children.append(Transform246)
Transform248 = x3d.Transform()
Transform248.translation = [0.125,0,0.11999999731779099]
Shape249 = x3d.Shape()
Shape249.USE = "skinsphere"

Transform248.children.append(Shape249)

HAnimSegment239.children.append(Transform248)
Transform250 = x3d.Transform()
Transform250.translation = [0.16500000655651093,0,0.11999999731779099]
Shape251 = x3d.Shape()
Shape251.USE = "skinsphere"

Transform250.children.append(Shape251)

HAnimSegment239.children.append(Transform250)
Transform252 = x3d.Transform()
Transform252.translation = [0.086999997496604919,0,0.12200000137090683]
Shape253 = x3d.Shape()
Shape253.USE = "skinsphere"

Transform252.children.append(Shape253)

HAnimSegment239.children.append(Transform252)
Transform254 = x3d.Transform()
Transform254.translation = [0.090000003576278687,0.012000000104308128,0.18799999356269836]
Shape255 = x3d.Shape()
Shape255.USE = "skinsphere"

Transform254.children.append(Shape255)

HAnimSegment239.children.append(Transform254)
Transform256 = x3d.Transform()
Transform256.translation = [0.10999999940395355,0.010999999940395355,0.18999999761581421]
Shape257 = x3d.Shape()
Shape257.USE = "skinsphere"

Transform256.children.append(Shape257)

HAnimSegment239.children.append(Transform256)
Transform258 = x3d.Transform()
Transform258.translation = [0.12800000607967377,0.010999999940395355,0.18500000238418579]
Shape259 = x3d.Shape()
Shape259.USE = "skinsphere"

Transform258.children.append(Shape259)

HAnimSegment239.children.append(Transform258)
Transform260 = x3d.Transform()
Transform260.translation = [0.14200000464916229,0.010999999940395355,0.17800000309944153]
Shape261 = x3d.Shape()
Shape261.USE = "skinsphere"

Transform260.children.append(Shape261)

HAnimSegment239.children.append(Transform260)
Transform262 = x3d.Transform()
Transform262.translation = [0.15399999916553497,0.0099999997764825821,0.1679999977350235]
Shape263 = x3d.Shape()
Shape263.USE = "skinsphere"

Transform262.children.append(Shape263)

HAnimSegment239.children.append(Transform262)
HAnimSite264 = x3d.HAnimSite()
HAnimSite264.DEF = "Joe_l_metatarsal_pha5"
HAnimSite264.name = "l_metatarsal_pha5"
HAnimSite264.translation = [0.16500000655651093,0.0099999997764825821,0.11999999731779099]
Shape265 = x3d.Shape()
Shape265.USE = "sitebox"

HAnimSite264.children.append(Shape265)

HAnimSegment239.children.append(HAnimSite264)
HAnimSite266 = x3d.HAnimSite()
HAnimSite266.DEF = "Joe_l_digit2"
HAnimSite266.name = "l_digit2"
HAnimSite266.translation = [0.10999999940395355,0.010999999940395355,0.18999999761581421]
Shape267 = x3d.Shape()
Shape267.USE = "sitebox"

HAnimSite266.children.append(Shape267)

HAnimSegment239.children.append(HAnimSite266)

HAnimJoint238.children.append(HAnimSegment239)

HAnimJoint220.children.append(HAnimJoint238)

HAnimJoint206.children.append(HAnimJoint220)

HAnimJoint186.children.append(HAnimJoint206)

HAnimJoint158.children.append(HAnimJoint186)

HAnimJoint132.children.append(HAnimJoint158)

HAnimJoint102.children.append(HAnimJoint132)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.DEF = "Joe_r_hip"
HAnimJoint268.center = [-0.10000000149011612,0.92000001668930054,0]
HAnimJoint268.name = "r_hip"
HAnimJoint268.skinCoordIndex = [91,92,98,99,100,101]
HAnimJoint268.skinCoordWeight = [0.64999997615814209,1,1,1,1,1]
HAnimJoint268.stiffness = [0,0,0]
HAnimSegment269 = x3d.HAnimSegment()
HAnimSegment269.DEF = "Joe_r_thigh"
HAnimSegment269.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment269.name = "r_thigh"
Transform270 = x3d.Transform()
Transform270.translation = [-0.10000000149011612,0.92000001668930054,0]
Shape271 = x3d.Shape()
Shape271.USE = "jointbox"

Transform270.children.append(Shape271)

HAnimSegment269.children.append(Transform270)
Shape272 = x3d.Shape()
IndexedLineSet273 = x3d.IndexedLineSet()
IndexedLineSet273.coordIndex = [0,1,-1]
Coordinate274 = x3d.Coordinate()

IndexedLineSet273.coord = Coordinate274

Shape272.geometry = IndexedLineSet273
Appearance275 = x3d.Appearance()
Appearance275.USE = "SegmentLine"

Shape272.appearance = Appearance275

HAnimSegment269.children.append(Shape272)
Transform276 = x3d.Transform()
Transform276.translation = [-0.079000003635883331,0.92000001668930054,-0.14000000059604645]
Shape277 = x3d.Shape()
Shape277.USE = "skinsphere"

Transform276.children.append(Shape277)

HAnimSegment269.children.append(Transform276)
Transform278 = x3d.Transform()
Transform278.translation = [-0.10000000149011612,0.89999997615814209,0.075000002980232239]
Shape279 = x3d.Shape()
Shape279.USE = "skinsphere"

Transform278.children.append(Shape279)

HAnimSegment269.children.append(Transform278)
Transform280 = x3d.Transform()
Transform280.translation = [-0.17100000381469727,0.64999997615814209,0]
Shape281 = x3d.Shape()
Shape281.USE = "skinsphere"

Transform280.children.append(Shape281)

HAnimSegment269.children.append(Transform280)
Transform282 = x3d.Transform()
Transform282.translation = [-0.019999999552965164,0.64999997615814209,0]
Shape283 = x3d.Shape()
Shape283.USE = "skinsphere"

Transform282.children.append(Shape283)

HAnimSegment269.children.append(Transform282)
Transform284 = x3d.Transform()
Transform284.translation = [-0.10000000149011612,0.64999997615814209,-0.079999998211860657]
Shape285 = x3d.Shape()
Shape285.USE = "skinsphere"

Transform284.children.append(Shape285)

HAnimSegment269.children.append(Transform284)
Transform286 = x3d.Transform()
Transform286.translation = [-0.10000000149011612,0.64999997615814209,0.070000000298023224]
Shape287 = x3d.Shape()
Shape287.USE = "skinsphere"

Transform286.children.append(Shape287)

HAnimSegment269.children.append(Transform286)
HAnimSite288 = x3d.HAnimSite()
HAnimSite288.DEF = "Joe_r_knee_crease"
HAnimSite288.name = "r_knee_crease"
HAnimSite288.translation = [-0.11500000208616257,0.46599999070167542,-0.054999999701976776]
Shape289 = x3d.Shape()
Shape289.USE = "sitebox"

HAnimSite288.children.append(Shape289)

HAnimSegment269.children.append(HAnimSite288)
HAnimSite290 = x3d.HAnimSite()
HAnimSite290.DEF = "Joe_r_femoral_lateral_epicn"
HAnimSite290.name = "r_femoral_lateral_epicn"
HAnimSite290.translation = [-0.17000000178813934,0.46599999070167542,0]
Shape291 = x3d.Shape()
Shape291.USE = "sitebox"

HAnimSite290.children.append(Shape291)

HAnimSegment269.children.append(HAnimSite290)
HAnimSite292 = x3d.HAnimSite()
HAnimSite292.DEF = "Joe_r_femoral_medial_epicn"
HAnimSite292.name = "r_femoral_medial_epicn"
HAnimSite292.translation = [-0.05000000074505806,0.46599999070167542,0]
Shape293 = x3d.Shape()
Shape293.USE = "sitebox"

HAnimSite292.children.append(Shape293)

HAnimSegment269.children.append(HAnimSite292)

HAnimJoint268.children.append(HAnimSegment269)
HAnimJoint294 = x3d.HAnimJoint()
HAnimJoint294.DEF = "Joe_r_knee"
HAnimJoint294.center = [-0.05000000074505806,0.46599999070167542,0]
HAnimJoint294.name = "r_knee"
HAnimJoint294.skinCoordIndex = [362,363,364,365,366,367,368,369]
HAnimJoint294.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint294.stiffness = [0,0,0]
HAnimSegment295 = x3d.HAnimSegment()
HAnimSegment295.DEF = "Joe_r_calf"
HAnimSegment295.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment295.name = "r_calf"
Transform296 = x3d.Transform()
Transform296.translation = [-0.10000000149011612,0.49129998683929443,0]
Shape297 = x3d.Shape()
Shape297.USE = "jointbox"

Transform296.children.append(Shape297)

HAnimSegment295.children.append(Transform296)
Shape298 = x3d.Shape()
IndexedLineSet299 = x3d.IndexedLineSet()
IndexedLineSet299.coordIndex = [0,1,-1]
Coordinate300 = x3d.Coordinate()

IndexedLineSet299.coord = Coordinate300

Shape298.geometry = IndexedLineSet299
Appearance301 = x3d.Appearance()
Appearance301.USE = "SegmentLine"

Shape298.appearance = Appearance301

HAnimSegment295.children.append(Shape298)
Transform302 = x3d.Transform()
Transform302.translation = [-0.11500000208616257,0.46599999070167542,0.059999998658895493]
Shape303 = x3d.Shape()
Shape303.USE = "skinsphere"

Transform302.children.append(Shape303)

HAnimSegment295.children.append(Transform302)
Transform304 = x3d.Transform()
Transform304.translation = [-0.11500000208616257,0.46599999070167542,-0.054999999701976776]
Shape305 = x3d.Shape()
Shape305.USE = "skinsphere"

Transform304.children.append(Shape305)

HAnimSegment295.children.append(Transform304)
Transform306 = x3d.Transform()
Transform306.translation = [-0.17000000178813934,0.46599999070167542,0]
Shape307 = x3d.Shape()
Shape307.USE = "skinsphere"

Transform306.children.append(Shape307)

HAnimSegment295.children.append(Transform306)
Transform308 = x3d.Transform()
Transform308.translation = [-0.05000000074505806,0.46599999070167542,0]
Shape309 = x3d.Shape()
Shape309.USE = "skinsphere"

Transform308.children.append(Shape309)

HAnimSegment295.children.append(Transform308)
Transform310 = x3d.Transform()
Transform310.translation = [-0.17000000178813934,0.30000001192092896,0]
Shape311 = x3d.Shape()
Shape311.USE = "skinsphere"

Transform310.children.append(Shape311)

HAnimSegment295.children.append(Transform310)
Transform312 = x3d.Transform()
Transform312.translation = [-0.059999998658895493,0.30000001192092896,0]
Shape313 = x3d.Shape()
Shape313.USE = "skinsphere"

Transform312.children.append(Shape313)

HAnimSegment295.children.append(Transform312)
Transform314 = x3d.Transform()
Transform314.translation = [-0.10000000149011612,0.30000001192092896,-0.05000000074505806]
Shape315 = x3d.Shape()
Shape315.USE = "skinsphere"

Transform314.children.append(Shape315)

HAnimSegment295.children.append(Transform314)
Transform316 = x3d.Transform()
Transform316.translation = [-0.10000000149011612,0.30000001192092896,0.05000000074505806]
Shape317 = x3d.Shape()
Shape317.USE = "skinsphere"

Transform316.children.append(Shape317)

HAnimSegment295.children.append(Transform316)
HAnimSite318 = x3d.HAnimSite()
HAnimSite318.DEF = "Joe_r_lateral_malleolus"
HAnimSite318.name = "r_lateral_malleolus"
HAnimSite318.translation = [-0.15000000596046448,0.070000000298023224,0]
Shape319 = x3d.Shape()
Shape319.USE = "sitebox"

HAnimSite318.children.append(Shape319)

HAnimSegment295.children.append(HAnimSite318)
HAnimSite320 = x3d.HAnimSite()
HAnimSite320.DEF = "Joe_r_medial_malleolus"
HAnimSite320.name = "r_medial_malleolus"
HAnimSite320.translation = [-0.085000000894069672,0.086000002920627594,0.012500000186264515]
Shape321 = x3d.Shape()
Shape321.USE = "sitebox"

HAnimSite320.children.append(Shape321)

HAnimSegment295.children.append(HAnimSite320)

HAnimJoint294.children.append(HAnimSegment295)
HAnimJoint322 = x3d.HAnimJoint()
HAnimJoint322.DEF = "Joe_r_ankle"
HAnimJoint322.center = [-0.11500000208616257,0.068999998271465302,0]
HAnimJoint322.name = "r_ankle"
HAnimJoint322.skinCoordIndex = [370,371,372,373]
HAnimJoint322.skinCoordWeight = [1,1,1,1]
HAnimJoint322.stiffness = [0,0,0]
HAnimSegment323 = x3d.HAnimSegment()
HAnimSegment323.DEF = "Joe_r_hindfoot"
HAnimSegment323.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment323.name = "r_hindfoot"
Transform324 = x3d.Transform()
Transform324.translation = [-0.10000000149011612,0.071199998259544373,0]
Shape325 = x3d.Shape()
Shape325.USE = "jointbox"

Transform324.children.append(Shape325)

HAnimSegment323.children.append(Transform324)
Shape326 = x3d.Shape()
IndexedLineSet327 = x3d.IndexedLineSet()
IndexedLineSet327.coordIndex = [0,1,-1]
Coordinate328 = x3d.Coordinate()

IndexedLineSet327.coord = Coordinate328

Shape326.geometry = IndexedLineSet327
Appearance329 = x3d.Appearance()
Appearance329.USE = "SegmentLine"

Shape326.appearance = Appearance329

HAnimSegment323.children.append(Shape326)
Transform330 = x3d.Transform()
Transform330.translation = [-0.15000000596046448,0.070000000298023224,0]
Shape331 = x3d.Shape()
Shape331.USE = "skinsphere"

Transform330.children.append(Shape331)

HAnimSegment323.children.append(Transform330)
Transform332 = x3d.Transform()
Transform332.translation = [-0.085000000894069672,0.086000002920627594,0.012500000186264515]
Shape333 = x3d.Shape()
Shape333.USE = "skinsphere"

Transform332.children.append(Shape333)

HAnimSegment323.children.append(Transform332)
Transform334 = x3d.Transform()
Transform334.translation = [-0.11500000208616257,0.068999998271465302,-0.045000001788139343]
Shape335 = x3d.Shape()
Shape335.USE = "skinsphere"

Transform334.children.append(Shape335)

HAnimSegment323.children.append(Transform334)
Transform336 = x3d.Transform()
Transform336.translation = [-0.11699999868869781,0.097499996423721313,0.061500001698732376]
Shape337 = x3d.Shape()
Shape337.USE = "skinsphere"

Transform336.children.append(Shape337)

HAnimSegment323.children.append(Transform336)
HAnimSite338 = x3d.HAnimSite()
HAnimSite338.DEF = "Joe_r_sphyrion"
HAnimSite338.name = "r_sphyrion"
HAnimSite338.translation = [-0.090000003576278687,0.056000001728534698,0.012500000186264515]
Shape339 = x3d.Shape()
Shape339.USE = "sitebox"

HAnimSite338.children.append(Shape339)

HAnimSegment323.children.append(HAnimSite338)
HAnimSite340 = x3d.HAnimSite()
HAnimSite340.DEF = "Joe_r_calcaneous_post"
HAnimSite340.name = "r_calcaneous_post"
HAnimSite340.translation = [-0.11500000208616257,0.039999999105930328,-0.054999999701976776]
Shape341 = x3d.Shape()
Shape341.USE = "sitebox"

HAnimSite340.children.append(Shape341)

HAnimSegment323.children.append(HAnimSite340)

HAnimJoint322.children.append(HAnimSegment323)
HAnimJoint342 = x3d.HAnimJoint()
HAnimJoint342.DEF = "Joe_r_subtalar"
HAnimJoint342.center = [-0.10000000149011612,0.014999999664723873,-0.0099999997764825821]
HAnimJoint342.name = "r_subtalar"
HAnimJoint342.skinCoordIndex = [374,375,376]
HAnimJoint342.skinCoordWeight = [1,1,1]
HAnimJoint342.stiffness = [0,0,0]
HAnimSegment343 = x3d.HAnimSegment()
HAnimSegment343.DEF = "Joe_r_midproximal"
HAnimSegment343.name = "r_midproximal"
Transform344 = x3d.Transform()
Transform344.translation = [-0.10000000149011612,0.014999999664723873,-0.0099999997764825821]
Shape345 = x3d.Shape()
Shape345.USE = "jointbox"

Transform344.children.append(Shape345)

HAnimSegment343.children.append(Transform344)
Shape346 = x3d.Shape()
IndexedLineSet347 = x3d.IndexedLineSet()
IndexedLineSet347.coordIndex = [0,1,-1]
Coordinate348 = x3d.Coordinate()

IndexedLineSet347.coord = Coordinate348

Shape346.geometry = IndexedLineSet347
Appearance349 = x3d.Appearance()
Appearance349.USE = "SegmentLine"

Shape346.appearance = Appearance349

HAnimSegment343.children.append(Shape346)
Transform350 = x3d.Transform()
Transform350.translation = [-0.13750000298023224,0.0060000000521540642,-0.029999999329447746]
Shape351 = x3d.Shape()
Shape351.USE = "skinsphere"

Transform350.children.append(Shape351)

HAnimSegment343.children.append(Transform350)
Transform352 = x3d.Transform()
Transform352.translation = [-0.094999998807907104,0.0060000000521540642,-0.029999999329447746]
Shape353 = x3d.Shape()
Shape353.USE = "skinsphere"

Transform352.children.append(Shape353)

HAnimSegment343.children.append(Transform352)
Transform354 = x3d.Transform()
Transform354.translation = [-0.094999998807907104,0.0060000000521540642,-0.029999999329447746]
Shape355 = x3d.Shape()
Shape355.USE = "skinsphere"

Transform354.children.append(Shape355)

HAnimSegment343.children.append(Transform354)

HAnimJoint342.children.append(HAnimSegment343)
HAnimJoint356 = x3d.HAnimJoint()
HAnimJoint356.DEF = "Joe_r_midtarsal"
HAnimJoint356.center = [-0.11500000208616257,0.037000000476837158,0.090000003576278687]
HAnimJoint356.name = "r_midtarsal"
HAnimJoint356.skinCoordIndex = [377,378,379,380]
HAnimJoint356.skinCoordWeight = [1,1,1,1]
HAnimJoint356.stiffness = [0,0,0]
HAnimSegment357 = x3d.HAnimSegment()
HAnimSegment357.DEF = "Joe_r_middistal"
HAnimSegment357.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment357.name = "r_middistal"
Transform358 = x3d.Transform()
Transform358.translation = [-0.10000000149011612,0.019999999552965164,0.070000000298023224]
Shape359 = x3d.Shape()
Shape359.USE = "jointbox"

Transform358.children.append(Shape359)

HAnimSegment357.children.append(Transform358)
Shape360 = x3d.Shape()
IndexedLineSet361 = x3d.IndexedLineSet()
IndexedLineSet361.coordIndex = [0,1,-1]
Coordinate362 = x3d.Coordinate()

IndexedLineSet361.coord = Coordinate362

Shape360.geometry = IndexedLineSet361
Appearance363 = x3d.Appearance()
Appearance363.USE = "SegmentLine"

Shape360.appearance = Appearance363

HAnimSegment357.children.append(Shape360)
Transform364 = x3d.Transform()
Transform364.translation = [-0.11500000208616257,0.059999998658895493,0.10000000149011612]
Shape365 = x3d.Shape()
Shape365.USE = "skinsphere"

Transform364.children.append(Shape365)

HAnimSegment357.children.append(Transform364)
Transform366 = x3d.Transform()
Transform366.translation = [-0.11500000208616257,0,0.070000000298023224]
Shape367 = x3d.Shape()
Shape367.USE = "skinsphere"

Transform366.children.append(Shape367)

HAnimSegment357.children.append(Transform366)
Transform368 = x3d.Transform()
Transform368.translation = [-0.16500000655651093,0,0.070000000298023224]
Shape369 = x3d.Shape()
Shape369.USE = "skinsphere"

Transform368.children.append(Shape369)

HAnimSegment357.children.append(Transform368)
Transform370 = x3d.Transform()
Transform370.translation = [-0.16500000655651093,0,0.070000000298023224]
Shape371 = x3d.Shape()
Shape371.USE = "skinsphere"

Transform370.children.append(Shape371)

HAnimSegment357.children.append(Transform370)
HAnimSite372 = x3d.HAnimSite()
HAnimSite372.DEF = "Joe_r_metatarsal_pha1"
HAnimSite372.name = "r_metatarsal_pha1"
HAnimSite372.translation = [-0.11500000208616257,0.019999999552965164,0.12200000137090683]
Shape373 = x3d.Shape()
Shape373.USE = "sitebox"

HAnimSite372.children.append(Shape373)

HAnimSegment357.children.append(HAnimSite372)

HAnimJoint356.children.append(HAnimSegment357)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.DEF = "Joe_r_metatarsal"
HAnimJoint374.center = [-0.10000000149011612,0.0099999997764825821,0.14000000059604645]
HAnimJoint374.name = "r_metatarsal"
HAnimJoint374.skinCoordIndex = [381,382,383,384,385,386,387,388,389]
HAnimJoint374.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint374.stiffness = [0,0,0]
HAnimSegment375 = x3d.HAnimSegment()
HAnimSegment375.DEF = "Joe_r_forefoot"
HAnimSegment375.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment375.name = "r_forefoot"
Transform376 = x3d.Transform()
Transform376.translation = [-0.10859999805688858,0.0099999997764825821,0.14000000059604645]
Shape377 = x3d.Shape()
Shape377.USE = "jointbox"

Transform376.children.append(Shape377)

HAnimSegment375.children.append(Transform376)
Shape378 = x3d.Shape()
IndexedLineSet379 = x3d.IndexedLineSet()
IndexedLineSet379.coordIndex = [0,1,-1]
Coordinate380 = x3d.Coordinate()

IndexedLineSet379.coord = Coordinate380

Shape378.geometry = IndexedLineSet379
Appearance381 = x3d.Appearance()
Appearance381.USE = "SegmentLine"

Shape378.appearance = Appearance381

HAnimSegment375.children.append(Shape378)
Transform382 = x3d.Transform()
Transform382.translation = [-0.11500000208616257,0.039999999105930328,0.12999999523162842]
Shape383 = x3d.Shape()
Shape383.USE = "skinsphere"

Transform382.children.append(Shape383)

HAnimSegment375.children.append(Transform382)
Transform384 = x3d.Transform()
Transform384.translation = [-0.125,0,0.11999999731779099]
Shape385 = x3d.Shape()
Shape385.USE = "skinsphere"

Transform384.children.append(Shape385)

HAnimSegment375.children.append(Transform384)
Transform386 = x3d.Transform()
Transform386.translation = [-0.16500000655651093,0,0.11999999731779099]
Shape387 = x3d.Shape()
Shape387.USE = "skinsphere"

Transform386.children.append(Shape387)

HAnimSegment375.children.append(Transform386)
Transform388 = x3d.Transform()
Transform388.translation = [-0.086999997496604919,0,0.12200000137090683]
Shape389 = x3d.Shape()
Shape389.USE = "skinsphere"

Transform388.children.append(Shape389)

HAnimSegment375.children.append(Transform388)
Transform390 = x3d.Transform()
Transform390.translation = [-0.090000003576278687,0.012000000104308128,0.18799999356269836]
Shape391 = x3d.Shape()
Shape391.USE = "skinsphere"

Transform390.children.append(Shape391)

HAnimSegment375.children.append(Transform390)
Transform392 = x3d.Transform()
Transform392.translation = [-0.10999999940395355,0.010999999940395355,0.18999999761581421]
Shape393 = x3d.Shape()
Shape393.USE = "skinsphere"

Transform392.children.append(Shape393)

HAnimSegment375.children.append(Transform392)
Transform394 = x3d.Transform()
Transform394.translation = [-0.12800000607967377,0.010999999940395355,0.18500000238418579]
Shape395 = x3d.Shape()
Shape395.USE = "skinsphere"

Transform394.children.append(Shape395)

HAnimSegment375.children.append(Transform394)
Transform396 = x3d.Transform()
Transform396.translation = [-0.14200000464916229,0.010999999940395355,0.17800000309944153]
Shape397 = x3d.Shape()
Shape397.USE = "skinsphere"

Transform396.children.append(Shape397)

HAnimSegment375.children.append(Transform396)
Transform398 = x3d.Transform()
Transform398.translation = [-0.15399999916553497,0.0099999997764825821,0.1679999977350235]
Shape399 = x3d.Shape()
Shape399.USE = "skinsphere"

Transform398.children.append(Shape399)

HAnimSegment375.children.append(Transform398)
HAnimSite400 = x3d.HAnimSite()
HAnimSite400.DEF = "Joe_r_metatarsal_pha5"
HAnimSite400.name = "r_metatarsal_pha5"
HAnimSite400.translation = [-0.16500000655651093,0.0099999997764825821,0.11999999731779099]
Shape401 = x3d.Shape()
Shape401.USE = "sitebox"

HAnimSite400.children.append(Shape401)

HAnimSegment375.children.append(HAnimSite400)
HAnimSite402 = x3d.HAnimSite()
HAnimSite402.DEF = "Joe_r_digit2"
HAnimSite402.name = "r_digit2"
HAnimSite402.translation = [-0.10999999940395355,0.010999999940395355,0.18999999761581421]
Shape403 = x3d.Shape()
Shape403.USE = "sitebox"

HAnimSite402.children.append(Shape403)

HAnimSegment375.children.append(HAnimSite402)

HAnimJoint374.children.append(HAnimSegment375)

HAnimJoint356.children.append(HAnimJoint374)

HAnimJoint342.children.append(HAnimJoint356)

HAnimJoint322.children.append(HAnimJoint342)

HAnimJoint294.children.append(HAnimJoint322)

HAnimJoint268.children.append(HAnimJoint294)

HAnimJoint102.children.append(HAnimJoint268)

HAnimJoint90.children.append(HAnimJoint102)
HAnimJoint404 = x3d.HAnimJoint()
HAnimJoint404.DEF = "Joe_vl5"
HAnimJoint404.center = [0,1.0449999570846558,-0.094999998807907104]
HAnimJoint404.name = "vl5"
HAnimJoint404.skinCoordIndex = [28,76]
HAnimJoint404.skinCoordWeight = [1,1]
HAnimJoint404.stiffness = [0,0,0]
HAnimSegment405 = x3d.HAnimSegment()
HAnimSegment405.DEF = "Joe_toPelvisMarker"
HAnimSegment405.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment405.name = "toPelvis"
Shape406 = x3d.Shape()
IndexedLineSet407 = x3d.IndexedLineSet()
IndexedLineSet407.coordIndex = [0,1,-1]
Coordinate408 = x3d.Coordinate()

IndexedLineSet407.coord = Coordinate408

Shape406.geometry = IndexedLineSet407
Appearance409 = x3d.Appearance()
Appearance409.USE = "SegmentLine"

Shape406.appearance = Appearance409

HAnimSegment405.children.append(Shape406)

HAnimJoint404.children.append(HAnimSegment405)
HAnimSegment410 = x3d.HAnimSegment()
HAnimSegment410.DEF = "Joe_l5"
HAnimSegment410.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment410.name = "l5"
Shape411 = x3d.Shape()
IndexedLineSet412 = x3d.IndexedLineSet()
IndexedLineSet412.coordIndex = [0,1,-1]
Coordinate413 = x3d.Coordinate()

IndexedLineSet412.coord = Coordinate413

Shape411.geometry = IndexedLineSet412
Appearance414 = x3d.Appearance()
Appearance414.USE = "SegmentLine"

Shape411.appearance = Appearance414

HAnimSegment410.children.append(Shape411)
HAnimSite415 = x3d.HAnimSite()
HAnimSite415.DEF = "Joe_waist_preferred_post"
HAnimSite415.name = "waist_preferred_post"
HAnimSite415.translation = [0,1.0915000438690186,-0.10909999907016754]
Shape416 = x3d.Shape()
Shape416.USE = "sitebox"

HAnimSite415.children.append(Shape416)

HAnimSegment410.children.append(HAnimSite415)
HAnimSite417 = x3d.HAnimSite()
HAnimSite417.DEF = "Joe_navel"
HAnimSite417.name = "navel"
HAnimSite417.translation = [0,1.0722500085830688,0.090000003576278687]
Shape418 = x3d.Shape()
Shape418.USE = "sitebox"

HAnimSite417.children.append(Shape418)

HAnimSegment410.children.append(HAnimSite417)

HAnimJoint404.children.append(HAnimSegment410)
HAnimJoint419 = x3d.HAnimJoint()
HAnimJoint419.DEF = "Joe_vl4"
HAnimJoint419.center = [0,1.068,-0.085]
HAnimJoint419.name = "vl4"
HAnimSegment420 = x3d.HAnimSegment()
HAnimSegment420.DEF = "Joe_l4"
HAnimSegment420.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment420.name = "l4"
Shape421 = x3d.Shape()
IndexedLineSet422 = x3d.IndexedLineSet()
IndexedLineSet422.coordIndex = [0,1,-1]
Coordinate423 = x3d.Coordinate()

IndexedLineSet422.coord = Coordinate423

Shape421.geometry = IndexedLineSet422
Appearance424 = x3d.Appearance()
Appearance424.USE = "SegmentLine"

Shape421.appearance = Appearance424

HAnimSegment420.children.append(Shape421)
Transform425 = x3d.Transform()
Transform425.translation = [0,1.068,-0.085]
Shape426 = x3d.Shape()
Shape426.USE = "jointbox"

Transform425.children.append(Shape426)

HAnimSegment420.children.append(Transform425)

HAnimJoint419.children.append(HAnimSegment420)
HAnimJoint427 = x3d.HAnimJoint()
HAnimJoint427.DEF = "Joe_vl3"
HAnimJoint427.center = [0,1.092,-0.0725]
HAnimJoint427.name = "vl3"
HAnimSegment428 = x3d.HAnimSegment()
HAnimSegment428.DEF = "Joe_l3"
HAnimSegment428.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment428.name = "l3"
Shape429 = x3d.Shape()
IndexedLineSet430 = x3d.IndexedLineSet()
IndexedLineSet430.coordIndex = [0,1,-1]
Coordinate431 = x3d.Coordinate()

IndexedLineSet430.coord = Coordinate431

Shape429.geometry = IndexedLineSet430
Appearance432 = x3d.Appearance()
Appearance432.USE = "SegmentLine"

Shape429.appearance = Appearance432

HAnimSegment428.children.append(Shape429)
Transform433 = x3d.Transform()
Transform433.translation = [0,1.092,-0.0725]
Shape434 = x3d.Shape()
Shape434.USE = "jointbox"

Transform433.children.append(Shape434)

HAnimSegment428.children.append(Transform433)

HAnimJoint427.children.append(HAnimSegment428)
HAnimJoint435 = x3d.HAnimJoint()
HAnimJoint435.DEF = "Joe_vl2"
HAnimJoint435.center = [0,1.12,-0.065]
HAnimJoint435.name = "vl2"
HAnimJoint435.skinCoordIndex = [16,18,25,83,84,85,86,87,88]
HAnimJoint435.skinCoordWeight = [1,1,1,1,1,1,0.7,1,0.8]
HAnimSegment436 = x3d.HAnimSegment()
HAnimSegment436.DEF = "Joe_l2"
HAnimSegment436.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment436.name = "l2"
Shape437 = x3d.Shape()
IndexedLineSet438 = x3d.IndexedLineSet()
IndexedLineSet438.coordIndex = [0,1,-1]
Coordinate439 = x3d.Coordinate()

IndexedLineSet438.coord = Coordinate439

Shape437.geometry = IndexedLineSet438
Appearance440 = x3d.Appearance()
Appearance440.USE = "SegmentLine"

Shape437.appearance = Appearance440

HAnimSegment436.children.append(Shape437)
Transform441 = x3d.Transform()
Transform441.translation = [0,1.1200000047683716,-0.064999997615814209]
Shape442 = x3d.Shape()
Shape442.USE = "jointbox"

Transform441.children.append(Shape442)

HAnimSegment436.children.append(Transform441)
Transform443 = x3d.Transform()
Transform443.translation = [-0.086999997496604919,1.190000057220459,-0.090000003576278687]
Shape444 = x3d.Shape()
Shape444.USE = "skinsphere"

Transform443.children.append(Shape444)

HAnimSegment436.children.append(Transform443)
Transform445 = x3d.Transform()
Transform445.translation = [0.086999997496604919,1.190000057220459,-0.090000003576278687]
Shape446 = x3d.Shape()
Shape446.USE = "skinsphere"

Transform445.children.append(Shape446)

HAnimSegment436.children.append(Transform445)
Transform447 = x3d.Transform()
Transform447.translation = [0.17200000584125519,1.3200000524520874,-0.029999999329447746]
Shape448 = x3d.Shape()
Shape448.USE = "skinsphere"

Transform447.children.append(Shape448)

HAnimSegment436.children.append(Transform447)
Transform449 = x3d.Transform()
Transform449.translation = [-0.17200000584125519,1.3200000524520874,-0.029999999329447746]
Shape450 = x3d.Shape()
Shape450.USE = "skinsphere"

Transform449.children.append(Shape450)

HAnimSegment436.children.append(Transform449)
Transform451 = x3d.Transform()
Transform451.translation = [0.15000000596046448,1.2300000190734863,-0.014999999664723873]
Shape452 = x3d.Shape()
Shape452.USE = "skinsphere"

Transform451.children.append(Shape452)

HAnimSegment436.children.append(Transform451)
Transform453 = x3d.Transform()
Transform453.translation = [-0.15000000596046448,1.2300000190734863,-0.014999999664723873]
Shape454 = x3d.Shape()
Shape454.USE = "skinsphere"

Transform453.children.append(Shape454)

HAnimSegment436.children.append(Transform453)
HAnimSite455 = x3d.HAnimSite()
HAnimSite455.DEF = "Joe_r_rib10"
HAnimSite455.name = "r_rib10"
HAnimSite455.translation = [-0.086999997496604919,1.190000057220459,0.090000003576278687]
Shape456 = x3d.Shape()
Shape456.USE = "sitebox"

HAnimSite455.children.append(Shape456)

HAnimSegment436.children.append(HAnimSite455)
HAnimSite457 = x3d.HAnimSite()
HAnimSite457.DEF = "Joe_l_rib10"
HAnimSite457.name = "l_rib10"
HAnimSite457.translation = [0.086999997496604919,1.190000057220459,0.090000003576278687]
Shape458 = x3d.Shape()
Shape458.USE = "sitebox"

HAnimSite457.children.append(Shape458)

HAnimSegment436.children.append(HAnimSite457)
HAnimSite459 = x3d.HAnimSite()
HAnimSite459.DEF = "Joe_rib10_midspine"
HAnimSite459.name = "rib10_midspine"
HAnimSite459.translation = [0,1.1908,-0.1113]
Shape460 = x3d.Shape()
Shape460.USE = "sitebox"

HAnimSite459.children.append(Shape460)

HAnimSegment436.children.append(HAnimSite459)

HAnimJoint435.children.append(HAnimSegment436)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.DEF = "Joe_vl1"
HAnimJoint461.center = [0,1.1459,-0.0625]
HAnimJoint461.name = "vl1"
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.DEF = "Joe_l1"
HAnimSegment462.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment462.name = "l1"
Shape463 = x3d.Shape()
IndexedLineSet464 = x3d.IndexedLineSet()
IndexedLineSet464.coordIndex = [0,1,-1]
Coordinate465 = x3d.Coordinate()

IndexedLineSet464.coord = Coordinate465

Shape463.geometry = IndexedLineSet464
Appearance466 = x3d.Appearance()
Appearance466.USE = "SegmentLine"

Shape463.appearance = Appearance466

HAnimSegment462.children.append(Shape463)
Transform467 = x3d.Transform()
Transform467.translation = [0,1.1459,-0.0625]
Shape468 = x3d.Shape()
Shape468.USE = "jointbox"

Transform467.children.append(Shape468)

HAnimSegment462.children.append(Transform467)

HAnimJoint461.children.append(HAnimSegment462)
HAnimJoint469 = x3d.HAnimJoint()
HAnimJoint469.DEF = "Joe_vt12"
HAnimJoint469.center = [0,1.1790000200271606,-0.068000003695487976]
HAnimJoint469.name = "vt12"
HAnimJoint469.stiffness = [0,0,0]
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.DEF = "Joe_t12"
HAnimSegment470.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment470.name = "t12"
Shape471 = x3d.Shape()
IndexedLineSet472 = x3d.IndexedLineSet()
IndexedLineSet472.coordIndex = [0,1,-1]
Coordinate473 = x3d.Coordinate()

IndexedLineSet472.coord = Coordinate473

Shape471.geometry = IndexedLineSet472
Appearance474 = x3d.Appearance()
Appearance474.USE = "SegmentLine"

Shape471.appearance = Appearance474

HAnimSegment470.children.append(Shape471)
Transform475 = x3d.Transform()
Transform475.translation = [0,1.1790000200271606,-0.068000003695487976]
Shape476 = x3d.Shape()
Shape476.USE = "jointbox"

Transform475.children.append(Shape476)

HAnimSegment470.children.append(Transform475)

HAnimJoint469.children.append(HAnimSegment470)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.DEF = "Joe_vt11"
HAnimJoint477.center = [0,1.2678999900817871,-0.081000000238418579]
HAnimJoint477.name = "vt11"
HAnimJoint477.stiffness = [0,0,0]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.DEF = "Joe_t11"
HAnimSegment478.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment478.name = "t11"
Shape479 = x3d.Shape()
IndexedLineSet480 = x3d.IndexedLineSet()
IndexedLineSet480.coordIndex = [0,1,-1]
Coordinate481 = x3d.Coordinate()

IndexedLineSet480.coord = Coordinate481

Shape479.geometry = IndexedLineSet480
Appearance482 = x3d.Appearance()
Appearance482.USE = "SegmentLine"

Shape479.appearance = Appearance482

HAnimSegment478.children.append(Shape479)
Transform483 = x3d.Transform()
Transform483.translation = [0,1.2144999504089355,-0.075499996542930603]
Shape484 = x3d.Shape()
Shape484.USE = "jointbox"

Transform483.children.append(Shape484)

HAnimSegment478.children.append(Transform483)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint485 = x3d.HAnimJoint()
HAnimJoint485.DEF = "Joe_vt10"
HAnimJoint485.center = [0,1.2419999837875366,-0.090000003576278687]
HAnimJoint485.name = "vt10"
HAnimJoint485.skinCoordIndex = [15]
HAnimJoint485.skinCoordWeight = [1]
HAnimJoint485.stiffness = [0,0,0]
HAnimSegment486 = x3d.HAnimSegment()
HAnimSegment486.DEF = "Joe_t10"
HAnimSegment486.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment486.name = "t10"
Shape487 = x3d.Shape()
IndexedLineSet488 = x3d.IndexedLineSet()
IndexedLineSet488.coordIndex = [0,1,-1]
Coordinate489 = x3d.Coordinate()

IndexedLineSet488.coord = Coordinate489

Shape487.geometry = IndexedLineSet488
Appearance490 = x3d.Appearance()
Appearance490.USE = "SegmentLine"

Shape487.appearance = Appearance490

HAnimSegment486.children.append(Shape487)
Transform491 = x3d.Transform()
Transform491.translation = [0,1.2419999837875366,-0.090000003576278687]
Shape492 = x3d.Shape()
Shape492.USE = "jointbox"

Transform491.children.append(Shape492)

HAnimSegment486.children.append(Transform491)
HAnimSite493 = x3d.HAnimSite()
HAnimSite493.DEF = "Joe_substernale"
HAnimSite493.name = "substernale"
HAnimSite493.translation = [0,1.25,0.11299999803304672]
Shape494 = x3d.Shape()
Shape494.USE = "sitebox"

HAnimSite493.children.append(Shape494)

HAnimSegment486.children.append(HAnimSite493)

HAnimJoint485.children.append(HAnimSegment486)
HAnimJoint495 = x3d.HAnimJoint()
HAnimJoint495.DEF = "Joe_vt9"
HAnimJoint495.center = [0,1.2680000066757202,-0.10000000149011612]
HAnimJoint495.name = "vt9"
HAnimJoint495.skinCoordIndex = [13,14]
HAnimJoint495.skinCoordWeight = [1,1]
HAnimJoint495.stiffness = [0,0,0]
HAnimSegment496 = x3d.HAnimSegment()
HAnimSegment496.DEF = "Joe_t9"
HAnimSegment496.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment496.name = "t9"
Shape497 = x3d.Shape()
IndexedLineSet498 = x3d.IndexedLineSet()
IndexedLineSet498.coordIndex = [0,1,-1]
Coordinate499 = x3d.Coordinate()

IndexedLineSet498.coord = Coordinate499

Shape497.geometry = IndexedLineSet498
Appearance500 = x3d.Appearance()
Appearance500.USE = "SegmentLine"

Shape497.appearance = Appearance500

HAnimSegment496.children.append(Shape497)
Transform501 = x3d.Transform()
Transform501.translation = [0,1.2680000066757202,-0.10000000149011612]
Shape502 = x3d.Shape()
Shape502.USE = "jointbox"

Transform501.children.append(Shape502)

HAnimSegment496.children.append(Transform501)
HAnimSite503 = x3d.HAnimSite()
HAnimSite503.DEF = "Joe_r_thelion"
HAnimSite503.name = "r_thelion"
HAnimSite503.translation = [-0.11349999904632568,1.3179999589920044,0.094999998807907104]
Shape504 = x3d.Shape()
Shape504.USE = "sitebox"

HAnimSite503.children.append(Shape504)

HAnimSegment496.children.append(HAnimSite503)
HAnimSite505 = x3d.HAnimSite()
HAnimSite505.DEF = "Joe_l_thelion"
HAnimSite505.name = "l_thelion"
HAnimSite505.translation = [0.11349999904632568,1.3179999589920044,0.094999998807907104]
Shape506 = x3d.Shape()
Shape506.USE = "sitebox"

HAnimSite505.children.append(Shape506)

HAnimSegment496.children.append(HAnimSite505)

HAnimJoint495.children.append(HAnimSegment496)
HAnimJoint507 = x3d.HAnimJoint()
HAnimJoint507.DEF = "Joe_vt8"
HAnimJoint507.center = [0,1.2940000295639038,-0.10999999940395355]
HAnimJoint507.name = "vt8"
HAnimJoint507.stiffness = [0,0,0]
HAnimSegment508 = x3d.HAnimSegment()
HAnimSegment508.DEF = "Joe_t8"
HAnimSegment508.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment508.name = "t8"
Shape509 = x3d.Shape()
IndexedLineSet510 = x3d.IndexedLineSet()
IndexedLineSet510.coordIndex = [0,1,-1]
Coordinate511 = x3d.Coordinate()

IndexedLineSet510.coord = Coordinate511

Shape509.geometry = IndexedLineSet510
Appearance512 = x3d.Appearance()
Appearance512.USE = "SegmentLine"

Shape509.appearance = Appearance512

HAnimSegment508.children.append(Shape509)
Transform513 = x3d.Transform()
Transform513.translation = [0,1.2940000295639038,-0.10999999940395355]
Shape514 = x3d.Shape()
Shape514.USE = "jointbox"

Transform513.children.append(Shape514)

HAnimSegment508.children.append(Transform513)

HAnimJoint507.children.append(HAnimSegment508)
HAnimJoint515 = x3d.HAnimJoint()
HAnimJoint515.DEF = "Joe_vt7"
HAnimJoint515.center = [0,1.3229999542236328,-0.11550000309944153]
HAnimJoint515.name = "vt7"
HAnimJoint515.stiffness = [0,0,0]
HAnimSegment516 = x3d.HAnimSegment()
HAnimSegment516.DEF = "Joe_t7"
HAnimSegment516.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment516.name = "t7"
Shape517 = x3d.Shape()
IndexedLineSet518 = x3d.IndexedLineSet()
IndexedLineSet518.coordIndex = [0,1,-1]
Coordinate519 = x3d.Coordinate()

IndexedLineSet518.coord = Coordinate519

Shape517.geometry = IndexedLineSet518
Appearance520 = x3d.Appearance()
Appearance520.USE = "SegmentLine"

Shape517.appearance = Appearance520

HAnimSegment516.children.append(Shape517)
Transform521 = x3d.Transform()
Transform521.translation = [0,1.3229999542236328,-0.11550000309944153]
Shape522 = x3d.Shape()
Shape522.USE = "jointbox"

Transform521.children.append(Shape522)

HAnimSegment516.children.append(Transform521)

HAnimJoint515.children.append(HAnimSegment516)
HAnimJoint523 = x3d.HAnimJoint()
HAnimJoint523.DEF = "Joe_vt6"
HAnimJoint523.center = [0,1.3519999980926514,-0.11999999731779099]
HAnimJoint523.name = "vt6"
HAnimJoint523.stiffness = [0,0,0]
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.DEF = "Joe_t6"
HAnimSegment524.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment524.name = "t6"
Shape525 = x3d.Shape()
IndexedLineSet526 = x3d.IndexedLineSet()
IndexedLineSet526.coordIndex = [0,1,-1]
Coordinate527 = x3d.Coordinate()

IndexedLineSet526.coord = Coordinate527

Shape525.geometry = IndexedLineSet526
Appearance528 = x3d.Appearance()
Appearance528.USE = "SegmentLine"

Shape525.appearance = Appearance528

HAnimSegment524.children.append(Shape525)
Transform529 = x3d.Transform()
Transform529.translation = [0,1.3519999980926514,-0.11999999731779099]
Shape530 = x3d.Shape()
Shape530.USE = "jointbox"

Transform529.children.append(Shape530)

HAnimSegment524.children.append(Transform529)

HAnimJoint523.children.append(HAnimSegment524)
HAnimJoint531 = x3d.HAnimJoint()
HAnimJoint531.DEF = "Joe_vt5"
HAnimJoint531.center = [0,1.3810000419616699,-0.12349999696016312]
HAnimJoint531.name = "vt5"
HAnimJoint531.stiffness = [0,0,0]
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.DEF = "Joe_t5"
HAnimSegment532.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment532.name = "t5"
Shape533 = x3d.Shape()
IndexedLineSet534 = x3d.IndexedLineSet()
IndexedLineSet534.coordIndex = [0,1,-1]
Coordinate535 = x3d.Coordinate()

IndexedLineSet534.coord = Coordinate535

Shape533.geometry = IndexedLineSet534
Appearance536 = x3d.Appearance()
Appearance536.USE = "SegmentLine"

Shape533.appearance = Appearance536

HAnimSegment532.children.append(Shape533)
Transform537 = x3d.Transform()
Transform537.translation = [0,1.3810000419616699,-0.12349999696016312]
Shape538 = x3d.Shape()
Shape538.USE = "jointbox"

Transform537.children.append(Shape538)

HAnimSegment532.children.append(Transform537)

HAnimJoint531.children.append(HAnimSegment532)
HAnimJoint539 = x3d.HAnimJoint()
HAnimJoint539.DEF = "Joe_vt4"
HAnimJoint539.center = [0,1.4099999666213989,-0.12349999696016312]
HAnimJoint539.name = "vt4"
HAnimJoint539.skinCoordIndex = [81]
HAnimJoint539.skinCoordWeight = [1]
HAnimJoint539.stiffness = [0,0,0]
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.DEF = "Joe_t4"
HAnimSegment540.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment540.name = "t4"
Shape541 = x3d.Shape()
IndexedLineSet542 = x3d.IndexedLineSet()
IndexedLineSet542.coordIndex = [0,1,-1]
Coordinate543 = x3d.Coordinate()

IndexedLineSet542.coord = Coordinate543

Shape541.geometry = IndexedLineSet542
Appearance544 = x3d.Appearance()
Appearance544.USE = "SegmentLine"

Shape541.appearance = Appearance544

HAnimSegment540.children.append(Shape541)
Transform545 = x3d.Transform()
Transform545.translation = [0,1.4099999666213989,-0.12349999696016312]
Shape546 = x3d.Shape()
Shape546.USE = "jointbox"

Transform545.children.append(Shape546)

HAnimSegment540.children.append(Transform545)
Transform547 = x3d.Transform()
Transform547.translation = [0,1.4099999666213989,-0.14499999582767487]
Shape548 = x3d.Shape()
Shape548.USE = "skinsphere"

Transform547.children.append(Shape548)

HAnimSegment540.children.append(Transform547)

HAnimJoint539.children.append(HAnimSegment540)
HAnimJoint549 = x3d.HAnimJoint()
HAnimJoint549.DEF = "Joe_vt3"
HAnimJoint549.center = [0,1.437999963760376,-0.11999999731779099]
HAnimJoint549.name = "vt3"
HAnimJoint549.stiffness = [0,0,0]
HAnimSegment550 = x3d.HAnimSegment()
HAnimSegment550.DEF = "Joe_t3"
HAnimSegment550.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment550.name = "t3"
Shape551 = x3d.Shape()
IndexedLineSet552 = x3d.IndexedLineSet()
IndexedLineSet552.coordIndex = [0,1,-1]
Coordinate553 = x3d.Coordinate()

IndexedLineSet552.coord = Coordinate553

Shape551.geometry = IndexedLineSet552
Appearance554 = x3d.Appearance()
Appearance554.USE = "SegmentLine"

Shape551.appearance = Appearance554

HAnimSegment550.children.append(Shape551)
Transform555 = x3d.Transform()
Transform555.translation = [0,1.437999963760376,-0.11999999731779099]
Shape556 = x3d.Shape()
Shape556.USE = "jointbox"

Transform555.children.append(Shape556)

HAnimSegment550.children.append(Transform555)

HAnimJoint549.children.append(HAnimSegment550)
HAnimJoint557 = x3d.HAnimJoint()
HAnimJoint557.DEF = "Joe_vt2"
HAnimJoint557.center = [0,1.468000054359436,-0.10499999672174454]
HAnimJoint557.name = "vt2"
HAnimJoint557.stiffness = [0,0,0]
HAnimSegment558 = x3d.HAnimSegment()
HAnimSegment558.DEF = "Joe_t2"
HAnimSegment558.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment558.name = "t2"
Shape559 = x3d.Shape()
IndexedLineSet560 = x3d.IndexedLineSet()
IndexedLineSet560.coordIndex = [0,1,-1]
Coordinate561 = x3d.Coordinate()

IndexedLineSet560.coord = Coordinate561

Shape559.geometry = IndexedLineSet560
Appearance562 = x3d.Appearance()
Appearance562.USE = "SegmentLine"

Shape559.appearance = Appearance562

HAnimSegment558.children.append(Shape559)
Transform563 = x3d.Transform()
Transform563.translation = [0,1.468000054359436,-0.10499999672174454]
Shape564 = x3d.Shape()
Shape564.USE = "jointbox"

Transform563.children.append(Shape564)

HAnimSegment558.children.append(Transform563)

HAnimJoint557.children.append(HAnimSegment558)
HAnimJoint565 = x3d.HAnimJoint()
HAnimJoint565.DEF = "Joe_vt1"
HAnimJoint565.center = [0,1.497,-0.09]
HAnimJoint565.name = "vt1"
HAnimJoint565.skinCoordIndex = [11,24]
HAnimJoint565.skinCoordWeight = [1,1]
HAnimSegment566 = x3d.HAnimSegment()
HAnimSegment566.DEF = "Joe_t1"
HAnimSegment566.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment566.name = "t1"
Shape567 = x3d.Shape()
IndexedLineSet568 = x3d.IndexedLineSet()
IndexedLineSet568.coordIndex = [0,1,-1]
Coordinate569 = x3d.Coordinate()

IndexedLineSet568.coord = Coordinate569

Shape567.geometry = IndexedLineSet568
Appearance570 = x3d.Appearance()
Appearance570.USE = "SegmentLine"

Shape567.appearance = Appearance570

HAnimSegment566.children.append(Shape567)
Transform571 = x3d.Transform()
Transform571.translation = [0,1.497,-0.09]
Shape572 = x3d.Shape()
Shape572.USE = "jointbox"

Transform571.children.append(Shape572)

HAnimSegment566.children.append(Transform571)
HAnimSite573 = x3d.HAnimSite()
HAnimSite573.DEF = "Joe_suprasternale"
HAnimSite573.name = "suprasternale"
HAnimSite573.translation = [0,1.440000057220459,0.029999999329447746]
Shape574 = x3d.Shape()
Shape574.USE = "sitebox"

HAnimSite573.children.append(Shape574)

HAnimSegment566.children.append(HAnimSite573)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.DEF = "Joe_cervicale"
HAnimSite575.name = "cervicale"
HAnimSite575.translation = [0,1.5299999713897705,-0.083999998867511749]
Shape576 = x3d.Shape()
Shape576.USE = "sitebox"

HAnimSite575.children.append(Shape576)

HAnimSegment566.children.append(HAnimSite575)

HAnimJoint565.children.append(HAnimSegment566)
HAnimJoint577 = x3d.HAnimJoint()
HAnimJoint577.DEF = "Joe_vc7"
HAnimJoint577.center = [0,1.5249999761581421,-0.071999996900558472]
HAnimJoint577.name = "vc7"
HAnimJoint577.skinCoordIndex = [74,75]
HAnimJoint577.skinCoordWeight = [1,1]
HAnimJoint577.stiffness = [0,0,0]
HAnimSegment578 = x3d.HAnimSegment()
HAnimSegment578.DEF = "Joe_c7"
HAnimSegment578.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment578.name = "c7"
Shape579 = x3d.Shape()
IndexedLineSet580 = x3d.IndexedLineSet()
IndexedLineSet580.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate581 = x3d.Coordinate()

IndexedLineSet580.coord = Coordinate581

Shape579.geometry = IndexedLineSet580
Appearance582 = x3d.Appearance()
Appearance582.USE = "SegmentLine"

Shape579.appearance = Appearance582

HAnimSegment578.children.append(Shape579)
Transform583 = x3d.Transform()
Transform583.translation = [0,1.5249999761581421,-0.071999996900558472]
Shape584 = x3d.Shape()
Shape584.USE = "jointbox"

Transform583.children.append(Shape584)

HAnimSegment578.children.append(Transform583)
HAnimSite585 = x3d.HAnimSite()
HAnimSite585.DEF = "Joe_r_neck_base"
HAnimSite585.name = "r_neck_base"
HAnimSite585.translation = [-0.064599998295307159,1.5148999691009521,-0.038499999791383743]
Shape586 = x3d.Shape()
Shape586.USE = "sitebox"

HAnimSite585.children.append(Shape586)

HAnimSegment578.children.append(HAnimSite585)
HAnimSite587 = x3d.HAnimSite()
HAnimSite587.DEF = "Joe_l_neck_base"
HAnimSite587.name = "l_neck_base"
HAnimSite587.translation = [0.064599998295307159,1.5148999691009521,-0.038499999791383743]
Shape588 = x3d.Shape()
Shape588.USE = "sitebox"

HAnimSite587.children.append(Shape588)

HAnimSegment578.children.append(HAnimSite587)

HAnimJoint577.children.append(HAnimSegment578)
HAnimJoint589 = x3d.HAnimJoint()
HAnimJoint589.DEF = "Joe_vc6"
HAnimJoint589.center = [0,1.5399999618530273,-0.05000000074505806]
HAnimJoint589.name = "vc6"
HAnimJoint589.stiffness = [0,0,0]
HAnimSegment590 = x3d.HAnimSegment()
HAnimSegment590.DEF = "Joe_c6"
HAnimSegment590.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment590.name = "c6"
Shape591 = x3d.Shape()
IndexedLineSet592 = x3d.IndexedLineSet()
IndexedLineSet592.coordIndex = [0,1,-1]
Coordinate593 = x3d.Coordinate()

IndexedLineSet592.coord = Coordinate593

Shape591.geometry = IndexedLineSet592
Appearance594 = x3d.Appearance()
Appearance594.USE = "SegmentLine"

Shape591.appearance = Appearance594

HAnimSegment590.children.append(Shape591)
Transform595 = x3d.Transform()
Transform595.translation = [0,1.5399999618530273,-0.05000000074505806]
Shape596 = x3d.Shape()
Shape596.USE = "jointbox"

Transform595.children.append(Shape596)

HAnimSegment590.children.append(Transform595)

HAnimJoint589.children.append(HAnimSegment590)
HAnimJoint597 = x3d.HAnimJoint()
HAnimJoint597.DEF = "Joe_vc5"
HAnimJoint597.center = [0,1.5520000457763672,-0.035000000149011612]
HAnimJoint597.name = "vc5"
HAnimJoint597.stiffness = [0,0,0]
HAnimSegment598 = x3d.HAnimSegment()
HAnimSegment598.DEF = "Joe_c5"
HAnimSegment598.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment598.name = "c5"
Transform599 = x3d.Transform()
Transform599.translation = [0,1.5520000457763672,-0.035000000149011612]
Shape600 = x3d.Shape()
Shape600.USE = "jointbox"

Transform599.children.append(Shape600)

HAnimSegment598.children.append(Transform599)
Shape601 = x3d.Shape()
IndexedLineSet602 = x3d.IndexedLineSet()
IndexedLineSet602.coordIndex = [0,1,-1]
Coordinate603 = x3d.Coordinate()

IndexedLineSet602.coord = Coordinate603

Shape601.geometry = IndexedLineSet602
Appearance604 = x3d.Appearance()
Appearance604.USE = "SegmentLine"

Shape601.appearance = Appearance604

HAnimSegment598.children.append(Shape601)

HAnimJoint597.children.append(HAnimSegment598)
HAnimJoint605 = x3d.HAnimJoint()
HAnimJoint605.DEF = "Joe_vc4"
HAnimJoint605.center = [0,1.5674999952316284,-0.025599999353289604]
HAnimJoint605.name = "vc4"
HAnimJoint605.stiffness = [0,0,0]
HAnimSegment606 = x3d.HAnimSegment()
HAnimSegment606.DEF = "Joe_c4"
HAnimSegment606.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment606.name = "c4"
Shape607 = x3d.Shape()
IndexedLineSet608 = x3d.IndexedLineSet()
IndexedLineSet608.coordIndex = [0,1,-1]
Coordinate609 = x3d.Coordinate()

IndexedLineSet608.coord = Coordinate609

Shape607.geometry = IndexedLineSet608
Appearance610 = x3d.Appearance()
Appearance610.USE = "SegmentLine"

Shape607.appearance = Appearance610

HAnimSegment606.children.append(Shape607)
Transform611 = x3d.Transform()
Transform611.translation = [0,1.5674999952316284,-0.025599999353289604]
Shape612 = x3d.Shape()
Shape612.USE = "jointbox"

Transform611.children.append(Shape612)

HAnimSegment606.children.append(Transform611)

HAnimJoint605.children.append(HAnimSegment606)
HAnimJoint613 = x3d.HAnimJoint()
HAnimJoint613.DEF = "Joe_vc3"
HAnimJoint613.center = [0,1.5822499990463257,-0.018500000238418579]
HAnimJoint613.name = "vc3"
HAnimJoint613.stiffness = [0,0,0]
HAnimSegment614 = x3d.HAnimSegment()
HAnimSegment614.DEF = "Joe_c3"
HAnimSegment614.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment614.name = "c3"
Shape615 = x3d.Shape()
IndexedLineSet616 = x3d.IndexedLineSet()
IndexedLineSet616.coordIndex = [0,1,-1]
Coordinate617 = x3d.Coordinate()

IndexedLineSet616.coord = Coordinate617

Shape615.geometry = IndexedLineSet616
Appearance618 = x3d.Appearance()
Appearance618.USE = "SegmentLine"

Shape615.appearance = Appearance618

HAnimSegment614.children.append(Shape615)
Transform619 = x3d.Transform()
Transform619.translation = [0,1.5822499990463257,-0.018500000238418579]
Shape620 = x3d.Shape()
Shape620.USE = "jointbox"

Transform619.children.append(Shape620)

HAnimSegment614.children.append(Transform619)

HAnimJoint613.children.append(HAnimSegment614)
HAnimJoint621 = x3d.HAnimJoint()
HAnimJoint621.DEF = "Joe_vc2"
HAnimJoint621.center = [0,1.5950000286102295,-0.017500000074505806]
HAnimJoint621.name = "vc2"
HAnimJoint621.stiffness = [0,0,0]
HAnimSegment622 = x3d.HAnimSegment()
HAnimSegment622.DEF = "Joe_c2"
HAnimSegment622.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment622.name = "c2"
Shape623 = x3d.Shape()
IndexedLineSet624 = x3d.IndexedLineSet()
IndexedLineSet624.coordIndex = [0,1,-1]
Coordinate625 = x3d.Coordinate()

IndexedLineSet624.coord = Coordinate625

Shape623.geometry = IndexedLineSet624
Appearance626 = x3d.Appearance()
Appearance626.USE = "SegmentLine"

Shape623.appearance = Appearance626

HAnimSegment622.children.append(Shape623)
Transform627 = x3d.Transform()
Transform627.translation = [0,1.5950000286102295,-0.017500000074505806]
Shape628 = x3d.Shape()
Shape628.USE = "jointbox"

Transform627.children.append(Shape628)

HAnimSegment622.children.append(Transform627)

HAnimJoint621.children.append(HAnimSegment622)
HAnimJoint629 = x3d.HAnimJoint()
HAnimJoint629.DEF = "Joe_vc1"
HAnimJoint629.center = [0,1.6100000143051147,-0.014999999664723873]
HAnimJoint629.name = "vc1"
HAnimJoint629.stiffness = [0,0,0]
HAnimSegment630 = x3d.HAnimSegment()
HAnimSegment630.DEF = "Joe_c1"
HAnimSegment630.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment630.name = "c1"
Shape631 = x3d.Shape()
IndexedLineSet632 = x3d.IndexedLineSet()
IndexedLineSet632.coordIndex = [0,1,-1]
Coordinate633 = x3d.Coordinate()

IndexedLineSet632.coord = Coordinate633

Shape631.geometry = IndexedLineSet632
Appearance634 = x3d.Appearance()
Appearance634.USE = "SegmentLine"

Shape631.appearance = Appearance634

HAnimSegment630.children.append(Shape631)
Transform635 = x3d.Transform()
Transform635.translation = [0,1.6100000143051147,-0.014999999664723873]
Shape636 = x3d.Shape()
Shape636.USE = "jointbox"

Transform635.children.append(Shape636)

HAnimSegment630.children.append(Transform635)

HAnimJoint629.children.append(HAnimSegment630)
HAnimJoint637 = x3d.HAnimJoint()
HAnimJoint637.DEF = "Joe_skullbase"
HAnimJoint637.center = [0,1.6299999952316284,-0.0099999997764825821]
HAnimJoint637.name = "skullbase"
HAnimJoint637.skinCoordIndex = [0,1,2,3,4,5,6,7,8,9]
HAnimJoint637.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1]
HAnimJoint637.stiffness = [0,0,0]
HAnimSegment638 = x3d.HAnimSegment()
HAnimSegment638.DEF = "Joe_skull"
HAnimSegment638.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment638.name = "skull"
Shape639 = x3d.Shape()
IndexedLineSet640 = x3d.IndexedLineSet()
IndexedLineSet640.coordIndex = [0,1,-1,0,2,-1]
Coordinate641 = x3d.Coordinate()

IndexedLineSet640.coord = Coordinate641

Shape639.geometry = IndexedLineSet640
Appearance642 = x3d.Appearance()
Appearance642.USE = "SegmentLine"

Shape639.appearance = Appearance642

HAnimSegment638.children.append(Shape639)
Transform643 = x3d.Transform()
Transform643.translation = [0,1.6299999952316284,-0.0099999997764825821]
Shape644 = x3d.Shape()
Shape644.USE = "jointbox"

Transform643.children.append(Shape644)

HAnimSegment638.children.append(Transform643)
HAnimSite645 = x3d.HAnimSite()
HAnimSite645.DEF = "Joe_skull_tip"
HAnimSite645.name = "skull_tip"
HAnimSite645.translation = [0,1.7699999809265137,0]
Shape646 = x3d.Shape()
Shape646.USE = "sitebox"

HAnimSite645.children.append(Shape646)

HAnimSegment638.children.append(HAnimSite645)
HAnimSite647 = x3d.HAnimSite()
HAnimSite647.DEF = "Joe_sellion"
HAnimSite647.name = "sellion"
HAnimSite647.translation = [0,1.6649999618530273,0.090000003576278687]
Shape648 = x3d.Shape()
Shape648.USE = "sitebox"

HAnimSite647.children.append(Shape648)

HAnimSegment638.children.append(HAnimSite647)
HAnimSite649 = x3d.HAnimSite()
HAnimSite649.DEF = "Joe_r_infraorbitale"
HAnimSite649.name = "r_infraorbitale"
HAnimSite649.translation = [-0.032999999821186066,1.6200000047683716,0.086999997496604919]
Shape650 = x3d.Shape()
Shape650.USE = "sitebox"

HAnimSite649.children.append(Shape650)

HAnimSegment638.children.append(HAnimSite649)
HAnimSite651 = x3d.HAnimSite()
HAnimSite651.DEF = "Joe_l_infraorbitale"
HAnimSite651.name = "l_infraorbitale"
HAnimSite651.translation = [0.032999999821186066,1.6200000047683716,0.086999997496604919]
Shape652 = x3d.Shape()
Shape652.USE = "sitebox"

HAnimSite651.children.append(Shape652)

HAnimSegment638.children.append(HAnimSite651)
HAnimSite653 = x3d.HAnimSite()
HAnimSite653.DEF = "Joe_supramenton"
HAnimSite653.name = "supramenton"
HAnimSite653.translation = [0,1.5499999523162842,0.097000002861022949]
Shape654 = x3d.Shape()
Shape654.USE = "sitebox"

HAnimSite653.children.append(Shape654)

HAnimSegment638.children.append(HAnimSite653)
HAnimSite655 = x3d.HAnimSite()
HAnimSite655.DEF = "Joe_r_tragion"
HAnimSite655.name = "r_tragion"
HAnimSite655.translation = [-0.076999999582767487,1.6399999856948853,-0.0099999997764825821]
Shape656 = x3d.Shape()
Shape656.USE = "sitebox"

HAnimSite655.children.append(Shape656)

HAnimSegment638.children.append(HAnimSite655)
HAnimSite657 = x3d.HAnimSite()
HAnimSite657.DEF = "Joe_r_gonion"
HAnimSite657.name = "r_gonion"
HAnimSite657.translation = [-0.052000001072883606,1.5800000429153442,0.014999999664723873]
Shape658 = x3d.Shape()
Shape658.USE = "sitebox"

HAnimSite657.children.append(Shape658)

HAnimSegment638.children.append(HAnimSite657)
HAnimSite659 = x3d.HAnimSite()
HAnimSite659.DEF = "Joe_l_tragion"
HAnimSite659.name = "l_tragion"
HAnimSite659.translation = [0.076999999582767487,1.6399999856948853,-0.0099999997764825821]
Shape660 = x3d.Shape()
Shape660.USE = "sitebox"

HAnimSite659.children.append(Shape660)

HAnimSegment638.children.append(HAnimSite659)
HAnimSite661 = x3d.HAnimSite()
HAnimSite661.DEF = "Joe_l_gonion"
HAnimSite661.name = "l_gonion"
HAnimSite661.translation = [0.063100002706050873,1.5800000429153442,0.014999999664723873]
Shape662 = x3d.Shape()
Shape662.USE = "sitebox"

HAnimSite661.children.append(Shape662)

HAnimSegment638.children.append(HAnimSite661)
HAnimSite663 = x3d.HAnimSite()
HAnimSite663.DEF = "Joe_nuchale"
HAnimSite663.name = "nuchale"
HAnimSite663.translation = [0,1.625,-0.092500001192092896]
Shape664 = x3d.Shape()
Shape664.USE = "sitebox"

HAnimSite663.children.append(Shape664)

HAnimSegment638.children.append(HAnimSite663)

HAnimJoint637.children.append(HAnimSegment638)
HAnimJoint665 = x3d.HAnimJoint()
HAnimJoint665.DEF = "Joe_l_eyeball_joint"
HAnimJoint665.center = [0.034,1.659,0.06]
HAnimJoint665.name = "l_eyeball_joint"
HAnimSegment666 = x3d.HAnimSegment()
HAnimSegment666.DEF = "Joe_l_eyeball"
HAnimSegment666.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment666.name = "l_eyeball"
Shape667 = x3d.Shape()
IndexedLineSet668 = x3d.IndexedLineSet()
IndexedLineSet668.coordIndex = [0,1,-1]
Coordinate669 = x3d.Coordinate()

IndexedLineSet668.coord = Coordinate669

Shape667.geometry = IndexedLineSet668
Appearance670 = x3d.Appearance()
Appearance670.USE = "SegmentLine"

Shape667.appearance = Appearance670

HAnimSegment666.children.append(Shape667)
Transform671 = x3d.Transform()
Transform671.scale = [1,1,1.4]
Transform671.translation = [0.034,1.655,0.065]
Shape672 = x3d.Shape()
Shape672.USE = "jointbox"

Transform671.children.append(Shape672)

HAnimSegment666.children.append(Transform671)

HAnimJoint665.children.append(HAnimSegment666)

HAnimJoint637.children.append(HAnimJoint665)
HAnimJoint673 = x3d.HAnimJoint()
HAnimJoint673.DEF = "Joe_r_eyeball_joint"
HAnimJoint673.center = [-0.034,1.659,0.06]
HAnimJoint673.name = "r_eyeball_joint"
HAnimSegment674 = x3d.HAnimSegment()
HAnimSegment674.DEF = "Joe_r_eyeball"
HAnimSegment674.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment674.name = "r_eyeball"
Shape675 = x3d.Shape()
IndexedLineSet676 = x3d.IndexedLineSet()
IndexedLineSet676.coordIndex = [0,1,-1]
Coordinate677 = x3d.Coordinate()

IndexedLineSet676.coord = Coordinate677

Shape675.geometry = IndexedLineSet676
Appearance678 = x3d.Appearance()
Appearance678.USE = "SegmentLine"

Shape675.appearance = Appearance678

HAnimSegment674.children.append(Shape675)
Transform679 = x3d.Transform()
Transform679.scale = [1,1,1.4]
Transform679.translation = [-0.034,1.655,0.065]
Shape680 = x3d.Shape()
Shape680.USE = "jointbox"

Transform679.children.append(Shape680)

HAnimSegment674.children.append(Transform679)

HAnimJoint673.children.append(HAnimSegment674)

HAnimJoint637.children.append(HAnimJoint673)

HAnimJoint629.children.append(HAnimJoint637)

HAnimJoint621.children.append(HAnimJoint629)

HAnimJoint613.children.append(HAnimJoint621)

HAnimJoint605.children.append(HAnimJoint613)

HAnimJoint597.children.append(HAnimJoint605)

HAnimJoint589.children.append(HAnimJoint597)

HAnimJoint577.children.append(HAnimJoint589)

HAnimJoint565.children.append(HAnimJoint577)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.DEF = "Joe_l_sternoclavicular"
HAnimJoint681.center = [0.082,1.4488,-0.0353]
HAnimJoint681.name = "l_sternoclavicular"
HAnimJoint681.skinCoordIndex = [12]
HAnimJoint681.skinCoordWeight = [1]
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.DEF = "Joe_l_clavicle"
HAnimSegment682.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment682.name = "l_clavicle"
Shape683 = x3d.Shape()
IndexedLineSet684 = x3d.IndexedLineSet()
IndexedLineSet684.coordIndex = [0,1,-1]
Coordinate685 = x3d.Coordinate()

IndexedLineSet684.coord = Coordinate685

Shape683.geometry = IndexedLineSet684
Appearance686 = x3d.Appearance()
Appearance686.USE = "SegmentLine"

Shape683.appearance = Appearance686

HAnimSegment682.children.append(Shape683)
Transform687 = x3d.Transform()
Transform687.translation = [0.082000002264976501,1.4487999677658081,-0.035300001502037048]
Shape688 = x3d.Shape()
Shape688.USE = "jointbox"

Transform687.children.append(Shape688)

HAnimSegment682.children.append(Transform687)
HAnimSite689 = x3d.HAnimSite()
HAnimSite689.DEF = "Joe_l_clavicale"
HAnimSite689.name = "l_clavicale"
HAnimSite689.translation = [0.029999999329447746,1.4600000381469727,0.035000000149011612]
Shape690 = x3d.Shape()
Shape690.USE = "sitebox"

HAnimSite689.children.append(Shape690)

HAnimSegment682.children.append(HAnimSite689)

HAnimJoint681.children.append(HAnimSegment682)
HAnimJoint691 = x3d.HAnimJoint()
HAnimJoint691.DEF = "Joe_l_acromioclavicular"
HAnimJoint691.center = [0.096199996769428253,1.4269000291824341,-0.042399998754262924]
HAnimJoint691.name = "l_acromioclavicular"
HAnimJoint691.skinCoordIndex = [79]
HAnimJoint691.skinCoordWeight = [1]
HAnimJoint691.stiffness = [0,0,0]
HAnimSegment692 = x3d.HAnimSegment()
HAnimSegment692.DEF = "Joe_l_scapula"
HAnimSegment692.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment692.name = "l_scapula"
Shape693 = x3d.Shape()
IndexedLineSet694 = x3d.IndexedLineSet()
IndexedLineSet694.coordIndex = [0,1,-1]
Coordinate695 = x3d.Coordinate()

IndexedLineSet694.coord = Coordinate695

Shape693.geometry = IndexedLineSet694
Appearance696 = x3d.Appearance()
Appearance696.USE = "SegmentLine"

Shape693.appearance = Appearance696

HAnimSegment692.children.append(Shape693)
Transform697 = x3d.Transform()
Transform697.translation = [0.096199996769428253,1.4269000291824341,-0.042399998754262924]
Shape698 = x3d.Shape()
Shape698.USE = "jointbox"

Transform697.children.append(Shape698)

HAnimSegment692.children.append(Transform697)
Transform699 = x3d.Transform()
Transform699.translation = [0.10999999940395355,1.4270000457763672,-0.13750000298023224]
Shape700 = x3d.Shape()
Shape700.USE = "skinsphere"

Transform699.children.append(Shape700)

HAnimSegment692.children.append(Transform699)
HAnimSite701 = x3d.HAnimSite()
HAnimSite701.DEF = "Joe_l_acromion"
HAnimSite701.name = "l_acromion"
HAnimSite701.translation = [0.17499999701976776,1.4824999570846558,-0.059999998658895493]
Shape702 = x3d.Shape()
Shape702.USE = "sitebox"

HAnimSite701.children.append(Shape702)

HAnimSegment692.children.append(HAnimSite701)
HAnimSite703 = x3d.HAnimSite()
HAnimSite703.DEF = "Joe_l_axilla_ant"
HAnimSite703.name = "l_axilla_ant"
HAnimSite703.translation = [0.17000000178813934,1.3799999952316284,0.0070000002160668373]
Shape704 = x3d.Shape()
Shape704.USE = "sitebox"

HAnimSite703.children.append(Shape704)

HAnimSegment692.children.append(HAnimSite703)
HAnimSite705 = x3d.HAnimSite()
HAnimSite705.DEF = "Joe_l_axilla_post"
HAnimSite705.name = "l_axilla_post"
HAnimSite705.translation = [0.15999999642372131,1.3799999952316284,-0.125]
Shape706 = x3d.Shape()
Shape706.USE = "sitebox"

HAnimSite705.children.append(Shape706)

HAnimSegment692.children.append(HAnimSite705)

HAnimJoint691.children.append(HAnimSegment692)
HAnimJoint707 = x3d.HAnimJoint()
HAnimJoint707.DEF = "Joe_l_shoulder"
HAnimJoint707.center = [0.20000000298023224,1.440000057220459,-0.039999999105930328]
HAnimJoint707.name = "l_shoulder"
HAnimJoint707.skinCoordIndex = [41,42,44,80,102,103,104,105]
HAnimJoint707.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint707.stiffness = [0,0,0]
HAnimSegment708 = x3d.HAnimSegment()
HAnimSegment708.DEF = "Joe_l_upperarm"
HAnimSegment708.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment708.name = "l_upperarm"
Shape709 = x3d.Shape()
IndexedLineSet710 = x3d.IndexedLineSet()
IndexedLineSet710.coordIndex = [0,1,-1]
Coordinate711 = x3d.Coordinate()

IndexedLineSet710.coord = Coordinate711

Shape709.geometry = IndexedLineSet710
Appearance712 = x3d.Appearance()
Appearance712.USE = "SegmentLine"

Shape709.appearance = Appearance712

HAnimSegment708.children.append(Shape709)
Transform713 = x3d.Transform()
Transform713.translation = [0.20000000298023224,1.440000057220459,-0.039999999105930328]
Shape714 = x3d.Shape()
Shape714.USE = "jointbox"

Transform713.children.append(Shape714)

HAnimSegment708.children.append(Transform713)
Transform715 = x3d.Transform()
Transform715.translation = [0.23499999940395355,1.4199999570846558,-0.0625]
Shape716 = x3d.Shape()
Shape716.USE = "skinsphere"

Transform715.children.append(Shape716)

HAnimSegment708.children.append(Transform715)
Transform717 = x3d.Transform()
Transform717.translation = [0.25,1.2699999809265137,-0.039999999105930328]
Shape718 = x3d.Shape()
Shape718.USE = "skinsphere"

Transform717.children.append(Shape718)

HAnimSegment708.children.append(Transform717)
Transform719 = x3d.Transform()
Transform719.translation = [0.17000000178813934,1.2699999809265137,-0.039999999105930328]
Shape720 = x3d.Shape()
Shape720.USE = "skinsphere"

Transform719.children.append(Shape720)

HAnimSegment708.children.append(Transform719)
Transform721 = x3d.Transform()
Transform721.translation = [0.20000000298023224,1.2699999809265137,-0.090000003576278687]
Shape722 = x3d.Shape()
Shape722.USE = "skinsphere"

Transform721.children.append(Shape722)

HAnimSegment708.children.append(Transform721)
Transform723 = x3d.Transform()
Transform723.translation = [0.20000000298023224,1.2699999809265137,0.019999999552965164]
Shape724 = x3d.Shape()
Shape724.USE = "skinsphere"

Transform723.children.append(Shape724)

HAnimSegment708.children.append(Transform723)
HAnimSite725 = x3d.HAnimSite()
HAnimSite725.DEF = "Joe_l_humeral_medial_epicn"
HAnimSite725.name = "l_humeral_medial_epicn"
HAnimSite725.translation = [0.16500000655651093,1.1388000249862671,-0.039999999105930328]
Shape726 = x3d.Shape()
Shape726.USE = "sitebox"

HAnimSite725.children.append(Shape726)

HAnimSegment708.children.append(HAnimSite725)
HAnimSite727 = x3d.HAnimSite()
HAnimSite727.DEF = "Joe_l_radiale"
HAnimSite727.name = "l_radiale"
HAnimSite727.translation = [0.23000000417232513,1.1330000162124634,-0.054999999701976776]
Shape728 = x3d.Shape()
Shape728.USE = "sitebox"

HAnimSite727.children.append(Shape728)

HAnimSegment708.children.append(HAnimSite727)
HAnimSite729 = x3d.HAnimSite()
HAnimSite729.DEF = "Joe_l_humeral_lateral_epicn"
HAnimSite729.name = "l_humeral_lateral_epicn"
HAnimSite729.translation = [0.24400000274181366,1.1388000249862671,-0.039999999105930328]
Shape730 = x3d.Shape()
Shape730.USE = "sitebox"

HAnimSite729.children.append(Shape730)

HAnimSegment708.children.append(HAnimSite729)

HAnimJoint707.children.append(HAnimSegment708)
HAnimJoint731 = x3d.HAnimJoint()
HAnimJoint731.DEF = "Joe_l_elbow"
HAnimJoint731.center = [0.20000000298023224,1.1388000249862671,-0.039999999105930328]
HAnimJoint731.name = "l_elbow"
HAnimJoint731.skinCoordIndex = [45,46,47,109,110,111,112,113,115,116,117,118]
HAnimJoint731.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint731.stiffness = [0,0,0]
HAnimSegment732 = x3d.HAnimSegment()
HAnimSegment732.DEF = "Joe_l_forearm"
HAnimSegment732.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment732.name = "l_forearm"
Shape733 = x3d.Shape()
IndexedLineSet734 = x3d.IndexedLineSet()
IndexedLineSet734.coordIndex = [0,1,-1]
Coordinate735 = x3d.Coordinate()

IndexedLineSet734.coord = Coordinate735

Shape733.geometry = IndexedLineSet734
Appearance736 = x3d.Appearance()
Appearance736.USE = "SegmentLine"

Shape733.appearance = Appearance736

HAnimSegment732.children.append(Shape733)
Transform737 = x3d.Transform()
Transform737.translation = [0.20000000298023224,1.1388000249862671,-0.039999999105930328]
Shape738 = x3d.Shape()
Shape738.USE = "jointbox"

Transform737.children.append(Shape738)

HAnimSegment732.children.append(Transform737)
Transform739 = x3d.Transform()
Transform739.translation = [0.20000000298023224,1.1388000249862671,-0.013000000268220901]
Shape740 = x3d.Shape()
Shape740.USE = "skinsphere"

Transform739.children.append(Shape740)

HAnimSegment732.children.append(Transform739)
Transform741 = x3d.Transform()
Transform741.translation = [0.22499999403953552,1,-0.0099999997764825821]
Shape742 = x3d.Shape()
Shape742.USE = "skinsphere"

Transform741.children.append(Shape742)

HAnimSegment732.children.append(Transform741)
Transform743 = x3d.Transform()
Transform743.translation = [0.22499999403953552,1,-0.070000000298023224]
Shape744 = x3d.Shape()
Shape744.USE = "skinsphere"

Transform743.children.append(Shape744)

HAnimSegment732.children.append(Transform743)
Transform745 = x3d.Transform()
Transform745.translation = [0.18500000238418579,1,-0.0099999997764825821]
Shape746 = x3d.Shape()
Shape746.USE = "skinsphere"

Transform745.children.append(Shape746)

HAnimSegment732.children.append(Transform745)
Transform747 = x3d.Transform()
Transform747.translation = [0.18500000238418579,1,-0.070000000298023224]
Shape748 = x3d.Shape()
Shape748.USE = "skinsphere"

Transform747.children.append(Shape748)

HAnimSegment732.children.append(Transform747)
HAnimSite749 = x3d.HAnimSite()
HAnimSite749.DEF = "Joe_l_radial_styloid"
HAnimSite749.name = "l_radial_styloid"
HAnimSite749.translation = [0.19009999930858612,0.86449998617172241,-0.041499998420476913]
Shape750 = x3d.Shape()
Shape750.USE = "sitebox"

HAnimSite749.children.append(Shape750)

HAnimSegment732.children.append(HAnimSite749)
HAnimSite751 = x3d.HAnimSite()
HAnimSite751.DEF = "Joe_l_olecranon"
HAnimSite751.name = "l_olecranon"
HAnimSite751.translation = [0.20000000298023224,1.1388000249862671,-0.079999998211860657]
Shape752 = x3d.Shape()
Shape752.USE = "sitebox"

HAnimSite751.children.append(Shape752)

HAnimSegment732.children.append(HAnimSite751)

HAnimJoint731.children.append(HAnimSegment732)
HAnimJoint753 = x3d.HAnimJoint()
HAnimJoint753.DEF = "Joe_l_wrist"
HAnimJoint753.center = [0.20000000298023224,0.87000000476837158,-0.039999999105930328]
HAnimJoint753.name = "l_wrist"
HAnimJoint753.skinCoordIndex = [119,120,121,122,123,124,125,126]
HAnimJoint753.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint753.stiffness = [0,0,0]
HAnimSegment754 = x3d.HAnimSegment()
HAnimSegment754.DEF = "Joe_l_hand"
HAnimSegment754.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment754.name = "l_hand"
Shape755 = x3d.Shape()
IndexedLineSet756 = x3d.IndexedLineSet()
IndexedLineSet756.coordIndex = [0,1,-1,0,2,-1,0,3,-1,0,4,-1,0,5,-1]
Coordinate757 = x3d.Coordinate()

IndexedLineSet756.coord = Coordinate757

Shape755.geometry = IndexedLineSet756
Appearance758 = x3d.Appearance()
Appearance758.USE = "SegmentLine"

Shape755.appearance = Appearance758

HAnimSegment754.children.append(Shape755)
Transform759 = x3d.Transform()
Transform759.translation = [0.20000000298023224,0.87000000476837158,-0.039999999105930328]
Shape760 = x3d.Shape()
Shape760.USE = "jointbox"

Transform759.children.append(Shape760)

HAnimSegment754.children.append(Transform759)
HAnimSite761 = x3d.HAnimSite()
HAnimSite761.DEF = "Joe_l_metacarpal_pha2"
HAnimSite761.name = "l_metacarpal_pha2"
HAnimSite761.translation = [0.20090000331401825,0.81389999389648438,-0.02370000071823597]
Shape762 = x3d.Shape()
Shape762.USE = "sitebox"

HAnimSite761.children.append(Shape762)

HAnimSegment754.children.append(HAnimSite761)
HAnimSite763 = x3d.HAnimSite()
HAnimSite763.DEF = "Joe_l_ulnar_styloid"
HAnimSite763.name = "l_ulnar_styloid"
HAnimSite763.translation = [0.21420000493526459,0.85290002822875977,-0.064800001680850983]
Shape764 = x3d.Shape()
Shape764.USE = "sitebox"

HAnimSite763.children.append(Shape764)

HAnimSegment754.children.append(HAnimSite763)
HAnimSite765 = x3d.HAnimSite()
HAnimSite765.DEF = "Joe_l_metacarpal_pha5"
HAnimSite765.name = "l_metacarpal_pha5"
HAnimSite765.translation = [0.19290000200271606,0.78600001335144043,-0.11219999939203262]
Shape766 = x3d.Shape()
Shape766.USE = "sitebox"

HAnimSite765.children.append(Shape766)

HAnimSegment754.children.append(HAnimSite765)

HAnimJoint753.children.append(HAnimSegment754)
HAnimJoint767 = x3d.HAnimJoint()
HAnimJoint767.DEF = "Joe_l_thumb1"
HAnimJoint767.center = [0.19239999353885651,0.84719997644424438,-0.053399998694658279]
HAnimJoint767.name = "l_thumb1"
HAnimJoint767.skinCoordIndex = [127,128]
HAnimJoint767.skinCoordWeight = [1,1]
HAnimJoint767.stiffness = [0,0,0]
HAnimSegment768 = x3d.HAnimSegment()
HAnimSegment768.DEF = "Joe_l_thumb_metacarpal"
HAnimSegment768.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment768.name = "l_thumb_metacarpal"
Shape769 = x3d.Shape()
IndexedLineSet770 = x3d.IndexedLineSet()
IndexedLineSet770.coordIndex = [0,1,-1]
Coordinate771 = x3d.Coordinate()

IndexedLineSet770.coord = Coordinate771

Shape769.geometry = IndexedLineSet770
Appearance772 = x3d.Appearance()
Appearance772.USE = "SegmentLine"

Shape769.appearance = Appearance772

HAnimSegment768.children.append(Shape769)
Transform773 = x3d.Transform()
Transform773.translation = [0.19239999353885651,0.84719997644424438,-0.053399998694658279]
Shape774 = x3d.Shape()
Shape774.USE = "jointbox"

Transform773.children.append(Shape774)

HAnimSegment768.children.append(Transform773)

HAnimJoint767.children.append(HAnimSegment768)
HAnimJoint775 = x3d.HAnimJoint()
HAnimJoint775.DEF = "Joe_l_thumb2"
HAnimJoint775.center = [0.19509999454021454,0.82260000705718994,0.024599999189376831]
HAnimJoint775.name = "l_thumb2"
HAnimJoint775.skinCoordIndex = [138,139,140,141,142,143]
HAnimJoint775.skinCoordWeight = [0.5,0.5,0.5,1,1,1]
HAnimJoint775.stiffness = [0,0,0]
HAnimSegment776 = x3d.HAnimSegment()
HAnimSegment776.DEF = "Joe_l_thumb_proximal"
HAnimSegment776.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment776.name = "l_thumb_distal"
Shape777 = x3d.Shape()
IndexedLineSet778 = x3d.IndexedLineSet()
IndexedLineSet778.coordIndex = [0,1,-1]
Coordinate779 = x3d.Coordinate()

IndexedLineSet778.coord = Coordinate779

Shape777.geometry = IndexedLineSet778
Appearance780 = x3d.Appearance()
Appearance780.USE = "SegmentLine"

Shape777.appearance = Appearance780

HAnimSegment776.children.append(Shape777)
Transform781 = x3d.Transform()
Transform781.translation = [0.19509999454021454,0.82260000705718994,0.024599999189376831]
Shape782 = x3d.Shape()
Shape782.USE = "jointbox"

Transform781.children.append(Shape782)

HAnimSegment776.children.append(Transform781)

HAnimJoint775.children.append(HAnimSegment776)
HAnimJoint783 = x3d.HAnimJoint()
HAnimJoint783.DEF = "Joe_l_thumb3"
HAnimJoint783.center = [0.19550000131130219,0.81590002775192261,0.046399999409914017]
HAnimJoint783.name = "l_thumb3"
HAnimJoint783.skinCoordIndex = [144,145,146,147,148,149,150,151,152]
HAnimJoint783.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint783.stiffness = [0,0,0]
HAnimSegment784 = x3d.HAnimSegment()
HAnimSegment784.DEF = "Joe_l_thumb_distal"
HAnimSegment784.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment784.name = "l_thumb_distal"
Shape785 = x3d.Shape()
IndexedLineSet786 = x3d.IndexedLineSet()
IndexedLineSet786.coordIndex = [0,1,-1]
Coordinate787 = x3d.Coordinate()

IndexedLineSet786.coord = Coordinate787

Shape785.geometry = IndexedLineSet786
Appearance788 = x3d.Appearance()
Appearance788.USE = "SegmentLine"

Shape785.appearance = Appearance788

HAnimSegment784.children.append(Shape785)
Transform789 = x3d.Transform()
Transform789.translation = [0.19550000131130219,0.81590002775192261,0.046399999409914017]
Shape790 = x3d.Shape()
Shape790.USE = "jointbox"

Transform789.children.append(Shape790)

HAnimSegment784.children.append(Transform789)
HAnimSite791 = x3d.HAnimSite()
HAnimSite791.DEF = "Joe_l_thumb_distal_tip"
HAnimSite791.name = "l_thumb_distal_tip"
HAnimSite791.translation = [0.19820000231266022,0.80610001087188721,0.07590000331401825]
Shape792 = x3d.Shape()
Shape792.USE = "sitebox"

HAnimSite791.children.append(Shape792)

HAnimSegment784.children.append(HAnimSite791)

HAnimJoint783.children.append(HAnimSegment784)

HAnimJoint775.children.append(HAnimJoint783)

HAnimJoint767.children.append(HAnimJoint775)

HAnimJoint753.children.append(HAnimJoint767)
HAnimJoint793 = x3d.HAnimJoint()
HAnimJoint793.DEF = "Joe_l_index0"
HAnimJoint793.center = [0.19830000400543213,0.80239999294281006,-0.028000000864267349]
HAnimJoint793.name = "l_index0"
HAnimJoint793.skinCoordIndex = [129,130]
HAnimJoint793.skinCoordWeight = [1,1]
HAnimJoint793.stiffness = [0,0,0]
HAnimSegment794 = x3d.HAnimSegment()
HAnimSegment794.DEF = "Joe_l_index_metacarpal"
HAnimSegment794.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment794.name = "l_index_metacarpal"
Shape795 = x3d.Shape()
IndexedLineSet796 = x3d.IndexedLineSet()
IndexedLineSet796.coordIndex = [0,1,-1]
Coordinate797 = x3d.Coordinate()

IndexedLineSet796.coord = Coordinate797

Shape795.geometry = IndexedLineSet796
Appearance798 = x3d.Appearance()
Appearance798.USE = "SegmentLine"

Shape795.appearance = Appearance798

HAnimSegment794.children.append(Shape795)
Transform799 = x3d.Transform()
Transform799.translation = [0.1983,0.8024,-0.028]
Shape800 = x3d.Shape()
Shape800.USE = "jointbox"

Transform799.children.append(Shape800)

HAnimSegment794.children.append(Transform799)

HAnimJoint793.children.append(HAnimSegment794)
HAnimJoint801 = x3d.HAnimJoint()
HAnimJoint801.DEF = "Joe_l_index1"
HAnimJoint801.center = [0.1983,0.7815,-0.028]
HAnimJoint801.name = "l_index1"
HAnimJoint801.skinCoordIndex = [138,139,140,153,154,155,163]
HAnimJoint801.skinCoordWeight = [0.5,0.5,0.5,1,1,1,0.5]
HAnimSegment802 = x3d.HAnimSegment()
HAnimSegment802.DEF = "Joe_l_index_proximal"
HAnimSegment802.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment802.name = "l_index_proximal"
Shape803 = x3d.Shape()
IndexedLineSet804 = x3d.IndexedLineSet()
IndexedLineSet804.coordIndex = [0,1,-1]
Coordinate805 = x3d.Coordinate()

IndexedLineSet804.coord = Coordinate805

Shape803.geometry = IndexedLineSet804
Appearance806 = x3d.Appearance()
Appearance806.USE = "SegmentLine"

Shape803.appearance = Appearance806

HAnimSegment802.children.append(Shape803)
Transform807 = x3d.Transform()
Transform807.translation = [0.1983,0.7815,-0.028]
Shape808 = x3d.Shape()
Shape808.USE = "jointbox"

Transform807.children.append(Shape808)

HAnimSegment802.children.append(Transform807)

HAnimJoint801.children.append(HAnimSegment802)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.DEF = "Joe_l_index2"
HAnimJoint809.center = [0.2017,0.7363,-0.0248]
HAnimJoint809.name = "l_index2"
HAnimJoint809.skinCoordIndex = [166,167,168,169]
HAnimJoint809.skinCoordWeight = [1,1,1,1]
HAnimSegment810 = x3d.HAnimSegment()
HAnimSegment810.DEF = "Joe_l_index_middle"
HAnimSegment810.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment810.name = "l_index_middle"
Shape811 = x3d.Shape()
IndexedLineSet812 = x3d.IndexedLineSet()
IndexedLineSet812.coordIndex = [0,1,-1]
Coordinate813 = x3d.Coordinate()

IndexedLineSet812.coord = Coordinate813

Shape811.geometry = IndexedLineSet812
Appearance814 = x3d.Appearance()
Appearance814.USE = "SegmentLine"

Shape811.appearance = Appearance814

HAnimSegment810.children.append(Shape811)
Transform815 = x3d.Transform()
Transform815.translation = [0.2017,0.7363,-0.0248]
Shape816 = x3d.Shape()
Shape816.USE = "jointbox"

Transform815.children.append(Shape816)

HAnimSegment810.children.append(Transform815)

HAnimJoint809.children.append(HAnimSegment810)
HAnimJoint817 = x3d.HAnimJoint()
HAnimJoint817.DEF = "Joe_l_index3"
HAnimJoint817.center = [0.20280000567436218,0.71390002965927124,-0.023600000888109207]
HAnimJoint817.name = "l_index3"
HAnimJoint817.skinCoordIndex = [170,171,172,173,174,175,176,177,178]
HAnimJoint817.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint817.stiffness = [0,0,0]
HAnimSegment818 = x3d.HAnimSegment()
HAnimSegment818.DEF = "Joe_l_index_distal"
HAnimSegment818.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment818.name = "l_index_distal"
Shape819 = x3d.Shape()
IndexedLineSet820 = x3d.IndexedLineSet()
IndexedLineSet820.coordIndex = [0,1,-1]
Coordinate821 = x3d.Coordinate()

IndexedLineSet820.coord = Coordinate821

Shape819.geometry = IndexedLineSet820
Appearance822 = x3d.Appearance()
Appearance822.USE = "SegmentLine"

Shape819.appearance = Appearance822

HAnimSegment818.children.append(Shape819)
Transform823 = x3d.Transform()
Transform823.translation = [0.20280000567436218,0.71390002965927124,-0.023600000888109207]
Shape824 = x3d.Shape()
Shape824.USE = "jointbox"

Transform823.children.append(Shape824)

HAnimSegment818.children.append(Transform823)
HAnimSite825 = x3d.HAnimSite()
HAnimSite825.DEF = "Joe_l_index_distal_tip"
HAnimSite825.name = "l_index_distal_tip"
HAnimSite825.translation = [0.20890000462532043,0.68580001592636108,-0.024499999359250069]
Shape826 = x3d.Shape()
Shape826.USE = "sitebox"

HAnimSite825.children.append(Shape826)

HAnimSegment818.children.append(HAnimSite825)
HAnimSite827 = x3d.HAnimSite()
HAnimSite827.DEF = "Joe_l_dactylion"
HAnimSite827.name = "l_dactylion"
HAnimSite827.translation = [0.20559999346733093,0.67430001497268677,-0.048200000077486038]
Shape828 = x3d.Shape()
Shape828.USE = "sitebox"

HAnimSite827.children.append(Shape828)

HAnimSegment818.children.append(HAnimSite827)

HAnimJoint817.children.append(HAnimSegment818)

HAnimJoint809.children.append(HAnimJoint817)

HAnimJoint801.children.append(HAnimJoint809)

HAnimJoint793.children.append(HAnimJoint801)

HAnimJoint753.children.append(HAnimJoint793)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.DEF = "Joe_l_middle0"
HAnimJoint829.center = [0.19869999587535858,0.80290001630783081,-0.05299999937415123]
HAnimJoint829.name = "l_middle0"
HAnimJoint829.skinCoordIndex = [131,132]
HAnimJoint829.skinCoordWeight = [1,1]
HAnimJoint829.stiffness = [0,0,0]
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.DEF = "Joe_l_middle_metacarpal"
HAnimSegment830.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment830.name = "l_middle_metacarpal"
Shape831 = x3d.Shape()
IndexedLineSet832 = x3d.IndexedLineSet()
IndexedLineSet832.coordIndex = [0,1,-1]
Coordinate833 = x3d.Coordinate()

IndexedLineSet832.coord = Coordinate833

Shape831.geometry = IndexedLineSet832
Appearance834 = x3d.Appearance()
Appearance834.USE = "SegmentLine"

Shape831.appearance = Appearance834

HAnimSegment830.children.append(Shape831)
Transform835 = x3d.Transform()
Transform835.translation = [0.19869999587535858,0.80290001630783081,-0.05299999937415123]
Shape836 = x3d.Shape()
Shape836.USE = "jointbox"

Transform835.children.append(Shape836)

HAnimSegment830.children.append(Transform835)

HAnimJoint829.children.append(HAnimSegment830)
HAnimJoint837 = x3d.HAnimJoint()
HAnimJoint837.DEF = "Joe_l_middle1"
HAnimJoint837.center = [0.19869999587535858,0.78179997205734253,-0.05299999937415123]
HAnimJoint837.name = "l_middle1"
HAnimJoint837.skinCoordIndex = [156,157,163,164]
HAnimJoint837.skinCoordWeight = [1,1,0.5,0.5]
HAnimJoint837.stiffness = [0,0,0]
HAnimSegment838 = x3d.HAnimSegment()
HAnimSegment838.DEF = "Joe_l_middle_proximal"
HAnimSegment838.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment838.name = "l_middle_proximal"
Shape839 = x3d.Shape()
IndexedLineSet840 = x3d.IndexedLineSet()
IndexedLineSet840.coordIndex = [0,1,-1]
Coordinate841 = x3d.Coordinate()

IndexedLineSet840.coord = Coordinate841

Shape839.geometry = IndexedLineSet840
Appearance842 = x3d.Appearance()
Appearance842.USE = "SegmentLine"

Shape839.appearance = Appearance842

HAnimSegment838.children.append(Shape839)
Transform843 = x3d.Transform()
Transform843.translation = [0.19869999587535858,0.78179997205734253,-0.05299999937415123]
Shape844 = x3d.Shape()
Shape844.USE = "jointbox"

Transform843.children.append(Shape844)

HAnimSegment838.children.append(Transform843)

HAnimJoint837.children.append(HAnimSegment838)
HAnimJoint845 = x3d.HAnimJoint()
HAnimJoint845.DEF = "Joe_l_middle2"
HAnimJoint845.center = [0.2012999951839447,0.72729998826980591,-0.050299998372793198]
HAnimJoint845.name = "l_middle2"
HAnimJoint845.skinCoordIndex = [179,180,181,182]
HAnimJoint845.skinCoordWeight = [1,1,1,1]
HAnimJoint845.stiffness = [0,0,0]
HAnimSegment846 = x3d.HAnimSegment()
HAnimSegment846.DEF = "Joe_l_middle_middle"
HAnimSegment846.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment846.name = "l_middle_middle"
Shape847 = x3d.Shape()
IndexedLineSet848 = x3d.IndexedLineSet()
IndexedLineSet848.coordIndex = [0,1,-1]
Coordinate849 = x3d.Coordinate()

IndexedLineSet848.coord = Coordinate849

Shape847.geometry = IndexedLineSet848
Appearance850 = x3d.Appearance()
Appearance850.USE = "SegmentLine"

Shape847.appearance = Appearance850

HAnimSegment846.children.append(Shape847)
Transform851 = x3d.Transform()
Transform851.translation = [0.2012999951839447,0.72729998826980591,-0.050299998372793198]
Shape852 = x3d.Shape()
Shape852.USE = "jointbox"

Transform851.children.append(Shape852)

HAnimSegment846.children.append(Transform851)

HAnimJoint845.children.append(HAnimSegment846)
HAnimJoint853 = x3d.HAnimJoint()
HAnimJoint853.DEF = "Joe_l_middle3"
HAnimJoint853.center = [0.20260000228881836,0.70109999179840088,-0.049400001764297485]
HAnimJoint853.name = "l_middle3"
HAnimJoint853.skinCoordIndex = [183,184,185,186,187,188,189,190,191]
HAnimJoint853.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint853.stiffness = [0,0,0]
HAnimSegment854 = x3d.HAnimSegment()
HAnimSegment854.DEF = "Joe_l_middle_distal"
HAnimSegment854.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment854.name = "l_middle_distal"
Shape855 = x3d.Shape()
IndexedLineSet856 = x3d.IndexedLineSet()
IndexedLineSet856.coordIndex = [0,1,-1]
Coordinate857 = x3d.Coordinate()

IndexedLineSet856.coord = Coordinate857

Shape855.geometry = IndexedLineSet856
Appearance858 = x3d.Appearance()
Appearance858.USE = "SegmentLine"

Shape855.appearance = Appearance858

HAnimSegment854.children.append(Shape855)
HAnimSite859 = x3d.HAnimSite()
HAnimSite859.DEF = "Joe_l_middle_distal_tip"
HAnimSite859.name = "l_middle_distal_tip"
HAnimSite859.translation = [0.20800000429153442,0.67309999465942383,-0.049100000411272049]
Shape860 = x3d.Shape()
Shape860.USE = "sitebox"

HAnimSite859.children.append(Shape860)

HAnimSegment854.children.append(HAnimSite859)
Transform861 = x3d.Transform()
Transform861.translation = [0.20260000228881836,0.70109999179840088,-0.049400001764297485]
Shape862 = x3d.Shape()
Shape862.USE = "jointbox"

Transform861.children.append(Shape862)

HAnimSegment854.children.append(Transform861)

HAnimJoint853.children.append(HAnimSegment854)

HAnimJoint845.children.append(HAnimJoint853)

HAnimJoint837.children.append(HAnimJoint845)

HAnimJoint829.children.append(HAnimJoint837)

HAnimJoint753.children.append(HAnimJoint829)
HAnimJoint863 = x3d.HAnimJoint()
HAnimJoint863.DEF = "Joe_l_ring0"
HAnimJoint863.center = [0.1956000030040741,0.80190002918243408,-0.079400002956390381]
HAnimJoint863.name = "l_ring0"
HAnimJoint863.skinCoordIndex = [133,134]
HAnimJoint863.skinCoordWeight = [1,1]
HAnimJoint863.stiffness = [0,0,0]
HAnimSegment864 = x3d.HAnimSegment()
HAnimSegment864.DEF = "Joe_l_ring_metacarpal"
HAnimSegment864.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment864.name = "l_ring_metacarpal"
Shape865 = x3d.Shape()
IndexedLineSet866 = x3d.IndexedLineSet()
IndexedLineSet866.coordIndex = [0,1,-1]
Coordinate867 = x3d.Coordinate()

IndexedLineSet866.coord = Coordinate867

Shape865.geometry = IndexedLineSet866
Appearance868 = x3d.Appearance()
Appearance868.USE = "SegmentLine"

Shape865.appearance = Appearance868

HAnimSegment864.children.append(Shape865)
Transform869 = x3d.Transform()
Transform869.translation = [0.1956000030040741,0.80190002918243408,-0.079400002956390381]
Shape870 = x3d.Shape()
Shape870.USE = "jointbox"

Transform869.children.append(Shape870)

HAnimSegment864.children.append(Transform869)

HAnimJoint863.children.append(HAnimSegment864)
HAnimJoint871 = x3d.HAnimJoint()
HAnimJoint871.DEF = "Joe_l_ring1"
HAnimJoint871.center = [0.1956000030040741,0.78149998188018799,-0.079400002956390381]
HAnimJoint871.name = "l_ring1"
HAnimJoint871.skinCoordIndex = [158,159,164,165]
HAnimJoint871.skinCoordWeight = [1,1,0.5,0.5]
HAnimJoint871.stiffness = [0,0,0]
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.DEF = "Joe_l_ring_proximal"
HAnimSegment872.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment872.name = "l_ring_proximal"
Shape873 = x3d.Shape()
IndexedLineSet874 = x3d.IndexedLineSet()
IndexedLineSet874.coordIndex = [0,1,-1]
Coordinate875 = x3d.Coordinate()

IndexedLineSet874.coord = Coordinate875

Shape873.geometry = IndexedLineSet874
Appearance876 = x3d.Appearance()
Appearance876.USE = "SegmentLine"

Shape873.appearance = Appearance876

HAnimSegment872.children.append(Shape873)
Transform877 = x3d.Transform()
Transform877.translation = [0.1956000030040741,0.78149998188018799,-0.079400002956390381]
Shape878 = x3d.Shape()
Shape878.USE = "jointbox"

Transform877.children.append(Shape878)

HAnimSegment872.children.append(Transform877)

HAnimJoint871.children.append(HAnimSegment872)
HAnimJoint879 = x3d.HAnimJoint()
HAnimJoint879.DEF = "Joe_l_ring2"
HAnimJoint879.center = [0.19730000197887421,0.72869998216629028,-0.077699996531009674]
HAnimJoint879.name = "l_ring2"
HAnimJoint879.skinCoordIndex = [192,193,194,195]
HAnimJoint879.skinCoordWeight = [1,1,1,1]
HAnimJoint879.stiffness = [0,0,0]
HAnimSegment880 = x3d.HAnimSegment()
HAnimSegment880.DEF = "Joe_l_ring_middle"
HAnimSegment880.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment880.name = "l_ring_middle"
Shape881 = x3d.Shape()
IndexedLineSet882 = x3d.IndexedLineSet()
IndexedLineSet882.coordIndex = [0,1,-1]
Coordinate883 = x3d.Coordinate()

IndexedLineSet882.coord = Coordinate883

Shape881.geometry = IndexedLineSet882
Appearance884 = x3d.Appearance()
Appearance884.USE = "SegmentLine"

Shape881.appearance = Appearance884

HAnimSegment880.children.append(Shape881)
Transform885 = x3d.Transform()
Transform885.translation = [0.19730000197887421,0.72869998216629028,-0.077699996531009674]
Shape886 = x3d.Shape()
Shape886.USE = "jointbox"

Transform885.children.append(Shape886)

HAnimSegment880.children.append(Transform885)

HAnimJoint879.children.append(HAnimSegment880)
HAnimJoint887 = x3d.HAnimJoint()
HAnimJoint887.DEF = "Joe_l_ring3"
HAnimJoint887.center = [0.19830000400543213,0.70450001955032349,-0.076700001955032349]
HAnimJoint887.name = "l_ring3"
HAnimJoint887.skinCoordIndex = [196,197,198,199,200,201,202,203,204]
HAnimJoint887.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint887.stiffness = [0,0,0]
HAnimSegment888 = x3d.HAnimSegment()
HAnimSegment888.DEF = "Joe_l_ring_distal"
HAnimSegment888.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment888.name = "l_ring_distal"
Shape889 = x3d.Shape()
IndexedLineSet890 = x3d.IndexedLineSet()
IndexedLineSet890.coordIndex = [0,1,-1]
Coordinate891 = x3d.Coordinate()

IndexedLineSet890.coord = Coordinate891

Shape889.geometry = IndexedLineSet890
Appearance892 = x3d.Appearance()
Appearance892.USE = "SegmentLine"

Shape889.appearance = Appearance892

HAnimSegment888.children.append(Shape889)
Transform893 = x3d.Transform()
Transform893.translation = [0.19830000400543213,0.70450001955032349,-0.076700001955032349]
Shape894 = x3d.Shape()
Shape894.USE = "jointbox"

Transform893.children.append(Shape894)

HAnimSegment888.children.append(Transform893)
HAnimSite895 = x3d.HAnimSite()
HAnimSite895.DEF = "Joe_l_ring_distal_tip"
HAnimSite895.name = "l_ring_distal_tip"
HAnimSite895.translation = [0.20350000262260437,0.67500001192092896,-0.075599998235702515]
Shape896 = x3d.Shape()
Shape896.USE = "sitebox"

HAnimSite895.children.append(Shape896)

HAnimSegment888.children.append(HAnimSite895)

HAnimJoint887.children.append(HAnimSegment888)

HAnimJoint879.children.append(HAnimJoint887)

HAnimJoint871.children.append(HAnimJoint879)

HAnimJoint863.children.append(HAnimJoint871)

HAnimJoint753.children.append(HAnimJoint863)
HAnimJoint897 = x3d.HAnimJoint()
HAnimJoint897.DEF = "Joe_l_pinky0"
HAnimJoint897.center = [0.1925,0.8066,-0.1036]
HAnimJoint897.name = "l_pinky0"
HAnimJoint897.skinCoordIndex = [135,136,137,165]
HAnimJoint897.skinCoordWeight = [1,1,1,0.5]
HAnimSegment898 = x3d.HAnimSegment()
HAnimSegment898.DEF = "Joe_l_pinky_metacarpal"
HAnimSegment898.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment898.name = "l_pinky_metacarpal"
Shape899 = x3d.Shape()
IndexedLineSet900 = x3d.IndexedLineSet()
IndexedLineSet900.coordIndex = [0,1,-1]
Coordinate901 = x3d.Coordinate()

IndexedLineSet900.coord = Coordinate901

Shape899.geometry = IndexedLineSet900
Appearance902 = x3d.Appearance()
Appearance902.USE = "SegmentLine"

Shape899.appearance = Appearance902

HAnimSegment898.children.append(Shape899)
Transform903 = x3d.Transform()
Transform903.translation = [0.19249999523162842,0.80659997463226318,-0.10360000282526016]
Shape904 = x3d.Shape()
Shape904.USE = "jointbox"

Transform903.children.append(Shape904)

HAnimSegment898.children.append(Transform903)

HAnimJoint897.children.append(HAnimSegment898)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.DEF = "Joe_l_pinky1"
HAnimJoint905.center = [0.19249999523162842,0.78659999370574951,-0.10360000282526016]
HAnimJoint905.name = "l_pinky1"
HAnimJoint905.skinCoordIndex = [160,161,162]
HAnimJoint905.skinCoordWeight = [1,1,1]
HAnimJoint905.stiffness = [0,0,0]
HAnimSegment906 = x3d.HAnimSegment()
HAnimSegment906.DEF = "Joe_l_pinky_proximal"
HAnimSegment906.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment906.name = "l_pinky_proximal"
Shape907 = x3d.Shape()
IndexedLineSet908 = x3d.IndexedLineSet()
IndexedLineSet908.coordIndex = [0,1,-1]
Coordinate909 = x3d.Coordinate()

IndexedLineSet908.coord = Coordinate909

Shape907.geometry = IndexedLineSet908
Appearance910 = x3d.Appearance()
Appearance910.USE = "SegmentLine"

Shape907.appearance = Appearance910

HAnimSegment906.children.append(Shape907)
Transform911 = x3d.Transform()
Transform911.translation = [0.19249999523162842,0.78659999370574951,-0.10360000282526016]
Shape912 = x3d.Shape()
Shape912.USE = "jointbox"

Transform911.children.append(Shape912)

HAnimSegment906.children.append(Transform911)

HAnimJoint905.children.append(HAnimSegment906)
HAnimJoint913 = x3d.HAnimJoint()
HAnimJoint913.DEF = "Joe_l_pinky2"
HAnimJoint913.center = [0.19380000233650208,0.74519997835159302,-0.10239999741315842]
HAnimJoint913.name = "l_pinky2"
HAnimJoint913.skinCoordIndex = [205,206,207,208]
HAnimJoint913.skinCoordWeight = [1,1,1,1]
HAnimJoint913.stiffness = [0,0,0]
HAnimSegment914 = x3d.HAnimSegment()
HAnimSegment914.DEF = "Joe_l_pinky_middle"
HAnimSegment914.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment914.name = "l_pinky_middle"
Transform915 = x3d.Transform()
Transform915.translation = [0.1938,0.7452,-0.1024]
Shape916 = x3d.Shape()
Shape916.USE = "jointbox"

Transform915.children.append(Shape916)

HAnimSegment914.children.append(Transform915)
Shape917 = x3d.Shape()
IndexedLineSet918 = x3d.IndexedLineSet()
IndexedLineSet918.coordIndex = [0,1,-1]
Coordinate919 = x3d.Coordinate()

IndexedLineSet918.coord = Coordinate919

Shape917.geometry = IndexedLineSet918
Appearance920 = x3d.Appearance()
Appearance920.USE = "SegmentLine"

Shape917.appearance = Appearance920

HAnimSegment914.children.append(Shape917)

HAnimJoint913.children.append(HAnimSegment914)
HAnimJoint921 = x3d.HAnimJoint()
HAnimJoint921.DEF = "Joe_l_pinky3"
HAnimJoint921.center = [0.19480000436306,0.72769999504089355,-0.10170000046491623]
HAnimJoint921.name = "l_pinky3"
HAnimJoint921.skinCoordIndex = [209,210,211,212,213,214,215,216,217]
HAnimJoint921.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint921.stiffness = [0,0,0]
HAnimSegment922 = x3d.HAnimSegment()
HAnimSegment922.DEF = "Joe_l_pinky_distal"
HAnimSegment922.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment922.name = "l_pinky_distal"
Shape923 = x3d.Shape()
IndexedLineSet924 = x3d.IndexedLineSet()
IndexedLineSet924.coordIndex = [0,1,-1]
Coordinate925 = x3d.Coordinate()

IndexedLineSet924.coord = Coordinate925

Shape923.geometry = IndexedLineSet924
Appearance926 = x3d.Appearance()
Appearance926.USE = "SegmentLine"

Shape923.appearance = Appearance926

HAnimSegment922.children.append(Shape923)
Transform927 = x3d.Transform()
Transform927.translation = [0.1948,0.7277,-0.1017]
Shape928 = x3d.Shape()
Shape928.USE = "jointbox"

Transform927.children.append(Shape928)

HAnimSegment922.children.append(Transform927)
HAnimSite929 = x3d.HAnimSite()
HAnimSite929.DEF = "Joe_l_pinky_distal_tip"
HAnimSite929.name = "l_pinky_distal_tip"
HAnimSite929.translation = [0.20139999687671661,0.70090001821517944,-0.10119999945163727]
Shape930 = x3d.Shape()
Shape930.USE = "sitebox"

HAnimSite929.children.append(Shape930)

HAnimSegment922.children.append(HAnimSite929)

HAnimJoint921.children.append(HAnimSegment922)

HAnimJoint913.children.append(HAnimJoint921)

HAnimJoint905.children.append(HAnimJoint913)

HAnimJoint897.children.append(HAnimJoint905)

HAnimJoint753.children.append(HAnimJoint897)

HAnimJoint731.children.append(HAnimJoint753)

HAnimJoint707.children.append(HAnimJoint731)

HAnimJoint691.children.append(HAnimJoint707)

HAnimJoint681.children.append(HAnimJoint691)

HAnimJoint565.children.append(HAnimJoint681)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.DEF = "Joe_r_sternoclavicular"
HAnimJoint931.center = [-0.029999999329447746,1.4600000381469727,0]
HAnimJoint931.name = "r_sternoclavicular"
HAnimJoint931.skinCoordIndex = [10]
HAnimJoint931.skinCoordWeight = [1]
HAnimJoint931.stiffness = [0,0,0]
HAnimSegment932 = x3d.HAnimSegment()
HAnimSegment932.DEF = "Joe_r_clavicle"
HAnimSegment932.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment932.name = "r_clavicle"
Shape933 = x3d.Shape()
IndexedLineSet934 = x3d.IndexedLineSet()
IndexedLineSet934.coordIndex = [0,1,-1]
Coordinate935 = x3d.Coordinate()

IndexedLineSet934.coord = Coordinate935

Shape933.geometry = IndexedLineSet934
Appearance936 = x3d.Appearance()
Appearance936.USE = "SegmentLine"

Shape933.appearance = Appearance936

HAnimSegment932.children.append(Shape933)
Transform937 = x3d.Transform()
Transform937.translation = [-0.029999999329447746,1.4600000381469727,0.019999999552965164]
Shape938 = x3d.Shape()
Shape938.USE = "jointbox"

Transform937.children.append(Shape938)

HAnimSegment932.children.append(Transform937)
HAnimSite939 = x3d.HAnimSite()
HAnimSite939.DEF = "Joe_r_clavicale"
HAnimSite939.name = "r_clavicale"
HAnimSite939.translation = [-0.029999999329447746,1.4600000381469727,0.035000000149011612]
Shape940 = x3d.Shape()
Shape940.USE = "sitebox"

HAnimSite939.children.append(Shape940)

HAnimSegment932.children.append(HAnimSite939)

HAnimJoint931.children.append(HAnimSegment932)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.DEF = "Joe_r_acromioclavicular"
HAnimJoint941.center = [-0.090000003576278687,1.4099999666213989,-0.10999999940395355]
HAnimJoint941.name = "r_acromioclavicular"
HAnimJoint941.skinCoordIndex = [77,29]
HAnimJoint941.skinCoordWeight = [1,0.89999997615814209]
HAnimJoint941.stiffness = [0,0,0]
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.DEF = "Joe_r_scapula"
HAnimSegment942.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment942.name = "r_scapula"
Shape943 = x3d.Shape()
IndexedLineSet944 = x3d.IndexedLineSet()
IndexedLineSet944.coordIndex = [0,1,-1]
Coordinate945 = x3d.Coordinate()

IndexedLineSet944.coord = Coordinate945

Shape943.geometry = IndexedLineSet944
Appearance946 = x3d.Appearance()
Appearance946.USE = "SegmentLine"

Shape943.appearance = Appearance946

HAnimSegment942.children.append(Shape943)
Transform947 = x3d.Transform()
Transform947.translation = [-0.090000003576278687,1.4099999666213989,-0.090000003576278687]
Shape948 = x3d.Shape()
Shape948.USE = "jointbox"

Transform947.children.append(Shape948)

HAnimSegment942.children.append(Transform947)
Transform949 = x3d.Transform()
Transform949.translation = [-0.10999999940395355,1.4270000457763672,-0.13750000298023224]
Shape950 = x3d.Shape()
Shape950.USE = "skinsphere"

Transform949.children.append(Shape950)

HAnimSegment942.children.append(Transform949)
HAnimSite951 = x3d.HAnimSite()
HAnimSite951.DEF = "Joe_r_acromion"
HAnimSite951.name = "r_acromion"
HAnimSite951.translation = [-0.17800000309944153,1.4824999570846558,-0.0625]
Shape952 = x3d.Shape()
Shape952.USE = "sitebox"

HAnimSite951.children.append(Shape952)

HAnimSegment942.children.append(HAnimSite951)
HAnimSite953 = x3d.HAnimSite()
HAnimSite953.DEF = "Joe_r_axilla_ant"
HAnimSite953.name = "r_axilla_ant"
HAnimSite953.translation = [-0.17000000178813934,1.3799999952316284,0.0070000002160668373]
Shape954 = x3d.Shape()
Shape954.USE = "sitebox"

HAnimSite953.children.append(Shape954)

HAnimSegment942.children.append(HAnimSite953)
HAnimSite955 = x3d.HAnimSite()
HAnimSite955.DEF = "Joe_r_axilla_post"
HAnimSite955.name = "r_axilla_post"
HAnimSite955.translation = [-0.15999999642372131,1.3799999952316284,-0.12700000405311584]
Shape956 = x3d.Shape()
Shape956.USE = "sitebox"

HAnimSite955.children.append(Shape956)

HAnimSegment942.children.append(HAnimSite955)

HAnimJoint941.children.append(HAnimSegment942)
HAnimJoint957 = x3d.HAnimJoint()
HAnimJoint957.DEF = "Joe_r_shoulder"
HAnimJoint957.center = [-0.20000000298023224,1.440000057220459,-0.039999999105930328]
HAnimJoint957.name = "r_shoulder"
HAnimJoint957.skinCoordIndex = [29,30,32,78,218,219,220,221,86,88]
HAnimJoint957.skinCoordWeight = [0.10000000149011612,1,1,1,1,1,1,1,0.30000001192092896,0.20000000298023224]
HAnimJoint957.stiffness = [0,0,0]
HAnimSegment958 = x3d.HAnimSegment()
HAnimSegment958.DEF = "Joe_r_upperarm"
HAnimSegment958.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment958.name = "r_upperarm"
Transform959 = x3d.Transform()
Transform959.translation = [-0.20000000298023224,1.440000057220459,-0.039999999105930328]
Shape960 = x3d.Shape()
Shape960.USE = "jointbox"

Transform959.children.append(Shape960)

HAnimSegment958.children.append(Transform959)
Shape961 = x3d.Shape()
IndexedLineSet962 = x3d.IndexedLineSet()
IndexedLineSet962.coordIndex = [0,1,-1]
Coordinate963 = x3d.Coordinate()

IndexedLineSet962.coord = Coordinate963

Shape961.geometry = IndexedLineSet962
Appearance964 = x3d.Appearance()
Appearance964.USE = "SegmentLine"

Shape961.appearance = Appearance964

HAnimSegment958.children.append(Shape961)
Transform965 = x3d.Transform()
Transform965.translation = [-0.17800000309944153,1.4824999570846558,-0.0625]
Shape966 = x3d.Shape()
Shape966.USE = "skinsphere"

Transform965.children.append(Shape966)

HAnimSegment958.children.append(Transform965)
Transform967 = x3d.Transform()
Transform967.translation = [-0.17000000178813934,1.3799999952316284,0.0070000002160668373]
Shape968 = x3d.Shape()
Shape968.USE = "skinsphere"

Transform967.children.append(Shape968)

HAnimSegment958.children.append(Transform967)
Transform969 = x3d.Transform()
Transform969.translation = [-0.15999999642372131,1.3799999952316284,-0.12700000405311584]
Shape970 = x3d.Shape()
Shape970.USE = "skinsphere"

Transform969.children.append(Shape970)

HAnimSegment958.children.append(Transform969)
Transform971 = x3d.Transform()
Transform971.translation = [-0.23499999940395355,1.4199999570846558,-0.0625]
Shape972 = x3d.Shape()
Shape972.USE = "skinsphere"

Transform971.children.append(Shape972)

HAnimSegment958.children.append(Transform971)
Transform973 = x3d.Transform()
Transform973.translation = [-0.23000000417232513,1.2350000143051147,-0.039999999105930328]
Shape974 = x3d.Shape()
Shape974.USE = "skinsphere"

Transform973.children.append(Shape974)

HAnimSegment958.children.append(Transform973)
Transform975 = x3d.Transform()
Transform975.translation = [-0.15999999642372131,1.2300000190734863,-0.039999999105930328]
Shape976 = x3d.Shape()
Shape976.USE = "skinsphere"

Transform975.children.append(Shape976)

HAnimSegment958.children.append(Transform975)
Transform977 = x3d.Transform()
Transform977.translation = [-0.20000000298023224,1.2300000190734863,-0.10499999672174454]
Shape978 = x3d.Shape()
Shape978.USE = "skinsphere"

Transform977.children.append(Shape978)

HAnimSegment958.children.append(Transform977)
Transform979 = x3d.Transform()
Transform979.translation = [-0.20000000298023224,1.2350000143051147,0.019999999552965164]
Shape980 = x3d.Shape()
Shape980.USE = "skinsphere"

Transform979.children.append(Shape980)

HAnimSegment958.children.append(Transform979)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.DEF = "Joe_r_humeral_medial_epicn"
HAnimSite981.name = "r_humeral_medial_epicn"
HAnimSite981.translation = [-0.16500000655651093,1.1388000249862671,-0.039999999105930328]
Shape982 = x3d.Shape()
Shape982.USE = "sitebox"

HAnimSite981.children.append(Shape982)

HAnimSegment958.children.append(HAnimSite981)
HAnimSite983 = x3d.HAnimSite()
HAnimSite983.DEF = "Joe_r_radiale"
HAnimSite983.name = "r_radiale"
HAnimSite983.translation = [-0.23000000417232513,1.1330000162124634,-0.054999999701976776]
Shape984 = x3d.Shape()
Shape984.USE = "sitebox"

HAnimSite983.children.append(Shape984)

HAnimSegment958.children.append(HAnimSite983)
HAnimSite985 = x3d.HAnimSite()
HAnimSite985.DEF = "Joe_r_humeral_lateral_epicn"
HAnimSite985.name = "r_humeral_lateral_epicn"
HAnimSite985.translation = [-0.24400000274181366,1.1388000249862671,-0.039999999105930328]
Shape986 = x3d.Shape()
Shape986.USE = "sitebox"

HAnimSite985.children.append(Shape986)

HAnimSegment958.children.append(HAnimSite985)

HAnimJoint957.children.append(HAnimSegment958)
HAnimJoint987 = x3d.HAnimJoint()
HAnimJoint987.DEF = "Joe_r_elbow"
HAnimJoint987.center = [-0.20000000298023224,1.1388000249862671,-0.039999999105930328]
HAnimJoint987.name = "r_elbow"
HAnimJoint987.skinCoordIndex = [33,34,35,225,226,227,228,229,231,232,233,234]
HAnimJoint987.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint987.stiffness = [0,0,0]
HAnimSegment988 = x3d.HAnimSegment()
HAnimSegment988.DEF = "Joe_r_forearm"
HAnimSegment988.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment988.name = "r_forearm"
Shape989 = x3d.Shape()
IndexedLineSet990 = x3d.IndexedLineSet()
IndexedLineSet990.coordIndex = [0,1,-1]
Coordinate991 = x3d.Coordinate()

IndexedLineSet990.coord = Coordinate991

Shape989.geometry = IndexedLineSet990
Appearance992 = x3d.Appearance()
Appearance992.USE = "SegmentLine"

Shape989.appearance = Appearance992

HAnimSegment988.children.append(Shape989)
Transform993 = x3d.Transform()
Transform993.translation = [-0.20000000298023224,1.1388000249862671,-0.039999999105930328]
Shape994 = x3d.Shape()
Shape994.USE = "jointbox"

Transform993.children.append(Shape994)

HAnimSegment988.children.append(Transform993)
Transform995 = x3d.Transform()
Transform995.translation = [-0.20000000298023224,1.1388000249862671,0.013000000268220901]
Shape996 = x3d.Shape()
Shape996.USE = "skinsphere"

Transform995.children.append(Shape996)

HAnimSegment988.children.append(Transform995)
Transform997 = x3d.Transform()
Transform997.translation = [-0.22499999403953552,1,-0.0099999997764825821]
Shape998 = x3d.Shape()
Shape998.USE = "skinsphere"

Transform997.children.append(Shape998)

HAnimSegment988.children.append(Transform997)
Transform999 = x3d.Transform()
Transform999.translation = [-0.22499999403953552,1,-0.070000000298023224]
Shape1000 = x3d.Shape()
Shape1000.USE = "skinsphere"

Transform999.children.append(Shape1000)

HAnimSegment988.children.append(Transform999)
Transform1001 = x3d.Transform()
Transform1001.translation = [-0.18500000238418579,1,-0.0099999997764825821]
Shape1002 = x3d.Shape()
Shape1002.USE = "skinsphere"

Transform1001.children.append(Shape1002)

HAnimSegment988.children.append(Transform1001)
Transform1003 = x3d.Transform()
Transform1003.translation = [-0.18500000238418579,1,-0.070000000298023224]
Shape1004 = x3d.Shape()
Shape1004.USE = "skinsphere"

Transform1003.children.append(Shape1004)

HAnimSegment988.children.append(Transform1003)
HAnimSite1005 = x3d.HAnimSite()
HAnimSite1005.DEF = "Joe_r_radial_styloid"
HAnimSite1005.name = "r_radial_styloid"
HAnimSite1005.translation = [-0.20000000298023224,0.89999997615814209,-0.014999999664723873]
Shape1006 = x3d.Shape()
Shape1006.USE = "sitebox"

HAnimSite1005.children.append(Shape1006)

HAnimSegment988.children.append(HAnimSite1005)
HAnimSite1007 = x3d.HAnimSite()
HAnimSite1007.DEF = "Joe_r_olecranon"
HAnimSite1007.name = "r_olecranon"
HAnimSite1007.translation = [-0.20000000298023224,1.1388000249862671,-0.079999998211860657]
Shape1008 = x3d.Shape()
Shape1008.USE = "sitebox"

HAnimSite1007.children.append(Shape1008)

HAnimSegment988.children.append(HAnimSite1007)

HAnimJoint987.children.append(HAnimSegment988)
HAnimJoint1009 = x3d.HAnimJoint()
HAnimJoint1009.DEF = "Joe_r_wrist"
HAnimJoint1009.center = [-0.20000000298023224,0.88999998569488525,-0.039999999105930328]
HAnimJoint1009.name = "r_wrist"
HAnimJoint1009.skinCoordIndex = [235,236,237,238,239,240,241,242]
HAnimJoint1009.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint1009.stiffness = [0,0,0]
HAnimSegment1010 = x3d.HAnimSegment()
HAnimSegment1010.DEF = "Joe_r_hand"
HAnimSegment1010.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1010.name = "r_hand"
Shape1011 = x3d.Shape()
IndexedLineSet1012 = x3d.IndexedLineSet()
IndexedLineSet1012.coordIndex = [0,1,-1,0,2,-1,0,3,-1,0,4,-1,0,5,-1]
Coordinate1013 = x3d.Coordinate()

IndexedLineSet1012.coord = Coordinate1013

Shape1011.geometry = IndexedLineSet1012
Appearance1014 = x3d.Appearance()
Appearance1014.USE = "SegmentLine"

Shape1011.appearance = Appearance1014

HAnimSegment1010.children.append(Shape1011)
Transform1015 = x3d.Transform()
Transform1015.translation = [-0.20000000298023224,0.88999998569488525,-0.039999999105930328]
Shape1016 = x3d.Shape()
Shape1016.USE = "jointbox"

Transform1015.children.append(Shape1016)

HAnimSegment1010.children.append(Transform1015)
HAnimSite1017 = x3d.HAnimSite()
HAnimSite1017.DEF = "Joe_r_ulnar_styloid"
HAnimSite1017.name = "r_ulnar_styloid"
HAnimSite1017.translation = [-0.20000000298023224,0.89999997615814209,-0.085000000894069672]
Shape1018 = x3d.Shape()
Shape1018.USE = "sitebox"

HAnimSite1017.children.append(Shape1018)

HAnimSegment1010.children.append(HAnimSite1017)

HAnimJoint1009.children.append(HAnimSegment1010)
HAnimJoint1019 = x3d.HAnimJoint()
HAnimJoint1019.DEF = "Joe_r_thumb1"
HAnimJoint1019.center = [-0.20000000298023224,0.85000002384185791,0]
HAnimJoint1019.name = "r_thumb1"
HAnimJoint1019.skinCoordIndex = [243,244]
HAnimJoint1019.skinCoordWeight = [1,1]
HAnimJoint1019.stiffness = [0,0,0]
HAnimSegment1020 = x3d.HAnimSegment()
HAnimSegment1020.DEF = "Joe_r_thumb_metacarpal"
HAnimSegment1020.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1020.name = "r_thumb_metacarpal"
Shape1021 = x3d.Shape()
IndexedLineSet1022 = x3d.IndexedLineSet()
IndexedLineSet1022.coordIndex = [0,1,-1]
Coordinate1023 = x3d.Coordinate()

IndexedLineSet1022.coord = Coordinate1023

Shape1021.geometry = IndexedLineSet1022
Appearance1024 = x3d.Appearance()
Appearance1024.USE = "SegmentLine"

Shape1021.appearance = Appearance1024

HAnimSegment1020.children.append(Shape1021)
Transform1025 = x3d.Transform()
Transform1025.translation = [-0.20000000298023224,0.85000002384185791,0]
Shape1026 = x3d.Shape()
Shape1026.USE = "jointbox"

Transform1025.children.append(Shape1026)

HAnimSegment1020.children.append(Transform1025)

HAnimJoint1019.children.append(HAnimSegment1020)
HAnimJoint1027 = x3d.HAnimJoint()
HAnimJoint1027.DEF = "Joe_r_thumb2"
HAnimJoint1027.center = [-0.20000000298023224,0.81999999284744263,0.029999999329447746]
HAnimJoint1027.name = "r_thumb2"
HAnimJoint1027.skinCoordIndex = [254,255,256,257,258,259]
HAnimJoint1027.skinCoordWeight = [0.5,0.5,0.5,1,1,1]
HAnimJoint1027.stiffness = [0,0,0]
HAnimSegment1028 = x3d.HAnimSegment()
HAnimSegment1028.DEF = "Joe_r_thumb_proximal"
HAnimSegment1028.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1028.name = "r_thumb_proximal"
Shape1029 = x3d.Shape()
IndexedLineSet1030 = x3d.IndexedLineSet()
IndexedLineSet1030.coordIndex = [0,1,-1]
Coordinate1031 = x3d.Coordinate()

IndexedLineSet1030.coord = Coordinate1031

Shape1029.geometry = IndexedLineSet1030
Appearance1032 = x3d.Appearance()
Appearance1032.USE = "SegmentLine"

Shape1029.appearance = Appearance1032

HAnimSegment1028.children.append(Shape1029)
Transform1033 = x3d.Transform()
Transform1033.translation = [-0.20000000298023224,0.81999999284744263,0.029999999329447746]
Shape1034 = x3d.Shape()
Shape1034.USE = "jointbox"

Transform1033.children.append(Shape1034)

HAnimSegment1028.children.append(Transform1033)

HAnimJoint1027.children.append(HAnimSegment1028)
HAnimJoint1035 = x3d.HAnimJoint()
HAnimJoint1035.DEF = "Joe_r_thumb3"
HAnimJoint1035.center = [-0.20000000298023224,0.80000001192092896,0.05000000074505806]
HAnimJoint1035.name = "r_thumb3"
HAnimJoint1035.skinCoordIndex = [260,261,262,263,264,265,266,267,268]
HAnimJoint1035.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint1035.stiffness = [0,0,0]
HAnimSegment1036 = x3d.HAnimSegment()
HAnimSegment1036.DEF = "Joe_r_thumb_distal"
HAnimSegment1036.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1036.name = "r_thumb_distal"
Shape1037 = x3d.Shape()
IndexedLineSet1038 = x3d.IndexedLineSet()
IndexedLineSet1038.coordIndex = [0,1,-1]
Coordinate1039 = x3d.Coordinate()

IndexedLineSet1038.coord = Coordinate1039

Shape1037.geometry = IndexedLineSet1038
Appearance1040 = x3d.Appearance()
Appearance1040.USE = "SegmentLine"

Shape1037.appearance = Appearance1040

HAnimSegment1036.children.append(Shape1037)
Transform1041 = x3d.Transform()
Transform1041.DEF = "Thumbnail"
Transform1041.translation = [-0.20000000298023224,0.7850000262260437,0.075000002980232239]
Shape1042 = x3d.Shape()
Shape1042.USE = "skinsphere"

Transform1041.children.append(Shape1042)

HAnimSegment1036.children.append(Transform1041)
Transform1043 = x3d.Transform()
Transform1043.translation = [-0.20000000298023224,0.80000001192092896,0.05000000074505806]
Shape1044 = x3d.Shape()
Shape1044.USE = "jointbox"

Transform1043.children.append(Shape1044)

HAnimSegment1036.children.append(Transform1043)
HAnimSite1045 = x3d.HAnimSite()
HAnimSite1045.DEF = "Joe_r_thumb_distal_tip"
HAnimSite1045.name = "r_thumb_distal_tip"
HAnimSite1045.translation = [-0.20000000298023224,0.77999997138977051,0.070000000298023224]
Shape1046 = x3d.Shape()
Shape1046.USE = "sitebox"

HAnimSite1045.children.append(Shape1046)

HAnimSegment1036.children.append(HAnimSite1045)

HAnimJoint1035.children.append(HAnimSegment1036)

HAnimJoint1027.children.append(HAnimJoint1035)

HAnimJoint1019.children.append(HAnimJoint1027)

HAnimJoint1009.children.append(HAnimJoint1019)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.DEF = "Joe_r_index0"
HAnimJoint1047.center = [-0.20000000298023224,0.8399999737739563,-0.014999999664723873]
HAnimJoint1047.name = "r_index0"
HAnimJoint1047.skinCoordIndex = [245,246]
HAnimJoint1047.skinCoordWeight = [1,1]
HAnimJoint1047.stiffness = [0,0,0]
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.DEF = "Joe_r_index_metacarpal"
HAnimSegment1048.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1048.name = "r_index_metacarpal"
Shape1049 = x3d.Shape()
IndexedLineSet1050 = x3d.IndexedLineSet()
IndexedLineSet1050.coordIndex = [0,1,-1]
Coordinate1051 = x3d.Coordinate()

IndexedLineSet1050.coord = Coordinate1051

Shape1049.geometry = IndexedLineSet1050
Appearance1052 = x3d.Appearance()
Appearance1052.USE = "SegmentLine"

Shape1049.appearance = Appearance1052

HAnimSegment1048.children.append(Shape1049)
Transform1053 = x3d.Transform()
Transform1053.translation = [-0.20000000298023224,0.8399999737739563,-0.014999999664723873]
Shape1054 = x3d.Shape()
Shape1054.USE = "jointbox"

Transform1053.children.append(Shape1054)

HAnimSegment1048.children.append(Transform1053)
HAnimSite1055 = x3d.HAnimSite()
HAnimSite1055.DEF = "Joe_r_metacarpal_pha2"
HAnimSite1055.name = "r_metacarpal_pha2"
HAnimSite1055.translation = [-0.20000000298023224,0.7929999828338623,-0.004999999888241291]
Shape1056 = x3d.Shape()
Shape1056.USE = "sitebox"

HAnimSite1055.children.append(Shape1056)

HAnimSegment1048.children.append(HAnimSite1055)

HAnimJoint1047.children.append(HAnimSegment1048)
HAnimJoint1057 = x3d.HAnimJoint()
HAnimJoint1057.DEF = "Joe_r_index1"
HAnimJoint1057.center = [-0.20000000298023224,0.7929999828338623,-0.014999999664723873]
HAnimJoint1057.name = "r_index1"
HAnimJoint1057.skinCoordIndex = [254,255,256,269,270,271,279]
HAnimJoint1057.skinCoordWeight = [0.5,0.5,0.5,1,1,1,0.5]
HAnimJoint1057.stiffness = [0,0,0]
HAnimSegment1058 = x3d.HAnimSegment()
HAnimSegment1058.DEF = "Joe_r_index_proximal"
HAnimSegment1058.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1058.name = "r_index_proximal"
Shape1059 = x3d.Shape()
IndexedLineSet1060 = x3d.IndexedLineSet()
IndexedLineSet1060.coordIndex = [0,1,-1]
Coordinate1061 = x3d.Coordinate()

IndexedLineSet1060.coord = Coordinate1061

Shape1059.geometry = IndexedLineSet1060
Appearance1062 = x3d.Appearance()
Appearance1062.USE = "SegmentLine"

Shape1059.appearance = Appearance1062

HAnimSegment1058.children.append(Shape1059)
Transform1063 = x3d.Transform()
Transform1063.translation = [-0.20000000298023224,0.7929999828338623,-0.014999999664723873]
Shape1064 = x3d.Shape()
Shape1064.USE = "jointbox"

Transform1063.children.append(Shape1064)

HAnimSegment1058.children.append(Transform1063)

HAnimJoint1057.children.append(HAnimSegment1058)
HAnimJoint1065 = x3d.HAnimJoint()
HAnimJoint1065.DEF = "Joe_r_index2"
HAnimJoint1065.center = [-0.20000000298023224,0.74500000476837158,-0.014999999664723873]
HAnimJoint1065.name = "r_index2"
HAnimJoint1065.skinCoordIndex = [282,283,284,285]
HAnimJoint1065.skinCoordWeight = [1,1,1,1]
HAnimJoint1065.stiffness = [0,0,0]
HAnimSegment1066 = x3d.HAnimSegment()
HAnimSegment1066.DEF = "Joe_r_index_middle"
HAnimSegment1066.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1066.name = "r_index_middle"
Shape1067 = x3d.Shape()
IndexedLineSet1068 = x3d.IndexedLineSet()
IndexedLineSet1068.coordIndex = [0,1,-1]
Coordinate1069 = x3d.Coordinate()

IndexedLineSet1068.coord = Coordinate1069

Shape1067.geometry = IndexedLineSet1068
Appearance1070 = x3d.Appearance()
Appearance1070.USE = "SegmentLine"

Shape1067.appearance = Appearance1070

HAnimSegment1066.children.append(Shape1067)
Transform1071 = x3d.Transform()
Transform1071.translation = [-0.20000000298023224,0.74500000476837158,-0.014999999664723873]
Shape1072 = x3d.Shape()
Shape1072.USE = "jointbox"

Transform1071.children.append(Shape1072)

HAnimSegment1066.children.append(Transform1071)

HAnimJoint1065.children.append(HAnimSegment1066)
HAnimJoint1073 = x3d.HAnimJoint()
HAnimJoint1073.DEF = "Joe_r_index3"
HAnimJoint1073.center = [-0.20000000298023224,0.72000002861022949,-0.014999999664723873]
HAnimJoint1073.name = "r_index3"
HAnimJoint1073.skinCoordIndex = [286,287,288,289,290,291,292,293,294]
HAnimJoint1073.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint1073.stiffness = [0,0,0]
HAnimSegment1074 = x3d.HAnimSegment()
HAnimSegment1074.DEF = "Joe_r_index_distal"
HAnimSegment1074.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1074.name = "r_index_distal"
Shape1075 = x3d.Shape()
IndexedLineSet1076 = x3d.IndexedLineSet()
IndexedLineSet1076.coordIndex = [0,1,-1]
Coordinate1077 = x3d.Coordinate()

IndexedLineSet1076.coord = Coordinate1077

Shape1075.geometry = IndexedLineSet1076
Appearance1078 = x3d.Appearance()
Appearance1078.USE = "SegmentLine"

Shape1075.appearance = Appearance1078

HAnimSegment1074.children.append(Shape1075)
Transform1079 = x3d.Transform()
Transform1079.translation = [-0.20000000298023224,0.72000002861022949,-0.014999999664723873]
Shape1080 = x3d.Shape()
Shape1080.USE = "jointbox"

Transform1079.children.append(Shape1080)

HAnimSegment1074.children.append(Transform1079)
HAnimSite1081 = x3d.HAnimSite()
HAnimSite1081.DEF = "Joe_r_index_distal_tip"
HAnimSite1081.name = "r_index_distal_tip"
HAnimSite1081.translation = [-0.20000000298023224,0.69499999284744263,-0.014999999664723873]
Shape1082 = x3d.Shape()
Shape1082.USE = "sitebox"

HAnimSite1081.children.append(Shape1082)

HAnimSegment1074.children.append(HAnimSite1081)

HAnimJoint1073.children.append(HAnimSegment1074)

HAnimJoint1065.children.append(HAnimJoint1073)

HAnimJoint1057.children.append(HAnimJoint1065)

HAnimJoint1047.children.append(HAnimJoint1057)

HAnimJoint1009.children.append(HAnimJoint1047)
HAnimJoint1083 = x3d.HAnimJoint()
HAnimJoint1083.DEF = "Joe_r_middle0"
HAnimJoint1083.center = [-0.20000000298023224,0.83499997854232788,-0.039999999105930328]
HAnimJoint1083.name = "r_middle0"
HAnimJoint1083.skinCoordIndex = [247,248]
HAnimJoint1083.skinCoordWeight = [1,1]
HAnimJoint1083.stiffness = [0,0,0]
HAnimSegment1084 = x3d.HAnimSegment()
HAnimSegment1084.DEF = "Joe_r_middle_metacarpal"
HAnimSegment1084.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1084.name = "r_middle_metacarpal"
Shape1085 = x3d.Shape()
IndexedLineSet1086 = x3d.IndexedLineSet()
IndexedLineSet1086.coordIndex = [0,1,-1]
Coordinate1087 = x3d.Coordinate()

IndexedLineSet1086.coord = Coordinate1087

Shape1085.geometry = IndexedLineSet1086
Appearance1088 = x3d.Appearance()
Appearance1088.USE = "SegmentLine"

Shape1085.appearance = Appearance1088

HAnimSegment1084.children.append(Shape1085)
Transform1089 = x3d.Transform()
Transform1089.translation = [-0.20000000298023224,0.83499997854232788,-0.039999999105930328]
Shape1090 = x3d.Shape()
Shape1090.USE = "jointbox"

Transform1089.children.append(Shape1090)

HAnimSegment1084.children.append(Transform1089)

HAnimJoint1083.children.append(HAnimSegment1084)
HAnimJoint1091 = x3d.HAnimJoint()
HAnimJoint1091.DEF = "Joe_r_middle1"
HAnimJoint1091.center = [-0.20000000298023224,0.78799998760223389,-0.039999999105930328]
HAnimJoint1091.name = "r_middle1"
HAnimJoint1091.skinCoordIndex = [272,273,279,280]
HAnimJoint1091.skinCoordWeight = [1,1,0.5,0.5]
HAnimJoint1091.stiffness = [0,0,0]
HAnimSegment1092 = x3d.HAnimSegment()
HAnimSegment1092.DEF = "Joe_r_middle_proximal"
HAnimSegment1092.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1092.name = "r_middle_proximal"
Shape1093 = x3d.Shape()
IndexedLineSet1094 = x3d.IndexedLineSet()
IndexedLineSet1094.coordIndex = [0,1,-1]
Coordinate1095 = x3d.Coordinate()

IndexedLineSet1094.coord = Coordinate1095

Shape1093.geometry = IndexedLineSet1094
Appearance1096 = x3d.Appearance()
Appearance1096.USE = "SegmentLine"

Shape1093.appearance = Appearance1096

HAnimSegment1092.children.append(Shape1093)
Transform1097 = x3d.Transform()
Transform1097.translation = [-0.20000000298023224,0.78799998760223389,-0.039999999105930328]
Shape1098 = x3d.Shape()
Shape1098.USE = "jointbox"

Transform1097.children.append(Shape1098)

HAnimSegment1092.children.append(Transform1097)

HAnimJoint1091.children.append(HAnimSegment1092)
HAnimJoint1099 = x3d.HAnimJoint()
HAnimJoint1099.DEF = "Joe_r_middle2"
HAnimJoint1099.center = [-0.20000000298023224,0.74000000953674316,-0.039999999105930328]
HAnimJoint1099.name = "r_middle2"
HAnimJoint1099.skinCoordIndex = [295,296,297,298]
HAnimJoint1099.skinCoordWeight = [1,1,1,1]
HAnimJoint1099.stiffness = [0,0,0]
HAnimSegment1100 = x3d.HAnimSegment()
HAnimSegment1100.DEF = "Joe_r_middle_middle"
HAnimSegment1100.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1100.name = "r_middle_middle"
Shape1101 = x3d.Shape()
IndexedLineSet1102 = x3d.IndexedLineSet()
IndexedLineSet1102.coordIndex = [0,1,-1]
Coordinate1103 = x3d.Coordinate()

IndexedLineSet1102.coord = Coordinate1103

Shape1101.geometry = IndexedLineSet1102
Appearance1104 = x3d.Appearance()
Appearance1104.USE = "SegmentLine"

Shape1101.appearance = Appearance1104

HAnimSegment1100.children.append(Shape1101)
Transform1105 = x3d.Transform()
Transform1105.translation = [-0.20000000298023224,0.74000000953674316,-0.039999999105930328]
Shape1106 = x3d.Shape()
Shape1106.USE = "jointbox"

Transform1105.children.append(Shape1106)

HAnimSegment1100.children.append(Transform1105)

HAnimJoint1099.children.append(HAnimSegment1100)
HAnimJoint1107 = x3d.HAnimJoint()
HAnimJoint1107.DEF = "Joe_r_middle3"
HAnimJoint1107.center = [-0.20000000298023224,0.71420001983642578,-0.039999999105930328]
HAnimJoint1107.name = "r_middle3"
HAnimJoint1107.skinCoordIndex = [299,300,301,302,303,304,305,306,307]
HAnimJoint1107.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint1107.stiffness = [0,0,0]
HAnimSegment1108 = x3d.HAnimSegment()
HAnimSegment1108.DEF = "Joe_r_middle_distal"
HAnimSegment1108.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1108.name = "r_middle_distal"
Shape1109 = x3d.Shape()
IndexedLineSet1110 = x3d.IndexedLineSet()
IndexedLineSet1110.coordIndex = [0,1,-1]
Coordinate1111 = x3d.Coordinate()

IndexedLineSet1110.coord = Coordinate1111

Shape1109.geometry = IndexedLineSet1110
Appearance1112 = x3d.Appearance()
Appearance1112.USE = "SegmentLine"

Shape1109.appearance = Appearance1112

HAnimSegment1108.children.append(Shape1109)
Transform1113 = x3d.Transform()
Transform1113.translation = [-0.20000000298023224,0.71420001983642578,-0.039999999105930328]
Shape1114 = x3d.Shape()
Shape1114.USE = "jointbox"

Transform1113.children.append(Shape1114)

HAnimSegment1108.children.append(Transform1113)
HAnimSite1115 = x3d.HAnimSite()
HAnimSite1115.DEF = "Joe_r_dactylion"
HAnimSite1115.name = "r_dactylion"
HAnimSite1115.translation = [-0.20000000298023224,0.68000000715255737,-0.039999999105930328]
Shape1116 = x3d.Shape()
Shape1116.USE = "sitebox"

HAnimSite1115.children.append(Shape1116)

HAnimSegment1108.children.append(HAnimSite1115)
HAnimSite1117 = x3d.HAnimSite()
HAnimSite1117.DEF = "Joe_r_middle_distal_tip"
HAnimSite1117.name = "r_middle_distal_tip"
HAnimSite1117.translation = [-0.20000000298023224,0.68000000715255737,-0.039999999105930328]
Shape1118 = x3d.Shape()
Shape1118.USE = "sitebox"

HAnimSite1117.children.append(Shape1118)

HAnimSegment1108.children.append(HAnimSite1117)

HAnimJoint1107.children.append(HAnimSegment1108)

HAnimJoint1099.children.append(HAnimJoint1107)

HAnimJoint1091.children.append(HAnimJoint1099)

HAnimJoint1083.children.append(HAnimJoint1091)

HAnimJoint1009.children.append(HAnimJoint1083)
HAnimJoint1119 = x3d.HAnimJoint()
HAnimJoint1119.DEF = "Joe_r_ring0"
HAnimJoint1119.center = [-0.2,0.835,-0.065]
HAnimJoint1119.name = "r_ring0"
HAnimJoint1119.skinCoordIndex = [249,250]
HAnimJoint1119.skinCoordWeight = [1,1]
HAnimSegment1120 = x3d.HAnimSegment()
HAnimSegment1120.DEF = "Joe_r_ring_metacarpal"
HAnimSegment1120.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1120.name = "r_ring_metacarpal"
Shape1121 = x3d.Shape()
IndexedLineSet1122 = x3d.IndexedLineSet()
IndexedLineSet1122.coordIndex = [0,1,-1]
Coordinate1123 = x3d.Coordinate()

IndexedLineSet1122.coord = Coordinate1123

Shape1121.geometry = IndexedLineSet1122
Appearance1124 = x3d.Appearance()
Appearance1124.USE = "SegmentLine"

Shape1121.appearance = Appearance1124

HAnimSegment1120.children.append(Shape1121)
Transform1125 = x3d.Transform()
Transform1125.translation = [-0.20000000298023224,0.83499997854232788,-0.064999997615814209]
Shape1126 = x3d.Shape()
Shape1126.USE = "jointbox"

Transform1125.children.append(Shape1126)

HAnimSegment1120.children.append(Transform1125)

HAnimJoint1119.children.append(HAnimSegment1120)
HAnimJoint1127 = x3d.HAnimJoint()
HAnimJoint1127.DEF = "Joe_r_ring1"
HAnimJoint1127.center = [-0.20000000298023224,0.7929999828338623,-0.064999997615814209]
HAnimJoint1127.name = "r_ring1"
HAnimJoint1127.skinCoordIndex = [274,275,280,281]
HAnimJoint1127.skinCoordWeight = [1,1,0.5,0.5]
HAnimJoint1127.stiffness = [0,0,0]
HAnimSegment1128 = x3d.HAnimSegment()
HAnimSegment1128.DEF = "Joe_r_ring_proximal"
HAnimSegment1128.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1128.name = "r_ring_proximal"
Shape1129 = x3d.Shape()
IndexedLineSet1130 = x3d.IndexedLineSet()
IndexedLineSet1130.coordIndex = [0,1,-1]
Coordinate1131 = x3d.Coordinate()

IndexedLineSet1130.coord = Coordinate1131

Shape1129.geometry = IndexedLineSet1130
Appearance1132 = x3d.Appearance()
Appearance1132.USE = "SegmentLine"

Shape1129.appearance = Appearance1132

HAnimSegment1128.children.append(Shape1129)
Transform1133 = x3d.Transform()
Transform1133.translation = [-0.20000000298023224,0.7929999828338623,-0.064999997615814209]
Shape1134 = x3d.Shape()
Shape1134.USE = "jointbox"

Transform1133.children.append(Shape1134)

HAnimSegment1128.children.append(Transform1133)

HAnimJoint1127.children.append(HAnimSegment1128)
HAnimJoint1135 = x3d.HAnimJoint()
HAnimJoint1135.DEF = "Joe_r_ring2"
HAnimJoint1135.center = [-0.20000000298023224,0.74000000953674316,-0.064999997615814209]
HAnimJoint1135.name = "r_ring2"
HAnimJoint1135.skinCoordIndex = [308,309,310,311]
HAnimJoint1135.skinCoordWeight = [1,1,1,1]
HAnimJoint1135.stiffness = [0,0,0]
HAnimSegment1136 = x3d.HAnimSegment()
HAnimSegment1136.DEF = "Joe_r_ring_middle"
HAnimSegment1136.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1136.name = "r_ring_middle"
Shape1137 = x3d.Shape()
IndexedLineSet1138 = x3d.IndexedLineSet()
IndexedLineSet1138.coordIndex = [0,1,-1]
Coordinate1139 = x3d.Coordinate()

IndexedLineSet1138.coord = Coordinate1139

Shape1137.geometry = IndexedLineSet1138
Appearance1140 = x3d.Appearance()
Appearance1140.USE = "SegmentLine"

Shape1137.appearance = Appearance1140

HAnimSegment1136.children.append(Shape1137)
Transform1141 = x3d.Transform()
Transform1141.translation = [-0.20000000298023224,0.74000000953674316,-0.064999997615814209]
Shape1142 = x3d.Shape()
Shape1142.USE = "jointbox"

Transform1141.children.append(Shape1142)

HAnimSegment1136.children.append(Transform1141)

HAnimJoint1135.children.append(HAnimSegment1136)
HAnimJoint1143 = x3d.HAnimJoint()
HAnimJoint1143.DEF = "Joe_r_ring3"
HAnimJoint1143.center = [-0.20000000298023224,0.71770000457763672,-0.064999997615814209]
HAnimJoint1143.name = "r_ring3"
HAnimJoint1143.skinCoordIndex = [312,313,314,315,316,317,318,319,320]
HAnimJoint1143.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint1143.stiffness = [0,0,0]
HAnimSegment1144 = x3d.HAnimSegment()
HAnimSegment1144.DEF = "Joe_r_ring_distal"
HAnimSegment1144.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1144.name = "r_ring_distal"
Shape1145 = x3d.Shape()
IndexedLineSet1146 = x3d.IndexedLineSet()
IndexedLineSet1146.coordIndex = [0,1,-1]
Coordinate1147 = x3d.Coordinate()

IndexedLineSet1146.coord = Coordinate1147

Shape1145.geometry = IndexedLineSet1146
Appearance1148 = x3d.Appearance()
Appearance1148.USE = "SegmentLine"

Shape1145.appearance = Appearance1148

HAnimSegment1144.children.append(Shape1145)
Transform1149 = x3d.Transform()
Transform1149.translation = [-0.20000000298023224,0.71770000457763672,-0.064999997615814209]
Shape1150 = x3d.Shape()
Shape1150.USE = "jointbox"

Transform1149.children.append(Shape1150)

HAnimSegment1144.children.append(Transform1149)
HAnimSite1151 = x3d.HAnimSite()
HAnimSite1151.DEF = "Joe_r_ring_distal_tip"
HAnimSite1151.name = "r_ring_distal_tip"
HAnimSite1151.translation = [-0.20000000298023224,0.69499999284744263,-0.064999997615814209]
Shape1152 = x3d.Shape()
Shape1152.USE = "sitebox"

HAnimSite1151.children.append(Shape1152)

HAnimSegment1144.children.append(HAnimSite1151)

HAnimJoint1143.children.append(HAnimSegment1144)

HAnimJoint1135.children.append(HAnimJoint1143)

HAnimJoint1127.children.append(HAnimJoint1135)

HAnimJoint1119.children.append(HAnimJoint1127)

HAnimJoint1009.children.append(HAnimJoint1119)
HAnimJoint1153 = x3d.HAnimJoint()
HAnimJoint1153.DEF = "Joe_r_pinky0"
HAnimJoint1153.center = [-0.20000000298023224,0.8399999737739563,-0.085000000894069672]
HAnimJoint1153.name = "r_pinky0"
HAnimJoint1153.skinCoordIndex = [251,252,253,281]
HAnimJoint1153.skinCoordWeight = [1,1,1,0.5]
HAnimJoint1153.stiffness = [0,0,0]
HAnimSegment1154 = x3d.HAnimSegment()
HAnimSegment1154.DEF = "Joe_r_pinky_metacarpal"
HAnimSegment1154.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1154.name = "r_pinky_metacarpal"
Shape1155 = x3d.Shape()
IndexedLineSet1156 = x3d.IndexedLineSet()
IndexedLineSet1156.coordIndex = [0,1,-1]
Coordinate1157 = x3d.Coordinate()

IndexedLineSet1156.coord = Coordinate1157

Shape1155.geometry = IndexedLineSet1156
Appearance1158 = x3d.Appearance()
Appearance1158.USE = "SegmentLine"

Shape1155.appearance = Appearance1158

HAnimSegment1154.children.append(Shape1155)
Transform1159 = x3d.Transform()
Transform1159.translation = [-0.20000000298023224,0.8399999737739563,-0.085000000894069672]
Shape1160 = x3d.Shape()
Shape1160.USE = "jointbox"

Transform1159.children.append(Shape1160)

HAnimSegment1154.children.append(Transform1159)
HAnimSite1161 = x3d.HAnimSite()
HAnimSite1161.DEF = "Joe_r_metacarpal_pha5"
HAnimSite1161.name = "r_metacarpal_pha5"
HAnimSite1161.translation = [-0.20000000298023224,0.79000002145767212,-0.094999998807907104]
Shape1162 = x3d.Shape()
Shape1162.USE = "sitebox"

HAnimSite1161.children.append(Shape1162)

HAnimSegment1154.children.append(HAnimSite1161)

HAnimJoint1153.children.append(HAnimSegment1154)
HAnimJoint1163 = x3d.HAnimJoint()
HAnimJoint1163.DEF = "Joe_r_pinky1"
HAnimJoint1163.center = [-0.20000000298023224,0.79000002145767212,-0.085000000894069672]
HAnimJoint1163.name = "r_pinky1"
HAnimJoint1163.skinCoordIndex = [276,277,278]
HAnimJoint1163.skinCoordWeight = [1,1,1]
HAnimJoint1163.stiffness = [0,0,0]
HAnimSegment1164 = x3d.HAnimSegment()
HAnimSegment1164.DEF = "Joe_r_pinky_proximal"
HAnimSegment1164.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1164.name = "r_pinky_proximal"
Shape1165 = x3d.Shape()
IndexedLineSet1166 = x3d.IndexedLineSet()
IndexedLineSet1166.coordIndex = [0,1,-1]
Coordinate1167 = x3d.Coordinate()

IndexedLineSet1166.coord = Coordinate1167

Shape1165.geometry = IndexedLineSet1166
Appearance1168 = x3d.Appearance()
Appearance1168.USE = "SegmentLine"

Shape1165.appearance = Appearance1168

HAnimSegment1164.children.append(Shape1165)
Transform1169 = x3d.Transform()
Transform1169.translation = [-0.20000000298023224,0.79000002145767212,-0.085000000894069672]
Shape1170 = x3d.Shape()
Shape1170.USE = "jointbox"

Transform1169.children.append(Shape1170)

HAnimSegment1164.children.append(Transform1169)

HAnimJoint1163.children.append(HAnimSegment1164)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.DEF = "Joe_r_pinky2"
HAnimJoint1171.center = [-0.20000000298023224,0.75499999523162842,-0.085000000894069672]
HAnimJoint1171.name = "r_pinky2"
HAnimJoint1171.skinCoordIndex = [321,322,323,324]
HAnimJoint1171.skinCoordWeight = [1,1,1,1]
HAnimJoint1171.stiffness = [0,0,0]
HAnimSegment1172 = x3d.HAnimSegment()
HAnimSegment1172.DEF = "Joe_r_pinky_middle"
HAnimSegment1172.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1172.name = "r_pinky_middle"
Shape1173 = x3d.Shape()
IndexedLineSet1174 = x3d.IndexedLineSet()
IndexedLineSet1174.coordIndex = [0,1,-1]
Coordinate1175 = x3d.Coordinate()

IndexedLineSet1174.coord = Coordinate1175

Shape1173.geometry = IndexedLineSet1174
Appearance1176 = x3d.Appearance()
Appearance1176.USE = "SegmentLine"

Shape1173.appearance = Appearance1176

HAnimSegment1172.children.append(Shape1173)
Transform1177 = x3d.Transform()
Transform1177.translation = [-0.20000000298023224,0.75499999523162842,-0.085000000894069672]
Shape1178 = x3d.Shape()
Shape1178.USE = "jointbox"

Transform1177.children.append(Shape1178)

HAnimSegment1172.children.append(Transform1177)

HAnimJoint1171.children.append(HAnimSegment1172)
HAnimJoint1179 = x3d.HAnimJoint()
HAnimJoint1179.DEF = "Joe_r_pinky3"
HAnimJoint1179.center = [-0.20000000298023224,0.73500001430511475,-0.090000003576278687]
HAnimJoint1179.name = "r_pinky3"
HAnimJoint1179.skinCoordIndex = [325,326,327,328,329,330,331,332,333]
HAnimJoint1179.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint1179.stiffness = [0,0,0]
HAnimSegment1180 = x3d.HAnimSegment()
HAnimSegment1180.DEF = "Joe_r_pinky_distal"
HAnimSegment1180.momentsOfInertia = [0,0,0,0,0,0,0,0,0]
HAnimSegment1180.name = "r_pinky_distal"
Shape1181 = x3d.Shape()
IndexedLineSet1182 = x3d.IndexedLineSet()
IndexedLineSet1182.coordIndex = [0,1,-1]
Coordinate1183 = x3d.Coordinate()

IndexedLineSet1182.coord = Coordinate1183

Shape1181.geometry = IndexedLineSet1182
Appearance1184 = x3d.Appearance()
Appearance1184.USE = "SegmentLine"

Shape1181.appearance = Appearance1184

HAnimSegment1180.children.append(Shape1181)
Transform1185 = x3d.Transform()
Transform1185.translation = [-0.20000000298023224,0.73500001430511475,-0.085000000894069672]
Shape1186 = x3d.Shape()
Shape1186.USE = "jointbox"

Transform1185.children.append(Shape1186)

HAnimSegment1180.children.append(Transform1185)
HAnimSite1187 = x3d.HAnimSite()
HAnimSite1187.DEF = "Joe_r_pinky_distal_tip"
HAnimSite1187.name = "r_pinky_distal_tip"
HAnimSite1187.translation = [-0.20000000298023224,0.72000002861022949,-0.085000000894069672]
Shape1188 = x3d.Shape()
Shape1188.USE = "sitebox"

HAnimSite1187.children.append(Shape1188)

HAnimSegment1180.children.append(HAnimSite1187)

HAnimJoint1179.children.append(HAnimSegment1180)

HAnimJoint1171.children.append(HAnimJoint1179)

HAnimJoint1163.children.append(HAnimJoint1171)

HAnimJoint1153.children.append(HAnimJoint1163)

HAnimJoint1009.children.append(HAnimJoint1153)

HAnimJoint987.children.append(HAnimJoint1009)

HAnimJoint957.children.append(HAnimJoint987)

HAnimJoint941.children.append(HAnimJoint957)

HAnimJoint931.children.append(HAnimJoint941)

HAnimJoint565.children.append(HAnimJoint931)

HAnimJoint557.children.append(HAnimJoint565)

HAnimJoint549.children.append(HAnimJoint557)

HAnimJoint539.children.append(HAnimJoint549)

HAnimJoint531.children.append(HAnimJoint539)

HAnimJoint523.children.append(HAnimJoint531)

HAnimJoint515.children.append(HAnimJoint523)

HAnimJoint507.children.append(HAnimJoint515)

HAnimJoint495.children.append(HAnimJoint507)

HAnimJoint485.children.append(HAnimJoint495)

HAnimJoint477.children.append(HAnimJoint485)

HAnimJoint469.children.append(HAnimJoint477)

HAnimJoint461.children.append(HAnimJoint469)

HAnimJoint435.children.append(HAnimJoint461)

HAnimJoint427.children.append(HAnimJoint435)

HAnimJoint419.children.append(HAnimJoint427)

HAnimJoint404.children.append(HAnimJoint419)

HAnimJoint90.children.append(HAnimJoint404)

HAnimHumanoid81.skeleton.append(HAnimJoint90)
HAnimJoint1189 = x3d.HAnimJoint()
HAnimJoint1189.USE = "Joe_sacroiliac"

HAnimHumanoid81.joints.append(HAnimJoint1189)
HAnimJoint1190 = x3d.HAnimJoint()
HAnimJoint1190.USE = "Joe_l_hip"

HAnimHumanoid81.joints.append(HAnimJoint1190)
HAnimJoint1191 = x3d.HAnimJoint()
HAnimJoint1191.USE = "Joe_l_knee"

HAnimHumanoid81.joints.append(HAnimJoint1191)
HAnimJoint1192 = x3d.HAnimJoint()
HAnimJoint1192.USE = "Joe_l_ankle"

HAnimHumanoid81.joints.append(HAnimJoint1192)
HAnimJoint1193 = x3d.HAnimJoint()
HAnimJoint1193.USE = "Joe_l_subtalar"

HAnimHumanoid81.joints.append(HAnimJoint1193)
HAnimJoint1194 = x3d.HAnimJoint()
HAnimJoint1194.USE = "Joe_l_midtarsal"

HAnimHumanoid81.joints.append(HAnimJoint1194)
HAnimJoint1195 = x3d.HAnimJoint()
HAnimJoint1195.USE = "Joe_l_metatarsal"

HAnimHumanoid81.joints.append(HAnimJoint1195)
HAnimJoint1196 = x3d.HAnimJoint()
HAnimJoint1196.USE = "Joe_r_hip"

HAnimHumanoid81.joints.append(HAnimJoint1196)
HAnimJoint1197 = x3d.HAnimJoint()
HAnimJoint1197.USE = "Joe_r_knee"

HAnimHumanoid81.joints.append(HAnimJoint1197)
HAnimJoint1198 = x3d.HAnimJoint()
HAnimJoint1198.USE = "Joe_r_ankle"

HAnimHumanoid81.joints.append(HAnimJoint1198)
HAnimJoint1199 = x3d.HAnimJoint()
HAnimJoint1199.USE = "Joe_r_subtalar"

HAnimHumanoid81.joints.append(HAnimJoint1199)
HAnimJoint1200 = x3d.HAnimJoint()
HAnimJoint1200.USE = "Joe_r_midtarsal"

HAnimHumanoid81.joints.append(HAnimJoint1200)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.USE = "Joe_r_metatarsal"

HAnimHumanoid81.joints.append(HAnimJoint1201)
HAnimJoint1202 = x3d.HAnimJoint()
HAnimJoint1202.USE = "Joe_vl5"

HAnimHumanoid81.joints.append(HAnimJoint1202)
HAnimJoint1203 = x3d.HAnimJoint()
HAnimJoint1203.USE = "Joe_vl4"

HAnimHumanoid81.joints.append(HAnimJoint1203)
HAnimJoint1204 = x3d.HAnimJoint()
HAnimJoint1204.USE = "Joe_vl3"

HAnimHumanoid81.joints.append(HAnimJoint1204)
HAnimJoint1205 = x3d.HAnimJoint()
HAnimJoint1205.USE = "Joe_vl2"

HAnimHumanoid81.joints.append(HAnimJoint1205)
HAnimJoint1206 = x3d.HAnimJoint()
HAnimJoint1206.USE = "Joe_vl1"

HAnimHumanoid81.joints.append(HAnimJoint1206)
HAnimJoint1207 = x3d.HAnimJoint()
HAnimJoint1207.USE = "Joe_vt12"

HAnimHumanoid81.joints.append(HAnimJoint1207)
HAnimJoint1208 = x3d.HAnimJoint()
HAnimJoint1208.USE = "Joe_vt11"

HAnimHumanoid81.joints.append(HAnimJoint1208)
HAnimJoint1209 = x3d.HAnimJoint()
HAnimJoint1209.USE = "Joe_vt10"

HAnimHumanoid81.joints.append(HAnimJoint1209)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.USE = "Joe_vt9"

HAnimHumanoid81.joints.append(HAnimJoint1210)
HAnimJoint1211 = x3d.HAnimJoint()
HAnimJoint1211.USE = "Joe_vt8"

HAnimHumanoid81.joints.append(HAnimJoint1211)
HAnimJoint1212 = x3d.HAnimJoint()
HAnimJoint1212.USE = "Joe_vt7"

HAnimHumanoid81.joints.append(HAnimJoint1212)
HAnimJoint1213 = x3d.HAnimJoint()
HAnimJoint1213.USE = "Joe_vt6"

HAnimHumanoid81.joints.append(HAnimJoint1213)
HAnimJoint1214 = x3d.HAnimJoint()
HAnimJoint1214.USE = "Joe_vt5"

HAnimHumanoid81.joints.append(HAnimJoint1214)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.USE = "Joe_vt4"

HAnimHumanoid81.joints.append(HAnimJoint1215)
HAnimJoint1216 = x3d.HAnimJoint()
HAnimJoint1216.USE = "Joe_vt3"

HAnimHumanoid81.joints.append(HAnimJoint1216)
HAnimJoint1217 = x3d.HAnimJoint()
HAnimJoint1217.USE = "Joe_vt2"

HAnimHumanoid81.joints.append(HAnimJoint1217)
HAnimJoint1218 = x3d.HAnimJoint()
HAnimJoint1218.USE = "Joe_vt1"

HAnimHumanoid81.joints.append(HAnimJoint1218)
HAnimJoint1219 = x3d.HAnimJoint()
HAnimJoint1219.USE = "Joe_vc7"

HAnimHumanoid81.joints.append(HAnimJoint1219)
HAnimJoint1220 = x3d.HAnimJoint()
HAnimJoint1220.USE = "Joe_vc6"

HAnimHumanoid81.joints.append(HAnimJoint1220)
HAnimJoint1221 = x3d.HAnimJoint()
HAnimJoint1221.USE = "Joe_vc5"

HAnimHumanoid81.joints.append(HAnimJoint1221)
HAnimJoint1222 = x3d.HAnimJoint()
HAnimJoint1222.USE = "Joe_vc4"

HAnimHumanoid81.joints.append(HAnimJoint1222)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.USE = "Joe_vc3"

HAnimHumanoid81.joints.append(HAnimJoint1223)
HAnimJoint1224 = x3d.HAnimJoint()
HAnimJoint1224.USE = "Joe_vc2"

HAnimHumanoid81.joints.append(HAnimJoint1224)
HAnimJoint1225 = x3d.HAnimJoint()
HAnimJoint1225.USE = "Joe_vc1"

HAnimHumanoid81.joints.append(HAnimJoint1225)
HAnimJoint1226 = x3d.HAnimJoint()
HAnimJoint1226.USE = "Joe_skullbase"

HAnimHumanoid81.joints.append(HAnimJoint1226)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.USE = "Joe_l_eyeball_joint"

HAnimHumanoid81.joints.append(HAnimJoint1227)
HAnimJoint1228 = x3d.HAnimJoint()
HAnimJoint1228.USE = "Joe_r_eyeball_joint"

HAnimHumanoid81.joints.append(HAnimJoint1228)
HAnimJoint1229 = x3d.HAnimJoint()
HAnimJoint1229.USE = "Joe_l_sternoclavicular"

HAnimHumanoid81.joints.append(HAnimJoint1229)
HAnimJoint1230 = x3d.HAnimJoint()
HAnimJoint1230.USE = "Joe_l_acromioclavicular"

HAnimHumanoid81.joints.append(HAnimJoint1230)
HAnimJoint1231 = x3d.HAnimJoint()
HAnimJoint1231.USE = "Joe_l_shoulder"

HAnimHumanoid81.joints.append(HAnimJoint1231)
HAnimJoint1232 = x3d.HAnimJoint()
HAnimJoint1232.USE = "Joe_l_elbow"

HAnimHumanoid81.joints.append(HAnimJoint1232)
HAnimJoint1233 = x3d.HAnimJoint()
HAnimJoint1233.USE = "Joe_l_wrist"

HAnimHumanoid81.joints.append(HAnimJoint1233)
HAnimJoint1234 = x3d.HAnimJoint()
HAnimJoint1234.USE = "Joe_l_thumb1"

HAnimHumanoid81.joints.append(HAnimJoint1234)
HAnimJoint1235 = x3d.HAnimJoint()
HAnimJoint1235.USE = "Joe_l_thumb2"

HAnimHumanoid81.joints.append(HAnimJoint1235)
HAnimJoint1236 = x3d.HAnimJoint()
HAnimJoint1236.USE = "Joe_l_thumb3"

HAnimHumanoid81.joints.append(HAnimJoint1236)
HAnimJoint1237 = x3d.HAnimJoint()
HAnimJoint1237.USE = "Joe_l_index0"

HAnimHumanoid81.joints.append(HAnimJoint1237)
HAnimJoint1238 = x3d.HAnimJoint()
HAnimJoint1238.USE = "Joe_l_index1"

HAnimHumanoid81.joints.append(HAnimJoint1238)
HAnimJoint1239 = x3d.HAnimJoint()
HAnimJoint1239.USE = "Joe_l_index2"

HAnimHumanoid81.joints.append(HAnimJoint1239)
HAnimJoint1240 = x3d.HAnimJoint()
HAnimJoint1240.USE = "Joe_l_index3"

HAnimHumanoid81.joints.append(HAnimJoint1240)
HAnimJoint1241 = x3d.HAnimJoint()
HAnimJoint1241.USE = "Joe_l_middle0"

HAnimHumanoid81.joints.append(HAnimJoint1241)
HAnimJoint1242 = x3d.HAnimJoint()
HAnimJoint1242.USE = "Joe_l_middle1"

HAnimHumanoid81.joints.append(HAnimJoint1242)
HAnimJoint1243 = x3d.HAnimJoint()
HAnimJoint1243.USE = "Joe_l_middle2"

HAnimHumanoid81.joints.append(HAnimJoint1243)
HAnimJoint1244 = x3d.HAnimJoint()
HAnimJoint1244.USE = "Joe_l_middle3"

HAnimHumanoid81.joints.append(HAnimJoint1244)
HAnimJoint1245 = x3d.HAnimJoint()
HAnimJoint1245.USE = "Joe_l_ring0"

HAnimHumanoid81.joints.append(HAnimJoint1245)
HAnimJoint1246 = x3d.HAnimJoint()
HAnimJoint1246.USE = "Joe_l_ring1"

HAnimHumanoid81.joints.append(HAnimJoint1246)
HAnimJoint1247 = x3d.HAnimJoint()
HAnimJoint1247.USE = "Joe_l_ring2"

HAnimHumanoid81.joints.append(HAnimJoint1247)
HAnimJoint1248 = x3d.HAnimJoint()
HAnimJoint1248.USE = "Joe_l_ring3"

HAnimHumanoid81.joints.append(HAnimJoint1248)
HAnimJoint1249 = x3d.HAnimJoint()
HAnimJoint1249.USE = "Joe_l_pinky0"

HAnimHumanoid81.joints.append(HAnimJoint1249)
HAnimJoint1250 = x3d.HAnimJoint()
HAnimJoint1250.USE = "Joe_l_pinky1"

HAnimHumanoid81.joints.append(HAnimJoint1250)
HAnimJoint1251 = x3d.HAnimJoint()
HAnimJoint1251.USE = "Joe_l_pinky2"

HAnimHumanoid81.joints.append(HAnimJoint1251)
HAnimJoint1252 = x3d.HAnimJoint()
HAnimJoint1252.USE = "Joe_l_pinky3"

HAnimHumanoid81.joints.append(HAnimJoint1252)
HAnimJoint1253 = x3d.HAnimJoint()
HAnimJoint1253.USE = "Joe_r_sternoclavicular"

HAnimHumanoid81.joints.append(HAnimJoint1253)
HAnimJoint1254 = x3d.HAnimJoint()
HAnimJoint1254.USE = "Joe_r_acromioclavicular"

HAnimHumanoid81.joints.append(HAnimJoint1254)
HAnimJoint1255 = x3d.HAnimJoint()
HAnimJoint1255.USE = "Joe_r_shoulder"

HAnimHumanoid81.joints.append(HAnimJoint1255)
HAnimJoint1256 = x3d.HAnimJoint()
HAnimJoint1256.USE = "Joe_r_elbow"

HAnimHumanoid81.joints.append(HAnimJoint1256)
HAnimJoint1257 = x3d.HAnimJoint()
HAnimJoint1257.USE = "Joe_r_wrist"

HAnimHumanoid81.joints.append(HAnimJoint1257)
HAnimJoint1258 = x3d.HAnimJoint()
HAnimJoint1258.USE = "Joe_r_thumb1"

HAnimHumanoid81.joints.append(HAnimJoint1258)
HAnimJoint1259 = x3d.HAnimJoint()
HAnimJoint1259.USE = "Joe_r_thumb2"

HAnimHumanoid81.joints.append(HAnimJoint1259)
HAnimJoint1260 = x3d.HAnimJoint()
HAnimJoint1260.USE = "Joe_r_thumb3"

HAnimHumanoid81.joints.append(HAnimJoint1260)
HAnimJoint1261 = x3d.HAnimJoint()
HAnimJoint1261.USE = "Joe_r_index0"

HAnimHumanoid81.joints.append(HAnimJoint1261)
HAnimJoint1262 = x3d.HAnimJoint()
HAnimJoint1262.USE = "Joe_r_index1"

HAnimHumanoid81.joints.append(HAnimJoint1262)
HAnimJoint1263 = x3d.HAnimJoint()
HAnimJoint1263.USE = "Joe_r_index2"

HAnimHumanoid81.joints.append(HAnimJoint1263)
HAnimJoint1264 = x3d.HAnimJoint()
HAnimJoint1264.USE = "Joe_r_index3"

HAnimHumanoid81.joints.append(HAnimJoint1264)
HAnimJoint1265 = x3d.HAnimJoint()
HAnimJoint1265.USE = "Joe_r_middle0"

HAnimHumanoid81.joints.append(HAnimJoint1265)
HAnimJoint1266 = x3d.HAnimJoint()
HAnimJoint1266.USE = "Joe_r_middle1"

HAnimHumanoid81.joints.append(HAnimJoint1266)
HAnimJoint1267 = x3d.HAnimJoint()
HAnimJoint1267.USE = "Joe_r_middle2"

HAnimHumanoid81.joints.append(HAnimJoint1267)
HAnimJoint1268 = x3d.HAnimJoint()
HAnimJoint1268.USE = "Joe_r_middle3"

HAnimHumanoid81.joints.append(HAnimJoint1268)
HAnimJoint1269 = x3d.HAnimJoint()
HAnimJoint1269.USE = "Joe_r_ring0"

HAnimHumanoid81.joints.append(HAnimJoint1269)
HAnimJoint1270 = x3d.HAnimJoint()
HAnimJoint1270.USE = "Joe_r_ring1"

HAnimHumanoid81.joints.append(HAnimJoint1270)
HAnimJoint1271 = x3d.HAnimJoint()
HAnimJoint1271.USE = "Joe_r_ring2"

HAnimHumanoid81.joints.append(HAnimJoint1271)
HAnimJoint1272 = x3d.HAnimJoint()
HAnimJoint1272.USE = "Joe_r_ring3"

HAnimHumanoid81.joints.append(HAnimJoint1272)
HAnimJoint1273 = x3d.HAnimJoint()
HAnimJoint1273.USE = "Joe_r_pinky0"

HAnimHumanoid81.joints.append(HAnimJoint1273)
HAnimJoint1274 = x3d.HAnimJoint()
HAnimJoint1274.USE = "Joe_r_pinky1"

HAnimHumanoid81.joints.append(HAnimJoint1274)
HAnimJoint1275 = x3d.HAnimJoint()
HAnimJoint1275.USE = "Joe_r_pinky2"

HAnimHumanoid81.joints.append(HAnimJoint1275)
HAnimJoint1276 = x3d.HAnimJoint()
HAnimJoint1276.USE = "Joe_r_pinky3"

HAnimHumanoid81.joints.append(HAnimJoint1276)
HAnimJoint1277 = x3d.HAnimJoint()
HAnimJoint1277.USE = "Joe_HumanoidRoot"

HAnimHumanoid81.skeleton.append(HAnimJoint1277)

Group80.children.append(HAnimHumanoid81)

Group79.children.append(Group80)

Scene35.children.append(Group79)
TimeSensor1278 = x3d.TimeSensor()
TimeSensor1278.DEF = "Time1"
TimeSensor1278.cycleInterval = 2.8599999999999999
TimeSensor1278.loop = True

Scene35.children.append(TimeSensor1278)
TimeSensor1279 = x3d.TimeSensor()
TimeSensor1279.DEF = "Time2"
TimeSensor1279.cycleInterval = 5.7199999999999998
TimeSensor1279.loop = True

Scene35.children.append(TimeSensor1279)
TimeSensor1280 = x3d.TimeSensor()
TimeSensor1280.DEF = "Time3"
TimeSensor1280.cycleInterval = 5.7999999999999998
TimeSensor1280.loop = True

Scene35.children.append(TimeSensor1280)
OrientationInterpolator1281 = x3d.OrientationInterpolator()
OrientationInterpolator1281.DEF = "Pitch"
OrientationInterpolator1281.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1281)
OrientationInterpolator1282 = x3d.OrientationInterpolator()
OrientationInterpolator1282.DEF = "Yaw"
OrientationInterpolator1282.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1282)
OrientationInterpolator1283 = x3d.OrientationInterpolator()
OrientationInterpolator1283.DEF = "Roll"
OrientationInterpolator1283.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1283)
OrientationInterpolator1284 = x3d.OrientationInterpolator()
OrientationInterpolator1284.DEF = "vc6Yaw"
OrientationInterpolator1284.key = [0,0.20000000298023224,0.40000000596046448,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1284)
ROUTE1285 = x3d.ROUTE()
ROUTE1285.fromField = "fraction_changed"
ROUTE1285.fromNode = "Time2"
ROUTE1285.toField = "set_fraction"
ROUTE1285.toNode = "vc6Yaw"

Scene35.children.append(ROUTE1285)
ROUTE1286 = x3d.ROUTE()
ROUTE1286.fromField = "value_changed"
ROUTE1286.fromNode = "vc6Yaw"
ROUTE1286.toField = "set_rotation"
ROUTE1286.toNode = "Joe_vc6"

Scene35.children.append(ROUTE1286)
OrientationInterpolator1287 = x3d.OrientationInterpolator()
OrientationInterpolator1287.DEF = "EyeballsRotation"
OrientationInterpolator1287.key = [0,0.10000000149011612,0.20000000298023224,0.30000001192092896,0.40000000596046448,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1287)
ROUTE1288 = x3d.ROUTE()
ROUTE1288.fromField = "fraction_changed"
ROUTE1288.fromNode = "Time3"
ROUTE1288.toField = "set_fraction"
ROUTE1288.toNode = "EyeballsRotation"

Scene35.children.append(ROUTE1288)
ROUTE1289 = x3d.ROUTE()
ROUTE1289.fromField = "value_changed"
ROUTE1289.fromNode = "EyeballsRotation"
ROUTE1289.toField = "set_rotation"
ROUTE1289.toNode = "Joe_r_eyeball_joint"

Scene35.children.append(ROUTE1289)
ROUTE1290 = x3d.ROUTE()
ROUTE1290.fromField = "value_changed"
ROUTE1290.fromNode = "EyeballsRotation"
ROUTE1290.toField = "set_rotation"
ROUTE1290.toNode = "Joe_l_eyeball_joint"

Scene35.children.append(ROUTE1290)
OrientationInterpolator1291 = x3d.OrientationInterpolator()
OrientationInterpolator1291.DEF = "r_sternoclavicularRelax"
OrientationInterpolator1291.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1291)
OrientationInterpolator1292 = x3d.OrientationInterpolator()
OrientationInterpolator1292.DEF = "r_acromioclavicularRelax"
OrientationInterpolator1292.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1292)
OrientationInterpolator1293 = x3d.OrientationInterpolator()
OrientationInterpolator1293.DEF = "r_shoulderRelax"
OrientationInterpolator1293.key = [0,0.10000000149011612,0.30000001192092896,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1293)
OrientationInterpolator1294 = x3d.OrientationInterpolator()
OrientationInterpolator1294.DEF = "r_elbowRelax"
OrientationInterpolator1294.key = [0,0.15000000596046448,0.40000000596046448,0.60000002384185791,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1294)
OrientationInterpolator1295 = x3d.OrientationInterpolator()
OrientationInterpolator1295.DEF = "r_wristRelax"
OrientationInterpolator1295.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1295)
OrientationInterpolator1296 = x3d.OrientationInterpolator()
OrientationInterpolator1296.DEF = "r_index0Relax"
OrientationInterpolator1296.key = [0,0.10000000149011612,0.30000001192092896,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1296)
OrientationInterpolator1297 = x3d.OrientationInterpolator()
OrientationInterpolator1297.DEF = "r_index1Relax"
OrientationInterpolator1297.key = [0,0.10000000149011612,0.20000000298023224,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1297)
OrientationInterpolator1298 = x3d.OrientationInterpolator()
OrientationInterpolator1298.DEF = "r_middle0Relax"
OrientationInterpolator1298.key = [0,0.10000000149011612,0.30000001192092896,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1298)
OrientationInterpolator1299 = x3d.OrientationInterpolator()
OrientationInterpolator1299.DEF = "r_middle1Relax"
OrientationInterpolator1299.key = [0,0.10000000149011612,0.20000000298023224,0.30000001192092896,0.40000000596046448,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1299)
OrientationInterpolator1300 = x3d.OrientationInterpolator()
OrientationInterpolator1300.DEF = "r_ring0Relax"
OrientationInterpolator1300.key = [0,0.10000000149011612,0.30000001192092896,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1300)
OrientationInterpolator1301 = x3d.OrientationInterpolator()
OrientationInterpolator1301.DEF = "r_ring1Relax"
OrientationInterpolator1301.key = [0,0.10000000149011612,0.40000000596046448,0.5,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1301)
OrientationInterpolator1302 = x3d.OrientationInterpolator()
OrientationInterpolator1302.DEF = "r_pinky0Relax"
OrientationInterpolator1302.key = [0,0.10000000149011612,0.30000001192092896,0.5,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1302)
OrientationInterpolator1303 = x3d.OrientationInterpolator()
OrientationInterpolator1303.DEF = "r_pinky1Relax"
OrientationInterpolator1303.key = [0,0.10000000149011612,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1303)
OrientationInterpolator1304 = x3d.OrientationInterpolator()
OrientationInterpolator1304.DEF = "r_thumb1Relax"
OrientationInterpolator1304.key = [0,0.029999999329447746,0.079999998211860657,0.20000000298023224,0.30000001192092896,0.40000000596046448,0.5,0.80000001192092896,0.94999998807907104,1]

Scene35.children.append(OrientationInterpolator1304)
OrientationInterpolator1305 = x3d.OrientationInterpolator()
OrientationInterpolator1305.DEF = "r_thumb2Relax"
OrientationInterpolator1305.key = [0,0.20000000298023224,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1305)
OrientationInterpolator1306 = x3d.OrientationInterpolator()
OrientationInterpolator1306.DEF = "r_thumb3Relax"
OrientationInterpolator1306.key = [0,0.20000000298023224,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1306)
OrientationInterpolator1307 = x3d.OrientationInterpolator()
OrientationInterpolator1307.DEF = "r_fingers2Relax"
OrientationInterpolator1307.key = [0,0.10000000149011612,0.20000000298023224,0.30000001192092896,0.40000000596046448,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1307)
OrientationInterpolator1308 = x3d.OrientationInterpolator()
OrientationInterpolator1308.DEF = "r_fingers3Relax"
OrientationInterpolator1308.key = [0,0.10000000149011612,0.20000000298023224,0.30000001192092896,0.40000000596046448,0.5,0.60000002384185791,0.69999998807907104,0.80000001192092896,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1308)
ROUTE1309 = x3d.ROUTE()
ROUTE1309.fromField = "value_changed"
ROUTE1309.fromNode = "r_sternoclavicularRelax"
ROUTE1309.toField = "set_rotation"
ROUTE1309.toNode = "Joe_r_sternoclavicular"

Scene35.children.append(ROUTE1309)
ROUTE1310 = x3d.ROUTE()
ROUTE1310.fromField = "value_changed"
ROUTE1310.fromNode = "r_acromioclavicularRelax"
ROUTE1310.toField = "set_rotation"
ROUTE1310.toNode = "Joe_r_acromioclavicular"

Scene35.children.append(ROUTE1310)
ROUTE1311 = x3d.ROUTE()
ROUTE1311.fromField = "value_changed"
ROUTE1311.fromNode = "r_shoulderRelax"
ROUTE1311.toField = "set_rotation"
ROUTE1311.toNode = "Joe_r_shoulder"

Scene35.children.append(ROUTE1311)
ROUTE1312 = x3d.ROUTE()
ROUTE1312.fromField = "value_changed"
ROUTE1312.fromNode = "r_elbowRelax"
ROUTE1312.toField = "set_rotation"
ROUTE1312.toNode = "Joe_r_elbow"

Scene35.children.append(ROUTE1312)
ROUTE1313 = x3d.ROUTE()
ROUTE1313.fromField = "value_changed"
ROUTE1313.fromNode = "r_wristRelax"
ROUTE1313.toField = "set_rotation"
ROUTE1313.toNode = "Joe_r_wrist"

Scene35.children.append(ROUTE1313)
ROUTE1314 = x3d.ROUTE()
ROUTE1314.fromField = "value_changed"
ROUTE1314.fromNode = "r_thumb1Relax"
ROUTE1314.toField = "set_rotation"
ROUTE1314.toNode = "Joe_r_thumb1"

Scene35.children.append(ROUTE1314)
ROUTE1315 = x3d.ROUTE()
ROUTE1315.fromField = "value_changed"
ROUTE1315.fromNode = "r_thumb2Relax"
ROUTE1315.toField = "set_rotation"
ROUTE1315.toNode = "Joe_r_thumb2"

Scene35.children.append(ROUTE1315)
ROUTE1316 = x3d.ROUTE()
ROUTE1316.fromField = "value_changed"
ROUTE1316.fromNode = "r_thumb3Relax"
ROUTE1316.toField = "set_rotation"
ROUTE1316.toNode = "Joe_r_thumb3"

Scene35.children.append(ROUTE1316)
ROUTE1317 = x3d.ROUTE()
ROUTE1317.fromField = "value_changed"
ROUTE1317.fromNode = "r_index0Relax"
ROUTE1317.toField = "set_rotation"
ROUTE1317.toNode = "Joe_r_index0"

Scene35.children.append(ROUTE1317)
ROUTE1318 = x3d.ROUTE()
ROUTE1318.fromField = "value_changed"
ROUTE1318.fromNode = "r_index1Relax"
ROUTE1318.toField = "set_rotation"
ROUTE1318.toNode = "Joe_r_index1"

Scene35.children.append(ROUTE1318)
ROUTE1319 = x3d.ROUTE()
ROUTE1319.fromField = "value_changed"
ROUTE1319.fromNode = "r_fingers2Relax"
ROUTE1319.toField = "set_rotation"
ROUTE1319.toNode = "Joe_r_index2"

Scene35.children.append(ROUTE1319)
ROUTE1320 = x3d.ROUTE()
ROUTE1320.fromField = "value_changed"
ROUTE1320.fromNode = "r_fingers3Relax"
ROUTE1320.toField = "set_rotation"
ROUTE1320.toNode = "Joe_r_index3"

Scene35.children.append(ROUTE1320)
ROUTE1321 = x3d.ROUTE()
ROUTE1321.fromField = "value_changed"
ROUTE1321.fromNode = "r_middle0Relax"
ROUTE1321.toField = "set_rotation"
ROUTE1321.toNode = "Joe_r_middle0"

Scene35.children.append(ROUTE1321)
ROUTE1322 = x3d.ROUTE()
ROUTE1322.fromField = "value_changed"
ROUTE1322.fromNode = "r_middle1Relax"
ROUTE1322.toField = "set_rotation"
ROUTE1322.toNode = "Joe_r_middle1"

Scene35.children.append(ROUTE1322)
ROUTE1323 = x3d.ROUTE()
ROUTE1323.fromField = "value_changed"
ROUTE1323.fromNode = "r_fingers2Relax"
ROUTE1323.toField = "set_rotation"
ROUTE1323.toNode = "Joe_r_middle2"

Scene35.children.append(ROUTE1323)
ROUTE1324 = x3d.ROUTE()
ROUTE1324.fromField = "value_changed"
ROUTE1324.fromNode = "r_fingers3Relax"
ROUTE1324.toField = "set_rotation"
ROUTE1324.toNode = "Joe_r_middle3"

Scene35.children.append(ROUTE1324)
ROUTE1325 = x3d.ROUTE()
ROUTE1325.fromField = "value_changed"
ROUTE1325.fromNode = "r_ring0Relax"
ROUTE1325.toField = "set_rotation"
ROUTE1325.toNode = "Joe_r_ring0"

Scene35.children.append(ROUTE1325)
ROUTE1326 = x3d.ROUTE()
ROUTE1326.fromField = "value_changed"
ROUTE1326.fromNode = "r_ring1Relax"
ROUTE1326.toField = "set_rotation"
ROUTE1326.toNode = "Joe_r_ring1"

Scene35.children.append(ROUTE1326)
ROUTE1327 = x3d.ROUTE()
ROUTE1327.fromField = "value_changed"
ROUTE1327.fromNode = "r_fingers2Relax"
ROUTE1327.toField = "set_rotation"
ROUTE1327.toNode = "Joe_r_ring2"

Scene35.children.append(ROUTE1327)
ROUTE1328 = x3d.ROUTE()
ROUTE1328.fromField = "value_changed"
ROUTE1328.fromNode = "r_fingers3Relax"
ROUTE1328.toField = "set_rotation"
ROUTE1328.toNode = "Joe_r_ring3"

Scene35.children.append(ROUTE1328)
ROUTE1329 = x3d.ROUTE()
ROUTE1329.fromField = "value_changed"
ROUTE1329.fromNode = "r_pinky0Relax"
ROUTE1329.toField = "set_rotation"
ROUTE1329.toNode = "Joe_r_pinky0"

Scene35.children.append(ROUTE1329)
ROUTE1330 = x3d.ROUTE()
ROUTE1330.fromField = "value_changed"
ROUTE1330.fromNode = "r_pinky1Relax"
ROUTE1330.toField = "set_rotation"
ROUTE1330.toNode = "Joe_r_pinky1"

Scene35.children.append(ROUTE1330)
ROUTE1331 = x3d.ROUTE()
ROUTE1331.fromField = "value_changed"
ROUTE1331.fromNode = "r_fingers2Relax"
ROUTE1331.toField = "set_rotation"
ROUTE1331.toNode = "Joe_r_pinky2"

Scene35.children.append(ROUTE1331)
ROUTE1332 = x3d.ROUTE()
ROUTE1332.fromField = "value_changed"
ROUTE1332.fromNode = "r_fingers3Relax"
ROUTE1332.toField = "set_rotation"
ROUTE1332.toNode = "Joe_r_pinky3"

Scene35.children.append(ROUTE1332)
OrientationInterpolator1333 = x3d.OrientationInterpolator()
OrientationInterpolator1333.DEF = "r_sternoclavicularRoll"
OrientationInterpolator1333.key = [0,0.20000000298023224,0.40000000596046448,0.5,0.69999998807907104,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1333)
OrientationInterpolator1334 = x3d.OrientationInterpolator()
OrientationInterpolator1334.DEF = "r_acromioclavicularRoll"
OrientationInterpolator1334.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1334)
OrientationInterpolator1335 = x3d.OrientationInterpolator()
OrientationInterpolator1335.DEF = "r_shoulderRoll"
OrientationInterpolator1335.key = [0,0.20000000298023224,0.40000000596046448,0.5,0.85000002384185791,1]

Scene35.children.append(OrientationInterpolator1335)
OrientationInterpolator1336 = x3d.OrientationInterpolator()
OrientationInterpolator1336.DEF = "r_ForeArmPitch"
OrientationInterpolator1336.key = [0,0.15000000596046448,0.30000001192092896,0.5,0.69999998807907104,0.89999997615814209,1]

Scene35.children.append(OrientationInterpolator1336)
OrientationInterpolator1337 = x3d.OrientationInterpolator()
OrientationInterpolator1337.DEF = "r_wristRoll"
OrientationInterpolator1337.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.64999997615814209,0.75,0.85000002384185791,1]

Scene35.children.append(OrientationInterpolator1337)
OrientationInterpolator1338 = x3d.OrientationInterpolator()
OrientationInterpolator1338.DEF = "r_handPitch"
OrientationInterpolator1338.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1338)
OrientationInterpolator1339 = x3d.OrientationInterpolator()
OrientationInterpolator1339.DEF = "r_thumb1Pitch"
OrientationInterpolator1339.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1339)
OrientationInterpolator1340 = x3d.OrientationInterpolator()
OrientationInterpolator1340.DEF = "r_thumb2Pitch"
OrientationInterpolator1340.key = [0,0.20000000298023224,0.40000000596046448,0.60000002384185791,0.80000001192092896,1]

Scene35.children.append(OrientationInterpolator1340)
OrientationInterpolator1341 = x3d.OrientationInterpolator()
OrientationInterpolator1341.DEF = "l_shoulderRoll"
OrientationInterpolator1341.key = [0,0.20000000298023224,0.40000000596046448,0.5,0.85000002384185791,1]

Scene35.children.append(OrientationInterpolator1341)
ROUTE1342 = x3d.ROUTE()
ROUTE1342.fromField = "fraction_changed"
ROUTE1342.fromNode = "Time2"
ROUTE1342.toField = "set_fraction"
ROUTE1342.toNode = "r_sternoclavicularRoll"

Scene35.children.append(ROUTE1342)
ROUTE1343 = x3d.ROUTE()
ROUTE1343.fromField = "fraction_changed"
ROUTE1343.fromNode = "Time2"
ROUTE1343.toField = "set_fraction"
ROUTE1343.toNode = "r_acromioclavicularRoll"

Scene35.children.append(ROUTE1343)
ROUTE1344 = x3d.ROUTE()
ROUTE1344.fromField = "fraction_changed"
ROUTE1344.fromNode = "Time2"
ROUTE1344.toField = "set_fraction"
ROUTE1344.toNode = "r_shoulderRoll"

Scene35.children.append(ROUTE1344)
ROUTE1345 = x3d.ROUTE()
ROUTE1345.fromField = "fraction_changed"
ROUTE1345.fromNode = "Time2"
ROUTE1345.toField = "set_fraction"
ROUTE1345.toNode = "r_ForeArmPitch"

Scene35.children.append(ROUTE1345)
ROUTE1346 = x3d.ROUTE()
ROUTE1346.fromField = "fraction_changed"
ROUTE1346.fromNode = "Time2"
ROUTE1346.toField = "set_fraction"
ROUTE1346.toNode = "r_wristRoll"

Scene35.children.append(ROUTE1346)
ROUTE1347 = x3d.ROUTE()
ROUTE1347.fromField = "fraction_changed"
ROUTE1347.fromNode = "Time2"
ROUTE1347.toField = "set_fraction"
ROUTE1347.toNode = "r_handPitch"

Scene35.children.append(ROUTE1347)
ROUTE1348 = x3d.ROUTE()
ROUTE1348.fromField = "fraction_changed"
ROUTE1348.fromNode = "Time2"
ROUTE1348.toField = "set_fraction"
ROUTE1348.toNode = "r_thumb1Pitch"

Scene35.children.append(ROUTE1348)
ROUTE1349 = x3d.ROUTE()
ROUTE1349.fromField = "fraction_changed"
ROUTE1349.fromNode = "Time2"
ROUTE1349.toField = "set_fraction"
ROUTE1349.toNode = "r_thumb2Pitch"

Scene35.children.append(ROUTE1349)
ROUTE1350 = x3d.ROUTE()
ROUTE1350.fromField = "value_changed"
ROUTE1350.fromNode = "r_sternoclavicularRoll"
ROUTE1350.toField = "set_rotation"
ROUTE1350.toNode = "Joe_r_sternoclavicular"

Scene35.children.append(ROUTE1350)
ROUTE1351 = x3d.ROUTE()
ROUTE1351.fromField = "value_changed"
ROUTE1351.fromNode = "r_acromioclavicularRoll"
ROUTE1351.toField = "set_rotation"
ROUTE1351.toNode = "Joe_r_acromioclavicular"

Scene35.children.append(ROUTE1351)
ROUTE1352 = x3d.ROUTE()
ROUTE1352.fromField = "value_changed"
ROUTE1352.fromNode = "r_shoulderRoll"
ROUTE1352.toField = "set_rotation"
ROUTE1352.toNode = "Joe_r_shoulder"

Scene35.children.append(ROUTE1352)
ROUTE1353 = x3d.ROUTE()
ROUTE1353.fromField = "value_changed"
ROUTE1353.fromNode = "r_ForeArmPitch"
ROUTE1353.toField = "set_rotation"
ROUTE1353.toNode = "Joe_r_elbow"

Scene35.children.append(ROUTE1353)
ROUTE1354 = x3d.ROUTE()
ROUTE1354.fromField = "value_changed"
ROUTE1354.fromNode = "r_wristRoll"
ROUTE1354.toField = "set_rotation"
ROUTE1354.toNode = "Joe_r_wrist"

Scene35.children.append(ROUTE1354)
ROUTE1355 = x3d.ROUTE()
ROUTE1355.fromField = "value_changed"
ROUTE1355.fromNode = "r_handPitch"
ROUTE1355.toField = "set_rotation"
ROUTE1355.toNode = "Joe_r_index0"

Scene35.children.append(ROUTE1355)
ROUTE1356 = x3d.ROUTE()
ROUTE1356.fromField = "value_changed"
ROUTE1356.fromNode = "r_handPitch"
ROUTE1356.toField = "set_rotation"
ROUTE1356.toNode = "Joe_r_index1"

Scene35.children.append(ROUTE1356)
ROUTE1357 = x3d.ROUTE()
ROUTE1357.fromField = "value_changed"
ROUTE1357.fromNode = "r_handPitch"
ROUTE1357.toField = "set_rotation"
ROUTE1357.toNode = "Joe_r_index2"

Scene35.children.append(ROUTE1357)
ROUTE1358 = x3d.ROUTE()
ROUTE1358.fromField = "value_changed"
ROUTE1358.fromNode = "r_handPitch"
ROUTE1358.toField = "set_rotation"
ROUTE1358.toNode = "Joe_r_index3"

Scene35.children.append(ROUTE1358)
ROUTE1359 = x3d.ROUTE()
ROUTE1359.fromField = "value_changed"
ROUTE1359.fromNode = "r_handPitch"
ROUTE1359.toField = "set_rotation"
ROUTE1359.toNode = "Joe_r_middle0"

Scene35.children.append(ROUTE1359)
ROUTE1360 = x3d.ROUTE()
ROUTE1360.fromField = "value_changed"
ROUTE1360.fromNode = "r_handPitch"
ROUTE1360.toField = "set_rotation"
ROUTE1360.toNode = "Joe_r_middle1"

Scene35.children.append(ROUTE1360)
ROUTE1361 = x3d.ROUTE()
ROUTE1361.fromField = "value_changed"
ROUTE1361.fromNode = "r_handPitch"
ROUTE1361.toField = "set_rotation"
ROUTE1361.toNode = "Joe_r_middle2"

Scene35.children.append(ROUTE1361)
ROUTE1362 = x3d.ROUTE()
ROUTE1362.fromField = "value_changed"
ROUTE1362.fromNode = "r_handPitch"
ROUTE1362.toField = "set_rotation"
ROUTE1362.toNode = "Joe_r_middle3"

Scene35.children.append(ROUTE1362)
ROUTE1363 = x3d.ROUTE()
ROUTE1363.fromField = "value_changed"
ROUTE1363.fromNode = "r_handPitch"
ROUTE1363.toField = "set_rotation"
ROUTE1363.toNode = "Joe_r_ring0"

Scene35.children.append(ROUTE1363)
ROUTE1364 = x3d.ROUTE()
ROUTE1364.fromField = "value_changed"
ROUTE1364.fromNode = "r_handPitch"
ROUTE1364.toField = "set_rotation"
ROUTE1364.toNode = "Joe_r_ring1"

Scene35.children.append(ROUTE1364)
ROUTE1365 = x3d.ROUTE()
ROUTE1365.fromField = "value_changed"
ROUTE1365.fromNode = "r_handPitch"
ROUTE1365.toField = "set_rotation"
ROUTE1365.toNode = "Joe_r_ring2"

Scene35.children.append(ROUTE1365)
ROUTE1366 = x3d.ROUTE()
ROUTE1366.fromField = "value_changed"
ROUTE1366.fromNode = "r_handPitch"
ROUTE1366.toField = "set_rotation"
ROUTE1366.toNode = "Joe_r_ring3"

Scene35.children.append(ROUTE1366)
ROUTE1367 = x3d.ROUTE()
ROUTE1367.fromField = "value_changed"
ROUTE1367.fromNode = "r_handPitch"
ROUTE1367.toField = "set_rotation"
ROUTE1367.toNode = "Joe_r_pinky0"

Scene35.children.append(ROUTE1367)
ROUTE1368 = x3d.ROUTE()
ROUTE1368.fromField = "value_changed"
ROUTE1368.fromNode = "r_handPitch"
ROUTE1368.toField = "set_rotation"
ROUTE1368.toNode = "Joe_r_pinky1"

Scene35.children.append(ROUTE1368)
ROUTE1369 = x3d.ROUTE()
ROUTE1369.fromField = "value_changed"
ROUTE1369.fromNode = "r_handPitch"
ROUTE1369.toField = "set_rotation"
ROUTE1369.toNode = "Joe_r_pinky2"

Scene35.children.append(ROUTE1369)
ROUTE1370 = x3d.ROUTE()
ROUTE1370.fromField = "value_changed"
ROUTE1370.fromNode = "r_handPitch"
ROUTE1370.toField = "set_rotation"
ROUTE1370.toNode = "Joe_r_pinky3"

Scene35.children.append(ROUTE1370)
ROUTE1371 = x3d.ROUTE()
ROUTE1371.fromField = "value_changed"
ROUTE1371.fromNode = "r_thumb1Pitch"
ROUTE1371.toField = "set_rotation"
ROUTE1371.toNode = "Joe_r_thumb1"

Scene35.children.append(ROUTE1371)
ROUTE1372 = x3d.ROUTE()
ROUTE1372.fromField = "value_changed"
ROUTE1372.fromNode = "r_thumb2Pitch"
ROUTE1372.toField = "set_rotation"
ROUTE1372.toNode = "Joe_r_thumb2"

Scene35.children.append(ROUTE1372)
ROUTE1373 = x3d.ROUTE()
ROUTE1373.fromField = "value_changed"
ROUTE1373.fromNode = "r_thumb2Pitch"
ROUTE1373.toField = "set_rotation"
ROUTE1373.toNode = "Joe_r_thumb3"

Scene35.children.append(ROUTE1373)
ROUTE1374 = x3d.ROUTE()
ROUTE1374.fromField = "value_changed"
ROUTE1374.fromNode = "l_shoulderRoll"
ROUTE1374.toField = "set_rotation"
ROUTE1374.toNode = "Joe_l_shoulder"

Scene35.children.append(ROUTE1374)
Group1375 = x3d.Group()
PositionInterpolator1376 = x3d.PositionInterpolator()
PositionInterpolator1376.DEF = "HUMANOIDROOT_POSITION_ANIMATOR"
PositionInterpolator1376.key = [0,0.041669998317956924,0.125,0.16670000553131104,0.20829999446868896,0.25,0.29170000553131104,0.375,0.45829999446868896,0.5,0.54170000553131104,0.58329999446868896,0.625,0.70829999446868896,0.75,0.79170000553131104,0.875,0.91670000553131104,1]

Group1375.children.append(PositionInterpolator1376)
OrientationInterpolator1377 = x3d.OrientationInterpolator()
OrientationInterpolator1377.DEF = "HUMANOIDROOT_ANIMATOR"
OrientationInterpolator1377.key = [0,1]

Group1375.children.append(OrientationInterpolator1377)
OrientationInterpolator1378 = x3d.OrientationInterpolator()
OrientationInterpolator1378.DEF = "L_HIP_ANIMATOR"
OrientationInterpolator1378.key = [0,0.25,0.375,0.5,0.66670000553131104,0.79170000553131104,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1378)
OrientationInterpolator1379 = x3d.OrientationInterpolator()
OrientationInterpolator1379.DEF = "L_KNEE_ANIMATOR"
OrientationInterpolator1379.key = [0,0.20829999446868896,0.375,0.5,0.66670000553131104,0.79170000553131104,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1379)
OrientationInterpolator1380 = x3d.OrientationInterpolator()
OrientationInterpolator1380.DEF = "L_ANKLE_ANIMATOR"
OrientationInterpolator1380.key = [0,0.125,0.20829999446868896,0.375,0.66670000553131104,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1380)
OrientationInterpolator1381 = x3d.OrientationInterpolator()
OrientationInterpolator1381.DEF = "R_ANKLE_ANIMATOR"
OrientationInterpolator1381.key = [0,0.125,0.20829999446868896,0.375,0.45829999446868896,0.5,0.66670000553131104,0.75,0.77999997138977051,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1381)
OrientationInterpolator1382 = x3d.OrientationInterpolator()
OrientationInterpolator1382.DEF = "L_subtalar_ANIMATOR"
OrientationInterpolator1382.key = [0,0.30000001192092896,1]

Group1375.children.append(OrientationInterpolator1382)
OrientationInterpolator1383 = x3d.OrientationInterpolator()
OrientationInterpolator1383.DEF = "L_MIDTARSAL_ANIMATOR"
OrientationInterpolator1383.key = [0,0.5,1]

Group1375.children.append(OrientationInterpolator1383)
OrientationInterpolator1384 = x3d.OrientationInterpolator()
OrientationInterpolator1384.DEF = "L_metatarsal_ANIMATOR"
OrientationInterpolator1384.key = [0,0.20000000298023224,0.40000000596046448,0.80000001192092896,1]

Group1375.children.append(OrientationInterpolator1384)
OrientationInterpolator1385 = x3d.OrientationInterpolator()
OrientationInterpolator1385.DEF = "R_HIP_ANIMATOR"
OrientationInterpolator1385.key = [0,0.125,0.20829999446868896,0.29170000553131104,0.375,0.5,0.66670000553131104,0.79170000553131104,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1385)
OrientationInterpolator1386 = x3d.OrientationInterpolator()
OrientationInterpolator1386.DEF = "R_KNEE_ANIMATOR"
OrientationInterpolator1386.key = [0,0.125,0.20829999446868896,0.29170000553131104,0.375,0.5,0.66670000553131104,0.79170000553131104,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1386)
OrientationInterpolator1387 = x3d.OrientationInterpolator()
OrientationInterpolator1387.DEF = "R_subtalar_ANIMATOR"
OrientationInterpolator1387.key = [0,0.225,0.25,0.35,0.45,0.85,0.91]

Group1375.children.append(OrientationInterpolator1387)
OrientationInterpolator1388 = x3d.OrientationInterpolator()
OrientationInterpolator1388.DEF = "R_MIDTARSAL_ANIMATOR"
OrientationInterpolator1388.key = [0,0.2199999988079071,1]

Group1375.children.append(OrientationInterpolator1388)
OrientationInterpolator1389 = x3d.OrientationInterpolator()
OrientationInterpolator1389.DEF = "R_metatarsal_ANIMATOR"
OrientationInterpolator1389.key = [0,0.20000000298023224,0.40000000596046448,0.80000001192092896,1]

Group1375.children.append(OrientationInterpolator1389)
OrientationInterpolator1390 = x3d.OrientationInterpolator()
OrientationInterpolator1390.DEF = "VL5_ANIMATOR"
OrientationInterpolator1390.key = [0,0.20829999446868896,0.375,0.75,0.83329999446868896,1]

Group1375.children.append(OrientationInterpolator1390)
OrientationInterpolator1391 = x3d.OrientationInterpolator()
OrientationInterpolator1391.DEF = "SKULLBASE_ANIMATOR"
OrientationInterpolator1391.key = [0,0.375,0.41670000553131104,0.5,0.58329999446868896,0.66670000553131104,0.75,0.83329999446868896,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1391)
OrientationInterpolator1392 = x3d.OrientationInterpolator()
OrientationInterpolator1392.DEF = "L_SHOULDER_ANIMATOR"
OrientationInterpolator1392.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1392)
OrientationInterpolator1393 = x3d.OrientationInterpolator()
OrientationInterpolator1393.DEF = "L_ELBOW_ANIMATOR"
OrientationInterpolator1393.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1393)
OrientationInterpolator1394 = x3d.OrientationInterpolator()
OrientationInterpolator1394.DEF = "L_WRIST_ANIMATOR"
OrientationInterpolator1394.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1394)
OrientationInterpolator1395 = x3d.OrientationInterpolator()
OrientationInterpolator1395.DEF = "R_SHOULDER_ANIMATOR"
OrientationInterpolator1395.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1395)
OrientationInterpolator1396 = x3d.OrientationInterpolator()
OrientationInterpolator1396.DEF = "R_ELBOW_ANIMATOR"
OrientationInterpolator1396.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1396)
OrientationInterpolator1397 = x3d.OrientationInterpolator()
OrientationInterpolator1397.DEF = "R_WRIST_ANIMATOR"
OrientationInterpolator1397.key = [0,0.375,0.91670000553131104,1]

Group1375.children.append(OrientationInterpolator1397)

Scene35.children.append(Group1375)
ROUTE1398 = x3d.ROUTE()
ROUTE1398.fromField = "fraction_changed"
ROUTE1398.fromNode = "Time1"
ROUTE1398.toField = "set_fraction"
ROUTE1398.toNode = "HUMANOIDROOT_POSITION_ANIMATOR"

Scene35.children.append(ROUTE1398)
ROUTE1399 = x3d.ROUTE()
ROUTE1399.fromField = "fraction_changed"
ROUTE1399.fromNode = "Time1"
ROUTE1399.toField = "set_fraction"
ROUTE1399.toNode = "HUMANOIDROOT_ANIMATOR"

Scene35.children.append(ROUTE1399)
ROUTE1400 = x3d.ROUTE()
ROUTE1400.fromField = "fraction_changed"
ROUTE1400.fromNode = "Time1"
ROUTE1400.toField = "set_fraction"
ROUTE1400.toNode = "L_HIP_ANIMATOR"

Scene35.children.append(ROUTE1400)
ROUTE1401 = x3d.ROUTE()
ROUTE1401.fromField = "fraction_changed"
ROUTE1401.fromNode = "Time1"
ROUTE1401.toField = "set_fraction"
ROUTE1401.toNode = "L_KNEE_ANIMATOR"

Scene35.children.append(ROUTE1401)
ROUTE1402 = x3d.ROUTE()
ROUTE1402.fromField = "fraction_changed"
ROUTE1402.fromNode = "Time1"
ROUTE1402.toField = "set_fraction"
ROUTE1402.toNode = "L_ANKLE_ANIMATOR"

Scene35.children.append(ROUTE1402)
ROUTE1403 = x3d.ROUTE()
ROUTE1403.fromField = "fraction_changed"
ROUTE1403.fromNode = "Time1"
ROUTE1403.toField = "set_fraction"
ROUTE1403.toNode = "L_subtalar_ANIMATOR"

Scene35.children.append(ROUTE1403)
ROUTE1404 = x3d.ROUTE()
ROUTE1404.fromField = "fraction_changed"
ROUTE1404.fromNode = "Time1"
ROUTE1404.toField = "set_fraction"
ROUTE1404.toNode = "L_MIDTARSAL_ANIMATOR"

Scene35.children.append(ROUTE1404)
ROUTE1405 = x3d.ROUTE()
ROUTE1405.fromField = "fraction_changed"
ROUTE1405.fromNode = "Time1"
ROUTE1405.toField = "set_fraction"
ROUTE1405.toNode = "L_metatarsal_ANIMATOR"

Scene35.children.append(ROUTE1405)
ROUTE1406 = x3d.ROUTE()
ROUTE1406.fromField = "fraction_changed"
ROUTE1406.fromNode = "Time1"
ROUTE1406.toField = "set_fraction"
ROUTE1406.toNode = "R_HIP_ANIMATOR"

Scene35.children.append(ROUTE1406)
ROUTE1407 = x3d.ROUTE()
ROUTE1407.fromField = "fraction_changed"
ROUTE1407.fromNode = "Time1"
ROUTE1407.toField = "set_fraction"
ROUTE1407.toNode = "R_KNEE_ANIMATOR"

Scene35.children.append(ROUTE1407)
ROUTE1408 = x3d.ROUTE()
ROUTE1408.fromField = "fraction_changed"
ROUTE1408.fromNode = "Time1"
ROUTE1408.toField = "set_fraction"
ROUTE1408.toNode = "R_ANKLE_ANIMATOR"

Scene35.children.append(ROUTE1408)
ROUTE1409 = x3d.ROUTE()
ROUTE1409.fromField = "fraction_changed"
ROUTE1409.fromNode = "Time1"
ROUTE1409.toField = "set_fraction"
ROUTE1409.toNode = "R_subtalar_ANIMATOR"

Scene35.children.append(ROUTE1409)
ROUTE1410 = x3d.ROUTE()
ROUTE1410.fromField = "fraction_changed"
ROUTE1410.fromNode = "Time1"
ROUTE1410.toField = "set_fraction"
ROUTE1410.toNode = "R_MIDTARSAL_ANIMATOR"

Scene35.children.append(ROUTE1410)
ROUTE1411 = x3d.ROUTE()
ROUTE1411.fromField = "fraction_changed"
ROUTE1411.fromNode = "Time1"
ROUTE1411.toField = "set_fraction"
ROUTE1411.toNode = "R_metatarsal_ANIMATOR"

Scene35.children.append(ROUTE1411)
ROUTE1412 = x3d.ROUTE()
ROUTE1412.fromField = "fraction_changed"
ROUTE1412.fromNode = "Time1"
ROUTE1412.toField = "set_fraction"
ROUTE1412.toNode = "VL5_ANIMATOR"

Scene35.children.append(ROUTE1412)
ROUTE1413 = x3d.ROUTE()
ROUTE1413.fromField = "fraction_changed"
ROUTE1413.fromNode = "Time1"
ROUTE1413.toField = "set_fraction"
ROUTE1413.toNode = "SKULLBASE_ANIMATOR"

Scene35.children.append(ROUTE1413)
ROUTE1414 = x3d.ROUTE()
ROUTE1414.fromField = "fraction_changed"
ROUTE1414.fromNode = "Time1"
ROUTE1414.toField = "set_fraction"
ROUTE1414.toNode = "L_SHOULDER_ANIMATOR"

Scene35.children.append(ROUTE1414)
ROUTE1415 = x3d.ROUTE()
ROUTE1415.fromField = "fraction_changed"
ROUTE1415.fromNode = "Time1"
ROUTE1415.toField = "set_fraction"
ROUTE1415.toNode = "L_ELBOW_ANIMATOR"

Scene35.children.append(ROUTE1415)
ROUTE1416 = x3d.ROUTE()
ROUTE1416.fromField = "fraction_changed"
ROUTE1416.fromNode = "Time1"
ROUTE1416.toField = "set_fraction"
ROUTE1416.toNode = "L_WRIST_ANIMATOR"

Scene35.children.append(ROUTE1416)
ROUTE1417 = x3d.ROUTE()
ROUTE1417.fromField = "value_changed"
ROUTE1417.fromNode = "HUMANOIDROOT_POSITION_ANIMATOR"
ROUTE1417.toField = "set_translation"
ROUTE1417.toNode = "Joe_HumanoidRoot"

Scene35.children.append(ROUTE1417)
ROUTE1418 = x3d.ROUTE()
ROUTE1418.fromField = "value_changed"
ROUTE1418.fromNode = "HUMANOIDROOT_ANIMATOR"
ROUTE1418.toField = "set_rotation"
ROUTE1418.toNode = "Joe_HumanoidRoot"

Scene35.children.append(ROUTE1418)
ROUTE1419 = x3d.ROUTE()
ROUTE1419.fromField = "value_changed"
ROUTE1419.fromNode = "L_HIP_ANIMATOR"
ROUTE1419.toField = "set_rotation"
ROUTE1419.toNode = "Joe_l_hip"

Scene35.children.append(ROUTE1419)
ROUTE1420 = x3d.ROUTE()
ROUTE1420.fromField = "value_changed"
ROUTE1420.fromNode = "L_KNEE_ANIMATOR"
ROUTE1420.toField = "set_rotation"
ROUTE1420.toNode = "Joe_l_knee"

Scene35.children.append(ROUTE1420)
ROUTE1421 = x3d.ROUTE()
ROUTE1421.fromField = "value_changed"
ROUTE1421.fromNode = "L_ANKLE_ANIMATOR"
ROUTE1421.toField = "set_rotation"
ROUTE1421.toNode = "Joe_l_ankle"

Scene35.children.append(ROUTE1421)
ROUTE1422 = x3d.ROUTE()
ROUTE1422.fromField = "value_changed"
ROUTE1422.fromNode = "L_MIDTARSAL_ANIMATOR"
ROUTE1422.toField = "set_rotation"
ROUTE1422.toNode = "Joe_l_midtarsal"

Scene35.children.append(ROUTE1422)
ROUTE1423 = x3d.ROUTE()
ROUTE1423.fromField = "value_changed"
ROUTE1423.fromNode = "L_subtalar_ANIMATOR"
ROUTE1423.toField = "set_rotation"
ROUTE1423.toNode = "Joe_l_subtalar"

Scene35.children.append(ROUTE1423)
ROUTE1424 = x3d.ROUTE()
ROUTE1424.fromField = "value_changed"
ROUTE1424.fromNode = "L_metatarsal_ANIMATOR"
ROUTE1424.toField = "set_rotation"
ROUTE1424.toNode = "Joe_l_metatarsal"

Scene35.children.append(ROUTE1424)
ROUTE1425 = x3d.ROUTE()
ROUTE1425.fromField = "value_changed"
ROUTE1425.fromNode = "R_HIP_ANIMATOR"
ROUTE1425.toField = "set_rotation"
ROUTE1425.toNode = "Joe_r_hip"

Scene35.children.append(ROUTE1425)
ROUTE1426 = x3d.ROUTE()
ROUTE1426.fromField = "value_changed"
ROUTE1426.fromNode = "R_KNEE_ANIMATOR"
ROUTE1426.toField = "set_rotation"
ROUTE1426.toNode = "Joe_r_knee"

Scene35.children.append(ROUTE1426)
ROUTE1427 = x3d.ROUTE()
ROUTE1427.fromField = "value_changed"
ROUTE1427.fromNode = "R_ANKLE_ANIMATOR"
ROUTE1427.toField = "set_rotation"
ROUTE1427.toNode = "Joe_r_ankle"

Scene35.children.append(ROUTE1427)
ROUTE1428 = x3d.ROUTE()
ROUTE1428.fromField = "value_changed"
ROUTE1428.fromNode = "R_subtalar_ANIMATOR"
ROUTE1428.toField = "set_rotation"
ROUTE1428.toNode = "Joe_r_subtalar"

Scene35.children.append(ROUTE1428)
ROUTE1429 = x3d.ROUTE()
ROUTE1429.fromField = "value_changed"
ROUTE1429.fromNode = "R_MIDTARSAL_ANIMATOR"
ROUTE1429.toField = "set_rotation"
ROUTE1429.toNode = "Joe_r_midtarsal"

Scene35.children.append(ROUTE1429)
ROUTE1430 = x3d.ROUTE()
ROUTE1430.fromField = "value_changed"
ROUTE1430.fromNode = "R_metatarsal_ANIMATOR"
ROUTE1430.toField = "set_rotation"
ROUTE1430.toNode = "Joe_r_metatarsal"

Scene35.children.append(ROUTE1430)
ROUTE1431 = x3d.ROUTE()
ROUTE1431.fromField = "value_changed"
ROUTE1431.fromNode = "VL5_ANIMATOR"
ROUTE1431.toField = "set_rotation"
ROUTE1431.toNode = "Joe_vl5"

Scene35.children.append(ROUTE1431)
ROUTE1432 = x3d.ROUTE()
ROUTE1432.fromField = "value_changed"
ROUTE1432.fromNode = "SKULLBASE_ANIMATOR"
ROUTE1432.toField = "set_rotation"
ROUTE1432.toNode = "Joe_skullbase"

Scene35.children.append(ROUTE1432)
ROUTE1433 = x3d.ROUTE()
ROUTE1433.fromField = "value_changed"
ROUTE1433.fromNode = "L_SHOULDER_ANIMATOR"
ROUTE1433.toField = "set_rotation"
ROUTE1433.toNode = "Joe_l_shoulder"

Scene35.children.append(ROUTE1433)
ROUTE1434 = x3d.ROUTE()
ROUTE1434.fromField = "value_changed"
ROUTE1434.fromNode = "L_ELBOW_ANIMATOR"
ROUTE1434.toField = "set_rotation"
ROUTE1434.toNode = "Joe_l_elbow"

Scene35.children.append(ROUTE1434)
ROUTE1435 = x3d.ROUTE()
ROUTE1435.fromField = "value_changed"
ROUTE1435.fromNode = "L_WRIST_ANIMATOR"
ROUTE1435.toField = "set_rotation"
ROUTE1435.toNode = "Joe_l_wrist"

Scene35.children.append(ROUTE1435)
ROUTE1436 = x3d.ROUTE()
ROUTE1436.fromField = "value_changed"
ROUTE1436.fromNode = "R_SHOULDER_ANIMATOR"
ROUTE1436.toField = "set_rotation"
ROUTE1436.toNode = "Joe_r_shoulder"

Scene35.children.append(ROUTE1436)
ROUTE1437 = x3d.ROUTE()
ROUTE1437.fromField = "value_changed"
ROUTE1437.fromNode = "R_ELBOW_ANIMATOR"
ROUTE1437.toField = "set_rotation"
ROUTE1437.toNode = "Joe_r_elbow"

Scene35.children.append(ROUTE1437)
ROUTE1438 = x3d.ROUTE()
ROUTE1438.fromField = "value_changed"
ROUTE1438.fromNode = "R_WRIST_ANIMATOR"
ROUTE1438.toField = "set_rotation"
ROUTE1438.toNode = "Joe_r_wrist"

Scene35.children.append(ROUTE1438)

X3D0.Scene = Scene35
f = open("JoeSkeletonSkinSiteSaluteWalk_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
