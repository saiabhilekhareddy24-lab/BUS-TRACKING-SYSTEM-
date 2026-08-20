Bus Tracking System Using Python
1. Introduction

The Bus Tracking System is a Python-based simulation project designed to track the real-time location and status of buses operating on predefined routes.

The system simulates multiple buses moving along different routes and displays information such as:

Bus ID
Current location
Speed
Route
Bus status
Simulation time

This project demonstrates the basic concepts behind a GPS-based public transportation tracking system.

2. Objectives

The main objectives of this project are:

To simulate real-time bus movement.
To track the location of multiple buses.
To display bus speed and status.
To provide a simple testbench for verifying the tracking system.
To demonstrate how Python can be used to develop a transportation monitoring application.
3. Technologies Used
Python 3
Object-Oriented Programming
Mathematical calculations
Unit testing
GitHub
4. System Architecture
             +------------------+
             |   Bus Database   |
             +--------+---------+
                      |
                      v
             +------------------+
             | Route Management |
             +--------+---------+
                      |
                      v
             +------------------+
             | Bus Tracking     |
             | Simulation       |
             +--------+---------+
                      |
                      v
             +------------------+
             | Location/Status  |
             | Display          |
             +------------------+

5. Features
Multiple Bus Tracking

The system can simulate multiple buses simultaneously.

Route Tracking

Each bus follows a predefined route consisting of multiple coordinate points.

Speed Monitoring

The speed of each bus is stored and displayed during the simulation.

Location Tracking

The current X-Y coordinates of each bus are calculated at every simulation step.

Status Monitoring

The system reports whether a bus is operating normally or is stopped.

6. How the Simulation Works

Each bus has:

A unique bus ID
A route
A speed
A current position

The simulation divides the route into sections and calculates the bus position between two points using interpolation.

For example:

Stop A -------- Stop B -------- Stop C
(0,0)             (5,2)             (10,4)


The bus position changes gradually between the stops.

7. Installation

Clone the project:

git clone https://github.com/YOUR_USERNAME/bus-tracking-system.git
cd bus-tracking-system


No external Python packages are required.

Run the main program:

python bus_tracking.py


Run the testbench:

python -m unittest test_bus_tracking.py

8. Example Output
BUS TRACKING SYSTEM
===================

Time: 0 min
B01 | Location: (0.00, 0.00) | Speed: 25.0 km/h | Status: RUNNING
B02 | Location: (10.00, 0.00) | Speed: 25.0 km/h | Status: RUNNING
B03 | Location: (0.00, 4.00) | Speed: 25.0 km/h | Status: RUNNING

Time: 5 min
B01 | Location: (4.84, 2.00) | Speed: 20.2 km/h | Status: RUNNING
B02 | Location: (4.00, 3.00) | Speed: 20.2 km/h | Status: RUNNING
B03 | Location: (5.00, 3.00) | Speed: 20.2 km/h | Status: RUNNING


The exact numerical output can vary depending on the simulation parameters.

9. Testing

The project includes a Python unittest testbench.

The testbench verifies:

Bus creation
Route validity
Position calculation
Speed values
Bus status
10. Future Enhancements

The project can be extended by adding:

GPS integration
Google Maps/OpenStreetMap integration
Graphical user interface
Web-based dashboard
Database connectivity
Passenger mobile application
Estimated arrival time
Bus stop notifications
Traffic-aware route calculation
11. Conclusion

The Bus Tracking System demonstrates how Python can be used to simulate a basic real-time public transportation tracking application.

Although this project uses simulated coordinates instead of physical GPS devices, the same basic concepts can be extended to a real-world bus tracking system.

12. Author

Student Project - Bus Tracking System

Built using Python.
