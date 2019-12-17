import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import filedialog

from Phase0 import phase0
from Phase0_1 import phase0_1
from Phase1 import phase1
from Phase2 import phase2
from Phase3 import phase3

from form_viewer import form_viewer



#Tk class generating
root = tk.Tk()


# screen size
root.geometry("700x500")


# screen title
root.title("N1MM to JARL log converter")


# パラメータ
folder_path = tk.StringVar()
form_file = tk.StringVar()
adif_file = tk.StringVar()

log_file = tk.StringVar()
HL_file = tk.StringVar()


Ph0_data = []
Callsign = ""
FD_coe = 1
Contest_name = ""
Multi = ""


def ask_form():
    """　form.txtファイル選択ボタンの動作
    """
    global path
    global folder_path
    path = filedialog.askdirectory()
#    form_f = filedialog.askopenfilename(filetypes =  [('テキストファイル','*.txt')] , initialdir = './' )
    folder_path.set(path)
#    form_file.set(form_f)

#    print( "-------- ask_input() " ) 
#    print( "path       : ", path )
#    print( "folder_path: ", folder_path )
#    print( "form_f     ; ", form_f )
#    print( "form_file  : ",form_file )

    return


def ask_adif():
    """　adif.adiファイル選択ボタンの動作
    """
#    path = filedialog.askdirectory()
    adif_f = filedialog.askopenfilename(filetypes =  [('テキストファイル','*.adi')] , initialdir = './' )
#    folder_path.set(path)
    adif_file.set(adif_f)

    print( "-------- ask_adif() " ) 
#    print( "path: ", path )
#    print( "folder_path: ", folder_path )
    print( "adif_f   ; ", adif_f )
    print( "adif_file: ",adif_file )

    return


def data_clear():
    Remarks1.delete(0, tk.END)
    My_multi.delete(0, tk.END)
    Guest.set(False)
    FD_contest.set(False)
    Multi_Op.set(False)
    Contest_type.set(False)
    AA_contest.set(False)
    Power_code.set(False)
    JST_convert_flag.set(False)
#    Time_convert.set(False)
    QSLyesno.set(False)
    form_file.set('')
    adif_file.set('')

    
def ok_click() :
    Multi = My_multi.get()
    mbox.showinfo('My Multi', Multi )

    return Callsign


def log_generate() :
    Guest_op =Guest.get()
    FD = FD_contest.get()
    Mop = Multi_Op.get()
    form = form_file.get()
    file_path = folder_path.get()
    
    Ph0_data = phase0(Guest_op, FD, Mop, file_path )
#    Ph0_data = phase0(Guest_op, FD, Mop, form)
#    Ph0_data = phase0(Guest_op, FD, Mop )
    Callsign = Ph0_data[0]
#    mbox.showinfo( "Callsign", Callsign )
    FD_coe = int(Ph0_data[1])
    Contest_name = phase0_1( Callsign, file_path )
#    a = Remarks1.get()
#    mbox.showinfo('Log Remarks', 'Remark: ' + a )
    
    #  Phase1を起動
    #       ADIFファイルのログライン分割を1ラインに修正
    phase1( Callsign, file_path )


    #  Phase2を起動
    #     スコアサマリーの生成、JARLサマリーシートへ得点を転記
    phase2( Callsign , FD_coe , Contest_name, file_path )

    #Phase3を起動
    Multi = My_multi.get()
#    Time_conv = Time_convert.get()
    QSL = QSLyesno.get()
    JST_conv = JST_convert_flag.get()
    Power = Power_code.get()
    AA = AA_contest.get()
    
    phase3( Callsign , Contest_name, QSL, JST_conv, QSL, Multi, AA, Remarks1.get(), file_path )


def form_view() :
    file_path = folder_path.get()
    form_viewer(file_path)

  
def closing():
#    exit()
    root.destroy()



# チェックON・OFF変数
Guest = tk.BooleanVar()
Guest.set(False)

FD_contest = tk.BooleanVar()
FD_contest.set(False)

Multi_Op = tk.BooleanVar()
Multi_Op.set(False)

Contest_type = tk.BooleanVar()
Contest_type.set(False)

AA_contest = tk.BooleanVar()
AA_contest.set(False)

Power_code = tk.BooleanVar()
Power_code.set(False)

JST_convert_flag = tk.BooleanVar()
JST_convert_flag.set(False)

#Time_convert = tk.BooleanVar()
#Time_convert.set(False)
QSLyesno = tk.BooleanVar()
QSLyesno.set(False)


# check botton
check_Guest = tk.Checkbutton(root, variable = Guest, text ="ゲストオペ運用ですか?")
check_Guest.place(x=140, y=50)

check_FD_contest = tk.Checkbutton(root, variable = FD_contest , text ="FDコンテストですか？")
check_FD_contest.place(x=140, y=70)

check_Multi_Op = tk.Checkbutton(root, variable = Multi_Op , text ="マルチオペ運用ですか？")
check_Multi_Op.place(x=140, y=90)

check_Contest_type = tk.Checkbutton(root, variable = Contest_type , text ="通常のContestですか?")
check_Contest_type.place(x=140, y=110)

check_AA_contest = tk.Checkbutton(root, variable = AA_contest , text ="ALL Asia DX contestですか?")
check_AA_contest.place(x=140, y=130)

check_Power_code = tk.Checkbutton(root, variable = Power_code , text ="1.2GHzバンド以上のパワーコードをMからLに変換します?")
check_Power_code.place(x=140, y=150)

check_JST_convert_flag = tk.Checkbutton(root, variable = JST_convert_flag , text ="ロギングはUTCでJSTに変換しますか？")
check_JST_convert_flag.place(x=140, y=170)

#check_Time_convert = tk.Checkbutton(root, variable = Time_convert , text ="UTCをJSTに変換しますか？")
#check_Time_convert.place(x=140, y=190)
check_QSLyesno = tk.Checkbutton(root, variable = QSLyesno , text ="QSLカードを発行しますか？")
check_QSLyesno.place(x=140, y=190)


# label
label_contest_number = tk.Label( text="My Contest Multi: ")
label_contest_number.place(x=30, y=230)

Remarks1 = tk.Label(        text="Hamlog Remarks1: ")
Remarks1.place(x=30, y=250)
label_top = tk.Label( text ="N1MM+ ADIFファイルからJARLコンテストログ生成ツール")
label_top.pack()

label_term1 = tk.Label( text ="１．パラメータ設定")
label_term1.place(x=10,y=30)

label_term2 = tk.Label( text ="２．")
label_term2.place(x=10,y=350)

label_term2 = tk.Label( text ="３．")
label_term2.place(x=10,y=390)



# ウィジット作成（form.txtファイル）
form_label = tk.Label(root, text="データフォルダ指定")
form_label.place(x=30, y=290)
#form_box = tk.Entry(root, textvariable= form_file, width=80)
form_box = tk.Entry(root, textvariable= folder_path, width=80)
form_box.place(x=145, y=290)
form_btn = tk.Button(root, text="参照", command=ask_form)
form_btn.place(x=650, y=290)


# ウィジット作成（ADIFファイル）
#output_label = tk.Label(root, text="ADIFファイル:")
#output_label.place(x=30, y=310)
#output_box = tk.Entry(root, textvariable=adif_file, width=80)
#output_box.place(x=145, y=310)
#output_btn = tk.Button(root, text="参照", command=ask_adif)
#output_btn.place(x=650, y=310)


# text box
My_multi = tk.Entry(width=10)
My_multi.place(x=145,y=230)

Remarks1 = tk.Entry(width=40)
Remarks1.place(x=145,y=250)


clear_Button = tk.Button(root,text='パラメータClear', command = data_clear )
#clear_Button.pack(  fill = 'none', padx=20, side = 'bottom'  )
clear_Button.place(x=40 , y=50)

okButton =tk.Button( root, text='form.txtファイルの確認と修正', command = form_view )
#okButton.pack( fill = 'none', padx=20, side = 'bottom' )
okButton.place(x=40 , y=350)

okButton =tk.Button( root, text='コンテストログ生成', command = log_generate )
#okButton.pack( fill = 'none', padx=20, side = 'bottom' )
okButton.place(x=40 , y=390)

closeButton =tk.Button( root, text='Close', command = closing )
closeButton.place(x=370 , y=470)


root.mainloop()
