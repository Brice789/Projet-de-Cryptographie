import json
from cryptography import x509
import base64

cert = json.loads(open('ca.json').read())

data = cert['data']['leaf_cert']['as_der']

cert_obj = x509.load_der_x509_certificate(base64.b64decode(data))

print(cert_obj.public_key().public_numbers().n)
