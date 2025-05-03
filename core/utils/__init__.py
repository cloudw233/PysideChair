from datetime import datetime
from astral.sun import sun
from astral import LocationInfo


def is_daytime(city="Beijing", lat=39.9, lon=116.4):
    # 创建城市位置信息
    location = LocationInfo(
        name=city,
        region="China",
        timezone="Asia/Shanghai",
        latitude=lat,
        longitude=lon
    )

    s = sun(location.observer, date=datetime.now())
    current_time = datetime.now()

    return s["sunrise"].time() <= current_time.time() <= s["sunset"].time()
