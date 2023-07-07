import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 0, 255), thickness=3):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def detect_lane_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    
    edges = cv2.Canny(blur, 50, 150)
    
    
    height, width = edges.shape[:2]
    roi_vertices = np.array([[(0, height), (width / 2, height / 2), (width, height)]], dtype=np.int32)
    roi_edges = region_of_interest(edges, roi_vertices)
    
    
    lines = cv2.HoughLinesP(roi_edges, rho=1, theta=np.pi/180, threshold=30, minLineLength=20, maxLineGap=100)
    
  
    result = np.copy(image)
    draw_lines(result, lines)
    
    return result
image = cv2.imread('road_image.jpg')


result = detect_lane_lines(image)


cv2.imshow('Lane Detection', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
