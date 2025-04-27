import matplotlib.pyplot as plt

# Read the file
with open("news_result.txt", "r") as file:
    data = file.readlines()

# Process data
words = []
counts = []
for line in data:
    word, count = line.strip().split("\t")
    words.append(word)
    counts.append(int(count))

# Sort by frequency (descending)
sorted_indices = sorted(range(len(counts)), key=lambda i: counts[i], reverse=True)
top_words = [words[i] for i in sorted_indices[:10]]
top_counts = [counts[i] for i in sorted_indices[:10]]

# Plot the data
plt.figure(figsize=(10, 5))
plt.bar(top_words, top_counts, color='blue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Most Common Words in News Articles")
plt.xticks(rotation=45)
plt.show()

