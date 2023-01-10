#import the necessary libraries
import io
from PIL import Image
import base64
#artwork = '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52\x00\x00\x00\x0A\x00\x00\x00\x0A\x08\x02\x00\x00\x00\x02\x50\x58\xEA\x00\x00\x00\x04\x67\x41\x4D\x41\x00\x00\xAF\xC8\x37\x05\x8A\xE9\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6F\x66\x74\x77\x61\x72\x65\x00\x41\x64\x6F\x62\x65\x20\x49\x6D\x61\x67\x65\x52\x65\x61\x64\x79\x71\xC9\x65\x3C\x00\x00\x00\x18\x49\x44\x41\x54\x78\xDA\x62\xFC\x3F\x95\x9F\x01\x37\x60\x62\xC0\x0B\x46\x60\x0C\x46\x60\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
artwork = '\x1a\n\x00\x00\x00\r'

# image_data = base64.b64decode('\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x0a\x00\x00\x00\x0a\x08\x02\x00\x00\x00\x02\x50\x58\xea\x00\x00\x00\x04\x67\x41\x4d\x41\x00\x00\xaf\xc8\x37\x05\x8a\xe9\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\x66\x74\x77\x61\x72\x65\x00\x41\x64\x6f\x62\x65\x20\x49\x6d\x61\x67\x65\x52\x65\x61\x64\x79\x71\xc9\x65\x3c\x00\x00\x00\x18\x49\x44\x41\x54\x78\xda\x62\xfc\x3f\x95\x9f\x01\x37\x60\x62\xc0\x0b\x46\x60\x0c\x46\x60\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82')
image_data = base64.b64decode(artwork)
with open('image.png', 'wb') as f:
    f.write(image_data)

#artwork = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# artwork = b'PNG\r\n\x1a\n\x00\x00\x00\r'
# result_file = 'result_file'

# with open(result_file, 'wb') as file_handler:
#     file_handler.write(artwork)
#Image.open('image.png')#.save(result_file + '.png', 'PNG')

#open the file containing the raw byte data
# with open('raw_byte_data.bin', 'rb') as f:
#     data = f.read()

# #convert the raw byte data to an image
# image = Image.open(io.BytesIO(data))

# #save the image
# image.save('image.jpg')