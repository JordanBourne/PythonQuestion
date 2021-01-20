'''
For our record keeping, we use a CRM called Zoho,
in which we have modeled the records from the previous step as:
Leads - For the parent business record
Remittance Records - For the individual address records

Sometimes in our data, we get a new Remittance Record for a lead that already exists
While other times both the Remittance Record and Lead are both net new

Write a function that can take in a list of remittance records and creates and groups them in mock zoho
'''
from mockZoho import find_remittance_record, create_lead, create_remittance_record

sample_records = [
    { 'address_id': 'PO Box 5857+City+KY', 'name': 'First Data Corp', 'volume': 200 },
    { 'address_id': 'PO Box 8888+City+FL', 'name': 'First Data Corp', 'volume': 100 },
    { 'address_id': 'PO Box 1234+City+CO', 'name': 'New Corp', 'volume': 100 },
    { 'address_id': 'PO Box 9124+City+WY', 'name': 'New Corp', 'volume': 100 },
]


def run_update(records):
    # implement
    return


if __name__ == '__main__':
    run_update(sample_records)