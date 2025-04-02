import qrcode
from PIL import Image

# URL para o QR Code
url = "https://caca-ao-tesouro-connectlinksp.netlify.app/"

# Criar o QR Code
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta correção de erro
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Criar imagem do QR Code com fundo branco
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

# Dividir o QR Code em duas cores na diagonal (azul e laranja)
qr_width, qr_height = qr_img.size
pixels = qr_img.load()

for x in range(qr_width):
    for y in range(qr_height):
        if pixels[x, y] == (0, 0, 0):  # Pixels pretos do QR Code
            if y > x:  # Define a diagonal para separação de cores
                pixels[x, y] = (0, 0, 255)  # Azul
            else:
                pixels[x, y] = (255, 165, 0)  # Laranja

# Salvar o QR Code final
output_path = "C:/Users/Elisa/Pictures/Screenshots/Caça_ao_tesouro/qrcode_azul_laranja.png"
qr_img.save(output_path)

# Retornar o caminho do QR Code gerado
output_path