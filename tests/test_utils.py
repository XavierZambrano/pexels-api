from unittest import TestCase
import json

from pexels_api.api import API
from pexels_api.tools.utils import filter_video_entries_by_duration, \
    filter_video_entries_by_orientation, filter_video_entries_by_size, \
    filter_video_entries

class TestFilterVideoEntries(TestCase):
    def setUp(self):
        with open('./tests/assets/mock_videos.json', 'r') as f:
            mock_json = json.load(f)

        self.api = API('fake_api_key')
        self.api.json = mock_json
        self.videos = self.api.get_video_entries()

    def test_filter_video_entries_by_duration(self):
        videos = filter_video_entries_by_duration(self.videos, min_duration=13, max_duration=16)
        videos_id = [video.id for video in videos]

        self.assertEqual(videos_id, [9011099, 4583678])

    def test_filter_video_entries_by_orientation(self):
        videos = filter_video_entries_by_orientation(self.videos, orientation='portrait')
        videos_id = [video.id for video in videos]

        self.assertEqual(videos_id, [4562023, 9011099, 6707366, 5667135, 4434370, 8953694, 4583678, 7318819, 8044817, 4341226])

        videos = filter_video_entries_by_orientation(self.videos, orientation='landscape')
        videos_id = [video.id for video in videos]

        self.assertEqual(videos_id, [])

        videos = filter_video_entries_by_orientation(self.videos, orientation='square')
        videos_id = [video.id for video in videos]

        self.assertEqual(videos_id, [])

    def test_filter_video_entries_by_orientation_no_valid_orientation(self):
        with self.assertRaises(ValueError):
            filter_video_entries_by_orientation(self.videos, orientation='horizontal')

    def test_filter_video_entries_by_size(self):
        videos = filter_video_entries_by_size(self.videos, min_size='large')
        videos_id = [video.id for video in videos]
        self.assertEqual(videos_id, [5667135, 4434370])

        videos = filter_video_entries_by_size(self.videos, min_size='medium')
        videos_id = [video.id for video in videos]
        self.assertEqual(videos_id, [9011099, 6707366, 5667135, 4434370, 8953694, 4583678, 7318819, 8044817, 4341226])

        videos = filter_video_entries_by_size(self.videos, min_size='small')
        videos_id = [video.id for video in videos]
        self.assertEqual(videos_id, [4562023, 9011099, 6707366, 5667135, 4434370, 8953694, 4583678, 7318819, 8044817, 4341226])
