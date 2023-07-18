

import csv
import glob
import logging
import math

import requests
from geographiclib.geodesic import Geodesic
import navpy
# Offline configuration switch
offline_config = True  # Set to True to use offline configuration
offline_swarm = True  # Set to True to use offline swarm

class DroneConfig:
    def __init__(self,drones,config_url,swarm_url,offline_config=True, offline_swarm=True, hw_id=None):
        self.hw_id = self.get_hw_id(hw_id)
        self.trigger_time = 0
        self.offline_config = offline_config
        self.offline_swarm = offline_swarm
        self.config = self.read_config()
        self.swarm = self.read_swarm()
        self.state = 0
        self.pos_id = self.get_hw_id(hw_id)
        self.mission = 0
        self.trigger_time = 0
        self.position = {'lat': 0, 'long': 0, 'alt': 0}
        self.velocity = {'vel_n': 0, 'vel_e': 0, 'vel_d': 0}
        self.yaw = 0
        self.battery = 0
        self.last_update_timestamp = 0
        self.home_position = None
        self.position_setpoint_LLA = {'lat': 0, 'long': 0, 'alt': 0}
        self.position_setpoint_NED = {'north': 0, 'east': 0, 'down': 0}
        self.velocity_setpoint_NED = {'north': 0, 'east': 0, 'down': 0}
        self.yaw_setpoint=0
        self.target_drone = None
        self.drones = drones
        self.config_url = config_url
        self.swarm_url = swarm_url
        

    def get_hw_id(self, hw_id=None):
        if hw_id is not None:
            return hw_id

        hw_id_files = glob.glob("*.hwID")
        if hw_id_files:
            hw_id_file = hw_id_files[0]
            print(f"Hardware ID file found: {hw_id_file}")
            hw_id = hw_id_file.split(".")[0]
            print(f"Hardware ID: {hw_id}")
            return hw_id
        else:
            print("Hardware ID file not found. Please check your files.")
            return None

    def read_file(self, filename, source, hw_id):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['hw_id'] == hw_id:
                    print(f"Configuration for HW_ID {hw_id} found in {source}.")
                    return row
        return None

    def read_config(self):
        if self.offline_config:
            return self.read_file('config.csv', 'local CSV file', self.hw_id)
        else:
            print("Loading configuration from online source...")
            try:
                print(f'Attempting to download file from: {self.config_url}')
                response = requests.get(self.config_url)

                if response.status_code != 200:
                    print(f'Error downloading file: {response.status_code} {response.reason}')
                    return None

                with open('online_config.csv', 'w') as f:
                    f.write(response.text)

                return self.read_file('online_config.csv', 'online CSV file', self.hw_id)

            except Exception as e:
                print(f"Failed to load online configuration: {e}")
        
        print("Configuration not found.")
        return None

    def read_swarm(self):
        """
        Reads the swarm configuration file, which includes the list of nodes in the swarm.
        The function supports both online and offline modes.
        In online mode, it downloads the swarm configuration file from the specified URL.
        In offline mode, it reads the swarm configuration file from the local disk.
        """
        if self.offline_swarm:
            return self.read_file('swarm.csv', 'local CSV file', self.hw_id)
        else:
            print("Loading swarm configuration from online source...")
            try:
                print(f'Attempting to download file from: {self.swarm_url}')
                response = requests.get(self.swarm_url)

                if response.status_code != 200:
                    print(f'Error downloading file: {response.status_code} {response.reason}')
                    return None

                with open('online_swarm.csv', 'w') as f:
                    f.write(response.text)

                return self.read_file('online_swarm.csv', 'online CSV file', self.hw_id)

            except Exception as e:
                print(f"Failed to load online swarm configuration: {e}")
        
        print("Swarm configuration not found.")
        return None
    def calculate_setpoints(self):
        self.find_target_drone()

        if self.target_drone:
            self.calculate_position_setpoint_LLA()
            self.calculate_position_setpoint_NED()
            self.calculate_velocity_setpoint_NED()
            self.calculate_yaw_setpoint()
            logging.debug(f"Setpoint updated | Position: [N:{self.position_setpoint_NED.get('north')}, E:{self.position_setpoint_NED.get('east')}, D:{self.position_setpoint_NED.get('down')}] | Velocity: [N:{self.velocity_setpoint_NED.get('vel_n')}, E:{self.velocity_setpoint_NED.get('vel_e')}, D:{self.velocity_setpoint_NED.get('vel_d')}] | following drone {self.target_drone.hw_id}, with offsets [N:{self.swarm.get('offset_n', 0)},E:{self.swarm.get('offset_e', 0)},Alt:{self.swarm.get('offset_alt', 0)}]")

        elif self.swarm.get('follow') == 0:
            print(f"Drone {self.hw_id} is a master drone and not following anyone.")
        else:
            print(f"No drone to follow for drone with hw_id: {self.hw_id}")

    def find_target_drone(self):
        # find which drone it should follow
        follow_hw_id = int(self.swarm['follow'])
        if follow_hw_id == 0:
            print(f"Drone {self.hw_id} is a master drone and not following anyone.")
        elif follow_hw_id == self.hw_id:
            print(f"Drone {self.hw_id} is set to follow itself. This is not allowed.")
        else:
            self.target_drone = self.drones[follow_hw_id]
            if self.target_drone:
                print(f"Drone {self.hw_id} is following drone {self.target_drone.hw_id}")
                pass
            else:
                print(f"No target drone found for drone with hw_id: {self.hw_id}")

    def calculate_position_setpoint_LLA(self):
        # find its setpoints
        offset_n = self.swarm.get('offset_n', 0)
        offset_e = self.swarm.get('offset_e', 0)
        offset_alt = self.swarm.get('offset_alt', 0)

        # find its target drone position
        if self.target_drone:
            # Calculate new LLA with offset
            geod = Geodesic.WGS84  # define the WGS84 ellipsoid
            g = geod.Direct(float(self.target_drone.position['lat']), float(self.target_drone.position['long']), 90, float(offset_e))
            g = geod.Direct(g['lat2'], g['lon2'], 0, float(offset_n))

            self.position_setpoint_LLA = {
                'lat': g['lat2'],
                'long': g['lon2'],
                'alt': float(self.target_drone.position['alt']) + float(offset_alt),  
            }

            # The above method calculates a new LLA coordinate by moving a certain distance 
            # in the north (latitude) and east (longitude) direction. This is an approximation, 
            # and it assumes that a degree of latitude and longitude represents the same distance 
            # everywhere on the globe. For small distances, this should be a reasonable approximation, 
            # but for larger distances, this approximation may not hold true. If more accuracy is 
            # required, one should use a more advanced method or library that can account for the 
            # curvature of the earth.

            #print(f"Position setpoint for drone {self.hw_id}: {self.position_setpoint_LLA}")
        else:
            print(f"No target drone found for drone with hw_id: {self.hw_id}")

    def calculate_position_setpoint_NED(self):
        if self.target_drone:
            self.position_setpoint_NED = self.convert_LLA_to_NED(self.position_setpoint_LLA)
            #print(f"NED Position setpoint for drone {self.hw_id}: {self.position_setpoint_NED}")
        else:
            print(f"No target drone found for drone with hw_id: {self.hw_id}")
            
    def calculate_yaw_setpoint(self):
        if self.target_drone:
            self.yaw_setpoint = self.target_drone.yaw
            #print(f"Yaw setpoint for drone {self.hw_id}: {self.yaw_setpoint}")
        else:
            print(f"No target drone found for drone with hw_id: {self.hw_id}")


    def calculate_velocity_setpoint_NED(self):
        # velocity setpoints is exactly the same as the target drone velocity
        if self.target_drone:
            self.velocity_setpoint_NED = self.target_drone.velocity
            #print(f"NED Velocity setpoint for drone {self.hw_id}: {self.velocity_setpoint_NED}")
        else:
            print(f"No target drone found for drone with hw_id: {self.hw_id}")

    def convert_LLA_to_NED(self, LLA):
        if self.home_position:
            lat = LLA['lat']
            long = LLA['long']
            alt = LLA['alt']
            home_lat = self.home_position['lat']
            home_long = self.home_position['long']
            home_alt = self.home_position['alt']

            ned = navpy.lla2ned(lat, long, alt, home_lat, home_long, home_alt)

            position_NED = {
                'north': ned[0],
                'east': ned[1],
                'down': ned[2]
            }

            return position_NED
        else:
            print("Home position is not set")
            return None
        
    def radian_to_degrees_heading(self,yaw_radians):
        # Convert the yaw angle to degrees
        yaw_degrees = math.degrees(yaw_radians)

        # Normalize to a heading (0-360 degrees)
        if yaw_degrees < 0:
            yaw_degrees += 360

        return yaw_degrees

