from PIL import Image
import random
import sys

if(len(sys.argv) != 3):
    print('encrypt <image> <text>')
    sys.exit()

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

imageName = sys.argv[1]
bits = text_to_bits(sys.argv[2])
    
img = Image.open(imageName, 'r')
pixels = img.load()
width, height = img.size

pixelSpacing = round(width * height / len(bits))

print('Image size: {0}x{1} Data size:{2} \nEncrypting...'.format(width, height, len(bits))) 

i = 0
for x in range(width - 1):
    for y in range(height):
        if(i % pixelSpacing == 0):
            r, g, b = pixels[x + 1, y]

            if(bits[round(i / pixelSpacing)] == '0'):
                if(pixels[x + 1, y] == pixels[x, y]):
                    pixels[x, y] = (max(r - 1, 0), max(g - 1, 0), max(b - 1, 0))
            else:
                pixels[x, y] = (r, g, b)

        i += 1

img.save('{0}.png'.format(pixelSpacing))

print('Done')


