from datetime import datetime
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", user="root", passwd="yashwant12345",database='attendance')
cursor = connection.cursor()


def markAttendance(name, rollno):
    with open('D:/AMS/AttendanceManagementSystemusingFaceRecognition-master/Attendance.csv', 'r+') as f:
        nameList = []
        rollnoList = []
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            rollnoList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {rollno}, {dtString}')
            query = """INSERT INTO attendance (name, rollno, time) VALUES (%s, %s, %s)"""
            tuples = (name, rollno, dtString)
            cursor.execute(query, tuples)
            connection.commit()
            print("Attendance marked for Roll No.: " + rollno)
