# Prepare-own-data-set-in-PASCAL-VOC-form

I used plate_tagger to annotate my own data, which creates the yaml files.
plate_tagger is forked in my repository.
Each yaml file contains data like that:

    
    image_file: DEV934_3135.bmp.jpg

    image_width: 2304

    image_height: 1296

    plate_corners_gt: 516 495 573 490 574 539 515 541        #Coordinates of four corners     

    plate_number_gt: g0v931                 #license plate number

    plate_inverted_gt: false
  
### 1.Create xml files

Then I extracted relavant data in yaml files, and created xml files which are used for Faster RCNN training.  rea

Usage:

Extract data and create xml files:

    python xml.py -i <input yaml dir> -o <output xml dir>

The structure of PASCAL VOC data set like that:
    
    └── VOC2007　
        ├── Annotations　　

        ├── ImageSets　　

        │   ├── Layout　　

        │   ├── Main　　

        │   └── Segmentation　　

        ├── JPEGImages　　

        ├── SegmentationClass　　

        └── SegmentationObject　　

You have to put your xml files in Annotateions file. 

### 2.Create txt files
You have to create 4 txt files, including trainval.txt, test.txt, train.txt, val.txt and put them into ./VOC2007/ImageSets/Main .

You can use sort_txt.m to create these 4 txt files.

