import os
from django import views
from django.shortcuts import render
from google.cloud import bigquery

from google_auth_oauthlib import flow

# # : Uncomment the line below to set the `launch_browser` variable.
# launch_browser = True
# #
# # The `launch_browser` boolean variable indicates if a local server is used
# # as the callback URL in the auth flow. A value of `True` is recommended,
# # but a local server does not work if accessing the application remotely,
# # such as over SSH or from a remote Jupyter notebook.

# appflow = flow.InstalledAppFlow.from_client_secrets_file(
#     "client_secret.json", scopes=["https://www.googleapis.com/auth/bigquery"]
# )

# if launch_browser:
#     appflow.run_local_server()
# else:
#     appflow.run_console()

# credentials = appflow.credentials

credentials_path = '/home/nipul/project/django-play/django_play/test-big-query-360506-532c845d5c08.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


class BigQuery():

    # client = bigquery.Client(project='test-big-query-360506',credentials= credentials)
    client = bigquery.Client()
    # table_id = 'test-big-query-360506.test_big_query.user_information'
    # rows_to_insert = [
    #     {u'name': 'A', 'status': True, 'value': 22},
    #     {u'name': 'B', 'status': False, 'value': 22}
    # ]
    # errors = client.insert_rows_json(table_id, rows_to_insert)
    # if errors == []:
    #     print('ROWS ADDED!!!')
    # else:
    #     print('FAILED TO ADD!!!')


    # Perform a query.
    # QUERY = (
    #     'INSERT INTO `test-big-query-360506.test_big_query.user_information`'
    #     'VALUES ("A", "true", 20)'
    # )
    QUERY = (
        'SELECT * FROM `test-big-query-360506.test_big_query.user_information`'
    )

    print("0")
    query_job = client.query(QUERY)  # API request
    print("A")
    rows = query_job.result()  # Waits for query to finish

    print("B")
    for row in rows:
        print('A')
