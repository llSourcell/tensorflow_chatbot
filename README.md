# Tensorflow Chatbot
Chatbot made using tensor flow and trained using Cornell movie dialouge corpus .

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

To run along with UI on your web browser :

- install flask on your venv
- open execute.py 
 
 comment this _conf_ints = [ (key, int(value)) for key,value in parser.items('ints') ]
 uncomment the assignement below it for _conf_ints
 
 comment this _conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
 uncomment the assignement below it for _conf_floats
 
 comment this _conf_strings = [ (key, str(value)) for key,value in parser.items('strings') ]
 uncomment the assignement below it for _conf_strings


- run ui/app.py


Credits
===========
Credit for the vast majority of code here goes to siraj and  [suriyadeepan]
