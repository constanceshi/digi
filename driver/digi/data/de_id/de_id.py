from digi.data.de_id.hipaa import PII as hipaa_PII
from digi.data.de_id.ccpa import PII as ccpa_PII
from digi.data.de_id.util import order_of_operations, operators

class De_id:
    def __init__(self, hipaa=True, ccpa=False, exceptions=[]):
        self.hipaa = hipaa
        self.ccpa = ccpa
        self.exceptions = exceptions
        self.PII = {}
        if self.hipaa:
            self.PII = dict(hipaa_PII)
        if self.ccpa:
            for operation in order_of_operations:
                self.PII[operation].extend(ccpa_PII[operation])

    def gen(self):
        zed_flow = ["yield this"]
        for operation in order_of_operations:
            if self.PII[operation]:
                operation_list = []
                for d in self.PII[operation]:
                    field = list(d.keys())[0]
                    if field not in self.exceptions:
                        operation_list.append(d[field])
                operation_string = operators[operation].join(operation_list)
                if operation == "drop":
                    operation_string = f"{operation} " + operation_string
            zed_flow.append(operation_string)
        return " | ".join(zed_flow)

# class Hipaa(Deid):
#     def __init__(self, ):


# # def hipaa():

#     # todo every += creates a new string
#     # create an array of keywords and operators?

#     # benchmark time, try dropping multiple fields
#     # compare before and after

#     # hipaa class 
#     # methods to generate dataflow
#     # hipaa().x().y().gen() -> string
#     # x is shorthand zipcode, fuzz matching
#     # make module extensible
#     # constructor pattern like spark
#     # group them together and drop ssn, to drop all ssn related aliases
#     # like peekaboo modularity

#     # general util functions?
#     # dropping field function
#     # fuzzy matching function
#     #    soundex algorithm, checking substrings of the field
#     # condensing into shorter/fewer characters/digits function (keep first n digits)

#     de_id_operations = ["yield this"]

#     # Name
#     de_id_operations.append(" | drop name")
#     de_id_operations.append(" | drop first_name")
#     de_id_operations.append(" | drop last_name")

#     # Geographic Subdivisions
#     # todo: keep state size or larger
#     # todo: keep first three digits of zip codes, except for explicitly listed zip codes that have populations less than 20,000, which must be replace by 000

#     de_id_operations.append(" | drop location")
#     de_id_operations.append(" | drop address")
#     de_id_operations.append(" | drop city")
#     de_id_operations.append(" | drop county")
#     de_id_operations.append(" | drop region")
#     de_id_operations.append(" | drop zipcode")

#     # Date
#     # todo: keep year, dates not directly related to individual
#     de_id_operations.append(" | drop date")
#     de_id_operations.append(" | drop time")
#     de_id_operations.append(" | drop ts")

#     # Phone and Fax Numbers
#     de_id_operations.append(" | drop phone")
#     de_id_operations.append(" | drop phone_number")
#     de_id_operations.append(" | drop fax")
#     de_id_operations.append(" | drop fax_number")

#     # Email Address
#     de_id_operations.append(" | drop email")
#     de_id_operations.append(" | drop email_address")

#     # social security number
#     de_id_operations.append(" | drop ssn")
#     de_id_operations.append(" | drop social_security_number")

#     # Medical Record Number
#     # Health-plan Beneficiary Numbers
#     # Account Numbers
#     # Certificate/license Numbers
#     # Vehicle Identifiers and Serial Numbers (Including License Plate Numbers)
#     # Device Identifiers and Serial Numbers
#     # Internet URLs
#     # IP Addresses
#     # Biometric Identifiers (Including Fingerprints and Voice-Prints)
#     # Full-face Photographic Images
#     # Other Unique Identifying Numbers, Characteristics or Code




#     # todo: remove, for testing
#     de_id_operations.append(" | drop watt")

#     return "".join(de_id_operations)