from urllib import request


def find_novel(url):
    with request.urlopen(url) as f:
        data = f.read()
        content = data.decode('utf-8')

        '<a href="/0_142/8773791.html">下一章</a>'

        next_page_start = content.index('下一章') - len('<a href="/0_142/8773791.html">')
        next_link_start = content.index('"', next_page_start) + 1
        next_link_end = content.index('"', next_link_start)
        next_link = content[next_link_start:next_link_end]
        next_url = 'http://www.xxbiquge.com' + next_link


        title_start_str = '<h1>'
        title_end_str = '</h1>'

        title_start_pos = content.index(title_start_str)
        title_end_pos = content.index(title_end_str, title_start_pos)

        title = '\n' + content[title_start_pos + len(title_start_str):title_end_pos] + '\n\n'

        start_str = '<div id="content">'
        end_str = '</div>'

        start_pos = content.index(start_str)
        # print(startPos)
        end_pos = content.index(end_str, start_pos+18)
        # print(endPos)

        novel = content[start_pos+len(start_str):end_pos]
        novel = novel.replace('<br /><br />', '\n')
        novel = novel.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '    ')

        return title + novel + '\n', next_url


temp_url = 'http://www.xxbiquge.com/0_142/8773465.html'
temp_novel = find_novel(url=temp_url)
# print(temp_novel[0])
print(temp_novel[1])
