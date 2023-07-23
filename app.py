import gradio as gr
import transformers as pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_name = "gyesibiney/covid-tweet-sentimental-Analysis-roberta"  # Replace with the name of the pre-trained model you want to use
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sentiment = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def get_sentiment(input_text):
    return sentiment(input_text)


#Function to predict sentiments from the input text using the model
    prediction = model.predict([text])[0]
    if label==-1:
       return "Negative"
    elif label== 0:
        return "Neutral"
    else:
        return "Positive"

iface = gr.Interface(fn=get_sentiment,title="Sentimental Analysis", inputs="text",outputs="text")
iface.launch(inline=True)
