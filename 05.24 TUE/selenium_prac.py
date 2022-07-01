from selenium import webdriver


browser = webdriver.Chrome()
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%A0%EC%96%91%EC%9D%B4&oquery=%EA%B0%95%EC%95%84%EC%A7%80&tqi=hoxJOwp0YidssjyfsDRssssst8o-187193'
browser.get(url)
