import ctypes
import os
import sys
import threading
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk

import cv2 as cv


class Application:
    def __init__(self):
        self.change_savepath = False
        self.current_path = ""
        self.list_extension = (".jpg", ".png", ".tiff", ".webp", ".bmp")
        self.list_src = []
        self.savepath = ""

    def window(self):
        def info(title, content):
            tkinter.messagebox.showinfo(title, content)

            return None

        def func1(event):
            thread1 = threading.Thread(target=openflies)
            thread1.start()

        def openflies():
            self.list_src = list(tkinter.filedialog.askopenfilenames())
            if not self.list_src:
                sys.exit()
            else:
                pass

            self.current_path = os.path.dirname(self.list_src[0])

            if len(self.list_src) == 1:
                tkstr_filecount.set("1 file selected")
            else:
                tkstr_filecount.set(
                    "{} files selected".format(len(self.list_src))
                )

        def func3(event):
            thread3 = threading.Thread(target=process)
            thread3.start()

        def process():
            if len(self.list_src) == 0:
                info("info", "No file selected.")
                sys.exit()

            flip_horizontally, flip_vertical, w, h = False, False, 0, 0
            progressbar["maximum"] = len(self.list_src)
            progressbar["value"] = 0

            flip_horizontally = tkbool_horizontal.get()
            flip_vertical = tkbool_vertical.get()

            rotate_tkint_degree = tkint_degree.get()

            var_extension = combobox_extension.get()

            if not entry_w.get():
                iw = None
            else:
                try:
                    iw = int(entry_w.get())
                    if iw < 0:
                        flip_horizontally = True
                        iw = abs(iw)
                    else:
                        pass
                except:
                    info("Error", "Invalid input")
                    entry_w.delete(0, tkinter.END)
                    entry_h.delete(0, tkinter.END)
                    sys.exit()

            if not entry_h.get():
                ih = None
            else:
                try:
                    ih = int(entry_h.get())
                    if ih < 0:
                        flip_vertical = True
                        ih = abs(ih)
                    else:
                        pass
                except:
                    info("Error", "Invalid input")
                    entry_w.delete(0, tkinter.END)
                    entry_h.delete(0, tkinter.END)
                    sys.exit()

            ignore_count = 0

            for src in self.list_src:
                img = cv.imread(src)
                if img is None:
                    ignore_count += 1
                    progressbar["value"] += 1
                    continue
                else:
                    pass

                h, w, c = img.shape

                if not iw and not ih:
                    pass
                elif iw and ih:
                    img = cv.resize(img, dsize=(iw, ih))
                elif iw and not ih:
                    img = cv.resize(img, dsize=(iw, round(iw / w * h)))
                elif not iw and ih:
                    img = cv.resize(img, dsize=(round(ih / h * w), ih))
                else:
                    pass

                if flip_horizontally == True:
                    img = cv.flip(img, 1)
                else:
                    pass

                if flip_vertical == True:
                    img = cv.flip(img, 0)
                else:
                    pass

                if rotate_tkint_degree == 0:
                    pass
                elif rotate_tkint_degree == 90:
                    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
                elif rotate_tkint_degree == 180:
                    img = cv.rotate(img, cv.ROTATE_180)
                elif rotate_tkint_degree == 270:
                    img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
                else:
                    pass

                addname = entry_name.get()

                if self.change_savepath == False:
                    cv.imwrite(
                        "{}{}{}".format(
                            os.path.splitext(src)[0], addname, var_extension
                        ),
                        img,
                    )
                elif self.change_savepath == True:
                    cv.imwrite(
                        "{}/{}{}{}".format(
                            self.savepath,
                            os.path.splitext(os.path.basename(src))[0],
                            addname,
                            var_extension,
                        ),
                        img,
                    )
                else:
                    pass

                progressbar["value"] += 1

            if len(self.list_src) - ignore_count == 1:
                msg1 = "1 file processed successfully"
            elif len(self.list_src) - ignore_count == 0:
                msg1 = "No file processed successfully"
            else:
                msg1 = "{} files processed successfully".format(
                    len(self.list_src) - ignore_count
                )
            if ignore_count == 1:
                msg2 = "1 file ignored"
            elif ignore_count == 0:
                msg2 = "No file ignored"
            else:
                msg2 = "{} files ignored".format(ignore_count)

            info("Operation completed", "{}\n{}".format(msg1, msg2))
            progressbar["value"] = 0

        def func4(event):
            self.change_savepath = True
            self.savepath = tkinter.filedialog.askdirectory()
            tkstr_savepath.set(self.savepath)

        def func5(event):
            self.change_savepath = False
            tkstr_savepath.set("(Current path)")

        def func6(event):
            tkstr_name.set("sample{}.(ext)".format(entry_name.get()))

        def func7(event):
            entry_name.delete(0, tkinter.END)
            entry_name.insert(0, "_modified")
            tkstr_name.set("sample{}.(ext)".format(entry_name.get()))

        def cancel(event):
            root.destroy()

        root = tkinter.Tk()
        root.title("Image Converter & Editor (v1.1)")
        root.geometry("+10+10")
        root.resizable(False, False)

        icon_data = """iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAA
                    BgRJREFUeF7dm9tPXEUcx7/DAoWCQEvBLgRaW6kCrSmCmphq9MUY0/hQjKa2Tz7w
                    4IMmxv/CS4zaRNM0Jt4eNaTGxqghRiAaMdHEStK41HjjsrBlWfa+54wZdg979nAu
                    M+fMHNB52pydmd/v95nf7zeXM4dgF8o3N+hgXQS/MtGHbysrUMygZ+goWQxbHRK2
                    wG9jlJplGgCMZwPdJFSdQhNmNdww2Aqg8lwf6CaRMAZHOYCZBfqBTnHRyRgHAFvV
                    SxreGoySF1SCUAbg6j90f0cWaS/l3QBst02iaWCA5L368vO/EgBO7m6nIBeASkMV
                    +UEqgOkYLVKgXmQkRACwfnWKzbtuJ5W5Q0SSfV0pAGZi9CUdeM2POqIADBn5EiZO
                    9pDLfmSa2wQGIOLuQUPArn3QsPANIKjhHtOg8MD6BSEMYDpG/6JAr7CGDg38hoBd
                    d5qO+bsPkyER3bgBzCzQx3SKL0Q656krE8B2fijizMleMsMjnwuALHdXkQPcjOQJ
                    C1cAKg2XnQP8grAFMBujz2nAFR4XClpHRQjY6ZQrYfxUD/nE+t8OALO/0Qc1Aq74
                    CWo8ax8WACaroGF4OEq2tuFG2QHgwzlKjxwA2B81+1YZ1tr0EQYAtsFmm/ClFPDQ
                    8drtti0ApucD/VVtWUNVRSWAO7uqWk8vlH+7Api8Th9PZXGNVTzUAhzvrHag6UDc
                    c28njkkFgKOdQH1dVZcbcWClMohUx/DDA9UwqPGAyZ/pk6kiJs1m3NsLNJiOJtaz
                    QK4kbqhTC5kAWhqBaHtVUkkHvvu9VnJJw8ijJ8hPtjnADoBR0RwS7JmssJAFwOzu
                    TD/D5a3gfQNgHdUR4L6+2i6DgggKwGr47M2tLbNjCQTA6LWvA+hpq8ooaEAi4y8s
                    /ALobQeaG6sy/04CN9e8dZACwBBzfx9gnlRW0wCLO5EiCoDloyMHqxLYYM9UMjyP
                    XKkAZOQHEQC8ce4GQgkAJrAxAoxYNsk8+YEHgNXwuT/8z0TKABjUT3QBB5qrY5Ap
                    ABsu57luALpagXZTX7cywPUlHkdXnAR5VLBOm8ub5eWotdgBYLPNsUO1NZ2mNR5d
                    zHWUe4BVIa/1gxWAjDjflRzgJrStCRjsNmVuCjCPYMUAwEacjbxRflkE2KpTdgnd
                    A8wG3BMFmhuqTzZyAFtTdJlO+XNFYO5P2WZX+9tVANZpU7W722HcEwAMxS6Mln/J
                    SnA8frMnAKytraNQKOLls+UN+0c/Avvqwzkd2lUApZKGeDyxPVBmAMbDaFt5UaWq
                    7BqAxcX4DpvsABiV2LGcihI6ADvDDcPcAKgCERqAZDKFTCbnOog8AFgHrY1AZ4sc
                    f1AOQNcplpdXubTlBWB0xtYM5sUSlxBLJaUA3NzdTllRADLCQgmApaVVULudjscQ
                    +QXAumUHMf0d4j4gFUA6ncXGRmVRL65LzTrAR/OtJmzrzfYavEUaAFF3lxkCdn31
                    V95meYEIDECG4SLToJdB1v+91g++AazEE9BKmqg+UqZBUaHsrRA7NbYr7gBMr8aM
                    xvl8AYlEUlQHrvpBkiCPgO7W2u03a+P6aoxVYG+Hjc5lurvqHOAGxBwWXG+HVRuu
                    Mgd4gfAEcGU6PZa4lf6Bx8WC1lEdAlb99u/D0LlTZN783PaKzDtfJ8+nMvmPgxro
                    1T5MAI31OPf0afKpVSfXS1KvXF1RekkkLAAXx5w/wuC6JqcKhGoAboYbnsAFgFW+
                    PJV6ZH0zO+Xl1iL/qwLQHMGZ8RGJFyXNRr1xbS1WLGnHRAx1qisbQIRg/vyooquy
                    ViNkhIVMADzubjcQ3CHgNIpBQMgA4Ndw4Rzg5vKXvko+n8nmL4mGRRAATRFMPDWy
                    Bz6YMBv9+uerWU3TuXfnfgDUEWw+O7rHPpnxmx9EAQR1dyU5wMnt35uiTaubcdf3
                    u7wADraj6Yn/0mdzZihvf7n+bjZXmPCzG2yox5vPnCYviuYWkfqBZwFeYa9+FqfW
                    g1MnDyAE+oXR/8mns175IRo13WgGoCLO3QYpNA8wK/H+99k7lldSW7f7DADNQM/4
                    WPifz/8L3Wy4X8djjKsAAAAASUVORK5CYII="""

        root.tk.call(
            "wm", "iconphoto", root._w, tkinter.PhotoImage(data=icon_data)
        )

        inner = ttk.Frame(root)
        inner.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=(0, 10))

        column0 = tkinter.Canvas(inner, width=200, height=1)
        column1 = tkinter.Canvas(inner, width=50, height=1)
        column2 = tkinter.Canvas(inner, width=200, height=1)
        column0.grid(column=0, row=0)
        column1.grid(column=1, row=0)
        column2.grid(column=2, row=0)

        title_files = ttk.Label(inner, text="Files", font=("", 0, "bold"))
        title_files.grid(
            column=0,
            row=1,
            columnspan=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        lable_files = ttk.Label(inner, text="File(s):")
        lable_files.grid(
            column=0,
            row=2,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        button_open = ttk.Button(inner, text="Open", width=10)
        button_open.grid(
            column=0,
            row=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_open.bind("<Button-1>", func1)

        tkstr_filecount = tkinter.StringVar()
        tkstr_filecount.set("No file selected")
        label_status = ttk.Label(inner, textvariable=tkstr_filecount)
        label_status.grid(
            column=2,
            row=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        # button_clear = ttk.Button(inner, text="Clear", width=8)
        # button_clear.grid(column=, row=, sticky=tkinter.W, ipadx=0, ipady=0, padx=10, pady=4)
        # button_clear.bind("<Button-1>", func2)

        title_editor = ttk.Label(inner, text="Editor", font=("", 0, "bold"))
        title_editor.grid(
            column=0,
            row=4,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        label_w = ttk.Label(inner, text="Width (px):")
        label_w.grid(
            column=0,
            row=5,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        entry_w = ttk.Entry(inner, width=10)
        entry_w.grid(
            column=0,
            row=6,
            columnspan=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        label_h = ttk.Label(inner, text="Height (px):")
        label_h.grid(
            column=0,
            row=7,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        entry_h = ttk.Entry(inner, width=10)
        entry_h.grid(
            column=0,
            row=8,
            columnspan=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        tkbool_horizontal = tkinter.BooleanVar()
        tkbool_vertical = tkinter.BooleanVar()

        # label_horizontal = tkinter.Label(inner, text="")
        # label_horizontal.grid(sticky=tkinter.E)
        # label_vertical = tkinter.Label(inner, text="")
        # label_vertical.grid(sticky=tkinter.E)

        checkbutton_horizontal = ttk.Checkbutton(
            inner, text="Flip Horizontally", variable=tkbool_horizontal
        )
        checkbutton_horizontal.grid(
            column=0,
            row=9,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        checkbutton_vartical = ttk.Checkbutton(
            inner, text="Flip Vertically", variable=tkbool_vertical
        )
        checkbutton_vartical.grid(
            column=0,
            row=10,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        radiobuttons = ttk.Frame(inner)
        radiobuttons.grid(
            column=0,
            row=11,
            columnspan=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        tkint_degree = tkinter.IntVar()

        radiobutton_0 = ttk.Radiobutton(
            radiobuttons, text="Rotate 0°", variable=tkint_degree, value=0
        )
        radiobutton_0.grid(
            column=0,
            row=0,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        radiobutton_90 = ttk.Radiobutton(
            radiobuttons, text="Rotate 90°", variable=tkint_degree, value=90
        )
        radiobutton_90.grid(
            column=1,
            row=0,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        radiobutton_180 = ttk.Radiobutton(
            radiobuttons, text="Rotate 180°", variable=tkint_degree, value=180
        )
        radiobutton_180.grid(
            column=0,
            row=1,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        radiobutton_270 = ttk.Radiobutton(
            radiobuttons, text="Rotate 270°", variable=tkint_degree, value=270
        )
        radiobutton_270.grid(
            column=1,
            row=1,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        label_output_properties = ttk.Label(
            inner, text="Output Properties", font=("", 0, "bold")
        )
        label_output_properties.grid(
            column=0,
            row=12,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        label_extension = ttk.Label(inner, text="Extension:")
        label_extension.grid(
            column=0,
            row=13,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        combobox_extension = ttk.Combobox(
            inner,
            justify="center",
            state="readonly",
            values=self.list_extension,
            width=10,
        )
        combobox_extension.grid(
            column=0,
            row=14,
            columnspan=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        combobox_extension.set(".jpg")

        label_name = ttk.Label(inner, text="Name:")
        label_name.grid(
            column=0,
            row=15,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        tkstr_name = tkinter.StringVar()

        label_namepreview = ttk.Label(inner, textvariable=tkstr_name)
        label_namepreview.grid(
            column=0,
            row=16,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=2,
        )

        entry_name = ttk.Entry(inner, width=10)
        entry_name.grid(
            column=0,
            row=17,
            columnspan=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        entry_name.insert(0, "_modified")
        tkstr_name.set("sample{}.(ext)".format(entry_name.get()))

        button_updatename = ttk.Button(inner, text="Update", width=10)
        button_updatename.grid(
            column=0,
            row=18,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_updatename.bind("<Button-1>", func6)

        button_clearname = ttk.Button(inner, text="Default", width=10)
        button_clearname.grid(
            column=2,
            row=18,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_clearname.bind("<Button-1>", func7)

        label_save = ttk.Label(inner, text="Save in:")
        label_save.grid(
            column=0,
            row=19,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        tkstr_savepath = tkinter.StringVar()
        tkstr_savepath.set("(Current path)")

        label_savepath = ttk.Label(inner, textvariable=tkstr_savepath)
        label_savepath.grid(
            column=0,
            row=20,
            columnspan=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=2,
        )

        button_browse = ttk.Button(inner, text="Browse", width=10)
        button_browse.grid(
            column=0,
            row=21,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_browse.bind("<Button-1>", func4)

        button_clearpath = ttk.Button(inner, text="Clear")
        button_clearpath.grid(
            column=2,
            row=21,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_clearpath.bind("<Button-1>", func5)

        title_status = ttk.Label(inner, text="Status", font=("", 0, "bold"))
        title_status.grid(
            column=0,
            row=22,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        label_progress = ttk.Label(inner, text="Progress:")
        label_progress.grid(
            column=0,
            row=23,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=(2, 0),
        )

        progressbar = ttk.Progressbar(
            inner,
            orient="horizontal",
            maximum=100,
            value=0,
            length=10,
            mode="determinate",
        )
        progressbar.grid(
            column=0,
            row=24,
            columnspan=3,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        button_ok = ttk.Button(inner, text="Start", width=10)
        button_ok.grid(
            column=2,
            row=25,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )
        button_ok.bind("<Return>", func3)
        button_ok.bind("<Button-1>", func3)

        root.bind("<Return>", func3)
        root.bind("<Escape>", cancel)
        root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

        root.mainloop()

        return None


def main():
    root = Application()
    root.window()


if __name__ == "__main__":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

    main()
