import pandas as pd
import re
import json

# Sample scraped message
data = [
    {
        "id": 6016,
        "sender": -1001307493052,
        "timestamp": "2025-01-16T06:29:40+00:00",
        "text": """💥💥...................................💥💥

📌 2in1 Glass oil Sprayer and Dispenser

👍 ከመቀነሻ በተጨማሪ እንደ ስፕሬይ የሚያገለግል

ዋጋ፦  💲🏷 1100 ብር

♦️ውስን ፍሬ ነው ያለው🔥🔥🔥

🏢 አድራሻ👉

📍ቁ.1️⃣♦️መገናኛ መሰረት ደፋር ሞል ሁለተኛ ፎቅ ቢሮ ቁ. S05/S06

📍 ቁ.2️⃣♦️ፒያሳ ጊዮርጊስ አደባባይ ራመት_ታቦር_ኦዳ_ህንፃ 1ኛ ፎቅ ሱቅ ቁ. G1 -107

📲 0902660722
📲 0928460606
""",
        "media": "./downloads/photo_2025-01-16_06-29-40.jpg"
    }
]

# Load the data
df = pd.DataFrame(data)

# Function to preprocess text
def clean_text(text):
    # Remove emojis and unnecessary punctuation
    text = re.sub(r"[^\w\s፡።፣፤፥፦፧፨]", "", text)  # Removes non-text characters
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Apply preprocessing
df["cleaned_text"] = df["text"].apply(clean_text)

# Save as CSV for further use
df.to_csv("preprocessed_data.csv", index=False)
print("Preprocessed data saved to preprocessed_data.csv")
