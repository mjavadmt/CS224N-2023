# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from utils import evaluate_places

num_dev_set = 500

dummy_predictions = ["London" for i in range(num_dev_set)]

acc = evaluate_places("birth_dev.tsv", dummy_predictions)

print(f"out of {num_dev_set} items we got accuracy {acc[1] / 100} with just predicting `London`")
