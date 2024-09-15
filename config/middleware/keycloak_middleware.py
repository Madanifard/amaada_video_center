from keycloak import KeycloakOpenID
from django.conf import settings
from django.http import JsonResponse

keycloak_openid = KeycloakOpenID(
    server_url=f"{settings.KEYCLOAK_CONFIG['KEYCLOAK_URL']}/",
    client_id=settings.KEYCLOAK_CONFIG['CLIENT_ID'],
    realm_name=settings.KEYCLOAK_CONFIG['REALM'],
    client_secret_key=settings.KEYCLOAK_CONFIG['CLIENT_SECRET'],
    verify=settings.KEYCLOAK_CONFIG['VERIFY_SSL']
)


class KeycloakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization', None)

        if token:
            try:
                token = token.split()[1]
                user_info = keycloak_openid.userinfo(token)
                request.user_info = user_info
            except Exception as e:
                return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)
        return response
