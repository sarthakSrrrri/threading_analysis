import psutil
import os
def get_metrices():

    process = psutil.Process(os.getpid())
    memory_info = process.memory_full_info().rss / (1024 * 1024)
    return memory_info
   


# class RAGEvaluator:
#     def __init__(self):
#         self.gpt2_model, self.gpt2_tokenizer = self.load_gpt2_model()
#         id2label = {"0": "not toxic", "1": "toxic"} 
#         label2id = {"not toxic": "0", "toxic": "1"}
#         self.bias_pipeline = pipeline("zero-shot-classification", model="Hate-speech-CNERG/dehatebert-mono-english" , abel2id=label2id, id2label=id2label , device = "cuda:1")

#     def load_gpt2_model(self):
#         model = GPT2LMHeadModel.from_pretrained('gpt2')
#         tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#         return model, tokenizer

#     def evaluate_bleu_rouge(self, candidates, references):
#         bleu_score = corpus_bleu(candidates, [references]).score
#         scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
#         rouge_scores = [scorer.score(ref, cand) for ref, cand in zip(references, candidates)]
#         rouge1 = sum([score['rouge1'].fmeasure for score in rouge_scores]) / len(rouge_scores)
#         return bleu_score, rouge1

#     def evaluate_bert_score(self, candidates, references):
#         P, R, F1 = score(candidates, references, lang="en", model_type='bert-base-multilingual-cased')
#         return P.mean().item(), R.mean().item(), F1.mean().item()


#     def evaluate_diversity(self, texts):
#         all_tokens = [tok for text in texts for tok in text.split()]
#         unique_bigrams = set(ngrams(all_tokens, 2))
#         diversity_score = len(unique_bigrams) / len(all_tokens) if all_tokens else 0
#         return diversity_score

#     def evaluate_racial_bias(self, text):
#         results = self.bias_pipeline([text], candidate_labels=["hate speech", "not hate speech"])
#         bias_score = results[0]['scores'][results[0]['labels'].index('hate speech')]
#         return bias_score

#     def evaluate_all(self, response, reference):
#         candidates = [response]
#         references = [reference]
#         bleu, rouge1 = self.evaluate_bleu_rouge(candidates, references)
#         bert_p, bert_r, bert_f1 = self.evaluate_bert_score(candidates, references)
#         diversity = self.evaluate_diversity(candidates)
#         racial_bias = self.evaluate_racial_bias(response)
#         return {
#             "BLEU": bleu,
#             "ROUGE-1": rouge1,
#             "BERT P": bert_p,
#             "BERT R": bert_r,
#             "BERT F1": bert_f1,
#             "Diversity": diversity,
#             "Racial Bias": racial_bias
#         }
