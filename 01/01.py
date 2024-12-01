import numpy as np
import pandas as pd

def read():
    df = pd.read_csv("01/01.txt", sep="\\s+", header=None)
    return df[[0]], df[[1]]

def main():
    # Part 1
    left_list, right_list = read()
    left_list.columns = right_list.columns = ["Locations"]
    left_list = left_list.sort_values(by="Locations").reset_index(drop=True)
    right_list = right_list.sort_values(by="Locations").reset_index(drop=True)
    distances = np.abs(right_list - left_list)
    print(f"Total distance: {distances["Locations"].sum()}")

    # Part 2
    occurances = right_list.groupby(["Locations"]).size() 

    def find_occurances(x):
        if x in occurances.keys():
            return occurances[x]
        else:
            return 0
        
    similarity_sum = 0
    for i in range(left_list.size):
        l = left_list["Locations"].iloc[i]
        score = l * find_occurances(l)
        similarity_sum += score
    
    print(f"Total similarity: {similarity_sum}")



if __name__ == "__main__":
    main()