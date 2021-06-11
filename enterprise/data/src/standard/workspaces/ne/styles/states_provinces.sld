<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>states_provinces</se:Name>
    <UserStyle>
      <se:Name>State / Province</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>state_province_highlight</se:Name>
          <se:Description>
            <se:Title>State / Province Highlight</se:Title>
          </se:Description>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>sr_adm0_a3</ogc:PropertyName>
              <ogc:Function name="env">
                <ogc:Literal>adm0</ogc:Literal>
                <ogc:Literal></ogc:Literal>
              </ogc:Function>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ffffff</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>state_province</se:Name>
          <se:Description>
            <se:Title>State / Province</se:Title>
          </se:Description>
          <se:ElseFilter />
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#eeecdf</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
