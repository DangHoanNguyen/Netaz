# Netaz is a network analyzer with functionalities:
  - Capture Internet traffics
  - Visualize traffics
The application is created to visualize Internet traffics, from which, suspected traffics can easily be identified.
# How to run:
## Chosing the right Terminal and Python version:
  The application is runnable in Linux Terminals (Ubuntu, ...) 
  The current python version is 3.10.xx
## Install required libraries
  ```
  pip install -r "requirement.txt"
  ```
## Commands:
  - To run packet sniffer:
    ```
    python3 netaz.py <network interface> // can be eth0,...
    ```
  - Testing sniffer: Open another terminal of the same type and input command to generate Internet Traffics, for example:
    ```
    nc <domanain> <port>
    ```
  - Return to the previous terminal to terminate the capturing. And the retrieved data is stored in "logdata.json".
  - To visualize the retrieved data:
    ```
    python3 netazvisualizer.py logdata.json
    ```
  
