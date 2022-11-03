import time

from appium import webdriver
from selenium.webdriver import remote

def get_emulator_driver():
    # adb shell dumpsys window | grep -E 'mCurrentFocus'    mac/linux
    # adb shell dumpsys window | find "mCurrentFocus"       windows
    url = "http://127.0.0.1:4734/wd/hub"
    cap = {
        "platformName":"Android",
        # "deviceName":"emulator-5554",
        "deviceName":"I7QKU8INLFEEMZTW",
        "appActivity": "com.android.vending.AssetBrowserActivity",
        "appPackage": "com.android.vending",
        "noReset": "true"
        # "browserName": "Play store"
        # "app": "C:/Users/91808/PycharmProjects/Python_Mobile_Testing/owl_eyes/app_location/Zomato.apk"
        # "fullReset" : "true"
    }
    driver = webdriver.Remote(url, cap)
    return driver

driver = get_emulator_driver()
# context = driver.contexts
# print(context)
try:
    time.sleep(5)
    driver.find_element_by_android_uiautomator('textContains("Search for apps")').click()
    driver.find_element_by_android_uiautomator('textContains("Search for apps")').send_keys("ola")
    driver.press_keycode(66)
    time.sleep(10)
finally:
    driver.quit()