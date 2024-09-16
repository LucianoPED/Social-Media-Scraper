# Exposing modules

from .face_scrap import FacebookScraper
from .x_scrap import TwitterScraper
from .ig_scrap import InstagramScraper

__all__ = ["FacebookScraper", "TwitterScraper", "InstagramScraper"]