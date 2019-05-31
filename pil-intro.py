from PIL import Image
import os

img = Image.open('images/profile.jpg')
img.show()
new_img = Image.open('images/profile.jpg').convert('L')
new_img.show()

filelist = ['images/profile.jpg', 'images/moon.jpg', 'images/mean_profile.jpg']

for file in filelist:
    outfile = os.path.split(file)[0]+".png"
    if file != outfile:
        try:
            Image.open(file).save(outfile)
        except IOError:
            print("cannot convert"), file