from flask import Blueprint, jsonify, render_template
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from nasdaq.models.nasdaq import MostActive, db
import pandas as pd

scraper_bp = Blueprint('scraper', __name__,
                       static_url_path="scraper")

header = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
url = "https://www.nasdaq.com/market-activity/most-active"


@scraper_bp.route("/")
def index():
    return render_template('scraper/index.html')


@scraper_bp.route('/most_active/<to_sql>')
@scraper_bp.route('/most_active/')
def scrap(to_sql=False):
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    most_active_url = "https://www.nasdaq.com/market-activity/most-active"
    driver.get(most_active_url)
    table = driver.find_element_by_css_selector(
        'div.most-active__data-container--share-volume').find_elements_by_css_selector("tr.most-active__row")
    most_active_list = []
    for row in table:
        #     print(row.text)
        most_active = dict()
        most_active['symbol'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[0].text
        most_active['name'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[1].text
        most_active['last'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[2].text
        most_active['change'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[3].text
        most_active['volume'] = row.find_elements_by_css_selector("td.most-active__cell.most-active__cell--heading")[4].text
        if to_sql:
            db.session.add(MostActive(most_active["symbol"], most_active["name"],
                                      float(most_active["last"][1:]), float(most_active["change"]),
                                      float(most_active["volume"].replace(",",""))))
            db.session.commit()
        most_active_list.append(most_active)

    df = pd.DataFrame(most_active_list)
    return render_template('scraper/index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
