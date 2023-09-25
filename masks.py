from PIL import Image, ImageDraw



def softs(img,fotos):
    image = Image.open(img)

    w, h = image.size

    mask = Image.new('RGBA', (w,h), (255,255,255,0))
    r = ImageDraw.Draw(mask)

    w_h = int(h * 0.5)

    r.rectangle((0, 0, w, w_h), fill=(255,255,255))

    o_h = int(h * 0.5)
    r.rectangle((0, h - o_h, w, h), fill=(130, 130, 130))


    image.paste(mask,(0,0),mask)




    return image.save(fotos)