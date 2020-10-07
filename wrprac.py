# 파일 쓰기
# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
# for i in [1,2,3,4,5]:
#     f.write(f"{i}번째 줄이에요\n")
# f.close()

from wordcloud import WordCloud
from PIL import Image
import numpy as np

# 파일 읽기
text = ''
with open("lucky.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('샵검색','').replace('와우','').replace('지금','').replace('아니','').replace('그래','').replace('응응','').replace('내가','').replace('다들','').replace('그냥','').replace('너무','').replace('나는','').replace('이제','').replace('오늘','').replace('진짜','').replace('근데','').replace('나도','').replace('맞아','').replace('ㅋ','').replace('ㅠ','').replace('이모티콘\n','').replace('사진\n','').replace('ㅎ','')

# print(text)

# 마스킹된 부분으로 자르는 코드

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path="C:/Windows/Fonts/malgunbd.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")


# # 이용가능한 글꼴 path 보기
# import matplotlib.font_manager as fm
# #
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)