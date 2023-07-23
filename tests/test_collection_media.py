from unittest import TestCase
import json
import dotenv
from dotenv import load_dotenv
import os

from pexels_api.api import API
from pexels_api.exceptions import PexelsNoVideoWithEqualOrHigherResolution
from pexels_api.tools.utils import filter_video_entries


class TestCollectionMedia(TestCase):
    def setUp(self):
        load_dotenv()
        PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
        self.api = API(PEXELS_API_KEY)

    def test_collection_media(self):
        self.api.search_collection_media('wpfmesw', media_type='videos', page=1, results_per_page=5)
        print(self.api.total_results)
        videos = self.api.get_collection_media_entries()
        videos = filter_video_entries(videos, min_size='medium', orientation='portrait')
        for i, m in enumerate(videos):
            print(m.link)
