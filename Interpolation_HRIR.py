'''
Interpolation code for HRIR:
Input: HRIR data for azimuth[-80,-65,-55,-45:5:45,55,65,80]
       with elevation 0 and 180.
Output: HRIR data for azimuth[-80:1:80]
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
        Min_HRIR = input_dict[azimuthMin]
        Max_HRIR = input_dict[azimuthMax]
        updated_hrir = (1 - scale_factor)*Min_HRIR + scale_factor*Max_HRIR
        input_dict.update({currAzimuth:updated_hrir})
    return input_dict

pkl_file = open('HRIR_l_58_e0.pkl', 'rb')
input_hrir_l_0 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_r_58_e0.pkl', 'rb')
input_hrir_r_0 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_l_58_e180.pkl', 'rb')
input_hrir_l_180 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_r_58_e180.pkl', 'rb')
input_hrir_r_180 = pickle.load(pkl_file)
pkl_file.close()

#CIPIC database have data for following azimuth angles
input_azimuth = [-80,-65,-55,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,55,65,80]

#Create dictionary
input_hrir_l_dict0 = dict(zip(input_azimuth, input_hrir_l_0))
input_hrir_r_dict0 = dict(zip(input_azimuth, input_hrir_r_0))
input_hrir_l_dict180 = dict(zip(input_azimuth, input_hrir_l_180))
input_hrir_r_dict180 = dict(zip(input_azimuth, input_hrir_r_180))
#print(input_hrir_l_dict180)

#Interpolate data
hrir_l_dict0 = interpolate_itd(input_azimuth,input_hrir_l_dict0)
hrir_r_dict0 = interpolate_itd(input_azimuth,input_hrir_r_dict0)
hrir_l_dict180 = interpolate_itd(input_azimuth,input_hrir_l_dict180)
hrir_r_dict180 = interpolate_itd(input_azimuth,input_hrir_r_dict180)

print(hrir_l_dict180)
#for key, value in input_hrir_l_dict180.items() :
#    print (key,value)
