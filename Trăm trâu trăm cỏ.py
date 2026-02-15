"""Lập trình giải bài toán dân gian TRĂM TRÂU TRĂM CỎ:
"Trâu đứng ăn năm
Trâu nằm ăn ba
Lụ khụ trâu già
Ba con một bó
Trăm con ăn cỏ
Trăm bó no nê.
Hỏi có bao nhiêu trâu đứng, trâu nằm, trâu già?"""
for traudung in range(0, 101):
    for traunam in range(0, 101 - traudung):
        traugia = 100 - traudung - traunam
        if (traudung * 5 + traunam * 3 + traugia * 1 == 100) and (traugia % 3 == 0):
            print("Trâu đứng:", traudung, "Trâu nằm:", traunam, "Trâu già:", traugia)