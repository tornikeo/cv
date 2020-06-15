from selenium import webdriver

options = webdriver.firefox.options.Options()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.get('http://localhost:8000')
assert 'Django' in browser.title