import html
import prettytable as pt
url = 'https://www.baidu.com' # link to point to
pt.add_row(['2018-10-10','' + url + ''])
text = pt.get_html_string(format=True)
text = html.unescape(text) 