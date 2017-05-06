"use strict";

var fs = require('fs');
var mkdirp = require('node-mkdirp');
var mapToMethod = require('./mapToMethod.js');
var mapToMethod2 = require('./mapToMethod2.js');
var jsonlint = require('jsonlint');
var fieldTypes = require('./fieldTypes.js');
var Ajv = require('ajv');

var xmldom = require('xmldom');
var DOMImplementation = new xmldom.DOMImplementation();

var X3DJSONLD = require('./X3DJSONLD.js');
var ConvertToX3DOM = X3DJSONLD.ConvertToX3DOM;

Object.assign(mapToMethod, {
});

for (var map in mapToMethod2) {
	Object.assign(mapToMethod[map], mapToMethod2[map]);
}

var validate = function() { return false; }

function doValidate(json, file, success, failure) {
	var retval = false;
	var version = json.X3D["@version"];
	var error = ""
	if (typeof validate[version] !== 'undefined') {
		var valid = validate[version](json);
		if (!valid) {
			var errs = validate[version].errors;
			for (var e in errs) {
				error += "\r\n keyword: " + errs[e].keyword + "\r\n";
				error += " dataPath: " + errs[e].dataPath + "\r\n";
				error += " message: " + errs[e].message + "\r\n";
				error += " params: " + JSON.stringify(errs[e].params) + "\r\n";
				error += " file: " + file + "\r\n";
				error += " version: " + version + "\r\n";
			}
		}
		retval = valid;
	}
	if (retval && typeof success == 'function') {
		success();
	} else if (typeof failure === 'function') {
		failure(error);
	} else {
		console.error("User selected failure");
	}
}

function loadSchema(json, file, doValidate, success, failure) {
	var versions = { "3.0":true,"3.1":true,"3.2":true,"3.3":true,"3.4":true, "4.0":true }
	var version = json.X3D["@version"];
	if (!versions[version]) {
		console.error("Can only validate version 3.0-4.0 presently. Switching version to 3.3.");
		version = "3.3";
	}
        if (typeof validate[version] === 'undefined') {
		var ajv = new Ajv({ allErrors:true});
		ajv.addFormat("uri", /^(?:[a-z][a-z0-9+\-.]*:)?(?:\/?\/(?:(?:[a-z0-9\-._~!$&'()*+,;=:]|%[0-9a-f]{2})*@)?(?:\[(?:(?:(?:(?:[0-9a-f]{1,4}:){6}|::(?:[0-9a-f]{1,4}:){5}|(?:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){4}|(?:(?:[0-9a-f]{1,4}:){0,1}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){3}|(?:(?:[0-9a-f]{1,4}:){0,2}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){2}|(?:(?:[0-9a-f]{1,4}:){0,3}[0-9a-f]{1,4})?::[0-9a-f]{1,4}:|(?:(?:[0-9a-f]{1,4}:){0,4}[0-9a-f]{1,4})?::)(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?))|(?:(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4})?::[0-9a-f]{1,4}|(?:(?:[0-9a-f]{1,4}:){0,6}[0-9a-f]{1,4})?::)|[Vv][0-9a-f]+\.[a-z0-9\-._~!$&'()*+,;=:]+)\]|(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|(?:[a-z0-9\-._~!$&'()*+,;=]|%[0-9a-f]{2})*)(?::\d*)?(?:\/(?:[a-z0-9\-._~!$&'()*+,;=:@]|%[0-9a-f]{2})*)*|\/(?:(?:[a-z0-9\-._~!$&'()*+,;=:@]|%[0-9a-f]{2})+(?:\/(?:[a-z0-9\-._~!$&'()*+,;=:@]|%[0-9a-f]{2})*)*)?|(?:[a-z0-9\-._~!$&'()*+,;=:@]|%[0-9a-f]{2})+(?:\/(?:[a-z0-9\-._~!$&'()*+,;=:@]|%[0-9a-f]{2})*)*)?(?:\?(?:[a-z0-9\-._~!$&'()*+,;=:@\/?]|%[0-9a-f]{2})*)?(?:\#(?:[a-z0-9\-._~!$&'()*+,;=:@\/?]|%[0-9a-f]{2})*)?$/i);

		
		var metaschema = fs.readFileSync('draft-04-JSONSchema.json');
		var metaschemajson = JSON.parse(metaschema.toString());
		ajv.addMetaSchema(metaschemajson);
		var schema = fs.readFileSync("x3d-"+version+"-JSONSchema.json");
		var schemajson = JSON.parse(schema.toString());
		ajv.addSchema(schemajson);
		console.log("Schema", version, "added");
		validate[version] = ajv.compile(schemajson);
		if (typeof validate[version] === 'undefined') {
			console.error("Schema", version, "not compiled");
		}
		doValidate(json, file, success, failure);
	} else {
		doValidate(json, file, success, failure);
	}
}

function convertJSON(options) {

	var files = process.argv;
	for (var f in files) {
		var file = files[f];
		if (file.match(/node_modules|package.json|JSONSchema/)) {
			continue;
		}
		var basefile = file.substr(0, file.lastIndexOf("."));
		var file = basefile+".json";
		var str = fs.readFileSync(file).toString();
		if (typeof str === 'undefined') {
			throw("Read nothing, or possbile error");
		}
		var json = null;
		try {  
			json = JSON.parse(str);
		} catch (e) {
			console.error("================================================================================");
			console.error("File:", file);
			console.error("Error:", e);
			continue;
		}
		var xml = [];
		var NS = "http://www.web3d.org/specifications/x3d";
		loadX3DJS(json, file, xml, NS, loadSchema, doValidate, function(element) {
			if (typeof element === undefined) {
				throw ("Undefined element returned from loadX3DJS()")
			}
			if (typeof element === null) {
				throw ("Null element returned from loadX3DJS()")
			}
			// filename conversion goes here.
			basefile = basefile.replace(/^[cC]:\/x3d-code\//g, "")
			basefile = basefile.replace(/-|\.| /g, "_")
			// handle filenames with leading zeros and java keywords
			basefile = basefile.replace(/^(.*[\\\/])([0-9].*|default|switch|for)$/, "$1_$2")
			mkdirp(basefile.substr(0, basefile.lastIndexOf("/")));

			var outfile = basefile+".json";
			fs.writeFileSync(outfile, str);
			for (var ser in options) {
				var serializer = require(ser);
				str = new serializer().serializeToString(json, element, basefile, mapToMethod, fieldTypes)
				if (typeof str !== 'undefined') {
					var outfile = basefile+options[ser];
					fs.writeFileSync(outfile, str);
				} else {
					throw("Wrote nothing, serializer returned nothing");
				}
			}
		});
	}
}


/**
 * json -- JavaScript JSON object
 * path -- used for determining subURLs
 * xml -- unused, see X3DJSONLD.js version
 * NS -- ununsed, see X3DJSONLD.js version
 * loadSchema -- to load JSON schema
 * doValidate -- function to validate JSON
 * callback -- function which receives return element
 */

function loadX3DJS(json, path, xml, NS, loadSchema, doValidate, callback) {
	if (typeof json === 'undefined') {
		console.error('json undefined.  Look in', path, 'for hints');
	}
	var version = json.X3D["@version"];
	var docType = DOMImplementation.createDocumentType("X3D", 'ISO//Web3D//DTD X3D '+version+'//EN" "http://www.web3d.org/specifications/x3d-'+version+'.dtd', null);
	var document = DOMImplementation.createDocument(null, "X3D", docType);
	// Bring in JSON to DOM/XML conversion --  used to build DOM/XML.
	X3DJSONLD.setDocument(document);
	X3DJSONLD.setCDATACreateFunction(function(document, element, str) {
		// for script nodes
		/*
		var child = document.createCDATASection(str);
		*/
		var y = str
			.replace(/'([^'\r]*)\n([^']*)'/g, "'$1\\n$2'")
			.replace(/&lt;/g, "<")
			.replace(/&gt;/g, ">")
			.replace(/&amp;/g, "&")
		;
		var child = document.createCDATASection(y);
		if (str !== y) {
			// console.log("CDATA Replacing",str,"with",y);
		}
		element.appendChild(child);
	});

	document.insertBefore(document.createProcessingInstruction('xml', 'version="1.0" encoding="'+json.X3D["encoding"]+'"'), document.doctype);
	var element = document.getElementsByTagNameNS(null, "X3D")[0];
	element.setAttribute("xmlns:xsd", 'http://www.w3.org/2001/XMLSchema-instance');

	// TODO Probably shouldn't call convert before we validate
	ConvertToX3DOM(json, "", element, path);

	loadSchema(json, path, doValidate, function() {
		callback(element);
	}, function(e) {
		console.error("Failed ", path, e);
		callback(element); // TODO should not return element, but we are overriding
	});
}

if (typeof module === 'object')  {
	module.exports = {
		loadX3DJS: loadX3DJS,
		convertJSON: convertJSON,
		loadSchema: loadSchema,
		doValidate: doValidate
	};
}
