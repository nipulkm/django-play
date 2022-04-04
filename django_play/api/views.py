import json
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayViewApi(APIView):
    def get(self, request):
        
        data = {
            "user": "https://api.calendly.com/users/9f0ea630-5359-406b-9c90-e45b7ec2485f"
        }
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjQ5MDc3NDU0LCJqdGkiOiIxNGE5NmYyMC1kZDNkLTQ3M2EtYTA4Yi00NjNlMWU0NTIwZDMiLCJ1c2VyX3V1aWQiOiI0ZDZhZDVmNy03MGE0LTRhMTAtYmUwZS0yY2Q1Y2Y3NmE3OTEifQ.CUaIqn4MiQ_rvCjPy2hUb94qwlmRsE7uoai47RbRWNg",
            "Content-Type": "application/json"
        }
        url = "https://api.calendly.com/event_types"
        response = requests.get(url, headers=headers, data=json.dumps(data))
        return Response({"Messege: ": response.json()})

    def post(self, request):
        data = {
            "email": "nipulkm@gmail.com"
        }
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjQ5MDc3NDU0LCJqdGkiOiIxNGE5NmYyMC1kZDNkLTQ3M2EtYTA4Yi00NjNlMWU0NTIwZDMiLCJ1c2VyX3V1aWQiOiI0ZDZhZDVmNy03MGE0LTRhMTAtYmUwZS0yY2Q1Y2Y3NmE3OTEifQ.CUaIqn4MiQ_rvCjPy2hUb94qwlmRsE7uoai47RbRWNg",
            "Content-Type": "application/json"
        }
        url = "https://api.calendly.com/organizations/8e852818-cc51-4742-b3d9-718a7b6d1880/invitations"
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return Response({"Messege: ": response.json()})
