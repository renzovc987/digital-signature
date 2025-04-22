from pyhanko.sign import signers
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter

# Ruta del PDF a firmar
pdf_path = 'documento.pdf'
signed_pdf_path = 'document_signed.pdf'

# Crear el firmador
try:
    cms_signer = signers.SimpleSigner.load(
        'private_key.pem',
        'certificate.pem'
        # No proporcionar key_passphrase ya que la clave no está cifrada
    )
except Exception as e:
    print(f"Error al cargar el firmador: {e}")

# Cargar el PDF
try:
    with open(pdf_path, 'rb') as doc:
        w = IncrementalPdfFileWriter(doc)
        
        # Firmar el PDF
        signed_pdf = signers.sign_pdf(
            w, 
            signers.PdfSignatureMetadata(field_name='Signature1'),
            signer=cms_signer,
        )
        
        # Guardar el PDF firmado
        with open(signed_pdf_path, 'wb') as out_file:
            # Escribir el PDF firmado en el archivo
            out_file.write(signed_pdf.read())

    print(f'PDF firmado guardado en {signed_pdf_path}')
except Exception as e:
    print(f"Error al firmar el PDF: {e}")
