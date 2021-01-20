leads = [
    {
        'name': 'First Data Corp',
        'address_ids': ['PO Box 6765+City+FL', 'PO Box 5857+City+KY'],
        'volume': 300
    },
    {
        'name': 'FMC Corp',
        'addresS_ids': ['PO Box 7985+City+WA', 'PO Box 7062+City+CT', 'PO Box 3176+City+FL'],
        'volume': 600
    }
]

remittance_records = [
    { 'address_id': 'PO Box 6765+City+FL', 'name': 'First Data Corp', 'volume': 100, 'lead': leads[0] },
    { 'address_id': 'PO Box 5857+City+KY', 'name': 'First Data Corp', 'volume': 200, 'lead': leads[0] },
    { 'address_id': 'PO Box 7985+City+WA', 'name': 'FMC Corp', 'volume': 100, 'lead': leads[1] },
    { 'address_id': 'PO Box 7062+City+CT', 'name': 'FMC Corp', 'volume': 200, 'lead': leads[1] },
    { 'address_id': 'PO Box 3176+City+FL', 'name': 'FMC Corp', 'volume': 300, 'lead': leads[1] }
]


def find_remittance_record(address_id):
    return next((item for item in remittance_records if item['address_id'] == address_id), None)


def create_remittance_record(record):
    remittance_records.append(record)


def create_lead(lead):
    leads.append(lead)
