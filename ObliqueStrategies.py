import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setContent("ObliqueStrategies.x3d")
meta2.setName("title")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setContent("Text scripting and animation example using Oblique Strategies card set by Brian Eno.")
meta3.setName("description")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setContent("Don Brutzman, John Kelly, Ben Cheng")
meta4.setName("creator")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setContent("3 November 2013")
meta5.setName("created")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setContent("18 October 2015")
meta6.setName("modified")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setContent("oblique.html")
meta7.setName("reference")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setContent("ObliqueStrategies.txt")
meta8.setName("reference")

head1.addMeta(meta8)
meta9 = x3d.meta()
meta9.setContent("ObliqueStrategiesScript.js")
meta9.setName("reference")

head1.addMeta(meta9)
meta10 = x3d.meta()
meta10.setContent("http://music.hyperreal.org/artists/brian_eno/oblique/oblique.html")
meta10.setName("reference")

head1.addMeta(meta10)
meta11 = x3d.meta()
meta11.setContent("http://www.eno-web.co.uk/obliques.html")
meta11.setName("reference")

head1.addMeta(meta11)
meta12 = x3d.meta()
meta12.setContent("http://gothpunk.com/haiku-intro.html")
meta12.setName("reference")

head1.addMeta(meta12)
meta13 = x3d.meta()
meta13.setContent("http://www.rtqe.net/ObliqueStrategies/OSintro.html")
meta13.setName("reference")

head1.addMeta(meta13)
meta14 = x3d.meta()
meta14.setContent("https://en.wikipedia.org/wiki/Oblique_Strategies")
meta14.setName("reference")

head1.addMeta(meta14)
meta15 = x3d.meta()
meta15.setContent("Brian Eno, Oblique Strategies")
meta15.setName("subject")

head1.addMeta(meta15)
meta16 = x3d.meta()
meta16.setContent("images/ObliqueStrategiesEntryScreen.png")
meta16.setName("Image")

head1.addMeta(meta16)
meta17 = x3d.meta()
meta17.setContent("http://translate.google.com/translate_tts?tl=en&q=hello%20X3D")
meta17.setName("audio")

head1.addMeta(meta17)
meta18 = x3d.meta()
meta18.setContent("translate_tts_HelloX3D.mp3")
meta18.setName("audio")

head1.addMeta(meta18)
meta19 = x3d.meta()
meta19.setContent("translate_tts_HelloX3D.wav")
meta19.setName("audio")

head1.addMeta(meta19)
meta20 = x3d.meta()
meta20.setContent("multiliingual translation parameter")
meta20.setName("TODO")

head1.addMeta(meta20)
meta21 = x3d.meta()
meta21.setContent("http://stackoverflow.com/questions/9163988/download-mp3-from-google-translate-text-to-speech")
meta21.setName("reference")

head1.addMeta(meta21)
meta22 = x3d.meta()
meta22.setContent("http://www.greenbot.com/article/2105862/how-to-get-started-with-google-text-to-speech.html")
meta22.setName("reference")

head1.addMeta(meta22)
meta23 = x3d.meta()
meta23.setContent("under development, scene Sound/AudioClip triggering (or retrieved file format) not working")
meta23.setName("warning")

head1.addMeta(meta23)
meta24 = x3d.meta()
meta24.setContent("BSContact error: Script node TextScript: parse error: line 15 \" var strategy = [];")
meta24.setName("warning")

head1.addMeta(meta24)
meta25 = x3d.meta()
meta25.setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/Inspiration/ObliqueStrategies.x3d")
meta25.setName("identifier")

head1.addMeta(meta25)
meta26 = x3d.meta()
meta26.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
meta26.setName("generator")

head1.addMeta(meta26)
meta27 = x3d.meta()
meta27.setContent("../license.html")
meta27.setName("license")

head1.addMeta(meta27)

X3D0.setHead(head1)
Scene28 = x3d.Scene()
NavigationInfo29 = x3d.NavigationInfo()
NavigationInfo29.setType(["EXAMINE","ANY"])

Scene28.addChildren(NavigationInfo29)
Background30 = x3d.Background()
Background30.setSkyColor([0.419608,0.427451,1])

Scene28.addChildren(Background30)
Transform31 = x3d.Transform()
Transform31.setScale([0.4,0.4,0.4])
Transform31.setTranslation([0,1,0])
TouchSensor32 = x3d.TouchSensor()
TouchSensor32.setDEF("RandomTextClickedSensor")
TouchSensor32.setDescription("Select to see a new strategy")

Transform31.addChildren(TouchSensor32)
Shape33 = x3d.Shape()
Text34 = x3d.Text()
Text34.setString(["Oblique Strategies","","(Over One Hundred Worthwhile Dilemmas)","","by Brian Eno and Peter Schmidt"])
FontStyle35 = x3d.FontStyle()
FontStyle35.setDEF("MessageFont")
FontStyle35.setFamily(["SANS"])
FontStyle35.setJustify(["MIDDLE","MIDDLE"])
FontStyle35.setStyle("BOLD")

Text34.setFontStyle(FontStyle35)

Shape33.setGeometry(Text34)
Appearance36 = x3d.Appearance()
Material37 = x3d.Material()
Material37.setDiffuseColor([1,1,1])

Appearance36.setMaterial(Material37)

Shape33.setAppearance(Appearance36)

Transform31.addChildren(Shape33)
Transform38 = x3d.Transform()
Transform38.setScale([10,3,1])
Shape39 = x3d.Shape()
Shape39.setDEF("HeadlineClickSurface")
IndexedFaceSet40 = x3d.IndexedFaceSet()
IndexedFaceSet40.setCoordIndex([0,1,2,3,-1])
IndexedFaceSet40.setSolid(False)
Coordinate41 = x3d.Coordinate()
Coordinate41.setPoint([1,1,0,1,-1,0,-1,-1,0,-1,1,0])

IndexedFaceSet40.setCoord(Coordinate41)

Shape39.setGeometry(IndexedFaceSet40)
Appearance42 = x3d.Appearance()
Material43 = x3d.Material()
Material43.setAmbientIntensity(0.245763)
Material43.setDiffuseColor([0.34773,0.090909,0.005289])
Material43.setShininess(0.07)
Material43.setSpecularColor([0.336735,0.051091,0.051091])
Material43.setTransparency(0.8)

Appearance42.setMaterial(Material43)

Shape39.setAppearance(Appearance42)

Transform38.addChildren(Shape39)

Transform31.addChildren(Transform38)

Scene28.addChildren(Transform31)
Script44 = x3d.Script()
Script44.setDEF("TextScript")
Script44.setUrl(["../node/ObliqueStrategiesScript.js"])
# initialize() method includes unit test to printAllStrategies() to console 
# TODO insert field definitions here (index string_changed previous next random) and then animate! 
field45 = x3d.field()
field45.setAccessType("initializeOnly")
field45.setAppinfo("index for active strategy card, -1 means no selection")
field45.setName("index")
field45.setType("SFInt32")
field45.setValue("0")

Script44.addField(field45)
field46 = x3d.field()
field46.setAccessType("outputOnly")
field46.setAppinfo("latest strategy card value")
field46.setName("string_changed")
field46.setType("MFString")

Script44.addField(field46)
field47 = x3d.field()
field47.setAccessType("outputOnly")
field47.setAppinfo("url to invoke Google Translate")
field47.setName("textToSpeechUrl")
field47.setType("MFString")

Script44.addField(field47)
field48 = x3d.field()
field48.setAccessType("outputOnly")
field48.setAppinfo("activate Sound node")
field48.setName("newCardTime")
field48.setType("SFTime")

Script44.addField(field48)
field49 = x3d.field()
field49.setAccessType("inputOnly")
field49.setName("selectPreviousCard")
field49.setType("SFBool")

Script44.addField(field49)
field50 = x3d.field()
field50.setAccessType("inputOnly")
field50.setName("selectNextCard")
field50.setType("SFBool")

Script44.addField(field50)
field51 = x3d.field()
field51.setAccessType("inputOnly")
field51.setName("selectRandomCard")
field51.setType("SFBool")

Script44.addField(field51)
field52 = x3d.field()
field52.setAccessType("initializeOnly")
field52.setAppinfo("controls console tracing")
field52.setName("traceEnabled")
field52.setType("SFBool")
field52.setValue("true")

Script44.addField(field52)

Scene28.addChildren(Script44)
Transform53 = x3d.Transform()
Transform53.setDEF("CardTransform")
Transform53.setScale([0.4,0.4,0.4])
Transform53.setTranslation([0,-1.5,0])
Shape54 = x3d.Shape()
Text55 = x3d.Text()
Text55.setDEF("CardText")
FontStyle56 = x3d.FontStyle()
FontStyle56.setFamily(["SANS"])
FontStyle56.setJustify(["MIDDLE","MIDDLE"])
FontStyle56.setStyle("BOLD")

Text55.setFontStyle(FontStyle56)

Shape54.setGeometry(Text55)
Appearance57 = x3d.Appearance()
Material58 = x3d.Material()
Material58.setDiffuseColor([1,1,1])

Appearance57.setMaterial(Material58)

Shape54.setAppearance(Appearance57)

Transform53.addChildren(Shape54)
ROUTE59 = x3d.ROUTE()
ROUTE59.setFromField("string_changed")
ROUTE59.setFromNode("TextScript")
ROUTE59.setToField("string")
ROUTE59.setToNode("CardText")

Transform53.addChildren(ROUTE59)
Sound60 = x3d.Sound()
Sound60.setDEF("CardSoundSpatialization")
Sound60.setMaxBack(100)
Sound60.setMaxFront(100)
Sound60.setMinBack(20)
Sound60.setMinFront(20)
# Make sure the sound source AudioClip is audible at the user location 
# Not all X3D players seem to use the .mp3 
# &#38; is ampersand character, avoids escaping problems and inconsistencies in browsers and X3D players 
# %20 is space character used in uri/url encoding 
AudioClip61 = x3d.AudioClip()
AudioClip61.setDEF("TextToSpeechAudioClip")
AudioClip61.setDescription("sends strategy text google translate")
AudioClip61.setUrl(["http://translate.google.com/translate_tts?tl=en&q=Feed%20the%20recording%20back%20out%20of%20the%20medium","translate_tts_mp3FileFormatNotSupported.wav"])

Sound60.setSource(AudioClip61)

Transform53.addChildren(Sound60)
ROUTE62 = x3d.ROUTE()
ROUTE62.setFromField("textToSpeechUrl")
ROUTE62.setFromNode("TextScript")
ROUTE62.setToField("url")
ROUTE62.setToNode("TextToSpeechAudioClip")

Transform53.addChildren(ROUTE62)
ROUTE63 = x3d.ROUTE()
ROUTE63.setFromField("newCardTime")
ROUTE63.setFromNode("TextScript")
ROUTE63.setToField("startTime")
ROUTE63.setToNode("TextToSpeechAudioClip")

Transform53.addChildren(ROUTE63)

Scene28.addChildren(Transform53)
Transform64 = x3d.Transform()
Transform64.setScale([0.4,0.4,0.4])
Transform64.setTranslation([-3.2,2.5,0])
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.setDEF("PreviousTextClickedSensor")
TouchSensor65.setDescription("Select to see previous strategy")

Transform64.addChildren(TouchSensor65)
ROUTE66 = x3d.ROUTE()
ROUTE66.setFromField("isActive")
ROUTE66.setFromNode("PreviousTextClickedSensor")
ROUTE66.setToField("selectPreviousCard")
ROUTE66.setToNode("TextScript")

Transform64.addChildren(ROUTE66)
Shape67 = x3d.Shape()
Text68 = x3d.Text()
Text68.setString(["previous"])
FontStyle69 = x3d.FontStyle()
FontStyle69.setUSE("MessageFont")

Text68.setFontStyle(FontStyle69)

Shape67.setGeometry(Text68)
Appearance70 = x3d.Appearance()
Appearance70.setDEF("InterfaceAppearance")
Material71 = x3d.Material()
Material71.setDiffuseColor([1,0,0.6])

Appearance70.setMaterial(Material71)

Shape67.setAppearance(Appearance70)

Transform64.addChildren(Shape67)
Transform72 = x3d.Transform()
Transform72.setScale([2,0.6,1])
Shape73 = x3d.Shape()
Shape73.setDEF("TransparentClickSurface")
# support Selectable Text with a scalable IFS 
IndexedFaceSet74 = x3d.IndexedFaceSet()
IndexedFaceSet74.setCoordIndex([0,1,2,3,-1])
IndexedFaceSet74.setSolid(False)
Coordinate75 = x3d.Coordinate()
Coordinate75.setPoint([1,1,0,1,-1,0,-1,-1,0,-1,1,0])

IndexedFaceSet74.setCoord(Coordinate75)

Shape73.setGeometry(IndexedFaceSet74)
Appearance76 = x3d.Appearance()
Material77 = x3d.Material()
Material77.setTransparency(1)

Appearance76.setMaterial(Material77)

Shape73.setAppearance(Appearance76)

Transform72.addChildren(Shape73)

Transform64.addChildren(Transform72)

Scene28.addChildren(Transform64)
Transform78 = x3d.Transform()
Transform78.setScale([0.4,0.4,0.4])
Transform78.setTranslation([3.5,2.5,0])
TouchSensor79 = x3d.TouchSensor()
TouchSensor79.setDEF("NextTextClickedSensor")
TouchSensor79.setDescription("Select to see next strategy")

Transform78.addChildren(TouchSensor79)
ROUTE80 = x3d.ROUTE()
ROUTE80.setFromField("isActive")
ROUTE80.setFromNode("NextTextClickedSensor")
ROUTE80.setToField("selectNextCard")
ROUTE80.setToNode("TextScript")

Transform78.addChildren(ROUTE80)
Shape81 = x3d.Shape()
Text82 = x3d.Text()
Text82.setString(["next"])
FontStyle83 = x3d.FontStyle()
FontStyle83.setUSE("MessageFont")

Text82.setFontStyle(FontStyle83)

Shape81.setGeometry(Text82)
Appearance84 = x3d.Appearance()
Appearance84.setUSE("InterfaceAppearance")

Shape81.setAppearance(Appearance84)

Transform78.addChildren(Shape81)
Transform85 = x3d.Transform()
Transform85.setScale([1.2,0.6,1])
Shape86 = x3d.Shape()
Shape86.setUSE("TransparentClickSurface")

Transform85.addChildren(Shape86)

Transform78.addChildren(Transform85)

Scene28.addChildren(Transform78)
Transform87 = x3d.Transform()
Transform87.setScale([0.4,0.4,0.4])
Transform87.setTranslation([-3.3,-0.5,0])
TouchSensor88 = x3d.TouchSensor()
TouchSensor88.setUSE("RandomTextClickedSensor")

Transform87.addChildren(TouchSensor88)
ROUTE89 = x3d.ROUTE()
ROUTE89.setFromField("isActive")
ROUTE89.setFromNode("RandomTextClickedSensor")
ROUTE89.setToField("selectRandomCard")
ROUTE89.setToNode("TextScript")

Transform87.addChildren(ROUTE89)
Shape90 = x3d.Shape()
Text91 = x3d.Text()
Text91.setString(["random"])
FontStyle92 = x3d.FontStyle()
FontStyle92.setUSE("MessageFont")

Text91.setFontStyle(FontStyle92)

Shape90.setGeometry(Text91)
Appearance93 = x3d.Appearance()
Appearance93.setUSE("InterfaceAppearance")

Shape90.setAppearance(Appearance93)

Transform87.addChildren(Shape90)
Transform94 = x3d.Transform()
Transform94.setScale([1.8,0.6,1])
Shape95 = x3d.Shape()
Shape95.setUSE("TransparentClickSurface")

Transform94.addChildren(Shape95)

Transform87.addChildren(Transform94)

Scene28.addChildren(Transform87)
Transform96 = x3d.Transform()
Transform96.setScale([0.4,0.4,0.4])
Transform96.setTranslation([3.3,-0.5,0])
Anchor97 = x3d.Anchor()
Anchor97.setDEF("TextToSpeechAnchor")
Anchor97.setDescription("text to speech in browser")
Anchor97.setParameter(["target=_blank"])
Anchor97.setUrl(["http://translate.google.com/translate_tts?tl=en&q=Overtly%20resist%20change"])
ROUTE98 = x3d.ROUTE()
ROUTE98.setFromField("textToSpeechUrl")
ROUTE98.setFromNode("TextScript")
ROUTE98.setToField("url")
ROUTE98.setToNode("TextToSpeechAnchor")

Anchor97.addChildren(ROUTE98)
Shape99 = x3d.Shape()
Text100 = x3d.Text()
Text100.setString(["speech"])
FontStyle101 = x3d.FontStyle()
FontStyle101.setUSE("MessageFont")

Text100.setFontStyle(FontStyle101)

Shape99.setGeometry(Text100)
Appearance102 = x3d.Appearance()
Appearance102.setUSE("InterfaceAppearance")

Shape99.setAppearance(Appearance102)

Anchor97.addChildren(Shape99)
Transform103 = x3d.Transform()
Transform103.setScale([1.8,0.6,1])
Shape104 = x3d.Shape()
Shape104.setUSE("TransparentClickSurface")

Transform103.addChildren(Shape104)

Anchor97.addChildren(Transform103)

Transform96.addChildren(Anchor97)

Scene28.addChildren(Transform96)

X3D0.setScene(Scene28)
X3D0.toFileX3D("ObliqueStrategies_RoundTrip.x3d")
