"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    """
    x = control_dist_km
    control = x
    time = 0

    if 600 < control <= 1000:
        y = x
        y =- 600
        time =+ (y/28)
        time =+ (200/30) + (200/32) + (200/34)
    elif 400 < control <= 600:
        y = x
        y =- 400
        time =+ (y/30)
        time =+ (200/32) + (200/34)
    elif 200 < control <= 400:
        y = x
        y =- 200
        time =+ (y/32)
        time =+ (200/34)
    else:
        time =+ (x/34)

    x = parseInt(time, 10)
    y = (time - x) * 60

    start = arrow.get(brevet_start_time)
    start = start.replace(hours =+ x)
    start = start.replace(minutes =+ y)
    """
    return arrow.now().isoformat 


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    """
    x = control_dist_km
    control = x
    time = 0

    if 600 < control <= 1000:
        y = x
        y =- 600
        time =+ (y/11.428)
        time =+ (600/15)
    else:
        time =+ (x/15)

    x = parseInt(time, 10)
    y = (time - x) * 60

    end = arrow.get(brevet_start_time)
    end = start.replace(hours =+ x)
    end = start.replace(minutes =+ y)
    """
    return arrow.now().isoformat
