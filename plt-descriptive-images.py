from PIL import Image
from pylab import *

img = array(Image.open('images/profile.jpg'))
imshow(img)
#show()

x = [100, 150, 300, 400]
y = [50, 500, 200, 500]

plot(x, y, 'r*')
plot(x[:2], y[:2], 'r')
plot(x[2:], y[2:], 'ks:')

title('Plot do Marcão')

show()
