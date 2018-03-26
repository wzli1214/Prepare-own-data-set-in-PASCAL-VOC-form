%%  
%Based on the generated XML files; The code makes the trainval.txt, train.txt, test.txt and val.txt of the VOC2007 data set.   
%eg. trainval accounts for 50% of the entire dataset, test accounts for 50% of the entire dataset. train accounts for 50% of trainval, val accounts for 50% of trainval.
%The percentage above can be modified according to your own dataset. If the data sets are relatively small, test and val can be less.
%%  
%Pay attention to modifying the folder path  
xmlfilepath='F:\linux 文件\Annotations';  
txtsavepath='F:\linux 文件\ImageSets\Main\';  
trainval_percent=0.9;%Trainval accounts for the percentage of the entire dataset, and the rest is the percentage of test.  
train_percent=0.9;%Train accounts for the percentage of trainval, and the rest is the percentage of val.
  
%%  
xmlfile=dir(xmlfilepath);  
numOfxml=length(xmlfile)-2; 
  
  
trainval=sort(randperm(numOfxml,floor(numOfxml*trainval_percent)));  
test=sort(setdiff(1:numOfxml,trainval));  
  
  
trainvalsize=length(trainval);%the size of trainval  
train=sort(trainval(randperm(trainvalsize,floor(trainvalsize*train_percent))));  
val=sort(setdiff(trainval,train));  
  
  
ftrainval=fopen([txtsavepath 'trainval.txt'],'w');  
ftest=fopen([txtsavepath 'test.txt'],'w');  
ftrain=fopen([txtsavepath 'train.txt'],'w');  
fval=fopen([txtsavepath 'val.txt'],'w');  
  
  
for i=1:numOfxml  
    if ismember(i,trainval)  
        fprintf(ftrainval,'%s\n',xmlfile(i+2).name(1:end-4));  
        if ismember(i,train)  
            fprintf(ftrain,'%s\n',xmlfile(i+2).name(1:end-4));  
        else  
            fprintf(fval,'%s\n',xmlfile(i+2).name(1:end-4));  
        end  
    else  
        fprintf(ftest,'%s\n',xmlfile(i+2).name(1:end-4));  
    end  
end  
fclose(ftrainval);  
fclose(ftrain);  
fclose(fval);  
fclose(ftest);  
