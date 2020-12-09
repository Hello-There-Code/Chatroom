# Chatroom

# Environment
The code was built and ran on Linux Ubuntu 18.04
Coded and executed in Python 2.7

# Instructions
Open terminal
Run the following lines:

    python keygen.py

    python server.py <IP> <Port>

    python client.py <IP> <Port>

# Installations
    pip install cryptography

# Test Cases
Test 1:

Input:

    python server.py 0.0.0.0
    
    python client.py 8080

Output: Please input arguments: python script, IP, Port

Test 2:

  Server Input: 
    
    python server.py 0.0.0.0 8080
    
    Enter username: John

  Server Output: 

    Listening for connections...
    127.0.0.1 has connected
    Adam has entered the chat
    Me (Enter 'quit' to close chat): ___
  
  Client Input: 

    python client.py 0.0.0.0 8080
    
    Enter username: Adam
    
  Client Output:
  
    Connecting to host...
    Successfully connected to host: 0.0.0.0
    John has entered the chat
 
Test 3:

  Server Input: 
    
    Me (Enter 'quit' to close chat): Hello
  

  Client Output:
  
    John: Hello
    Me (Enter 'quit' to close chat):
    
  Client Input: 

    Me(Enter 'quit' to close chat): quit
    
  Server Output:
  
    Adam: quit
    Chat has ended
   
  Client Output:
  
    Chat has ended
