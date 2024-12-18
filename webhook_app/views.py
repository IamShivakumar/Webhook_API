from django.shortcuts import render
from rest_framework import generics,status
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webhook_app.serializers import AccountSerializer,DestinationSerializer
from webhook_app.models import Accounts,Destinations

#------------------Account CRUD Operation Views------------------------------------
class accountListCreateView(generics.ListCreateAPIView):
    queryset=Accounts.objects.all()
    serializer_class=AccountSerializer

class accountRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Accounts.objects.all()
    serializer_class=AccountSerializer
    lookup_field='account_id'

#------------------Destination CRUD Operation Views------------------------
class destionationListCreateView(generics.ListCreateAPIView):
    serializer_class=DestinationSerializer
    def get_queryset(self):
        return Destinations.objects.filter(account__account_id=self.kwargs['account_id'])
    def perform_create(self, serializer):
        account = Accounts.objects.get(account_id=self.kwargs['account_id'])
        serializer.save(account=account)
    
class destinationRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Destinations.objects.all()
    serializer_class=DestinationSerializer

#----------------Handling Incoming Data------------------------------------------
@api_view(['POST'])
def incoming_data(request):
    token=request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({'message':"Un Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        account=Accounts.objects.get(app_secret_token=token)
        data=request.data
        destinations=Destinations.objects.filter(account=account)
        for destination in destinations:
            url = destination.url
            method = destination.http_method
            headers = destination.headers
            print(url,method,headers)
            if method=="GET":
                print("Inside GET Method")
                if not isinstance(data,dict):
                    return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
                response=requests.get(url=url, params=data, headers=headers)
            elif method in ["POST","PUT"]:
                print("Inside Post Or Put Method")
                response= requests.request(method,url,json=data,headers=headers)
            # if response.status_code != 200:
            #     return Response({'error': f'Failed to send to {url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": "Data sent successfully"}, status=status.HTTP_200_OK)
    except Accounts.DoesNotExist:
        return Response({"message": "Invalid Token"}, status=status.HTTP_401_UNAUTHORIZED)