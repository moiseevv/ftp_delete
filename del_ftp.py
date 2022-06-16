import ftplib,os
import codecs

def delete_serv(serv):
    ftp = ftplib.FTP(serv)
    ftp.login('***', '***')
    list_files = ftp.nlst()
    
    
    for filename in list_files:
        if '.xlsx' in filename:
            print('Удаление файла - ', filename)
            try:
                ftpResponse = ftp.delete(filename)
                print(ftpResponse)
            except ftplib.error_perm:
                print('!!! Произошла ОШИБКА ')
    ftp.quit()
    
if __name__ == '__main__':
    mas_comp = ['192.168.***.**','192.168.***.**','192.168.***.**','192.168.***.**']
    
    for serv in mas_comp:
        delete_serv(serv)
