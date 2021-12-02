import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

#@pytest.mark.new_user
#class TestUserAddToBasketFromProductPage():
#    @pytest.fixture(autouse=True)
 #   def setup(self, browser):
 #       linka = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
  #      email = str(time.time()) + "@fakemail.org"
  #      password = "426244123ABCdefhg"
   #     product_page = ProductPage(browser, linka)
   #     product_page.open()
   #     product_page.go_to_login_page()
    #    page = LoginPage(browser, browser.current_url)
    #    page.open()
    #    page.register_new_user(email, password)
    #    page.should_be_authorized_user()

    #@pytest.mark.need_review
   # def test_user_can_add_product_to_basket(self, browser):
     #   linka = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
     #   page = ProductPage(browser, linka)
      #  page.open()
       # page.add_to_cart()
       # page.solve_quiz_and_get_code()
       # page.product_name_is_correct()
      #  page.should_be_correct_adding_product_price()

   # def test_user_cant_see_success_message(self, browser):
       # linka = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        #page = ProductPage(browser, linka)
       # page.open()
       # page.should_not_be_success_message()


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#@pytest.mark.need_review
#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.solve_quiz_and_get_code()
#    page.product_name_is_correct()
#    page.should_be_correct_adding_product_price()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    linkk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, linkk)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    linkk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, linkk)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    linkk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, linkk)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    #time.sleep(1)
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_null_text()




