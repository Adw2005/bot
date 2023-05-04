from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# criando o espaço para o detach dentro de uma variável

options = Options()
options.add_experimental_option("detach", True)

# adicionando paramétro no codigo

navegador = webdriver.Chrome(options=options)

service = Service(ChromeDriverManager().install())

# entrar no navegador

navegador.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1683206197&rver=7.3.6960.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2frpsauth%2fv1%2faccount%2fSignInCallback%3fstate%3deyJSdSI6Imh0dHBzOi8vd3d3Lm1pY3Jvc29mdC5jb20vcHQtYnIiLCJMYyI6IjEwNDYiLCJIb3N0Ijoid3d3Lm1pY3Jvc29mdC5jb20ifQ&lc=1046&id=74335&aadredir=0")

# LOgando na conta da microsoft

navegador.find_element('xpath', '//*[@id="i0116"]').send_keys("cagetheelephant1819@gmail.com")
time.sleep(1)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="i0118"]').send_keys("1819290906Ad")
time.sleep(1)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="wcpConsentBannerCtrl"]/div[3]/button[1]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="close-epb"]').click()


