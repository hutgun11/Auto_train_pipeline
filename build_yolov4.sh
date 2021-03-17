logdatetime=$(date +'%Y%m%d-%H%M')
host=$HOSTNAME
echo "logdatetime: ${host}, ${logdatetime}"
cd /data0/pepsi_rack
/data0/darknet/darknet detector train model-config/trainer.data model-config/yolo_tiny.cfg ../pre_train/yolov4.conv.137 -dont_show -map >>log${logdatetime}.txt

python best_weight.py -p log${logdatetime}.txt