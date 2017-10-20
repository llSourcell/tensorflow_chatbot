# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Utilities for downloading data from WMT, tokenizing, vocabularies."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
from io import open
from collections import Counter

from tensorflow.python.platform import gfile

# Special vocabulary symbols - we always put them at the start.
_PAD = "_PAD"
_GO = "_GO"
_EOS = "_EOS"
_UNK = "_UNK"
_START_VOCAB = [_PAD, _GO, _EOS, _UNK]

PAD_ID = 0
GO_ID = 1
EOS_ID = 2
UNK_ID = 3

# Regular expressions used to tokenize.
_WORD_SPLIT = re.compile("([.,!?\"':;)(])")
_DIGIT_RE = re.compile(r"\d")

CORNELL_MOVIE_CORPUS_ENCODING = 'ISO-8859-2'


def basic_tokenizer(sentence):
    """Very basic tokenizer: split the sentence into a list of tokens."""
    all_words = []
    for space_separated_fragment in sentence.strip().split():
        words = re.split(_WORD_SPLIT, space_separated_fragment)
        for word in words:
            if word:
                all_words.append(word)
    return all_words


def create_vocabulary(vocabulary_path, data_path, max_vocabulary_size,
                      tokenizer=None, normalize_digits=True):
    if not tokenizer:
        tokenizer = basic_tokenizer

    if not os.path.exists(vocabulary_path):
        print("Creating vocabulary %s from %s" % (vocabulary_path, data_path))
        vocab = Counter()
        with open(data_path, 'rt', encoding='utf8') as f:
            for counter, sentence in enumerate(f, 1):
                if counter % 100000 == 0:
                    print("  processing line %d" % counter)
                tokens = tokenizer(sentence)
                for w in tokens:
                    if normalize_digits:
                        word = re.sub(_DIGIT_RE, '0', w)
                    else:
                        word = w
                    vocab[word] += 1

            vocab_list = _START_VOCAB + sorted(vocab, key=vocab.get, reverse=True)
            print('>> Full Vocabulary Size :', len(vocab_list))
            if len(vocab_list) > max_vocabulary_size:
                vocab_list = vocab_list[:max_vocabulary_size]
                print('>>>> Vocab Truncated to: {}'.format(max_vocabulary_size))
            with open(vocabulary_path, 'wt', encoding='utf8') as vocab_file:
                for w in vocab_list:
                    vocab_file.write(w + '\n')


def initialize_vocabulary(vocabulary_path, encoding=CORNELL_MOVIE_CORPUS_ENCODING):
    vocab = {}
    rev_vocab = []
    if gfile.Exists(vocabulary_path):
        with open(vocabulary_path, 'rt', encoding=encoding) as f:
            for index, line in enumerate(f, 1):
                element = line.strip()
                rev_vocab.append(element)
                vocab[element] = index
        assert len(vocab) == len(rev_vocab)
        if not (vocab and rev_vocab):
            raise ValueError('File empty: {}'.format(vocabulary_path))
    else:
        raise ValueError("Vocabulary file %s not found.", vocabulary_path)
    return vocab, rev_vocab


def sentence_to_token_ids(sentence, vocabulary, tokenizer=None, normalize_digits=True):
    if not tokenizer:
        tokenizer = basic_tokenizer
    words = tokenizer(sentence)
    if not normalize_digits:
        return [vocabulary.get(w, UNK_ID) for w in words]
    # Normalize digits by 0 before looking words up in the vocabulary.
    return [vocabulary.get(re.sub(_DIGIT_RE, '0', w), UNK_ID) for w in words]


def data_to_token_ids(data_path, target_path, vocabulary_path,
                      tokenizer=None, normalize_digits=True):
    if not gfile.Exists(target_path):
        print("Tokenizing data in %s" % data_path)
        vocab, _ = initialize_vocabulary(vocabulary_path)
        with gfile.GFile(data_path, mode="rb") as data_file:
            with gfile.GFile(target_path, mode="w") as tokens_file:
                for counter, line in enumerate(data_file, 1):
                    if counter % 100000 == 0:
                        print("  tokenizing line %d" % counter)
                    token_ids = sentence_to_token_ids(line, vocab, tokenizer,
                                                      normalize_digits)
                    tokens_file.write(" ".join([str(tok) for tok in token_ids]) + "\n")


def prepare_custom_data(working_directory, train_enc, train_dec, test_enc, test_dec, enc_vocabulary_size,
                        dec_vocabulary_size, tokenizer=None):
    # Create vocabularies of the appropriate sizes.
    enc_vocab_path = os.path.join(working_directory, "vocab%d.enc" % enc_vocabulary_size)
    dec_vocab_path = os.path.join(working_directory, "vocab%d.dec" % dec_vocabulary_size)
    create_vocabulary(enc_vocab_path, train_enc, enc_vocabulary_size, tokenizer)
    create_vocabulary(dec_vocab_path, train_dec, dec_vocabulary_size, tokenizer)

    # Create token ids for the training data.
    enc_train_ids_path = train_enc + (".ids%d" % enc_vocabulary_size)
    dec_train_ids_path = train_dec + (".ids%d" % dec_vocabulary_size)
    data_to_token_ids(train_enc, enc_train_ids_path, enc_vocab_path, tokenizer)
    data_to_token_ids(train_dec, dec_train_ids_path, dec_vocab_path, tokenizer)

    # Create token ids for the development data.
    enc_dev_ids_path = test_enc + (".ids%d" % enc_vocabulary_size)
    dec_dev_ids_path = test_dec + (".ids%d" % dec_vocabulary_size)
    data_to_token_ids(test_enc, enc_dev_ids_path, enc_vocab_path, tokenizer)
    data_to_token_ids(test_dec, dec_dev_ids_path, dec_vocab_path, tokenizer)

    return enc_train_ids_path, dec_train_ids_path, enc_dev_ids_path, dec_dev_ids_path, enc_vocab_path, dec_vocab_path
