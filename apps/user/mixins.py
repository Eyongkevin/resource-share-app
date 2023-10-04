from . import serializers


class RetrictInactiveUsersMixin:
    def get_serializer_class(self):
        if not self.request.user.is_active:
            return serializers.UserUpdateModelSerializer
        else:
            return serializers.UserModelSerializer
