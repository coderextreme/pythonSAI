import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("browser.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/browser.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a script test with embedded \\n between single quotes, a double backslash \\\\ a backslash \\ and a closing quote \"") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ScriptObject() \
     .setDEF("Browser") \
     .setSourceCode('''ecmascript:\n"+
"                function initialize() {\n"+
"		    Browser.print('DUDES\\n'+'\"DUDETTES');\n"+
"                }''')
    ) \
    .addChild(ScriptObject() \
     .setDEF("Clouds") \
     .setSourceCode('''ecmascript:\n"+
"\n"+
"\n"+
"function cumulustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"var xxx = ' '+' '+\n"+
"'	Transform		\\n'+\n"+
"'    ' + '               	\\n';\n"+
"\n"+
"}''')
    ) \
   ) \

X3D0.toFileX3D("./future/./browser.newf.x3d")
