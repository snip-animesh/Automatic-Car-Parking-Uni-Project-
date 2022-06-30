Automatic Car Parking System Analyzing CCTV Footage

1) When all the parking slots are full with car and a  car is trying to enter , parking gate won't be opened and a buzzer 
will make sound. 

2) If there is any available slots , then lcd display will show free slot numbers and gate will be opened if a car wants to enter.


About programm files -

ParkingSpacePicker - Using this programm , we will define the parking slots and entry and outro position of the parking.
We have to mark entry first , outro second. Then 1 to last . CarParkPos file generated using the positions of parking slots. 
Height and width are set manually in this programm. And this height and width value are used in next 2 programms. 

mainWithTrackbars - In this programm we have found threshold and median value .

main - This is the main file . Putted threshold and median value in this code what we got from mainWithTrackbars programm. Heigh and width are set what we got from ParkingSpacePicker. And array is generated in this programm . If any car at any slot , it will generate 1 else 0 . 

controller - Araay got from main programm . and using this value , Lcd, rgb ,servo and buzzer are controlled. 

Resources are used before getting real cctv footage . and dataGenerator programm is used before getting real cctv footage to check
hardware parts response.


"Demo Video of Final Project link "
https://drive.google.com/file/d/16AMruPS40tZNm3t4G5TGBcHca1skBcvq/view?usp=sharing