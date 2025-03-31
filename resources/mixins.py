from rest_framework.response import Response
from rest_framework import status

class BaseModelMixin:
    """
    Base mixin to dynamically retrieve the model name from the serializer class.
    """
    @property
    def model_name(self):
        if hasattr(self, 'serializer_class') and hasattr(self.serializer_class.Meta, 'model'):
            return self.serializer_class.Meta.model.__name__
        return "Object"  # Default fallback

class OwnerCreateMixin:
    """
    Automatically assigns the logged-in user as the owner of an object.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OwnerQuerySetMixin:
    """
    Filters queryset based on the logged-in user.
    """
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(owner=self.request.user)

class CreateResponseMixin(BaseModelMixin):
    """
    Custom response mixin for create operations.
    """
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    {
                        "status": "success",
                        "message": f"{self.model_name} created successfully.",
                        "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "status": "error",
                    "message": f"{self.model_name} creation failed.",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while creating {self.model_name}.",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CustomListResponseMixin(BaseModelMixin):
    """
    Custom response mixin for list operations.
    """
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return Response(
                    {
                        "status": "error",
                        "message": f"No {self.model_name} found. Please create a {self.model_name.lower()}."
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = self.get_serializer(queryset, many=True)
            return Response(
                {
                    "status": "success",
                    "message": f"{self.model_name} objects retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while retrieving {self.model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CustomRetrieveResponseMixin(BaseModelMixin):
    """
    Custom response mixin for retrieve operations.
    """
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                {
                    "status": "success",
                    "message": f"{self.model_name} retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while retrieving {self.model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CustomUpdateResponseMixin(BaseModelMixin):
    """
    Custom response mixin for update operations.
    """
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {
                    "status": "success",
                    "message": f"{self.model_name} updated successfully.",
                    "data": response.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while updating {self.model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CustomDeleteResponseMixin(BaseModelMixin):
    """
    Custom response mixin for delete operations.
    """
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {
                    "status": "success",
                    "message": f"{self.model_name} deleted successfully."
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while trying to delete {self.model_name.lower()}.",
                    "details": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

