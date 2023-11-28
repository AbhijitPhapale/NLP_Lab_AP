#Assignment no : 2
#Name : Abhijit Balasaheb Phapale
#Batch : B3
#Roll no : 45
#Title : Regular Expression using python re library

import re

def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'IP Addresses': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        'Dates': re.findall(r"(?:(?:[0-2]?[0-9]|3[01])\/(?:0[1-9]|1[0-2])\/(?:19|20)\d{2})", text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
    }
    return result

# Example usage:
sample_text = """
First Dataset
Visit our website at https://www.openai.com.
For support, contact us at support@openai.com.
IP address: 192.154.0.1
Date: 11/02/2012
PAN number: GBFPP3452P

Second Dataset
Visit our website at https://www.netflix.com.
For more info connect with  contact@netflix.com.
IP address: 192.168.2.1
Date: 23/01/2003
PAN number: CYRKD1290J
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""
Output:

URLs: ['https://www.openai.com.', 'https://www.netflix.com.']
IP Addresses: ['192.154.0.1', '192.168.2.1']
Dates: ['11/02/2012', '23/01/2003']
PAN Numbers: ['GBFPP3452P', 'CYRKD1290J']

"""