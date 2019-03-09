import csv
import requests
from tkinter import *
from tkinter import filedialog


def process_CSV(import_CSV_dir, export_CSV_dir):

    f = open(import_CSV_dir, encoding="utf8")
    csv_f = csv.reader(f)
    csv_l = list(csv_f)


    with open(export_CSV_dir, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)

        lst = []
        for row in csv_l:
            for col in row:
                if col[-4:].lower() == ".csv":
                    lst.append(get_CSV_Content(col))
                else:
                    lst.append(col)
            filewriter.writerow(lst)
            lst = []

    f.close()

def get_CSV_Content(CSV_URL):
    returnString = ""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        if my_list[0].lower().__contains__("<!DOCTYPE html>".lower()):
            return CSV_URL
        else:
            for row in my_list[1:]:
                for col in row:
                    returnString += col + " "
                returnString = returnString[:-1] + ", "
    return returnString[:-2]


def selectImportFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file,", filetypes=(("CSV files", "*.csv"), ("all files","*.*")))
    if filename != "":
        importFromEntry.delete(0, END)
        importFromEntry.insert(0, filename)

def selectExportFile():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file,",
                                                 filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if filename != "":
        if filename[-4:].lower() != ".csv":
            filename += ".csv"
        exportToEntry.delete(0, END)
        exportToEntry.insert(0, filename)

def exportFile():
    if importFromEntry.get() != "" and exportToEntry != "":
        process_CSV(importFromEntry.get(), exportToEntry.get())
        exportToEntry.delete(0, END)
        importFromEntry.delete(0, END)



root = Tk()
root.title("EXP")
#root.iconbitmap("EXP.ico")


importFrom = Label(root, text="Import File from:")
importFromEntry = Entry(root, width=100)
importFromDir = Button(root, text="...", width=4, command=selectImportFile)


exportTo = Label(root, text="Export file to:", )
exportToEntry = Entry(root, width=100)
exportToDir = Button(root, text="...", width=4, command=selectExportFile)

importFrom.grid(row=0, sticky=E)
importFromEntry.grid(row=0, column=1)
importFromDir.grid(row=0, column=2)

exportTo.grid(row=1, column=0, sticky=E)
exportToEntry.grid(row=1, column=1)
exportToDir.grid(row=1, column=2)

exportButton = Button(root, text="Export", width=10, command=exportFile)
exportButton.grid(columnspan=2)


root.mainloop()


