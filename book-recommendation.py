# import libraries (you may add additional imports but you may not have to)
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# get data files
!wget https://cdn.freecodecamp.org/project-data/books/book-crossings.zip

!unzip book-crossings.zip

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'

# import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

user_counts = df_ratings['user'].value_counts()
active_users = user_counts[user_counts >= 200].index
df_ratings_filtered = df_ratings[df_ratings['user'].isin(active_users)]

book_counts = df_ratings['isbn'].value_counts()
popular_books = book_counts[book_counts >= 100].index
df_ratings_filtered = df_ratings_filtered[df_ratings_filtered['isbn'].isin(popular_books)]

df = pd.merge(df_ratings_filtered, df_books, on='isbn')

df_pivot = df.pivot_table(index='title', columns='user', values='rating').fillna(0)
matrix = csr_matrix(df_pivot.values)

# function to return recommended books - this will be tested
def get_recommends(book = ""):
  if book not in df_pivot.index:
        return "Book not found in dataset."

  book_row = df_pivot.loc[book].values.reshape(1, -1)

  distances, indices = model.kneighbors(book_row, n_neighbors=6)

  recommended_books = []

  for i in range(1, len(distances.flatten())):
      title = df_pivot.index[indices.flatten()[i]]
      dist = distances.flatten()[i]
      recommended_books.append([title, dist])

  recommended_books = sorted(recommended_books, key=lambda x: x[1], reverse=True)
    
  return [book, recommended_books]


model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(matrix)

books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2): 
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge! 🎉🎉🎉🎉🎉")
  else:
    print("You haven't passed yet. Keep trying!")

test_book_recommendation()