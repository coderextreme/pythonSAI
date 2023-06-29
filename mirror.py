print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "EnvironmentalEffects"
component2.level = 3

head1.children.append(component2)
component3 = x3d.component()
component3.name = "Shaders"
component3.level = 1

head1.children.append(component3)
component4 = x3d.component()
component4.name = "CubeMapTexturing"
component4.level = 1

head1.children.append(component4)
component5 = x3d.component()
component5.name = "Texturing"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Rendering"
component6.level = 1

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Shape"
component7.level = 1

head1.children.append(component7)
component8 = x3d.component()
component8.name = "Grouping"
component8.level = 1

head1.children.append(component8)
meta9 = x3d.meta()
meta9.name = "title"
meta9.content = "mirror.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "creator"
meta10.content = "John Carlson"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "generator"
meta11.content = "manual"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://coderextreme.net/X3DJSONLD/mirror.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "description"
meta13.content = "sphere with alternating backgrounds"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
Viewpoint15 = x3d.Viewpoint()
Viewpoint15.position = [0,5,100]
Viewpoint15.description = "Switch background and images texture"

Scene14.children.append(Viewpoint15)
TextureBackground16 = x3d.TextureBackground()
ImageTexture17 = x3d.ImageTexture()
ImageTexture17.DEF = "leftBackgroundTexture"
ImageTexture17.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_left.png"]

TextureBackground16.leftTexture = ImageTexture17
ImageTexture18 = x3d.ImageTexture()
ImageTexture18.DEF = "rightBackgroundTexture"
ImageTexture18.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_right.png"]

TextureBackground16.rightTexture.append(ImageTexture18)
ImageTexture19 = x3d.ImageTexture()
ImageTexture19.DEF = "frontBackgroundTexture"
ImageTexture19.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_front.png"]

TextureBackground16.frontTexture.append(ImageTexture19)
ImageTexture20 = x3d.ImageTexture()
ImageTexture20.DEF = "backBackgroundTexture"
ImageTexture20.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_back.png"]

TextureBackground16.backTexture = ImageTexture20
ImageTexture21 = x3d.ImageTexture()
ImageTexture21.DEF = "topBackgroundTexture"
ImageTexture21.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_top.png"]

TextureBackground16.topTexture.append(ImageTexture21)
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.DEF = "bottomBackgroundTexture"
ImageTexture22.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_bottom.png"]

TextureBackground16.bottomTexture = ImageTexture22

Scene14.children.append(TextureBackground16)
Transform23 = x3d.Transform()
Shape24 = x3d.Shape()
Appearance25 = x3d.Appearance()
Material26 = x3d.Material()
Material26.diffuseColor = [0.7,0.7,0.7]
Material26.specularColor = [0.5,0.5,0.5]

Appearance25.material = Material26
ComposedCubeMapTexture27 = x3d.ComposedCubeMapTexture()
ImageTexture28 = x3d.ImageTexture()
ImageTexture28.DEF = "backShader"
ImageTexture28.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_back.png"]

ComposedCubeMapTexture27.backTexture = ImageTexture28
ImageTexture29 = x3d.ImageTexture()
ImageTexture29.DEF = "bottomShader"
ImageTexture29.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_bottom.png"]

ComposedCubeMapTexture27.bottomTexture = ImageTexture29
ImageTexture30 = x3d.ImageTexture()
ImageTexture30.DEF = "frontShader"
ImageTexture30.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_front.png"]

ComposedCubeMapTexture27.frontTexture.append(ImageTexture30)
ImageTexture31 = x3d.ImageTexture()
ImageTexture31.DEF = "leftShader"
ImageTexture31.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_left.png"]

ComposedCubeMapTexture27.leftTexture = ImageTexture31
ImageTexture32 = x3d.ImageTexture()
ImageTexture32.DEF = "rightShader"
ImageTexture32.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_right.png"]

ComposedCubeMapTexture27.rightTexture.append(ImageTexture32)
ImageTexture33 = x3d.ImageTexture()
ImageTexture33.DEF = "topShader"
ImageTexture33.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/src/main/resources/images/all_probes/beach_cross/beach_top.png"]

ComposedCubeMapTexture27.topTexture.append(ImageTexture33)

Appearance25.texture = ComposedCubeMapTexture27
ComposedShader34 = x3d.ComposedShader()
ComposedShader34.DEF = "x3dom"
ComposedShader34.language = "GLSL"
field35 = x3d.field()
field35.name = "chromaticDispertion"
field35.accessType = "inputOutput"
field35.type = "SFVec3f"
field35.value = [0.98,1,1.033]

ComposedShader34.field.append(field35)
field36 = x3d.field()
field36.name = "cube"
field36.accessType = "inputOutput"
field36.type = "SFInt32"
field36.value = 0

ComposedShader34.field.append(field36)
field37 = x3d.field()
field37.name = "bias"
field37.accessType = "inputOutput"
field37.type = "SFFloat"
field37.value = 0.5

ComposedShader34.field.append(field37)
field38 = x3d.field()
field38.name = "scale"
field38.accessType = "inputOutput"
field38.type = "SFFloat"
field38.value = 0.5

ComposedShader34.field.append(field38)
field39 = x3d.field()
field39.name = "power"
field39.accessType = "inputOutput"
field39.type = "SFFloat"
field39.value = 2

ComposedShader34.field.append(field39)
ShaderPart40 = x3d.ShaderPart()
ShaderPart40.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart40.type = "VERTEX"

ComposedShader34.parts.append(ShaderPart40)
ShaderPart41 = x3d.ShaderPart()
ShaderPart41.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/mix.fs"]
ShaderPart41.type = "FRAGMENT"

ComposedShader34.parts.append(ShaderPart41)

Appearance25.shaders.append(ComposedShader34)
ComposedShader42 = x3d.ComposedShader()
ComposedShader42.DEF = "x_ite"
ComposedShader42.language = "GLSL"
#http://hypertextbook.com/facts/2005/JustinChe.shtml
field43 = x3d.field()
field43.name = "chromaticDispertion"
field43.accessType = "inputOutput"
field43.type = "SFVec3f"
field43.value = [0.98,1,1.033]

ComposedShader42.field.append(field43)
field44 = x3d.field()
field44.name = "cube"
field44.accessType = "inputOutput"
field44.type = "SFInt32"
field44.value = 0

ComposedShader42.field.append(field44)
field45 = x3d.field()
field45.name = "bias"
field45.accessType = "inputOutput"
field45.type = "SFFloat"
field45.value = 0.5

ComposedShader42.field.append(field45)
field46 = x3d.field()
field46.name = "scale"
field46.accessType = "inputOutput"
field46.type = "SFFloat"
field46.value = 0.5

ComposedShader42.field.append(field46)
field47 = x3d.field()
field47.name = "power"
field47.accessType = "inputOutput"
field47.type = "SFFloat"
field47.value = 2

ComposedShader42.field.append(field47)
ShaderPart48 = x3d.ShaderPart()
ShaderPart48.url = ["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"]
ShaderPart48.type = "VERTEX"

ComposedShader42.parts.append(ShaderPart48)
ShaderPart49 = x3d.ShaderPart()
ShaderPart49.url = ["../shaders/x_itemix.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_itemix.fs"]
ShaderPart49.type = "FRAGMENT"

ComposedShader42.parts.append(ShaderPart49)

Appearance25.shaders.append(ComposedShader42)

Shape24.appearance = Appearance25
Sphere50 = x3d.Sphere()
Sphere50.radius = 30

Shape24.geometry = Sphere50

Transform23.children.append(Shape24)
Script51 = x3d.Script()
Script51.DEF = "UrlSelector"
Script51.directOutput = True
field52 = x3d.field()
field52.name = "frontUrls"
field52.type = "MFString"
field52.accessType = "initializeOnly"
field52.value = ["../resources/images/all_probes/beach_cross/beach_front.png","../resources/images/all_probes/building_cross/building_front.png","../resources/images/all_probes/campus_cross/campus_front.png","../resources/images/all_probes/galileo_cross/galileo_front.png","../resources/images/all_probes/grace_cross/grace_front.png","../resources/images/all_probes/kitchen_cross/kitchen_front.png","../resources/images/all_probes/rnl_cross/rnl_front.png","../resources/images/all_probes/stpeters_cross/stpeters_front.png","../resources/images/all_probes/uffizi_cross/uffizi_front.png"]

Script51.field.append(field52)
field53 = x3d.field()
field53.name = "backUrls"
field53.type = "MFString"
field53.accessType = "initializeOnly"
field53.value = ["../resources/images/all_probes/beach_cross/beach_back.png","../resources/images/all_probes/building_cross/building_back.png","../resources/images/all_probes/campus_cross/campus_back.png","../resources/images/all_probes/galileo_cross/galileo_back.png","../resources/images/all_probes/grace_cross/grace_back.png","../resources/images/all_probes/kitchen_cross/kitchen_back.png","../resources/images/all_probes/rnl_cross/rnl_back.png","../resources/images/all_probes/stpeters_cross/stpeters_back.png","../resources/images/all_probes/uffizi_cross/uffizi_back.png"]

Script51.field.append(field53)
field54 = x3d.field()
field54.name = "leftUrls"
field54.type = "MFString"
field54.accessType = "initializeOnly"
field54.value = ["../resources/images/all_probes/beach_cross/beach_left.png","../resources/images/all_probes/building_cross/building_left.png","../resources/images/all_probes/campus_cross/campus_left.png","../resources/images/all_probes/galileo_cross/galileo_left.png","../resources/images/all_probes/grace_cross/grace_left.png","../resources/images/all_probes/kitchen_cross/kitchen_left.png","../resources/images/all_probes/rnl_cross/rnl_left.png","../resources/images/all_probes/stpeters_cross/stpeters_left.png","../resources/images/all_probes/uffizi_cross/uffizi_left.png"]

Script51.field.append(field54)
field55 = x3d.field()
field55.name = "rightUrls"
field55.type = "MFString"
field55.accessType = "initializeOnly"
field55.value = ["../resources/images/all_probes/beach_cross/beach_right.png","../resources/images/all_probes/building_cross/building_right.png","../resources/images/all_probes/campus_cross/campus_right.png","../resources/images/all_probes/galileo_cross/galileo_right.png","../resources/images/all_probes/grace_cross/grace_right.png","../resources/images/all_probes/kitchen_cross/kitchen_right.png","../resources/images/all_probes/rnl_cross/rnl_right.png","../resources/images/all_probes/stpeters_cross/stpeters_right.png","../resources/images/all_probes/uffizi_cross/uffizi_right.png"]

Script51.field.append(field55)
field56 = x3d.field()
field56.name = "topUrls"
field56.type = "MFString"
field56.accessType = "initializeOnly"
field56.value = ["../resources/images/all_probes/beach_cross/beach_top.png","../resources/images/all_probes/building_cross/building_top.png","../resources/images/all_probes/campus_cross/campus_top.png","../resources/images/all_probes/galileo_cross/galileo_top.png","../resources/images/all_probes/grace_cross/grace_top.png","../resources/images/all_probes/kitchen_cross/kitchen_top.png","../resources/images/all_probes/rnl_cross/rnl_top.png","../resources/images/all_probes/stpeters_cross/stpeters_top.png","../resources/images/all_probes/uffizi_cross/uffizi_top.png"]

Script51.field.append(field56)
field57 = x3d.field()
field57.name = "bottomUrls"
field57.type = "MFString"
field57.accessType = "initializeOnly"
field57.value = ["../resources/images/all_probes/beach_cross/beach_bottom.png","../resources/images/all_probes/building_cross/building_bottom.png","../resources/images/all_probes/campus_cross/campus_bottom.png","../resources/images/all_probes/galileo_cross/galileo_bottom.png","../resources/images/all_probes/grace_cross/grace_bottom.png","../resources/images/all_probes/kitchen_cross/kitchen_bottom.png","../resources/images/all_probes/rnl_cross/rnl_bottom.png","../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","../resources/images/all_probes/uffizi_cross/uffizi_bottom.png"]

Script51.field.append(field57)
field58 = x3d.field()
field58.name = "front_changed"
field58.type = "MFString"
field58.accessType = "outputOnly"

Script51.field.append(field58)
field59 = x3d.field()
field59.name = "back_changed"
field59.type = "MFString"
field59.accessType = "outputOnly"

Script51.field.append(field59)
field60 = x3d.field()
field60.name = "left_changed"
field60.type = "MFString"
field60.accessType = "outputOnly"

Script51.field.append(field60)
field61 = x3d.field()
field61.name = "right_changed"
field61.type = "MFString"
field61.accessType = "outputOnly"

Script51.field.append(field61)
field62 = x3d.field()
field62.name = "top_changed"
field62.type = "MFString"
field62.accessType = "outputOnly"

Script51.field.append(field62)
field63 = x3d.field()
field63.name = "bottom_changed"
field63.type = "MFString"
field63.accessType = "outputOnly"

Script51.field.append(field63)
field64 = x3d.field()
field64.name = "set_fraction"
field64.type = "SFFloat"
field64.accessType = "inputOnly"

Script51.field.append(field64)
field65 = x3d.field()
field65.name = "old"
field65.type = "SFInt32"
field65.accessType = "inputOutput"
field65.value = -1

Script51.field.append(field65)

Script51.sourceCode = '''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }'''

Transform23.children.append(Script51)
TimeSensor66 = x3d.TimeSensor()
TimeSensor66.DEF = "Clock"
TimeSensor66.cycleInterval = 45
TimeSensor66.loop = True

Transform23.children.append(TimeSensor66)
ROUTE67 = x3d.ROUTE()
ROUTE67.fromNode = "Clock"
ROUTE67.fromField = "fraction_changed"
ROUTE67.toNode = "UrlSelector"
ROUTE67.toField = "set_fraction"

Transform23.children.append(ROUTE67)
ROUTE68 = x3d.ROUTE()
ROUTE68.fromNode = "UrlSelector"
ROUTE68.fromField = "front_changed"
ROUTE68.toNode = "frontBackgroundTexture"
ROUTE68.toField = "url"

Transform23.children.append(ROUTE68)
ROUTE69 = x3d.ROUTE()
ROUTE69.fromNode = "UrlSelector"
ROUTE69.fromField = "back_changed"
ROUTE69.toNode = "backBackgroundTexture"
ROUTE69.toField = "url"

Transform23.children.append(ROUTE69)
ROUTE70 = x3d.ROUTE()
ROUTE70.fromNode = "UrlSelector"
ROUTE70.fromField = "left_changed"
ROUTE70.toNode = "leftBackgroundTexture"
ROUTE70.toField = "url"

Transform23.children.append(ROUTE70)
ROUTE71 = x3d.ROUTE()
ROUTE71.fromNode = "UrlSelector"
ROUTE71.fromField = "right_changed"
ROUTE71.toNode = "rightBackgroundTexture"
ROUTE71.toField = "url"

Transform23.children.append(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromNode = "UrlSelector"
ROUTE72.fromField = "top_changed"
ROUTE72.toNode = "topBackgroundTexture"
ROUTE72.toField = "url"

Transform23.children.append(ROUTE72)
ROUTE73 = x3d.ROUTE()
ROUTE73.fromNode = "UrlSelector"
ROUTE73.fromField = "bottom_changed"
ROUTE73.toNode = "bottomBackgroundTexture"
ROUTE73.toField = "url"

Transform23.children.append(ROUTE73)
ROUTE74 = x3d.ROUTE()
ROUTE74.fromNode = "UrlSelector"
ROUTE74.fromField = "front_changed"
ROUTE74.toNode = "frontShader"
ROUTE74.toField = "url"

Transform23.children.append(ROUTE74)
ROUTE75 = x3d.ROUTE()
ROUTE75.fromNode = "UrlSelector"
ROUTE75.fromField = "back_changed"
ROUTE75.toNode = "backShader"
ROUTE75.toField = "url"

Transform23.children.append(ROUTE75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromNode = "UrlSelector"
ROUTE76.fromField = "left_changed"
ROUTE76.toNode = "leftShader"
ROUTE76.toField = "url"

Transform23.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromNode = "UrlSelector"
ROUTE77.fromField = "right_changed"
ROUTE77.toNode = "rightShader"
ROUTE77.toField = "url"

Transform23.children.append(ROUTE77)
ROUTE78 = x3d.ROUTE()
ROUTE78.fromNode = "UrlSelector"
ROUTE78.fromField = "top_changed"
ROUTE78.toNode = "topShader"
ROUTE78.toField = "url"

Transform23.children.append(ROUTE78)
ROUTE79 = x3d.ROUTE()
ROUTE79.fromNode = "UrlSelector"
ROUTE79.fromField = "bottom_changed"
ROUTE79.toNode = "bottomShader"
ROUTE79.toField = "url"

Transform23.children.append(ROUTE79)

Scene14.children.append(Transform23)

X3D0.Scene = Scene14
f = open("././mirror_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
