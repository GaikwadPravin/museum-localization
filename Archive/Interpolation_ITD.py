'''
Interpolation code for ITD:
Input: ITD data for azimuth[-80,-65,-55,-45:5:45,55,65,80]
       with elevation 0 and 180.
Output: ITD data for azimuth[-80:1:80]
       with elevation 0 and 180.
'''
import pickle

#Function to find adjacent minimum azimuth angle
def find_min(current_val):
    while True:
        current_val = current_val - 1
        min_exists = current_val in input_azimuth
        if min_exists:
            return current_val

#Function to find adjacent maximum azimuth angle
def find_max(current_val):
    while True:
        current_val = current_val + 1
        max_exists = current_val in input_azimuth
        if max_exists:
            return current_val

#Function to find interpolated data for missing angles
def interpolate_itd(input_azimuth, input_dict):
    for currAzimuth in range(-80,80):
        if currAzimuth in input_azimuth:
            continue
        azimuthMin = find_min(currAzimuth)
        azimuthMax = find_max(currAzimuth)
        delayMin = input_dict[azimuthMin]
        delayMax = input_dict[azimuthMax]
        scale_factor = abs(currAzimuth - azimuthMin)/abs(azimuthMax - azimuthMin)
        delay = (1 - scale_factor) * delayMin + scale_factor * delayMax
        input_dict.update({currAzimuth:delay})
    return input_dict

#Load CIPIC user 58, elevation 0, ITD data
pkl_file1 = open('ITD_58_e0.pkl', 'rb')
itd_e0 = pickle.load(pkl_file1)
pkl_file1.close()

#Load CIPIC user 58, elevation 180, ITD data
pkl_file1 = open('ITD_58_e180.pkl', 'rb')
itd_e180 = pickle.load(pkl_file1)
pkl_file1.close()

#CIPIC database have data for following azimuth angles
input_azimuth = [-80,-65,-55,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,55,65,80]

#Create dictionary
input_itd_dict0 = dict(zip(input_azimuth, itd_e0))
input_itd_dict180 = dict(zip(input_azimuth, itd_e180))

#Interpolate data
itd_dict0 = interpolate_itd(input_azimuth,input_itd_dict0)
itd_dict180 = interpolate_itd(input_azimuth,input_itd_dict180)

'''
for key in sorted(itd_dict0):
    print ("%s: %s\t\t %s: %s" % (key, itd_dict0[key] , key, itd_dict180[key]))
    #print ("%s: %s" % (key, itd_dict0[key]))
'''
