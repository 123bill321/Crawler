import os
import sys
import shutil
from xml.dom import minidom

# path = os.getcwd() + '/'
Normal_permission_list = {'ACCESS_LOCATION_EXTRA_COMMANDS','ACCESS_NETWORK_STATE',
'ACCESS_NOTIFICATION_POLICY','ACCESS_WIFI_STATE','BLUETOOTH','BLUETOOTH_ADMIN',
'BROADCAST_STICKY','CHANGE_NETWORK_STATE','CHANGE_WIFI_MULTICAST_STATE','CHANGE_WIFI_STATE',
'DISABLE_KEYGUARD','EXPAND_STATUS_BAR','GET_PACKAGE_SIZE','INSTALL_SHORTCUT','INTERNET',
'KILL_BACKGROUND_PROCESSES','MODIFY_AUDIO_SETTINGS','NFC','READ_SYNC_SETTINGS',
'READ_SYNC_STATS','RECEIVE_BOOT_COMPLETED','REORDER_TASKS','REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
'REQUEST_INSTALL_PACKAGES','SET_ALARM','SET_TIME_ZONE','SET_WALLPAPER','SET_WALLPAPER_HINTS',
'TRANSMIT_IR','UNINSTALL_SHORTCUT','USE_FINGERPRINT','VIBRATE','WAKE_LOCK','WRITE_SYNC_SETTINGS'}
Danger_permission_list = {'READ_CALENDAR','WRITE_CALENDAR','CAMERA','READ_CONTACTS',
'WRITE_CONTACTS','GET_ACCOUNTS','ACCESS_FINE_LOCATION','ACCESS_COARSE_LOCATION','RECORD_AUDIO',
'READ_PHONE_STATE','CALL_PHONE','READ_CALL_LOG','WRITE_CALL_LOG','ADD_VOICEMAIL',
'USE_SIP','PROCESS_OUTGOING_CALLS','BODY_SENSORS','SEND_SMS','RECEIVE_SMS','READ_SMS',
'RECEIVE_WAP_PUSH','RECEIVE_MMS','READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE'}

def Permission(file):
    path = './'
    d_temp = {"No_normal":[],"No_danger":[]}
    path = path + file+ '/' +'AndroidManifest.xml'
    temp = ''

    dom = minidom.parse(path)
    root = dom.documentElement
    nodes = root.getElementsByTagName('uses-permission')
    permission = ''
    for node in nodes:
        permission = node.attributes['android:name'].value
        temp = Find_normal_permission(permission)
        if temp != 'false':
            d_temp['No_normal'].append(temp)
        temp = Find_danger_permission(permission)
        if temp != 'false':
            d_temp['No_danger'].append(temp)
    return d_temp
def Find_normal_permission(permission):
    for i in Normal_permission_list:
        if permission.find(i) != -1:
            return i
    return 'false'
def Find_danger_permission(permission):
    for i in Danger_permission_list:
        if permission.find(i) != -1:
            return i
    return 'false'
def Anylsis (file_name):
    d = {}
    out_file = 'temp'
    if os.path.exists(file_name):
        try:
            cmd = r'apktool d %s -o %s ' %(file_name, out_file)
        except OSError, e:
            print ("Error: %s - %s." % (e.filename,e.strerror))
    else:
        print "file not found"
        raw_input("Enter any key to continue!")
        sys.exit(0)

    os.system(cmd)
    d = Permission(out_file)
    if os.path.exists(out_file):
        try:
            shutil.rmtree(out_file)
        except OSError, e:
            print ("Error: %s - %s." % (e.filename,e.strerror))
    else:
        print "file not found"
        raw_input("Enter any key to continue!")
        sys.exit(0)
    return d
def main():
    # f = {'a':[],'b':[]}
    # f['a'].append('1')
    # f['a'].append('2')
    # print f
    # f['a'] = Normal_permission_list
    # print f
    f = Anylsis('APKPure_v1.2.7_apkpure.com.apk')
    for i in f:
        print f[i],'\n'
if __name__ == '__main__':
    main()
    # f = Anylsis('APKPure_v1.2.7_apkpure.com.apk')
    # print f
    # file = 'APKPure_v1.2.7_apkpure.com.apk'
    # out_file = 'temp'
    # cmd = r'apktool d %s -o %s ' %(file, out_file)# use apktool2.0.1
    # os.system(cmd)
    # Permission(out_file)
    # shutil.rmtree(out_file) #remove folder
