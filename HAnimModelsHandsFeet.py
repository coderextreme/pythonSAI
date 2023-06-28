print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "HAnim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "HAnimModelsHandsFeet.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "Left and right hands and feet, using high-fidelity definitions for HAnim version 2.0"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "YOO Kwan Hee and Don Brutzman"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "8 February 2015"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "8 March 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "warning"
meta8.content = "not yet to scale"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "warning"
meta9.content = "TODO will X3D HAnim component add a new level to support LOA-4 functionality?"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "TODO"
meta10.content = "how to have HAnimHumanoid root with Inline IMPORT/EXPORT of limbs?"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "Image"
meta11.content = "HAnimModelsHandsFeet.png"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "Image"
meta12.content = "HAnimModelsHandsFeetWithFour1mGrids.png"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "https://www.web3d.org/working-groups/humanoid-animation-HAnim"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "https://www.web3d.org/documents/specifications/19774/V2.0"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "https://www.web3d.org/specifications/X3Dv4Draft/ISO-IEC19775-1v4-WD2/Part01/components/hanim.html"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "subject"
meta16.content = "X3D HAnim humanoid animation"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "identifier"
meta17.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelsHandsFeet.x3d"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "generator"
meta18.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "license"
meta19.content = "../license.html"

head1.children.append(meta19)

X3D0.head = head1
Scene20 = x3d.Scene()
WorldInfo21 = x3d.WorldInfo()
WorldInfo21.title = "HAnimModelsHandsFeet.x3d"

Scene20.children.append(WorldInfo21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.description = "Hands and feet 10m"

Scene20.children.append(Viewpoint22)
Viewpoint23 = x3d.Viewpoint()
Viewpoint23.description = "Hands and feet 1.7m"
Viewpoint23.position = [0,0,1.7]

Scene20.children.append(Viewpoint23)
Transform24 = x3d.Transform()
Transform24.translation = [-1,1,0]
Inline25 = x3d.Inline()
Inline25.url = ["HAnimModelHandLeft.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelHandLeft.x3d","HAnimModelHandLeft.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelHandLeft.wrl"]

Transform24.children.append(Inline25)
#Grid overlay authoring hint: first adjust grid scale to convenient large size, then adjust overall scale for your scene model
Transform26 = x3d.Transform()
Transform26.DEF = "GridXY_20x20Fixed_AdjustScale"
Transform26.scale = [0.1,0.1,0.1]
Inline27 = x3d.Inline()
Inline27.DEF = "GridXY_20x20Fixed"
Inline27.url = ["GridXY_20x20Fixed.x3d","../../Savage/Tools/Authoring/GridXY_20x20Fixed.x3d","https://savage.nps.edu/Savage/Tools/Authoring/GridXY_20x20Fixed.x3d","GridXY_20x20Fixed.wrl","../../Savage/Tools/Authoring/GridXY_20x20Fixed.wrl","https://savage.nps.edu/Savage/Tools/Authoring/GridXY_20x20Fixed.wrl"]

Transform26.children.append(Inline27)

Transform24.children.append(Transform26)

Scene20.children.append(Transform24)
Transform28 = x3d.Transform()
Transform28.translation = [1,1,0]
Inline29 = x3d.Inline()
Inline29.url = ["HAnimModelHandRight.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelHandRight.x3d","HAnimModelHandRight.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelHandRight.wrl"]

Transform28.children.append(Inline29)
Transform30 = x3d.Transform()
Transform30.USE = "GridXY_20x20Fixed_AdjustScale"

Transform28.children.append(Transform30)

Scene20.children.append(Transform28)
Transform31 = x3d.Transform()
Transform31.translation = [-1,-1,0]
#rotation='0 0 1 3.141593'
Inline32 = x3d.Inline()
Inline32.url = ["HAnimModelFootLeft.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelFootLeft.x3d","HAnimModelFootLeft.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelFootLeft.wrl"]

Transform31.children.append(Inline32)
Transform33 = x3d.Transform()
Transform33.USE = "GridXY_20x20Fixed_AdjustScale"

Transform31.children.append(Transform33)

Scene20.children.append(Transform31)
Transform34 = x3d.Transform()
Transform34.translation = [1,-1,0]
#rotation='0 0 1 3.141593'
Inline35 = x3d.Inline()
Inline35.url = ["HAnimModelFootRight.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelFootRight.x3d","HAnimModelFootRight.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/HAnimModelFootRight.wrl"]

Transform34.children.append(Inline35)
Transform36 = x3d.Transform()
Transform36.USE = "GridXY_20x20Fixed_AdjustScale"

Transform34.children.append(Transform36)

Scene20.children.append(Transform34)

X3D0.Scene = Scene20
f = open("././HAnimModelsHandsFeet_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
