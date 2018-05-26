# blockchain-python
A simple implementation of Blockchain in Python

# Blockchain Class (blockchain.py)
The Blockchain class can be used to create a blockchain object which has basic functionalities to add a block with given data to the blockchain and validate the integrity of blocks in the blockchain. Functionalities such as mining is exposed using flask

# Flask App (flaskwebapp.py)
This program has flask web app definition to expose the functionalities of blockchain to users.
It allows mining of a block using a GET request. (/mine)
It allows viewing the details of the Blockchain. (/blockchain)
It allows saving of Blockchain as a JSON file.   (/save)
