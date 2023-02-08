# Elevator System - Python

# Problem Solved:

- An elevator system, which can be initialized with `n` elevator.

- When provided input as below, it processes each request, based on simple cost functions.

- Each elevator has below capabilites :
    -  Move Up and Down
    -  Open and Close Door
    -  Start and Stop Running
    -  Display Current Status
    -  Decide weather to move up or down, given a list of request


- Elevator System takes care of :

  -   Creation of system with an array of objects of elevator.
  -   Decides which lift to associate which floor.
  -   Marks which elevator is available or busy.
  -   Can mark which elevator is operational and which is not.


# ASSUMPTION:

- Elevator System has got only one button  per elevator outside the elevator.

- So if there are a total of 5 elevators, there will be 5 buttons.

- Note that, this dosent not mimic real world, when you would have a total of 10 buttons for 5 elevators ( one for up and one for down)

- Once the elevator reaches its called point, then based on what floor is requested, it moves either up or down.

# How to Run:

sudo docker-compose build # Build your Service
sudo docker-compose up # Runs your application

# Imporvements:

1. Error handling could be improved.
2. Enhance system to have better cost functions.


