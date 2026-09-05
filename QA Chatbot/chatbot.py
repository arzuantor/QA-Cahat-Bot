import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("QA Chat Bot Dataset.csv")

# Clean data
df["Question"] = df["Question"].fillna("").astype(str)
df["Answer"] = df["Answer"].fillna("").astype(str)

df = df[df["Question"].str.strip() != ""]

ans = df["Answer"]

# TF-IDF
vec = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)

faq_vec = vec.fit_transform(df["Question"])


def get_faq_answer(user_query, threshold=0.1):

    query = vec.transform([user_query])

    similarity = cosine_similarity(query, faq_vec).flatten()

    best_match = similarity.argmax()
    score = similarity[best_match]

    if score >= threshold:
        return ans.iloc[best_match]

    return "Sorry sir! I don't have any knowledge about our services."