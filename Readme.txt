CCTV Footage Based Automatic Car Parking System.

1) Now in modern era , every car parking spaces must have a CCTV . My project is based on this cctv footage using the technique "Image 
Processing" . Analyzing CCTV footage , we will detect empty parking slots and non empty slots . Depending on this result we will allow 
car to enter at parking slot and before entering driver of the car can know the available slot number from a lcd display placed at the 
gate of the parking space. 

2) A special goal of this project is to stop the use of "IR Sensor" to make parking garage automated. No IR sensor is used in my project.

3) When all the parking slots are full with car and a  car is trying to enter , parking gate won't be opened and a buzzer 
will make sound. 

4) If there is any available slots , then lcd display will show free slot numbers and gate will be opened if a car wants to enter.

5) Parking gate will must open if any car wants to leave.

6) When there is available slots in parking space, the rgb will emmit green light. If there is no slots available rgb will emmit red light and if any vehicle wants to go out from parking space then rgb will emmit blue light.
About programm files -

ParkingSpacePicker - Using this programm , we will define the parking slots and entry and outro position of the parking.
We have to mark entry first , outro second. Then 1 to last . CarParkPos file generated using the positions of parking slots. 
Height and width are set manually in this programm. And this height and width value are used in next 2 programms. 

mainWithTrackbars - In this programm we have found threshold and median value .

main - This is the main file . Putted threshold and median value in this code what we got from mainWithTrackbars programm. Heigh and width are set what we got from ParkingSpacePicker. And array is generated in this programm . If any car at any slot , it will generate 1 else 0 . 

controller - Araay got from main programm . and using this value , Lcd, rgb ,servo and buzzer are controlled. 



"Demo Video of Final Project link "
https://drive.google.com/file/d/16AMruPS40tZNm3t4G5TGBcHca1skBcvq/view?usp=sharing

About the video file -
1) Left part of the video is captured by an  external phone. Check lcd display in this video very carefullly if it is displaying correctly as well as it is observed that every function of the project is working properly. "CAMERA" heading is used above it.

2) Right part of the video is our cctv footage which we analysed and depending on the data we got, we communicated with arduino .