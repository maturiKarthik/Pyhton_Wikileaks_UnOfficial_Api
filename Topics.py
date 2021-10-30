from Scrapper import ScrapManager, Const


# Fetch topics
class Topics(object):
    topic = []

    def __init__(self):
        pass

    def get_topics(self):
        scrap_manager = ScrapManager(Const.BASE_URL)
        topics = scrap_manager.find_elements(Const.UL, {"class": Const.NAV})[0]
        topics_list = ScrapManager(topics)
        for link in topics_list.find_elements(Const.A, "no"):
            Topics.topic.append({
                str(link.text): str(link.get(Const.HREF))
            })
        return Topics.topic
