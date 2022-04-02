from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
#Sign in doesn't exist?
signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("yes")
password_box = browser.find_element_by_id("password")
password_box.send_keys("no")
password_box.submit()

assert "yes" in browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "yes" in link_label

input("Press Enter to Stop")
browser.quit()

