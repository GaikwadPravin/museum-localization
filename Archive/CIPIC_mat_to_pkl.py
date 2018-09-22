import scipy.io as scp                              # to load .mat file
import pickle

# .mat file to .pkl conversion


hrtf_db = scp.loadmat('CIPIC_58_HRTF.mat')

hrir_l_58_0 = hrtf_db['hrir_l'][:,7:,]
hrir_l_58_elevation_0 = np.compress([True], hrir_l_58_0, axis=1)
hrir_l_58_elevation_0_2d = np.resize(hrir_l_58_elevation_0, (25,200))           #Left, Elevation 0 degree data 25x200

hrir_l_58_180 = hrtf_db['hrir_l'][:,39:,]
hrir_l_58_elevation_180 = np.compress([True], hrir_l_58_180, axis=1)
hrir_l_58_elevation_180_2d = np.resize(hrir_l_58_elevation_180, (25,200))       #Left, Elevation 180 degree data 25x200

hrir_r_58_0 = hrtf_db['hrir_r'][:,7:,]
hrir_r_58_elevation_0 = np.compress([True], hrir_r_58_0, axis=1)
hrir_r_58_elevation_0_2d = np.resize(hrir_r_58_elevation_0, (25,200))           #Right, Elevation 0 degree data 25x200

hrir_r_58_180 = hrtf_db['hrir_r'][:,39:,]
hrir_r_58_elevation_180 = np.compress([True], hrir_r_58_180, axis=1)
hrir_r_58_elevation_180_2d = np.resize(hrir_r_58_elevation_180, (25,200))       #Right, Elevation 180 degree data 25x200


itd_58_elevation_0 = hrtf_db['ITD'][:,7]
itd_58_elevation_180 = hrtf_db['ITD'][:,39]

output1 = open('HRIR_l_58_e0.pkl', 'wb')
output2 = open('HRIR_l_58_e180.pkl', 'wb')
output3 = open('HRIR_r_58_e0.pkl', 'wb')
output4 = open('HRIR_r_58_e180.pkl', 'wb')
output5 = open('ITD_58_e0.pkl', 'wb')
output6 = open('ITD_58_e180.pkl', 'wb')

pickle.dump(hrir_l_58_elevation_0_2d, output1)
pickle.dump(hrir_l_58_elevation_180_2d, output2)
pickle.dump(hrir_r_58_elevation_0_2d, output3)
pickle.dump(hrir_r_58_elevation_180_2d, output4)
pickle.dump(itd_58_elevation_0, output5)
pickle.dump(itd_58_elevation_180, output6)

'''

pkl_file = open('HRIR_l_58_e0.pkl', 'rb')
hrir_l_0 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_l_58_e180.pkl', 'rb')
hrir_l_180 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_r_58_e0.pkl', 'rb')
hrir_r_0 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('HRIR_r_58_e180.pkl', 'rb')
hrir_r_180 = pickle.load(pkl_file)
pkl_file.close()

pkl_file1 = open('ITD_58_e0.pkl', 'rb')
itd_e0 = pickle.load(pkl_file1)
pkl_file1.close()

pkl_file1 = open('ITD_58_e180.pkl', 'rb')
itd_e180 = pickle.load(pkl_file1)
pkl_file1.close()
'''
