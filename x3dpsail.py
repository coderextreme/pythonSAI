import jnius_config
jnius_config.set_classpath('.', 'c:/x3d-code/www.web3d.org/x3d/stylesheets/java/jars/X3DJSAIL.3.3.full.jar', './X3DJSAIL.3.3.full.jar')
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
X3DSoundNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundNode')
X3DTimeDependentNode = autoclass('org.web3d.x3d.sai.Time.X3DTimeDependentNode')
X3DSoundSourceNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundSourceNode')
X3DTexture2DNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTexture2DNode')
X3DTexture3DNode = autoclass('org.web3d.x3d.sai.Texturing3D.X3DTexture3DNode')
X3DTextureCoordinateNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureCoordinateNode')
X3DTextureTransformNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureTransformNode')
X3DTouchSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DTouchSensorNode')
X3DTriggerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DTriggerNode')
X3DVertexAttributeNode = autoclass('org.web3d.x3d.sai.Shaders.X3DVertexAttributeNode')
X3DViewpointNode = autoclass('org.web3d.x3d.sai.Navigation.X3DViewpointNode')
X3DViewportNode = autoclass('org.web3d.x3d.sai.Layering.X3DViewportNode')
X3DVolumeDataNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeDataNode')
X3DFogObject = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DFogObject')
X3DMetadataObject = autoclass('org.web3d.x3d.sai.Core.X3DMetadataObject')
X3DProgrammableShaderObject = autoclass('org.web3d.x3d.sai.Shaders.X3DProgrammableShaderObject')
Anchor = autoclass('org.web3d.x3d.jsail.Networking.AnchorObject')
Appearance = autoclass('org.web3d.x3d.jsail.Shape.AppearanceObject')
Arc2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Arc2DObject')
ArcClose2D = autoclass('org.web3d.x3d.jsail.Geometry2D.ArcClose2DObject')
AudioClip = autoclass('org.web3d.x3d.jsail.Sound.AudioClipObject')
Background = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.BackgroundObject')
BallJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.BallJointObject')
Billboard = autoclass('org.web3d.x3d.jsail.Navigation.BillboardObject')
BlendedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.BlendedVolumeStyleObject')
BooleanFilter = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanFilterObject')
BooleanSequencer = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanSequencerObject')
BooleanToggle = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanToggleObject')
BooleanTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.BooleanTriggerObject')
BoundaryEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.BoundaryEnhancementVolumeStyleObject')
BoundedPhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.BoundedPhysicsModelObject')
Box = autoclass('org.web3d.x3d.jsail.Geometry3D.BoxObject')
CADAssembly = autoclass('org.web3d.x3d.jsail.CADGeometry.CADAssemblyObject')
CADFace = autoclass('org.web3d.x3d.jsail.CADGeometry.CADFaceObject')
CADLayer = autoclass('org.web3d.x3d.jsail.CADGeometry.CADLayerObject')
CADPart = autoclass('org.web3d.x3d.jsail.CADGeometry.CADPartObject')
CartoonVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.CartoonVolumeStyleObject')
Circle2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Circle2DObject')
ClipPlane = autoclass('org.web3d.x3d.jsail.Rendering.ClipPlaneObject')
CollidableOffset = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableOffsetObject')
CollidableShape = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollidableShapeObject')
Collision = autoclass('org.web3d.x3d.jsail.Navigation.CollisionObject')
CollisionCollection = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionCollectionObject')
CollisionSensor = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSensorObject')
CollisionSpace = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.CollisionSpaceObject')
Color = autoclass('org.web3d.x3d.jsail.Rendering.ColorObject')
ColorChaser = autoclass('org.web3d.x3d.jsail.Followers.ColorChaserObject')
ColorDamper = autoclass('org.web3d.x3d.jsail.Followers.ColorDamperObject')
ColorInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.ColorInterpolatorObject')
ColorRGBA = autoclass('org.web3d.x3d.jsail.Rendering.ColorRGBAObject')
ComposedCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.ComposedCubeMapTextureObject')
ComposedShader = autoclass('org.web3d.x3d.jsail.Shaders.ComposedShaderObject')
ComposedTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.ComposedTexture3DObject')
ComposedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ComposedVolumeStyleObject')
Cone = autoclass('org.web3d.x3d.jsail.Geometry3D.ConeObject')
ConeEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.ConeEmitterObject')
Contact = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.ContactObject')
Contour2D = autoclass('org.web3d.x3d.jsail.NURBS.Contour2DObject')
ContourPolyline2D = autoclass('org.web3d.x3d.jsail.NURBS.ContourPolyline2DObject')
Coordinate = autoclass('org.web3d.x3d.jsail.Rendering.CoordinateObject')
CoordinateChaser = autoclass('org.web3d.x3d.jsail.Followers.CoordinateChaserObject')
CoordinateDamper = autoclass('org.web3d.x3d.jsail.Followers.CoordinateDamperObject')
CoordinateDouble = autoclass('org.web3d.x3d.jsail.NURBS.CoordinateDoubleObject')
CoordinateInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolatorObject')
CoordinateInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.CoordinateInterpolator2DObject')
Cylinder = autoclass('org.web3d.x3d.jsail.Geometry3D.CylinderObject')
CylinderSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.CylinderSensorObject')
DirectionalLight = autoclass('org.web3d.x3d.jsail.Lighting.DirectionalLightObject')
DISEntityManager = autoclass('org.web3d.x3d.jsail.DIS.DISEntityManagerObject')
DISEntityTypeMapping = autoclass('org.web3d.x3d.jsail.DIS.DISEntityTypeMappingObject')
Disk2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Disk2DObject')
DoubleAxisHingeJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.DoubleAxisHingeJointObject')
EaseInEaseOut = autoclass('org.web3d.x3d.jsail.Interpolation.EaseInEaseOutObject')
EdgeEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.EdgeEnhancementVolumeStyleObject')
ElevationGrid = autoclass('org.web3d.x3d.jsail.Geometry3D.ElevationGridObject')
EspduTransform = autoclass('org.web3d.x3d.jsail.DIS.EspduTransformObject')
ExplosionEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.ExplosionEmitterObject')
Extrusion = autoclass('org.web3d.x3d.jsail.Geometry3D.ExtrusionObject')
FillProperties = autoclass('org.web3d.x3d.jsail.Shape.FillPropertiesObject')
FloatVertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.FloatVertexAttributeObject')
Fog = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.FogObject')
FogCoordinate = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.FogCoordinateObject')
FontStyle = autoclass('org.web3d.x3d.jsail.Text.FontStyleObject')
ForcePhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.ForcePhysicsModelObject')
GeneratedCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.GeneratedCubeMapTextureObject')
GeoCoordinate = autoclass('org.web3d.x3d.jsail.Geospatial.GeoCoordinateObject')
GeoElevationGrid = autoclass('org.web3d.x3d.jsail.Geospatial.GeoElevationGridObject')
GeoLocation = autoclass('org.web3d.x3d.jsail.Geospatial.GeoLocationObject')
GeoLOD = autoclass('org.web3d.x3d.jsail.Geospatial.GeoLODObject')
GeoMetadata = autoclass('org.web3d.x3d.jsail.Geospatial.GeoMetadataObject')
GeoOrigin = autoclass('org.web3d.x3d.jsail.Geospatial.GeoOriginObject')
GeoPositionInterpolator = autoclass('org.web3d.x3d.jsail.Geospatial.GeoPositionInterpolatorObject')
GeoProximitySensor = autoclass('org.web3d.x3d.jsail.Geospatial.GeoProximitySensorObject')
GeoTouchSensor = autoclass('org.web3d.x3d.jsail.Geospatial.GeoTouchSensorObject')
GeoTransform = autoclass('org.web3d.x3d.jsail.Geospatial.GeoTransformObject')
GeoViewpoint = autoclass('org.web3d.x3d.jsail.Geospatial.GeoViewpointObject')
Group = autoclass('org.web3d.x3d.jsail.Grouping.GroupObject')
HAnimDisplacer = autoclass('org.web3d.x3d.jsail.HAnim.HAnimDisplacerObject')
HAnimHumanoid = autoclass('org.web3d.x3d.jsail.HAnim.HAnimHumanoidObject')
HAnimJoint = autoclass('org.web3d.x3d.jsail.HAnim.HAnimJointObject')
HAnimMotion = autoclass('org.web3d.x3d.jsail.HAnim.HAnimMotionObject')
HAnimSegment = autoclass('org.web3d.x3d.jsail.HAnim.HAnimSegmentObject')
HAnimSite = autoclass('org.web3d.x3d.jsail.HAnim.HAnimSiteObject')
ImageCubeMapTexture = autoclass('org.web3d.x3d.jsail.CubeMapTexturing.ImageCubeMapTextureObject')
ImageTexture = autoclass('org.web3d.x3d.jsail.Texturing.ImageTextureObject')
ImageTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.ImageTexture3DObject')
IndexedFaceSet = autoclass('org.web3d.x3d.jsail.Geometry3D.IndexedFaceSetObject')
IndexedLineSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedLineSetObject')
IndexedQuadSet = autoclass('org.web3d.x3d.jsail.CADGeometry.IndexedQuadSetObject')
IndexedTriangleFanSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleFanSetObject')
IndexedTriangleSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleSetObject')
IndexedTriangleStripSet = autoclass('org.web3d.x3d.jsail.Rendering.IndexedTriangleStripSetObject')
Inline = autoclass('org.web3d.x3d.jsail.Networking.InlineObject')
IntegerSequencer = autoclass('org.web3d.x3d.jsail.EventUtilities.IntegerSequencerObject')
IntegerTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.IntegerTriggerObject')
IsoSurfaceVolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.IsoSurfaceVolumeDataObject')
KeySensor = autoclass('org.web3d.x3d.jsail.KeyDeviceSensor.KeySensorObject')
Layer = autoclass('org.web3d.x3d.jsail.Layering.LayerObject')
LayerSet = autoclass('org.web3d.x3d.jsail.Layering.LayerSetObject')
Layout = autoclass('org.web3d.x3d.jsail.Layout.LayoutObject')
LayoutGroup = autoclass('org.web3d.x3d.jsail.Layout.LayoutGroupObject')
LayoutLayer = autoclass('org.web3d.x3d.jsail.Layout.LayoutLayerObject')
LinePickSensor = autoclass('org.web3d.x3d.jsail.Picking.LinePickSensorObject')
LineProperties = autoclass('org.web3d.x3d.jsail.Shape.LinePropertiesObject')
LineSet = autoclass('org.web3d.x3d.jsail.Rendering.LineSetObject')
LoadSensor = autoclass('org.web3d.x3d.jsail.Networking.LoadSensorObject')
LocalFog = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.LocalFogObject')
LOD = autoclass('org.web3d.x3d.jsail.Navigation.LODObject')
Material = autoclass('org.web3d.x3d.jsail.Shape.MaterialObject')
Matrix3VertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.Matrix3VertexAttributeObject')
Matrix4VertexAttribute = autoclass('org.web3d.x3d.jsail.Shaders.Matrix4VertexAttributeObject')
MetadataBoolean = autoclass('org.web3d.x3d.jsail.Core.MetadataBooleanObject')
MetadataDouble = autoclass('org.web3d.x3d.jsail.Core.MetadataDoubleObject')
MetadataFloat = autoclass('org.web3d.x3d.jsail.Core.MetadataFloatObject')
MetadataInteger = autoclass('org.web3d.x3d.jsail.Core.MetadataIntegerObject')
MetadataSet = autoclass('org.web3d.x3d.jsail.Core.MetadataSetObject')
MetadataString = autoclass('org.web3d.x3d.jsail.Core.MetadataStringObject')
MotorJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.MotorJointObject')
MovieTexture = autoclass('org.web3d.x3d.jsail.Texturing.MovieTextureObject')
MultiTexture = autoclass('org.web3d.x3d.jsail.Texturing.MultiTextureObject')
MultiTextureCoordinate = autoclass('org.web3d.x3d.jsail.Texturing.MultiTextureCoordinateObject')
MultiTextureTransform = autoclass('org.web3d.x3d.jsail.Texturing.MultiTextureTransformObject')
NavigationInfo = autoclass('org.web3d.x3d.jsail.Navigation.NavigationInfoObject')
Normal = autoclass('org.web3d.x3d.jsail.Rendering.NormalObject')
NormalInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.NormalInterpolatorObject')
NurbsCurve = autoclass('org.web3d.x3d.jsail.NURBS.NurbsCurveObject')
NurbsCurve2D = autoclass('org.web3d.x3d.jsail.NURBS.NurbsCurve2DObject')
NurbsOrientationInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsOrientationInterpolatorObject')
NurbsPatchSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsPatchSurfaceObject')
NurbsPositionInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsPositionInterpolatorObject')
NurbsSet = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSetObject')
NurbsSurfaceInterpolator = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSurfaceInterpolatorObject')
NurbsSweptSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSweptSurfaceObject')
NurbsSwungSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsSwungSurfaceObject')
NurbsTextureCoordinate = autoclass('org.web3d.x3d.jsail.NURBS.NurbsTextureCoordinateObject')
NurbsTrimmedSurface = autoclass('org.web3d.x3d.jsail.NURBS.NurbsTrimmedSurfaceObject')
OpacityMapVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.OpacityMapVolumeStyleObject')
OrientationChaser = autoclass('org.web3d.x3d.jsail.Followers.OrientationChaserObject')
OrientationDamper = autoclass('org.web3d.x3d.jsail.Followers.OrientationDamperObject')
OrientationInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.OrientationInterpolatorObject')
OrthoViewpoint = autoclass('org.web3d.x3d.jsail.Navigation.OrthoViewpointObject')
PackagedShader = autoclass('org.web3d.x3d.jsail.Shaders.PackagedShaderObject')
ParticleSystem = autoclass('org.web3d.x3d.jsail.ParticleSystems.ParticleSystemObject')
PickableGroup = autoclass('org.web3d.x3d.jsail.Picking.PickableGroupObject')
PixelTexture = autoclass('org.web3d.x3d.jsail.Texturing.PixelTextureObject')
PixelTexture3D = autoclass('org.web3d.x3d.jsail.Texturing3D.PixelTexture3DObject')
PlaneSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.PlaneSensorObject')
PointEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.PointEmitterObject')
PointLight = autoclass('org.web3d.x3d.jsail.Lighting.PointLightObject')
PointPickSensor = autoclass('org.web3d.x3d.jsail.Picking.PointPickSensorObject')
PointProperties = autoclass('org.web3d.x3d.jsail.Shape.PointPropertiesObject')
PointSet = autoclass('org.web3d.x3d.jsail.Rendering.PointSetObject')
Polyline2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Polyline2DObject')
PolylineEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.PolylineEmitterObject')
Polypoint2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Polypoint2DObject')
PositionChaser = autoclass('org.web3d.x3d.jsail.Followers.PositionChaserObject')
PositionChaser2D = autoclass('org.web3d.x3d.jsail.Followers.PositionChaser2DObject')
PositionDamper = autoclass('org.web3d.x3d.jsail.Followers.PositionDamperObject')
PositionDamper2D = autoclass('org.web3d.x3d.jsail.Followers.PositionDamper2DObject')
PositionInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.PositionInterpolatorObject')
PositionInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.PositionInterpolator2DObject')
PrimitivePickSensor = autoclass('org.web3d.x3d.jsail.Picking.PrimitivePickSensorObject')
ProgramShader = autoclass('org.web3d.x3d.jsail.Shaders.ProgramShaderObject')
ProjectionVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ProjectionVolumeStyleObject')
ProtoInstance = autoclass('org.web3d.x3d.jsail.Core.ProtoInstanceObject')
ProximitySensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.ProximitySensorObject')
QuadSet = autoclass('org.web3d.x3d.jsail.CADGeometry.QuadSetObject')
ReceiverPdu = autoclass('org.web3d.x3d.jsail.DIS.ReceiverPduObject')
Rectangle2D = autoclass('org.web3d.x3d.jsail.Geometry2D.Rectangle2DObject')
RigidBody = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBodyObject')
RigidBodyCollection = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.RigidBodyCollectionObject')
ScalarChaser = autoclass('org.web3d.x3d.jsail.Followers.ScalarChaserObject')
ScalarDamper = autoclass('org.web3d.x3d.jsail.Followers.ScalarDamperObject')
ScalarInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.ScalarInterpolatorObject')
ScreenFontStyle = autoclass('org.web3d.x3d.jsail.Layout.ScreenFontStyleObject')
ScreenGroup = autoclass('org.web3d.x3d.jsail.Layout.ScreenGroupObject')
Script = autoclass('org.web3d.x3d.jsail.Scripting.ScriptObject')
SegmentedVolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.SegmentedVolumeDataObject')
ShadedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ShadedVolumeStyleObject')
ShaderPart = autoclass('org.web3d.x3d.jsail.Shaders.ShaderPartObject')
ShaderProgram = autoclass('org.web3d.x3d.jsail.Shaders.ShaderProgramObject')
Shape = autoclass('org.web3d.x3d.jsail.Shape.ShapeObject')
SignalPdu = autoclass('org.web3d.x3d.jsail.DIS.SignalPduObject')
SilhouetteEnhancementVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.SilhouetteEnhancementVolumeStyleObject')
SingleAxisHingeJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.SingleAxisHingeJointObject')
SliderJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.SliderJointObject')
Sound = autoclass('org.web3d.x3d.jsail.Sound.SoundObject')
Sphere = autoclass('org.web3d.x3d.jsail.Geometry3D.SphereObject')
SphereSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.SphereSensorObject')
SplinePositionInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolatorObject')
SplinePositionInterpolator2D = autoclass('org.web3d.x3d.jsail.Interpolation.SplinePositionInterpolator2DObject')
SplineScalarInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SplineScalarInterpolatorObject')
SpotLight = autoclass('org.web3d.x3d.jsail.Lighting.SpotLightObject')
SquadOrientationInterpolator = autoclass('org.web3d.x3d.jsail.Interpolation.SquadOrientationInterpolatorObject')
StaticGroup = autoclass('org.web3d.x3d.jsail.Grouping.StaticGroupObject')
StringSensor = autoclass('org.web3d.x3d.jsail.KeyDeviceSensor.StringSensorObject')
SurfaceEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.SurfaceEmitterObject')
Switch = autoclass('org.web3d.x3d.jsail.Grouping.SwitchObject')
TexCoordChaser2D = autoclass('org.web3d.x3d.jsail.Followers.TexCoordChaser2DObject')
TexCoordDamper2D = autoclass('org.web3d.x3d.jsail.Followers.TexCoordDamper2DObject')
Text = autoclass('org.web3d.x3d.jsail.Text.TextObject')
TextureBackground = autoclass('org.web3d.x3d.jsail.EnvironmentalEffects.TextureBackgroundObject')
TextureCoordinate = autoclass('org.web3d.x3d.jsail.Texturing.TextureCoordinateObject')
TextureCoordinate3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate3DObject')
TextureCoordinate4D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureCoordinate4DObject')
TextureCoordinateGenerator = autoclass('org.web3d.x3d.jsail.Texturing.TextureCoordinateGeneratorObject')
TextureProperties = autoclass('org.web3d.x3d.jsail.Texturing.TexturePropertiesObject')
TextureTransform = autoclass('org.web3d.x3d.jsail.Texturing.TextureTransformObject')
TextureTransform3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureTransform3DObject')
TextureTransformMatrix3D = autoclass('org.web3d.x3d.jsail.Texturing3D.TextureTransformMatrix3DObject')
TimeSensor = autoclass('org.web3d.x3d.jsail.Time.TimeSensorObject')
TimeTrigger = autoclass('org.web3d.x3d.jsail.EventUtilities.TimeTriggerObject')
ToneMappedVolumeStyle = autoclass('org.web3d.x3d.jsail.VolumeRendering.ToneMappedVolumeStyleObject')
TouchSensor = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.TouchSensorObject')
Transform = autoclass('org.web3d.x3d.jsail.Grouping.TransformObject')
TransformSensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.TransformSensorObject')
TransmitterPdu = autoclass('org.web3d.x3d.jsail.DIS.TransmitterPduObject')
TriangleFanSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleFanSetObject')
TriangleSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleSetObject')
TriangleSet2D = autoclass('org.web3d.x3d.jsail.Geometry2D.TriangleSet2DObject')
TriangleStripSet = autoclass('org.web3d.x3d.jsail.Rendering.TriangleStripSetObject')
TwoSidedMaterial = autoclass('org.web3d.x3d.jsail.Shape.TwoSidedMaterialObject')
UniversalJoint = autoclass('org.web3d.x3d.jsail.RigidBodyPhysics.UniversalJointObject')
Viewpoint = autoclass('org.web3d.x3d.jsail.Navigation.ViewpointObject')
ViewpointGroup = autoclass('org.web3d.x3d.jsail.Navigation.ViewpointGroupObject')
Viewport = autoclass('org.web3d.x3d.jsail.Layering.ViewportObject')
VisibilitySensor = autoclass('org.web3d.x3d.jsail.EnvironmentalSensor.VisibilitySensorObject')
VolumeData = autoclass('org.web3d.x3d.jsail.VolumeRendering.VolumeDataObject')
VolumeEmitter = autoclass('org.web3d.x3d.jsail.ParticleSystems.VolumeEmitterObject')
VolumePickSensor = autoclass('org.web3d.x3d.jsail.Picking.VolumePickSensorObject')
WindPhysicsModel = autoclass('org.web3d.x3d.jsail.ParticleSystems.WindPhysicsModelObject')
WorldInfo = autoclass('org.web3d.x3d.jsail.Core.WorldInfoObject')
component = autoclass('org.web3d.x3d.jsail.Core.componentObject')
connect = autoclass('org.web3d.x3d.jsail.Core.connectObject')
EXPORT = autoclass('org.web3d.x3d.jsail.Networking.EXPORTObject')
ExternProtoDeclare = autoclass('org.web3d.x3d.jsail.Core.ExternProtoDeclareObject')
field = autoclass('org.web3d.x3d.jsail.Core.fieldObject')
fieldValue = autoclass('org.web3d.x3d.jsail.Core.fieldValueObject')
head = autoclass('org.web3d.x3d.jsail.Core.headObject')
IMPORT = autoclass('org.web3d.x3d.jsail.Networking.IMPORTObject')
IS = autoclass('org.web3d.x3d.jsail.Core.ISObject')
meta = autoclass('org.web3d.x3d.jsail.Core.metaObject')
ProtoBody = autoclass('org.web3d.x3d.jsail.Core.ProtoBodyObject')
ProtoDeclare = autoclass('org.web3d.x3d.jsail.Core.ProtoDeclareObject')
ProtoInterface = autoclass('org.web3d.x3d.jsail.Core.ProtoInterfaceObject')
ROUTE = autoclass('org.web3d.x3d.jsail.Core.ROUTEObject')
Scene = autoclass('org.web3d.x3d.jsail.Core.SceneObject')
unit = autoclass('org.web3d.x3d.jsail.Core.unitObject')
X3D = autoclass('org.web3d.x3d.jsail.Core.X3DObject')
SFBool = autoclass('org.web3d.x3d.jsail.fields.SFBoolObject')
MFBool = autoclass('org.web3d.x3d.jsail.fields.MFBoolObject')
SFColor = autoclass('org.web3d.x3d.jsail.fields.SFColorObject')
MFColor = autoclass('org.web3d.x3d.jsail.fields.MFColorObject')
SFColorRGBA = autoclass('org.web3d.x3d.jsail.fields.SFColorRGBAObject')
MFColorRGBA = autoclass('org.web3d.x3d.jsail.fields.MFColorRGBAObject')
SFDouble = autoclass('org.web3d.x3d.jsail.fields.SFDoubleObject')
MFDouble = autoclass('org.web3d.x3d.jsail.fields.MFDoubleObject')
SFFloat = autoclass('org.web3d.x3d.jsail.fields.SFFloatObject')
MFFloat = autoclass('org.web3d.x3d.jsail.fields.MFFloatObject')
SFImage = autoclass('org.web3d.x3d.jsail.fields.SFImageObject')
MFImage = autoclass('org.web3d.x3d.jsail.fields.MFImageObject')
SFInt32 = autoclass('org.web3d.x3d.jsail.fields.SFInt32Object')
MFInt32 = autoclass('org.web3d.x3d.jsail.fields.MFInt32Object')
SFMatrix3d = autoclass('org.web3d.x3d.jsail.fields.SFMatrix3dObject')
MFMatrix3d = autoclass('org.web3d.x3d.jsail.fields.MFMatrix3dObject')
SFMatrix3f = autoclass('org.web3d.x3d.jsail.fields.SFMatrix3fObject')
MFMatrix3f = autoclass('org.web3d.x3d.jsail.fields.MFMatrix3fObject')
SFMatrix4d = autoclass('org.web3d.x3d.jsail.fields.SFMatrix4dObject')
MFMatrix4d = autoclass('org.web3d.x3d.jsail.fields.MFMatrix4dObject')
SFMatrix4f = autoclass('org.web3d.x3d.jsail.fields.SFMatrix4fObject')
MFMatrix4f = autoclass('org.web3d.x3d.jsail.fields.MFMatrix4fObject')
SFString = autoclass('org.web3d.x3d.jsail.fields.SFStringObject')
SFNode = autoclass('org.web3d.x3d.jsail.fields.SFNodeObject')
MFNode = autoclass('org.web3d.x3d.jsail.fields.MFNodeObject')
SFRotation = autoclass('org.web3d.x3d.jsail.fields.SFRotationObject')
MFRotation = autoclass('org.web3d.x3d.jsail.fields.MFRotationObject')
MFString = autoclass('org.web3d.x3d.jsail.fields.MFStringObject')
SFTime = autoclass('org.web3d.x3d.jsail.fields.SFTimeObject')
MFTime = autoclass('org.web3d.x3d.jsail.fields.MFTimeObject')
SFVec2d = autoclass('org.web3d.x3d.jsail.fields.SFVec2dObject')
MFVec2d = autoclass('org.web3d.x3d.jsail.fields.MFVec2dObject')
SFVec2f = autoclass('org.web3d.x3d.jsail.fields.SFVec2fObject')
MFVec2f = autoclass('org.web3d.x3d.jsail.fields.MFVec2fObject')
SFVec3d = autoclass('org.web3d.x3d.jsail.fields.SFVec3dObject')
MFVec3d = autoclass('org.web3d.x3d.jsail.fields.MFVec3dObject')
SFVec3f = autoclass('org.web3d.x3d.jsail.fields.SFVec3fObject')
MFVec3f = autoclass('org.web3d.x3d.jsail.fields.MFVec3fObject')
SFVec4d = autoclass('org.web3d.x3d.jsail.fields.SFVec4dObject')
MFVec4d = autoclass('org.web3d.x3d.jsail.fields.MFVec4dObject')
SFVec4f = autoclass('org.web3d.x3d.jsail.fields.SFVec4fObject')
MFVec4f = autoclass('org.web3d.x3d.jsail.fields.MFVec4fObject')
