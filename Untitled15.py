#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os


# In[9]:


os.dir


# In[14]:


os.chdir( 'E:\Modules\Modules\Project\Sign-Language-Reserach\RealTimeObjectDetection')


# In[15]:


pwd


# In[16]:


import cv2


# In[17]:


import uuid


# In[18]:


import time


# In[19]:


IMAGES_PATH ='Tensorflow\workspace\images\collectedimages'


# In[20]:


labels = ['hello', 'thanks','yes', 'na', 'iloveyou']
number_imgs = 15


# In[21]:


for label in labels:
    get_ipython().system("mkdir {'Tensorflow\\workspace\\images\\collectedimages\\\\'+label}")
    cap = cv2.VideoCapture(0)
    print('collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname,frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


# In[ ]:




