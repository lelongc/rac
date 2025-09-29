# # -*- coding: utf-8 -*-
# """
# Created on Wed Aug 20 07:17:45 2025

# @author: Lê Thành Long 
# """

# print("résumé".encode("utf-8"))
# # b'r\xc3\xa9sum\xc3\xa9'
# print("El Niño".encode("utf-8"))
# # b'El Ni\xc3\xb1o'

# print(b"r\xc3\xa9sum\xc3\xa9".decode("utf-8"))
# # 'résumé'
# print(b"El Ni\xc3\xb1o".decode("utf-8"))
# # 'El Niño'


# # chuyển mã hex sang binary 
# print(" ".join(f"{i:08b}" for i in (0xc3, 0xb1)))
# # '11000011 10110001'


# import locale
# #  locale.getpreferredencoding()
# 'utf-8'

# #  all(len(chr(i).encode("ascii")) == 1 for i in range(128))
# # True

# ibrow = "🤨"
# len(ibrow)

# ibrow.encode("utf-8")

# len(ibrow.encode("utf-8"))


# # Calling list() on a bytes object gives you
# # the decimal value for each byte
list(b'\xf0\x9f\xa4\xa8')

#  letters = "αβγδ"
#  rawdata = letters.encode("utf-8")
#  print(rawdata)
#  print( rawdata.decode("utf-8"))
# # 'αβγδ'
# print (rawdata.decode("utf-16")  )# 😧
# # '뇎닎돎듎'


# text = "記者 鄭啟源 羅智堅"
# print(len(text.encode("utf-8")))

# print(len(text.encode("utf-16")))

# s1="ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH"
# s2='Khoa Công nghệ thông tin'
# s1_encoded = s1.encode('utf-8')
# s2_encoded = s2.encode('utf-8')
# print(s1_encoded)
# print(s2_encoded)



# s1=b'Vi\xe1\xbb\x87t Nam m\xe1\xba\xbfn y\xc3\xaau' ; 
# s2= b'ng\xc6\xb0\xe1\xbb\x9di Vi\xe1\xbb\x87t d\xc3\xb9ng h\xc3\xa0ng Vi\xe1\xbb\x87t'
# # a)Viết lệnh giải mã chuỗi s1 và s2 và cho biết kết quả.
# s1_decoded = s1.decode('utf-8')
# s2_decoded = s2.decode('utf-8')
# print(s1_decoded)
# print(s2_decoded)

# print(len(s1))
# print(len(s2))

# print(list(s1))
# print(list(s2))



text = "記者 鄭啟源 羅智堅"
text_encoded = text.encode('utf-8')
print(text_encoded)

print(len(text))
print(len(text.encode('utf-8')))
