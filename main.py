import cv2
import numpy as np


def boxneighbors(a, boxSize, rowNumber, columnNumber): #sliding window to get pixel area
    return np.array([[a[i][j] for j in range(columnNumber, columnNumber + boxSize-1)]
                     for i in range(rowNumber, rowNumber + boxSize-1)])

fourcc = cv2.VideoWriter_fourcc(*'XVID') #video settings
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (316,272)) #video settings
size = 11  # circle diameter
size = int(size / 2)  # circle radius
img = cv2.imread("input.png", 1)  #jpg, png, bmp, etc...
pic = np.copy(img)
b = pic[..., 0]
b = np.pad(b, (int(size / 2), int(size / 2)), 'symmetric')
g = pic[..., 1]
g = np.pad(g, (int(size / 2), int(size / 2)), 'symmetric')
r = pic[..., 2]
r = np.pad(r, (int(size / 2), int(size / 2)), 'symmetric')
canva = np.copy(pic)
canva[..., 0] = 0
canva[..., 1] = 0
canva[..., 2] = 0
cv2.namedWindow("output")
cv2.moveWindow("output", 20, 20)
for i in range(0, len(pic) - 1, size * 2):
    for j in range(0, len(pic[i]) - 1, size * 2):
        pix_b = int(np.mean(boxneighbors(b, size, i + int(size / 2), j + int(size / 2))))
        pix_g = int(np.mean(boxneighbors(g, size, i + int(size / 2), j + int(size / 2))))
        pix_r = int(np.mean(boxneighbors(r, size, i + int(size / 2), j + int(size / 2))))
        center_coordinates = (j + int(size / 2), i + int(size / 2))
        radius = size
        color = (pix_b, pix_g, pix_r)
        thickness = -1
        canva = cv2.circle(canva, center_coordinates, radius, color, thickness)
        out.write(canva) #write to video
        cv2.imshow('output', canva)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            pass
        # img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# cv2.imshow('img2', canva)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output.png", canva)
