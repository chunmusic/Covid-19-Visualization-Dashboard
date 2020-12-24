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
    population_world = 0
    noofresult = int(response['results'])

    # new_world = response['response']['All']['cases']['new']

    for x in range(0, noofresult):
        mylist.append(response['response'][x]['country'])

        if response['response'][x]['country'] == "All":
            world_index = x
        elif response['response'][x]['country'] == "Thailand":
            thai_index = x

        if response['response'][x]['population'] == None:
            population_world += 0
        else:
            population_world += response['response'][x]['population']


    new_world = "{:,}".format(int(response['response'][world_index]['cases']['new']))
    active_world = "{:,}".format(int(response['response'][world_index]['cases']['active']))
    critical_world = "{:,}".format(int(response['response'][world_index]['cases']['critical']))
    recovered_world = "{:,}".format(int(response['response'][world_index]['cases']['recovered']))

    total_world_raw = int(response['response'][world_index]['cases']['total'])
    total_world = "{:,}".format(total_world_raw)
    
    deaths_world = "{:,}".format(int(response['response'][world_index]['deaths']['total']))

    population_world_raw = int(population_world)
    population_world = "{:,}".format(population_world)

    infected_world_percent = round((total_world_raw/population_world_raw)*100,2)

    selectedcountry = 'Thailand'
    new = "{:,}".format(int(response['response'][thai_index]['cases']['new']))
    active = "{:,}".format(int(response['response'][thai_index]['cases']['active']))
    critical = "{:,}".format(int(response['response'][thai_index]['cases']['critical']))
    recovered = "{:,}".format(int(response['response'][thai_index]['cases']['recovered']))

    total_raw = int(response['response'][thai_index]['cases']['total'])
    total = "{:,}".format(total_raw)
    
    deaths = "{:,}".format(int(response['response'][thai_index]['deaths']['total']))

    population_raw = int(response['response'][thai_index]['population'])
    population = "{:,}".format(int(response['response'][thai_index]['population']))

    infected_percent = round((total_raw/population_raw)*100,2)

    date = response['response'][thai_index]['day']


    context = {'mylist': mylist, 'new_world': new_world, 'active_world': active_world, 'critical_world': critical_world, 'recovered_world': recovered_world, 'total_world': total_world, 'deaths_world': deaths_world,
                'population_raw':population_raw, 'population_world_raw':population_world_raw,'population_world':population_world,'population':population,'total_world_raw':total_world_raw,'total_raw':total_raw,
                'infected_world_percent':infected_world_percent,'infected_percent':infected_percent,
                'date':date,'selectedcountry': selectedcountry, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}

    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']

        noofresult = int(response['results'])

        for x in range(0, noofresult):

            if selectedcountry == response['response'][x]['country']:


                date = response['response'][x]['day']

                if response['response'][x]['deaths']['total'] == None:
                    deaths = str(0)
                else:
                    deaths = "{:,}".format(int(response['response'][x]['deaths']['total']))

                if response['response'][x]['cases']['critical'] == None:
                    critical = str(0)
                else:
                    critical = "{:,}".format(int(response['response'][x]['cases']['critical']))

                if response['response'][x]['cases']['new'] == None:
                    new = str(0)
                else:
                    new = "{:,}".format(int(response['response'][x]['cases']['new']))

                if response['response'][x]['cases']['total'] == None:
                    total = str(0)
                    total_raw = 0 
                else:
                    total = "{:,}".format(int(response['response'][x]['cases']['total']))
                    total_raw = int(response['response'][x]['cases']['total'])

                if response['response'][x]['cases']['active'] == None:
                    active = str(0)
                else:
                    active = "{:,}".format(int(response['response'][x]['cases']['active']))

                if response['response'][x]['cases']['recovered'] == None:
                    recovered = str(0)
                else:
                    recovered = "{:,}".format(int(response['response'][x]['cases']['recovered']))

                if response['response'][x]['population'] == None:
                    population = str(0)
                else:
                    population_raw = int(response['response'][x]['population'])
                    population = "{:,}".format(int(response['response'][x]['population']))

                infected_percent = round((total_raw/population_raw)*100,2)


        context = {'mylist': mylist, 'new_world': new_world, 'active_world': active_world, 'critical_world': critical_world, 'recovered_world': recovered_world, 'total_world': total_world, 'deaths_world': deaths_world,
                   'population_raw':population_raw, 'population_world_raw':population_world_raw,'population_world':population_world,'population':population,'total_world_raw':total_world_raw,'total_raw':total_raw,
                   'infected_world_percent':infected_world_percent,'infected_percent':infected_percent,
                   'date':date,'selectedcountry': selectedcountry, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}

        return render(request, 'coviddashboard.html', context)

    # because render function does not accept string directly. it only accepts dictionary.
    return render(request, 'coviddashboard.html', context)
