from django.shortcuts import render

import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "80eb4aa2f3msh280c9abec6fc23ep135073jsn14f5a58e28aa",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# print(response.text)

# Create your views here.


def dashboardview(request):

    mylist = []
    noofresult = int(response['results'])

    # new_world = response['response']['All']['cases']['new']

    for x in range(0, noofresult):
        mylist.append(response['response'][x]['country'])

        if response['response'][x]['country'] == "All":
            world_index = x
        elif response['response'][x]['country'] == "Thailand":
            thai_index = x

    new_world = response['response'][world_index]['cases']['new']
    active_world = response['response'][world_index]['cases']['active']
    critical_world = response['response'][world_index]['cases']['critical']
    recovered_world = response['response'][world_index]['cases']['recovered']
    total_world = response['response'][world_index]['cases']['total']
    deaths_world = response['response'][world_index]['deaths']['total']


    selectedcountry = 'Thailand'
    new = response['response'][thai_index]['cases']['new']
    active = response['response'][thai_index]['cases']['active']
    critical = response['response'][thai_index]['cases']['critical']
    recovered = response['response'][thai_index]['cases']['recovered']
    total = response['response'][thai_index]['cases']['total']
    deaths = response['response'][thai_index]['deaths']['total']


    context = {'mylist': mylist, 'new_world': new_world, 'active_world': active_world, 'critical_world': critical_world, 'recovered_world': recovered_world, 'total_world': total_world, 'deaths_world': deaths_world,
               'selectedcountry': selectedcountry, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}

    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']

        noofresult = int(response['results'])

        for x in range(0, noofresult):

            if selectedcountry == response['response'][x]['country']:

                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = response['response'][x]['deaths']['total']

                if deaths == None:
                    deaths = str(0)

                if critical == None:
                    critical = str(0)
                
                if new == None:
                    new = str(0)

                if total == None:
                    total = str(0)

                if active == None:
                    active = str(0)

                if recovered == None:
                    recovered = str(0)


        context = {'mylist': mylist, 'new_world': new_world, 'active_world': active_world, 'critical_world': critical_world, 'recovered_world': recovered_world, 'total_world': total_world, 'deaths_world': deaths_world,
                   'selectedcountry': selectedcountry, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}

        return render(request, 'coviddashboard.html', context)

    # because render function does not accept string directly. it only accepts dictionary.
    return render(request, 'coviddashboard.html', context)
