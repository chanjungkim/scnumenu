import requests
from bs4 import BeautifulSoup
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def scraping():
    now = datetime.now()
    file_path = datetime.strftime(now, "./home.jsp")

    url = "http://www.scnu.ac.kr/mbs/dorm/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    menus = soup.select('div.todayMenu_list')
    f = open(file_path, 'w', encoding='utf-8')
    data = "%s" % menus
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = '<!DOCTYPE html>\n<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>'+'\n<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>'+'\n<%@ taglib prefix="spring" uri="http://www.springframework.org/tags"%>'+'\n<html>\n<head>\n<meta charset="utf-8">\n<title>Welcome</title>\n<script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'+'\n<script src = "<%=request.getContextPath()%>/resources/js/menu.js" ></script>'+'\n<link rel = "stylesheet" href = "<%=request.getContextPath()%>/resources/css/menu.css">'+'\n</head>\n<body>'+data+'\n</body>\n</html>'
    # print(data)
    f.write(data)
    f.close()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    print("START!")
    scheduler.add_job(scraping, 'interval', seconds=10, )
    print("END!")

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        print("END!")
        pass
