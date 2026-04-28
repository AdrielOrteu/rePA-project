from abc import ABC, abstractmethod
import numpy as np

class Rating (ABC):
    pass

class SimpleRating (Rating):
    pass

class CollaborativeRating (Rating):
    pass
