from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from cloudy.cloudAuth.models import Credential
from libcloud.types import Provider 
from libcloud.providers import get_driver,DRIVERS

def index(request):
    return render_to_response( 'consoleHome/index.html' )


def node_list(request):
    nodes = []
    providers = []
    accounts = Credential.objects.all()

    for account in accounts:
         provider = account.service_provider
         Driver = get_driver(provider)

         id = account.api_id
         secret = account.api_secret

         conn = Driver(account.api_id, account.api_secret)
         nodes[provider] = conn.list_nodes()
         providers.append(provider)

    return render_to_response( 'consoleHome/node_list.html', {
        'nodes': nodes,
        'providers': providers,
    } )


