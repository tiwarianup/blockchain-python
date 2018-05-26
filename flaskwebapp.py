# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:32:25 2018

@author: anuptiwari
"""

# Required modules import 
import json
import string
from random import randint, choice
from flask import Flask, jsonify
from blockchain import Blockchain

#Web app code using Flask module
#app definition
app = Flask(__name__)

#Blockchain instance creation
blockchain = Blockchain()

#Mining a new block using get request
@app.route('/mine', methods = ['GET'])
def mineBlock():
    prevBlock = blockchain.getPrevBlock()
    prevProof = prevBlock['proof']
    proof     = blockchain.proofofWork(prevProof)
    prevHash  = blockchain.blockHash(prevBlock)
    #Some random data to populate in the blockchain
    data      = {
            'randomNumber': str(randint(1000, 9999)),
            'randomString': ''.join(choice(string.ascii_letters) for m in range(25))
            }
    #Creating a block with inputs
    block     = blockchain.createBlock(proof, prevHash, data)
    #Generating a response back to user
    response  = {'message': 'Congrats! A block was successfully mined with attributes.',
                 'index': block['index'],
                 'timestamp':block['timestamp'],
                 'proof':block['proof'],
                 'previous_hash':block['previous_hash'],
                 'data':block['data']
                 }
    #Returning the response and status code
    return jsonify(response), 200

@app.route('/blockchain', methods = ['GET'])
def getBlockchain():
    #Generating a response back to user
    #A dictionary with the blockchain and its length as key-value pair
    response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
            }
    #Returning the response and status code
    return jsonify(response), 200

@app.route('/save', methods=['GET'])
def saveBlockchain():
    #Saving blockchain data to a JSON file
    data = blockchain.chain
    with open('blockchain-json.json', 'w') as outfile:
        json.dump(data, outfile)
    response  = {'message': 'The blockchain was saved to JSON file'}
    #Returning the response and status code
    return jsonify(response), 200

#Running the flask app on localhost at port 5000
app.run(host = 'localhost', port = 5000)


