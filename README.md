# Twitch Hate Speech Detection Bot
It is a twitch Bot used for blocking hateful chatters.
This bot intercepts the message from a twitch channel and apply the inference on that message to determine 3 things, whether the message is a 'hate_speech' or 'offensive_language' or is 'neither'.
The NLP model was made using BERT and trained on the large dataset of offensive language dataset found on kaggle. The dataset was originally of twiter hate speech data. But the same datatset can be utilised for this purpose. As twitch also has a '@username' feature.
Althought the trained model is overfitted it still shows promising results. But further tuning is required in the dataset.

Some Screenshots:
<br>
<br>
<img src="https://user-images.githubusercontent.com/43596461/206324835-2bb62083-d5c1-456a-9481-6e60cd778169.png" width="1024">
<br>
<br>
As you can see you can the model is not perfect, we can trick the model into thinking that we are saying something neutral. But it does blocks out the extreme examples.
<br>
<br>
<img src="https://user-images.githubusercontent.com/43596461/206328934-9667b549-4d2a-4a28-af9d-457f6d46ac12.png" width="1024">
<br>
<br>
