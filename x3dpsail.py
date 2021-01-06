import jnius_config
jnius_config.set_classpath('.', 'c:/x3d-code/www.web3d.org/x3d/stylesheets/java/jars/X3DJSAIL.4.0.full.jar', './X3DJSAIL.4.0.full.jar')
from jnius import autoclass
CommentsBlock = autoclass('org.web3d.x3d.jsail.Core.CommentsBlock')
X3DNode = autoclass('org.web3d.x3d.sai.Core.X3DNode')
X3DAppearanceChildNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceChildNode')
X3DAppearanceNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceNode')
X3DChildNode = autoclass('org.web3d.x3d.sai.Core.X3DChildNode')
X3DBindableNode = autoclass('org.web3d.x3d.sai.Core.X3DBindableNode')
X3DBackgroundNode = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DBackgroundNode')
X3DFollowerNode = autoclass('org.web3d.x3d.sai.Followers.X3DFollowerNode')
X3DChaserNode = autoclass('org.web3d.x3d.sai.Followers.X3DChaserNode')
X3DGeometricPropertyNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometricPropertyNode')
X3DColorNode = autoclass('org.web3d.x3d.sai.Rendering.X3DColorNode')
X3DVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeRenderStyleNode')
X3DComposableVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DComposableVolumeRenderStyleNode')
X3DGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometryNode')
X3DComposedGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DComposedGeometryNode')
X3DCoordinateNode = autoclass('org.web3d.x3d.sai.Rendering.X3DCoordinateNode')
X3DDamperNode = autoclass('org.web3d.x3d.sai.Followers.X3DDamperNode')
X3DSensorNode = autoclass('org.web3d.x3d.sai.Core.X3DSensorNode')
X3DPointingDeviceSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DPointingDeviceSensorNode')
X3DDragSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DDragSensorNode')
X3DEnvironmentalSensorNode = autoclass('org.web3d.x3d.sai.EnvironmentalSensor.X3DEnvironmentalSensorNode')
X3DTextureNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureNode')
X3DEnvironmentTextureNode = autoclass('org.web3d.x3d.sai.CubeMapTexturing.X3DEnvironmentTextureNode')
X3DFontStyleNode = autoclass('org.web3d.x3d.sai.Text.X3DFontStyleNode')
X3DBoundedObject = autoclass('org.web3d.x3d.sai.Grouping.X3DBoundedObject')
X3DGroupingNode = autoclass('org.web3d.x3d.sai.Grouping.X3DGroupingNode')
X3DInfoNode = autoclass('org.web3d.x3d.sai.Core.X3DInfoNode')
X3DInterpolatorNode = autoclass('org.web3d.x3d.sai.Interpolation.X3DInterpolatorNode')
X3DKeyDeviceSensorNode = autoclass('org.web3d.x3d.sai.KeyDeviceSensor.X3DKeyDeviceSensorNode')
X3DPickableObject = autoclass('org.web3d.x3d.sai.Picking.X3DPickableObject')
X3DLayerNode = autoclass('org.web3d.x3d.sai.Layering.X3DLayerNode')
X3DLayoutNode = autoclass('org.web3d.x3d.sai.Layout.X3DLayoutNode')
X3DLightNode = autoclass('org.web3d.x3d.sai.Lighting.X3DLightNode')
X3DMaterialNode = autoclass('org.web3d.x3d.sai.Shape.X3DMaterialNode')
X3DNBodyCollidableNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollidableNode')
X3DNBodyCollisionSpaceNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollisionSpaceNode')
X3DNetworkSensorNode = autoclass('org.web3d.x3d.sai.Networking.X3DNetworkSensorNode')
X3DNormalNode = autoclass('org.web3d.x3d.sai.Rendering.X3DNormalNode')
X3DNurbsControlCurveNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsControlCurveNode')
X3DParametricGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DParametricGeometryNode')
X3DNurbsSurfaceGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsSurfaceGeometryNode')
X3DOneSidedMaterialNode = autoclass('org.web3d.x3d.sai.Shape.X3DOneSidedMaterialNode')
X3DParticleEmitterNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticleEmitterNode')
X3DParticlePhysicsModelNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticlePhysicsModelNode')
X3DPickSensorNode = autoclass('org.web3d.x3d.sai.Picking.X3DPickSensorNode')
X3DProductStructureChildNode = autoclass('org.web3d.x3d.sai.CADGeometry.X3DProductStructureChildNode')
X3DPrototypeInstance = autoclass('org.web3d.x3d.sai.Core.X3DPrototypeInstance')
X3DRigidJointNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DRigidJointNode')
X3DUrlObject = autoclass('org.web3d.x3d.sai.Networking.X3DUrlObject')
X3DScriptNode = autoclass('org.web3d.x3d.sai.Scripting.X3DScriptNode')
X3DSequencerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DSequencerNode')
X3DShaderNode = autoclass('org.web3d.x3d.sai.Shaders.X3DShaderNode')
X3DShapeNode = autoclass('org.web3d.x3d.sai.Shape.X3DShapeNode')
X3DTextureCoordinateNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureCoordinateNode')
X3DSingleTextureCoordinateNode = autoclass('org.web3d.x3d.sai.Texturing.X3DSingleTextureCoordinateNode')
X3DSingleTextureNode = autoclass('org.web3d.x3d.sai.Texturing.X3DSingleTextureNode')
X3DTextureTransformNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureTransformNode')
X3DSingleTextureTransformNode = autoclass('org.web3d.x3d.sai.Texturing.X3DSingleTextureTransformNode')
X3DSoundNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundNode')
X3DSoundChannelNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundChannelNode')
X3DSoundDestinationNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundDestinationNode')
X3DTimeDependentNode = autoclass('org.web3d.x3d.sai.Time.X3DTimeDependentNode')
X3DSoundProcessingNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundProcessingNode')
X3DSoundSourceNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundSourceNode')
X3DTexture2DNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTexture2DNode')
X3DTexture3DNode = autoclass('org.web3d.x3d.sai.Texturing3D.X3DTexture3DNode')
X3DTextureProjectorNode = autoclass('org.web3d.x3d.sai.TextureProjector.X3DTextureProjectorNode')
X3DTouchSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DTouchSensorNode')
X3DTriggerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DTriggerNode')
X3DVertexAttributeNode = autoclass('org.web3d.x3d.sai.Shaders.X3DVertexAttributeNode')
X3DViewpointNode = autoclass('org.web3d.x3d.sai.Navigation.X3DViewpointNode')
X3DViewportNode = autoclass('org.web3d.x3d.sai.Layering.X3DViewportNode')
X3DVolumeDataNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeDataNode')
X3DFogObject = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DFogObject')
X3DMetadataObject = autoclass('org.web3d.x3d.sai.Core.X3DMetadataObject')
X3DProgrammableShaderObject = autoclass('org.web3d.x3d.sai.Shaders.X3DProgrammableShaderObject')
AcousticProperties = autoclass('org.web3d.x3d.jsail.Shape.AcousticProperties')
Analyser = autoclass('org.web3d.x3d.jsail.Sound.Analyser')
Anchor = autoclass('org.web3d.x3d.jsail.Networking.Anchor')
Appearance = autoclass('org.web3d.x3d.jsail.Shape.Appearance')
Arc2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Arc2D')
ArcClose2D = autoclass('org.web3d.x3d.jsail.Geometry2D.ArcClose2D')
AudioClip = autoclass('org.web3d.x3d.jsail.Sound.AudioClip')
AudioDestination = autoclass('org.web3d.x3d.jsail.Sound.AudioDestination')
Background = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.Background')
BallJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.BallJoint')
Billboard = autoclass('org.web3d.x3d.jsail.Navigation.Billboard')
BiquadFilter = autoclass('org.web3d.x3d.jsail.Sound.BiquadFilter')
BlendedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.BlendedVolumeStyle')
BooleanFilter = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanFilter')
BooleanSequencer = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanSequencer')
BooleanToggle = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanToggle')
BooleanTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanTrigger')
BoundaryEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.BoundaryEnhancementVolumeStyle')
BoundedPhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.BoundedPhysicsModel')
Box = autoclass('org.web3d.x3d.jsail.Geometry3D.Box')
BufferAudioSource = autoclass('org.web3d.x3d.jsail.Sound.BufferAudioSource')
CADAssembly = autoclass('org.web3d.x3d.jsail.CADGeometry.CADAssembly')
CADFace = autoclass('org.web3d.x3d.jsail.CADGeometry.CADFace')
CADLayer = autoclass('org.web3d.x3d.jsail.CADGeometry.CADLayer')
CADPart = autoclass('org.web3d.x3d.jsail.CADGeometry.CADPart')
CartoonVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.CartoonVolumeStyle')
ChannelMerger = autoclass('org.web3d.x3d.jsail.Sound.ChannelMerger')
ChannelSelector = autoclass('org.web3d.x3d.jsail.Sound.ChannelSelector')
ChannelSplitter = autoclass('org.web3d.x3d.jsail.Sound.ChannelSplitter')
Circle2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Circle2D')
ClipPlane = autoclass('org.web3d.x3d.jsail.Rendering.ClipPlane')
CollidableOffset = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableOffset')
CollidableShape = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableShape')
Collision = autoclass('org.web3d.x3d.jsail.Navigation.Collision')
CollisionCollection = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionCollection')
CollisionSensor = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSensor')
CollisionSpace = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSpace')
Color = autoclass('org.web3d.x3d.jsail.Rendering.Color')
ColorChaser = autoclass('org.web3d.x3d.jsail.Followers.ColorChaser')
ColorDamper = autoclass('org.web3d.x3d.jsail.Followers.ColorDamper')
ColorInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.ColorInterpolator')
ColorRGBA = autoclass('org.web3d.x3d.jsail.Rendering.ColorRGBA')
ComposedCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.ComposedCubeMapTexture')
ComposedShader = autoclass('org.web3d.x3d.jsail.Shaders.ComposedShader')
ComposedTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.ComposedTexture3D')
ComposedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ComposedVolumeStyle')
Cone = autoclass('org.web3d.x3d.jsail.Geometry3D.Cone')
ConeEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.ConeEmitter')
Contact = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.Contact')
Contour2D = autoclass('org.web3d.x3d.jsail.NURBS.Contour2D')
ContourPolyline2D = autoclass('org.web3d.x3d.jsail.NURBS.ContourPolyline2D')
Convolver = autoclass('org.web3d.x3d.jsail.Sound.Convolver')
Coordinate = autoclass('org.web3d.x3d.jsail.Rendering.Coordinate')
CoordinateChaser = autoclass('org.web3d.x3d.jsail.Followers.CoordinateChaser')
CoordinateDamper = autoclass('org.web3d.x3d.jsail.Followers.CoordinateDamper')
CoordinateDouble = autoclass('org.web3d.x3d.jsail.NURBS.CoordinateDouble')
CoordinateInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolator')
CoordinateInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolator2D')
Cylinder = autoclass('org.web3d.x3d.jsail.Geometry3D.Cylinder')
CylinderSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.CylinderSensor')
Delay = autoclass('org.web3d.x3d.jsail.Sound.Delay')
DirectionalLight = autoclass('org.web3d.x3d.jsail.Lighting.DirectionalLight')
DISEntityManager = autoclass('org.web3d.x3d.jsail.DIS.DISEntityManager')
DISEntityTypeMapping = autoclass('org.web3d.x3d.jsail.DIS.DISEntityTypeMapping')
Disk2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Disk2D')
DoubleAxisHingeJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.DoubleAxisHingeJoint')
DynamicsCompressor = autoclass('org.web3d.x3d.jsail.Sound.DynamicsCompressor')
EaseInEaseOut = autoclass('org.web3d.x3d.jsail.Interpolation.EaseInEaseOut')
EdgeEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.EdgeEnhancementVolumeStyle')
ElevationGrid = autoclass('org.web3d.x3d.jsail.Geometry3D.ElevationGrid')
EspduTransform = autoclass('org.web3d.x3d.jsail.DIS.EspduTransform')
ExplosionEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.ExplosionEmitter')
Extrusion = autoclass('org.web3d.x3d.jsail.Geometry3D.Extrusion')
FillProperties = autoclass('org.web3d.x3d.jsail.Shape.FillProperties')
FloatVertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.FloatVertexAttribute')
Fog = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.Fog')
FogCoordinate = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.FogCoordinate')
FontStyle = autoclass('org.web3d.x3d.jsail.Text.FontStyle')
ForcePhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.ForcePhysicsModel')
Gain = autoclass('org.web3d.x3d.jsail.Sound.Gain')
GeneratedCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.GeneratedCubeMapTexture')
GeoCoordinate = autoclass('org.web3d.x3d.jsail.Geospatial.GeoCoordinate')
GeoElevationGrid = autoclass('org.web3d.x3d.jsail.Geospatial.GeoElevationGrid')
GeoLocation = autoclass('org.web3d.x3d.jsail.Geospatial.GeoLocation')
GeoLOD = autoclass('org.web3d.x3d.jsail.Geospatial.GeoLOD')
GeoMetadata = autoclass('org.web3d.x3d.jsail.Geospatial.GeoMetadata')
GeoOrigin = autoclass('org.web3d.x3d.jsail.Geospatial.GeoOrigin')
GeoPositionInterpolator = autoclass('org.web3d.x3d.jsail.Geospatial.GeoPositionInterpolator')
GeoProximitySensor = autoclass('org.web3d.x3d.jsail.Geospatial.GeoProximitySensor')
GeoTouchSensor = autoclass('org.web3d.x3d.jsail.Geospatial.GeoTouchSensor')
GeoTransform = autoclass('org.web3d.x3d.jsail.Geospatial.GeoTransform')
GeoViewpoint = autoclass('org.web3d.x3d.jsail.Geospatial.GeoViewpoint')
Group = autoclass('org.web3d.x3d.jsail.Grouping.Group')
HAnimDisplacer = autoclass('org.web3d.x3d.jsail.HAnim.HAnimDisplacer')
HAnimHumanoid = autoclass('org.web3d.x3d.jsail.HAnim.HAnimHumanoid')
HAnimJoint = autoclass('org.web3d.x3d.jsail.HAnim.HAnimJoint')
HAnimMotion = autoclass('org.web3d.x3d.jsail.HAnim.HAnimMotion')
HAnimSegment = autoclass('org.web3d.x3d.jsail.HAnim.HAnimSegment')
HAnimSite = autoclass('org.web3d.x3d.jsail.HAnim.HAnimSite')
ImageCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.ImageCubeMapTexture')
ImageTexture = autoclass('org.web3d.x3d.jsail.Texturing.ImageTexture')
ImageTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.ImageTexture3D')
IndexedFaceSet = autoclass('org.web3d.x3d.jsail.Geometry3D.IndexedFaceSet')
IndexedLineSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedLineSet')
IndexedQuadSet = autoclass('org.web3d.x3d.jsail.CADGeometry.IndexedQuadSet')
IndexedTriangleFanSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleFanSet')
IndexedTriangleSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleSet')
IndexedTriangleStripSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleStripSet')
Inline = autoclass('org.web3d.x3d.jsail.Networking.Inline')
IntegerSequencer = autoclass('org.web3d.x3d.jsail.EventUtilities.IntegerSequencer')
IntegerTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.IntegerTrigger')
IsoSurfaceVolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.IsoSurfaceVolumeData')
KeySensor = autoclass('org.web3d.x3d.jsail.KeyDeviceSensor.KeySensor')
Layer = autoclass('org.web3d.x3d.jsail.Layering.Layer')
LayerSet = autoclass('org.web3d.x3d.jsail.Layering.LayerSet')
Layout = autoclass('org.web3d.x3d.jsail.Layout.Layout')
LayoutGroup = autoclass('org.web3d.x3d.jsail.Layout.LayoutGroup')
LayoutLayer = autoclass('org.web3d.x3d.jsail.Layout.LayoutLayer')
LinePickSensor = autoclass('org.web3d.x3d.jsail.Picking.LinePickSensor')
LineProperties = autoclass('org.web3d.x3d.jsail.Shape.LineProperties')
LineSet = autoclass('org.web3d.x3d.jsail.Rendering.LineSet')
ListenerPointSource = autoclass('org.web3d.x3d.jsail.Sound.ListenerPointSource')
LoadSensor = autoclass('org.web3d.x3d.jsail.Networking.LoadSensor')
LocalFog = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.LocalFog')
LOD = autoclass('org.web3d.x3d.jsail.Navigation.LOD')
Material = autoclass('org.web3d.x3d.jsail.Shape.Material')
Matrix3VertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.Matrix3VertexAttribute')
Matrix4VertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.Matrix4VertexAttribute')
MetadataBoolean = autoclass('org.web3d.x3d.jsail.Core.MetadataBoolean')
MetadataDouble = autoclass('org.web3d.x3d.jsail.Core.MetadataDouble')
MetadataFloat = autoclass('org.web3d.x3d.jsail.Core.MetadataFloat')
MetadataInteger = autoclass('org.web3d.x3d.jsail.Core.MetadataInteger')
MetadataSet = autoclass('org.web3d.x3d.jsail.Core.MetadataSet')
MetadataString = autoclass('org.web3d.x3d.jsail.Core.MetadataString')
MicrophoneSource = autoclass('org.web3d.x3d.jsail.Sound.MicrophoneSource')
MotorJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.MotorJoint')
MovieTexture = autoclass('org.web3d.x3d.jsail.Texturing.MovieTexture')
MultiTexture = autoclass('org.web3d.x3d.jsail.Texturing.MultiTexture')
MultiTextureCoordinate = autoclass('org.web3d.x3d.jsail.Texturing.MultiTextureCoordinate')
MultiTextureTransform = autoclass('org.web3d.x3d.jsail.Texturing.MultiTextureTransform')
NavigationInfo = autoclass('org.web3d.x3d.jsail.Navigation.NavigationInfo')
Normal = autoclass('org.web3d.x3d.jsail.Rendering.Normal')
NormalInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.NormalInterpolator')
NurbsCurve = autoclass('org.web3d.x3d.jsail.NURBS.NurbsCurve')
NurbsCurve2D = autoclass('org.web3d.x3d.jsail.NURBS.NurbsCurve2D')
NurbsOrientationInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsOrientationInterpolator')
NurbsPatchSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsPatchSurface')
NurbsPositionInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsPositionInterpolator')
NurbsSet = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSet')
NurbsSurfaceInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSurfaceInterpolator')
NurbsSweptSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSweptSurface')
NurbsSwungSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSwungSurface')
NurbsTextureCoordinate = autoclass('org.web3d.x3d.jsail.NURBS.NurbsTextureCoordinate')
NurbsTrimmedSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsTrimmedSurface')
OpacityMapVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.OpacityMapVolumeStyle')
OrientationChaser = autoclass('org.web3d.x3d.jsail.Followers.OrientationChaser')
OrientationDamper = autoclass('org.web3d.x3d.jsail.Followers.OrientationDamper')
OrientationInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.OrientationInterpolator')
OrthoViewpoint = autoclass('org.web3d.x3d.jsail.Navigation.OrthoViewpoint')
OscillatorSource = autoclass('org.web3d.x3d.jsail.Sound.OscillatorSource')
PackagedShader = autoclass('org.web3d.x3d.jsail.Shaders.PackagedShader')
ParticleSystem = autoclass('org.web3d.x3d.jsail.ParticleSystems.ParticleSystem')
PeriodicWave = autoclass('org.web3d.x3d.jsail.Sound.PeriodicWave')
PhysicalMaterial = autoclass('org.web3d.x3d.jsail.Shape.PhysicalMaterial')
PickableGroup = autoclass('org.web3d.x3d.jsail.Picking.PickableGroup')
PixelTexture = autoclass('org.web3d.x3d.jsail.Texturing.PixelTexture')
PixelTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.PixelTexture3D')
PlaneSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.PlaneSensor')
PointEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.PointEmitter')
PointLight = autoclass('org.web3d.x3d.jsail.Lighting.PointLight')
PointPickSensor = autoclass('org.web3d.x3d.jsail.Picking.PointPickSensor')
PointProperties = autoclass('org.web3d.x3d.jsail.Shape.PointProperties')
PointSet = autoclass('org.web3d.x3d.jsail.Rendering.PointSet')
Polyline2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Polyline2D')
PolylineEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.PolylineEmitter')
Polypoint2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Polypoint2D')
PositionChaser = autoclass('org.web3d.x3d.jsail.Followers.PositionChaser')
PositionChaser2D = autoclass('org.web3d.x3d.jsail.Followers.PositionChaser2D')
PositionDamper = autoclass('org.web3d.x3d.jsail.Followers.PositionDamper')
PositionDamper2D = autoclass('org.web3d.x3d.jsail.Followers.PositionDamper2D')
PositionInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.PositionInterpolator')
PositionInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.PositionInterpolator2D')
PrimitivePickSensor = autoclass('org.web3d.x3d.jsail.Picking.PrimitivePickSensor')
ProgramShader = autoclass('org.web3d.x3d.jsail.Shaders.ProgramShader')
ProjectionVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ProjectionVolumeStyle')
ProtoInstance = autoclass('org.web3d.x3d.jsail.Core.ProtoInstance')
ProximitySensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.ProximitySensor')
QuadSet = autoclass('org.web3d.x3d.jsail.CADGeometry.QuadSet')
ReceiverPdu = autoclass('org.web3d.x3d.jsail.DIS.ReceiverPdu')
Rectangle2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Rectangle2D')
RigidBody = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBody')
RigidBodyCollection = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBodyCollection')
ScalarChaser = autoclass('org.web3d.x3d.jsail.Followers.ScalarChaser')
ScalarDamper = autoclass('org.web3d.x3d.jsail.Followers.ScalarDamper')
ScalarInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.ScalarInterpolator')
ScreenFontStyle = autoclass('org.web3d.x3d.jsail.Layout.ScreenFontStyle')
ScreenGroup = autoclass('org.web3d.x3d.jsail.Layout.ScreenGroup')
Script = autoclass('org.web3d.x3d.jsail.Scripting.Script')
SegmentedVolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.SegmentedVolumeData')
ShadedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ShadedVolumeStyle')
ShaderPart = autoclass('org.web3d.x3d.jsail.Shaders.ShaderPart')
ShaderProgram = autoclass('org.web3d.x3d.jsail.Shaders.ShaderProgram')
Shape = autoclass('org.web3d.x3d.jsail.Shape.Shape')
SignalPdu = autoclass('org.web3d.x3d.jsail.DIS.SignalPdu')
SilhouetteEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.SilhouetteEnhancementVolumeStyle')
SingleAxisHingeJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.SingleAxisHingeJoint')
SliderJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.SliderJoint')
Sound = autoclass('org.web3d.x3d.jsail.Sound.Sound')
SpatialSound = autoclass('org.web3d.x3d.jsail.Sound.SpatialSound')
Sphere = autoclass('org.web3d.x3d.jsail.Geometry3D.Sphere')
SphereSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.SphereSensor')
SplinePositionInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolator')
SplinePositionInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolator2D')
SplineScalarInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SplineScalarInterpolator')
SpotLight = autoclass('org.web3d.x3d.jsail.Lighting.SpotLight')
SquadOrientationInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SquadOrientationInterpolator')
StaticGroup = autoclass('org.web3d.x3d.jsail.Grouping.StaticGroup')
StreamAudioDestination = autoclass('org.web3d.x3d.jsail.Sound.StreamAudioDestination')
StreamAudioSource = autoclass('org.web3d.x3d.jsail.Sound.StreamAudioSource')
StringSensor = autoclass('org.web3d.x3d.jsail.KeyDeviceSensor.StringSensor')
SurfaceEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.SurfaceEmitter')
Switch = autoclass('org.web3d.x3d.jsail.Grouping.Switch')
TexCoordChaser2D = autoclass('org.web3d.x3d.jsail.Followers.TexCoordChaser2D')
TexCoordDamper2D = autoclass('org.web3d.x3d.jsail.Followers.TexCoordDamper2D')
Text = autoclass('org.web3d.x3d.jsail.Text.Text')
TextureBackground = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.TextureBackground')
TextureCoordinate = autoclass('org.web3d.x3d.jsail.Texturing.TextureCoordinate')
TextureCoordinate3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate3D')
TextureCoordinate4D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate4D')
TextureCoordinateGenerator = autoclass('org.web3d.x3d.jsail.Texturing.TextureCoordinateGenerator')
TextureProjector = autoclass('org.web3d.x3d.jsail.TextureProjector.TextureProjector')
TextureProjectorParallel = autoclass('org.web3d.x3d.jsail.TextureProjector.TextureProjectorParallel')
TextureProperties = autoclass('org.web3d.x3d.jsail.Texturing.TextureProperties')
TextureTransform = autoclass('org.web3d.x3d.jsail.Texturing.TextureTransform')
TextureTransform3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureTransform3D')
TextureTransformMatrix3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureTransformMatrix3D')
TimeSensor = autoclass('org.web3d.x3d.jsail.Time.TimeSensor')
TimeTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.TimeTrigger')
ToneMappedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ToneMappedVolumeStyle')
TouchSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.TouchSensor')
Transform = autoclass('org.web3d.x3d.jsail.Grouping.Transform')
TransformSensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.TransformSensor')
TransmitterPdu = autoclass('org.web3d.x3d.jsail.DIS.TransmitterPdu')
TriangleFanSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleFanSet')
TriangleSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleSet')
TriangleSet2D = autoclass('org.web3d.x3d.jsail.Geometry2D.TriangleSet2D')
TriangleStripSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleStripSet')
TwoSidedMaterial = autoclass('org.web3d.x3d.jsail.Shape.TwoSidedMaterial')
UniversalJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.UniversalJoint')
UnlitMaterial = autoclass('org.web3d.x3d.jsail.Shape.UnlitMaterial')
Viewpoint = autoclass('org.web3d.x3d.jsail.Navigation.Viewpoint')
ViewpointGroup = autoclass('org.web3d.x3d.jsail.Navigation.ViewpointGroup')
Viewport = autoclass('org.web3d.x3d.jsail.Layering.Viewport')
VisibilitySensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.VisibilitySensor')
VolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.VolumeData')
VolumeEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.VolumeEmitter')
VolumePickSensor = autoclass('org.web3d.x3d.jsail.Picking.VolumePickSensor')
WaveShaper = autoclass('org.web3d.x3d.jsail.Sound.WaveShaper')
WindPhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.WindPhysicsModel')
WorldInfo = autoclass('org.web3d.x3d.jsail.Core.WorldInfo')
component = autoclass('org.web3d.x3d.jsail.Core.component')
connect = autoclass('org.web3d.x3d.jsail.Core.connect')
EXPORT = autoclass('org.web3d.x3d.jsail.Networking.EXPORT')
ExternProtoDeclare = autoclass('org.web3d.x3d.jsail.Core.ExternProtoDeclare')
field = autoclass('org.web3d.x3d.jsail.Core.field')
fieldValue = autoclass('org.web3d.x3d.jsail.Core.fieldValue')
head = autoclass('org.web3d.x3d.jsail.Core.head')
IMPORT = autoclass('org.web3d.x3d.jsail.Networking.IMPORT')
IS = autoclass('org.web3d.x3d.jsail.Core.IS')
meta = autoclass('org.web3d.x3d.jsail.Core.meta')
ProtoBody = autoclass('org.web3d.x3d.jsail.Core.ProtoBody')
ProtoDeclare = autoclass('org.web3d.x3d.jsail.Core.ProtoDeclare')
ProtoInterface = autoclass('org.web3d.x3d.jsail.Core.ProtoInterface')
ROUTE = autoclass('org.web3d.x3d.jsail.Core.ROUTE')
Scene = autoclass('org.web3d.x3d.jsail.Core.Scene')
unit = autoclass('org.web3d.x3d.jsail.Core.unit')
X3D = autoclass('org.web3d.x3d.jsail.Core.X3D')
SFBool = autoclass('org.web3d.x3d.jsail.fields.SFBool')
MFBool = autoclass('org.web3d.x3d.jsail.fields.MFBool')
SFColor = autoclass('org.web3d.x3d.jsail.fields.SFColor')
MFColor = autoclass('org.web3d.x3d.jsail.fields.MFColor')
SFColorRGBA = autoclass('org.web3d.x3d.jsail.fields.SFColorRGBA')
MFColorRGBA = autoclass('org.web3d.x3d.jsail.fields.MFColorRGBA')
SFDouble = autoclass('org.web3d.x3d.jsail.fields.SFDouble')
MFDouble = autoclass('org.web3d.x3d.jsail.fields.MFDouble')
SFFloat = autoclass('org.web3d.x3d.jsail.fields.SFFloat')
MFFloat = autoclass('org.web3d.x3d.jsail.fields.MFFloat')
SFImage = autoclass('org.web3d.x3d.jsail.fields.SFImage')
MFImage = autoclass('org.web3d.x3d.jsail.fields.MFImage')
SFInt32 = autoclass('org.web3d.x3d.jsail.fields.SFInt32')
MFInt32 = autoclass('org.web3d.x3d.jsail.fields.MFInt32')
SFMatrix3d = autoclass('org.web3d.x3d.jsail.fields.SFMatrix3d')
MFMatrix3d = autoclass('org.web3d.x3d.jsail.fields.MFMatrix3d')
SFMatrix3f = autoclass('org.web3d.x3d.jsail.fields.SFMatrix3f')
MFMatrix3f = autoclass('org.web3d.x3d.jsail.fields.MFMatrix3f')
SFMatrix4d = autoclass('org.web3d.x3d.jsail.fields.SFMatrix4d')
MFMatrix4d = autoclass('org.web3d.x3d.jsail.fields.MFMatrix4d')
SFMatrix4f = autoclass('org.web3d.x3d.jsail.fields.SFMatrix4f')
MFMatrix4f = autoclass('org.web3d.x3d.jsail.fields.MFMatrix4f')
SFString = autoclass('org.web3d.x3d.jsail.fields.SFString')
SFNode = autoclass('org.web3d.x3d.jsail.fields.SFNode')
MFNode = autoclass('org.web3d.x3d.jsail.fields.MFNode')
SFRotation = autoclass('org.web3d.x3d.jsail.fields.SFRotation')
MFRotation = autoclass('org.web3d.x3d.jsail.fields.MFRotation')
MFString = autoclass('org.web3d.x3d.jsail.fields.MFString')
SFTime = autoclass('org.web3d.x3d.jsail.fields.SFTime')
MFTime = autoclass('org.web3d.x3d.jsail.fields.MFTime')
SFVec2d = autoclass('org.web3d.x3d.jsail.fields.SFVec2d')
MFVec2d = autoclass('org.web3d.x3d.jsail.fields.MFVec2d')
SFVec2f = autoclass('org.web3d.x3d.jsail.fields.SFVec2f')
MFVec2f = autoclass('org.web3d.x3d.jsail.fields.MFVec2f')
SFVec3d = autoclass('org.web3d.x3d.jsail.fields.SFVec3d')
MFVec3d = autoclass('org.web3d.x3d.jsail.fields.MFVec3d')
SFVec3f = autoclass('org.web3d.x3d.jsail.fields.SFVec3f')
MFVec3f = autoclass('org.web3d.x3d.jsail.fields.MFVec3f')
SFVec4d = autoclass('org.web3d.x3d.jsail.fields.SFVec4d')
MFVec4d = autoclass('org.web3d.x3d.jsail.fields.MFVec4d')
SFVec4f = autoclass('org.web3d.x3d.jsail.fields.SFVec4f')
MFVec4f = autoclass('org.web3d.x3d.jsail.fields.MFVec4f')
