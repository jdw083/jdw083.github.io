-------------
Intro
-------------

Python Tag Parser for Ignition SCADA</br>
Created by James Windham</br>
Created on Dec 9, 2022</br>
Personal Email: jwindham94@gmail.com</br>
Business Email: windhamllc1@gmail.com</br>


This is the readme for the pyTagParse program located in this folder.

![image](https://user-images.githubusercontent.com/25441533/207164168-318d0079-1744-4878-b5ac-cf4f0a6ce68f.png)
![image](https://user-images.githubusercontent.com/25441533/207168037-e38a0832-601b-409b-8c93-f2675fed8fa8.png)
![image](https://user-images.githubusercontent.com/25441533/207168116-734762e1-385a-415b-9ac0-336ebcd823c1.png)
![image](https://user-images.githubusercontent.com/25441533/207168174-aa27cfd4-c8cb-476b-8877-0be784104360.png)




This program was written by me to solve the problem of having no way of parsing through Ignition SCADA PLC tag exports from the tag browser. The old solution was 1/2 day or more of copypasting and hating life after someone requests a pull of PLC tags from the SCADA browser. This program will solve that issue.

-------------
Instructions
-------------

instructions are simple. Follow the steps on the screen since there are only two.

1. Choose JSON or XML tag export file. This should be the file Ignition gives you after exporting in JSON or XML format.</br>
2. Choose export location. This will be the location that the CSV conversion will be saved.</br>
  2.1. Choose whether you will be opening the file in MS Excel after it is completed. This will be set to YES as default.</br>
  
-------------
Usage
-------------

This should only be used for Igntion tag export files in JSON or XML format. Anything else will not work.

12/12/2022:

I have added XML functionality to write out Ignition transaction groups into pipe-delimited CSV (or PSV to be exact)
