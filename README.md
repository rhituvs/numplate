
# License Plate Recognition using OpenCV and EasyOCR

This project is a simple implementation of License Plate Recognition (LPR) using OpenCV and EasyOCR libraries. It captures video frames from a camera, detects the license plates in those frames, saves the cropped license plate images, and then performs Optical Character Recognition (OCR) on those images to extract the license plate numbers.


## Output

### License Plate Detection




![license detect](https://user-images.githubusercontent.com/110397578/232276861-ef15f637-39b0-4549-9a6c-852fc6edda8b.png)

The output of the program displays the real-time video feed captured from the camera with the license plate detected and highlighted with a green bounding box.

### License Plate Recognition
![scaned_img_0](https://user-images.githubusercontent.com/110397578/232276952-23ee71e7-c4e7-4ab5-bca7-614a11ee7c03.jpg)

When you press the 's' key on the keyboard, the license plate image will be saved, and OCR will be performed on it to extract the license plate number. The extracted number will be printed in the console.

### Excel File

![PLATE NUM](https://user-images.githubusercontent.com/110397578/232277138-a192200d-f6d9-4506-9ab2-4836ac2c8ed0.png)

The extracted license plate number will also be saved in an Excel file named license_plate.xlsx in the following format:


## Limitations and Future Improvements
* The Haar Cascade classifier used in this project can be improved to increase the accuracy of license plate detection.
* The EasyOCR library can be replaced with other OCR libraries to improve the accuracy of license plate number extraction.
* The program can be extended to detect and recognize license plates from multiple cars in a single video frame.
