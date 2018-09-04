import sys
import requests
import urllib3
from bs4 import BeautifulSoup
from pathlib import Path


def download_all_lessons():
    """
    :return: All lesson for all 9 levels of TTMIK :)
    """
    # Start level index
    # Set path to where files will be downloaded to
    # Set Download url parent link
    level = 1
    download_path = Path("/home/hameed/Downloads/TTMIK_Unit_Lessons")
    download_path.mkdir(parents=True, exist_ok=True)
    download_root = "http://traffic.libsyn.com/talktomeinkorean/ttmik-"

    # For the 9 levels available
    for i in range(9):
        # Set the level's path and set lesson to 1
        path = download_path / str(level)
        path.mkdir(parents=True, exist_ok=True)
        lesson_num = 1

        # 30 Lessons in each level
        while lesson_num <= 30:
            # Name of the current lesson
            lesson = 'l'+ str(level) + 'l' + str(lesson_num)

            # Append the download link root to point to current lesson
            # HTTP Get Method with requests
            # Write content to specified file
            mp3_site = download_root + lesson + '.mp3'
            mp3 = requests.get(mp3_site)
            with open((path / str(lesson + '.mp3')), 'wb') as m:
                m.write(mp3.content)

            pdf_site = download_root + lesson + '.pdf'
            pdf = requests.get(pdf_site)
            with open((path / str(lesson + '.pdf')), 'wb') as p:
                p.write(pdf.content)

            lesson_num += 1

        level += 1



    # root_url = "http://talktomeinkorean.com/l1l2.pdf/"
    # source_code = requests.get(root_url)
    # plain_text = source_code.text
    # root_page = BeautifulSoup(plain_text, "html.parser")

    # lessons = root_page.find('div',{'class':'entry-content'})

    # lessons = lessons.findAll('a')
    # while lesson_num <= 30:
    #     source_code = requests.get(root_url)
    #     plain_text = source_code.text
    #     print(len(plain_text))
    #
    #     root_page = BeautifulSoup(plain_text, "html.parser")
    #     # print(root_page.prettify())
    #     for link in root_page.findAll('div',):
    #         # print(link.get('href'))
    #         print(link.p)
    #
    #     lesson_num += 1
    #     print(lesson_num)


download_all_lessons()