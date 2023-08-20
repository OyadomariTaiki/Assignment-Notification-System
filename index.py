from selenium import webdriver
import time
import datetime
from dateutil.relativedelta import relativedelta
import requests

dt_today = datetime.datetime.now() - relativedelta(months=1)
dt_tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

driver_path = "driver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://oh-o2.meiji.ac.jp/portal/index")
wait = driver.implicitly_wait(20)

driver.find_element_by_partial_link_text("ログインする").click()
wait

driver.find_element_by_name("ACCOUNTUID").send_keys("154R214067")
wait

driver.find_element_by_name("PASSWORD").send_keys("Oya114514")
wait

driver.find_element_by_name("SUBMIT").click()
wait

driver.find_element_by_id("navi-classweb").click()
wait

driver.find_element_by_link_text("英語リーディング１").click()
wait

# 英語リーディング１、課題期限の取得
englishreading1_homeworks_limit = driver.find_elements_by_css_selector(
    "#questionnaire .date")
# 英語リーディング１、課題期限の条件分岐
englishreading1_homework_limit_today_index = None
englishreading1_homework_limit_today_element = None
englishreading1_homework_limit_tomorrow_index = None
englishreading1_homework_limit_tomorrow_element = None

for i, englishreading1_homework_limit in enumerate(englishreading1_homeworks_limit):
    # 今日
    if dt_today.strftime('%Y/%m/%d') in englishreading1_homework_limit.text:
        englishreading1_homework_limit_today_index = i
        englishreading1_homework_limit_today_element = englishreading1_homework_limit.text
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in englishreading1_homework_limit.text:
        englishreading1_homework_limit_tomorrow_index = i
        englishreading1_homework_limit_tomorrow_element = englishreading1_homework_limit.text
# 英語リーディング１、課題タイトルの取得
englishreading1_homeworks_title = driver.find_elements_by_css_selector(
    "#questionnaire tr td:nth-child(2) span")
# 英語リーディング１、課題タイトルの条件分岐
englishreading1_homework_title_today = None
englishreading1_homework_title_tomorrow = None

for i, englishreading1_homework_title in enumerate(englishreading1_homeworks_title):
    # 今日
    if i == englishreading1_homework_limit_today_index:
        englishreading1_homework_title_today = englishreading1_homework_title.text
    # 明日
    if i == englishreading1_homework_limit_tomorrow_index:
        englishreading1_homework_title_tomorrow = englishreading1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("中国語１　ｂ").click()
wait

# 中国語１b、課題期限の取得
chinese1b_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 中国語１b、課題期限の条件分岐
chinese1b_homework_limit_today_index = None
chinese1b_homework_limit_today_element = None
chinese1b_homework_limit_tomorrow_index = None
chinese1b_homework_limit_tomorrow_element = None

for i, chinese1b_homework_limit_all in enumerate(chinese1b_homeworks_limit):
    chinese1b_homework_limit = chinese1b_homework_limit_all.text.split('～')[1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in chinese1b_homework_limit:
        chinese1b_homework_limit_today_index = i
        chinese1b_homework_limit_today_element = chinese1b_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in chinese1b_homework_limit:
        chinese1b_homework_limit_tomorrow_index = i
        chinese1b_homework_limit_tomorrow_element = chinese1b_homework_limit
# 中国語１b、課題タイトルの取得
chinese1b_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 中国語１b、課題タイトルの条件分岐
chinese1b_homework_title_today = None
chinese1b_homework_title_tomorrow = None

for i, chinese1b_homework_title in enumerate(chinese1b_homeworks_title):
    # 今日
    if i == chinese1b_homework_limit_today_index:
        chinese1b_homework_title_today = chinese1b_homework_title.text
    # 明日
    if i == chinese1b_homework_limit_tomorrow_index:
        chinese1b_homework_title_tomorrow = chinese1b_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("情報処理実習１").click()
wait

# 情報処理実習１、課題期限の取得
informationprocessingtraining1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 情報処理実習１、課題期限の条件分岐
informationprocessingtraining1_homework_limit_today_index = None
informationprocessingtraining1_homework_limit_today_element = None
informationprocessingtraining1_homework_limit_tomorrow_index = None
informationprocessingtraining1_homework_limit_tomorrow_element = None

for i, informationprocessingtraining1_homework_limit_all in enumerate(informationprocessingtraining1_homeworks_limit):
    informationprocessingtraining1_homework_limit = informationprocessingtraining1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in informationprocessingtraining1_homework_limit:
        informationprocessingtraining1_homework_limit_today_index = i
        informationprocessingtraining1_homework_limit_today_element = informationprocessingtraining1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in informationprocessingtraining1_homework_limit:
        informationprocessingtraining1_homework_limit_tomorrow_index = i
        informationprocessingtraining1_homework_limit_tomorrow_element = informationprocessingtraining1_homework_limit
# 情報処理実習１、課題タイトルの取得
informationprocessingtraining1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 情報処理実習１、課題タイトルの条件分岐
informationprocessingtraining1_homework_title_today = None
informationprocessingtraining1_homework_title_tomorrow = None

for i, informationprocessingtraining1_homework_title in enumerate(informationprocessingtraining1_homeworks_title):
    # 今日
    if i == informationprocessingtraining1_homework_limit_today_index:
        informationprocessingtraining1_homework_title_today = informationprocessingtraining1_homework_title.text
    # 明日
    if i == informationprocessingtraining1_homework_limit_tomorrow_index:
        informationprocessingtraining1_homework_title_tomorrow = informationprocessingtraining1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("機械情報工学").click()
wait

# 機械情報工学、課題期限の取得
mechanicalinformationengineering_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 機械情報工学、課題期限の条件分岐
mechanicalinformationengineering_homework_limit_today_index = None
mechanicalinformationengineering_homework_limit_today_element = None
mechanicalinformationengineering_homework_limit_tomorrow_index = None
mechanicalinformationengineering_homework_limit_tomorrow_element = None

for i, mechanicalinformationengineering_homework_limit_all in enumerate(mechanicalinformationengineering_homeworks_limit):
    mechanicalinformationengineering_homework_limit = mechanicalinformationengineering_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in mechanicalinformationengineering_homework_limit:
        mechanicalinformationengineering_homework_limit_today_index = i
        mechanicalinformationengineering_homework_limit_today_element = mechanicalinformationengineering_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in mechanicalinformationengineering_homework_limit:
        mechanicalinformationengineering_homework_limit_tomorrow_index = i
        mechanicalinformationengineering_homework_limit_tomorrow_element = mechanicalinformationengineering_homework_limit
# 機械情報工学、課題タイトルの取得
mechanicalinformationengineering_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 機械情報工学、課題タイトルの条件分岐
mechanicalinformationengineering_homework_title_today = None
mechanicalinformationengineering_homework_title_tomorrow = None

for i, mechanicalinformationengineering_homework_title in enumerate(mechanicalinformationengineering_homeworks_title):
    # 今日
    if i == mechanicalinformationengineering_homework_limit_today_index:
        mechanicalinformationengineering_homework_title_today = mechanicalinformationengineering_homework_title.text
    # 明日
    if i == mechanicalinformationengineering_homework_limit_tomorrow_index:
        mechanicalinformationengineering_homework_title_tomorrow = mechanicalinformationengineering_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("工業力学１・演習").click()
wait

# 工業力学１・演習、課題期限の取得
industrialmechanics1exercise_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 工業力学１・演習、課題期限の条件分岐
industrialmechanics1exercise_homework_limit_today_index = None
industrialmechanics1exercise_homework_limit_today_element = None
industrialmechanics1exercise_homework_limit_tomorrow_index = None
industrialmechanics1exercise_homework_limit_tomorrow_element = None

for i, industrialmechanics1exercise_homework_limit_all in enumerate(industrialmechanics1exercise_homeworks_limit):
    industrialmechanics1exercise_homework_limit = industrialmechanics1exercise_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in industrialmechanics1exercise_homework_limit:
        industrialmechanics1exercise_homework_limit_today_index = i
        industrialmechanics1exercise_homework_limit_today_element = industrialmechanics1exercise_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in industrialmechanics1exercise_homework_limit:
        industrialmechanics1exercise_homework_limit_tomorrow_index = i
        industrialmechanics1exercise_homework_limit_tomorrow_element = industrialmechanics1exercise_homework_limit
# 工業力学１・演習、課題タイトルの取得
industrialmechanics1exercise_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 工業力学１・演習、課題タイトルの条件分岐
industrialmechanics1exercise_homework_title_today = None
industrialmechanics1exercise_homework_title_tomorrow = None

for i, industrialmechanics1exercise_homework_title in enumerate(industrialmechanics1exercise_homeworks_title):
    # 今日
    if i == industrialmechanics1exercise_homework_limit_today_index:
        industrialmechanics1exercise_homework_title_today = industrialmechanics1exercise_homework_title.text
    # 明日
    if i == industrialmechanics1exercise_homework_limit_tomorrow_index:
        industrialmechanics1exercise_homework_title_tomorrow = industrialmechanics1exercise_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("基礎力学１").click()
wait

# 基礎力学１、課題期限の取得
basicmechanics1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 基礎力学１、課題期限の条件分岐
basicmechanics1_homework_limit_today_index = None
basicmechanics1_homework_limit_today_element = None
basicmechanics1_homework_limit_tomorrow_index = None
basicmechanics1_homework_limit_tomorrow_element = None

for i, basicmechanics1_homework_limit_all in enumerate(basicmechanics1_homeworks_limit):
    basicmechanics1_homework_limit = basicmechanics1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in basicmechanics1_homework_limit:
        basicmechanics1_homework_limit_today_index = i
        basicmechanics1_homework_limit_today_element = basicmechanics1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in basicmechanics1_homework_limit:
        basicmechanics1_homework_limit_tomorrow_index = i
        basicmechanics1_homework_limit_tomorrow_element = basicmechanics1_homework_limit
# 基礎力学１、課題タイトルの取得
basicmechanics1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 基礎力学１、課題タイトルの条件分岐
basicmechanics1_homework_title_today = None
basicmechanics1_homework_title_tomorrow = None

for i, basicmechanics1_homework_title in enumerate(basicmechanics1_homeworks_title):
    # 今日
    if i == basicmechanics1_homework_limit_today_index:
        basicmechanics1_homework_title_today = basicmechanics1_homework_title.text
    # 明日
    if i == basicmechanics1_homework_limit_tomorrow_index:
        basicmechanics1_homework_title_tomorrow = basicmechanics1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("健康・スポーツ学１").click()
wait

# 健康・スポーツ学１、課題期限の取得
healthandsportsstudies1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 健康・スポーツ学１、課題期限の条件分岐
healthandsportsstudies1_homework_limit_today_index = None
healthandsportsstudies1_homework_limit_today_element = None
healthandsportsstudies1_homework_limit_tomorrow_index = None
healthandsportsstudies1_homework_limit_tomorrow_element = None

for i, healthandsportsstudies1_homework_limit_all in enumerate(healthandsportsstudies1_homeworks_limit):
    healthandsportsstudies1_homework_limit = healthandsportsstudies1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in healthandsportsstudies1_homework_limit:
        healthandsportsstudies1_homework_limit_today_index = i
        healthandsportsstudies1_homework_limit_today_element = healthandsportsstudies1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in healthandsportsstudies1_homework_limit:
        healthandsportsstudies1_homework_limit_tomorrow_index = i
        healthandsportsstudies1_homework_limit_tomorrow_element = healthandsportsstudies1_homework_limit
# 健康・スポーツ学１、課題タイトルの取得
healthandsportsstudies1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 健康・スポーツ学１、課題タイトルの条件分岐
healthandsportsstudies1_homework_title_today = None
healthandsportsstudies1_homework_title_tomorrow = None

for i, healthandsportsstudies1_homework_title in enumerate(healthandsportsstudies1_homeworks_title):
    # 今日
    if i == healthandsportsstudies1_homework_limit_today_index:
        healthandsportsstudies1_homework_title_today = healthandsportsstudies1_homework_title.text
    # 明日
    if i == healthandsportsstudies1_homework_limit_tomorrow_index:
        healthandsportsstudies1_homework_title_tomorrow = healthandsportsstudies1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("中国語１　ａ").click()
wait

# 中国語１　ａ、課題期限の取得
chinese1a_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 中国語１　ａ、課題期限の条件分岐
chinese1a_homework_limit_today_index = None
chinese1a_homework_limit_today_element = None
chinese1a_homework_limit_tomorrow_index = None
chinese1a_homework_limit_tomorrow_element = None

for i, chinese1a_homework_limit_all in enumerate(chinese1a_homeworks_limit):
    chinese1a_homework_limit = chinese1a_homework_limit_all.text.split('～')[1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in chinese1a_homework_limit:
        chinese1a_homework_limit_today_index = i
        chinese1a_homework_limit_today_element = chinese1a_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in chinese1a_homework_limit:
        chinese1a_homework_limit_tomorrow_index = i
        chinese1a_homework_limit_tomorrow_element = chinese1a_homework_limit
# 中国語１　ａ、課題タイトルの取得
chinese1a_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 中国語１　ａ、課題タイトルの条件分岐
chinese1a_homework_title_today = None
chinese1a_homework_title_tomorrow = None

for i, chinese1a_homework_title in enumerate(chinese1a_homeworks_title):
    # 今日
    if i == chinese1a_homework_limit_today_index:
        chinese1a_homework_title_today = chinese1a_homework_title.text
    # 明日
    if i == chinese1a_homework_limit_tomorrow_index:
        chinese1a_homework_title_tomorrow = chinese1a_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("確率・統計").click()
wait

# 確率・統計、課題期限の取得
probabilitystatistics_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 確率・統計、課題期限の条件分岐
probabilitystatistics_homework_limit_today_index = None
probabilitystatistics_homework_limit_today_element = None
probabilitystatistics_homework_limit_tomorrow_index = None
probabilitystatistics_homework_limit_tomorrow_element = None

for i, probabilitystatistics_homework_limit_all in enumerate(probabilitystatistics_homeworks_limit):
    probabilitystatistics_homework_limit = probabilitystatistics_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in probabilitystatistics_homework_limit:
        probabilitystatistics_homework_limit_today_index = i
        probabilitystatistics_homework_limit_today_element = probabilitystatistics_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in probabilitystatistics_homework_limit:
        probabilitystatistics_homework_limit_tomorrow_index = i
        probabilitystatistics_homework_limit_tomorrow_element = probabilitystatistics_homework_limit
# 確率・統計、課題タイトルの取得
probabilitystatistics_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 確率・統計、課題タイトルの条件分岐
probabilitystatistics_homework_title_today = None
probabilitystatistics_homework_title_tomorrow = None

for i, probabilitystatistics_homework_title in enumerate(probabilitystatistics_homeworks_title):
    # 今日
    if i == probabilitystatistics_homework_limit_today_index:
        probabilitystatistics_homework_title_today = probabilitystatistics_homework_title.text
    # 明日
    if i == probabilitystatistics_homework_limit_tomorrow_index:
        probabilitystatistics_homework_title_tomorrow = probabilitystatistics_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("基礎化学１").click()
wait

# 基礎化学１、課題期限の取得
basicchemistry1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 基礎化学１、課題期限の条件分岐
basicchemistry1_homework_limit_today_index = None
basicchemistry1_homework_limit_today_element = None
basicchemistry1_homework_limit_tomorrow_index = None
basicchemistry1_homework_limit_tomorrow_element = None

for i, basicchemistry1_homework_limit_all in enumerate(basicchemistry1_homeworks_limit):
    basicchemistry1_homework_limit = basicchemistry1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in basicchemistry1_homework_limit:
        basicchemistry1_homework_limit_today_index = i
        basicchemistry1_homework_limit_today_element = basicchemistry1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in basicchemistry1_homework_limit:
        basicchemistry1_homework_limit_tomorrow_index = i
        basicchemistry1_homework_limit_tomorrow_element = basicchemistry1_homework_limit
# 基礎化学１、課題タイトルの取得
basicchemistry1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 基礎化学１、課題タイトルの条件分岐
basicchemistry1_homework_title_today = None
basicchemistry1_homework_title_tomorrow = None

for i, basicchemistry1_homework_title in enumerate(basicchemistry1_homeworks_title):
    # 今日
    if i == basicchemistry1_homework_limit_today_index:
        basicchemistry1_homework_title_today = basicchemistry1_homework_title.text
    # 明日
    if i == basicchemistry1_homework_limit_tomorrow_index:
        basicchemistry1_homework_title_tomorrow = basicchemistry1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("基礎微分積分１").click()
wait

# 基礎微分積分１、課題期限の取得
fundamentalcalculus1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 基礎微分積分１、課題期限の条件分岐
fundamentalcalculus1_homework_limit_today_index = None
fundamentalcalculus1_homework_limit_today_element = None
fundamentalcalculus1_homework_limit_tomorrow_index = None
fundamentalcalculus1_homework_limit_tomorrow_element = None

for i, fundamentalcalculus1_homework_limit_all in enumerate(fundamentalcalculus1_homeworks_limit):
    fundamentalcalculus1_homework_limit = fundamentalcalculus1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in fundamentalcalculus1_homework_limit:
        fundamentalcalculus1_homework_limit_today_index = i
        fundamentalcalculus1_homework_limit_today_element = fundamentalcalculus1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in fundamentalcalculus1_homework_limit:
        fundamentalcalculus1_homework_limit_tomorrow_index = i
        fundamentalcalculus1_homework_limit_tomorrow_element = fundamentalcalculus1_homework_limit
# 基礎微分積分１、課題タイトルの取得
fundamentalcalculus1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 基礎微分積分１、課題タイトルの条件分岐
fundamentalcalculus1_homework_title_today = None
fundamentalcalculus1_homework_title_tomorrow = None

for i, fundamentalcalculus1_homework_title in enumerate(fundamentalcalculus1_homeworks_title):
    # 今日
    if i == fundamentalcalculus1_homework_limit_today_index:
        fundamentalcalculus1_homework_title_today = fundamentalcalculus1_homework_title.text
    # 明日
    if i == fundamentalcalculus1_homework_limit_tomorrow_index:
        fundamentalcalculus1_homework_title_tomorrow = fundamentalcalculus1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("基礎線形代数１").click()
wait

# 基礎線形代数１、課題期限の取得
basiclinearalgebra1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 基礎線形代数１、課題期限の条件分岐
basiclinearalgebra1_homework_limit_today_index = None
basiclinearalgebra1_homework_limit_today_element = None
basiclinearalgebra1_homework_limit_tomorrow_index = None
basiclinearalgebra1_homework_limit_tomorrow_element = None

for i, basiclinearalgebra1_homework_limit_all in enumerate(basiclinearalgebra1_homeworks_limit):
    basiclinearalgebra1_homework_limit = basiclinearalgebra1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in basiclinearalgebra1_homework_limit:
        basiclinearalgebra1_homework_limit_today_index = i
        basiclinearalgebra1_homework_limit_today_element = basiclinearalgebra1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in basiclinearalgebra1_homework_limit:
        basiclinearalgebra1_homework_limit_tomorrow_index = i
        basiclinearalgebra1_homework_limit_tomorrow_element = basiclinearalgebra1_homework_limit
# 基礎線形代数１、課題タイトルの取得
basiclinearalgebra1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 基礎線形代数１、課題タイトルの条件分岐
basiclinearalgebra1_homework_title_today = None
basiclinearalgebra1_homework_title_tomorrow = None

for i, basiclinearalgebra1_homework_title in enumerate(basiclinearalgebra1_homeworks_title):
    # 今日
    if i == basiclinearalgebra1_homework_limit_today_index:
        basiclinearalgebra1_homework_title_today = basiclinearalgebra1_homework_title.text
    # 明日
    if i == basiclinearalgebra1_homework_limit_tomorrow_index:
        basiclinearalgebra1_homework_title_tomorrow = basiclinearalgebra1_homework_title.text

driver.find_element_by_link_text("クラスウェブ").click()
wait

driver.find_element_by_link_text("英語コミュニケーション１").click()
wait

# 英語コミュニケーション１、課題期限の取得
englishcommunication1_homeworks_limit = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(2)")
# 英語コミュニケーション１、課題期限の条件分岐
englishcommunication1_homework_limit_today_index = None
englishcommunication1_homework_limit_today_element = None
englishcommunication1_homework_limit_tomorrow_index = None
englishcommunication1_homework_limit_tomorrow_element = None

for i, englishcommunication1_homework_limit_all in enumerate(englishcommunication1_homeworks_limit):
    englishcommunication1_homework_limit = englishcommunication1_homework_limit_all.text.split('～')[
        1]
    # 今日
    if dt_today.strftime('%Y/%m/%d') in englishcommunication1_homework_limit:
        englishcommunication1_homework_limit_today_index = i
        englishcommunication1_homework_limit_today_element = englishcommunication1_homework_limit
    # 明日
    if dt_tomorrow.strftime('%Y/%m/%d') in englishcommunication1_homework_limit:
        englishcommunication1_homework_limit_tomorrow_index = i
        englishcommunication1_homework_limit_tomorrow_element = englishcommunication1_homework_limit
# 英語コミュニケーション１、課題タイトルの取得
englishcommunication1_homeworks_title = driver.find_elements_by_css_selector(
    "#report tr td:nth-child(1) span")
# 英語コミュニケーション１、課題タイトルの条件分岐
englishcommunication1_homework_title_today = None
englishcommunication1_homework_title_tomorrow = None

for i, englishcommunication1_homework_title in enumerate(englishcommunication1_homeworks_title):
    # 今日
    if i == englishcommunication1_homework_limit_today_index:
        englishcommunication1_homework_title_today = englishcommunication1_homework_title.text
    # 明日
    if i == englishcommunication1_homework_limit_tomorrow_index:
        englishcommunication1_homework_title_tomorrow = englishcommunication1_homework_title.text

driver.quit()
'''
print(englishreading1_homework_title_today)
print(englishreading1_homework_limit_today_element)
print(englishreading1_homework_title_tomorrow)
print(englishreading1_homework_limit_tomorrow_element)

print(chinese1b_homework_title_today)
print(chinese1b_homework_limit_today_element)
print(chinese1b_homework_title_tomorrow)
print(chinese1b_homework_limit_tomorrow_element)

print(informationprocessingtraining1_homework_title_today)
print(informationprocessingtraining1_homework_limit_today_element)
print(informationprocessingtraining1_homework_title_tomorrow)
print(informationprocessingtraining1_homework_limit_tomorrow_element)

print(mechanicalinformationengineering_homework_title_today)
print(mechanicalinformationengineering_homework_limit_today_element)
print(mechanicalinformationengineering_homework_title_tomorrow)
print(mechanicalinformationengineering_homework_limit_tomorrow_element)

print(industrialmechanics1exercise_homework_title_today)
print(industrialmechanics1exercise_homework_limit_today_element)
print(industrialmechanics1exercise_homework_title_tomorrow)
print(industrialmechanics1exercise_homework_limit_tomorrow_element)

print(basicmechanics1_homework_title_today)
print(basicmechanics1_homework_limit_today_element)
print(basicmechanics1_homework_title_tomorrow)
print(basicmechanics1_homework_limit_tomorrow_element)

print(healthandsportsstudies1_homework_title_today)
print(healthandsportsstudies1_homework_limit_today_element)
print(healthandsportsstudies1_homework_title_tomorrow)
print(healthandsportsstudies1_homework_limit_tomorrow_element)

print(chinese1a_homework_title_today)
print(chinese1a_homework_limit_today_element)
print(chinese1a_homework_title_tomorrow)
print(chinese1a_homework_limit_tomorrow_element)

print(probabilitystatistics_homework_title_today)
print(probabilitystatistics_homework_limit_today_element)
print(probabilitystatistics_homework_title_tomorrow)
print(probabilitystatistics_homework_limit_tomorrow_element)

print(basicchemistry1_homework_title_today)
print(basicchemistry1_homework_limit_today_element)
print(basicchemistry1_homework_title_tomorrow)
print(basicchemistry1_homework_limit_tomorrow_element)

print(fundamentalcalculus1_homework_title_today)
print(fundamentalcalculus1_homework_limit_today_element)
print(fundamentalcalculus1_homework_title_tomorrow)
print(fundamentalcalculus1_homework_limit_tomorrow_element)

print(basiclinearalgebra1_homework_title_today)
print(basiclinearalgebra1_homework_limit_today_element)
print(basiclinearalgebra1_homework_title_tomorrow)
print(basiclinearalgebra1_homework_limit_tomorrow_element)

print(englishcommunication1_homework_title_today)
print(englishcommunication1_homework_limit_today_element)
print(englishcommunication1_homework_title_tomorrow)
print(englishcommunication1_homework_limit_tomorrow_element)
'''
# LINEに送信
send_contents_array_today = []
send_contents_array_tomorrow = []
# 英語リーディング１
if englishreading1_homework_title_today != None:
    englishreading1_homework_today = '英語リーディング１' + \
        englishreading1_homework_title_today + \
        englishreading1_homework_limit_today_element
    send_contents_array_today.append(englishreading1_homework_today)
if englishreading1_homework_title_tomorrow != None:
    englishreading1_homework_tomorrow = '英語リーディング１' + englishreading1_homework_title_tomorrow + \
        englishreading1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(englishreading1_homework_tomorrow)
# 中国語１b
if chinese1b_homework_title_today != None:
    chinese1b_homework_today = '中国語１b' + \
        chinese1b_homework_title_today + \
        chinese1b_homework_limit_today_element
    send_contents_array_today.append(chinese1b_homework_today)
if chinese1b_homework_title_tomorrow != None:
    chinese1b_homework_tomorrow = '中国語１b' + chinese1b_homework_title_tomorrow + \
        chinese1b_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(chinese1b_homework_tomorrow)
# 情報処理実習１
if informationprocessingtraining1_homework_title_today != None:
    informationprocessingtraining1_homework_today = '情報処理実習１' + \
        informationprocessingtraining1_homework_title_today + \
        informationprocessingtraining1_homework_limit_today_element
    send_contents_array_today.append(
        informationprocessingtraining1_homework_today)
if informationprocessingtraining1_homework_title_tomorrow != None:
    informationprocessingtraining1_homework_tomorrow = '情報処理実習１' + informationprocessingtraining1_homework_title_tomorrow + \
        informationprocessingtraining1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        informationprocessingtraining1_homework_tomorrow)
# 機械情報工学
if mechanicalinformationengineering_homework_title_today != None:
    mechanicalinformationengineering_homework_today = '機械情報工学' + \
        mechanicalinformationengineering_homework_title_today + \
        mechanicalinformationengineering_homework_limit_today_element
    send_contents_array_today.append(
        mechanicalinformationengineering_homework_today)
if mechanicalinformationengineering_homework_title_tomorrow != None:
    mechanicalinformationengineering_homework_tomorrow = '機械情報工学' + mechanicalinformationengineering_homework_title_tomorrow + \
        mechanicalinformationengineering_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        mechanicalinformationengineering_homework_tomorrow)
# 工業力学１・演習
if industrialmechanics1exercise_homework_title_today != None:
    industrialmechanics1exercise_homework_today = '工業力学１・演習' + \
        industrialmechanics1exercise_homework_title_today + \
        industrialmechanics1exercise_homework_limit_today_element
    send_contents_array_today.append(
        industrialmechanics1exercise_homework_today)
if industrialmechanics1exercise_homework_title_tomorrow != None:
    industrialmechanics1exercise_homework_tomorrow = '工業力学１・演習' + industrialmechanics1exercise_homework_title_tomorrow + \
        industrialmechanics1exercise_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        industrialmechanics1exercise_homework_tomorrow)
# 基礎力学１
if basicmechanics1_homework_title_today != None:
    basicmechanics1_homework_today = '基礎力学１' + \
        basicmechanics1_homework_title_today + \
        basicmechanics1_homework_limit_today_element
    send_contents_array_today.append(basicmechanics1_homework_today)
if basicmechanics1_homework_title_tomorrow != None:
    basicmechanics1_homework_tomorrow = '基礎力学１' + basicmechanics1_homework_title_tomorrow + \
        basicmechanics1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(basicmechanics1_homework_tomorrow)
# 健康スポーツ学１
if healthandsportsstudies1_homework_title_today != None:
    healthandsportsstudies1_homework_today = '健康スポーツ学１' + \
        healthandsportsstudies1_homework_title_today + \
        healthandsportsstudies1_homework_limit_today_element
    send_contents_array_today.append(healthandsportsstudies1_homework_today)
if healthandsportsstudies1_homework_title_tomorrow != None:
    healthandsportsstudies1_homework_tomorrow = '健康スポーツ学１' + healthandsportsstudies1_homework_title_tomorrow + \
        healthandsportsstudies1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        healthandsportsstudies1_homework_tomorrow)
# 中国語１a
if chinese1a_homework_title_today != None:
    chinese1a_homework_today = '中国語１a' + \
        chinese1a_homework_title_today + \
        chinese1a_homework_limit_today_element
    send_contents_array_today.append(chinese1a_homework_today)
if chinese1a_homework_title_tomorrow != None:
    chinese1a_homework_tomorrow = '中国語１a' + chinese1a_homework_title_tomorrow + \
        chinese1a_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(chinese1a_homework_tomorrow)
# 確率統計
if probabilitystatistics_homework_title_today != None:
    probabilitystatistics_homework_today = '確率統計' + \
        probabilitystatistics_homework_title_today + \
        probabilitystatistics_homework_limit_today_element
    send_contents_array_today.append(probabilitystatistics_homework_today)
if probabilitystatistics_homework_title_tomorrow != None:
    probabilitystatistics_homework_tomorrow = '確率統計' + probabilitystatistics_homework_title_tomorrow + \
        probabilitystatistics_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        probabilitystatistics_homework_tomorrow)
# 基礎化学１
if basicchemistry1_homework_title_today != None:
    basicchemistry1_homework_today = '基礎化学１' + \
        basicchemistry1_homework_title_today + \
        basicchemistry1_homework_limit_today_element
    send_contents_array_today.append(basicchemistry1_homework_today)
if basicchemistry1_homework_title_tomorrow != None:
    basicchemistry1_homework_tomorrow = '基礎化学１' + basicchemistry1_homework_title_tomorrow + \
        basicchemistry1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(basicchemistry1_homework_tomorrow)
# 基礎微分積分１
if fundamentalcalculus1_homework_title_today != None:
    fundamentalcalculus1_homework_today = '基礎微分積分１' + \
        fundamentalcalculus1_homework_title_today + \
        fundamentalcalculus1_homework_limit_today_element
    send_contents_array_today.append(fundamentalcalculus1_homework_today)
if fundamentalcalculus1_homework_title_tomorrow != None:
    fundamentalcalculus1_homework_tomorrow = '基礎微分積分１' + fundamentalcalculus1_homework_title_tomorrow + \
        fundamentalcalculus1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(fundamentalcalculus1_homework_tomorrow)
# 基礎線形代数１
if basiclinearalgebra1_homework_title_today != None:
    basiclinearalgebra1_homework_today = '基礎線形代数１' + \
        basiclinearalgebra1_homework_title_today + \
        basiclinearalgebra1_homework_limit_today_element
    send_contents_array_today.append(basiclinearalgebra1_homework_today)
if basiclinearalgebra1_homework_title_tomorrow != None:
    basiclinearalgebra1_homework_tomorrow = '基礎線形代数１' + basiclinearalgebra1_homework_title_tomorrow + \
        basiclinearalgebra1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(basiclinearalgebra1_homework_tomorrow)
# 英語コミュニケーション１
if englishcommunication1_homework_title_today != None:
    englishcommunication1_homework_today = '英語コミュニケーション１' + \
        englishcommunication1_homework_title_today + \
        englishcommunication1_homework_limit_today_element
    send_contents_array_today.append(englishcommunication1_homework_today)
if englishcommunication1_homework_title_tomorrow != None:
    englishcommunication1_homework_tomorrow = '英語コミュニケーション１' + englishcommunication1_homework_title_tomorrow + \
        englishcommunication1_homework_limit_tomorrow_element
    send_contents_array_tomorrow.append(
        englishcommunication1_homework_tomorrow)

# LINEへ送信


def main():
    url = 'https://notify-api.line.me/api/notify'
    access_token = 'CbjSqVlRJ3lLPG5qfer0VLEx7QEGIfevd5w6mAGfUC1'
    headers = {'Authorization': f'Bearer {access_token}'}
    message = '今日' + '\n' + \
        '\n'.join(send_contents_array_today) + '\n' + '明日' + \
        '\n'.join(send_contents_array_tomorrow)
    params = {'message': message}
    line_notify = requests.post(url, headers=headers, params=params)


main()
