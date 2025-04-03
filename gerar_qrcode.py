import qrcode

# URL do site que deseja transformar em QR Code
url = "https://caca-ao-tesouro-connectlinksp.netlify.app/gazinho2"

# Criar QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(fill="black", back_color="white")

# Salvar a imagem
img.save("qrcode.png")

print("QR Code gerado com sucesso! Verifique o arquivo 'qrcode.png'.")
