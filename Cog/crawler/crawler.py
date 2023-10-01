from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_cpbl_now():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver =  webdriver.Chrome(options=chrome_options)

    team_name_dict = {
        '/team/index?teamNo=AJL011':'樂天桃猿',
        '/team/index?teamNo=ACN011':'中信兄弟',
        '/team/index?teamNo=ADD011':'統一獅',
        '/team/index?teamNo=AEO011':'富邦悍將',
        '/team/index?teamNo=AAA011':'味全龍'
        
    }
    game_status_dict = {}
    game_live = []
    game_end = []
    game_wait = []

    
    driver.get("http://cpbl.com.tw/")
    page_source = driver.page_source
    # 關閉WebDriver
    driver.quit()
    
    # 使用BeautifulSoup解析HTML內容
    soup = BeautifulSoup(page_source, 'html.parser')
    game_end_list = soup.find('div', {'class': 'IndexScheduleList major'}).find_all('div', {'class': 'game_item final'})
    if game_end_list:
        for game in game_end_list:
            box = game.find('div', {'class': 'VSBox'})
            away_team_name = box.find('div',{'class':'team away'}).find('div',{'class':'team_name'}).text
            away_team_score = box.find('div',{'class':'score'}).find('div',{'class':'num away'}).text
            home_team_name = box.find('div',{'class':'team home'}).find('div',{'class':'team_name'}).text
            home_team_score = box.find('div',{'class':'score'}).find('div',{'class':'num home'}).text
            game_end.append("{} {} : {} {}".format(away_team_name, away_team_score, home_team_score, home_team_name))
    game_status_dict['game_end'] = game_end 
        

    # game_wait_list = soup.find('div', {'class': 'IndexScheduleList major'}).select('div.game_item:not([class*=" "])')
    # if game_wait_list:
    #     for game in game_wait_list:
    #         box = game.find('div', {'class': 'VSBox'})
    #         away_team_href = box.find('div',{'class':'team away'}).find('div',{'class':'team_name'}).a['href']
    #         away_team_name = team_name_dict[away_team_href]
    #         home_team_href = box.find('div',{'class':'team home'}).find('div',{'class':'team_name'}).a['href']
    #         home_team_name = team_name_dict[home_team_href]
    #         game_wait.append("{} : {}".format(away_team_name,  home_team_name))
    # game_status_dict['game_wait'] = game_wait 

    game_live_list = soup.find('div', {'class': 'IndexScheduleList major'}).find_all('div', {'class': 'game_item live'})
    if game_live_list:
        for game in game_live_list:
            box = game.find('div', {'class': 'VSBox'})
            away_team_name = box.find('div',{'class':'team away'}).find('div',{'class':'team_name'}).text
            away_team_score = box.find('div',{'class':'score'}).find('div',{'class':'num away'}).text
            home_team_name = box.find('div',{'class':'team home'}).find('div',{'class':'team_name'}).text
            home_team_score = box.find('div',{'class':'score'}).find('div',{'class':'num home'}).text
            game_live.append("{} {} : {} {}".format(away_team_name, away_team_score, home_team_score, home_team_name))
    game_status_dict['game_live'] = game_live 

    if not game_live_list and not game_end_list:
        game_wait_list = soup.find('div', {'class': 'IndexScheduleList major'}).find_all('div', {'class': 'game_item live'})
        if game_wait_list:
            for game in game_wait_list:
                box = game.find('div', {'class': 'VSBox'})
                away_team_href = box.find('div',{'class':'team away'}).find('div',                        {'class':'team_name'}).a['href']
                away_team_name = team_name_dict[away_team_href]
                home_team_href = box.find('div',{'class':'team home'}).find('div',                        {'class':'team_name'}).a['href']
                home_team_name = team_name_dict[home_team_href]
                game_wait.append("{} : {}".format(away_team_name,  home_team_name))
    game_status_dict['game_wait'] = game_wait 
    
    return game_status_dict
    