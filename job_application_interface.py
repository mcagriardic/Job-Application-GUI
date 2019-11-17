from tkinter import *
import tkinter
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from pathlib import Path
from datetime import datetime
import time


class JobApplicationApp(object):

    def __init__(self):
        self.__window = Tk()

        self.__window_title = None
        self.__window_dimensions = None

        #cn = company_name -- company name and its grid
        self.__lbl_cn = None
        self.__txt_entry_cn = None
        
        #jt = job title
        self.__lbl_jt = None
        self.__txt_entry_jt = None
        
        #pl = position level
        self.__lbl_pl = None
        self.__cbox_pl = None

        #jl = Job Location
        self.__lbl_jl = None
        self.__txt_entry_jl = None

        self.__lbl_x_notes = None
        self.__s_txt_entry_x_notes = None

        self.__lbl_status = None

        self.__btn_register = None

        self.txt_var_cn = StringVar()
        self.txt_var_jt = StringVar()
        self.txt_var_pl = StringVar()
        self.txt_var_jl = StringVar()
        self.status = StringVar()


        self.output_cn = None
        self.output_pt = None
        self.output_cn = None
        self.output_jl = None
        self.output_x_notes = None


    def __setWindowNameandDimensions(self):
        self.__window_title = self.__window.title("Job Application Registry")
        self.__window.geometry("340x180")


    def __setCompanyLabelNameandGrid(self):
        self.__lbl_cn = Label(self.__window, text="Company Name: ")
        self.__lbl_cn.grid(column = 0, row = 0)


    def __setCompanyTextEntryDimensionsandGrid(self):
        self.__txt_entry_cn = Entry(self.__window, textvariable = self.txt_var_cn, width=23)
        self.__txt_entry_cn.grid(column=2, row=0)


    def __setStatusLabelNameandGrid(self):
        self.__lbl_status = Label(self.__window, text="--Status--")
        self.__lbl_status.place(x = 260, y = 0)
        self.__setStatusState()

    def __setStatusState(self):
        self.status.set("...")
        status_state = Label(self.__window, text=self.status.get(), textvariable = self.status)
        status_state.place(x = 260, y = 16)


    def __setJobTitleLabelNameandGrid(self):
        self.__lbl_jt = Label(self.__window, text="Position Title: ")
        self.__lbl_jt.grid(column = 0, sticky="W", row = 1)


    def __setJobTitleTextEntryDimensionsandGrid(self):
        self.__txt_entry_jt = Entry(self.__window, textvariable = self.txt_var_jt, width=23)
        self.__txt_entry_jt.grid(column=2, row=1)


    def __setJobLevelCBoxNameandGrid(self):
        self.__lbl_pl = Label(self.__window, text="Position Level: ")
        self.__lbl_pl.grid(column = 0, sticky="W", row = 2)


    def __setJobLevelComboboxDimensionsGridandValues(self):
        self.__cbox_pl = ttk.Combobox(self.__window, textvariable = self.txt_var_pl)
        cbox_pl_values = ("Entry", "Mid-Senior", "Senior")
        self.__cbox_pl["values"] = cbox_pl_values
        self.__cbox_pl.grid(column=2, row=2)


    def __setJobLocationLabelNameandGrid(self):
        self.__lbl_jl = Label(self.__window, text = "Job Location: ")
        self.__lbl_jl.grid(column = 0, sticky="W", row = 3)


    def __setJobLocationTextEntryDimensionsandGrid(self):
        self.__txt_entry_jl = Entry(self.__window, textvariable = self.txt_var_jl, width=23)
        self.__txt_entry_jl.grid(column=2, row=3)


    def __setExtraNotesLabelNameandGrid(self):
        self.__lbl_x_notes = Label(self.__window, text = "Extra notes: ")
        self.__lbl_x_notes.place(x = 0, y = 100)


    def __setExtraNotesScrolledTextEntryDimensionsandGrid(self):
        self.__s_txt_entry_x_notes = ScrolledText(self.__window, width=25, height=3)
        self.__s_txt_entry_x_notes.place(x = 99, y = 85)


    def __setRegisterButtonNamenandGrid(self):
        self.__btn_register = Button(self.__window, text="Click to Register!", command = lambda: self.__retrieveInput())
        self.__btn_register.place(relx=0.7, rely=1.0, anchor=SE)


    def __retrieveInput(self):

        self.output_cn = self.txt_var_cn.get()
        self.output_jt = self.txt_var_jt.get()
        self.output_pl = self.txt_var_pl.get()
        self.output_jl = self.txt_var_jl.get()
        self.output_x_notes = self.__s_txt_entry_x_notes.get("1.0", 'end-1c')

        try:
            self.__writetoCSV()
            self.status.set("Success!")
        except:
            self.status.set("Fail!")

    def __writetoCSV(self):
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        file_path = "C:\\Users\\Cagri\\Google Drive\\Applications.csv"
        my_file = Path(file_path)
        
        columns = ["Date",
                   "Company Name",
                   "Position Title",
                   "Position Level",
                   "Job Location",
                   "Extra Notes"]

        if my_file.is_file():
            df = pd.read_csv(file_path)
        else:
            df = pd.DataFrame(columns = columns)
            df.to_csv(file_path)
        
        data_to_append = [dt_string, self.output_cn, self.output_jt, self.output_pl, self.output_jl, self.output_x_notes ]
        df_to_append = pd.DataFrame([data_to_append], columns = columns)

        df = df.append(df_to_append, sort = True)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df[columns]
        df.to_csv(file_path)

        self.__clearText()


    def __clearText(self):

        self.__txt_entry_cn.delete("0", "end")
        self.__txt_entry_jt.delete("0", "end")
        self.__cbox_pl.delete("0", "end")
        self.__txt_entry_jl.delete("0", "end")
        self.__s_txt_entry_x_notes.delete("1.0", END)


    def runApp(self):
        self.__setWindowNameandDimensions()
        self.__setCompanyLabelNameandGrid()
        self.__setCompanyTextEntryDimensionsandGrid()
        self.__setJobTitleLabelNameandGrid()
        self.__setJobTitleTextEntryDimensionsandGrid()
        self.__setJobLevelCBoxNameandGrid()
        self.__setJobLevelComboboxDimensionsGridandValues()
        self.__setJobLocationLabelNameandGrid()
        self.__setJobLocationTextEntryDimensionsandGrid()
        self.__setExtraNotesLabelNameandGrid()
        self.__setExtraNotesScrolledTextEntryDimensionsandGrid()
        self.__setStatusLabelNameandGrid()
        self.__setRegisterButtonNamenandGrid()


        self.__window.mainloop()

app = JobApplicationApp()
app.runApp()