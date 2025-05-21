# app/utils/drawing.py
import cv2

def draw_corner_rect(img, bbox, l=20, t=5, rt=1, colorR=(255, 0, 255), colorC=(255, 255, 76)):
    """
    Manual implementation of corner rectangle drawing function
    
    Args:
        img: Image to draw on
        bbox: Bounding box in format [x, y, w, h]
        l: Length of corner lines
        t: Thickness of lines
        rt: Thickness of rectangle
        colorR: Color of rectangle
        colorC: Color of corner lines
    
    Returns:
        Image with drawn corner rectangle
    """
    x, y, w, h = bbox
    
    # Draw main rectangle
    cv2.rectangle(img, (x, y), (x + w, y + h), colorR, rt)
    
    # Draw corner lines
    # Top left
    cv2.line(img, (x, y), (x + l, y), colorC, t)
    cv2.line(img, (x, y), (x, y + l), colorC, t)
    
    # Top right
    cv2.line(img, (x + w, y), (x + w - l, y), colorC, t)
    cv2.line(img, (x + w, y), (x + w, y + l), colorC, t)
    
    # Bottom left
    cv2.line(img, (x, y + h), (x + l, y + h), colorC, t)
    cv2.line(img, (x, y + h), (x, y + h - l), colorC, t)
    
    # Bottom right
    cv2.line(img, (x + w, y + h), (x + w - l, y + h), colorC, t)
    cv2.line(img, (x + w, y + h), (x + w, y + h - l), colorC, t)
    
    return img
