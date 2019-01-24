# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)


srch_list = ['박근혜', '朴', '이명박', ',前', '김대중', '문재인', '文', '대통령', '홍준표', '트럼프', '김정은', '노무현']
title = "<h2><a href='http://theimpeter.com/24220/'>‘세종시 수정안 부결’ 과 의 원칙론</a></h2>"
content = "[caption]국회본회의 표결 안상수와 전대표 세종시 수정안중 행복도시 특별법안이 국회에서 찬성 105·반대 164로 부결되었다.[/ca] 이 결과는 당연하면서도 정말 어이없다고 말할 수 밖에 없는 사건이다.  원칙을 지키지 않는..."


text = content.split("[/caption]").__len__()

print(text)

valid = True

tt = next((s for s in srch_list if s in content), None)
ss = next((s for s in srch_list if s in title), None)
print(ss)

if not next((s for s in srch_list if s in content), None) and not next((s for s in srch_list if s in title), None):
    valid = False


print(valid)

