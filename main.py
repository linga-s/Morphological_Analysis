import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from bi_lstm_attention_training_code import predict_sentece
from tagCase import tagCase
from tagGender import tagGender
from tagNumber import tagNumber
from tagPerson import tagPerson
from findPOSTag import TAGGING_POS


inp = "వారు కూరగాయలు బజార్లో అమ్మటానికి వచ్చారు"

Root_Forms = predict_sentece(inp)
Gender = tagGender(inp)
Number = tagNumber(inp)
Case = tagCase(inp)
Person = tagPerson(inp)
POS_tags = TAGGING_POS(inp)

print(Root_Forms)
print(Gender)
print(Number)
print(Case)
print(Person)
print(POS_tags)