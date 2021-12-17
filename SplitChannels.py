from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Full")
X3D0.setVersion("4.0")
head1 = head()
meta2 = meta()
meta2.setName("title")
meta2.setContent("SplitChannels.x3d")

head1.addMeta(meta2)
meta3 = meta()
meta3.setName("description")
meta3.setContent("This X3D scene includes a simple sound source which can be moved right and left. Depending on the position of the sound source, the user can hear the produced sound from the corresponding output speaker. Accordingly, there is a source that can be passed through a SpatialSound for the spatialization of the input audio. The approach is based on the relative position of the source and the listener, in comparison to the panner.")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("info")
meta4.setContent("This work presents an innovative solution of the spatial sound in X3DOM framework, that based on a combinational methodology. Specifically, we suggested the enrichment of X3DOM with spatial sound features, using both the X3D sound nodes and the structure of Web Audio API.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("creator")
meta5.setContent("Efi Lakka, Athanasios Malamos, Dick Puk, Don Brutzman")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("created")
meta6.setContent("28 October 2020")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("modified")
meta7.setContent("5 December 2021")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("reference")
meta8.setContent("CHANGELOG.txt")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("TODO")
meta9.setContent("credit for audio files")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("reference")
meta10.setContent("http://www.medialab.hmu.gr/minipages/x3domAudio")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("identifier")
meta11.setContent("https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/SplitChannels.x3d")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("generator")
meta12.setContent("X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("license")
meta13.setContent("../license.html")

head1.addMeta(meta13)

X3D0.setHead(head1)
Scene14 = Scene()
WorldInfo15 = WorldInfo()
WorldInfo15.setTitle("SplitChannels.x3d")

Scene14.addChildren(WorldInfo15)
NavigationInfo16 = NavigationInfo()
NavigationInfo16.setType(["ON"])

Scene14.addChildren(NavigationInfo16)
Background17 = Background()
Background17.setSkyColor([0.2,0.2,0.21])

Scene14.addChildren(Background17)
Viewpoint18 = Viewpoint()
Viewpoint18.setOrientation([1,0,0,-0.5])
Viewpoint18.setPosition([0,500,600])
Viewpoint18.setRetainUserOffsets(True)

Scene14.addChildren(Viewpoint18)
Transform19 = Transform()
Transform19.setDEF("PowerR")
Transform19.setTranslation([100,400,400])
Transform20 = Transform()
Transform20.setRotation([1,0,0,-0.5])
Transform20.setTranslation([0,40,0])
Shape21 = Shape()
Appearance22 = Appearance()
Appearance22.setDEF("audio_emit")
Material23 = Material()
Material23.setDiffuseColor([0,1,0])
Material23.setEmissiveColor([0.8,0.8,0.8])
Material23.setSpecularColor([0.01,0.01,0.01])

Appearance22.setMaterial(Material23)

Shape21.setAppearance(Appearance22)
Box24 = Box()
Box24.setSize([10,80,0.01])

Shape21.setGeometry(Box24)

Transform20.addChildren(Shape21)

Transform19.addChildren(Transform20)
Transform25 = Transform()
Transform25.setRotation([1,0,0,-0.5])
Transform25.setTranslation([-2.7,37,0])
Shape26 = Shape()
Appearance27 = Appearance()
Appearance27.setDEF("audio_emit2")
Material28 = Material()
Material28.setDiffuseColor([0,1,0])
Material28.setEmissiveColor([0.8,0.8,0.8])
Material28.setSpecularColor([0.01,0.01,0.01])

Appearance27.setMaterial(Material28)
ImageTexture29 = ImageTexture()
ImageTexture29.setUrl(["images/line.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/line.png"])

Appearance27.setTexture(ImageTexture29)

Shape26.setAppearance(Appearance27)
Box30 = Box()
Box30.setSize([25,83,0.01])

Shape26.setGeometry(Box30)

Transform25.addChildren(Shape26)

Transform19.addChildren(Transform25)
Transform31 = Transform()
Transform31.setDEF("volumeRight")
Transform31.setRotation([1,0,0,-0.5])
Transform31.setScale([10,10,10])
Transform31.setTranslation([0,-10,0])
Shape32 = Shape()
Appearance33 = Appearance()
Material34 = Material()
Material34.setAmbientIntensity(0.0933)
Material34.setDiffuseColor([0.345,0.345,0.882])
Material34.setShininess(0.51)
Material34.setSpecularColor([0.46,0.46,0.46])

Appearance33.setMaterial(Material34)

Shape32.setAppearance(Appearance33)
Text35 = Text()
Text35.setString(["Right Channel Volume"])
FontStyle36 = FontStyle()
FontStyle36.setFamily(["Times"])
FontStyle36.setStyle("BOLD")

Text35.setFontStyle(FontStyle36)

Shape32.setGeometry(Text35)

Transform31.addChildren(Shape32)

Transform19.addChildren(Transform31)

Scene14.addChildren(Transform19)
Transform37 = Transform()
Transform37.setDEF("PowerL")
Transform37.setTranslation([-100,400,400])
Transform38 = Transform()
Transform38.setRotation([1,0,0,-0.5])
Transform38.setTranslation([0,40,0])
Shape39 = Shape()
Appearance40 = Appearance()
Appearance40.setDEF("audio_emit3")
Material41 = Material()
Material41.setDiffuseColor([0,1,0])
Material41.setEmissiveColor([0.8,0.8,0.8])
Material41.setSpecularColor([0.01,0.01,0.01])

Appearance40.setMaterial(Material41)

Shape39.setAppearance(Appearance40)
Box42 = Box()
Box42.setSize([10,80,0.01])

Shape39.setGeometry(Box42)

Transform38.addChildren(Shape39)

Transform37.addChildren(Transform38)
Transform43 = Transform()
Transform43.setRotation([1,0,0,-0.5])
Transform43.setTranslation([13.2,37,0])
Shape44 = Shape()
Appearance45 = Appearance()
Appearance45.setDEF("audio_emit4")
Material46 = Material()
Material46.setDiffuseColor([0,1,0])
Material46.setEmissiveColor([0.8,0.8,0.8])
Material46.setSpecularColor([0.01,0.01,0.01])

Appearance45.setMaterial(Material46)
ImageTexture47 = ImageTexture()
ImageTexture47.setUrl(["images/line.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/line.png"])

Appearance45.setTexture(ImageTexture47)

Shape44.setAppearance(Appearance45)
Box48 = Box()
Box48.setSize([25,83,0.01])

Shape44.setGeometry(Box48)

Transform43.addChildren(Shape44)

Transform37.addChildren(Transform43)
Transform49 = Transform()
Transform49.setDEF("volumeLeft")
Transform49.setRotation([1,0,0,-0.5])
Transform49.setScale([10,10,10])
Transform49.setTranslation([0,-10,0])
Shape50 = Shape()
Appearance51 = Appearance()
Material52 = Material()
Material52.setAmbientIntensity(0.0933)
Material52.setDiffuseColor([0.345,0.345,0.882])
Material52.setShininess(0.51)
Material52.setSpecularColor([0.46,0.46,0.46])

Appearance51.setMaterial(Material52)

Shape50.setAppearance(Appearance51)
Text53 = Text()
Text53.setString(["Left Channel Volume"])
FontStyle54 = FontStyle()
FontStyle54.setFamily(["Times"])
FontStyle54.setStyle("BOLD")

Text53.setFontStyle(FontStyle54)

Shape50.setGeometry(Text53)

Transform49.addChildren(Shape50)

Transform37.addChildren(Transform49)

Scene14.addChildren(Transform37)
Transform55 = Transform()
Shape56 = Shape()
Appearance57 = Appearance()
Appearance57.setDEF("floor")
Material58 = Material()
Material58.setDiffuseColor([0.1,0.1,0.1])
Material58.setShininess(0.8)
Material58.setSpecularColor([0.5,0.6,0.7])

Appearance57.setMaterial(Material58)

Shape56.setAppearance(Appearance57)
Box59 = Box()
Box59.setSize([1500,10,500])

Shape56.setGeometry(Box59)

Transform55.addChildren(Shape56)

Scene14.addChildren(Transform55)
ListenerPointSource60 = ListenerPointSource()
ListenerPointSource60.setTrackCurrentView(True)

Scene14.addChildren(ListenerPointSource60)
StreamAudioDestination61 = StreamAudioDestination()
Gain62 = Gain()
ChannelMerger63 = ChannelMerger()
ChannelSelector64 = ChannelSelector()
Gain65 = Gain()
Gain65.setUSE("ChannelSplitter")

ChannelSelector64.addChildren(Gain65)

ChannelMerger63.addChildren(ChannelSelector64)
ChannelSelector66 = ChannelSelector()
ChannelSelector66.setChannelSelection(1)
Gain67 = Gain()
Gain67.setUSE("ChannelSplitter")

ChannelSelector66.addChildren(Gain67)

ChannelMerger63.addChildren(ChannelSelector66)

Gain62.addChildren(ChannelMerger63)

StreamAudioDestination61.addChildren(Gain62)

Scene14.addChildren(StreamAudioDestination61)
ChannelSplitter68 = ChannelSplitter()
ChannelSplitter68.setDEF("ChannelSplitter")
ChannelSplitter68.setChannelCountMode("explicit")
AudioClip69 = AudioClip()
AudioClip69.setDescription("Violin")
AudioClip69.setUrl(["sound/violin.mp3","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/sound/violin.mp3"])

ChannelSplitter68.addOutputs(AudioClip69)

Scene14.addChildren(ChannelSplitter68)
Transform70 = Transform()
Transform70.setDEF("Audio3")
Transform70.setRotation([1,0,0,-0.5])
Transform70.setTranslation([0,100,0])
Shape71 = Shape()
Appearance72 = Appearance()
Appearance72.setDEF("audio_emit5")
Material73 = Material()
Material73.setDiffuseColor([0.3,1,0.3])
Material73.setEmissiveColor([0.8,0.8,0.8])
Material73.setSpecularColor([0.01,0.01,0.01])

Appearance72.setMaterial(Material73)
ImageTexture74 = ImageTexture()
ImageTexture74.setUrl(["images/loudspeaker.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/loudspeaker.png"])

Appearance72.setTexture(ImageTexture74)

Shape71.setAppearance(Appearance72)
Box75 = Box()
Box75.setSize([100,100,0.001])

Shape71.setGeometry(Box75)

Transform70.addChildren(Shape71)

Scene14.addChildren(Transform70)

X3D0.setScene(Scene14)
X3D0.toFileX3D("././SplitChannels_RoundTrip.x3d")