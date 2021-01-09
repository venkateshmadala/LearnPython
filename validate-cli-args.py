#import sys module
import sys
#print number of cli args
print(len(sys.argv))
#validate cli args
if len(sys.argv) < 4:
    print("you have entered invalid number, Please enter valid values")
elif len(sys.argv) > 8:
    print("too many arguments to handle")
else:
    print("valid input cli args got shared, proceeding further")