print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.2"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.content = "CloudsProcedural4.x3d"
meta2.name = "title"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.content = "X3D utilizing ecmascript to develop quasi volumetric 3D clouds from png image textured billboard nodes."
meta3.name = "description"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.content = "Capt Darren W. Murphy"
meta4.name = "creator"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "1 November 2007"
meta5.name = "created"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "14 January 2014"
meta6.name = "modified"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "https://savage.nps.edu/Savage/Environment/Atmosphere/CloudsProcedural4.x3d"
meta7.name = "identifier"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "X3D-Edit, https://www.web3d.org/x3d/content/README.X3D-Edit.html"
meta8.name = "generator"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "../../license.html"
meta9.name = "license"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.content = "fix links"
meta10.name = "TODO"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
""" A png image file for the cloud texture must be designated in the ecmascript node. """
Viewpoint12 = x3d.Viewpoint()
Viewpoint12.description = "Main"
Viewpoint12.jump = False
Viewpoint12.orientation = [0,1,0,1.57]
Viewpoint12.position = [50000,1000,42000]

Scene11.children.append(Viewpoint12)
Viewpoint13 = x3d.Viewpoint()
Viewpoint13.description = "Light House Tower"
Viewpoint13.jump = False
Viewpoint13.orientation = [0,1,0,1.3]
Viewpoint13.position = [45000,1290,44000]

Scene11.children.append(Viewpoint13)
Viewpoint14 = x3d.Viewpoint()
Viewpoint14.description = "centerWest"
Viewpoint14.jump = False
Viewpoint14.orientation = [0,1,0,2.5]
Viewpoint14.position = [48000,1000,20000]

Scene11.children.append(Viewpoint14)
Background15 = x3d.Background()

Scene11.children.append(Background15)
DirectionalLight16 = x3d.DirectionalLight()
DirectionalLight16.ambientIntensity = 1
DirectionalLight16.direction = [-1,0,0]
DirectionalLight16.global_ = True

Scene11.children.append(DirectionalLight16)
Group17 = x3d.Group()
Group17.DEF = "Terrain"
Transform18 = x3d.Transform()
Transform18.scale = [50,50,50]
Transform18.translation = [25000,0,25000]
Inline19 = x3d.Inline()
Inline19.url = ["MontereyBayLargeMesh.x3d","https://savage.nps.edu/Savage/Environment/Atmosphere/MontereyBayLargeMesh.x3d","MontereyBayLargeMesh.wrl","https://savage.nps.edu/Savage/Environment/Atmosphere/MontereyBayLargeMesh.wrl"]

Transform18.children.append(Inline19)

Group17.children.append(Transform18)
Transform20 = x3d.Transform()
Transform20.rotation = [1,0,0,1.57]
Transform20.translation = [25000,0,25000]
Shape21 = x3d.Shape()
Rectangle2D22 = x3d.Rectangle2D()
Rectangle2D22.size = [77000,55000]

Shape21.geometry = Rectangle2D22
Appearance23 = x3d.Appearance()
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.url = ["ocean.png","https://savage.nps.edu/Savage/Environment/Atmosphere/ocean.png"]

Appearance23.texture = ImageTexture24

Shape21.appearance = Appearance23

Transform20.children.append(Shape21)

Group17.children.append(Transform20)

Scene11.children.append(Group17)
Group25 = x3d.Group()
Group25.DEF = "Placemarks"
Transform26 = x3d.Transform()
Transform26.scale = [50,50,50]
Transform26.translation = [45000,30,44000]
Inline27 = x3d.Inline()
Inline27.url = ["Lighthouse.x3d","https://savage.nps.edu/Savage/Environment/Atmosphere/Lighthouse.x3d","Lighthouse.wrl","https://savage.nps.edu/Savage/Environment/Atmosphere/Lighthouse.wrl"]

Transform26.children.append(Inline27)

Group25.children.append(Transform26)

Scene11.children.append(Group25)
Group28 = x3d.Group()
Group28.DEF = "Clouds"
Transform29 = x3d.Transform()
Transform29.DEF = "Cumulus"

Group28.children.append(Transform29)
Transform30 = x3d.Transform()
Transform30.DEF = "Cirrus"

Group28.children.append(Transform30)
Transform31 = x3d.Transform()
Transform31.DEF = "Fog"

Group28.children.append(Transform31)
Script32 = x3d.Script()
Script32.DEF = "PixelScript"
Script32.directOutput = True
field33 = x3d.field()
field33.accessType = "initializeOnly"
field33.name = "Cumulus"
field33.type = "SFNode"
Transform34 = x3d.Transform()
Transform34.USE = "Cumulus"

field33.children.append(Transform34)

Script32.field.append(field33)
field35 = x3d.field()
field35.accessType = "initializeOnly"
field35.name = "Cirrus"
field35.type = "SFNode"
Transform36 = x3d.Transform()
Transform36.USE = "Cirrus"

field35.children.append(Transform36)

Script32.field.append(field35)
field37 = x3d.field()
field37.accessType = "initializeOnly"
field37.name = "Fog"
field37.type = "SFNode"

Script32.field.append(field37)

Script32.sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"\n"+
"function cumulustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"	X = 50000*Math.random();          //  X horizontal range\n"+
"	Y = 1000 + 300*Math.random();	 //  Y vertical base + range\n"+
"	Z = 50000*Math.random();         // z horizontal range\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function cumulusscale() // these values scale a cloud within a designated size\n"+
"{\n"+
"\n"+
"	var maxscale = 1;\n"+
"\n"+
"	scale = Math.round(9+maxscale*Math.random());\n"+
"	X = 1.5*scale;\n"+
"	Y = scale;\n"+
"	Z = scale;\n"+
"\n"+
"	randomscale = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomscale;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function cirrustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"	X = 50000*Math.random();          //  X horizontal range\n"+
"	Y = 8000 + 1000*Math.random();	 //  Y vertical base + range\n"+
"	Z = 50000*Math.random();         // z horizontal range\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function cirrusscale() // these values scale a cloud within a designated size\n"+
"{\n"+
"\n"+
"	var maxscale = 1;\n"+
"\n"+
"	scale = Math.round(9+maxscale*Math.random());\n"+
"	X = 1.5*scale;\n"+
"	Y = 2*Math.random();\n"+
"	Z = 1.5*scale;\n"+
"\n"+
"	randomscale = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomscale;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function cumulussectiontranslation() // These random values place another portion of cumulus type cloud\n"+
"{\n"+
"\n"+
"	randomtheta = 6.28319*Math.random();\n"+
"	randomphi = .7854*Math.random();\n"+
"	randomradius = 90 + 5*Math.random();//the first whole number should be close to the sectionradius\n"+
"\n"+
"	X = randomradius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"	Z = randomradius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"	Y = randomradius*Math.cos(randomphi);\n"+
"	\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"function cirrussectiontranslation() // These random values place another portion of cirrus type cloud\n"+
"{\n"+
"\n"+
"	randomtheta = 6.28319*Math.random();\n"+
"	randomphi = .7854*Math.random();\n"+
"	randomradius = 90 + 5*Math.random();//the first whole number should be close to the sectionradius\n"+
"\n"+
"	X = randomradius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"	Z = randomradius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"	Y = randomradius*Math.cos(randomphi);\n"+
"	\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function rotation() // This random value is for the billboard rotation not used in this script\n"+
"{\n"+
"\n"+
"\n"+
"	radians = 6.28*Math.random();\n"+
"\n"+
"	randomr = new String('0 0 1 ' + radians );\n"+
"	\n"+
"	\n"+
"	return randomr;\n"+
"	\n"+
"}\n"+
"\n"+
"function cumulus()\n"+
"{\n"+
"\n"+
"var maxi = 20;  // number of clouds\n"+
"\n"+
"var maxj = 5; // denotes how many portions affecting the size of the cloud\n"+
"\n"+
"var maxk = 8;  // number of billboards indicating cloud density\n"+
"\n"+
"var sectionradius = 100;  //radius of individual cloud sections\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"for (var i=0; i < maxi; i++) \n"+
"{\n"+
"\n"+
"\n"+
"\n"+
"CloudStringA = '	Transform {		\\n' +\n"+
"'    scale '+ cumulusscale() + '               	\\n' +\n"+
"'    translation '+ cumulustranslation() + '    \\n' +    // cloud placement\n"+
"'    children [	                                \\n';\n"+
"\n"+
"\n"+
"CloudStringB = new Array();\n"+
"CloudStringF = new Array();\n"+
"\n"+
"   	for (var j=0; j < maxj; j++)\n"+
"   	{\n"+
"\n"+
"	radius = 0;\n"+
"\n"+
"	CloudStringB[j]= '  Transform {		    	       \\n' +\n"+
"	'    translation '+ cumulussectiontranslation() + '    \\n' +     // section placement\n"+
"	'    children [	                                       \\n';\n"+
"\n"+
"	\n"+
"	CloudStringC = new Array();\n"+
"	image = new String();\n"+
"\n"+
"      		for (var k=1; k < maxk; k++)  // maxk value denotes how many textured billboards make up the cloud \n"+
"      		{\n"+
"\n"+
"\n"+
"		randomtheta = 6.28319*Math.random();\n"+
"		randomphi = 1.57079*Math.random();\n"+
"		radius = radius+(sectionradius/maxk); // radius incremental steps based on billow radius and max billboards\n"+
"\n"+
"		X = radius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"		Z = radius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"		Y = radius*Math.cos(randomphi);\n"+
"\n"+
"\n"+
"		if (Y <= 30) //cloud shading and lighting control\n"+
"  	{	\n"+
"	image = ' \\\"CloudTexture1_5.png\\\" \\\"https://savage.nps.edu/Savage/Environment/Spheretexture.png\\\" \\n';\n"+
"  	}\n"+
"\n"+
"  		else\n"+
"  	{	\n"+
"	image = ' \\\"CloudTexture1_4.png\\\" \\\"https://savage.nps.edu/Savage/Environment/Spheretexture.png\\\" \\n';\n"+
"  	}\n"+
"\n"+
"	\n"+
"		\n"+
"		Billboardtranslation = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"		CloudStringC[k] = '	Transform {		                \\n' +\n"+
"		'            translation '+ Billboardtranslation   + '          \\n' +     // random billboard placement within radius designated above\n"+
"		'	  children [	                                        \\n' +\n"+
"		'	      Billboard {	                                \\n' +\n"+
"		'	        axisOfRotation 0 0 0	                        \\n' +     // 0 0 0 designates rotation on all axis\n"+
"		'	        children [	                                \\n' +\n"+
"		'	            Transform {	                		\\n' +\n"+
"		'	              rotation  0 0 0 0 		        \\n' +     // a rotation of the individual billboards can be defined\n"+
"		'	              children [	                        \\n' +\n"+
"		'	                  Shape {	                        \\n' +\n"+
"		'	                    appearance Appearance {	        \\n' +\n"+
"		'				material Material {		\\n' +\n"+
"		'				                }  		\\n' +\n"+
"		'	                      texture ImageTexture {	        \\n' +\n"+
"		'	                        url [ ' + image + ' ]           \\n' + \n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                    geometry IndexedFaceSet {	        \\n' +     // define type of geometry to texture\n"+
"		'	                      coordIndex [ 0, 1, 2, 3 ]	        \\n' +\n"+
"		'			      solid FALSE		        \\n' +\n"+
"		'	                      coord Coordinate {	        \\n' +\n"+
"		'	                        point [ 50 50 0,	        \\n' +     // define size of the geometry. Here 100 meter 2D square.\n"+
"		'	                                50 -50 0,	        \\n' +\n"+
"		'	                               -50 -50 0,	        \\n' +\n"+
"		'	                               -50 50 0 ]	        \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                  }	                                \\n' +\n"+
"		'	              ]	                                        \\n' +\n"+
"		'	            }	                                        \\n' +\n"+
"		'	       ]	                                        \\n' +\n"+
"		'	   }	                                                \\n' +\n"+
"		'      ]	                                                \\n' +\n"+
"		'     }	                                                        \\n';      \n"+
"		\n"+
"\n"+
"		}\n"+
"\n"+
"	CloudStringD = CloudStringC.join(' ');\n"+
"\n"+
"	\n"+
"	CloudStringE = '   ]	                 \\n' +\n"+
"	'	}	                         \\n';\n"+
"\n"+
"	CloudStringF[j] = CloudStringB[j] + CloudStringD +CloudStringE;\n"+
"\n"+
"\n"+
"	}\n"+
"\n"+
"CloudStringG = CloudStringF.join(' ');\n"+
"\n"+
"CloudStringH = '      ]	                                        \\n' +\n"+
"'     }	                                                        \\n' +\n"+
"'#########################################################      \\n';\n"+
"\n"+
"CloudString = CloudStringA + CloudStringG + CloudStringH;\n"+
"\n"+
"\n"+
"\n"+
"newNode = Browser.createVrmlFromString(CloudString);\n"+
"Cumulus.children[i] = newNode[0];\n"+
"\n"+
"\n"+
"   }\n"+
"\n"+
"}\n"+
"\n"+
"function cirrus()\n"+
"\n"+
"{\n"+
"\n"+
"var maxi = 2;  // number of clouds\n"+
"\n"+
"var maxj = 5; // denotes how many portions affecting the size of the cloud\n"+
"\n"+
"var maxk = 8;  // number of billboards indicating cloud density\n"+
"\n"+
"var sectionradius = 1000;  //radius of individual cloud sections\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"for (var i=0; i < maxi; i++) \n"+
"{\n"+
"\n"+
"\n"+
"\n"+
"CloudStringA = '	Transform {		 \\n' +\n"+
"'    scale '+ cirrusscale() + '               	 \\n' +\n"+
"'    translation '+ cirrustranslation() + '      \\n' +    // cloud placement\n"+
"'    children [	                                 \\n';\n"+
"\n"+
"\n"+
"CloudStringB = new Array();\n"+
"CloudStringF = new Array();\n"+
"\n"+
"   	for (var j=0; j < maxj; j++)\n"+
"   	{\n"+
"\n"+
"	radius = 0;\n"+
"\n"+
"	CloudStringB[j]= '  Transform {		    	      \\n' +\n"+
"	'    translation '+ cirrussectiontranslation() + '    \\n' +     // section placement\n"+
"	'    children [	                                      \\n';\n"+
"\n"+
"	\n"+
"	CloudStringC = new Array();\n"+
"\n"+
"      		for (var k=1; k < maxk; k++)  // maxk value denotes how many textured billboards make up the cloud \n"+
"      		{\n"+
"\n"+
"\n"+
"		randomtheta = 6.28319*Math.random();\n"+
"		randomphi = 1.57079*Math.random();\n"+
"		radius = radius+(sectionradius/maxk); // radius incremental steps based on section radius and max billboards\n"+
"\n"+
"		X = radius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"		Z = radius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"		Y = radius*Math.cos(randomphi);\n"+
"		\n"+
"		Billboardtranslation = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"		CloudStringC[k] = '	Transform {		                \\n' +\n"+
"		'            translation '+ Billboardtranslation   + '          \\n' +     // random billboard placement within radius designated above\n"+
"		'	  children [	                                        \\n' +\n"+
"		'	      Billboard {	                                \\n' +\n"+
"		'	        axisOfRotation 0 0 0	                        \\n' +     // 0 0 0 designates rotation on all axis\n"+
"		'	        children [	                                \\n' +\n"+
"		'	            Transform {	                		\\n' +\n"+
"		'	              rotation '  + rotation() + '	        \\n' +\n"+
"		'	              children [	                        \\n' +\n"+
"		'	                  Shape {	                        \\n' +\n"+
"		'	                    appearance Appearance {	        \\n' +\n"+
"		'			    material Material {			\\n' +\n"+
"		'			    }					\\n' +\n"+
" 		'	                      texture ImageTexture {	        \\n' +\n"+
"		'	                        url [\\\"cloudtexture3.png\\\" \\\"https://savage.nps.edu/Savage/Environment/cloudtexture1_4.png\\\" ] \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                    geometry IndexedFaceSet {	        \\n' +     // define type of geometry to texture\n"+
"		'	                      coordIndex [ 0, 1, 2, 3 ]	        \\n' +\n"+
"		'			      solid FALSE		        \\n' +\n"+
"		'	                      coord Coordinate {	        \\n' +\n"+
"		'	                        point [ 500 500 0,	        \\n' +     // define size of the geometry. Here 100 meter 2D square.\n"+
"		'	                                500 -500 0,	        \\n' +\n"+
"		'	                               -500 -500 0,	        \\n' +\n"+
"		'	                               -500 500 0 ]	        \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                  }	                                \\n' +\n"+
"		'	              ]	                                        \\n' +\n"+
"		'	            }	                                        \\n' +\n"+
"		'	       ]	                                        \\n' +\n"+
"		'	   }	                                                \\n' +\n"+
"		'      ]	                                                \\n' +\n"+
"		'     }	                                                        \\n';      \n"+
"		\n"+
"\n"+
"		}\n"+
"\n"+
"	CloudStringD = CloudStringC.join(' ');\n"+
"\n"+
"	CloudStringE = '   ]	                 \\n' +\n"+
"	'	}	                         \\n';\n"+
"\n"+
"	CloudStringF[j] = CloudStringB[j] + CloudStringD +CloudStringE;\n"+
"\n"+
"\n"+
"	}\n"+
"\n"+
"CloudStringG = CloudStringF.join(' ');\n"+
"\n"+
"CloudStringH = '      ]	                                        \\n' +\n"+
"'     }	                                                        \\n' +\n"+
"'#########################################################      \\n';\n"+
"\n"+
"CloudString = CloudStringA + CloudStringG + CloudStringH;\n"+
"\n"+
"\n"+
"\n"+
"newNode = Browser.createVrmlFromString(CloudString);\n"+
"Cirrus.children[i] = newNode[0];\n"+
"\n"+
"  }\n"+
"\n"+
"}\n"+
"\n"+
"\n"+
"function initialize()\n"+
"\n"+
"{\n"+
"\n"+
"cumulus();\n"+
"\n"+
"cirrus();\n"+
"}\n"+
"'''

Group28.children.append(Script32)
DirectionalLight38 = x3d.DirectionalLight()
DirectionalLight38.ambientIntensity = 1
DirectionalLight38.color = [1,0,0]
DirectionalLight38.direction = [-1,-1,0]
DirectionalLight38.global_ = True

Group28.children.append(DirectionalLight38)

Scene11.children.append(Group28)

X3D0.Scene = Scene11
f = open("CloudsProcedural4_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
