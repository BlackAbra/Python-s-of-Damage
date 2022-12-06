# try:
#     dosya_read = open('dosya10.txt','r')
#     okudum = dosya_read.read()
#     dosya_read.close()
#     print('deger >>',okudum)
# except Exception as Err:
#         print('hata',Err)


try: 
    print('Reading File No 10')
    dosya_read = open('dosya10.txt','r')
    read_info = dosya_read.read()
    dosya_read.close()
    print(' Readed Info ', read_info)
except Exception as ErrorCatch:
    print('File cannot be readed', ErrorCatch)