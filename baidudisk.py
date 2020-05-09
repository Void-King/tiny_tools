from bypy import ByPy
# 获取一个bypy对象，封装了所有百度云文件操作的方法
bp = ByPy()
# 百度网盘创建文件夹
# bp.mkdir(remotepath = 'Cost')
#上传文件至文件夹
# upload中参数代表复制文件，默认值为'overwrite'，指定'newcopy'不会覆盖重复文件
# bp.upload(localpath= r'cost.ini', ondup='overwrite --rapid-upload-only')
# print('上传完成！！')
bp.download(localpath = r'./')
print('下载完成！！')