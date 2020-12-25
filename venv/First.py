from selenium import webdriver

class Music:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\adabral\\Downloads\\chromedriver_win32\\chromedriver")
        self.driver.maximize_window()

    def play(self):
        #name = imput("Enter the name of your youtube channel")

        self.driver.get("https://www.youtube.com/watch?v=7M-jsjLB20Y")
        self.driver.find_element_by_xpath(self,"""//*[@id="movie_player"]/div[30]/div[2]/div[1]/button""")

bot = Music()
bot.play()