from flask import jsonify, Blueprint, render_template
from AnilistPython import Anilist

server = Blueprint(__name__, "server")

def getData():
    anilist = Anilist()
    anime = anilist.get_anime("one piece")
    nameOfAnime = anime["name_english"]
    epNumber = anime["next_airing_ep"]["episode"]
    nextEpRelease = anime["next_airing_ep"]["timeUntilAiring"]
    min, sec = divmod(nextEpRelease, 60)
    hours, min = divmod(min, 60)
    days, hours = divmod(hours, 24)
    data = {"name": nameOfAnime, "epNum": epNumber, "days": days, "hours": hours, "min": min, "sec": sec}
    return data

@server.route('/')
def getNextEpisode():
    data = getData()
    return render_template("index.html", anime=data["name"], epNum=data["epNum"], days=data["days"], hours=data["hours"], min=data["min"], sec=data["sec"])

@server.route('/data')
def getJson():
    data = getData()
    return jsonify(data)



