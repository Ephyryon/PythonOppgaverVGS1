from PIL import Image, ImageFilter
def main():
    with Image.open("imgs/in.jpg") as img:
        img1 = img.rotate(180)
        img1.save("imgs/out_rotated.jpg")
        img2 = img.resize([1920, 1080])
        img2.save("imgs/out_resized.png")
        img3 = img.filter(ImageFilter.BLUR)
        img3.save("imgs/out_blur.jpg")
main()