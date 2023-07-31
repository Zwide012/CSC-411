# CSC-411
Mini Project

This code implements the Producer-Consumer Problem.

Where The producer function generates random student information and stores it in an ITstudents class. It then wraps the student information into an XML format and saves it to a file. The XML file is placed in a directory shared with the buffer and the corresponding integer is inserted into the buffer/queue.

The consumer function reads the content of the XML file shared with the buffer and removes the corresponding integer from the buffer/queue. It then unwraps the XML file and gathers the student information into an ITstudent class. The consumer clears or deletes the XML file and calculates the average mark of the student’s courses. It then determines whether the student passed or failed and prints on screen information such as student name, ID, programme, courses and associated marks, average mark, and pass/fail information.

The code also sets up a socket connection between the producer and consumer using localhost. The producer sends the XML data over the socket connection to the consumer, which receives it and processes it in a similar manner as before.

