from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def buildList():
	f = open("shoppingList.txt", "r")
	lines = f.readlines()
	i = 0
	for line in lines:
		lines[i] = line.strip()
		i += 1
	return lines

def main():
	fName = "Lori"
	lName = "Goldsmith"
	username = "joshuasurfer@gmail.com"
	psw = "p22-DGGA"
	shoppingList = buildList()
	cardNum = 4430466051124609
	expDate = "0/22"
	csv = 236

	browser = webdriver.Chrome('/Users/joshgoldsmith/Documents/PythonLibraries/chromedriver')
	browser.get('https://grocery.walmart.com/')
	time.sleep(3)
	signInLink = browser.find_element_by_xpath("//a[@data-automation-id='signInLink']/span[@data-automation-id='my-account-text']")
	signInLink.click()

	input("Please Enter your Email and Password. After Press ENTER to continue")

	searchBar = browser.find_element_by_xpath("//form[@id='searchForm']/input")
	i = 0
	for item in shoppingList:
		searchBar = browser.find_element_by_xpath("//form[@id='searchForm']/input")
		if i != 0:
			clearBtn = browser.find_element_by_xpath("//form[@id='searchForm']/button[1]")
			clearBtn.click()
		searchBar.send_keys(item)
		searchBar.send_keys(Keys.ENTER)
		i += 1
		time.sleep(2)
		addToCart = browser.find_element_by_xpath("(//button[@type='button'])[4]")
		addToCart.click()
		time.sleep(2)

	input("Please confirm cart then press ENTER to continue")

	checkOut = browser.find_element_by_xpath("//button[contains(.,'Check Out')]")
	checkOut.click()
	time.sleep(3)
	continueTo = browser.find_element_by_xpath("//a[@data-automation-id='checkoutLink']")
	continueTo.click()

	input("Please select a time that works for you. Then press ENTER to continue")

	addCard = browser.find_element_by_xpath("//span[contains(.,'Add new credit/debit card')]")
	addCard.click()

	fNameInpt = browser.find_element_by_id("firstName")
	fNameInpt.send_keys(fName)
	lNameInpt = browser.find_element_by_id("lastName")
	lNameInpt.send_keys(lName)
	cardInpt = browser.find_element_by_name("creditCard")
	cardInpt.send_keys(cardNum)




	input("Please press ENTER to EXIT")


	browser.quit();
main()