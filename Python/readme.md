-------------
Intro
-------------

Python Tag Parser for Ignition SCADA</br>
Created by James Windham
Created on Dec 9, 2022
Personal Email: jwindham94@gmail.com
Business Email: windhamllc1@gmail.com


This is the readme for the pyTagParse program located in this folder.

![image](https://user-images.githubusercontent.com/25441533/206825520-ecbde5b2-f7cb-4ee5-baef-ab9bcd10b5e2.png)

This program was written by me to solve the problem of having no way of parsing through Ignition SCADA tag exports from the tag browser. The old solution was 1/2 day or more of copypasting and hating life after someone requests a pull of tags from the browser. This program will solve that issue.

-------------
Instructions
-------------

instructions are simple. Follow the steps on the screen since there are only two.

1. Choose JSON tag export file. This should be the file Ignition gives you after exporting in JSON format.
2. Choose export location. This will be the location that the CSV conversion will be saved.
  2.1. Choose whether you will be opening the file in MS Excel after it is completed. This will be set to YES as default.
  
-------------
Usage
-------------

This should only be used for Igntion tag export files in JSON format. Anything else will not work.

I am currently working on adding in XML tag export functionality for transaction group exports.
