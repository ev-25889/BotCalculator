from PIL import Image, ImageDraw, ImageFont



def get_numbers(date):
    hoy = int(date.split('.')[0])
    mes = int(date.split('.')[1])
    ano = int(date.split('.')[2])
    """"""
    while hoy > 22:
        hoy = int(str(hoy)[0]) + int(str(hoy)[1])
    while mes > 22:
        mes = int(str(mes)[0]) + int(str(mes)[1])
    while ano > 22:
        sum = 0
        while ano > 0:
            sum += ano % 10
            ano //= 10
        ano = sum

    hoymes = hoy + mes
    hoyano = hoy + ano
    mesano = mes + ano

    while hoymes > 22:
        hoymes = int(str(hoymes)[0]) + int(str(hoymes)[1])
    while hoyano > 22:
        hoyano = int(str(hoyano)[0]) + int(str(hoyano)[1])
    while mesano > 22:
        mesano = int(str(mesano)[0]) + int(str(mesano)[1])

    return hoy, mes, ano, hoymes, mesano, hoyano



def create_picture(date, chat_id):
    image = Image.open("matrix.png")
    hoy, mes, ano, hoymes, hoyano, mesano = get_numbers(date=date)
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype("Helvetica", 25, encoding="unic")
    drawer.text((25, 200), str(hoy),  fill='red', font=font)
    drawer.text((150, 10), str(mes),  fill='red', font=font)
    drawer.text((275, 200), str(ano),  fill='red', font=font)
    drawer.text((25, 70), str(hoymes),  fill='blue', font=font)
    drawer.text((150, 265), str(hoyano),  fill='blue', font=font)
    drawer.text((275, 70), str(mesano),  fill='blue', font=font)
    image_name = '{}.png'.format(chat_id)
    image.save(image_name)
    #image.show()
    return image_name


#print(create_picture('30.10.1999'))
#print(create_picture('30.10.1943'))
#print(create_picture('14.01.2004'))
#print(create_picture('25.12.2022'))