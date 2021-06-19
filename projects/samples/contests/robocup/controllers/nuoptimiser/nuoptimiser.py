# NUbots 2021

from controller import Supervisor, AnsiCodes, Node

import socket

# protobuf
import simulator_message_pb2

def main():
    # start the webots supervisor
    supervisor = Supervisor()
    time_step = int(supervisor.getBasicTimeStep())
    time_count = 0
    print("hello world")
    
    print(make_optimiser_sensor_measurements_message())
    print("-- DIVIDER --")
    print(make_optimiser_sensor_measurements_message().SerializeToString())

    # with open('log.txt', 'w') as log_file:

def make_message(msg_type, text):
    msg = simulator_message_pb2.Message()
    if msg_type == "warning_msg":
        msg.message_type = simulator_message_pb2.Message.MessageType.WARNING_MESSAGE
    else:
        msg.message_type = simulator_message_pb2.Message.MessageType.ERROR_MESSAGE
    msg.text = text
    return msg

def add_accelerometer(message, name):
    accel = message.accelerometers.add()
    accel.name = name
    accel.value.X = 1
    accel.value.Y = 2
    accel.value.Z = 3

def add_gyro(message, name):
    gyro = message.gyros.add()
    gyro.name = name
    gyro.value.X = 1
    gyro.value.Y = 2
    gyro.value.Z = 3

def add_robot_position(message, name):
    pos = message.robot_position.add()
    pos.name = name
    pos.value.X = 1
    pos.value.Y = 2
    pos.value.Z = 3

def make_optimiser_sensor_measurements_message():
    message = simulator_message_pb2.OptimiserSensorMeasurements()
    message.time = 1
    message.real_time = 2
    add_accelerometer(message, "arm")
    add_accelerometer(message, "leg")
    add_gyro(message, "arm")
    add_gyro(message, "leg")
    add_robot_position(message, "robot1")
    return message

def udp_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def udp_recieve():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes



main()