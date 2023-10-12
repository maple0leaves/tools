## Randomly make dateset smaller 

some datasets mybe too large,it is difficult to do an experiment,so I make it smaller .<br>

#### 1.USE

```python
if __name__ =="__main__":

    files =['test', 'train', 'trainval', 'val']
    # deletion_ratio : how many do you want to delete ,save 1- deletion_ratio
    deletion_ratio = 0.5
    # imgpath is images path
    # labelpath is labels path
    # depend on deletion_ratio remove label in labelpath and use label
    # file name save img in imgpath .
    for file in files:
        imgpath = r'F:\ZZLcode\hand_glove_last\images\\'+file
        labelpath = r'F:\ZZLcode\hand_glove_last\labels\\'+file
        # labelpath could not change 
        delete_labels_by_ratio(labelpath, 0.5)
        makesmall(imgpath=imgpath, labelpath=labelpath)
```





