from abc import ABC, abstractmethod
import pandas as pd
import re

class Content (ABC):
    
    @abstractmethod
    def load_content(self):
        pass

class Movie (Content):
    def __init__(self):
        #_id: int
        #genres: str
        #released: int
        #rating: float
        #timestamp: str
        self.content_dict: dict[str, dict] = {}
    
    @staticmethod
    def _extract_info(row):
        title_full = row['title']
        year_match = re.search(r'\((\d{4})\)$', title_full)
        
        if year_match:
            year = int(year_match.group(1))
            # Remove the " (YYYY)" part from the title string
            clean_title = re.sub(r'\s\(\d{4}\)$', '', title_full)
        else:
            year = None
            clean_title = title_full
        
        return clean_title, year
    def load_content(self):
        movies_df = pd.read_csv("./books/Books.csv")
        
        with open("./books/Books.csv", "r") as books_file:
            pass
        # Apply extraction to create new columns
        movies_df[['title', 'release_year']] = movies_df.apply(
            lambda x: pd.Series(self.extract_info(x)), axis=1
        )
        
        # 3. Convert genres string into a list of strings
        movies_df['genres'] = movies_df['genres'].str.split('|')
        
        # 4. Set movieId as the index and convert to a nested dictionary
        # 'index' orientation creates the {index: {column: value}} structure you need
        content_dict = movies_df.set_index('movieId').to_dict(orient='index')


class Book (Content):
    def __init__(self):
        #ISBN: str
        #title: str
        #author: str
        #publication_year: int
        #publisher: str
        self.content_dict: dict[str, dict] = {}
    
    def load_content(self):
        pass