class PexelsInvalidToken(Exception):
    pass

class PexelsInvalidPhotoID(Exception):
    pass

class PexelsConnectionClosed(Exception):
    pass

class PexelsInvalidQuery(Exception):
    pass

class PexelsInvalidCollectionId(Exception):
    pass

class PexelsForbidden(Exception):
    pass

class PexelsResourceUnavailable(Exception):
    pass

class PexelsUnknownException(Exception):
    pass

class PexelsNoVideoWithEqualOrHigherResolution(Exception):
    pass
