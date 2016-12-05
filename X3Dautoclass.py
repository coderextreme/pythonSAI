import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from jnius import autoclass
X3DNode = autoclass('org.web3d.x3d.sai.Core.X3DNode')
X3DLayerNode = autoclass('org.web3d.x3d.sai.Layering.X3DLayerNode')
LayoutLayerObject = autoclass('org.web3d.x3d.java.Layout.LayoutLayerObject')
X3DChildNode = autoclass('org.web3d.x3d.sai.Core.X3DChildNode')
X3DTriggerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DTriggerNode')
IntegerTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.IntegerTriggerObject')
X3DGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometryNode')
IndexedLineSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedLineSetObject')
X3DAppearanceChildNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceChildNode')
X3DMaterialNode = autoclass('org.web3d.x3d.sai.Shape.X3DMaterialNode')
MaterialObject = autoclass('org.web3d.x3d.java.Shape.MaterialObject')
X3DSensorNode = autoclass('org.web3d.x3d.sai.Core.X3DSensorNode')
X3DPointingDeviceSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DPointingDeviceSensorNode')
X3DDragSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DDragSensorNode')
PlaneSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.PlaneSensorObject')
DISEntityManagerObject = autoclass('org.web3d.x3d.java.DIS.DISEntityManagerObject')
X3DProductStructureChildNode = autoclass('org.web3d.x3d.sai.CADGeometry.X3DProductStructureChildNode')
X3DTextureNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureNode')
X3DTexture3DNode = autoclass('org.web3d.x3d.sai.Texturing3D.X3DTexture3DNode')
X3DUrlObject = autoclass('org.web3d.x3d.sai.Networking.X3DUrlObject')
ImageTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.ImageTexture3DObject')
X3DBoundedObject = autoclass('org.web3d.x3d.sai.Grouping.X3DBoundedObject')
X3DGroupingNode = autoclass('org.web3d.x3d.sai.Grouping.X3DGroupingNode')
AnchorObject = autoclass('org.web3d.x3d.java.Networking.AnchorObject')
CADFaceObject = autoclass('org.web3d.x3d.java.CADGeometry.CADFaceObject')
X3DGeometricPropertyNode = autoclass('org.web3d.x3d.sai.Rendering.X3DGeometricPropertyNode')
X3DNormalNode = autoclass('org.web3d.x3d.sai.Rendering.X3DNormalNode')
X3DFontStyleNode = autoclass('org.web3d.x3d.sai.Text.X3DFontStyleNode')
FontStyleObject = autoclass('org.web3d.x3d.java.Text.FontStyleObject')
X3DFollowerNode = autoclass('org.web3d.x3d.sai.Followers.X3DFollowerNode')
X3DDamperNode = autoclass('org.web3d.x3d.sai.Followers.X3DDamperNode')
OrientationDamperObject = autoclass('org.web3d.x3d.java.Followers.OrientationDamperObject')
X3DEnvironmentTextureNode = autoclass('org.web3d.x3d.sai.CubeMapTexturing.X3DEnvironmentTextureNode')
BooleanTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanTriggerObject')
X3DParametricGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DParametricGeometryNode')
X3DNurbsSurfaceGeometryNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsSurfaceGeometryNode')
X3DFogObject = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DFogObject')
LocalFogObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.LocalFogObject')
X3DBindableNode = autoclass('org.web3d.x3d.sai.Core.X3DBindableNode')
X3DViewpointNode = autoclass('org.web3d.x3d.sai.Navigation.X3DViewpointNode')
ViewpointObject = autoclass('org.web3d.x3d.java.Navigation.ViewpointObject')
X3DNetworkSensorNode = autoclass('org.web3d.x3d.sai.Networking.X3DNetworkSensorNode')
X3DShapeNode = autoclass('org.web3d.x3d.sai.Shape.X3DShapeNode')
X3DSequencerNode = autoclass('org.web3d.x3d.sai.EventUtilities.X3DSequencerNode')
BooleanSequencerObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanSequencerObject')
X3DColorNode = autoclass('org.web3d.x3d.sai.Rendering.X3DColorNode')
ColorObject = autoclass('org.web3d.x3d.java.Rendering.ColorObject')
X3DNBodyCollidableNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollidableNode')
CollidableOffsetObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollidableOffsetObject')
X3DChaserNode = autoclass('org.web3d.x3d.sai.Followers.X3DChaserNode')
PositionChaser2DObject = autoclass('org.web3d.x3d.java.Followers.PositionChaser2DObject')
Arc2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Arc2DObject')
TimeTriggerObject = autoclass('org.web3d.x3d.java.EventUtilities.TimeTriggerObject')
X3DTextureTransformNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureTransformNode')
TextureTransform3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureTransform3DObject')
FogCoordinateObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.FogCoordinateObject')
X3DBackgroundNode = autoclass('org.web3d.x3d.sai.EnvironmentalEffects.X3DBackgroundNode')
BackgroundObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.BackgroundObject')
Disk2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Disk2DObject')
X3DRigidJointNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DRigidJointNode')
MotorJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.MotorJointObject')
X3DTextureCoordinateNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTextureCoordinateNode')
TextureCoordinate4DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureCoordinate4DObject')
X3DVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeRenderStyleNode')
X3DComposableVolumeRenderStyleNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DComposableVolumeRenderStyleNode')
OpacityMapVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.OpacityMapVolumeStyleObject')
Rectangle2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Rectangle2DObject')
BoxObject = autoclass('org.web3d.x3d.java.Geometry3D.BoxObject')
FogObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.FogObject')
Polyline2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Polyline2DObject')
TextureCoordinateGeneratorObject = autoclass('org.web3d.x3d.java.Texturing.TextureCoordinateGeneratorObject')
X3DTexture2DNode = autoclass('org.web3d.x3d.sai.Texturing.X3DTexture2DNode')
X3DParticlePhysicsModelNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticlePhysicsModelNode')
X3DPrototypeInstance = autoclass('org.web3d.x3d.sai.Core.X3DPrototypeInstance')
ProtoInstanceObject = autoclass('org.web3d.x3d.java.Core.ProtoInstanceObject')
X3DVertexAttributeNode = autoclass('org.web3d.x3d.sai.Shaders.X3DVertexAttributeNode')
FloatVertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.FloatVertexAttributeObject')
X3DParticleEmitterNode = autoclass('org.web3d.x3d.sai.ParticleSystems.X3DParticleEmitterNode')
PolylineEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.PolylineEmitterObject')
X3DViewportNode = autoclass('org.web3d.x3d.sai.Layering.X3DViewportNode')
SliderJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.SliderJointObject')
BoundedPhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.BoundedPhysicsModelObject')
ComposedCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.ComposedCubeMapTextureObject')
UniversalJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.UniversalJointObject')
CartoonVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.CartoonVolumeStyleObject')
TexCoordDamper2DObject = autoclass('org.web3d.x3d.java.Followers.TexCoordDamper2DObject')
ComposedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ComposedVolumeStyleObject')
TexCoordChaser2DObject = autoclass('org.web3d.x3d.java.Followers.TexCoordChaser2DObject')
X3DPickSensorNode = autoclass('org.web3d.x3d.sai.Picking.X3DPickSensorNode')
PointPickSensorObject = autoclass('org.web3d.x3d.java.Picking.PointPickSensorObject')
EaseInEaseOutObject = autoclass('org.web3d.x3d.java.Interpolation.EaseInEaseOutObject')
GeoViewpointObject = autoclass('org.web3d.x3d.java.Geospatial.GeoViewpointObject')
MultiTextureCoordinateObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureCoordinateObject')
BooleanToggleObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanToggleObject')
TransformObject = autoclass('org.web3d.x3d.java.Grouping.TransformObject')
X3DEnvironmentalSensorNode = autoclass('org.web3d.x3d.sai.EnvironmentalSensor.X3DEnvironmentalSensorNode')
GeoProximitySensorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoProximitySensorObject')
ComposedTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.ComposedTexture3DObject')
LayerObject = autoclass('org.web3d.x3d.java.Layering.LayerObject')
fieldObject = autoclass('org.web3d.x3d.java.Core.fieldObject')
ProjectionVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ProjectionVolumeStyleObject')
CylinderObject = autoclass('org.web3d.x3d.java.Geometry3D.CylinderObject')
TwoSidedMaterialObject = autoclass('org.web3d.x3d.java.Shape.TwoSidedMaterialObject')
fieldValueObject = autoclass('org.web3d.x3d.java.Core.fieldValueObject')
ScreenFontStyleObject = autoclass('org.web3d.x3d.java.Layout.ScreenFontStyleObject')
X3DCoordinateNode = autoclass('org.web3d.x3d.sai.Rendering.X3DCoordinateNode')
GeoCoordinateObject = autoclass('org.web3d.x3d.java.Geospatial.GeoCoordinateObject')
TextureBackgroundObject = autoclass('org.web3d.x3d.java.EnvironmentalEffects.TextureBackgroundObject')
X3DSoundNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundNode')
TextureTransformMatrix3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureTransformMatrix3DObject')
LineSetObject = autoclass('org.web3d.x3d.java.Rendering.LineSetObject')
X3DProgrammableShaderObject = autoclass('org.web3d.x3d.sai.Shaders.X3DProgrammableShaderObject')
ShaderProgramObject = autoclass('org.web3d.x3d.java.Shaders.ShaderProgramObject')
X3DComposedGeometryNode = autoclass('org.web3d.x3d.sai.Rendering.X3DComposedGeometryNode')
QuadSetObject = autoclass('org.web3d.x3d.java.CADGeometry.QuadSetObject')
Matrix4VertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.Matrix4VertexAttributeObject')
IMPORTObject = autoclass('org.web3d.x3d.java.Networking.IMPORTObject')
ProtoBodyObject = autoclass('org.web3d.x3d.java.Core.ProtoBodyObject')
PositionDamperObject = autoclass('org.web3d.x3d.java.Followers.PositionDamperObject')
PrimitivePickSensorObject = autoclass('org.web3d.x3d.java.Picking.PrimitivePickSensorObject')
X3DTimeDependentNode = autoclass('org.web3d.x3d.sai.Time.X3DTimeDependentNode')
X3DSoundSourceNode = autoclass('org.web3d.x3d.sai.Sound.X3DSoundSourceNode')
NurbsCurveObject = autoclass('org.web3d.x3d.java.NURBS.NurbsCurveObject')
X3DTouchSensorNode = autoclass('org.web3d.x3d.sai.PointingDeviceSensor.X3DTouchSensorNode')
TransformSensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.TransformSensorObject')
PositionDamper2DObject = autoclass('org.web3d.x3d.java.Followers.PositionDamper2DObject')
headObject = autoclass('org.web3d.x3d.java.Core.headObject')
StaticGroupObject = autoclass('org.web3d.x3d.java.Grouping.StaticGroupObject')
unitObject = autoclass('org.web3d.x3d.java.Core.unitObject')
ProximitySensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.ProximitySensorObject')
ProtoDeclareObject = autoclass('org.web3d.x3d.java.Core.ProtoDeclareObject')
InlineObject = autoclass('org.web3d.x3d.java.Networking.InlineObject')
X3DInterpolatorNode = autoclass('org.web3d.x3d.sai.Interpolation.X3DInterpolatorNode')
CoordinateInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.CoordinateInterpolator2DObject')
X3DKeyDeviceSensorNode = autoclass('org.web3d.x3d.sai.KeyDeviceSensor.X3DKeyDeviceSensorNode')
NormalInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.NormalInterpolatorObject')
X3DPickableObject = autoclass('org.web3d.x3d.sai.Picking.X3DPickableObject')
PickableGroupObject = autoclass('org.web3d.x3d.java.Picking.PickableGroupObject')
X3DShaderNode = autoclass('org.web3d.x3d.sai.Shaders.X3DShaderNode')
PackagedShaderObject = autoclass('org.web3d.x3d.java.Shaders.PackagedShaderObject')
NurbsSwungSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSwungSurfaceObject')
OrthoViewpointObject = autoclass('org.web3d.x3d.java.Navigation.OrthoViewpointObject')
ConeEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.ConeEmitterObject')
ProgramShaderObject = autoclass('org.web3d.x3d.java.Shaders.ProgramShaderObject')
ElevationGridObject = autoclass('org.web3d.x3d.java.Geometry3D.ElevationGridObject')
TexturePropertiesObject = autoclass('org.web3d.x3d.java.Texturing.TexturePropertiesObject')
ParticleSystemObject = autoclass('org.web3d.x3d.java.ParticleSystems.ParticleSystemObject')
X3DLayoutNode = autoclass('org.web3d.x3d.sai.Layout.X3DLayoutNode')
SphereObject = autoclass('org.web3d.x3d.java.Geometry3D.SphereObject')
IndexedFaceSetObject = autoclass('org.web3d.x3d.java.Geometry3D.IndexedFaceSetObject')
ViewpointGroupObject = autoclass('org.web3d.x3d.java.Navigation.ViewpointGroupObject')
EXPORTObject = autoclass('org.web3d.x3d.java.Networking.EXPORTObject')
KeySensorObject = autoclass('org.web3d.x3d.java.KeyDeviceSensor.KeySensorObject')
PositionChaserObject = autoclass('org.web3d.x3d.java.Followers.PositionChaserObject')
GeoTransformObject = autoclass('org.web3d.x3d.java.Geospatial.GeoTransformObject')
GeneratedCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.GeneratedCubeMapTextureObject')
X3DLightNode = autoclass('org.web3d.x3d.sai.Lighting.X3DLightNode')
PointLightObject = autoclass('org.web3d.x3d.java.Lighting.PointLightObject')
HAnimJointObject = autoclass('org.web3d.x3d.java.HAnim.HAnimJointObject')
CollidableShapeObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollidableShapeObject')
SplinePositionInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.SplinePositionInterpolator2DObject')
ComposedShaderObject = autoclass('org.web3d.x3d.java.Shaders.ComposedShaderObject')
ColorInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.ColorInterpolatorObject')
ArcClose2DObject = autoclass('org.web3d.x3d.java.Geometry2D.ArcClose2DObject')
ExplosionEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.ExplosionEmitterObject')
ColorRGBAObject = autoclass('org.web3d.x3d.java.Rendering.ColorRGBAObject')
FillPropertiesObject = autoclass('org.web3d.x3d.java.Shape.FillPropertiesObject')
CollisionCollectionObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionCollectionObject')
ShaderPartObject = autoclass('org.web3d.x3d.java.Shaders.ShaderPartObject')
LayoutGroupObject = autoclass('org.web3d.x3d.java.Layout.LayoutGroupObject')
ReceiverPduObject = autoclass('org.web3d.x3d.java.DIS.ReceiverPduObject')
ColorChaserObject = autoclass('org.web3d.x3d.java.Followers.ColorChaserObject')
ProtoInterfaceObject = autoclass('org.web3d.x3d.java.Core.ProtoInterfaceObject')
ROUTEObject = autoclass('org.web3d.x3d.java.Core.ROUTEObject')
SingleAxisHingeJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.SingleAxisHingeJointObject')
ColorDamperObject = autoclass('org.web3d.x3d.java.Followers.ColorDamperObject')
BillboardObject = autoclass('org.web3d.x3d.java.Navigation.BillboardObject')
ShadedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ShadedVolumeStyleObject')
ScreenGroupObject = autoclass('org.web3d.x3d.java.Layout.ScreenGroupObject')
TriangleFanSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleFanSetObject')
X3DMetadataObject = autoclass('org.web3d.x3d.sai.Core.X3DMetadataObject')
MetadataSetObject = autoclass('org.web3d.x3d.java.Core.MetadataSetObject')
Polypoint2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Polypoint2DObject')
SphereSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.SphereSensorObject')
X3DScriptNode = autoclass('org.web3d.x3d.sai.Scripting.X3DScriptNode')
ScriptObject = autoclass('org.web3d.x3d.java.Scripting.ScriptObject')
connectObject = autoclass('org.web3d.x3d.java.Core.connectObject')
X3DVolumeDataNode = autoclass('org.web3d.x3d.sai.VolumeRendering.X3DVolumeDataNode')
SegmentedVolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.SegmentedVolumeDataObject')
MetadataFloatObject = autoclass('org.web3d.x3d.java.Core.MetadataFloatObject')
LoadSensorObject = autoclass('org.web3d.x3d.java.Networking.LoadSensorObject')
LayoutObject = autoclass('org.web3d.x3d.java.Layout.LayoutObject')
CoordinateDamperObject = autoclass('org.web3d.x3d.java.Followers.CoordinateDamperObject')
PointSetObject = autoclass('org.web3d.x3d.java.Rendering.PointSetObject')
ImageCubeMapTextureObject = autoclass('org.web3d.x3d.java.CubeMapTexturing.ImageCubeMapTextureObject')
OrientationChaserObject = autoclass('org.web3d.x3d.java.Followers.OrientationChaserObject')
CollisionSensorObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionSensorObject')
TriangleStripSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleStripSetObject')
LODObject = autoclass('org.web3d.x3d.java.Navigation.LODObject')
CylinderSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.CylinderSensorObject')
IndexedQuadSetObject = autoclass('org.web3d.x3d.java.CADGeometry.IndexedQuadSetObject')
ViewportObject = autoclass('org.web3d.x3d.java.Layering.ViewportObject')
BallJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.BallJointObject')
DirectionalLightObject = autoclass('org.web3d.x3d.java.Lighting.DirectionalLightObject')
NavigationInfoObject = autoclass('org.web3d.x3d.java.Navigation.NavigationInfoObject')
NurbsPositionInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsPositionInterpolatorObject')
ScalarInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.ScalarInterpolatorObject')
LinePickSensorObject = autoclass('org.web3d.x3d.java.Picking.LinePickSensorObject')
OrientationInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.OrientationInterpolatorObject')
TextureCoordinateObject = autoclass('org.web3d.x3d.java.Texturing.TextureCoordinateObject')
componentObject = autoclass('org.web3d.x3d.java.Core.componentObject')
SilhouetteEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.SilhouetteEnhancementVolumeStyleObject')
MultiTextureTransformObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureTransformObject')
NurbsPatchSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsPatchSurfaceObject')
X3DAppearanceNode = autoclass('org.web3d.x3d.sai.Shape.X3DAppearanceNode')
AppearanceObject = autoclass('org.web3d.x3d.java.Shape.AppearanceObject')
X3DNurbsControlCurveNode = autoclass('org.web3d.x3d.sai.NURBS.X3DNurbsControlCurveNode')
ContourPolyline2DObject = autoclass('org.web3d.x3d.java.NURBS.ContourPolyline2DObject')
SplineScalarInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SplineScalarInterpolatorObject')
X3DInfoNode = autoclass('org.web3d.x3d.sai.Core.X3DInfoNode')
DISEntityTypeMappingObject = autoclass('org.web3d.x3d.java.DIS.DISEntityTypeMappingObject')
TouchSensorObject = autoclass('org.web3d.x3d.java.PointingDeviceSensor.TouchSensorObject')
ClipPlaneObject = autoclass('org.web3d.x3d.java.Rendering.ClipPlaneObject')
GroupObject = autoclass('org.web3d.x3d.java.Grouping.GroupObject')
PositionInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.PositionInterpolatorObject')
ToneMappedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.ToneMappedVolumeStyleObject')
HAnimSiteObject = autoclass('org.web3d.x3d.java.HAnim.HAnimSiteObject')
WorldInfoObject = autoclass('org.web3d.x3d.java.Core.WorldInfoObject')
BoundaryEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.BoundaryEnhancementVolumeStyleObject')
Contour2DObject = autoclass('org.web3d.x3d.java.NURBS.Contour2DObject')
TimeSensorObject = autoclass('org.web3d.x3d.java.Time.TimeSensorObject')
HAnimDisplacerObject = autoclass('org.web3d.x3d.java.HAnim.HAnimDisplacerObject')
Circle2DObject = autoclass('org.web3d.x3d.java.Geometry2D.Circle2DObject')
GeoElevationGridObject = autoclass('org.web3d.x3d.java.Geospatial.GeoElevationGridObject')
NurbsSurfaceInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSurfaceInterpolatorObject')
ShapeObject = autoclass('org.web3d.x3d.java.Shape.ShapeObject')
WindPhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.WindPhysicsModelObject')
AudioClipObject = autoclass('org.web3d.x3d.java.Sound.AudioClipObject')
NurbsTrimmedSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsTrimmedSurfaceObject')
SwitchObject = autoclass('org.web3d.x3d.java.Grouping.SwitchObject')
NurbsSweptSurfaceObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSweptSurfaceObject')
CoordinateInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.CoordinateInterpolatorObject')
StringSensorObject = autoclass('org.web3d.x3d.java.KeyDeviceSensor.StringSensorObject')
MovieTextureObject = autoclass('org.web3d.x3d.java.Texturing.MovieTextureObject')
LayerSetObject = autoclass('org.web3d.x3d.java.Layering.LayerSetObject')
metaObject = autoclass('org.web3d.x3d.java.Core.metaObject')
RigidBodyCollectionObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.RigidBodyCollectionObject')
ScalarDamperObject = autoclass('org.web3d.x3d.java.Followers.ScalarDamperObject')
TriangleSet2DObject = autoclass('org.web3d.x3d.java.Geometry2D.TriangleSet2DObject')
ExternProtoDeclareObject = autoclass('org.web3d.x3d.java.Core.ExternProtoDeclareObject')
Matrix3VertexAttributeObject = autoclass('org.web3d.x3d.java.Shaders.Matrix3VertexAttributeObject')
MetadataIntegerObject = autoclass('org.web3d.x3d.java.Core.MetadataIntegerObject')
GeoMetadataObject = autoclass('org.web3d.x3d.java.Geospatial.GeoMetadataObject')
BlendedVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.BlendedVolumeStyleObject')
ForcePhysicsModelObject = autoclass('org.web3d.x3d.java.ParticleSystems.ForcePhysicsModelObject')
DoubleAxisHingeJointObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.DoubleAxisHingeJointObject')
SignalPduObject = autoclass('org.web3d.x3d.java.DIS.SignalPduObject')
GeoLODObject = autoclass('org.web3d.x3d.java.Geospatial.GeoLODObject')
NurbsCurve2DObject = autoclass('org.web3d.x3d.java.NURBS.NurbsCurve2DObject')
PixelTextureObject = autoclass('org.web3d.x3d.java.Texturing.PixelTextureObject')
VolumeEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.VolumeEmitterObject')
EspduTransformObject = autoclass('org.web3d.x3d.java.DIS.EspduTransformObject')
GeoOriginObject = autoclass('org.web3d.x3d.java.Geospatial.GeoOriginObject')
MetadataBooleanObject = autoclass('org.web3d.x3d.java.Core.MetadataBooleanObject')
IntegerSequencerObject = autoclass('org.web3d.x3d.java.EventUtilities.IntegerSequencerObject')
IsoSurfaceVolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.IsoSurfaceVolumeDataObject')
SceneObject = autoclass('org.web3d.x3d.java.Core.SceneObject')
VisibilitySensorObject = autoclass('org.web3d.x3d.java.EnvironmentalSensor.VisibilitySensorObject')
LinePropertiesObject = autoclass('org.web3d.x3d.java.Shape.LinePropertiesObject')
X3DObject = autoclass('org.web3d.x3d.java.Core.X3DObject')
GeoPositionInterpolatorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoPositionInterpolatorObject')
X3DNBodyCollisionSpaceNode = autoclass('org.web3d.x3d.sai.RigidBodyPhysics.X3DNBodyCollisionSpaceNode')
CollisionSpaceObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.CollisionSpaceObject')
NormalObject = autoclass('org.web3d.x3d.java.Rendering.NormalObject')
ExtrusionObject = autoclass('org.web3d.x3d.java.Geometry3D.ExtrusionObject')
SurfaceEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.SurfaceEmitterObject')
ISObject = autoclass('org.web3d.x3d.java.Core.ISObject')
ConeObject = autoclass('org.web3d.x3d.java.Geometry3D.ConeObject')
PositionInterpolator2DObject = autoclass('org.web3d.x3d.java.Interpolation.PositionInterpolator2DObject')
NurbsTextureCoordinateObject = autoclass('org.web3d.x3d.java.NURBS.NurbsTextureCoordinateObject')
SpotLightObject = autoclass('org.web3d.x3d.java.Lighting.SpotLightObject')
IndexedTriangleStripSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleStripSetObject')
SplinePositionInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SplinePositionInterpolatorObject')
PointEmitterObject = autoclass('org.web3d.x3d.java.ParticleSystems.PointEmitterObject')
CADLayerObject = autoclass('org.web3d.x3d.java.CADGeometry.CADLayerObject')
GeoTouchSensorObject = autoclass('org.web3d.x3d.java.Geospatial.GeoTouchSensorObject')
CollisionObject = autoclass('org.web3d.x3d.java.Navigation.CollisionObject')
IndexedTriangleSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleSetObject')
TriangleSetObject = autoclass('org.web3d.x3d.java.Rendering.TriangleSetObject')
TextureTransformObject = autoclass('org.web3d.x3d.java.Texturing.TextureTransformObject')
ImageTextureObject = autoclass('org.web3d.x3d.java.Texturing.ImageTextureObject')
HAnimHumanoidObject = autoclass('org.web3d.x3d.java.HAnim.HAnimHumanoidObject')
MultiTextureObject = autoclass('org.web3d.x3d.java.Texturing.MultiTextureObject')
NurbsOrientationInterpolatorObject = autoclass('org.web3d.x3d.java.NURBS.NurbsOrientationInterpolatorObject')
MetadataDoubleObject = autoclass('org.web3d.x3d.java.Core.MetadataDoubleObject')
HAnimSegmentObject = autoclass('org.web3d.x3d.java.HAnim.HAnimSegmentObject')
CoordinateChaserObject = autoclass('org.web3d.x3d.java.Followers.CoordinateChaserObject')
SoundObject = autoclass('org.web3d.x3d.java.Sound.SoundObject')
RigidBodyObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.RigidBodyObject')
MetadataStringObject = autoclass('org.web3d.x3d.java.Core.MetadataStringObject')
EdgeEnhancementVolumeStyleObject = autoclass('org.web3d.x3d.java.VolumeRendering.EdgeEnhancementVolumeStyleObject')
CADAssemblyObject = autoclass('org.web3d.x3d.java.CADGeometry.CADAssemblyObject')
TextObject = autoclass('org.web3d.x3d.java.Text.TextObject')
CADPartObject = autoclass('org.web3d.x3d.java.CADGeometry.CADPartObject')
ScalarChaserObject = autoclass('org.web3d.x3d.java.Followers.ScalarChaserObject')
VolumeDataObject = autoclass('org.web3d.x3d.java.VolumeRendering.VolumeDataObject')
SquadOrientationInterpolatorObject = autoclass('org.web3d.x3d.java.Interpolation.SquadOrientationInterpolatorObject')
ContactObject = autoclass('org.web3d.x3d.java.RigidBodyPhysics.ContactObject')
BooleanFilterObject = autoclass('org.web3d.x3d.java.EventUtilities.BooleanFilterObject')
CoordinateDoubleObject = autoclass('org.web3d.x3d.java.NURBS.CoordinateDoubleObject')
GeoLocationObject = autoclass('org.web3d.x3d.java.Geospatial.GeoLocationObject')
VolumePickSensorObject = autoclass('org.web3d.x3d.java.Picking.VolumePickSensorObject')
CoordinateObject = autoclass('org.web3d.x3d.java.Rendering.CoordinateObject')
TransmitterPduObject = autoclass('org.web3d.x3d.java.DIS.TransmitterPduObject')
TextureCoordinate3DObject = autoclass('org.web3d.x3d.java.Texturing3D.TextureCoordinate3DObject')
PixelTexture3DObject = autoclass('org.web3d.x3d.java.Texturing3D.PixelTexture3DObject')
NurbsSetObject = autoclass('org.web3d.x3d.java.NURBS.NurbsSetObject')
IndexedTriangleFanSetObject = autoclass('org.web3d.x3d.java.Rendering.IndexedTriangleFanSetObject')
