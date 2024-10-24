import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = []

    for establishment in root.findall(".//EstablishmentDetail"):
        business_name = establishment.find('BusinessName').text
        business_type = establishment.find('BusinessType').text
        address_1 = establishment.find('AddressLine1').text
        address_2 = establishment.find('AddressLine2').text
        address_3 = establishment.find('AddressLine3').text
        address_4 = establishment.find('AddressLine4').text if establishment.find('AddressLine4') is not None else ''
        postcode = establishment.find('PostCode').text
        fhrs_id = establishment.find('FHRSID').text
        rating_value = establishment.find('RatingValue').text
        rating_date = establishment.find('RatingDate').text
        local_authority = establishment.find('LocalAuthorityName').text
        geocode_longitude = establishment.find('.//geocode/longitude').text
        geocode_latitude = establishment.find('.//geocode/latitude').text
        hygiene_score = establishment.find('.//scores/Hygiene').text
        structural_score = establishment.find('.//scores/Structural').text
        confidence_in_management = establishment.find('.//scores/ConfidenceInManagement').text

        establishment_data = {
            'Business Name': business_name,
            'Business Type': business_type,
            'Address Line 1': address_1,
            'Address Line 2': address_2,
            'Address Line 3': address_3,
            'Address Line 4': address_4,
            'Postcode': postcode,
            'FHRS ID': fhrs_id,
            'Rating Value': rating_value,
            'Rating Date': rating_date,
            'Local Authority': local_authority,
            'Longitude': geocode_longitude,
            'Latitude': geocode_latitude,
            'Hygiene Score': hygiene_score,
            'Structural Score': structural_score,
            'Confidence in Management': confidence_in_management
        }

        data.append(establishment_data)

    return data

xml_files = ['./data_source/ask_italian/ask_italian.xml', './data_source/jd_wetherspoon/jd_wetherspoon.xml'] 

all_data = []
for file in xml_files:
    all_data.extend(parse_xml(file))

df = pd.DataFrame(all_data)
df.to_excel('./company_data/hospitality_data.xlsx', index=False)

print('successfully saved')
