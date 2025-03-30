from rest_framework.response import Response
from rest_framework import status

class OwnerCreateMixin:
    """
    Mixin to automatically assign the currently logged-in user as the owner of an object.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OwnerQuerySetMixin:
    """
    Mixin to filter queryset based on the logged-in user (model has 'owner' field).
    """
    def get_queryset(self):
        model = self.serializer_class.Meta.model  # Get the model from the serializer
        return model.objects.filter(owner=self.request.user)

    @property
    def model_name(self):
        """Return a readable model name as a string for responses."""
        return self.serializer_class.Meta.model._meta.verbose_name.title()  # Human-readable
    

class CreateResponseMixin:
    """
    Mixin to provide a custom response for create operations in DRF views.
    """
    @property
    def model_name(self):
        """Dynamically retrieve model name from serializer_class."""
        if hasattr(self, 'serializer_class') and hasattr(self.serializer_class.Meta, 'model'):
            return self.serializer_class.Meta.model.__name__
        
        raise AttributeError(f"{self.__class__.__name__} is missing a serializer with a defined model.")

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            model_name = self.model_name  # Dynamically fetch the model name
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    {
                        "status": "success",
                        "message": f"{model_name} created successfully.",
                        "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                    {
                        "status": "error",
                        "message": f"{model_name} creation failed.",
                        "errors": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while creating {model_name}.",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class CustomListResponseMixin:
    """
    Mixin to customize list API responses with success and error messages.
    """
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            model_name = self.model_name  # Retrieving model's name using @property

            if not queryset.exists():
                return Response(
                    {
                        "status": "error",
                        "message": f"No {model_name} found. Please create some {model_name.lower()}s."
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = self.get_serializer(queryset, many=True)
            return Response(
                {
                    "status": "success",
                    "message": f"{model_name} objects retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while retrieving {model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CustomRetrieveResponseMixin:
    """
    Mixin to customize retrieve API responses with success messages.
    """
    def retrieve(self, request, *args, **kwargs):
        try:
            # Get the object instance
            instance = self.get_object()
            # Serialize the retrieved object
            serializer = self.get_serializer(instance)
            model_name = self.model_name  # Uses the property from OwnerQuerySetMixin

            return Response(
                {
                    "status": "success",
                    "message": f"{model_name} retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while retrieving {model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            
class CustomUpdateResponseMixin:
    """
    Mixin to customize update API responses with success messages.
    """
    def update(self, request, *args, **kwargs):
        try:
            # Call DRF's default update method
            response = super().update(request, *args, **kwargs)
            model_name = self.model_name  # Uses property from OwnerQuerySetMixin

            return Response(
                {
                    "status": "success",
                    "message": f"{model_name} updated successfully.",
                    "data": response.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while updating {model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CustomDeleteResponseMixin:
    """
    Mixin to customize delete API responses with success and error messages.
    """
    def delete(self, request, *args, **kwargs):
        try:
            # Get the specific object to delete
            instance = self.get_object()
            model_name = self.model_name  # Get model name dynamically

            # Perform deletion
            self.perform_destroy(instance)
            return Response(
                {
                    "status": "success",
                    "message": f"{model_name} deleted successfully."
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while trying to delete {model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

