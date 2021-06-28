from poetry.core.utils._compat import urlparse


def get_current_url(request):
    current_url = urlparse.urlparse(request.url)
    return urlparse.urlunparse((current_url.scheme, current_url.netloc, "", "", "", ""))
