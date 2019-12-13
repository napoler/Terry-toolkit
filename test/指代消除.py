# Load your usual SpaCy model (one of SpaCy English models)
# https://github.com/napoler/Chinese_models_for_SpaCy
import spacy
nlp = spacy.load('zh')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(u'我 姐姐 有个 狗狗 . 她 很 喜欢 它')

print(doc._.has_coref)
print(doc._.coref_clusters)