import requests
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class ThirdPartyAPIView(APIView):
    """
        Query Params:
            - status
            - ordering
            - search
            - page
            - limit
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        # Make a GET request to the third-party API endpoint
        url = 'http://localhost:8000/api/v1/task_3/product/'
        token = self.get_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        status = request.query_params.get('status')
        ordering = request.query_params.get('ordering')
        search = request.query_params.get('search')
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')

        params = {}
        if status:
            params['status'] = status
        if ordering:
            params['ordering'] = ordering
        if search:
            params['search'] = search
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        response = requests.get(url, headers=headers, params=params)

        # Handle the response
        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            # Handle error responses
            error_message = response.json().get('error_message')
            return Response({'error': error_message}, status=response.status_code)

    def get_token(self):
        url = 'http://127.0.0.1:8000/api/v1/task_1/token/'
        body = {
            "username": "admin",
            "password": "1"
        }

        response = requests.post(url, data=body)
        token = json.loads(response.text)
        return token['access']
