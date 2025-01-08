import statistics

FOLDER = 'swimdata/'
"""Module providing a function printing python version."""
def read_swim_data(filename):
# task1- Breaking the filename
    swimmer,age,distance,stroke=filename.removesuffix('.txt').split('-')

#Task2- Fetch the data from file
    # Get the details from file and break it into list
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times= lines[0].strip().split(',')

    # To get the average of time convert the string values from earlier list and convert it to int and process to hundredths.
    converts = []
    for t in times:
        if ":" in t:
            minutes, rest = t.split(':')
            seconds, hundredths = rest.split('.')
        else:
            minutes=0
            seconds, hundredths = t.split('.')
        converts.append((int(minutes)*60*100) + (int(seconds)*100) + int(hundredths))
      

    # Once all the string values are converted, check the mean by below method. 
    average = statistics.mean(converts)

    # Revert it back to original format.
    mins_secs, hundredths = str(round(average/100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = (mins_secs//60)
    seconds = mins_secs - minutes*60

    average = f"{minutes} ':' {seconds} '.' {hundredths}"
    return swimmer,age,distance,stroke,times,average,converts
