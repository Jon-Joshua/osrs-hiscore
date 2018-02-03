import requests
import csv

class Hiscores:
    REGULAR = 0
    IRONMAN = 1
    U_IRONMAN = 2
    HC_IROMAN = 3
    DEADMAN = 4
    S_DEADMAN = 5


class Constants:
    # List of hiscore values in order of apperance in hiscore.
    SKILLS = [
            'overall', 'attack', 'strength', 'defence', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking',
            'woodcutting','fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore',
            'agility', 'theiving', 'slayer', 'farming', 'runecraft', 'hunter', 'construction'
    ]
    HISCORE_COLS = ['rank', 'level', 'experience']
    HISCORE_URLS = [ '', '_ironman', '_ultimate', '_hardcore_ironman', '_deadman', '_seasonal' ]


class HiscoresError(Exception):
    # Raise HiscoresError with smol error message.
    def raise_not_found(username):
        not_found_error_msg = '404 Error: {} not found in hiscore'.format(username)
        raise HiscoresError(not_found_error_msg)


class OSRSHiscores:
    # User-agent for http requests.
    USER_AGENT = 'osrs-hiscore'

    def __init__(self, user_agent=None):
        if user_agent != None:
            self.USER_AGENT = user_agent


    def get(self, username, hiscore=0):
        url = 'http://services.runescape.com/m=hiscore_oldschool{}/index_lite.ws?player={}'.format(Constants.HISCORE_URLS[hiscore], username)
        response = requests.get(url, headers={'User-agent': self.USER_AGENT})

        # If username not found, raise exception.
        if response.status_code == 404:
            HiscoresError.raise_not_found(username)

        return self._parse(response.content.decode('utf-8'))


    def _parse(self, response):
        # Parse request into CSV reader and split into list.
        reader = csv.reader(response.splitlines(), delimiter=',')
        hs_list = list(reader)

        hs_array = {}
        hs_cols = Constants.HISCORE_COLS
        hs_cols_len = len(hs_cols)
        hs_skills = Constants.SKILLS
        hs_skills_len = len(hs_skills)

        for x in range(hs_skills_len):
            cur_skill = hs_skills[x]
            hs_array[cur_skill] = {}
            for y in range(hs_cols_len):
                hs_array[cur_skill][hs_cols[y]] = int(hs_list[x][y])
        return hs_array



