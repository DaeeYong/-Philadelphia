'''
윈도우 기준(경로 표기 문제 때문에, 다른 운영체제에서는 동작하지 않을 수 있음.)
video -> openpose -> json file
vs code의 터미널 위치는 openpose 에 있어야 함.
sepcial thanks : Jingeun Lee
'''

import os

json_dir_path = 'C:/Users/admin/Desktop/project/json_test/'

openpose_path = 'C:/Users/admin/Desktop/project/openpose-1.7.0/openpose/bin/OpenPoseDemo.exe'
video_dir_path = 'C:/Users/admin/Desktop/project/openpose-1.7.0/openpose/video/'

video_list = os.listdir(video_dir_path)
print("<video list>")
for video_name in video_list:
    print("Done : " + video_name)

cnt = 0
length = len(video_list)
for video_name in video_list:
    cnt += 1
    os.mkdir(json_dir_path + video_name)
    json_file_path = json_dir_path + video_name + '/'
    command = openpose_path + ' --video ' + video_dir_path + video_name + ' --number_people_max 2 --write_json ' + json_file_path + ' --display 0 --render_pose 0'
    os.system(command)
    print(f'[{cnt}/{length}] processed\n')

