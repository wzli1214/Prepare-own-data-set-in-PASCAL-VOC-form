import yaml
import os 
import argparse
from lxml import etree, objectify


ps = argparse.ArgumentParser()
ps.add_argument('-i', help = 'input yaml dir', required = True)
ps.add_argument('-o',help = 'output xml dir', required = True)

args = ps.parse_args()

def createXML(number, file, yamldata, rename): 
    # number: The number of yaml files 
    # file: Image name
    # yamldata: Relevant data of yaml file
    # rename: image name first part, eg: 000001
    E = objectify.ElementMaker(annotate=False)
    anno_tree = E.annotation(
        E.folder('VOC2007'),
        E.filename(file),
        E.size(
        E.width(yamldata[0][0]),
        E.height(yamldata[0][1]),
        E.depth(3)
        ),
        E.segmented(0),
    )
    
    E2 = objectify.ElementMaker(annotate=False)
    anno_tree2 = E2.object(
        E.name("license"),
        E.pose("Unspecified"),
        E.truncated(0),
        E.difficult(0),

        E.bndbox(
        E.xmin(yamldata[1][0]),
        E.ymin(yamldata[1][1]),
        E.xmax(yamldata[1][2]),
        E.ymax(yamldata[1][3])
    ),
    )
    anno_tree.append(anno_tree2)

    if number > 1:
        E3 = objectify.ElementMaker(annotate=False)
        anno_tree3 = E3.object(
            E.name("license"),
            E.pose("Unspecified"),
            E.truncated(0),
            E.difficult(0),

            E.bndbox(
            E.xmin(yamldata[3][0]),
            E.ymin(yamldata[3][1]),
            E.xmax(yamldata[3][2]),
            E.ymax(yamldata[3][3])
        ),
        )
        anno_tree.append(anno_tree3)

        if number >2:
            E4 = objectify.ElementMaker(annotate=False)
            anno_tree4 = E4.object(
                E.name("license"),
                E.pose("Unspecified"),
                E.truncated(0),
                E.difficult(0),

                E.bndbox(
                E.xmin(yamldata[5][0]),
                E.ymin(yamldata[5][1]),
                E.xmax(yamldata[5][2]),
                E.ymax(yamldata[5][3])
            ),
            )
            anno_tree.append(anno_tree4)
    newname = '{:s}.xml'.format(rename)
    etree.ElementTree(anno_tree).write(os.path.join(args.o, newname), pretty_print=True)



for f in os.listdir(args.i):
    if not f.endswith('.jpg'):
        continue
    parts = f.split('.')
    firstname = parts[0]

    yamldata = []
    num = 0
    for m in os.listdir(args.i):
        if not m.endswith('.yaml'):
            continue
        parts1 = m.split('-')
        yamlname = parts1[0]
        if yamlname == firstname:
            openyaml = open(os.path.join(args.i, m))
            yamlfile = yaml.load(openyaml)
            imgwidth = yamlfile['image_width']
            imgheight = yamlfile['image_height']
            resolution = [imgwidth, imgheight]
            rect = yamlfile['plate_corners_gt']
            t = rect.split(' ')
            x1 = int(t[0])
            y1 = int(t[1])
            x2 = int(t[2])
            y2 = int(t[3])
            x3 = int(t[4])
            y3 = int(t[5])
            x4 = int(t[6])
            y4 = int(t[7])
            xlist = [x1, x2, x3, x4]
            ylist = [y1, y2, y3, y4]
            xmin = min(xlist)
            xmax = max(xlist)
            ymin = min(ylist)
            ymax = max(ylist)
            corner = [xmin, ymin, xmax, ymax]
            yamldata.append(resolution)
            yamldata.append(corner)
            num +=1
    print('%s is processing, %s has %d yaml files'%(f,f,num))
    convert = createXML(num, f, yamldata, firstname)






        
            













