'''
json_dir에서 joint pos 추출 후, 엑셀 형태롤 저장
joint_pos idx가 2라고 가정
'''

from dragon import dragonV
import os

json_dir_path = '/Users/ivory/Desktop/WorkSpace/Philadelphia/json/'
json_folder_list = [folder for folder in os.listdir(json_dir_path) if os.path.isdir(os.path.join(json_dir_path ,folder))]
xlsx_path = '/Users/ivory/Desktop/WorkSpace/Philadelphia/excel/'

#json file들을 excel 로 저장, --number_people_max 2 이기 때문에 0, 1로 저장
for each_json_folder in json_folder_list:
    json_file_list = dragonV.get_jsons_list(json_dir_path + each_json_folder + '/')

    dragonV.jsons2excel(json_dir_path + each_json_folder + '/', [], 0, each_json_folder + '0' +'.xlsx', xlsx_path)
    dragonV.jsons2excel(json_dir_path + each_json_folder + '/', [], 1, each_json_folder + '1' +'.xlsx', xlsx_path)
