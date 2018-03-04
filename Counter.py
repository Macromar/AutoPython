from selenium.webdriver.common.action_chains import ActionChains


def login(driver, user, password, url):
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("loginbutton").click()
    driver.find_element_by_id("email").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()


def count_friends(driver):
    footer = driver.find_element_by_id("pageFooter")
    bottom = False

    while not bottom:
        try:
            driver.find_element_by_id("pagelet_timeline_medley_movies")
            bottom = True
        except Exception:
            ActionChains(driver).move_to_element(footer).perform()

    friends_count = len(driver.find_elements_by_xpath("//*[@class='_698']"))
    return friends_count


def from_main_to_friends(driver, url):
    user_id = driver.find_element_by_xpath("//*[@id='userNav']/ul/li").get_attribute("data-nav-item-id")
    user_uri = url + user_id + "/friends"
    driver.get(user_uri)
    return
