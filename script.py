import cv2
import pytesseract
from PIL import Image
import sys


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# originalImage= cv2.imread(r'E:\python\image to text\ronak10th.jpeg')
image_path = r"E:\project\node\pj\python\ronak10th.jpeg"
originalImage = cv2.imread(image_path)


grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

(thresh, threshold_img) = cv2.threshold(originalImage, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('Black white image', threshold_img)

# cv2.imshow('Original image',originalImage)
# cv2.imshow('Gray image', grayImage)

# cv2.imwrite(r'E:\python\image to text\savedimage.jpeg',grayImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# configuring parameters for tesseract

custom_config = r"--oem 3 --psm 6"

# now feeding image to tesseract

details = pytesseract.image_to_data(
    threshold_img, output_type=pytesseract.Output.DICT, config=custom_config, lang="eng"
)



total_boxes = len(details["text"])

for sequence_number in range(total_boxes):

    if int(details["conf"][sequence_number]) > 30:

        (x, y, w, h) = (
            details["left"][sequence_number],
            details["top"][sequence_number],
            details["width"][sequence_number],
            details["height"][sequence_number],
        )

        threshold_img = cv2.rectangle(
            threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2
        )

# display image

# cv2.imshow('captured text', threshold_img)
# cv2.imwrite(r'E:\python\image to text\savedimage.jpeg',threshold_img)

# Maintain output window until user presses a key

# cv2.waitKey(0)

# Destroying present windows on screen

# cv2.destroyAllWindows()

parse_text = []

word_list = []

last_word = ""

for word in details["text"]:

    if word != "":

        word_list.append(word)

        last_word = word

    if (last_word != "" and word == "") or (word == details["text"][-1]):

        parse_text.append(word_list)

        word_list = []


import csv
import os

with open("result_text.txt", "w", newline="") as file:

    csv.writer(file, delimiter=" ").writerows(parse_text)

text_file = open("result_text.txt", "r")
recognized_text = text_file.read()
text_file.close()
if os.path.exists("result_text.txt"):
    os.remove("result_text.txt")


def get_details(st_name, st_roll_no, total_marks_got):
    # y=list(student_tuple)
    # print("Enter the following details:")
    # st_name=input("Name:")
    # st_roll_no = input("Roll no:")
    # total_marks_got=input("Enter the total marks received:")
    y = []
    y.append(st_name)
    y.append(st_roll_no)
    y.append(total_marks_got)
    return tuple(y)


# student_tuple=()
# student_tuple=get_details(student_tuple)           # input data
# print(student_tuple)
student_tuple = get_details("RONAK GUPTA", "1692289", "516")

import re

# searching the input data in extracted text
def search_data_from_extr(student_tuple):
    count = 0
    for i in range(0, len(student_tuple)):
        if re.search(student_tuple[i], recognized_text):
            count += 0
        else:
            count += 1
    return count


error_count = search_data_from_extr(student_tuple)
if error_count > 0:
    print("not verified")
else:
    print("verified")
