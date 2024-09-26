# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:33:21 2022

@author: adars
"""

import datetime
import hashlib
import json
import requests
from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse

#  Building a Medical Virtualchain

class Medicalchain:
    
    def __init__(self):
        self.virtualchain = []
        self.medical_sessions = []
        self.create_session(previous_hash = '0')
        self.devices = set()
    def create_session(self, previous_hash):
        session = {'session_index': len(self.virtualchain) + 1,
                 'timestamp': str( datetime.datetime.now()),
                 'previous_hash': previous_hash,
                 'medical_sessions': self.medical_sessions
                 }
        self.medical_sessions = []
        self.virtualchain.append(session)
        return session
    
    def obtain_previous_session(self):
        return self.virtualchain[-1]

    
    def hash(self, session):
        encoded_session = json.dumps(session, sort_keys = True).encode()
        return hashlib.sha256(encoded_session).hexdigest()
    
    def is_session_genuine(self,chain):
        previous_session = chain[0]
        session_index = 1
        while session_index < len(chain):
            session = chain[session_index]
            if session['previous_hash'] != self.hash(previous_session):
                return False
            previous_session= session
            session_index += 1
            return True
        
    def add_patient_data(self, patientID, receiver ):
        self.medical_sessions.append({'patientID': patientID,
                                  'receiver': receiver})
        previous_session = self.obtain_previous_session()
        return previous_session['session_index'] + 1
    
    def connect_device(self, address):
        parsed_url = urlparse(address)
        self.devices.add(parsed_url.netloc)
 
    def update_chain(self):
        network = self.devices
        updated_chain = None
        max_length = len(self.virtualchain)
        for device in network:
            response  = requests.get(f'http://{device}/obtain_chain')
            if response.status_code == 200:
                length = response.json()['length']
                virtualchain  = response.json()['virtualchain']
                if length > max_length and self.is_session_genuine(virtualchain):
                    max_length = length
                    updated_chain = virtualchain
        if updated_chain:
            self.virtualchain = updated_chain
            return True

        return False
    

# Creating a Web App
app = Flask(__name__)

# Creating an address for the device on port 5000 
device_address = str(uuid4()).replace('-','')

medicalchain = Medicalchain()

# Adding new sessions
@app.route('/add_session',methods=['GET'])
def add_session():
    previous_session = medicalchain.obtain_previous_session()
    previous_hash = medicalchain.hash(previous_session)
    medicalchain.add_patient_data(patientID = device_address, receiver='Medical_Server')
    session = medicalchain.create_session(previous_hash)
    response = {'message': 'Session appended',
                'session_index': session['session_index'],
                'timestamp':session['timestamp'],
                'previous_hash': session['previous_hash'],
                'medical_sessions': session['medical_sessions']
                }
    return jsonify(response), 200

# Obtain and see the chain
@app.route('/obtain_chain',methods=['GET'])
def obtain_chain():
    response = {'virtualchain': medicalchain.virtualchain,
                'length':len(medicalchain.virtualchain) }
    return jsonify(response), 200

#  Verify the chain whether it is valid or not
@app.route('/verify_chain',methods=['GET'])
def verify_chain():
    verify_chain  = medicalchain.is_session_genuine(medicalchain.virtualchain)
    if verify_chain:
        response = {'message':'All inforamtion verified in  Chain'}
    else:
        response = {'message':'Invalid Inforamtion Detected. Verification Failed'}
    return jsonify(response), 200


# Adding Patient info to the chain

@app.route('/add_patient_data',methods=['POST'])
def add_patient_data():
    json = request.get_json()
    patient_datas = ['patientID','receiver']
    if not all (data in json for data in  patient_datas):
        return 'Some datas of the session are missing', 400
    session_index = medicalchain.add_patient_data(json['patientID'],json['receiver'])
    response = {'message': f'This data will be added to chain {session_index}' }
    return jsonify(response), 201

#  Distributed Network

# connect devices
@app.route('/connect_device',methods=['POST'])
def connect_device():
    json = request.get_json()
    devices = json.get('devices')
    if devices is None:
        return "No device", 400
    for device in devices:
        medicalchain.connect_device(device)
    response = {'message': f'{"Devices are  connected"}',
                'All_devices': list(medicalchain.devices)}
    return jsonify(response), 201

# Updating the chain
@app.route('/update_chain',methods=['GET'])
def update_chain():
    is_valid_updated  = medicalchain.update_chain()
    if is_valid_updated:
        response = {'message':'Medical Chain Updated',
                    'updated_chain': medicalchain.virtualchain }
    else:
        response = {'message':'Medical Chain is up to date',
                    'present_chain': medicalchain.virtualchain}
    return jsonify(response), 200

# Initiate the application
app.run(host = '0.0.0.0',port = 5003)