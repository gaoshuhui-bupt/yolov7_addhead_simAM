Welcome!
This repo uses modified official yolov7 official implementations of YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors, main change is add small object detect layer
and SimAM attention  module in neck and head . The modified structure is shown in the figure

Training
python -m torch.distributed.launch --nproc_per_node 8 --master_port 9527 train.py --workers 8 --device 0,1,2,3,4,5,6,7 --sync-bn --batch-size 16 --data data/coco_bird_merge_all_pin.yaml --img 1280 1280 --cfg cfg/training/yolov7-addhead-simAM.yaml --weights 'yolov7.pt' --hyp data/hyp.scratch.p5.yaml
