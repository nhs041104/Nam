def image_to_byte_array(image_path):
    with open(image_path, "rb") as image_file:
        byte_array = bytearray(image_file.read())
    return byte_array

image_path = "C:\\Users\\남현승\\Desktop\\programing\\etc\\ok.png"

image_byte_array = image_to_byte_array(image_path)

print(len(image_byte_array))
