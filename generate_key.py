from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar una clave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Guardar la clave privada en un archivo .pem
with open('private_key.pem', 'wb') as key_file:
    key_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )
