"""
Ace quiere ser voluntario para viajar a K-Pax, para ello la 
Agencia Espacial Canadiense requiere que llene un
formulario que ayude a obtener más información de él y su 
familia. Tu debes ayudar a Ace creando un programa para 
completar la información solicitada sin sobrescribir e
archivo. Ten presente que los datos con * son los más
importantes, si uno de esos campos no se llena, no podrá ser
admitido, en caso de que el dato solicitado no sea
importante, el programa deberá poner “unknown”.
"""
# loading regex module
import re
# open the file to read the information fields and the file to wirte the information
with open('required_data.txt', 'r') as fi, open('information_file.txt', 'w') as fo:
    #READS THE 'REQUIRED_DATA.txt' FILE
    lines = fi.readlines()
    # SHOWS A MESSAGE
    print("PLEASE, ENTER THE REQUIRED INFORMATION IN EACH FIELD")
    # ITERATES OVER LINES IN FILE
    for line in lines:
        # REGEX PATTERN
        pattern = ":"
        # SEARCHES PATTER IN EACH LINE
        if re.search(pattern, line):
            # ERASES WHITE SPACES IN EACH LINE
            line = line.rstrip()
            # CHECKS IF LINE CONTAINS "MOTHER" STRING
            if "Mother" in line:
                # SHOWS A MESSAGE
                print ("Enter your mother´s information")
                # WRITE THE READ LINE IN THE "information_file.txt"
                fo.write(f"{line}\n")
                # CONTINUES TO THE NEXT LINE
                continue
            # CHECKS IF LINE CONTAINS "fATHER" STRING
            elif "Father" in line:
                # SHOWS A MESSAGE
                print ("Enter your father´s information")
                 # WRITE THE READ LINE IN THE "information_file.txt"
                fo.write(f"{line}\n")
                # CONTINUES TO THE NEXT LINE
                continue
            # CHECKS IF LINE CONTAINS "Brother" STRING
            elif "Brother" in line:
                # SHOWS A MESSAGE
                print ("Enter your Brother´s information")
                # WRITE THE READ LINE IN THE "information_file.txt"
                fo.write(f"{line}\n")
                # CONTINUES TO THE NEXT LINE
                continue
            # CHECKS IF LINE CONTAINS "Sister" STRING
            elif "Sister" in line:
                 # SHOWS A MESSAGE
                print ("Enter your Sister´s information")
                # WRITE THE READ LINE IN THE "information_file.txt"
                fo.write(f"{line}\n")
                # CONTINUES TO THE NEXT LINE
                continue
            # SHOWS THE CURRENT LINE IN LOOP
            print(line)
            # CAPTURES AND SAVE USER'S ENTRY IN entry variable
            entry = input()
            # ADDS AND SAVES THE USER'S ENTRY TO CURRENT LINE
            line = line + f" {entry}\n"
            # WRITES THE MODIFIED LINE IN "information_file.txt"
            fo.write(line)
        # FALSE CONDITION FOR re.search(pattern, line)
        else:
            # WRITES THE LINE IN "information_file.txt"
            fo.write(line)