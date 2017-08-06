import novelspider

temp_url = 'http://www.xxbiquge.com/0_142/8773465.html'

for i in range(1000):
    try:
        novel_tul = novelspider.find_novel(temp_url)
        temp_url = novel_tul[1]
        if temp_url == 'http://www.xxbiquge.com/0_142/':
            break
        with open('novel.txt', 'a') as novel_file:
            novel_file.write(novel_tul[0])
    except Exception as e:
        er = e
        # print('i = ' + str(i))

