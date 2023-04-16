import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
import glob
import pandas as pd
import os

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) == ord('q'):
        break

    elif cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
        reader = easyocr.Reader(["en"])
        image_files = glob.glob("plates/*.jpg")
        latest_image_file = max(image_files, key=os.path.getctime)

        # Recognize text in the latest saved image
        result = reader.readtext(latest_image_file)
        plate_text = ''
        for text in result:
            if text[1].isalnum() and text[1].isupper():
                plate_text += text[1] + " "
        print(plate_text)

        # Create a new DataFrame to store the license plate information
        df = pd.DataFrame({'No': [count], 'License_plate': [plate_text]})

        # Check if the file already exists
        if os.path.exists('license_plate.xlsx'):
            # Append the new data to the existing file
            existing_df = pd.read_excel('license_plate.xlsx')
            updated_df = existing_df.append(df, ignore_index=True)
            updated_df.to_excel('license_plate.xlsx', index=False)
        else:
            # Save the new data to a new file
            df.to_excel('license_plate.xlsx', index=False)
