import re

def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'IP Addresses': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        'Dates': re.findall(r'([1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
    }
    return result

# Example usage:
sample_text = """
First Dataset
Visit our website at https://www.technews.com.
For support, contact us at support@textnews.com.
IP address: 192.168.0.1
Date: 23/11/2023
PAN number: AUJPD4551B

Second Dataset
Visit our website at https://www.animebattlecenter.com.
For more info connect with  info@anibc.com.
IP address: 192.148.7.1
Date: 22/10/2023
PAN number: CYRKD1290J
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""
Output:

URLs: ['https://www.technews.com.', 'https://www.animebattlecenter.com.']
IP Addresses: ['192.168.0.1', '192.148.7.1']
Dates: [('23', '11', '20')]
PAN Numbers: ['AUJPD4551B', 'CYRKD1290J']
"""