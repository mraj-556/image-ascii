from pywhatkit import image_to_ascii_art as it
import cv2

img = 'img1.jpeg'
text = 'acii.text'
a = it(img,text)
print(a)