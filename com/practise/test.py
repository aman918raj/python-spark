from azure.identity import  DefaultAzureCredential
import os

#os.environ["ANALYTICS_SQL_CONNECTION_STRING"]="mssql+pyodbc:///?odbc_connect=DRIVER%3D%7BODBC+Driver+17+for+SQL+Server%7D%3BSERVER%3Dtcp%3Asql113372e1dv.database.windows.net%2C1433%3BDATABASE%3Dsql113372e1dv%3BAuthentication%3DActiveDirectoryMsi%3B"

azure_credentials = DefaultAzureCredential()
TOKEN_URL = "https://database.windows.net/"
SQL_COPT_SS_ACCESS_TOKEN = 1256
raw_token = azure_credentials.get_token(TOKEN_URL).token.encode("utf-16-le")
print(raw_token)

