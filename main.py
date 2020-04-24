from os import walk, path, system
import socket


files_list = []
dir_list = []
sock = None
data = ''

def discovery(initial_path):
    
    global dir_list, files_list

    for dirpath, dirs, files in walk(initial_path):
        
        for _file in files:
            
            absolute_path = path.abspath(path.join(dirpath, _file)) 
            
            if dirpath not in dir_list: 
                dir_list.append(dirpath)
            
            files_list.append(absolute_path)

    
    
    return True



def dir_tree(init_path):

    global dir_list, files_listm, data, sock 

    for it in data:
        sock.send(it)
        tmp = ''
        
        while '[root@GX662:' not in tmp:
            tmp += sock.recv(1024)
        
        if 'directory' in tmp: dir_list.append(it)
        else: files_list.append(it)

    for _dir in dir_list:
        _path = init_path+_dir
        system('mkdir '+_path)



    return True



def connection(ip='10.0.1.7',port='23'):
    global sock

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))


def get_file(save_locate):
    global files_list, sock

    for _file in files_list:
        data = ''
        sock.send('base64 '+_file.encode())
        
        while '[root@GX662:' not in data: 
            data += sock.recv(1024).decode()
        
        tmp = 'echo '+data+' | base64 -d '+save_locate+_file
        system(tmp)
    
    return True


def main():
    global sock, data 

    save_locate = '' #onde sera salvo a arvore de arquivos 
   

if __name__ == "__main__":
    main()
