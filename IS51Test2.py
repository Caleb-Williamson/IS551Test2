#calculate_percent_above_average function
def calculate_percent_above_average(ll,avg):
        cnt=0
        for a in ll:
                if(a>avg):
                        cnt+=1
        return ((cnt/len(ll))*100)

#main function

if __name__ == "__main__":
        #opening python file
        #Here file name is abc.py you can change it 
        #as per your file name
        f = open("Final.txt", "r")
        #spliting element by enter
        l=f.read().split("\n")
        ll = []
        for a in l:
                if(a!=''):
                        ll.append(int(a))
        #ll is list of integers
        #printing number of grades
        print("Number of grades : ",len(ll))

        #lets calculate average grade
        avg=0
        for a in ll:
                avg+=a
        avg=avg/len(ll)
        print("Average of grades : ",avg)
        print("Percentage of grades above average: ",calculate_percent_above_average(ll,avg),"%")