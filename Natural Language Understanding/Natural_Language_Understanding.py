import spacy
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.models import load_model


# Get Intents    
# Load the model
dl_model = load_model("Notebooks\BOW.h5")

lemma = WordNetLemmatizer()
words = pickle.load(open("data\words.pkl",'rb'))
classes = pickle.load(open("data\classes.pkl",'rb'))
token = Tokenizer(num_words=(len(words)+1))
token.fit_on_texts(words)

# define a function to clean the text
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = word_tokenize(sentence)
    
    # stem each word - create short form for word
    sentence_words = [lemma.lemmatize(word.lower()) for word in sentence_words if word not in stopwords.words('english')]
    return sentence_words

def predict(sentence):
    
    # filter predictions below a threshold
    bow = token.texts_to_matrix([clean_up_sentence(sentence)]) 
    res = dl_model.predict(bow)[0]
    results = [[i,r] for i,r in enumerate(res) if r>.50]
    
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = {"Intent":classes[r[0]] for r in results}
    return return_list

# Get Entities
path = 'Name Entity Recognition'
nlp = spacy.load(path)

def NER(sentence):
    doc = nlp(sentence)
    result = {ent.label_: ent.text for ent in doc.ents}        
    return result
    
    
# Final Function That Return both of intent and entities For Utterance
def NLU(sentence):
    intent = predict(sentence)
    entity = NER(sentence)
    
    if entity == {}:
        result = {'Text' : sentence,'Intent': intent['Intent'],'Entities':'None'}
    else:
        result = {'Text' : sentence,'Intent': intent['Intent'],'Entities':entity}
        
    return result


