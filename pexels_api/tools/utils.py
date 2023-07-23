from pexels_api.tools.video import Video


def filter_video_entries_by_duration(videos: list[Video], min_duration: int, max_duration: int) -> list[Video]:
    videos_with_duration = []
    for video in videos:
        # < because video.duration is round up, if =< some videos will pass with half less (or more) second of duration
        if min_duration < video.duration < max_duration:
            videos_with_duration.append(video)

    return videos_with_duration


def filter_video_entries_by_orientation(videos: list[Video], orientation: str) -> list[Video]:
    valid_orientations = ['portrait', 'landscape', 'square']
    if orientation not in valid_orientations:
        raise ValueError(f'orientation must be one of {valid_orientations}')

    videos_filtered_by_orientation = {
        'portrait': [],
        'landscape': [],
        'square': []
    }
    for video in videos:
        if video.height > video.width:
            videos_filtered_by_orientation['portrait'].append(video)
        elif video.height < video.width:
            videos_filtered_by_orientation['landscape'].append(video)
        else:
            videos_filtered_by_orientation['square'].append(video)

    return videos_filtered_by_orientation[orientation]


def filter_video_entries_by_size(videos: list[Video], min_size: str) -> list[Video]:
    sizes = {
        'large': (3840, 2160),  # 4K
        'medium': (1920, 1080),  # Full HD
        'small': (1280, 720),  # HD
    }
    if min_size not in sizes.keys():
        raise ValueError(f'size must be one of {sizes}')
    min_resolution = sizes[min_size][0] * sizes[min_size][1]

    videos_filtered = []
    for video in videos:
        video_resolution = video.height * video.width
        if video_resolution >= min_resolution:
            videos_filtered.append(video)

    return videos_filtered


def filter_video_entries(
        videos : list[Video], min_duration: int = 0,
        max_duration: int = 9999999, orientation: str = None,
        min_size: str = None) -> list[Video]:
    videos_filtered = videos

    videos_filtered = filter_video_entries_by_duration(videos_filtered, min_duration, max_duration)
    if orientation:
        videos_filtered = filter_video_entries_by_orientation(videos_filtered, orientation)
    if min_size:
        videos_filtered = filter_video_entries_by_size(videos_filtered, min_size)

    return videos_filtered
