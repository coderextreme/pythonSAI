"use strict";

var mapToMethod = require('./mapToMethod.js');
var mapToMethod2 = require('./mapToMethod2.js');

console.log("FOO", mapToMethod2);
for (var par in mapToMethod2) {
	console.log(par);
	for (var child in mapToMethod2[par]) {
		console.log("\t", child);
		mapToMethod[par][child] = mapToMethod2[par][child];
		console.log("\t", "\t", mapToMethod[par][child]);
	}
}
