from xml.dom import minidom
xmldoc = minidom.parse("test_meta.xml")
nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetaData")
coeffs = {}
for node in nodes:
    bn = node.getElementsByTagName("ps:BandNumber")[0].firstChild.data
    if bn in ['1', '2', '3', '4']:
        i = int(bn)
        value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
        coeffs[i] = float(value)
# multiple by coeffs
band_blue2 = band_blue * coeffs[1]
band_green2 = band_green * coeffs[2]
band_red2 = band_red * coeffs[3]
band_nir2 = band_nir * coeffs[4]

