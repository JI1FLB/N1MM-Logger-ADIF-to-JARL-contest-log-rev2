def form_viewer(path) :

    import tkinter as tk

    import os


    # Main windows
    editor = tk.Tk()
    editor.title('form file Viewer')

    def open_form() :
        fill_in_form = open( path + "/form.txt" ,"r", encoding='utf-8')
        fill_in = fill_in_form.readlines()
        for fill in fill_in :
            fill = fill.lstrip('[')
            fill = fill.lstrip()
            fill = fill.rstrip(']')
            fill = fill.rstrip()
            text_widget.insert('end',fill+'\n')
        fill_in_form.close()


    def save_form() :
        # form.txtファイルのバックアップを追加する。
        save_form = text_widget.get('1.0','end -1c')
        fill_in_form_new = open( path + "/form.txt" ,"w", encoding='utf-8')
        fill_in_form_new.write( save_form )
        fill_in_form_new.close()
        # 表示情報の削除
        text_widget.delete('1.0','end')
        

    def close_disp() :
        editor.destroy()
        

    text_widget = tk.Text(editor)
    text_widget.grid(column = 0, row = 0, sticky = (tk.N, tk.S, tk.E, tk.W))

    editor.columnconfigure(0, weight = 1)
    editor.rowconfigure(0, weight = 1)

    #メニューバー作成 
    men = tk.Menu(editor) 

    #メニューバーを画面にセット 
    editor.config(menu=men) 

    #メニューに親メニュー（ファイル）を作成する 
    menu_file = tk.Menu(editor) 
    men.add_cascade(label='ファイル', menu=menu_file) 

    #親メニューに子メニュー（開く・閉じる）を追加する 
    menu_file.add_command(label='Open', command=open_form) 
    menu_file.add_separator()
    menu_file.add_command(label='Save', command=save_form)
    menu_file.add_separator() 
    menu_file.add_command(label='close', command=close_disp)

    editor.mainloop()
