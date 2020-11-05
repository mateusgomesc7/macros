# Importing Image and ImageGrab module from PIL package  
from PIL import ImageGrab 

# using the grab method 
im2 = ImageGrab.grab().load()
    
# im2.show()

color = im2[100, 100]

print(color)