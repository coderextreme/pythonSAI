const Ajv2020 = require("ajv/dist/2020");
const addFormats = require("ajv-formats-draft2019");
var ajv = new Ajv2020({allErrors:true, verbose:true});
addFormats(ajv, {mode: "full", formats: ["uri-reference", "uri", "iri-reference", "iri"], keywords: true});  // fast mode is "fast"

var X3DJSONLD = require('./X3DJSONLD.js');
X3DJSONLD = Object.assign(X3DJSONLD, { processURLs : function(urls) { return urls; }});
var selectObjectFromJSObj = X3DJSONLD.selectObjectFromJSObj;
var validate = { };

function doValidate(json, validated_version, file, X3DJSONLD, success, failure, e) {
	var retval = false;
	if (e) {
		if (typeof alert === 'function') {
			alert(e);
		}
		console.error(e);
	}
	var version = "4.0";
	if (typeof json.X3D !== 'undefined') {
		version = json.X3D["@version"];
	}
	if (typeof validated_version !== 'undefined') {
		var valid = validated_version(json);
		if (!valid) {
			var errs = validated_version.errors;
			if (typeof localize === 'function') {
				localize(validated_version.errors);
			}
			var error = "";
			for (var e in errs) {
				error += "\n keyword: " + errs[e].keyword + "\n";
				var dataPath = errs[e].dataPath.replace(/^\./, "").replace(/[\.\[\]']+/g, " > ").replace(/ >[ \t]*$/, "");
	
				error += " dataPath: " + dataPath+ "\n";
				var selectedObject = X3DJSONLD.selectObjectFromJSObj(json, dataPath);
				error += " value: " + JSON.stringify(selectedObject,
					function(k, v) {
					    var v2 = JSON.parse(JSON.stringify(v));
					    if (typeof v2 === 'object') {
						    for (var o in v2) {
					    		if (typeof v2[o] === 'object') {
								    v2[o] = "|omitted|";
							}
					            }
					    }
					    return v2;
					}) + "\n";
				error += " message: " + errs[e].message + "\n";
				error += " params: " + JSON.stringify(errs[e].params) + "\n";
				error += " file: " + file + "\n";
			}
		}
		if (typeof confirm !== 'function') {
			confirm = function(error) {
				return true;
			};
		}

		retval = (valid || confirm(error));
	}
	if (retval && typeof success == 'function') {
		success();
	} else if (typeof failure === 'function') {
		failure(e);
	} else {
		console.error("User selected failure");
	}
}

function addSchema(ajv, schemajson, version) {
      ajv.addSchema(schemajson);
      var validated_version = ajv.compile(schemajson);
      validate[version] = validated_version;
      if (typeof validated_version === 'undefined') {
	      console.error("Schema not compiled");
      }
      return validated_version;
}

function loadSchema(json, file, doValidate, X3DJSONLD, success, failure) {
	var versions = { "3.0":true,"3.1":true,"3.2":true,"3.3":true,"4.0":true }
	var version = "4.0";
	if (typeof json.X3D !== 'undefined') {
		version = json.X3D["@version"];
	}
	if (!versions[version]) {
		console.error("Can only validate version 3.0-4.0 presently. Switching version to 4.0.");
		version = "4.0";
	}
	var validated_version = validate[version];
        if (typeof validated_version === 'undefined') {
		      if (typeof $ === 'function' && typeof $.getJSON === 'function') {
			      $.getJSON("./x3d-"+version+"-JSONSchema.json", function(schemajson) {
				      validated_version = addSchema(ajv, schemajson, version);
				      doValidate(json, validated_version, file, X3DJSONLD, success, undefined);
				}).fail(function(e) {
				   doValidate(json, validated_version, file, X3DJSONLD, undefined, failure, e);
				});
		      } else if (typeof fs === 'object') {
				var schema = fs.readFileSync("./x3d-"+version+"-JSONSchema.json");
				var schemajson = JSON.parse(schema.toString());
				validated_version = addSchema(ajv, schemajson, version);
				doValidate(json, validated_version, file, X3DJSONLD, success, undefined);
		      }
	} else {
	      doValidate(json, validated_version, file, X3DJSONLD, success, undefined);
	}
}
/**
 * Load X3D JSON into an element.
 * DOMImplementation - normally document.implementation
 * jsobj - the JavaScript object to convert to XML and DOM.
 * path - the path of the JSON file.
 * NS - a namespace for X_ITE (optional) -- stripped out.
 * loadSchema -- the loadSchema function
 * doValidate -- the doValidate function
 * X3DJSONLD -- X3DJSONLD
 * callback -- returns the element whose scene children to append or insert into the DOM.
 */
function loadX3DJS(DOMImplementation, jsobj, path, NS, loadSchema, doValidate, X3DJSONLD, callback) {
	X3DJSONLD.x3djsonNS = NS;
	loadSchema(jsobj, path, doValidate, X3DJSONLD, function() {
		var child, xml;
		[ child, xml ] = X3DJSONLD.loadJsonIntoXml(DOMImplementation, jsobj, path);
		callback(child, xml);
	}, function(e) {
		console.error(e);
		callback(null, null);
	});
}

/*
 * replaceX3DJSON
 * replace children of an element with DOM created from X3D JSON.
 *	also, generate xml for inclusion elsewhere
 *
 * parent -- parent DOM element
 * json (json object) -- json to convert to DOM
 * url -- name of path/filename json loaded from
 * NS -- XML namespace (optional)
 * next -- to return the element or null
 * returns element loaded, followed by xml
 */
function replaceX3DJSON(parent, json, url, NS, next) {

	loadX3DJS(DOMImplementation, json, url, NS, loadSchema, doValidate, X3DJSONLD, function(child, xml) {
		if (child != null) {
			while (parent.firstChild) {
			    parent.removeChild(parent.firstChild);
			}
			parent.appendChild(child);
		}
		next(child, xml);
	});
}

if (typeof module === 'object')  {
	module.exports = {
		replaceX3DJSON: replaceX3DJSON,
		loadSchema: loadSchema,
		loadX3DJS: loadX3DJS,
		doValidate: doValidate
	};
}
