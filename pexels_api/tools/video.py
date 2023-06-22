from ..exceptions import PexelsNoVideoWithEqualOrHigherResolution


class Video:
    def __init__(self, json_video):
        self.__video = json_video

    @property
    def id(self):
        return int(self.__video["id"])

    @property
    def width(self):
        return int(self.__video["width"])

    @property
    def height(self):
        return int(self.__video["height"])

    @property
    def videographer(self):
        return self.__video["user"]["name"]

    @property
    def url(self):
        return self.__video["url"]

    @property
    def image_preview(self):
        return self.__video['image']

    @property
    def description(self):
        return self.url.split("/")[-2].replace(f"-{self.id}", "").replace("-", " ")

    @property
    def duration(self):
        return self.__video["duration"]

    @property
    def highest_resolution_video(self):
        # Since each video will always have the same aspect ratio, just different resolutions....
        # It really doesn't matter whether we sort by width or height here, we're just looking for the
        # highest number.
        highest_resolution_video_dict = {}
        for dictionary in self.__video["video_files"]:
            if not highest_resolution_video_dict:
                highest_resolution_video_dict = dictionary
            else:
                if dictionary["width"] > highest_resolution_video_dict["width"]:
                    highest_resolution_video_dict = dictionary
        return highest_resolution_video_dict

    def link_closest_higher_resolution(self, resolution: tuple):
        """
        Return the link to the video with the equal or closest higher resolution.

        Example if resolution is (1080, 1920) and exist:
        - (900, 1800)
        - (1000, 2000)
        - (1100, 2200)
        - (1200, 2400)
        Then the link to (1100, 2200) will be returned.

        Example if resolution is (1080, 1920) and exist:
        - (900, 1600)
        - (1080, 1920)
        - (1170, 2080)
        Then the link to (1080, 1920) will be returned.
        """

        sorted_video_files = sorted(self.__video["video_files"], key=lambda x: x["width"])
        for video_file in sorted_video_files:
            if video_file["width"] >= resolution[0] and video_file["height"] >= resolution[1]:
                return video_file["link"]

        raise PexelsNoVideoWithEqualOrHigherResolution(
            'No video with equal or higher resolution found.')

    @property
    def highest_resolution_width(self):
        return int(self.highest_resolution_video['width'])

    @property
    def highest_resolution_height(self):
        return int(self.highest_resolution_video['height'])

    @property
    def link(self):
        return self.highest_resolution_video['link']

    @property
    def extension(self):
        return self.highest_resolution_video['file_type'].split("/")[-1]
