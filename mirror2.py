print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Shaders"
component2.level = 1

head1.children.append(component2)
component3 = x3d.component()
component3.name = "CubeMapTexturing"
component3.level = 1

head1.children.append(component3)
component4 = x3d.component()
component4.name = "Texturing"
component4.level = 1

head1.children.append(component4)
component5 = x3d.component()
component5.name = "Rendering"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Shape"
component6.level = 4

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Grouping"
component7.level = 3

head1.children.append(component7)
meta8 = x3d.meta()
meta8.name = "title"
meta8.content = "mirror2.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "creator"
meta9.content = "John Carlson"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "generator"
meta10.content = "manual"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "https://coderextreme.net/X3DJSONLD/src/main/data/mirror2.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "description"
meta12.content = "a mirrored sphere"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
Viewpoint14 = x3d.Viewpoint()
Viewpoint14.position = [0,5,100]
Viewpoint14.description = "Switch background and images texture"

Scene13.children.append(Viewpoint14)
Background15 = x3d.Background()
Background15.DEF = "cube"
Background15.leftUrl = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_left.png"]
Background15.rightUrl = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_right.png"]
Background15.frontUrl = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_front.png"]
Background15.backUrl = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_back.png"]
Background15.topUrl = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_top.png"]
Background15.bottomUrl = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_bottom.png"]

Scene13.children.append(Background15)
Transform16 = x3d.Transform()
Shape17 = x3d.Shape()
Appearance18 = x3d.Appearance()
Material19 = x3d.Material()
Material19.diffuseColor = [0.7,0.7,0.7]
Material19.specularColor = [0.5,0.5,0.5]

Appearance18.material = Material19
ComposedCubeMapTexture20 = x3d.ComposedCubeMapTexture()
ImageTexture21 = x3d.ImageTexture()
ImageTexture21.DEF = "backShader"
ImageTexture21.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_back.png"]

ComposedCubeMapTexture20.backTexture = ImageTexture21
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.DEF = "bottomShader"
ImageTexture22.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_bottom.png"]

ComposedCubeMapTexture20.bottomTexture = ImageTexture22
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.DEF = "frontShader"
ImageTexture23.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_front.png"]

ComposedCubeMapTexture20.frontTexture.append(ImageTexture23)
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.DEF = "leftShader"
ImageTexture24.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_left.png"]

ComposedCubeMapTexture20.leftTexture = ImageTexture24
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.DEF = "rightShader"
ImageTexture25.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_right.png"]

ComposedCubeMapTexture20.rightTexture.append(ImageTexture25)
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.DEF = "topShader"
ImageTexture26.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/all_probes/beach_cross/beach_top.png"]

ComposedCubeMapTexture20.topTexture.append(ImageTexture26)

Appearance18.texture = ComposedCubeMapTexture20
ComposedShader27 = x3d.ComposedShader()
ComposedShader27.DEF = "x_ite"
ComposedShader27.language = "GLSL"
#http://hypertextbook.com/facts/2005/JustinChe.shtml
field28 = x3d.field()
field28.name = "chromaticDispertion"
field28.accessType = "inputOutput"
field28.type = "SFVec3f"
field28.value = [0.98,1,1.033]

ComposedShader27.field.append(field28)
field29 = x3d.field()
field29.name = "cube"
field29.accessType = "inputOutput"
field29.type = "SFInt32"
field29.value = 0

ComposedShader27.field.append(field29)
field30 = x3d.field()
field30.name = "bias"
field30.accessType = "inputOutput"
field30.type = "SFFloat"
field30.value = 0.5

ComposedShader27.field.append(field30)
field31 = x3d.field()
field31.name = "scale"
field31.accessType = "inputOutput"
field31.type = "SFFloat"
field31.value = 0.5

ComposedShader27.field.append(field31)
field32 = x3d.field()
field32.name = "power"
field32.accessType = "inputOutput"
field32.type = "SFFloat"
field32.value = 2

ComposedShader27.field.append(field32)
ShaderPart33 = x3d.ShaderPart()
ShaderPart33.url = ["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"]
ShaderPart33.type = "VERTEX"

ComposedShader27.parts.append(ShaderPart33)
ShaderPart34 = x3d.ShaderPart()
ShaderPart34.url = ["../shaders/x_itemix.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_itemix.fs"]
ShaderPart34.type = "FRAGMENT"

ComposedShader27.parts.append(ShaderPart34)

Appearance18.shaders.append(ComposedShader27)
ComposedShader35 = x3d.ComposedShader()
ComposedShader35.DEF = "x3dom"
ComposedShader35.language = "GLSL"
field36 = x3d.field()
field36.name = "chromaticDispertion"
field36.accessType = "inputOutput"
field36.type = "SFVec3f"
field36.value = [0.98,1,1.033]

ComposedShader35.field.append(field36)
field37 = x3d.field()
field37.name = "cube"
field37.accessType = "inputOutput"
field37.type = "SFInt32"
field37.value = 0

ComposedShader35.field.append(field37)
field38 = x3d.field()
field38.name = "bias"
field38.accessType = "inputOutput"
field38.type = "SFFloat"
field38.value = 0.5

ComposedShader35.field.append(field38)
field39 = x3d.field()
field39.name = "scale"
field39.accessType = "inputOutput"
field39.type = "SFFloat"
field39.value = 0.5

ComposedShader35.field.append(field39)
field40 = x3d.field()
field40.name = "power"
field40.accessType = "inputOutput"
field40.type = "SFFloat"
field40.value = 2

ComposedShader35.field.append(field40)
ShaderPart41 = x3d.ShaderPart()
ShaderPart41.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart41.type = "VERTEX"

ComposedShader35.parts.append(ShaderPart41)
ShaderPart42 = x3d.ShaderPart()
ShaderPart42.url = ["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/mix.fs"]
ShaderPart42.type = "FRAGMENT"

ComposedShader35.parts.append(ShaderPart42)

Appearance18.shaders.append(ComposedShader35)

Shape17.appearance = Appearance18
Sphere43 = x3d.Sphere()
Sphere43.radius = 30

Shape17.geometry = Sphere43

Transform16.children.append(Shape17)
Script44 = x3d.Script()
Script44.DEF = "UrlSelector"
Script44.directOutput = True
field45 = x3d.field()
field45.name = "frontUrls"
field45.type = "MFString"
field45.accessType = "initializeOnly"
field45.value = ["../resources/images/all_probes/beach_cross/beach_front.png","../resources/images/all_probes/building_cross/building_front.png","../resources/images/all_probes/campus_cross/campus_front.png","../resources/images/all_probes/galileo_cross/galileo_front.png","../resources/images/all_probes/grace_cross/grace_front.png","../resources/images/all_probes/kitchen_cross/kitchen_front.png","../resources/images/all_probes/rnl_cross/rnl_front.png","../resources/images/all_probes/stpeters_cross/stpeters_front.png","../resources/images/all_probes/uffizi_cross/uffizi_front.png"]

Script44.field.append(field45)
field46 = x3d.field()
field46.name = "backUrls"
field46.type = "MFString"
field46.accessType = "initializeOnly"
field46.value = ["../resources/images/all_probes/beach_cross/beach_back.png","../resources/images/all_probes/building_cross/building_back.png","../resources/images/all_probes/campus_cross/campus_back.png","../resources/images/all_probes/galileo_cross/galileo_back.png","../resources/images/all_probes/grace_cross/grace_back.png","../resources/images/all_probes/kitchen_cross/kitchen_back.png","../resources/images/all_probes/rnl_cross/rnl_back.png","../resources/images/all_probes/stpeters_cross/stpeters_back.png","../resources/images/all_probes/uffizi_cross/uffizi_back.png"]

Script44.field.append(field46)
field47 = x3d.field()
field47.name = "leftUrls"
field47.type = "MFString"
field47.accessType = "initializeOnly"
field47.value = ["../resources/images/all_probes/beach_cross/beach_left.png","../resources/images/all_probes/building_cross/building_left.png","../resources/images/all_probes/campus_cross/campus_left.png","../resources/images/all_probes/galileo_cross/galileo_left.png","../resources/images/all_probes/grace_cross/grace_left.png","../resources/images/all_probes/kitchen_cross/kitchen_left.png","../resources/images/all_probes/rnl_cross/rnl_left.png","../resources/images/all_probes/stpeters_cross/stpeters_left.png","../resources/images/all_probes/uffizi_cross/uffizi_left.png"]

Script44.field.append(field47)
field48 = x3d.field()
field48.name = "rightUrls"
field48.type = "MFString"
field48.accessType = "initializeOnly"
field48.value = ["../resources/images/all_probes/beach_cross/beach_right.png","../resources/images/all_probes/building_cross/building_right.png","../resources/images/all_probes/campus_cross/campus_right.png","../resources/images/all_probes/galileo_cross/galileo_right.png","../resources/images/all_probes/grace_cross/grace_right.png","../resources/images/all_probes/kitchen_cross/kitchen_right.png","../resources/images/all_probes/rnl_cross/rnl_right.png","../resources/images/all_probes/stpeters_cross/stpeters_right.png","../resources/images/all_probes/uffizi_cross/uffizi_right.png"]

Script44.field.append(field48)
field49 = x3d.field()
field49.name = "topUrls"
field49.type = "MFString"
field49.accessType = "initializeOnly"
field49.value = ["../resources/images/all_probes/beach_cross/beach_top.png","../resources/images/all_probes/building_cross/building_top.png","../resources/images/all_probes/campus_cross/campus_top.png","../resources/images/all_probes/galileo_cross/galileo_top.png","../resources/images/all_probes/grace_cross/grace_top.png","../resources/images/all_probes/kitchen_cross/kitchen_top.png","../resources/images/all_probes/rnl_cross/rnl_top.png","../resources/images/all_probes/stpeters_cross/stpeters_top.png","../resources/images/all_probes/uffizi_cross/uffizi_top.png"]

Script44.field.append(field49)
field50 = x3d.field()
field50.name = "bottomUrls"
field50.type = "MFString"
field50.accessType = "initializeOnly"
field50.value = ["../resources/images/all_probes/beach_cross/beach_bottom.png","../resources/images/all_probes/building_cross/building_bottom.png","../resources/images/all_probes/campus_cross/campus_bottom.png","../resources/images/all_probes/galileo_cross/galileo_bottom.png","../resources/images/all_probes/grace_cross/grace_bottom.png","../resources/images/all_probes/kitchen_cross/kitchen_bottom.png","../resources/images/all_probes/rnl_cross/rnl_bottom.png","../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","../resources/images/all_probes/uffizi_cross/uffizi_bottom.png"]

Script44.field.append(field50)
field51 = x3d.field()
field51.name = "front_changed"
field51.type = "MFString"
field51.accessType = "outputOnly"

Script44.field.append(field51)
field52 = x3d.field()
field52.name = "back_changed"
field52.type = "MFString"
field52.accessType = "outputOnly"

Script44.field.append(field52)
field53 = x3d.field()
field53.name = "left_changed"
field53.type = "MFString"
field53.accessType = "outputOnly"

Script44.field.append(field53)
field54 = x3d.field()
field54.name = "right_changed"
field54.type = "MFString"
field54.accessType = "outputOnly"

Script44.field.append(field54)
field55 = x3d.field()
field55.name = "top_changed"
field55.type = "MFString"
field55.accessType = "outputOnly"

Script44.field.append(field55)
field56 = x3d.field()
field56.name = "bottom_changed"
field56.type = "MFString"
field56.accessType = "outputOnly"

Script44.field.append(field56)
field57 = x3d.field()
field57.name = "set_fraction"
field57.type = "SFFloat"
field57.accessType = "inputOnly"

Script44.field.append(field57)
field58 = x3d.field()
field58.name = "old"
field58.type = "SFInt32"
field58.accessType = "inputOutput"
field58.value = -1

Script44.field.append(field58)

Script44.sourceCode = '''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    // Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }'''

Transform16.children.append(Script44)
TimeSensor59 = x3d.TimeSensor()
TimeSensor59.DEF = "Clock"
TimeSensor59.cycleInterval = 45
TimeSensor59.loop = True

Transform16.children.append(TimeSensor59)
ROUTE60 = x3d.ROUTE()
ROUTE60.fromNode = "Clock"
ROUTE60.fromField = "fraction_changed"
ROUTE60.toNode = "UrlSelector"
ROUTE60.toField = "set_fraction"

Transform16.children.append(ROUTE60)
ROUTE61 = x3d.ROUTE()
ROUTE61.fromNode = "UrlSelector"
ROUTE61.fromField = "front_changed"
ROUTE61.toNode = "cube"
ROUTE61.toField = "frontUrl"

Transform16.children.append(ROUTE61)
ROUTE62 = x3d.ROUTE()
ROUTE62.fromNode = "UrlSelector"
ROUTE62.fromField = "back_changed"
ROUTE62.toNode = "cube"
ROUTE62.toField = "backUrl"

Transform16.children.append(ROUTE62)
ROUTE63 = x3d.ROUTE()
ROUTE63.fromNode = "UrlSelector"
ROUTE63.fromField = "left_changed"
ROUTE63.toNode = "cube"
ROUTE63.toField = "leftUrl"

Transform16.children.append(ROUTE63)
ROUTE64 = x3d.ROUTE()
ROUTE64.fromNode = "UrlSelector"
ROUTE64.fromField = "right_changed"
ROUTE64.toNode = "cube"
ROUTE64.toField = "rightUrl"

Transform16.children.append(ROUTE64)
ROUTE65 = x3d.ROUTE()
ROUTE65.fromNode = "UrlSelector"
ROUTE65.fromField = "top_changed"
ROUTE65.toNode = "cube"
ROUTE65.toField = "topUrl"

Transform16.children.append(ROUTE65)
ROUTE66 = x3d.ROUTE()
ROUTE66.fromNode = "UrlSelector"
ROUTE66.fromField = "bottom_changed"
ROUTE66.toNode = "cube"
ROUTE66.toField = "bottomUrl"

Transform16.children.append(ROUTE66)
ROUTE67 = x3d.ROUTE()
ROUTE67.fromNode = "UrlSelector"
ROUTE67.fromField = "front_changed"
ROUTE67.toNode = "frontShader"
ROUTE67.toField = "url"

Transform16.children.append(ROUTE67)
ROUTE68 = x3d.ROUTE()
ROUTE68.fromNode = "UrlSelector"
ROUTE68.fromField = "back_changed"
ROUTE68.toNode = "backShader"
ROUTE68.toField = "url"

Transform16.children.append(ROUTE68)
ROUTE69 = x3d.ROUTE()
ROUTE69.fromNode = "UrlSelector"
ROUTE69.fromField = "left_changed"
ROUTE69.toNode = "leftShader"
ROUTE69.toField = "url"

Transform16.children.append(ROUTE69)
ROUTE70 = x3d.ROUTE()
ROUTE70.fromNode = "UrlSelector"
ROUTE70.fromField = "right_changed"
ROUTE70.toNode = "rightShader"
ROUTE70.toField = "url"

Transform16.children.append(ROUTE70)
ROUTE71 = x3d.ROUTE()
ROUTE71.fromNode = "UrlSelector"
ROUTE71.fromField = "top_changed"
ROUTE71.toNode = "topShader"
ROUTE71.toField = "url"

Transform16.children.append(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromNode = "UrlSelector"
ROUTE72.fromField = "bottom_changed"
ROUTE72.toNode = "bottomShader"
ROUTE72.toField = "url"

Transform16.children.append(ROUTE72)

Scene13.children.append(Transform16)

X3D0.Scene = Scene13
f = open("././mirror2_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
