import os
import sys
import subprocess
import tkinter
from tkinter import messagebox, filedialog
import csv

def compare(file1, file2, x=3):
    if len(file1) != 0:
        file1 = file1
    else:
        file1 = input('Please input file 1 location: ')
    
    if len(file2) != 0:
        file2 = file2
    else:
        file2 = input('Please input file 2 location: ')    
    
    compareLocation = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'Comparison')
    
    if os.path.exists(compareLocation):
        print ('location available')
        pass
    else:
        os.makedirs(os.path.dirname(file2) + "/" + 'Comparison_Folder')
        os.makedirs(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'Comparison'))
        print ('output folder created') 

#     if os.path.splitext(self.file1)[-1] == '.hdf5':
#         if os.path-splitext(self.file2)[-1] == '.hdf5':
#             out = ('{}_RT'.format (os.path.splitext(os.path.basename(self.file2))[0])) #Create filename of comparison file
#             fileout = ('h5diff -c {} {} >{}/{}.csv'.format(os.path.abspath(file1), os.path.abspath(file2), self.compareLocation, out)) #Set command -c =  , -v = Verbose mode — Print difference information, list of objects, warnings, etc
#             os.system(fileout)
# 			
# 			file = '{}{}.csv'.format(self.compareLocation, out)
# 			input_file = open(file,'r')
# 			reader_file = csv.reader(input_file)
# 			value_file = len(list(reader_file)
# 			
# 			if value_file > x:
#             #print('too many')
#             msg='Would you like to quit the application?\n {}'.format(value_file)
#             choice = QMessageBox.question(None, 'Error limit exceeded',
#                                             msg, QMessageBox.Yes | QMessageBox.No)
#             if choice == QMessageBox.Yes:
#                 return
#                 #pass
#             else:
#                 QMessageBox.information(None, 'Return to RT Suite', 'Regression suite application will continue')
#                 pass
# 		else:
# 		    QMessageBox.information(None, 'Operation cancelled', 'Comparison stopped as file types do not match')
#             return
    # if os.path.splitext(file1)[-1] == '.hdf5':
    #     if os.path.splitext(file2)[-1] == '.hdf5':		
    if file1.endswith('.hdf5'):
        if file2.endswith('.hdf5'):
            out = ('{}_RT'.format (os.path.splitext(os.path.basename(file2))[0])) #Create filename of comparison file
            
            file = '{}/{}.csv'.format(compareLocation, out)
            if os.path.exists(file):
                tkinter.Tk().withdraw()
                msg='Over write report file?'
                MsgBox=messagebox.askyesno(title='File already exists', message=msg)
                if MsgBox == 'yes':
                    return file
                if MsgBox == 'no':
                    # location = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'Comparison')
                    file = filedialog.asksaveasfilename(initialdir = compareLocation, initialfile = "<filename>_RT", title="Select file name", filetypes=(("csv files","*.csv"),("all files", "*.*")),defaultextension=".csv")
            
            fileout = ('h5diff -c {} {} >{}'.format(os.path.abspath(file1), os.path.abspath(file2), file)) #Set command -c =  , -v = Verbose mode — Print difference information, list of objects, warnings, etc
            os.system(fileout)
            
            input_file = open(file,'r')
            reader_file = csv.reader(input_file)
            value_file = len(list(reader_file))
            
            if value_file > x:
                tkinter.Tk().withdraw()
                msg='Would you like to quit the application?\n {}'.format(value_file)
                MsgBox=messagebox.askyesno(title='Error limit exceeded', message=msg)
                if MsgBox == 'yes':
                    return
                else:
                    tkinter.Tk().withdraw()
                    tkinter.messagebox.showinfo('Return to RT Suite', 'Regression suite application will continue')
                #print('too many')
                    pass
        else:       
            tkinter.Tk().withdraw()
            messagebox.showinfo('Operation cancelled', 'Comparison stopped as file types do not match')
            return
			
# 	elif os.path.splitext(self.file1)[-1] == '.csv' or '.ads':
# 	    if os.path-splitext(self.file2)[-1] == '.csv' or '.ads':
# 		    with open ((os.path.abspath(self.file1)), 'r') as t1, open ((os.path.abspath(self.file2)), 'r') as t2:
#                 fileone = t1.readlines()
#                 filetwo = t2.readlines()
# 			
# 			fileout = ('{}/{}_RT.csv'.format(self.compareLocation, os.path.splitext(os.path.basename(self.file2))[0])) #Set compare file location and filename
#
# 			with open (fileout,'w') as outFile: #Run comparison of ASCII files
# 			    for line in filetwo:
# 				    if line not in fileone:
# 					    outFile.write(line)
# 			
# 			input_file = open(file,'r')
# 			reader_file = csv.reader(input_file)
# 			value_file = len(list(reader_file))
#
#             if value > x:
#                 #print('too many')
#                 msg='Would you like to quit the application?\n {}'.format(value)
#                 choice = QMessageBox.question(None, 'Error limit exceeded', msg, QMessageBox.Yes | QMessageBox.No)
#                 if choice == QMessageBox.Yes:
#                     return
#                     #pass
#                 else:
#                     QMessageBox.information(None, 'Return to RT Suite', 'Regression suite application will continue')
#                     pass
				
    elif file1.endswith(('.csv', '.ads')):
        if file2.endswith(('.csv', '.ads')):
            with open ((os.path.abspath(file1)), 'r') as t1, open ((os.path.abspath(file2)), 'r') as t2:
                fileone = t1.readlines()
                filetwo = t2.readlines()
			
            fileout = ('{}/{}_RT.csv'.format(compareLocation, os.path.splitext(os.path.basename(file2))[0])) #Set compare file location and filename
            if os.path.exists(fileout):
                tkinter.Tk().withdraw()
                msg='Over write report file?'
                MsgBox=messagebox.askyesno(title='File already exists', message=msg)
                if MsgBox == 'yes':
                    return fileout
                if MsgBox == 'no':
                    # location = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'Comparison')
                    fileout = filedialog.asksaveasfilename(initialdir = compareLocation, initialfile = "<filename>_RT", title="Select file name", filetypes=(("csv files","*.csv"),("all files", "*.*")),defaultextension=".csv")

            with open (fileout,'w') as outFile: #Run comparison of ASCII files
                for line in filetwo:
                    if line not in fileone:
                        outFile.write(line)
			
            input_file = open(fileout,'r')
            reader_file = csv.reader(input_file)
            value_file = len(list(reader_file))

            if value_file > x:
                tkinter.Tk().withdraw()
                msg='Would you like to quit the application?\n {}'.format(value_file)
                MsgBox=messagebox.askyesno(title='Error limit exceeded', message=msg)
                if MsgBox == 'yes':
                    return
                if MsgBox == 'nos':
                    tkinter.Tk().withdraw()
                    tkinter.messagebox.showinfo('Return to RT Suite', 'Regression suite application will continue')
                #print('too many')
                    pass
        else:    
            tkinter.Tk().withdraw()
            messagebox.showinfo('Operation cancelled', 'Comparison stopped as file types do not match')
            return
				
# 	elif os.path.splitext(self.file1)[-1] == '.ads':
# 	    if os.path-splitext(self.file2)[-1] == '.ads':
# 		    with open ((os.path.abspath(self.file1)), 'r') as t1, open ((os.path.abspath(self.file2)), 'r') as t2:
#                 fileone = t1.readlines()
#                 filetwo = t2.readlines()
# 			
# 			fileout = ('{}/{}_RT.csv'.format(self.compareLocation, os.path.splitext(os.path.basename(self.file2))[0])) #Set compare file location and filename
#
# 			with open (fileout,'w') as outFile: #Run comparison of ASCII files
# 			    for line in filetwo:
# 				    if line not in fileone:
# 					    outFile.write(line)
# 			
# 			input_file = open(file,'r')
# 			reader_file = csv.reader(input_file)
# 			value_file = len(list(reader_file))
#
#             if value > x:
#                 #print('too many')
#                 msg='Would you like to quit the application?\n {}'.format(value)
#                 choice = QMessageBox.question(None, 'Error limit exceeded', msg, QMessageBox.Yes | QMessageBox.No)
#                 if choice == QMessageBox.Yes:
#                     return
#                     #pass
#                 else:
#                     QMessageBox.information(None, 'Return to RT Suite', 'Regression suite application will continue')
#                     pass

    else:
        tkinter.Tk().withdraw()
        messagebox.showinfo('Operation cancelled', 'Comparison stopped as file types do not match')
        return

# @classmethod
# def report(cls, location):
#     reportList = []
#     store = []
    
#     reportDirectory = location
    
#     for file in os.listdir(reportDirectory):
#         if file.endswith('*_RT.csv'):
#             reportList.append(os.path.join(reportDirectory, file))
    
#     outFile = '{}/report.txt'.format(os.path.abspath(location))
    
#     N = 5
#     for item in reportList:
#         with open(item) as f:
#             head = [next(f, '') for x in range(N)]
#             layout = (('{} \n *len(head)').format(*head))
#             store.append('File checked: {} \n Error report: (first 5 lines) \n {}'.format(os.path.abspath(item), layout))   #Load report to list QU: How to print headers as bold text?
    
#     with open(outFile,'w') as f:
#         for item in store:
#             f.write('\n {}\n'.format(item))
    
#     if os.name == 'nt': #print report to screen
#         file_out = ('start notepad.exe {}'.format(outFile))
#         os.system(file_out)
#     else:
#         subprocess.call(['nedit',outFile])

def report(location):
    reportList = []
    store = []
    print (location)
    if len(location) != 0:
        reportDirectory = location
    else:
        reportDirectory = input('Please input report location: ')
    # reportDirectory = location
    
    for file in os.listdir(reportDirectory):
        if file.endswith('_RT.csv'):
            reportList.append(os.path.join(reportDirectory, file))
    print(reportList)
    outFile = '{}/report.txt'.format(os.path.abspath(location))
    
    N = 5
    for item in reportList:
        with open(item) as f:
            head = [next(f, '') for x in range(N)]
            layout = (('{} \n' *len(head)).format(*head))
            store.append('File checked: {} \n Error report: (first 5 lines) \n {}'.format(os.path.abspath(item), layout))   #Load report to list
    
    with open(outFile,'w') as f:
        for item in store:
            f.write('\n {}\n'.format(item))
    
    if os.name == 'nt': #print report to screen
        file_out = ('start notepad.exe {}'.format(outFile))
        os.system(file_out)
    else:
        subprocess.call(['nedit',outFile])

if __name__ == "__main__":
    # globals()[sys.argv[1]]()
    if len(sys.argv) == 4:
        compare(file1=sys.argv[2],file2=sys.argv[3]) #python compare_test.py compare <file1> <file2> 
    # compare(file1=sys.argv[2],file2=sys.argv[3], x=int(sys.argv[4])) #python compare_test.py compare <file1> <file2> <x>
    if len(sys.argv) == 3:
        report(location=sys.argv[2])
