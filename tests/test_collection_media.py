from unittest import TestCase
import json
import dotenv
from dotenv import load_dotenv
import os

from pexels_api.api import API
from pexels_api.exceptions import PexelsNoVideoWithEqualOrHigherResolution


class TestCollectionMedia(TestCase):
    def setUp(self):
        load_dotenv()
        PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
        self.api = API(PEXELS_API_KEY)

    def test_collection_media(self):
        self.api.search_collection_media('ulshmms', media_type='videos', page=1, results_per_page=25)
        media = self.api.get_collection_media_entries()
        for i, m in enumerate(media):
            print(i)
            print(m.url)
