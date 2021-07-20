from PIL import Image

ASCII_CHARS = ["@","#","$","%","?","*","^",";",":",",","."]
ASCII_CHARS=ASCII_CHARS[::-1]
#resize
def resize_image(image,new_width):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    # tuple
    new_image= image.resize((new_width, new_height))
    return(new_image)




#greyify
def greyify(image):
    greyifying_image = image.convert("L")  #<color scheme>
    return(greyifying_image)


#img_to_ASCII
def pixels_to_ascii(image):
    # getdata se list 
    pixels = image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


#main
def main():
    new_width=int(input("Enter required width: "))
    path = input("Enter pathname to an image: ")
    image=Image.open(path)
    new_wali_image = pixels_to_ascii(greyify(resize_image(image, new_width)))
    ascii_image="\n".join([new_wali_image[index:(index+new_width)] for index in range(0, len(new_wali_image), new_width)])
    print(ascii_image)


main()
