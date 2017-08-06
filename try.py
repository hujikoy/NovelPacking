import novelspider

start_index_1 = 1006272
end_index_1 = 1007299

start_index_2 = 8742328
end_index_2 = 8884200

for i in range(8760931, end_index_2+1):
    try:
        novel = novelspider.find_novel('http://www.xxbiquge.com/0_142/' + str(i) + '.html')
        with open('novel.txt', 'a') as novel_file:
            novel_file.write(novel)
    except Exception as e:
        er = e
        # print('i = ' + str(i))

