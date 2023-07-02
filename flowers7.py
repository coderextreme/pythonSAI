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
meta8.content = "flowers7.x3d"

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
meta11.content = "https://coderextreme.net/X3DJSONLD/flowers7.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "description"
meta12.content = "a flower"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
NavigationInfo14 = x3d.NavigationInfo()

Scene13.children.append(NavigationInfo14)
#Images courtesy of Paul Debevec's Light Probe Image Gallery
Background15 = x3d.Background()
Background15.DEF = "background"
Background15.backUrl = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]
Background15.bottomUrl = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]
Background15.frontUrl = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]
Background15.leftUrl = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]
Background15.rightUrl = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]
Background15.topUrl = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]

Scene13.children.append(Background15)
Viewpoint16 = x3d.Viewpoint()
Viewpoint16.position = [0,0,40]
Viewpoint16.description = "Transparent rose"

Scene13.children.append(Viewpoint16)
Transform17 = x3d.Transform()
Shape18 = x3d.Shape()
Appearance19 = x3d.Appearance()
Material20 = x3d.Material()
Material20.diffuseColor = [0.7,0.7,0.7]
Material20.specularColor = [0.5,0.5,0.5]

Appearance19.material = Material20
ComposedCubeMapTexture21 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture21.DEF = "texture"
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.DEF = "backShader"
ImageTexture22.url = ["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]

ComposedCubeMapTexture21.backTexture = ImageTexture22
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.DEF = "bottomShader"
ImageTexture23.url = ["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]

ComposedCubeMapTexture21.bottomTexture = ImageTexture23
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.DEF = "frontShader"
ImageTexture24.url = ["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]

ComposedCubeMapTexture21.frontTexture = ImageTexture24
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.DEF = "leftShader"
ImageTexture25.url = ["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]

ComposedCubeMapTexture21.leftTexture = ImageTexture25
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.DEF = "rightShader"
ImageTexture26.url = ["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]

ComposedCubeMapTexture21.rightTexture = ImageTexture26
ImageTexture27 = x3d.ImageTexture()
ImageTexture27.DEF = "topShader"
ImageTexture27.url = ["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]

ComposedCubeMapTexture21.topTexture = ImageTexture27

Appearance19.texture = ComposedCubeMapTexture21
ComposedShader28 = x3d.ComposedShader()
ComposedShader28.DEF = "x3dom"
ComposedShader28.language = "GLSL"
field29 = x3d.field()
field29.name = "cube"
field29.type = "SFInt32"
field29.accessType = "inputOutput"
field29.value = 0

ComposedShader28.field.append(field29)
field30 = x3d.field()
field30.name = "chromaticDispertion"
field30.accessType = "initializeOnly"
field30.type = "SFVec3f"
field30.value = [0.98,1,1.033]

ComposedShader28.field.append(field30)
field31 = x3d.field()
field31.name = "bias"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = 0.5

ComposedShader28.field.append(field31)
field32 = x3d.field()
field32.name = "scale"
field32.type = "SFFloat"
field32.accessType = "inputOutput"
field32.value = 0.5

ComposedShader28.field.append(field32)
field33 = x3d.field()
field33.name = "power"
field33.type = "SFFloat"
field33.accessType = "inputOutput"
field33.value = 2

ComposedShader28.field.append(field33)
field34 = x3d.field()
field34.name = "a"
field34.type = "SFFloat"
field34.accessType = "inputOutput"
field34.value = 10

ComposedShader28.field.append(field34)
field35 = x3d.field()
field35.name = "b"
field35.type = "SFFloat"
field35.accessType = "inputOutput"
field35.value = 1

ComposedShader28.field.append(field35)
field36 = x3d.field()
field36.name = "c"
field36.type = "SFFloat"
field36.accessType = "inputOutput"
field36.value = 20

ComposedShader28.field.append(field36)
field37 = x3d.field()
field37.name = "d"
field37.type = "SFFloat"
field37.accessType = "inputOutput"
field37.value = 20

ComposedShader28.field.append(field37)
field38 = x3d.field()
field38.name = "tdelta"
field38.type = "SFFloat"
field38.accessType = "inputOutput"
field38.value = 0

ComposedShader28.field.append(field38)
field39 = x3d.field()
field39.name = "pdelta"
field39.type = "SFFloat"
field39.accessType = "inputOutput"
field39.value = 0

ComposedShader28.field.append(field39)
#<field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field>
ShaderPart40 = x3d.ShaderPart()
ShaderPart40.url = ["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom_flowers_chromatic.vs"]
ShaderPart40.type = "VERTEX"

ComposedShader28.parts.append(ShaderPart40)
ShaderPart41 = x3d.ShaderPart()
ShaderPart41.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs"]
ShaderPart41.type = "FRAGMENT"

ComposedShader28.parts.append(ShaderPart41)

Appearance19.shaders.append(ComposedShader28)
ComposedShader42 = x3d.ComposedShader()
ComposedShader42.DEF = "x_ite"
ComposedShader42.language = "GLSL"
field43 = x3d.field()
field43.name = "cube"
field43.type = "SFNode"
field43.accessType = "inputOutput"
ComposedCubeMapTexture44 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture44.USE = "texture"

field43.children.append(ComposedCubeMapTexture44)

ComposedShader42.field.append(field43)
field45 = x3d.field()
field45.name = "chromaticDispertion"
field45.accessType = "initializeOnly"
field45.type = "SFVec3f"
field45.value = [0.98,1,1.033]

ComposedShader42.field.append(field45)
field46 = x3d.field()
field46.name = "bias"
field46.type = "SFFloat"
field46.accessType = "inputOnly"
field46.value = 0.5

ComposedShader42.field.append(field46)
field47 = x3d.field()
field47.name = "scale"
field47.type = "SFFloat"
field47.accessType = "inputOnly"
field47.value = 0.5

ComposedShader42.field.append(field47)
field48 = x3d.field()
field48.name = "power"
field48.type = "SFFloat"
field48.accessType = "inputOnly"
field48.value = 2

ComposedShader42.field.append(field48)
field49 = x3d.field()
field49.name = "a"
field49.type = "SFFloat"
field49.accessType = "inputOnly"
field49.value = 10

ComposedShader42.field.append(field49)
field50 = x3d.field()
field50.name = "b"
field50.type = "SFFloat"
field50.accessType = "inputOnly"
field50.value = 1

ComposedShader42.field.append(field50)
field51 = x3d.field()
field51.name = "c"
field51.type = "SFFloat"
field51.accessType = "inputOnly"
field51.value = 20

ComposedShader42.field.append(field51)
field52 = x3d.field()
field52.name = "d"
field52.type = "SFFloat"
field52.accessType = "inputOnly"
field52.value = 20

ComposedShader42.field.append(field52)
field53 = x3d.field()
field53.name = "tdelta"
field53.type = "SFFloat"
field53.accessType = "inputOnly"
field53.value = 0

ComposedShader42.field.append(field53)
field54 = x3d.field()
field54.name = "pdelta"
field54.type = "SFFloat"
field54.accessType = "inputOnly"
field54.value = 0

ComposedShader42.field.append(field54)
ShaderPart55 = x3d.ShaderPart()
ShaderPart55.url = ["../shaders/x_ite_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite_flowers_chromatic.vs"]
ShaderPart55.type = "VERTEX"

ComposedShader42.parts.append(ShaderPart55)
ShaderPart56 = x3d.ShaderPart()
ShaderPart56.url = ["../shaders/x_ite.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.fs"]
ShaderPart56.type = "FRAGMENT"

ComposedShader42.parts.append(ShaderPart56)

Appearance19.shaders.append(ComposedShader42)

Shape18.appearance = Appearance19
Sphere57 = x3d.Sphere()

Shape18.geometry = Sphere57

Transform17.children.append(Shape18)

Scene13.children.append(Transform17)
Script58 = x3d.Script()
Script58.DEF = "UrlSelector"
Script58.directOutput = True
field59 = x3d.field()
field59.name = "frontUrls"
field59.type = "MFString"
field59.accessType = "initializeOnly"
field59.value = ["../resources/images/all_probes/beach_cross/beach_front.png","../resources/images/all_probes/building_cross/building_front.png","../resources/images/all_probes/campus_cross/campus_front.png","../resources/images/all_probes/galileo_cross/galileo_front.png","../resources/images/all_probes/grace_cross/grace_front.png","../resources/images/all_probes/kitchen_cross/kitchen_front.png","../resources/images/all_probes/rnl_cross/rnl_front.png","../resources/images/all_probes/stpeters_cross/stpeters_front.png","../resources/images/all_probes/uffizi_cross/uffizi_front.png"]

Script58.field.append(field59)
field60 = x3d.field()
field60.name = "backUrls"
field60.type = "MFString"
field60.accessType = "initializeOnly"
field60.value = ["../resources/images/all_probes/beach_cross/beach_back.png","../resources/images/all_probes/building_cross/building_back.png","../resources/images/all_probes/campus_cross/campus_back.png","../resources/images/all_probes/galileo_cross/galileo_back.png","../resources/images/all_probes/grace_cross/grace_back.png","../resources/images/all_probes/kitchen_cross/kitchen_back.png","../resources/images/all_probes/rnl_cross/rnl_back.png","../resources/images/all_probes/stpeters_cross/stpeters_back.png","../resources/images/all_probes/uffizi_cross/uffizi_back.png"]

Script58.field.append(field60)
field61 = x3d.field()
field61.name = "leftUrls"
field61.type = "MFString"
field61.accessType = "initializeOnly"
field61.value = ["../resources/images/all_probes/beach_cross/beach_left.png","../resources/images/all_probes/building_cross/building_left.png","../resources/images/all_probes/campus_cross/campus_left.png","../resources/images/all_probes/galileo_cross/galileo_left.png","../resources/images/all_probes/grace_cross/grace_left.png","../resources/images/all_probes/kitchen_cross/kitchen_left.png","../resources/images/all_probes/rnl_cross/rnl_left.png","../resources/images/all_probes/stpeters_cross/stpeters_left.png","../resources/images/all_probes/uffizi_cross/uffizi_left.png"]

Script58.field.append(field61)
field62 = x3d.field()
field62.name = "rightUrls"
field62.type = "MFString"
field62.accessType = "initializeOnly"
field62.value = ["../resources/images/all_probes/beach_cross/beach_right.png","../resources/images/all_probes/building_cross/building_right.png","../resources/images/all_probes/campus_cross/campus_right.png","../resources/images/all_probes/galileo_cross/galileo_right.png","../resources/images/all_probes/grace_cross/grace_right.png","../resources/images/all_probes/kitchen_cross/kitchen_right.png","../resources/images/all_probes/rnl_cross/rnl_right.png","../resources/images/all_probes/stpeters_cross/stpeters_right.png","../resources/images/all_probes/uffizi_cross/uffizi_right.png"]

Script58.field.append(field62)
field63 = x3d.field()
field63.name = "topUrls"
field63.type = "MFString"
field63.accessType = "initializeOnly"
field63.value = ["../resources/images/all_probes/beach_cross/beach_top.png","../resources/images/all_probes/building_cross/building_top.png","../resources/images/all_probes/campus_cross/campus_top.png","../resources/images/all_probes/galileo_cross/galileo_top.png","../resources/images/all_probes/grace_cross/grace_top.png","../resources/images/all_probes/kitchen_cross/kitchen_top.png","../resources/images/all_probes/rnl_cross/rnl_top.png","../resources/images/all_probes/stpeters_cross/stpeters_top.png","../resources/images/all_probes/uffizi_cross/uffizi_top.png"]

Script58.field.append(field63)
field64 = x3d.field()
field64.name = "bottomUrls"
field64.type = "MFString"
field64.accessType = "initializeOnly"
field64.value = ["../resources/images/all_probes/beach_cross/beach_bottom.png","../resources/images/all_probes/building_cross/building_bottom.png","../resources/images/all_probes/campus_cross/campus_bottom.png","../resources/images/all_probes/galileo_cross/galileo_bottom.png","../resources/images/all_probes/grace_cross/grace_bottom.png","../resources/images/all_probes/kitchen_cross/kitchen_bottom.png","../resources/images/all_probes/rnl_cross/rnl_bottom.png","../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","../resources/images/all_probes/uffizi_cross/uffizi_bottom.png"]

Script58.field.append(field64)
field65 = x3d.field()
field65.name = "front"
field65.type = "MFString"
field65.accessType = "inputOutput"

Script58.field.append(field65)
field66 = x3d.field()
field66.name = "back"
field66.type = "MFString"
field66.accessType = "inputOutput"

Script58.field.append(field66)
field67 = x3d.field()
field67.name = "left"
field67.type = "MFString"
field67.accessType = "inputOutput"

Script58.field.append(field67)
field68 = x3d.field()
field68.name = "right"
field68.type = "MFString"
field68.accessType = "inputOutput"

Script58.field.append(field68)
field69 = x3d.field()
field69.name = "top"
field69.type = "MFString"
field69.accessType = "inputOutput"

Script58.field.append(field69)
field70 = x3d.field()
field70.name = "bottom"
field70.type = "MFString"
field70.accessType = "inputOutput"

Script58.field.append(field70)
field71 = x3d.field()
field71.name = "set_fraction"
field71.type = "SFFloat"
field71.accessType = "inputOnly"

Script58.field.append(field71)
field72 = x3d.field()
field72.name = "old"
field72.type = "SFInt32"
field72.accessType = "inputOutput"
field72.value = -1

Script58.field.append(field72)

Script58.sourceCode = '''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front[0] = frontUrls[side];\n"+
"                    back[0] = backUrls[side];\n"+
"                    left[0] = leftUrls[side];\n"+
"                    right[0] = rightUrls[side];\n"+
"                    top[0] = topUrls[side];\n"+
"                    bottom[0] = bottomUrls[side];\n"+
"            }\n"+
"        }'''

Scene13.children.append(Script58)
#<TimeSensor DEF=\"Clock\" cycleInterval=\"45\" loop='true'/> <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='UrlSelector' toField='set_fraction'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='background' toField='frontUrl'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='background' toField='backUrl'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='background' toField='leftUrl'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='background' toField='rightUrl'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='background' toField='topUrl'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='background' toField='bottomUrl'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='frontShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='backShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='leftShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='rightShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='topShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='bottomShader' toField='url'/>
Script73 = x3d.Script()
Script73.DEF = "Animate"
Script73.directOutput = True
field74 = x3d.field()
field74.name = "set_fraction"
field74.type = "SFFloat"
field74.accessType = "inputOnly"

Script73.field.append(field74)
field75 = x3d.field()
field75.name = "a"
field75.type = "SFFloat"
field75.accessType = "inputOutput"
field75.value = 10

Script73.field.append(field75)
field76 = x3d.field()
field76.name = "b"
field76.type = "SFFloat"
field76.accessType = "inputOutput"
field76.value = 1

Script73.field.append(field76)
field77 = x3d.field()
field77.name = "c"
field77.type = "SFFloat"
field77.accessType = "inputOutput"
field77.value = 20

Script73.field.append(field77)
field78 = x3d.field()
field78.name = "d"
field78.type = "SFFloat"
field78.accessType = "inputOutput"
field78.value = 20

Script73.field.append(field78)
field79 = x3d.field()
field79.name = "tdelta"
field79.type = "SFFloat"
field79.accessType = "inputOutput"
field79.value = 0

Script73.field.append(field79)
field80 = x3d.field()
field80.name = "pdelta"
field80.type = "SFFloat"
field80.accessType = "inputOutput"
field80.value = 0

Script73.field.append(field80)

Script73.sourceCode = '''ecmascript:\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		a = a + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		b = b + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		c = c + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		d = d + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	tdelta = tdelta + 0.5;\n"+
"	pdelta = pdelta + 0.5;\n"+
"	if (a < 1) {\n"+
"		a = 10;\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		b = 10;\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		d = 4;\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		d = 4;\n"+
"	}\n"+
"}'''

Scene13.children.append(Script73)
TimeSensor81 = x3d.TimeSensor()
TimeSensor81.DEF = "TourTime"
TimeSensor81.cycleInterval = 5
TimeSensor81.loop = True

Scene13.children.append(TimeSensor81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromNode = "TourTime"
ROUTE82.fromField = "fraction_changed"
ROUTE82.toNode = "Animate"
ROUTE82.toField = "set_fraction"

Scene13.children.append(ROUTE82)
ROUTE83 = x3d.ROUTE()
ROUTE83.fromNode = "Animate"
ROUTE83.fromField = "a"
ROUTE83.toNode = "x_ite"
ROUTE83.toField = "a"

Scene13.children.append(ROUTE83)
ROUTE84 = x3d.ROUTE()
ROUTE84.fromNode = "Animate"
ROUTE84.fromField = "b"
ROUTE84.toNode = "x_ite"
ROUTE84.toField = "b"

Scene13.children.append(ROUTE84)
ROUTE85 = x3d.ROUTE()
ROUTE85.fromNode = "Animate"
ROUTE85.fromField = "c"
ROUTE85.toNode = "x_ite"
ROUTE85.toField = "c"

Scene13.children.append(ROUTE85)
ROUTE86 = x3d.ROUTE()
ROUTE86.fromNode = "Animate"
ROUTE86.fromField = "d"
ROUTE86.toNode = "x_ite"
ROUTE86.toField = "d"

Scene13.children.append(ROUTE86)
ROUTE87 = x3d.ROUTE()
ROUTE87.fromNode = "Animate"
ROUTE87.fromField = "pdelta"
ROUTE87.toNode = "x_ite"
ROUTE87.toField = "pdelta"

Scene13.children.append(ROUTE87)
ROUTE88 = x3d.ROUTE()
ROUTE88.fromNode = "Animate"
ROUTE88.fromField = "tdelta"
ROUTE88.toNode = "x_ite"
ROUTE88.toField = "tdelta"

Scene13.children.append(ROUTE88)
ROUTE89 = x3d.ROUTE()
ROUTE89.fromNode = "Animate"
ROUTE89.fromField = "a"
ROUTE89.toNode = "x3dom"
ROUTE89.toField = "a"

Scene13.children.append(ROUTE89)
ROUTE90 = x3d.ROUTE()
ROUTE90.fromNode = "Animate"
ROUTE90.fromField = "b"
ROUTE90.toNode = "x3dom"
ROUTE90.toField = "b"

Scene13.children.append(ROUTE90)
ROUTE91 = x3d.ROUTE()
ROUTE91.fromNode = "Animate"
ROUTE91.fromField = "c"
ROUTE91.toNode = "x3dom"
ROUTE91.toField = "c"

Scene13.children.append(ROUTE91)
ROUTE92 = x3d.ROUTE()
ROUTE92.fromNode = "Animate"
ROUTE92.fromField = "d"
ROUTE92.toNode = "x3dom"
ROUTE92.toField = "d"

Scene13.children.append(ROUTE92)
ROUTE93 = x3d.ROUTE()
ROUTE93.fromNode = "Animate"
ROUTE93.fromField = "pdelta"
ROUTE93.toNode = "x3dom"
ROUTE93.toField = "pdelta"

Scene13.children.append(ROUTE93)
ROUTE94 = x3d.ROUTE()
ROUTE94.fromNode = "Animate"
ROUTE94.fromField = "tdelta"
ROUTE94.toNode = "x3dom"
ROUTE94.toField = "tdelta"

Scene13.children.append(ROUTE94)

X3D0.Scene = Scene13
f = open("././flowers7_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
