from urllib import request
import re

class Spider_content(object):

    url = 'http://www.pesmaster.com/l-messi/pes-2019/player/2104663/'
    
    info_column_pattern = '<div class="player-info-column-1">([\s\S]*?)</div>'
    position_pattern = '<div class="player-info-column-2">([\s\S]*?)</div>'
    main_column_pattern = '<div class="player-main-column">([\s\S]*?)</div>'

    r = request.urlopen(url)
    htmls = r.read()
    htmls = str(htmls, encoding = 'utf-8')

    info_column_htmls =  re.findall(info_column_pattern, htmls)
    position_htmls = re.findall(position_pattern, htmls)
    main_column_htmls =  re.findall(main_column_pattern, htmls)



a = 1