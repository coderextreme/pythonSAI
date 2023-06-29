print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Full"
X3D0.version = "4.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "AllAudioGraphNodesTest.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "List of all X3D4 audio graph nodes to test infrastructure and validation support. Absence of attributes means that checking and removal of default values is working."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "25 October 2020"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "26 November 2021"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "warning"
meta7.content = "Developmental test, no actual 3D model expected"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "identifier"
meta8.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/AllAudioGraphNodesTest.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "generator"
meta9.content = "X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "license"
meta10.content = "../license.html"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
WorldInfo12 = x3d.WorldInfo()
WorldInfo12.title = "AllAudioGraphNodes.x3d"

Scene11.children.append(WorldInfo12)
Shape13 = x3d.Shape()
Box14 = x3d.Box()

Shape13.geometry = Box14
Appearance15 = x3d.Appearance()
AcousticProperties16 = x3d.AcousticProperties()
AcousticProperties16.description = "Testing of X3D4 nodes demonstrating W3C Audio API in progress"
AcousticProperties16.diffuse = 0.25
AcousticProperties16.refraction = 0.5
AcousticProperties16.specular = 1

Appearance15.acousticProperties = AcousticProperties16
Material17 = x3d.Material()

Appearance15.material = Material17

Shape13.appearance = Appearance15

Scene11.children.append(Shape13)
Sound18 = x3d.Sound()
Sound18.location = [0,1.6,0]
AudioClip19 = x3d.AudioClip()
AudioClip19.description = "testing"
AudioClip19.url = ["sound/saxophone.mp3","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/sound/saxophone.mp3"]

Sound18.source = AudioClip19

Scene11.children.append(Sound18)
Sound20 = x3d.Sound()
Sound20.location = [0,1.6,0]
MovieTexture21 = x3d.MovieTexture()
MovieTexture21.description = "testing"
MovieTexture21.url = ["bogus.mpg","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/bogus.mpg"]

Sound20.source = MovieTexture21

Scene11.children.append(Sound20)
SpatialSound22 = x3d.SpatialSound()
SpatialSound22.distanceModel = "INVERSE"
Analyser23 = x3d.Analyser()
Analyser23.channelCountMode = "MAX"
Analyser23.channelInterpretation = "SPEAKERS"
StreamAudioDestination24 = x3d.StreamAudioDestination()
StreamAudioDestination24.channelCountMode = "MAX"
StreamAudioDestination24.channelInterpretation = "SPEAKERS"
BiquadFilter25 = x3d.BiquadFilter()
BiquadFilter25.channelCountMode = "MAX"
BiquadFilter25.channelInterpretation = "SPEAKERS"
BiquadFilter25.type = "LOWPASS"
ChannelMerger26 = x3d.ChannelMerger()
ChannelMerger26.channelCountMode = "MAX"
ChannelMerger26.channelInterpretation = "SPEAKERS"
ChannelSelector27 = x3d.ChannelSelector()
ChannelSelector27.channelCountMode = "MAX"
ChannelSelector27.channelInterpretation = "SPEAKERS"
ChannelSplitter28 = x3d.ChannelSplitter()
ChannelSplitter28.channelCountMode = "MAX"
ChannelSplitter28.channelInterpretation = "SPEAKERS"
Convolver29 = x3d.Convolver()
Convolver29.channelCountMode = "MAX"
Convolver29.channelInterpretation = "SPEAKERS"
Delay30 = x3d.Delay()
Delay30.channelCountMode = "MAX"
Delay30.channelInterpretation = "SPEAKERS"
DynamicsCompressor31 = x3d.DynamicsCompressor()
DynamicsCompressor31.channelCountMode = "MAX"
DynamicsCompressor31.channelInterpretation = "SPEAKERS"
Gain32 = x3d.Gain()
Gain32.channelCountMode = "MAX"
Gain32.channelInterpretation = "SPEAKERS"
StreamAudioDestination33 = x3d.StreamAudioDestination()
StreamAudioDestination33.channelCountMode = "MAX"
StreamAudioDestination33.channelInterpretation = "SPEAKERS"
WaveShaper34 = x3d.WaveShaper()
WaveShaper34.channelCountMode = "MAX"
WaveShaper34.channelInterpretation = "SPEAKERS"
#The following X3DSoundSourceNode nodes have no audio-graph children
BufferAudioSource35 = x3d.BufferAudioSource()
BufferAudioSource35.channelCountMode = "MAX"
BufferAudioSource35.channelInterpretation = "SPEAKERS"

WaveShaper34.children.append(BufferAudioSource35)
ListenerPointSource36 = x3d.ListenerPointSource()

WaveShaper34.children.append(ListenerPointSource36)
MicrophoneSource37 = x3d.MicrophoneSource()

WaveShaper34.children.append(MicrophoneSource37)
OscillatorSource38 = x3d.OscillatorSource()
OscillatorSource38.frequency = 440

WaveShaper34.children.append(OscillatorSource38)
StreamAudioSource39 = x3d.StreamAudioSource()
StreamAudioSource39.channelCountMode = "MAX"
StreamAudioSource39.channelInterpretation = "SPEAKERS"

WaveShaper34.children.append(StreamAudioSource39)

StreamAudioDestination33.children.append(WaveShaper34)

Gain32.children.append(StreamAudioDestination33)

DynamicsCompressor31.children.append(Gain32)

Delay30.children.append(DynamicsCompressor31)

Convolver29.children.append(Delay30)

ChannelSplitter28.outputs.append(Convolver29)

ChannelSelector27.children.append(ChannelSplitter28)

ChannelMerger26.children.append(ChannelSelector27)

BiquadFilter25.children.append(ChannelMerger26)

StreamAudioDestination24.children.append(BiquadFilter25)

Analyser23.children.append(StreamAudioDestination24)

SpatialSound22.children.append(Analyser23)

Scene11.children.append(SpatialSound22)

X3D0.Scene = Scene11
f = open("././AllAudioGraphNodesTest_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
