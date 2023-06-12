from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from dict_all_size_guide import dict_sizeguide
from setting import tl_price
from product_links import dior_perfume 
import selenium
# from selenium import webdriver
from woocommerce import API
from bs4 import BeautifulSoup
import json
import sqlite3
import csv
import logging
import requests
import sys   
from urllib.request import Request, urlopen
import time
# import path
import logging
import base64
# from base64 import urlsafe_b64encode
import shutil
# from translate import Translator
# b64encode
proxy_host = 'localhost:55579'
PROXY_USERNAME = "x7992"
PROXY_PASSWORD = "tohid123456789"
import logging
requests.timeout = 40

#driver manager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
# options = Options()
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location='/usr/bin/google-chrome-beta'
chrome_options.add_experimental_option("detach", True)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# import PIL
# import numpy
# from PIL import Image
# from PIL import Image
import glob
import glob, os

















# from selenium.webdriver.common.keys import Keys
# import selenium.webdriver.common.keys
# from selenium.webdriver.common.action_chains import ActionChains
# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..')))
# from dict_all_size_guide import dict_sizeguide
# from setting import tl_price
# # from product_links import ipekyol
# # from product_links import ecco_ayyakkabi
# # from product_links import aldo
# # from product_links import massimodutti

# from product_links import Koton




# import selenium
# # from selenium import webdriver
# from woocommerce import API
# from bs4 import BeautifulSoup
# import json
# import sqlite3
# import csv
# import logging
# import requests
# import sys   
# from urllib.request import Request, urlopen
# import time
# import logging
# import base64
# import shutil
# proxy_host = 'localhost:55579'
# PROXY_USERNAME = "x7992"
# PROXY_PASSWORD = "tohid123456789"
# import logging
# # import platform
# from selenium import webdriver
# # if platform.system() == 'Windows':
# #     PHANTOMJS_PATH = './phantomjs.exe'
# #     CHROME_PATH = '../chromedriver.exe'
# #     FIREFOX_PATH = '../geckodriver.exe'
# # else:
# #     PHANTOMJS_PATH = './phantomjs'
# #     CHROME_PATH = './chromedriver'
# #     FIREFOX_PATH = './firefox'

# requests.timeout = 40
# # chrome_options = webdriver.ChromeOptions()



# # chrome_options.add_extension('../cyberghost.crx')



# # from selenium.webdriver.firefox.options import Options
# # options = Options()


# # #-------------------------------------------------------------------#

# # firefox_profile = webdriver.FirefoxProfile()
# # firefox_profile.set_preference('permissions.default.image', 2)
# # firefox_options = webdriver.FirefoxOptions()
# # firefox_profile.update_preferences()


# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options


# options = Options()
# options.binary_location='C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
# options.add_extension('../cyberghost.crx')




# # #-------------------------------------------------------------------#

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# import PIL
# import numpy
# from PIL import Image
# from PIL import Image
# import glob
# import glob, os






wcapi = API(
	url="https://shahremun.com",
	consumer_key="",
	consumer_secret="",
	# consumer_key="",
	# consumer_secret="",
    version="wc/v3",
    timeout= 160
)


conn_costdb = sqlite3.connect('../shipping_cost.db')
c_cost = conn_costdb.cursor()
def create_tables_cost():
	c_cost.execute('''CREATE TABLE IF NOT EXISTS categori_sku
			 (id integer primary key, name text , slug text,id_categori integer ,cost integer)''')
# create_tables_cost()



conn_dictdb = sqlite3.connect('trendyol_dict.db')
# conn_dictdb = sqlite3.connect('../turk.db')
# conn.text_factory = str
c_dict = conn_dictdb.cursor()
def create_tables_dict():
	c_dict.execute('''CREATE TABLE IF NOT EXISTS color
			 (id integer primary key, tr text UNIQUE, fa text ,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS material
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS care
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')
	c_dict.execute('''CREATE TABLE IF NOT EXISTS description
			 (id integer primary key, tr text UNIQUE, fa text,brandname_dict text)''')

create_tables_dict()




conn = sqlite3.connect('stock.db')
c = conn.cursor()	
def create_tables():
	c.execute('''CREATE TABLE IF NOT EXISTS urls
			 (id integer primary key, url text UNIQUE, barcode text,title text, categorie_id int,gharanti text,done int,tag_name text,tag_slug text,tag_id int)''')
	c.execute('''CREATE TABLE IF NOT EXISTS prev_stock
			 (id integer primary key, barcode text UNIQUE, price int, wp_id int, qty int, in_stock int)''')
	c.execute('''CREATE TABLE IF NOT EXISTS pre_process
			 (id integer primary key, barcode text UNIQUE, size text, price int,sales_price int, done int, title text, url text,image_list text, product_color text, country text,description text,gharanti text,supplier text,categorie_id text,image_name text,image_alt text,slug text,tag_name text,tag_slug text,tag_id int)''')
	c.execute('''CREATE TABLE IF NOT EXISTS product_sku
			 (id integer primary key, wp_sku text UNIQUE, wp_id integer, variation_id integer)''')




def gen_url(start_link,page_num):
	offset_i = start_link.find("offset=")
	page_i = start_link.find("&page-size")
	url = start_link[:offset_i] + "offset=" + str(page_num) + start_link[page_i:]
	print(url)
	return url


# def get_color(url):
# 	color_start = url.find("?colorId") + 9
# 	have_style = url.find("&style")
# 	if have_style != -1:
# 		color = url[color_start:have_style]
# 	else:
# 		color = url[color_start:]

# 	return color



def color_no_trans(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'details-section')
		# print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//*[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		if detailattributestitle_text == "Ürün Özellikleri":
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				if span1=="Renk":
					span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
					print("span2  ==>>",span2)

					
					# Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					Dimensions_text_ =span2 
					
					description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None






def color_description(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'details-section')
		# print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//*[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		if detailattributestitle_text == "Ürün Özellikleri":
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				if span1=="Renk":
					span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
					print("span2  ==>>",span2)

					c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						strong_li_fa = span1
						c_dict.execute('INSERT OR IGNORE INTO color VALUES (?,?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol",""))
						
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						strong_li_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",strong_li_fa)

					c_dict.execute('SELECT fa FROM color where tr = ?',(span2,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						product_color_fa = span2
						c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						product_color_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",product_color_fa)

					# Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					Dimensions_text_ =product_color_fa 
					
					description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None





def material_description(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'details-section')
		# print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//*[contains(text(), 'Materyal Bileşeni')]") 
		detailattributestitle_text = detailattributestitle.text
		if detailattributestitle_text == "Materyal Bileşeni":
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					strong_li_fa = span1
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					strong_li_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",strong_li_fa)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					product_color_fa = span2
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					product_color_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",product_color_fa)

				Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					
				description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None






def other_description(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'details-section')
		# print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//*[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		if detailattributestitle_text == "Ürün Özellikleri":
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					strong_li_fa = span1
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					strong_li_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",strong_li_fa)

				c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
				result_color = c_dict.fetchone()
				if not result_color:
					print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
					# product_color_fa = translator(translate_url, product_color_tr)
					# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
					product_color_fa = span2
					c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
					conn_dictdb.commit()
				if result_color:
					print("result>>>>>>>>>>>>>",result_color[0])
					product_color_fa = str(result_color[0])
				print("product_color_fa>>>>>>>>>>",product_color_fa)

				Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					
				description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None







def get_images(browser):
	try:
		product_details = browser.find_element(By.CLASS_NAME, 'styles-module_sliderBase__swkx1.product-slide-container')
		if product_details:
			images_ul = product_details.find_elements(By.TAG_NAME, 'img')
			print("images_ul",images_ul)	
			

			images_pre_list =[]
			for img in images_ul:
				image= img.get_attribute("src").replace("/128/192/","/1200/1800/")
				print("image>>>>>>>>>",image)
				if image:
					images_pre_list.append(image)
			print("images_pre_list=======>>>",images_pre_list)
			image_list = '|'.join([str(elem) for elem in images_pre_list])
			print(image_list)
			return image_list
		else:
			return None

	except Exception as e:
		base_product_image = browser.find_element(By.CLASS_NAME, 'base-product-image').find_element(By.TAG_NAME, 'img').get_attribute("src").replace("ty41","mnresize/1200/1800/ty41")
		if base_product_image:
			print("base_product_image",base_product_image)	
			images_pre_list =[]
			images_pre_list.append(base_product_image)
			image_list = '|'.join([str(elem) for elem in images_pre_list])
			print(image_list)
			return image_list
		else:
			return None





def get_price(browser,categorie_id):
	try:
		price_all = browser.find_element(By.CLASS_NAME, 'product-price-container')
		print(price_all)
		try:

			print("mm")
			price_sal_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-dsc')
			price_string = price_sal_str.text.replace(".","").replace("TL","")
			sales_price = price_string[:price_string.find(",")]			
			price_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-org')
			price_string = price_str.text.replace(".","").replace("TL","")
			price = price_string[:price_string.find(",")]
			print(price, sales_price)
			c_cost.execute('SELECT cost FROM categori_sku where id_categori = ?',(categorie_id,))
			result = c_cost.fetchone()
			if result:
				cost = int(result[0])
				print("cost>>>>>>>>>>>>>>>>>>",cost)
				return int(((int(price) + 12 ) * tl_price + cost)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + cost)/1000) * 1000
			else:
				return int(((int(price) + 12 ) * tl_price + 200000)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + 200000 )/1000) * 1000


		except Exception as e:
			price_str = price_all.find_element(By.CSS_SELECTOR, 'span.prc-dsc')
			print("price_str",price_str.text)
			price_string = price_str.text.replace(".","").replace("TL","")
			price = price_string[:price_string.find(",")]
			sales_price = price
			print(price, sales_price)
			c_cost.execute('SELECT cost FROM categori_sku where id_categori = ?',(categorie_id,))
			result = c_cost.fetchone()
			if result:
				cost = int(result[0])
				print("cost>>>>>>>>>>>>>>>>>>",cost)
				return int(((int(price) + 12 ) * tl_price + cost)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + cost)/1000) * 1000
			else:
				# return int(((int(round(price)) + 12 ) * 5200 + cost)/1000) * 1000,int(((int(round(sales_price)) + 12 ) * 5200 + cost)/1000) * 1000

				return int(((int(price) + 12 ) * tl_price + 200000)/1000) * 1000,int(((int(sales_price) + 12 ) * tl_price + 200000 )/1000) * 1000


	except Exception as e:
		# print(e)
		return None
 




def get_size(browser):
	try:
		size_box = browser.find_element(By.CLASS_NAME, 'size-variant-wrapper').find_elements(By.CSS_SELECTOR, 'div.sp-itm:not(.so.sp-itm)')		
		size_list = []
		for item in size_box:
			print(item)
			size = item.text
			size_list.append(size)
		print(size_list)
		return size_list
	except Exception as e:
		try:
			print(e)
			button_size = browser.find_element(By.CLASS_NAME, 'product-button-container').find_element(By.CSS_SELECTOR, 'button.add-to-basket')
			if button_size:
				return["تک سایز"]
			else:
				return None
		except:
			return None





# translate_browser = webdriver.Chrome(executable_path = CHROME_PATH,options = chrome_options)

# def translator(url,char):
# 	translate_browser.get(url)
# 	textarea = translate_browser.find_element(By.CLASS_NAME, 'er8xn')
# 	textarea.send_keys(str(char))
# 	time.sleep(5)
# 	translation = translate_browser.find_element(By.CLASS_NAME, 'VIiyi').text
# 	# VIiyi
# 	print(translation)
# 	# input()
# 	return translation

# translate_url = "https://translate.google.com/?hl=nl&sl=tr&tl=fa&op=translate"









cache_url = "chrome://settings/clearBrowserData?search=history"
def delete_cache(url,browser):
	driver = browser
	driver.execute_script("window.open('');")
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[-1])
	time.sleep(2)
	driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
	time.sleep(2)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
	actions.perform()
	time.sleep(2)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
	actions.perform()
	time.sleep(5) # wait some time to finish
	driver.close() # close this tab
	driver.switch_to.window(driver.window_handles[0]) # switch back






def get_color(browser):
	try:
		detail_border = browser.find_element(By.CLASS_NAME, 'detail-border')
		print("detail_border ===>>>",detail_border)
		detailattributestitle = detail_border.find_element(By.XPATH, "//h2[contains(text(), 'Ürün Özellikleri')]") 
		detailattributestitle_text = detailattributestitle.text
		print("detailattributestitle_text---000,",detailattributestitle_text)
		if detailattributestitle_text == "Ürün Özellikleri":
			# input("--rün Özellikler-----------enter ...")
			print("detailattributestitle_text ====>>",detailattributestitle_text)
			Product_description_ul = detailattributestitle.find_element(By.XPATH, "following-sibling::ul")			
			Product_description_li_all = Product_description_ul.find_elements(By.TAG_NAME, 'li')
			print("li ===============>>>>>",Product_description_li_all)
			Product_description_list =[]
			description_split_list=[]
			for li in Product_description_li_all:
				span1 = li.find_elements(By.TAG_NAME, 'span')[0].text
				print("span1 ==>>",span1)
				span2 = li.find_elements(By.TAG_NAME, 'span')[1].text
				print("span2  ==>>",span2)
				if span1 =="Renk":
					c_dict.execute('SELECT fa FROM material where tr = ?',(span1,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span1)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						strong_li_fa = span1
						c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span1),str(strong_li_fa),"trendyol"))
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						strong_li_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",strong_li_fa)

					c_dict.execute('SELECT fa FROM material where tr = ?',(span2,))
					result_color = c_dict.fetchone()
					if not result_color:
						print("rrrrrrrrrrrrrrrrrrrrrrrr",span2)
						# product_color_fa = translator(translate_url, product_color_tr)
						# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
						product_color_fa = span2
						c_dict.execute('INSERT OR IGNORE INTO material VALUES (?,?,?,?)',(None,str(span2),str(product_color_fa),"trendyol"))
						conn_dictdb.commit()
					if result_color:
						print("result>>>>>>>>>>>>>",result_color[0])
						product_color_fa = str(result_color[0])
					print("product_color_fa>>>>>>>>>>",product_color_fa)

					# Dimensions_text_ = "<li>"+ strong_li_fa + ":" +product_color_fa + "</li>"
					Dimensions_text_ = product_color_fa

						
					description_split_list.append(Dimensions_text_)

			description_all_str = ''.join([str(elem) for elem in description_split_list])
			# description_final = "<ul>"+str(description_all_str) + "</ul>"
			description_final = str(description_all_str)

			print("color_final>>>>>>>>>>>>>>>>>>",description_final)
			return description_final


		
	except Exception as e:
		# print(e)
		return None





def make_ready(just_update = True):
	browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=chrome_options)
	# browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
	# browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

	# browser = webdriver.Firefox(executable_path = FIREFOX_PATH,options=firefox_options)
	# browser.set_page_load_timeout(2)
	c.execute('SELECT * FROM urls WHERE done=0')
	urls = c.fetchall()
	count = 0
	for idx, url in enumerate(urls):
	# for url in urls:
		try:
			title_main = url[3]
			page_link = url[1]
			barcode = url[2]
			categorie_id = url[4]
			gharanti_pre=url[5]
			tag_name =url[7]
			tag_slug =url[8]
			tag_id = url[9]
			# print(page_link)
			c.execute('SELECT * FROM pre_process WHERE barcode=?',(barcode,))
			query = c.fetchone()
			print(query)
			# input("1234567")
			if not  query:
				print("page_link",page_link)
				if just_update:
					print("just_update")
					c.execute("SELECT * FROM product_sku WHERE wp_sku LIKE ?",(str(barcode)+"%",))
					in_stock = c.fetchone()
					if in_stock:
						url = url[1]
						browser.get(url)
						
						# time.sleep(2)
						barcode =barcode	
						try:
							add_to_basket_soldout = browser.find_element(By.CSS_SELECTOR, 'button.add-to-basket.sold-out')					
							if add_to_basket_soldout:
								# return None
								print("no size")
						except:
							
							size = get_size(browser)
							if size:
								size_string = "|".join(size)						
								# categorie_id =categorie_id
								price,sales_price = get_price(browser,categorie_id)
								c.execute('INSERT OR IGNORE INTO pre_process VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(None,barcode,size_string,price,sales_price,0,"title",url,"image_list","product_color_fa","country","description","gharanti","supplier",None,"str(image_name)","image_alt","slug","str(tag_name)","tag_slug",None))
								
								conn.commit()
								c.execute('UPDATE urls SET barcode=? WHERE url=?',(barcode,url))
								conn.commit()
								c.execute('UPDATE urls SET done=1 WHERE barcode!=11')
								conn.commit()
						# else:
						# 	c.execute('UPDATE urls SET done=22 WHERE url=?',(url,))
						# 	conn.commit()


						# count +=1
						# if count == 300:
						# 	print("ooooooohhhhhhhhhhhhhhhhhhhhhhh")
						# 	deletecache = delete_cache(cache_url,browser)
						# 	count=0
								


				else:
					# print("qw12")
					url = url[1]
					browser.get(url)
					# time.sleep(1)
					try:
						size = get_size(browser)
						if size:
							# print("kkk")
							# # barcode = browser.find_element(By.CLASS_NAME, '')("product-sku").text.strip()
							# url_str = str(url)
							# # if "?" in url_str:
							# barcode_string = url_str[:url_str.find("-p-")]
							# barcode_str = barcode_string[barcode_string.rfind("-"):]
							# print("barcode_str",barcode_str)
							# color_string = url_str[url_str.find("-p-"):url_str.find("?")]
							# # print("barcode_string",barcode_string)
							# barcode = barcode_str.replace("-p-","-color-").strip("-") + color_string.replace("-p-","-color-")
							# print(".....barcode:",barcode)
							# print(barcode)
							# print("barcode >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",barcode,"<<<<<<<<<<<<<<<<<<<<<barcode")					
							

							title_contain_barcode = browser.find_element(By.CLASS_NAME, 'pr-new-br').find_element(By.TAG_NAME, 'span').text
							barcode_str = title_contain_barcode[title_contain_barcode.rfind(" "):]
							barcode_strip = barcode_str.strip()
							print("barcode_str ====>>",barcode_str)
							try:
								# product_color_tr = color_no_trans(browser)
								# print(product_color_tr,"product_color_tr")
								# input("ccccc")
								product_color_tr= browser.find_element(By.CLASS_NAME, 'selected.slc-img').get_attribute("title").replace(" ","-").replace("/","-")
								if product_color_tr:
									product_color_t = product_color_tr.replace(" ","-")
									barcode = barcode_strip + "-" + str(product_color_tr)
									print("barcode ====>>",barcode)
							except:
							# else:
								barcode = barcode_strip
								print("barcode ====>>",barcode)



							size_string = "|".join(size)	
							print("size_string>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",size_string,"<<<<<<<<<<<<<<<<<<<<<size_string")	
							# for i in range(1,100):
							# 	time.sleep(.3)
							# 	time.sleep(.3)
							# 	precent = str(i)
							# 	script_string = "window.scrollTo(0, document.body.scrollHeight - (document.body.scrollHeight * %s / 100 ) );" %(str(i))
							# 	browser.execute_script(script_string)
											
							# SCROLL_PAUSE_TIME = 0.5
							# # Get scroll height
							# last_height = browser.execute_script("return document.body.scrollHeight")
							# while True:
							# 	# Scroll down to bottom
							# 	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
							# 	# Wait to load page
							# 	time.sleep(SCROLL_PAUSE_TIME)
							# 	# Calculate new scroll height and compare with last scroll height
							# 	new_height = browser.execute_script("return document.body.scrollHeight")
							# 	if new_height == last_height:
							# 		break
							# 	last_height = new_height
							image_list = get_images(browser)
							print("image_list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",image_list,"<<<<<<<<<<<<<<<<<<<<<image_list")					
							
							price,sales_price = get_price(browser,categorie_id)
							print("sales_price ,price >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",sales_price,price,"<<<<<<<<<<<<<<<<<<<<<sales_price,price")					
							
						
							
							# try:
							# 	product_color_tr= browser.find_element(By.CLASS_NAME, 'selected.slc-img').get_attribute("title")
							# 	print("color_div  ==>>>",product_color_tr)
							# 	c_dict.execute('SELECT fa FROM color where tr = ?',(product_color_tr,))
							# 	result_color = c_dict.fetchone()
							# 	if not result_color:
							# 		print("rrrrrrrrrrrrrrrrrrrrrrrr",product_color_tr)
							# 		# product_color_fa = translator(translate_url, product_color_tr)
							# 		# print("product_color_fa>>>>>>>>>>>>",product_color_fa)
							# 		product_color_fa = product_color_tr
							# 		c_dict.execute('INSERT OR IGNORE INTO color VALUES (?,?,?,?,?)',(None,str(product_color_tr),str(product_color_fa),"trendyol",""))
							# 		conn_dictdb.commit()
							# 	if result_color:
							# 		print("result>>>>>>>>>>>>>",result_color[0])
							# 		product_color_fa = str(result_color[0])
							# 	print("product_color_fa>>>>>>>>>>",product_color_fa)

							# 	print("product_color_fa >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",product_color_fa,"<<<<<<<<<<<<<<<<<<<<<product_color_fa")					
							
							# except:
							# 	product_color_fa = " "
							# product_color_fa_trans = color_description(browser)
							# print("product_color_fa_trans----->>.",product_color_fa_trans)
							# input("product_color_fa")

							product_color_fa_trans = get_color(browser)

							otherr_description  = other_description(browser)

							material = material_description(browser)
							# print("material>>>>>",material)
							if material:
								descriptionn ='<h3>'+"مشخصات:"+'</h3>'+ '<ul>'+str(otherr_description)+'</ul>'+'<br>'+'<h3>'+"جنس:"+'</h3>'+'<ul>'+ str(material) +'</ul>'
								description = descriptionn.replace("None","").replace("<ul>None</ul>","")
								print("description (((((((((((((((((",description,"))))))))))))))))))))))")	
							else:
								descriptionn ='<h3>'+"مشخصات:"+'</h3>'+ '<ul>'+str(otherr_description)+'</ul>'
								description = descriptionn.replace("None","").replace("<ul>None</ul>","")
								print("description (((((((((((((((((",description,"))))))))))))))))))))))")												
							# title = title_main + " "+product_color_fa +" "+"یو اس پولو"
							# title = title_main +" "+"آوا"+ " " + str(barcode)
							# title = title_main +" "+"اکو "+ " " + str(barcode)
							# title = title_main +" "+"آلدو"+ " " + str(barcode)
							barcode_fa = barcode_strip + "-" + product_color_fa_trans
							title = title_main +" "+"دیور"+ " " + str(barcode_fa)


							slug = title_main.replace(" ","-") + "-" + barcode	
							gharanti = gharanti_pre
							country ="فرانسه"
							supplier = "atrshop"
							image_name = str(title_main)+ " "+product_color_fa_trans +" "+" "+"dior"
							print("image_name>>>>>>>>>>>>>",image_name)
							image_alt = image_name							
							c.execute('INSERT OR IGNORE INTO pre_process VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(None,barcode,size_string,price,sales_price,0,title,url,image_list,product_color_fa_trans,country,description,gharanti,supplier,categorie_id,str(image_name),image_alt,slug,str(tag_name),tag_slug,tag_id))
							conn.commit()
							c.execute('UPDATE urls SET barcode=? WHERE url=?',(barcode,url))
							conn.commit()
							c.execute('UPDATE urls SET done=1 WHERE barcode!=11')
							conn.commit()
					except Exception as e:
						print(e)	
					# else:
					# 	c.execute('UPDATE urls SET done=22 WHERE url=?',(url,))
					# 	conn.commit()
		except TimeoutException as e:
			print("Exception has been thrown. ")
			print(str(e))
			browser.set_page_load_timeout(30)
			time.sleep(50)
			continue	









def looper(crawl_list):
	browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=chrome_options)
	# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

	# browser = webdriver.Chrome(executable_path=CHROME_PATH,chrome_options=chrome_options)
	time.sleep(10)
	# page_number = 1
	for page in crawl_list:
		page_number = 1
		# for i in range(0,10):
		while True:
			next_page = str(page["url"]) + '&pi=' + str(page_number)
			# page_number += 1
			# print(	next_page)	
			# if page_number ==6:
			# 	break
			
			print(next_page)
			# browser.get(page["url"])
			browser.get(next_page)
			time.sleep(10)
			# while True:
			title =page["title"]
			gharanti = page["gharanti"]
			categorie_id =page["categorie_id"]
			tag_name=page["tag_name"]
			tag_slug=page["tag_slug"]
			tag_id=page["tag_id"]

			# input("Enter...")
			try:	

				products = browser.find_elements(By.CLASS_NAME, 'p-card-wrppr')
				if products:
					for product in products:		
						raw_link = product.find_element(By.TAG_NAME, 'a').get_attribute("href")
						p_link =raw_link
						c.execute('SELECT * FROM urls WHERE url=?',(p_link,))
						query = c.fetchone()
						if not query:
							c.execute('INSERT or IGNORE INTO urls VALUES (?,?,?,?,?,?,?,?,?,?)',(None,p_link,11,title,categorie_id,gharanti,0,tag_name,tag_slug,tag_id))
							conn.commit()
				# page_number += 1	
				# page_number = page_number + 1
				# print(next_page)
					page_number += 1
				else:
					break
					# return	
			except Exception as e:
				print(e)
				break

				
		else:
			return







def fetch_sku(options = None):
	
	# api_string = "products?per_page=%d&page=%d&stock_status=%s&search=%s"
	api_string = "products?per_page=%d&page=%d&stock_status=%s"

	if options:
		# api_string = "products?per_page=%d&page=%d&stock_status=%s&search=%s" + "&" + options
		api_string = "products?per_page=%d&page=%d&stock_status=%s" + "&" + options


	i = 1
	while True:
		try:
			# result = wcapi.get(api_string%(60,i,'instock','ترندیول')).json()
			result = wcapi.get(api_string%(60,i,'instock')).json()
			if result:
				print("page: " + str(i))
				i += 1
				for product in result:
					wp_sku = product['sku']
					print("wp_sku>>>>>",wp_sku)
					wp_id = int(product['id'])
					if (len(product['variations']) != 0 ):
						wp_variation = int(product['variations'][0])
					else:
						wp_variation = int(0000)
					c.execute('SELECT * FROM product_sku WHERE wp_sku = ?',(wp_sku,))
					record = c.fetchone()
					# if not record:
					c.execute('INSERT OR IGNORE INTO product_sku VALUES (?,?,?,?)',(None,wp_sku,wp_id,wp_variation))
					conn.commit()
			else:
				i += 1
				print("page: " + str(i))
				for product in result:
					wp_sku = product['sku']
					wp_id = int(product['id'])
					if (len(product['variations']) != 0 ):
						wp_variation = int(product['variations'][0])
					else:
						wp_variation = int(0000)
					c.execute('SELECT * FROM product_sku WHERE wp_sku = ?',(wp_sku,))
					record = c.fetchone()
					# if not record:
					c.execute('INSERT OR IGNORE INTO product_sku VALUES (?,?,?,?)',(None,wp_sku,wp_id,wp_variation))
					conn.commit()
				return
		except Exception as e:
			print(e)
			i -= 1
			time.sleep(50)











def image_appender(images_string,image_guide_categori,image_name,image_alt):
	img_json_list = []
	# images_list = images_string.split("|")
	images_list = images_string
	image_name =image_name
	image_alt = image_alt
	for image_url in images_list:
		image_img = "65.108.221.176/files/"+str(image_url)
		print(image_img)
		image = image_img.replace("\\","/")
		print("qqqqqqqqqqqqqqqqqqqqqqq",str(image))
		print("image_name",image_name)
		print("image_alt",image_alt)
		img_json_list.append({"src": image,"name": image_name,"alt": image_alt })
	if image_guide_categori and img_json_list:
		img_json_list.append({"id":int(image_guide_categori) ,"name": "راهنمای سایز","alt": "راهنمای سایز" })
		# input("gggggggggggggggggggggggggggggggggggg")

		# img_json_list.append({"src":image_guide_categori ,"name": "راهنمای سایز","alt": "راهنمای سایز" })

	# else:
	return img_json_list


def tag_appender(tag_name,tag_slug,tag_id):
	if tag_name:
		tag_dict = {
			"id": tag_id,
			"name": str(tag_name),
			"slug": str(tag_slug)
		}

		return [tag_dict]
	else:
		print("mmm")
		return []
	
	








def json_product(barcode,tag_name,tag_slug,tag_id,attributes,meta_data_product,image_guide_categori,product_color,gharanti,supplier,title,slug,description,image_name,image_alt,country,image_string,size, price,sales_price,attr,in_wp_stock = False,on_sale = False):

# def json_product(barcode,title,tag_name,tag_slug,tag_id,attributes,image_guide_categori,product_color,gharanti,supplier,slug,description,image_name,image_alt,country,image_string,size, price,sales_price,attr,in_wp_stock = False,on_sale = False):
	if price > sales_price:
		on_sale = True

	variation_data = {
		"regular_price" : str(price),
		"sale_price" : str(sales_price)
	}

	if in_wp_stock:
		data = {
			"sku": barcode,
			"type": "variable",
			"attributes":attributes,
			"meta_data":meta_data_product
		}
	else:
		image_list = image_appender(image_string,image_guide_categori,image_name,image_alt)
		tag_list = tag_appender(tag_name, tag_slug, tag_id)
		data = {
		    "name":title,
		    "slug":slug,    
		    "sku": barcode,
		    "shipping_class": "international-shipping",
    		"shipping_class_id": 3830,
		    "type": "variable",
		    "status": "draft",
		    "description": str(description),
		    "managing_stock":True,
		    "stock_quantity":2,
		    "in_stock":True,
			"tags": tag_list,
		    "attributes": [
		    	{	
		    		"id": 23,
		            "name": "size",
		            "slug": "size",
		            "visible": False,
		            "variation": True,
		            "options":size
		        },
		        {
                "id": 1,
                "name": "color",
                "slug": "pa_color",
                "position": 1,
                "type": "select",
                "visible": False,
                "variation": False,
                "options":[str(product_color)]
            	},
            	{
                "id": 11,
                "name": "کشور",
                "slug": "pa_country",
                "type": "select",
                "visible": False,
                "variation": False,
                "options":[str(country)]

            	},
            	{
		        "id": 13,
		        "name": "گارانتی",
		        "slug": "pa_warranty",
		        "type": "select",
		        "visible": False,
                "variation": False,
		        "options":[gharanti]
            	},
            	{
            	"id": 25,
		        "name": "تامین کننده",
		        "slug": "pa_supplier",
		        "type": "select",
		        "visible": False,
                "variation": False,
		        "options":[str(supplier)]
            	}            	

		    ],

		    "images": image_list
		}
	return data,variation_data

















def add_update(prev_barcode,cur_barcode,url,tag_name,tag_slug,tag_id,image_guide_categori, size_list, price, sales_price,image_string,product_color,country,title,slug,description,gharanti,supplier,categorie_id,image_name,image_alt):
	t = (str(prev_barcode),)
	c.execute('SELECT * FROM product_sku WHERE wp_sku Like ?', (t))
	p_detail = c.fetchone()
	print("ISSS AVAIALABEL >>>>>" + str(p_detail) )
	print("this is where we eant >>>>")
	# if p_detail:
	# 	print("yeeeeeeeeeeeeeeeeeeeeeeeeeeej")
	# 	attr_id = int(p_detail[3])
	# 	print("attr_id:" + str(attr_id))
	# 	wp_id = int(p_detail[2])
	# 	print("wp_id:" + str(wp_id))

	# 	get_meta_data_product = wcapi.get("products/%s"%wp_id).json()
	# 	meta_data_product = get_meta_data_product['meta_data']
	# 	meta_data_product.append({ "key": "product_url", "value": str(url) })
	# 	print("meta_data_product++::",meta_data_product)

	# 	get_attributes_product = wcapi.get("products/%s"%wp_id).json()
	# 	print("get_attributes_product-----",get_attributes_product)
	# 	attributes_product = get_attributes_product['attributes']
	# 	if attributes_product:
	# 		for dict_item in attributes_product:
	# 			if dict_item['id']==23:
	# 				print("yes size ")
	# 				dict_item['options'] = size_list
	# 			else:
	# 				attributes_product.append({'id': 23, 'name': 'سایز', 'position': 0, 'visible': False, 'variation': True, 'options':size_list})
	# 				# dict_item['options'] = size_list
	# 		for dict_item in attributes_product:
	# 			if dict_item['id']==1:
	# 				print(dict_item)
	# 				sub_color = dict_item['options']
	# 				if len(sub_color)==1:
	# 				# if sub_color:
	# 					print("sub_color:::::",sub_color)
	# 					c_dict.execute('SELECT * FROM color WHERE fa like ?',(sub_color[0],))
	# 					dict_detail = c_dict.fetchone()
	# 					if dict_detail:
	# 						print("----yes sub_color----")
	# 						main_color = str(dict_detail[4])
	# 						if main_color:
	# 							print("main_color--->>",main_color)
	# 							dict_item['options'] = [str(main_color)]
	# 						else:
	# 							subcolor = str(dict_detail[2])
	# 							print("subcolor",subcolor)
	# 							dict_item['options'] = [str(subcolor)]
	# 							print("color---------->>",dict_item['options'])
	# 				else:
	# 					sub_color = ' '.join([str(elem) for elem in reversed(sub_color)])
	# 					print("123wsx",sub_color)
	# 					c_dict.execute('SELECT * FROM color WHERE fa like ?',(sub_color,))
	# 					dict_detail = c_dict.fetchone()
	# 					if dict_detail:
	# 						print("----yes sub_color----")
	# 						main_color = str(dict_detail[4])
	# 						if main_color:
	# 							print("main_color--->>",main_color)
	# 							dict_item['options'] = [str(main_color)]
	# 						else:
	# 							subcolor = str(dict_detail[2])
	# 							print("subcolor",subcolor)
	# 							dict_item['options'] = [str(subcolor)]
	# 							print("color---------->>",dict_item['options'])




					

		
			
	# 		attributes = attributes_product
	# 		print("--------attributes------------------",attributes)
		
	# 		# print("attributes_product----------",attributes_product)
	# 		# print("attributes_product[0]['id']",attributes_product[0])
	# 		# if attributes_product[0]['id']==23:
	# 		# 	attributes_product[0]['options'] = size_list
	# 		# 	sub_color = attributes_product[4]['options']
	# 		# 	print("sub_color--->>",sub_color[0])
	# 		# 	c_dict.execute('SELECT * FROM color WHERE fa like ?',(sub_color))
	# 		# 	dict_detail = c_dict.fetchone()
	# 		# 	if dict_detail:
	# 		# 		print("----yes sub_color----")
	# 		# 		main_color = str(dict_detail[4])
	# 		# 		# if main_color:
	# 		# 		# 	print("main_color--->>",main_color)
	# 		# 		# 	attributes_product[4]['options'] = main_color
	# 		# 		# else:
	# 		# 		subcolor = str(dict_detail[2])
	# 		# 		print("subcolor",subcolor)
	# 		# 		attributes_product[4]['options'] = subcolor
	# 		# 		print("color---------->>",attributes_product[4]['options'])
	# 			# attributes = attributes_product
	# 			# print("--------attributes------------------",attributes)

	# 		old_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,attributes,meta_data_product,image_guide_categori,product_color,gharanti,supplier,title,slug,description,image_name,image_alt,country,image_string, size_list, price,sales_price,attr_id,in_wp_stock = True)
	# 		# old_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,"attributes",image_guide_categori,product_color,gharanti,supplier,title,slug,description,image_name,image_alt,country,image_string, size_list, price,sales_price,attr_id,in_wp_stock = True)

	# 		print("after json")
	# 		json_result = wcapi.put("products/%s"%wp_id, old_json).json()
	# 		variation_result = wcapi.put("products/%s/variations/%s" % (wp_id,attr_id), p_variation)
	# 		print("is available")
	# # else:
	print("111111111111111111111111111111111111111111111111111111111111111")
	attr_id = None
	wp_id= ""
	new_json,p_variation = json_product(cur_barcode,tag_name,tag_slug,tag_id,"attributes","meta_data_product",image_guide_categori,product_color,gharanti,supplier,title,slug,description,image_name,image_alt,country,image_string, size_list, price,sales_price,attr_id,in_wp_stock = False)
	json_result = wcapi.post("products", new_json).json()
	print("json_result---------------",json_result)
	if 'id' in json_result:
		wp_id = json_result['id']
		variation_result = wcapi.post("products/%s/variations" % wp_id, p_variation)
		print(variation_result)
		brand = wcapi.put("products/%s" % wp_id , {'brands':'3412'})
		category = wcapi.put("products/%s" % wp_id , {"categories": [{"id": categorie_id}]})
		print("categorie_id",category)


def Convert_images_to_list():
	connection = sqlite3.connect("stock.db")
	crsr = connection.cursor()
	crsr.execute('SELECT * FROM pre_process ')
	result = crsr.fetchall()
	barcode_list =[]
	for row in result:
		barcode = row[1]
		print(barcode)
		barcode_list.append(barcode)
	image_list = []
	for barcode in barcode_list:
		image_str_list =[]		
		for file in glob.glob("trendyol_images/%s"%(barcode)):
			for image in glob.glob("trendyol_images/%s/*.jpeg"%(barcode)):
				image_str_list.append(image)
		# print(image_str_list)
		image_list.append(image_str_list)
		# images_str = "|".join(image_list)

	dict_images = dict(zip(barcode_list, image_list))
	return dict_images







def new_dict_sizeguide(dict_sizeguide,categori_id,brand_id):
	print("dict_sizeguide>>>",dict_sizeguide)
	new_dict_sizeguide={}
	for key,value in dict_sizeguide.items():
		new_dict = {}
		for key_value,value_value in value.items():
			print("key_value",key_value)
			for tuple_andis in key_value:
				new_dict[str(tuple_andis)]=str(value_value)
		new_dict_sizeguide[key]=new_dict
	try:	
		size_guid = new_dict_sizeguide[brand_id][categori_id]	
		return new_dict_sizeguide[brand_id][categori_id]
		
	except Exception as e:
		return None
		


# def new_dict_sizeguide(dict_sizeguide,categori_id,brand_id):
# 	print("dict_sizeguide>>>",dict_sizeguide)
# 	new_dict_sizeguide={}
# 	for key,value in dict_sizeguide.items():
# 		new_dict = {}
# 		for key_value,value_value in value.items():
# 			for tuple_andis in key_value:
# 				new_dict[str(tuple_andis)]=str(value_value)
# 		new_dict_sizeguide[key]=new_dict
# 	try:	
# 		size_guid = new_dict_sizeguide[brand_id][categori_id]	
# 		return new_dict_sizeguide[brand_id][str(categori_id)]
		
# 	except Exception as e:
# 		return None
		


def sync_stocks(prev_barcode_suffix,cur_barcode_suffix):
	c.execute('SELECT * FROM pre_process where done=0')
	result = c.fetchall()
	print(result[0][0])
	id_product = result[0][0]
	try:
		for row in result:
			id_product = row[0]	
			# id_product = row[0]
			barcode = row[1]
			print("ssss")
			print(barcode)
			url = row[7]
			title = row[6]
			dict_images = Convert_images_to_list()
			description =row[11]
			print(dict_images)
			gharanti = row[12]
			categorie_id =row[14]
			print("categori_id",type(categorie_id))
			brand_id ="cacharel"
			image_guide_categori = new_dict_sizeguide(dict_sizeguide,str(categorie_id),brand_id)
			print("image_guide_categori>>>>>>>>>>>>>>",image_guide_categori)
			# image_guide_categori = check_sizeguide(categorie_id,brand_id)
			image_string = dict_images[str(barcode)]
			# image_guide_categori = new_dict_sizeguide(dict_sizeguide,str(categorie_id),brand_id)
			# print("image_guide_categori>>>>>>>>>>>>>>",image_guide_categori)
			# # image_guide_categori = check_sizeguide(str(categorie_id))
			# image_string = dict_images[str(barcode)]
			print("image_string00000000000000000",image_string)
			if image_string:
				barcode,size_list,price,sales_price,done,image_string,product_color,country,title,slug,description,gharanti,supplier,categorie_id,image_name,image_alt,image_guide_categori,tag_name,tag_slug,tag_id= row[1],row[2].split('|'),row[4],row[3],row[5],image_string,row[9],row[10],row[6],row[17],row[11],row[12],row[13],row[14],row[15],row[16],image_guide_categori,row[18],row[19],row[20]
				print(str(barcode) + "||" + str(size_list)  + "||") 
				prev_barcode = barcode + prev_barcode_suffix 
				print("prev_barcode:" + str(prev_barcode))
				cur_barcode = barcode + cur_barcode_suffix 
				print("current barcode:" + str(cur_barcode))
				if done == 0:
					print("its not done and we are working on it ....")
					wp_id = add_update(prev_barcode,cur_barcode,url,tag_name,tag_slug,tag_id,image_guide_categori, size_list, price, sales_price,image_string,product_color,country,title,slug,description,gharanti,supplier,categorie_id,image_name,image_alt)
					print("wp_id")
					print(wp_id)	
					# input("enter .....")
					c.execute('UPDATE pre_process SET done=? WHERE barcode=?',(int(1),barcode))
					print("adding/updating "+ str(barcode) + "\n")
					conn.commit()
			# input("dd")
	except:
		time.sleep(50)
		id_product =id_product
		while True:
			try:
				c.execute('SELECT * FROM pre_process where done=0 and id >= ? ',(id_product,))
				result = c.fetchall()
				for row in result:
					id_product = row[0]	
					# id_product = row[0]
					barcode = row[1]
					print("ssss")
					print(barcode)
					url = row[7]
					title = row[6]
					dict_images = Convert_images_to_list()
					description =row[11]
					print(dict_images)
					gharanti = row[12]
					categorie_id =row[14]
					print("categori_id",type(categorie_id))
					brand_id ="koton"
					image_guide_categori = new_dict_sizeguide(dict_sizeguide,str(categorie_id),brand_id)
					print("image_guide_categori>>>>>>>>>>>>>>",image_guide_categori)
					# image_guide_categori = check_sizeguide(categorie_id,brand_id)
					image_string = dict_images[str(barcode)]
					# image_guide_categori = new_dict_sizeguide(dict_sizeguide,str(categorie_id),brand_id)
					# print("image_guide_categori>>>>>>>>>>>>>>",image_guide_categori)
					# # image_guide_categori = check_sizeguide(str(categorie_id))
					# image_string = dict_images[str(barcode)]
					print("image_string00000000000000000",image_string)
					if image_string:
						barcode,size_list,price,sales_price,done,image_string,product_color,country,title,slug,description,gharanti,supplier,categorie_id,image_name,image_alt,image_guide_categori,tag_name,tag_slug,tag_id= row[1],row[2].split('|'),row[4],row[3],row[5],image_string,row[9],row[10],row[6],row[17],row[11],row[12],row[13],row[14],row[15],row[16],image_guide_categori,row[18],row[19],row[20]
						print(str(barcode) + "||" + str(size_list)  + "||") 
						prev_barcode = barcode + prev_barcode_suffix 
						print("prev_barcode:" + str(prev_barcode))
						cur_barcode = barcode + cur_barcode_suffix 
						print("current barcode:" + str(cur_barcode))
						if done == 0:
							print("its not done and we are working on it ....")
							wp_id = add_update(prev_barcode,cur_barcode,url,tag_name,tag_slug,tag_id,image_guide_categori, size_list, price, sales_price,image_string,product_color,country,title,slug,description,gharanti,supplier,categorie_id,image_name,image_alt)
							print("wp_id")
							print(wp_id)	
							# input("enter .....")
							c.execute('UPDATE pre_process SET done=? WHERE barcode=?',(int(1),barcode))
							print("adding/updating "+ str(barcode) + "\n")
							conn.commit()
			except: 
				id_product -= 1
				time.sleep(30)





def file_count(file_name):
	result = []
	for files in os.walk('img'):
		return len([s for s in files[2] if file_name in s])

def create_image(barcode):
	img_code = "hm" + barcode[2:]
	# img_count = file_count(img_code)
	img_count = 4
	img_list = []
	suffix = ['b','a','c','d','e','f','g']
	url = "https://shahremun.com/wp-content/uploads/2017/09/"
	for i in range(img_count):
		img_dict = {}
		img_dict["src"] = url + img_code + str(suffix[0]) + ".jpeg"
		img_dict["position"] = i
		img_list.append(json.dumps(img_dict))

		suffix.pop(0)

	return img_list
# print create_image("hm12154554")



												
def have_file(file_name):
	result = []
	for files in os.walk('img'):
		for file in files[2]:
			if str(file_name) in file:
				print("*********++++++" + str(file))
				return True
		return False



def list_images():
	# browser = webdriver.PhantomJS(PHANTOMJS_PATH)
	# browser = webdriver.Firefox(executable_path='./geckodriver',firefox_options=options)
	browser = webdriver.Chrome(executable_path=CHROME_PATH,chrome_options=optionss)
	# fetch_sku("status=draft")
	c.execute('SELECT * FROM urls')
	urls = c.fetchall()
	for url in urls:
		barcode = url[1].rsplit('.',2)[1]
		print(barcode)
		c.execute("SELECT * FROM pre_process WHERE barcode LIKE ?",(str(barcode)+"%",))
		# c.execute("SELECT * FROM product_sku WHERE wp_sku LIKE ?",(str(barcode)+"%",))
		have_code = c.fetchone()
		if have_code:
			if list_files(barcode):
				delete_file(barcode)

def list_files(file_name):
	result = []
	for files in os.walk('img'):
		for file in files[2]:
			if str(file_name) in file:
				result.append(file)
	print("image list:" + str(result))
	print("the lenght is :" + str(len(result)))			
	if len(result) == 1 :
		return True
	else:
		return False

def delete_file(file_name):
	for files in os.walk('img'):
		for file in files[2]:
			if str(file_name) in file:
				print("yes files is in list")
				print("-----" + str())
				try:
					if os.path.isfile("/img/"+str(file)):
						print("HHOOOOOOLLAAA")
						os.remove("/img/"+str(file))
						# time.sleep(2)
				except Exception as e:
					print("exception" + str(e))







create_tables()
# looper(avva)
# looper(ipekyol)
# looper(ecco_ayyakkabi)
# looper(aldo)
# looper(gap)

# looper(dior_perfume)

# fetch_sku()
# make_ready(just_update = False)
# make_ready(just_update = True)
sync_stocks("-tnn1","-tnn1")

# download_images()
# list_images()
# print file_count('0505071002')

