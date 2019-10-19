from PIL import Image

image = Image.open('monro.jpg')

red_pixels, green_pixels, blue_pixels = image.split()

crop_pixels1 = 100
crop_pixels2 = 50

first_red_picture = red_pixels.crop((crop_pixels1,
                                     0,
                                     red_pixels.width,
                                     red_pixels.height))

second_red_picture = red_pixels.crop((crop_pixels2,
                                      0,
                                      red_pixels.width - crop_pixels2,
                                      red_pixels.height))

first_blue_picture = blue_pixels.crop((0,
                                       0,
                                       blue_pixels.width - crop_pixels1,
                                       blue_pixels.height))

second_blue_picture = blue_pixels.crop((crop_pixels2,
                                        0,
                                        blue_pixels.width - crop_pixels2,
                                        blue_pixels.height))

green_picture = green_pixels.crop((crop_pixels2,
                                   0,
                                   green_pixels.width - crop_pixels2,
                                   red_pixels.height))

red_pixels = Image.blend(first_red_picture, second_red_picture, 0.5)
blue_pixels = Image.blend(first_blue_picture, second_blue_picture, 0.5)
green_pixels = Image.blend(green_picture, green_picture, 0.5)

image = Image.merge('RGB', (red_pixels, green_pixels, blue_pixels))

coefficient = 0
width = 0
height = 0

if image.width > image.height:
    coefficient = image.width / 80
    width = int(image.width / coefficient)
    height = int(image.height / coefficient)
else:
    coefficient = image.height / 80
    width = int(image.width / coefficient)
    height = int(image.height / coefficient)

image.thumbnail((width, height))
image.save('small.jpg')
