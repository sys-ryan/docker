
import docker, subprocess, sys
import os, json
import time

def checkDockerContainerStatus(name):
    client = docker.from_env()
    container_list=(client.containers())

    for con_data in container_list:
        if str(con_data['Names']).find(name)==3:
            return (con_data['Id'])
    return False

# Dummy
exceptFile = ["$Recycle.Bin",]
def DummyCheck():
    root_dir = "/"
    count = 0
    dir_c = 0
    fileNumber = 0

    f = open("FileInSystem.txt",'w')

    for (root, dirs, files) in os.walk(root_dir):
        #print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                dir_c += 1

                f.write(dir_name+"\n")

        if len(files) > 0:
            for file_name in files:
                #print("file: " + file_name)
                f.write("   "+file_name+"\n")
                fileNumber+=1

        # if count % 10000 == 0:
            # print("Processing."+ ('.'*int(count/10000)))

        count += 1
    f.close()
    return str(fileNumber) 
    
def get_status(container_name, container_id):
    data=subprocess.check_output("docker exec " + container_id + " ps -eo pcpu,rss,cmd --sort -rss | grep " + container_name, shell=True)
    data=(str(data).strip())
    data=str(data).replace("b'", "").replace("'", "").replace("\\n", "")
    data = " ".join(data.split())
    data = data.split(" ")
    total_file_number = DummyCheck()
    return str(data[0]), str(data[1]), str(data[2]), total_file_number

def load_container(container_id):
    with open("/data_set/"+str(container_id)+".json", "r") as json_file:
        json_data = json.load(json_file)
        return json_data

def init_json(container_name, container_id):
    data={}
    data['data']=[]
    cpu_usage, memory_usage, app_name, total_file_number = get_status(container_name, container_id)
    default = {'timestamp': int(time.time()), 'cpu_usage' : cpu_usage, 'memory_usage': memory_usage, 'app_name': container_name, 'total_file_number' : total_file_number}
    data['data'].append(default)
    json_data=data
    with open("/data_set/"+str(container_id)+".json", 'w') as outfile:
        json.dump(json_data, outfile)


def get_json(container_id):
        load_json = (load_container(container_id))

        loop=0
        msg=''
        for data in load_json['data']:
                loop += 1
                msg+="[{0}] - Timestamp : {1}\tCPU Usage : {2} %\tMemory Usage : {3} KB,\tTotal File Number(Aging) : {4}\n".format(data['app_name'],data['timestamp'],data['cpu_usage'],data['memory_usage'],data['total_file_number'])
        return msg

def main():
        try:
                container_name = str(sys.argv[1])
                container_id = checkDockerContainerStatus(container_name)
                if container_id:
                        pass
                else:
                        msg = "Not found"
                        print(msg)

                print("container_name: "+container_name)
                print(container_id)
                init_json(container_name, container_id)
                data = get_json(container_id)
                print(data)
        except:
                print("ERROR")





if __name__ == "__main__":
        main()
