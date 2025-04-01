class ProfileViewMixin:
    def get_object(self):
        # Return the user's profile
        return self.request.user.profile