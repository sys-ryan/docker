import os, sys
  
def read_files(fname1, fname2, fname3):
        f1 = open(fname1, 'r')
        line1 = f1.readline()

        f2 = open(fname2, 'r')
        line2 = f2.readline()

        f3 = open(fname3, 'r')
        line3 = f3.readline()

        f1.close()
        f2.close()
        f3.close()

        return (str(line1), str(line2), str(line3))

def result(line1, line2, line3):
        line1 = line1.split('/')
        line2 = line2.split('/')
        line3 = line3.split('/')

        file_number1 = int(line1[0])
        file_number2 = int(line2[0])
        file_number3 = int(line3[0])

        file_size1 = int(line1[1])
        file_size2 = int(line2[1])
        file_size3 = int(line3[1])

        #File Number Aging
        installed = file_number2 - file_number1
        not_deleted = file_number3 - file_number1

        installed *= 1.0
        not_deleted *= 1.0

        file_num_aging = (not_deleted / installed) * 100


        #File Size Aging
        installed_sz = file_size2 - file_size1
        not_deleted_sz = file_size3 - file_size1

        installed_sz *= 1.0
        not_deleted_sz *= 1.0

        file_sz_aging = (not_deleted_sz / installed_sz) * 100
 
        msg1 = 'The number of installed files : ' + str(installed)
        msg2 = 'The number of not deleted files : ' + str(not_deleted)
        msg3 = 'File Number Aging : ' + str(file_num_aging)
        msg4 = 'File Size Aging : ' + str(file_sz_aging)

        print(msg1)
        print(msg2)
        print(msg3)
        print(msg4)

        f = open('./aging_evaluation_result', 'w')
        f.write(msg1 + '\n')
        f.write(msg2 + '\n')
        f.write(msg3 + '\n')
        f.write(msg4 + '\n')
        f.close()
        

def main():
        fname1 = str(sys.argv[1])
        fname2 = str(sys.argv[2])
        fname3 = str(sys.argv[3])

        line1, line2, line3 = read_files(fname1, fname2, fname3)

        result(line1, line2, line3)

if __name__ == "__main__":
        main()
