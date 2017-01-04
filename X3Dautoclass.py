import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from jnius import autoclass
X3DNode = autoclass('org.web3d.x3d.sai.Core.X3DNode')
X3DChildNode = autoclass('org.web3d.x3d.sai.Core.X3DChildNode')
X3DSensorNode = autoclass('org.web3d.x3d.sai.Core.X3DSensorNode')
X3DKeyDeviceSensorNode = autoclass('org.web3d.x3d.sai.KeyDeviceSensor.X3DKeyDeviceSensorNode')
StringSensorObject = autoclass('org.web3d.x3d.java.KeyDeviceSensor.StringSensorObject')
RigidBodyObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.RigidBodyObject')
X3DPointingDeviceSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DPointingDeviceSensorNode')
X3DTouchSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DTouchSensorNode')
TouchSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.TouchSensorObject')
X3DPickSensorNode = autoclass('org.web3d.x3d.sai.Picking.X3DPickSensorNode')
LinePickSensorObject = autoclass('org.web3d.x3d.java.Picking.LinePickSensorObject')
X3DParticleEmitterNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticleEmitterNode')
PointEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.PointEmitterObject')
X3DDragSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DDragSensorNode')
X3DBindableNode = autoclass('org.web3d.x3d.sai.Core.X3DBindableNode')
X3DViewpointNode = autoclass('org.web3d.x3d.sai.Navigation.X3DViewpointNode')
X3DLayoutNode = autoclass('org.web3d.x3d.sai.Layout.X3DLayoutNode')
X3DBoundedObject = autoclass('org.web3d.x3d.sai.Grouping.X3DBoundedObject')
HAnimJointObject = autoclass('org.web3d.x3d.java.HAnim.HAnimJointObject')
X3DFollowerNode = autoclass('org.web3d.x3d.sai.Followers.X3DFollowerNode')
X3DChaserNode = autoclass('org.web3d.x3d.sai.Followers.X3DChaserNode')
PositionChaser2DObject = autoclass('org.web3d.x3d.java.Followers.PositionChaser2DObject')
X3DUrlObject = autoclass('org.web3d.x3d.sai.Networking.X3DUrlObject')
ShaderPartObject = autoclass('org.web3d.x3d.java.Shaders.ShaderPartObject')
X3DVolumeDataNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeDataNode')
IsoSurfaceVolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.IsoSurfaceVolumeDataObject')
X3DInterpolatorNode = autoclass('org.web3d.x3d.sai.Interpolation.X3DInterpolatorNode')
SplinePositionInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SplinePositionInterpolatorObject')
X3DGroupingNode = autoclass('org.web3d.x3d.sai.Grouping.X3DGroupingNode')
LayoutGroupObject = autoclass('org.web3d.x3d.java.Layout.LayoutGroupObject')
EaseInEaseOutObject = autoclass('org.web3d.x3d.java.Interpolation.EaseInEaseOutObject')
X3DAppearanceChildNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceChildNode')
X3DTextureTransformNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureTransformNode')
TextureTransformObject = autoclass('org.web3d.x3d.java.Texturing.TextureTransformObject')
ExternProtoDeclareObject = autoclass('org.web3d.x3d.java.Core.ExternProtoDeclareObject')
X3DGeometricPropertyNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometricPropertyNode')
X3DVertexAttributeNode = autoclass('org.web3d.x3d.sai.Shaders.X3DVertexAttributeNode')
Contour2DObject = autoclass('org.web3d.x3d.java.NURBS.Contour2DObject')
Matrix4VertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.Matrix4VertexAttributeObject')
X3DVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeRenderStyleNode')
ProjectionVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ProjectionVolumeStyleObject')
X3DLayerNode = autoclass('org.web3d.x3d.sai.Layering.X3DLayerNode')
ColorInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.ColorInterpolatorObject')
X3DMaterialNode = autoclass('org.web3d.x3d.sai.Shape.X3DMaterialNode')
MaterialObject = autoclass('org.web3d.x3d.java.Shape.MaterialObject')
X3DPrototypeInstance = autoclass('org.web3d.x3d.sai.Core.X3DPrototypeInstance')
ProtoInstanceObject = autoclass('org.web3d.x3d.java.Core.ProtoInstanceObject')
MultiTextureTransformObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureTransformObject')
X3DInfoNode = autoclass('org.web3d.x3d.sai.Core.X3DInfoNode')
WorldInfoObject = autoclass('org.web3d.x3d.java.Core.WorldInfoObject')
X3DComposableVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DComposableVolumeRenderStyleNode')
BlendedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.BlendedVolumeStyleObject')
IMPORTObject = autoclass('org.web3d.x3d.java.Networking.IMPORTObject')
X3DCoordinateNode = autoclass('org.web3d.x3d.sai.Rendering.X3DCoordinateNode')
X3DTextureCoordinateNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureCoordinateNode')
MultiTextureCoordinateObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureCoordinateObject')
X3DGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometryNode')
ElevationGridObject = autoclass('org.web3d.x3d.java.Geometry3D.ElevationGridObject')
X3DTextureNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureNode')
X3DTexture3DNode = autoclass('org.web3d.x3d.sai.Texturing3D.X3DTexture3DNode')
X3DBackgroundNode = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DBackgroundNode')
TextureBackgroundObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.TextureBackgroundObject')
BooleanFilterObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanFilterObject')
ISObject = autoclass('org.web3d.x3d.java.Core.ISObject')
X3DRigidJointNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DRigidJointNode')
UniversalJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.UniversalJointObject')
X3DNormalNode = autoclass('org.web3d.x3d.sai.Rendering.X3DNormalNode')
NormalObject = autoclass('org.web3d.x3d.java.Rendering.NormalObject')
BillboardObject = autoclass('org.web3d.x3d.java.Navigation.BillboardObject')
PolylineEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.PolylineEmitterObject')
X3DMetadataObject = autoclass('org.web3d.x3d.sai.Core.X3DMetadataObject')
MetadataSetObject = autoclass('org.web3d.x3d.java.Core.MetadataSetObject')
X3DNurbsControlCurveNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsControlCurveNode')
MetadataDoubleObject = autoclass('org.web3d.x3d.java.Core.MetadataDoubleObject')
ConeObject = autoclass('org.web3d.x3d.java.Geometry3D.ConeObject')
TransformObject = autoclass('org.web3d.x3d.java.Grouping.TransformObject')
X3DAppearanceNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceNode')
X3DLightNode = autoclass('org.web3d.x3d.sai.Lighting.X3DLightNode')
DirectionalLightObject = autoclass('org.web3d.x3d.java.Lighting.DirectionalLightObject')
X3DComposedGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DComposedGeometryNode')
IndexedTriangleFanSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleFanSetObject')
ComposedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ComposedVolumeStyleObject')
LayoutLayerObject = autoclass('org.web3d.x3d.java.Layout.LayoutLayerObject')
GeoLocationObject = autoclass('org.web3d.x3d.java.Geospatial.GeoLocationObject')
SwitchObject = autoclass('org.web3d.x3d.java.Grouping.SwitchObject')
NavigationInfoObject = autoclass('org.web3d.x3d.java.Navigation.NavigationInfoObject')
OrthoViewpointObject = autoclass('org.web3d.x3d.java.Navigation.OrthoViewpointObject')
X3DNetworkSensorNode = autoclass('org.web3d.x3d.sai.Networking.X3DNetworkSensorNode')
TransmitterPduObject = autoclass('org.web3d.x3d.java.DIS.TransmitterPduObject')
BoxObject = autoclass('org.web3d.x3d.java.Geometry3D.BoxObject')
AnchorObject = autoclass('org.web3d.x3d.java.Networking.AnchorObject')
HAnimSegmentObject = autoclass('org.web3d.x3d.java.HAnim.HAnimSegmentObject')
ClipPlaneObject = autoclass('org.web3d.x3d.java.Rendering.ClipPlaneObject')
CADLayerObject = autoclass('org.web3d.x3d.java.CADGeometry.CADLayerObject')
SurfaceEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.SurfaceEmitterObject')
VolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.VolumeDataObject')
NurbsPositionInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsPositionInterpolatorObject')
X3DColorNode = autoclass('org.web3d.x3d.sai.Rendering.X3DColorNode')
ColorRGBAObject = autoclass('org.web3d.x3d.java.Rendering.ColorRGBAObject')
MotorJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.MotorJointObject')
X3DTriggerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DTriggerNode')
TimeTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.TimeTriggerObject')
BooleanTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanTriggerObject')
X3DSequencerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DSequencerNode')
X3DTexture2DNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTexture2DNode')
ImageTextureObject = autoclass('org.web3d.x3d.java.Texturing.ImageTextureObject')
LinePropertiesObject = autoclass('org.web3d.x3d.java.Shape.LinePropertiesObject')
CylinderObject = autoclass('org.web3d.x3d.java.Geometry3D.CylinderObject')
ExtrusionObject = autoclass('org.web3d.x3d.java.Geometry3D.ExtrusionObject')
BallJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.BallJointObject')
TwoSidedMaterialObject = autoclass('org.web3d.x3d.java.Shape.TwoSidedMaterialObject')
PixelTextureObject = autoclass('org.web3d.x3d.java.Texturing.PixelTextureObject')
PointPickSensorObject = autoclass('org.web3d.x3d.java.Picking.PointPickSensorObject')
X3DEnvironmentTextureNode = autoclass('org.web3d.x3d.sai.CubeMapTexturing.X3DEnvironmentTextureNode')
GeneratedCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.GeneratedCubeMapTextureObject')
ShadedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ShadedVolumeStyleObject')
X3DTimeDependentNode = autoclass('org.web3d.x3d.sai.Time.X3DTimeDependentNode')
X3DSoundSourceNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundSourceNode')
AudioClipObject = autoclass('org.web3d.x3d.java.Sound.AudioClipObject')
X3DScriptNode = autoclass('org.web3d.x3d.sai.Scripting.X3DScriptNode')
ScriptObject = autoclass('org.web3d.x3d.java.Scripting.ScriptObject')
SphereSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.SphereSensorObject')
MetadataStringObject = autoclass('org.web3d.x3d.java.Core.MetadataStringObject')
OpacityMapVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.OpacityMapVolumeStyleObject')
X3DProductStructureChildNode = autoclass('org.web3d.x3d.sai.CADGeometry.X3DProductStructureChildNode')
CADFaceObject = autoclass('org.web3d.x3d.java.CADGeometry.CADFaceObject')
VolumeEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.VolumeEmitterObject')
X3DParticlePhysicsModelNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticlePhysicsModelNode')
TexCoordChaser2DObject = autoclass('org.web3d.x3d.java.Followers.TexCoordChaser2DObject')
Polyline2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Polyline2DObject')
StaticGroupObject = autoclass('org.web3d.x3d.java.Grouping.StaticGroupObject')
ProtoDeclareObject = autoclass('org.web3d.x3d.java.Core.ProtoDeclareObject')
SingleAxisHingeJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.SingleAxisHingeJointObject')
ProtoBodyObject = autoclass('org.web3d.x3d.java.Core.ProtoBodyObject')
GeoElevationGridObject = autoclass('org.web3d.x3d.java.Geospatial.GeoElevationGridObject')
IndexedLineSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedLineSetObject')
ImageCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.ImageCubeMapTextureObject')
PlaneSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.PlaneSensorObject')
CoordinateChaserObject = autoclass('org.web3d.x3d.java.Followers.CoordinateChaserObject')
TriangleSet2DObject = autoclass('org.web3d.x3d.java.Geometry2D.TriangleSet2DObject')
CoordinateObject = autoclass('org.web3d.x3d.java.Rendering.CoordinateObject')
LayoutObject = autoclass('org.web3d.x3d.java.Layout.LayoutObject')
X3DEnvironmentalSensorNode = autoclass('org.web3d.x3d.sai.EnvironmentalSensor.X3DEnvironmentalSensorNode')
GeoProximitySensorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoProximitySensorObject')
NurbsOrientationInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsOrientationInterpolatorObject')
X3DDamperNode = autoclass('org.web3d.x3d.sai.Followers.X3DDamperNode')
ScalarDamperObject = autoclass('org.web3d.x3d.java.Followers.ScalarDamperObject')
SplinePositionInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.SplinePositionInterpolator2DObject')
X3DShaderNode = autoclass('org.web3d.x3d.sai.Shaders.X3DShaderNode')
X3DProgrammableShaderObject = autoclass('org.web3d.x3d.sai.Shaders.X3DProgrammableShaderObject')
ComposedShaderObject = autoclass('org.web3d.x3d.java.Shaders.ComposedShaderObject')
MetadataFloatObject = autoclass('org.web3d.x3d.java.Core.MetadataFloatObject')
GeoPositionInterpolatorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoPositionInterpolatorObject')
ProximitySensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.ProximitySensorObject')
SceneObject = autoclass('org.web3d.x3d.java.Core.SceneObject')
GeoViewpointObject = autoclass('org.web3d.x3d.java.Geospatial.GeoViewpointObject')
X3DShapeNode = autoclass('org.web3d.x3d.sai.Shape.X3DShapeNode')
ShapeObject = autoclass('org.web3d.x3d.java.Shape.ShapeObject')
X3DNBodyCollidableNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollidableNode')
CollidableOffsetObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollidableOffsetObject')
X3DFontStyleNode = autoclass('org.web3d.x3d.sai.Text.X3DFontStyleNode')
ImageTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.ImageTexture3DObject')
ScalarChaserObject = autoclass('org.web3d.x3d.java.Followers.ScalarChaserObject')
CylinderSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.CylinderSensorObject')
X3DParametricGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DParametricGeometryNode')
NurbsSweptSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSweptSurfaceObject')
Disk2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Disk2DObject')
IntegerSequencerObject = autoclass('org.web3d.x3d.java.EventUtilities.IntegerSequencerObject')
Circle2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Circle2DObject')
TextureCoordinate3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureCoordinate3DObject')
GeoMetadataObject = autoclass('org.web3d.x3d.java.Geospatial.GeoMetadataObject')
PrimitivePickSensorObject = autoclass('org.web3d.x3d.java.Picking.PrimitivePickSensorObject')
X3DNurbsSurfaceGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsSurfaceGeometryNode')
NurbsPatchSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsPatchSurfaceObject')
headObject = autoclass('org.web3d.x3d.java.Core.headObject')
BackgroundObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.BackgroundObject')
PointSetObject = autoclass('org.web3d.x3d.java.Rendering.PointSetObject')
PackagedShaderObject = autoclass('org.web3d.x3d.java.Shaders.PackagedShaderObject')
MultiTextureObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureObject')
ContactObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.ContactObject')
TextureCoordinate4DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureCoordinate4DObject')
NurbsCurveObject = autoclass('org.web3d.x3d.java.NURBS.NurbsCurveObject')
fieldObject = autoclass('org.web3d.x3d.java.Core.fieldObject')
CartoonVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.CartoonVolumeStyleObject')
SpotLightObject = autoclass('org.web3d.x3d.java.Lighting.SpotLightObject')
GroupObject = autoclass('org.web3d.x3d.java.Grouping.GroupObject')
EdgeEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.EdgeEnhancementVolumeStyleObject')
ColorDamperObject = autoclass('org.web3d.x3d.java.Followers.ColorDamperObject')
WindPhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.WindPhysicsModelObject')
TriangleFanSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleFanSetObject')
SignalPduObject = autoclass('org.web3d.x3d.java.DIS.SignalPduObject')
VisibilitySensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.VisibilitySensorObject')
BooleanToggleObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanToggleObject')
MetadataIntegerObject = autoclass('org.web3d.x3d.java.Core.MetadataIntegerObject')
IndexedFaceSetObject = autoclass('org.web3d.x3d.java.Geometry3D.IndexedFaceSetObject')
CollidableShapeObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollidableShapeObject')
PositionInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.PositionInterpolator2DObject')
TextureCoordinateObject = autoclass('org.web3d.x3d.java.Texturing.TextureCoordinateObject')
OrientationDamperObject = autoclass('org.web3d.x3d.java.Followers.OrientationDamperObject')
HAnimHumanoidObject = autoclass('org.web3d.x3d.java.HAnim.HAnimHumanoidObject')
ToneMappedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ToneMappedVolumeStyleObject')
NurbsSwungSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSwungSurfaceObject')
ShaderProgramObject = autoclass('org.web3d.x3d.java.Shaders.ShaderProgramObject')
MovieTextureObject = autoclass('org.web3d.x3d.java.Texturing.MovieTextureObject')
ROUTEObject = autoclass('org.web3d.x3d.java.Core.ROUTEObject')
FontStyleObject = autoclass('org.web3d.x3d.java.Text.FontStyleObject')
MetadataBooleanObject = autoclass('org.web3d.x3d.java.Core.MetadataBooleanObject')
PointLightObject = autoclass('org.web3d.x3d.java.Lighting.PointLightObject')
CoordinateDoubleObject = autoclass('org.web3d.x3d.java.NURBS.CoordinateDoubleObject')
LODObject = autoclass('org.web3d.x3d.java.Navigation.LODObject')
TimeSensorObject = autoclass('org.web3d.x3d.java.Time.TimeSensorObject')
X3DFogObject = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DFogObject')
CollisionSensorObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionSensorObject')
ConeEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.ConeEmitterObject')
CADPartObject = autoclass('org.web3d.x3d.java.CADGeometry.CADPartObject')
NurbsTrimmedSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsTrimmedSurfaceObject')
ForcePhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.ForcePhysicsModelObject')
KeySensorObject = autoclass('org.web3d.x3d.java.KeyDeviceSensor.KeySensorObject')
IndexedTriangleStripSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleStripSetObject')
Rectangle2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Rectangle2DObject')
FogCoordinateObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.FogCoordinateObject')
X3DViewportNode = autoclass('org.web3d.x3d.sai.Layering.X3DViewportNode')
DISEntityTypeMappingObject = autoclass('org.web3d.x3d.java.DIS.DISEntityTypeMappingObject')
Matrix3VertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.Matrix3VertexAttributeObject')
ColorChaserObject = autoclass('org.web3d.x3d.java.Followers.ColorChaserObject')
NurbsSurfaceInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSurfaceInterpolatorObject')
CADAssemblyObject = autoclass('org.web3d.x3d.java.CADGeometry.CADAssemblyObject')
GeoOriginObject = autoclass('org.web3d.x3d.java.Geospatial.GeoOriginObject')
SilhouetteEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.SilhouetteEnhancementVolumeStyleObject')
FillPropertiesObject = autoclass('org.web3d.x3d.java.Shape.FillPropertiesObject')
X3DObject = autoclass('org.web3d.x3d.java.Core.X3DObject')
LineSetObject = autoclass('org.web3d.x3d.java.Rendering.LineSetObject')
FogObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.FogObject')
TexCoordDamper2DObject = autoclass('org.web3d.x3d.java.Followers.TexCoordDamper2DObject')
ComposedCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.ComposedCubeMapTextureObject')
PositionChaserObject = autoclass('org.web3d.x3d.java.Followers.PositionChaserObject')
CoordinateDamperObject = autoclass('org.web3d.x3d.java.Followers.CoordinateDamperObject')
X3DPickableObject = autoclass('org.web3d.x3d.sai.Picking.X3DPickableObject')
ViewpointGroupObject = autoclass('org.web3d.x3d.java.Navigation.ViewpointGroupObject')
PositionInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.PositionInterpolatorObject')
ParticleSystemObject = autoclass('org.web3d.x3d.java.ParticleSystems.ParticleSystemObject')
SplineScalarInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SplineScalarInterpolatorObject')
X3DNBodyCollisionSpaceNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollisionSpaceNode')
TextObject = autoclass('org.web3d.x3d.java.Text.TextObject')
ArcClose2DObject = autoclass('org.web3d.x3d.java.Geometry2D.ArcClose2DObject')
TextureTransformMatrix3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureTransformMatrix3DObject')
NurbsSetObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSetObject')
ColorObject = autoclass('org.web3d.x3d.java.Rendering.ColorObject')
NurbsCurve2DObject = autoclass('org.web3d.x3d.java.NURBS.NurbsCurve2DObject')
OrientationChaserObject = autoclass('org.web3d.x3d.java.Followers.OrientationChaserObject')
HAnimDisplacerObject = autoclass('org.web3d.x3d.java.HAnim.HAnimDisplacerObject')
unitObject = autoclass('org.web3d.x3d.java.Core.unitObject')
PositionDamperObject = autoclass('org.web3d.x3d.java.Followers.PositionDamperObject')
TexturePropertiesObject = autoclass('org.web3d.x3d.java.Texturing.TexturePropertiesObject')
SegmentedVolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.SegmentedVolumeDataObject')
DoubleAxisHingeJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.DoubleAxisHingeJointObject')
RigidBodyCollectionObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.RigidBodyCollectionObject')
EXPORTObject = autoclass('org.web3d.x3d.java.Networking.EXPORTObject')
CollisionCollectionObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionCollectionObject')
IndexedTriangleSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleSetObject')
DISEntityManagerObject = autoclass('org.web3d.x3d.java.DIS.DISEntityManagerObject')
LocalFogObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.LocalFogObject')
Arc2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Arc2DObject')
ExplosionEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.ExplosionEmitterObject')
TransformSensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.TransformSensorObject')
LayerSetObject = autoclass('org.web3d.x3d.java.Layering.LayerSetObject')
AppearanceObject = autoclass('org.web3d.x3d.java.Shape.AppearanceObject')
ScalarInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.ScalarInterpolatorObject')
connectObject = autoclass('org.web3d.x3d.java.Core.connectObject')
HAnimSiteObject = autoclass('org.web3d.x3d.java.HAnim.HAnimSiteObject')
CollisionSpaceObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionSpaceObject')
ContourPolyline2DObject = autoclass('org.web3d.x3d.java.NURBS.ContourPolyline2DObject')
TextureTransform3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureTransform3DObject')
BoundedPhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.BoundedPhysicsModelObject')
TriangleStripSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleStripSetObject')
InlineObject = autoclass('org.web3d.x3d.java.Networking.InlineObject')
SquadOrientationInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SquadOrientationInterpolatorObject')
ProtoInterfaceObject = autoclass('org.web3d.x3d.java.Core.ProtoInterfaceObject')
PositionDamper2DObject = autoclass('org.web3d.x3d.java.Followers.PositionDamper2DObject')
ComposedTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.ComposedTexture3DObject')
X3DSoundNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundNode')
CoordinateInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.CoordinateInterpolator2DObject')
PixelTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.PixelTexture3DObject')
CoordinateInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.CoordinateInterpolatorObject')
NurbsTextureCoordinateObject = autoclass('org.web3d.x3d.java.NURBS.NurbsTextureCoordinateObject')
IntegerTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.IntegerTriggerObject')
fieldValueObject = autoclass('org.web3d.x3d.java.Core.fieldValueObject')
CollisionObject = autoclass('org.web3d.x3d.java.Navigation.CollisionObject')
EspduTransformObject = autoclass('org.web3d.x3d.java.DIS.EspduTransformObject')
FloatVertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.FloatVertexAttributeObject')
ScreenGroupObject = autoclass('org.web3d.x3d.java.Layout.ScreenGroupObject')
ScreenFontStyleObject = autoclass('org.web3d.x3d.java.Layout.ScreenFontStyleObject')
GeoTouchSensorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoTouchSensorObject')
BooleanSequencerObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanSequencerObject')
IndexedQuadSetObject = autoclass('org.web3d.x3d.java.CADGeometry.IndexedQuadSetObject')
TriangleSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleSetObject')
OrientationInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.OrientationInterpolatorObject')
NormalInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.NormalInterpolatorObject')
ProgramShaderObject = autoclass('org.web3d.x3d.java.Shaders.ProgramShaderObject')
LayerObject = autoclass('org.web3d.x3d.java.Layering.LayerObject')
ReceiverPduObject = autoclass('org.web3d.x3d.java.DIS.ReceiverPduObject')
LoadSensorObject = autoclass('org.web3d.x3d.java.Networking.LoadSensorObject')
SphereObject = autoclass('org.web3d.x3d.java.Geometry3D.SphereObject')
componentObject = autoclass('org.web3d.x3d.java.Core.componentObject')
GeoTransformObject = autoclass('org.web3d.x3d.java.Geospatial.GeoTransformObject')
metaObject = autoclass('org.web3d.x3d.java.Core.metaObject')
VolumePickSensorObject = autoclass('org.web3d.x3d.java.Picking.VolumePickSensorObject')
GeoLODObject = autoclass('org.web3d.x3d.java.Geospatial.GeoLODObject')
BoundaryEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.BoundaryEnhancementVolumeStyleObject')
PickableGroupObject = autoclass('org.web3d.x3d.java.Picking.PickableGroupObject')
ViewportObject = autoclass('org.web3d.x3d.java.Layering.ViewportObject')
GeoCoordinateObject = autoclass('org.web3d.x3d.java.Geospatial.GeoCoordinateObject')
ViewpointObject = autoclass('org.web3d.x3d.java.Navigation.ViewpointObject')
SliderJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.SliderJointObject')
Polypoint2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Polypoint2DObject')
QuadSetObject = autoclass('org.web3d.x3d.java.CADGeometry.QuadSetObject')
TextureCoordinateGeneratorObject = autoclass('org.web3d.x3d.java.Texturing.TextureCoordinateGeneratorObject')
SoundObject = autoclass('org.web3d.x3d.java.Sound.SoundObject')
