[strings]
# Mode : train, test, serve
mode = train
train_enc = data/train.enc
train_dec = data/train.dec
test_enc = data/test.enc
test_dec = data/test.enc
# folder where checkpoints, vocabulary, temporary data will be stored
working_directory = working_dir/
[ints]
# vocabulary size 
# 	20,000 is a reasonable size
enc_vocab_size = 45000
dec_vocab_size = 45000
# number of LSTM layers : 1/2/3
num_layers = 2
# typical options : 128, 256, 512, 1024
layer_size = 900
# dataset size limit; typically none : no limit
max_train_data_size = 50000
batch_size = 10
# steps per checkpoint
# 	Note : At a checkpoint, models parameters are saved, model is evaluated
#			and results are printed
steps_per_checkpoint = 200
[floats]
learning_rate = 0.001
learning_rate_decay_factor = 0.9
max_gradient_norm = 5.0
##############################################################################
# Note : Edit the bucket sizes at line47 of execute.py (_buckets)
# 
#	Learn more about the configurations from this link
#		https://www.tensorflow.org/versions/r0.9/tutorials/seq2seq/index.html
##############################################################################
