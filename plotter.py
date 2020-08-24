import matplotlib.pyplot as plt
import os

def csv_parser(filepath):
    with open(filepath, 'r') as tf:
        lines = list(tf)
        while "\n" in lines:
            lines.remove("\n")
        firstword = lines[0].split(',')
        secondword = lines[1].split(',')
        numeric = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+', 'e', 'E'}
        while set(firstword[0]).issubset(numeric) == False:
            if set(secondword[0]).issubset(numeric) == True:
                break
            else:
                lines.pop(0)
                firstword = secondword
                secondword = lines[1].split(',')

        labels = firstword
        labels[-1] = labels[-1][:-1]
        lines.pop(0)
        time = []
        values = [[] for x in range(1, len(labels))]
        for line in lines[:-1]:
            words = line.replace(',', ' ').split()
            if len(words) >= 2:
                words[-1].replace('\n', '')
                time.append(float(words[0]))
                for i in range(1, len(words)):
                    values[i-1].append(float(words[i]))
                    
    return time, values, labels                    
                                       

filepath = "hola"
while os.path.exists(filepath) == False:
	filepath = input("Input valid file path: ")

try:
    time, values, labels = csv_parser(filepath)
    
    print(labels)
    
    fig = plt.figure(figsize=(10,5))
    
    for i in range(len(values)):
    	plt.plot(time, values[i], label=labels[i+1])
    
    plt.grid()
    plt.xlabel(labels[0])
    plt.legend()
    plt.tight_layout()
    plt.show()
except:
    print("Critical Error!")