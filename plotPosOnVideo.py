'excel file 형태로 저장된 Joint pos를 비디오에 plotting'

import cv2
from dragon import dragonV

exlx_path0 = '/Users/ivory/Desktop/WorkSpace/Philadelphia/excel/walk_turn_rear.mp40.xlsx'
exlx_path1 = '/Users/ivory/Desktop/WorkSpace/Philadelphia/excel/walk_turn_rear.mp41.xlsx'
video_path = '/Users/ivory/Desktop/WorkSpace/lab/pp01/walk_turn_rear.mp4'
frame_data_list = dragonV.xlsx2data(exlx_path0)

dragonV.play_marked_position_from_video(frame_data_list, video_path, 'walk_turn_rear')