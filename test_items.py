import time
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_lang(browser):
    browser.get(url)
    button = browser.find_elements_by_class_name(
        "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button) > 0, "Button is not defined"
    time.sleep(30)
