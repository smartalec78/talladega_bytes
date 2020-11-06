import math

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # list out all available params
    all_wheels_on_track = params['all_wheels_on_track'] #: Boolean,        # flag to indicate if the agent is on the track
    #locX = paramsparams['x'] #: float,                            # agent's x-coordinate in meters
    #locY = params['y'] #: float,                            # agent's y-coordinate in meters
    #closest_objects = params['closest_objects'] #: [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    #closest_waypoints = params['closest_waypoints'] #: [int, int],       # indices of the two nearest waypoints.
    distance_from_center = params['distance_from_center'] #: float,         # distance in meters from the track center 
    is_crashed = params['is_crashed'] #: Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    is_left_of_center = params['is_left_of_center'] #: Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    is_offtrack = params['is_offtrack'] #: Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    is_reversed = params['is_reversed'] #: Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading = params['heading'] #: float,                      # agent's yaw in degrees
    #objects_distance = params['objects_distance'] #: [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    #objects_heading = params['objects_heading'] #: [float, ],          # list of the objects' headings in degrees between -180 and 180.
    #objects_left_of_center = params['objects_left_of_center'] #: [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    #objects_location = params['objects_location'] #: [(float, float),], # list of object locations [(x,y), ...].
    #objects_speed = params['objects_speed'] #: [float, ],            # list of the objects' speeds in meters per second.
    progress = params['progress'] #: float,                     # percentage of track completed
    speed = params['speed'] #: float,                        # agent's speed in meters per second (m/s)
    steering_angle = params['steering_angle'] #: float,               # agent's steering angle in degrees
    #steps = params['steps'] #: int,                          # number steps completed
    #track_length = params['track_length'] #: float,                 # track length in meters.
    #track_width = params['track_width'] #: float,                  # width of the track
    #waypoints = params['waypoints'] #: [(float, float), ]        # list of (x,y) as milestones along the track center
    
    # assume no reward at first
    reward = 0
    
    # increase points for getting further down the track
    # if you make it all the way, 100 pts
    reward += progress
    
    
    
    # slight penalty if not all wheels on the track
    reward -= 5 * float(not all_wheels_on_track)
    
    
    # larger penalty if completely off track
    reward -= 20 * float(is_offtrack)
    
    
    # another large penalty if crashed
    reward -= 25 *float(is_crashed)
    reward -= 25 * float(is_reversed)
    
    
    # penalize for steering too much while going fast
    reward += speed*math.cos(steering_angle*math.pi/180)
    
    reward += math.pow(10,-distance_from_center)
    
    
    
    return float(reward)