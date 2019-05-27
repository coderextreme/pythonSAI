import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("StringArrayEncodingExamples.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Demonstrate simple X3D MFString (string array) encoding.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("27 May 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("27 May 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("X3dHeaderPrototypeSyntaxExamples.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationSection")).setContent(x3dpsail.SFString("X3D encodings, ISO/IEC 19775-1, Part 1: Architecture and base components, 5 Field type reference, 5.3.14 SFString and MFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationUrl")).setContent(x3dpsail.SFString("http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/fieldsDef.html#SFStringAndMFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationSection")).setContent(x3dpsail.SFString("X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 5.3.14 SFString and MFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationUrl")).setContent(x3dpsail.SFString("http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/EncodingOfFields.html#SFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationSection")).setContent(x3dpsail.SFString("X3D encodings, ISO/IEC 19776-2 v3.3, Part 2: Classic VRML encoding, 5.15 SFString and MFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("specificationUrl")).setContent(x3dpsail.SFString("http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/EncodingOfFields.html#SFString")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamples.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("EntryView")).setDescription(x3dpsail.SFString("Hello MFString syntax")))
        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([0.6,1,0.8])))
        .addChild(x3dpsail.Shape()
          .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["One, Two, Three","","He said, \"Immel did it!\""]))
            #alternative XML encoding: Text string='\"One, Two, Three\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'

            #alternative Java source: .setString(new String [] {\"One, Two, Three\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})

            .setFontStyle(x3dpsail.FontStyle().setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"])).setStyle(x3dpsail.SFString("BOLD"))))
          .setAppearance(x3dpsail.Appearance()
            .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.6,0.4,0.2)))))))

X3D0.toFileX3D("./future/./StringArrayEncodingExamples_RoundTrip.x3d")
