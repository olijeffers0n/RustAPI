import json
import random
import time

from ..rustplus_proto import AppTeamInfo


class TeamManager:

    _leader_id: int = 0
    _members = []

    @staticmethod
    def init() -> None:
        with open("./rustapi/data/team.json", "r") as team:
            data = json.load(team)
            TeamManager._leader_id = data["leaderId"]
            TeamManager._members = data["members"]

    @staticmethod
    def get_team_info() -> AppTeamInfo:
        team_info = AppTeamInfo()
        team_info.leaderSteamId = TeamManager._leader_id

        members = []
        for member in TeamManager._members:
            mem = AppTeamInfo.Member()
            mem.steamId = member["id"]
            mem.name = member["name"]
            mem.x = random.randint(0, 6000000) / 1000
            mem.y = random.randint(0, 6000000) / 1000
            online = bool(random.randint(0, 1))
            mem.isOnline = online
            mem.spawnTime = int(time.time() - random.randint(0, 60*60*12))
            mem.isAlive = bool(random.randint(0, 1)) if online else False
            mem.deathTime = int(time.time() - random.randint(0, 60*60*10)) if not mem.isAlive else 0

            members.append(mem)

        team_info.members.extend(members)

        return team_info
