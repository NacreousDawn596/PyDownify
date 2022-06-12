import re
import requests
import sys

def get(url):
    html=str(requests.get(url).text)
    end_point, dependent, independent = [], [".png",".jpg",".wav",".jpeg",".json",".js",".php",".xml"], ["http://","https://","file://","php://","ftp://","./","../","/"]
    for i in [idk.split("\\")[0] for idk in re.split(f"'|\"|,|\*|\n|[|]", html) if idk.split("\\")[0] != ""]:
        if not i:
            pass
        else:
            for de in independent:
                if i.startswith(de): end_point.append(i)
            for ind in dependent:
                if i.endswith(ind):
                    if i[0] == "/": end_point.append(f"{url}{i}")
                    else: end_point.append(f"{url}/{i}")
    ik = []
    for idk in [item for item in end_point if item != []]:
        if idk[0] == "/": ik.append(f"{url}{idk}")
        else: ik.append(idk)
    return ik
