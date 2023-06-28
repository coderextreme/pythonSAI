"use strict";

const DOUBLE_SUFFIX = '';
const FLOAT_SUFFIX = '';

let fs = require("fs");

function PythonSerializer () {
this.code = [];
this.codeno = 0;
this.preno = 0;
}


PythonSerializer.prototype = {
	serializeToString : function(json, element, clazz, mapToMethod, fieldTypes) {
		this.code = [];
		this.codeno = 0;
		this.preno = 0;
		let stack = [];

		let str = "";
		// str += "# -*- coding: "+json.X3D.encoding+" -*-\n";

		// str += "print('<?xml version=\"1.0\" encoding=\"UTF-8\"?>')\n";
		str += "print('<!--')\n";
		str += "import x3d\n";
		str += "print('-->')\n";

		stack.unshift(this.preno);
		this.preno++;
		let bodystr = "";
        
        // https://stackoverflow.com/questions/48469666/error-enoent-no-such-file-or-directory-open-moviedata-json
        // https://stackoverflow.com/questions/3151436/how-can-i-get-the-current-directory-name-in-javascript
        // console.log('Current directory: ' + process.cwd()); // Node.js method for current directory - not what is needed here
        // https://flaviocopes.com/node-get-current-folder/ use __dirname under Node.js
		bodystr += ""+element.nodeName+stack[0]+" = x3d."+element.nodeName;
		bodystr += "()\n";
		bodystr += this.subSerializeToString(element, mapToMethod, fieldTypes, 3, stack);

		str += bodystr;
		str += "f = open(\""+clazz+"_RoundTrip.x3d\", \"w\")\n";
		str += "f.write("+element.nodeName+stack[0]+".XML())\n";
		str += "f.close()\n";
		stack.shift();
		return str;
	},

	printSubArray : function (attrType, type, values, co, j, lead, trail) {
                if (type === "int") {
                        for (let v in values) {
				if (values[v] > 0x7fffffff) {
				    values[v] = values[v] - 4294967296
				}

				/*
                                if (values[v] > 4200000000) {
                                        values[v] = "0x"+parseInt(values[v]).toString(16).toUpperCase();
                                }
				*/
                        }
                }
                if (type === "boolean") {
                        for (let v in values) {
				if (values[v] === 'true') {
					values[v] = "True";
				} else if (values[v] === 'false') {
					values[v] = "False";
				}
			}
		}
		if (values[0] === "" || values[0] === null) {
			values.shift();
		}
		if (values.length >= 0 && (values[values.length-1] === "" || values[values.length-1] === null)) {
			values.pop();
		}
		if (attrType === "MFRotation") {
			return '('+lead+values.map(a => parseFloat(a).toFixed(4)).join(j)+trail+')';
		} else if (attrType === "MFVec3f") {
			return '('+lead+values.map(a => parseFloat(a).toFixed(4)).join(j)+trail+')';
		// } else if (attrType === "SFString") {
			// let s =  '('+lead+values.join(',')+trail+')';
			// return s;
		} else {
			return '['+lead+values.join(j)+trail+']';
		}
	},

	printParentChild : function (element, node, cn, mapToMethod, n) {
		let prepre = ".";
		let addpre = "";
		if (cn > 0 && node.nodeName !== 'IS') {
			addpre = "";
		}
		if (node.nodeName === 'field') {
			addpre = "";
		}

		let method = node.nodeName;
		if (typeof mapToMethod[element.nodeName] === 'object') {
			if (typeof mapToMethod[element.nodeName][node.nodeName] === 'string') {
				addpre = "";
				method = mapToMethod[element.nodeName][node.nodeName];
			}
		} else if (typeof mapToMethod[element.nodeName] === 'string') {
			addpre = "";
			method = mapToMethod[element.nodeName];
		}
		for (let a in node.attributes) {
			let attrs = node.attributes;
			try {
				parseInt(a);
				let attrsa = attrs[a];
				let attr = attrsa.nodeName;
				if (attrs.hasOwnProperty(a) && attrsa.nodeType == 2) {
					if (attr === "containerField") {
						method = attrsa;
						if (method === "Shaders") {
							addpre = "";
							method = "child";
						} else {
							if (attrs[a].nodeValue == "joints" 
								|| attrs[a].nodeValue == "sites" 
								|| attrs[a].nodeValue == "segments" 
							) {
								method = ""+attrs[a];
							} else {
								method = ""+attrs[a];
							}
							addpre = "";
						}
					}
				}
			} catch (e) {
			}
		}
		if (element.nodeName === 'Scene' && addpre+method === "setMetadata") {
			method = "metadata"
			addpre = "";
		}
		if (node.nodeName === 'LayerSet' && addpre+method === "addChild") {
			method = "layerSet"
			addpre = "";
		}
		if (method === "setShaders") {
			method = "shaders"
			addpre = "";
		}
		return prepre+addpre+method;
	},
	stringValue : function(attrsa, attr, attrType, element, attrs) {
		let strval;
		let nodeValue = attrsa.nodeValue;
	retype:
		if (nodeValue === 'NULL') {
			strval = "";
			return strval;
		}
		if (attrType === "SFString") {
			if (attr === "value") {
				for (let a in attrs) {
					if (attrs[a].nodeName === "type") {
						attrType = attrs[a].nodeValue;
						break;
					}
				}
			}
		}
		if (attrType === "SFString") {
			if (attr === "accessType") {
				strval = '"'+nodeValue+'"';
			} else {
				strval = '"'+nodeValue.
					replace(/\\n/g, '\\\\n').
					replace(/\\?"/g, "\\\"")
					+'"';
			}
		} else if (attrType === "SFInt32") {
			strval = nodeValue;
		} else if (attrType === "SFFloat") {
			strval = nodeValue+FLOAT_SUFFIX;
		} else if (attrType === "SFDouble") {
			strval = nodeValue+DOUBLE_SUFFIX;
		} else if (attrType === "SFBool") {
			if (nodeValue === 'true') {
				strval = "True";
			} else if (nodeValue === 'false') {
				strval = "False";
			} else {
				strval = nodeValue;
			}
		} else if (attrType === "SFTime") {
			strval = nodeValue+DOUBLE_SUFFIX;
		} else if (attrType === "MFTime") {
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
		} else if (attrType === "MFString") {
			nodeValue = nodeValue.replace(/^ *(.*) *$/, "$1");
			strval = this.printSubArray(attrType, "java.lang.String",
				nodeValue.substr(1, nodeValue.length-2).split(/"[ ,\t\r\n]+"/).
				map(function(x) {
					let y = x.
					       replace(/(\\\\+)/g, '$1$1').
					       replace(/\\\\"/g, '\\\"').
					       replace(/""/g, '\\"\\"').
					       replace(/&quot;&quot;/g, '\\"\\"').
					       // replace(/&/g, "&amp;").
					       replace(/\\n/g, '\\n');
					if (y !== x) {
					}
					return y;
				}), this.codeno, '","', '"', '"');
		} else if (
			attrType === "MFInt32"||
			attrType === "MFImage"||
			attrType === "SFImage") {
			strval = this.printSubArray(attrType, "int", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, ',', '', '');
		} else if (
			attrType === "SFColor"||
			attrType === "MFColor"||
			attrType === "SFColorRGBA"||
			attrType === "MFColorRGBA"||
			attrType === "SFVec2f"||
			attrType === "SFVec3f"||
			attrType === "SFVec4f"||
			attrType === "MFVec2f"||
			attrType === "MFVec3f"||
			attrType === "MFVec4f"||
			attrType === "SFMatrix3f"||
			attrType === "SFMatrix4f"||
			attrType === "MFMatrix3f"||
			attrType === "MFMatrix4f"||
			attrType === "SFRotation"||
			attrType === "MFRotation"||
			attrType === "MFFloat") {
			strval = this.printSubArray(attrType, "float", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, FLOAT_SUFFIX+',', '', FLOAT_SUFFIX);
		} else if (
			attrType === "SFVec2d"||
			attrType === "SFVec3d"||
			attrType === "SFVec4d"||
			attrType === "MFVec2d"||
			attrType === "MFVec3d"||
			attrType === "MFVec4d"||
			attrType === "SFMatrix3d"||
			attrType === "SFMatrix4d"||
			attrType === "MFMatrix3d"||
			attrType === "MFMatrix4d"||
			attrType === "MFDouble") {
			strval = this.printSubArray(attrType, "double", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, DOUBLE_SUFFIX+',', '', DOUBLE_SUFFIX);
		} else if (attrType === "MFBool") {
			strval = this.printSubArray(attrType, "boolean", nodeValue.split(/[ ,\t\r\n]+/), this.codeno, ',', '', '');
		} else {
			strval = '"'+nodeValue.replace(/\n/g, '\\\\n').replace(/\\?"/g, "\\\"")+'"';
		}
		return strval;
	},
	subSerializeToString : function(element, mapToMethod, fieldTypes, n, stack) {
		let str = "";
		let attrType = "";
		for (let a in element.attributes) {
			let attrs = element.attributes;
			try {
				parseInt(a);
				let attrsa = attrs[a];
				if (attrs.hasOwnProperty(a) && attrsa.nodeType == 2) {
					let attr = attrsa.nodeName;
					if (attr === "xmlns:xsd") {
						continue;
					} else if (attr === "xsd:noNamespaceSchemaLocation" ) {
						continue;
					} else if (attr === 'containerField') {
						continue;
					} else if (attr === "id") {
						continue;
					} else if (element.nodeName === "Sphere" && attr === "subdivision") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "showStat") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "showLog") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "width") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "height") {
						continue;
					} else if (element.nodeName === "X3D" && attr === "backend") {
						continue;
					} else if (element.nodeName === "Background" && attr === "groundTransparency") {
						continue;
					} else if (element.nodeName === "Background" && attr === "skyTransparency") {
						continue;
					}
					attrType = "SFString";
					if (typeof fieldTypes[element.nodeName] !== 'undefined') {
						attrType = fieldTypes[element.nodeName][attr];
					}
					let strval = this.stringValue(attrsa, attr, attrType, element, attrs);
					let method = attr;
					if (attr === "class") {
						method = "cssClass";
					}
					str += element.nodeName+stack[0];
					str += '.'+method+" = "+strval+"\n";
				}
			} catch (e) {
			}
			attrType = "";
		}
		for (let cn in element.childNodes) {
			let node = element.childNodes[cn];
			if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 1) {
				stack.unshift(this.preno);
				this.preno++;
				let ch = "";
				if (node.nodeName === "#sourceCode") {
					ch += node.nodeName.substring(1)+stack[0]+" = ";
					ch += node.nodeValue;
				} else {
					ch += node.nodeName+stack[0]+" = x3d."+node.nodeName;
					ch += "()\n";
				}

				let bodystr = this.subSerializeToString(node, mapToMethod, fieldTypes, n+1, stack);
				ch += bodystr;
				ch += "\n"
				let method = this.printParentChild(element, node, cn, mapToMethod, n);
				if (method === ".addMeta" || method === ".addComponent"|| method === ".addUnit") {
					method = ".children";
				} else if (method === ".setIS") {
					method = ".IS";
				} else if (method.indexOf(". containerField") === 0) {
					method = "."+method.substring(method.indexOf('"')+1, method.lastIndexOf('"'));
				} else if (method === ".setScene" ||
					method === ".setProtoInterface" ||
					method === ".setProtoBody") {
					method = method.substring(0,1) + method.substring(4);
				} else if (method === ".#sourceCode") {
					method = method.substring(0,1) + method.substring(2);
				} else {
					method = method.substring(0,1) + method.substring(4,5).toLowerCase() + method.substr(5);

				}
				if (method === ".Scene" ||
					method === ".IS" ||
					method === ".appearance" ||
					method === ".texture" ||
					method === ".fontStyle" ||
					method === ".material" ||
					method === ".geometry" ||
					method === ".head" ||
					method === ".proxy" ||
					method === ".ProtoInterface" ||
					method === ".ProtoBody") {
					ch += element.nodeName+stack[1]+method+" = "+node.nodeName+stack[0]+"\n";
				} else if (method === ".sourceCode") {
					ch += element.nodeName+stack[1]+method+" = "+node.nodeName.substring(1)+stack[0]+"\n";
				} else {
					ch += element.nodeName+stack[1]+method+".append("+node.nodeName+stack[0]+")\n";
				}
				str += ch;
				stack.shift();
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 8) {
				let y = node.nodeValue.
					replace(/\\/g, '\\\\').
					replace(/"/g, '\\"');
				// str += ".addComments(CommentsBlock(\"\"\""+y+"\"\"\")) \\\n";
				str += y.split("\r\n").map(function(x) {
					return x.replace(/^/g, '#');
					}).join("\r\n");
				str += "\r\n";
				if (y !== node.nodeValue) {
				}
			} else if (element.childNodes.hasOwnProperty(cn) && node.nodeType == 4) {
				str += "\n"+element.nodeName+stack[0];
				str += ".sourceCode = '''"+node.nodeValue.split(/\r?\n/).map(function(x) {
					return x.
					        replace(/\\/g, '\\\\').
						replace(/"/g, '\\"')
						replace(/$/g, '\\')
						/*
						.replace(/\\n/g, "\\\\n")
						*/
					;
					}).join('\\n\"+\n\"')+"'''\n";
			}
	        		
		}
		return str;
	}
};


if (typeof module === 'object')  {
	module.exports = PythonSerializer;
}

