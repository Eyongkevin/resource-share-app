from django.utils.deprecation import MiddlewareMixin


class HandleContentTypeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """Called during pre-processing"""

        # breakpoint()
        request.headers["Content-Type"] = (
            "" if request.headers.get("Content-Type") is None else None
        )

    def process_response(self, request, response):
        """Called during post-processing"""

        return response
