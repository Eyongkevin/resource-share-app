from rest_framework.exceptions import PermissionDenied

DEFAULT_CATEGORY_ID = 1


# <idea>Mixin
class DenyDeletionOfDefaultCategoryMixin:
    # We want to get the category's id we are about to delete
    # We want to compare it with the DEFAULT_CATEGORY_ID
    # If True, we want raise an exception.

    # This is the method to use for Listing
    def get_queryset(self):
        queryset = super().get_queryset()
        # breakpoint()
        if (
            not hasattr(self, "action") or self.action == "destroy"
        ):  # because of viewsets
            pk = self.kwargs["pk"]
            deleted_queryset = queryset.get(pk=pk)
            if deleted_queryset.pk == DEFAULT_CATEGORY_ID:
                # raise an exception
                raise PermissionDenied(f"Not allowed to delete category with id {pk}")
        # Never forget
        return queryset

    # def get_object(self)  is expected to return a single object.


#  def destroy(self, request, *args, **kwargs):
#      breakpoint()
