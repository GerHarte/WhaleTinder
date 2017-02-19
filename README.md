WhaleTinder
-----------

When working on (Kaggle Right Whale Recognition Challenge)[https://www.kaggle.com/c/noaa-right-whale-recognition] I was looking to build whale detector to locate the pixels in an image that contain a whale.

After taking a few thousand images of whales, and breaking them into tiles I was left with a challenge of manually classifying them into which have whales and which don't to build a supervised classifier.

Tinder's UI seemed like a very efficient way of classifying images into two buckets, so I found (jTinder)[https://github.com/do-web/jTinder] a javascript version of a similar UI and modified it to take images and sort them into folders based on which way you swipe.


To Run
-------

1. Install Flask
2. Clone the repo
3. Navigate to /WhaleTinder
4. Make sure your folder references in app.py point to your local machine.
5. Copy all your images to classify into  **/WhaleTinder/static/img/unclassified**
6. Run python app.py
7. Find your local IP address
8. On your phone or your computer, navigate to http://<YOUR_IP>:5001
9. Swipe right if it matches a positive case, and left if it's a negative case

All images swiped right land in **/WhaleTinder/static/img/whales** and all swiped left land in **/WhaleTinder/static/img/non_whales**

Change the folder names or locations as required


Screenshots
-----------

<img src = "IMG_4803.PNG" />

<img src = "IMG_4804.PNG" />

<img src = "IMG_4805.PNG" />

<img src = "IMG_4806.PNG" />

<img src = "IMG_4807.PNG" />