import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("EnvironmentalEffects")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("EnvironmentalEffects")).setLevel(x3dpsail.SFInt32(3)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("ball.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/ball.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("a prismatic sphere"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo().setType(x3dpsail.MFString(["ANY","EXAMINE","FLY","LOOKAT"])))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Tour Views")))
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Sphere())
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5)))
              .setTexture(x3dpsail.ComposedCubeMapTexture().setDEF(x3dpsail.SFString("texture"))
                .setBack(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])))
                .setBottom(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])))
                .setFront(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])))
                .setLeft(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])))
                .setRight(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])))
                .setTop(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))))
              #<ProgramShader DEF='ProgramShader' containerField='shaders' language='GLSL'> <ShaderProgram url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' containerField='programs' type='VERTEX'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'/> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'/> </ShaderProgram> <ShaderProgram url='\"../shaders/freewrl.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.fs\"' containerField='programs' type='FRAGMENT'/> </ProgramShader>

              #<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='fw_Texture_unit0' type='SFNode' accessType=\"initializeOnly\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/contact.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/contact.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>

              #<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='inputOutput' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='scale' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='power' accessType='inputOutput' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/octaga.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/octaga.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>

              #<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' accessType='initializeOnly' type='SFInt32' value='0'></field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>

              #

              .addShaders(x3dpsail.ComposedShader().setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("inputOutput"))
                  .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setDEF(x3dpsail.SFString("common")).setUrl(x3dpsail.MFString(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
              .addShaders(x3dpsail.ComposedShader().setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("initializeOnly"))
                  .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUSE(x3dpsail.SFString("common")))))))))

X3D0.toFileX3D("./future/./ball_RoundTrip.x3d")
