from django.db.models import Q
from django.http import HttpResponse
from app01 import models
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# def addCSV(request):
#     df = pd.read_csv("C:/Users/Mingle/Desktop/NY-House-Dataset.csv",
#                      encoding='utf-8')
#     for index, row in df.iterrows():
 #         beds_value = row['BEDS']
#         hashed_value = hash(beds_value)
#         if hashed_value % 2 == 0:
#             models.Property.objects.create(BROKERTITLE=row['BROKERTITLE'], TYPE=row["TYPE"], PRICE=row['PRICE'],
#                                            BEDS=row['BEDS']
#                                            , BATH=row['BATH'], PROPERTYSQFT=row['PROPERTYSQFT'], ADDRESS=row['ADDRESS'],
#                                            STATE=row['STATE']
#                                            , MAIN_ADDRESS=row['MAIN_ADDRESS'],
#                                            ADMINISTRATIVE_AREA_LEVEL_2=row['ADMINISTRATIVE_AREA_LEVEL_2']
#                                            , LOCALITY=row['LOCALITY'], SUBLOCALITY=row['SUBLOCALITY'],
#                                            STREET_NAME=row['STREET_NAME']
#                                            , LONG_NAME=row['LONG_NAME'], FORMATTED_ADDRESS=row['FORMATTED_ADDRESS'],
#                                            LATITUDE=row['LATITUDE'], LONGITUDE=row['LONGITUDE'])
#         else:
#             models.Property.objects.using("secondary").create(BROKERTITLE=row['BROKERTITLE'], TYPE=row["TYPE"],
#                                                               PRICE=row['PRICE'], BEDS=row['BEDS']
#                                                               , BATH=row['BATH'], PROPERTYSQFT=row['PROPERTYSQFT'],
#                                                               ADDRESS=row['ADDRESS'], STATE=row['STATE']
#                                                               , MAIN_ADDRESS=row['MAIN_ADDRESS'],
#                                                               ADMINISTRATIVE_AREA_LEVEL_2=row[
#                                                                   'ADMINISTRATIVE_AREA_LEVEL_2']
#                                                               , LOCALITY=row['LOCALITY'],
#                                                               SUBLOCALITY=row['SUBLOCALITY'],
#                                                               STREET_NAME=row['STREET_NAME']
#                                                               , LONG_NAME=row['LONG_NAME'],
#                                                               FORMATTED_ADDRESS=row['FORMATTED_ADDRESS'],
#                                                               LATITUDE=row['LATITUDE'], LONGITUDE=row['LONGITUDE'])
#
#     return HttpResponse("CSV file processing successful")


def house_list(request, page=1):
    # Get the search parameters from the GET request
    Broker_title = request.GET.get('searchBROKERTITLE', "")
    search_type = request.GET.get('searchType', "")
    search_address = request.GET.get('searchAddress', "")
    # Create a query object to store the query parameters
    query = Q()
    # If the Broker title is provided, add it to the query
    if Broker_title:
        query &= Q(BROKERTITLE__icontains=Broker_title)
    # If the search type is provided, add it to the query
    if search_type:
        query &= Q(TYPE__icontains=search_type)
    # If the search address is provided, add it to the query
    if search_address:
        query &= Q(MAIN_ADDRESS__icontains=search_address)
    # Filter the properties based on the query parameters
    informations1 = models.Property.objects.filter(query)
    informations2 = models.Property.objects.using("secondary").filter(query)
    # Combine the two filtered queries
    combined_informations = list(informations1) + list(informations2)
    # Create a paginator object with the combined informations and the page number
    paginator = Paginator(combined_informations, 10, 1)
    # Get the page information based on the page number
    try:
        pageInfo = paginator.get_page(page)
    # If the page number is not an integer, get the first page
    except PageNotAnInteger:
        pageInfo = paginator.get_page(1)
    # If the page number is out of range, get the last page
    except EmptyPage:
        pageInfo = paginator.get_page(paginator.num_pages)
    # Create a context dictionary with the search parameters and the page information
    context = {
        'Broker_title': Broker_title,
        'search_type': search_type,
        'search_address': search_address,
        "pageInfo": pageInfo,
    }
    # Render the page with the context
    return render(request, 'house_list.html', {"context": context})


def house_list_add(request):
    if request.method == "GET":
        return render(request, 'house_add.html')

    # Get the values of the form fields
    BROKERTITLE = request.POST.get('BROKERTITLE')
    TYPE = request.POST.get('TYPE')
    PRICE = request.POST.get('PRICE')
    BEDS = request.POST.get('BEDS')
    BATH = request.POST.get('BATH')
    PROPERTYSQFT = request.POST.get('PROPERTYSQFT')
    ADDRESS = request.POST.get('ADDRESS')
    STATE = request.POST.get('STATE')
    MAIN_ADDRESS = request.POST.get('MAIN_ADDRESS')
    ADMINISTRATIVE_AREA_LEVEL_2 = request.POST.get('ADMINISTRATIVE_AREA_LEVEL_2')
    LOCALITY = request.POST.get('LOCALITY')
    SUBLOCALITY = request.POST.get('SUBLOCALITY')
    STREET_NAME = request.POST.get('STREET_NAME')
    LONG_NAME = request.POST.get('LONG_NAME')
    FORMATTED_ADDRESS = request.POST.get('FORMATTED_ADDRESS')
    LATITUDE = request.POST.get('LATITUDE')
    LONGITUDE = request.POST.get('LONGITUDE')

    beds_hash = hash(int(BEDS))
    if beds_hash % 2 == 0:
        # This line creates a new Property object in the primary database
        models.Property.objects.create(BROKERTITLE=BROKERTITLE, TYPE=TYPE, PRICE=PRICE,
                                       BEDS=BEDS
                                       , BATH=BATH, PROPERTYSQFT=PROPERTYSQFT, ADDRESS=ADDRESS,
                                       STATE=STATE
                                       , MAIN_ADDRESS=MAIN_ADDRESS,
                                       ADMINISTRATIVE_AREA_LEVEL_2=ADMINISTRATIVE_AREA_LEVEL_2
                                       , LOCALITY=LOCALITY, SUBLOCALITY=SUBLOCALITY,
                                       STREET_NAME=STREET_NAME
                                       , LONG_NAME=LONG_NAME, FORMATTED_ADDRESS=FORMATTED_ADDRESS,
                                       LATITUDE=LATITUDE, LONGITUDE=LONGITUDE)

    else:
        # This line creates a new Property object in the secondary database
        models.Property.objects.using("secondary").create(BROKERTITLE=BROKERTITLE, TYPE=TYPE, PRICE=PRICE,
                                                          BEDS=BEDS
                                                          , BATH=BATH, PROPERTYSQFT=PROPERTYSQFT, ADDRESS=ADDRESS,
                                                          STATE=STATE
                                                          , MAIN_ADDRESS=MAIN_ADDRESS,
                                                          ADMINISTRATIVE_AREA_LEVEL_2=ADMINISTRATIVE_AREA_LEVEL_2
                                                          , LOCALITY=LOCALITY, SUBLOCALITY=SUBLOCALITY,
                                                          STREET_NAME=STREET_NAME
                                                          , LONG_NAME=LONG_NAME, FORMATTED_ADDRESS=FORMATTED_ADDRESS,
                                                          LATITUDE=LATITUDE, LONGITUDE=LONGITUDE)

    # This line redirects the user to the houseList view
    return redirect("/houseList/")


def house_list_edit(request, nid, sid):
    if request.method == "GET":
        beds_hash = hash(int(sid))
        if beds_hash % 2 == 0:
            row_object = models.Property.objects.filter(Id=nid).first()
            return render(request, 'house_add.html', {"row_object": row_object})
        else:
            row_object = models.Property.objects.using("secondary").filter(Id=nid).first()
            return render(request, 'house_add.html', {"row_object": row_object})

    BROKERTITLE = request.POST.get('BROKERTITLE')
    TYPE = request.POST.get('TYPE')
    PRICE = request.POST.get('PRICE')
    BEDS = request.POST.get('BEDS')
    BATH = request.POST.get('BATH')
    PROPERTYSQFT = request.POST.get('PROPERTYSQFT')
    ADDRESS = request.POST.get('ADDRESS')
    STATE = request.POST.get('STATE')
    MAIN_ADDRESS = request.POST.get('MAIN_ADDRESS')
    ADMINISTRATIVE_AREA_LEVEL_2 = request.POST.get('ADMINISTRATIVE_AREA_LEVEL_2')
    LOCALITY = request.POST.get('LOCALITY')
    SUBLOCALITY = request.POST.get('SUBLOCALITY')
    STREET_NAME = request.POST.get('STREET_NAME')
    LONG_NAME = request.POST.get('LONG_NAME')
    FORMATTED_ADDRESS = request.POST.get('FORMATTED_ADDRESS')
    LATITUDE = request.POST.get('LATITUDE')
    LONGITUDE = request.POST.get('LONGITUDE')
    if hash(int(BEDS)) % 2 == 0:
        models.Property.objects.filter(Id=nid).update(BROKERTITLE=BROKERTITLE, TYPE=TYPE, PRICE=PRICE,
                                                      BEDS=BEDS
                                                      , BATH=BATH, PROPERTYSQFT=PROPERTYSQFT, ADDRESS=ADDRESS,
                                                      STATE=STATE
                                                      , MAIN_ADDRESS=MAIN_ADDRESS,
                                                      ADMINISTRATIVE_AREA_LEVEL_2=ADMINISTRATIVE_AREA_LEVEL_2
                                                      , LOCALITY=LOCALITY, SUBLOCALITY=SUBLOCALITY,
                                                      STREET_NAME=STREET_NAME
                                                      , LONG_NAME=LONG_NAME, FORMATTED_ADDRESS=FORMATTED_ADDRESS,
                                                      LATITUDE=LATITUDE, LONGITUDE=LONGITUDE)
    else:
        models.Property.objects.using("secondary").filter(Id=nid).update(BROKERTITLE=BROKERTITLE, TYPE=TYPE,
                                                                         PRICE=PRICE,
                                                                         BEDS=BEDS
                                                                         , BATH=BATH, PROPERTYSQFT=PROPERTYSQFT,
                                                                         ADDRESS=ADDRESS,
                                                                         STATE=STATE
                                                                         , MAIN_ADDRESS=MAIN_ADDRESS,
                                                                         ADMINISTRATIVE_AREA_LEVEL_2=ADMINISTRATIVE_AREA_LEVEL_2
                                                                         , LOCALITY=LOCALITY, SUBLOCALITY=SUBLOCALITY,
                                                                         STREET_NAME=STREET_NAME
                                                                         , LONG_NAME=LONG_NAME,
                                                                         FORMATTED_ADDRESS=FORMATTED_ADDRESS,
                                                                         LATITUDE=LATITUDE, LONGITUDE=LONGITUDE)
    return redirect("/houseList/")


def house_delete(request, nid, sid):
    if request.method == "GET":
        beds_hash = hash(int(sid))
        if beds_hash % 2 == 0:
            models.Property.objects.filter(Id=nid).delete()
        else:
            models.Property.objects.using("secondary").filter(Id=nid).delete()
    return redirect("/houseList/")


def houseListUser(request, page=1):
    Broker_title = request.GET.get('searchBROKERTITLE', "")
    search_type = request.GET.get('searchType', "")
    search_address = request.GET.get('searchAddress', "")
    query = Q()
    if Broker_title:
        query &= Q(BROKERTITLE__icontains=Broker_title)
    if search_type:
        query &= Q(TYPE__icontains=search_type)
    if search_address:
        query &= Q(MAIN_ADDRESS__icontains=search_address)
    informations1 = models.Property.objects.filter(query)
    informations2 = models.Property.objects.using("secondary").filter(query)
    combined_informations = list(informations1) + list(informations2)
    paginator = Paginator(combined_informations, 10, 1)
    try:
        pageInfo = paginator.get_page(page)
    except PageNotAnInteger:
        pageInfo = paginator.get_page(1)
    except EmptyPage:
        pageInfo = paginator.get_page(paginator.num_pages)
    context = {
        'Broker_title': Broker_title,
        'search_type': search_type,
        'search_address': search_address,
        "pageInfo": pageInfo,
    }
    return render(request, 'house_list1.html', {"context": context})
