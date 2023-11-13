

# Range:
data=[5, 17, 6, 12, 17, 17, 19, 4, 6, 15, 21, 8]

sorted_data=sorted(data) # this sorts the data in order
print(sorted_data)

# Activity 1: Create function that calculates the range of interger data in a list
# RANGE is subtracting 'lowest' value from 'highest' value
min_value=min(data) 
max_value=max(data)
range=max_value-min_value
print("Range", range)



# Activity 2: Same data create different fuctions that calculate, Mean, Mode & Median values
# MEAN is found by adding all the values up & dividing by the number of values = bascially it gives you the average!
## TO WORK OUT MEAN:
count=len(data) # counts how many numbers/intergers in the list
print(count)

sum=sum(data) # sums the numbers/intergers in list
print(sum)

mean_value=sum/count # this returns the mean value (sum value/number in value)
print(mean_value)

# MODE is the value that appears most often in list
## TO WORK OUT MEAN:
from scipy.stats import mode # scipy has mode function so installed and imported
mode_value=mode(sorted_data) # calculate the mode
print(mode_value) # indicates that the mode dataset, and the number of times it occurs


##MEDIAN is the middle value of the ordered list (data set). If 2 middle values, add them and divide by 2
# this only works because scipy.stats is imported!
n=len(sorted_data) #calulates the median. If n is odd, it directly takes the middle value. If n is even, it calculates the average of the two middle values

if n%2==1:
     median_value=sorted_data[n // 2] #// rounds number down so is 'floor %' - always takes it lower
else:
     middle1=sorted_data[(n//2)-1]
     middle2=sorted_data[n//2]
     median_value=(middle1+middle2)/2
print(median_value)




# Activity 3:
# -  Using those functions calculate the Mean, Mode and Median values of MegaBytes Sales figures
# - Then remove Sunday figures and see how values change?