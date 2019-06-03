from PIL import Image
import numpy

#generate empty map
np_im=numpy.zeros((444,401))
np_im+=255
img=Image.fromarray(np_im)
img=img.convert('L')
img.save("src/fetch_gazebo/fetch_gazebo_demo/maps/empty_map.pgm")

#transform image to grayscale array
im=Image.open("src/fetch_gazebo/fetch_gazebo_demo/maps/test_zone.pgm").convert('L')
(width,height)=im.size
grayscale=list(im.getdata())
grayscale=(numpy.array(grayscale)).reshape((height,width))