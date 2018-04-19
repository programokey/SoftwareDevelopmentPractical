from urllib import parse, request
if __name__ == '__main__':
    import base64
    f = open('2333.jpg','rb')
    file_data = f.read()
    f.close()
    file_data = base64.b64encode(file_data).decode('utf-8')
    data = {
        'token':'12345677',
        'path':'/media_file/pictures/2333.jpg',
        'data':file_data
    }
    data = parse.urlencode(data).encode(encoding='utf-8')
    web_site = 'http://localhost:5000'
    upload_request = request.Request(url='%s/api/upload'%web_site, data=data, method='POST')
    upload_request = request.urlopen(upload_request)
    print(upload_request.read())

'''
'token': 用于身份验证，必须为'12345677'
'path':  文件路径，必须和数据库中的文件路径相同，
        格式为：
            图片： /media_file/pictures/<文件名>
            视频： /media_file/videos/<文件名>
'data':
    使用base64对二进制文件进行编码后发送
'''