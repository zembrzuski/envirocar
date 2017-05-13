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

    # TODO separar em 4 lugares esse cara.
    left1 = np.min(longitudes)
    right1 = np.mean(longitudes)
    top1 = np.mean(latitudes)
    bottom1 = np.min(latitudes)
    r1_string = str(left1)+","+str(bottom1)+","+str(right1)+","+str(top1)

    left2 = np.mean(longitudes)
    right2 = np.max(longitudes)
    top2 = np.mean(latitudes)
    bottom2 = np.min(latitudes)
    r2_string = str(left2) + "," + str(bottom2) + "," + str(right2) + "," + str(top2)

    left3 = np.min(longitudes)
    right3 = np.mean(longitudes)
    top3 = np.max(latitudes)
    bottom3 = np.mean(latitudes)
    r3_string = str(left3) + "," + str(bottom3) + "," + str(right3) + "," + str(top3)

    left4 = np.mean(longitudes)
    right4 = np.max(longitudes)
    top4 = np.max(latitudes)
    bottom4 = np.mean(latitudes)
    r4_string = str(left4) + "," + str(bottom4) + "," + str(right4) + "," + str(top4)

    reg1_top_left     = r1_string
    reg2_top_right    = r2_string
    reg3_bottom_left  = r3_string
    reg4_bottom_right = r4_string

    return [reg1_top_left, reg2_top_right, reg3_bottom_left, reg4_bottom_right]


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

    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()

    return wayss
