import math
from math import cos as cos
from math import sin as sin
from math import pow as pow
from math import pi as pi

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track'] #: Boolean,        # flag to indicate if the agent is on the track
    #locX = paramsparams['x'] #: float,                            # agent's x-coordinate in meters
    #locY = params['y'] #: float,                            # agent's y-coordinate in meters
    is_crashed = params['is_crashed'] #: Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    is_left_of_center = params['is_left_of_center'] #: Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    is_offtrack = params['is_offtrack'] #: Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    is_reversed = params['is_reversed'] #: Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading = params['heading'] #: float,                      # agent's yaw in degrees

    progress = params['progress'] #: float,                     # percentage of track completed
    speed = params['speed'] #: float,                        # agent's speed in meters per second (m/s)
    steering_angle = params['steering_angle'] #: float,               # agent's steering angle in degrees
    #steps = params['steps'] #: int,                          # number steps completed
    #track_length = params['track_length'] #: float,                 # track length in meters.
    #waypoints = params['waypoints'] #: [(float, float), ]        # list of (x,y) as milestones along the track center
    
    velocity_vector = [math.cos(heading*math.pi/180), math.sin(heading*math.pi/180)]
    persistent_vel_vector = velocity_vector
    # assume no reward at first
    reward = 0
    
    # increase points for getting further down the track
    # if you make it all the way, 100 pts
    #reward += progress - last_progress
    #last_progress = progress # so apparently you can't have persistent variables here
    
    
    # slight penalty if not all wheels on the track
    reward -= 5 * float(not all_wheels_on_track)
    
    # larger penalty if completely off track
    reward -= 20 * float(is_offtrack)
    
    # another large penalty if crashed
    reward -= 25 *float(is_crashed)
    reward -= 25 * float(is_reversed)
    
    # penalize for steering too much while going fast
    reward += math.pow(speed,-math.cos(2*steering_angle*math.pi/180))
    # spd*cos(2*ang*pi/180)^2 + (cos(2*ang*pi/180)*cos(2*a*pi/180)^(2*spd))/(spd^(1/2) + 1)
    spd = speed
    ang2 = steering_angle * 2*pi/180
    reward += spd*(pow(cos(ang2),2)) + (cos(ang2)*pow(cos(ang2),2*spd))/(pow(spd,0.5)+1)
    
    
    reward += pow(10,-distance_from_center)
    
    return float(reward)