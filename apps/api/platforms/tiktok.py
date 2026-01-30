from .base import SocialPlatform

class TikTok(SocialPlatform):
    def auth(self):
        # This is a mock implementation.
        # It redirects to a mock callback that simulates a successful login.
        return "/auth/tiktok/mock_callback"

    def upload(self, file_path):
        # TODO: Implement TikTok video upload
        pass
