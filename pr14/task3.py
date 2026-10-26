import qrcode

NAME = "Nazar"
SURNAME = "Mischuck"
GROUP = "IT-32"
EMAIL = "nazariybeeest@gmail.com"

print(f"{NAME} {SURNAME}, {GROUP}")

text = f"{NAME} {SURNAME}, {GROUP}, {EMAIL}"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")