class ProfileViewMixin:
    def get_object(self):
        # Return the logged-in user's profile
        return self.request.user.profile