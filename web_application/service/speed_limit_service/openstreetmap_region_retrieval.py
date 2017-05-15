import numpy as np
from threading import Thread

import web_application.service.speed_limit_service.openstreetmap_parser as parser
import web_application.service.speed_limit_service.openstreetmap_requester as openstreetmap_requester

#
# http://wiki.openstreetmap.org/wiki/Downloading_data#Construct_a_URL_for_the_HTTP_API
#

# left, bottom, right, top (min long, min lat, max long, max lat)
#URL = "http://api.openstreetmap.org/api/0.6/map?bbox={},{},{},{}"
URL2 = "http://api.openstreetmap.org/api/0.6/map?bbox={}"


def create_regions(coordinates):

    latitudes = list(map(lambda x: x['lat'], coordinates))
    longitudes = list(map(lambda x: x['lng'], coordinates))

    left1 = np.percentile(longitudes, 0)
    right1 = np.percentile(longitudes, .333)
    top1 = np.mean(latitudes)
    bottom1 = np.min(latitudes)
    r1_string = str(left1)+","+str(bottom1)+","+str(right1)+","+str(top1)

    left2 = np.percentile(longitudes, .333)
    right2 = np.percentile(longitudes, .666)
    top2 = np.mean(latitudes)
    bottom2 = np.min(latitudes)
    r2_string = str(left2)+","+str(bottom2)+","+str(right2)+","+str(top2)

    left3 = np.percentile(longitudes, .666)
    right3 = np.percentile(longitudes, 1)
    top3 = np.mean(latitudes)
    bottom3 = np.min(latitudes)
    r3_string = str(left3)+","+str(bottom3)+","+str(right3)+","+str(top3)











    left5 = np.percentile(longitudes, 0)
    right5 = np.percentile(longitudes, .333)
    top5 = np.max(latitudes)
    bottom5 = np.mean(latitudes)
    r5_string = str(left5)+","+str(bottom5)+","+str(right5)+","+str(top5)

    left6 = np.percentile(longitudes, .333)
    right6 = np.percentile(longitudes, .666)
    top6 = np.max(latitudes)
    bottom6 = np.mean(latitudes)
    r6_string = str(left6)+","+str(bottom6)+","+str(right6)+","+str(top6)

    left7 = np.percentile(longitudes, .666)
    right7 = np.percentile(longitudes, 1)
    top7 = np.max(latitudes)
    bottom7 = np.mean(latitudes)
    r7_string = str(left7)+","+str(bottom7)+","+str(right7)+","+str(top7)

    return [r1_string, r2_string, r3_string, r5_string, r6_string, r7_string]


def threaded_function(region, wayss):
    payload = openstreetmap_requester.do_request(URL2.format(region))
    ways_information = parser.do_the_parsing(payload)
    wayss.append(ways_information)


def retrieve_region_ways(coordinates):
    regions = create_regions(coordinates)

    wayss = []

    thread0 = Thread(target=threaded_function, args=(regions[0], wayss))
    thread0.start()

    thread1 = Thread(target=threaded_function, args=(regions[1], wayss))
    thread1.start()

    thread2 = Thread(target=threaded_function, args=(regions[2], wayss))
    thread2.start()

    thread3 = Thread(target=threaded_function, args=(regions[3], wayss))
    thread3.start()

    thread4 = Thread(target=threaded_function, args=(regions[4], wayss))
    thread4.start()

    thread5 = Thread(target=threaded_function, args=(regions[5], wayss))
    thread5.start()

    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    return wayss
