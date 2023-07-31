# CSC-411
Mini Project

This code implements the Producer-Consumer Problem.

Where The producer function generates random student information and stores it in an ITstudents class. That is, the member variables of the ITstudent are generated using a random 
generating algorithm. The variables include Student Name, Student ID (8 digits), Programme, a list of Courses and the associated mark for each course. It then wraps the student information into an XML format and saves it to files. The XML files are placed in a directory shared with the buffer and the corresponding integer is inserted into the buffer/queue.

The consumer function reads the content of the XML files shared with the buffer and removes the corresponding integer from the buffer/queue. It then unwraps the XML files and gathers the student information into an ITstudent class. The consumer clears or deletes the XML files and calculates the average mark of the student’s courses. It then determines whether the student passed or failed and prints on screen information such as student name, ID, programme, courses and associated marks, average mark, and pass/fail information.

The code also sets up a socket connection between the producer and consumer using localhost. The producer sends the XML data over the socket connection to the consumer, which receives it and processes it in a similar manner as before.

