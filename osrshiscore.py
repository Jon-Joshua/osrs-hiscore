import requests
import csv

class HiscoreError(Exception):
    pass

class OSRSHiscore:

    def __init__(self, user_agent=None):
        if user_agent != None:
            self.user_agent = user_agent

    user_agent = 'osrs-hiscore'

    # Raise HiscoreError with smol error message.
    def raise_not_found(self, username):
        not_found_error_msg = '404 Error: {} not found in hiscore'.format(username)
        raise HiscoreError(not_found_error_msg)

    def get(self, username, hiscore=''):
        # Change hiscore kwarg to hiscore url appendix.
        hiscore_url = ''
        if hiscore != '':
            if hiscore == 'im':
                hiscore_url = '_ironman'
            elif hiscore == 'ui':
                hiscore_url = '_ultimate'
            elif hiscore == 'hci':
                hiscore_url = '_hardcore_ironman'
            elif hiscore == 'dmm':
                hiscore_url = '_deadman'
            elif hiscore == 'sdmm':
                hiscore_url = '_seasonal'
            else:
                return

        url = 'http://services.runescape.com/m=hiscore_oldschool{}/index_lite.ws?player={}'.format(hiscore_url, username)

        response = requests.get(url, headers={'User-agent': self.user_agent})

        # If username not found, raise exception.
        if response.status_code == 404:
            self.raise_not_found(username)

        return self._parse(response.content.decode('utf-8'))

    def _parse(self, response):
        hs_array = {}

        # List of hiscore values in order of apperance in hiscore.
        skills = [
                'overall', 'attack', 'strength', 'defence', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking',
                'woodcutting','fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore',
                'agility', 'theiving', 'slayer', 'farming', 'runecraft', 'hunter', 'construction'
        ]

        titles = ['rank', 'level', 'experience']

        reader = csv.reader(response.splitlines(), delimiter=',')
        hs_list = list(reader)

        for x in range(len(skills)):
            cur_skill = skills[x]
            hs_array[cur_skill] = {}
            for y in range(len(titles)):
                hs_array[cur_skill][titles[y]] = int(hs_list[x][y])
        return hs_array



