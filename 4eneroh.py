# "Regular expressions can be used to search, edit and manipulate text", but the syntax takes time to learn.
# if you dont already know RE, they way you were doing it, str.split()/strip()/... is the best way

# imports code that other people have written, i think the equivavlent in C is "#include ___", idk though i dont know C yet
import re

# create a calendar in a dicitonary, lists are easier to use, but a dictionary is more appropriate in this scenario
# i spread it out over multiple lines to make it easier to understand,

# my code doesn't account for leap years, nor different years (start december, end january), accounting for months is annoying enough
dayspermonth = {"Jan": 31,
                "Feb": 28,
                "Mar": 31,
                "Apr": 30,
                "May": 31,
                "Jun": 30,
                "Jul": 31,
                "Aug": 31,
                "Sep": 30,
                "Oct": 31,
                "Nov": 30,
                "Dec": 31}


def daysToReview(input_string):
    # Section 1: first line of output
    # Regular Expression (RE) that removes whitespace and "/" for this specific string format and puts it into a dictionary
    expression = re.compile(
        r'(\w*)\s(\w*)\s(\w*)\s(\/)\s(\w*)\s(\w*)\s(\w*)\s(\d*)\s(\/)\s(\w*)\s(\w*)\s(\w*)\s(\d*)', re.VERBOSE)
    # runs the RE on the string
    output = expression.match(input_string)
    # if we get a match, the program continues
    if output:
        # prints the first line of output
        print(list(output.groups()))

# Section 2: making it easy to do the second line
        # if make and match another RE because i cant be bothered extracting the relevant info form the first RE, so i just do another
        # ideally i would just get rid of the first output line but i cant do that
        expression1 = re.compile(
            r'\w*\s(\w*\s\w*)\s\/\s\w*\s\w*\s(\w*)\s(\d*)\s\/\s\w*\s\w*\s(\w*)\s(\d*)', re.VERBOSE)
        output1 = expression1.match(input_string)
        # i turn the dictionary into a list. while doing so i make the numbers integers and the words capitalised, as that is what i wrote in the calendar dictionary
        output1 = [int(group) if group.isdigit() else group.capitalize()
                   for group in output1.groups()]

# Section 3: calculating days passed
        # i get the days remaining in the start month subtract them from the total days in the month and then add the days in the ending month given.
        dayspassed = dayspermonth[output1[1]]-output1[2]+output1[4]
        # this is a short and cancerous way of dealing with periods longer than a month.
        # i made it shorter by excluding an if statement that would check if there is months inbetween the given months, by using the for statement to do so.
        # 1. the index of the end month is minused from the start month. giving the amount of months between. the loop iterates that many times minus 1 as it starts at 1 instead of 0
        # this also acts as a contional statement (if statement) and only runs if there is more than 1 month inbetween the months given
        for n in range(1, list(dayspermonth).index(output1[3])-list(dayspermonth).index(output1[1])):
            # since i used a dictionary for the calendar this is longer than it would be if i used a list.
            # it gets the amount of days in each month in between given months and adds them to the counter
            dayspassed += dayspermonth[list(dayspermonth)[list(dayspermonth).index(output1[3])+n+1]]
        # prints out the name and the days passed,
        # i am not a fan of formatting strings using %d/... or "text"+dayspassed+"..." the "f" at the start allows you to put stuff in directly by using "{}", this is great for formatting
        # other things can be done in the "{}" as well, such as arithmetic or calling functions...
        print(f"{output1[0]} completed this review in {dayspassed} days")

# Section 4: unnecessary
    # if someone put in something that doesnt follow the format (spaces and "/" are required) 'word word word / word word word digit / word word word digit'. the RE wont work and nothing would happen
    else:
        # so i show an error message
        print("format your stuff properly")


# Section 5: Good practice
# if you run this program you'll run this program.
# this enables it to not be run when you import it, you should learn about this later, i could "import 4eneroh" into another program and use this function, without the line below it wouldn't work properly
if __name__ == "__main__":
    # there are many ways of getting inputs, you should learn about the 'sys' module later but this is the easiest way.
    # uncommment the line below to try your own inputs,
    # input_string = input("Input here: ") # <----- this line
    # this is used to make testing easier, i dont have to copy and paste this in each time i want to test, i just have to run it.
    input_string = "Reviewer Leslie Norman / Review assigned mar 1 / Review submitted jul 4"
    # calling the function
    daysToReview(input_string)
