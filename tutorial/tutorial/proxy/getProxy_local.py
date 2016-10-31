import requests
import json

def getProxy_local(filename):
    """

    :param filename:
    :return:  map{1:url, 2:url,...}
    """
    with open(filename,'r') as f:
        map=json.load(f)

    return map


