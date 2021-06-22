<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" version="1.0.0" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>ngdc</sld:Name>
      <sld:Title>NGDC</sld:Title>
      <sld:Abstract>A palette used by the US National Geophysical Data Center (NGDC) for relief maps using the ETOPO1 global relief model.
      
      The topographic colors are based on GMT globe by Lester M. Anderson of CASP, UK, modified by Jesse Varner and Elliot Lim (NOAA/NGDC) to have a smaller band of white at the highest elevations. The bathymetry is based on GMT haxby, popularised by Bill Haxby, LDEO.
      </sld:Abstract>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry color="#0a0079" quantity="-11000" label="-11000"/>
              <sld:ColorMapEntry color="#1a0089" quantity="-10500.799999999999" label="-10501"/>
              <sld:ColorMapEntry color="#260098" quantity="-9999.6499999999996" label="-10000"/>
              <sld:ColorMapEntry color="#1b03a6" quantity="-9500.4500000000007" label="-9500"/>
              <sld:ColorMapEntry color="#1006b4" quantity="-8999.2999999999993" label="-8999"/>
              <sld:ColorMapEntry color="#0509c1" quantity="-8500.1000000000004" label="-8500"/>
              <sld:ColorMapEntry color="#000ecb" quantity="-8000.8999999999996" label="-8001"/>
              <sld:ColorMapEntry color="#0016d2" quantity="-7499.75" label="-7500"/>
              <sld:ColorMapEntry color="#001ed8" quantity="-7000.5499999999993" label="-7001"/>
              <sld:ColorMapEntry color="#0027df" quantity="-6499.3999999999996" label="-6499"/>
              <sld:ColorMapEntry color="#0c44e7" quantity="-6000.1999999999998" label="-6000"/>
              <sld:ColorMapEntry color="#1a66f0" quantity="-5499.0499999999993" label="-5499"/>
              <sld:ColorMapEntry color="#1375f4" quantity="-4999.8500000000004" label="-5000"/>
              <sld:ColorMapEntry color="#0e85f9" quantity="-4500.6500000000005" label="-4501"/>
              <sld:ColorMapEntry color="#159efc" quantity="-3999.5" label="-4000"/>
              <sld:ColorMapEntry color="#1eb2ff" quantity="-3500.3000000000002" label="-3500"/>
              <sld:ColorMapEntry color="#2bbaff" quantity="-2999.1499999999996" label="-2999"/>
              <sld:ColorMapEntry color="#37c1ff" quantity="-2499.9499999999989" label="-2500"/>
              <sld:ColorMapEntry color="#41c8ff" quantity="-2000.75" label="-2001"/>
              <sld:ColorMapEntry color="#4fd2ff" quantity="-1499.6000000000004" label="-1500"/>
              <sld:ColorMapEntry color="#5edfff" quantity="-1000.3999999999996" label="-1000"/>
              <sld:ColorMapEntry color="#8ae3ff" quantity="-499.25" label="-499"/>
              <sld:ColorMapEntry color="#b2edff" quantity="-0.0" label="0"/>
              <sld:ColorMapEntry color="#336600" quantity="1.0" label="0"/>
              <sld:ColorMapEntry color="#33cc66" quantity="99.400000000001455" label="99"/>
              <sld:ColorMapEntry color="#bbe492" quantity="200.80000000000109" label="201"/>
              <sld:ColorMapEntry color="#ffdcb9" quantity="499.14999999999964" label="499"/>
              <sld:ColorMapEntry color="#f3ca89" quantity="1000.2999999999993" label="1000"/>
              <sld:ColorMapEntry color="#e6b858" quantity="1499.5" label="1500"/>
              <sld:ColorMapEntry color="#d9a627" quantity="2000.6499999999996" label="2001"/>
              <sld:ColorMapEntry color="#a89a1f" quantity="2499.8500000000004" label="2500"/>
              <sld:ColorMapEntry color="#a49019" quantity="2999.0499999999993" label="2999"/>
              <sld:ColorMapEntry color="#a28613" quantity="3500.2000000000007" label="3500"/>
              <sld:ColorMapEntry color="#9f7b0d" quantity="3999.3999999999996" label="3999"/>
              <sld:ColorMapEntry color="#9c7107" quantity="4500.5500000000011" label="4501"/>
              <sld:ColorMapEntry color="#996600" quantity="4999.75" label="5000"/>
              <sld:ColorMapEntry color="#a25959" quantity="5500.8999999999978" label="5501"/>
              <sld:ColorMapEntry color="#b27676" quantity="6000.1000000000022" label="6000"/>
              <sld:ColorMapEntry color="#b79393" quantity="6499.2999999999993" label="6499"/>
              <sld:ColorMapEntry color="#c2b0b0" quantity="7000.4500000000007" label="7000"/>
              <sld:ColorMapEntry color="#cccccc" quantity="7499.6500000000015" label="7500"/>
              <sld:ColorMapEntry color="#e5e5e5" quantity="8000.7999999999993" label="8001"/>
              <sld:ColorMapEntry color="#ffffff" quantity="8500" label="8500"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>