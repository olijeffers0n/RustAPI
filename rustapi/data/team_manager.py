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
            members = data["members"]

        for member in members:
            mem = AppTeamInfo.Member()
            mem.steamId = member["id"]
            mem.name = member["name"]
            online = bool(random.randint(0, 1))
            mem.isOnline = online
            mem.spawnTime = int(time.time() - random.randint(0, 60*60*12))
            mem.isAlive = bool(random.randint(0, 1))
            mem.deathTime = int(time.time() - random.randint(0, 60*60*10)) if not mem.isAlive else 0
            mem.x = random.randint(1000000, 5000000) / 1000
            mem.y = random.randint(1000000, 5000000) / 1000

            TeamManager._members.append(mem)


    @staticmethod
    def _offset_coords(member) -> AppTeamInfo.Member:

        member.x += random.randint(-100, 100) / 10
        member.y += random.randint(-100, 100) / 10

        member.x = max(500, min(5500, member.x))
        member.y = max(500, min(5500, member.y))

        return member

    @staticmethod
    def get_team_info() -> AppTeamInfo:
        team_info = AppTeamInfo()
        team_info.leaderSteamId = TeamManager._leader_id

        members = []
        for member in TeamManager._members:
            if member.isOnline:
                member = TeamManager._offset_coords(member)

            members.append(member)

        team_info.members.extend(members)

        return team_info

    @staticmethod
    def set_leader(current, target) -> bool:

        if current != TeamManager._leader_id:
            return False

        if target not in [member["id"] for member in TeamManager._members]:
            return False

        TeamManager._leader_id = target
        return True
