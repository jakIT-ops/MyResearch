from tensorflow.python.keras.layers import GRU, Input, Dense, TimeDistributed
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Activation
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.losses import sparse_categorical_crossentropy
print("Imported Successfully!")

# Model architecture
def simple_model(input_shape, output_sequence_length, code_vocab_size, plaintext_vocab_size):

    learning_rate = 1e-3

    input_seq = Input(input_shape[1:])
    rnn = GRU(64, return_sequences=True)(input_seq)
    logits = TimeDistributed(Dense(plaintext_vocab_size))(rnn)

    model = Model(input_seq, Activation('softmax')(logits))
    model.compile(loss=sparse_categorical_crossentropy,
                  optimizer=Adam(learning_rate),
                  metrics=['accuracy'])
    return model

print("Function Created Successfully!")

# Reshaping the data
tmp_x = pad(preproc_code_sentences, preproc_plaintext_sentences.shape[1])
tmp_x = tmp_x.reshape((-1, preproc_plaintext_sentences.shape[-2], 1))

# Create the Model Object
simple_rnn_model = simple_model(
    tmp_x.shape,
    preproc_plaintext_sentences.shape[1],
    len(code_tokenizer.word_index)+1,
    len(plaintext_tokenizer.word_index)+1)

print("Model Object Created Successfully!")

simple_rnn_model.fit(tmp_x, preproc_plaintext_sentences, batch_size=64, epochs=6, validation_split=0.2)

# Test the model

def logits_to_text(logits, tokenizer):
    index_to_words = {id: word for word, id in tokenizer.word_index.items()}
    index_to_words[0] = '<PAD>'

    return ' '.join([index_to_words[prediction] for prediction in np.argmax(logits, 1) if index_to_words[prediction]!= '<PAD>'])

print("Function Created Successfully!")
