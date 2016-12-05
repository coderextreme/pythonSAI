<?xml version="1.0" encoding="UTF-8"?>
<!--
    title       : CreateX3dSceneAccessInterfaceJava.xslt
    created     :  6 June 2016
    creator     : Don Brutzman
    description : Create open-source X3D Scene Access Interface (SAI) library in Java
    reference   : build.xml target BuildSceneAuthoringInterfacesJava.saxon
    reference   : AllX3dElementsAttributes.xml
    reference   : AllX3dElementsAttributesTextTemplate.xslt
    reference   : http://www.w3.org/TR/xslt
    identifier  : http://www.web3d.org/x3d/stylesheets/AllX3dElementsAttributesTextTemplate.xslt
    license     : license.html
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0"
                xmlns:xs ="http://www.w3.org/2001/XMLSchema" extension-element-prefixes="xs"
	            xmlns:fn ="http://www.w3.org/2005/xpath-functions">
	
    <xsl:output method="html" encoding="UTF8" cdata-section-elements="javadocBlock interfaceBlock implementationBlock"/> <!-- output methods:  xml html text -->
    
	<xsl:variable name="debug"><xsl:text>false</xsl:text></xsl:variable>
	
	<xsl:variable name="saiPackage"               >                <xsl:text>org.web3d.x3d.sai</xsl:text></xsl:variable>
	<xsl:variable name="saiPackageDirectorySource">       <xsl:text>java/src/org/web3d/x3d/sai</xsl:text></xsl:variable>
	<xsl:variable name="saiPackageDirectoryBuild" >     <xsl:text>java/build/org/web3d/x3d/sai</xsl:text></xsl:variable>
	<!-- TODO restructure concrete hierarchy -->
	<xsl:variable name="concreteSubpackageName"   >                              <xsl:text>java</xsl:text></xsl:variable>
	<xsl:variable name="concretePackage"          >                <xsl:text>org.web3d.x3d.java</xsl:text></xsl:variable>
	<xsl:variable name="concretePackageDirectorySource">  <xsl:text>java/src/org/web3d/x3d/java</xsl:text></xsl:variable>
	<xsl:variable name="concretePackageDirectoryBuild" ><xsl:text>java/build/org/web3d/x3d/java</xsl:text></xsl:variable>
	<xsl:variable name="jsaiClassSuffix"    ><xsl:text>Object</xsl:text></xsl:variable>
	<xsl:variable name="jsaiInterfaceSuffix"><xsl:text>Interface</xsl:text></xsl:variable>

	<xsl:variable name="saiJavaSpecificationRootUrl"><xsl:text>http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2</xsl:text></xsl:variable>
	<xsl:variable name="saiAbstractSpecificationRootUrl"><xsl:text>http://www.web3d.org/documents/specifications/19775-2/V3.3/Part02</xsl:text></xsl:variable>
	<xsl:variable name="x3dAbstractSpecificationRootUrl"><xsl:text>http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01</xsl:text></xsl:variable>
	
	<xsl:variable name="newValue"><xsl:text>newValue</xsl:text></xsl:variable><!-- default parameter name -->
	<xsl:variable name="x3d.tooltips.path">
		<xsl:text>../tooltips/x3d-3.3.profile.xml</xsl:text>
	</xsl:variable>
	<xsl:variable name="x3d.tooltips.document" select="doc($x3d.tooltips.path)"/>
	
	<xsl:variable name="modifySpecificationInterfaces"><xsl:text>false</xsl:text></xsl:variable> 
	<!-- false: match original Java SAI design with many root-level classes and interfaces -->
	<!--  true: experimental, match good design practice by inserting relevant subpackages -->

    <!-- ======================================================= -->
    
    <xsl:template match="/"> <!-- process root of input document -->
	
		<!-- process fixed files -->
		<xsl:call-template name="FieldDefinitions"/>
		<xsl:call-template name="BaseTypeDefinitions"/>
		
		<xsl:call-template name="ServiceInterfaces"/>
		<xsl:call-template name="StatementInterfaces"/>
		<xsl:call-template name="ExceptionDefinitions"/>
		<xsl:call-template name="NodeTypeDefinitions"/>
		<xsl:call-template name="ObjectTypeDefinitions"/>
		<xsl:call-template name="NodeInterfacesDefinitions"/>
		
		<!-- instantiable Plain Old Java Object (POJO) classes -->
		<xsl:call-template name="ConcreteNodeObjectDefinitions"/>
        
        <!-- process elements and comments -->
        <xsl:apply-templates select="X3DObjectModel/* | comment()"/>
        
    </xsl:template>

    <!-- ===================================================== -->
    
    <xsl:template match="*"> <!-- rule to process each element -->
        
        <!-- common initial processing for each element -->
        <xsl:text disable-output-escaping="yes">&lt;</xsl:text>
        <xsl:value-of select="local-name()"/>
        
        <xsl:apply-templates select="@*"/> <!-- process attributes for this element -->
        
        <!-- <xsl:apply-templates select="*"/> no need to recurse on child elements -->
        
        <!-- common final processing for each element -->
        <xsl:text disable-output-escaping="yes">/&gt;</xsl:text><!-- end element -->
        <xsl:text>&#10;</xsl:text>
        
    </xsl:template>

    <!-- ===================================================== -->
    
    <xsl:template match="@*"> <!-- rule to process each attribute -->
        
        <!-- common processing for each attribute -->
        <xsl:text> </xsl:text>
        <xsl:value-of select="local-name()"/>
        <xsl:text>='</xsl:text>
        <xsl:value-of select="."/>
        <xsl:text>'</xsl:text>
        
    </xsl:template>

    <!-- ===================================================== -->
    
    <xsl:template match="comment()"> <!-- rule to process each comment -->
    
        <xsl:text disable-output-escaping="yes">&lt;!--</xsl:text>
        <xsl:value-of select="."/>
        <xsl:text disable-output-escaping="yes">--&gt;</xsl:text>
        <xsl:text>&#10;</xsl:text>
        
    </xsl:template>

    <!-- ===================================================== -->
	
	<xsl:variable name="licenseBlock">
		<!-- inserted in each autogenerated source file -->
		<xsl:text>/*</xsl:text><xsl:text>&#10;</xsl:text>
			<xsl:variable name="license.filename"><xsl:text>license.txt</xsl:text></xsl:variable>
			<xsl:value-of select="unparsed-text($license.filename)"/>
		<xsl:text>*/</xsl:text><xsl:text>&#10;</xsl:text>
		<xsl:text>&#10;</xsl:text>
	</xsl:variable>
    <!-- ===================================================== -->
    
    <xsl:template name="isX3dStatement">
		<xsl:param name="name"/>
		<!-- note that ROUTE, *Proto* and CommentsBlock are X3D Statements which are also allowed as X3DChildNode -->
		<xsl:value-of select="
			($name = 'connect') or ($name = 'field') or ($name = 'fieldValue') or ($name = 'IS') or ($name = 'ROUTE') or 
			($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare') or ($name = 'ProtoInstance') or ($name = 'ProtoInterface') or ($name = 'ProtoBody') or 
			($name = 'X3D') or ($name = 'head') or ($name = 'component') or ($name = 'meta') or ($name = 'unit') or ($name = 'Scene') or 
            ($name = 'IMPORT') or ($name = 'EXPORT') or ($name = 'CommentsBlock')"/>
	</xsl:template>

	<!-- ===================================================== -->
    
    <xsl:template name="javaType">
		<xsl:param name="x3dType"/>
		<xsl:param name="isInterface"/>
		<xsl:variable name="baseType" select="//SimpleType[@name = $x3dType]/@baseType"/>
		
		<xsl:choose>
			<xsl:when test="( $x3dType = 'SFString') or ( $x3dType = 'xs:string') or ( $x3dType = 'xs:token') or
                            ($baseType = 'SFString') or ($baseType = 'xs:string') or ($baseType = 'xs:token')">
				<xsl:text>String</xsl:text>
			</xsl:when>
			<xsl:when test="(($x3dType = 'MFString') or ($baseType = 'MFString')) and ($isInterface = 'true')">
				<xsl:text>String[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFString') or ($baseType = 'MFString')">
				<xsl:text disable-output-escaping="yes">ArrayList&lt;String&gt;</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'SFBool') or ($baseType = 'SFBool')">
				<xsl:text>boolean</xsl:text>
			</xsl:when>
			<xsl:when test="(($x3dType = 'MFBool') or ($baseType = 'MFBool')) and ($isInterface = 'true')">
				<xsl:text>boolean[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFBool') or ($baseType = 'MFBool')">
				<xsl:text disable-output-escaping="yes">ArrayList&lt;Boolean&gt;</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'SFInt32') or ($baseType = 'SFInt32')">
				<xsl:text>int</xsl:text>
			</xsl:when>
			<xsl:when test="(( $x3dType = 'MFInt32') or  ($x3dType = 'SFImage') or  ($x3dType = 'MFImage') or
                             ($baseType = 'MFInt32') or ($baseType = 'SFImage') or ($baseType = 'MFImage')) and ($isInterface = 'true')">
				<xsl:text>int[]</xsl:text>
			</xsl:when>
			<xsl:when test="( $x3dType = 'MFInt32') or  ($x3dType = 'SFImage') or  ($x3dType = 'MFImage') or
                            ($baseType = 'MFInt32') or ($baseType = 'SFImage') or ($baseType = 'MFImage')">
				<xsl:text>ArrayList&lt;Integer&gt;</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'SFFloat') or ($baseType = 'SFFloat')">
				<xsl:text>float</xsl:text>
			</xsl:when>
			<xsl:when test="(($x3dType = 'MFFloat') or ($baseType = 'MFFloat')) and ($isInterface = 'true')">
				<xsl:text>float[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFFloat') or ($baseType = 'MFFloat')">
				<xsl:text disable-output-escaping="yes">ArrayList&lt;Float&gt;</xsl:text>
			</xsl:when>
			<xsl:when test="contains( $x3dType,'FVec2f') or contains( $x3dType,'FVec3f') or (@baseType='boundingBoxSizeType') or contains( $x3dType,'FVec4f') or contains( $x3dType,'FRotation') or contains( $x3dType,'FColor') or
                            contains($baseType,'FVec2f') or contains($baseType,'FVec3f') or ($baseType='boundingBoxSizeType') or contains($baseType,'FVec4f') or contains($baseType,'FRotation') or contains($baseType,'FColor')">
				<xsl:text>float[]</xsl:text>
			</xsl:when>
			<xsl:when test="( $x3dType = 'SFMatrix3f') or ( $x3dType = 'MFMatrix3f') or ( $x3dType = 'SFMatrix4f') or ($ x3dType = 'MFMatrix4f') or
                            ($baseType = 'SFMatrix3f') or ($baseType = 'MFMatrix3f') or ($baseType = 'SFMatrix4f') or ($baseType = 'MFMatrix4f')">
				<xsl:text>float[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'SFDouble') or ($x3dType = 'SFTime') or ($baseType = 'SFDouble') or ($baseType = 'SFTime')">
				<xsl:text>double</xsl:text>
			</xsl:when>
			<xsl:when test="(($x3dType = 'MFDouble') or ($x3dType = 'MFTime') or ($baseType = 'MFDouble') or ($baseType = 'MFTime')) and ($isInterface = 'true')">
				<xsl:text>double[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFDouble') or ($x3dType = 'MFTime') or ($baseType = 'MFDouble') or ($baseType = 'MFTime')">
				<xsl:text disable-output-escaping="yes">ArrayList&lt;Double&gt;</xsl:text>
			</xsl:when>
			<xsl:when test="contains( $x3dType,'FVec2d') or contains( $x3dType,'FVec3d') or contains( $x3dType,'FVec4d') or
                            contains($baseType,'FVec2d') or contains($baseType,'FVec3d') or contains($baseType,'FVec4d')">
				<xsl:text>double[]</xsl:text>
			</xsl:when>
			<xsl:when test="( $x3dType = 'SFMatrix3d') or ( $x3dType = 'MFMatrix3d') or ( $x3dType = 'SFMatrix4d') or ( $x3dType = 'MFMatrix4d') or
                            ($baseType = 'SFMatrix3d') or ($baseType = 'MFMatrix3d') or ($baseType = 'SFMatrix4d') or ($baseType = 'MFMatrix4d')">
				<xsl:text>double[]</xsl:text>
			</xsl:when>
			<!-- X3D Java Specification interface definitions are completely ambiguous, there is no benefit to 
                 including unnecessarily loose node typing accessors for a single node.  Omitted this general/harmful case.
			<xsl:when test="($x3dType = 'SFNode') and ($isInterface = 'true')">
				<xsl:text>X3DNode</xsl:text>
			</xsl:when> -->
			<xsl:when test="($x3dType = 'SFNode')">
				<xsl:choose>
					<xsl:when test="(string-length(@acceptableNodeTypes) > 0) and not(contains(@acceptableNodeTypes,'|'))">
						<!-- not always singular, example CADFace shape field (Shape|LOD|Transform) -->
						<xsl:value-of select="@acceptableNodeTypes"/>
						<xsl:variable name="isX3dStatement">
							<xsl:call-template name="isX3dStatement">
								<xsl:with-param name="name" select="@name"/>
							</xsl:call-template>
						</xsl:variable>
						<xsl:if test="($isX3dStatement = 'true')">
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
						</xsl:if>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>X3DNode</xsl:text><!-- TODO more precise node-type checks -->
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFNode') and ($isInterface = 'true')">
				<xsl:text>X3DNode[]</xsl:text>
			</xsl:when>
			<xsl:when test="($x3dType = 'MFNode')">
				<xsl:choose>
					<xsl:when test="(string-length(@acceptableNodeTypes) > 0) and not(contains(@acceptableNodeTypes,'|'))">
						<!-- not always singular, example CADFace shape field (Shape|LOD|Transform) -->
						<xsl:text disable-output-escaping="yes">ArrayList&lt;</xsl:text><!-- ArrayList<> -->
						<xsl:value-of select="@acceptableNodeTypes"/>
						<xsl:variable name="isX3dStatement">
							<xsl:call-template name="isX3dStatement">
								<xsl:with-param name="name" select="@name"/>
							</xsl:call-template>
						</xsl:variable>
						<xsl:if test="($isX3dStatement = 'true')">
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
						</xsl:if>
						<!--
						<xsl:if test="not($isInterface = 'true') and not($isX3dStatement = 'true')">
							<xsl:value-of select="$jsaiInterfaceSuffix"/>
						</xsl:if>
						--><!-- append to type name -->
						<xsl:text disable-output-escaping="yes">&gt;</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text disable-output-escaping="yes">ArrayList&lt;X3DNode&gt;</xsl:text><!-- TODO more precise node-type checks -->
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="(string-length($x3dType) = 0)">
				<xsl:text> (error: Java type not provided) </xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<xsl:text> (error: Java type not found for </xsl:text>
				<xsl:value-of select="$x3dType"/>
				<xsl:text>) </xsl:text>
			</xsl:otherwise>
		</xsl:choose>
    </xsl:template>

    <!-- ===================================================== -->
    
    <xsl:template name="javaValue">
		<xsl:param name="x3dType"/>
		<xsl:param name="schemaValue"/>
		<xsl:param name="javadoc"><xsl:text>false</xsl:text></xsl:param>
				
		<xsl:variable name="xmlValue">
			<xsl:choose>
				<xsl:when test="($schemaValue='[]')">
				</xsl:when>
				<xsl:when test="starts-with($schemaValue,'[') and ends-with($schemaValue,']')">
					<xsl:value-of select="substring($schemaValue,2,(string-length($schemaValue)-2))"/>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$schemaValue"/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
		<xsl:choose>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFString')">
				<xsl:text>"</xsl:text>
				<!-- enumeration value: escape each quote character as \" -->
				<xsl:call-template name="escape-quotes-recurse">
					<xsl:with-param name="inputString" select="$xmlValue"/>
				</xsl:call-template>
				<xsl:text>"</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'EscapeQuotedSFString')">
				<xsl:text>"</xsl:text>
				<!-- enumeration value: escape each quote character as \" -->
				<xsl:call-template name="escape-quotes-recurse">
					<xsl:with-param name="inputString" select="concat('&quot;',$xmlValue,'&quot;')"/>
				</xsl:call-template>
				<xsl:text>"</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'MFString')">
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;(Arrays.asList(</xsl:text><!-- ArrayList<> -->
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>new String[] {</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
				<!-- avoid empty string when actual value is empty list -->
				<xsl:if test="(string-length(normalize-space($xmlValue)) > 0)">
					<xsl:text>"</xsl:text>
					<!-- enumeration value: escape each quote character as \" -->
					<xsl:call-template name="escape-quotes-recurse">
						<xsl:with-param name="inputString" select="translate($xmlValue,' ',',')"/>
					</xsl:call-template>
					<xsl:text>"</xsl:text>
				</xsl:if>
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text>))</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>}</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFBool')">
				<xsl:value-of select="$xmlValue"/>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'MFBool') or ($x3dType = 'MFInt32') or ($x3dType = 'SFImage') or ($x3dType = 'MFImage')">
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;(Arrays.asList(</xsl:text><!-- ArrayList<> -->
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>{</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:value-of select="translate($xmlValue,' ',',')"/>
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text>))</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>}</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFInt32')">
				<xsl:value-of select="$xmlValue"/>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFFloat')">
				<!-- Java float constants have 'f' appended, e.g. 1.0f -->
				<xsl:call-template name="append-f-to-float-values-recurse">
					<xsl:with-param name="inputString" select="normalize-space($xmlValue)"/>
				</xsl:call-template>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFDouble') or ($x3dType = 'SFTime')">
				<xsl:value-of select="$xmlValue"/>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'MFFloat') or ($x3dType = 'MFDouble') or ($x3dType = 'MFTime')">
				<!-- Java float constants have 'f' appended, e.g. 1.0f -->
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;(Arrays.asList(</xsl:text><!-- ArrayList<> -->
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>{</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="($x3dType = 'MFFloat')">
						<xsl:call-template name="append-f-to-float-values-recurse">
							<xsl:with-param name="inputString" select="normalize-space($xmlValue)"/>
						</xsl:call-template>
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name="append-zero-to-double-values-recurse">
							<xsl:with-param name="inputString" select="normalize-space($xmlValue)"/>
						</xsl:call-template>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:choose>
					<xsl:when test="($javadoc='false')">
						<xsl:text>))</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>}</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			 <!-- ========================================
			<xsl:when test="($x3dType = 'MFDouble') or ($x3dType = 'MFTime')">
				<xsl:text>{</xsl:text>
				<xsl:value-of select="translate($xmlValue,' ',',')"/>
				<xsl:text>}</xsl:text>
			</xsl:when> -->
			 <!-- ======================================== -->
			<xsl:when test="contains($x3dType,'FVec2f') or contains($x3dType,'FVec3f') or contains($x3dType,'FVec4f') or contains($x3dType,'FRotation') or contains($x3dType,'FColor')">
				<xsl:text>{</xsl:text>
				<!-- Java float constants have 'f' appended, e.g. 1.0f -->
				<xsl:call-template name="append-f-to-float-values-recurse">
					<xsl:with-param name="inputString" select="normalize-space($xmlValue)"/>
				</xsl:call-template>
				<xsl:text>}</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFMatrix3f') or ($x3dType = 'MFMatrix3f') or ($x3dType = 'SFMatrix4f') or ($x3dType = 'MFMatrix4f')">
				<xsl:text>{</xsl:text>
				<!-- Java float constants have 'f' appended, e.g. 1.0f -->
				<xsl:call-template name="append-f-to-float-values-recurse">
					<xsl:with-param name="inputString" select="normalize-space($xmlValue)"/>
				</xsl:call-template>
				<xsl:text>}</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="contains($x3dType,'FVec2d') or contains($x3dType,'FVec3d') or contains($x3dType,'FVec4d')">
				<xsl:text>{</xsl:text>
				<xsl:value-of select="translate($xmlValue,' ',',')"/>
				<xsl:text>}</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:when test="($x3dType = 'SFMatrix3d') or ($x3dType = 'MFMatrix3d') or ($x3dType = 'SFMatrix4d') or ($x3dType = 'MFMatrix4d')">
				<xsl:text>{</xsl:text>
				<xsl:value-of select="translate($xmlValue,' ',',')"/>
				<xsl:text>}</xsl:text>
			</xsl:when>
			 <!-- ======================================== -->
			<xsl:otherwise>
				<!-- default: treat as simple String -->
				<xsl:text>"</xsl:text>
				<xsl:value-of select="$xmlValue"/>
				<xsl:text>"</xsl:text>
			</xsl:otherwise>
		</xsl:choose>
    </xsl:template>

    <!-- ===================================================== -->
    
    <xsl:template name="tupleSize">
		<xsl:param name="x3dType"/>
		
		<xsl:choose>
			<xsl:when test="contains($x3dType,'FBool')   or contains($x3dType,'FInt32')  or contains($x3dType,'FFloat') or 
                            contains($x3dType,'FDouble') or contains($x3dType,'FString') or contains($x3dType,'FTime') or 
                            contains($x3dType,'FNode')">
				<xsl:text>1</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FVec2')">
				<xsl:text>2</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FVec3') or contains($x3dType,'FColor') or (@baseType='boundingBoxSizeType')">
				<xsl:text>3</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FVec4') or contains($x3dType,'Rotation')">
				<xsl:text>4</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FMatrix3')">
				<xsl:text>9</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FMatrix4')">
				<xsl:text>16</xsl:text>
			</xsl:when>
			<xsl:when test="contains($x3dType,'FImage')">
				<!-- irregular tuple size -->
				<xsl:text>0</xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<!-- report problem -->
				<xsl:message>
					<xsl:text>*** tupleSize not computed for type=</xsl:text>
					<xsl:value-of select="$x3dType"/>
				</xsl:message>
				<xsl:text>0</xsl:text>
			</xsl:otherwise>
		</xsl:choose>
				
    </xsl:template>

    <!-- ===================================================== -->
	
	<!-- template to create interface or class source file -->
	<xsl:template name="sourceFile">
		<xsl:param name="name"><xsl:text>..missing name..</xsl:text></xsl:param>
		<xsl:param name="imports"/>
		<xsl:param name="inConcretePackage"><xsl:text>false</xsl:text></xsl:param>
		<xsl:param name="visibility"><xsl:text>public</xsl:text></xsl:param>
		<xsl:param name="isAbstract"/>
		<xsl:param name="isInterface"/>
		<xsl:param name="extends"/>
		<xsl:param name="implements"/>
		<xsl:param name="subPackage"/>
		<xsl:param name="description"/>
		<xsl:param name="saiJavaSpecificationSection"/>
		<xsl:param name="saiJavaSpecificationRelativeUrl"/>
		<xsl:param name="saiAbstractSpecificationSection"/>
		<xsl:param name="saiAbstractSpecificationRelativeUrl"/>
		<xsl:param name="x3dAbstractSpecificationSection"/>
		<xsl:param name="x3dAbstractSpecificationRelativeUrl"/>
		<!-- How to Write Doc Comments for the Javadoc Tool http://www.oracle.com/technetwork/articles/java/index-137868.html -->
		<xsl:param name=       "javadocBlock"/> <!-- typically has additional javadoc for each member -->
		<xsl:param name=     "interfaceBlock"/> <!-- top-level insertion for interface signatures -->
		<xsl:param name="implementationBlock"/> <!-- top-level insertion for class implementations -->
			
		<!-- Determine if current source is an Exception, Field or service type defined by X3D SAI specification -->
		<xsl:variable   name="isException"
					  select="starts-with($saiJavaSpecificationSection,'B.7') or ends-with($name,'Exception')"/>
		<xsl:variable   name="isFieldInterface"   
					  select="starts-with($saiJavaSpecificationSection,'B.4')"/>
		<xsl:variable   name="isServiceInterface"
					  select="starts-with($saiJavaSpecificationSection,'B.5')"/>
		<xsl:variable   name="hasField"
					  select="(count(//InterfaceDefinition/field) > 0)"/>
		<xsl:variable   name="hasJavadocBlock"
					  select="(string-length(normalize-space($javadocBlock)) > 0)"/>
		<xsl:variable   name="hasInterfaceBlock"
					  select="(string-length(normalize-space($interfaceBlock)) > 0)"/>
		<xsl:variable   name="hasImplementationBlock"
					  select="(string-length(normalize-space($implementationBlock)) > 0)"/>
		<xsl:variable name="baseType" select="//ConcreteNode[@name=$name]/InterfaceDefinition/Inheritance/@baseType"/>
		<xsl:variable name="additionalInheritanceBaseType" select="//ConcreteNode[@name=$name]/InterfaceDefinition/AdditionalInheritance/@baseType"/>
		
		<!-- Determine if current source uses an Exception, Field or service type defined by X3D SAI specification -->
		<!-- B.4 Field interfaces -->
		<xsl:variable   name="hasFieldInterface"   
					  select="(   ($isInterface = 'true') and
							   (contains($interfaceBlock,'SF')     or
								contains($interfaceBlock,'MF')     or
								contains($interfaceBlock,'Matrix'))) or
							  (not($isInterface = 'true') and
							   (contains($implementationBlock,'SF')     or
								contains($implementationBlock,'MF')     or
								contains($implementationBlock,'Matrix'))) or
							  InterfaceDefinition/field[starts-with(@type,'SF')] or
							  InterfaceDefinition/field[starts-with(@type,'MF')] or
							  InterfaceDefinition/field[contains(@type,'Matrix')]"/>
		<!-- B.5 Service interfaces -->
		<xsl:variable   name="hasServiceInterface" 
					  select="(   ($isInterface = 'true') and
							   (contains($interfaceBlock,'BrowserEvent')    or
								contains($interfaceBlock,'BrowserFactory')  or
								contains($interfaceBlock,'X3DComponent')    or
								contains($interfaceBlock,'ExternalBrowser') or
								contains($interfaceBlock,'BrowserListener'))) or
							  (not($isInterface = 'true') and
							   (contains($implementationBlock,'BrowserEvent')    or
								contains($implementationBlock,'BrowserFactory')  or
								contains($implementationBlock,'X3DComponent')    or
								contains($implementationBlock,'ExternalBrowser') or
								contains($implementationBlock,'BrowserListener'))) or
							  InterfaceDefinition/field[starts-with(@type,'BrowserEvent')]    or
							  InterfaceDefinition/field[starts-with(@type,'BrowserFactory')]  or
							  InterfaceDefinition/field[starts-with(@type,'X3DComponent')]    or
							  InterfaceDefinition/field[starts-with(@type,'ExternalBrowser')] or
							  InterfaceDefinition/field[starts-with(@type,'BrowserListener')]"/>
		<!-- B.7 Exception definitions -->
		<xsl:variable   name="hasException"
					  select="(contains($interfaceBlock,'Exception') or contains($implementationBlock,'Exception'))"/>
		
		<xsl:variable name="thisClassName">
			<xsl:value-of select="$name"/>
			<xsl:if test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
						  not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not(starts-with($name,'X3DConcrete'))">
				<xsl:value-of select="$jsaiClassSuffix"/>
			</xsl:if>
		</xsl:variable>
		<xsl:variable name="sourceFilePath">
			<xsl:choose>
				<xsl:when test="($inConcretePackage = 'true')">
					<xsl:value-of select="$concretePackageDirectorySource"/>
				</xsl:when>
				<xsl:when test="($isInterface = 'true') or ($isException or $isServiceInterface) or ($name = 'X3DFieldEvent')">
					<xsl:value-of select="$saiPackageDirectorySource"/>
				</xsl:when>
				<xsl:otherwise><!-- concretes -->
					<xsl:value-of select="$concretePackageDirectorySource"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:choose>
				<xsl:when test="not($isInterface = 'true') and ($isFieldInterface) and not($name = 'X3DFieldEvent')">
					<xsl:text>/</xsl:text>
					<xsl:text>fields</xsl:text>
				</xsl:when>
				<xsl:when test="(string-length($subPackage) > 0)">
					<xsl:text>/</xsl:text>
					<xsl:value-of select="translate($subPackage,'-','')"/><!-- no componentName hypens allowed (e.g. H-Anim) -->
				</xsl:when>
			</xsl:choose>
			<xsl:text>/</xsl:text>
			<xsl:value-of select="$thisClassName"/>
			<xsl:text>.java</xsl:text>
		</xsl:variable>
		<xsl:variable name="canThrowFieldValueException"
                    select="(string-length(@minExclusive) > 0) or (string-length(@maxExclusive) > 0) or
                            (string-length(@minInclusive) > 0) or (string-length(@maxInclusive) > 0)"/>
		
		<xsl:variable name="isClassX3dStatement">
			<xsl:call-template name="isX3dStatement">
				<xsl:with-param name="name" select="$name"/>
			</xsl:call-template>
		</xsl:variable>
		
		<xsl:variable name="hasChildrenField" select="string((count(InterfaceDefinition/field[@name = 'children']) > 0)
														and not($name = 'CADPart'))"/>
<!-- debug 
<xsl:message>
	<xsl:text>*** sourceFile/$name=</xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:text>, $hasChildrenField=</xsl:text>
	<xsl:value-of select="$hasChildrenField"/>
	<xsl:text>, $isInterface=</xsl:text>
	<xsl:value-of select="$isInterface"/>
</xsl:message>
-->	
		<!-- create source file -->
		<xsl:result-document href="{$sourceFilePath}" method="html" omit-xml-declaration="yes" encoding="UTF8" indent="yes">
			<xsl:value-of select="$licenseBlock"/>
			
			<xsl:text>package </xsl:text>
			<xsl:choose>
				<xsl:when test="($inConcretePackage = 'true')">
					<xsl:value-of select="$concretePackage"/>
				</xsl:when>
				<xsl:when test="($isInterface = 'true') or ($isException or $isServiceInterface) or ($name = 'X3DFieldEvent')">
					<xsl:value-of select="$saiPackage"/>
				</xsl:when>
				<xsl:otherwise><!-- concretes -->
					<xsl:value-of select="$concretePackage"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:if test="string-length($subPackage) > 0">
				<xsl:text>.</xsl:text>
				<xsl:value-of select="translate($subPackage,'/-','.')"/><!-- trailing slash to dot., no componentName hypens allowed (e.g. H-Anim) -->
			</xsl:if>
			<xsl:text>;</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>&#10;</xsl:text>
			
			<xsl:if test="string-length(normalize-space($imports)) > 0">
				<xsl:value-of select="$imports" disable-output-escaping="yes"/> <!-- top-level insertion for class or interface -->
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<!-- imports for built-in types -->
			<xsl:if test="(not($isInterface = 'true') or //field[@type='MFNode']) and not(starts-with($name,'SF')) and not(starts-with($name,'MF')) and 
							  not(starts-with($thisClassName, 'X3DConcrete'))">
				<xsl:text>import java.util.*;</xsl:text>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:if test="true()"><!-- ($isInterface = 'true') -->
				<xsl:choose>
					<xsl:when test="($modifySpecificationInterfaces = 'true')">
						<xsl:if test="$hasFieldInterface">
							<xsl:text>import org.web3d.x3d.sai.fields.*;</xsl:text>
							<xsl:text>&#10;</xsl:text>
						</xsl:if>
						<xsl:if test="$hasException or $canThrowFieldValueException">
							<xsl:text>import org.web3d.x3d.sai.exceptions.*;</xsl:text>
							<xsl:text>&#10;</xsl:text>
						</xsl:if>
						<xsl:if test="$hasServiceInterface">
							<xsl:text>import org.web3d.x3d.sai.services.*;</xsl:text>
							<xsl:text>&#10;</xsl:text>
						</xsl:if>
					</xsl:when>
					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="contains($name,'FNode')">
								<xsl:text>import org.web3d.x3d.sai.Core.*;  // making sure</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:if test="($inConcretePackage = 'true')">
									<xsl:text>import org.web3d.x3d.java.*; // again making sure #1</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
							</xsl:when>
							<xsl:when test="(($hasFieldInterface or $hasException or $hasServiceInterface or $canThrowFieldValueException) and (string-length($subPackage) > 0))
											 and not(starts-with($name,'SF')) and not(starts-with($name,'MF'))">
								<!-- TODO stronger filtering many be needed to avoid superfluous declaration -->
								<xsl:text>import org.web3d.x3d.sai.*;  // making sure</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:if test="($inConcretePackage = 'true')">
									<xsl:text>import org.web3d.x3d.java.*; // again making sure #2</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
							</xsl:when>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:if test="not($isInterface = 'true')">
					<xsl:if test="($name = 'X3D')">
						<!-- X3D imports -->
						<xsl:text>
import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.*;
</xsl:text>
					</xsl:if>
					<xsl:text>import org.web3d.x3d.sai.Core.*;  // making sure</xsl:text>
					<xsl:text>&#10;</xsl:text>
					<xsl:if test="($inConcretePackage = 'true')">
						<xsl:text>
import org.web3d.x3d.java.*; // again making sure #3
import org.web3d.x3d.java.Core.*;
</xsl:text>
						<xsl:text>&#10;</xsl:text>
					</xsl:if>
				</xsl:if>
				<xsl:if test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and 
							  not(starts-with($thisClassName, 'X3DConcrete'))">
					<xsl:text>import org.web3d.x3d.java.fields.*; // making sure</xsl:text>
					<xsl:text>&#10;</xsl:text>
					<xsl:choose>
						<xsl:when test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram') or ($name = 'ProtoInterface')">
							<xsl:text>import org.web3d.x3d.java.Core.fieldObject;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						</xsl:when>
						<xsl:when test="($name = 'ProtoInstance')">
							<xsl:text>import org.web3d.x3d.java.Core.fieldValueObject;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						</xsl:when>
					</xsl:choose>
				</xsl:if>
			
				<!-- generalized
				<xsl:variable   name="hasCoreComponentType"   
							  select="contains($interfaceBlock,'Metadata')             or contains($implementationBlock,'Metadata')             or
									  contains($interfaceBlock,'ProtoInstance')        or contains($implementationBlock,'ProtoInstance')        or
									  contains($interfaceBlock,'WorldInfo')            or contains($implementationBlock,'WorldInfo')            or
									  contains($interfaceBlock,'X3DBindableNode')      or contains($implementationBlock,'X3DBindableNode')      or
									  contains($interfaceBlock,'X3DChildNode')         or contains($implementationBlock,'X3DChildNode')         or
									  contains($interfaceBlock,'X3DInfoNode')          or contains($implementationBlock,'X3DInfoNode')          or
									  contains($interfaceBlock,'X3DNode')              or contains($implementationBlock,'X3DNode')              or
									  contains($interfaceBlock,'X3DPrototypeInstance') or contains($implementationBlock,'X3DPrototypeInstance') or
									  contains($interfaceBlock,'X3DSensorNode')        or contains($implementationBlock,'X3DSensorNode')        or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'Metadata')]  or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'ProtoInstance')]  or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'WorldInfo')]  or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DBindableNode')]      or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DChildNode')]         or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DInfoNode')]          or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DNode')]              or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DPrototypeInstance')] or
									  InterfaceDefinition/field[contains(@acceptableNodeTypes, 'X3DSensorNode')]"/>
				<xsl:if test="($hasCoreComponentType) and ($subPackage != 'Core')">
					<xsl:text>import org.web3d.x3d.sai.Core.*;</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
				-->

				<!-- loop over fields to find further imports -->
				<!-- TODO filter out duplicates -->
				<xsl:for-each select="InterfaceDefinition/field[not(starts-with(@name,'set'))][string-length(@acceptableNodeTypes) > 0]">

					<xsl:variable name="fieldName" select="@name"/><!-- avoid duplicates -->
					<xsl:if test="not(preceding-sibling::*[@name = $fieldName])">
						<xsl:variable name="acceptableType"          select="@acceptableNodeTypes"/>
						<xsl:variable name="acceptableTypeComponent" select="//*[@name = $acceptableType]/InterfaceDefinition/componentInfo/@name"/>
						<xsl:if test="(string-length($acceptableType) > 0)">
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
	<xsl:text>*** field/@name=</xsl:text>
	<xsl:value-of select="@name"/>
	<xsl:text>, $acceptableType=</xsl:text>
	<xsl:value-of select="$acceptableType"/>
	<xsl:text>, $acceptableTypeComponent=</xsl:text>
	<xsl:value-of select="$acceptableTypeComponent"/>
</xsl:message>
</xsl:if>
							<!-- TODO make this filter more restrictive to eliminate redundant imports, perhaps by using tokenize -->
							<xsl:if test="(string-length($acceptableTypeComponent) > 0) and
                                          (count(preceding-sibling::*[contains(//*[@name = @acceptableNodeTypes]//componentInfo/@name, $acceptableTypeComponent)]) = 0)">
								<xsl:choose>
									<xsl:when test="($isInterface = 'true') and not($inConcretePackage = 'true')">
										<xsl:text>import org.web3d.x3d.sai.</xsl:text>
										<xsl:if test="not($acceptableTypeComponent = 'fields') or ($modifySpecificationInterfaces = 'true')">
											<xsl:value-of select="translate($acceptableTypeComponent,'-','')"/>
											<xsl:text>.</xsl:text>
										</xsl:if>
										<xsl:text>*;</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>import org.web3d.x3d.sai.</xsl:text>
										<xsl:value-of select="translate($acceptableTypeComponent,'-','')"/>
										<xsl:text>.*;</xsl:text>
										<xsl:text>
import org.web3d.x3d.java.*; // again making sure #4
</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>import org.web3d.x3d.java.</xsl:text>
										<xsl:value-of select="translate($acceptableTypeComponent,'-','')"/>
										<xsl:text>.*;</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:if>
						</xsl:if>
					</xsl:if>
				</xsl:for-each>
				
				<!-- special imports -->
				<xsl:if test="InterfaceDefinition/field[(@type = 'MFNode') and (((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove')))]">
					<xsl:text>import java.util.Arrays;</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
				
				<xsl:if test="($name = 'ROUTE')">
					<xsl:text>import org.web3d.x3d.java.Scripting.*; // for ROUTEObject</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
			</xsl:if>
			
			<!-- no need to include current package in imports -->
			<!-- convention: avoid adding import calls for fully qualified class references -->
			<!-- TODO confirm handling of more than one comma-separated import -->
			<!--
			<xsl:if test="(string-length($extends) > 0) and contains($extends,'.')">
				<xsl:text>import </xsl:text>
				<xsl:value-of select="$extends"/>
				<xsl:text>;</xsl:text>
				<xsl:text>&#10;</xsl:text><xsl:text>&#10;</xsl:text>
			</xsl:if>
			-->
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
	<xsl:text>*** field/@name=</xsl:text>
	<xsl:value-of select="@name"/>
	<xsl:text>, $description=</xsl:text>
	<xsl:value-of select="$description"/>
	<xsl:text>, $javadocBlock=</xsl:text>
	<xsl:value-of select="$javadocBlock"/>
</xsl:message>
</xsl:if>
			<!-- start class/interface javadoc -->
			<xsl:text>&#10;</xsl:text>
			<xsl:text>/**</xsl:text><xsl:text>&#10;</xsl:text>
			<xsl:choose>
				<xsl:when test="string-length(normalize-space($description)) > 0">
					<xsl:text> * </xsl:text><xsl:value-of select="normalize-space($description)"/>
					<xsl:text>&#10;</xsl:text>
					<xsl:text> * </xsl:text><xsl:text>&#10;</xsl:text>
					<xsl:text> * </xsl:text>
					<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
					<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
					<xsl:text>&#10;</xsl:text>
				</xsl:when>
				<xsl:when test="($isInterface = 'true') and not($inConcretePackage = 'true')">
					<xsl:text> * Abstract node interface, defined by X3D specification to support X3D Java interoperability.</xsl:text>
					<xsl:text>&#10;</xsl:text>
					<xsl:text> * </xsl:text><xsl:text>&#10;</xsl:text>
					<xsl:text> * </xsl:text>
					<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
					<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
					<xsl:text>&#10;</xsl:text>
				</xsl:when>
				<xsl:when test="($isException)">
					<!-- exception description is provided by each exception -->
				</xsl:when>
				<xsl:when test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface)">
					<!-- node description is provided by first sentence of tooltip -->
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>
						<xsl:text> *** </xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:text> has no description...</xsl:text>
					</xsl:message>
				</xsl:otherwise>
			</xsl:choose>
			
			<xsl:if test="string-length(normalize-space($javadocBlock)) > 0">
				<xsl:text> * </xsl:text><xsl:value-of select="normalize-space($javadocBlock)" disable-output-escaping="yes"/><xsl:text>&#10;</xsl:text> <!-- top-level insertion for interface or class -->
				<xsl:text> * </xsl:text><xsl:text>&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:variable name="isX3dStatement">
				<xsl:call-template name="isX3dStatement">
					<xsl:with-param name="name" select="@name"/>
				</xsl:call-template>
			</xsl:variable>
			
			<xsl:if test="doc-available($x3d.tooltips.path)">
				<xsl:variable name="tooltipText" select="replace($x3d.tooltips.document//element[@name = $name]/@tooltip,'&#8734;','infinity')"/>
				
				<xsl:variable name="containsHintWarning" select="contains($tooltipText,'Hint:') or contains($tooltipText,'Warning:')"/>
				<xsl:if test="(string-length($tooltipText) > 0)">
					<xsl:text> * </xsl:text>
					<xsl:text disable-output-escaping="yes">&lt;i&gt;X3D </xsl:text>
					<xsl:choose>
						<xsl:when test="($isX3dStatement = 'true')">
							<xsl:text>statement</xsl:text>
						</xsl:when>
						<xsl:otherwise>
							<xsl:text>node</xsl:text>
						</xsl:otherwise>
					</xsl:choose>
					<xsl:text disable-output-escaping="yes"> tooltip&lt;/i&gt;: </xsl:text>
					<xsl:choose>
						<xsl:when test="$containsHintWarning">
							<xsl:variable name="preambleHint"    select="normalize-space(substring-before($tooltipText,'Hint:'))"/>
							<xsl:variable name="preambleWarning" select="normalize-space(substring-before($tooltipText,'Warning:'))"/>
							<xsl:choose>
								<xsl:when test="(string-length($preambleHint) > 0) and 
												 ((string-length($preambleWarning) = 0) or (string-length($preambleWarning) > string-length($preambleHint)))">
									<xsl:call-template name="hyperlink">
										<xsl:with-param name="string">
											<xsl:value-of select="$preambleHint"/>
										</xsl:with-param>
									</xsl:call-template>
									<xsl:text>&#10;</xsl:text>
									<xsl:text> * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;ul&gt;</xsl:text>
									<xsl:call-template name="insert-javadoc-line-breaks-recurse">
										<xsl:with-param name="inputString"><xsl:value-of select="substring-after(normalize-space($tooltipText),$preambleHint)"/></xsl:with-param>
										<xsl:with-param name="breakText1"><xsl:text>Hint:</xsl:text></xsl:with-param>
										<xsl:with-param name="breakText2"><xsl:text>Warning:</xsl:text></xsl:with-param>
									</xsl:call-template>
									<xsl:text>&#10;</xsl:text>
									<xsl:text> * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/ul&gt;</xsl:text>
								</xsl:when>
								<xsl:otherwise>
									<xsl:call-template name="hyperlink">
										<xsl:with-param name="string">
											<xsl:value-of select="$preambleWarning"/>
										</xsl:with-param>
									</xsl:call-template>
									<xsl:text>&#10;</xsl:text>
									<xsl:text> * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;ul&gt;</xsl:text>
									<xsl:call-template name="insert-javadoc-line-breaks-recurse">
										<xsl:with-param name="inputString"><xsl:value-of select="substring-after(normalize-space($tooltipText),$preambleWarning)"/></xsl:with-param>
										<xsl:with-param name="breakText1"><xsl:text>Hint:</xsl:text></xsl:with-param>
										<xsl:with-param name="breakText2"><xsl:text>Warning:</xsl:text></xsl:with-param>
									</xsl:call-template>
									<xsl:text>&#10;</xsl:text>
									<xsl:text> * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/ul&gt;</xsl:text>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
						<xsl:otherwise>
							<xsl:copy-of select="$tooltipText"/>
						</xsl:otherwise>
					</xsl:choose>
					<xsl:text>&#10;</xsl:text>
					<xsl:text> * </xsl:text>
					<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
					<xsl:text>&#10;</xsl:text>
					<xsl:if test="not($containsHintWarning)">
						<xsl:text> * </xsl:text>
						<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
						<xsl:text>&#10;</xsl:text>
					</xsl:if>				
				</xsl:if>
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
	<xsl:text>*** $name=</xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:text>, $x3d.tooltips.path=</xsl:text>
	<xsl:value-of select="$x3d.tooltips.path"/>
	<xsl:text>, doc-available($x3d.tooltips.path)=</xsl:text>
	<xsl:value-of select="doc-available($x3d.tooltips.path)"/>
	<xsl:text>, $tooltipText=</xsl:text>
	<xsl:value-of select="$tooltipText"/>
	<!--
	<xsl:text>&#10;</xsl:text>
	<xsl:text>  $tooltipTextWithHyperlinks=</xsl:text>
	<xsl:copy-of select="$tooltipTextWithHyperlinks"/>
	-->
</xsl:message>
</xsl:if>
			</xsl:if> <!-- end tooltip -->
			
			<xsl:if test="not($isInterface = 'true') and
						  (   contains($name, 'FColor')            or contains($name, 'Background')           or 
						   starts-with($name, 'ColorChaser')       or starts-with($name, 'ColorDamper')       or contains($name, 'Light')      or 
						   starts-with($name, 'ColorInterpolator') or starts-with($name, 'ParticleSystem')    or contains($name, 'Fog')        or
						   starts-with($name, 'Fog')               or starts-with($name, 'TextureProperties') or contains($name, 'Material')   or
						   starts-with($name, 'FillProperties')    or starts-with($name, 'LineProperties')    or starts-with($name, 'MultiTexture') or
						   starts-with($name, 'EdgeEnhancementVolumeStyle') or starts-with($name, 'CartoonVolumeStyle') or
						   starts-with($name, 'OpacityMapVolumeStyle')      or starts-with($name, 'ToneMappedVolumeStyle'))">
				
				<xsl:text> * Note that {@linkplain SFColor</xsl:text>
				<xsl:value-of select="$jsaiClassSuffix"/>
				<xsl:text>#ALICEBLUE SFColor</xsl:text><xsl:value-of select="$jsaiClassSuffix"/>
				<xsl:text>} also provides a variety of color constants.</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			
			<xsl:if test="($name = 'meta')">
				<xsl:text>&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes"> Metadata terms for consistent referencing:</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;ul&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; Dublin Core Metadata Initiative (DCMI): &lt;a href="http://www.dublincore.org/documents/dcmi-terms" target="_blank"&gt;Terms&lt;/a&gt; and </xsl:text>
				<xsl:text disable-output-escaping="yes"> &lt;a href="http://www.dublincore.org/documents/dces" target="_blank"&gt;Element Set&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; HTML5 section 4.2.5: &lt;a href="https://www.w3.org/TR/html5/document-metadata.html#the-meta-element" target="_blank"&gt;The meta element&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; HTML4 section 7.4.4: &lt;a href="http://www.w3.org/TR/html4/struct/global.html#h-7.4.4" target="_blank"&gt;Meta data&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; &lt;a href="http://vancouver-webpages.com/META" target="_blank"&gt;Dictionary of HTML META Tags&lt;/a&gt; </xsl:text>
				<xsl:text disable-output-escaping="yes">   (&lt;a href="http://vancouver-webpages.com/META/about-mk-metas2.html" target="_blank"&gt;About&lt;/a&gt;) &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;/ul&gt;&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes"> Metadata terms for language codes:</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;ul&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; IETF Best Current Practice (BCP) 47: &lt;a href="https://tools.ietf.org/html/bcp47" target="_blank"&gt;Tags for Identifying Languages&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; ISO 639-2: &lt;a href="http://www.loc.gov/standards/iso639-2/langhome.html" target="_blank"&gt;Codes for the Representation of Names of Languages&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; Internet Assigned Numbers Authority (IANA) Protocol Registries: &lt;a href="http://www.iana.org/protocols#index_L" target="_blank"&gt;Language Tags&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;/ul&gt;&#10;</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			
			<xsl:if test="($name = 'unit')">
				<xsl:text>&#10;</xsl:text>`
				<xsl:text disable-output-escaping="yes"> * &lt;a href="http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/concepts.html#Standardunitscoordinates" target="_blank"&gt;X3D specification: 4.3.6 Standard units and coordinate system&lt;/a&gt; &#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> defines how scale factors can modify an entire scene.</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * Scale-conversion constants provide correct names and values for common conversion factors. References:</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;ul&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; &lt;a href="http://www.unit-conversion.info" target="_blank"&gt;Unit conversion&lt;/a&gt; website &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; &lt;a href="http://en.wikipedia.org/wiki/Newton_%28unit%29#Conversion_factors" target="_blank"&gt;Wikipedia Conversion factors, units of force&lt;/a&gt; &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;li&gt; &lt;a href="http://www.unitsconversion.com.ar/massunitsconversion/index.htm" target="_blank"&gt;Unit conversion&lt;/a&gt; website &lt;/li&gt;&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"> * &lt;/ul&gt;&#10;</xsl:text>
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			
			<xsl:if test="not($name = 'CommentsBlock') and not($name = 'ConfigurationProperties') and not($inConcretePackage = 'true')"> <!-- final entries -->
				<xsl:text> * </xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;i&gt;Package hint:&lt;/i&gt; </xsl:text>
				<xsl:choose>
					<xsl:when test="($isInterface = 'true')">
						<xsl:text> This interface is defined by the X3D Java Language Binding Specification for the Scene Authoring Interface (SAI).</xsl:text>
					</xsl:when>
					<!-- TODO confirm wording OK in each case: -->
					<xsl:when test="($isFieldInterface or $isException or $isServiceInterface)">
						<xsl:text> This specification class is defined by the X3D Java Language Binding Specification for the Scene Authoring Interface (SAI).</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text> This </xsl:text>
						<xsl:value-of select="$concretePackage"/>
						<xsl:text> concrete class is used for implementing a standalone X3D object as a Plain Old Java Object (POJO).</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text> * If you are writing Java code for use inside an X3D Script node, compile using the </xsl:text>
						<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
						<xsl:value-of select="$saiPackage"/>
						<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
						<xsl:text> package instead.</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:text> *</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text> * @author Don Brutzman and Roy Walmsley</xsl:text><xsl:text>&#10;</xsl:text>
			
			<xsl:if test="(string-length($saiJavaSpecificationSection) > 0) or (string-length($saiJavaSpecificationRelativeUrl) > 0)">
				<!-- diagnostics if one is missing -->
				<xsl:if test="not($saiJavaSpecificationSection) or (string-length($saiJavaSpecificationSection) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains saiJavaSpecificationRelativeUrl but not saiJavaSpecificationSection</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="not($saiJavaSpecificationRelativeUrl) or (string-length($saiJavaSpecificationRelativeUrl) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains saiJavaSpecificationSection but not saiJavaSpecificationRelativeUrl</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="ends-with($saiJavaSpecificationRelativeUrl,'#')">
					<xsl:message>
						<xsl:text>*** Code-generation error: saiJavaSpecificationRelativeUrl=</xsl:text>
						<xsl:value-of select="$saiJavaSpecificationRelativeUrl"/>
						<xsl:text> ends with # and is missing bookmark</xsl:text>
					</xsl:message>
				</xsl:if>
				<!-- javadoc -->
				<xsl:text> * @see </xsl:text>
				<xsl:element name="a">
					<xsl:attribute name="href">
						<xsl:value-of select="$saiJavaSpecificationRootUrl"/>
						<xsl:text>/</xsl:text>
						<xsl:value-of select="$saiJavaSpecificationRelativeUrl"/>
					</xsl:attribute>
					<xsl:attribute name="target">
						<xsl:text>_blank</xsl:text>
					</xsl:attribute>
					<xsl:text>SAI Java Specification</xsl:text>
					<xsl:if test="string-length($saiJavaSpecificationSection) > 0">
						<xsl:text>: </xsl:text>
						<xsl:value-of select="$saiJavaSpecificationSection"/>
					</xsl:if>
				</xsl:element>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:if test="(string-length($saiAbstractSpecificationSection) > 0) or (string-length($saiAbstractSpecificationRelativeUrl) > 0)">
				<!-- diagnostics if one is missing -->
				<xsl:if test="not($saiAbstractSpecificationSection) or (string-length($saiAbstractSpecificationSection) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains saiAbstractSpecificationRelativeUrl but not saiAbstractSpecificationSection</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="not($saiAbstractSpecificationRelativeUrl) or (string-length($saiAbstractSpecificationRelativeUrl) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains saiAbstractSpecificationSection but not saiAbstractSpecificationRelativeUrl</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="ends-with($saiAbstractSpecificationRelativeUrl,'#')">
					<xsl:message>
						<xsl:text>*** Code-generation error: saiAbstractSpecificationRelativeUrl=</xsl:text>
						<xsl:value-of select="$saiAbstractSpecificationRelativeUrl"/>
						<xsl:text> ends with # and is missing bookmark</xsl:text>
					</xsl:message>
				</xsl:if>
				<!-- javadoc -->
				<xsl:text> * @see </xsl:text>
				<xsl:element name="a">
					<xsl:attribute name="href">
						<xsl:value-of select="$saiAbstractSpecificationRootUrl"/>
						<xsl:text>/</xsl:text>
						<xsl:value-of select="$saiAbstractSpecificationRelativeUrl"/>
					</xsl:attribute>
					<xsl:attribute name="target">
						<xsl:text>_blank</xsl:text>
					</xsl:attribute>
					<xsl:text>SAI Abstract Specification</xsl:text>
					<xsl:if test="string-length($saiAbstractSpecificationSection) > 0">
						<xsl:text>: </xsl:text>
						<xsl:value-of select="$saiAbstractSpecificationSection"/>
					</xsl:if>
				</xsl:element>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:if test="(string-length($x3dAbstractSpecificationSection) > 0) or (string-length($x3dAbstractSpecificationRelativeUrl) > 0)">
				<!-- diagnostics if one is missing -->
				<xsl:if test="not($x3dAbstractSpecificationSection) or (string-length($x3dAbstractSpecificationSection) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains x3dAbstractSpecificationRelativeUrl but not x3dAbstractSpecificationSection</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="not($x3dAbstractSpecificationRelativeUrl) or (string-length($x3dAbstractSpecificationRelativeUrl) = 0)">
					<xsl:message>
						<xsl:text>*** Code-generation error: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> definition contains x3dAbstractSpecificationSection but not x3dAbstractSpecificationRelativeUrl</xsl:text>
					</xsl:message>
				</xsl:if>
				<xsl:if test="ends-with($x3dAbstractSpecificationSection,'#')">
					<xsl:message>
						<xsl:text>*** Code-generation error: x3dAbstractSpecificationSection=</xsl:text>
						<xsl:value-of select="$x3dAbstractSpecificationSection"/>
						<xsl:text> ends with # and is missing bookmark</xsl:text>
					</xsl:message>
				</xsl:if>
				<!-- javadoc -->
				<xsl:text> * @see </xsl:text>
				<xsl:element name="a">
					<xsl:attribute name="href">
						<xsl:value-of select="$x3dAbstractSpecificationRootUrl"/>
						<xsl:text>/</xsl:text>
						<xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/>
					</xsl:attribute>
					<xsl:attribute name="target">
						<xsl:text>_blank</xsl:text>
					</xsl:attribute>
					<xsl:text>X3D Abstract Specification</xsl:text>
					<xsl:if test="string-length($x3dAbstractSpecificationSection) > 0">
						<xsl:text>: </xsl:text>
						<xsl:value-of select="$x3dAbstractSpecificationSection"/>
					</xsl:if>
				</xsl:element>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			<xsl:if test="not($name = 'CommentsBlock')">
				<xsl:text> * @see </xsl:text>
				<xsl:element name="a">
					<xsl:attribute name="href">
						<xsl:text>http://www.web3d.org/x3d/content/X3dTooltips.html#</xsl:text>
						<xsl:value-of select="$name"/>
					</xsl:attribute>
					<xsl:attribute name="target">
						<xsl:text>_blank</xsl:text>
					</xsl:attribute>
					<xsl:text>X3D Tooltips</xsl:text>
					<xsl:if test="not(starts-with($name, 'SF')) and not(starts-with($name, 'MF')) and
								  not(starts-with($name, 'X3D') and (string-length($name) > 3))">
						<xsl:text>: </xsl:text>
						<xsl:value-of select="$name"/>
					</xsl:if>
				</xsl:element>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
			
			<xsl:text> * @see </xsl:text>
			<xsl:element name="a">
				<xsl:attribute name="href">
					<xsl:text>http://www.web3d.org/x3d/content/examples/X3dResources.html</xsl:text>
				</xsl:attribute>
				<xsl:attribute name="target">
					<xsl:text>_blank</xsl:text>
				</xsl:attribute>
				<xsl:text>X3D Resources</xsl:text>
			</xsl:element>
			<xsl:text>&#10;</xsl:text>
			
			<xsl:text> * @see </xsl:text>
			<xsl:element name="a">
				<xsl:variable name="sceneAuthoringHintSection">
						<xsl:choose>
							<xsl:when test="($name = 'AudioClip') or ($name = 'Sound')">
								<xsl:text>Audio</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'Color')">
								<xsl:text>metaTags</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'meta')">
								<xsl:text>metaTags</xsl:text>
							</xsl:when>
							<xsl:when test="starts-with($name,'Metadata')">
								<xsl:text>Metadata</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'Inline') or ($name = 'IMPORT') or ($name = 'EXPORT') or ($name = 'AS') or starts-with($name,'Proto')">
								<xsl:text>InlinesPrototypes</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'Script')">
								<xsl:text>Scripts</xsl:text>
							</xsl:when>
							<xsl:when test="contains($name, 'Texture')">
								<xsl:text>Images</xsl:text>
							</xsl:when>
							<xsl:when test="contains($name, 'Triangle') or contains($name, 'Face') or contains($name, 'Quad')">
								<xsl:text>Meshes</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'Transform')">
								<xsl:text>CoordinateSystems</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'url')">
								<xsl:text>urls</xsl:text>
							</xsl:when>
							<xsl:when test="contains($name,'Viewpoint') or ($name = 'NavigationInfo')">
								<xsl:text>Viewpoints</xsl:text>
							</xsl:when>
							<xsl:when test="contains($name, 'Volume')">
								<xsl:text>Volume</xsl:text>
							</xsl:when>
						</xsl:choose>
					</xsl:variable>
				<xsl:attribute name="href">
					<xsl:text>http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html</xsl:text>
					<!-- append relevant bookmarks -->
					<xsl:if test="(string-length($sceneAuthoringHintSection) > 0)">
						<xsl:text>#</xsl:text>
						<xsl:value-of select="$sceneAuthoringHintSection"/>
					</xsl:if>
				</xsl:attribute>
				<xsl:attribute name="target">
					<xsl:text>_blank</xsl:text>
				</xsl:attribute>
				<xsl:text>X3D Scene Authoring Hints</xsl:text>
				<xsl:if test="(string-length($sceneAuthoringHintSection) > 0)">
					<xsl:text>: </xsl:text>
					<xsl:value-of select="$sceneAuthoringHintSection"/>
				</xsl:if>
			</xsl:element>
			<xsl:text>&#10;</xsl:text>
			<xsl:choose>
				<xsl:when test="($name = 'IS')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
	 * @see connectObject
	 * @see ProtoDeclareObject
	 * @see ProtoInterfaceObject
	 * @see ProtoBodyObject
	 * @see ProtoInstanceObject
]]></xsl:text>
				</xsl:when>
				<xsl:when test="($name = 'connect')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
	 * @see ISObject
	 * @see ProtoDeclareObject
	 * @see ProtoInterfaceObject
	 * @see ProtoBodyObject
	 * @see ProtoInstanceObject
]]></xsl:text>
				</xsl:when>
			</xsl:choose>
			
			<xsl:text> */</xsl:text><!-- end javadoc -->
			<xsl:text>&#10;</xsl:text>
			
			<!-- ********************************************************************************** -->
			<!-- generate source code -->
			<xsl:value-of select="$visibility"/>
			<xsl:if test="(string-length($visibility) > 0)">
				<xsl:text> </xsl:text>
			</xsl:if>
			<xsl:if test="($isAbstract = 'true')">
				<xsl:text>abstract</xsl:text>
				<xsl:text> </xsl:text>
			</xsl:if>
			<xsl:choose>
				<xsl:when test="($isInterface = 'true')">
					<xsl:text>interface</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:text>class</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$name"/>
			<xsl:if test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
						  not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not(starts-with($name,'X3DConcrete'))">
				<xsl:value-of select="$jsaiClassSuffix"/>
			</xsl:if>
			<xsl:if test="string-length($extends) > 0">
				<xsl:text> extends </xsl:text>
				<xsl:choose>
					<xsl:when test="contains($extends,'.')">
						<!-- TODO substring after last . http://stackoverflow.com/questions/17468891/substring-after-last-character-in-xslt -->
						<xsl:value-of select="$extends"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="$extends"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
			<xsl:if test="string-length($implements) > 0">
				<xsl:text> implements </xsl:text>
				<xsl:value-of select="$implements"/>
			</xsl:if>
			
			<xsl:variable name="wrapClassBrackets">
				<!-- BrowserEvent and BrowserFactory are classes ; $isClassX3dStatement or or -->
				<xsl:value-of select="(not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and not($name = 'CommentsBlock'))
                                       or ($name = 'BrowserFactory') or ($name = 'BrowserFactoryImpl') or ($name = 'BrowserListener')"/>
			</xsl:variable>
			<xsl:if test="($wrapClassBrackets)">
				<xsl:text>&#10;</xsl:text>
				<xsl:text>{</xsl:text>
			</xsl:if>
			
			<!-- interfaceBlock and sourceFile completeness diagnostics -->
			<xsl:choose>
				<xsl:when test="($isInterface = 'true') and ($hasInterfaceBlock)">
					<xsl:if test="starts-with(normalize-space($interfaceBlock),'{')">
						<xsl:message>
							<xsl:text>*** Code-generation warning: $interfaceBlock starts with {</xsl:text>
						</xsl:message>
					</xsl:if>
					<xsl:value-of select="$interfaceBlock" disable-output-escaping="yes"/> <!-- typically has additional javadoc for each member -->
				</xsl:when>
				<xsl:when test="($isInterface = 'true') and not($hasField)">
					<xsl:message>
						<xsl:text>*** Code-generation warning: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> has no interfaceBlock defined, stub comment inserted</xsl:text>
						<!-- debug -->
						<xsl:text>; $hasField=</xsl:text>
						<xsl:value-of select="$hasField"/>
						<xsl:text>, $isInterface=</xsl:text>
						<xsl:value-of select="$isInterface"/>
						<xsl:text>, $hasInterfaceBlock=</xsl:text>
						<xsl:value-of select="$hasInterfaceBlock"/>
						<xsl:text>, $hasImplementationBlock=</xsl:text>
						<xsl:value-of select="$hasImplementationBlock"/>
					</xsl:message>
					<!--
					<xsl:if test="not($hasInterfaceBlock)">
						<xsl:text>

	// TODO define interfaceBlock in CreateX3dSceneAccessInterfaceJava.xslt</xsl:text>
					</xsl:if>
					-->
				</xsl:when>
				<xsl:when test="not($isInterface = 'true') and not($hasField) and not($hasImplementationBlock) and not($name = 'CommentsBlock')">
					<xsl:message>
						<xsl:text>*** Code-generation warning: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> has no implementationBlock defined, stub comment inserted</xsl:text>
						<!-- debug -->
						<xsl:text>; $hasField=</xsl:text>
						<xsl:value-of select="$hasField"/>
						<xsl:text>, $isInterface=</xsl:text>
						<xsl:value-of select="$isInterface"/>
						<xsl:text>, $hasInterfaceBlock=</xsl:text>
						<xsl:value-of select="$hasInterfaceBlock"/>
						<xsl:text>, $hasImplementationBlock=</xsl:text>
						<xsl:value-of select="$hasImplementationBlock"/>
					</xsl:message>
					<!--
					<xsl:text>
	// TODO define implementationBlock in CreateX3dSceneAccessInterfaceJava.xslt
					</xsl:text>
					-->
				</xsl:when>
				<xsl:when test="($isInterface = 'true') or not($isInterface = 'true')">
					<!-- fallthrough case, OK -->
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>
						<xsl:text>*** Code-generation warning: </xsl:text>
						<xsl:value-of select="$name"/>
						<xsl:text> has illegal definition, $isInterface=</xsl:text>
						<xsl:value-of select="$isInterface"/>
						<xsl:text> (allowed values are true or false)</xsl:text>
					</xsl:message>
					<xsl:text>
						
	// TODO code-generation error, need to correctly define $isInterface as true or false in CreateX3dSceneAccessInterfaceJava.xslt
					</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
					
			<xsl:if test="not($hasChildrenField = 'true') and not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
                          not(starts-with($name, 'X3DConcrete'))">
				<xsl:text disable-output-escaping="yes"><![CDATA[
	private ArrayList<String> commentsList; // provided since no children array present
]]></xsl:text>
			</xsl:if>
			
			<xsl:choose>
				<xsl:when test="($isInterface = 'true') and ($inConcretePackage = 'true')">
					<!-- all done with this interface, which extends SAI interface -->
				</xsl:when>
				<xsl:when test="($hasField)">

					<!-- ===================================================== -->
					<!-- Source code: Member declarations -->
					<xsl:choose>
						<!-- define default attribute types and SFString/MFString enumeration constants (if any) -->
						<xsl:when test="($isInterface = 'true') or ($name = 'CommentsBlock')">
							<!-- no output -->
						</xsl:when>
						<xsl:when test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface)">
							<!-- Source code: member object declarations -->
							<xsl:for-each select="InterfaceDefinition/field[((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove')) and
												  not(@name = 'DEF') and not(@name = 'USE') and not(@name = 'class')]">

								<xsl:if test="position()=1">
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	// Member value declarations are encapsulated and private, using preferred Java types for concretes library</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:variable name="isX3dStatement">
									<xsl:call-template name="isX3dStatement">
										<xsl:with-param name="name" select="@name"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="memberObjectName"><!-- lower camel case, usually -->
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="@name"/>
										</xsl:when>
										<xsl:when test="(@name = 'AS')"><!-- special case: IMPORT, EXPORT -->
											<xsl:value-of select="@name"/>
										</xsl:when>
										<xsl:when test="(@name = 'set_boolean')"> <!-- special case: BooleanFilter, BooleanToggle, IntegerTrigger -->
											<xsl:text>booleanField</xsl:text>
										</xsl:when>
										<xsl:when test="starts-with(@name,'set_')">
											<xsl:value-of select="translate(substring(substring-after(@name,'set_'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
											<xsl:value-of select="substring(substring-after(@name,'set_'),2)"/>
										</xsl:when>
										<xsl:when test="starts-with(@name,'set')">
											<xsl:value-of select="translate(substring(substring-after(@name,'set'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
											<xsl:value-of select="substring(substring-after(@name,'set'),2)"/>
										</xsl:when>
										<xsl:when test="contains(@name,'_changed')">
											<xsl:value-of select="translate(substring(substring-before(@name,'_changed'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
											<xsl:value-of select="substring(substring-before(@name,'_changed'),2)"/>
										</xsl:when>
										<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
											<!-- unmodified -->
											<xsl:value-of select="@name"/>
										</xsl:when>
										<xsl:when test="(@name = 'class')">
											<!-- getClass() is reserved by Java Object() class -->
											<xsl:text>cssClass</xsl:text>
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="translate(substring(@name,1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
											<xsl:value-of select="substring(@name,2)"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:variable>
								<xsl:variable name="normalizedMemberObjectName">
									<!-- translate name into legal Java form here to avoid xpath problems -->
									<xsl:value-of select="translate($memberObjectName,'-','_')"/>
									<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
										<xsl:text>List</xsl:text><!-- append to member name -->
									</xsl:if>
								</xsl:variable>
								<xsl:if test="not(preceding-sibling::*[@name=$memberObjectName]) and not(preceding-sibling::*[@name=concat('set',$memberObjectName)]) and not(preceding-sibling::*[@name=concat('set_',$memberObjectName)]) and not(preceding-sibling::*[@name=concat($memberObjectName,'_changed')])">
									<xsl:variable name="javaType">
										<!-- can include collections, must be escaped -->
										<xsl:call-template name="javaType">
											<xsl:with-param name="x3dType" select="@type"/>
											<xsl:with-param name="isInterface" select="$isInterface"/>
										</xsl:call-template>
									</xsl:variable>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	private </xsl:text>
									<xsl:value-of select="$javaType" disable-output-escaping="yes"/><!-- append to type name -->
									<xsl:if test="($isX3dStatement = 'true') and starts-with(@type,'X3D') and (ends-with(@type,'Node') or ends-with(@type,'Object'))">
										<xsl:value-of select="$jsaiInterfaceSuffix"/>
									</xsl:if>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:if test="contains($javaType,'ArrayList')">
										<xsl:text disable-output-escaping="yes"><![CDATA[ = new ArrayList<>()]]></xsl:text>
									</xsl:if>
									<xsl:text>;</xsl:text>
									<xsl:if test="contains(@acceptableNodeTypes,'|')">
										<xsl:text> // acceptable node types: </xsl:text>
										<xsl:value-of select="@acceptableNodeTypes"/>
										<!-- TODO is it possible to restrict these further when setting children? -->
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="(@type = 'SFNode') and not($isX3dStatement = 'true')">
										<!-- add corresponding member variable for SFNode ProtoInstance substitution -->
									<xsl:text>	private ProtoInstanceObject </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text>ProtoInstance; // allowed alternative for </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field</xsl:text>
									<xsl:text>&#10;</xsl:text>
									</xsl:if>
								</xsl:if>
							</xsl:for-each>
						
							<!-- Source code: add special constant definitions -->
							<xsl:choose>
								<xsl:when test="($name = 'X3D')">
									<!-- Excerpt from X3D-Edit SchemaData.java -->
									<xsl:text disable-output-escaping="yes"><![CDATA[
	/** XML header */
	public static final String XML_HEADER = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>";
										
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_4_1 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 4.1//EN\" \"http://www.web3d.org/specifications/x3d-4.1.dtd\">";
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_4_0 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 4.0//EN\" \"http://www.web3d.org/specifications/x3d-4.0.dtd\">";
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_3_3 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 3.3//EN\" \"http://www.web3d.org/specifications/x3d-3.3.dtd\">";
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_3_2 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 3.2//EN\" \"http://www.web3d.org/specifications/x3d-3.2.dtd\">";
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_3_1 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 3.1//EN\" \"http://www.web3d.org/specifications/x3d-3.1.dtd\">";
	/** X3D Document Type Definition http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String DOCTYPE_3_0 = "<!DOCTYPE X3D PUBLIC \"ISO//Web3D//DTD X3D 3.0//EN\" \"http://www.web3d.org/specifications/x3d-3.0.dtd\">";

	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_3_0_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-3.0.xsd'";
	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_3_1_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-3.1.xsd'";
	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_3_2_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-3.2.xsd'";
	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_3_3_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-3.3.xsd'";
	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_4_0_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-4.0.xsd'";
	/** X3D Schema attributes http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Validation */
	public static final String SCHEMA_4_1_ATTRIBUTES = "xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-4.1.xsd'";

]]></xsl:text>
								</xsl:when>
								<xsl:when test="not($isInterface = 'true') and ($name = 'unit')">
									<!-- unit factors from X3D-Edit X3dSchemaData.java -->
									<xsl:text disable-output-escaping="yes"><![CDATA[
	// Scale factors http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#Scale

	/** unit statement conversionFactor for converting scene values of angles to Radians from Degrees */
	public static final double CONVERSIONFACTOR_ANGLES_toRadiansFromDegrees = 0.0174532925167;
	/** unit statement conversionFactor for converting scene values of angles to Radians from FullCircle */
	public static final double CONVERSIONFACTOR_ANGLES_toRadiansFromFullCircle = 6.283185307179;
	/** unit statement conversionFactor for converting scene values of angles to Radians from Grads */
	public static final double CONVERSIONFACTOR_ANGLES_toRadiansFromGrads = 0.01570796326795;

	/** unit statement conversionFactor for converting scene values of length to Meters from Pica */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromPica = 0.0042175176;
	/** unit statement conversionFactor for converting scene values of length to Meters from Inches */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromInches = 0.0254;
	/** unit statement conversionFactor for converting scene values of length to Meters from Feet */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromFeet = 0.3048;
	/** unit statement conversionFactor for converting scene values of length to Meters from Yards */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromYards = 0.9144;
	/** unit statement conversionFactor for converting scene values of length to Meters from Fathoms */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromFathoms = 1.8288;
	/** unit statement conversionFactor for converting scene values of length to Meters from Furlongs */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromFurlongs = 201.1684;
	/** unit statement conversionFactor for converting scene values of length to Meters from Miles */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromMiles = 1609.344;
	/** unit statement conversionFactor for converting scene values of length to Meters from Nautical Miles */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromNauticalMiles = 1852.0;
	/** unit statement conversionFactor for converting scene values of length to Meters from Microns */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromMicrons = 0.000001;
	/** unit statement conversionFactor for converting scene values of length to Meters from Millimeters */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromMillimeters = 0.001;
	/** unit statement conversionFactor for converting scene values of length to Meters from Centimeters */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromCentimeters = 0.01;
	/** unit statement conversionFactor for converting scene values of length to Meters from Kilometers */
	public static final double CONVERSIONFACTOR_LENGTH_toMetersFromKilometers = 1000.0;
										
	/** unit statement conversionFactor for converting scene values of force to Newtons from Dynes */
	public static final double CONVERSIONFACTOR_FORCE_toNewtonsFromDynes = 0.00001;
	/** unit statement conversionFactor for converting scene values of force to Newtons from Kilogram-force */
	public static final double CONVERSIONFACTOR_FORCE_toNewtonsFromKilogramForce = 9.8068;
	/** unit statement conversionFactor for converting scene values of force to Newtons from Pounds-force */
	public static final double CONVERSIONFACTOR_FORCE_toNewtonsFromPoundsForce = 4.4482;
	/** unit statement conversionFactor for converting scene values of force to Newtons from Poundal */
	public static final double CONVERSIONFACTOR_FORCE_toNewtonsFromPoundal = 0.13826;
										
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Grains Avoirdupois (gr) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromGrains = 0.00006479891;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Drams Avoirdupois (dr) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromDrams = 0.001771845195312;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Ounces Avoirdupois (oz) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromOunces = 0.028349523125;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Troy Ounces (toz) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromTroyOunces = 0.0311034768;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Pounds Avoirdupois (lb) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromPounds = 0.45359237;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Stone, i.e. 14 Pounds Avoirdupois (lb) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromStone = 6.35029318;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Tons (U.S. short) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromTons = 907.18474;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Micrograms */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFrom = 0.000000001;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Milligrams */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromMilligrams = 0.000001;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Centigrams */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromCentigrams = 0.00001;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Carats */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromCarats = 0.0002;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Grams (g) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromGrams = 0.001;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Dekagrams */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromDekagrams = 0.01;
	/** unit statement conversionFactor for converting scene values of mass to Kilograms (kg) from Metric Tonnes (t) */
	public static final double CONVERSIONFACTOR_MASS_toKilogramsFromMetricTonnes = 1000.0;
										
]]></xsl:text>
								</xsl:when>
								<xsl:when test="not($isInterface = 'true') and (($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram'))">
									<xsl:text disable-output-escaping="yes"><![CDATA[
	private ArrayList<fieldObject> fieldList = new ArrayList<>(); // instantiation

	private String sourceCode;
]]></xsl:text>
								</xsl:when>
								<xsl:when test="not($isInterface = 'true') and (($name = 'ProtoBody'))">
									<xsl:text disable-output-escaping="yes"><![CDATA[
	/** The first node of a prototype declaration determines its node type, and a reference is stored here. 
		The node itself also remains in the children list, in order with other CommentBlocks and additional ProtoBody contained nodes. */
	private X3DConcreteNode primaryNode;
]]></xsl:text>
								</xsl:when>
								<!--  ProtoInterface fieldList and ProtoInstance fieldValueList declarations handled separately -->
							</xsl:choose>
							
							<xsl:if test="not($isInterface = 'true') and not($isX3dStatement = 'true')">
									<xsl:text disable-output-escaping="yes"><![CDATA[
	/** IS/connect statements might be used if this node is within a ProtoBody and connections are defined between prototype fields and built-in node fields */
	private ISObject IS;
]]></xsl:text>
							</xsl:if>

							<!-- Source code: String enumeration constants -->
							<xsl:for-each select="InterfaceDefinition/field/enumeration[(@value!='...') and (string-length(normalize-space(@value)) > 0)]">

								<xsl:if test="position()=1">
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	// ===== String constants for enumeration values ensure correct syntax and avoid run-time errors =====</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:variable name="fieldName" select="translate(../@name,'-','_')"/>

								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/** </xsl:text>
								<xsl:value-of select="../@type"/>
								<xsl:text> field named </xsl:text>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:value-of select="$fieldName"/>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:choose>
									<xsl:when test="(../@type = 'SFString')">
										<xsl:text> can equal this </xsl:text>
									</xsl:when>
									<xsl:when test="(../@type = 'MFString') and (../@additionalEnumerationValuesAllowed='true')">
										<xsl:text> is an array that can include this escape-quoted </xsl:text>
									</xsl:when>
									<xsl:when test="(../@type = 'MFString')">
										<xsl:text> is an array that can equal this escape-quoted </xsl:text>
									</xsl:when>
								</xsl:choose>
								<xsl:text>enumeration value </xsl:text>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:call-template name="javaValue">
									<xsl:with-param name="javadoc"><xsl:text>true</xsl:text></xsl:with-param>
									<xsl:with-param name="x3dType">
										<xsl:choose>
											<xsl:when test="(../@type='MFString') and not(contains(@value,'&quot;'))">
												<xsl:text>EscapeQuotedSFString</xsl:text><!-- intentional override -->
											</xsl:when>
											<xsl:when test="(../@type='MFString')">
												<xsl:text>MFString</xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:text>SFString</xsl:text><!-- intentional override -->
											</xsl:otherwise>
										</xsl:choose>
									</xsl:with-param>
									<xsl:with-param name="schemaValue">
										<xsl:value-of select="@value"/>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:text> (Java syntax) or </xsl:text>
								<xsl:if test="(../@type='MFString')">
									<xsl:text>quoted enumeration value </xsl:text>
								</xsl:if>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:if test="(../@type='MFString')">
									<xsl:text>'</xsl:text>
								</xsl:if>
								<xsl:value-of select="@value"/>
								<xsl:if test="(../@type='MFString')">
									<xsl:text>'</xsl:text>
								</xsl:if>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:text> (XML syntax).</xsl:text>
								<xsl:if test="(string-length(@appinfo) > 0)">
									<!-- TODO why isn't @appinfo appearing?  example metaNameValues --> 
									<xsl:text>&#10;</xsl:text>
									<xsl:text>       * </xsl:text>
									<xsl:value-of select="@appinfo"/>
								</xsl:if>
								<xsl:text> */</xsl:text><!-- end javadoc -->
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	public static final </xsl:text>
								<!-- TODO not all String enumeration constants are final arrays, some are addable elements -->
								<xsl:value-of disable-output-escaping="yes">
									<!-- can include collections, must be escaped -->
									<xsl:call-template name="javaType">
										<xsl:with-param name="x3dType" select="../@type"/>
									</xsl:call-template>
								</xsl:value-of>
								<xsl:text> </xsl:text>
								<xsl:value-of select="upper-case($fieldName)"/>
								<xsl:text>_</xsl:text>
								<!-- enumeration name: omit " character, others become _ underscore -->
								<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
								<xsl:text> = </xsl:text>
								<xsl:call-template name="javaValue">
									<xsl:with-param name="x3dType">
										<xsl:value-of select="../@type"/>
									</xsl:with-param>
									<xsl:with-param name="schemaValue">
										<xsl:value-of select="@value"/>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:text>;</xsl:text>
								<xsl:text>&#10;</xsl:text>
							</xsl:for-each>									
							
							<xsl:if test="not($isInterface = 'true')">
								<xsl:choose>
									<xsl:when test="($name = 'X3DConcreteElement')">
										<xsl:text disable-output-escaping="yes"><![CDATA[
	/** String constant <i>NAME</i> provides name of this element; overridden by implementing class. */
	protected static final String NAME = ""; // must be overridden
]]></xsl:text>
									</xsl:when>
									<xsl:when test="starts-with($name, 'X3DConcrete')">
										<!-- do not re-declare NAME, let class definition provide override -->
									</xsl:when>
									<xsl:when test="($name = 'ConfigurationProperties')">
										<!-- do not re-declare NAME, let class definition provide override -->
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	// String constants for default field values match X3D Schema definitions</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text disable-output-escaping="yes"><![CDATA[
	/** String constant <i>NAME</i> provides name of this element: <i>]]></xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text disable-output-escaping="yes"><![CDATA[</i>. */
	@SuppressWarnings("FieldNameHidesFieldInSuperclass")
	protected static final String NAME = "]]></xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text><![CDATA[";

	/** Provides name of this element: ]]></xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text><![CDATA[.
	 * @return name of this element
	 */
	@Override
	public final String getElementName()
	{
		return NAME;
	}
]]></xsl:text>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:if>

							<!-- Source code: _DEFAULT_VALUE definitions -->
							<xsl:for-each select="InterfaceDefinition/field[((@type='SFString') or (@type='MFString') or (string-length(normalize-space(@default)) > 0)) and 
											      not(@type='SFNode') and not(@type='MFNode') and
												  not(@name = 'DEF') and not(@name = 'USE') and not(@name = 'class')]">


								<xsl:variable name="isX3dStatement">
									<xsl:call-template name="isX3dStatement">
										<xsl:with-param name="name" select="@name"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="fieldName" select="translate(@name,'-','_')"/>

								<xsl:variable name="defaultValue">
									<xsl:value-of select="@default"/>
								</xsl:variable>

								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/** </xsl:text>
								<xsl:if test="($name = 'field') and ((@name = 'type') or (@name = 'accessType'))">
									<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
									<xsl:text>Initial value is required to be set for validity:</xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
									<xsl:text> </xsl:text>
								</xsl:if>
								<xsl:value-of select="@type"/>
								<xsl:text> field named </xsl:text>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:value-of select="$fieldName"/>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:text> has default </xsl:text>
								<xsl:choose>
									<xsl:when test="(string-length($defaultValue) > 0)">
										<xsl:if test="(@type = 'MFString')">
											<xsl:text>escape-quoted </xsl:text>
										</xsl:if>
										<xsl:text>value </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:call-template name="javaValue">
											<xsl:with-param name="javadoc"><xsl:text>true</xsl:text></xsl:with-param>
											<xsl:with-param name="x3dType">
												<xsl:value-of select="@type"/>
											</xsl:with-param>
											<xsl:with-param name="schemaValue">
												<xsl:value-of select="$defaultValue"/>
											</xsl:with-param>
										</xsl:call-template>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text> (Java syntax) or </xsl:text>
										<xsl:if test="(@type = 'MFString')">
											<xsl:text>quoted value </xsl:text>
										</xsl:if>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:value-of select="$defaultValue"/>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text> (XML syntax)</xsl:text>
									</xsl:when>
									<xsl:when test="starts-with(@type, 'MF')">
										<xsl:text>value equal to an empty list</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>value equal to an empty string</xsl:text>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:text>. </xsl:text>
								<xsl:text>*/</xsl:text><!-- end javadoc -->
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	public static final </xsl:text>
								<xsl:value-of disable-output-escaping="yes">
									<!-- can include collections, must be escaped -->
									<xsl:call-template name="javaType">
										<xsl:with-param name="x3dType" select="@type"/>
										<xsl:with-param name="isInterface" select="$isInterface"/>
									</xsl:call-template>
								</xsl:value-of>
								<xsl:text> </xsl:text>
								<xsl:value-of select="upper-case($fieldName)"/>
								<xsl:text>_DEFAULT_VALUE</xsl:text>
								<xsl:text> = </xsl:text>
								<xsl:call-template name="javaValue">
									<xsl:with-param name="x3dType">
										<xsl:value-of select="@type"/>
									</xsl:with-param>
									<xsl:with-param name="schemaValue">
										<xsl:value-of select="$defaultValue"/>
									</xsl:with-param>
								</xsl:call-template>
								<xsl:text>;</xsl:text>
								<xsl:text>&#10;</xsl:text>
							</xsl:for-each>

							<xsl:variable name="isX3dStatement">
								<xsl:call-template name="isX3dStatement">
									<xsl:with-param name="name" select="@name"/>
								</xsl:call-template>
							</xsl:variable>
							
							<xsl:if test="InterfaceDefinition/field[((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove'))]">
								<!-- Source code: getType -->
								<xsl:text disable-output-escaping="yes">
	/** Indicate type corresponding to field name.
	 * @param fieldName name of field in this X3D </xsl:text>
								<xsl:choose>
								   <xsl:when test="($isX3dStatement = 'true')">
									   <xsl:text>statement</xsl:text>
								   </xsl:when>
								   <xsl:otherwise>
									   <xsl:text>node</xsl:text>
								   </xsl:otherwise>
								</xsl:choose>
								<xsl:text disable-output-escaping="yes">
	 * @return X3D type (SFvec3f etc.), otherwise UnknownField_fieldName if not recognized
	 */
	@Override		
	public String getType(String fieldName)
	{
		String result;
		switch (fieldName)
		{</xsl:text>
								<xsl:for-each select="InterfaceDefinition/field[((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove'))]">
									<xsl:if test="position()=1">
										<xsl:text>
			// String constants for exact field type values matching X3D Schema definitions,
			// thus avoiding spelling errors and allowing type-matching checks</xsl:text>
									</xsl:if>
									<xsl:variable name="fieldName" select="translate(@name,'-','_')"/>
									<xsl:variable name="hasPrecedingFieldDefinition">
										<!-- example: ParticleSystem has 'geometry' field annotation overriding Shape node -->
										<xsl:value-of select="(count(preceding-sibling::*[@name = $fieldName]) > 0)"/>
									</xsl:variable>
									<xsl:if test="not($hasPrecedingFieldDefinition = 'true')">
										<xsl:text>
			case "</xsl:text><xsl:value-of select="@name"/><xsl:text>":
				result = "</xsl:text><xsl:value-of select="@type"/><xsl:text>";
				break;</xsl:text>
									</xsl:if>
								</xsl:for-each>
									<xsl:text disable-output-escaping="yes">
			default:
				result = "UnknownField_</xsl:text><xsl:value-of select="@name"/>
				<xsl:text>"; // unique return value avoids mistaken comparison matches</xsl:text>
									<xsl:text>
		}
</xsl:text>
								<!-- now check special-case fields -->
								<xsl:choose>
									<xsl:when test="($name = 'Script')">
										<xsl:text>		// now check author-defined fields
		fieldObject fromFieldObject = this.getFieldByName(fieldName);
		if (fromFieldObject != null)
			result = fromFieldObject.getType(); // found it!
</xsl:text>
									</xsl:when>
									<xsl:when test="($name = 'ProtoInstance')">
										<!-- TODO -->
									</xsl:when>
								</xsl:choose>
								<xsl:text>		return result;
	}
</xsl:text>
								<!-- Source code: getAccessType -->
								<xsl:text disable-output-escaping="yes">
	/** Indicate accessType corresponding to field name.
	 * @param fieldName name of field in this X3D </xsl:text>
								<xsl:choose>
								   <xsl:when test="($isX3dStatement = 'true')">
									   <xsl:text>statement</xsl:text>
								   </xsl:when>
								   <xsl:otherwise>
									   <xsl:text>node</xsl:text>
								   </xsl:otherwise>
								</xsl:choose>
								<xsl:text disable-output-escaping="yes">
	 * @return X3D accessType (inputOnly etc.), otherwise UnknownField_fieldName if not recognized
	 */
	@Override
	public String getAccessType(String fieldName)
	{
		String result;
		switch (fieldName)
		{</xsl:text>
								<xsl:for-each select="InterfaceDefinition/field[((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove'))]">
									<xsl:if test="position()=1">
										<xsl:text>
			// String constants for exact field accessType values matching X3D Schema definitions,
			// thus avoiding spelling errors and allowing accessType-matching checks</xsl:text>
									</xsl:if>
									<xsl:variable name="fieldName" select="translate(@name,'-','_')"/>
									<xsl:variable name="hasPrecedingFieldDefinition">
										<!-- example: ParticleSystem has 'geometry' field annotation overriding Shape node -->
										<xsl:value-of select="(count(preceding-sibling::*[@name = $fieldName]) > 0)"/>
									</xsl:variable>
									<xsl:if test="not($hasPrecedingFieldDefinition = 'true')">
										<xsl:text>
			case "</xsl:text><xsl:value-of select="@name"/><xsl:text>":
				result = "</xsl:text><xsl:value-of select="@accessType"/><xsl:text>";
				break;</xsl:text>
									</xsl:if>
								</xsl:for-each>
								<xsl:text disable-output-escaping="yes">
			default:
				result = "UnknownField_</xsl:text><xsl:value-of select="@name"/>
				<xsl:text>"; // unique return value avoids mistaken matches
		}
</xsl:text>
								<!-- now check special-case fields -->
								<xsl:choose>
									<xsl:when test="($name = 'Script')">
										<xsl:text>		// now check author-defined fields
		fieldObject fromFieldObject = this.getFieldByName(fieldName);
		if (fromFieldObject != null)
			result = fromFieldObject.getAccessType(); // found it!
</xsl:text>
									</xsl:when>
									<xsl:when test="($name = 'ProtoInstance')">
									<!--
										<xsl:text>		// now check author-defined fields
		// TODO must find ProtoDeclare and ExternProtoDeclare by name
		
		fieldObject fromFieldObject = this.getFieldByName(fieldName);
		if (fromFieldObject != null)
			result = fromFieldObject.getAccessType(); // found it!
</xsl:text>
									-->
									</xsl:when>
								</xsl:choose>

									<xsl:text>		return result;
	}
</xsl:text>
							</xsl:if> <!-- end getType(fieldName), getAccessType(fieldName) -->
							
							<xsl:if test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
								<xsl:text>
	/** Contained plain-text source code */
	private String SOURCECODE_DEFAULT_VALUE = "";
								</xsl:text>
							</xsl:if>

							<!-- containerField defaults -->
							<xsl:if test="(string-length(InterfaceDefinition/containerField/@name) > 0)">
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/** containerField describes typical field relationship of a node to its parent.</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 * Usage is not ordinarily needed when using this API, default value is provided for informational purposes. */</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	String containerField_DEFAULT_VALUE = "</xsl:text>
								<xsl:value-of select="InterfaceDefinition/containerField/@name"/>
								<xsl:text>";</xsl:text>
								<xsl:text>&#10;</xsl:text>

								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/** containerField describes typical field relationship of a node to its parent.</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 * Usage is not ordinarily needed when using this API, alternative values are provided for informational purposes. */</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	String[] containerField_ALTERNATE_VALUES = { "</xsl:text>
								<xsl:value-of select="InterfaceDefinition/containerField/@name"/>
								<xsl:text>"</xsl:text>
								<!-- TODO iterate over values and add to array, once recorded in X3D XML Schema and X3D Object Model -->
								<xsl:text> };</xsl:text>
								<xsl:text>&#10;</xsl:text>
							</xsl:if>

							<xsl:if test="not($isX3dStatement = 'true')">
								<!-- Source code: _TOFIELD, FROM_FIELD definitions -->
								<xsl:for-each select="InterfaceDefinition/field[not((@name = 'DEF') or (@name = 'USE') or (@name = 'class'))]">
									<xsl:if test="position()=1">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	// String constants for field names usable in ROUTE statements</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:variable name="isX3dStatement">
										<xsl:call-template name="isX3dStatement">
											<xsl:with-param name="name" select="@name"/>
										</xsl:call-template>
									</xsl:variable>
									<xsl:variable name="name" select="@name"/>
									<xsl:variable name="fieldName" select="translate(@name,'-','_')"/>

									<xsl:variable name="hasPrecedingFieldDefinition">
										<!-- example: ParticleSystem has 'geometry' field annotation overriding Shape node -->
										<xsl:value-of select="(count(preceding-sibling::*[@name = $name]) > 0)"/>
									</xsl:variable>

									<!-- output event names -->
									<xsl:if test="(@accessType = 'outputOnly') or (@accessType='inputOutput') and not($hasPrecedingFieldDefinition = 'true')
												  and not($name = 'field') and not($name = 'fieldValue')">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	/** fromField ROUTE name for </xsl:text>
										<xsl:value-of select="@type"/>
										<xsl:text> field named </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:value-of select="$fieldName"/>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text>. </xsl:text>
										<xsl:text>*/</xsl:text><!-- end javadoc -->
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	public static final String fromField_</xsl:text>
										<xsl:value-of select="upper-case($fieldName)"/>
										<xsl:text> = "</xsl:text>
										<xsl:value-of select="$fieldName"/>
										<xsl:text>";</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>

									<!-- input event names -->
									<xsl:if test="(@accessType = 'inputOnly') or (@accessType='inputOutput') and not($hasPrecedingFieldDefinition = 'true') and not($isX3dStatement = 'true')">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	/** toField ROUTE name for </xsl:text>
										<xsl:value-of select="@type"/>
										<xsl:text> field named </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:value-of select="$fieldName"/>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text>. </xsl:text>
										<xsl:text>*/</xsl:text><!-- end javadoc -->
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	public static final String toField_</xsl:text>
										<xsl:value-of select="upper-case($fieldName)"/>
										<xsl:text> = "</xsl:text>
										<xsl:value-of select="$fieldName"/>
										<xsl:text>";</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
								</xsl:for-each>
							</xsl:if>
							
							<!-- Source code: constructor method -->
							<xsl:if test="not(starts-with($name, 'X3DConcrete'))"><!-- which have no initialize() method -->
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/** public constructor for </xsl:text>
								<xsl:value-of select="$thisClassName"/>
								<xsl:if test="(@type='MFNode')">
									<xsl:text>[]</xsl:text>
								</xsl:if>
								<xsl:text> to initialize member variables with default values. */</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	public </xsl:text>
								<xsl:value-of select="$name"/>
								<xsl:if test="not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not(starts-with($name,'X3DConcrete'))">
									<xsl:value-of select="$jsaiClassSuffix"/>
								</xsl:if>
								<xsl:if test="(@type='MFNode')">
									<xsl:text>[]</xsl:text>
								</xsl:if>
								<xsl:text>()</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	{</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>		super(); // constructor invocation and corresponding initialize()</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>		initialize();</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	}</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>&#10;</xsl:text>

								<!-- initialize() method -->
								<xsl:if test="not(contains($implementationBlock,' void initialize'))">
									<!-- Source code: initialize method -->
									<xsl:text>
	/** Initialize all member variables to default values. */
	@Override
	public final void initialize()
	{
		super.initialize();</xsl:text>
									<!-- initialize each field with default values -->
									<xsl:for-each select="InterfaceDefinition/field[
													not(starts-with(@name,'set_')) and not(ends-with(@name,'_changed')) and
													not(@name = 'DEF') and not(@name = 'USE') and not(@name = 'class') and
												 ((@accessType='inputOutput') or (@accessType='initializeOnly') or (string-length(@accessType)=0))]">
										<xsl:variable name="isX3dStatement">
											<xsl:call-template name="isX3dStatement">
												<xsl:with-param name="name" select="@name"/>
											</xsl:call-template>
										</xsl:variable>

										<!-- TODO avoid duplication, refactor as call-template; alternatively override X3D Object Model -->
										<xsl:variable name="defaultValue">
											<!-- Provide default values where useRequired in XML Schema, e.g. X3D version -->
											<xsl:choose>
												<xsl:when test="(@type='SFNode') or (@default='NULL')">
													<xsl:text>null</xsl:text>
												</xsl:when>
												<xsl:when test="(@type='MFNode')">
													<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;()</xsl:text><!-- ArrayList<> -->
												</xsl:when>
												<xsl:when test="(string-length(@default) > 0)">
													<xsl:value-of select="@default"/>
												</xsl:when>
											</xsl:choose>
										</xsl:variable>

										<xsl:text>&#10;</xsl:text>
										<xsl:text>		</xsl:text>
										<xsl:choose>
											<xsl:when test="(@name = 'class')">
												<!-- getClass() is reserved by Java Object() class -->
												<xsl:text>cssClass</xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="translate(@name,'-','_')"/> <!-- translate name here to avoid xpath problems -->
											</xsl:otherwise>
										</xsl:choose>
										<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
											<xsl:text>List</xsl:text><!-- append to member name -->
										</xsl:if>
										<xsl:text> = </xsl:text>
										<xsl:choose>
											<xsl:when test="(@type='SFNode') or (@type='MFNode')">
												<xsl:value-of select="$defaultValue" disable-output-escaping="yes"/>
												<xsl:text>;</xsl:text>
												<xsl:if test="($defaultValue = 'null')">
													<xsl:text> // clear out any prior node</xsl:text>
													<xsl:if test="(@type='MFNode')">
														<xsl:text>s</xsl:text>
													</xsl:if>
												</xsl:if>
											</xsl:when>
											<!-- TODO check if $defaultValue test is correct -->
											<xsl:when test="(@type='SFString') or (string-length(normalize-space($defaultValue)) > 0)">
												<xsl:value-of select="upper-case(translate(@name,'-','_'))"/> <!-- translate name here to avoid xpath problems -->
												<xsl:text>_DEFAULT_VALUE;</xsl:text>
											</xsl:when>
											<xsl:when test="(@type='MFString')">
												<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;(</xsl:text><!-- ArrayList<> -->
												<xsl:value-of select="upper-case(translate(@name,'-','_'))"/> <!-- translate name here to avoid xpath problems -->
												<xsl:text>_DEFAULT_VALUE</xsl:text>
												<xsl:text>);</xsl:text>
											</xsl:when>
											<xsl:when test="(@type='MFBool') or (@type = 'MFInt32') or (@type = 'SFImage') or (@type = 'MFImage') or (@type='MFFloat') or (@type='MFDouble') or (@type='MFTime')">
												<xsl:text disable-output-escaping="yes">new ArrayList&lt;&gt;();</xsl:text><!-- ArrayList<> -->
											</xsl:when>
											<xsl:when test="starts-with(@type,'MF')">
												<xsl:text> new </xsl:text>
												<xsl:value-of disable-output-escaping="yes">
													<!-- can include collections, must be escaped -->
													<xsl:call-template name="javaType">
														<xsl:with-param name="x3dType" select="@type"/>
														<xsl:with-param name="isInterface" select="$isInterface"/>
													</xsl:call-template>
												</xsl:value-of>
												<xsl:text> { };</xsl:text>
											</xsl:when>
											<xsl:when test="(string-length($defaultValue) = 0)">
												<!-- all fields should have a default value; report error if found -->
												<xsl:message>
													<xsl:text>*** No default value found for </xsl:text>
													<xsl:value-of select="$name"/>
													<xsl:text> field </xsl:text>
													<xsl:value-of select="@name"/>
												</xsl:message>
											</xsl:when>
										</xsl:choose>
									</xsl:for-each>
									<xsl:text>&#10;</xsl:text>

									<xsl:if test="not($hasChildrenField = 'true') and not(starts-with($name, 'X3DConcrete'))">
										<xsl:text disable-output-escaping="yes"><![CDATA[
		commentsList = new ArrayList<>(); // instantiate
]]></xsl:text>
									</xsl:if>
									<xsl:choose>
										<xsl:when test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
											<xsl:text disable-output-escaping="yes"><![CDATA[
			fieldList = new ArrayList<>(); // instantiate

			sourceCode = SOURCECODE_DEFAULT_VALUE; // reset
	]]></xsl:text>
										</xsl:when>
										<xsl:when test="($name = 'ProtoInterface')">
											<xsl:text disable-output-escaping="yes"><![CDATA[
			fieldList = new ArrayList<>(); // instantiate
	]]></xsl:text>
										</xsl:when>
										<xsl:when test="($name = 'ProtoInstance')">
											<xsl:text disable-output-escaping="yes"><![CDATA[
			fieldValueList = new ArrayList<>(); // instantiate
	]]></xsl:text>
										</xsl:when>
									</xsl:choose>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
							</xsl:if>
				
							<!-- Add class-specific methods and member definitions -->
							<xsl:variable name="protectedPreamble">
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	// Protected member value declarations are encapsulated and private, for internal library use only</xsl:text>
								<xsl:text>&#10;</xsl:text>
							</xsl:variable>
							<xsl:choose>
								<xsl:when test="($name = 'X3D')">
									<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * File extension for X3D XML Encoding, with dot prepended: <i>x3d</i>.
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/X3D_XML.html">X3D XML Encoding</a>
	 */
	public static final String FILE_EXTENSION_X3D = ".x3d";
										
	/**
	 * File extension for X3D ClassicVRML Encoding, with dot prepended: <i>x3dv</i>.
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/X3D_ClassicVRML.html">X3D ClassicVRML Encoding</a>
	 */
	public static final String FILE_EXTENSION_CLASSICVRML = ".x3dv";
										
	/**
	 * File extension for VRML97 Encoding, with dot prepended: <i>wrl</i>.
	 * @see <a href="http://www.web3d.org/documents/specifications/14772/V2.0/index.html">VRML97 Encoding</a>
	 */
	public static final String FILE_EXTENSION_VRML97 = ".wrl";
										
	/**
	 * Serialize scene graph using <i>toStringX3D()</i> then create a new X3D file with extension <i>x3d</i>.
	 * @see X3DObject#toStringX3D()
	 * @see <a href="https://docs.oracle.com/javase/tutorial/essential/io/file.html#textfiles">Buffered I/O Methods for Text Files</a>
	 * @param fileName name of file to create and save, can include local directory path
	 * @return File containing result (if operation succeeds)
	 */
	public File toFileX3D(String fileName)
	{
		if (!fileName.endsWith(FILE_EXTENSION_X3D))
		{
			throw new X3DException("fileName " + fileName + " does not end with extension \"" + FILE_EXTENSION_X3D + "\"");
		}
		Path outputFilePath = Paths.get(fileName);
		outputFilePath.toAbsolutePath(); // debug check, defaults to local directory
		
		// http://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html
		// http://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html
		Charset charset = Charset.forName("UTF-8");
										
		validate(); // strict checks before serializing scene and saving file

		String outputSceneText = toStringX3D();
		try (BufferedWriter bufferedWriter = Files.newBufferedWriter(outputFilePath, charset))
		{
			bufferedWriter.write(outputSceneText, 0, outputSceneText.length());
			return outputFilePath.toFile();
		}
		catch (IOException exception)
		{
			throw new X3DException("IOException for fileName " + fileName + ", unable to save file: " + exception);
		}
	}
	/**
	 * Serialize scene graph using <i>toStringClassicVRML()</i> then create a new X3D file with extension <i>x3d</i>.
	 * @see X3DObject#toStringClassicVRML()
	 * @see <a href="https://docs.oracle.com/javase/tutorial/essential/io/file.html#textfiles">Buffered I/O Methods for Text Files</a>
	 * @param fileName name of file to create and save, can include local directory path
	 * @return File containing result (if operation succeeds)
	 */
	public File toFileClassicVRML(String fileName)
	{
		if (!fileName.endsWith(FILE_EXTENSION_CLASSICVRML))
		{
			throw new X3DException("fileName " + fileName + " does not end with extension \"" + FILE_EXTENSION_CLASSICVRML + "\"");
		}
		Path outputFilePath = Paths.get(fileName);
		outputFilePath.toAbsolutePath(); // debug check, defaults to local directory
		
		// http://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html
		// http://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html
		Charset charset = Charset.forName("UTF-8");
		
		validate(); // strict checks before serializing scene and saving file

		String outputSceneText = toStringClassicVRML();
		try (BufferedWriter bufferedWriter = Files.newBufferedWriter(outputFilePath, charset))
		{
			bufferedWriter.write(outputSceneText, 0, outputSceneText.length());
			return outputFilePath.toFile();
		}
		catch (IOException exception)
		{
			throw new X3DException("IOException for fileName " + fileName + ", unable to save file: " + exception);
		}
	}
	/**
	 * Serialize scene graph using <i>toStringVRML97()</i> then create a new X3D file with extension <i>wrl</i>.
	 * @see X3DObject#toStringVRML97()
	 * @see <a href="https://docs.oracle.com/javase/tutorial/essential/io/file.html#textfiles">Buffered I/O Methods for Text Files</a>
	 * @param fileName name of file to create and save, can include local directory path
	 * @return File containing result (if operation succeeds)
	 */
	public File toFileVRML97(String fileName)
	{
		if (!fileName.endsWith(FILE_EXTENSION_VRML97))
		{
			throw new X3DException("fileName " + fileName + " does not end with extension \"" + FILE_EXTENSION_VRML97 + "\"");
		}
		Path outputFilePath = Paths.get(fileName);
		outputFilePath.toAbsolutePath(); // debug check, defaults to local directory
		
		// http://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html
		// http://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html
		Charset charset = Charset.forName("UTF-8");
		
		validate(); // strict checks before serializing scene and saving file

		String outputSceneText = toStringVRML97();
		try (BufferedWriter bufferedWriter = Files.newBufferedWriter(outputFilePath, charset))
		{
			bufferedWriter.write(outputSceneText, 0, outputSceneText.length());
			return outputFilePath.toFile();
		}
		catch (IOException exception)
		{
			throw new X3DException("IOException for fileName " + fileName + ", unable to save file: " + exception);
		}
	}
]]></xsl:text>
								</xsl:when>
								<xsl:when test="($name = 'X3DConcreteElement')">
									<xsl:value-of select="$protectedPreamble"/>
									<xsl:text disable-output-escaping="yes"><![CDATA[
	private X3DConcreteElement parentObject = null; // X3D node or statement
										
	/**
	 * Provide object reference to parent X3D node or statement, if any.
	 * This reference is named "parentObject" rather than "parent" to avoid potential name collision with any X3D field named "parent".
	 * @return object reference to parent X3D node or statement, otherwise null if none
	 */			
	public X3DConcreteElement getParentObject()
	{
		return parentObject;
	}
										
	/**
	 * Package-internal method to set parent object reference.
	 * @param newParentObject object reference to parent node or X3D statement that contains this node
	 */			
	public void setParentObject(X3DConcreteElement newParentObject)
	{
		parentObject = newParentObject;
	}
										
	/**
	 * Package-protected internal method to clear parent object reference, if any.
	 */			
	public void clearParentObject()
	{
		setParentObject(null);
	}

	/**
	 * Find object reference to ancestor Scene element, if this node or statement is part of an SceneObject scene graph.
	 * @return ancestor Scene reference if attached, otherwise null
	 */
	public SceneObject getAncestorSceneObject()
	{
		if ((this instanceof X3DNode) && ((X3DNode)this) instanceof SceneObject)
			return (SceneObject)((X3DNode)this);
		X3DConcreteElement element = this.getParentObject();
		while (element != null)
		{
			if (element instanceof SceneObject)
				 return (SceneObject)element;
			else element = ((X3DConcreteElement)element).getParentObject(); // walk up the tree
		}
		return null; // not found
	}
	/**
	 * Find object reference to ancestor X3D element, if this node or statement is part of an X3DObject model.
	 * @return ancestor X3D reference if attached, otherwise null
	 */	
	public X3DObject getAncestorX3DObject()
	{
		if (((X3DNode)this) instanceof X3DObject)
			return (X3DObject)((X3DNode)this);
		X3DConcreteElement element = this.getParentObject();
		while (element != null)
		{
			if (element instanceof X3DObject)
				 return (X3DObject)element;
			else element = ((X3DConcreteElement)element).getParentObject(); // walk up the tree
		}
		return null; // not found
	}

	/** Provides name of this element.
	 * @return name of this element
	 */
	abstract public String getElementName(); // must be overridden

	/** Indicate type corresponding to field name.
	 * @param fieldName name of field in this X3D statement
	 * @return X3D type (SFvec3f etc.), otherwise UnknownField_fieldName if not recognized
	 */			
	abstract public String getType(String fieldName); // must be overridden
										
	/** Indicate accessType corresponding to field name.
	 * @param fieldName name of field in this X3D statement
	 * @return X3D accessType (inputOnly etc.), otherwise UnknownField_fieldName if not recognized
	 */			
	abstract public String getAccessType(String fieldName); // must be overridden
										
	/**
	 * Recursive method to provide object reference to node or statement by name, if found as this element or in a contained
element.
	 * Elements of interest: ProtoDeclare/ExternProtoDeclare/ProtoInstance, field/fieldValue, H-Anim nodes
	 * @param elementName name of element to find
	 * @return object reference to element
	 */		
	abstract public X3DConcreteElement getElementByName(String elementName); // required interface
]]></xsl:text>
								</xsl:when>
								<xsl:when test="($name = 'X3DConcreteNode')">
									<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Recursive method to provide object reference to node by DEF name, found either as this node or in a contained node (if any).
	 * @param DEFname DEF name of node to find
	 * @return object reference to node
	 */
	abstract public X3DConcreteNode getNodeByDEF(String DEFname); // required interface
]]></xsl:text>
								</xsl:when>
							</xsl:choose>
						</xsl:when>
					</xsl:choose>
					<!-- ===================================================== -->
					<!-- Source code: accessor methods -->

					<xsl:for-each select="InterfaceDefinition/field[not(starts-with(@name,'set'))]"> <!-- TODO check filtering is consistently effective -->

						<xsl:if test="position()=1">
							<xsl:text>&#10;</xsl:text>
							<xsl:text>	// ==== Accessor methods: strongly typed get/set methods for compile-time strictness ====</xsl:text>
							<xsl:text>&#10;</xsl:text>
							<xsl:text>&#10;</xsl:text>
						</xsl:if>
						<xsl:variable name="isX3dStatement">
							<xsl:call-template name="isX3dStatement">
								<xsl:with-param name="name" select="@name"/>
							</xsl:call-template>
						</xsl:variable>
						<xsl:variable name="isX3dStatement">
							<xsl:call-template name="isX3dStatement">
								<xsl:with-param name="name" select="@name"/>
							</xsl:call-template>
						</xsl:variable>
						<!-- TODO why are duplicate field definitions in X3D Object Model? likely due to duplicate entries in appinfo and content model, e.g. LOD, ParticleSystems-->
						<xsl:variable name="fieldName" select="@name"/>

						<!-- avoid duplicates, avoid statement accessors for interfaces -->
						<xsl:if test="not(preceding-sibling::*[@name = $fieldName]) and not(($isInterface = 'true') and ($isX3dStatement = 'true'))">
							<xsl:variable name="javaType">
								<xsl:call-template name="javaType">
									<xsl:with-param name="x3dType" select="@type"/>
									<xsl:with-param name="isInterface" select="$isInterface"/>
								</xsl:call-template>
							</xsl:variable>
							<xsl:variable name="javaPrimitiveType">
								<xsl:call-template name="javaType">
									<xsl:with-param name="x3dType" select="@type"/>
									<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
								</xsl:call-template>
							</xsl:variable>
							<xsl:variable name="javaReferenceType">
								<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
							</xsl:variable>
							<xsl:variable name="isArrayType">
								<!-- TODO remove restrictions when ArrayList types added -->
								<xsl:value-of select="starts-with(@type,'MF') and not(contains(@type,'Color') or contains(@type,'Vec') or contains(@type,'Rotation') or contains(@type,'Matrix')) and contains($javaType,'[]')"/>
							</xsl:variable>
							<xsl:variable name="isArrayListType">
								<xsl:value-of select="contains($javaType,'&lt;')"/>
							</xsl:variable>
							<xsl:variable name="tooltipText">
								<xsl:value-of select="$x3d.tooltips.document//element[@name = $name]/attribute[@name = $fieldName]/@tooltip" disable-output-escaping="yes"/>
							</xsl:variable>
							<xsl:variable name="fieldTooltip">
								<xsl:if test="(string-length(normalize-space($tooltipText)) > 0)"><!-- doc-available($x3d.tooltips.path) -->
									<xsl:value-of select="replace($tooltipText,'&#8734;','infinity')" disable-output-escaping="yes"/>
									<!-- consistent javadoc punctuation -->
									<xsl:if test="not(ends-with(normalize-space($tooltipText),'.'))">
										<xsl:text>.</xsl:text>
									</xsl:if>
								</xsl:if>
							</xsl:variable>
							<xsl:variable name="x3dType" select="@name"/>

							<!-- javadoc from BuildSpecificationLanguageBindingJava.xslt-->
							<xsl:variable name="type">
								<xsl:value-of select="@type"/>
							</xsl:variable>
							<xsl:variable name="isEnumerationType" select="false()"/>
							<xsl:variable name="tupleNess">
								<xsl:choose>
									<xsl:when test="contains($type,'FVec2')">
										<xsl:text>2-tuple </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'FVec3') or ends-with($type,'FColor') or (@baseType='boundingBoxSizeType')">
										<xsl:text>3-tuple </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'FVec4') or ends-with($type,'FRotation') or contains($type,'FColorRGBA')">
										<xsl:text>4-tuple </xsl:text>
									</xsl:when>
									<xsl:when test="starts-with($type,'MF')">
										<!-- <xsl:text>1-tuple </xsl:text> -->
									</xsl:when>
								</xsl:choose>
							</xsl:variable>

<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
	<xsl:text>*** @name=</xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:text>, $type=</xsl:text>
	<xsl:value-of select="$type"/>
	<xsl:text>, $tupleNess=</xsl:text>
	<xsl:value-of select="$tupleNess"/>
</xsl:message>
</xsl:if>

							<xsl:variable name="enumerationValues">
								<xsl:for-each select="enumeration">
									<xsl:text>"</xsl:text>
									<xsl:value-of select="@value"/>
									<xsl:text>"</xsl:text>
									<xsl:if test="not(position() = last())">
										<xsl:text>|</xsl:text>
									</xsl:if>
								</xsl:for-each>
							</xsl:variable>
							<xsl:variable name="CamelCaseName"><!-- upper camel case -->
								<xsl:choose>
									<xsl:when test="starts-with(@name,'set_')">
										<xsl:value-of select="translate(substring(substring-after(@name,'set_'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
										<xsl:value-of select="substring(substring-after(@name,'set_'),2)"/>
									</xsl:when>
									<xsl:when test="starts-with(@name,'set')">
										<xsl:value-of select="translate(substring(substring-after(@name,'set'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
										<xsl:value-of select="substring(substring-after(@name,'set'),2)"/>
									</xsl:when>
									<xsl:when test="contains(@name,'_changed')">
										<xsl:value-of select="translate(substring(substring-before(@name,'_changed'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
										<xsl:value-of select="substring(substring-before(@name,'_changed'),2)"/>
									</xsl:when>
									<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
										<!-- unmodified -->
										<xsl:value-of select="@name"/>
									</xsl:when>
									<xsl:when test="(@name = 'class')">
										<!-- getClass() is reserved by Java Object() class -->
										<xsl:text>CssClass</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="translate(substring(@name,1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
										<xsl:value-of select="substring(@name,2)"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>
							<xsl:variable name="memberObjectName"><!-- lower camel case, usually -->
								<xsl:choose>
									<xsl:when test="($isX3dStatement = 'true')">
										<xsl:value-of select="@name"/>
									</xsl:when>
									<xsl:when test="(@name = 'AS')"><!-- special case: IMPORT, EXPORT -->
										<xsl:value-of select="@name"/>
									</xsl:when>
									<xsl:when test="(@name = 'set_boolean')"> <!-- special case: BooleanFilter, BooleanToggle, IntegerTrigger -->
										<xsl:text>booleanField</xsl:text>
									</xsl:when>
									<xsl:when test="(@name = 'set_boolean')"> <!-- special case: BooleanFilter, BooleanToggle, IntegerTrigger -->
										<xsl:text>booleanField</xsl:text>
									</xsl:when>
									<xsl:when test="starts-with(@name,'set_')">
										<xsl:value-of select="translate(substring(substring-after(@name,'set_'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
										<xsl:value-of select="substring(substring-after(@name,'set_'),2)"/>
									</xsl:when>
									<xsl:when test="starts-with(@name,'set')">
										<xsl:value-of select="translate(substring(substring-after(@name,'set'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
										<xsl:value-of select="substring(substring-after(@name,'set'),2)"/>
									</xsl:when>
									<xsl:when test="contains(@name,'_changed')">
										<xsl:value-of select="translate(substring(substring-before(@name,'_changed'),1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
										<xsl:value-of select="substring(substring-before(@name,'_changed'),2)"/>
									</xsl:when>
									<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
										<!-- unmodified -->
										<xsl:value-of select="@name"/>
									</xsl:when>
									<xsl:when test="(@name = 'class')">
										<!-- getClass() is reserved by Java Object() class -->
										<xsl:text>cssClass</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="translate(substring($CamelCaseName,1,1),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')"/>
										<xsl:value-of select="substring($CamelCaseName,2)"/>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:variable>
							<xsl:variable name="normalizedMemberObjectName">
								<!-- translate name into legal Java form here to avoid xpath problems -->
								<xsl:value-of select="translate($memberObjectName,'-','_')"/>
								<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
									<xsl:text>List</xsl:text><!-- append to member name -->
								</xsl:if>
							</xsl:variable>

							<!-- TODO create Javadoc matching spec, including reference to contains(@acceptableNodeTypes,'|') -->

							<!-- Source code: provide accessor methods according to accessType ========================= -->

							<!-- get method -->
							<xsl:if test="((@accessType='outputOnly') or (@accessType='initializeOnly') or (@accessType='inputOutput') or (string-length(@accessType) = 0))
										  and ((@name = 'address') or (not(starts-with(@name,'add')) 
										  and not(starts-with(@name,'remove'))
										  and not((@name = 'DEF') or (@name = 'USE') or (@name = 'class'))))">
								<!-- javadoc from BuildSpecificationLanguageBindingJava.xslt-->
								<xsl:text>	/**</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 * Provide </xsl:text>
	<xsl:if test="($debug = 'true')">
	<xsl:text>($javaType=</xsl:text>
	<xsl:value-of select="$javaType"/>
	<xsl:text>, isArrayType=</xsl:text>
	<xsl:value-of select="$isArrayType"/>
	<xsl:text>, isArrayListType=</xsl:text>
	<xsl:value-of select="$isArrayListType"/>
	<xsl:text>, javaPrimitiveType=</xsl:text>
	<xsl:value-of select="$javaPrimitiveType"/>
	<xsl:text>, javaReferenceType=</xsl:text>
	<xsl:value-of select="$javaReferenceType"/>
	<xsl:text>, isX3dStatement=</xsl:text>
	<xsl:value-of select="$isX3dStatement"/>
	<xsl:text>, isClassX3dStatement=</xsl:text>
	<xsl:value-of select="$isClassX3dStatement"/>
	<xsl:text>) </xsl:text>
	</xsl:if>
								<xsl:choose>
									<xsl:when test="contains($javaType,'[]')"><!-- array -->
										<xsl:text>array of </xsl:text>
										<xsl:value-of select="$tupleNess"/>
										<xsl:value-of select="substring-before($javaType,'[]')"/>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:text> results </xsl:text>
									</xsl:when>
									<xsl:when test="($isArrayListType = 'true')"><!-- boxed type such as ArrayList<String> -->
										<xsl:text>array of </xsl:text>
										<xsl:value-of select="$tupleNess"/>
										<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:text> results </xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="$tupleNess"/>
										<xsl:choose>
											<xsl:when test="($name = 'ProtoBody') and (@name = 'children')">
												<xsl:text disable-output-escaping="yes"><![CDATA[ArrayList<X3DNode>]]></xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="$javaType" disable-output-escaping="yes"/><!-- append to type name -->
												<xsl:if test="($isX3dStatement = 'true') and starts-with(@type,'X3D') and (ends-with(@type,'Node') or ends-with(@type,'Object'))">
													<xsl:value-of select="$jsaiInterfaceSuffix"/>
												</xsl:if>
											</xsl:otherwise>
										</xsl:choose>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:choose>
											<xsl:when test="(ends-with(@type,'FNode'))">
												<xsl:text> instance </xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:text> value </xsl:text>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:otherwise>
								</xsl:choose>
								<!-- value restrictions, if any -->
								<xsl:choose>
									<xsl:when test="contains($type,'RGBA')">
										<xsl:text>using RGBA values [0..1] </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'Color')">
										<xsl:text>using RGB values [0..1] </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'otation') or contains(@name,'otation') or contains(@name,'angle') or contains(@name,'Angle')">
										<xsl:text>in radians </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'Time')">
										<xsl:text>in seconds </xsl:text>
									</xsl:when>
									<xsl:when test="($type='SFNode')">
										<xsl:text>(using a properly typed node or X3DPrototypeInstance) </xsl:text>
									</xsl:when>
									<xsl:when test="($type='MFNode')">
										<xsl:text>(using a properly typed node array or X3DPrototypeInstance array) </xsl:text>
									</xsl:when>
								</xsl:choose>
								<xsl:call-template name="list-restrictions"/>

								<xsl:text>from </xsl:text>
								<xsl:value-of select="@accessType"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="@type"/>
								<xsl:text> field </xsl:text>
								<xsl:if test="not(ends-with(@type,'FNode'))">
									<xsl:text>named </xsl:text>
								</xsl:if>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:value-of select="@name"/>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:text>.</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:if test="(string-length($fieldTooltip) > 0)">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;i&gt;Tooltip&lt;/i&gt;. </xsl:text>
									<xsl:value-of select="normalize-space(substring-after($fieldTooltip,']'))" disable-output-escaping="no"/>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:if test="((@type='SFString') or (@type='MFString')) and (enumeration) and not($isInterface = 'true')">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Available enumeration values for string comparison: </xsl:text>
									<xsl:for-each select="enumeration">
										<xsl:if test="position() > 1">
											<xsl:text>, </xsl:text>
										</xsl:if>
										<xsl:text>{@link </xsl:text>
										<xsl:text>#</xsl:text>
										<xsl:value-of select="upper-case(../@name)"/>
										<xsl:text>_</xsl:text>
										<!-- enumeration name: omit " character, others become _ underscore -->
										<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
										<xsl:text> </xsl:text>
										<!-- enumeration name: omit " character, others become _ underscore -->
										<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
										<xsl:text>}</xsl:text>
									</xsl:for-each>
									<xsl:text>.</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:if test="(@type = 'MFNode') and (contains(@acceptableNodeTypes,'|'))">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text> Warning: acceptable node types are limited to </xsl:text>
									<xsl:value-of select="@acceptableNodeTypes"/>
									<xsl:text>.</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:text>	 * @return value of </xsl:text>
								<xsl:value-of select="@name"/>
								<xsl:if test="(@name != 'field')">
									<xsl:text> field</xsl:text>
								</xsl:if>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 */</xsl:text><!-- end javadoc -->
								<xsl:text>&#10;</xsl:text>
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:text>// ($isInterface=</xsl:text>
<xsl:value-of select="$isInterface"/>
<xsl:text>, $isException=</xsl:text>
<xsl:value-of select="$isException"/>
<xsl:text>, $isServiceInterface=</xsl:text>
<xsl:value-of select="$isServiceInterface"/>
<xsl:text>, $isX3dStatement=</xsl:text>
<xsl:value-of select="$isX3dStatement"/>
<xsl:text>, $isClassX3dStatement=</xsl:text>
<xsl:value-of select="$isClassX3dStatement"/>
<xsl:text>, preceding-sibling::Inheritance=</xsl:text>
<xsl:value-of select="preceding-sibling::Inheritance"/>
<xsl:text>, $baseType=</xsl:text>
<xsl:value-of select="$baseType"/>
<xsl:text>, $additionalInheritanceBaseType=</xsl:text>
<xsl:value-of select="$additionalInheritanceBaseType"/>
<xsl:text>)</xsl:text>
<xsl:text>&#10;</xsl:text>
</xsl:if>
								<!-- source code: get method -->
								<xsl:if test="(not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')) or
												 (($isInterface = 'true') and //AbstractNodeType  [@name = $baseType                     ]/InterfaceDefinition/field[@name = $fieldName]) or
												 (($isInterface = 'true') and //AbstractNodeType  [@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName]) or
												 (($isInterface = 'true') and //AbstractObjectType[@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName])">
									<xsl:text>	@Override</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:text>	public </xsl:text>
								<xsl:choose>
									<!--
									<xsl:when test="($name = 'ProtoBody') and (@name = 'children')">
										<xsl:text disable-output-escaping="yes"><![CDATA[ArrayList<X3DNode>]]></xsl:text>
									</xsl:when>
									-->
									<xsl:when test="(@type = 'MFNode') and (($isClassX3dStatement = 'true') or ($isX3dStatement = 'true') or (@name = 'addChildren') or (@name = 'removeChildren'))">
										<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="$javaPrimitiveType"/>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:text> get</xsl:text>
								<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
								<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
									<xsl:text>List</xsl:text><!-- append to member name -->
								</xsl:if>
								<xsl:text>()</xsl:text>
								<xsl:choose>
									<xsl:when test="($isInterface = 'true')">
										<xsl:text>;</xsl:text>
										<xsl:if test="contains(@acceptableNodeTypes,'|')">
											<xsl:text> // acceptable node types: </xsl:text>
											<xsl:value-of select="@acceptableNodeTypes"/>
										</xsl:if>
										<xsl:text>&#10;</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	{</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:choose>
											<!-- check if SFNode subtype cast necessary -->
											<xsl:when test="(@type = 'SFNode') and not($javaPrimitiveType = $javaType) and not($isX3dStatement = 'true')">
												<xsl:text>		return (</xsl:text>
												<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
												<xsl:text>)</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
											</xsl:when>
											<xsl:when test="(@type = 'MFNode') and (($isX3dStatement = 'true') or ($isClassX3dStatement = 'true'))">
												<xsl:text>		return </xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
											</xsl:when>
											<xsl:when test="not($isX3dStatement = 'true') and
															((($isArrayListType = 'true') and contains($javaType,'ArrayList')) or
															 ((@type = 'MFNode') and not(starts-with($javaPrimitiveType, $javaReferenceType)) and not($isClassX3dStatement = 'true')))">
												<xsl:text>		final </xsl:text>
												<xsl:choose>
													<xsl:when test="($isX3dStatement = 'true')">
														<xsl:value-of select="@name"/>
														<xsl:value-of select="$jsaiClassSuffix"/>
														<xsl:if test="(@type='MFNode')">
															<xsl:text>[]</xsl:text>
														</xsl:if>
													</xsl:when>
													<xsl:otherwise>
														<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
													</xsl:otherwise>
												</xsl:choose>
												<xsl:text> valuesArray = new </xsl:text>
												<xsl:choose>
													<xsl:when test="($isX3dStatement = 'true')">
														<xsl:value-of select="$normalizedMemberObjectName"/>
													</xsl:when>
													<xsl:otherwise>
														<xsl:value-of select="substring-before($javaPrimitiveType,'[')"/>
													</xsl:otherwise>
												</xsl:choose>
												<xsl:text>[</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>.size()];</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		int i = 0;</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		for (</xsl:text>
												<xsl:value-of select="$javaReferenceType"/>
												<xsl:text> arrayElement : </xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>) {</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			valuesArray[i++] = </xsl:text>
												<xsl:if test="(@type = 'MFNode') and not($javaPrimitiveType = $javaType) and not(starts-with($javaPrimitiveType, $javaReferenceType)) and not($isX3dStatement = 'true')">
													<!-- cast -->
													<xsl:text>(</xsl:text>
													<xsl:value-of select="substring-before($javaPrimitiveType,'[')" disable-output-escaping="yes"/>
													<xsl:text>)</xsl:text>
												</xsl:if>
												<xsl:text>arrayElement;</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		}</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		return valuesArray</xsl:text>
												<!--
												final boolean[] primitives = new boolean[booleanList.size()];
												for (Boolean object : booleanList) {
													primitives[i++] = object;
												}
												return primitives;
												-->
												<!-- http://docs.oracle.com/javase/8/docs/api/java/util/List.html#toArray -->
												<!-- http://stackoverflow.com/questions/5615664/coverting-a-boolean-object-array-to-boolean-primitive-array -->
											</xsl:when>
											<xsl:otherwise>
												<xsl:text>		return </xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
											</xsl:otherwise>
										</xsl:choose>
										<xsl:text>;</xsl:text>
										<xsl:text>&#10;</xsl:text>

										<xsl:text>	}</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:otherwise>
								</xsl:choose>

								<xsl:if test="((@type='MFNode') or (@type='MFString') or (@type='MFBool') or (@type = 'MFInt32') or (@type = 'SFImage') or (@type = 'MFImage') or (@type = 'MFBool') or (@type = 'MFInt32') or (@type = 'SFImage') or (@type = 'MFImage') or (@type='MFFloat') or (@type='MFDouble') or (@type='MFTime'))
											   and not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to get ArrayList </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value of </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field, similar to {@link #get</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>()} </xsl:text>
									<xsl:text>&#10;</xsl:text>
									<!-- TODO
									<xsl:text> * @see java.util.ArrayList</xsl:text>
									<xsl:text>&#10;</xsl:text>
									-->
									<xsl:text>	 * @return value of </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:if test="(@name != 'field')">
										<xsl:text> field</xsl:text>
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public </xsl:text>
									<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
									<xsl:text> get</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>List()</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		return </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text>;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<!-- end of get accessors -->
							</xsl:if>

							<!-- javadoc: set method accessor(s) -->
							<xsl:if test="((@accessType='inputOnly') or (@accessType='initializeOnly') or (@accessType='inputOutput') or (string-length(@accessType) = 0))
										  and (((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove')))">
								<!-- javadoc from BuildSpecificationLanguageBindingJava.xslt-->
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	/**</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 * Assign </xsl:text>
	<xsl:if test="($debug = 'true')">
	<xsl:text>($javaType=</xsl:text>
	<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
	<xsl:text>, isArrayType=</xsl:text>
	<xsl:value-of select="$isArrayType"/>
	<xsl:text>, isArrayListType=</xsl:text>
	<xsl:value-of select="$isArrayListType"/>
	<xsl:text>, javaPrimitiveType=</xsl:text>
	<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
	<xsl:text>, javaReferenceType=</xsl:text>
	<xsl:value-of select="$javaReferenceType" disable-output-escaping="yes"/>
	<xsl:text>, isX3dStatement=</xsl:text>
	<xsl:value-of select="$isX3dStatement"/>
	<xsl:text>, isClassX3dStatement=</xsl:text>
	<xsl:value-of select="$isClassX3dStatement"/>
	<xsl:text>) </xsl:text>
	</xsl:if>
								<xsl:value-of select="$tupleNess"/>
								<xsl:choose>
									<xsl:when test="contains($javaType,'[]')">
										<xsl:value-of select="substring-before($javaType,'[]')"/>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:text> array </xsl:text>
									</xsl:when>
									<xsl:when test="($isArrayListType = 'true')"><!-- boxed type such as ArrayList<String> -->
										<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:text> array </xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
										<xsl:if test="$isEnumerationType">
											<xsl:text> enumeration</xsl:text>
										</xsl:if>
										<xsl:choose>
											<xsl:when test="(ends-with(@type,'FNode'))">
												<xsl:text> instance </xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:text> value </xsl:text>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:otherwise>
								</xsl:choose>
								<!-- value restrictions, if any -->
								<xsl:choose>
									<xsl:when test="(@name = 'GeoOrigin') or (@name = 'geoOrigin')">
										<xsl:text>(deprecated node, optional) </xsl:text>
									</xsl:when>
									<xsl:when test="$isEnumerationType">
										<xsl:text>(</xsl:text>
										<xsl:value-of select="$enumerationValues"/>
										<xsl:text>) </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'RGBA')">
										<xsl:text>using RGBA values [0..1] </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'Color')">
										<xsl:text>using RGB values [0..1] </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'otation') or contains(@name,'otation') or contains(@name,'angle') or contains(@name,'Angle')">
										<xsl:text>in radians </xsl:text>
									</xsl:when>
									<xsl:when test="contains($type,'Time')">
										<xsl:text>in seconds </xsl:text>
									</xsl:when>
									<xsl:when test="($type='SFNode')">
										<xsl:text>(using a properly typed node) </xsl:text>
									</xsl:when>
									<xsl:when test="($type='MFNode')">
										<xsl:text>(using a properly typed node array) </xsl:text>
									</xsl:when>
								</xsl:choose>
								<xsl:call-template name="list-restrictions"/>
								<xsl:text>to </xsl:text>
								<xsl:value-of select="@accessType"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="@type"/>
								<xsl:text> field </xsl:text>
								<xsl:if test="not(ends-with(@type,'FNode'))">
									<xsl:text>named </xsl:text>
								</xsl:if>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:value-of select="@name"/>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:if test="((@type='SFString') or (@type='MFString')) and (enumeration) and not($isInterface = 'true')">
									<xsl:choose>
										<xsl:when test="not(@additionalEnumerationValuesAllowed='true')">
											<xsl:text>.</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	 * </xsl:text>
											<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
											<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	 * Warning: authors can only choose from a strict list of enumeration values </xsl:text>
										</xsl:when>
										<xsl:when test="   (@additionalEnumerationValuesAllowed='true')">
											<xsl:text>.</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	 * </xsl:text>
											<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
											<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	 * Hint: authors have option to choose from an extendible list of predefined enumeration values </xsl:text>
										</xsl:when>
									</xsl:choose>
									<xsl:text>(</xsl:text>
									<xsl:for-each select="enumeration">
										<xsl:if test="position() > 1">
											<xsl:text>, </xsl:text>
										</xsl:if>
										<xsl:text>{@link </xsl:text>
										<xsl:text>#</xsl:text>
										<xsl:value-of select="upper-case(../@name)"/>
										<xsl:text>_</xsl:text>
										<!-- enumeration name: omit " character, others become _ underscore -->
										<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
										<xsl:text> </xsl:text>
										<!-- enumeration name: omit " character, others become _ underscore -->
										<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
										<xsl:text>}</xsl:text>
									</xsl:for-each>
									<xsl:text>)</xsl:text>
								</xsl:if>
								<xsl:text>.</xsl:text>

								<xsl:text>&#10;</xsl:text>
								<xsl:if test="(string-length($fieldTooltip) > 0)">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;i&gt;Tooltip&lt;/i&gt;. </xsl:text>
									<!-- TODO recurse to insert line breaks for each Hint: -->
									<!-- TODO regular expression to insert links for url text -->
									<xsl:value-of select="normalize-space(substring-after($fieldTooltip,']'))" disable-output-escaping="no"/>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:choose>
									<xsl:when test="(@name = 'DEF')">
										<xsl:text>	 * </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
										<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	 * </xsl:text>
										<xsl:text> Note that setting the DEF value clears the USE value.</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:when>
									<xsl:when test="(@name = 'USE')">
										<xsl:text>	 * </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
										<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	 * </xsl:text>
										<xsl:text> Note that setting the USE value resets all other fields to their default values.</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:when>
								</xsl:choose>
								<xsl:if test="(@type = 'MFNode') and (contains(@acceptableNodeTypes,'|'))">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text> Warning: acceptable node types are limited to </xsl:text>
									<xsl:value-of select="@acceptableNodeTypes"/>
									<xsl:text>.</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:if test="(@name = 'name') and (($name = 'component') or ($name = 'meta') or ($name = 'unit') or starts-with($name, 'field') or starts-with($name, 'CAD') or starts-with($name, 'HAnim') or contains($name, 'Proto'))">
									<xsl:text>	 * </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
									<xsl:text disable-output-escaping="yes"><![CDATA[@see <a href="http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#NamingConventions">X3D Scene Authoring Hints: Naming Conventions</a>]]></xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:text>	 * @param </xsl:text>
								<xsl:value-of select="$newValue"/>
								<xsl:text> is new value for the </xsl:text>
								<xsl:value-of select="@name"/>
								<xsl:text> field.</xsl:text>
								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 * @return {@link </xsl:text>
								<xsl:value-of select="$thisClassName"/>
								<xsl:text>} - namely </xsl:text>
								<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
								<xsl:text>this</xsl:text>
								<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
								<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
								<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
								<!-- http://parlab.eecs.berkeley.edu/wiki/_media/patterns
								     http://parlab.eecs.berkeley.edu/wiki/_media/patterns/pipeline-v1.pdf -->
								<!-- http://commons.apache.org/sandbox/commons-pipeline/pipeline_basics.html -->

								<xsl:text>&#10;</xsl:text>
								<xsl:text>	 */</xsl:text><!-- end javadoc -->
								<xsl:text>&#10;</xsl:text>
								<xsl:variable name="newValueNullExceptionCheck">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> == null)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
									<xsl:text>("</xsl:text>
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="substring-before($javaPrimitiveType,'[]')"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is null and cannot be set"); // newValueNullExceptionCheck</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>
								<xsl:variable name="newValueNullClearsFieldReturnThis">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> == null)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			</xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:if test="($isX3dStatement = 'true') and not(@name = 'children')">
										<xsl:text>List</xsl:text>
									</xsl:if>
									<xsl:text>.clear(); // newValueNullClearsFieldReturnThis</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			return</xsl:text>
									<xsl:if test="not(@name = 'children')">
										<xsl:text> this</xsl:text>
									</xsl:if>
									<xsl:text>;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>
								<xsl:variable name="newValueNullClearsFieldReturnVoid">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> == null)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			</xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:if test="($isX3dStatement = 'true') and not(@name = 'children')">
										<xsl:text>List</xsl:text>
									</xsl:if>
									<xsl:text>.clear(); // newValueNullClearsFieldReturnVoid</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			return;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>
								<xsl:variable name="newValueNullReturnVoid">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> == null) return; // newValueNullReturnVoid</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>
								<xsl:variable name="newValueNullReturnThis">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> == null) return this</xsl:text>
									<xsl:text>; // newValueNullReturnThis</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>
								<xsl:variable name="newProtoInstanceNodeNullReturnThis">
									<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
									<xsl:text>		if (newProtoInstanceNode == null) return this</xsl:text>
									<xsl:text>; // newProtoInstanceNodeNullReturnThis</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:variable>

								<!-- source code: set method -->
								<xsl:if test="(not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')) or
												 (($isInterface = 'true') and //AbstractNodeType  [@name = $baseType                     ]/InterfaceDefinition/field[@name = $fieldName]) or
												 (($isInterface = 'true') and //AbstractNodeType  [@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName]) or
												 (($isInterface = 'true') and //AbstractObjectType[@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName])">
									<xsl:text>	@Override</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								<xsl:text>	public </xsl:text>
								<xsl:value-of select="$thisClassName"/>
								<xsl:text> </xsl:text>
								<xsl:choose>
									<xsl:when test="(@name = 'addChildren') or (@name = 'removeChildren')">
										<!-- no change in corresponding method name -->
										<xsl:value-of select="@name"/>
										<!-- TODO update javadoc descriptions accordingly -->
										<!-- TODO SFNode utility methods corresponding to MFNode methods -->
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>set</xsl:text>
										<xsl:choose>
											<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
												<!-- unmodified -->
												<xsl:value-of select="@name"/>
											</xsl:when>
											<xsl:when test="(@name = 'class')">
												<!-- getClass() is reserved by Java Object() class -->
												<xsl:text>CssClass</xsl:text>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
											</xsl:otherwise>
										</xsl:choose>
										<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
											<xsl:text>List</xsl:text><!-- append to member name -->
										</xsl:if>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:text>(</xsl:text>
								<xsl:choose>
									<xsl:when test="(@type = 'MFNode') and (($isClassX3dStatement = 'true') or ($isX3dStatement = 'true') or (@name = 'addChildren') or (@name = 'removeChildren'))">
										<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
									</xsl:when>
									<xsl:otherwise>
										<xsl:value-of select="$javaPrimitiveType"/>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:text> </xsl:text>
								<xsl:value-of select="$newValue"/>
								<xsl:text>)</xsl:text>
								<xsl:choose>
									<xsl:when test="($isInterface = 'true')">
										<xsl:text>;</xsl:text>
										<xsl:if test="contains(@acceptableNodeTypes,'|')">
											<xsl:text> // acceptable node types: </xsl:text>
											<xsl:value-of select="@acceptableNodeTypes"/>
										</xsl:if>
										<xsl:text>&#10;</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	{</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:call-template name="set-newValue-validity-checks">
											<xsl:with-param name="canThrowFieldValueException"><xsl:value-of select="$canThrowFieldValueException"/></xsl:with-param>
											<xsl:with-param name="isArrayType"      ><xsl:value-of select="$isArrayType"/></xsl:with-param>
											<xsl:with-param name="isArrayListType"  ><xsl:value-of select="$isArrayListType"/></xsl:with-param>
											<xsl:with-param name="x3dType"          ><xsl:value-of select="@type"/></xsl:with-param>
											<xsl:with-param name="comparisonType"   ><xsl:text></xsl:text>simple</xsl:with-param>
										</xsl:call-template>
										<xsl:if test="(($name = 'field') or ($name = 'fieldValue')) and (@name = 'value')">
													<xsl:text disable-output-escaping="yes"><![CDATA[		// check for legal type
		if (getType().equals("SFNode") || getType().equals("MFNode"))
		{
			throw new InvalidProtoException("field name='" + getName() + "' with type='" + getType() +
					"' cannot have any simple-type value (newValue='" + newValue + "').  Use setChildren() method instead.");
		}
]]></xsl:text>
										</xsl:if>
										<xsl:choose>
											<xsl:when test="(@name = 'DEF')">
												<xsl:text>		setConcreteUSE(""); // ensure that no previous USE value remains</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		setConcreteDEF(</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>); // private superclass methods</xsl:text>
											</xsl:when>
											<xsl:when test="(@name = 'USE')">
												<xsl:text>		initialize(); // reset all other field values to default (equivalent to empty)</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		setConcreteUSE(</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>); // private superclass method</xsl:text>
											</xsl:when>
											<xsl:when test="(@name = 'class')">
												<xsl:text>		setConcreteCssClass(</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>); // private superclass method</xsl:text>
											</xsl:when>
											<!-- http://stackoverflow.com/questions/10530353/convert-string-array-to-arraylist -->
											<xsl:when test="(@type = 'SFNode') and not($javaPrimitiveType = $javaType) and not($isX3dStatement = 'true')">
												<xsl:value-of select="$newValueNullReturnThis"/>
												<!-- SFNode subtype checks necessary -->
												<xsl:text>	if (</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text> instanceof </xsl:text>
												<xsl:value-of select="$javaType"/>
												<xsl:text>)</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>	{</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>       </xsl:text>
												<xsl:value-of select="@name"/>
												<xsl:text> = </xsl:text>
												<xsl:text>(</xsl:text>
												<xsl:value-of select="$javaType"/>
												<xsl:text>)</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>;</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>       ((X3DConcreteElement) </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>).setParentObject(this);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>	}</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>	else throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
												<xsl:text>("</xsl:text>
												<xsl:value-of select="$javaPrimitiveType"/>
												<xsl:text> </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>=(</xsl:text>
					<xsl:value-of select="$x3dType"/>
					<xsl:value-of select="$jsaiClassSuffix"/>
					<xsl:text>.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
												<xsl:text>) is not instanceof </xsl:text>
												<xsl:value-of select="$javaType"/>
												<xsl:text>; </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>=" + </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>);</xsl:text>
											</xsl:when>
											<xsl:when test="(@type = 'MFNode') and (($isX3dStatement = 'true') or ($isClassX3dStatement = 'true'))">
												<xsl:if test="($name = 'ProtoBody')">
													<xsl:text>		if (primaryNode != null)
		{
			primaryNode.setParentObject(null);
		    primaryNode = null;
		}
</xsl:text>
												</xsl:if>
												<xsl:text>		</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text> = </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>;</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		for (</xsl:text>
												<xsl:value-of select="$javaReferenceType"/>
												<xsl:text> arrayElement : </xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>)</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		{</xsl:text>
												<xsl:if test="($name = 'ProtoBody')">
													<xsl:text disable-output-escaping="yes"><![CDATA[
			if ((primaryNode == null) && (arrayElement instanceof X3DConcreteNode))
			{
				primaryNode = (X3DConcreteNode) arrayElement; // remember node type
				primaryNode.setParentObject(this);
			}
]]></xsl:text>	
												</xsl:if>
												<!--special set method validation checks -->
												<xsl:choose>
													<xsl:when test="($name = 'ExternProtoDeclare') and (@name = 'field')">
		<!-- check to ensure that no value is present within field having parent ExternProtoDeclare -->
		<xsl:text disable-output-escaping="yes"><![CDATA[			// No value is allowed within field having parent ExternProtoDeclare
			if (!arrayElement.getValue().isEmpty() || !arrayElement.getChildren().isEmpty())
			{
				String foundValue;
				if (!arrayElement.getValue().isEmpty())
					 foundValue = arrayElement.getValue();
				else foundValue = arrayElement.getChildren().toString();
			
				throw new InvalidProtoException("ExternProtoDeclare name='" + name +
					"' with field name='" + arrayElement.getName() +
					"' cannot have any initial value (found \"" + foundValue + 
					"\"). Instead use ProtoInstance fieldValue to override the original default ProtoDeclare field value.");
			}
]]></xsl:text>
													</xsl:when>
												</xsl:choose>
												<xsl:text>			((X3DConcreteElement) arrayElement).setParentObject(this);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		}</xsl:text>
												<xsl:text>&#10;</xsl:text>
											</xsl:when>
											<xsl:when test="(@type = 'MFNode') and not(starts-with($javaType, $javaReferenceType)) and not($isX3dStatement = 'true')">
												<xsl:value-of select="$newValueNullReturnThis"/>
												<xsl:text>		</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>.clear(); // reset</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<!-- MFNode subtype checks necessary -->
												<xsl:text>		for (int i = 0; i </xsl:text>
												<xsl:text disable-output-escaping="yes">&lt; </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>.length; i++) {</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			if  (</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>[i] instanceof </xsl:text>
												<xsl:value-of select="$javaReferenceType"/>
												<xsl:text>)</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			{</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>				</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>.add(</xsl:text>
												<xsl:if test="not($isX3dStatement = 'true')">
													<!-- cast -->
													<xsl:text>(</xsl:text>
													<xsl:value-of select="$javaReferenceType"/>
													<xsl:text>)</xsl:text>
												</xsl:if>
												<xsl:value-of select="$newValue"/>
												<xsl:text>[i]);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:if test="($name = 'ProtoBody') and not($isInterface = 'true')">
													<xsl:text disable-output-escaping="yes"><![CDATA[
			if ((primaryNode == null) && (]]></xsl:text><xsl:value-of select="$newValue"/><xsl:text> instanceof X3DConcreteNode))
			{
				primaryNode = (X3DConcreteNode) </xsl:text><xsl:value-of select="$newValue"/><xsl:text>; // remember node type
				primaryNode.setParentObject(this);
			}
</xsl:text>	
												</xsl:if>
												<xsl:text>				((X3DConcreteElement) </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>[i]).setParentObject(this);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			}</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			else throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
												<xsl:text>("</xsl:text>
												<xsl:value-of select="$javaPrimitiveType"/>
												<xsl:text> </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>["+i+"] is not instanceof </xsl:text>
												<xsl:value-of select="$javaReferenceType"/>
												<xsl:text>; </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>=" + </xsl:text>
												<xsl:text> Arrays.toString(</xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>)</xsl:text>
												<xsl:text>);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		}</xsl:text>
											</xsl:when>
											<xsl:when test="($isArrayListType = 'true') and not($javaReferenceType = 'X3DNode') and not($isX3dStatement = 'true')">
												<xsl:value-of select="$newValueNullReturnThis"/>
												<!-- http://stackoverflow.com/questions/39873596/convert-array-of-strings-to-boolean-list-in-java -->
												<xsl:text>		</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text>.clear(); // reset</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		for (int i = 0; i </xsl:text>
												<xsl:text disable-output-escaping="yes">&lt; </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>.length; i++)</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		{</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:choose>
													<xsl:when test="(@type = 'MFNode') and not(starts-with($javaPrimitiveType, $javaReferenceType))">
														<!-- SFNode subtype checks necessary -->
														<xsl:text>			if (</xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>[i] instanceof </xsl:text>
														<xsl:value-of select="$javaReferenceType"/>
														<xsl:value-of select="$jsaiClassSuffix"/>
														<xsl:text>)</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>			{</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:if test="($name = 'ProtoBody') and not($isInterface = 'true')">
															<xsl:text disable-output-escaping="yes"><![CDATA[
				if ((primaryNode == null) && (]]></xsl:text><xsl:value-of select="$newValue"/><xsl:text> instanceof X3DConcreteNode))
				{
					primaryNode = (X3DConcreteNode) </xsl:text><xsl:value-of select="$newValue"/><xsl:text>[i]; // remember node type
					primaryNode.setParentObject(this);
				}
</xsl:text>	
														</xsl:if>
														<xsl:text>				</xsl:text>
														<xsl:value-of select="@name"/>
														<xsl:text>.add(</xsl:text>
														<xsl:text>(</xsl:text>
														<xsl:value-of select="$javaReferenceType"/>
														<xsl:value-of select="$jsaiClassSuffix"/>
														<xsl:text>)</xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>[i]);</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>       ((X3DConcreteElement) </xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>[i]).setParentObject(this); // apparently unused?</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>			}</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>			else throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
														<xsl:text>("</xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>["+i+"] is not instanceof </xsl:text>
														<xsl:value-of select="$javaReferenceType"/>
														<xsl:value-of select="$jsaiClassSuffix"/>
														<xsl:text>; </xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>=" + </xsl:text>
														<xsl:choose>
															<xsl:when test="starts-with(@type,'MF')">
																<xsl:text> Arrays.toString(</xsl:text>
																<xsl:value-of select="$newValue"/>
																<xsl:text>)</xsl:text>
															</xsl:when>
															<xsl:otherwise>
																<xsl:value-of select="$x3dType"/>
																<xsl:value-of select="$jsaiClassSuffix"/>
																<xsl:text>.toString(</xsl:text>
																<xsl:value-of select="$newValue"/>
																<xsl:text>)</xsl:text>
															</xsl:otherwise>
														</xsl:choose>
														<xsl:text>);</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>		}</xsl:text>
														<xsl:text>&#10;</xsl:text>
													</xsl:when>
													<xsl:otherwise>
														<xsl:text>			</xsl:text>
														<xsl:value-of select="@name"/>
														<xsl:text>.add(</xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>[i]);</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>		}</xsl:text>
														<xsl:text>&#10;</xsl:text>
													</xsl:otherwise>
												</xsl:choose>
											</xsl:when>
											<xsl:otherwise>
												<xsl:text>		</xsl:text>
												<xsl:value-of select="$normalizedMemberObjectName"/>
												<xsl:text> = </xsl:text>
												<xsl:value-of select="$newValue"/>
												<xsl:text>;</xsl:text>
												<!-- set SFNode -->
												<xsl:if test="(@type = 'SFNode')">
													<xsl:text>
		if (</xsl:text><xsl:value-of select="$newValue"/><xsl:text> != null)
		   ((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>).setParentObject(this);</xsl:text>
													<xsl:if test="not($isX3dStatement = 'true')">
														<xsl:text>
		if (</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>ProtoInstance != null) // housekeeping
		{
			</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>ProtoInstance.setParentObject(null);
			</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>ProtoInstance = null;
		}
</xsl:text>
													</xsl:if>
												</xsl:if>
											</xsl:otherwise>
										</xsl:choose>

										<xsl:text>&#10;</xsl:text>
										<xsl:text>		return this;</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	}</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:text>&#10;</xsl:text>

								<!-- additional field utility methods for concrete classes -->

								<xsl:if test="not((@type='SFNode') or (@type='MFNode'))
											   and not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to assign typed object </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value to </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field, similar to {@link #set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
									<xsl:text>)}. </xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new value for the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @return {@link </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text>} - namely </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
									<xsl:text>this</xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
									<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
									<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text> set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$type" disable-output-escaping="yes"/>
									<xsl:value-of select="$jsaiClassSuffix"/>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="($isArrayListType = 'true') and not($javaReferenceType = 'X3DNode') and not($isX3dStatement = 'true')">
										<xsl:value-of select="$newValueNullReturnThis"/>
									</xsl:if>
									<!-- assumption: SF/MF object assignment is OK due to object integrity
									<xsl:call-template name="set-newValue-validity-checks">
										<xsl:with-param name="canThrowFieldValueException"><xsl:value-of select="$canThrowFieldValueException"/></xsl:with-param>
										<xsl:with-param name="isArrayType"      ><xsl:value-of select="$isArrayType"/></xsl:with-param>
										<xsl:with-param name="isArrayListType"  ><xsl:value-of select="$isArrayListType"/></xsl:with-param>
										<xsl:with-param name="x3dType"          ><xsl:value-of select="@type"/></xsl:with-param>
										<xsl:with-param name="javaReferenceType"><xsl:value-of select="$javaReferenceType"/></xsl:with-param>
										<xsl:with-param name="comparisonType"   ><xsl:text>complex</xsl:text></xsl:with-param>
									</xsl:call-template>
									-->
									<xsl:text>		</xsl:text>
									<xsl:text>set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>.getPrimitiveValue()</xsl:text>
									<xsl:text>);</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		return this;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>

								<xsl:if test="((@type='MFNode') or (@type='MFString') or (@type='MFBool') or (@type = 'MFInt32') or (@type = 'SFImage') or (@type = 'MFImage') or (@type='MFFloat') or (@type='MFDouble') or (@type='MFTime'))
											   and not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to assign ArrayList </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value of </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field, similar to {@link #set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
									<xsl:text>)}. </xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new value for the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @return {@link </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text>} - namely </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
									<xsl:text>this</xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
									<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
									<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text> set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$javaType" disable-output-escaping="yes"/>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:value-of select="$newValueNullReturnThis"/>
									<xsl:call-template name="set-newValue-validity-checks">
										<xsl:with-param name="canThrowFieldValueException"><xsl:value-of select="$canThrowFieldValueException"/></xsl:with-param>
										<xsl:with-param name="isArrayType"      ><xsl:value-of select="$isArrayType"/></xsl:with-param>
										<xsl:with-param name="isArrayListType"  ><xsl:value-of select="$isArrayListType"/></xsl:with-param>
										<xsl:with-param name="x3dType"          ><xsl:value-of select="@type"/></xsl:with-param>
										<xsl:with-param name="javaReferenceType"><xsl:value-of select="$javaReferenceType"/></xsl:with-param>
										<xsl:with-param name="comparisonType"   ><xsl:text>complex</xsl:text></xsl:with-param>
									</xsl:call-template>
									<xsl:text>		</xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> = </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="(@type='MFNode')"><!-- setParentObject -->
										<xsl:text>		</xsl:text>
										<xsl:text>for (</xsl:text>
										<xsl:value-of select="$javaReferenceType" disable-output-escaping="yes"/>
										<xsl:text> element : </xsl:text>
										<xsl:value-of select="$newValue"/>
										<xsl:text>)</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>			((X3DConcreteElement) element).setParentObject(this);</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:text>		return this;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>

								<xsl:if test="(@type = 'MFNode') and (((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove'))) and not($isInterface = 'true')
											   and not($isInterface = 'true') and not($isX3dStatement = 'true')">
									<!-- source code: addSingleThing -->
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Add single </xsl:text>
									<xsl:if test="not(starts-with(@name,'child'))">
										<xsl:text>child </xsl:text>
									</xsl:if>
									<xsl:value-of select="@name"/>
									<xsl:text> node to array of existing nodes (if any).</xsl:text>
									<xsl:if test="(contains(@acceptableNodeTypes,'|'))">
										<xsl:text> Warning: acceptable node types are limited to </xsl:text>
										<xsl:value-of select="@acceptableNodeTypes"/>
										<xsl:text>.</xsl:text>
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new value to be appended the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:if test="($isX3dStatement = 'true')">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	 * @return {@link </xsl:text>
										<xsl:value-of select="$thisClassName"/>
										<xsl:text>} - namely </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:text>this</xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
										<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									</xsl:if>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>

									<xsl:text>	public </xsl:text>
									<!-- allow method pipelining, if appropropriate -->
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="ancestor::*[@name]/@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:text>void</xsl:text>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:choose>
										<xsl:when test="not(starts-with(@name,'add'))">
											<xsl:text> add</xsl:text>
											<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:text> </xsl:text>
											<xsl:value-of select="$normalizedMemberObjectName"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text>(</xsl:text>
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="$javaReferenceType"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>	
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:value-of select="$newValueNullReturnVoid"/>
									<xsl:text>		</xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text>.add(</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>);</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		((X3DConcreteElement) </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>).setParentObject(this); // here2</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="($name = 'ProtoBody')">
										<xsl:text disable-output-escaping="yes"><![CDATA[
		if ((primaryNode == null) && (]]></xsl:text><xsl:value-of select="$newValue"/><xsl:text> instanceof X3DConcreteNode))
		{
			primaryNode = (X3DConcreteNode) </xsl:text><xsl:value-of select="$newValue"/><xsl:text>; // remember node type
			primaryNode.setParentObject(this);
		}
</xsl:text>	
									</xsl:if>
									<!-- allow method pipelining, if appropropriate -->
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:text>		return this;</xsl:text>
											<xsl:text>&#10;</xsl:text>
										</xsl:when>
										<!-- requirement to match SAI interfaces prevents adding further support -->
									</xsl:choose>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>

								<xsl:if test="(@type = 'MFNode') and (((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove')) and not(starts-with(@name,'field')))">
									<!-- source code: addSomething -->
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Add array of </xsl:text>
									<xsl:if test="not(starts-with(@name,'child'))">
										<xsl:text>child </xsl:text>
									</xsl:if>
									<xsl:value-of select="@name"/>
									<xsl:text> nodes to array of existing nodes (if any).</xsl:text>
									<xsl:if test="(contains(@acceptableNodeTypes,'|'))">
										<xsl:text> Warning: acceptable node types are limited to </xsl:text>
										<xsl:value-of select="@acceptableNodeTypes"/>
										<xsl:text>.</xsl:text>
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new value array to be appended the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:if test="($isX3dStatement = 'true')">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	 * @return {@link </xsl:text>
										<xsl:value-of select="$thisClassName"/>
										<xsl:text>} - namely </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:text>this</xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
										<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
	<!-- debug -->
	<xsl:if test="($debug = 'true')">
	<xsl:text>// ($isInterface=</xsl:text>
	<xsl:value-of select="$isInterface"/>
	<xsl:text>, preceding-sibling::Inheritance=</xsl:text>
	<xsl:value-of select="preceding-sibling::Inheritance"/>
	<xsl:text>, $isX3dStatement=</xsl:text>
	<xsl:value-of select="$isX3dStatement"/>
	<xsl:text>)</xsl:text>
	<xsl:text>&#10;</xsl:text>
	</xsl:if>
									<xsl:if test="(not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')) or
													 (($isInterface = 'true') and //AbstractNodeType  [@name = $baseType                     ]/InterfaceDefinition/field[@name = $fieldName]) or
													 (($isInterface = 'true') and //AbstractNodeType  [@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName]) or
													 (($isInterface = 'true') and //AbstractObjectType[@name = $additionalInheritanceBaseType]/InterfaceDefinition/field[@name = $fieldName])">
										<xsl:text>	@Override</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:text>	public </xsl:text>
									<!-- allow method pipelining, if appropropriate -->
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="ancestor::*[@name]/@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:text>void</xsl:text>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:choose>
										<xsl:when test="not(starts-with(@name,'add'))">
											<xsl:text>add</xsl:text>
											<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="$normalizedMemberObjectName"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text>(</xsl:text>
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="$javaPrimitiveType"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>									
									<xsl:choose>
										<xsl:when test="($isInterface = 'true')">
											<xsl:text>;</xsl:text>
											<xsl:if test="contains(@acceptableNodeTypes,'|')">
												<xsl:text> // acceptable node types: </xsl:text>
												<xsl:value-of select="@acceptableNodeTypes"/>
											</xsl:if>
											<xsl:text>&#10;</xsl:text>
										</xsl:when>
										<xsl:otherwise>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	{</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true')">
													<xsl:value-of select="$newValueNullReturnThis"/>
												</xsl:when>
												<xsl:otherwise>
													<xsl:value-of select="$newValueNullReturnVoid"/>
												</xsl:otherwise>
											</xsl:choose>
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true') and (@type = 'MFNode')">
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		</xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>.add(</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>).setParentObject(this);</xsl:text>
												</xsl:when>
												<xsl:when test="(@type = 'MFNode')">
													<!-- do not reset array when adding to it -->
													<!-- MFNode subtype checks necessary -->
													<xsl:text>		for (int i = 0; i </xsl:text>
													<xsl:text disable-output-escaping="yes">&lt; </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>.length; i++)</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		{</xsl:text>
													<xsl:if test="($name = 'ProtoBody') and not($isInterface = 'true')">
														<xsl:text disable-output-escaping="yes"><![CDATA[
			if ((primaryNode == null) && (]]></xsl:text><xsl:value-of select="$newValue"/><xsl:text>[i] instanceof X3DConcreteNode))
			{
				primaryNode = (X3DConcreteNode) </xsl:text><xsl:value-of select="$newValue"/><xsl:text>[i]; // remember node type
				primaryNode.setParentObject(this);
			}
</xsl:text>	
													</xsl:if>
													<xsl:text>			if  (</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>[i] instanceof </xsl:text>
													<xsl:value-of select="$javaReferenceType"/>
													<xsl:text>)</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			{</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>				</xsl:text>
													<xsl:value-of select="@name"/>
													<xsl:text>.add(</xsl:text>
													<xsl:text>(</xsl:text>
													<xsl:value-of select="$javaReferenceType"/>
													<xsl:text>)</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>[i]);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>				((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>[i]).setParentObject(this);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			}</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			else throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
													<xsl:text>("</xsl:text>
													<xsl:value-of select="$javaPrimitiveType"/>
													<xsl:text> </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>["+i+"] is not instanceof </xsl:text>
													<xsl:value-of select="$javaReferenceType"/>
													<xsl:text>; </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>=" + </xsl:text>
													<xsl:text> Arrays.toString(</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>)</xsl:text>
													<xsl:text>);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		}</xsl:text>
												</xsl:when>
												<xsl:otherwise>
													<xsl:text>		</xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>.add(</xsl:text>
													<!--
													<xsl:if test="(@type = 'MFNode')">
														<xsl:text>(X3DNode)</xsl:text>
													</xsl:if>
													-->
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
													<xsl:if test="(@type = 'MFNode') and (string-length(@acceptableNodeTypes) > 0)">
														<xsl:text> // acceptable node types: </xsl:text>
														<xsl:value-of select="@acceptableNodeTypes"/>
													</xsl:if>
												</xsl:otherwise>
											</xsl:choose>
											<xsl:text>&#10;</xsl:text>
											<!-- allow method pipelining, if appropropriate -->
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true')">
													<xsl:text>		return this;</xsl:text>
													<xsl:text>&#10;</xsl:text>
												</xsl:when>
												<!-- requirement to match SAI interfaces prevents adding further support -->
											</xsl:choose>
											<xsl:text>}</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>&#10;</xsl:text>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:if>

								<xsl:if test="(@type = 'MFNode') and (((@name = 'address') or not(starts-with(@name,'add'))) and not(starts-with(@name,'remove')))">
									<!-- source code: addMFNodeSomething(SFNodeValue) method -->
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Set single </xsl:text>
									<xsl:if test="not(starts-with(@name,'child'))">
										<xsl:text>child </xsl:text>
									</xsl:if>
									<xsl:value-of select="@name"/>
									<xsl:text> node, replacing array of existing nodes (if any).</xsl:text>
									<xsl:if test="(contains(@acceptableNodeTypes,'|'))">
										<xsl:text> Warning: acceptable node types are limited to </xsl:text>
										<xsl:value-of select="@acceptableNodeTypes"/>
										<xsl:text>.</xsl:text>
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="not($isX3dStatement = 'true') and not($isInterface = 'true')">
										<xsl:text>	 * Unable to return this object and pipeline methods since abstract SAI specifies void return type.</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text disable-output-escaping="yes"><![CDATA[	 * @see <a href="http://stackoverflow.com/questions/14694852/can-overridden-methods-differ-in-return-type" target="_blank">stackoverflow: Can overridden methods differ in return type?</a>]]></xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new node for the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:if test="($isX3dStatement = 'true')">
										<xsl:text>&#10;</xsl:text>
										<xsl:text>	 * @return {@link </xsl:text>
										<xsl:value-of select="$thisClassName"/>
										<xsl:text>} - namely </xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
										<xsl:text>this</xsl:text>
										<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
										<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
										<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									</xsl:if>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
	<!-- debug -->
	<xsl:if test="($debug = 'true')">
	<xsl:text>// ($isInterface=</xsl:text>
	<xsl:value-of select="$isInterface"/>
	<xsl:text>, preceding-sibling::Inheritance=</xsl:text>
	<xsl:value-of select="preceding-sibling::Inheritance"/>
	<xsl:text>, $isX3dStatement=</xsl:text>
	<xsl:value-of select="$isX3dStatement"/>
	<xsl:text>)</xsl:text>
	<xsl:text>&#10;</xsl:text>
	</xsl:if>
									<xsl:if test="not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
										<xsl:text>	@Override</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:text>	public </xsl:text>
									<!-- allow method pipelining, if appropropriate -->
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="ancestor::*[@name]/@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:text>void</xsl:text>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:choose>
										<xsl:when test="not(starts-with(@name,'add'))">
											<xsl:text>set</xsl:text>
											<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="$normalizedMemberObjectName"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text>(</xsl:text>
									<xsl:choose>
										<xsl:when test="($isX3dStatement = 'true')">
											<xsl:value-of select="@name"/>
											<xsl:value-of select="$jsaiClassSuffix"/>
											<!-- singleton, no [] -->
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="substring-before($javaPrimitiveType,'[]')"/>
										</xsl:otherwise>
									</xsl:choose>
									<xsl:text> </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>									
									<xsl:choose>
										<xsl:when test="($isInterface = 'true')">
											<xsl:text>;</xsl:text>
											<xsl:if test="contains(@acceptableNodeTypes,'|')">
												<xsl:text> // acceptable node types: </xsl:text>
												<xsl:value-of select="@acceptableNodeTypes"/>
											</xsl:if>
											<xsl:text>&#10;</xsl:text>
										</xsl:when>
										<xsl:otherwise>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>	{</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:if test="($name = 'ProtoBody')">
												<xsl:text disable-output-escaping="yes"><![CDATA[		if ((newValue == null) && (primaryNode != null))]]></xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		{</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			primaryNode.setParentObject(null);</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>			primaryNode = null; // clear from ProtoBody</xsl:text>
												<xsl:text>&#10;</xsl:text>
												<xsl:text>		}</xsl:text>
												<xsl:text>&#10;</xsl:text>
											</xsl:if>
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true')">
													<xsl:value-of select="$newValueNullClearsFieldReturnThis"/>
												</xsl:when>
												<xsl:otherwise>
													<xsl:value-of select="$newValueNullClearsFieldReturnVoid"/>
												</xsl:otherwise>
											</xsl:choose>
											<xsl:choose>
												<xsl:when test="($name = 'ExternProtoDeclare') and (@name = 'field')">
		<!-- check to ensure that no value is present within field having parent ExternProtoDeclare -->
		<xsl:text disable-output-escaping="yes"><![CDATA[		// No value is allowed within field having parent ExternProtoDeclare
		if (!newValue.getValue().isEmpty() || !newValue.getChildren().isEmpty())
		{
			String foundValue;
			if (!newValue.getValue().isEmpty())
				 foundValue = newValue.getValue();
			else foundValue = newValue.getChildren().toString();
			
			throw new InvalidProtoException("ExternProtoDeclare name='" + name +
					"' with field name='" + newValue.getName() +
					"' cannot have any initial value (found \"" + foundValue + 
					"\"). Instead use ProtoInstance fieldValue to override the original default ProtoDeclare field value.");
		}
]]></xsl:text>
												</xsl:when>
											</xsl:choose>
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true') and (@type = 'MFNode')">
													<xsl:text>		</xsl:text>
													<xsl:text>for (</xsl:text>
													<xsl:value-of select="$javaReferenceType" disable-output-escaping="yes"/>
													<xsl:text> element : </xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>)</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			((X3DConcreteElement) element).clearParentObject();</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		</xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>.clear();</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		</xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>.add(</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>).setParentObject(this);</xsl:text>
													<xsl:text>&#10;</xsl:text>
												</xsl:when>
												<xsl:when test="(@type = 'MFNode')">
													<xsl:text>		if  (</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text> instanceof </xsl:text>
													<xsl:choose>
														<xsl:when test="($name = 'ProtoBody')">
															<xsl:text>X3DNode</xsl:text>
														</xsl:when>
														<xsl:otherwise>
															<xsl:value-of select="$javaReferenceType"/>
														</xsl:otherwise>
													</xsl:choose>
													<xsl:text>)</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		{</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			</xsl:text>
													<xsl:text>for (</xsl:text>
													<xsl:value-of select="$javaReferenceType" disable-output-escaping="yes"/>
													<xsl:text> element : </xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>)</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>				((X3DConcreteElement) element).clearParentObject();</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			</xsl:text>
													<xsl:value-of select="@name"/>
													<xsl:text>.clear();</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>).setParentObject(this);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>			</xsl:text>
													<xsl:if test="($name = 'ProtoBody')">
														<xsl:text>if ((</xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text disable-output-escaping="yes"><![CDATA[ instanceof X3DConcreteNode) && (primaryNode == null))]]></xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>				 primaryNode = (X3DConcreteNode) </xsl:text>
														<xsl:value-of select="$newValue"/>
														<xsl:text>; // remember node type</xsl:text>
														<xsl:text>&#10;</xsl:text>
														<xsl:text>			</xsl:text><!-- continue and include primaryNode in children list -->
													</xsl:if>
													<xsl:value-of select="@name"/>
													<xsl:text>.add(</xsl:text>
													<xsl:text>(</xsl:text>
													<xsl:choose>
														<xsl:when test="($name = 'ProtoBody')">
															<xsl:text>X3DNode</xsl:text>
														</xsl:when>
														<xsl:otherwise>
															<xsl:value-of select="$javaReferenceType"/>
														</xsl:otherwise>
													</xsl:choose>
													<xsl:text>)</xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		}</xsl:text>
													<xsl:text>&#10;</xsl:text>
													<xsl:text>		else throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
													<xsl:text>("</xsl:text>
													<xsl:value-of select="substring-before($javaPrimitiveType,'[]')"/>
													<xsl:text> </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text> is not instanceof </xsl:text>
													<xsl:value-of select="$javaReferenceType"/>
													<xsl:text>; </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>=" + </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
												</xsl:when>
												<xsl:otherwise><!-- apparently unused -->
													<xsl:text>		</xsl:text>
													<xsl:value-of select="$normalizedMemberObjectName"/>
													<xsl:text>.add(</xsl:text>
													<!--
													<xsl:if test="(@type = 'MFNode')">
														<xsl:text>(X3DNode)</xsl:text>
													</xsl:if>
													-->
													<xsl:value-of select="$newValue"/>
													<xsl:text>);</xsl:text>
													<xsl:if test="(@type = 'MFNode') and (string-length(@acceptableNodeTypes) > 0)">
														<xsl:text> // acceptable node types: </xsl:text>
														<xsl:value-of select="@acceptableNodeTypes"/>
													</xsl:if>
													<xsl:text>		((X3DConcreteElement) </xsl:text>
													<xsl:value-of select="$newValue"/>
													<xsl:text>).setParentObject(this);</xsl:text>
													<xsl:text>&#10;</xsl:text>
												</xsl:otherwise>
											</xsl:choose>
											<xsl:text>&#10;</xsl:text>
											<!-- allow method pipelining, if appropropriate -->
											<xsl:choose>
												<xsl:when test="($isX3dStatement = 'true')">
													<xsl:text>		return this;</xsl:text>
													<xsl:text>&#10;</xsl:text>
												</xsl:when>
												<!-- requirement to match SAI interfaces prevents adding further support, must return void -->
											</xsl:choose>
											<xsl:text>}</xsl:text>
											<xsl:text>&#10;</xsl:text>
											<xsl:text>&#10;</xsl:text>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:if>

								<xsl:if test="((@type='SFNode') or starts-with($javaType,'X3D')) and not($isInterface = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to clear </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value of </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field.</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<!-- TODO
									<xsl:text> * @see java.util.ArrayList</xsl:text>
									<xsl:text>&#10;</xsl:text>
									-->
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public void clear</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>()</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		((X3DConcreteElement) </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text>).clearParentObject();</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		</xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> = null; // reset SFNode field</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>

								<xsl:if test="((@type='MFNode') or (@type='MFString') or (@type='MFBool') or (@type = 'MFInt32') or (@type = 'SFImage') or (@type = 'MFImage') or (@type='MFFloat') or (@type='MFDouble') or (@type='MFTime')) and not($isInterface = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to clear ArrayList </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value of </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field.</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public void clear</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>()</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:if test="(@type='MFNode')">
										<xsl:text>		</xsl:text>
										<xsl:text>for (</xsl:text>
										<xsl:value-of select="$javaReferenceType" disable-output-escaping="yes"/>
										<xsl:text> element : </xsl:text>
										<xsl:value-of select="$normalizedMemberObjectName"/>
										<xsl:text>)</xsl:text>
										<xsl:text>&#10;</xsl:text>
										<xsl:text>			((X3DConcreteElement) element).clearParentObject();</xsl:text>
										<xsl:text>&#10;</xsl:text>
									</xsl:if>
									<xsl:text>		</xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text>.clear(); // reset</xsl:text>
									<xsl:text>&#10;</xsl:text>
	<xsl:if test="($name = 'ProtoBody')">
		<xsl:text>&#10;</xsl:text>
		<xsl:text>		if (primaryNode != null)</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>		{</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>			primaryNode.setParentObject(null);</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>			primaryNode = null; // clear from ProtoBody</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>		}</xsl:text>
		<xsl:text>&#10;</xsl:text>
	</xsl:if>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>

								<xsl:if test="((@type='MFFloat') or (@type='MFDouble') or (@type='MFTime'))
											   and not($isInterface = 'true') and not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to assign floating-point array </xsl:text>
									<xsl:if test="not($normalizedMemberObjectName = 'value')">
										<xsl:text>value of </xsl:text>
									</xsl:if>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field, similar to {@link #set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(</xsl:text>
									<xsl:value-of select="$javaPrimitiveType" disable-output-escaping="yes"/>
									<xsl:text>)}. </xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @param </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text> is new value for the </xsl:text>
									<xsl:value-of select="@name"/>
									<xsl:text> field.</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * @return {@link </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text>} - namely </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
									<xsl:text>this</xsl:text>
									<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
									<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).</xsl:text>
									<!-- https://en.wikipedia.org/wiki/Pipeline_(software) -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 */</xsl:text><!-- end javadoc -->
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	public </xsl:text>
									<xsl:value-of select="$thisClassName"/>
									<xsl:text> set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(int[] </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>)</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	{</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:value-of select="$newValueNullReturnThis"/>
									<xsl:call-template name="set-newValue-validity-checks">
										<xsl:with-param name="canThrowFieldValueException"><xsl:value-of select="$canThrowFieldValueException"/></xsl:with-param>
										<xsl:with-param name="isArrayType"      ><xsl:value-of select="$isArrayType"/></xsl:with-param>
										<xsl:with-param name="isArrayListType"  ><xsl:value-of select="$isArrayListType"/></xsl:with-param>
										<xsl:with-param name="x3dType"          ><xsl:value-of select="@type"/></xsl:with-param>
										<xsl:with-param name="javaReferenceType"><xsl:value-of select="$javaReferenceType"/></xsl:with-param>
										<xsl:with-param name="comparisonType"   ><xsl:text>complex</xsl:text></xsl:with-param>
									</xsl:call-template>
									<xsl:text>		</xsl:text>
									<xsl:value-of select="substring-before($javaPrimitiveType,'[]')" disable-output-escaping="yes"/>
									<xsl:text>[] holdArray = new </xsl:text>
									<xsl:value-of select="substring-before($javaPrimitiveType,'[]')" disable-output-escaping="yes"/>
									<xsl:text>[newValue.length];</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		for (int i = 0; i </xsl:text>
									<xsl:text disable-output-escaping="yes">&lt; </xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>.length; i++) {</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>			</xsl:text>
									<xsl:text>holdArray[i] = (</xsl:text>
									<xsl:value-of select="substring-before($javaPrimitiveType,'[]')" disable-output-escaping="yes"/>
									<xsl:text>)</xsl:text>
									<xsl:value-of select="$newValue"/>
									<xsl:text>[i];</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		}</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		</xsl:text>
									<xsl:text>set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(holdArray);</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>		return this;</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	}</xsl:text>
									<xsl:text>&#10;</xsl:text>
								</xsl:if>
								
								<xsl:choose>
									<xsl:when test="((@name = 'children') and not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
													not($name = 'ConfigurationProperties') and not($name = 'CADPart'))">
										<xsl:text>
	/**
	 * Add comment as CommentsBlock to children field
	 * @param newComment initial value
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (String newComment)
	{
		if (newComment == null) return this;
		children.add(new CommentsBlock (newComment));
		return this;
	}
	/**
	 * Add comments array as CommentsBlock to children field
	 * @param newComments array of comments
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (String[] newComments)
	{
		if (newComments == null) return this;
		children.add(new CommentsBlock (newComments));
		return this;
	}
	/**
	 * Add CommentsBlock to children field
	 * @param newCommentsBlock block of comments to add
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (CommentsBlock newCommentsBlock)
	{
		if (newCommentsBlock == null) return this;
		children.add(newCommentsBlock);
		return this;
	}
										</xsl:text>
									</xsl:when>
								</xsl:choose>

								<xsl:if test="(@type='SFNode') and not($isX3dStatement = 'true') and not($isInterface = 'true')">
									<xsl:text>	/**</xsl:text>
									<xsl:text>&#10;</xsl:text>
									<xsl:text>	 * Utility method to assign ProtoInstance to </xsl:text>
									<xsl:value-of select="$normalizedMemberObjectName"/>
									<xsl:text> field.</xsl:text>
									<xsl:text disable-output-escaping="yes"><![CDATA[
	 * @param newProtoInstanceNode is the new ProtoInstance node for the ]]></xsl:text><xsl:value-of select="@name"/><xsl:text disable-output-escaping="yes"><![CDATA[ field
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
]]></xsl:text>
									<xsl:text>	public </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> set</xsl:text>
									<xsl:value-of select="translate($CamelCaseName,'-','_')"/> <!-- translate name here to avoid xpath problems -->
									<xsl:text>(ProtoInstanceObject newProtoInstanceNode)
	{
		if (</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text> != null)
		{
			((X3DConcreteElement) </xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>).setParentObject(null);
			</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text> = null;
		}
		</xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>ProtoInstance = newProtoInstanceNode;
		if (newProtoInstanceNode != null)
		    newProtoInstanceNode.setParentObject(this);
		return this;
	}
	/**
	 * Provide properly typed ProtoInstance for </xsl:text><xsl:value-of select="@accessType"/>
		<xsl:text disable-output-escaping="yes"><![CDATA[ SFNode field <i>]]></xsl:text>
		<xsl:value-of select="$normalizedMemberObjectName"/>
		<xsl:text disable-output-escaping="yes"><![CDATA[</i>, if available.
	 * @return ProtoInstance value of geometry field
	 */
	public ProtoInstanceObject get]]></xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>ProtoInstance()
	{
		return </xsl:text><xsl:value-of select="$normalizedMemberObjectName"/><xsl:text>ProtoInstance;
	}
</xsl:text>
								</xsl:if>
								<!-- end of per-field set accessors and field utility methods for concrete classes -->
							</xsl:if>
							<!-- debug
							<xsl:message>
								<xsl:text>*** @CamelCaseName=</xsl:text>
								<xsl:value-of select="$CamelCaseName"/>
								<xsl:text>, accessType=</xsl:text>
								<xsl:value-of select="@accessType"/>
							</xsl:message> -->
						</xsl:if>
						
					</xsl:for-each>
					<!-- finished with InterfaceDefinition/field loop -->

					<xsl:if test="($hasImplementationBlock)">
						<xsl:if test="starts-with(normalize-space($implementationBlock),'{')">
							<xsl:message>
								<xsl:text>*** Code-generation warning: $interfaceBlock starts with {</xsl:text>
							</xsl:message>
						</xsl:if>
						<xsl:value-of select="$implementationBlock" disable-output-escaping="yes"/> <!-- typically has additional javadoc included -->
					</xsl:if>

					<!-- Additional per-class utility methods -->
					<xsl:if test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
								  not($name = 'ConfigurationProperties') and not(starts-with($thisClassName, 'X3DConcrete'))">
						
						<xsl:text>&#10;</xsl:text>
						<xsl:text>	// Additional utility methods for this class ==============================</xsl:text>

						<xsl:variable name="hasChild">
							<xsl:value-of select="(count(*) + count(comment()) > 0)"/>
						</xsl:variable>
						<xsl:variable name="hasAttributes">
							<xsl:value-of select="(count(*) + count(comment()) > 0)"/>
						</xsl:variable>
						<xsl:variable name="isX3dStatement">
							<xsl:call-template name="isX3dStatement">
								<xsl:with-param name="name" select="@name"/>
							</xsl:call-template>
						</xsl:variable>
								
						<!-- utility constructors -->
						<xsl:choose>
							<xsl:when test="not($isX3dStatement = 'true') and not($isClassX3dStatement = 'true')">
								<xsl:variable name="tooltipTextIS">
									<xsl:value-of select="$x3d.tooltips.document//element[@name = 'IS']/@tooltip" disable-output-escaping="yes"/>
								</xsl:variable>
								<xsl:text>
	/**
	 * Utility constructor that assigns DEF name after initializing member variables with default values
	 * @param DEFname unique DEF name for this X3D node
	 */
	public </xsl:text>
			<xsl:value-of select="$thisClassName"/>
	<xsl:text disable-output-escaping="yes"><![CDATA[ (String DEFname)
	{
		initialize();
		setDEF(DEFname);
	}
	/**
	 * Assign String value to field named <i>IS</i> for establishing IS/connect field connections between ProtoInterface fields and internal ProtoBody nodes.
	 * The IS statement connects node fields defined inside a ProtoBody declaration back to corresponding ProtoInterface fields.
	 * @param newValue is new value for the description field.
	 * @return {@link ]]></xsl:text><xsl:value-of select="$name"/><xsl:text disable-output-escaping="yes"><![CDATA[Object} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$name"/><xsl:text disable-output-escaping="yes"><![CDATA[Object setIS(ISObject newValue)
	{
		if (IS != null)
			IS.setParentObject(null);
		IS = newValue;
		IS.setParentObject(this);
		return this;
	}
		
	/**
	 * Provide String value from field named <i>IS</i> for establishing IS/connect field connections between ProtoInterface fields and internal ProtoBody nodes.
	 * The IS statement connects node fields defined inside a ProtoBody declaration back to corresponding ProtoInterface fields.
	 * @return {@link ]]></xsl:text><xsl:value-of select="$name"/><xsl:text disable-output-escaping="yes"><![CDATA[Object} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public ISObject getIS()
	{
		return IS;
	}
]]></xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare') or ($name = 'ProtoInstance')">
								<xsl:text>
	/**
	 * Utility constructor that assigns </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> name after initializing member variables with default values
	 * @param prototypeName initial name for this </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> statement
	 */
	public </xsl:text>
			<xsl:value-of select="$thisClassName"/>
	<xsl:text disable-output-escaping="yes"><![CDATA[ (String prototypeName)
	{
		initialize();
		setName(prototypeName);
	}
	/**
	 * ]]></xsl:text>
	 <xsl:if test="($name = 'ExternProtoDeclare')">
		 <xsl:text>(TODO not yet supported in ExternProtoDeclare) </xsl:text>
	 </xsl:if>
	 <xsl:text disable-output-escaping="yes"><![CDATA[Inspect first node within ProtoDeclare ProtoBody to determine node type of corresponding ProtoInstance]]></xsl:text>
	 <xsl:if test="($name = 'ProtoDeclare') or ($name = 'ProtoBody')">
		 <xsl:text disable-output-escaping="yes"><![CDATA[, local copy maintained in ProtoBody <i>primaryNode</i>]]></xsl:text>
	 </xsl:if>
	 <xsl:text disable-output-escaping="yes"><![CDATA[.
	 * @see <a href="http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/concepts.html#PROTOdefinitionsemantics">X3D Abstract Specification: 4.4.4.3 PROTO definition semantics</a>]]></xsl:text>
	 <xsl:choose>
		 <xsl:when test="($name = 'ProtoDeclare')">
			 <xsl:text disable-output-escaping="yes"><![CDATA[
	 * @see ProtoBodyObject#getNodeType()
	 * @see ExternProtoDeclareObject#getNodeType()
	 * @see ProtoInstanceObject#getNodeType()]]></xsl:text>
		 </xsl:when>
		 <xsl:when test="($name = 'ExternProtoDeclare')">
			 <xsl:text disable-output-escaping="yes"><![CDATA[
	 * @see ProtoDeclareObject#getNodeType()
	 * @see ProtoBodyObject#getNodeType()
	 * @see ProtoInstanceObject#getNodeType()]]></xsl:text>
		 </xsl:when>
		 <xsl:when test="($name = 'ProtoInstance')">
			 <xsl:text disable-output-escaping="yes"><![CDATA[
	 * @see ProtoDeclareObject#getNodeType()
	 * @see ProtoBodyObject#getNodeType()
	 * @see ExternProtoDeclareObject#getNodeType()]]></xsl:text>
		 </xsl:when>
	 </xsl:choose>
	 <xsl:text disable-output-escaping="yes"><![CDATA[
		 
	 * @return name of X3D node corresponding to node type for this ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> statement
	 */
	public String getNodeType()
	{
		</xsl:text>
		<xsl:choose>
			<xsl:when test="($name = 'ProtoDeclare')">
				<xsl:text>
		if (ProtoBody != null)
			 return ProtoBody.getNodeType();
		else return "UNDEFINED";</xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'ExternProtoDeclare')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		String errorNotice = new String();
		if (getAncestorSceneObject() == null)
		{
			errorNotice += "ProtoInstance name='" + getName() + "' is not connected to a scene graph and cannot be checked.";
			validationResult.append(errorNotice).append("\n");
			return "PrototypeNotFoundWhenNotConnectedToSceneGraph"; // not found
		}
		X3DConcreteElement matchingDeclaration = getAncestorSceneObject().getElementByName(getName());
		if      ((matchingDeclaration != null) && (matchingDeclaration instanceof ProtoDeclareObject))
		{
			// added matching methods for getNodeType() in ProtoDeclare, ProtoBody
			return ((ProtoDeclareObject) matchingDeclaration).getNodeType();
		}
		else return "UNKNOWN"; // not found]]></xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'ProtoInstance')">
				<xsl:text disable-output-escaping="yes"><![CDATA[// check for corresponding declaration
		String errorNotice = new String();
		if (getAncestorSceneObject() == null)
		{
			errorNotice += "ProtoInstance name='" + getName() + "' is not connected to a scene graph and cannot be checked.";
			validationResult.append(errorNotice).append("\n");
			return "PrototypeNotFoundWhenNotConnectedToSceneGraph"; // not found
		}
		X3DConcreteElement matchingDeclaration = getAncestorSceneObject().getElementByName(getName());
		if      ((matchingDeclaration != null) && (matchingDeclaration instanceof ProtoDeclareObject))
		{
			// added matching methods for getNodeType() in ProtoDeclare, ProtoBody
			return ((ProtoDeclareObject) matchingDeclaration).getNodeType();
		}
		else if ((matchingDeclaration != null) && (matchingDeclaration instanceof ExternProtoDeclareObject))
		{
			return ((ExternProtoDeclareObject) matchingDeclaration).getNodeType();
		}
		else return "UNKNOWN"; // not found]]></xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<xsl:text>return "UNKNOWN"; // TODO figure out corresponding query that loads ProtoDeclare </xsl:text>
				<xsl:text>via ExternProtoDeclare url,then inspects it</xsl:text>
			</xsl:otherwise>
		</xsl:choose>
<xsl:text>
	}
</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'ProtoBody')">
								<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * First node within ProtoDeclare ProtoBody determines node type of corresponding ProtoInstance, local reference maintained in member variable named <i>primaryNode</i>.
	 * @see <a href="http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/concepts.html#PROTOdefinitionsemantics">X3D Abstract Specification: 4.4.4.3 PROTO definition semantics</a>
	 * @see ProtoDeclareObject#getNodeType()
	 * @see ExternProtoDeclareObject#getNodeType()
	 * @see ProtoInstanceObject#getNodeType()
	 * @return name of X3D node corresponding to node type for this ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ statement
	 */
	public String getNodeType ()
	{
		if (primaryNode != null)
		     return primaryNode.getElementName();
		else return "UNDEFINED";
	}
]]></xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'field')">
								<xsl:text>
	// no other constructors because field must have name, type, accessType (required)
	/**
	 * Utility constructor that assigns name, type, accessType (required)
	 * @param fieldName name for this field (required, and locally unique among peer fields)
	 * @param fieldType appropriate type value for this field (required)
	 * @param fieldAccessType appropriate accessType value for this field (required)
	 */
	public </xsl:text>
	<xsl:value-of select="$thisClassName"/>
	<xsl:text> (String fieldName, String fieldType, String fieldAccessType)
	{
		initialize();
		      setName(fieldName);		// apply checks
		      setType(fieldType);		// apply checks
		setAccessType(fieldAccessType);	// apply checks
	}
	/**
	 * Utility constructor that assigns name, type, accessType (required) and default value (if appropriate)
	 * @param fieldName name for this field (required, and locally unique among peer fields)
	 * @param fieldType appropriate type value for this field (required)
	 * @param fieldAccessType appropriate accessType value for this field (required)
	 * @param defaultValue string version of default value for this field (if appropriate)
	 */
	public </xsl:text>
	<xsl:value-of select="$thisClassName"/>
	<xsl:text> (String fieldName, String fieldType, String fieldAccessType, String defaultValue)
	{
		initialize();
		      setName(fieldName);		// apply checks
		      setType(fieldType);		// apply checks
		setAccessType(fieldAccessType);	// apply checks
		     setValue(defaultValue);	// apply checks
	}
</xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'fieldValue')">
								<xsl:text>
	/**
	 * Utility constructor that also assigns fieldValueName
	 * @param fieldValueName unique DEF name for this X3D node
	 */
	public </xsl:text>
	<xsl:value-of select="$thisClassName"/>
	<xsl:text> (String fieldValueName)
	{
		initialize();
		setName(fieldValueName);
	}
	/**
	 * Utility constructor that also assigns fieldValueName, defaultValue
	 * @param fieldValueName unique name for this field
	 * @param defaultValue string version of defaultValue for this field
	 */
	public </xsl:text>
	<xsl:value-of select="$thisClassName"/>
	<xsl:text> (String fieldValueName, String defaultValue)
	{
		initialize();
		setName (fieldValueName);
	    setValue(defaultValue);
	}
</xsl:text>
							</xsl:when>
						</xsl:choose>
						
						<!-- commentsBlock -->
						<xsl:if test="(not($hasChildrenField = 'true') and not(starts-with($name, 'X3DConcrete')) and not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
										not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not($name = 'CADPart'))">
							<xsl:text>
	/**
	 * Add comment as CommentsBlock to contained commentsList.
	 * @param newComment initial value
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (String newComment)
	{
		commentsList.add(newComment);
		return this;
	}
	/**
	 * Add comments array as CommentsBlock to contained commentsList.
	 * @param newComments array of comments
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (String[] newComments)
	{
		commentsList.addAll(Arrays.asList(newComments));
		return this;
	}
	/**
	 * Add CommentsBlock to contained commentsList.
	 * @param newCommentsBlock block of comments to add
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (CommentsBlock newCommentsBlock)
	{
		commentsList.addAll(newCommentsBlock.toStringList());
		return this;
	}</xsl:text>
						</xsl:if>
							
						<!-- toStringX3D -->
						<xsl:if test="not(starts-with($thisClassName, 'X3DConcrete'))">
							<xsl:text disable-output-escaping="yes"><![CDATA[
		
	/**
	 * Recursive method to provide X3D string serialization of this model subgraph.
	 * @param level number of levels of indentation for this element
	 * @return X3D string
	 */
	@Override
	public String toStringX3D(int level)
	{]]></xsl:text>
	<xsl:if test="not($name = 'CommentsBlock')">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		boolean hasAttributes = true; // TODO check for non-default attribute values
		boolean      hasChild = ]]></xsl:text>
		<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
			<xsl:text>(IS != null) || </xsl:text>
		</xsl:if>
		<xsl:variable name="fieldsList" select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
														((@accessType='initializeOnly') or (@accessType='inputOutput'))]"/>
		<xsl:for-each select="$fieldsList">
			<xsl:variable name="isX3dStatement">
				<xsl:call-template name="isX3dStatement">
					<xsl:with-param name="name" select="@name"/>
				</xsl:call-template>
			</xsl:variable>
			<xsl:if test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
				<xsl:text>(!fieldList.isEmpty()) || (!sourceCode.isEmpty()) || </xsl:text>
			</xsl:if>
			<xsl:choose>
				<xsl:when test="(@type = 'SFNode')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="@name"/>
					<xsl:text> != null)</xsl:text>
				</xsl:when>
				<xsl:otherwise><!-- (@type='MFNode') -->
					<xsl:text>(!</xsl:text>
					<xsl:value-of select="@name"/>
					<xsl:if test="($isX3dStatement = 'true')">
						<xsl:text>List</xsl:text><!-- append to member name -->
					</xsl:if>
					<xsl:text>.isEmpty())</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			
			<xsl:if test="(last() > position()) or not($hasChildrenField = 'true')">
				<xsl:text> || </xsl:text>
			</xsl:if>
		</xsl:for-each>
		<xsl:choose>
			<xsl:when test="not($hasChildrenField = 'true')">
				<xsl:text disable-output-escaping="yes">!commentsList.isEmpty()</xsl:text>
			</xsl:when>
			<xsl:when test="1 > count($fieldsList)">
				<xsl:text>false</xsl:text><!-- TODO account for CommentsBlock -->
			</xsl:when>
		</xsl:choose>
		<xsl:text>;
</xsl:text><!-- hasChild definition complete -->
	</xsl:if>
	<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		if (getUSE().length() > 0)
			hasChild = false; // USE nodes only include attributes for USE and non-default containerField]]></xsl:text><!-- append to member name -->
	</xsl:if>
	<xsl:text disable-output-escaping="yes"><![CDATA[
		StringBuilder indent = new StringBuilder();
		int  indentIncrement = ConfigurationProperties.getIndentIncrement();
		char indentCharacter = ConfigurationProperties.getIndentCharacter();
		for (int i = 0; i < (level * indentIncrement); i++)
			indent.append(indentCharacter); // level of indentation for this level

		StringBuilder stringX3D = new StringBuilder();
]]></xsl:text>						
		
		<!-- special constants needed for serialization toStringX3D -->
		<xsl:choose>					
			<xsl:when test="($name = 'X3D')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		stringX3D.append(XML_HEADER).append("\n");
		switch (version)
		{
			case "3.0":
				stringX3D.append(DOCTYPE_3_0).append("\n");
				break;
			case "3.1":
				stringX3D.append(DOCTYPE_3_1).append("\n");
				break;
			case "3.2":
				stringX3D.append(DOCTYPE_3_2).append("\n");
				break;
			case "3.3":
				stringX3D.append(DOCTYPE_3_3).append("\n");
				break;
			case "4.0":
				stringX3D.append(DOCTYPE_4_0).append("\n");
				break;
			case "4.1":
				stringX3D.append(DOCTYPE_4_1).append("\n");
				break;
			default:
				stringX3D.append("<!-- unknown DOCTYPE for X3D version ").append(version).append(" -->").append("\n");
		}]]></xsl:text>
			</xsl:when>
		</xsl:choose>
		
		<xsl:choose>
			<xsl:when test="($name = 'CommentsBlock')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		for (String comment : commentsList)
		{
			stringX3D.append(indent).append("<!-- ").append(comment).append(" -->").append("\n");
		}]]></xsl:text>
			</xsl:when>
			<xsl:otherwise>
				
		<xsl:text disable-output-escaping="yes"><![CDATA[
		stringX3D.append(indent).append("<]]></xsl:text><xsl:value-of select="$name"/><xsl:text><![CDATA["); // start opening tag
		if (hasAttributes)
		{]]></xsl:text>
			<!-- DEF, USE, name attributes first for readability and to match X3D Canonical Form -->
			<xsl:if test="InterfaceDefinition/field[@name = 'DEF']">
				<xsl:text>
			if (!getDEF().equals(DEF_DEFAULT_VALUE))
			{
				stringX3D.append(" DEF='").append(SFStringObject.toString(getDEF())).append("'");
			}</xsl:text>
			</xsl:if>
			<xsl:if test="InterfaceDefinition/field[@name = 'USE']">
				<xsl:text>
			if (!getUSE().equals(USE_DEFAULT_VALUE))
			{
				stringX3D.append(" USE='").append(SFStringObject.toString(getUSE())).append("'");
			}</xsl:text>
			</xsl:if>
			<xsl:if test="InterfaceDefinition/field[@name = 'name']">
				<xsl:text>
			if (!getName().equals(NAME_DEFAULT_VALUE))
			{
				stringX3D.append(" name='").append(SFStringObject.toString(getName())).append("'");
			}</xsl:text>
			</xsl:if>
			<!-- attributes (i.e. non-node fields) -->
			<xsl:for-each select="InterfaceDefinition/field[not(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and not(@name = 'DEF') and not(@name = 'USE') and not(@name = 'name') and 
                                                            ((@accessType='initializeOnly') or (@accessType='inputOutput'))]">
				<xsl:variable name="fieldName" select="translate(@name,'-','_')"/><!-- handle http-equiv etc. -->
				<xsl:variable name="isSingleValueType">
					<xsl:value-of select="starts-with(@type,'SF') and not(contains(@type, 'Vec')) and not(contains(@type, 'Matrix'))"/>
				</xsl:variable>
				<xsl:variable name="CamelCaseName"><!-- upper camel case -->
					<xsl:choose>
						<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
							<!-- unmodified -->
							<xsl:value-of select="@name"/>
						</xsl:when>
						<xsl:when test="(@name = 'class')">
							<!-- getClass() is reserved by Java Object() class -->
							<xsl:text>CssClass</xsl:text>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="translate(substring($fieldName,1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
							<xsl:value-of select="substring($fieldName,2)"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>
				<xsl:variable name="javaType">
					<xsl:call-template name="javaType">
						<xsl:with-param name="x3dType" select="@type"/>
						<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
					</xsl:call-template>
				</xsl:variable>
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
<xsl:text>// ($fieldName=</xsl:text>
<xsl:value-of select="$fieldName"/>
<xsl:text>, $hasChild=</xsl:text>
<xsl:value-of select="$hasChild"/>
<xsl:text>, $hasAttributes=</xsl:text>
<xsl:value-of select="$hasAttributes"/>
<xsl:text>, CamelCaseName=</xsl:text>
<xsl:value-of select="$CamelCaseName"/>
<xsl:text>, javaType=</xsl:text>
<xsl:value-of select="$javaType"/>
<xsl:text>, isSingleValueType=</xsl:text>
<xsl:value-of select="$isSingleValueType"/>
<xsl:text>)</xsl:text>
</xsl:message>
</xsl:if>

				<xsl:text><![CDATA[
			if (]]></xsl:text>
			<xsl:choose>
				<!-- required attributes -->
				<xsl:when test="(($name = 'X3D') and (($fieldName = 'profile') or ($fieldName = 'version'))) or
								(($name = 'HAnimHumanoid') and ($fieldName = 'version')) or
								(($name = 'component') and ($fieldName = 'level')) or
								(($name = 'unit')      and ($fieldName = 'conversionFactor'))">
					<xsl:text><![CDATA[true) // required attribute]]></xsl:text>
				</xsl:when>
				<xsl:when test="(@type = 'SFBool') or (@type = 'SFInt32') or (@type = 'SFFloat') or (@type = 'SFDouble') or (@type = 'SFTime')">
					<xsl:text><![CDATA[(get]]></xsl:text>
					<xsl:value-of select="$CamelCaseName"/>
					<xsl:text disable-output-escaping="yes"><![CDATA[() != ]]></xsl:text>
					<xsl:value-of select="upper-case($fieldName)"/>
					<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
				</xsl:when>
				<xsl:when test="contains($javaType, 'ArrayList')">
					<xsl:text><![CDATA[(get]]></xsl:text>
					<xsl:value-of select="$CamelCaseName"/>
					<xsl:text disable-output-escaping="yes"><![CDATA[().length > 0) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
				</xsl:when>
				<xsl:when test="($isSingleValueType = 'true')">
					<xsl:text><![CDATA[!get]]></xsl:text>
					<xsl:value-of select="$CamelCaseName"/>
					<xsl:text><![CDATA[().equals(]]></xsl:text>
					<xsl:value-of select="upper-case($fieldName)"/>
					<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
				</xsl:when>
				<xsl:when test="(string-length(@default) > 0)">
					<xsl:text><![CDATA[!Arrays.equals(get]]></xsl:text>
					<xsl:value-of select="$CamelCaseName"/>
					<xsl:text><![CDATA[(), ]]></xsl:text>
					<xsl:value-of select="upper-case($fieldName)"/>
					<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:text><![CDATA[get]]></xsl:text>
					<xsl:value-of select="$CamelCaseName"/>
					<xsl:text disable-output-escaping="yes"><![CDATA[().length > 0)]]></xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text><![CDATA[
			{
				stringX3D.append(" ]]></xsl:text>
				<xsl:value-of select="$fieldName"/>
				<xsl:text>='").append(</xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:value-of select="$jsaiClassSuffix"/>
				<xsl:text>.toString(get</xsl:text>
				<xsl:value-of select="$CamelCaseName"/>
				<xsl:text>())).append("'");
			}</xsl:text>
			</xsl:for-each>
			<xsl:choose>					
				<xsl:when test="($name = 'X3D')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
				switch (version)
				{
					case "3.0":
						stringX3D.append(" ").append(SCHEMA_3_0_ATTRIBUTES);
						break;
					case "3.1":
						stringX3D.append(" ").append(SCHEMA_3_1_ATTRIBUTES);
						break;
					case "3.2":
						stringX3D.append(" ").append(SCHEMA_3_2_ATTRIBUTES);
						break;
					case "3.3":
						stringX3D.append(" ").append(SCHEMA_3_3_ATTRIBUTES);
						break;
					case "4.0":
						stringX3D.append(" ").append(SCHEMA_4_0_ATTRIBUTES);
						break;
					case "4.1":
						stringX3D.append(" ").append(SCHEMA_4_1_ATTRIBUTES);
						break;
					default:
						stringX3D.append(" ").append(SCHEMA_3_3_ATTRIBUTES); // TODO error condition
						break;
				}]]></xsl:text>
				</xsl:when>
			</xsl:choose>
			
			<xsl:text disable-output-escaping="yes"><![CDATA[
		}
		if (hasChild) // has contained node(s), comment(s), IS/connect and/or source code
		{
			stringX3D.append(">").append("\n"); // finish opening tag
]]></xsl:text>
		<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
			<xsl:text>
			if (getIS() != null)
				stringX3D.append(getIS().toStringX3D(level + indentIncrement));</xsl:text>
		</xsl:if>
			<xsl:text disable-output-escaping="yes"><![CDATA[

			// recursively iterate over child element]]></xsl:text>
			<xsl:if test="InterfaceDefinition/field[(@type = 'MFNode')] or
				   (count(InterfaceDefinition/field[contains(@type,'FNode')]) > 1)">
				<xsl:text>s</xsl:text>
			</xsl:if>
			<xsl:text>&#10;</xsl:text>
			
			<xsl:for-each select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
															((@accessType='initializeOnly') or (@accessType='inputOutput')) and
                                                            not(@name = 'meta')]">
				<!-- special order for head elements: meta comes last, handled afterwards -->
				<!-- sort ProtoInterface before ProtoBody -->
				<xsl:sort select="(@name = 'ProtoBody')"/>
				<xsl:sort select="(@name = 'ProtoInterface')"/>
				
				<xsl:variable name="javaType">
					<xsl:call-template name="javaType">
						<xsl:with-param name="x3dType" select="@type"/>
						<xsl:with-param name="isInterface" select="$isInterface"/>
					</xsl:call-template>
				</xsl:variable>
				<xsl:variable name="javaReferenceType">
					<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
				</xsl:variable>
				<xsl:variable name="isX3dStatement">
					<xsl:call-template name="isX3dStatement">
						<xsl:with-param name="name" select="@name"/>
					</xsl:call-template>
				</xsl:variable>

				<xsl:choose>
					<xsl:when test="(@type = 'SFNode')">
						<!-- cast abstract element to concrete type -->
						<xsl:text><![CDATA[
			if      (]]></xsl:text><xsl:value-of select="@name"/><xsl:text><![CDATA[ != null)
					 stringX3D.append(((X3DConcreteElement)]]></xsl:text><xsl:value-of select="@name"/>
						<xsl:text><![CDATA[).toStringX3D(level + indentIncrement));]]></xsl:text>
						<xsl:if test="not($isX3dStatement = 'true')">
						<xsl:text><![CDATA[
			else if (]]></xsl:text><xsl:value-of select="@name"/><xsl:text><![CDATA[ProtoInstance != null)
					 stringX3D.append(((X3DConcreteElement)]]></xsl:text><xsl:value-of select="@name"/>
						<xsl:text><![CDATA[ProtoInstance).toStringX3D(level + indentIncrement));]]></xsl:text>
						</xsl:if>
					</xsl:when>
					<xsl:otherwise> <!-- MFNode -->
						<xsl:text><![CDATA[
			for (]]></xsl:text><xsl:value-of select="$javaReferenceType"/><xsl:text><![CDATA[ element : ]]></xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:if test="($isX3dStatement = 'true') and (@type='MFNode')">
							<xsl:text>List</xsl:text><!-- append to member name -->
						</xsl:if>
						<!-- cast abstract element to concrete type -->
						<xsl:text><![CDATA[)
				 stringX3D.append(((X3DConcreteElement)element).toStringX3D(level + indentIncrement));]]></xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>
			
			<xsl:if test="($name = 'head')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
			// note required order of component, unit, meta (though relaxation of this requirement has been proposed)
			for (metaObject element : metaList)
				 stringX3D.append(((metaObject)element).toStringX3D(level + indentIncrement));
]]></xsl:text>
			</xsl:if>
			
			<xsl:if test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
				<xsl:text disable-output-escaping="yes"><![CDATA[

			for (fieldObject element : fieldList)
				 stringX3D.append(((fieldObject)element).toStringX3D(level + indentIncrement));

			if (sourceCode.trim().length() > 0)
				stringX3D.append("<![CDATA[\n").append(sourceCode)
				         .append("\n]]></xsl:text><xsl:text>]]</xsl:text><xsl:text disable-output-escaping="yes"><![CDATA[>\n");
]]></xsl:text>
			</xsl:if>
			
			<xsl:if test="(not($hasChildrenField = 'true') and not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
							not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not($name = 'CADPart'))">
				<xsl:text><![CDATA[
			if (!commentsList.isEmpty())
			{
				CommentsBlock commentsBlock = new CommentsBlock(commentsList);
				stringX3D.append(commentsBlock.toStringX3D(level + indentIncrement));
			}]]></xsl:text>
			</xsl:if>

			<xsl:text disable-output-escaping="yes"><![CDATA[
			stringX3D.append(indent).append("</]]></xsl:text>
			<xsl:value-of select="$name"/>
			<xsl:text disable-output-escaping="yes"><![CDATA[>").append("\n"); // finish closing tag
		}
		else
		{
			stringX3D.append("/>").append("\n"); // otherwise finish singleton tag
		}]]></xsl:text>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:text disable-output-escaping="yes"><![CDATA[
		return stringX3D.toString();
	}
]]></xsl:text>
						</xsl:if>
							
						<!-- toStringClassicVRML -->
						<xsl:if test="not(starts-with($thisClassName, 'X3DConcrete'))">
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:text>// ($name=</xsl:text>
<xsl:value-of select="$name"/>
<xsl:text>, isX3dStatement=</xsl:text>
<xsl:value-of select="$isX3dStatement"/>
<xsl:text>, isClassX3dStatement=</xsl:text>
<xsl:value-of select="$isClassX3dStatement"/>
<xsl:text>, $hasChild=</xsl:text>
<xsl:value-of select="$hasChild"/>
<xsl:text>, $hasAttributes=</xsl:text>
<xsl:value-of select="$hasAttributes"/>
</xsl:if>

						<!-- toStringClassicVRML() encoding -->
						<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Recursive method to provide ClassicVRML string serialization.
	 * @param level number of levels of indentation for this element
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/grammar.html">Extensible 3D (X3D) encodings Part 2: Classic VRML encoding, Annex A: Grammar</a>
	 * @return ClassicVRML string
	 */
	@Override
	public String toStringClassicVRML(int level)
	{
		StringBuilder stringClassicVRML = new StringBuilder();]]></xsl:text>
	<xsl:if test="not($name = 'CommentsBlock')">
		<xsl:text><![CDATA[
		boolean hasAttributes = ]]></xsl:text>
		<xsl:value-of select="$hasAttributes"/>
		<xsl:text><![CDATA[; // TODO further refinement
		boolean      hasChild = ]]></xsl:text>
		<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
			<xsl:text>(IS != null) || </xsl:text>
		</xsl:if>
		<xsl:variable name="fieldsList" select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
														((@accessType='initializeOnly') or (@accessType='inputOutput'))]"/>
		<xsl:for-each select="$fieldsList">
			<xsl:variable name="isX3dStatement">
				<xsl:call-template name="isX3dStatement">
					<xsl:with-param name="name" select="@name"/>
				</xsl:call-template>
			</xsl:variable>
			
			<xsl:choose>
				<xsl:when test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
					<xsl:text>(!fieldList.isEmpty()) || (!sourceCode.isEmpty()) || </xsl:text>
				</xsl:when>
				<xsl:when test="($name = 'ProtoInstance')">
					<xsl:text>(!fieldValueList.isEmpty()) || </xsl:text>
				</xsl:when>
			</xsl:choose>
			<xsl:choose>
				<xsl:when test="(@type = 'SFNode')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="@name"/>
					<xsl:text> != null)</xsl:text>
				</xsl:when>
				<xsl:otherwise><!-- (@type='MFNode') -->
					<xsl:text>(!</xsl:text>
					<xsl:value-of select="@name"/>
					<xsl:if test="($isX3dStatement = 'true')">
						<xsl:text>List</xsl:text><!-- append to member name -->
					</xsl:if>
					<xsl:text>.isEmpty())</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			
			<xsl:if test="(last() > position()) or not($hasChildrenField = 'true')">
				<xsl:text> || </xsl:text>
			</xsl:if>
		</xsl:for-each>
		<xsl:choose>
			<xsl:when test="not($hasChildrenField = 'true')">
				<xsl:text disable-output-escaping="yes">!commentsList.isEmpty()</xsl:text>
			</xsl:when>
			<xsl:when test="1 > count($fieldsList)">
				<xsl:text>false</xsl:text><!-- TODO account for CommentsBlock -->
			</xsl:when>
		</xsl:choose>
		<xsl:text>;</xsl:text><!-- hasChild definition complete -->
	</xsl:if>
	<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		if (getUSE().length() > 0)
		{
			hasAttributes = false;
			hasChild      = false; // USE nodes include no other fields
		}]]></xsl:text><!-- append to member name -->
	</xsl:if>
	<xsl:if test="not((@name = 'X3D') or (@name = 'head') or (@name = 'meta') or (@name = 'unit') or (@name = 'component') or (@name = 'Scene'))">
		<!-- avoid defining indentCharacter for nodes with no indentation, helps to ensure that consistent logic follows -->
		<xsl:text disable-output-escaping="yes"><![CDATA[
		StringBuilder  indent = new StringBuilder();
		char  indentCharacter = ConfigurationProperties.getIndentCharacter();
		int   indentIncrement = ConfigurationProperties.getIndentIncrement();
		for (int i = 0; i < (level * indentIncrement); i++)
			indent.append(indentCharacter); // level of indentation for this level
]]></xsl:text>			
	</xsl:if>			
		
		<!-- preliminary special handling of statement names themselves, then proceed with additional content -->
		<xsl:choose>
			<xsl:when test="($name = 'X3D')">
				<!-- header needed for serialization toStringClassicVRML -->
				<xsl:text>
		stringClassicVRML.append("#X3D V").append(version).append(" utf8").append("\n");
		stringClassicVRML.append("PROFILE").append(" ").append(profile).append("\n");</xsl:text>
			</xsl:when>
			<xsl:when test="(@name = 'head') or (@name = 'Scene')">
				<!-- special output provided separately by X3D, only mention name as a comment here -->
				<xsl:text>
		stringClassicVRML.append("# </xsl:text><xsl:value-of select="@name"/><xsl:text>").append("\n");</xsl:text>
			</xsl:when>
		</xsl:choose>
		<!-- keep these xsl:choose statements separate -->
		<xsl:choose>
			<xsl:when test="($name = 'CommentsBlock')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		for (String comment : commentsList)
		{
			stringClassicVRML.append("# ").append(comment).append("\n").append(indent);
		}]]></xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'component')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		// http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/concepts.html#ComponentStatementSyntax
		stringClassicVRML.append("COMPONENT ").append(name).append(":").append(getLevel()).append("\n");
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'meta')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		// http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/concepts.html#METAStatementSyntax
		stringClassicVRML.append("META \"").append(name).append("\" \"").append(content).append("\"").append("\n");
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'unit')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		// http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/concepts.html#UNITStatementSyntax
		stringClassicVRML.append("UNIT ").append(category).append(" ").append(name).append(" ").append(conversionFactor).append("\n");
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="($name = 'ROUTE')">
				<!-- formatting note: "TO" preceded by tab character to alight consecutive ROUTE outputs, for some cases -->
				<xsl:text disable-output-escaping="yes"><![CDATA[
		stringClassicVRML.append("ROUTE ").append(fromNode).append(".").append(fromField)
			.append(" TO ").append(toNode).append(".").append(toField).append("\n").append(indent);
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@name = 'ProtoDeclare')">
				<!-- special handling -->
				<xsl:text disable-output-escaping="yes"><![CDATA[
		stringClassicVRML.append("PROTO ").append(name).append(" [").append("\n").append(indent);
		
		if (!getAppinfo().equals(APPINFO_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("# [appinfo] ").append("\"").append(SFStringObject.toString(getAppinfo())).append("\"");
		}
		if (!getDocumentation().equals(DOCUMENTATION_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append("\n").append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("# [documentation] ").append("\"").append(SFStringObject.toString(getDocumentation())).append("\"").append("\n").append(indent).append(indentCharacter);
		}
				
		// recursively iterate over child elements

		if (ProtoInterface != null)
		{
			stringClassicVRML.append(ProtoInterface.toStringClassicVRML(level + indentIncrement));
			for (fieldObject nextField : ProtoInterface.getFieldList())
			{
				stringClassicVRML.append(nextField.toStringClassicVRML(level + indentIncrement));
			}
		}
		if (!commentsList.isEmpty())
		{
			CommentsBlock commentsBlock = new CommentsBlock(commentsList);
			stringClassicVRML.append(commentsBlock.toStringClassicVRML(level));
		}
		stringClassicVRML.append("] {").append("\n").append(indent);
					
		if (ProtoBody != null)
		{
			stringClassicVRML.append(ProtoBody.toStringClassicVRML(level + indentIncrement));
			for (X3DNode element : ProtoBody.getChildren())
			{
				stringClassicVRML.append(((X3DConcreteElement) element).toStringClassicVRML(level + indentIncrement));
			}
		}
		stringClassicVRML.append("}").append("\n").append(indent);
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@name = 'ExternProtoDeclare')">
				<!-- special handling -->
				<xsl:text disable-output-escaping="yes"><![CDATA[
		stringClassicVRML.append("EXTERNPROTO ").append(name).append(" [").append("\n").append(indent);
		
		if (!getAppinfo().equals(APPINFO_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("# [appinfo] ").append("\"").append(SFStringObject.toString(getAppinfo())).append("\"");
		}
		if (!getDocumentation().equals(DOCUMENTATION_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append("\n").append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("# [documentation] ").append("\"").append(SFStringObject.toString(getDocumentation())).append("\"").append("\n").append(indent).append(indentCharacter);
		}
		if (getUrl().length > 0)
		{
			stringClassicVRML.append("\n").append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("url ").append("[ ").append(MFStringObject.toString(getUrl())).append(" ]");
		}
				
		// recursively iterate over child elements

		for (fieldObject element : fieldList)
		{
			stringClassicVRML.append(((X3DConcreteElement)element).toStringClassicVRML(level));
		}
		if (!commentsList.isEmpty())
		{
			CommentsBlock commentsBlock = new CommentsBlock(commentsList);
			stringClassicVRML.append(commentsBlock.toStringClassicVRML(level));
		}
		stringClassicVRML.append("]").append("\n").append(indent);]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@name = 'ProtoInterface') or (@name = 'ProtoBody')">
				<!-- special output provided separately by ProtoDeclare, only mention name as a comment here -->
				<xsl:text>
		stringClassicVRML.append("# </xsl:text><xsl:value-of select="@name"/><xsl:text>").append("\n").append(indent);</xsl:text>
			</xsl:when>
			<xsl:otherwise>
			<!-- DEF, USE, name attributes first for readability and to match X3D Canonical Form -->
			<xsl:if test="InterfaceDefinition/field[@name = 'DEF']">
				<xsl:text>
		if (!getDEF().equals(DEF_DEFAULT_VALUE))
		{
			stringClassicVRML.append("DEF ").append(SFStringObject.toString(getDEF())).append(" ");
		}</xsl:text>
			</xsl:if>
			<xsl:if test="InterfaceDefinition/field[@name = 'USE']">
				<xsl:text>
		if (!getUSE().equals(USE_DEFAULT_VALUE))
		{
			 stringClassicVRML.append("USE ").append(SFStringObject.toString(getUSE())).append("\n");
		}
		else // only have further output if not a USE node
		{</xsl:text>
				<!-- all done with this USE node -->
			</xsl:if>
			<xsl:choose>
				<xsl:when test="($name = 'ProtoInstance')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
			if (getName().isEmpty())
				 stringClassicVRML.append("NoNameFoundError");
			else stringClassicVRML.append(getName());
			stringClassicVRML.append(" { "); // define ProtoInstance node name, fieldValue content follows
]]></xsl:text>
				</xsl:when>
				<xsl:when test="not($isX3dStatement = 'true')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
			stringClassicVRML.append("]]></xsl:text><xsl:value-of select="$name"/><xsl:text><![CDATA[").append(" { "); // define node name, node content follows
]]></xsl:text>
				</xsl:when>
			</xsl:choose>
			<xsl:if test="not($isX3dStatement = 'true') and not($name = 'Script')">
				<xsl:text>
			if (hasAttributes || hasChild)
			{</xsl:text>
				<xsl:text>
				stringClassicVRML.append("\n")</xsl:text>
			<xsl:text>.append(indent).append(indentCharacter); // fields for this node follow</xsl:text>
			<xsl:text>
			}</xsl:text>
			</xsl:if>
			
			<xsl:if test="($name = 'fieldValue')">
				<xsl:text>
		// fieldValue type is figured out using ProtoDeclare/ExternProtoDeclare field getType()</xsl:text>
			</xsl:if>
			<xsl:choose>
				<!-- special handling -->
				<xsl:when test="($name = 'field') or ($name = 'fieldValue')">
					<xsl:text>
		// </xsl:text>
		<xsl:value-of select="$name"/>
					<xsl:text> definition
		stringClassicVRML.append("\n").append(indent).append(indentCharacter).append(indentCharacter)</xsl:text>
					<xsl:if test="($name = 'field')">
						<xsl:text disable-output-escaping="yes">.append(accessType).append(" ").append(type).append(" ")</xsl:text>
					</xsl:if>
					<!-- getType() defined for both field and fieldValue -->
					<xsl:text disable-output-escaping="yes"><![CDATA[.append(name);
		if (value.length() > 0)
		{
			stringClassicVRML.append(" ");
			if (getType().equals("SFString"))
				 stringClassicVRML.append("\"").append(value).append("\"");
			else stringClassicVRML             .append(value);
		}]]></xsl:text>
					<xsl:if test="($name = 'field')">
						<!-- append field [appinfo], add field [documentation] -->
						<xsl:text disable-output-escaping="yes"><![CDATA[
		if (!getAppinfo().equals(APPINFO_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append(" # [appinfo] ").append("\"").append(SFStringObject.toString(getAppinfo())).append("\"").append("\n").append(indent).append(indentCharacter);
		}
		if (!getDocumentation().equals(DOCUMENTATION_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())
		{
			stringClassicVRML.append("\n").append(indent).append(indentCharacter).append(indentCharacter);
			stringClassicVRML.append("# [documentation] ").append("\"").append(SFStringObject.toString(getDocumentation())).append("\"").append("\n").append(indent).append(indentCharacter);
		}]]></xsl:text>
					</xsl:if>
					<xsl:text disable-output-escaping="yes"><![CDATA[
		stringClassicVRML.append("\n");
]]></xsl:text>
				</xsl:when>
				<xsl:otherwise>
			<xsl:text>
			if (hasAttributes)
			{</xsl:text>
			<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
				boolean hasISconnect = (getIS() != null) && !getIS().getConnectList().isEmpty();]]></xsl:text>
			</xsl:if>
			<xsl:if test="(InterfaceDefinition/field[@name = 'name']) and not($name = 'ProtoInstance')">
				<xsl:text>
				if (!getName().equals(NAME_DEFAULT_VALUE))
				{
					stringClassicVRML.append("\n")</xsl:text>
				<xsl:if test="not($isX3dStatement = 'true')">
					<xsl:text>.append(indent).append(indentCharacter).append(indentCharacter)</xsl:text>
				</xsl:if>
				<xsl:text>.append("name ").append("\"").append(SFStringObject.toString(getName())).append("\"").append("\n")</xsl:text>
				<xsl:if test="not($isX3dStatement = 'true')">
					<xsl:text><![CDATA[.append(indent)]]></xsl:text>
				</xsl:if>
				<xsl:text>;
				}</xsl:text>
			</xsl:if>
				
			<xsl:for-each select="InterfaceDefinition/field[not(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and not(@name = 'DEF') and not(@name = 'USE') and not(@name = 'name') and
                                                            ((@accessType='initializeOnly') or (@accessType='inputOutput'))]">
				<xsl:variable name="fieldName" select="translate(@name,'-','_')"/><!-- handle http-equiv etc. -->
				<xsl:variable name="isSingleValueType">
					<xsl:value-of select="starts-with(@type,'SF') and not(contains(@type, 'Vec')) and not(contains(@type, 'Matrix'))"/>
				</xsl:variable>
				<xsl:variable name="CamelCaseName"><!-- upper camel case -->
					<xsl:choose>
						<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
							<!-- unmodified -->
							<xsl:value-of select="@name"/>
						</xsl:when>
						<xsl:when test="(@name = 'class')">
							<!-- getClass() is reserved by Java Object() class -->
							<xsl:text>CssClass</xsl:text>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="translate(substring($fieldName,1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
							<xsl:value-of select="substring($fieldName,2)"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>
				<xsl:variable name="javaType">
					<xsl:call-template name="javaType">
						<xsl:with-param name="x3dType" select="@type"/>
						<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
					</xsl:call-template>
				</xsl:variable>
<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
<xsl:text>// ($fieldName=</xsl:text>
<xsl:value-of select="$fieldName"/>
<xsl:text>, CamelCaseName=</xsl:text>
<xsl:value-of select="$CamelCaseName"/>
<xsl:text>, javaType=</xsl:text>
<xsl:value-of select="$javaType"/>
<xsl:text>, isSingleValueType=</xsl:text>
<xsl:value-of select="$isSingleValueType"/>
<xsl:text>)</xsl:text>
</xsl:message>
</xsl:if>
				<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
				if (hasISconnect)
				{
					for (connectObject element : getIS().getConnectList())
					{
						if (element.getNodeField().equals("]]></xsl:text><xsl:value-of select="@name"/><xsl:text><![CDATA["))
						{
							stringClassicVRML.append(indentCharacter).append("]]></xsl:text>
							<xsl:value-of select="@name"/>
							<xsl:text>").append(" IS ").append(element.getProtoField()).append("\n").append(indent).append(indentCharacter); // found matching connect
						}
					}
				}
				else </xsl:text>
				</xsl:if>
				<xsl:text>if (</xsl:text>
				<xsl:choose>
					<!-- avoided attributes -->
					<xsl:when test="($name = 'X3D')">
						<xsl:text><![CDATA[false) // attribute handled separately]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'ProtoInstance') and (@name = 'name')">
						<!-- name attribute handled previously -->
					</xsl:when>
					<!-- required attributes -->
					<xsl:when test="(($name = 'X3D') and (($fieldName = 'profile') or ($fieldName = 'version'))) or
									(($name = 'HAnimHumanoid') and ($fieldName = 'version')) or
									(($name = 'component') and ($fieldName = 'level')) or
									(($name = 'unit')      and ($fieldName = 'conversionFactor'))">
						<xsl:text><![CDATA[true) // required attribute]]></xsl:text>
					</xsl:when>
					<xsl:when test="(@type = 'SFBool') or (@type = 'SFInt32') or (@type = 'SFFloat') or (@type = 'SFDouble') or (@type = 'SFTime')">
						<xsl:text><![CDATA[(get]]></xsl:text>
						<xsl:value-of select="$CamelCaseName"/>
						<xsl:text disable-output-escaping="yes"><![CDATA[() != ]]></xsl:text>
						<xsl:value-of select="upper-case($fieldName)"/>
						<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
					</xsl:when>
					<xsl:when test="contains($javaType, 'ArrayList')">
						<xsl:text><![CDATA[get]]></xsl:text>
						<xsl:value-of select="$CamelCaseName"/>
						<xsl:text disable-output-escaping="yes"><![CDATA[().length > 0)]]></xsl:text>
					</xsl:when>
					<xsl:when test="($isSingleValueType = 'true')">
						<xsl:text><![CDATA[!get]]></xsl:text>
						<xsl:value-of select="$CamelCaseName"/>
						<xsl:text><![CDATA[().equals(]]></xsl:text>
						<xsl:value-of select="upper-case($fieldName)"/>
						<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
					</xsl:when>
					<xsl:when test="(string-length(@default) > 0)">
						<xsl:text><![CDATA[!Arrays.equals(get]]></xsl:text>
						<xsl:value-of select="$CamelCaseName"/>
						<xsl:text><![CDATA[(), ]]></xsl:text>
						<xsl:value-of select="upper-case($fieldName)"/>
						<xsl:text><![CDATA[_DEFAULT_VALUE) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text><![CDATA[(get]]></xsl:text>
						<xsl:value-of select="$CamelCaseName"/>
						<xsl:text disable-output-escaping="yes"><![CDATA[().length > 0) || ConfigurationProperties.isShowDefaultAttributes())]]></xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			
				<!-- output simple-field value -->
				<xsl:text><![CDATA[
				{
					stringClassicVRML]]></xsl:text>
				<xsl:text><![CDATA[.append("]]></xsl:text>
				<!-- unsupported attribute -->
				<xsl:if test="(@name = 'class')">
					<xsl:text># </xsl:text>
				</xsl:if>
				<xsl:value-of select="$fieldName"/>
				<xsl:text> ")</xsl:text>
				<xsl:choose>
					<xsl:when test="(@type = 'SFString')">
						<xsl:text>.append("\"")</xsl:text>
					</xsl:when>
					<xsl:when test="starts-with(@type, 'MF')">
						<xsl:text>.append("[ ")</xsl:text>
					</xsl:when>
				</xsl:choose>
				<xsl:text>.append(</xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:value-of select="$jsaiClassSuffix"/>
				<xsl:text>.toString(get</xsl:text>
				<xsl:value-of select="$CamelCaseName"/>
				<xsl:text>()))</xsl:text>
				<xsl:choose>
					<xsl:when test="(@type = 'SFString')">
						<xsl:text>.append("\"")</xsl:text>
					</xsl:when>
					<xsl:when test="starts-with(@type, 'MF')">
						<xsl:text>.append(" ]")</xsl:text>
					</xsl:when>
				</xsl:choose>
				<xsl:text>.append("\n")</xsl:text>
				<xsl:if test="not($isX3dStatement = 'true')">
					<xsl:text><![CDATA[.append(indent).append(indentCharacter)]]></xsl:text>
				</xsl:if>
				<xsl:text>;
				}</xsl:text>
			</xsl:for-each>
			
						<xsl:text disable-output-escaping="yes"><![CDATA[
			}]]></xsl:text>
						<xsl:if test="InterfaceDefinition/field[@name = 'USE']">
							<xsl:text>
		}</xsl:text>
						</xsl:if> <!-- end hasAttributes -->
					</xsl:otherwise>
				</xsl:choose>

				<xsl:text disable-output-escaping="yes"><![CDATA[
		if (hasChild) // has contained node(s), comment(s), IS/connect and/or source code
		{]]></xsl:text>
				<xsl:text>
			// recursively iterate over child element</xsl:text>
				<xsl:if test="InterfaceDefinition/field[(@type = 'MFNode')] or
					   (count(InterfaceDefinition/field[contains(@type,'FNode')]) > 1)">
					<xsl:text>s</xsl:text>
				</xsl:if>
				<xsl:text>&#10;</xsl:text>

			<xsl:for-each select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
															((@accessType='initializeOnly') or (@accessType='inputOutput')) and
                                                            not(@name = 'meta')]">
				<!-- special order for head elements: meta comes last, handled afterwards -->
				<!-- sort ProtoInterface before ProtoBody -->
				<xsl:sort select="(@name = 'ProtoBody')"/>
				<xsl:sort select="(@name = 'ProtoInterface')"/>
				<!-- TODO have ProtoDeclare handle ProtoBody and ProtoInterface -->
				
				<xsl:variable name="javaType">
					<xsl:call-template name="javaType">
						<xsl:with-param name="x3dType" select="@type"/>
						<xsl:with-param name="isInterface" select="$isInterface"/>
					</xsl:call-template>
				</xsl:variable>
				<xsl:variable name="javaReferenceType">
					<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
				</xsl:variable>
				<xsl:variable name="isFieldX3dStatement">
					<xsl:call-template name="isX3dStatement">
						<xsl:with-param name="name" select="@name"/>
					</xsl:call-template>
				</xsl:variable>

				<xsl:choose>
					<xsl:when test="(@type = 'X3D') or (@type = 'head') or (@type = 'Scene')">
						<!-- already handled -->
					</xsl:when>
					<xsl:when test="(@type = 'SFNode')">
						<xsl:text><![CDATA[
			if (]]></xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:text><![CDATA[ != null)
			{]]></xsl:text>
						<xsl:if test="not($isX3dStatement = 'true')">
							<!-- TODO containerField name alternatives -->
							<xsl:text><![CDATA[
				stringClassicVRML.append(indentCharacter).append("]]></xsl:text>
							<xsl:value-of select="@name"/>
							<xsl:text>").append(" "); // containerField for SFNode</xsl:text><!-- watch out for CommentsBlock or ROUTE -->
						</xsl:if>
						<!-- cast abstract element to concrete type -->
						<xsl:text>
				stringClassicVRML.append(((X3DConcreteElement) </xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:choose>
							<xsl:when test="not($isX3dStatement = 'true')">
								<xsl:text>).toStringClassicVRML(level + indentIncrement));
				stringClassicVRML.append(indent); // end SFNode</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:text>).toStringClassicVRML(level)); // end X3D statement</xsl:text>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:text>
			}</xsl:text>
						<xsl:if test="not($isX3dStatement = 'true')"><!-- output ProtoInstance -->
							<xsl:text>
			else if (</xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:text><![CDATA[ProtoInstance != null)
			{
				stringClassicVRML.append(indentCharacter).append("]]></xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:text>").append(" "); // containerField for SFNode</xsl:text><!-- watch out for CommentsBlock or ROUTE -->
						<!-- cast abstract element to concrete type, output ProtoInstance alternative (if present) -->
						<xsl:text>
				stringClassicVRML.append(((X3DConcreteElement) </xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:text>ProtoInstance).toStringClassicVRML(level + indentIncrement));
				stringClassicVRML.append(indent); // end SFNode ProtoInstance
			}</xsl:text>
						</xsl:if>
					</xsl:when>
					<xsl:otherwise> <!-- MFNode -->
						<xsl:choose>
							<xsl:when test="not($isX3dStatement = 'true') or (@name = 'ROUTE')">
								<xsl:text>
			if (</xsl:text>
								<xsl:value-of select="@name"/>
								<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
									<xsl:text>List</xsl:text><!-- append to member name -->
								</xsl:if>
								 <xsl:text disable-output-escaping="yes"><![CDATA[.size() > 0)
			{
				stringClassicVRML.append(indentCharacter).append(indentCharacter).append("]]></xsl:text>
								<!-- TODO containerField name alternatives -->
								<xsl:value-of select="@name"/>
								<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
									<xsl:text>List</xsl:text><!-- append to member name -->
								</xsl:if>
								<xsl:text>").append(" [").append("\n")
					.append(indent).append(indentCharacter).append(indentCharacter); // containerField for MFNode array</xsl:text>
							</xsl:when>
							<xsl:otherwise>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:text>
			for (</xsl:text>
						<xsl:value-of select="$javaReferenceType"/>
						<xsl:text> element : </xsl:text>
						<xsl:value-of select="@name"/>
						<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
							<xsl:text>List</xsl:text><!-- append to member name -->
						</xsl:if>
						<xsl:text>)
			{</xsl:text>
						<!-- cast abstract element to concrete type -->
						<xsl:text>
				stringClassicVRML.append(((X3DConcreteElement</xsl:text>
						<xsl:choose>
							<xsl:when test="not($isX3dStatement = 'true') or (@name = 'ROUTE')">
								<xsl:text><![CDATA[)element).toStringClassicVRML(level + indentIncrement + indentIncrement))]]></xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:text><![CDATA[)element).toStringClassicVRML(level))]]></xsl:text>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:text>;</xsl:text>
						
						<xsl:if test="not((@type = 'X3D') or (@type = 'head') or (@type = 'Scene'))">
							<xsl:text>
			}</xsl:text>
						</xsl:if>
			
						<xsl:if test="not($isX3dStatement = 'true') or (@name = 'ROUTE')">
							<xsl:text>
				stringClassicVRML.append(indent).append(indentCharacter).append(indentCharacter).append("]").append("\n")
					.append(indent); // end MFNode array
			}
</xsl:text>
						</xsl:if>
			
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>
			
			<xsl:if test="($name = 'head')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
			// note required order of component, unit, meta (though relaxation of this requirement has been proposed)
			for (metaObject element : metaList)
			{
				 stringClassicVRML.append(((metaObject)element).toStringClassicVRML(level));
			}
]]></xsl:text>
			</xsl:if>
			
			<!-- special handling -->
			<xsl:choose>
				<xsl:when test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
					<xsl:text disable-output-escaping="yes"><![CDATA[

			for (fieldObject element : fieldList)
			{
				 stringClassicVRML.append(((fieldObject)element).toStringClassicVRML(level + indentIncrement));
			}
			if (sourceCode.trim().length() > 0)
			{
				String trimmedSource = sourceCode; // workaround, TODO fix BS Contact bug with leading whitespace
				stringClassicVRML.append(indent).append(indentCharacter).append(indentCharacter)
					.append("url [ \"").append(sourceCode).append("\n").append("\" ]").append("\n");
			}
]]></xsl:text>
				</xsl:when>
			</xsl:choose>
			
			<xsl:if test="(not($hasChildrenField = 'true') and not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
							not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock') and not($name = 'CADPart'))">
				<xsl:text><![CDATA[
			if (!commentsList.isEmpty())
			{
				CommentsBlock commentsBlock = new CommentsBlock(commentsList);]]></xsl:text>
				<xsl:choose>
					<xsl:when test="not($isX3dStatement = 'true')">
						<xsl:text>
				stringClassicVRML.append(commentsBlock.toStringClassicVRML(level));
				stringClassicVRML.append(indent); // end SFNode
			}</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>
				stringClassicVRML.append(commentsBlock.toStringClassicVRML(level));
			}</xsl:text>
						
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
			
			<xsl:text disable-output-escaping="yes"><![CDATA[
		}]]></xsl:text>
			<xsl:if test="not($isX3dStatement = 'true')">
				<xsl:text>
		if (hasAttributes || hasChild)
		{
			stringClassicVRML.append("}").append("\n"); // finish node content
		}</xsl:text>
			</xsl:if>
			</xsl:otherwise>
		</xsl:choose>

		<xsl:if test="($name = 'ProtoInstance')">
			<xsl:text disable-output-escaping="yes"><![CDATA[
		stringClassicVRML.append(indent).append("}").append("\n"); // finish closing tag]]></xsl:text>
		</xsl:if>
			
		<xsl:text disable-output-escaping="yes"><![CDATA[
		return stringClassicVRML.toString();
	}
]]></xsl:text>
						</xsl:if>
					
						<!-- toStringVRML97() -->
						<xsl:if test="not(starts-with($thisClassName, 'X3DConcrete'))">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Recursive method to provide VRML97 string serialization.
	 * @param level number of levels of indentation for this element
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772/V2.0/index.html">Virtual Reality Modeling Language (VRML) 97 specification</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772-1/V2.1/index.html">VRML 97 v2.1 Amendment</a>
	 * @return VRML97 string
	 */
	@Override
	public String toStringVRML97(int level)
	{
		return toStringClassicVRML(level)]]></xsl:text>
	<xsl:choose>
		<xsl:when test="($name = 'X3D')">
			<!-- TODO fix this hack more thoroughly, possibly via ConfigurationProperties or else by optional parameter in method signature -->
			<xsl:text>.replace("#X3D V3.3 utf8","#VRML V2.0 utf8").replace("PROFILE ","#PROFILE ")
		.replace("COMPONENT ","#COMPONENT ").replace("META ","#META ").replace("UNIT ","#UNIT "); // hide unavailable X3D feature</xsl:text>s
		</xsl:when>
		<xsl:when test="($name = 'component')">
			<xsl:text>.replace("COMPONENT ","#COMPONENT "); // hide unavailable X3D feature</xsl:text>
		</xsl:when>
		<xsl:when test="($name = 'meta')">
			<xsl:text>.replace("META ","#META "); // hide unavailable X3D feature</xsl:text>
		</xsl:when>
		<xsl:when test="($name = 'component')">
			<xsl:text>.replace("UNIT ","#UNIT "); // hide unavailable X3D feature</xsl:text>
		</xsl:when>
		<xsl:otherwise>
			<xsl:text>;</xsl:text>
		</xsl:otherwise>
	</xsl:choose>
	<xsl:text disable-output-escaping="yes"><![CDATA[
	}
]]></xsl:text>
						</xsl:if>
					
						<!-- getNodeByDEF() -->
						<xsl:if test="(not($isX3dStatement = 'true') and not($name = 'CommentsBlock') and not(starts-with($thisClassName, 'X3DConcrete'))) or
									  ($name = 'ProtoInstance') or ($name = 'Scene')"><!-- Scene includes nodes with DEF -->
							<xsl:text>
	/**
	 * Recursive method to provide object reference to node by DEF name, if found as this node or in a contained node.
	 * @param DEFname DEF name of node to find
	 * @return object reference to node
	 */</xsl:text>
							<xsl:if test="not($name = 'Scene')">
								<xsl:text>
	@Override</xsl:text>
							</xsl:if>
								<xsl:text>
	public X3DConcreteNode getNodeByDEF(String DEFname)
	{
		X3DConcreteNode referenceNode;
</xsl:text>
							<xsl:if test="not($name = 'Scene')">
								<xsl:text>
		if (getDEF().equals(DEFname))
			return this;
</xsl:text>
							</xsl:if>
							
							<xsl:for-each select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
															((@accessType='initializeOnly') or (@accessType='inputOutput'))]">
								<xsl:variable name="isFieldX3dStatement">
									<xsl:call-template name="isX3dStatement">
										<xsl:with-param name="name" select="@name"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaType">
									<xsl:call-template name="javaType">
										<xsl:with-param name="x3dType" select="@type"/>
										<xsl:with-param name="isInterface" select="$isInterface"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaReferenceType">
									<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
								</xsl:variable>
								<xsl:choose>
									<xsl:when test="($isFieldX3dStatement = 'true')">
										<!-- ignore, statements do not include DEF -->
									</xsl:when>
									<xsl:when test="(@type = 'SFNode')">
										<xsl:text>
		if (</xsl:text><xsl:value-of select="@name"/><xsl:text> != null)
		{
			referenceNode = ((X3DConcreteNode) </xsl:text><xsl:value-of select="@name"/><xsl:text>).getNodeByDEF(DEFname); // SFNode
			if (referenceNode != null)
				return referenceNode;
		}</xsl:text>
									</xsl:when>
									<xsl:when test="(@type = 'MFNode')">
										<xsl:text>
		for (</xsl:text>
		<xsl:value-of select="$javaReferenceType"/>
		<xsl:text> element : </xsl:text><xsl:value-of select="@name"/><xsl:text>) // MFNode
		{
			if (element instanceof X3DConcreteNode)
			{
				if (((X3DConcreteNode) element).getDEF().equals(DEFname))
					return (X3DConcreteNode) element; // found, this node
			
				// not yet found, continue with depth-first search of current child element
				referenceNode = ((X3DConcreteNode) element).getNodeByDEF(DEFname);
				if (referenceNode != null)
					return referenceNode; // found in child
			}
		}</xsl:text>
									</xsl:when>
								</xsl:choose>
							</xsl:for-each>
	<xsl:text disable-output-escaping="yes"><![CDATA[
		return null; // not found, in this node or in chilren nodes
	}
]]></xsl:text>
						</xsl:if>
					
						<!-- getElementByName() -->
						<xsl:if test="not(starts-with($thisClassName, 'X3DConcrete'))">
							<xsl:text>
	/**
	 * Recursive method to provide object reference to node or statement by name, if found as this element or in a contained element.
	 * Elements of interest: ProtoDeclare/ExternProtoDeclare/ProtoInstance, H-Anim nodes
	 * @param elementName name of element to find
	 * @return object reference to element
	 */
	public X3DConcreteElement getElementByName(String elementName)
	{
		X3DConcreteElement referenceElement;
</xsl:text>
							<xsl:if test="InterfaceDefinition/field[@name = 'name']">
								<xsl:text>
		if (getName().equals(elementName))
			return this;
</xsl:text>
							</xsl:if>
							
							<xsl:for-each select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
															((@accessType='initializeOnly') or (@accessType='inputOutput'))]">
								<xsl:variable name="isFieldX3dStatement">
									<xsl:call-template name="isX3dStatement">
										<xsl:with-param name="name" select="@name"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaType">
									<xsl:call-template name="javaType">
										<xsl:with-param name="x3dType" select="@type"/>
										<xsl:with-param name="isInterface" select="$isInterface"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaReferenceType">
									<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
								</xsl:variable>
								<xsl:choose>
									<xsl:when test="(@name = 'field') or (@name = 'fieldValue')">
										<xsl:text>
		for (</xsl:text>
		<xsl:value-of select="@name"/>
		<xsl:text>Object element : </xsl:text><xsl:value-of select="@name"/><xsl:text>List)
		{
			if (element instanceof X3DConcreteElement)
			{
				referenceElement = ((X3DConcreteElement) element).getElementByName(elementName);
				if (referenceElement != null)
					return referenceElement;
			}
		}</xsl:text>
									</xsl:when>
									<xsl:when test="(@type = 'SFNode') or (@name = 'ProtoDeclare') or (@name = 'ExternProtoDeclare') or (@name = 'ProtoInstance')">
										<xsl:text>
		if (</xsl:text><xsl:value-of select="@name"/><xsl:text> != null)
		{
			referenceElement = ((X3DConcreteElement) </xsl:text><xsl:value-of select="@name"/><xsl:text>).getElementByName(elementName);
			if (referenceElement != null)
				return referenceElement;
		}</xsl:text>
									</xsl:when>
									<xsl:when test="(@type = 'MFNode') and 
													(not($isFieldX3dStatement = 'true') or starts-with(@name,'field'))">
										<xsl:text>
		for (</xsl:text>
		<xsl:value-of select="$javaReferenceType"/>
		<xsl:text> element : </xsl:text><xsl:value-of select="@name"/><xsl:text>) // MFNode
		{
			if (element instanceof X3DConcreteElement)
			{
				referenceElement = ((X3DConcreteElement) element).getElementByName(elementName);
				if (referenceElement != null)
					return referenceElement;
			}
		}</xsl:text>
									</xsl:when>
								</xsl:choose>
							</xsl:for-each>
	<xsl:text disable-output-escaping="yes"><![CDATA[
		return null; // not found, in this element or in child elements
	}
]]></xsl:text>
						</xsl:if>
					
						<!-- validate() -->
						<xsl:if test="not(starts-with($thisClassName, 'X3DConcrete'))">
							<xsl:text>
		
	/**
	 * Recursive method to validate this element plus all contained nodes and statements.
	 * @return validation results
	 */
	@Override
	public String validate()
	{
		validationResult = new StringBuilder(); // prepare for updated results
</xsl:text>
							<xsl:for-each select="InterfaceDefinition/field[(contains(@type,'FNode')) and not(starts-with(@name,'set')) and not(ends-with(@name,'changed')) and 
															((@accessType='initializeOnly') or (@accessType='inputOutput'))]">
								<xsl:variable name="isFieldX3dStatement">
									<xsl:call-template name="isX3dStatement">
										<xsl:with-param name="name" select="@name"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaType">
									<xsl:call-template name="javaType">
										<xsl:with-param name="x3dType" select="@type"/>
										<xsl:with-param name="isInterface" select="$isInterface"/>
									</xsl:call-template>
								</xsl:variable>
								<xsl:variable name="javaReferenceType">
									<xsl:value-of select="substring-before(substring-after($javaType,'&lt;'),'&gt;')"/>
								</xsl:variable>
								<xsl:variable name="CamelCaseName"><!-- upper camel case -->
									<xsl:choose>
										<xsl:when test="starts-with(@name,'set_')">
											<xsl:value-of select="translate(substring(substring-after(@name,'set_'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
											<xsl:value-of select="substring(substring-after(@name,'set_'),2)"/>
										</xsl:when>
										<xsl:when test="starts-with(@name,'set')">
											<xsl:value-of select="translate(substring(substring-after(@name,'set'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
											<xsl:value-of select="substring(substring-after(@name,'set'),2)"/>
										</xsl:when>
										<xsl:when test="contains(@name,'_changed')">
											<xsl:value-of select="translate(substring(substring-before(@name,'_changed'),1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
											<xsl:value-of select="substring(substring-before(@name,'_changed'),2)"/>
										</xsl:when>
										<xsl:when test="(@name = 'DEF') or (@name = 'USE')">
											<!-- unmodified -->
											<xsl:value-of select="@name"/>
										</xsl:when>
										<xsl:when test="(@name = 'class')">
											<!-- getClass() is reserved by Java Object() class -->
											<xsl:text>CssClass</xsl:text>
										</xsl:when>
										<xsl:otherwise>
											<xsl:value-of select="translate(substring(@name,1,1),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"/>
											<xsl:value-of select="substring(@name,2)"/>
										</xsl:otherwise>
									</xsl:choose>
								</xsl:variable>
							
								<xsl:choose>
									<xsl:when test="(@type = 'SFNode')">
										<xsl:text>
		if (</xsl:text><xsl:value-of select="@name"/><xsl:text> != null)
		{
			set</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>(get</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>());
			((X3DConcreteElement) </xsl:text><xsl:value-of select="@name"/><xsl:text>).validate(); // exercise field checks, SFNode
			validationResult.append(((X3DConcreteElement) </xsl:text><xsl:value-of select="@name"/><xsl:text>).getValidationResult());
		}</xsl:text>
				<xsl:if test="not($isX3dStatement = 'true')">
					<xsl:text>
		if (</xsl:text><xsl:value-of select="@name"/><xsl:text>ProtoInstance != null)
		{
			set</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>(get</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>ProtoInstance());
			((X3DConcreteElement) </xsl:text><xsl:value-of select="@name"/><xsl:text>ProtoInstance).validate(); // exercise field checks, SFNode
			validationResult.append(((X3DConcreteElement) </xsl:text><xsl:value-of select="@name"/><xsl:text>ProtoInstance).getValidationResult());
		}
		if ((</xsl:text>   <xsl:value-of select="@name"/><xsl:text disable-output-escaping="yes"><![CDATA[ != null) && (]]></xsl:text>
						   <xsl:value-of select="@name"/><xsl:text>ProtoInstance != null))
		{
			String errorNotice = "Internal Java SAI library error, illegal SFNode field, both </xsl:text><xsl:value-of select="@name"/><xsl:text> and </xsl:text>
				<xsl:value-of select="@name"/><xsl:text>ProtoInstance are set simultaneously";
			validationResult.append(errorNotice);
				throw new InvalidProtoException(errorNotice); // report error
		}</xsl:text>
				</xsl:if>
									</xsl:when>
									<xsl:when test="(@type = 'MFNode')">
										<xsl:text>
		for (</xsl:text>
		<xsl:value-of select="$javaReferenceType"/>
		<xsl:text> element : </xsl:text><xsl:value-of select="@name"/>
						<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
							<xsl:text>List</xsl:text><!-- append to member name -->
						</xsl:if>
						<xsl:text>) // MFNode
		{
			((X3DConcreteElement) element).validate(); // exercise field checks, MFNode element
			validationResult.append(((X3DConcreteElement) element).getValidationResult());
		}
		set</xsl:text><xsl:value-of select="$CamelCaseName"/>
						<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
							<xsl:text>List</xsl:text><!-- append to member name -->
						</xsl:if>
						<xsl:text>(get</xsl:text><xsl:value-of select="$CamelCaseName"/>
						<xsl:if test="($isFieldX3dStatement = 'true') and (@type='MFNode')">
							<xsl:text>List</xsl:text><!-- append to member name -->
						</xsl:if>
						<xsl:text>()); // also test getter/setter validation
</xsl:text>
									</xsl:when>
									<xsl:otherwise>
										<xsl:text>
		set</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>(get</xsl:text><xsl:value-of select="$CamelCaseName"/><xsl:text>()); // exercise field checks, simple types
</xsl:text>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:for-each>
							
							<!-- Special validation tests -->
							<!-- TODO regular expresions (regexes) -->
							
							<xsl:choose>
								<xsl:when test="(@name = 'ROUTE')">
									<xsl:text disable-output-escaping="yes"><![CDATA[
		// TODO NMTOKEN checks for no whitespace, hopefully handled automatically once support added

		// check ROUTE node-type validity; note that each ROUTE must already be connected to scene graph
		
		String errorNotice = new String();
		String ROUTE_description = "      FROM " + 
				fromNode + "." + fromField + " TO " +
				  toNode + "." +   toField;
										
		if (getAncestorSceneObject() == null)
		{
			errorNotice += "ROUTE is not connected to a scene graph and cannot be checked.";
			validationResult.append(errorNotice).append("\n").append(ROUTE_description).append("\n");
		}
		else
		{
			X3DConcreteNode fromNodeObject = getAncestorSceneObject().getNodeByDEF(fromNode);
			X3DConcreteNode   toNodeObject = getAncestorSceneObject().getNodeByDEF(  toNode);

			String  fromNodeType = fromNodeObject.getClass().getSimpleName().split("Object")[0]; // substring-before Object
			String    toNodeType =   toNodeObject.getClass().getSimpleName().split("Object")[0]; // substring-before Object

			String       fromFieldType = fromNodeObject.getType      (fromField);
			String         toFieldType =   toNodeObject.getType      (  toField);
			String fromFieldAccessType = fromNodeObject.getAccessType(fromField);
			String   toFieldAccessType =   toNodeObject.getAccessType(  toField);
										
			ROUTE_description = "      FROM " + 
				fromNode + "." + fromField + " (" + fromNodeType + "." + fromFieldType + "." + fromFieldAccessType + ") TO " +
				  toNode + "." +   toField + " (" +   toNodeType + "." +   toFieldType + "." +   toFieldAccessType + ")";

			if (!fromFieldType.equals(toFieldType))
			{
				errorNotice += "ROUTE has source-destination type mismatch. ";
			}
			if (!fromFieldAccessType.equals(fieldObject.ACCESSTYPE_INPUTOUTPUT) &&
				!fromFieldAccessType.equals(fieldObject.ACCESSTYPE_OUTPUTONLY))
			{
				errorNotice += "ROUTE event source must have accessType='inputOutput' or accessType='outputOnly'. ";
			}
			if (!  toFieldAccessType.equals(fieldObject.ACCESSTYPE_INPUTOUTPUT) &&
				!  toFieldAccessType.equals(fieldObject.ACCESSTYPE_INPUTONLY))
			{
				errorNotice += "ROUTE event destination must have accessType='inputOutput' or accessType='outputOnly'. ";
			}
			if (!errorNotice.isEmpty())
			{
				validationResult.append(errorNotice).append("\n").append(ROUTE_description).append("\n");
				throw new InvalidFieldValueException(errorNotice + ", " + ROUTE_description);
			}
		}
]]></xsl:text>
								</xsl:when>
								<!-- ProtoBody might contain only comments
								<xsl:when test="(@name = 'ProtoBody')">
									<xsl:text disable-output-escaping="yes"><![CDATA[
		if ((primaryNode == null) && !getChildren().isEmpty()) // must have primaryNode if any children are present
		{
			String errorNotice = "ProtoBody primaryNode is null, but getChildren() has" + getChildren().size() + " entries";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidProtoException(errorNotice); // report error
		}
]]></xsl:text>
								</xsl:when> -->
							</xsl:choose>
							
							<xsl:if test="not($isX3dStatement = 'true') and not($name = 'CommentsBlock')">
								<xsl:text disable-output-escaping="yes"><![CDATA[
		if (getIS() != null)
		{
			if (getIS().getConnectList().isEmpty())
			{
				String errorNotice = "IS statement present, but contains no connect statements";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidProtoException(errorNotice); // report error
			}				
			// TODO also check that this node has ancestor ProtoBody, and that a field with same name also exists, so that IS is legal
		}]]></xsl:text>
							</xsl:if>

							<xsl:text>
		return validationResult.toString();
	}
</xsl:text>
						</xsl:if>

						<!-- addComments() for single String -->
						<xsl:if test="not($isInterface = 'true') and not($isFieldInterface or $isException or $isServiceInterface) and
									  not(//field[@name = 'children']) and not($name = 'ConfigurationProperties') and not($name = 'CommentsBlock')">
							<xsl:text>
		/**
		 * Utility method to add a comment to this </xsl:text>
							<xsl:value-of select="$name"/>
							<xsl:text>.
		 * @param newComment is new comment string to add to list of comments.
		 * @see CommentsBlock
	</xsl:text>
							<xsl:text>	 * @return {@link </xsl:text>
							<xsl:value-of select="$thisClassName"/>
							<xsl:text>} - namely </xsl:text>
							<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
							<xsl:text>this</xsl:text>
							<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
							<xsl:text> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
		 */
		public </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text> addComments (String newComment)
		{</xsl:text>
							<xsl:choose>
								<xsl:when test="//field[@name = 'children']">
									<xsl:text>
			addChildren(new CommentsBlock(newComment));
			return this;</xsl:text>
								</xsl:when>
								<xsl:otherwise>
									<xsl:text>
			commentsList.add(newComment);
			return this;</xsl:text>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:text>
		}
	</xsl:text>
						</xsl:if>
						
						<xsl:choose><!-- node-unique and statement-unique methods -->
							
							<xsl:when test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
								<!-- field utilities -->
							<xsl:if test="($name = 'Script') or ($name = 'ShaderPart') or ($name = 'ShaderProgram')">
								<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Add field to fieldList for this ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text>
	 * @param newField is field to add
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ addField (fieldObject newField)
	{
		String errorNotice = new String();
		for (fieldObject priorField : fieldList) // check for field with duplicate name
		{
			if (priorField.getName().equals(newField.getName()))
			{
				errorNotice += "Illegal addField() invocation, provided duplicate newField name='" + newField.getName() + "'";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidFieldException(errorNotice);
			}
		}
		String fieldValidationResult = newField.validate();
		if (!fieldValidationResult.trim().isEmpty())
		{
			errorNotice += "Illegal addField() invocation, invalid newField.validation(): " + fieldValidationResult;
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldException(errorNotice);
		}
		fieldList.add(newField);
		return this;
	}
	/**
	 * Clear all fields
	 */
	public void clearField ()
	{
		fieldList.clear();
	}

	/**
	 * Provide list of fields.
	 * @return value of field list
	 */
	public ArrayList<fieldObject> getFieldList()
	{
		return fieldList;
	}

	/**
	 * Set new source code (for example, JavaScript)
	 * @param newSourceText is source code to set
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ setSourceCode (String newSourceText)
	{
		if (newSourceText == null)
		{
			String errorNotice = "Illegal setSourceCode() invocation, String newSourceText is null";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		else if (!newSourceText.trim().startsWith("ecmascript:") && (newSourceText.trim().length() > 0))
		{
			String errorNotice = "Illegal setSourceCode() invocation, String newSourceText must start with \"ecmascript:\"";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		sourceCode = newSourceText;
		return this;
	}

	/**
	 * Set new source code (for example, JavaScript)
	 * @param newSourceText is source to set
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ setSourceCode (StringBuilder newSourceText)
	{
		if (newSourceText == null)
		{
			String errorNotice = "Illegal setSourceCode() invocation, StringBuilder newSourceText is null";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		else if (!newSourceText.toString().trim().startsWith("ecmascript:") && (newSourceText.toString().trim().length() > 0))
		{
			String errorNotice = "Illegal setSourceCode() invocation, StringBuilder newSourceText must start with \"ecmascript:\"";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		sourceCode = newSourceText.toString();
		return this;
	}

	/**
	 * Append source code (for example, JavaScript)
	 * @param newSourceText is source to append
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ appendSourceCode (String newSourceText)
	{
		sourceCode += newSourceText;
		return this;
	}

	/**
	 * Append source code (for example, JavaScript)
	 * @param newSourceText is source to append
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ appendSourceCode (StringBuilder newSourceText)
	{
		if (newSourceText == null)
		{
			String errorNotice = "Illegal appendSourceCode() invocation, StringBuilder newSourceText is null";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		else sourceCode += newSourceText.toString();
		return this;
	}

	/**
	 * Clear all source code
	 * @return {@link ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ clear ()
	{
		sourceCode = SOURCECODE_DEFAULT_VALUE;
		return this;
	}
		
	/**
	 * Find contained field statement by name, if present.
	 * @param fieldName is name attribute for field of interest
	 * @return fieldObject reference of interest, null otherwise
	 */
	public fieldObject getFieldByName (String fieldName)
	{
		for (fieldObject element : fieldList)
		{
			 if (element.getName().equalsIgnoreCase(fieldName))
				 return element;
		}
		return null;
	}
]]></xsl:text>
								</xsl:if>
								<!-- addField, getFieldByName methods are repeated for ProtoInterface and ExternProtoDeclare -->
							</xsl:when>
							<xsl:when test="($name = 'ProtoInterface') or ($name = 'ExternProtoDeclare')">
								<!-- addField, getFieldByName methods repeat a Script method -->
								<xsl:text>
	/**
	 * Add field to fieldList for this </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text>
	 * @param newField is field to add
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ addField (fieldObject newField)
	{
		String errorNotice = new String();
		for (fieldObject priorField : fieldList) // check for field with duplicate name
		{
			if (priorField.getName().equals(newField.getName()))
			{
				errorNotice += "Illegal addField() invocation, provided duplicate newField name='" + newField.getName() + "'";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidFieldException(errorNotice);
			}
		}
		String fieldValidationResult = newField.validate();
		if (!fieldValidationResult.trim().isEmpty())
		{
			errorNotice += "Illegal addField() invocation, invalid newField.validation(): " + fieldValidationResult;
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldException(errorNotice);
		}
		fieldList.add(newField);
		return this;
	}
		
	/**
	 * Find contained field statement by name, if present.
	 * @param fieldName is name attribute for field of interest
	 * @return fieldObject reference of interest, null otherwise
	 */
	public fieldObject getFieldByName (String fieldName)
	{
		for (fieldObject element : fieldList)
		{
			 if (element.getName().equalsIgnoreCase(fieldName))
				 return element;
		}
		return null;
	}
]]></xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'ProtoInstance')">
								<xsl:text>
	/**
	 * Add fieldValue
	 * @param newFieldValue is fieldValue to add
	 * @return {@link </xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive
setAttribute method invocations).
	 */
	public ]]></xsl:text><xsl:value-of select="$thisClassName"/><xsl:text disable-output-escaping="yes"><![CDATA[ addFieldValue (fieldValueObject newFieldValue)
	{
		String errorNotice = new String();
		for (fieldValueObject priorFieldValue : fieldValueList) // check for field with duplicate name
		{
			if (priorFieldValue.getName().equals(newFieldValue.getName()))
			{
				errorNotice += "Illegal addFieldValue() invocation, provided duplicate newFieldValue name='" + newFieldValue.getName() + "'";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidFieldValueException(errorNotice);
			}
		}
		String fieldValueValidationResult = newFieldValue.validate();
		if (!fieldValueValidationResult.trim().isEmpty())
		{
			errorNotice += "Illegal addFieldValue() invocation, invalid newFieldValue.validation(): " + fieldValueValidationResult;
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldException(errorNotice);
		}
		fieldValueList.add(newFieldValue);
		return this;
	}
	
	/**
	 * Find contained fieldValue statement by name, if present.
	 * @param fieldValueName is name attribute for fieldValue of interest
	 * @return fieldValueObject reference of interest, null otherwise
	 */
	public fieldValueObject getFieldValueByName (String fieldValueName)
	{
		for (fieldValueObject element : fieldValueList)
		{
			 if (element.getName().equalsIgnoreCase(fieldValueName))
				 return element;
		}
		return null;
	}
]]></xsl:text>
							</xsl:when>
							<xsl:when test="($name = 'head')">
								<xsl:text>
	/**
	 * Find contained meta statement by name, if present.
	 * @param metaName is name attribute for meta element of interest
	 * @return metaObject reference of interest, null otherwise
	 */
	public metaObject getMetaByName (String metaName)
	{
		for (metaObject element : metaList)
		{
			 if (element.getName().equalsIgnoreCase(metaName))
				 return element;
		}
		return null;
	}
									
	/**
	 * Find contained component statement by name, if present.
	 * @param componentName is name attribute for component element of interest
	 * @return componentObject reference of interest, null otherwise
	 */
	public componentObject getComponentByName (String componentName)
	{
		for (componentObject element : componentList)
		{
			 if (element.getName().equalsIgnoreCase(componentName))
				 return element;
		}
		return null;
	}
									
	/**
	 * Find contained unit statement by name, if present.
	 * @param unitName is name attribute for unit element of interest
	 * @return unitObject reference of interest, null otherwise
	 */
	public unitObject getUnitByName (String unitName)
	{
		for (unitObject element : unitList)
		{
			 if (element.getName().equalsIgnoreCase(unitName))
				 return element;
		}
		return null;
	}
</xsl:text>
							</xsl:when>
						</xsl:choose><!-- node-unique and statement-unique methods -->
						
					</xsl:if>
	
					<xsl:if test="($name = 'fieldValue') and not($isInterface = 'true')">
						<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Provide base type of this fieldValue declaration from corresponding ProtoDeclare/ExternProtoDeclare field declaration.
	 * String value ['SFBool'|'MFBool'|'SFColor'|'MFColor'|'SFColorRGBA'|'MFColorRGBA'|'SFDouble'|'MFDouble'|'SFFloat'|'MFFloat'|'SFImage'|'MFImage'|'SFInt32'|'SFNode'|'MFNode'|'MFInt32'|'SFRotation'|'MFRotation'|'SFString'|'MFString'|'SFTime'|'MFTime'|'SFVec2d'|'MFVec2d'|'SFVec2f'|'MFVec2f'|'SFVec3d'|'MFVec3d'|'SFVec3f'|'MFVec3f'|'SFVec4d'|'MFVec4d'|'SFVec4f'|'MFVec4f'|'SFMatrix3d'|'MFMatrix3d'|'SFMatrix3f'|'MFMatrix3f'|'SFMatrix4d'|'MFMatrix4d'|'SFMatrix4f'|'MFMatrix4f'] from inputOutput SFString field named <i>type</i>.
	 * <br><br>
	 * @see fieldObject
	 * @return type value from corresponding field declaration
	 */
	public String getType()
	{
		String prototypeName;
		String fieldValueType = "fieldValueTypeNotFound";
		String errorNotice = new String();
							
		if (getParentObject() != null)
			 prototypeName = ((ProtoInstanceObject) getParentObject()).getName();
		else prototypeName = "PrototypeDeclarationNotFound";
		fieldObject fieldDefinition = new fieldObject();
										
		if (getAncestorSceneObject() == null)
		{
			errorNotice += "fieldValue is not connected to a scene graph and cannot be checked.";
			validationResult.append(errorNotice).append("\n");
			return fieldValueType;
		}
		X3DConcreteElement correspondingPrototype = getAncestorSceneObject().getElementByName(prototypeName);
		if      (correspondingPrototype == null)
		{
			errorNotice = "ProtoInstance name='" + prototypeName + "' does not have a corresponding ProtoDeclare name='" + 
						   name + "' definition";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidProtoException(errorNotice); // report error
		}
		else if (correspondingPrototype instanceof ProtoDeclareObject)
		{
			fieldDefinition = ((ProtoDeclareObject) correspondingPrototype).getProtoInterface().getFieldByName(name);
			if (fieldDefinition != null)
				fieldValueType = fieldDefinition.getType(); // found in scene graph
			else
			{
				errorNotice = "fieldValue name='" + name + "' does not have a corresponding ProtoDeclare field name='" +
							   name + "' definition";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidProtoException(errorNotice); // report error
			}
		}
		else if (correspondingPrototype instanceof ExternProtoDeclareObject)
		{
			fieldDefinition = ((ExternProtoDeclareObject) correspondingPrototype).getFieldByName(name);
			if (fieldDefinition != null)
				fieldValueType = fieldDefinition.getType(); // found in scene graph
			else
			{
				errorNotice = "fieldValue name='" + name + "' does not have a corresponding ProtoDeclare field name='" +
							   name + "' definition";
				validationResult.append(errorNotice).append("\n");
				throw new InvalidProtoException(errorNotice); // report error
			}
		}
		return fieldValueType;
	}
]]></xsl:text>
					</xsl:if>
					<!-- TODO consider pass-through methods for ProtoDeclare that hand off to contained (or provided) ProtoInterface -->
					 <!-- end Additional per-class utility methods -->
				</xsl:when>
				<xsl:when test="not($hasInterfaceBlock) and not($hasImplementationBlock)"><!-- and no fields present for this interface -->
					<!-- note definition error -->
					<xsl:message>
						<xsl:text>*** No fields, neither interfaceBlock or implementationBlock found</xsl:text>
					</xsl:message>
					<xsl:text>
	// No field interfaces defined in X3D Object Model
</xsl:text>
				</xsl:when>
			</xsl:choose>
					
			<!-- additional utility methods -->
			<xsl:if test="not($isInterface = 'true') and
							(($name = 'CommentsBlock') or ($name = 'ROUTE') or 
							 ($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare'))">
				<xsl:text disable-output-escaping="yes"><![CDATA[
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
@Override
public X3DMetadataObject getMetadata()
{
return null;
}

/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
@Override
public ]]></xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:if test="($name = 'ROUTE') or ($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare')">
		<xsl:value-of select="$jsaiClassSuffix"/>
	</xsl:if>
	<xsl:text disable-output-escaping="yes"><![CDATA[	setMetadata(X3DMetadataObject newValue)
{
return this; // No action
}
]]></xsl:text>
<!--
<xsl:text disable-output-escaping="yes"><![CDATA[
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
public String getDEF()
{
return "";
}
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
public String getUSE()
{
return "";
}
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
public String getCssClass()
{
return "";
}
]]></xsl:text>
-->
<xsl:text disable-output-escaping="yes"><![CDATA[
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface.
* @param newValue ignored */
@Deprecated
@Override
public ]]></xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:if test="($name = 'ROUTE') or ($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare')">
		<xsl:value-of select="$jsaiClassSuffix"/>
	</xsl:if>
	<xsl:text disable-output-escaping="yes"><![CDATA[ setDEF(String newValue)
{
return this; // no action
}
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface.
* @param newValue ignored */
@Deprecated
@Override
public ]]></xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:if test="($name = 'ROUTE') or ($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare')">
		<xsl:value-of select="$jsaiClassSuffix"/>
	</xsl:if>
	<xsl:text disable-output-escaping="yes"><![CDATA[ setUSE(String newValue)
{
return this; // no action
}
@Deprecated
@Override
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface.
* @param newValue ignored */
public ]]></xsl:text>
	<xsl:value-of select="$name"/>
	<xsl:if test="($name = 'ROUTE') or ($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare')">
		<xsl:value-of select="$jsaiClassSuffix"/>
	</xsl:if>
	<xsl:text disable-output-escaping="yes"><![CDATA[ setCssClass(String newValue)
{
return this; // no action
}
]]></xsl:text>
			</xsl:if>
			<xsl:if test="($name = 'CommentsBlock')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
@Override
public String getType(String fieldName)
{
return "";
}
/** DO NOT USE: operation ignored. This method has no effect, a stub is necessary to implement X3DChildNode interface. */
@Deprecated
@Override
public String getAccessType(String fieldName)
{
return "";
}
]]></xsl:text>
			</xsl:if>
			
			<!-- finished source file definition -->
			<xsl:if test="($wrapClassBrackets)">
				<xsl:text>}</xsl:text>
				<xsl:text>&#10;</xsl:text>
			</xsl:if>
				
		</xsl:result-document> <!-- save file -->
	</xsl:template><!-- sourceFile -->

    <!-- ===================================================== -->
    <!-- ===================================================== -->
    <!-- ===================================================== -->
    
    <!-- create fixed (unchanging) files -->
	
	<xsl:template name="FieldDefinitions">
		
		<xsl:variable name="subPackage">
			<xsl:choose>
				<xsl:when test="($modifySpecificationInterfaces = 'true')">
					<xsl:text>fields</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<!-- otherwise Java SAI specification has no subPackage for the interfaces, they go in the root package - very unusual. -->
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
	
		<!-- TODO specification: fix prose regarding X3DField, seems incorrect. -->
		<!-- TODO specification: change constant values to final, add toString method. -->
		<!-- TODO specification: add data types following MFString (officially approved version dates back to v3.0). -->
		<!-- Note that X3DFieldTypes an interface but it is not implemented by anything else. -->
		
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DFieldTypes</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Set of constants corresponding to each X3D field type and accessType.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.11 X3DFieldTypes</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DFieldTypes</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.15 SAIFieldType</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldType</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>5.3 Field types</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>fieldsDef.html#FieldTypes</xsl:text></xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
	public final int INPUT_ONLY = 1;
	public final int INITIALIZE_ONLY = 2;
	public final int INPUT_OUTPUT = 3;
	public final int OUTPUT_ONLY = 4;

	public final int SFBOOL = 1;
	public final int MFBOOL = 2;
	public final int SFINT32 = 3;
	public final int MFINT32 = 4;
	public final int SFFLOAT = 5;
	public final int MFFLOAT = 6;
	public final int SFDOUBLE = 7;
	public final int MFDOUBLE = 8;
	public final int SFTIME = 9;
	public final int MFTIME = 10;
	public final int SFNODE = 11;
	public final int MFNODE = 12;
	public final int SFVEC2F = 13;
	public final int MFVEC2F = 14;
	public final int SFVEC3F = 15;
	public final int MFVEC3F = 16;
	public final int SFVEC3D = 17;
	public final int MFVEC3D = 18;
	public final int SFROTATION = 19;
	public final int MFROTATION = 20;
	public final int SFCOLOR = 21;
	public final int MFCOLOR = 22;
	public final int SFCOLORRGBA = 23;
	public final int MFCOLORRGBA = 24;
	public final int SFIMAGE = 25;
	public final int MFIMAGE = 26;
	public final int SFSTRING = 27;
	public final int MFSTRING = 28;
	
	// added in v3.3
	public final int SFVEC2D = 29;
	public final int MFVEC2D = 30;
	public final int SFVEC4F = 31;
	public final int MFVEC4F = 32;
	public final int SFVEC4D = 33;
	public final int MFVEC4D = 34;
	public final int SFMATRIX3F = 35;
	public final int MFMATRIX3F = 36;
	public final int SFMATRIX3D = 37;
	public final int MFMATRIX3D = 38;
	public final int SFMATRIX4F = 39;
	public final int MFMATRIX4F = 40;
	public final int SFMATRIX4D = 41;
	public final int MFMATRIX4D = 42;
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
	
		<!-- ===================================================== -->

		<!-- TODO specification Table 5.1 Topics index, _B_ should be _BROWSER_: 5.4.3 SAI_B_ConnectionError 5.4.4 SAI_B_Initialized 5.4.5 SAI_B_Shutdown 5.4.6 SAI_B_URLError -->
		<!-- ToDO B.4.2 X3DFieldEvent is incorrectly listed as class, but is actually interface --> 
		<!-- TODO specification B.5.3 X3DFieldEvent is a duplicate and should be removed. -->
		<!-- TODO specification interface missing void. -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DFieldEvent</xsl:text></xsl:with-param>
			<!-- Note that X3DFieldEvent is listed in specification as a class, but it gets generated alongside other SAI interfaces (not .java concretes) -->
			<xsl:with-param name="isAbstract"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>java.util.EventObject</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>The event type is implemented as the class X3DFieldEvent. This class contains methods for obtaining the source of the event, the time (in X3D time) and any user defined data that occurred with the event.</xsl:text></xsl:with-param>
			<!-- saiJavaSpecificationSection also has reference at 5.4.7 SAIFieldEvent -->
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.2 X3DFieldEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>types.html#EventTypesSAIFieldEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.4.2 SAIFieldEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock"><xsl:text> @author Justin Couch
</xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock">
				<xsl:text><![CDATA[
	// unused
	/**
	 * Get the timestamp that this event occurred at.
	 * @return The time of this event, in X3D time coordinates.
	 */
	public double getTime();

	/**
	 * Construct a new X3DFieldEvent instance.
	 *
	 * @param sourceField The source field that generated this event
	 * @param newTimeStamp The timestamp of the event, in X3D time
	 * @param neweventDataObject Any user associated data with this event
	 */
	public X3DFieldEvent(Object sourceField, double newTimeStamp, Object neweventDataObject);

	/**
	 * Get data with this event.
	 * @return eventDataObject
	 */
	public Object getData();
]]></xsl:text>
			</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[
		/** The time stamp, in X3D time, that this event occurred at */
		protected double timeStamp;

		/** Passed field data for this event */
		protected Object eventDataObject;

		/**
		 * Construct a new X3DFieldEvent instance.
		 *
		 * @param sourceField The source field that generated this event
		 * @param newTimeStamp The timestamp of the event, in X3D time
		 * @param neweventDataObject Any user associated data with this event
		 */
		public X3DFieldEvent(Object sourceField, double newTimeStamp, Object neweventDataObject)
		{
			super(sourceField);

			timeStamp = newTimeStamp;
			eventDataObject = neweventDataObject;
		}

		/**
		 * Get the timestamp that this event occurred at.
		 * @return The time of this event, in X3D time coordinates.
		 */
		public double getTime() 
		{
			return timeStamp;
		}

		/**
		 * Get data with this event.
		 * @return eventDataObject
		 */
		public Object getData()
		{
			return eventDataObject;
		}
	]]></xsl:text>
				</xsl:with-param>
		</xsl:call-template>
	
		<!-- ===================================================== -->
	
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>java.util.EventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Listener for events passing values from one X3D field to another.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.3 X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>types.html#X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>6.3.20 registerBrowserInterest</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>servRef.html#RegisterBrowserInterest</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="interfaceBlock">
				<xsl:text><![CDATA[
	public void readableFieldChanged(X3DFieldEvent event);
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
	
		<!-- ===================================================== -->
	
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DFieldDefinition</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Representation of a node's field definition.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.4 X3DFieldDefinition</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>types.html#X3DFieldDefinition</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>6.3.10 SAIFieldDefinition</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>types.html#SAIFieldDefinition</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
<p>
The field definition holds the static field information such as the field
access type, the data type and the name of the field.
</p>
<p>
The implementation of the toString() method of this class shall return the
full IDL declaration of the field as per the specification, not the UTF8 or
XML format. Implementation of <code>.equals()</code> shall return true if
the two field definitions share the same access type, data type and name. It
shall not include the underlying field's values at that point in time.
</p>

@author Justin Couch
</xsl:with-param>
			<xsl:with-param name="interfaceBlock">
    /**
     * Get the name of this field. This will be something like "children"
     * or "translation". If the field is an exposed field then the name
     * give will be the base name without any <xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>set_<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text> or <xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>_changed<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
     * added to the name, regardless of how the initial field was fetched.
     *
     * @return The name of this field
     */
	public String getName();

    /**
     * Get the access type of the field. This will be one of field,
     * exposedField, eventIn or eventOut constants described in the
     * X3DFieldTypes interface.
     *
     * @return The access type of this node
     * @see X3DFieldTypes
     */
	public int getAccessType();

    /**
     * Get the field type. This string represents the field type such as
     * MFNode, SFInt32. The definition of the returned int value is
     * described in the X3DFieldType interface.
     *
     * @return A constant describing the field type
     * @see X3DFieldTypes
     */
	public int getFieldType();

    /**
     * Get the field type. This string represents the field type such as
     * MFNode, SFInt32, etc. A string is used to allow full extensibility.
     *
     * @return A string describing the field type
     */
	public String getFieldTypeString();
</xsl:with-param>
		</xsl:call-template>
	
		<!-- ===================================================== -->
	
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DField</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Base representation of an X3D field type.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.5 X3DField</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>types.html#X3DField</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.13 SAIField</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIField</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>4.4.2.2 Field semantics</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>concepts.html#FieldSemantics</xsl:text></xsl:with-param>
			<xsl:with-param name="interfaceBlock">
    /**
     * Get the definition of this field.
     *
     * @return The field definition to use
     */
    X3DFieldDefinition getDefinition();

    /**
     * Check to see if this field is readable. This may return two different
     * sets of values depending on the use. If this field is the field of a
     * script that has been passed to a script implementation, it will return
     * true if the field is an eventIn, exposedField or field and false for an
     * eventOut. If it is a field of any other circumstance (ie an external
     * application querying a node or a script querying another node it has a
     * reference to) it shall return true for eventOuts, exposedFields and
     * false for eventIn or field.
     *
     * @return true if the values of this field are readable
     */
    boolean isReadable();

    /**
     * Check to see if this field is writable. This may return two different
     * sets of values depending on the use. If this field is the field of a
     * script that has been passed to a script implementation, it will return
     * true if the field is an eventOut, exposedField or field and false for an
     * eventIn. If it is a field of any other circumstance (ie an external
     * application querying a node or a script querying another node it has a
     * reference to) it shall return true for eventIns, exposedFields and
     * false for eventOut or field.
     *
     * @return true if the values of this field are readable
     */
    boolean isWritable();

    /**
     * <p>
     * Add a listener for changes in this field. This works for listening to
     * changes in a readable field. A future extension to the specification,
     * or a browser-specific extension, may allow for listeners to be added
     * to writable nodes as well.
     * </p>
     * <p>
     * A listener instance cannot have multiple simultaneous registrations.
     * If the listener instance is currently registered, this request shall
     * be silently ignored.
     * </p>
     *
     * @param listener The listener to add
     */
    void addX3DEventListener(X3DFieldEventListener listener);

    /**
     * Remove a listener for changes in the readable field. If the listener is
     * not currently registered, this request shall be silently ignored.
     *
     * @param listener The listener to remove
     */
    void removeX3DEventListener(X3DFieldEventListener listener);

</xsl:with-param>
<!-- TODO specification: these methods are never defined in specification other than the interface listing. Omitted.
    /**
     * Associate user data with this field. Whenever an field is generated
     * on this field, this data will be available with the Event through
     * its getData method.
     *
     * @param data The data to associate with this eventOut instance
     */
    void setUserData(Object data);

    /**
     * Get the user data that is associated with this field.
     *
     * @return The user data, if any, associated with this field
     */
    Object getUserData();
-->
		</xsl:call-template>
	
		<!-- ===================================================== -->
	
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>MField</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DField</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Base interface for multiple-field (MF) array types.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.6 MField</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#MField</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text>
    /**
     * Get the size of the underlying data array. The size is the number of
     * elements for that data type. So for an MFFloat the size would be the
     * number of float values, but for an MFVec3f, it is the number of vectors
     * in the returned array (where a vector is 3 consecutive array indexes in
     * a flat array).
     *
     * @return The number of elements in this field array.
     */
	public int size();

    /**
     * Removes all values in the field array, and changes the array size to zero.
     */
	public void clear();

    /**
     * Remove one element of the field array at index position, if found.  Initial element is at index 0.
     * @param index The position of the element in the field array that gets removed.
     */
	public void remove(int index);
</xsl:text></xsl:with-param>
		</xsl:call-template>
		
		<!-- ===================================================== -->
			
		<!-- TODO specification needs to be interface, not class -->
		<!-- TODO specification accessor methods missing trailing semicolons, should not have bodies -->
		<!-- TODO decide on best implementation and then add it -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>Matrix3</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Describes a 3x3 Matrix as required by the SAIMatrix abstract type.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.4 Matrix3</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#Matrix3</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.20 SAIMatrix</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIMatrix</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock"><xsl:text><![CDATA[
@author Justin Couch
]]></xsl:text>
			</xsl:with-param>
			<!-- TODO: remove constructor definition from specification interface: public Matrix3(); -->
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
				
	public void setIdentity();
				
	public void set(int row, int column);

	public float get(int row, int column);

//	public void setTransform(SFVec3f translation, // TODO incompatible with double types
//		SFRotation rotation,
//		SFVec3f scale,
//		SFRotation scaleOrientation,
//		SFVec3f center);

//	public void getTransform(SFVec3f translation, // TODO incompatible with double types
//		SFRotation rotation,
//		SFVec3f scale);

	public Matrix3 inverse();

	public Matrix3 transpose();

	public Matrix3 multiplyLeft(Matrix3 matrix3x3);

	public Matrix3 multiplyRight(Matrix3 matrix3x3);

//	public Matrix3 multiplyRowVector(SFVec3f vec3f); // TODO incompatible with double types

//	public Matrix3 multiplyColVector(SFVec3f vec3f); // TODO incompatible with double types
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
		
		<!-- ===================================================== -->
			
		<!-- TODO specification accessor methods missing trailing semicolons -->
		<!-- TODO decide on best implementation and then add it -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>Matrix4</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Describes a 4x4 Matrix as required by the SAIMatrix abstract type.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.5 Matrix4</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#Matrix4</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.20 SAIMatrix</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIMatrix</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
    /* TODO: remove constructor definition from interface specification
	public Matrix4();
     */

	public void setIdentity();

	public void set(int row, int column);

	public float get(int row, int column);

//	public void setTransform(SFVec3f translation, // TODO incompatible with double types
//		SFRotation rotation,
//		SFVec3f scale,
//		SFRotation scaleOrientation,
//		SFVec3f center);

//	public void getTransform(SFVec3f translation, // TODO incompatible with double types
//		SFRotation rotation,
//		SFVec3f scale);

	public Matrix4 inverse();

	public Matrix4 transpose();

	public Matrix4 multiplyLeft(Matrix4 matrix4x4);

	public Matrix4 multiplyRight(Matrix4 matrix4x4);

//	public Matrix3 multiplyColVector(SFVec3f vec3f); // TODO SFVec4f ?  // TODO incompatible with double types

//	public Matrix3 multiplyColVector(SFVec3f vec3f); // TODO SFVec4f ?  // TODO incompatible with double types
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<!-- now concrete classes -->
		
		<!-- loop over fields to find further imports -->
		<xsl:for-each select="//FieldTypes/FieldType">
			
			<xsl:variable name="fieldName" select="@type"/>
			
			<xsl:variable name="javaType">
				<xsl:call-template name="javaType">
					<xsl:with-param name="x3dType" select="@type"/>
					<!-- isInterface true returns Java base types (e.g. float[] for SFColor, etc. -->
					<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
				</xsl:call-template>
			</xsl:variable>
			<xsl:variable name="isSingletonType">
				<xsl:value-of select="(@type = 'MFBool')   or (@type = 'MFInt32') or (@type = 'MFDouble') or (@type = 'MFFloat') or 
                                      (@type = 'MFString') or (@type = 'MFTime')  or (@type = 'MFNode') or
                                       starts-with(@type,'SF')"/>
			</xsl:variable>
			<xsl:variable name="tupleSize">
				<xsl:call-template name="tupleSize">
					<xsl:with-param name="x3dType" select="@type"/>
				</xsl:call-template>
			</xsl:variable>
			<xsl:variable name="javaPrimitiveType">
				<xsl:choose>
					<xsl:when test="($isSingletonType = 'true')">
						<xsl:value-of select="substring-before($javaType,'[')"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="$javaType"/><!-- array of array type -->
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			<xsl:variable name="dimensionSuffix">
				<xsl:choose>
					<xsl:when test="false() and ($javaType = $javaPrimitiveType)">
						<xsl:text>.size()</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>.length</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			<xsl:variable name="implements">
				<xsl:choose>
					<xsl:when test="contains($fieldName,'Matrix3')">
						<xsl:text> extends Matrix3</xsl:text>
					</xsl:when>
					<xsl:when test="contains($fieldName,'Matrix4')">
						<xsl:text> extends Matrix4</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			<xsl:variable name="imports">
				<xsl:choose>
					<xsl:when test="contains($fieldName,'FImage')">
						<xsl:text>import java.util.Arrays;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>import org.web3d.x3d.sai.InvalidFieldValueException;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>import java.awt.image.RenderedImage;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>import java.awt.image.WritableRenderedImage;</xsl:text>
					</xsl:when>
					<xsl:when test="contains($fieldName,'FMatrix')">
						<xsl:text>import org.web3d.x3d.sai.*;</xsl:text>
						<xsl:text>&#10;</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>import org.web3d.x3d.sai.InvalidFieldValueException;</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			<xsl:variable name="javadocBlock">
				<xsl:value-of select="InterfaceDefinition/@appinfo"/>
				<xsl:if test="($fieldName = 'SFColor')">
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"><![CDATA[@see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a>
]]></xsl:text>
				</xsl:if>
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text disable-output-escaping="yes">&lt;br&gt;</xsl:text><!-- line break -->
				<xsl:text>&#10;</xsl:text>
				<xsl:text disable-output-escaping="yes"><![CDATA[Related field object: {@link ]]></xsl:text>
				<xsl:choose>
					<xsl:when test="starts-with($fieldName,'SF')">
						<xsl:text>MF</xsl:text>
						<xsl:value-of select="substring-after($fieldName,'SF')"/>
						<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>SF</xsl:text>
						<xsl:value-of select="substring-after($fieldName,'MF')"/>
						<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					</xsl:otherwise>
				</xsl:choose>
				<xsl:text> }
</xsl:text>
			</xsl:variable>
<xsl:variable name="newValueNullExceptionCheck">
	<xsl:text>		if (</xsl:text>
	<xsl:value-of select="$newValue"/>
	<xsl:text> == null)</xsl:text>
	<xsl:text>&#10;</xsl:text>
	<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
	<xsl:text>("</xsl:text>
	<xsl:value-of select="@name"/>
	<xsl:value-of select="$jsaiClassSuffix"/>
	<xsl:text> </xsl:text>
	<xsl:value-of select="$newValue"/>
	<xsl:text> is null and cannot be set"); // fieldTest</xsl:text>
	<xsl:text>&#10;</xsl:text>
</xsl:variable>
<xsl:variable name="newValueNullReturnVoid">
	<!-- TODO avoid null-value checks by replacing with empty values instead, where possible -->
	<xsl:text>		if (</xsl:text>
	<xsl:value-of select="$newValue"/>
	<xsl:text> == null) return; // newValueNullReturnVoid2</xsl:text>
	<xsl:text>&#10;</xsl:text>
</xsl:variable>

<!-- debug
<xsl:if test="($debug = 'true')">
<xsl:message>
<xsl:text>// field ($fieldName=</xsl:text>
<xsl:value-of select="$fieldName"/>
<xsl:text>, $javaType=</xsl:text>
<xsl:value-of select="$javaType"/>
<xsl:text>, $isSingletonType=</xsl:text>
<xsl:value-of select="$isSingletonType"/>
<xsl:text>, tupleSize=</xsl:text>
<xsl:value-of select="$tupleSize"/>
<xsl:text>, $javaPrimitiveType=</xsl:text>
<xsl:value-of select="$javaPrimitiveType"/>
<xsl:text>, $dimensionSuffix=</xsl:text>
<xsl:value-of select="$dimensionSuffix"/>
<xsl:text>)</xsl:text>
</xsl:message>
</xsl:if> -->

			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$fieldName"/><xsl:value-of select="$jsaiClassSuffix"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:value-of select="$imports"/></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text>X3DConcreteField</xsl:text></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.</xsl:text><xsl:value-of select="$fieldName"/></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:text>fields</xsl:text></xsl:with-param>
				<xsl:with-param name="description">
					<xsl:text>This utility class provides a concrete implementation corresponding to </xsl:text>
					<xsl:value-of select="$fieldName"/>
					<xsl:text> X3D field type.</xsl:text>
				</xsl:with-param>
				<!-- TODO update -->
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.11 X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.15 SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="substring-after(InterfaceDefinition/@specificationUrl,'#')"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="InterfaceDefinition/@specificationUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="implementationBlock">
					
				<!-- FieldType default values -->
				<xsl:text>&#10;</xsl:text>
				<xsl:text>	/** Default value for this field type. */</xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:choose>
					<xsl:when test="($fieldName = 'SFBool')">
						<xsl:text>	public static final boolean DEFAULT_VALUE = true;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFInt32')">
						<xsl:text>	public static final int DEFAULT_VALUE = 0;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFFloat')">
						<xsl:text>	public static final float DEFAULT_VALUE = 0.0f;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFDouble')">
						<xsl:text>	public static final double DEFAULT_VALUE = 0.0;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFTime')">
						<xsl:text>	public static final double DEFAULT_VALUE = -1.0;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec2d')">
						<xsl:text>	public static final double[] DEFAULT_VALUE = {0.0, 0.0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec2f')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec3d')">
						<xsl:text>	public static final double[] DEFAULT_VALUE = {0.0, 0.0, 0.0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec3f')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f, 0.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFColor')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f, 0.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFColorRGBA')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f, 0.0f, 0.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec4d')">
						<xsl:text>	public static final double[] DEFAULT_VALUE = {0.0, 0.0, 0.0, 1.0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFVec4f')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f, 0.0f, 1.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFRotation')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {0.0f, 0.0f, 1.0f, 0.0f};</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>	/** Preferred default value for this field type, oriented for rotation about Y axis. */</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>	public static final float[] PREFERRED_DEFAULT_VALUE = {0.0f, 1.0f, 0.0f, 0.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFString')">
						<xsl:text>	public static final String DEFAULT_VALUE = "";</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFImage')">
						<xsl:text>	public static final int[] DEFAULT_VALUE = {0, 0, 0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFMatrix3d')">
						<xsl:text>	public static final double[] DEFAULT_VALUE = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFMatrix3f')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {1.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 1.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFMatrix4d')">
						<xsl:text>	public static final double[] DEFAULT_VALUE = {1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFMatrix4f')">
						<xsl:text>	public static final float[] DEFAULT_VALUE = {1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f};</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'SFNode')">
						<xsl:text>	</xsl:text><!-- tab -->
						<xsl:text>public static final X3DNode </xsl:text>
						<xsl:text>DEFAULT_VALUE</xsl:text>
						<xsl:text> = </xsl:text>
						<xsl:text>null;</xsl:text>
					</xsl:when>
					<xsl:when test="($fieldName = 'MFNode')">
						<xsl:text>	</xsl:text><!-- tab -->
						<xsl:text>public static final X3DNode[] </xsl:text>
						<xsl:text>DEFAULT_VALUE</xsl:text>
						<xsl:text> = </xsl:text>
						<xsl:text>new X3DNode[0]; // initialize as empty array</xsl:text>
					</xsl:when>
					<xsl:when test="starts-with($fieldName,'MF')">
						<xsl:text>	public static final </xsl:text>
						<xsl:value-of select="$javaType"/>
						<xsl:text> </xsl:text>
						<xsl:text>DEFAULT_VALUE = new </xsl:text>
						<xsl:value-of select="substring-before($javaType, '[]')"/>
						<xsl:text>[0]; // initialize as empty array</xsl:text>
					</xsl:when>
				</xsl:choose>
				<xsl:text>&#10;</xsl:text>
				
				<!-- SFColor convenience contants -->
				<xsl:if test="($fieldName = 'SFColor')">
					<xsl:text disable-output-escaping="yes"><![CDATA[
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ALICEBLUE = toFloatArray(0xf0f8ff); // decimal 240,248,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ANTIQUEWHITE = toFloatArray(0xfaebd7); // decimal 250,235,215
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] AQUA = toFloatArray(0x00ffff); // decimal 0,255,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] AQUAMARINE = toFloatArray(0x7fffd4); // decimal 127,255,212
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] AZURE = toFloatArray(0xf0ffff); // decimal 240,255,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BEIGE = toFloatArray(0xf5f5dc); // decimal 245,245,220
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BISQUE = toFloatArray(0xffe4c4); // decimal 255,228,196
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BLACK = toFloatArray(0x000000); // decimal 0,0,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BLANCHEDALMOND = toFloatArray(0xffebcd); // decimal 255,235,205
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BLUE = toFloatArray(0x0000ff); // decimal 0,0,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BLUEVIOLET = toFloatArray(0x8a2be2); // decimal 138,43,226
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BROWN = toFloatArray(0xa52a2a); // decimal 165,42,42
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] BURLYWOOD = toFloatArray(0xdeb887); // decimal 222,184,135
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CADETBLUE = toFloatArray(0x5f9ea0); // decimal 95,158,160
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CHARTREUSE = toFloatArray(0x7fff00); // decimal 127,255,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CHOCOLATE = toFloatArray(0xd2691e); // decimal 210,105,30
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CORAL = toFloatArray(0xff7f50); // decimal 255,127,80
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CORNFLOWERBLUE = toFloatArray(0x6495ed); // decimal 100,149,237
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CORNSILK = toFloatArray(0xfff8dc); // decimal 255,248,220
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CRIMSON = toFloatArray(0xdc143c); // decimal 220,20,60
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] CYAN = toFloatArray(0x00ffff); // decimal 0,255,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKBLUE = toFloatArray(0x00008b); // decimal 0,0,139
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKCYAN = toFloatArray(0x008b8b); // decimal 0,139,139
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKGOLDENROD = toFloatArray(0xb8860b); // decimal 184,134,11
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKGRAY = toFloatArray(0xa9a9a9); // decimal 169,169,169
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKGREEN = toFloatArray(0x006400); // decimal 0,100,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKGREY = toFloatArray(0xa9a9a9); // decimal 169,169,169
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKKHAKI = toFloatArray(0xbdb76b); // decimal 189,183,107
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKMAGENTA = toFloatArray(0x8b008b); // decimal 139,0,139
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKOLIVEGREEN = toFloatArray(0x556b2f); // decimal 85,107,47
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKORANGE = toFloatArray(0xff8c00); // decimal 255,140,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKORCHID = toFloatArray(0x9932cc); // decimal 153,50,204
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKRED = toFloatArray(0x8b0000); // decimal 139,0,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKSALMON = toFloatArray(0xe9967a); // decimal 233,150,122
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKSEAGREEN = toFloatArray(0x8fbc8f); // decimal 143,188,143
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKSLATEBLUE = toFloatArray(0x483d8b); // decimal 72,61,139
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKSLATEGRAY = toFloatArray(0x2f4f4f); // decimal 47,79,79
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKSLATEGREY = toFloatArray(0x2f4f4f); // decimal 47,79,79
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKTURQUOISE = toFloatArray(0x00ced1); // decimal 0,206,209
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DARKVIOLET = toFloatArray(0x9400d3); // decimal 148,0,211
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DEEPPINK = toFloatArray(0xff1493); // decimal 255,20,147
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DEEPSKYBLUE = toFloatArray(0x00bfff); // decimal 0,191,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DIMGRAY = toFloatArray(0x696969); // decimal 105,105,105
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DIMGREY = toFloatArray(0x696969); // decimal 105,105,105
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] DODGERBLUE = toFloatArray(0x1e90ff); // decimal 30,144,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] FIREBRICK = toFloatArray(0xb22222); // decimal 178,34,34
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] FLORALWHITE = toFloatArray(0xfffaf0); // decimal 255,250,240
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] FORESTGREEN = toFloatArray(0x228b22); // decimal 34,139,34
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] FUCHSIA = toFloatArray(0xff00ff); // decimal 255,0,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GAINSBORO = toFloatArray(0xdcdcdc); // decimal 220,220,220
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GHOSTWHITE = toFloatArray(0xf8f8ff); // decimal 248,248,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GOLD = toFloatArray(0xffd700); // decimal 255,215,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GOLDENROD = toFloatArray(0xdaa520); // decimal 218,165,32
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GRAY = toFloatArray(0x808080); // decimal 128,128,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GREEN = toFloatArray(0x008000); // decimal 0,128,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GREENYELLOW = toFloatArray(0xadff2f); // decimal 173,255,47
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] GREY = toFloatArray(0x808080); // decimal 128,128,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] HONEYDEW = toFloatArray(0xf0fff0); // decimal 240,255,240
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] HOTPINK = toFloatArray(0xff69b4); // decimal 255,105,180
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] INDIANRED = toFloatArray(0xcd5c5c); // decimal 205,92,92
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] INDIGO = toFloatArray(0x4b0082); // decimal 75,0,130
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] IVORY = toFloatArray(0xfffff0); // decimal 255,255,240
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] KHAKI = toFloatArray(0xf0e68c); // decimal 240,230,140
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LAVENDER = toFloatArray(0xe6e6fa); // decimal 230,230,250
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LAVENDERBLUSH = toFloatArray(0xfff0f5); // decimal 255,240,245
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LAWNGREEN = toFloatArray(0x7cfc00); // decimal 124,252,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LEMONCHIFFON = toFloatArray(0xfffacd); // decimal 255,250,205
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTBLUE = toFloatArray(0xadd8e6); // decimal 173,216,230
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTCORAL = toFloatArray(0xf08080); // decimal 240,128,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTCYAN = toFloatArray(0xe0ffff); // decimal 224,255,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTGOLDENRODYELLOW = toFloatArray(0xfafad2); // decimal 250,250,210
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTGRAY = toFloatArray(0xd3d3d3); // decimal 211,211,211
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTGREEN = toFloatArray(0x90ee90); // decimal 144,238,144
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTGREY = toFloatArray(0xd3d3d3); // decimal 211,211,211
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTPINK = toFloatArray(0xffb6c1); // decimal 255,182,193
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSALMON = toFloatArray(0xffa07a); // decimal 255,160,122
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSEAGREEN = toFloatArray(0x20b2aa); // decimal 32,178,170
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSKYBLUE = toFloatArray(0x87cefa); // decimal 135,206,250
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSLATEGRAY = toFloatArray(0x778899); // decimal 119,136,153
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSLATEGREY = toFloatArray(0x778899); // decimal 119,136,153
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTSTEELBLUE = toFloatArray(0xb0c4de); // decimal 176,196,222
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIGHTYELLOW = toFloatArray(0xffffe0); // decimal 255,255,224
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIME = toFloatArray(0x00ff00); // decimal 0,255,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LIMEGREEN = toFloatArray(0x32cd32); // decimal 50,205,50
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] LINEN = toFloatArray(0xfaf0e6); // decimal 250,240,230
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MAGENTA = toFloatArray(0xff00ff); // decimal 255,0,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MAROON = toFloatArray(0x800000); // decimal 128,0,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMAQUAMARINE = toFloatArray(0x66cdaa); // decimal 102,205,170
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMBLUE = toFloatArray(0x0000cd); // decimal 0,0,205
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMORCHID = toFloatArray(0xba55d3); // decimal 186,85,211
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMPURPLE = toFloatArray(0x9370db); // decimal 147,112,219
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMSEAGREEN = toFloatArray(0x3cb371); // decimal 60,179,113
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMSLATEBLUE = toFloatArray(0x7b68ee); // decimal 123,104,238
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMSPRINGGREEN = toFloatArray(0x00fa9a); // decimal 0,250,154
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMTURQUOISE = toFloatArray(0x48d1cc); // decimal 72,209,204
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MEDIUMVIOLETRED = toFloatArray(0xc71585); // decimal 199,21,133
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MIDNIGHTBLUE = toFloatArray(0x191970); // decimal 25,25,112
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MINTCREAM = toFloatArray(0xf5fffa); // decimal 245,255,250
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MISTYROSE = toFloatArray(0xffe4e1); // decimal 255,228,225
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] MOCCASIN = toFloatArray(0xffe4b5); // decimal 255,228,181
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] NAVAJOWHITE = toFloatArray(0xffdead); // decimal 255,222,173
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] NAVY = toFloatArray(0x000080); // decimal 0,0,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] OLDLACE = toFloatArray(0xfdf5e6); // decimal 253,245,230
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] OLIVE = toFloatArray(0x808000); // decimal 128,128,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] OLIVEDRAB = toFloatArray(0x6b8e23); // decimal 107,142,35
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ORANGE = toFloatArray(0xffa500); // decimal 255,165,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ORANGERED = toFloatArray(0xff4500); // decimal 255,69,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ORCHID = toFloatArray(0xda70d6); // decimal 218,112,214
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PALEGOLDENROD = toFloatArray(0xeee8aa); // decimal 238,232,170
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PALEGREEN = toFloatArray(0x98fb98); // decimal 152,251,152
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PALETURQUOISE = toFloatArray(0xafeeee); // decimal 175,238,238
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PALEVIOLETRED = toFloatArray(0xdb7093); // decimal 219,112,147
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PAPAYAWHIP = toFloatArray(0xffefd5); // decimal 255,239,213
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PEACHPUFF = toFloatArray(0xffdab9); // decimal 255,218,185
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PERU = toFloatArray(0xcd853f); // decimal 205,133,63
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PINK = toFloatArray(0xffc0cb); // decimal 255,192,203
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PLUM = toFloatArray(0xdda0dd); // decimal 221,160,221
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] POWDERBLUE = toFloatArray(0xb0e0e6); // decimal 176,224,230
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] PURPLE = toFloatArray(0x800080); // decimal 128,0,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] RED = toFloatArray(0xff0000); // decimal 255,0,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ROSYBROWN = toFloatArray(0xbc8f8f); // decimal 188,143,143
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] ROYALBLUE = toFloatArray(0x4169e1); // decimal 65,105,225
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SADDLEBROWN = toFloatArray(0x8b4513); // decimal 139,69,19
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SALMON = toFloatArray(0xfa8072); // decimal 250,128,114
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SANDYBROWN = toFloatArray(0xf4a460); // decimal 244,164,96
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SEAGREEN = toFloatArray(0x2e8b57); // decimal 46,139,87
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SEASHELL = toFloatArray(0xfff5ee); // decimal 255,245,238
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SIENNA = toFloatArray(0xa0522d); // decimal 160,82,45
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SILVER = toFloatArray(0xc0c0c0); // decimal 192,192,192
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SKYBLUE = toFloatArray(0x87ceeb); // decimal 135,206,235
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SLATEBLUE = toFloatArray(0x6a5acd); // decimal 106,90,205
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SLATEGRAY = toFloatArray(0x708090); // decimal 112,128,144
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SLATEGREY = toFloatArray(0x708090); // decimal 112,128,144
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SNOW = toFloatArray(0xfffafa); // decimal 255,250,250
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] SPRINGGREEN = toFloatArray(0x00ff7f); // decimal 0,255,127
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] STEELBLUE = toFloatArray(0x4682b4); // decimal 70,130,180
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] TAN = toFloatArray(0xd2b48c); // decimal 210,180,140
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] TEAL = toFloatArray(0x008080); // decimal 0,128,128
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] THISTLE = toFloatArray(0xd8bfd8); // decimal 216,191,216
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] TOMATO = toFloatArray(0xff6347); // decimal 255,99,71
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] TURQUOISE = toFloatArray(0x40e0d0); // decimal 64,224,208
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] VIOLET = toFloatArray(0xee82ee); // decimal 238,130,238
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] WHEAT = toFloatArray(0xf5deb3); // decimal 245,222,179
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] WHITE = toFloatArray(0xffffff); // decimal 255,255,255
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] WHITESMOKE = toFloatArray(0xf5f5f5); // decimal 245,245,245
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] YELLOW = toFloatArray(0xffff00); // decimal 255,255,0
	/** @see <a href="https://www.w3.org/TR/css3-color/#svg-color">CSS Color Module Level 3, 4.3. Extended color keywords</a> */
	public static float[] YELLOWGREEN = toFloatArray(0x9acd32); // decimal 154,205,50
]]></xsl:text>
					</xsl:if>
							
				<!-- method definitions for concrete fields -->
				<xsl:text><![CDATA[
	// Member value declaration is encapsulated and private, using preferred Java types for concretes library
	private ]]></xsl:text>
				<xsl:value-of select="$javaType"/>
				<xsl:text> </xsl:text>
				<xsl:value-of select="$fieldName"/>
				<xsl:text> = </xsl:text>
				<xsl:text>DEFAULT_VALUE;</xsl:text>
				<xsl:text>&#10;</xsl:text>

		<!-- Source code: constructor method using default initial value -->
		<xsl:text>
	/**
	 * public constructor for </xsl:text>
	<xsl:value-of select="$fieldName"/>
	<xsl:value-of select="$jsaiClassSuffix"/>
	<xsl:text> using default initial value.
	 */
	public </xsl:text>
	<xsl:value-of select="$fieldName"/>
	<xsl:value-of select="$jsaiClassSuffix"/>
	<xsl:text> ()
	{
		</xsl:text>
		<xsl:value-of select="$fieldName"/>
		<xsl:text> = </xsl:text>
		<xsl:text>DEFAULT_VALUE;
	}
</xsl:text>

		<!-- Source code: constructor method using single typed value -->
		<xsl:text>
	/**
	 * public constructor for </xsl:text>
	<xsl:value-of select="$fieldName"/>
	<xsl:value-of select="$jsaiClassSuffix"/>
	<xsl:text> using corresponding Java primitive as new initial value.
	 * @param newValue The new value to assign.
	 */
	public </xsl:text>
	<xsl:value-of select="$fieldName"/>
	<xsl:value-of select="$jsaiClassSuffix"/>
	<xsl:text> (</xsl:text>
	<xsl:value-of select="$javaType"/>
	<xsl:text> newValue)
	{</xsl:text>
		<!-- initial value checks -->
		<xsl:choose>
			<xsl:when test="starts-with(@type,'MF') and ends-with($javaType, '[]') and ($tupleSize > 1)">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		if      (newValue == null)
			     newValue = DEFAULT_VALUE;
		else if (newValue.length % ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ != 0) // ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[-tuple check
		{
			String errorNotice = "Illegal ]]></xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ float[] array length=" + newValue.length +
				", must be multiple of ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ or else be empty (newValue=" + toString(newValue) + ")";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
			</xsl:when>
		<xsl:when test="starts-with(@type,'SF') and ends-with($javaType, '[]') and ($tupleSize > 1)">
			<xsl:text disable-output-escaping="yes"><![CDATA[
		if      (newValue == null)
			     newValue = DEFAULT_VALUE;
		else if (newValue.length != ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[)
		{
			String errorNotice = "Illegal ]]></xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ float[] array length=" + newValue.length +
				", must equal ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ or else be empty (newValue=" + toString(newValue) + ")";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
			</xsl:when>
		<xsl:when test="ends-with($javaType, '[]')"><!-- ($tupleSize == 1) -->
			<xsl:text disable-output-escaping="yes"><![CDATA[
		if (newValue == null)
			newValue = DEFAULT_VALUE;
		]]></xsl:text>
			</xsl:when>
		</xsl:choose>
		<xsl:choose>
			<xsl:when test="(@type='SFColor')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		// initial value checks 
		float   red = newValue[0];
		float green = newValue[1];
		float  blue = newValue[2];
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue +
				"), all values must be in numeric range [0..1]";
		}
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFColorRGBA')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
		// initial value checks 
		float   red = newValue[0];
		float green = newValue[1];
		float  blue = newValue[2];	
		float alpha = newValue[3];	
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA value (" + red + "," + green + "," + blue + "," + alpha + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
			</xsl:when>
		</xsl:choose>
		<xsl:text>
		</xsl:text><!-- newline, indent -->
		<xsl:value-of select="$fieldName"/>
		<xsl:text> = newValue;
	}
</xsl:text>

		<!-- Utility constructors -->
		<xsl:choose>
			<xsl:when test="(@type='SFFloat')">
				<xsl:text>
	/**
	 * Public utility constructor using double as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFFloat</xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (double newValue)
	{
		SFFloat = (float) newValue;
	}
	/**
	 * Public utility constructor using int as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int newValue)
	{
		SFFloat = (float) newValue;
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFDouble')">
				<xsl:text><![CDATA[
	/**
	 * Public utility constructor using float as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFDouble]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (float newValue)
	{
		SFDouble = (double) newValue;
	}
	/**
	 * Public utility constructor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ using int as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFDouble]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int newValue)
	{
		SFDouble = (double) newValue;
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFTime')">
				<xsl:text>
	/**
	 * Public utility constructor using float as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFTime</xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (float newValue)
	{
		SFTime = (double) newValue;
	}
	/**
	 * Public utility constructor using int as new initial value.
	 * @param newValue The new value to assign.
	 */
	public SFTime]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int newValue)
	{
		SFTime = (int) newValue;
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFColor')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Public utility constructor using individual float types as new initial value.
	 * @param red first component
	 * @param green second component
	 * @param blue third component
	 */
	public SFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (float red, float green, float blue)
	{
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColor[0] = red;
		SFColor[1] = green;
		SFColor[2] = blue;
	}
	/**
	 * Public utility constructor using single HTML-style 0xRRGGBB hex value as new initial value.
	 * @param hexColorValue HTML color value (such as 0xAA2288)
	 */
	public SFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int hexColorValue)
	{
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number

		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColor[0] = red;
		SFColor[1] = green;
		SFColor[2] = blue;
	}
	/**
	 * Public utility method converting single HTML-style 0xRRGGBB hex value to three-tuple float array.
TODO: also MFColor.
	 * @param hexColorValue HTML color value (such as 0xAA2288)
	 * @return float[3] array containing X3D RGB values, each ranging [0..1]
	 */
	public static float[] toFloatArray (int hexColorValue)
	{
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float[] newFloatArray = {0.0f, 0.0f, 0.0f};
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		newFloatArray[0] = red;
		newFloatArray[1] = green;
		newFloatArray[2] = blue;
		return newFloatArray;
	}
	/**
	 * Public utility accessor method setting single HTML-style 0xRRGGBB hex value as new value.
	 * @param hexColorValue HTML color value (such as 0xAA2288)
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue (int hexColorValue)
	{
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal ;SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColor[0] = red;
		SFColor[1] = green;
		SFColor[2] = blue;
		return this;
	}
	/**
	 * Complement all color values in RGB space (i.e. subtract each component from 1).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementRGB ()
	{
		SFColor[0] = 1.0f - SFColor[0];
		SFColor[1] = 1.0f - SFColor[1];
		SFColor[2] = 1.0f - SFColor[2];
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFColorRGBA')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Public utility constructor using individual float types as new initial value.
	 * @param red first component
	 * @param green second component
	 * @param blue third component
	 * @param alpha fourth component for opaqueness (1 - transparency)
	 */
	public SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[  (float red, float green, float blue, float alpha)
	{
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA value (" + red + "," + green + "," + blue + "," + alpha + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColorRGBA[0] = red;
		SFColorRGBA[1] = green;
		SFColorRGBA[2] = blue;
		SFColorRGBA[3] = alpha;
	}
	/**
	 * Public utility constructor using single HTML-style 0xRRGGBB hex value as new initial value.
	 * @param hexColorValue HTML color value (such as 0xAA2288)
	 * @param alpha fourth component for opaqueness (1 - transparency)
	 */
	public SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int hexColorValue, float alpha)
	{
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColorRGBA[0] = red;
		SFColorRGBA[1] = green;
		SFColorRGBA[2] = blue;
		SFColorRGBA[3] = alpha;
	}
	/**
	 * Public utility accessor method setting single HTML-style 0xRRGGBB hex value as new value.
	 * @param hexColorValue HTML color value (such as 0xAA2288)
	 * @param alpha fourth component for opaqueness (1 - transparency)
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue (int hexColorValue, float alpha)
	{
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + "," + alpha + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColorRGBA[0] = red;
		SFColorRGBA[1] = green;
		SFColorRGBA[2] = blue;
		SFColorRGBA[3] = alpha;
		return this;
	}
	/**
	 * Complement all color values in RGB space (i.e. subtract each component from 1).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementRGB ()
	{
		SFColorRGBA[0] = 1.0f - SFColorRGBA[0];
		SFColorRGBA[1] = 1.0f - SFColorRGBA[1];
		SFColorRGBA[2] = 1.0f - SFColorRGBA[2];
	}
	/**
	 * Complement alpha value by subtracting it from 1.  Note transparency = (1 - alpha).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementAlpha ()
	{
		SFColorRGBA[3] = 1.0f - SFColorRGBA[3];
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='MFColor')">
				<!-- TODO hex array constructor and accessors -->
				<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Replaces a single value at the appropriate location in the existing value array.
	 * @param index The position of the selected value in the current array
	 * @param hexColorValue The HTML color value (such as 0xAA2288) to insert
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public MFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ set1Value(int index, int hexColorValue) throws ArrayIndexOutOfBoundsException
	{
		if (index >= MFColor.length / 3) // tupleness factor
		{
			String errorNotice = "Array index=" + index + " (for 3-tuples) is greater than MFColor array length=" + MFColor.length;
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		MFColor[3*index + 0] = red;
		MFColor[3*index + 1] = green;
		MFColor[3*index + 2] = blue;
		return this;
	}
	/**
	 * Complement all color values in RGB space (i.e. subtract each component from 1).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementRGB ()
	{
		for (int i = 0; i+2 < MFColor.length; i = i + 3)
		{
			MFColor[i+0] = 1.0f - MFColor[i+0];
			MFColor[i+1] = 1.0f - MFColor[i+1];
			MFColor[i+2] = 1.0f - MFColor[i+2];
		}
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='MFColorRGBA')">
				<!-- TODO hex array constructor and accessors -->
				<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Replaces a single value at the appropriate location in the existing value array.
	 * @param index The position of the selected value in the current array
	 * @param hexColorValue The HTML color value (such as 0xAA2288) to insert
	 * @param alpha fourth component for opaqueness (1 - transparency)
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public MFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ set1Value(int index, int hexColorValue, float alpha) throws ArrayIndexOutOfBoundsException
	{
		if (index >= MFColorRGBA.length / 4) // tupleness factor
		{
			String errorNotice = "Array index=" + index + " (for 4-tuples) is greater than MFColor array length=" + MFColorRGBA.length;
			validationResult.append(errorNotice).append("\n");
			throw new ArrayIndexOutOfBoundsException(errorNotice);
		}
		
		// http://stackoverflow.com/questions/12798611/splitting-a-hex-number
						 
		float   red = ((hexColorValue>>16) & 0xff) / 255.0f;
		float green = ((hexColorValue>> 8) & 0xff) / 255.0f;
		float  blue = ((hexColorValue    ) & 0xff) / 255.0f;
						 
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA value (" + red + "," + green + "," + blue + "," + alpha +
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		MFColorRGBA[4*index + 0] = red;
		MFColorRGBA[4*index + 1] = green;
		MFColorRGBA[4*index + 2] = blue;
		MFColorRGBA[4*index + 3] = alpha;
		return this;
	}
	/**
	 * Complement all color values of array in RGB space (i.e. subtract each component from 1).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementRGB ()
	{
		for (int i = 0; i+3 < MFColorRGBA.length; i = i + 4)
		{
			MFColorRGBA[i+0] = 1.0f - MFColorRGBA[i+0];
			MFColorRGBA[i+1] = 1.0f - MFColorRGBA[i+1];
			MFColorRGBA[i+2] = 1.0f - MFColorRGBA[i+2];
		}
	}
	/**
	 * Complement each alpha value of array by subtracting it from 1.  Note transparency = (1 - alpha).
	 * @see <a href="https://en.wikipedia.org/wiki/Negative_(photography)">Wikipedia: Negative (photography)</a>
	 * @see <a href="https://en.wikipedia.org/wiki/Complementary_colors">Wikipedia: Complementary colors</a>
	 */
	public void complementAlpha ()
	{
		for (int i = 0; i+3 < MFColorRGBA.length; i = i + 4)
		{
			MFColorRGBA[i+3] = 1.0f - MFColorRGBA[i+3];
		}
	}
]]></xsl:text>
			</xsl:when>
			<xsl:when test="(@type='SFRotation')">
				<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Utility method converting degrees to radians.
	 * @param angleDegrees value to convert
	 * @return angle value in radians
	 */
	public static float degreesToRadians (float angleDegrees)
	{
		return (float) (angleDegrees * Math.PI / 180.0);
	}
	/**
	 * Utility method converting degrees to radians.
	 * @param angleDegrees value to convert
	 * @return angle value in radians
	 */
	public static float degreesToRadians (int angleDegrees)
	{
		return (float) (angleDegrees * Math.PI / 180.0);
	}
	/**
	 * Utility method converting degrees to radians.
	 * @param angleDegrees value to convert
	 * @return angle value in radians
	 */
	public static float degreesToRadians (double angleDegrees)
	{
		return (float) (angleDegrees * Math.PI / 180.0);
	}
	/**
	 * Utility method converting radians to degrees.
	 * @param angleRadians value to convert
	 * @return angle value in degrees
	 */
	public static float radiansToDegrees (float angleRadians)
	{
		return (float) (angleRadians * 180.0 / Math.PI);
	}
	/**
	 * Utility method converting radians to degrees.
	 * @param angleRadians value to convert
	 * @return angle value in degrees
	 */
	public static float radiansToDegrees (double angleRadians)
	{
		return (float) (angleRadians * 180.0 / Math.PI);
	}
	/**
	 * Public utility constructor using individual float types as new initial axis-angle value.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @param angleRadians fourth component
	 */
	public SFRotation]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (float x, float y, float z, float angleRadians)
	{
		if ((x == 0.0f) && (y == 0.0f) && (z == 0.0f))
		{
			String errorNotice = "Illegal SFRotation value (" + x + "," + y + "," + z + "," + angleRadians + 
				") since (x,y,z) axis vector must have a direction and cannot be (0,0,0)";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		if (Math.abs(angleRadians) > 2.0 * Math.PI)
			System.err.println ("SFRotation constructor: questionable |angleRadians| > 2pi");
		SFRotation[0] = x;
		SFRotation[1] = y;
		SFRotation[2] = z;
		SFRotation[3] = angleRadians;
	}
	/**
	 * Public utility constructor using individual double types as new initial axis-angle value.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @param angleRadians fourth component
	 */
	public SFRotation]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (double x, double y, double z, double angleRadians)
	{
		if ((x == 0.0) && (y == 0.0) && (z == 0.0))
		{
			String errorNotice = "Illegal SFRotation value (" + x + "," + y + "," + z + "," + angleRadians + 
				") since (x,y,z) axis vector must have a direction and cannot be (0,0,0)";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		if (Math.abs(angleRadians) > 2.0 * Math.PI)
			System.err.println ("SFRotation constructor: questionable |angleRadians| > 2pi");
		SFRotation[0] = (float) x;
		SFRotation[1] = (float) y;
		SFRotation[2] = (float) z;
		SFRotation[3] = (float) angleRadians;
	}
	/**
	 * Public utility constructor using individual integer types as new initial axis, along with float angle value.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @param angleRadians fourth component
	 */
	public SFRotation]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ (int x, int y, int z, float angleRadians)
	{
		if ((x == 0) && (y == 0) && (z == 0))
		{
			String errorNotice = "Illegal SFRotation value (" + x + "," + y + "," + z + "," + angleRadians + 
				") since (x,y,z) axis vector must have a direction and cannot be (0,0,0)";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		if (Math.abs(angleRadians) > 2.0 * Math.PI)
			System.err.println ("SFRotation constructor: questionable |angleRadians| > 2pi");
		SFRotation[0] = (float) x;
		SFRotation[1] = (float) y;
		SFRotation[2] = (float) z;
		SFRotation[3] = (float) angleRadians;
	}
]]></xsl:text>
			</xsl:when>
		</xsl:choose>

		<!-- Source code: parse method -->
		<xsl:text>
	/**
	 * Provide String representation of typed value.
	 * @param value The value to convert to a String
	 * @return String version of value
	 */
	public static String toString (</xsl:text>
	<xsl:value-of select="$javaType"/>
	<xsl:text> value)
	{</xsl:text>
	<xsl:choose>
		<xsl:when test="not(contains($javaType,'[]'))">
			<xsl:text>
		return String.valueOf(value);</xsl:text>
		</xsl:when>
		<xsl:when test="(@type='MFString')">
			<xsl:text>
		return (new MFString</xsl:text><xsl:value-of select="$jsaiClassSuffix"/>
			<xsl:text>(value)).toString();</xsl:text>
		</xsl:when>
		<xsl:otherwise>
			<xsl:text disable-output-escaping="yes"><![CDATA[
		StringBuilder result = new StringBuilder();
		for (int i=0; i < value.length; i++)
		{
			result.append(value[i]).append(" ");
		}
		return result.toString().trim();]]></xsl:text>
		</xsl:otherwise>
	</xsl:choose>
	<xsl:text>
	}</xsl:text>

	<xsl:choose>
		<xsl:when test="contains($fieldName,'FImage') or contains($fieldName,'FMatrix')">
			<!-- specialty methods defined later instead -->
		</xsl:when>
		<xsl:when test="contains($javaType,'[]')"> <!-- java array; may be SF type -->
<xsl:text><![CDATA[
	/**
	 * Get the current value by copying it into the valueDestination array.
	 *@param valueDestination The array to be filled in with current field values.
	 */
	@Override
	public void getValue(]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[ valueDestination)
	{
		valueDestination = ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text><![CDATA[;
	}
]]></xsl:text>
		</xsl:when>
		<xsl:otherwise>
<xsl:text><![CDATA[
	/**
	 * Get the current value.
	 * @return current value
	 */
	@Override
	public ]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[ getValue()
	{
		return ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text><![CDATA[;
	}
]]></xsl:text>
		</xsl:otherwise>
	</xsl:choose>

<!-- consistent utility method -->
<xsl:text><![CDATA[
	/**
	 * Utility method to get current value as a java primitive type
	 * @return current value
	 */
	public ]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[ getPrimitiveValue()
	{
		return ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text><![CDATA[;
	}]]></xsl:text>

<!-- consistent utility method -->
<xsl:text><![CDATA[
	/**
	 * Utility method to get current value as a String
	 * @return current value
	 */
	@Override
	public String toString()
	{
		]]></xsl:text>
	<xsl:choose>
		<xsl:when test="(@type = 'SFString')">
			<xsl:text>return </xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>;</xsl:text>
		</xsl:when>
		<xsl:when test="(@type = 'SFBool') or (@type = 'SFInt32') or (@type = 'SFDouble') or (@type = 'SFFloat') or (@type = 'SFTime')">
			<xsl:text>return String.valueOf(</xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>);</xsl:text>
		</xsl:when>
		<xsl:when test="(@type = 'MFString')">
			<xsl:text disable-output-escaping="yes"><![CDATA[StringBuilder result = new StringBuilder();
		for (int i = 0; i < ]]></xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>.length; i++)
		{
			if (!</xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text disable-output-escaping="yes">[i].startsWith("\""))
				result.append("\"");
			result.append(String.valueOf(</xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text disable-output-escaping="yes">[i]));
			if (!</xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text disable-output-escaping="yes"><![CDATA[[i].startsWith("\""))
				result.append("\"");
			if (i < ]]></xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>.length - 1)
				result.append(" ");
		}
		return result.toString();</xsl:text>
		</xsl:when>
		<xsl:when test="(@type = 'MFBool') or (@type = 'MFInt32') or (@type = 'MFDouble') or (@type = 'MFFloat') or (@type = 'MFString') or (@type = 'MFTime') or
                        contains(@type,'Color') or contains(@type,'Rotation') or contains(@type,'FVec')">
			<xsl:text disable-output-escaping="yes"><![CDATA[StringBuilder result = new StringBuilder();
		for (int i = 0; i < ]]></xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>.length; i++)
		{
			result.append(String.valueOf(</xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text disable-output-escaping="yes"><![CDATA[[i]));
			if (i < ]]></xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:text>.length - 1)
				result.append(" ");
		}
		return result.toString();</xsl:text>
		</xsl:when>
		<xsl:otherwise>
			<xsl:text>return "TODO"; // unimplemented type toString()</xsl:text>
		</xsl:otherwise>
	</xsl:choose>
	
	<xsl:text><![CDATA[
	}]]></xsl:text>

   <xsl:if test="not(starts-with(@type,'MF')) and not(@type = 'SFImage') and not(contains(@type,'Matrix'))">
<xsl:text><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param newValue The replacement value to assign.
	 */
	@Override
	public void setValue(]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text disable-output-escaping="yes"><![CDATA[ newValue)
	{
]]></xsl:text>		
		<!-- initial value checks -->
		<xsl:choose>
			<xsl:when test="starts-with(@type,'MF') and ends-with($javaType, '[]') and ($tupleSize > 1)">
				<xsl:value-of select="$newValueNullReturnVoid"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[
		if      (newValue == null)
			     newValue = DEFAULT_VALUE;
		else if (newValue.length % ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ != 0) // ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[-tuple check
		{
			String errorNotice = "Illegal ]]></xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ float[] array length=" + newValue.length +
				", must be multiple of ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ or else be empty (newValue=" + toString(newValue) + ")";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
			</xsl:when>
			<xsl:when test="starts-with(@type,'SF') and ends-with($javaType, '[]') and ($tupleSize > 1)">
				<xsl:value-of select="$newValueNullReturnVoid"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[
		if      (newValue == null)
			     newValue = DEFAULT_VALUE;
		else if (newValue.length != ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[)
		{
			String errorNotice = "Illegal ]]></xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ float[] array length=" + newValue.length +
				", must equal ]]></xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes"><![CDATA[ or else be empty (newValue=" + toString(newValue) + ")";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
			</xsl:when>
		<xsl:when test="ends-with($javaType, '[]')"><!-- ($tupleSize == 1) -->
			<xsl:value-of select="$newValueNullReturnVoid"/>
			<xsl:text disable-output-escaping="yes"><![CDATA[
		if (newValue == null)
			newValue = DEFAULT_VALUE;
		]]></xsl:text>
			</xsl:when>
		</xsl:choose>
		<xsl:if test="(@type = 'SFRotation')">
			<xsl:text disable-output-escaping="yes"><![CDATA[
		float            x = newValue[0];
		float            y = newValue[1];
		float            z = newValue[2];
		float angleRadians = newValue[3];
		if ((x == 0.0f) && (y == 0.0f) && (z == 0.0f))
		{
			String errorNotice = "Illegal SFRotation value (" + x + "," + y + "," + z + "," + angleRadians + 
				") since (x,y,z) axis vector must have a direction and cannot be (0,0,0)";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		if (Math.abs(angleRadians) > 2.0 * Math.PI)
			System.err.println ("SFRotation constructor: questionable |angleRadians| > 2pi");
]]></xsl:text>
		</xsl:if>
	<xsl:choose>
		<xsl:when test="(@type='SFColor')">
			<xsl:text disable-output-escaping="yes"><![CDATA[
		// initial value checks
		float   red = newValue[0];
		float green = newValue[1];
		float  blue = newValue[2];
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
		</xsl:when>
		<xsl:when test="(@type='SFColorRGBA')">
			<xsl:text disable-output-escaping="yes"><![CDATA[
		// initial value checks
		float   red = newValue[0];
		float green = newValue[1];
		float  blue = newValue[2];	
		float alpha = newValue[3];	
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA value (" + red + "," + green + "," + blue + "," + alpha + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
		</xsl:when>
	</xsl:choose>
	<xsl:if test="not($isSingletonType = 'true')">
		<xsl:text>if (newValue.length != </xsl:text>
		<xsl:value-of select="$tupleSize"/>
		<xsl:text><![CDATA[)
		{
			String errorNotice = "newValue.length=" + newValue.length + " is greater than ]]></xsl:text>
		<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ tuple size=" + ]]></xsl:text>
		<xsl:value-of select="$tupleSize"/><xsl:text disable-output-escaping="yes"><![CDATA[;
			validationResult.append(errorNotice).append("\n");
			throw new ArrayIndexOutOfBoundsException(errorNotice);
		}
]]></xsl:text>
	</xsl:if>
	<xsl:value-of select="$fieldName"/>
	<xsl:text><![CDATA[ = newValue; // TODO check newValue length for array types
	}
]]></xsl:text>
   </xsl:if>
					<xsl:if test="starts-with(@type,'MF') and not(@type = 'MFImage') and not(contains(@type, 'FMatrix'))">
						<xsl:text disable-output-escaping="yes"><![CDATA[
/**
* <p>
* Get an individual value from this field array.
* </p><p>
* If the index is outside the bounds of the current array of data values, an ArrayIndexOutOfBoundsException is thrown.
* </p>
* @param index The position of the selected value in the current array]]></xsl:text>
<xsl:choose>
	<xsl:when test="($isSingletonType = 'true')">
		<xsl:text>
* @return The selected value</xsl:text>
	</xsl:when>
	<xsl:otherwise>
		<xsl:text>
* @param destinationValue where to place result for selected value</xsl:text>		
	</xsl:otherwise>
</xsl:choose>
<xsl:text disable-output-escaping="yes"><![CDATA[
* @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
*/
@Override
public ]]></xsl:text>
	<xsl:choose>
		<xsl:when test="($isSingletonType = 'true')">
			<xsl:value-of select="$javaPrimitiveType"/>
			<xsl:text> get1Value(int index)</xsl:text>
		</xsl:when>
		<xsl:otherwise>
			<xsl:text>void get1Value(int index, </xsl:text>
			<xsl:value-of select="$javaPrimitiveType"/>
			<xsl:text> destinationValue)</xsl:text>
		</xsl:otherwise>
	</xsl:choose>
	<xsl:text disable-output-escaping="yes"><![CDATA[
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
]]></xsl:text>
	<xsl:choose>
		<xsl:when test="($isSingletonType = 'true')">
			<xsl:text>	return </xsl:text>
			<xsl:value-of select="$fieldName"/>
			<xsl:choose>
				<xsl:when test="not(contains($javaPrimitiveType,'['))">
					<xsl:text>[index];</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:text>; // TODO fix array subset slicing [index];</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:when>
		<xsl:otherwise>
			<xsl:text>   // TODO fix array subset slicing</xsl:text>
		</xsl:otherwise>
	</xsl:choose>
<xsl:text disable-output-escaping="yes"><![CDATA[
}

/**
* Assign a new value to this field.
* @param size indicates size of result to apply to newValue array.
* @param newValue The replacement value array to assign.
*/
@Override
public void setValue(int size, ]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[ newValue)
{
	]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
	]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ = newValue; // TODO array size slicing
}
]]></xsl:text>
	<xsl:if test="(@type = 'MFRotation') or contains(@type,'FVec')">
		<!-- also add methods for square arrays -->
<xsl:text disable-output-escaping="yes"><![CDATA[
  /**
   * Get the current value by copying it into the valueDestination array.
   */
  @Override
  public void getValue(]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[[] valueDestination)
  {
	// TODO square array adjustment //// valueDestination = ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text><![CDATA[;
  }

/**
* Assign a new value to this field.
* @param size indicates size of result to apply to newValue array.
* @param newValue The replacement value array to assign.
*/
@Override
public void setValue(int size, ]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[[] newValue)
{
	]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
	// TODO array size slicing, handle double subscripts
}
]]></xsl:text>		
	</xsl:if>
<xsl:text disable-output-escaping="yes"><![CDATA[
/**
* Utility method to assign a new value to this field.
* @param newValue The replacement value array to assign.
*/	
public void setValue(]]></xsl:text><xsl:value-of select="$javaType"/><xsl:text><![CDATA[ newValue)
{
	if (newValue == null)
		newValue = new ]]></xsl:text>
		<xsl:value-of select="substring-before($javaType,'[]')"/>
		<xsl:text>[0];
	</xsl:text>
		<xsl:value-of select="$fieldName"/>
		<xsl:text disable-output-escaping="yes"><![CDATA[ = newValue; // TODO verify size for array types
}

/**
* Replaces a single value at the appropriate location in the existing value array.
* @param index The position of the selected value in the current array
* @param newValue The newValue to insert
*/
@Override
public void set1Value(int index, ]]></xsl:text><xsl:value-of select="$javaPrimitiveType"/><xsl:text><![CDATA[ newValue) throws ArrayIndexOutOfBoundsException
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
	// TODO ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[[index] = newValue;
}

/**
* Places a new value at the end of the existing value array, increasing the field length accordingly.
* @param newValue The newValue to append
*/
@Override
public void append(]]></xsl:text><xsl:value-of select="$javaPrimitiveType"/><xsl:text><![CDATA[ newValue)
{
	// TODO
}

/**
* Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
* @param index The position for the inserted value in the current array
* @param newValue The newValue to insert
*/
@Override
public void insertValue(int index, ]]></xsl:text><xsl:value-of select="$javaPrimitiveType"/><xsl:text><![CDATA[ newValue)
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
		
	// TODO
}
]]></xsl:text>
	<xsl:if test="(@type = 'MFTime')">
<xsl:text disable-output-escaping="yes"><![CDATA[
/**
* Places a new value at the end of the existing value array, increasing the field length accordingly.
* @param newValue The newValue to append
*/
@Override
public void append(long newValue)
{
	// TODO
}
	
/**
* Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
* @param index The position for the inserted value in the current array
* @param newValue The newValue to insert
*/
@Override
public void insertValue(int index, long newValue)
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
		
	// TODO
}
		
/**
* Replaces a single value at the appropriate location in the existing value array.
* @param index The position of the selected value in the current array
* @param newValue The newValue to insert
*/
@Override
public void set1Value(int index, long newValue) throws ArrayIndexOutOfBoundsException
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[;
		]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[[index] = (double) newValue;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
}
		
/**
* Replaces a single value at the appropriate location in the existing value array.
* @param index The position of the selected value in the current array
* @param newValue The newValue to insert
*/
@Override
public void setValue(int index, long[] newValue) throws ArrayIndexOutOfBoundsException
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[;
		// TODO copy, cast array // ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[[index] = (double) newValue;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}
}
]]></xsl:text>
	</xsl:if>
<xsl:text disable-output-escaping="yes"><![CDATA[
/**
 * Get the size of the underlying data array. The size is the number of
 * elements for that data type. So for an MFFloat the size would be the
 * number of float values, but for an MFVec3f, it is the number of vectors
 * in the returned array (where a vector is 3 consecutive array indexes in
 * a flat array).
 *
 * @return The number of elements in this field array.
 */
@Override
public int size()
{
	return ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:value-of select="$dimensionSuffix"/><xsl:text disable-output-escaping="yes"><![CDATA[;
}

/**
 * Removes all values in the field array, and changes the array size to zero.
 */
@Override
public void clear()  // here?
{
	]]></xsl:text>
	<xsl:value-of select="$fieldName"/>
	<xsl:text disable-output-escaping="yes"><![CDATA[ = new ]]></xsl:text>
	<xsl:choose>
		<xsl:when test="contains($javaPrimitiveType,'[')">
			<xsl:value-of select="substring-before($javaPrimitiveType,'[')"/>
		</xsl:when>
		<xsl:otherwise>
			<xsl:value-of select="$javaPrimitiveType"/>
		</xsl:otherwise>
	</xsl:choose>
	<xsl:text disable-output-escaping="yes"><![CDATA[[0];
}

/**
 * Remove one element of the field array at index position, if found.  Initial element is at index 0.
 * @param index The position of the element in the field array that gets removed.
 */
@Override
public void remove(int index)
{
	// TODO tupleness factor
	if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length)
	{
		String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
	<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length;
		validationResult.append(errorNotice).append("\n");
		throw new ArrayIndexOutOfBoundsException(errorNotice);
	}

	// TODO
}
]]></xsl:text>
					</xsl:if>

					<!-- specialized utility methods for field types in Java SAI specification -->
					<xsl:choose>
						<xsl:when test="(@type = 'SFTime')">
<xsl:text><![CDATA[	
/**
*	Get the current value.
* 	@return current value
*/
@Override
public long getJavaValue()
{
	return (long)SFTime;
}	
/**
* Assign a new value, converting seconds from (long) to (double).
* @param newValue The replacement value to assign.
*/
@Override
public void setValue(long newValue)
{
	SFTime = (double)newValue;
}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'MFTime')">
					<xsl:text><![CDATA[
/**
*	Get a single value.
* 	@return single value
*/
@Override
public long get1JavaValue(int index)
{
	return (long)MFTime[index];
}

/**
* Assign a new value array, converting seconds from (long) to (double).
* @param newValue The replacement value array to assign.
*/
@Override
public void setValue(long[] newValue)
{
]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
	// create new array and cast each value
	MFTime = new double[newValue.length];
	for (int i=0;i < newValue.length; i++)
	{
		MFTime[i] = (double)newValue[i];
	}
}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="starts-with(@type,'MFColor')">
							<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	@Override
	public void getValue(float[][] valueDestination)
	{
		// TODO
	}

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */
	@Override
	public void setValue(int size, float[][] newValue)
	{
]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
		// TODO
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test = "(@type = 'SFImage')">
							<xsl:text><![CDATA[
    /**
     * Get the width of the image.
     * @throws InvalidFieldValueException Invalid SFImage data found
     * @return The width of the image in pixels
     */
	@Override
	public int getWidth()
	{
		if  ((SFImage == null) || (SFImage.length < 3))
		{
			String errorNotice = "Null array or illegal data length for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		int      width = SFImage[0];
		int     height = getHeight();
		if ((width < 0) || (height < 0))
		{
			String errorNotice = "Illegal negative value: width=" + width + ", height=" + height + 
				" for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		return SFImage[0];
	}

    /**
     * Get the height of the image.
     * @throws InvalidFieldValueException Invalid SFImage data found
     * @return The height of the image in pixels
     */
	@Override
	public int getHeight()
	{
		if  ((SFImage == null) || (SFImage.length < 3))
		{
			String errorNotice = "Null array or illegal data length for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		int      width = getWidth();
		int     height = SFImage[1];
		if ((width < 0) || (height < 0))
		{
			String errorNotice = "Illegal negative value: width=" + width + ", height=" + height + 
				" for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		return SFImage[1];
	}

    /**
     * Get the number of color components in the image. The value will
     * always be between 1 and 4 indicating the number of components of
     * the color specification to be read from the image pixel data.
     * @throws InvalidFieldValueException Invalid SFImage data found
     * @return The number of components
     */
	@Override
	public int getComponents()
	{
		if  ((SFImage == null) || (SFImage.length < 3))
		{
			String errorNotice = "Null array or illegal data length for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		int components = SFImage[2];
		if ((components < 1) || (components > 4))
		{
			String errorNotice = "Illegal value, must be in range [1..4]: number of components=" + components + 
				" for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		return SFImage[2];
	}

    /**
     * Get the image pixel value in the given eventOut.
     * <p>
     * The number of items in the pixels array will be
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     * @param destinationPixels The array to copy pixel values into
     * @throws InvalidFieldValueException Invalid SFImage data found
     */
	@Override
	public void getPixels(int[] destinationPixels)
	{
		if  ((SFImage == null) || (SFImage.length < 3))
		{
			String errorNotice = "Null array or illegal data length for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}		
		int      width = getWidth();
		int     height = getHeight();
		int components = getComponents(); // includes error checks
		destinationPixels = new int[SFImage.length];	
		if ((width == 0) || (height == 0) || (components == 0))
		{
			destinationPixels = new int[0];
		}
		else if (SFImage.length > 3)
		{
			destinationPixels = new int[width * height * components];			// TODO necessary?
			destinationPixels = Arrays.copyOfRange(SFImage, 3, SFImage.length); // TODO verify
		}
		else
		{
			String errorNotice = "Illegal value for SFImage field type, getPixels() cannot get pixel array";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
	}

    /**
     * Fetch the Java representation of the underlying image from these pixels.
     * This is the same copy that the browser uses to generate texture
     * information from.
     * @return The image reference representing the current state
     */
	@Override
	public java.awt.image.WritableRenderedImage getImage()
	{
		return null; // TODO
	}

    /**
     * Set the image value in the given writable field to the new image defined
     * by a set of pixels.
     * <p>
     * @param image The new image to use as the source
     */
	@Override
	public void setImage(java.awt.image.RenderedImage image)
	{
		// TODO
	}

    /**
	 * Copy a region of the argument RenderedImage to replace a portion of the
	 * current SFimage.
	 * <p>
	 * The sub image set shall not resize the base image representation and
	 * therefore performs an intersection clip of the provided image. The user
	 * provided image shall be of the same format (pixel depth, pixel
	 * representation) as the original image obtained through the getImage()
	 * method.
	 * <p>
	 * RenderedImages are row order from top to bottom. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 0 |********|
	 * 1 |********|
	 * 2 |********|
	 * 3 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * SFImages are row order from bottom to top. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 3 |********|
	 * 2 |********|
	 * 1 |********|
	 * 0 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * <p>
	 * Note: The parameter srcYOffset is referenced to the RenderedImage object
	 * (indexed top to bottom).
	 * <br>
	 * The parameter destYOffset is referenced to the SFImage object
	 * (indexed bottom to top).
	 *
	 * @param image The new image to use as the source
	 * @param sourceWidth The width of the argument sub-image region to copy
	 * @param sourceHeight The height of the argument sub-image region to copy
	 * @param sourceXOffset The initial x dimension (width) offset into the
	 * argument sub-image that begins the region to copy
	 * @param sourceYOffset The initial y dimension (height) offset into the
	 * argument sub-image that begins the region to copy
	 * @param destinationXOffset The initial x dimension (width) offset in the SFimage
	 * object that begins the region to receive the copy
	 * @param destinationYOffset The initial y dimension (height) offset in the SFimage
	 * object that begins the region to receive the copy
	 */
	@Override
	public void setSubImage(java.awt.image.RenderedImage image,
                            int sourceWidth,
                            int sourceHeight,
                            int sourceXOffset,
                            int sourceYOffset,
                            int destinationXOffset,
                            int destinationYOffset)
	{
		// TODO
	}

    /**
     * Set the image value in the given writable field.
     * <p>
     * Image values are specified using a width, height and the number of
     * components. The number of items in the pixels array must be at least
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components. If the integer
     * contains values in bytes that are not used by the number of components
     * for that image, the values are ignored.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     *
     * @param width The width of the image in pixels
     * @param height The height of the image in pixels
     * @param components The number of color components [1-4]
     * @param pixels The array of pixel values as specified above.
     * @exception IllegalArgumentException The number of components or width/
     *    height are illegal values.
     * @exception ArrayIndexOutOfBoundsException The number of pixels provided by the
     *    caller is not enough for the width * height.
     * @throws IllegalArgumentException Invalid parameter(s) provided, no change was made
     */
	@Override
	public void setValue(int width,
                         int height,
                         int components,
                         int[] pixels)
	{
		if ((width < 0) || (height < 0))
		{
			String errorNotice = "Illegal negative value: width=" + width + ", height=" + height + 
				" for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}
		if ((components < 1) || (components > 4))
		{
			String errorNotice = "Illegal value, must be in range [1..4]: number of components=" + components + 
				" for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}
		if (((width * height * components) > 0) && (pixels.length < (width * height)))
		{
			String errorNotice = "Illegal number of pixels: pixels.length=" + pixels.length +
				", (width * height * components) = " + width + " * " + components + " * " + components + ") = " + 
				(width * height * components) + " for SFImage field type";
			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}					
		SFImage = new int[3 + (width * height)];
		SFImage[0] = width;
		SFImage[1] = height;
		SFImage[2] = components;
		System.arraycopy(pixels, 0, SFImage, 3, pixels.length);
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test = "(@type = 'MFImage')">
							<xsl:text><![CDATA[
    /**
     * Get the width of the image array.
     * @param imageIndex the index of the selected image
     * @return The width of the image in pixels
     */
	@Override
	public int getWidth(int imageIndex)
	{
		return 0; // TODO access correct image, return value
	}

    /**
     * Get the height of the image array.
     * @param imageIndex the index of the selected image
     * @return The height of the image in pixels
     */
	@Override
	public int getHeight(int imageIndex)
	{
		return 0; // TODO access correct image, return value
	}

    /**
     * Get the number of color components in the image. The value will
     * always be between 1 and 4 indicating the number of components of
     * the color specification to be read from the image pixel data.
     * @param imageIndex the index of the selected image
     * @return The number of components
     */
	@Override
	public int getComponents(int imageIndex)
	{
		return 0; // TODO access correct image, return value
	}

    /**
     * Get the image pixel value in the given eventOut.
     * <p>
     * The number of items in the pixels array will be
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     * @param imageIndex the index of the selected image
     * @param pixels The array to copy pixel values into
     */
	@Override
	public void getPixels(int imageIndex, int[] pixels)
	{
		// TODO
	}

    /**
     * Fetch the Java representation of the underlying image from these pixels.
     * This is the same copy that the browser uses to generate texture
     * information from.
     * @param imageIndex the index of the selected image
     * @return The image reference representing the current state
     */
	@Override
	public WritableRenderedImage getImage(int imageIndex)
	{
		return null; // TODO
	}

    /**
     * Set the image value in the given writable field to the new image defined
     * by a set of pixels.
     * @param imageIndex the index of the selected image
     * @param image The new image to use as the source
     */
	@Override
	public void setImage(int imageIndex, RenderedImage image)
	{
		// TODO
	}

    /**
	 * Copy a region of the argument RenderedImage to replace a portion of the
	 * current SFimage.
	 * <p>
	 * The sub image set shall not resize the base image representation and
	 * therefore performs an intersection clip of the provided image. The user
	 * provided image shall be of the same format (pixel depth, pixel
	 * representation) as the original image obtained through the getImage()
	 * method.
	 * <p>
	 * RenderedImages are row order from top to bottom. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 0 |********|
	 * 1 |********|
	 * 2 |********|
	 * 3 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * SFImages are row order from bottom to top. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 3 |********|
	 * 2 |********|
	 * 1 |********|
	 * 0 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * <p>
	 * Note: The parameter srcYOffset is referenced to the RenderedImage object
	 * (indexed top to bottom).
	 * <br>
	 * The parameter destYOffset is referenced to the SFImage object
	 * (indexed bottom to top).
	 *
	 * @param imageIndex the index of the selected image
	 * @param image The new image to use as the source
	 * @param sourceWidth The width of the argument sub-image region to copy
	 * @param sourceHeight The height of the argument sub-image region to copy
	 * @param sourceXOffset The initial x dimension (width) offset into the
	 * argument sub-image that begins the region to copy
	 * @param sourceYOffset The initial y dimension (height) offset into the
	 * argument sub-image that begins the region to copy
	 * @param destinationXOffset The initial x dimension (width) offset in the SFimage
	 * object that begins the region to receive the copy
	 * @param destinationYOffset The initial y dimension (height) offset in the SFimage
	 * object that begins the region to receive the copy
	 */
	@Override
	public void setSubImage(int imageIndex,
		RenderedImage image,
		int sourceWidth,
		int sourceHeight,
		int sourceXOffset,
		int sourceYOffset,
		int destinationXOffset,
		int destinationYOffset)
	{
		// TODO
	}

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param imageIndex the index of the selected image
     * @param newValue The newValue to set
     */
	@Override
	public void set1Value(int imageIndex, int newValue)
	{
		// TODO
	}

	@Override
	public void set1Value(int imageIndex,
		int width,
		int height,
		int components,
		int[] pixels)
	{
		// TODO
	}

    /**
     * Assign a new value array containing imageIndex, width, height, and components count, followed by array of pixels.
     * @param newValue The newValue to set
     */	
	@Override
	public void setValue(int[] newValue)
	{
]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
		// TODO
	}

	@Override
	public void setImage(RenderedImage[] image)
	{
		// TODO
	}

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	@Override
	public void append(RenderedImage[] newValue)
	{
]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
		// TODO
	}

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	@Override
	public void insertValue(int index, RenderedImage newValue)
	{
]]></xsl:text>
	<xsl:value-of select="$newValueNullExceptionCheck"/>
	<xsl:text><![CDATA[
		// TODO
	}
	/**
	 * Remove one element of the field array at index position, if found.  Initial element is at index 0.
	 * @param index The position of the element in the field array that gets removed.
	 */
	@Override
	public void remove (int index)
	{
		// TODO compute offset factor
		if (index >= ]]></xsl:text><xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length)
		{
			String errorNotice = "Array index=" + index + " is greater than ]]></xsl:text>
		<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ array length=" + ]]></xsl:text>
		<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length;
			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}
			
		// TODO
	}
	/**
	 * Removes all values in the field array, and changes the array size to zero.
	 */
	@Override
	public void clear()
	{
		]]></xsl:text>
		<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[ = new ]]></xsl:text><xsl:value-of select="substring-before($javaType,'[')"/><xsl:text disable-output-escaping="yes"><![CDATA[[0];
	}
	/**
	 * Get the size of the underlying data array. The size is the number of
	 * elements for that data type. So for an MFFloat the size would be the
	 * number of float values, but for an MFVec3f, it is the number of vectors
	 * in the returned array (where a vector is 3 consecutive array indexes in
	 * a flat array).
	 *
	 * @return The number of elements in this field array.
	 */
	@Override
	public int size()
	{
		return ]]></xsl:text>
		<xsl:value-of select="$fieldName"/><xsl:text disable-output-escaping="yes"><![CDATA[.length;
	}
]]></xsl:text>
					</xsl:when>
					<xsl:when test="(@type = 'SFMatrix3f') or (@type = 'MFMatrix3f')">
						<xsl:text disable-output-escaping="yes"><![CDATA[
	@Override
	public void setIdentity()
	{
		// TODO
	}

	@Override
	public void set(int row, int column)
	{
		// TODO
	}

	@Override
	public float get(int row, int column)
	{
		return 0.0f; // TODO
	}

	@Override
	public void setTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale,
		SFRotation scaleOrientation,
		SFVec3f center)
	{
		// TODO
	}

	@Override
	public void getTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale)
	{
		// TODO
	}

	@Override
	public Matrix3 inverse()
	{
		return null; // TODO
	}

	@Override
	public Matrix3 transpose()
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyLeft (Matrix3 matrix3x3)
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyRight(Matrix3 matrix3x3)
	{
		return null; // TODO
	}
	@Override
	public Matrix3 multiplyRowVector(SFVec3f vector3f) // TODO SFVec4f ?
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyColVector(SFVec3f vector3f) // TODO SFVec4f ?
	{
		return null; // TODO
	}
]]></xsl:text>
					</xsl:when>
					<xsl:when test="(@type = 'SFMatrix3d') or (@type = 'MFMatrix3d')">
						<xsl:text disable-output-escaping="yes"><![CDATA[
	@Override
	public void setIdentity()
	{
		// TODO
	}

	@Override
	public void set(int row, int column)
	{
		// TODO
	}

	@Override
	public float get(int row, int column)
	{
		return 0.0f; // TODO
	}

	@Override
	public void setTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale,
		SFRotation scaleOrientation,
		SFVec3d center)
	{
		// TODO
	}

	@Override
	public void getTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale)
	{
		// TODO
	}

	@Override
	public Matrix3 inverse()
	{
		return null; // TODO
	}

	@Override
	public Matrix3 transpose()
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyLeft (Matrix3 matrix3x3)
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyRight(Matrix3 matrix3x3)
	{
		return null; // TODO
	}
	@Override
	public Matrix3 multiplyRowVector(SFVec3d vector3d) // TODO SFVec4d ?
	{
		return null; // TODO
	}

	@Override
	public Matrix3 multiplyColVector(SFVec3d vector3d) // TODO SFVec4d ?
	{
		return null; // TODO
	}
]]></xsl:text>
					</xsl:when>
					<xsl:when test="(@type = 'SFMatrix4f') or (@type = 'MFMatrix4f')">
						<xsl:text disable-output-escaping="yes"><![CDATA[
	@Override
	public void setIdentity()
	{
		// TODO
	}

	@Override
	public void set(int row, int column)
	{
		// TODO
	}

	@Override
	public float get(int row, int column)
	{
		return 0.0f; // TODO
	}

	@Override
	public void setTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale,
		SFRotation scaleOrientation,
		SFVec3f center)
	{
		// TODO
	}

	@Override
	public void getTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale)
	{
		// TODO
	}

	@Override
	public Matrix4 inverse()
	{
		return null; // TODO
	}

	@Override
	public Matrix4 transpose()
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyLeft (Matrix4 matrix3x3)
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyRight(Matrix4 matrix3x3)
	{
		return null; // TODO
	}
	@Override
	public Matrix4 multiplyRowVector(SFVec3f vector3f) // TODO SFVec4f ?
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyColVector(SFVec3f vector3f) // TODO SFVec4f ?
	{
		return null; // TODO
	}
]]></xsl:text>
					</xsl:when>
					<xsl:when test="(@type = 'SFMatrix4d') or (@type = 'MFMatrix4d')">
						<xsl:text disable-output-escaping="yes"><![CDATA[
	@Override
	public void setIdentity()
	{
		// TODO
	}

	@Override
	public void set(int row, int column)
	{
		// TODO
	}

	@Override
	public float get(int row, int column)
	{
		return 0.0f; // TODO
	}

	@Override
	public void setTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale,
		SFRotation scaleOrientation,
		SFVec3d center)
	{
		// TODO
	}

	@Override
	public void getTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale)
	{
		// TODO
	}

	@Override
	public Matrix4 inverse()
	{
		return null; // TODO
	}

	@Override
	public Matrix4 transpose()
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyLeft (Matrix4 matrix3x3)
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyRight(Matrix4 matrix3x3)
	{
		return null; // TODO
	}
	@Override
	public Matrix4 multiplyRowVector(SFVec3d vector3d) // TODO SFVec4d ?
	{
		return null; // TODO
	}

	@Override
	public Matrix4 multiplyColVector(SFVec3d vector3d) // TODO SFVec4d ?
	{
		return null; // TODO
	}
]]></xsl:text>
					</xsl:when>
					</xsl:choose>
					
					<!-- additional utility methods for field types -->
					<!-- setValue convenience methods -->
					<xsl:choose>
						<xsl:when test="(@type = 'SFFloat')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Apply a double value to this float field type, note change in precision.
	 * @param newValue The double newValue to apply
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[  setValue(double newValue)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[ = (float) newValue;
		return this;
	}
	/*
	 * Apply an int value to this float field type, note change in precision.
	 * @param newValue The int newValue to apply
	 * @return {@link SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ } - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFFloat]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[  setValue(int newValue)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[ = (float) newValue;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFDouble') or (@type = 'SFTime')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Apply a float value to this double field type, note change in precision.
	 * @param newValue The float newValue to apply
	 * @return {@link ]]></xsl:text>
							<xsl:value-of select="@type"/>
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public ]]></xsl:text>
							<xsl:value-of select="@type"/>
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
							<xsl:text> setValue(float newValue)
	{
		</xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[ = (double) newValue;
		return this;
	}
	/*
	 * Apply an int value to this double field type, note change in precision.
	 * @param newValue The float newValue to apply
	 * @return {@link ]]></xsl:text>
							<xsl:value-of select="@type"/>
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
							<xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public ]]></xsl:text>
							<xsl:value-of select="@type"/>
							<xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
							<xsl:text> setValue(int newValue)
	{
		</xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[ = (double) newValue;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec2d')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @return {@link SFVec2d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec2d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(double x, double y)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec3d')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @return {@link SFVec3d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec3d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(double x, double y, double z)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[2] = z;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec4d')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @param t third component
	 * @return {@link SFVec4d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec4d]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(double x, double y, double z, double t)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[2] = z;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[3] = t;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec2f')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @return {@link SFVec2f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec2f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(float x, float y)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec3f')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @return {@link SFVec3f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec3f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(float x, float y, float z)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[2] = z;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFColor')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param red first component
	 * @param green second component
	 * @param blue third component
	 * @return {@link SFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFColor]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(float red, float green, float blue)
	{
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f))
		{
			String errorNotice = "Illegal SFColor value (" + red + "," + green + "," + blue + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = red;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = green;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[2] = blue;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFColorRGBA')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param red first component
	 * @param green second component
	 * @param blue third component
	 * @param alpha fourth component for opaqueness (1 - transparency)
	 * @return {@link SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(float red, float green, float blue, float alpha)
	{
		if ((red < 0.0f) || (red > 1.0f) || (green < 0.0f) || (green > 1.0f) || (blue < 0.0f) || (blue > 1.0f) || (alpha < 0.0f) || (alpha > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA value (" + red + "," + green + "," + blue + "," + alpha + 
				"), all values must be in numeric range [0..1]";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = red;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = green;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text disable-output-escaping="yes"><![CDATA[[2] = blue;
		return this;
	}
	/** Utility method to modify transparency
	 * @param newTransparency value [0..1]
	 * @return {@link SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFColorRGBA]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setTransparency (float newTransparency)
	{
		if ((newTransparency < 0.0f) || (newTransparency > 1.0f))
		{
			String errorNotice = "Illegal SFColorRGBA transparency value=" + newTransparency + 
												 ", must be within numeric range [0..1] inclusive";
			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		SFColorRGBA[3] = newTransparency;
		return this;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="(@type = 'SFVec4f')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Assign a new value to this field.
	 * @param x first component
	 * @param y second component
	 * @param z third component
	 * @param t fourth component
	 * @return {@link SFVec4f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public SFVec4f]]></xsl:text><xsl:value-of select="$jsaiClassSuffix"/><!-- append to type name -->
					 <xsl:text disable-output-escaping="yes"><![CDATA[ setValue(float x, float y, float z, float t)
	{
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[0] = x;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[1] = y;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[2] = z;
		]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[[3] = t;
		return this;
	}
]]></xsl:text>
						</xsl:when>
					</xsl:choose>
					<!-- primitive array methods -->
					<xsl:choose>
						<xsl:when test="contains(@type,'FVec2f')    or contains(@type,'FVec3f')    or contains(@type,'FVec4f')    or
										contains(@type,'FMatrix2f') or contains(@type,'FMatrix3f') or contains(@type,'FMatrix4f') or
										contains(@type,'MFFloat')   or contains(@type,'FColor')    or contains(@type,'FRotation')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Provide float array for this field type.
	 *
	 * @return Array of floats in this field array.
	 */
	public float[] toFloatArray()
	{
		return ]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[;
	}
]]></xsl:text>
						</xsl:when>
						<xsl:when test="contains(@type,'FVec2d')    or contains(@type,'FVec3d')    or contains(@type,'FVec4d')    or
										contains(@type,'FMatrix2d') or contains(@type,'FMatrix3d') or contains(@type,'FMatrix4d') or
										contains(@type,'MFTime')    or contains(@type,'MFDouble')">
							<xsl:text disable-output-escaping="yes"><![CDATA[
	/**
	 * Provide double array for this field type.
	 *
	 * @return Array of doubles in this field array.
	 */
	public double[] toFloatArray()
	{
		return ]]></xsl:text>
							<xsl:value-of select="$fieldName"/>
							<xsl:text><![CDATA[;
	}
]]></xsl:text>
						</xsl:when>
					</xsl:choose>
					
					<!-- class implementation definitions are complete -->
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
		
		</xsl:for-each>
		
			<!-- concrete implementation customization classes -->
		
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:text>X3DConcreteField</xsl:text></xsl:with-param>
				<xsl:with-param name="imports">
					<xsl:text>import java.util.ArrayList;
import org.web3d.x3d.sai.X3DFieldEventListener;</xsl:text>
				</xsl:with-param>
				<xsl:with-param name="inConcretePackage"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="isAbstract"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text><!-- TODO X3DConcreteElement --></xsl:text></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.X3DField</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:text>fields</xsl:text></xsl:with-param>
				<xsl:with-param name="description">
					<xsl:text>Concrete implementation class corresponding to X3DField.</xsl:text>
				</xsl:with-param>
				<!-- TODO update -->
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.11 X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.15 SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="InterfaceDefinition/@specificationUrl"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="InterfaceDefinition/@specificationUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock">
					<xsl:value-of select="InterfaceDefinition/@appinfo"/>
				</xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[
	// ===== Member value declarations are encapsulated and private, using preferred Java types for concretes library =====
										
	private boolean readable = true;
						
	private boolean writable = true;
						
	private ArrayList<X3DFieldEventListener> eventListenerList = new ArrayList<>();
		
	/** Results of local validation */
	protected static StringBuilder validationResult;
				
	/** Get output of results from prior validation, if any
	 * @return validation results
	 */		
	public String getValidationResult()
	{
		return validationResult.toString();
	}
						
	public X3DConcreteFieldDefinition getDefinition()
	{
		return null; // TODO
	}

	@Override
	public boolean isReadable()
	{
		return readable;
	}
						
	public void setReadable(boolean newValue)
	{
		readable = newValue;
	}

	@Override
	public boolean isWritable()
	{
		return writable;
	}
						
	public void setWritable(boolean newValue)
	{
		readable = newValue;
	}

	@Override
	public void addX3DEventListener(X3DFieldEventListener newListener)
	{
		eventListenerList.add(newListener);
	}

	@Override
	public void removeX3DEventListener(X3DFieldEventListener listener)
	{
		eventListenerList.remove(listener);
	}
	/*
	@Override
	public String validate()
	{
		return ""; // TODO
	}
	*/
]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
	
		<!-- ===================================================== -->
		
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:text>X3DConcreteFieldDefinition</xsl:text></xsl:with-param>
				<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="isAbstract"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.X3DFieldDefinition</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:text>fields</xsl:text></xsl:with-param>
				<xsl:with-param name="description">
					<xsl:text>Concrete implementation class corresponding to X3DField.</xsl:text>
				</xsl:with-param>
				<!-- TODO update -->
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.11 X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.15 SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="InterfaceDefinition/@specificationUrl"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="InterfaceDefinition/@specificationUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock">
					<xsl:text><![CDATA[
 * <p>
 * Representation of a node's field definition.
 * </p>
 * <p>
 * The field definition holds static field information such as the field
 * access type, data type and name of the field.
 * </p>
 * <p>
 * The implementation of the toString() method of this class shall return the
 * full IDL declaration of the field as per the specification, not the UTF8 or
 * XML format. Implementation of <code>.equals()</code> shall return true if
 * the two field definitions share the same access type, data type and name. It
 * shall not include the underlying field's values at that point in time.
 * </p>
 *
 * @author Justin Couch
]]></xsl:text>
					<xsl:value-of select="InterfaceDefinition/@appinfo"/>
				</xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[
	// Member value declarations are encapsulated and private, using preferred Java types for concretes library
										
	private String    name = "";
										
	private int accessType = X3DFieldTypes.INPUT_OUTPUT;
										
	private int  fieldType = X3DFieldTypes.SFSTRING;
					
    /**
     * Get the name of this field. This will be something like "children"
     * or "translation". If the field is an exposed field then the name
     * give will be the base name without any <i>set_</i> or <i>_changed</i>
     * added to the name, regardless of how the initial field was fetched.
     *
     * @return The name of this field
     */
	@Override
	public String getName()
	{
		return name;
	}
						
	public void setName(String newValue)
	{
		if (name.contains(" ")) // TODO other validity checks for name
		name = newValue;
	}
			
    /**
     * Get the access type of the field. This will be one of field,
     * exposedField, eventIn or eventOut constants described in the
     * X3DFieldTypes interface.
     *
     * @see X3DFieldTypes
     * @return The access type of this field
     */			
	@Override
	public int getAccessType()
	{
		return accessType;
	}
    /**
     * Set the access type of the field. This will be one of field,
     * exposedField, eventIn or eventOut constants described in the
     * X3DFieldTypes interface.
     *
     * @see X3DFieldTypes
     * @throws InvalidFieldValueException Illegal value provided, no change made
     * @param newValue The access type of this field
     */
	public void setAccessType(int newValue)
	{
		if ((newValue >= X3DFieldTypes.INPUT_ONLY) && (newValue <= X3DFieldTypes.OUTPUT_ONLY))
			accessType = newValue;
		else
		{
			String errorNotice = "Illegal value " + newValue + " for field type";
//			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
	}
					
    /**
     * Get the field type. This string represents the field type such as
     * MFNode, SFInt32. The definition of the returned int value is
     * described in the X3DFieldType interface.
     *
     * @return A constant describing the field type
     * @see X3DFieldTypes
     */	
	@Override
	public int getFieldType()
	{
		return fieldType;
	}

    /**
     * Set the field type of the field. This will be one of SFBool,
     * SFInt32, MFString (etc.) constants described in the
     * X3DFieldTypes interface.
     *
     * @see X3DFieldTypes
     * @throws InvalidFieldValueException Illegal value provided, no change made
     * @param newValue The access type of this field
     */
	public void setFieldType(int newValue)
	{
		if ((newValue >= X3DFieldTypes.SFBOOL) && (newValue <= X3DFieldTypes.MFMATRIX4D))
			accessType = newValue;
		else
		{
			String errorNotice = "Illegal value " + newValue + " for field type";
//			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		}
		fieldType = newValue;
	}

    /**
     * Get the field type. This string represents the field type such as
     * MFNode, SFInt32, etc. A string is used to allow full extensibility.
     *
     * @return A string describing the field type
     */	
	@Override
	public String getFieldTypeString()
	{
		return X3DConcreteFieldTypes.toFieldString(fieldType);
	}
]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
	
		<!-- ===================================================== -->

			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:text>X3DConcreteFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:text>fields</xsl:text></xsl:with-param>
				<xsl:with-param name="description"><xsl:text>Methods for constants corresponding to each X3D field type and accessType.</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.11 X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DFieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.2.15 SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIFieldType</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>5.3 Field types</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>fieldsDef.html#FieldTypes</xsl:text></xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[
		/**
		 * Convert accessType value to string
		 * @param accessType the accessType enumeration value to convert
		 * @return string name for accessType value */
		public static String toAccessTypeString (int accessType)
		{
			switch (accessType)
			{
				case INPUT_ONLY:
					return "inputOnly";
				case INITIALIZE_ONLY:
					return "initializeOnly";
				case INPUT_OUTPUT:
					return "inputOutput";
				case OUTPUT_ONLY:
					return "outputOnly";
				default:
					String message = "ERROR_UnknownTypeValue_" + accessType;
					System.err.println ("X3DFieldTypes.toString(" + accessType + ") " + message);
					return message; // TODO throw exception?
			}
		}
		/**
		 * Convert fieldType value to string
		 * @param fieldType the fieldType enumeration value to convert
		 * @return string name for fieldType value */
		public static String toFieldString (int fieldType)
		{
			switch (fieldType)
			{
				case SFBOOL:
					return "SFBool";
				case MFBOOL:
					return "MFBool";
				case SFINT32:
					return "SFInt32";
				case MFINT32:
					return "MFInt32";
				case SFFLOAT:
					return "SFFloat";
				case MFFLOAT:
					return "MFFloat";
				case SFDOUBLE:
					return "SFDouble";
				case MFDOUBLE:
					return "MFDouble";
				case SFTIME:
					return "SFTime";
				case MFTIME:
					return "MFTime";
				case SFNODE:
					return "SFNode";
				case MFNODE:
					return "MFNode";
				case SFVEC2F:
					return "SFVec2f";
				case MFVEC2F:
					return "MFVec2f";
				case SFVEC3F:
					return "SFVec3f";
				case MFVEC3F:
					return "MFVec3f";
				case SFVEC3D:
					return "SFVec3d";
				case MFVEC3D:
					return "MFVec3d";
				case SFROTATION:
					return "SFRotation";
				case MFROTATION:
					return "MFRotation";
				case SFCOLOR:
					return "SFColor";
				case MFCOLOR:
					return "MFColor";
				case SFCOLORRGBA:
					return "SFColorRGBA";
				case MFCOLORRGBA:
					return "MFColorRGBA";
				case SFIMAGE:
					return "SFImage";
				case MFIMAGE:
					return "MFImage";
				case SFSTRING:
					return "SFString";
				case MFSTRING:
					return "MFString";

				// added in v3.3
				case SFVEC2D:
					return "SFVec2d";
				case MFVEC2D:
					return "MFVec2d";
				case SFVEC4F:
					return "SFVec4f";
				case MFVEC4F:
					return "MFVec4f";
				case SFVEC4D:
					return "SFVec4d";
				case MFVEC4D:
					return "MFVec4d";
				case SFMATRIX3D:
					return "SFMatrix3d";
				case MFMATRIX3D:
					return "MFMatrix3d";
				case SFMATRIX3F:
					return "SFMatrix3f";
				case MFMATRIX3F:
					return "MFMatrix3f";
				case SFMATRIX4D:
					return "SFMatrix4d";
				case MFMATRIX4D:
					return "MFMatrix4d";
				case SFMATRIX4F:
					return "SFMatrix4f";
				case MFMATRIX4F:
					return "MFMatrix4f";
				default:
					String message = "ERROR_UnknownTypeValue_" + fieldType;
					System.err.println ("X3DFieldTypes.toString(" + fieldType + ") " + message);
					return message; // TODO throw exception?
			}
		}
	]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>

    </xsl:template> <!-- FieldDefinitions -->
	
    <!-- ===================================================== -->
	
	<xsl:template name="BaseTypeDefinitions">
		
		<xsl:variable name="subPackage">
			<xsl:if test="($modifySpecificationInterfaces = 'true')">
				<xsl:text>fields</xsl:text>
			</xsl:if>
		</xsl:variable>
		
		<!-- B.4 Field interfaces -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#FieldInterfaces -->
		<!-- TODO specificaton table bookmark link is incorrect -->
		<!-- Implemented in X3D Object model -->
		
		<!-- TODO get enumeration values and create final int constant values -->
		
		<xsl:for-each select="//FieldTypes/FieldType">
			
			<xsl:variable name="name"                                select="@type"/>
			<xsl:variable name="description"                         select="InterfaceDefinition/@appinfo"/>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			
			<xsl:variable name="extends">
				<!-- must have one; also note that each interface can be extended by another interface -->
				<xsl:choose>
					<xsl:when test="contains($name,'Matrix3')">
						<xsl:text>Matrix3</xsl:text>
					</xsl:when>
					<xsl:when test="contains($name,'Matrix4')">
						<xsl:text>Matrix4</xsl:text>
					</xsl:when>
					<xsl:when test="starts-with($name,'SF')">
						<xsl:text>X3DField</xsl:text>
					</xsl:when>
					<xsl:otherwise> <!-- MF -->
						<xsl:text>MField</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			
			<xsl:variable name="imports">
				<xsl:choose>
					<xsl:when test="($name = 'MFImage')">
						<xsl:text>
import java.awt.image.RenderedImage;
import java.awt.image.WritableRenderedImage;</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode') or ($name = 'MFNode')">
						<xsl:text>
import org.web3d.x3d.sai.Core.X3DNode;</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			
			<!-- TODO turn into template for reuse -->
			<xsl:variable name="saiJavaSpecificationSection">
				<xsl:choose>
					<xsl:when test="($name = 'SFBool')">
						<xsl:text>B.4.7</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFBool')">
						<xsl:text>B.4.8</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColor')">
						<xsl:text>B.4.9</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFColor')">
						<xsl:text>B.4.10</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColorRGBA')">
						<xsl:text>B.4.11</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFColorRGBA')">
						<xsl:text>B.4.12</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFDouble')">
						<xsl:text>B.4.13</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFDouble')">
						<xsl:text>B.4.14</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFFloat')">
						<xsl:text>B.4.15</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFFloat')">
						<xsl:text>B.4.16</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFImage')">
						<xsl:text>B.4.17</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFImage')">
						<xsl:text>B.4.18</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFInt32')">
						<xsl:text>B.4.19</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFInt32')">
						<xsl:text>B.4.20</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3d')">
						<xsl:text>B.4.21</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix3d')">
						<xsl:text>B.4.22</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3f')">
						<xsl:text>B.4.23</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix3f')">
						<xsl:text>B.4.24</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4d')">
						<xsl:text>B.4.25</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix4d')">
						<xsl:text>B.4.26</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4f')">
						<xsl:text>B.4.27</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix4f')">
						<xsl:text>B.4.28</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode')">
						<xsl:text>B.4.29</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFNode')">
						<xsl:text>B.4.30</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFRotation')">
						<xsl:text>B.4.31</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFRotation')">
						<xsl:text>B.4.32</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFString')">
						<xsl:text>B.4.33</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFString')">
						<xsl:text>B.4.34</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFTime')">
						<xsl:text>B.4.35</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFTime')">
						<xsl:text>B.4.36</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2d')">
						<xsl:text>B.4.37</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2d')">
						<xsl:text>B.4.38</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2f')">
						<xsl:text>B.4.39</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2f')">
						<xsl:text>B.4.40</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec3d')">
						<xsl:text>B.4.41</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec3d')">
						<xsl:text>B.4.42</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec3f')">
						<xsl:text>B.4.43</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec3f')">
						<xsl:text>B.4.44</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec4d')">
						<xsl:text>B.4.45</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec4d')">
						<xsl:text>B.4.46</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec4f')">
						<xsl:text>B.4.47</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec4f')">
						<xsl:text>B.4.48</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			
			<!-- TODO turn into template for reuse -->
			<xsl:variable name="saiAbstractSpecificationSection">
				<xsl:choose>
					<xsl:when test="($name = 'SFBool') or ($name = 'MFBool')">
						<xsl:text>5.2.2 SAIBoolean</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFString') or ($name = 'MFString')">
						<xsl:text>SAIString</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode') or ($name = 'MFNode')">
						<xsl:text>5.2.22 SAINode</xsl:text>
					</xsl:when>
					<xsl:when test="contains($name, 'Matrix')">
						<xsl:text>5.2.20 SAIMatrix</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>5.2.15 SAIFieldType</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			
			<!-- TODO turn into template for reuse -->
			<xsl:variable name="saiAbstractSpecificationRelativeUrl">
				<xsl:choose>
					<xsl:when test="($name = 'SFBool') or ($name = 'MFBool')">
						<xsl:text>dataRef.html#SAIBoolean</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFString') or ($name = 'MFString')">
						<xsl:text>dataRef.html#SAIString</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode') or ($name = 'MFNode')">
						<xsl:text>dataRef.html#SAINode</xsl:text>
					</xsl:when>
					<xsl:when test="contains($name, 'Matrix')">
						<xsl:text>dataRef.html#SAIMatrix</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>dataRef.html#SAIFieldType</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>
			
			<!-- TODO turn into template for reuse -->
			<xsl:variable name="x3dAbstractSpecificationSection">
				<xsl:choose>
					<xsl:when test="($name = 'SFBool')">
						<xsl:text>5.3.1 SFBool and MFBool</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFBool')">
						<xsl:text>5.3.1 SFBool and MFBool</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColor')">
						<xsl:text>5.3.2 SFColor and MFColor</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFColor')">
						<xsl:text>5.3.2 SFColor and MFColor</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColorRGBA')">
						<xsl:text>5.3.3 SFColorRGBA and MFColorRGBA</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFColorRGBA')">
						<xsl:text>5.3.3 SFColorRGBA and MFColorRGBA</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFDouble')">
						<xsl:text>5.3.4 SFDouble and MFDouble</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFDouble')">
						<xsl:text>5.3.4 SFDouble and MFDouble</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFFloat')">
						<xsl:text>5.3.5 SFFloat and MFFloat</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFFloat')">
						<xsl:text>5.3.5 SFFloat and MFFloat</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFImage')">
						<xsl:text>5.3.6 SFImage and MFImage</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFImage')">
						<xsl:text>5.3.6 SFImage and MFImage</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFInt32')">
						<xsl:text>5.3.7 SFInt32 and MFInt32</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFInt32')">
						<xsl:text>5.3.7 SFInt32 and MFInt32</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3d')">
						<xsl:text>5.3.8 SFMatrix3d and MFMatrix3d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix3d')">
						<xsl:text>5.3.8 SFMatrix3d and MFMatrix3d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3f')">
						<xsl:text>5.3.9 SFMatrix3f and MFMatrix3f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix3f')">
						<xsl:text>5.3.9 SFMatrix3f and MFMatrix3f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4d')">
						<xsl:text>5.3.10 SFMatrix4d and MFMatrix4d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix4d')">
						<xsl:text>5.3.10 SFMatrix4d and MFMatrix4d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4f')">
						<xsl:text>5.3.11 SFMatrix4f and MFMatrix4f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFMatrix4f')">
						<xsl:text>5.3.11 SFMatrix4f and MFMatrix4f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode')">
						<xsl:text>5.3.12 SFNode and MFNode</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFNode')">
						<xsl:text>5.3.12 SFNode and MFNode</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFRotation')">
						<xsl:text>5.3.13 SFRotation and MFRotation</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFRotation')">
						<xsl:text>5.3.13 SFRotation and MFRotation</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFString')">
						<xsl:text>5.3.14 SFString and MFString</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFString')">
						<xsl:text>5.3.14 SFString and MFString</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFTime')">
						<xsl:text>5.3.15 SFTime and MFTime</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFTime')">
						<xsl:text>5.3.15 SFTime and MFTime</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2d')">
						<xsl:text>5.3.16 SFVec2d and MFVec2d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2d')">
						<xsl:text>5.3.16 SFVec2d and MFVec2d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2f')">
						<xsl:text>5.3.17 SFVec2f and MFVec2f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2f')">
						<xsl:text>5.3.17 SFVec2f and MFVec2f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec3d')">
						<xsl:text>5.3.18 SFVec3d and MFVec3d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec3d')">
						<xsl:text>5.3.18 SFVec3d and MFVec3d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec3f')">
						<xsl:text>5.3.19 SFVec3f and MFVec3f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec3f')">
						<xsl:text>5.3.19 SFVec3f and MFVec3f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec4d')">
						<xsl:text>5.3.20 SFVec4d and MFVec4d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec4d')">
						<xsl:text>5.3.20 SFVec4d and MFVec4d</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec4f')">
						<xsl:text>5.3.21 SFVec4f and MFVec4f</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec4f')">
						<xsl:text>5.3.21 SFVec4f and MFVec4f</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			
			<xsl:variable name="javadocBlock">
			</xsl:variable>
			<!-- debug
			<xsl:message>
				<xsl:text>*** //FieldTypes/FieldType name=</xsl:text>
				<xsl:value-of select="$name"/>
				<xsl:text>, $javadocBlock=</xsl:text>
				<xsl:value-of select="$javadocBlock"/>
			</xsl:message> -->
			
			<xsl:variable name="interfaceBlock">
				<xsl:choose>
					<xsl:when test="($name = 'SFBool')">
						<xsl:text><![CDATA[
    /**
     *	Get the current value.
     * 	@return current value
     */	
	public boolean getValue();

    /**
     * Assign a new value to this field.
     * @param newValue The newValue to assign
     */	
	public void setValue(boolean newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFBool')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(boolean[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @return The selected value
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public boolean get1Value(int index);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, boolean[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to insert
     */
	public void set1Value(int index, boolean newValue) throws ArrayIndexOutOfBoundsException;

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(boolean newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, boolean newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColor')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param newValue The newValue to set
     */	
	public void setValue(float[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="starts-with($name,'MFColor')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[][] valueDestination);

    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @param valueDestination The array to be filled in with the selected current field value.
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public void get1Value(int index, float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param numColors The number of 3-tuple RGB colors in the newValue array
     * @param newValue The newValue to set
     */	
	public void setValue(int numColors, float[] newValue);

    /**
     * Assign a new value to this field.
     * @param numColors The number of 3-tuple RGB colors in the newValue array
     * @param newValue The newValue to set
     */	
	public void setValue(int numColors, float[][] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, float[] newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(float[] newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, float[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFColorRGBA')">
						<xsl:text>
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param newValue The newValue to set
     */	
	public void setValue(float[] newValue);
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFColorRGBA')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[][] valueDestination);

    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @param valueDestination The array to be filled in with the selected current field value.
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public void get1Value(int index, float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param numColors The number of 3-tuple RGB colors in the newValue array
     * @param newValue The new value to set
     */	
	public void setValue(int numColors, float[] newValue);

    /**
     * Assign a new value to this field.
     * @param numColors The number of 3-tuple RGB colors in the newValue array
     * @param newValue The new value to set
     */	
	public void setValue(int numColors, float[][] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, float[] newValue);

    /** 
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(float[] newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, float[] newValue);
]]>
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFDouble')">
						<xsl:text>
    /**
     *	Get the current value.
     * 	@return current value
     */	
	public double getValue();

    /**
     * Assign a new value to this field.
     * @param newValue The new value to set
     */	
	public void setValue(double newValue);
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFDouble')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(double[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @return The selected value
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public double get1Value(int index) throws ArrayIndexOutOfBoundsException;

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, double[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, double newValue) throws ArrayIndexOutOfBoundsException;

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(double newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, double newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFFloat')">
						<xsl:text><![CDATA[
    /**
     *	Get the current value.
     * 	@return current value
     */	
	public float getValue();

    /**
     * Assign a new value to this field.
     * @param newValue The new value to set
     */	
	public void setValue(float newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFFloat')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @return The selected value
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public float get1Value(int index) throws ArrayIndexOutOfBoundsException;

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, float[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, float newValue) throws ArrayIndexOutOfBoundsException;

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(float newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, float newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFImage')">
						<xsl:text><![CDATA[
    /**
     * Get the width of the image.
     * @return The width of the image in pixels
     */
	public int getWidth();

    /**
     * Get the height of the image.
     * @return The height of the image in pixels
     */
	public int getHeight();

    /**
     * Get the number of color components in the image. The value will
     * always be between 1 and 4 indicating the number of components of
     * the color specification to be read from the image pixel data.
     * @return The number of components
     */
	public int getComponents();

    /**
     * Get the image pixel value in the given eventOut.
     * <p>
     * The number of items in the pixels array will be
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     * @param pixels The array to copy pixel values into
     */
	public void getPixels(int[] pixels);

    /**
     * Fetch the Java representation of the underlying image from these pixels.
     * This is the same copy that the browser uses to generate texture
     * information from.
     * @return The image reference representing the current state
     */
	public java.awt.image.WritableRenderedImage getImage();

    /**
     * Set the image value in the given writable field to the new image defined
     * by a set of pixels.
     * <p>
     * @param image The new image to use as the source
     */
	public void setImage(java.awt.image.RenderedImage image);

    /**
	 * Copy a region of the argument RenderedImage to replace a portion of the
	 * current SFimage.
	 * <p>
	 * The sub image set shall not resize the base image representation and
	 * therefore performs an intersection clip of the provided image. The user
	 * provided image shall be of the same format (pixel depth, pixel
	 * representation) as the original image obtained through the getImage()
	 * method.
	 * <p>
	 * RenderedImages are row order from top to bottom. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 0 |********|
	 * 1 |********|
	 * 2 |********|
	 * 3 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * SFImages are row order from bottom to top. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 3 |********|
	 * 2 |********|
	 * 1 |********|
	 * 0 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * <p>
	 * Note: The parameter srcYOffset is referenced to the RenderedImage object
	 * (indexed top to bottom).
	 * <br>
	 * The parameter destYOffset is referenced to the SFImage object
	 * (indexed bottom to top).
	 *
	 * @param image The new image to use as the source
	 * @param sourceWidth The width of the argument sub-image region to copy
	 * @param sourceHeight The height of the argument sub-image region to copy
	 * @param sourceXOffset The initial x dimension (width) offset into the
	 * argument sub-image that begins the region to copy
	 * @param sourceYOffset The initial y dimension (height) offset into the
	 * argument sub-image that begins the region to copy
	 * @param destinationXOffset The initial x dimension (width) offset in the SFimage
	 * object that begins the region to receive the copy
	 * @param destinationYOffset The initial y dimension (height) offset in the SFimage
	 * object that begins the region to receive the copy
	 */
	public void setSubImage(java.awt.image.RenderedImage image,
                            int sourceWidth,
                            int sourceHeight,
                            int sourceXOffset,
                            int sourceYOffset,
                            int destinationXOffset,
                            int destinationYOffset);

    /**
     * Set the image value in the given writable field.
     * <p>
     * Image values are specified using a width, height and the number of
     * components. The number of items in the pixels array must be at least
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components. If the integer
     * contains values in bytes that are not used by the number of components
     * for that image, the values are ignored.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     *
     * @param width The width of the image in pixels
     * @param height The height of the image in pixels
     * @param components The number of color components [1-4]
     * @param pixels The array of pixel values as specified above.
     * @exception IllegalArgumentException The number of components or width/
     *    height are illegal values.
     * @exception ArrayIndexOutOfBoundsException The number of pixels provided by the
     *    caller is not enough for the width * height.
     */
	public void setValue(int width,
                         int height,
                         int components,
                         int[] pixels);

]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFImage')">
						<xsl:text><![CDATA[
    /**
     * Get the width of the image array.
     * @param imageIndex the index of the selected image
     * @return The width of the image in pixels
     */
	public int getWidth(int imageIndex);

    /**
     * Get the height of the image array.
     * @param imageIndex the index of the selected image
     * @return The height of the image in pixels
     */
	public int getHeight(int imageIndex);

    /**
     * Get the number of color components in the image. The value will
     * always be between 1 and 4 indicating the number of components of
     * the color specification to be read from the image pixel data.
     * @param imageIndex the index of the selected image
     * @return The number of components
     */
	public int getComponents(int imageIndex);

    /**
     * Get the image pixel value in the given eventOut.
     * <p>
     * The number of items in the pixels array will be
     * <code>width * height</code>. If there are less items than this an
     * ArrayIndexOutOfBoundsException will be generated. The integer values
     * are represented according to the number of components.
     * <p>
     *  <b>1 Component Images </b> <br>
     * The integer has the intensity value stored in the lowest byte and can be
     * obtained:
     *  <pre>
     *    intensity = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>2 Component Images </b> <br>
     * The integer has the transparency value stored in the lowest byte and the
     * intensity in the next byte:
     *  <pre>
     *    intensity = (pixel[i] &gt;&gt; 8) &amp;0xFF;
     *    alpha     = (pixel[i]     ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>3 Component Images </b> <br>
     * The three color components are stored in the integer array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    blue  = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     *  <b>4 Component Images </b> <br>
     * The integer has the value stored in the array as follows:
     *  <pre>
     *    red   = (pixel[i] &gt;&gt; 24) &amp;0xFF;
     *    green = (pixel[i] &gt;&gt; 16) &amp;0xFF;
     *    blue  = (pixel[i] &gt;&gt;  8) &amp;0xFF;
     *    alpha = (pixel[i]      ) &amp;0xFF;
     *  </pre>
     * <p>
     * The width and height values must be greater than or equal to zero. The
     * number of components is between 1 and 4. Any value outside of these
     * bounds will generate an IllegalArgumentException.
     * @param imageIndex the index of the selected image
     * @param pixels The array to copy pixel values into
     */
	public void getPixels(int imageIndex, int[] pixels);

    /**
     * Fetch the Java representation of the underlying image from these pixels.
     * This is the same copy that the browser uses to generate texture
     * information from.
     * @param imageIndex the index of the selected image
     * @return The image reference representing the current state
     */
	public WritableRenderedImage getImage(int imageIndex);

    /**
     * Set the image value in the given writable field to the new image defined
     * by a set of pixels.
     * @param imageIndex the index of the selected image
     * @param image The new image to use as the source
     */
	public void setImage(int imageIndex, RenderedImage image);

    /**
	 * Copy a region of the argument RenderedImage to replace a portion of the
	 * current SFimage.
	 * <p>
	 * The sub image set shall not resize the base image representation and
	 * therefore performs an intersection clip of the provided image. The user
	 * provided image shall be of the same format (pixel depth, pixel
	 * representation) as the original image obtained through the getImage()
	 * method.
	 * <p>
	 * RenderedImages are row order from top to bottom. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 0 |********|
	 * 1 |********|
	 * 2 |********|
	 * 3 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * SFImages are row order from bottom to top. A
	 * 4x8 RenderImage is indexed as follows:
	 *
	 *  <pre>
	 *
	 * X &gt;01234567
	 *   ----------
	 * 3 |********|
	 * 2 |********|
	 * 1 |********|
	 * 0 |********|
	 * ^ ----------
	 * Y
	 *
	 *  </pre>
	 *
	 * <p>
	 * Note: The parameter srcYOffset is referenced to the RenderedImage object
	 * (indexed top to bottom).
	 * <br>
	 * The parameter destYOffset is referenced to the SFImage object
	 * (indexed bottom to top).
	 *
	 * @param imageIndex the index of the selected image
	 * @param image The new image to use as the source
	 * @param sourceWidth The width of the argument sub-image region to copy
	 * @param sourceHeight The height of the argument sub-image region to copy
	 * @param sourceXOffset The initial x dimension (width) offset into the
	 * argument sub-image that begins the region to copy
	 * @param sourceYOffset The initial y dimension (height) offset into the
	 * argument sub-image that begins the region to copy
	 * @param destinationXOffset The initial x dimension (width) offset in the SFimage
	 * object that begins the region to receive the copy
	 * @param destinationYOffset The initial y dimension (height) offset in the SFimage
	 * object that begins the region to receive the copy
	 */
	public void setSubImage(int imageIndex,
		RenderedImage image,
                            int sourceWidth,
                            int sourceHeight,
                            int sourceXOffset,
                            int sourceYOffset,
                            int destinationXOffset,
                            int destinationYOffset);

	/**
	 * Replaces a single value at the appropriate location in the existing value array.
	 * @param imageIndex the index of the selected image
	 * @param newValue The newValue to set
	 */
	public void set1Value(int imageIndex, int newValue);

	public void set1Value(int imageIndex,
                          int width,
                          int height,
                          int components,
                          int[] pixels);

	/**
	 * Assign a new value array containing imageIndex, width, height, and components count, followed by array of pixels.
	 * @param newValue The newValue to set
	 */	
	public void setValue(int[] newValue);

	public void setImage(RenderedImage[] image);

	/**
	 * Places a new value at the end of the existing value array, increasing the field length accordingly.
	 * @param newValue The newValue to append
	 */
	public void append(RenderedImage[] newValue);

	/**
	 * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
	 * @param index The position for the inserted value in the current array
	 * @param newValue The newValue to insert
	 */
	public void insertValue(int index, RenderedImage newValue);
]]></xsl:text>
<!-- TODO specification missing closing } -->
					</xsl:when>
					<xsl:when test="($name = 'SFInt32')">
						<xsl:text><![CDATA[
	/**
	 *	Get the current value.
	 * 	@return current value
	 */	
	public int getValue();

	/**
	 * Assign a new value to this field.
	 * @param newValue The new value to set
	 */	
	public void setValue(int newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFInt32')">
						<xsl:text><![CDATA[
	/**
	 * Write the current value of the field out to the provided valueDestination array.
	 *
	 * @param valueDestination The array to be filled in with current field values.
	 * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
	 */
	public void getValue(int[] valueDestination);

	/**
	 * <p>
	 * Get an individual value from this field array.
	 * </p><p>
	 * If the index is outside the bounds of the current array of data values,
	 * an ArrayIndexOutOfBoundsException is thrown.
	 * </p>
	 * @param index The position of the selected value in the current array
	 * @return The selected value
	 * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
	 */
	public int get1Value(int index) throws ArrayIndexOutOfBoundsException;

	/**
	 * Assign a new value to this field.
	 * @param size indicates size of result to apply to newValue array.
	 * @param newValue The replacement value array to assign.
	 */	
	public void setValue(int size, int[] newValue);

	/**
	 * Replaces a single value at the appropriate location in the existing value array.
	 * @param imageIndex the index of the selected image
	 * @param newValue The newValue to set
	 */
	public void set1Value(int imageIndex, int newValue) throws ArrayIndexOutOfBoundsException;

	/**
	 * Places a new value at the end of the existing value array, increasing the field length accordingly.
	 * @param newValue The newValue to append
	 */
	public void append(int newValue);

	/**
	 * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
	 * @param index The position for the inserted value in the current array
	 * @param newValue The newValue to insert
	 */
	public void insertValue(int index, int newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3d') or ($name = 'MFMatrix3d')">
						<xsl:text>
	public void setTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale,
		SFRotation scaleOrientation,
		SFVec3d center);

	public void getTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale);
							
	public Matrix3 multiplyRowVector(SFVec3d vec3d);

	public Matrix3 multiplyColVector(SFVec3d vec3d);
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix3f') or ($name = 'MFMatrix3f')">
						<xsl:text>
	public void setTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale,
		SFRotation scaleOrientation,
		SFVec3f center);

	public void getTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale);

	public Matrix3 multiplyRowVector(SFVec3f vec3f);

	public Matrix3 multiplyColVector(SFVec3f vec3f);
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4d') or ($name = 'MFMatrix4d')">
						<xsl:text>
	public void setTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale,
		SFRotation scaleOrientation,
		SFVec3d center);

	public void getTransform(SFVec3d translation,
		SFRotation rotation,
		SFVec3d scale);

	public Matrix4 multiplyRowVector(SFVec3d vec3d); // TODO SFVec4d ?

	public Matrix4 multiplyColVector(SFVec3d vec3d); // TODO SFVec4d ?
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFMatrix4f') or ($name = 'MFMatrix4f')">
						<xsl:text>
	public void setTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale,
		SFRotation scaleOrientation,
		SFVec3f center);

	public void getTransform(SFVec3f translation,
		SFRotation rotation,
		SFVec3f scale);

	public Matrix4 multiplyRowVector(SFVec3f vec3f); // TODO SFVec4f ?

	public Matrix4 multiplyColVector(SFVec3f vec3f); // TODO SFVec4f ?
</xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFNode')">
						<xsl:text><![CDATA[
	/**
	 *	Get the current value.
	 * 	@return current value
	 */	
	public X3DNode getValue();

	/**
	 * Assign a new value to this field.
	 * @param newValue The new value to set
	 */	
	public void setValue(X3DNode newValue) throws InvalidNodeException;
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFNode')">
						<xsl:text><![CDATA[
	/**
	 * Write the current value of the field out to the provided copiedNodes array.
	 *
	 * @param copiedNodes The array to be filled in with current field values.
	 * @throws ArrayIndexOutOfBoundsException The provided copiedNodes array was too small
	 */
	public void getValue(X3DNode[] copiedNodes);

	/**
	 * <p>
	 * Get an individual value from this field array.
	 * </p>
	 * <p>
	 * If the index is outside the bounds of the current array of data values,
	 * an ArrayIndexOutOfBoundsException is thrown.
	 * </p>
	 * @param index The position of the selected value in the current array
	 * @return The selected value
	 * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
	 */
	public X3DNode get1Value(int index);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, X3DNode[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param imageIndex the index of the selected image
     * @param newValue The newValue to set
     */
	public void set1Value(int imageIndex, X3DNode newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(X3DNode newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param imageIndex the index of the selected image
     * @param newValue The newValue to insert
     */
	public void insertValue(int imageIndex, X3DNode newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFRotation')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(float[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFRotation')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[][] valueDestination);

    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @param valueDestination The array to be filled in with the selected current field value.
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public void get1Value(int index, float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param numRotations The number of 4-tuple rotations in the newValue array
     * @param newValue The newValue array of 4-tuple rotations to set
     */	
	public void setValue(int numRotations, float[] newValue);

    /**
     * Assign a new value to this field.
     * @param numRotations The number of 4-tuple rotations in the newValue array
     * @param newValue The newValue square array of 4-tuple rotations to set
     */	
	public void setValue(int numRotations, float[][] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, float[] newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(float[] newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, float[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFString')">
						<xsl:text><![CDATA[
    /**
     *	Get the current value.
     * 	@return current value
     */	
	public String getValue();

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(String newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFString')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(String[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @return The selected value
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public String get1Value(int index);

    /**
     * Assign a new value to this field.
     * @param numStrings The number of strings in the newValue array
     * @param newValue The newValue array of strings to set
     */	
	public void setValue(int numStrings, String[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, String newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(String newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, String newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFTime')">
						<xsl:text><![CDATA[
    /**
     *	Get the current value.
     * 	@return current value
     */	
	public double getValue();

	public long getJavaValue();

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(double newValue);

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(long newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFTime')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(double[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
	 * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @return The selected value
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public double get1Value(int index);

	public long get1JavaValue(int index);

    /**
     * Assign a new value
     * @param size indicates size of result to apply to newValue array
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, double[] newValue);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, long[] newValue);

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(long[] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, double newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, long newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(double newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(long newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, long newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, double newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2d') or ($name = 'SFVec3d') or ($name = 'SFVec4d')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(double[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(double[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2d') or ($name = 'MFVec3d') or ($name = 'MFVec4d')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(double[][] valueDestination);

    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(double[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @param valueDestination The array to be filled in with the selected current field value.
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public void get1Value(int index, double[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, double[] newValue);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, double[][] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, double[] newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(double[] newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, double[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'SFVec2f') or ($name = 'SFVec3f') or ($name = 'SFVec4f')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(float[] newValue);
]]></xsl:text>
					</xsl:when>
					<xsl:when test="($name = 'MFVec2f') or ($name = 'MFVec3f') or ($name = 'MFVec4f')">
						<xsl:text><![CDATA[
    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[][] valueDestination);

    /**
     * Write the current value of the field out to the provided valueDestination array.
     *
     * @param valueDestination The array to be filled in with current field values.
     * @throws ArrayIndexOutOfBoundsException The provided valueDestination array was too small.
     */
	public void getValue(float[] valueDestination);

    /**
     * <p>
     * Get an individual value from this field array.
     * </p><p>
     * If the index is outside the bounds of the current array of data values,
     * an ArrayIndexOutOfBoundsException is thrown.
     * </p>
     * @param index The position of the selected value in the current array
     * @param valueDestination The array to be filled in with the selected current field value.
     * @throws ArrayIndexOutOfBoundsException The index was outside of the bounds of the current array.
     */
	public void get1Value(int index, float[] valueDestination);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, float[] newValue);

    /**
     * Assign a new value to this field.
     * @param size indicates size of result to apply to newValue array.
     * @param newValue The replacement value array to assign.
     */	
	public void setValue(int size, float[][] newValue);

    /**
     * Replaces a single value at the appropriate location in the existing value array.
     * @param index The position of the selected value in the current array
     * @param newValue The newValue to set
     */
	public void set1Value(int index, float[] newValue);

    /**
     * Places a new value at the end of the existing value array, increasing the field length accordingly.
     * @param newValue The newValue to append
     */
	public void append(float[] newValue);

    /**
     * Insert a new value at the appropriate location in the existing value array, increasing the field length accordingly.
     * @param index The position for the inserted value in the current array
     * @param newValue The newValue to insert
     */
	public void insertValue(int index, float[] newValue);
]]></xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			
			<!-- TODO javadoc url links -->
		
			<!-- B.4 Field interfaces -->
			<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#FieldInterfaces -->

			<!-- abstract interfaces -->
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:value-of select="$imports"/></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
				<!-- update specification prose to include full package -->
				<xsl:with-param name="extends"><xsl:value-of select="$extends"/></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:value-of select="$saiJavaSpecificationSection"/></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:value-of select="$saiAbstractSpecificationSection"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:value-of select="$saiAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="$x3dAbstractSpecificationSection"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock"><xsl:value-of select="$interfaceBlock"/></xsl:with-param>
			</xsl:call-template>
		
		</xsl:for-each>
		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="ServiceInterfaces">
		
		<xsl:variable name="subPackage">
			<xsl:if test="($modifySpecificationInterfaces = 'true')">
				<xsl:text>services</xsl:text>
			</xsl:if>
		</xsl:variable>
		
		<!-- B.5 Service interfaces -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#ServiceInterfaces -->
		<!-- TODO fix specification designations: some of these service definitions are interfaces, not classes -->
			
		<!-- Note:  BrowserEvent must be a class since it extends java.util.EventObject -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>BrowserEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<!-- update specification prose to include full package -->
			<xsl:with-param name="extends"><xsl:text>java.util.EventObject</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Class representing events that happen in the Browser object.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.1 BrowserEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>5.4.1.2 SAI_Browser_Event</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>dataRef.html#SAIBrowserEvent</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implementationBlock"><![CDATA[
    /**
     * The X3D player has completed initial loading of the world. Event is generated
     * just after the scene has been loaded and just before the first event has been sent.
     */
	public static final int INITIALIZED = 0;

    /**
     * The currently loaded world is about to be unloaded. Called just before
     * the scene is about to be unloaded. If another world is going to replace this,
     * then an initialize event will be generated following this one.
     */
	public static final int SHUTDOWN = 1;

    /**
     * An error occurred in loading a scene from a URL call. Origin can be either
     * a createVrmlFromURL call or loadURL.
     */
	public static final int URL_ERROR = 2;

    /**
     * An error has occurred that has caused the connection between the X3D player
     * and the external application to fail. Potential causes include X3D player
     * failure or a lost network connection.
     */
	public static final int CONNECTION_ERROR = 10;

    /**
     * The number of reserved identifier numbers for event conditions. Any
     * value below this is considered to be a general specification-defined event as
     * found in the Java Scene Authoring Interface (SAI) specification. Any values
     * above this value are browser-specific messages.
     */
	public static final int LAST_IDENTIFIER = 100;
		
    /** The identifier of the event that this class instance represents */
    private int id;

    /**
     * Get the type of event that has occurred.
     *
     * @return The type of event as defined by the types
     * @see #INITIALIZED
     * @see #SHUTDOWN
     * @see #URL_ERROR
     * @see #CONNECTION_ERROR
     * @see #LAST_IDENTIFIER
     */
	public int getID()
    {
        return id;
	}

    /**
     * Create a new browser event.
     *
     * @param browser The source of the browser that generated this event
     * @param action The event type to create
     * @exception IllegalArgumentException if the action or browser id are not legal values
     */
	public BrowserEvent(Object browser, int action)
    {
        super(browser);

        if (browser == null)
		{
			String errorNotice = "Null browser reference";
//			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}

        if (action < 0)
		{
            String errorNotice = "Invalid event action type " + action;
//			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}

        id = action;
    }
				
    /**
     * Utility method providing the name of this event value.
     * @param value The BrowserEvent value of interest.
     * @return The name of this BrowserEvent value.
     */
	public String toString (int value)
	{
		switch (value)
		{
			case INITIALIZED:
				return "INITIALIZED";
			case SHUTDOWN:
				return "SHUTDOWN";
			case URL_ERROR:
				return "URL_ERROR";
			case CONNECTION_ERROR:
				return "CONNECTION_ERROR";
			case LAST_IDENTIFIER:
				return "LAST_IDENTIFIER";
			default:
				String message = "ERROR_UnknownBrowserEventValue_" + value;
				System.err.println ("BrowserEvent.toString(" + value + ") " + message);
				return message;
		}
	}
]]></xsl:with-param>
		</xsl:call-template>
		
		<!-- =========== -->

		<!-- TODO specification may need to define BrowserFactoryImpl X3DComponent and ExternalBrowser -->

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="imports">
import java.applet.Applet;
import java.io.InputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.security.AccessController;
import java.security.PrivilegedAction;
import java.util.Properties;
import java.util.Map;
</xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Factory class for obtaining references to browser instances.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.2 BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
<p>
An implementation-independent representation of the class used to access
and create browsers. The model follows that used by java.net.Socket. A
setImpl method is provided for browser writers to provide the internal
implementations of the browser.
</p>
<p>
An alternative way of doing this is through properties. The class,
when it loads first looks for a System property with the key:
</p>
<ul>
<li><code>x3d.sai.factory.class</code></li>
</ul>
<p>
If a non-null value is found for this key, it is used as the name of
the class to load as the default browser implementation. If no matching
System property is found, the initializer looks for the file
<code>x3d.properties</code> in the class path.
(For more information on how this works read
<code>java.lang.ClassLoader.getSystemResourceAsStream()</code>). If found,
and the file contains a non-null value for the <code>x3d.sai.factory.class</code>
key, this value is used as the name of the class to load as the default browser
implementation.
</p>
<p>
In either case (System properties or x3d.properties file), this name must
represent the full package qualified name of the class.
If a System property with the required key does not exist, or an x3d.properties
file does not exist or the x3d.properties file does not contain a property with
the required key for the name of the factory class, then
the default class name <code>org.web3d.x3d.sai.DefaultBrowserImpl</code> is assigned.
</p>
<p>
The class is loaded when a call is made to <code>getBrowser()</code> or
<code>createX3DComponent()</code> using the following method:
</p>

 <pre>
 Class factory_class = Class.forName(factory_class_name);
 factory = (BrowserFactoryImpl)factory_class.newInstance();
 </pre>

<p>
If a class cast exception is raised at the end, then an error is printed
but nothing is done about it. The result would be NullPointerExceptions
later in the code. Also, this may cause some security errors in some
web browsers.
</p>
<p>
To provide a custom implementation of the factory (which all
implementations must do) the user has the choice of the above options
of either setting a System property, making sure that an x3d.properties
file appears in the classpath <xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>before<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text> the sample implementation
that comes with the classes from the X3DC, or by calling setImpl. If
<code>setBrowserFactoryImpl</code> has not been called at the time that
any of the other methods have been, then the class will attempt to load
the implementation defined in the properties file. Attempting to call the
set implementation method after this point shall result in a X3DException
being generated. Otherwise, it shall use the set implementation.
</p>
@author Justin Couch</xsl:with-param>
			<xsl:with-param name="implementationBlock"><xsl:text><![CDATA[
    /** The name of the properties file to read things from */
    private static final String PROPERTIES_FILE_NAME = "x3d.properties";

    /** The name of all the properties that are used by this class */
    private static final String FACTORY_CLASS = "x3d.sai.factory.class";

    /** Properties file location that is Xj3D-specific */
    private static final String XJ3D_PROPERTIES_FILE =
        "config/3.0/spec/" + PROPERTIES_FILE_NAME;

    /** The default values of any properties */
    private static final String DEFAULT_FACTORY_CLASS =
        "org.web3d.x3d.sai.DefaultBrowserImpl";

    /** Null browser factory implementation error message */
    private static final String NULL_BROWSER_FACTORY_IMPL_ERR_MSG =
        "Provided factory is null";

    /** Factory has already been defined error message */
    private static final String FACTORY_ALREADY_DEFINED_ERR_MSG =
        "Factory already defined";

    /** Factory class not found error message */
    private static final String FACTORY_CLASS_NOT_FOUND_ERR_MSG =
        "Unable to find X3D player factory implementation\n";

    /** Unable to instantiate factory error message */
    private static final String UNABLE_TO_INSTANTIATE_FACTORY_ERR_MSG =
        "Error instantiating the X3D player factory\n";

    /** Class not a BrowserFactoryImpl error message */
    private static final String CLASS_NOT_A_BROWSER_FACTORY_IMPL_ERR_MSG =
        "The nominated browser factory is not an instance of ";

    /** BrowserFactoryImpl interface class name */
    private static final String BROWSER_FACTORY_IMPL_INTERFACE_CLASSNAME =
        "org.web3d.x3d.sai.BrowserFactoryImpl";

    /** The reference to the factory implementation used */
    private static BrowserFactoryImpl factory = null;

    /** The list of properties needed by this class */
    private final static Properties vrml_properties;

    /**
     * Static initializer method. Used to load the system properties for
     * this class. If there are none then it sets up the default values
     * that are needed.
     * <p>
     * At this stage it does not load the factory class, just in case the
     * user may set something at a later date.
     */
    static {
        vrml_properties = new Properties();

        // first look in System properties
        String factory_class_name = AccessController.doPrivileged(
                new PrivilegedAction<String>( ) {
                    @Override
                	public String run( ) {
                        return System.getProperty( FACTORY_CLASS );
                    }
                } );

        if ( factory_class_name != null ) {
            vrml_properties.put( FACTORY_CLASS, factory_class_name );
        }
        else {
            // a System property was not defined, look for an x3d.properties file
            InputStream is = null;
            try {
                // fetch the properties file as a stream
                is = AccessController.doPrivileged(
                    new PrivilegedAction<InputStream>() {
                        @Override
                    	public InputStream run() {
                            // privileged code goes here, for example:
                            return ClassLoader.getSystemResourceAsStream(PROPERTIES_FILE_NAME);
                        }
                    });

                // Fallback for WebStart
                if(is == null)
                    is = BrowserFactory.class.getClassLoader().getResourceAsStream(PROPERTIES_FILE_NAME);

                // Now try the Xj3D-internal version location.
                if(is == null) {
                    is = AccessController.doPrivileged(
                        new PrivilegedAction<InputStream>() {
                            @Override
                        	public InputStream run() {
                                // privileged code goes here, for example:
                                return ClassLoader.getSystemResourceAsStream(XJ3D_PROPERTIES_FILE);
                            }
                        });
                }

                // Fallback for WebStart
                if(is == null)
                    is = BrowserFactory.class.getClassLoader().getResourceAsStream(XJ3D_PROPERTIES_FILE);

                // If there is no x3d.properties file, then fill the properties list
                // ourselves so that everything works as advertised later on.
                if(is == null)
                    vrml_properties.put(FACTORY_CLASS, DEFAULT_FACTORY_CLASS);
                else {
                    // from that stream load it into a properties table
                    vrml_properties.load(is);
                }
            } catch(IOException ioe) {
                System.err.println(ioe);
            } finally {
                try {
                    is.close();
                } catch(IOException ioe) { }
            }
        }
    }

    /**
     * Remove the constructor from public calling. Should never instantiate
     * this class.
     */
    private BrowserFactory() {
    }

    /**
     * Set the factory implementation to use. If the parameter value is null
     * an exception will be thrown.
     *
     * @param fac - The new implementation to use
     * @throws SecurityException The environment does not allow a factory
     *   to be set
     * @throws IllegalArgumentException The argument factory instance is null
     * @throws X3DException The factory is already defined.
     */
	public static synchronized void setBrowserFactoryImpl( BrowserFactoryImpl fac )
        throws IllegalArgumentException, X3DException, SecurityException {

        if(fac == null)
		{
			String errorNotice = NULL_BROWSER_FACTORY_IMPL_ERR_MSG ;
//			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}

        if(factory != null)
		{
			String errorNotice =  FACTORY_ALREADY_DEFINED_ERR_MSG ;
//			validationResult.append(errorNotice).append("\n");
			throw new X3DException(errorNotice);
		}

        // Check to see whether we can really set the factory needed.
        SecurityManager security = System.getSecurityManager();
        if(security != null)
            security.checkSetFactory();

        factory = fac;
    }

    /**
     * Create an X3D player that can be used as an AWT component. The component
     * returned is guaranteed to be an instance of X3DComponent.
     *
     * @param params - Parameters to control the look and feel.
     * @return The component browser initialised to be empty.
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D player.
     * @see X3DComponent
     */
	public static X3DComponent createX3DComponent(Map<String, Object> params) throws NotSupportedException
    {
        X3DComponent comp = null;

        try {
            if(factory == null)
                loadFactoryImpl();

            // comp = factory.createComponent(params);  // TODO fix incorrect method signature
        } catch (NotSupportedException nse) {
            System.err.println("Tracing exception for debug:   Factory: " + factory);
            nse.printStackTrace(System.err);
            throw nse;
        }
        return comp;
    }

    /**
     * Get a browser from the given java applet reference as a base in the
     * current HTML page. Used when attempting to access a browser on the current
     * page as this applet and is the first browser on the page. Generically, the
     * same as calling getBrowser(applet, "", 0);
     *
     * @param applet The applet reference to use
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D player
     * @exception NoSuchBrowserException Could not locate an X3D player on the
     *    same page as the applet.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
	public static ExternalBrowser getBrowser(Applet applet)
        throws NotSupportedException, NoSuchBrowserException, ConnectionException {

        if(factory == null)
            loadFactoryImpl();

        // return factory.getBrowser(applet);  // TODO fix incorrect method signature
		return null; // throw NotSupportedException(); // TODO fix incorrect method signature
    }

    /**
     * Get a browser from the given java applet reference one some named page and
     * at some embed location. Used when attempting to access a browser on
     * another HTML page within a multi-framed environment, or if there are a
     * number of X3D player instances located on the same page.
     * <p>
     * If the frame name is a zero length string or null then it is assumed to be
     * located on the same HTML page as the applet. The index is the number of
     * the embed X3D player starting from the top of the page. If there are
     * other non-X3D plugins embedded in the page these are not taken into
     * account in calculating the embed index.
     *
     * @param applet - The applet reference to use
     * @param frameName - The name of the frame to look into for the browser
     * @param index - The embed index of the X3D player in the page
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D player.
     * @exception NoSuchBrowserException Could not locate an X3D player on the
     *    same page as the applet.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
	public static ExternalBrowser getBrowser(Applet applet, String frameName, int index)
        throws NotSupportedException, NoSuchBrowserException, ConnectionException {

        if(factory == null)
            loadFactoryImpl();

        // return factory.getBrowser(applet, frameName, index);  // TODO fix incorrect method signature
		return null;
    }

    /**
     * Get a reference to a browser that is located on a remote machine. This
     * a server application to send scene updates to a number of client browsers
     * located on remote machines. If there are a number of browsers running on
     * a remote machine, they can be differentiated by the port number they are
     * listening on.
     * <p>
     * There is no default port number for X3D players.
     *
     * @param address - The address of the machine to connect to
     * @param port - The port number on that machine to connect to.
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D player.
     * @exception NoSuchBrowserException Could not locate an X3D player on the
     *    same page as the applet.
     * @exception UnknownHostException Could not find the machine named in the
     *    address.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
	public static ExternalBrowser getBrowser(InetAddress address, int port)
        throws NotSupportedException, NoSuchBrowserException, UnknownHostException,
    ConnectionException {

        if(factory == null)
            loadFactoryImpl();

        // return factory.getBrowser(address, port);  // TODO fix incorrect method signature
		return null;
    }

    /**
     * Private method to load the resource file and use the appropriate class
     * defined in the properties file for dealing with the resource management
     * <p>
     * Assumes that the factory reference is currently null as it automatically
     * writes over the top of it.
     */
    private static void loadFactoryImpl( ) {

        try {
            // load the factory class
            String factory_class_name =
            vrml_properties.getProperty( FACTORY_CLASS, DEFAULT_FACTORY_CLASS );

            Class<?> factory_class = Class.forName( factory_class_name );
            factory = (BrowserFactoryImpl)factory_class.newInstance( );

        } catch( ClassNotFoundException cnfe ) {
            System.err.println( FACTORY_CLASS_NOT_FOUND_ERR_MSG );
            //cnfe.printStackTrace(System.err);

        } catch( InstantiationException ie ) {
            System.err.println( UNABLE_TO_INSTANTIATE_FACTORY_ERR_MSG );
            //ie.printStackTrace(System.err);

        } catch( IllegalAccessException iae ) {
            System.err.println( iae );
            //iae.printStackTrace(System.err);

        } catch( ClassCastException cce ) {
            System.err.println( CLASS_NOT_A_BROWSER_FACTORY_IMPL_ERR_MSG +
                BROWSER_FACTORY_IMPL_INTERFACE_CLASSNAME );
            //cce.printStackTrace(System.err);
        }
    }
]]></xsl:text></xsl:with-param>
		</xsl:call-template>

		<!-- TODO not defined in specification but apparently necessary? -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>BrowserFactoryImpl</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text><![CDATA[
import java.applet.Applet;
import java.net.UnknownHostException;
import java.net.InetAddress;
import java.util.Map;
]]></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Implementation of factory class for obtaining references to browser instances.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.2 BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock"><xsl:text><![CDATA[
<p>
The factory implementation interface for obtaining references to browser
instances.
</p>
<p>
Any implementation of a X3D browser that wishes to provide their own
customised version of the browser factory should must subclass this class.
In particular this is useful if the implementation needs to stay within the
package defined by the application for other reasons.
</p>
<p>
A default implementation of this class is the DefaultBrowserFactoryImpl which
is package access only.
</p>]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
    /**
     * Create a X3D browser that can be used as an AWT component. The component
     * returned is guaranteed to be an instance of X3DComponent.
     *
     * @param params Parameters to control the look and feel.
     * @return The component browser initialised to be empty.
     * @exception NotSupportedException The implementation does not support this
     *    type of browser.
     * @see X3DComponent
     */
    X3DComponent createComponent(Map<String, Object> params) throws NotSupportedException;

    /**
     * Get a browser from the given java applet reference as a base in the
     * current HTML page. Used when attempting to access a browser on the current
     * page as this applet and is the first browser on the page. Generically, the
     * same as calling getBrowser(applet, "", 0);
     *
     * @param applet The applet reference to use
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D browser
     * @exception NoSuchBrowserException Could not locate a X3D browser on the
     *    same page as the applet.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
    ExternalBrowser getBrowser(Applet applet) throws NotSupportedException, NoSuchBrowserException, ConnectionException;

    /**
     * Get a browser from the given java applet reference one some named page and
     * at some embed location. Used when attempting to access a browser on
     * another HTML page within a multi-framed environment, or if there are a
     * number of X3D browser instances located on the same page.
     * <p>
     * If the frame name is a zero length string or null then it is assumed to be
     * located on the same HTML page as the applet. The index is the number of
     * the embed X3D browser starting from the top of the page. If there are
     * other non-X3D plugins embedded in the page these are not taken into
     * account in calculating the embed index.
     *
     * @param applet The applet reference to use
     * @param frameName The name of the frame to look into for the browser
     * @param index The embed index of the X3D browser in the page
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D browser.
     * @exception NoSuchBrowserException Could not locate a X3D browser on the
     *    same page as the applet.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
    ExternalBrowser getBrowser(Applet applet,
                               String frameName,
                               int index)
        throws NotSupportedException, NoSuchBrowserException, ConnectionException;

    /**
     * Get a reference to a browser that is located on a remote machine. This
     * a server application to send scene updates to a number of client browsers
     * located on remote machines. If there are a number of browsers running on
     * a remote machine, they can be differentiated by the port number they are
     * listening on.
     * <p>
     * There is no default port number for X3D browsers.
     *
     * @param address The address of the machine to connect to
     * @param port The port number on that machine to connect to.
     * @return A reference to the Browser implementation
     * @exception NotSupportedException The implementation does not support this
     *    type of X3D browser.
     * @exception NoSuchBrowserException Could not locate a X3D browser on the
     *    same page as the applet.
     * @exception UnknownHostException Could not find the machine named in the
     *    address.
     * @exception ConnectionException An error occurred during the connecting
     *    process
     */
    ExternalBrowser getBrowser(InetAddress address, int port)
        throws NotSupportedException, NoSuchBrowserException, UnknownHostException, ConnectionException;
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<!-- TODO not defined in specification but apparently necessary? -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DComponent</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.2 BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock"><xsl:text><![CDATA[
<p>
Provides for implementation of a X3D player than runs as a
component and able to extract a Browser reference from it.
</p>
<p>
Generally this is used to provide a definition of an AWT component with a
VRML/X3D display capability. There is no reason why this can not be used for
other browser representations such as off-screen renderers or file savers.
<p>
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
    /**
     * Get a browser reference from this component that represents the
     * internals of this browser.
     *
     * @return A reference to the browser object represented by this component.
     */
    ExternalBrowser getBrowser();

    /**
     * Get a reference to the component implementation. For example, if this
     * is an AWT component, it would return an instance of {@link java.awt.Component}.
     * @return a reference to the component implementation
     */
    Object getImplementation();

    /**
     * Shutdown the component because it will no longer be needed. If the
     * component has already had this method called, it will silently ignore
     * any further requests.
     */
    void shutdown();
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<!-- TODO not defined in specification but apparently necessary?? check duplicated inner class above -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>ExternalBrowser</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.2 BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock"><xsl:text><![CDATA[
<p>
Browser interface that represents the additional abilities an external
application is granted to the X3D browser.
</p>
<p>
A number of the methods in this application can take strings representing URLs.
relative URL strings contained in URL fields of nodes or these method
arguments are interpreted as follows:
</p>
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
    /**
     * Lock the output from the external interface to the browser as the code
     * is about to begin a series of updates. No events will be passed to the
     * X3D world. They will be buffered pending release due to a subsequent
     * call to endUpdate.
     * <p>
     * This call is a nesting call which means subsequent calls to beginUpdate
     * are kept on a stack. No events will be released to the X3D browser
     * until as many endUpdates have been called as beginUpdate.
     *
     * @exception InvalidBrowserException The dispose method has been called on
     *    this browser reference.
     * @exception ConnectionException An error occurred in the connection to the
     *    browser.
     */
    void beginUpdate() throws InvalidBrowserException;

    /**
     * Release the output of events from the external interface into the
     * X3D browser. All events posted to this point from the last time that
     * beginUpdate was called are released into the X3D browser for
     * processing at the next available opportunity.
     * <p>
     * This call is a nesting call which means subsequent calls to beginUpdate
     * are kept on a stack. No events will be released to the X3D browser
     * until as many endUpdates have been called as beginUpdate.
     * <p>
     * If no beginUpdate has been called before calling this method, it has
     * no effect.
     *
     * @exception InvalidBrowserException The dispose method has been called on
     *    this browser reference.
     * @exception ConnectionException An error occurred in the connection to the
     *    browser.
     */
    void endUpdate() throws InvalidBrowserException;

    /**
     * Add a listener for browser events. Any changes in the browser will be
     * sent to this listener. The order of calling listeners is not guaranteed.
     * Checking is performed on whether the nominated listener is already
     * registered to ensure that multiple registration cannot take place.
     * Therefore it is possible to multiply register the one class
     * instance while only receiving one event.
     *
     * @param l The listener to add.
     * @exception NullPointerException If the provided listener reference is
     *     null
     * @exception InvalidBrowserException The dispose method has been called on
     *    this browser reference.
     * @exception ConnectionException An error occurred in the connection to the
     *    browser.
     */
    void addBrowserListener(BrowserListener l) throws InvalidBrowserException;

    /**
     * Remove a listener for browser events. After calling this method, the
     * listener will no longer receive events from this browser instance. If the
     * listener passed as an argument is not currently registered, the method
     * will silently exit.
     *
     * @param l The listener to remove
     * @exception NullPointerException If the provided listener reference is
     *     null
     * @exception InvalidBrowserException The dispose method has been called on
     *    this browser reference.
     * @exception ConnectionException An error occurred in the connection to the
     *    browser.
     */
    void removeBrowserListener(BrowserListener l) throws InvalidBrowserException;

    /**
     * Dispose the resources that are used by this instance. Should be called
     * just prior to leaving the application.
     */
    void dispose();
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
		
		<!-- TODO not defined in specification but apparently necessary?? check duplicated inner class above -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>BrowserListener</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>java.util.EventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Listener interface for classes wishing to know about changes in the browser</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.5.2 BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserFactory</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="interfaceBlock"><xsl:text><![CDATA[
    /**
     * Process an event that has occurred in the X3D player.
     *
     * @param event The event that caused this method to be called
     */
    void browserChanged(BrowserEvent event);
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="StatementInterfaces">
		
		<xsl:variable name="subPackage">
			<xsl:if test="($modifySpecificationInterfaces = 'true')">
				<xsl:text>statements</xsl:text>
			</xsl:if>
		</xsl:variable>
		
		<!-- B.6 Statement interfaces -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#StatementInterfaces -->
		
		<!-- TODO: specification  definitions for other statements; add accessor methods for setting values -->

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>ComponentInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.6.1 ComponentInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#ComponentInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>7.2.5.4 COMPONENT statement</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>components/core.html#COMPONENTStatement</xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
Description of a single component.1188311883
A component description contains useful pieces of information about
the requirements. Of primary importance is the specification component name and level.
Additional information includes title and URL for the component provider.
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock">
				<xsl:text><![CDATA[
    /**
     * Get the name of this component.
     * @return name The name of the component
     */
	public String getName();
				
    /**
     * Get the level of the component. A level is always greater than zero.
     * The level information may represent one of two things, depending on
     * how the component info was created. When created as part of a file that
     * is requesting a specific level of support, the level will indicate the
     * requested level, not the maximum available on the system. When this is
     * returned from a query of the system to see what components are available
     * then the level is maximum supported by the implementation.
     *
     * @return The level value for the component
	 */
	public int getLevel();
				
    /**
     * Get the title of this component. This is a long-form version that can
     * be used in a UI. If no title is set, will return null.
     *
     * @return The title string of the component
     */
	public String getTitle();
				
    /**
     * Get the URL of the provider. This is used for user interface information
     * to point an end user at someone who has implemented this bit of
     * functionality. It is not used by the system to download the component
     * or its definition.
     *
     * @return The URL of the provider as a string
     */
	public String getProviderURL();
				
    /**
     * Return a formatted string version of this component that conforms to
     * the X3D specification for X3D file encoding. The string will start
     * with the <code>COMPONENT</code> keyword, as per specification.
     *
     * @return A correctly formatted string.
     */
	public String toX3DString();
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>ProfileInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.6.2 ProfileInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#ProfileInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>7.2.5.3 PROFILE statement</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>components/core.html#PROFILEStatement</xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
Description of a single profile, which is a collection of components.
A profile defines the player or tool support needed for a particular scene.
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock">
				<xsl:text><![CDATA[
    /**
     * Get the name of this component.
     *
     * @return name The name of the component
     */
	public String getName();
				
    /**
     * Get the title of this component. This is a long-form version that can
     * be used in a UI.
     *
     * @return The title string of this component
     */
	public String getTitle();
				
    /**
     * Get the list of defined components for this profile. A profile will
     * always have one or more components.
     *
     * @return An array of ComponentInfo definitions for this profile
     */
	public ComponentInfo[] getComponents();

    /**
     * Return a formatted string version of this component that conforms to
     * the X3D specification for X3D file encoding. The string will start
     * with the <code>PROFILE</code> keyword, as per specification.
     *
     * @return A correctly formatted string
     */
	public String toX3DString();
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>UnitInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.6.3 UnitInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#UnitInfo</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>7.2.5.5 UNIT statement</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text>components/core.html#UNITStatement</xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
UNIT statements define data conversion factors for a scene that can override default units of measure for angles in radians, length in meters, etc. 
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="interfaceBlock">
				<xsl:text><![CDATA[
    /**
     * Get the name of this UNIT statement.
     *
     * @return The name of the UNIT statement
     */
	public String getName();
					
    /**
     * Get the category (angle | length | force | mass) of this UNIT statement.
     *
     * @return The category of the UNIT statement
     */
	public String getCategory();
					
    /**
     * Get the positive double-precision factor that converts new base unit to default base unit.
     *
     * @return The positive double-precision conversion factor of the UNIT statement
     */
	public double getConversionFactor();

    /**
     * Return a formatted string version of this component that conforms to
     * the X3D specification for X3D file encoding. The string will start
     * with the <code>UNIT</code> keyword, as per specification.
     *
     * @return A correctly formatted string
     */
	public String toX3DString();
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="ExceptionDefinitions">
		
		<xsl:variable name="subPackage">
			<xsl:if test="($modifySpecificationInterfaces = 'true')">
				<xsl:text>exceptions</xsl:text>
			</xsl:if>
		</xsl:variable>
		
		<!-- B.7 Exception definitions -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#ExceptionDefinitions -->
		
		<!-- TODO fix specification definitions to be interfaces for all of these classes, can't simply define method stubs in class definitions -->
		
		<!-- TODO fix specification TOC bookmark -->
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>RuntimeException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.1 X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The basic exception that is thrown by any X3D method call that needs to
throw an exception.

Based on RuntimeException so that the user has the choice of deciding
whether to catch the exception or not.
]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public X3DException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public X3DException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>BrowserNotSharedException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.2 BrowserNotSharedException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#BrowserNotSharedException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the user attempts to make method calls
that require this browser to be shared.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public BrowserNotSharedException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public BrowserNotSharedException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>ConnectionException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.6.3 ConnectionException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#ConnectionException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when an error occurs in the connection between
the external application and the X3D browser. Typically this might be a
network connection stopping or similar problem.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public ConnectionException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public ConnectionException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>ImportedNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.6.4 ImportedNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#ImportedNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the user attempts to use an IMPORTed node
incorrectly in the scene graph.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public ImportedNodeException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public ImportedNodeException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InsufficientCapabilitiesException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.5 InsufficientCapabilitiesException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InsufficientCapabilitiesException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a node of greater capabilities than
the scene's declared profile and additional components is attempted to be
added to that scene.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InsufficientCapabilitiesException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InsufficientCapabilitiesException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.6 InvalidBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the user attempts to access a method in
the Browser interface after the reference has had the dispose method called.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidBrowserException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidBrowserException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidDocumentException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.7 InvalidDocumentException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidDocumentException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the user attempts to import a DOM Document
to make it into an X3DScene and the document is not correctly structured.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidDocumentException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidDocumentException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidExecutionContextException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.8 InvalidExecutionContextException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidExecutionContextException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a reference to an ExecutionContext is
not valid.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidExecutionContextException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidExecutionContextException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidFieldException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.9 InvalidFieldException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidFieldException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
<p>
The exception that is thrown when a reference to any field is not valid.
Generally used as a base class to more specific invalid field methods.
</p>
<p>
A field may be invalid for a number of reasons:
</p>
<ul>
	<li>The user may have typed in the wrong name through a typo.</li>
	<li>The name may not correspond to a field in that node at all.</li>
	<li>The name given refers to a valid field but the field cannot be
     accessed as an outputOnly field.</li>
</ul></xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidFieldException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidFieldException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidFieldValueException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.10 InvalidFieldValueException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidFieldValueException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
This exception may be generated when a node verifies the correctness of a setValue operation.
The exception can occur during the scene-parsing process, or else by the field during
runtime as the user is trying to modify it.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidFieldValueException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidFieldValueException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.11 InvalidNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidNodeException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a reference to a Node is not valid.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidNodeException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidNodeException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidOperationTimingException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.12 InvalidOperationTimingException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidOperationTimingException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the user attempts to use an API call
outside of the predefined times when allowed.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidOperationTimingException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidOperationTimingException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidProtoException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.13 InvalidProtoException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidProtoException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a reference to a ProtoDeclare, ExternProtoDeclare
or ProtoInstance is not valid.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidProtoException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidProtoException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidRouteException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.14 InvalidRouteException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidRouteException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when any reference used by a ROUTE is not valid.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidRouteException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidRouteException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidURLException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text>B.7.15 InvalidURLException</xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidURLException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the ordered list of all URL and URN values are
invalid and cannot be parsed to form a proper URL/URN.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidURLException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidURLException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>InvalidX3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.16 InvalidX3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#InvalidX3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a the string passed to createVrmlFromString
or createX3dFromString method does not contain legal X3D, using either
UTF8 or XML syntax.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public InvalidX3DException()
	{
		// TODO
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public InvalidX3DException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>NodeInUseException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.17 NodeInUseException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#NodeInUseException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when a reference to a Node is already being
used when the user wants to add a new DEF, EXPORT or IMPORT definition.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public NodeInUseException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public NodeInUseException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>NodeUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.18 NodeUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#NodeUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when asking for a Node by name, and the
name is valid but the underlying node reference is not available from the
Inline yet.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public NodeUnavailableException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public NodeUnavailableException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>NoSuchBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.19 NoSuchBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#NoSuchBrowserException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the Browser factory is not able to locate
a browser with the given arguments.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public NoSuchBrowserException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public NoSuchBrowserException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>NotSupportedException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.20 NotSupportedException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#NotSupportedException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when an operation is not supported by an
underlying implementation.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public NotSupportedException()
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public NotSupportedException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>

		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>URLUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:value-of select="$subPackage"/></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text>X3DException</xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.7.21 URLUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#URLUnavailableException</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="javadocBlock">
				<xsl:text><![CDATA[
The exception that is thrown when the URL is not specified for the currently
browser instance or there is some other problem.]]></xsl:text>
			</xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
    /**
     * Construct a basic instance of this exception with no error message.
     */
	public URLUnavailableException() 
	{
    }

    /**
     * Constructs a new exception with a specific message report.
     * @param message description for this exception
     */
	public URLUnavailableException (String message)
    {
        super(message);
    }
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="NodeTypeDefinitions">
		
		<!-- B.2 Node type interfaces definitions -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#NodeTypeInterfaces -->
		
		<xsl:for-each select="//AbstractNodeTypes/AbstractNodeType">
			
			<xsl:variable name="name"                                select="@name"/>
			<xsl:variable name="description"                         select="InterfaceDefinition/@appinfo"/>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			<xsl:variable name="extends"                             select="InterfaceDefinition/Inheritance/@baseType"/>
			<xsl:variable name="componentName"                       select="translate(InterfaceDefinition/componentInfo/@name,'-','')"/>
			<xsl:variable name="componentLevel"                      select="InterfaceDefinition/componentInfo/@level"/>
			<xsl:variable name="javadocBlock">
				<!-- anything else? -->
			</xsl:variable>
		
			<!-- TODO add specification parameters... -->
			
			<xsl:variable name="additionalInheritances">
				<xsl:for-each select="InterfaceDefinition/AdditionalInheritance">
					<xsl:text>, </xsl:text>
					<xsl:value-of select="@baseType"/>
				</xsl:for-each>
			</xsl:variable>
			
			<xsl:variable name="imports">
				<!-- TODO do not import inherited (extends) interface if in same package -->
				<xsl:variable name="baseType"   select="$extends"/>
				<xsl:variable name="subPackage" select="//*[@name=$baseType]/InterfaceDefinition/componentInfo/@name"/><!-- corresponding subPackage name -->
				<xsl:if test="(string-length($extends) > 0) and (string-length($subPackage) > 0) and (string-length($baseType) > 0) and
                              ($componentName != $subPackage)">
					<xsl:text>import org.web3d.x3d.sai.</xsl:text>
					<xsl:if test="(string-length($subPackage) > 0)">
						<xsl:value-of select="$subPackage"/>
						<xsl:text>.</xsl:text>
					</xsl:if>
					<xsl:value-of select="$baseType"/>
					<xsl:text>;</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
					
				<xsl:for-each select="InterfaceDefinition/AdditionalInheritance">
					<xsl:variable   name="baseType" select="@baseType"/>
					<xsl:variable name="subPackage" select="//*[@name=$baseType]/InterfaceDefinition/componentInfo/@name"/><!-- corresponding subPackage name -->
					<!-- avoid imports from same package -->
					<xsl:if test="($componentName != $subPackage)">
						<xsl:text>import org.web3d.x3d.sai.</xsl:text>
						<xsl:if test="(string-length($subPackage) > 0)">
							<xsl:value-of select="$subPackage"/>
							<xsl:text>.</xsl:text>
						</xsl:if>
						<xsl:value-of select="$baseType"/>
						<xsl:text>;</xsl:text>
						<xsl:text>&#10;</xsl:text>
					</xsl:if>
				</xsl:for-each>
			</xsl:variable>
			
			<!-- TODO specification needs to say that abstract node types need to go into subpackage corresponding to component -->
	  
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:value-of select="$imports"/></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:value-of select="$componentName"/></xsl:with-param>
				<xsl:with-param name="extends"><xsl:value-of select="$extends"/><xsl:value-of select="$additionalInheritances"/></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
			<xsl:variable name="inheritanceName"                       select="InterfaceDefinition/Inheritance/@baseType"/>
			<xsl:variable name="inheritanceComponent"                  select="concat(//AbstractNodeType  [@name = $inheritanceName]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $inheritanceName]/InterfaceDefinition/componentInfo/@name)"/>
				
			<xsl:variable name="additionalInheritanceName1"            select="InterfaceDefinition/AdditionalInheritance[1]/@baseType"/>
			<xsl:variable name="additionalInheritanceComponent1"       select="concat(//AbstractNodeType  [@name = $additionalInheritanceName1]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $additionalInheritanceName1]/InterfaceDefinition/componentInfo/@name)"/>
			<xsl:variable name="additionalInheritanceName2"            select="InterfaceDefinition/AdditionalInheritance[2]/@baseType"/>
			<xsl:variable name="additionalInheritanceComponent2"       select="concat(//AbstractNodeType  [@name = $additionalInheritanceName2]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $additionalInheritanceName2]/InterfaceDefinition/componentInfo/@name)"/>
			<xsl:variable name="extendsInterface">
				<xsl:text>org.web3d.x3d.sai.</xsl:text>
				<xsl:value-of select="$componentName"/>
				<xsl:text>.</xsl:text>
				<xsl:value-of select="$name"/>
				
					<xsl:if test="(count(InterfaceDefinition/Inheritance) > 0) and (string-length($inheritanceComponent) > 0)">
						<xsl:text>,</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>										org.web3d.x3d.java.</xsl:text>
						<xsl:value-of select="$inheritanceComponent"/>
						<xsl:text>.</xsl:text>
						<xsl:value-of select="$inheritanceName"/>
						<xsl:value-of select="$jsaiInterfaceSuffix"/>
					</xsl:if>
					<xsl:if test="(count(InterfaceDefinition/AdditionalInheritance) > 0) and (string-length($additionalInheritanceComponent1) > 0)">
						<xsl:text>,</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>										org.web3d.x3d.java.</xsl:text>
						<xsl:value-of select="$additionalInheritanceComponent1"/>
						<xsl:text>.</xsl:text>
						<xsl:value-of select="$additionalInheritanceName1"/>
						<xsl:value-of select="$jsaiInterfaceSuffix"/>
					</xsl:if>
					<xsl:if test="(count(InterfaceDefinition/AdditionalInheritance) > 1) and (string-length($additionalInheritanceComponent2) > 0)">
						<xsl:text>,</xsl:text>
						<xsl:text>&#10;</xsl:text>
						<xsl:text>						org.web3d.x3d.java.</xsl:text>
						<xsl:value-of select="$additionalInheritanceComponent2"/>
						<xsl:text>.</xsl:text>
						<xsl:value-of select="$additionalInheritanceName2"/>
						<xsl:value-of select="$jsaiInterfaceSuffix"/>
					</xsl:if>
					<!-- debug 
					<xsl:text> // end extendsInheritance</xsl:text>
					-->
			</xsl:variable>

<!-- debug -->
<xsl:if test="($debug = 'true')">
<xsl:message>
<xsl:text>// NodeTypeDefinitions interfaces ($nameInterface=</xsl:text>
<xsl:value-of select="$name"/><xsl:value-of select="$jsaiInterfaceSuffix"/>
<xsl:text>, $inheritanceName=</xsl:text>
<xsl:value-of select="$inheritanceName"/>
<xsl:text>, $inheritanceComponent=</xsl:text>
<xsl:value-of select="$inheritanceComponent"/>
<xsl:text>, $additionalInheritanceName1=</xsl:text>
<xsl:value-of select="$additionalInheritanceName1"/>
<xsl:text>, $additionalInheritanceComponent1=</xsl:text>
<xsl:value-of select="$additionalInheritanceComponent1"/>
<xsl:text>, $additionalInheritanceName2=</xsl:text>
<xsl:value-of select="$additionalInheritanceName2"/>
<xsl:text>, $additionalInheritanceComponent2=</xsl:text>
<xsl:value-of select="$additionalInheritanceComponent2"/>
<xsl:text>)</xsl:text>
</xsl:message>
</xsl:if>
		</xsl:for-each>		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="ObjectTypeDefinitions">
		
		<!-- B.3 Auxiliary node type interfaces definitions -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#AuxiliaryNodeTypeInterfaces -->
		
		<xsl:for-each select="//AbstractObjectTypes/AbstractObjectType">
			
			<xsl:variable name="name"                                select="@name"/>
			<xsl:variable name="description"                         select="InterfaceDefinition/@appinfo"/>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			<xsl:variable name="extends"                             select="InterfaceDefinition/Inheritance/@baseType"/>
			<xsl:variable name="componentName"                       select="translate(InterfaceDefinition/componentInfo/@name,'-','')"/>
			<xsl:variable name="componentLevel"                      select="InterfaceDefinition/componentInfo/@level"/>
			<xsl:variable name="javadocBlock">
				<!-- anything else? -->
			</xsl:variable>
	  
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:value-of select="$componentName"/></xsl:with-param>
				<xsl:with-param name="extends"><xsl:value-of select="$extends"/></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>abstracts.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
		</xsl:for-each>		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="NodeInterfacesDefinitions">
		
		<!-- B.3 Auxiliary node type interfaces definitions -->
		<!-- http://www.web3d.org/documents/specifications/19777-2/V3.0/Part2/abstracts.html#AuxiliaryNodeTypeInterfaces -->
		
		<xsl:for-each select="//ConcreteNodes/ConcreteNode">
			
			<xsl:variable name="name"                                select="@name"/>
			<xsl:variable name="description"                         select="InterfaceDefinition/@appinfo"/>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			<xsl:variable name="extends"                             select="InterfaceDefinition/Inheritance/@baseType"/>
			<xsl:variable name="componentName"                       select="translate(InterfaceDefinition/componentInfo/@name,'-','')"/>
			<xsl:variable name="componentLevel"                      select="InterfaceDefinition/componentInfo/@level"/>
			<xsl:variable name="javadocBlock">
				<!-- anything else? -->
			</xsl:variable>
				
			<xsl:variable name="additionalInheritances">
				<xsl:for-each select="InterfaceDefinition/AdditionalInheritance">
					<xsl:text>, </xsl:text>
					<xsl:value-of select="@baseType"/>
				</xsl:for-each>
			</xsl:variable>
			
			<xsl:variable name="imports">
				<!-- TODO do not import inherited (extends) interface if in same package -->
				<xsl:variable name="baseType"   select="$extends"/>
				<xsl:variable name="subPackage" select="//*[@name=$baseType]/InterfaceDefinition/componentInfo/@name"/><!-- corresponding subPackage name -->
				<xsl:if test="(string-length($extends) > 0) and (string-length($subPackage) > 0) and (string-length($baseType) > 0) and
                              ($componentName != $subPackage)">
					<xsl:text>&#10;</xsl:text>
					<xsl:text>import org.web3d.x3d.sai.</xsl:text>
					<xsl:if test="(string-length($subPackage) > 0)">
						<xsl:value-of select="$subPackage"/>
						<xsl:text>.</xsl:text>
					</xsl:if>
					<xsl:value-of select="$baseType"/>
					<xsl:text>;</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
					
				<xsl:for-each select="InterfaceDefinition/AdditionalInheritance">
					<xsl:variable   name="baseType" select="@baseType"/>
					<xsl:variable name="subPackage" select="//*[@name=$baseType]/InterfaceDefinition/componentInfo/@name"/><!-- corresponding subPackage name -->
					<!-- avoid imports from same package -->
					<xsl:if test="($componentName != $subPackage)">
						<xsl:text>import org.web3d.x3d.sai.</xsl:text>
						<xsl:if test="(string-length($subPackage) > 0)">
							<xsl:value-of select="$subPackage"/>
							<xsl:text>.</xsl:text>
						</xsl:if>
						<xsl:value-of select="$baseType"/>
						<xsl:text>;</xsl:text>
						<xsl:text>&#10;</xsl:text>
					</xsl:if>
				</xsl:for-each>
			</xsl:variable>
			
			<!-- TODO add variable $x3dAbstractSpecificationSection -->
	  
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:value-of select="$imports"/></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:value-of select="$componentName"/></xsl:with-param>
				<xsl:with-param name="extends"><xsl:value-of select="$extends"/><xsl:value-of select="$additionalInheritances"/></xsl:with-param>
				<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>concretes.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
			</xsl:call-template>
			
		</xsl:for-each>
		
		<!-- create Javadoc package.html files for each subpackage -->
		<xsl:for-each select="//componentInfo[not(@name = preceding::componentInfo/@name)]">
		
			<xsl:variable name="componentName" select="translate(@name,'-','')"/>
			<xsl:variable name="sourceFilePath">
				<xsl:value-of select="$saiPackageDirectorySource"/>
				<xsl:text>/</xsl:text>
				<xsl:value-of select="translate(@name,'-','')"/><!-- no componentName hypens allowed (e.g. H-Anim) -->
				<xsl:text>/</xsl:text>
				<xsl:text>package.html</xsl:text>
			</xsl:variable>
			
			<xsl:variable name="componentDescription" select="//SimpleType[@name='componentNames']/enumeration[translate(@value,'-','') = $componentName]/@appinfo"/>
			
			<!-- debug
			<xsl:message>
				<xsl:text>*** componentName=</xsl:text>
				<xsl:value-of select="$componentName"/>
				<xsl:text>, sourceFilePath=</xsl:text>
				<xsl:value-of select="$sourceFilePath"/>
				<xsl:text>, componentDescription=</xsl:text>
				<xsl:value-of select="$componentDescription"/>
			</xsl:message> 
			-->
			
			<xsl:if test="(string-length($componentDescription) > 0)">
				<!-- create source file -->
				<xsl:result-document href="{$sourceFilePath}" method="html" omit-xml-declaration="yes" encoding="UTF8" indent="yes">
					<xsl:element name="html">
						<xsl:element name="body">
							<xsl:element name="p">
								<xsl:text>&#10;</xsl:text>
								<xsl:value-of select="$componentDescription"/>
							</xsl:element>
						</xsl:element>
					</xsl:element>

				</xsl:result-document>
			</xsl:if>			
		</xsl:for-each><!-- finished Javadoc package.html files for each subpackage -->
		
		<!-- root package.html -->
		<xsl:result-document href="{$saiPackageDirectorySource}/package.html" method="html" omit-xml-declaration="yes" encoding="UTF8" indent="yes">
			<xsl:element name="html">
				<xsl:element name="body">
					<xsl:element name="p">
						<xsl:text>
	The X3D Java Scene Access Interface (SAI) package is designe to 
	provide access to a browser and its contained scene graph,
	either within an internal X3D Script node or an external HTML script.</xsl:text>
					</xsl:element>
					<xsl:element name="p">
						<xsl:text>
	This package contains specification-defined X3D SAI interfaces and utility classes, 
	used for compiling Java source code to be used by an X3D Script node.
						</xsl:text>
					</xsl:element>
				</xsl:element>
			</xsl:element>
		</xsl:result-document>
		
    </xsl:template>
	
    <!-- ===================================================== -->
	
	<xsl:template name="ConcreteNodeObjectDefinitions">
		
		<!-- TODO X3D Java Language Binding specification section on concrete classes that match X3D Abstract Specification -->
		<!-- http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/nodeIndex.html -->
		
		<!-- Concrete classes for X3D nodes - - - - - - - - - -->
		
		<xsl:for-each select="//ConcreteNodes/ConcreteNode">
			
			<xsl:variable name="name"                                select="@name"/>
			<xsl:variable name="description"                         select="InterfaceDefinition/@appinfo"/>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			<xsl:variable name="componentName"                       select="translate(InterfaceDefinition/componentInfo/@name,'-','')"/>
			<xsl:variable name="componentLevel"                      select="InterfaceDefinition/componentInfo/@level"/>
			<xsl:variable name="interfaceName"                       select="InterfaceDefinition/Inheritance/@baseType"/>
			<xsl:variable name="interfaceComponent"                  select="concat(//AbstractNodeType  [@name = $interfaceName]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $interfaceName]/InterfaceDefinition/componentInfo/@name)"/>
			<xsl:variable name="additionalInterfaceName1"            select="InterfaceDefinition/AdditionalInheritance[1]/@baseType"/>
			<xsl:variable name="additionalInterfaceComponent1"       select="concat(//AbstractNodeType  [@name = $additionalInterfaceName1]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $additionalInterfaceName1]/InterfaceDefinition/componentInfo/@name)"/>
			<xsl:variable name="additionalInterfaceName2"            select="InterfaceDefinition/AdditionalInheritance[2]/@baseType"/>
			<xsl:variable name="additionalInterfaceComponent2"       select="concat(//AbstractNodeType  [@name = $additionalInterfaceName2]/InterfaceDefinition/componentInfo/@name,
                                                                                    //AbstractObjectType[@name = $additionalInterfaceName2]/InterfaceDefinition/componentInfo/@name)"/>
			<xsl:variable name="implements">
				<!-- SAI abstract interface reference -->
				<xsl:text>org.web3d.x3d.sai.</xsl:text>
				<xsl:value-of select="$componentName"/>
				<xsl:text>.</xsl:text>
				<xsl:value-of select="@name"/>
				<!-- TODO: remove concrete-package interface references
				<xsl:text>, </xsl:text>
				<xsl:text>&#10;</xsl:text>
				<xsl:text>										org.web3d.x3d.java.</xsl:text>
				<xsl:value-of select="$interfaceComponent"/>
				<xsl:text>.</xsl:text>
				<xsl:value-of select="$interfaceName"/>
				<xsl:value-of select="$jsaiInterfaceSuffix"/>
				<xsl:if test="(count(InterfaceDefinition/AdditionalInheritance) > 0) and (string-length($additionalInterfaceComponent1) > 0)">
					<xsl:text>,</xsl:text>
					<xsl:text>&#10;</xsl:text>
					<xsl:text>										org.web3d.x3d.java.</xsl:text>
					<xsl:value-of select="$additionalInterfaceComponent1"/>
					<xsl:text>.</xsl:text>
					<xsl:value-of select="$additionalInterfaceName1"/>
					<xsl:value-of select="$jsaiInterfaceSuffix"/>
				</xsl:if>
				<xsl:if test="(count(InterfaceDefinition/AdditionalInheritance) > 1) and (string-length($additionalInterfaceComponent2) > 0)">
					<xsl:text>,</xsl:text>
					<xsl:text>&#10;</xsl:text>
					<xsl:text>						org.web3d.x3d.java.</xsl:text>
					<xsl:value-of select="$additionalInterfaceComponent2"/>
					<xsl:text>.</xsl:text>
					<xsl:value-of select="$additionalInterfaceName2"/>
					<xsl:value-of select="$jsaiInterfaceSuffix"/>
				</xsl:if> -->
			</xsl:variable>
				
			<xsl:variable name="javadocBlock">
				<!-- anything else? -->
			</xsl:variable>
			
			<!-- TODO add variable $x3dAbstractSpecificationSection -->
	  
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<!-- TODO fix next -->
				<xsl:with-param name="subPackage"><xsl:value-of select="$componentName"/></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text>org.web3d.x3d.java.X3DConcreteNode</xsl:text></xsl:with-param>                             
				<xsl:with-param name="implements"><xsl:value-of select="$implements"/></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<!--
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>concretes.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param> -->

				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock"></xsl:with-param>
				<xsl:with-param name="implementationBlock"></xsl:with-param>
			</xsl:call-template>
			
		</xsl:for-each>
		
		<!-- Concrete classes for X3D statements - - - - - - - - - -->
		
		<xsl:for-each select="//Statements/Statement">
			
			<xsl:variable name="name"                                select="@name"/>
			<xsl:variable name="description">
				<xsl:value-of select="InterfaceDefinition/@appinfo"/> <!-- TODO duplicate -->
				<xsl:text> This concrete class represents an X3D </xsl:text>
				<xsl:if test="not($name = 'X3D')">
					<xsl:value-of select="$name"/>
					<xsl:text> </xsl:text>
				</xsl:if>
				<xsl:text>statement. </xsl:text>
			</xsl:variable>
			<xsl:variable name="x3dAbstractSpecificationRelativeUrl" select="substring-after(InterfaceDefinition/@specificationUrl,'Part01/')"/>
			<xsl:variable name="componentName"                       select="translate(InterfaceDefinition/componentInfo/@name,'-','')"/>
			<xsl:variable name="componentLevel"                      select="InterfaceDefinition/componentInfo/@level"/>
			<xsl:variable name="implements">
				<!-- X3D statements are not defined in specification abstract org.web3d.x3d.sai -->
				<xsl:choose>
					<xsl:when test="($name = 'ROUTE') or 
									($name = 'ProtoDeclare') or ($name = 'ExternProtoDeclare') or ($name = 'ProtoInstance')">
						<xsl:text>org.web3d.x3d.sai.Core.X3DChildNode</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:variable>
			<xsl:variable name="extends">
				<!-- X3D statements are not defined in specification abstract org.web3d.x3d.sai -->
				<!-- created for this library to ensure consistency -->
				<xsl:text>org.web3d.x3d.java.X3DConcreteStatement</xsl:text>
			</xsl:variable>
			<xsl:variable name="javadocBlock">
				<!-- anything else? -->
			</xsl:variable>
			
			<!-- debug
			<xsl:message>
				<xsl:text>*** X3D Statement @name=</xsl:text>
				<xsl:value-of select="@name"/>
				<xsl:text>, $componentName=</xsl:text>
				<xsl:value-of select="$componentName"/>
				<xsl:text>, $implements=</xsl:text>
				<xsl:value-of select="$implements"/>
			</xsl:message> 
			-->
			
			<!-- TODO add variable $x3dAbstractSpecificationSection -->
	  
			<xsl:call-template name="sourceFile">
				<xsl:with-param name="name"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="inConcretePackage"><xsl:text>true</xsl:text></xsl:with-param>
				<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
				<xsl:with-param name="subPackage"><xsl:value-of select="$componentName"/></xsl:with-param>
				<xsl:with-param name="extends"><xsl:text>org.web3d.x3d.java.X3DConcreteStatement</xsl:text></xsl:with-param>
				<xsl:with-param name="implements"><xsl:value-of select="$implements"/></xsl:with-param>
				<xsl:with-param name="description"><xsl:value-of select="$description"/></xsl:with-param>
				<!--
				<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>TODO</xsl:text></xsl:with-param>
				<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>concretes.html#</xsl:text><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
				<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param> -->

				<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:value-of select="$name"/></xsl:with-param>
				<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:value-of select="$x3dAbstractSpecificationRelativeUrl"/></xsl:with-param>
				<xsl:with-param name="javadocBlock"><xsl:value-of select="$javadocBlock"/></xsl:with-param>
				<xsl:with-param name="interfaceBlock">
					<xsl:text><![CDATA[]]></xsl:text>
				</xsl:with-param>
				<xsl:with-param name="implementationBlock"></xsl:with-param>
			</xsl:call-template>
			
		</xsl:for-each>
		
		<!-- create Javadoc package.html files for each subpackage -->
		<xsl:for-each select="//componentInfo[not(@name = preceding::componentInfo/@name)]">
		
			<xsl:variable name="componentName" select="translate(@name,'-','')"/>
			<xsl:variable name="sourceFilePath">
				<xsl:value-of select="$concretePackageDirectorySource"/>
				<xsl:text>/</xsl:text>
				<xsl:value-of select="translate(@name,'-','')"/><!-- no componentName hypens allowed (e.g. H-Anim) -->
				<xsl:text>/</xsl:text>
				<xsl:text>package.html</xsl:text>
			</xsl:variable>
			
			<xsl:variable name="componentDescription" select="//SimpleType[@name='componentNames']/enumeration[translate(@value,'-','') = $componentName]/@appinfo"/>
			
			<!-- debug
			<xsl:message>
				<xsl:text>*** componentName=</xsl:text>
				<xsl:value-of select="$componentName"/>
				<xsl:text>, sourceFilePath=</xsl:text>
				<xsl:value-of select="$sourceFilePath"/>
				<xsl:text>, componentDescription=</xsl:text>
				<xsl:value-of select="$componentDescription"/>
			</xsl:message> 
			-->
			
			<xsl:if test="(string-length($componentDescription) > 0)">
				<!-- create source file -->
				<xsl:result-document href="{$sourceFilePath}" method="html" omit-xml-declaration="yes" encoding="UTF8" indent="yes">
					<xsl:element name="html">
						<xsl:element name="body">
							<xsl:element name="p">
								<xsl:text>&#10;</xsl:text>
								<xsl:value-of select="$componentDescription"/>
							</xsl:element>
						</xsl:element>
					</xsl:element>

				</xsl:result-document>
			</xsl:if>
			
		</xsl:for-each>
		
		<!-- root package.html -->
		<xsl:result-document href="{$concretePackageDirectorySource}/package.html" method="html" omit-xml-declaration="yes" encoding="UTF8" indent="yes">
			<xsl:element name="html">
				<xsl:element name="body">
					<xsl:element name="p">
						<xsl:text>
		The X3D Java Scene Access Interface (SAI) library provides common
		shared X3D Java interfaces for concrete implementation classes.</xsl:text>
					</xsl:element>
					<xsl:element name="p">
						<xsl:text>
		This package contains abstract interfaces that are used by all
		concrete classes for X3D nodes and statements.</xsl:text>
					</xsl:element>
				</xsl:element>
			</xsl:element>
		</xsl:result-document>
		
    <!-- ===================================================== -->
			
	<!-- Utility concrete classes and interfaces for org.web3d.x3d.java package -->
	
	<xsl:call-template name="sourceFile">
		<xsl:with-param name="name"><xsl:text>ConfigurationProperties</xsl:text></xsl:with-param>
		<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
		<xsl:with-param name="subPackage"><xsl:text>Core</xsl:text></xsl:with-param>
		<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="description"><xsl:text>Custom developer configuration properties for X3D Java SAI Library usage.
Output serialization support is provided for indentation, X3D Canonicalization (C14N) and showing default attributes.
TODO more to follow!</xsl:text>
		</xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="javadocBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="interfaceBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="implementationBlock">
			<xsl:text><![CDATA[	// TODO enable user-specified properties file
				
	// TODO singleton pattern
	
	/** Default character-count increment for serializing scene output. */
	public  static final int indentIncrement_DEFAULT = 2;
				
	private static int indentIncrement = indentIncrement_DEFAULT; // static initialization

	/** Whitespace character for indenting when serializing scene output. */
	public  static final char indentCharacter_SPACE = ' ';
				
	/** Alternative whitespace character for indenting when serializing scene output. */
	public  static final char indentCharacter_TAB   = '\t';
				
	/** Default character for indenting when serializing scene output, initialized as indentCharacter_SPACE. */
	public  static final char indentCharacter_DEFAULT = indentCharacter_SPACE;
				
	private static char indentCharacter = indentCharacter_DEFAULT; // static initialization
				
	/** Whether to show default attribute values when serializing scene output, initialized as false. */
	public  static final boolean showDefaultAttributes_DEFAULT   = false;
				
	private static boolean showDefaultAttributes = showDefaultAttributes_DEFAULT; // static initialization
				
	/** Initialize this ConfigurationProperties instance. */
	public static final void initialize()
	{
		indentIncrement = indentIncrement_DEFAULT;
		indentCharacter = indentCharacter_DEFAULT;
		showDefaultAttributes = showDefaultAttributes_DEFAULT;
	}
	/**
	 * Get indentCharacter used when serializing scene output.
	 * @return indentCharacter (either indentCharacter_SPACE or indentCharacter_TAB). */
	public static char getIndentCharacter()
	{
		return indentCharacter;
	}
	/**
	 * Set indentCharacter used when serializing scene output.
	 * @param newIndentCharacter is new indent value (non-negative). */
	public static void setIndentCharacter (char newIndentCharacter)
	{
		if  ((newIndentCharacter == indentCharacter_SPACE) || (newIndentCharacter == indentCharacter_TAB))
			 indentCharacter = newIndentCharacter;
		else 
		{
			String errorNotice = "Invalid indentCharacter='" + newIndentCharacter + 
								 "' provided to ConfigurationProperties, expected indentCharacter_SPACE or indentCharacter_TAB";
//			validationResult.append(errorNotice).append("\n");
			throw new InvalidFieldValueException(errorNotice);
		} 
	}
	/**
	 * Get number of characters to indent when serializing scene output.
	 * @return number of characters (non-negative). */
	public static int getIndentIncrement()
	{
		return indentIncrement;
	}
	/**
	 * Set number of characters to indent when serializing scene output.
	 * @param newIndentIncrement is new indentIncrement value (non-negative). */
	public static void setIndentIncrement (int newIndentIncrement)
	{
		if  (newIndentIncrement >= 0)
			 indentIncrement = newIndentIncrement;
		else
		{
			indentIncrement = 0;
			String errorNotice = "Invalid indentIncrement=" + indentIncrement + " provided to ConfigurationProperties";
//			validationResult.append(errorNotice).append("\n");
			throw new IllegalArgumentException(errorNotice);
		}
	}]]></xsl:text><xsl:text><![CDATA[
	/**
	 * Indicate whether X3D Canonical Form is used for toStringX3D() XML output.
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-3/V3.3/Part03/concepts.html#X3DCanonicalForm">X3D Compressed binary encoding, 4.2.3 X3D canonical form</a>
	 * @see <a href="https://www.w3.org/TR/xml-c14n">Canonical XML</a>
	 * @see <a href="https://www.w3.org/TR/exi-c14n">Canonical EXI</a>
	 * @see <a href="http://santuario.apache.org">Apache Santuario</a>
	 * @see <a href="http://www.web3d.org/x3d/tools/canonical/doc/x3dTools.htm">X3D Canonicalization (C14N)</a>
	 * @return whether X3D Canonical Form is used. */
	public static boolean isX3dCanonicalForm()
	{
		return ((indentIncrement == indentIncrement_DEFAULT) &&
			    (indentCharacter == indentCharacter_DEFAULT));
	}
	/**
	 * Ensure that X3D Canonical Form is used for XML output.
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-3/V3.3/Part03/concepts.html#X3DCanonicalForm">X3D Compressed binary encoding, 4.2.3 X3D canonical form</a>
	 * @see <a href="https://www.w3.org/TR/xml-c14n">Canonical XML</a>
	 * @see <a href="https://www.w3.org/TR/exi-c14n">Canonical EXI</a>
	 * @see <a href="http://santuario.apache.org">Apache Santuario</a>
	 * @see <a href="http://www.web3d.org/x3d/tools/canonical/doc/x3dTools.htm">X3D Canonicalization (C14N)</a>
	 */
	public static void setX3dCanonicalForm()
	{
		indentIncrement = indentIncrement_DEFAULT;
		indentCharacter = indentCharacter_DEFAULT;
	}
	/**
	 * Indicate whether default attributes (and their values) are shown when serializing scene output.
	 * @return whether default attributes are shown. */
	public static boolean isShowDefaultAttributes()
	{
		return showDefaultAttributes;
	}
	/**
	 * Set whether default attributes (and their values) are shown when serializing scene output.
	 * @param newShowDefaultAttributes whether default attributes are shown. */
	public static void setShowDefaultAttributes(boolean newShowDefaultAttributes)
	{
		showDefaultAttributes = newShowDefaultAttributes;
	}
]]></xsl:text>
		</xsl:with-param>
	</xsl:call-template>
	
	<xsl:call-template name="sourceFile">
		<xsl:with-param name="name"><xsl:text>X3DConcreteElement</xsl:text></xsl:with-param>
		<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="inConcretePackage"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="visibility"><xsl:text>public</xsl:text><!-- no modifier means package-private --></xsl:with-param>
		<xsl:with-param name="isAbstract"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
		<xsl:with-param name="subPackage"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="description"><xsl:text>Abstract parent class for concrete X3D nodes and statements, containing common methods and member variables.</xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="javadocBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="interfaceBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="implementationBlock">
			<xsl:text><![CDATA[
		
	/** Results of local validation */
	protected StringBuilder validationResult = new StringBuilder();
				
	/** Get output of results from prior validation, if any
	 * @return validation results
	 */		
	public String getValidationResult()
	{
		return validationResult.toString();
	}
				
	/**
	 * Recursive method to provide X3D string serialization of this model subgraph.
	 * @return X3D string
	 */
	public String toStringX3D()
	{
		return toStringX3D(0); // apply next method with initial indentation level 0
	}
	
	/**
	 * Recursive method to provide X3D string serialization of this model subgraph.
	 * @param level number of levels of indentation for this element
	 * @return X3D string
	 */
	abstract public String toStringX3D(int level); // must be overridden
				
	/**
	 * Recursive method to provide ClassicVRML string serialization.
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/grammar.html">Extensible 3D (X3D) encodings Part 2: Classic VRML encoding, Annex A: Grammar</a>
	 * @return ClassicVRML string
	 */
	public String toStringClassicVRML()
	{
		return toStringClassicVRML(0); // apply next method with initial indentation level 0
	}
				
	/**
	 * Recursive method to provide ClassicVRML string serialization.
	 * @param level number of levels of indentation for this element
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/grammar.html">Extensible 3D (X3D) encodings Part 2: Classic VRML encoding, Annex A: Grammar</a>
	 * @return ClassicVRML string
	 */
	abstract public String toStringClassicVRML(int level); // must be overridden
				
	/**
	 * Recursive method to provide VRML97 string serialization.
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772/V2.0/index.html">Virtual Reality Modeling Language (VRML) 97 specification</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772-1/V2.1/index.html">VRML 97 v2.1 Amendment</a>
	 * @return VRML97 string
	 */
	public String toStringVRML97()
	{
		return toStringVRML97(0); // apply next method with initial indentation level 0
	}
			
	/**
	 * Recursive method to provide VRML97 string serialization.
	 * @param level number of levels of indentation for this element
	 * @see <a href="http://www.web3d.org/x3d/content/examples/X3dResources.html#VRML">X3D Resources: Virtual Reality Modeling Language (VRML) 97</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772/V2.0/index.html">Virtual Reality Modeling Language (VRML) 97 specification</a>
	 * @see <a href="http://www.web3d.org/documents/specifications/14772-1/V2.1/index.html">VRML 97 v2.1 Amendment</a>
	 * @return VRML97 string
	 */	
	abstract public String toStringVRML97(int level); // must be overridden

	/**
	 * Recursive method to validate this element plus all contained nodes and statements.
	 * @return validation results
	 */
	abstract public String validate(); // must be overridden
]]></xsl:text>
		</xsl:with-param>
	</xsl:call-template>
	
	<xsl:call-template name="sourceFile">
		<xsl:with-param name="name"><xsl:text>X3DConcreteNode</xsl:text></xsl:with-param>
		<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="inConcretePackage"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="visibility"><xsl:text>public</xsl:text><!-- no modifier means package-private --></xsl:with-param>
		<xsl:with-param name="isAbstract"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
		<xsl:with-param name="subPackage"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="extends"><xsl:text>org.web3d.x3d.java.X3DConcreteElement</xsl:text></xsl:with-param>
		<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="description"><xsl:text>Abstract parent class for concrete X3D nodes, containing common methods and member variables.</xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="javadocBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="interfaceBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="implementationBlock">
			<!-- TODO include DEF_USE and global (class) attributeGroup entries in X3D Object Model -->
			<xsl:text><![CDATA[
	// Member value declarations are encapsulated and protected, using preferred Java types for concretes library

	private String DEF; // TODO javadoc, refactor class hierarchy to make private

	private String USE; // TODO javadoc, refactor class hierarchy to make private

	private String cssClass; // TODO javadoc, refactor class hierarchy to make private

	// String constants for default field values match X3D Schema definitions

	/** SFString field named <i>DEF</i> has default value equal to an empty string. */
	public static final String DEF_DEFAULT_VALUE = "";

	/** SFString field named <i>USE</i> has default value equal to an empty string. */
	public static final String USE_DEFAULT_VALUE = "";

	/** SFString field named <i>class</i> has default value equal to an empty string. */
	public static final String CLASS_DEFAULT_VALUE = "";
				
	/** Initialize all member variables to default values. */
	public void initialize()
	{
		setParentObject(null);
		     DEF = DEF_DEFAULT_VALUE;
		     USE = USE_DEFAULT_VALUE;
		cssClass = CLASS_DEFAULT_VALUE;
	}
	/**
	 * Provide String value from inputOutput SFString field named <i>DEF</i>.
	 * <i>Tooltip</i>. DEF defines a unique ID name for this node, referenceable by other nodes. Hint: descriptive DEF names improve clarity and
help document a model. Hint: well-defined names can simplify design and debugging through improved author understanding. http://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#NamingConventions.
	 * @return value of DEF field
	 */
	public String getDEF()
	{
		return DEF;
	}

	/**
	 * Provide String value from inputOutput SFString field named <i>USE</i>.
	 * <i>Tooltip</i>. USE means reuse an already DEF-ed node ID, excluding all child nodes and all other attributes (except for containerField,
which can have a different value). Hint: USE references to previously defined DEF geometry (instead of duplicating nodes)
can improve performance. Warning: do NOT include any child nodes, a DEF attribute, or any other attribute values (except for
containerField) when defining a USE attribute. Warning: each USE value must match a corresponding DEF value that is defined
earlier in the scene.
	 * @return value of USE field
	 */
	public String getUSE()
	{
		return USE;
	}
	/**
	 * Provide String value from inputOutput SFString field named <i>class</i>.
	 * <i>Tooltip</i>. The class attribute is a space-separated list of classes, reserved for use by CSS cascading stylesheets. The class attribute
is only supported in XML encoding of X3D scenes.
	 * @return value of class field
	 */
	public String getCssClass()
	{
		return cssClass;
	}
	
	/** Protected internal superclass method to keep DEF private, scene authors should use method setDEF(newValue) instead.
	 * @param newValue is new value for the DEF field.
	 */
	protected void setConcreteDEF(String newValue)
	{
		if (newValue == null)
			newValue = new String(); // Principle of Least Astonishment (POLA)
			// https://en.wikipedia.org/wiki/Principle_of_least_astonishment
				
		// Check that newValue parameter meets naming requirements before assigning to scene graph
		if (!newValue.isEmpty() && 
			!newValue.matches("[a-zA-Z_][a-zA-Z_0-9]*")) // NMTOKEN character regex check
		{
			throw new org.web3d.x3d.sai.InvalidFieldValueException(NAME + " DEF newValue=\"" + newValue +
					"\" has illegal value, must use a valid name string.");
		}
		DEF = newValue;
	}
	/** Protected internal superclass method to keep USE private, scene authors should use method setUse(newValue) instead.
	 * @param newValue is new value for the USE field.
	 */
	protected final void setConcreteUSE(String newValue)
	{
		if (newValue == null)
			newValue = new String(); // Principle of Least Astonishment (POLA)
			https://en.wikipedia.org/wiki/Principle_of_least_astonishment
				
		// Check that newValue parameter meets naming requirements before assigning to scene graph
		if (!newValue.isEmpty() &&
			!newValue.matches("[a-zA-Z_][a-zA-Z_0-9]*")) // NMTOKEN character regex check
		{
			throw new org.web3d.x3d.sai.InvalidFieldValueException(NAME + " USE newValue=\"" + newValue +
					"\" has illegal value, must use a valid name string.");
		}
		USE = newValue;
	}
	/** Protected internal superclass method to keep cssClass private, scene authors should use method setCssClass(newValue) instead.
	 * @param newValue is new value for the cssClass field.
	 */
	protected void setConcreteCssClass(String newValue)
	{
		if (newValue == null)
			newValue = new String(); // Principle of Least Astonishment (POLA)
		cssClass = newValue;
	}
	/** Each concrete class must independently override this abstract method to enable object-specific method pipelining.
	 * @param DEFname is new value for the DEF field.
	 * @return {@link X3DConcreteNode} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations). */
	abstract public X3DConcreteNode setDEF(String DEFname);

	/** Each concrete class must independently override this abstract method to enable object-specific method pipelining.
	 * @param USEname is new value for the USE field.
	 * @return {@link X3DConcreteNode} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations). */
	abstract public X3DConcreteNode setUSE(String USEname);

	/** Each concrete class must independently override this abstract method to enable object-specific method pipelining.
	 * @param cssClass is new value for the class field.
	 * @return {@link X3DConcreteNode} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations). */
	abstract public X3DConcreteNode setCssClass(String cssClass);
]]></xsl:text>
		</xsl:with-param>
	</xsl:call-template>
	
	<xsl:call-template name="sourceFile">
		<xsl:with-param name="name"><xsl:text>X3DConcreteStatement</xsl:text></xsl:with-param>
		<xsl:with-param name="imports"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="inConcretePackage"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="visibility"><xsl:text>public</xsl:text><!-- no modifier means package-private --></xsl:with-param>
		<xsl:with-param name="isAbstract"><xsl:text>true</xsl:text></xsl:with-param>
		<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
		<xsl:with-param name="subPackage"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="extends"><xsl:text>org.web3d.x3d.java.X3DConcreteElement</xsl:text></xsl:with-param>
		<xsl:with-param name="implements"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="description"><xsl:text>Abstract parent class for concrete X3D statements, containing common methods and member variables.</xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="javadocBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="interfaceBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="implementationBlock">
			<xsl:text><![CDATA[
	/** Initialize all member variables to default values. */
	public void initialize()
	{
		setParentObject(null);
	}]]></xsl:text>
		</xsl:with-param>
	</xsl:call-template>
	
	<xsl:call-template name="sourceFile">
		<xsl:with-param name="name"><xsl:text>CommentsBlock</xsl:text></xsl:with-param>
		<xsl:with-param name="imports">
			<xsl:text>
import org.web3d.x3d.sai.Core.X3DMetadataObject; // making sure CommentsBlock
import org.web3d.x3d.java.*;</xsl:text>
		</xsl:with-param>
		<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
		<xsl:with-param name="subPackage"><xsl:text>Core</xsl:text></xsl:with-param>
		<xsl:with-param name="extends"><xsl:text>org.web3d.x3d.java.X3DConcreteStatement</xsl:text></xsl:with-param>
		<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.Core.X3DChildNode</xsl:text></xsl:with-param>
		<xsl:with-param name="description"><xsl:text>Utility class to enable adding one or more comment strings as a child node, treated as an X3D statement.</xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
		<xsl:with-param name="javadocBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="interfaceBlock">
			<xsl:text><![CDATA[]]></xsl:text>
		</xsl:with-param>
		<xsl:with-param name="implementationBlock">
			<xsl:text disable-output-escaping="yes"><![CDATA[
	/** String constant <i>NAME</i> provides name of this element. */
	@SuppressWarnings("FieldNameHidesFieldInSuperclass")
	protected static final String NAME = "CommentsBlock";

	/** Provides name of this element: CommentsBlock.
	 * @return name of this element
	 */
	@Override
	public final String getElementName()
	{
		return NAME;
	}
				
	/** public constructor for CommentsBlock. */
	public CommentsBlock()
	{
	  initialize();
	};

	/** public constructor for CommentsBlock to initialize with initial comment.
	 * @param newComment initial comment
	 */
	public CommentsBlock(String newComment)
	{
		initialize();
		commentsList.add(newComment);
	};

	/** public constructor for CommentsBlock to initialize with initial comments array.
	 * @param newComments[] initial comments
	 */
	public CommentsBlock(String newComments[])
	{
		initialize();
		if ((newComments != null) && (newComments.length > 0))
			commentsList.addAll(Arrays.asList(newComments));
	};
				
	/** public constructor for CommentsBlock to initialize with initial comments list.
	 * @param newCommentsList initial comments
	 */
	public CommentsBlock(ArrayList<String> newCommentsList)
	{
		initialize();
		commentsList.addAll(newCommentsList);
	};

	/**
	 * Add comment to CommentsBlock
	 * @param newComment initial value
	 * @return {@link CommentsBlock} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public CommentsBlock addComments(String newComment)
	{
		commentsList.add(newComment);
		return this;
	}
	/**
	 * Add comments array as CommentsBlock to children field
	 * @param newComments array of comments
	 * @return {@link CommentsBlock} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public CommentsBlock addComments(String[] newComments)
	{
		commentsList.addAll(Arrays.asList(newComments));
		return this;
	}
	/**
	 * Add comments array as CommentsBlock to children field
	 * @param newCommentsList list of comments
	 * @return {@link CommentsBlock} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public CommentsBlock addComments(ArrayList<String> newCommentsList)
	{
		commentsList.addAll(newCommentsList);
		return this;
	}
	/**
	 * Add CommentsBlock to children field
	 * @param newCommentsBlock block of comments to add
	 * @return {@link CommentsBlock} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public CommentsBlock addComments(CommentsBlock newCommentsBlock)
	{
		commentsList.addAll(Arrays.asList(newCommentsBlock.toStrings()));
		return this;
	}
	
	/**
	 * Provide CommentsBlock as string array
	 * @return all comments
	 */
	public String[] toStrings()
	{
		return (String[]) commentsList.toArray();
	}
	
	/**
	 * Provide CommentsBlock as ArrayList of string(s)
	 * @return all comments
	 */
	public ArrayList<String> toStringList()
	{
		return commentsList;
	}
				
	/** Initialize this CommentsBlock instance. */
	@Override
	public final void initialize()
	{
		super.initialize();
		commentsList = new ArrayList<>(); // reset
	}
	/** Clear all comments from this CommentsBlock.
	 * @return {@link CommentsBlock} - namely <i>this</i> same object to allow sequential method pipelining (i.e. consecutive setAttribute method invocations).
	 */
	public CommentsBlock clear()
	{
		initialize();
		return this;
	}
]]></xsl:text>
			
		</xsl:with-param>
	</xsl:call-template>
	
    <!-- ===================================================== -->
	
		<xsl:call-template name="sourceFile">
			<xsl:with-param name="name"><xsl:text>X3DConcreteFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="isInterface"><xsl:text>false</xsl:text></xsl:with-param>
			<xsl:with-param name="subPackage"><xsl:text>fields</xsl:text></xsl:with-param>
			<xsl:with-param name="extends"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implements"><xsl:text>org.web3d.x3d.sai.X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="imports"><xsl:text>import org.web3d.x3d.sai.X3DFieldEvent;</xsl:text></xsl:with-param>
			<xsl:with-param name="description"><xsl:text>Listener for events passing values from one X3D field to another.</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationSection"><xsl:text>B.4.3 X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="saiJavaSpecificationRelativeUrl"><xsl:text>types.html#X3DFieldEventListener</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationSection"><xsl:text>6.3.20 registerBrowserInterest</xsl:text></xsl:with-param>
			<xsl:with-param name="saiAbstractSpecificationRelativeUrl"><xsl:text>servRef.html#RegisterBrowserInterest</xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationSection"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="x3dAbstractSpecificationRelativeUrl"><xsl:text></xsl:text></xsl:with-param>
			<xsl:with-param name="implementationBlock">
				<xsl:text><![CDATA[
	@Override
	public void readableFieldChanged(X3DFieldEvent event)
	{
		// TODO;
	}
]]></xsl:text>
			</xsl:with-param>
		</xsl:call-template>
	
    </xsl:template> <!-- end of ConcreteNodeObjectDefinitions -->
	
    <!-- ===================================================== -->
	
<xsl:template name="set-newValue-validity-checks">
    <xsl:param name="canThrowFieldValueException"><xsl:text></xsl:text></xsl:param>
    <xsl:param name="isArrayType"><xsl:text></xsl:text></xsl:param>
    <xsl:param name="isArrayListType"><xsl:text></xsl:text></xsl:param>
    <xsl:param name="x3dType"><xsl:text></xsl:text></xsl:param>
    <xsl:param name="javaReferenceType"><xsl:text></xsl:text></xsl:param>
    <xsl:param name="comparisonType"><xsl:text></xsl:text></xsl:param>
	
	<!-- TODO regular expression checks -->
	
	<xsl:variable name="tupleSize">
		<xsl:call-template name="tupleSize">
			<xsl:with-param name="x3dType" select="@type"/>
		</xsl:call-template>
	</xsl:variable>
	<xsl:variable name="javaType">
		<!-- can include collections, must be escaped -->
		<xsl:call-template name="javaType">
			<xsl:with-param name="x3dType" select="@type"/>
		</xsl:call-template>
	</xsl:variable>

	<!-- debug diagnostic
	<xsl:message>	
		<xsl:text>set-newValue-validity-checks: name=</xsl:text>
		<xsl:value-of select="@name"/>
		<xsl:text>, type=</xsl:text>
		<xsl:value-of select="@type"/>
		<xsl:text>, isArrayType=</xsl:text>
		<xsl:value-of select="$isArrayType"/>
		<xsl:text>, isArrayListType=</xsl:text>
		<xsl:value-of select="$isArrayListType"/>
		<xsl:text>, baseType=</xsl:text>
		<xsl:value-of select="@baseType"/>
		<xsl:text>, javaReferenceType=</xsl:text>
		<xsl:value-of select="$javaReferenceType"/>
		<xsl:text>, comparisonType=</xsl:text>
		<xsl:value-of select="$comparisonType"/>
		<xsl:text>, tupleSize=</xsl:text>
		<xsl:value-of select="$tupleSize"/>
	</xsl:message>
	-->
	
	<xsl:choose>
		<xsl:when test="($isArrayType='true')">
			<xsl:text>  int i = 0;</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>  for (</xsl:text>
			<xsl:value-of select="$javaReferenceType"/>
			<xsl:text> arrayElement : </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:when>
		<xsl:when test="($isArrayListType = 'true')">
		</xsl:when>
	</xsl:choose>
	<xsl:variable name="newValueReference">
		<xsl:choose>
			<xsl:when test="($isArrayType='true')">
				<xsl:value-of select="$newValue"/>
				<xsl:text>[i]</xsl:text>
			</xsl:when>
			<xsl:when test="($isArrayListType = 'true')">
				<xsl:value-of select="$newValue"/>
				<xsl:text>[i]</xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$newValue"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:variable>
	<xsl:variable name="dimensionSuffix">
		<xsl:choose>
			<xsl:when test="(@baseType = 'boundingBoxSizeType')">
				<xsl:text>.length</xsl:text>
			</xsl:when>
			<xsl:when test="(($isArrayListType = 'true') and ($comparisonType = 'complex'))">
				<xsl:text>.size()</xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<xsl:text>.length</xsl:text>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:variable>
	
	<!-- TODO modulus checks for MF types -->
	<xsl:choose>
		<xsl:when test="(($isArrayType = 'false') or ($isArrayListType = 'true')) and (number($tupleSize) > 1)">
			<xsl:text>		if (newValue == null)
			newValue = new </xsl:text>
		<xsl:value-of select="substring-before($javaType,'[]')"/>
		<xsl:text>[0];
		// Check that newValue parameter has legal size before assigning to scene graph</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		if (newValue</xsl:text>
			<xsl:value-of select="$dimensionSuffix"/>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'SF')">
					<xsl:text> != </xsl:text>
					<xsl:value-of select="$tupleSize"/>
					<xsl:text>) // </xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes">-tuple check
		{</xsl:text>
				</xsl:when>
				<xsl:otherwise><!-- MF type -->
					<xsl:text> % </xsl:text>
					<xsl:value-of select="$tupleSize"/>
					<xsl:text> != 0) // </xsl:text>
				<xsl:value-of select="$tupleSize"/>
				<xsl:text disable-output-escaping="yes">-tuple check
		{</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="contains($dimensionSuffix, 'size')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
					<xsl:text> + "</xsl:text>
					<xsl:text> has size=" + </xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:value-of select="$dimensionSuffix"/>
					<xsl:text> + "</xsl:text>
					<xsl:choose>
						<xsl:when test="starts-with(@type,'SF')">
							<xsl:text> instead of required length </xsl:text>
							<xsl:value-of select="$tupleSize"/>
						</xsl:when>
						<xsl:otherwise><!-- MF type -->
							<xsl:text>, must be a multiple of </xsl:text>
							<xsl:value-of select="$tupleSize"/>
						</xsl:otherwise>
					</xsl:choose>					
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$x3dType"/>
					<xsl:value-of select="$jsaiClassSuffix"/>
					<xsl:text>.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>) + "</xsl:text>
					<xsl:text> has length=" + </xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:value-of select="$dimensionSuffix"/>
					<xsl:text> + "</xsl:text>
					<xsl:choose>
						<xsl:when test="starts-with(@type,'SF')">
							<xsl:text> instead of required length </xsl:text>
							<xsl:value-of select="$tupleSize"/>
						</xsl:when>
						<xsl:otherwise><!-- MF type -->
							<xsl:text>, must be a multiple of </xsl:text>
							<xsl:value-of select="$tupleSize"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		}</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:when>
	</xsl:choose>
	<xsl:choose>
		<xsl:when test="not($isArrayType = 'true')">
			<xsl:if test="($canThrowFieldValueException) and 
                  ((@type='SFInt32') or (@type='SFFloat') or (@type='SFDouble') or
                   (@type='SFVec2f') or (@type='SFVec2d') or (@type='SFVec3f')  or (@type='SFVec3d') or
                   (@type='SFVec4f') or (@type='SFVec4d') or (@baseType='boundingBoxSizeType') or
                   (((@type='SFString') or (@type='MFString')) and (enumeration) and not(@additionalEnumerationValuesAllowed='true')))">
				
		<xsl:if test="(string-length(@minExclusive) > 0) or (string-length(@minInclusive) > 0) or (string-length(@maxExclusive) > 0) or (string-length(@maxInclusive) > 0)">
			<xsl:text>  </xsl:text>
			<xsl:text>// Check that newValue parameter has legal value(s) before assigning to scene graph</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="(string-length(@minExclusive) > 0)">
			<xsl:text>  </xsl:text>
			<xsl:text>if (</xsl:text>
			<xsl:choose>
				<xsl:when test="(@type='SFInt32') or (@type='SFFloat') or (@type='SFDouble')">
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes"> &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
				</xsl:when>
				<xsl:when test="(@type='SFVec2f') or (@type='SFVec2d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec3f') or (@type='SFVec3d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec4f') or (@type='SFVec4d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[3] &lt;= </xsl:text>
					<xsl:value-of select="@minExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:message><xsl:text>*** set-newValue-validity-checks code-generation error</xsl:text></xsl:message>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>    throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'MF')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$newValue"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "</xsl:text>
			<xsl:text> is less than (or equal to) restriction minExclusive=</xsl:text>
			<xsl:value-of select="@minExclusive"/>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>  }</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="(string-length(@minInclusive) > 0)">
			<xsl:text>  </xsl:text>
			<xsl:text>if (</xsl:text>
			<xsl:choose>
				<xsl:when test="(@type='SFInt32') or (@type='SFFloat') or (@type='SFDouble')">
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes"> &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
				</xsl:when>
				<xsl:when test="(@type='SFVec2f') or (@type='SFVec2d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec3f') or (@type='SFVec3d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec4f') or (@type='SFVec4d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[3] &lt; </xsl:text>
					<xsl:value-of select="@minInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
			</xsl:choose>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>    throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'MF')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$newValue"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "</xsl:text>
			<xsl:text> is less than restriction minInclusive=</xsl:text>
			<xsl:value-of select="@minInclusive"/>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>  }</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="(string-length(@maxExclusive) > 0)">
			<xsl:text>  </xsl:text>
			<xsl:text>if (</xsl:text>
			<xsl:choose>
				<xsl:when test="(@type='SFInt32') or (@type='SFFloat') or (@type='SFDouble')">
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes"> &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
				</xsl:when>
				<xsl:when test="(@type='SFVec2f') or (@type='SFVec2d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec3f') or (@type='SFVec3d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec4f') or (@type='SFVec4d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[3] &gt;= </xsl:text>
					<xsl:value-of select="@maxExclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
			</xsl:choose>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>    throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'MF')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$x3dType"/>
					<xsl:value-of select="$jsaiClassSuffix"/>
					<xsl:text>.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "</xsl:text>
			<xsl:text> is greater than (or equal to) restriction maxExclusive=</xsl:text>
			<xsl:value-of select="@maxExclusive"/>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>  }</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="(string-length(@maxInclusive) > 0)">
			<xsl:text>  </xsl:text>
			<xsl:text>if (</xsl:text>
			<xsl:choose>
				<xsl:when test="(@type='SFInt32') or (@type='SFFloat') or (@type='SFDouble')">
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes"> &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
				</xsl:when>
				<xsl:when test="(@type='SFVec2f') or (@type='SFVec2d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec3f') or (@type='SFVec3d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:when test="(@type='SFVec4f') or (@type='SFVec4d')">
					<xsl:text>(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[0] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[1] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[2] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>) || (</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text disable-output-escaping="yes">[4] &gt; </xsl:text>
					<xsl:value-of select="@maxInclusive"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
			</xsl:choose>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>    throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'MF')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$x3dType"/>
					<xsl:value-of select="$jsaiClassSuffix"/>
					<xsl:text>.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "</xsl:text>
			<xsl:text> is greater than (or equal to) restriction maxInclusive</xsl:text>
			<xsl:value-of select="@maxInclusive"/>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>  }</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="(@baseType='boundingBoxSizeType')">
			<xsl:text>		// Check legal value for bounding box bboxSize</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		</xsl:text>
			<xsl:text>if (</xsl:text>
			<xsl:text>(</xsl:text>
			<xsl:text>(</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[0] &lt; 0) || (</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[1] &lt; 0) || (</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[2] &lt; 0)</xsl:text>
			<xsl:text disable-output-escaping="yes">) &amp;&amp; !((</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[0] == -1) &amp;&amp; (</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[1] == -1) &amp;&amp; (</xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text disable-output-escaping="yes">[2] == -1))</xsl:text>
			<xsl:text>) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=" + </xsl:text>
			<xsl:choose>
				<xsl:when test="starts-with(@type,'MF')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$x3dType"/>
					<xsl:value-of select="$jsaiClassSuffix"/>
					<xsl:text>.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "</xsl:text>
			<xsl:text> has negative value but is not equal to sentinel {-1,-1,-1} value.</xsl:text>
			<xsl:value-of select="@maxInclusive"/>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		}</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
		<xsl:if test="((@type='SFString') or (@type='MFString'))"><!-- TODO are there any other types with restricted values? -->
			<xsl:choose>
				<xsl:when test="(@type='SFString')">
					<xsl:text>		if (</xsl:text><xsl:value-of select="$newValue"/><xsl:text> == null)
					</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text> = new String(); // null string check</xsl:text>
				</xsl:when>
				<!-- TODO multiple methods? works for String but not ArrayList<String>
				<xsl:when test="(@type='MFString')">
					<xsl:text>String[0]</xsl:text>
				</xsl:when>
				-->
			</xsl:choose>
			<xsl:text>
		// Check that newValue parameter has one of the allowed legal values before assigning to scene graph</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		</xsl:text>
			<xsl:text>if (!(</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:for-each select="enumeration">
				<xsl:if test="position() > 1">
					<xsl:text> ||</xsl:text>
					<xsl:text>&#10;</xsl:text>
				</xsl:if>
				<xsl:text>			</xsl:text>
				<xsl:choose>
					<xsl:when test="($isArrayListType = 'true') and ($comparisonType = 'simple')">
						<xsl:text>Arrays.asList(</xsl:text>
						<xsl:value-of select="$newValue"/>
						<xsl:text>)</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="$newValue"/>
					</xsl:otherwise>
				</xsl:choose>
				<xsl:text>.equals(</xsl:text>
				<xsl:value-of select="upper-case(../@name)"/>
				<xsl:text>_</xsl:text>
				<!-- enumeration name: omit " character, others become _ underscore -->
				<xsl:value-of select="upper-case(translate(@value,' .-&quot;','___'))"/>
				<xsl:text>)</xsl:text>
			</xsl:for-each>
			<xsl:text>)) {</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
			<xsl:text>("</xsl:text>
			<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="@name"/>
			<xsl:text> </xsl:text>
			<xsl:value-of select="$newValue"/>
			<xsl:text>=\"" + </xsl:text>
			<xsl:choose>
				<xsl:when test="($isArrayListType = 'true') and ($comparisonType = 'simple')">
					<xsl:text> Arrays.toString(</xsl:text>
					<xsl:value-of select="$newValue"/>
					<xsl:text>)</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="$newValue"/>
				</xsl:otherwise>
			</xsl:choose>
			<xsl:text> + "\"</xsl:text>
			<xsl:text> has illegal value, must use a valid enumeration string.</xsl:text>
			<xsl:text>");</xsl:text>
			<xsl:text>&#10;</xsl:text>
			<xsl:text>		}</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:if>
	</xsl:if>
		</xsl:when>
		<xsl:otherwise>
			<!-- TODO ArrayList comparisons -->
		</xsl:otherwise>
	</xsl:choose>
	<xsl:if test="(@name = 'name')"><!-- required -->
		<xsl:text>		// Check that newValue parameter meets naming requirements before assigning to scene graph</xsl:text>
		<xsl:text>
		if (</xsl:text><xsl:value-of select="$newValue"/><xsl:text> == null) </xsl:text><xsl:value-of select="$newValue"/><xsl:text> = new String();
		if  (newValue.isEmpty() || 
			!newValue.matches("[a-zA-Z_][a-zA-Z_0-9]*")) // NMTOKEN character regex check</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>		{</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>			throw new org.web3d.x3d.sai.InvalidFieldValueException</xsl:text>
		<xsl:text>("</xsl:text>
		<xsl:value-of select="ancestor::*[string-length(@name) > 0]/@name"/>
		<xsl:text> </xsl:text>
		<xsl:value-of select="@name"/>
		<xsl:text> </xsl:text>
		<xsl:value-of select="$newValue"/>
		<xsl:text>=\"" + </xsl:text>
		<xsl:choose>
			<xsl:when test="($isArrayListType = 'true') and ($comparisonType = 'simple')">
				<xsl:text> Arrays.toString(</xsl:text>
				<xsl:value-of select="$newValue"/>
				<xsl:text>)</xsl:text>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$newValue"/>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:text> + "\"</xsl:text>
		<xsl:text> has illegal value, must use a valid name string.</xsl:text>
		<xsl:text>");</xsl:text>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>		}</xsl:text>
		<xsl:text>&#10;</xsl:text>
	</xsl:if>
	<xsl:choose>
		<xsl:when test="($isArrayType='true')">
			<xsl:text>	}</xsl:text>
			<xsl:text>&#10;</xsl:text>
		</xsl:when>
		<xsl:when test="($isArrayListType = 'true')">
		</xsl:when>
	</xsl:choose>
</xsl:template>
	
    <!-- ===================================================== -->
	
<!-- from BuildSpecificationLanguageBindingJava.xslt adapted for X3D Object Model-->
<xsl:template name="list-restrictions">
    <xsl:variable name="originalType" select="@type"/>
    <xsl:variable name="isEnumerationType" select="(count(enumeration) > 0)"/>
    <xsl:variable name="enumerationValues">
		<xsl:if test="enumeration">
			<xsl:text>[</xsl:text>
			<xsl:for-each select="enumeration">
				<xsl:text>'</xsl:text><!-- MFString enumeration values are quoted -->
				<xsl:value-of select="@value"/>
				<xsl:text>'</xsl:text>
				<xsl:if test="not(position() = last())">
					<xsl:text>|</xsl:text>
				</xsl:if>
			</xsl:for-each>
			<xsl:if test="(@additionalEnumerationValuesAllowed='true')">
				<xsl:choose>
					<xsl:when test="(@type='SFString')">
						<xsl:text>|'etc.'</xsl:text>
					</xsl:when>
					<xsl:when test="(@type='MFString')">
						<xsl:text>|'"etc."'</xsl:text>
					</xsl:when>
				</xsl:choose>
			</xsl:if>
			<xsl:text>]</xsl:text>
		</xsl:if>
    </xsl:variable>
    <xsl:choose>
        <xsl:when test="(@type='SFBool') or (@type='MFBool') or (@type='featurePointNames') or (@type='jointNames') or (@type='segmentNames') or (@type='siteNames')">
            <!-- no restriction-->
        </xsl:when>
        <xsl:when test="(@name = 'bboxSize')">
            <xsl:text>within allowed range of </xsl:text>
            <xsl:text>[0,infinity), or default value [-1 -1 -1], </xsl:text>
        </xsl:when>
        <xsl:when test="contains(@type,'RGBA')">
            <xsl:text>using RGBA values [0..1] </xsl:text>
        </xsl:when>
        <xsl:when test="contains(@type,'Color') or contains(@name,'Color') or contains(@name,'color')">
            <xsl:text>using RGB values [0..1] </xsl:text>
        </xsl:when>
        <xsl:when test="(@name = 'objectType')">
            <xsl:text>with quoted value(s) </xsl:text>
            <xsl:text>["ALL","NONE","TERRAIN",...] </xsl:text>
        </xsl:when>
        <xsl:when test="(@name = 'type') and (ancestor::*[@name='NavigationInfo'])">
            <xsl:text>with quoted value(s) </xsl:text>
            <xsl:text>["ANY","WALK","EXAMINE","FLY","LOOKAT","NONE","EXPLORE",...] </xsl:text>
        </xsl:when>
        <xsl:when test="(@name = 'transitionType') and (ancestor::*[@name='NavigationInfo'])">
            <xsl:text>with quoted value(s) </xsl:text>
            <xsl:text>["TELEPORT","LINEAR","ANIMATE",...] </xsl:text>
        </xsl:when>
        <xsl:when test="(@name = 'GeoOrigin') or (@name = 'geoOrigin')">
            <!-- http://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/deprecation/deprecation.html -->
            <xsl:text>(deprecated node, optional) </xsl:text>
        </xsl:when>
        <xsl:when test="((@type='SFString') or (@type='MFString')) and (string-length(xs:annotation/xs:documentation) > 0)">
            <xsl:value-of select="normalize-space(xs:annotation/xs:documentation)"/>
            <xsl:text> </xsl:text>
        </xsl:when>
        <xsl:when test="(string-length($enumerationValues) > 0)">
            <xsl:value-of select="$enumerationValues"/>
            <xsl:text> </xsl:text>
        </xsl:when>
        <xsl:when test="((@type='SFString') or (@type='MFString')) and (string-length(xs:simpleType/xs:restriction/@base) > 0)">
            <xsl:value-of select="xs:simpleType/xs:restriction/@base"/>
            <xsl:text> </xsl:text>
        </xsl:when>
        <xsl:when test="(@type='SFString') or (@type='MFString')">
            <!-- no restriction-->
        </xsl:when>
        <xsl:when test="(string-length(@minInclusive) > 0) or (string-length(@minExclusive) > 0) or (string-length(@maxInclusive) > 0) or (string-length(@maxExclusive) > 0)">
            <xsl:text>within allowed range of </xsl:text>
            <xsl:choose>
                <xsl:when test="(string-length(@minInclusive) > 0)">
                    <xsl:text>[</xsl:text>
                    <xsl:value-of select="@minInclusive"/>
                </xsl:when>
                <xsl:when test="(string-length(@minExclusive) > 0)">
                    <xsl:text>(</xsl:text>
                    <xsl:value-of select="@minExclusive"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>(-infinity</xsl:text> <!-- &#8734; &infin; infinity symbol -->
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text>,</xsl:text>
            <xsl:choose>
                <xsl:when test="(string-length(@maxInclusive) > 0)">
                    <xsl:value-of select="@maxInclusive"/>
                    <xsl:text>]</xsl:text>
                </xsl:when>
                <xsl:when test="(string-length(@maxExclusive) > 0)">
                    <xsl:value-of select="@maxExclusive"/>
                    <xsl:text>)</xsl:text>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>infinity)</xsl:text> <!-- &#8734; &infin; infinity symbol -->
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text> </xsl:text>
        </xsl:when>
        <!-- retrieve range for specially defined simpleTypes, e.g. intensityType -->
        <xsl:when test="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction">
			<xsl:text>within allowed range of </xsl:text>
            <xsl:choose>
                <xsl:when test="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:minInclusive">
                    <xsl:text>[</xsl:text>
                    <xsl:value-of select="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:minInclusive/@value"/>
                </xsl:when>
                <xsl:when test="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:minExclusive">
                    <xsl:text>(</xsl:text>
                    <xsl:value-of select="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:minExclusive/@value"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>(-infinity</xsl:text> <!-- &infin; infinity symbol -->
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text>,</xsl:text>
            <xsl:choose>
                <xsl:when test="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:maxInclusive">
                    <xsl:value-of select="/xs:schema/maxInclusive/@value"/>
                    <xsl:text>]</xsl:text>
                </xsl:when>
                <xsl:when test="/xs:schema/xs:simpleType[@name=$originalType]/xs:restriction/xs:maxExclusive">
                    <xsl:value-of select="/xs:schema/maxExclusive/@value"/>
                    <xsl:text>)</xsl:text>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>infinity)</xsl:text> <!-- &infin; infinity symbol -->
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text> </xsl:text>
        </xsl:when>
    </xsl:choose>
</xsl:template>

<!-- from BuildSpecificationLanguageBindingJava.xslt -->

<xsl:template name="escape-quotes-recurse">
  <xsl:param name="inputString"><xsl:text></xsl:text></xsl:param>
  <xsl:param name="indent"><xsl:text></xsl:text></xsl:param>
  <xsl:choose>
    <xsl:when test="not(contains($inputString,'&quot;'))">
      <xsl:value-of select="$inputString"/>
    </xsl:when>
    <!-- has quote, or has quote before \" -->
    <xsl:when test="not(contains($inputString,'\&quot;')) or (string-length(substring-before($inputString,'&quot;')) &lt; string-length(substring-before($inputString,'\&quot;')))">
      <xsl:value-of select="substring-before($inputString,'&quot;')"/>
      <xsl:text>\&quot;</xsl:text>
      <xsl:call-template name="escape-quotes-recurse">
        <xsl:with-param name="inputString" select="substring-after($inputString,'&quot;')"/>
      </xsl:call-template>
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="substring-before($inputString,'\&quot;')"/>
      <xsl:text>\&quot;</xsl:text>
      <xsl:call-template name="escape-quotes-recurse">
        <xsl:with-param name="inputString" select="substring-after($inputString,'\&quot;')"/>
      </xsl:call-template>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<xsl:template name="append-f-to-float-values-recurse">
  <xsl:param name="inputString"><xsl:text></xsl:text></xsl:param>
  <xsl:param name="indent"><xsl:text></xsl:text></xsl:param>
  <xsl:choose>
    <xsl:when test="not(string-length(normalize-space($inputString)) > 0)">
      <!-- empty value -->
    </xsl:when>
      <!-- singleton value -->
    <xsl:when test="not(contains($inputString,' ')) and not(contains($inputString,','))">
      <xsl:value-of select="$inputString"/>
      <xsl:text>f</xsl:text>
    </xsl:when>
    <!-- space, or space precedes comma (if comma is present) -->
    <xsl:when test="contains($inputString,' ') and 
                   (not(contains($inputString,',')) or 
                       (string-length(substring-before($inputString,',')) > string-length(substring-before($inputString,' '))))">
     <xsl:value-of select="substring-before($inputString,' ')"/>
      <xsl:text>f,</xsl:text>
      <xsl:call-template name="append-f-to-float-values-recurse">
        <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,' '))"/>
      </xsl:call-template>
    </xsl:when>
    <!-- comma precedes space -->
    <xsl:otherwise>
      <xsl:value-of select="substring-before($inputString,',')"/>
      <xsl:text>f,</xsl:text>
      <xsl:call-template name="append-f-to-float-values-recurse">
        <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,','))"/>
      </xsl:call-template>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<xsl:template name="append-zero-to-double-values-recurse">
  <!-- boxing of generics requires that double values be in double form, e.g. 0.0 vice 0 -->
  <xsl:param name="inputString"><xsl:text></xsl:text></xsl:param>
  <xsl:param name="indent"><xsl:text></xsl:text></xsl:param>
  <xsl:choose>
    <xsl:when test="not(string-length(normalize-space($inputString)) > 0)">
      <!-- empty value -->
    </xsl:when>
      <!-- singleton value -->
    <xsl:when test="not(contains($inputString,' ')) and not(contains($inputString,','))">
      <xsl:value-of select="$inputString"/>
	  <xsl:if test="not(contains($inputString,'.'))">
		  <xsl:text>.0</xsl:text>
	  </xsl:if>
    </xsl:when>
    <!-- space, or space precedes comma (if comma is present) -->
    <xsl:when test="contains($inputString,' ') and 
                   (not(contains($inputString,',')) or 
                       (string-length(substring-before($inputString,',')) > string-length(substring-before($inputString,' '))))">
      <xsl:variable name="element">
		  <xsl:value-of select="substring-before($inputString,' ')"/>
	  </xsl:variable>
	  <xsl:value-of select="$element"/>
	  <xsl:if test="not(contains($element,'.'))">
		  <xsl:text>.0</xsl:text>
	  </xsl:if>
	  <xsl:text>,</xsl:text>
      <xsl:call-template name="append-zero-to-double-values-recurse">
        <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,' '))"/>
      </xsl:call-template>
    </xsl:when>
    <!-- comma precedes space -->
    <xsl:otherwise>
      <xsl:variable name="element">
		  <xsl:value-of select="substring-before($inputString,',')"/>
	  </xsl:variable>
	  <xsl:value-of select="$element"/>
	  <xsl:if test="not(contains($element,'.'))">
		  <xsl:text>.0</xsl:text>
	  </xsl:if>
	  <xsl:text>,</xsl:text>
      <xsl:call-template name="append-zero-to-double-values-recurse">
        <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,','))"/>
      </xsl:call-template>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<xsl:template name="insert-javadoc-line-breaks-recurse">
  <!-- boxing of generics requires that double values be in double form, e.g. 0.0 vice 0 -->
  <xsl:param name="inputString"><xsl:text></xsl:text></xsl:param>
  <xsl:param name="breakText1"><xsl:text></xsl:text></xsl:param>
  <xsl:param name="breakText2"><xsl:text></xsl:text></xsl:param>
  <xsl:choose>
    <xsl:when test="not(string-length(normalize-space($inputString)) > 0)">
      <!-- empty string -->
    </xsl:when>
    <xsl:when test="not(string-length(normalize-space($breakText1)) > 0)">
      <!-- no breakText1 to break on -->
      <xsl:value-of select="$inputString"/>
    </xsl:when>
    <xsl:when test="not(string-length(normalize-space($breakText2)) > 0)">
      <!-- no breakText2 to break on -->
      <xsl:value-of select="$inputString"/>
    </xsl:when>
    <xsl:when test="not(contains($inputString,$breakText1)) and not(contains($inputString,$breakText2))">
      <!-- no breakText found so all done -->
      <xsl:value-of select="$inputString"/>
    </xsl:when>
    <xsl:when test="starts-with(normalize-space($inputString),$breakText1)">
		<!-- starts with Hint: -->
		<!-- insert javadoc line break -->
		<xsl:text>&#10;</xsl:text>
		<xsl:text> * </xsl:text>	
		<xsl:text disable-output-escaping="yes"> &lt;li&gt; </xsl:text>
		<!-- skip initial Hint: or Warning: and determine what is next -->
		<xsl:variable name="preambleHint"    select="normalize-space(substring-before(substring-after($inputString,$breakText1),'Hint:'))"/>
		<xsl:variable name="preambleWarning" select="normalize-space(substring-before(substring-after($inputString,$breakText1),'Warning:'))"/>
		<xsl:choose>
			<xsl:when test="(string-length($preambleHint) = 0) and (string-length($preambleWarning) = 0)">
				<!-- this is last substring, no preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="substring-before($inputString,':')"/>
				<xsl:text disable-output-escaping="yes">:&lt;/i&gt; </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="substring-after($inputString,':')"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
			</xsl:when>
			<xsl:when test="(string-length($preambleHint) > 0) and 
							 ((string-length($preambleWarning) = 0) or (string-length($preambleWarning) > string-length($preambleHint)))">
				<!-- Hint next follows this preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="$breakText1"/>
				<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
				<xsl:text> </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="$preambleHint"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
				<xsl:call-template name="insert-javadoc-line-breaks-recurse">
				  <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,$preambleHint))"/>
				  <xsl:with-param name="breakText1"   select="$breakText1"/>
				  <xsl:with-param name="breakText2"   select="$breakText2"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<!-- Warning next follows this preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="$breakText1"/>
				<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
				<xsl:text> </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="$preambleWarning"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
				<xsl:call-template name="insert-javadoc-line-breaks-recurse">
				  <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,$preambleWarning))"/>
				  <xsl:with-param name="breakText1"   select="$breakText1"/>
				  <xsl:with-param name="breakText2"   select="$breakText2"/>
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
    </xsl:when>
	<xsl:otherwise>
		<!-- starts with Warning: -->
		<!-- insert javadoc line break -->
		<xsl:text>&#10;</xsl:text>
		<xsl:text> * </xsl:text>
		<xsl:text disable-output-escaping="yes"> &lt;li&gt; </xsl:text>
		<!-- skip initial Hint: or Warning: and determine what is next -->
		<xsl:variable name="preambleHint"    select="normalize-space(substring-before(substring-after($inputString,$breakText2),'Hint:'))"/>
		<xsl:variable name="preambleWarning" select="normalize-space(substring-before(substring-after($inputString,$breakText2),'Warning:'))"/>
		<xsl:choose>
			<xsl:when test="(string-length($preambleHint) = 0) and (string-length($preambleWarning) = 0)">
				<!-- this is last substring, no preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="substring-before($inputString,':')"/>
				<xsl:text disable-output-escaping="yes">:&lt;/i&gt; </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="substring-after($inputString,':')"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
			</xsl:when>
			<xsl:when test="(string-length($preambleHint) > 0) and 
							 ((string-length($preambleWarning) = 0) or (string-length($preambleWarning) > string-length($preambleHint)))">
				<!-- Hint next follows this preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="$breakText2"/>
				<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
				<xsl:text> </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="$preambleHint"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
				<xsl:call-template name="insert-javadoc-line-breaks-recurse">
				  <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,$preambleHint))"/>
				  <xsl:with-param name="breakText1"   select="$breakText1"/>
				  <xsl:with-param name="breakText2"   select="$breakText2"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<!-- Warning next follows this preamble -->
				<xsl:text disable-output-escaping="yes">&lt;i&gt;</xsl:text>
				<xsl:value-of select="$breakText2"/>
				<xsl:text disable-output-escaping="yes">&lt;/i&gt;</xsl:text>
				<xsl:text> </xsl:text>
				<xsl:call-template name="hyperlink">
					<xsl:with-param name="string">
						<xsl:value-of select="$preambleWarning"/>
					</xsl:with-param>
				</xsl:call-template>
				<xsl:text disable-output-escaping="yes"> &lt;/li&gt; </xsl:text>
				<xsl:call-template name="insert-javadoc-line-breaks-recurse">
				  <xsl:with-param name="inputString" select="normalize-space(substring-after($inputString,$preambleWarning))"/>
				  <xsl:with-param name="breakText1"   select="$breakText1"/>
				  <xsl:with-param name="breakText2"   select="$breakText2"/>
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:otherwise>
  </xsl:choose>
</xsl:template>
    
    <xsl:template name="hyperlink">
		<!-- further adapted from X3dTooltipConversions.xslt -->
        <!-- Search and replace urls in text:  adapted (with thanks) from 
            http://www.dpawson.co.uk/xsl/rev2/regex2.html#d15961e67 by Jeni Tennison using url regex (http://[^ ]+) -->
        <!-- Justin Saunders http://regexlib.com/REDetails.aspx?regexp_id=37 url regex ((mailto:|(news|(ht|f)tp(s?))://){1}\S+) -->
        <xsl:param name="string" select="string(.)"/>
        <!-- wrap html text string with spaces to ensure no mismatches occur -->
        <xsl:variable name="spacedString">
            <xsl:text> </xsl:text>
            <xsl:value-of select="$string"/>
            <xsl:text> </xsl:text>
        </xsl:variable>
        <!-- diagnostic 
        <xsl:if test="contains($spacedString,'http')">
        </xsl:if>
            <xsl:message>
                <xsl:text>diagnostic: $spacedString=</xsl:text>
                <xsl:value-of select="normalize-space($spacedString)"/>
            </xsl:message>
        -->
        <!-- First: find and link url values.  Avoid matching encompassing quote marks. -->
        <xsl:analyze-string select="$spacedString" regex='(mailto:|((news|http|https|sftp)://)[a-zA-Z0-9._%+-/#()]+)'>
            <xsl:matching-substring>
                <!-- diagnostic
					<xsl:message>
						<xsl:text>*regex match success (</xsl:text>
						<xsl:value-of select="."/>
						<xsl:text>) </xsl:text>
					</xsl:message>
                -->
				<xsl:element name="a">
					<xsl:attribute name="href">
						<xsl:value-of select="."/>
					</xsl:attribute>
					<xsl:attribute name="target">
						<xsl:text>_blank</xsl:text>
					</xsl:attribute>
					<xsl:value-of select="."/>
					<xsl:if test="(contains(.,'youtube.com') or contains(.,'youtu.be')) and not(contains(.,'rel='))">
						<!-- prevent advertising other YouTube videos when complete -->
						<xsl:text disable-output-escaping="yes">&amp;rel=0</xsl:text>
					</xsl:if>
				</xsl:element>
				<!-- alternate form
				<xsl:text disable-output-escaping="no">&lt;a href="</xsl:text>
				<xsl:value-of select="."/>
				<xsl:text disable-output-escaping="no">" target="_blank"&gt;</xsl:text>
					<xsl:value-of select="."/>
				<xsl:text disable-output-escaping="no">&lt;/a&gt;</xsl:text>
				-->
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <!-- diagnostic
                <xsl:if test="(string-length(normalize-space(.)) > 0)">
                    <xsl:message>
                        <xsl:text>**regex match failure (</xsl:text>
                        <xsl:copy-of select="."/>
                        <xsl:text>)**</xsl:text>
                    </xsl:message>
                </xsl:if>
                -->
                <!-- avoid returning excess whitespace -->
                <xsl:choose>
                    <xsl:when test="(string-length(.) > 0) and (string-length(normalize-space(.)) = 0)">
                        <xsl:text> </xsl:text>
                    </xsl:when>
                    <xsl:when test="string-length(normalize-space(.)) > 0">
                        <xsl:copy-of select="." />
                    </xsl:when>
                </xsl:choose>
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>

</xsl:stylesheet>
