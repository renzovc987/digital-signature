from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.x509 import CertificateBuilder, Name, NameOID, BasicConstraints, random_serial_number
from cryptography.x509 import NameAttribute
import datetime

# Generar clave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Guardar clave privada en archivo .pem
with open('private_key.pem', 'wb') as key_file:
    key_file.write(
        private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=NoEncryption()
        )
    )

# Crear un nombre para el certificado
subject = issuer = Name([
    NameAttribute(NameOID.COUNTRY_NAME, 'US'),
    NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, 'California'),
    NameAttribute(NameOID.LOCALITY_NAME, 'San Francisco'),
    NameAttribute(NameOID.ORGANIZATION_NAME, 'My Company'),
    NameAttribute(NameOID.COMMON_NAME, 'mycompany.com')
])

# Crear el certificado
cert = CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    BasicConstraints(ca=False, path_length=None), critical=True,
).sign(private_key, hashes.SHA256())

# Guardar certificado en archivo .pem
with open('certificate.pem', 'wb') as cert_file:
    cert_file.write(
        cert.public_bytes(
            encoding=Encoding.PEM
        )
    )
