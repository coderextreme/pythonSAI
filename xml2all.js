"use strict";

// Convert X3D JSON to various formats

process.argv.shift();
process.argv.shift();

var convertXML = require('./convertXML.js');

convertXML([
	{ 
	serializer : './PythonPipeliningSerializer.js',
	folder : "./future/",
	extension : ".future.py",
	},
	{ 
	serializer : './PythonSerializer.js',
	folder : "./",
	extension : ".py",
	}
	]);
