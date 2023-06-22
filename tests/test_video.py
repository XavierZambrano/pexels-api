from unittest import TestCase
import json

from pexels_api.api import API
from pexels_api.exceptions import PexelsNoVideoWithEqualOrHigherResolution


class TestVideo(TestCase):
    def setUp(self):
        with open('./tests/assets/mock_videos.json', 'r') as f:
            mock_json = json.load(f)

        self.api = API('fake_api_key')
        self.api.json = mock_json

    def test_link_closest_higher_resolution(self):
        videos = self.api.get_video_entries()

        link = videos[0].link_closest_higher_resolution((0, 0))
        self.assertEqual(link, 'https://player.vimeo.com/external/425864361.sd.mp4?s=2c7fec7c5b41b0350c19f936d3ca50b6931e6bab&profile_id=139&oauth2_token_id=57447761')

        with self.assertRaises(PexelsNoVideoWithEqualOrHigherResolution):
            videos[0].link_closest_higher_resolution((1920, 1080))

        link = videos[1].link_closest_higher_resolution((1080, 1920))
        self.assertEqual(link, 'https://player.vimeo.com/external/581656130.hd.mp4?s=95e1ca5548d44784692f101853879ac71927cd16&profile_id=175&oauth2_token_id=57447761')

        link = videos[2].link_closest_higher_resolution((240, 427))
        self.assertEqual(link, 'https://player.vimeo.com/external/508108220.sd.mp4?s=47afe4ef4e371a6aa82a9fe9261d02da8f9963d7&profile_id=164&oauth2_token_id=57447761')
