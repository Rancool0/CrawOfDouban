


class UrlData():

    def wiret_data(self,file_obj,data,page_url):
        #写文件
            if page_url or data is None:
                return
            file_obj.write(page_url+'\n')
            file_obj.write('name:'+data['name'])
            file_obj.write('info:'+data['info'])
            file_obj.write('detail:'+data['detail']+'\n')
            file_obj.write('score:'+data['score']+'\n'+'\n')

