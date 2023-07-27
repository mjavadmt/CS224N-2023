import pandas as pd


def n_grams_calculator(sentence, grams):
    tokenized_sentence = sentence.split()
    grams_list = []
    for i in range(len(tokenized_sentence) - grams + 1):
        grams_list.append(" ".join(tokenized_sentence[i:i + grams]))

    return grams_list


df = pd.DataFrame(columns=["c", "r2", "max_ref", "min_ref_source"])
source_sentence = "resources be sufficient and predictable to"
reference_sentences = ["adequate and predictable resources are required"]
grams_nums = [2]
for gram_num in grams_nums:
    source_n_grams = n_grams_calculator(source_sentence, gram_num)
    for token in set(source_n_grams):
        occurrence_source = source_n_grams.count(token)
        counts_ref_occurrences = []
        for ref_sentence in reference_sentences:
            occurrence_ref = n_grams_calculator(ref_sentence, gram_num).count(token)
            counts_ref_occurrences.append(occurrence_ref)
        max_refs = max(counts_ref_occurrences)
        min_ref_source = min(max_refs, occurrence_source)
        df.loc[token] = [occurrence_source, *counts_ref_occurrences, max_refs, min_ref_source]
    print(f"{df['min_ref_source'].sum()}/{df['c'].sum()}")
