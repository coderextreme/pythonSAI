print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "Figure31_9SpinGroupPrototype.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "Figure 31.9, The VRML 2.0 Sourcebook, Copyright [1997] By Andrea L. Ames, David R. Nadeau, and John L. Moreland"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "reference"
meta4.content = "http://www.wiley.com/legacy/compbooks/vrml2sbk/ch31/31fig09.htm"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "translator"
meta5.content = "Don Brutzman"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "24 October 2000"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "20 October 2019"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "description"
meta8.content = "The SpinGroup prototype is used to automatically spin a group of three long rectangular boxes. Click on blue crossbar to activate second SpinGroup."

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "identifier"
meta9.content = "https://www.web3d.org/x3d/content/examples/Vrml2Sourcebook/Chapter31Prototypes/Figure31_9SpinGroupPrototype.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "generator"
meta10.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "license"
meta11.content = "../../license.html"

head1.children.append(meta11)

X3D0.head = head1
Scene12 = x3d.Scene()
WorldInfo13 = x3d.WorldInfo()
WorldInfo13.title = "Figure31_9SpinGroupPrototype.x3d"

Scene12.children.append(WorldInfo13)
ProtoDeclare14 = x3d.ProtoDeclare()
ProtoDeclare14.name = "SpinGroup"
ProtoInterface15 = x3d.ProtoInterface()
field16 = x3d.field()
field16.name = "children"
field16.accessType = "inputOutput"
field16.type = "MFNode"
#NULL node initialization

ProtoInterface15.field.append(field16)
field17 = x3d.field()
field17.name = "cycleInterval"
field17.accessType = "inputOutput"
field17.type = "SFTime"
field17.value = 1

ProtoInterface15.field.append(field17)
field18 = x3d.field()
field18.name = "loop"
field18.accessType = "inputOutput"
field18.type = "SFBool"
field18.value = False

ProtoInterface15.field.append(field18)
field19 = x3d.field()
field19.name = "startTime"
field19.accessType = "inputOutput"
field19.type = "SFTime"
field19.value = 0

ProtoInterface15.field.append(field19)
field20 = x3d.field()
field20.name = "stopTime"
field20.accessType = "inputOutput"
field20.type = "SFTime"
field20.value = 0

ProtoInterface15.field.append(field20)

ProtoDeclare14.ProtoInterface = ProtoInterface15
ProtoBody21 = x3d.ProtoBody()
Transform22 = x3d.Transform()
Transform22.DEF = "SpinGroupTransform"
IS23 = x3d.IS()
connect24 = x3d.connect()
connect24.nodeField = "children"
connect24.protoField = "children"

IS23.connect.append(connect24)

Transform22.IS = IS23

ProtoBody21.children.append(Transform22)
#following nodes will not be rendered, only the first node of a ProtoBody is drawn
TimeSensor25 = x3d.TimeSensor()
TimeSensor25.DEF = "SpinGroupClock"
IS26 = x3d.IS()
connect27 = x3d.connect()
connect27.nodeField = "cycleInterval"
connect27.protoField = "cycleInterval"

IS26.connect.append(connect27)
connect28 = x3d.connect()
connect28.nodeField = "loop"
connect28.protoField = "loop"

IS26.connect.append(connect28)
connect29 = x3d.connect()
connect29.nodeField = "startTime"
connect29.protoField = "startTime"

IS26.connect.append(connect29)
connect30 = x3d.connect()
connect30.nodeField = "stopTime"
connect30.protoField = "stopTime"

IS26.connect.append(connect30)

TimeSensor25.IS = IS26

ProtoBody21.children.append(TimeSensor25)
OrientationInterpolator31 = x3d.OrientationInterpolator()
OrientationInterpolator31.DEF = "Spinner"
OrientationInterpolator31.key = [0,0.5,1]
OrientationInterpolator31.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,3.1400,0.0000,1.0000,0.0000,6.2800)

ProtoBody21.children.append(OrientationInterpolator31)
ROUTE32 = x3d.ROUTE()
ROUTE32.fromField = "fraction_changed"
ROUTE32.fromNode = "SpinGroupClock"
ROUTE32.toField = "set_fraction"
ROUTE32.toNode = "Spinner"

ProtoBody21.children.append(ROUTE32)
ROUTE33 = x3d.ROUTE()
ROUTE33.fromField = "value_changed"
ROUTE33.fromNode = "Spinner"
ROUTE33.toField = "set_rotation"
ROUTE33.toNode = "SpinGroupTransform"

ProtoBody21.children.append(ROUTE33)

ProtoDeclare14.ProtoBody = ProtoBody21

Scene12.children.append(ProtoDeclare14)
#Now the scene proper begins. Nothing renders in a ProtoDeclare (or ExternProtoDeclare).
Viewpoint34 = x3d.Viewpoint()
Viewpoint34.description = "Click on blue crossbar to activate second SpinGroup"
Viewpoint34.orientation = [1,0,0,-0.52]
Viewpoint34.position = [0,18,30]

Scene12.children.append(Viewpoint34)
#Create an instance, meaning actual nodes that render
ProtoInstance35 = x3d.ProtoInstance()
ProtoInstance35.name = "SpinGroup"
fieldValue36 = x3d.fieldValue()
fieldValue36.name = "cycleInterval"
fieldValue36.value = "8"

ProtoInstance35.fieldValue.append(fieldValue36)
fieldValue37 = x3d.fieldValue()
fieldValue37.name = "loop"
fieldValue37.value = "true"

ProtoInstance35.fieldValue.append(fieldValue37)
fieldValue38 = x3d.fieldValue()
fieldValue38.name = "children"
Shape39 = x3d.Shape()
Box40 = x3d.Box()
Box40.size = [25,2,2]

Shape39.geometry = Box40
Appearance41 = x3d.Appearance()
Appearance41.DEF = "Green"
Material42 = x3d.Material()
Material42.diffuseColor = [0,1,0.3]

Appearance41.material = Material42

Shape39.appearance = Appearance41

fieldValue38.children.append(Shape39)
Shape43 = x3d.Shape()
Box44 = x3d.Box()
Box44.size = [2,25,2]

Shape43.geometry = Box44
Appearance45 = x3d.Appearance()
Appearance45.USE = "Green"

Shape43.appearance = Appearance45

fieldValue38.children.append(Shape43)
ProtoInstance46 = x3d.ProtoInstance()
ProtoInstance46.name = "SpinGroup"
ProtoInstance46.DEF = "SecondSpinGroup"
fieldValue47 = x3d.fieldValue()
fieldValue47.name = "cycleInterval"
fieldValue47.value = "4"

ProtoInstance46.fieldValue.append(fieldValue47)
fieldValue48 = x3d.fieldValue()
fieldValue48.name = "loop"
fieldValue48.value = "true"

ProtoInstance46.fieldValue.append(fieldValue48)
fieldValue49 = x3d.fieldValue()
fieldValue49.name = "stopTime"
fieldValue49.value = "1"

ProtoInstance46.fieldValue.append(fieldValue49)
fieldValue50 = x3d.fieldValue()
fieldValue50.name = "children"
TouchSensor51 = x3d.TouchSensor()
TouchSensor51.DEF = "ActivateSecondSpinGroup"
TouchSensor51.description = "Activate second SpinGroup by clicking blue bar"

fieldValue50.children.append(TouchSensor51)
Shape52 = x3d.Shape()
Box53 = x3d.Box()
Box53.size = [2,2.05,25]

Shape52.geometry = Box53
Appearance54 = x3d.Appearance()
Material55 = x3d.Material()
Material55.diffuseColor = [0,0.3,1]

Appearance54.material = Material55

Shape52.appearance = Appearance54

fieldValue50.children.append(Shape52)

ProtoInstance46.fieldValue.append(fieldValue50)
#stopTime > startTime ensures that initial state is stopped

fieldValue38.children.append(ProtoInstance46)

ProtoInstance35.fieldValue.append(fieldValue38)

Scene12.children.append(ProtoInstance35)
ROUTE56 = x3d.ROUTE()
ROUTE56.fromField = "touchTime"
ROUTE56.fromNode = "ActivateSecondSpinGroup"
ROUTE56.toField = "startTime"
ROUTE56.toNode = "SecondSpinGroup"

Scene12.children.append(ROUTE56)

X3D0.Scene = Scene12
f = open("././Figure31_9SpinGroupPrototype_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
