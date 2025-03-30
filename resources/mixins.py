class OwnerCreateMixin:
    """
    Mixin to automatically assign the currently logged-in user as the owner of an object.
    """
    def perform_create(self, serializer):
        print(f"DEBUG: Request User - {self.request.user}")  # Print the user
        print(f"DEBUG: Authenticated - {self.request.user.is_authenticated}")  # Check authentication
        serializer.save(owner=self.request.user)
