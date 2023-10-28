from rouge_score import rouge_scorer

# Define the ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Load reference summaries and generated summaries
reference_summary = " The Princely States denied participation in the Constituent Assembly as they were in the hopes that they would create their own independent states and rule them after the British left India. Hence the Constituent Assembly was formed with the 296 representatives from the British India. The Constituent Assembly was not elected on the basis of universal adult suffrage, and Muslims and Sikhs received special representation as minorities. These 296 representatives also included women members viz., Sarojini Naidu, Hansa Mehta, Durgabai Deshmukh, Rajkumari Amrit KaurandVijayalakshmi Pandit.Dr. B.R. Ambedkar, Sanjay Phakey, Jawaharlal Nehru, C. Rajagopalachari, Dr. Rajendra Prasad, Sardar Vallabhbhai Patel, Purushottam Mavalankar, Sandip kumar Patel, Maulana Abul Kalam Azad, Shyama Prasad Mukherjee, Nalini Ranjan Ghosh, Balwantrai Mehta H. P. Modi, Ari Bahadur Gururng and Frank Anthony were some important figures in the Constituent Assembly. Prominent jurists like Alladi Krishnaswamy Iyer, Benegal Narsing Rauand K. M. Munshiand Ganesh Mavlankar were also members of the Assembly."
generated_summary = "The Constituent Assembly was not elected on the basis of universal adult suffrage, and Muslims and Sikhs received special representation as minorities. Dr. B.R. Ambedkar, Sanjay Phakey, Jawaharlal Nehru, C. Rajagopalachari, Rajendra Prasad, Sardar Vallabhbhai Patel, Purushottam Mavalankar, Sandip kumar Patel, Maulana Abul Kalam Azad and Frank Anthony were some important figures in the Assembly."

# Calculate ROUGE scores
scores = scorer.score(reference_summary, generated_summary)

# Access individual ROUGE scores
rouge_1_precision = scores['rouge1'].precision
rouge_1_recall = scores['rouge1'].recall
rouge_1_f1 = scores['rouge1'].fmeasure

# Similarly, access scores for 'rouge2' and 'rougeL'
rouge_2_precision = scores['rouge2'].precision
rouge_2_recall = scores['rouge2'].recall
rouge_2_f1 = scores['rouge2'].fmeasure

rouge_L_precision = scores['rougeL'].precision
rouge_L_recall = scores['rougeL'].recall
rouge_L_f1 = scores['rougeL'].fmeasure
# ... and so on

# Print the ROUGE scores
print("ROUGE-1:")
print("Precision:", rouge_1_precision)
print("Recall:", rouge_1_recall)
print("F1 Score:", rouge_1_f1)

print("ROUGE-2:")
print("Precision:", rouge_2_precision)
print("Recall:", rouge_2_recall)
print("F1 Score:", rouge_2_f1)

print("ROUGE-L:")
print("Precision:", rouge_L_precision)
print("Recall:", rouge_L_recall)
print("F1 Score:", rouge_L_f1)


