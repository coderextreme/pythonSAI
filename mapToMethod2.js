var mapToMethod2 = {
	"Shape" : {
		"ProtoInstance": "setGeometry"
	},
	"HAnimJoint" : {
		"Transform" : "addChild"
	},
	"Appearance" : {
		"ProtoInstance" : "setMaterial",
		"ProgramShader" : "addShaders"
	},
	"ComposedShader" : {
		"field" : "addField"
	},
	"Script" : {
		"field" : "addField",
		"IS" : "setIS"
	},
	"MetadataSet" : {
		"ProtoInstance" : "setMetadata"
	},
	"ProtoInstance" : {
		"IS" : "setIS"
	},
	"X3DGroupingNode" : {
		"IS" : "setIS"
	},
	"CADAssembly" : {
		"IS" : "setIS"
	},
	"Billboard" : {
		"IS" : "setIS"
	},
	"GeoLocation" : {
		"IS" : "setIS"
	},
	"X3DViewportNode" : {
		"IS" : "setIS"
	},
	"LayoutLayer" : {
		"IS" : "setIS"
	},
	"LOD" : {
		"IS" : "setIS"
	},
	"Disk2D" : {
		"IS" : "setIS"
	},
	"Anchor" : {
		"IS" : "setIS"
	},
	"Group" : {
		"IS" : "setIS"
	},
	"RigidBody" : {
		"CollidableShape" : "addGeometry"
	},
	"Viewport" : {
		"IS" : "setIS"
	},
	"GeoTransform" : {
		"IS" : "setIS"
	},
	"ScreenGroup" : {
		"IS" : "setIS"
	},
	"EspduTransform" : {
		"IS" : "setIS"
	},
	"PickableGroup" : {
		"IS" : "setIS"
	},
	"HAnimHumanoid" : {
		"IS" : "addSkin",
		"HAnimJoint" : "addJoints",
		"HAnimSegment" : "addSegments",
		"HAnimSite": "addViewpoints",
		"Group" : "addSkeleton"
	},
	"X3DPickSensorNode" : {
		"IS" : "addPickedGeometry"
	},
	"VolumePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"Layer" : {
		"IS" : "setIS"
	},
	"StaticGroup" : {
		"IS" : "setIS"
	},
	"PointPickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"LayoutGroup" : {
		"IS" : "setIS"
	},
	"HAnimSite" : {
		"IS" : "setIS"
	},
	"field" : {
		"IS" : "setIS"
	},
	"Transform" : {
		"IS" : "setIS"
	},
	"ProtoBody" : {
		"IS" : "setIS",
		"ProgramShader" : "addChild"
	},
	"Collision" : {
		"IS" : "setIS",
		"Transform" : "addChild",
		"Group" : "addChild"
	},
	"PrimitivePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"CADLayer" : {
		"IS" : "setIS"
	},
	"fieldValue" : {
		"IS" : "setIS"
	},
	"GeoLOD" : {
		"IS" : "setIS",
		"GeoOrigin" : "setGeoOrigin"
	},
	"LinePickSensor" : {
		"IS" : "addPickedGeometry"
	},
	"GeoMetadata" : {
		"IS" : "addData"
	},
	"Switch" : {
		"IS" : "setIS"
	},
	"HAnimSegment" : {
		"IS" : "setIS"
	},
	"Scene" : {
		"IS" : "setIS",
		"LayerSet" : "addLayerSet",
		"MetadataString" : "addMetadata"
	}
};

module.exports = mapToMethod2;
