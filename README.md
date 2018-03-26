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

Then I extracted relavant data in yaml files, and created xml files which are used for Faster RCNN training.  

Usage:
Extract data and create xml files:

python xml.py -i <input yaml dir> -o <output xml dir>
