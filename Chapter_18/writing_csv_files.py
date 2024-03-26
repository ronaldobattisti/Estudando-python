"""
Writing CSV files

reader() -> writer()

witerow() is used tu write each line
"""
"""
from csv import writer

with open('Chapter_18/movies.csv', 'w', newline='') as file:
    writer_csv = writer(file)
    movie = None
    writer_csv.writerow(['Title', 'Gender', 'Duration'])
    while movie != 'skip':
        movie = input("Write the movie: ")
        if movie != 'skip':
            gender = input(f"Write the gender of the movie '{movie}': ")
            duration = input(f"Write the duration of the movie '{movie}': ")
            writer_csv.writerow([movie, gender, duration])
"""

# DictWriter
from csv import DictWriter

with open('Chapter_18/movies2.csv', 'w', newline='') as file:
    header = ['Title', 'Gender', 'Duration']
    writer_csv = DictWriter(file, fieldnames=header)
    writer_csv.writeheader()
    movie = None
    while movie != 'skip':
        movie = input("Write the movie name: ")
        if movie != 'skip':
            gender = input(f"Write the gender of the movie '{movie}': ")
            duration = input(f"Write the duration of the movie '{movie}': ")
            # the dict key shoud be the same as the header
            writer_csv.writerow(
                {'Title': movie, 'Gender': gender, 'Duration': duration})
