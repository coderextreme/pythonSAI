"use strict";

// Convert X3D JSON to various formats

process.argv.shift();
process.argv.shift();

var convertJSON = require('./convertJSON.js').convertJSON;

convertJSON([
	{ 
	serializer : './PythonPipeliningSerializer.js',
	folder : "./",
	extension : ".future.py",
	codeOutput : "./future/",
	},
	{ 
	serializer : './PythonSerializer.js',
	folder : "./",
	extension : ".py",
	codeOutput : "./",
	}
	]);
