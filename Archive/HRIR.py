import scipy.io as scp # used to load .mat file
import numpy as np
import sys

try:
    hrtf_db = scp.loadmat('CIPIC_58_HRTF.mat')
except RuntimeError:
    print("ERROR: couldn't load in the matlab file")
    sys.exit(0)

HRIR_LEFT = hrtf_db['hrir_l']
HRIR_RIGHT = hrtf_db['hrir_r']


def find_min(current_val):
    while True:
        current_val = current_val - 1
        min_exists = current_val in AZIMUTH_VALUES
        if min_exists:
            return current_val
            break


def find_max(current_val):
    while True:
        current_val = current_val + 1
        max_exists = current_val in AZIMUTH_VALUES
        if max_exists:
            return current_val
            break


def interpolate(user_azimuth, elevation):
    user_azimuth = round(user_azimuth)
    azimuth_max = find_max(user_azimuth)
    azimuth_min = find_min(user_azimuth)
    leftMin_HRIR = np.array(HRIR_LEFT_HASH[elevation][azimuth_min])  # an array of integers
    leftMax_HRIR = np.array(HRIR_LEFT_HASH[elevation][azimuth_max])
    rightMin_HRIR = np.array(HRIR_RIGHT_HASH[elevation][azimuth_min])
    rightMax_HRIR = np.array(HRIR_RIGHT_HASH[elevation][azimuth_max])
    scale_factor = abs(user_azimuth - azimuth_min) / abs(azimuth_max - azimuth_min)
    # multiply an array of integers(HRIR) by the scale factor
    left_hrir = (1 - scale_factor) * leftMin_HRIR + scale_factor * leftMax_HRIR
    right_hrir = (1 - scale_factor) * rightMin_HRIR + scale_factor * rightMax_HRIR
    # printing hrir values in a 1 by 20 array
    left_hrir_vals = []
    right_hrir_vals = []
    for val in left_hrir:
       left_hrir_vals.append(val)

    for val in right_hrir:
        right_hrir_vals.append(val)
    return left_hrir_vals, right_hrir_vals


HRIR_LEFT_HASH = {"Elevation 0": {},
                  "Elevation 180": {}}
HRIR_RIGHT_HASH = {"Elevation 0": {},
                   "Elevation 180": {}}

MISSING_VALUES = [-75, -70, -60, -50, 75, 70, 60, 50]
AZIMUTH_VALUES = [-80, -65, -55, -45, 40, -35, 30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 65, 80]


def initialize(elevation, elevation_index):
    azimuth_index = 0
    for azimuth in range(-80, 81):
        if azimuth % 5 == 0 and azimuth not in MISSING_VALUES:
            HRIR_LEFT_HASH[elevation][azimuth] = np.array((np.squeeze(HRIR_LEFT[azimuth_index][elevation_index][:])))
            HRIR_RIGHT_HASH[elevation][azimuth] = np.array(np.squeeze(HRIR_RIGHT[azimuth_index][elevation_index][:]))
            azimuth_index = azimuth_index + 1

    for azimuth in range(-80, 81):
        if azimuth not in AZIMUTH_VALUES:
            left_impulse, right_impulse = interpolate(azimuth, elevation)
            HRIR_LEFT_HASH[elevation][azimuth] = left_impulse
            HRIR_RIGHT_HASH[elevation][azimuth] = right_impulse


initialize("Elevation 0", 7)
initialize("Elevation 180", 39)