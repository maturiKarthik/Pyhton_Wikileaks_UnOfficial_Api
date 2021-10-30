from Scrapper import ScrapManager, Const


# Fetch Leaks
class Leaks(object):

    def __init__(self):
        pass

    def get_leaks(self, topic):
        featured_json = []
        print Const.BASE_URL + topic
        scrap_manger = ScrapManager(Const.BASE_URL + topic)
        new_scrap_manager = ScrapManager(scrap_manger.find_elements("ul", {"class": Const.GRID})[0])
        for li in new_scrap_manager.find_elements("a", "no"):
            data = ScrapManager(li)
            link = str(li.get('href'))
            test = link.split(":")
            if len(test) == 1:
                link = Const.BASE_URL + link
            featured_json.append({
                'link': link,
                'img': str(Const.BASE_URL + data.find_elements('img', "no")[0].get('src')),
                'title': data.find_elements(Const.H2, {"class": Const.TITLE})[0].text,
                'intro': data.find_elements('p', "no")[0].text,
                'time_stamp': str(data.find_elements(Const.DIV, {"class": Const.DATE})[0].text)
            })
        return featured_json
