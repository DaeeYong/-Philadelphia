from dragon import dragonV

idx0 ='/Users/ivory/Desktop/WorkSpace/lab/jointAndGt/pp086/pp086_omc_walk_turn_front.mp4/idx0.xlsx'
idx1 = '/Users/ivory/Desktop/WorkSpace/lab/jointAndGt/pp086/pp086_omc_walk_turn_front.mp4/idx1.xlsx' 
nogada = '/Users/ivory/Desktop/WorkSpace/lab/jointAndGt/pp086/pp086_omc_walk_turn_front.mp4/nogada.xlsx'  
video_path = '/Users/ivory/Documents/lab/verybigdata/pp086/30/pp086_omc_walk_turn_front.mp4'

idx0_frame_list = dragonV.xlsx2data(idx0)
idx1_frame_list = dragonV.xlsx2data(idx1)        
#nogada_frame_list = dragonV.xlsx2data(nogada)       

dragonV.mark_pos_on_video(video_path, idx0_frame_list, 'gait1', speed=1) 

print(len(idx0_frame_list))       
print(len(idx1_frame_list))