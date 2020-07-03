# command_line
collect on tools to start using command line arguments

# Burndown
Creates burndown graph and table assuming constant rate of burndown over the days passed until to do effort is meet.

burn(date1=sys.argv[2],date2=sys.argv[3], est=sys.argv[4], toDo=sys.argv[5]) # python burndown_test.py burn <date1> <date2> <est> <todo> 
example:
python burndown_test.py burn 20200505 20200630 40 15 # Graph will not be correct if today() falls outside this time box

# Compare
Compare two ASCII or HDF5 files (using h5diff).

if len(sys.argv) == 4:
        compare(file1=sys.argv[2],file2=sys.argv[3]) #python compare_test.py compare <file1> <file2> 
    # compare(file1=sys.argv[2],file2=sys.argv[3], x=int(sys.argv[4])) #python compare_test.py compare <file1> <file2> <x>
    if len(sys.argv) == 3:
        report(location=sys.argv[2])
