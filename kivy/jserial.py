# coding: UTF-8

import serial
import json

class Jserial:

    def __init__(self, comm, rate):
        self.ser = serial.Serial(comm, rate)

    def __del__(self):
        self.ser.close()

    def get_dict(self):
        self.read_data = self.ser.readline()
        self.dict = json.loads(self.read_data)
        return self.dict

