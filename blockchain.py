# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:38:13 2018
Blockchain.py 
@author: anuptiwari
"""

# Required modules import 
import datetime
import hashlib #Used for generating hashes of data
import json

# Blockchain class starts here

class Blockchain:
    
    #Constructor definition
    def __init__(self):
        # A blockchain initialized to empty list
        self.chain = []
        # Initializing the `Genesis` block
        self.createBlock(proof = 1, prevHash = '0', data = {})
    
    #Method to create a block with proof of work & hash from previous block
    def createBlock(self, proof, prevHash, data):
        newBlock = {
            'index': len(self.chain) + 1,              #block index
            'timestamp': str(datetime.datetime.now()), #current time
            'proof': proof,                            #proof of work (nonce)
            'previous_hash': prevHash,                 #hash from previous block
            'data': data
        }
        #Appending the new block to the blockchain
        self.chain.append(newBlock)
        return newBlock
    
    
    def getPrevBlock(self):
        return self.chain[-1]
    
    
    def proofofWork(self, prevProof):
        newProof = 1
        validProof = False
        while validProof is False:
            proofHash = hashlib.sha256(str(newProof**2 - prevProof**2).encode()).hexdigest()
            if proofHash[:4] == '0000':
                validProof = True
            else:
                newProof += 1
        return newProof
    
    def blockHash(self, block):
        encodedBlock = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    
    def isValidChain(self, chain):
        prevBlock = chain[0]
        blockIndex = 1
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block['prevHash'] != self.hash(prevBlock):
                return False
            prevProof = prevBlock['proof']
            proof = block['proof']
            proofHash = hashlib.sha256(str(proof**2 - prevProof**2).encode()).hexdigest()
            if proofHash[:4] != '0000':
                return False
            prevBlock = block
            blockIndex += 1
        return True
