from preprocess_text.preprocess_text import * 
from tensorflow.keras.models import load_model
import sys
# import os;

text=(clean_text(sys.argv[1]))
# text=clean_text("Hello how you do")
# print(text)
text_matrix=tokenize_text(text)
# print(os.path.abspath('./model_prediction/sentiment_analysis.h5'))
# model_abs_path=os.path.abspath('./model_prediction/sentiment_analysis.h5')
# print(text_matrix)
model = load_model('C:\\Users\Fakeha Rahman\Desktop\Sentiment Analysis\model_prediction\model\sentiment_analysis.h5')
print(model.predict(text_matrix)[0][0])
sys.stdout.flush()