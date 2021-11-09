import adal

tenant = "ca56a4a5-e300-406a-98ff-7e36a0baac5b"

sql_hostname = "sql113372e1dv.database.windows.net"

database_name = "cfl"

authority_host_uri = "https://login.microsoftonline.com"

authority_uri = authority_host_uri + '/' + tenant

client_id = "81159413-2ac8-4d22-894d-f9ef01b185bb"

resource_app_id_url = "https://database.windows.net"

context = adal.AuthenticationContext(authority_uri, api_version=None)
code = "b3411249-d316-49c1-9db1-b75b970837ca"
token = context.acquire_token_with_client_credentials(resource_app_id_url, code, client_id)
tokenx = bytes(token["accessToken"], "UTF-8")
print(tokenx)