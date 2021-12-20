import cv2
import os
from Encoding import findEncodings
from Webcam_Recognition import webcamRecognition
path = 'D:/AMS/AttendanceManagementSystemusingFaceRecognition-master/Images'
images = []
classNames = []
classRollno = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    nameLine = os.path.splitext(cl)[0]
    nameEntry = nameLine.split(",")
    classNames.append(nameEntry[0])
    classRollno.append(nameEntry[1])

print('Encoding in progress...')
print("Staring The Webcam...")
encodeListKnown = findEncodings(images)
print('Encoding Complete!')

webcamRecognition(encodeListKnown, classNames, classRollno)
while True:
    check = False
    print("Type Attendance to Take Attendance ")
    print("Type CheckStudent to Check the Student is Present or Not")
    TakeAttendanceOrCheckStudent = str(input()).lower()
    if TakeAttendanceOrCheckStudent == "checkstudent":
        StudentName = str(input("Enter Student Name for Checking..")).upper()
        for i in classNames:
            if i == StudentName:
                check = True
        if check == True:
            print(f"Yes {StudentName} is Present In class Right Now")
        else:
            print(f"No {StudentName} is Not Present In class Right Now")
    elif TakeAttendanceOrCheckStudent == "attendance":
        print('Encoding in progress...')
        print("Staring The Webcam...")
        encodeListKnown = findEncodings(images)
        print('Encoding Complete!')
        webcamRecognition(encodeListKnown, classNames, classRollno)
    elif TakeAttendanceOrCheckStudent == "exit":
        print("Closing.....")
        exit()
    else:
        continue
