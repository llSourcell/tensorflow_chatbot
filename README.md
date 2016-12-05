#Tensorflow Chatbot
Tensorflow Chatbot Demo by @Sirajology on [Youtube](https://youtu.be/SJDEOWLHYVo)

Overview
============
This is the full code for 'How to Make an Amazing Tensorflow Chatbot Easily' by @Sirajology on [Youtube](https://youtu.be/SJDEOWLHYVo). In this demo code, we implement Tensorflows [Sequence to Sequence](https://www.tensorflow.org/versions/r0.12/tutorials/seq2seq/index.html) model to train a
chatbot on the [Cornell Movie Dialogue dataset](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html). After training for a few hours, the bot is able to hold a fun conversation.


Dependencies
============
* numpy
* scipy 
* six
* tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html)

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies


Usage
===========

To train the bot, edit the `seq2seq.ini` file so that mode is set to train like so

`mode = train`

then run the code like so

``python execute.py``

To test the bot during or after training, edit the `seq2seq.ini` file so that mode is set to test like so

`mode = test`

then run the code like so

``python execute.py``


Challenge
===========

The challenge for this video is write an entirely different script using [TF Learn](http://tflearn.org/) to generate Lord of the Ring style sentences. Check out this very similar [example](https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm_generator_shakespeare.py), it uses TF Learn to generate Shakespeare-style sentences. Train your model on Lord of the rings text to do something similar! And play around with the hyperparameters to get a more accurate result. Post your GitHub link in the video comments and I'll judge it! 

###Due date: December 8th

Also see this issue, some people have found this discussion helpful
https://github.com/llSourcell/tensorflow_chatbot/issues/3

Credits
===========
Credit for the vast majority of code here goes to [suriyadeepan](https://github.com/suriyadeepan). I've merely created a wrapper to get people started. 
