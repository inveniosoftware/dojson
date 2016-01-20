<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:marc="http://www.loc.gov/MARC21/slim"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  exclude-result-prefixes="marc fn">
  <xsl:output method="xml"  indent="yes" encoding="UTF-8" omit-xml-declaration="yes"/>
  <xsl:template match="/">
    <xsl:if test="collection">
      <dc:collection xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
        <xsl:for-each select="collection">
          <xsl:for-each select="record">
            <dc:dc>
              <xsl:apply-templates select="."/>
            </dc:dc>
          </xsl:for-each>
        </xsl:for-each>
      </dc:collection>
    </xsl:if>
    <xsl:if test="record">
      <dc:dc xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:invenio="http://invenio-software.org/elements/1.0">
        <xsl:apply-templates/>
      </dc:dc>
    </xsl:if>
  </xsl:template>
  <xsl:template match="record">
    <!-- DOI -->
    <xsl:if test="datafield[@tag=024 and @ind1=7 and (subfield[@code='2']='doi' or subfield[@code='2']='DOI')]">
      <xsl:for-each select="datafield[@tag=024 and @ind1=7 and (subfield[@code='2']='doi' or subfield[@code='2']='DOI')]">
        <dc:identifier><xsl:text>doi:</xsl:text><xsl:value-of select="subfield[@code='a']"/></dc:identifier>
      </xsl:for-each>
    </xsl:if>
    <!-- Language -->
    <xsl:for-each select="datafield[@tag=041]">
      <dc:language>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:language>
    </xsl:for-each>
    <!-- Author/Creator -->
    <xsl:for-each select="datafield[@tag=100]">
      <dc:creator>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:creator>
    </xsl:for-each>
    <xsl:for-each select="datafield[@tag=700]">
      <dc:creator>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:creator>
    </xsl:for-each>
    <!-- Corporate Author/Creator, if no main author/creator -->
    <xsl:if test="not (datafield[@tag=100 and subfield[@code='a']] or datafield[@tag=700 and subfield[@code='a']])">
      <xsl:for-each select="datafield[@tag=110 and subfield[@code='a']]">
        <dc:creator><xsl:value-of select="subfield[@code='a']"/></dc:creator>
      </xsl:for-each>
      <xsl:for-each select="datafield[@tag=710 and subfield[@code='a']]">
        <dc:creator><xsl:value-of select="subfield[@code='a']"/></dc:creator>
      </xsl:for-each>
    </xsl:if>
    <!-- Title -->
    <xsl:for-each select="datafield[@tag=245]">
      <dc:title>
        <xsl:value-of select="subfield[@code='a']"/>
        <xsl:if test="subfield[@code='b']">
          <xsl:text>: </xsl:text><xsl:value-of select="subfield[@code='b']"/>
        </xsl:if>
      </dc:title>
    </xsl:for-each>
    <xsl:for-each select="datafield[@tag=111]">
      <dc:title>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:title>
    </xsl:for-each>
    <!-- Subject -->
    <xsl:for-each select="datafield[@tag=650 and @ind1=1 and @ind2=7]">
      <dc:subject>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:subject>
    </xsl:for-each>
    <!-- Main report number-->
    <xsl:for-each select="datafield[@tag=037]">
      <dc:identifier><xsl:value-of select="subfield[@code='a']"/></dc:identifier>
    </xsl:for-each>
    <!-- Additional report number-->
    <xsl:for-each select="datafield[@tag=088]">
      <dc:identifier><xsl:value-of select="subfield[@code='a']"/></dc:identifier>
    </xsl:for-each>
    <!-- Abstract -->
    <xsl:for-each select="datafield[@tag=520]">
      <dc:description>
        <xsl:value-of select="subfield[@code='a']"/>
      </dc:description>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
