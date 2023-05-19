from digi.data.de_id.util import PII_Fields, order_of_operations, drop, trim, replace

"""
Defines the PII Fields relevant to the HIPAA Privacy Rule mapped to Zed functions to de-identify them.
"""

# TODO fuzzy matching
# TODO if field is substring of field, do the same function

SMALL_POP_ZIPCODES = [] # TODO

# dictionary of dictionaries, mapping operation to a list of { fields to Zed commands }
PII = {}
for operation in order_of_operations:
    PII[operation] = []

drop_categories = ["name", "date", "phone", "email", "ssn", "mrn", "hbn", "account", "certificate", "vehicle", "device", "url", "ip", "biometric", "image"]
drop_fields = [field for category in drop_categories for field in PII_Fields[category]] # create flat list of fields
for field in drop_fields:
    PII["drop"].append({ field: drop(field) })

# replace fields
for field in PII_Fields["geography"]:
    PII["replace"].append({field: replace(field, lambda value: value in SMALL_POP_ZIPCODES, "000")})

# # trim fields
# for field in PII_Fields["geography"]:
#   PII[field] = trim(field, 3)