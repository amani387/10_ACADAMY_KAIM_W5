# Example: Tokenize and label
def tokenize_and_label(text):
    tokens = text.split()
    labels = []
    for token in tokens:
        if "Glass" in token:
            labels.append("B-Product")
        elif "1100" in token:
            labels.append("B-PRICE")
        elif "ደፋር" in token:
            labels.append("B-LOC")
        else:
            labels.append("O")
    return tokens, labels

# Tokenize and label the cleaned text
df["tokens"], df["labels"] = zip(*df["cleaned_text"].apply(tokenize_and_label))

# Save in CoNLL format
with open("labeled_data.conll", "w", encoding="utf-8") as f:
    for tokens, labels in zip(df["tokens"], df["labels"]):
        for token, label in zip(tokens, labels):
            f.write(f"{token} {label}\n")
        f.write("\n")
print("Labeled data saved to labeled_data.conll")
