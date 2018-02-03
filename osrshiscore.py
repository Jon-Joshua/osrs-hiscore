import requests

class OSRSHiscore:

    user_agent = 'osrs-hiscore'

    def get(self, username, hiscore=''):
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

        if response.status_code == 404:
            return

        parsed = self._parse(response.text)
        return parsed

    def _parse(self, response):
        hiscore_array = {}

        skills = [
                'overall', 'attack', 'strength', 'defence', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking',
                'woodcutting','fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore',
                'agility', 'theiving', 'slayer', 'farming', 'runecraft', 'hunter', 'construction'
        ]

        split_resp = response.split('\n')

        for x in range(len(skills)):
            skill = split_resp[x].split(',')
            cur_skill = skills[x]
            rank = skill[0]
            level = skill[1]
            experience = skill[2]

            hiscore_array[cur_skill] = {}
            hiscore_array[cur_skill]['rank'] = rank
            hiscore_array[cur_skill]['level'] = level
            hiscore_array[cur_skill]['xp'] = experience

        return hiscore_array



