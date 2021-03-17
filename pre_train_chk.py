import os
import re
import subprocess
import fnmatch
def chk_len_product(number_file_dataset,number_sum_file):
    if number_sum_file == number_file_dataset:
        status=True
    else:
        status=False
    return status
def check_status_config(trainer_data,cfg):
    str_cfg=True
    for i_tr,tr_data in enumerate(trainer_data):
        if 'classes' in tr_data: 
            class_tr=(re.search(r"([0-9]{1,3})",tr_data)).group()
            num_filter=(int(class_tr)+5)*3
    i_chk = 0 
    for i_cfg,cfg_data in enumerate(cfg):
        if 'filters' in cfg_data and str(num_filter) in cfg_data:
            i_chk +=1
        if 'classes' in cfg_data: 
            class_cfg=(re.search(r"([0-9]{1,3})",cfg_data)).group()
            if class_cfg == class_tr:
                i_chk +=1
    if i_chk != 6:
        str_cfg =False
    return str_cfg
try:
    directory = os.listdir('backup')
    for file in os.listdir('model-config'):
        if fnmatch.fnmatch(file,'*.cfg'):
            path_cfg=file
    if len(directory) == 0:
        print('back_up is emty')
        train= [open("model-config/train.txt")]
        test = [open("model-config/test.txt")]
        trainer_data=open("model-config/trainer.data")
        cfg=open(os.path.join('model-config',path_cfg))
        number_sum_file=(len(train)+len(test))*2
        dir ='dataset/images/'
        list =os.listdir(dir)
        number_file_dataset=len(list)
        status_len_pr=chk_len_product(number_file_dataset,number_sum_file)
        status_config=check_status_config(trainer_data,cfg)
        if status_len_pr and status_config:
            if os.path.isfile("chart.png") == False: #checktrain_by chart
                subprocess.call(['sh','./build_yolov4.sh'])
            else:
                pass
    else:
        pass

            
except:
    print('no_backup')
    pass