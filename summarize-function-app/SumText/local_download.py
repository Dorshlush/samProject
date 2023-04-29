from transformers import BartTokenizer, BartModel

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartModel.from_pretrained('facebook/bart-large-cnn')

model.save_pretrained('./facebook/bart-large-cnn')
tokenizer.save_pretrained('./facebook/bart-large-cnn')