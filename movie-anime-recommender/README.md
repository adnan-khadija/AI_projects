# Movie & Anime Recommender (Content-Based)

A simple content-based recommendation system built from scratch in Python, using cosine similarity on a hand-crafted dataset of anime, TV series, and movies.

This project was built as a learning exercise to understand the fundamentals of **feature engineering** and **vector similarity** before moving on to more advanced ML/AI tools.

## What it does

Given a title (e.g. `"One Piece"`), the system returns the top 5 most similar titles from the dataset, based on shared genres, content type, release year, and total watch time.

```
Recommendations for 'Dark':
  From            (score: 0.727)
  Lost            (score: 0.666)
  Kaiju No. 8     (score: 0.448)
  Dr. Stone       (score: 0.438)
  Breaking Bad    (score: 0.400)
```

## How it works

1. **Raw dataset** — a hand-picked list of 16 anime/series/movies, each described with simple attributes (type, genre, year, duration).
2. **Feature engineering**:
   - One-hot encoding of content type (anime / series / movie)
   - One-hot encoding of genres (a title can have multiple genres)
   - A unified "total watch time" feature (to make episodic content comparable to movies)
   - Min-max normalization of watch time and release year (so no feature dominates due to scale)
3. **Vectorization** — each title becomes a 15-dimension NumPy vector.
4. **Cosine similarity** — measures the angle between two vectors to quantify how similar two titles are.
5. **Top-N recommendation** — for a given title, all other titles are ranked by similarity score, and the top 5 are returned.

## Concepts covered

- One-hot encoding
- Min-max normalization
- Vector representation of categorical/numerical data
- Cosine similarity (`(A·B) / (||A|| × ||B||)`)
- Building a simple recommendation pipeline without external ML libraries (pure Python + NumPy)

## How to run

1. Open the notebook in [Google Colab](https://colab.research.google.com/).
2. Run all cells in order (`Runtime` → `Run all`).
3. At the bottom, call the recommendation function with any title from the dataset:

```python
recommander('Naruto', contenus_bruts)
```

No installation needed beyond what's pre-installed in Colab (NumPy is included by default).

## Current limitations

- Tiny dataset (16 titles) — recommendations are necessarily limited to what's available.
- Episode count per season is estimated (12 episodes/season) rather than using real data, which makes the "total watch time" feature approximate.
- No genre weighting — all genres are treated as equally important.
- No text-based features (e.g. plot/synopsis similarity via TF-IDF) yet.

## Possible next steps

- Add more titles and richer metadata (ratings, director, real episode counts).
- Add TF-IDF on synopses for richer content-based similarity.
- Compare against `sklearn.metrics.pairwise.cosine_similarity` to validate the from-scratch implementation.
- Wrap it in a small Streamlit app for an interactive UI.

## Tech stack

- Python 3
- NumPy
- Google Colab



