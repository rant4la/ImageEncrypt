from PIL import Image
import random
import sys

if(len(sys.argv) != 2):
    print('decrypt <image>')
    sys.exit()

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

imageName = sys.argv[1]

img = Image.open(imageName, 'r')
pixels = img.load()
width, height = img.size

pixelSpacing = int(imageName.split('.')[0])

print('Image size: {0}x{1} \nDecrypting...'.format(width, height)) 

bits = ''

i = 0
for x in range(width - 1):
    for y in range(height):
        if(i % pixelSpacing == 0):
            r, g, b = pixels[x + 1, y]

            if(pixels[x, y] == pixels[x + 1, y]):
                bits += '1'
            else:
                bits += '0'

        i += 1

print('Decrypted data: {0}'.format(text_from_bits(bits)))
