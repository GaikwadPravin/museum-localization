### Functional and Technical Requirement Document

1. General Information</br>
    1.1 Purpose</br>
    1.2 Scope</br>
    1.3 Project References</br>
    1.4 Acronyms and Abbreviations</br>
    1.5 Points of Contact</br>
2. Current System Summary</br>
3. Functional Requirements</br>
    3.1 Summary of Functions</br>
4. Performance Requirements</br>
    4.1 Specific Performance Requirements</br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1 Accuracy and Validity</br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.2 Timing</br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.3 Capacity Limits</br>
5. Additional System Requirements</br>
    5.1 System Description</br>
    5.2 Systems Integration </br>
6. Hardware and Software</br>
    6.1 Hardware</br>
    6.2 Software</br>
    6.3 Communications Requirements</br>
    6.4 Interface</br>


#### 1.0 General Information

###### 1.1 Purpose</br>
  The main purpose of this functional and technical requirement document is to give requirements about 3D Audio for Museum Exhibits project.

###### 1.2	Scope</br>
  This document will give details related to functional, technical, performance and other system related requirements identified by Dr. McMullen.

###### 1.3	Project References</br>
  Prospective solution providers must take into consideration the following supporting references to this document:</br>
  * https://github.com/ufsoundpadlab/museum-localization
  * Sensor Manufacture Website
  * Official Sample Code from Manufacture
  * Raspberry pi 3
  * Python 3
  * Archived MATLAB Code from 17 Spring
  * Archived Python Code from 18 Spring
  * Rendering Sound

###### 1.4	Acronyms and Abbreviations
  Following is a list of the acronyms and abbreviations used in the system:
  1. HRTF : Head Related Transfer Functions


###### 1.5	Points of Contact
  Please find the list of the point(s) of contact (POCs) that may be needed by
  the prospective solution provider:

| Contact Name     | Email     | Function |
| :------------- | :------------- |:------------- |
|Pravin Gaikwad | pravin10216@gmail.com / pravin.gaikwad@ufl.edu | Requirement Document, Sensor, 3D sound rendering |
|Sonali Mane | sonalimane1994@gmail.com / sonalimane@ufl.edu | Requirement Document, Sensor, 3D sound rendering |

#### 2.0	Current System Summary

Aim was to enhance the experience of the museum visitor by creating interactive soundscapes i.e. to infuse 3D audio into the museum exhibits in order to add another layer of immersion to the exhibits.
Current system tried to deliver the engaging audio experience using sensor technology, 3D audio and Raspberry pi.

System implemented:
1. User location is given by dashboard through UDP capital.
2. Tried to get location directly on pi, but failed.
3. Rendering Sound:
    1. Implemented rendering part from MATLAB to python.
    2. Implemented on server computer and then streamed to pi.
    3. On PC version, rendering HRTF works, but when running the same code on Pi, it has huge performance issue   .
4. Graphical User Interface is not that interactive.
5. GUI does not include real time user location tracking as well as log for location.
6. System cannot handle multiple users simultaneously.
7. Unable to detect the direction the user is facing.
8. Lack of GUI for museum curators and staff to program the 3D audio system.
9. System can not collect gyroscope data from sensor. Can't track user orientation.

#### 3.0	Functional Requirements

A user will be carrying a raspberry pi along with a sensor on his body. A headphone will be connected to pi, through which user can listen to specific rendered 3D audio sound depending on his/her current location in museum.

###### 3.1 Summary of Functions required
1. Rendering of 3D sound on Raspberry pi(preferable otherwise  implement it on server computer).
2. Render spatial sound effect based on one sound source
3. Render spatial sound effect based on multiple sound source, simultaneously, continuously, without any lag/gap.
4. Generate spatial sound effect based on user location.
5. Obtain user location data on pi(preferable otherwise get it on server computer).
6. Obtain user orientation data from gyroscope data of sensor. Fetch it to pi(preferable otherwise use it on sever computer).
7. Python based interactive GUI to include real time location update.
8. GUI should keep log of user location, which can be used to get the frequent location visited by users.(Graph can be plotted Frequency vs Location)
9. GUI should be capable of providing different source file as per location.
10. GUI should take into account sensor locations to plot real time user location(x,y axis on GUI).


#### 4.0 Performance Requirements
###### 4.1 Specific Performance Requirements
4.1.1. Accuracy and Validity
4.1.2. Timing
4.1.3. Capacity Limits

#### 6.0 Hardware and Software
  In 3D Audio for Museum Exhibits project hardware and software should work hand-in-hand.  
###### 6.1 Hardware
  Hardware to be used is Raspberry pi 3 and sensors from marvelmind robotics.

###### 6.2 Software
  Project will utilize MATLAB, python3 programming languages.

###### 6.3 Communications Requirements
  Communication requirements depends on the way of implementation
  * 3D sound rendering on Raspberry pi.
  * 3D sound rendering on server computer.

  ###### 1. Rendering on Raspberry pi.
  After successful implementation of 3D sound for one source on pi, implement the same for multiple source. Fetch data of sensors to raspberry pi directly, compute user location as well as orientation. Communicate that location (as well as orientation ) to python GUI. Keep log/track of location to plot graph of Frequency vs Location. GUI should be made such that different source files can be uploaded depending on museum map. Depending on user orientation and location increase intensity of particular sound file. Repeat this continuously. </br>

   **Communication should take place between following modules:**
   * Sensor -> Raspberry pi (All sensors location)</br>
   * Raspberry pi -> python GUI (Utilize data to plot museum map)</br>
   * python GUI -> Raspberry pi (Upload source files)</br>
   * Mobile Sensor -> Raspberry pi  (Location + orientation data acquisition and conversion)</br>
   * Raspberry pi -> pi audio output.</br>
   * Raspberry pi -> python GUI (Location tracking)</br>

   ###### 2. Rendering on server computer.
   After successful implementation of 3D sound for one source on computer, implement the same for multiple source. Fetch data of sensors to raspberry pi directly, compute user location as well as orientation. Communicate that location (as well as orientation ) to python GUI. Keep log/track of location to plot graph of Frequency vs Location. GUI should be made such that different source files can be uploaded depending on museum map. Depending on user orientation and location increase intensity of particular sound file and stream it to Raspberry pi. Repeat this continuously. </br>

   **Communication should take place between following modules:**
   * Sensor -> Raspberry pi (All sensors location)</br>
   * Raspberry pi -> python GUI (Utilize data to plot museum map)</br>
   * python GUI -> Raspberry pi (Upload source files)</br>
   * Mobile Sensor -> Raspberry pi  (Location + orientation data acquisition and conversion)</br>
   * Raspberry pi -> python GUI (Location tracking)</br>
   * server computer -> Raspberry pi (streaming)</br>
   * Raspberry pi -> pi audio output.</br>

###### 6.4 Interface

System diagram to be added.
