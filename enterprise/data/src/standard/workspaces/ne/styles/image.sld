<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld
http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
<UserLayer>
	<Name>image</Name>
	<UserStyle>
		<Name>image</Name>
		<Title>raster image</Title>
		<Abstract>Copied from raster with a slight transparency for brightness</Abstract>
		<FeatureTypeStyle>
	        <FeatureTypeName>Feature</FeatureTypeName>
			<Rule>
				<RasterSymbolizer>
				    <Opacity>0.95</Opacity>
				</RasterSymbolizer>

			</Rule>
		</FeatureTypeStyle>
	</UserStyle>
</UserLayer>
</StyledLayerDescriptor>