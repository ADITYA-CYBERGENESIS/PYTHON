from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# List of Instagram profile links
profile_links = [
    "https://www.instagram.com/ashleygraham/",
    "https://www.instagram.com/bellahadid/",
    "https://www.instagram.com/beyonce/",
    "https://www.instagram.com/charlidamelio/",
    "https://www.instagram.com/chiaraferragni/",
    "https://www.instagram.com/dollysingh/",
    "https://www.instagram.com/emrata/",
    "https://www.instagram.com/gigihadid/",
    "https://www.instagram.com/hudabeauty/",
    "https://www.instagram.com/jessicaalba/",
    "https://www.instagram.com/katyperry/",
    "https://www.instagram.com/kendalljenner/",
    "https://www.instagram.com/kimkardashian/",
    "https://www.instagram.com/ladygaga/",
    "https://www.instagram.com/lewishamilton/",
    "https://www.instagram.com/lisarenee36/",
    "https://www.instagram.com/livblaque/",
    "https://www.instagram.com/mirandakerr/",
    "https://www.instagram.com/nadinelewinsky/",
    "https://www.instagram.com/oliviaculpo/",
    "https://www.instagram.com/paulinaporizkova/",
    "https://www.instagram.com/selenagomez/",
    "https://www.instagram.com/sofiarichie/",
    "https://www.instagram.com/theellenshow/",
    "https://www.instagram.com/victoriabeckham/",
    "https://www.instagram.com/xololove/",
    "https://www.instagram.com/ashleytisdale/",
    "https://www.instagram.com/carodaur/",
    "https://www.instagram.com/chrissyteigen/",
    "https://www.instagram.com/daschapolanco/",
    "https://www.instagram.com/emmawatson/",
    "https://www.instagram.com/gabrielleunion/",
    "https://www.instagram.com/haileybieber/",
    "https://www.instagram.com/jenniferlopez/",
    "https://www.instagram.com/kyliejenner/",
    "https://www.instagram.com/ladylike/",
    "https://www.instagram.com/naileadevonne/",
    "https://www.instagram.com/natgeo/",
    "https://www.instagram.com/oliviarodrigo/",
    "https://www.instagram.com/rachelgreeneberg/",
    "https://www.instagram.com/rupikahiwal/",
    "https://www.instagram.com/skaijackson/",
    "https://www.instagram.com/stellamccartney/",
    "https://www.instagram.com/victoriajustice/",
    "https://www.instagram.com/zaweetawada/",
    "https://www.instagram.com/aashnashroff/",
    "https://www.instagram.com/ananyapanday/",
    "https://www.instagram.com/ayushmankhera/",
    "https://www.instagram.com/dollysingh/",
    "https://www.instagram.com/fayedsouza/",
    "https://www.instagram.com/jannatzubair29/",
    "https://www.instagram.com/jasminbhasin/",
    "https://www.instagram.com/kavitakaksha/",
    "https://www.instagram.com/khushboo.kapoor/",
    "https://www.instagram.com/kritisanon/",
    "https://www.instagram.com/kushakapila/",
    "https://www.instagram.com/malvikasitlani/",
    "https://www.instagram.com/mohenakumari/",
    "https://www.instagram.com/mostlysane/",
    "https://www.instagram.com/neethuchandran/",
    "https://www.instagram.com/pinkvilla/",
    "https://www.instagram.com/priyankachopra/",
    "https://www.instagram.com/rashikapoor/",
    "https://www.instagram.com/sakshisindwani/",
    "https://www.instagram.com/shilpashetty/",
    "https://www.instagram.com/sonamkapoor/",
    "https://www.instagram.com/the_sound_blaze/",
    "https://www.instagram.com/vogueindia/",
    "https://www.instagram.com/ashmitpatil/",
    "https://www.instagram.com/deepikapadukone/",
    "https://www.instagram.com/foodie_nation/",
    "https://www.instagram.com/gaurikhan/",
    "https://www.instagram.com/hellyshahofficial/",
    "https://www.instagram.com/imvkohli/",
    "https://www.instagram.com/jasminemalhotra/",
    "https://www.instagram.com/kajalraghwani/",
    "https://www.instagram.com/karanjohar/",
    "https://www.instagram.com/kritisangeethaanand/",
    "https://www.instagram.com/malavikaarora/",
    "https://www.instagram.com/missmalini/",
    "https://www.instagram.com/nehadhupia/",
    "https://www.instagram.com/officialneelamkothari/",
    "https://www.instagram.com/priyankaranbutalia/",
    "https://www.instagram.com/saraalikhan95/",
    "https://www.instagram.com/shefalishahofficial/",
    "https://www.instagram.com/shraddhakapoor/",
    "https://www.instagram.com/taruntahlanofficial/",
    "https://www.instagram.com/urvashirajbhansali/",
    "https://www.instagram.com/anniecruz/",
    "https://www.instagram.com/charmanestar/",
    "https://www.instagram.com/verucajames/",
    "https://www.instagram.com/lela_star_official1/",
    "https://www.instagram.com/thejessejane/",
    "https://www.instagram.com/evilaiden/",
    "https://www.instagram.com/toriblackofficial_/",
    "https://www.instagram.com/vepyrod/",
    "https://www.instagram.com/jennahaze/",
    "https://www.instagram.com/jessicadrake/",
    "https://www.instagram.com/stoya/",
    "https://www.instagram.com/lupefuentes/",
    "https://www.instagram.com/ms.avaaddam/",
    "https://www.instagram.com/1daisymarie/",
    "https://www.instagram.com/dillionharperexclusive_com/",
    "https://www.instagram.com/omgitslexi/",
    "https://www.instagram.com/official_hitomitanaka/",
    "https://www.instagram.com/nikkidelano/",
    "https://www.instagram.com/realnicoleaniston/",
    "https://www.instagram.com/romirain/",
    "https://www.instagram.com/christymack/",
    "https://www.instagram.com/thereallisaann/",
    "https://www.instagram.com/alettaoceanofficial1/",
    "https://www.instagram.com/whitegirlpoliticking/",
    "https://www.instagram.com/cheriedevillex/",
    "https://www.instagram.com/gianna/",
    "https://www.instagram.com/akadanidaniels/",
    "https://www.instagram.com/kendralust/",
    "https://www.instagram.com/miamalkova/",
    "https://www.instagram.com/sophiedee/",
    "https://www.instagram.com/lanarhoades/"
]


# Path to the chromedriver executable
chromedriver_path = "C:\chromedriver_win32"

# Instagram login credentials
username = "secy_chatys"
password = "Instagram11@22"

# Create a ChromeDriver service
service = Service(chromedriver_path)

# Create a new Chrome browser instance
driver = webdriver.Chrome(service=service)

# Open Instagram website
driver.get("https://www.instagram.com")

# Wait for the page to load
time.sleep(2)

# Find the username and password fields and enter your login credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load after login
time.sleep(4)

# Iterate over each profile link and view the profiles
for profile_link in profile_links:
    driver.get(profile_link)
    time.sleep(4)
    # Add your desired actions here (e.g., scraping profile information)

    # Move to the next profile link

# Close the browser
driver.quit()
