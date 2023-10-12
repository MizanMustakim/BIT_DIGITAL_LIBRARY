import cv2
import pytesseract
import spacy
import re

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

def extract(image_path):
    image = cv2.imread(image_path)

    # Define the new dimensions (width, height) for resizing
    new_width = 400  # Set your desired width
    new_height = 400  # Set your desired height

    # Resize the image
    image = cv2.resize(image, (new_width, new_height))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to automatically determine the threshold
    thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Use a larger rect_kernel to capture larger regions
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))

    # Increase the number of iterations for more dilation
    dilation = cv2.dilate(thresh, rect_kernel, iterations=2)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    image_copy = image.copy()
    
    # Define Regions of Interest (ROIs) as rectangular areas
    title_roi = (50, 00, 350, 220)  # Example: (x, y, width, height) for the title region
    author_roi = (50, 220, 350, 180)  # Example: (x, y, width, height) for the author region

    title_x, title_y, title_w, title_h = title_roi
    author_x, author_y, author_w, author_h = author_roi
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        print(x,y,w,h)
        cropped = image_copy[y : y + h, x : x + w]

        title_cropped = cropped[title_y:title_y+title_h, title_x:title_x+title_w]
        author_cropped = cropped[author_y:author_y+author_h, author_x:author_x+author_w]

        title = str(nlp(pytesseract.image_to_string(title_cropped)))
        author = str(nlp(pytesseract.image_to_string(author_cropped)))
        
        
        # Print the extracted title and author
        print("Title:", title.replace("\n", " "))
        print("Author:", author.strip())
        # print("Edition:", edition_number.strip())
        print("------------------")

        return title.replace("\n", " "), author.replace("\n", ", ")

if __name__ == "__main__":
    image_path = "./linear algebra book.jpg"
    extract(image_path)
