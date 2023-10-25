from selenium import webdriver
from pages_.logInPage import LogInPage
from pages_.cartPage import CartPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.get("https://www.amazon.com/ref=nav_logo")
#
# logInPageObj = LogInPage(driver)
# logInPageObj.fill_user_name_field("sast04709@gmail.com")
# logInPageObj.click_to_continue_Button()
# logInPageObj.fill_password_fill_element("AmazonAst25")
# logInPageObj.click_to_sign_in_button()

cartPageObj = CartPage(driver)
cartPageObj.clck_to_cart_button()
cartPageObj.delete_first_item_from_cart()

driver.close()

