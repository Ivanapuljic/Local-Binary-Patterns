import cv2
import numpy as np 

#loading and converting image to grayscale
img = cv2.imread("/home/osirv/Osirv projekt/lenna.bmp", cv2.IMREAD_GRAYSCALE) 
img_after = cv2.imread("/home/osirv/Osirv projekt/lenna.bmp", cv2.IMREAD_GRAYSCALE)

#selecting pixels, for each pixel in the image, neighbor pixels surrounding the center pixel are selected
def get_pixel(img, x, y):
    try:
        return img[x,y]
    except:
        pass

#comparing neighbor pixels values with center pixel value
#if center pixel has larger value than neighbor pixel, neighbor pixel value is set to 0
#if center pixel has smaller value than neighbor pixel, neighbor pixel value is set to 1; 
def calc_pixel_value(center_pixel, neighbor_pixels):
    value=[]
    for pixel in neighbor_pixels:
        if pixel >= center_pixel:
            value.append(1)
        else:
            value.append(0)
    return value
        
    
for x in range(0, len(img)): #select all rows
    for y in range(0, len(img)): #select all columns
        center_pixel     = img[x,y] #center pixel
        above_pixel      =get_pixel(img, x, y-1) #pixel above center pixel
        down_pixel       =get_pixel(img, x, y+1) #pixel under center pixel
        right_pixel      =get_pixel(img, x+1, y) #right pixel
        left_pixel       =get_pixel(img, x-1, y) #left pixel
        aboveleft_pixel  =get_pixel(img, x-1, y-1) #above left pixel
        aboveright_pixel =get_pixel(img, x+1, y-1 ) #above right pixel     
        downleft_pixel   =get_pixel(img, x-1, y+1) #down left pixel
        downright_pixel  =get_pixel(img, x+1, y+1) #down right pixel

       
        #selecting neighbour pixels clockwise, starting from the top left pixel and getting their value depending on the value of center pixel
        #store pixels in 8 bit array
        lbp_pixels = calc_pixel_value(center_pixel, [aboveleft_pixel, above_pixel, aboveright_pixel, right_pixel, downright_pixel, down_pixel, downleft_pixel, left_pixel])            
       
        
        lbp_combinations = [1, 2, 4, 8, 16, 32, 64, 128]
        lbp_pixel_value = 0
        for pixel in range(0, len(lbp_pixels)):
            #calculating final pixel value
            lbp_pixel_value = lbp_pixel_value+ (lbp_combinations[pixel]* lbp_pixels [pixel]) 

        img_after.itemset((x,y), lbp_pixel_value) 

            
cv2.imwrite ( "/home/osirv/Osirv projekt/" +'lbp2.png', img_after)            
cv2.imshow('before', img)
cv2.imshow('after', img_after)

cv2.waitKey(0)
  
cv2.destroyAllWindows()
    