from django.shortcuts import render
import torch
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
def index(request):
    if request.method == 'POST':
        print("Post")
        text = request.POST.get('input-text')
        # print(text)
        tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        torch_device = 'cpu'
        def bart_summarize(text):
            text = text.replace('\n','')
            text_input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024)['input_ids'].to(torch_device)
            summary_ids = model.generate(text_input_ids, num_beams=4, length_penalty=2.0, max_length=10000, min_length=56, no_repeat_ngram_size=3)           
            summary_txt = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
            return summary_txt
        sum = bart_summarize(text)
        print('bart_summarize', sum)
        return render(request, 'home.html', {'output': sum})
    return render(request, 'home.html')
