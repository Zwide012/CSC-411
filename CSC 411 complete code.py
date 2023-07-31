# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:12:10 2023

@author: Phathizwe and Dumane
"""

import queue
import random
import socket
import threading
import xml.etree.ElementTree as ET
from queue import Queue
from random import randint, choice




#------------------------------------------------------------------------------------------------------------------------------------

# Create a class to represent IT students
class ITstudent:
    def __init__(self, name, student_id, programme, courses):
        self.name = name
        self.student_id = student_id
        self.programme = programme
        self.courses = courses



#------------------------------------------------------------------------------------------------------------------------------------


    def to_xml(self):
        # Convert the student information to an XML format
        student = ET.Element('student')
        ET.SubElement(student, 'name').text = self.name
        ET.SubElement(student, 'student_id').text = str(self.student_id)
        ET.SubElement(student, 'programme').text = self.programme
        courses = ET.SubElement(student, 'courses')
        for course, mark in self.courses.items():
            c = ET.SubElement(courses, 'course')
            ET.SubElement(c, 'name').text = course
            ET.SubElement(c, 'mark').text = str(mark)
        return ET.tostring(student)
    
#------------------------------------------------------------------------------------------------------------------------------------

    def display_students(self):
     for student in ITstudent:
        print(f'Student Name: {student.name}')
        print(f'Student ID: {student.student_id}')
        print(f'Programme: {student.programme}')
        print('Courses:')
        for course, mark in student.courses.items():
            print(f' - {course}: {mark}')
        average_mark = sum(student.courses.values()) / len(student.courses)
        passed = average_mark >= 50
        print(f'Average Mark: {average_mark:.2f}')
        print(f'Pass/Fail: {"Pass" if passed else "Fail"}')
        print()

#------------------------------------------------------------------------------------------------------------------------------------            


    @staticmethod
    def from_xml(xml_string):
        # Convert an XML string to a student object
        root = ET.fromstring(xml_string)
        name = root.find('name').text
        student_id = int(root.find('student_id').text)
        programme = root.find('programme').text
        courses = {}
        for course in root.find('courses'):
            course_name = course.find('name').text
            mark = int(course.find('mark').text)
            courses[course_name] = mark
        return ITstudent(name, student_id, programme, courses)
    
#------------------------------------------------------------------------------------------------------------------------------------    
    
    

    def get_average_mark(self):
        # Calculate the average mark of the student's courses
        total_marks = sum(self.courses.values())
        num_courses = len(self.courses)
        return total_marks / num_courses
    
#------------------------------------------------------------------------------------------------------------------------------------    
    
    

    def has_passed(self):
        # Determine if the student has passed (average mark >= 50%)
        return self.get_average_mark() >= 50
    
    
#------------------------------------------------------------------------------------------------------------------------------------    

# Create a buffer with a maximum size of 10 elements
buffer = Queue(maxsize=10)



#------------------------------------------------------------------------------------------------------------------------------------
# Define the producer function



def producer():
    # Generate random student information and store it in an ITstudents class
    for i in range(10):
        
     first_names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
     last_names = ['Doe', 'Smith', 'Johnson']

    programmes = ['Computer Science', 'Information Technology', 'Software Engineering']
    courses_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    for i in range(1, 12):
        full_name=random.choice(first_names)+" "+random.choice(last_names)
        student_id = randint(10000000, 99999999)
        programme = choice(programmes)
        courses = {course: randint(0, 100) for course in courses_list}
        student = ITstudent(full_name, student_id, programme, courses)

        # Wrap the student information into an XML format and save it to a file
        xml_data = student.to_xml()
        with open(f'student{i}.xml', 'wb') as f:
            f.write(xml_data)
            
            
#------------------------------------------------------------------------------------------------------------------------------------            


# Place the XML file in a directory shared with the buffer and insert the corresponding integer into the buffer/queue
        buffer.put(i)


#------------------------------------------------------------------------------------------------------------------------------------


# Define the consumer function
def consumer():
    while not buffer.empty():
        # Read the content of the XML file shared with the buffer and remove the corresponding integer from the buffer/queue
        i = buffer.get()
        
         # Unwrap the XML file and gather the student information into an ITstudent class 
    with open(f'student{i}.xml', 'rb') as f:
             xml_data = f.read()
    student = ITstudent.from_xml(xml_data)
    

#------------------------------------------------------------------------------------------------------------------------------------
    

         # Clear or delete the XML file 
    open(f'student{i}.xml', 'w').close()

         # Calculate the average mark and determine whether the student passed or failed 
    average_mark = student.get_average_mark()
    passed = student.has_passed()
    

#------------------------------------------------------------------------------------------------------------------------------------
    
    
    # To display the student record
    
    def display_students (self) :
       for student in self.students:
           student.display()
           
           print()

#------------------------------------------------------------------------------------------------------------------------------------
        
 # Print on screen information such as student name, ID, programme, courses and associated marks, average mark, and pass/fail information 
    
 
 
    print(f'Student Name: {student.name}')
    print(f'Student ID: {student.student_id}')
    print(f'Programme: {student.programme}')
    print('Courses:')
    for course, mark in student.courses.items():
             print(f' - {course}: {mark}')
    print(f'Average Mark: {average_mark:.2f}')
    print(f'Pass/Fail: {"Pass" if passed else "Fail"}')
    print()
    
    
    
#------------------------------------------------------------------------------------------------------------------------------------    

# Start the producer and consumer threads
if __name__ == '__main__':
    buffer = queue.Queue()
    directory = '.'
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()

#------------------------------------------------------------------------------------------------------------------------------------


# Set up socket connection between producer and consumer using localhost
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#client_socket.connect(('localhost', 12345))
conn, addr = server_socket.accept()


#------------------------------------------------------------------------------------------------------------------------------------


# Send the XML data from the producer to the consumer over the socket connection
for i in range(1, 12):
    with open(f'student{i}.xml', 'rb') as f:
        xml_data = f.read()
    conn.sendall(xml_data)



#------------------------------------------------------------------------------------------------------------------------------------


# Receive the XML data on the consumer side and process it
while True:
    xml_data = client_socket.recv(1024)
    if not xml_data:
        break
    student = ITstudent.from_xml(xml_data)
    average_mark = student.get_average_mark()
    passed = student.has_passed()
    print(f'Student Name: {student.name}')
    print(f'Student ID: {student.student_id}')
    print(f'Programme: {student.programme}')
    print('Courses:')
    for course, mark in student.courses.items():
        print(f' - {course}: {mark}')
    print(f'Average Mark: {average_mark:.2f}')
    print(f'Pass/Fail: {"Pass" if passed else "Fail"}')
    print()

#------------------------------------------------------------------------------------------------------------------------------------

#Close the socket connections
conn.close()
client_socket.close()
server_socket.close()



 
   
 
