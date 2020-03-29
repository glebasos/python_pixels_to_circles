import cv2
import numpy as np


def boxneighbors(a, boxSize, rowNumber, columnNumber): #sliding window to get pixel area
    return np.array([[a[i][j] for j in range(columnNumber, columnNumber + boxSize-1)]
                     for i in range(rowNumber, rowNumber + boxSize-1)])

fourcc = cv2.VideoWriter_fourcc(*'XVID') #video settings
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (316,272)) #video settings
size_d = 4  # circle diameter (4 or more)
size_r = int(size_d / 2)  # circle radius
img = cv2.imread("input.png", 1)
pic = np.copy(img)
b = pic[..., 0]
b = np.pad(b, (size_r, size_r), 'symmetric')
g = pic[..., 1]
g = np.pad(g, (size_r, size_r), 'symmetric')
r = pic[..., 2]
r = np.pad(r, (size_r, size_r), 'symmetric')
canva = np.copy(pic)
canva[..., 0] = 0
canva[..., 1] = 0
canva[..., 2] = 0
cv2.namedWindow("output")
cv2.moveWindow("output", 20, 20)
for i in range(0, len(pic) - 1, size_r * 2):
    for j in range(0, len(pic[i]) - 1, size_r * 2):
        pix_b = int(np.mean(boxneighbors(b, size_r, i + size_r, j + size_r)))
        pix_g = int(np.mean(boxneighbors(g, size_r, i + size_r, j + size_r)))
        pix_r = int(np.mean(boxneighbors(r, size_r, i + size_r, j + size_r)))
        center_coordinates = (j + size_r, i + size_r)
        radius = size_r
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
