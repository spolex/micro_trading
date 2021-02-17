from flask_injector import inject
from selenium.webdriver import Firefox
from flask import jsonify


# TODO extract to config file
header = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
url = "https://www.nasdaq.com/market-activity/most-active"


class MostActive(object):
    @inject
    def get(self, webdriver: Firefox):
        """
        This will return the most active stocks of the day from nasdaq
        :return:
        """
        webdriver.get(url)

        table = webdriver.find_element_by_css_selector('div.most-active__data-container--share-volume')\
                         .find_elements_by_css_selector("tr.most-active__row")

        if not table:
            return {"error": "Not found most active stock"}, 400

        most_active_list = []
        # TODO create parser abstract class and Nasdaq parser object from this class
        for row in table:
            most_active = dict()
            most_active['symbol'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[0].text
            most_active['name'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[1].text
            most_active['last'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[2].text
            most_active['change'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[3].text
            most_active['volume'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[4].text
            most_active_list.append(most_active)

        return jsonify(most_active_list), 200


class_instance = MostActive()
