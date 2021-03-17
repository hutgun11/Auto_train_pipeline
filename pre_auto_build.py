import os
import re
import subprocess
import schedule
import time
 #for ubutu innohub

def chk_len_product(number_file_dataset,number_sum_file):
    if number_sum_file == number_file_dataset:
        status=True
    else:
        status=False
    return status
def check_status_config(trainer_data,cfg):
    str_cfg=True
    number_filter =6 # for tiny
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
    if i_chk != number_filter:
        str_cfg =False
    return str_cfg
def main():
    try:
        directory = os.listdir('backup')
        if len(directory) == 0:
            print('back_up is emty')
            # train= [open("model-config/train.txt")]
            # test = [open("model-config/test.txt")]
            train =sum(1 for line in open("model-config/train.txt"))
            test =sum(1 for line in open("model-config/test.txt"))
            print('cola',train,test)
            trainer_data=open("model-config/trainer.data")
            cfg=open("model-config/yolo_tiny.cfg")
            # number_sum_file=(len(train)+len(test))*2
            number_sum_file=(train+test)*2
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
                print('already build')
        else:
            pass


    except:
        print('no_backup')
        pass

schedule.every(30).minutes.do(main)
while True:
    os.chdir("/data0/pepsi_rack")
    schedule.run_pending()
    #print(i)
    time.sleep(1)
