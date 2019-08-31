import os
import sys
import ftplib

class myFtp:
    ftp = ftplib.FTP()
    
    def __init__(self, host, port=9000):
        self.ftp.connect(host,port)

    def Login(self, user, passwd):
        self.ftp.login(user, passwd)
        print('welcom: %s' % self.ftp.welcome)

    def checkFileDir(self, file_name):
        ret = ''
        try:
            ret = self.ftp.cwd(file_name)
            self.ftp.cwd('..')
        except ftplib.error_perm as fe:
            ret = fe
        finally:
            #print('checkFileDir finally ret= %s' % ret)
            if 'Error' in str(ret):
                return 'File'
            elif 'successful' in str(ret):
                return 'Dir'
            else:
                return 'Unknow'

    def DownloadFile(self, LocalFile, RemoteFile):
        file_handle = open(LocalFile, 'wb')
        #print('handle %s' % file_handle)
        #self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write)#接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR '+ RemoteFile, file_handle.write)
        file_handle.close()
        return True

    def DownloadFileTree(self, LocalDir, RemoteDir):
        print('RemoteDir %s' % RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        print('RemoteNames:%s' % RemoteNames)
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            print('Local = %s' % Local)
            print('file: %s' % self.ftp.nlst(file))

            #if file.find('.') == -1:
            if self.checkFileDir(file) == 'Dir':
                if not os.path.exists(Local):
                    os.makedirs(Local)
                self.DownloadFileTree(Local, file)
            else:
                self.DownloadFile(Local,file)

        self.ftp.cwd('..')
        return

    def close(self):
        self.ftp.quit()


if __name__ == "__main__":
    ftp = myFtp('201.234.3.1', 21)
    ftp.Login('root', '#48Va2#LY@R46JKx')
    ftp.DownloadFileTree('./laserbox_log', '/log')
    #ftp.DownloadFile('./laserbox_log/last.gcode', '/var/last.gcode')
    #ftp.DownloadFile('./upgrade.log.1970-01-01_00:00:08', '/log/upgrade.log.1970-01-01_00:00:08')
    #a = ftp.checkFileDir('/log/test')
    #print(a)
    ftp.close()
    print('OK!')
