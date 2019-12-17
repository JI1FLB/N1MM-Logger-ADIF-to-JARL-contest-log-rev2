def phase2( call:str, coe:int,Contest_name:str, path ):

    import os
    import datetime

    file_name = ""
    forming_file = ""
    score_file = ""
    summary2_file =""
    Callsign = ""
    okng = True



    #------------------------------------------------------------------------
    #
    #   ファイルネーム（コールサイン）の入力
    #
    #


    Callsign = call
    FD_coe =coe
    score_file = path + "/" + Callsign + "_score.txt"
    forming_file = path + "/" + Callsign + "_forming.adi"
    summary_file = path + "/" + Callsign + "_summary.txt"
    summary2_file = path + "/" + Callsign + "_temp_summary.txt"



    #--------------------------------------------------------
    #   
    #   summary,scure解析集計ルーチン
    #
    #

    output_log = open( forming_file ,"r",encoding='utf-8')
    score_log = open( score_file ,"w",encoding='utf-8')

    data=""
    data1=""
    data2=""
    data3=""

    log = ""
    i=0

    a = ""
    b = ""
    c = ""

    CALL = ""
    QSO_DATE = ""
    TIME_ON = ""
    FREQ = ""
    MODE = ""
    RST_SENT = ""
    RST_RCVD = ""
    APP_N1MM_EXCHANGE1 = ""
    My_multi = ""
    APP_N1MM_POINTS = ""
    okng = True
    yesno = ""


    #------------------------------------------
    #
    #   サマリ作成日付データの作成
    #

    today = datetime.date.today()
    todaydetail = datetime.datetime.today()


    #------------------------------------------
    #
    #   変数宣言
    #
    #

    QSO_160M = 0
    QSO_80M = 0
    QSO_40M = 0
    QSO_20M = 0
    QSO_15M = 0
    QSO_10M = 0
    QSO_6M = 0
    QSO_2M = 0
    QSO_70CM = 0
    QSO_23CM = 0
    QSO_13CM = 0
    QSO_6CM = 0
    QSO_3CM = 0


    point_160M = 0
    point_80M = 0
    point_40M = 0
    point_20M = 0
    point_15M = 0
    point_10M = 0
    point_6M = 0
    point_2M = 0
    point_70CM = 0
    point_23CM = 0
    point_13CM = 0
    point_6CM = 0
    point_3CM = 0


    Multi_160M = 0
    Multi_80M = 0
    Multi_40M = 0
    Multi_20M = 0
    Multi_15M = 0
    Multi_10M = 0
    Multi_6M = 0
    Multi_2M = 0
    Multi_70CM = 0
    Multi_23CM = 0
    Multi_13CM = 0
    Multi_6CM = 0
    Multi_3CM = 0


    Total = 0

    M_160M = set()
    M_80M = set()
    M_40M = set()
    M_20M = set()
    M_15M = set()
    M_10M = set()
    M_6M = set()
    M_2M = set()
    M_70CM = set()
    M_23CM = set()
    M_13CM = set()
    M_6CM = set()
    M_3CM = set()

    l=""
    TOTALSCORE = ""


    log = ""

    a = ""
    b = ""
    c = ""

    BAND = ""

    cnt = 0
#    FD_coe = 1

    EXCHANGE1 = ""
    COMMENT = ""
    SECTION = ""

    #--------------------------------------
    #
    #   コンテスト名取得
    #
    #

    Contest_name = Contest_name.rstrip()
    Contest_name = Contest_name.lstrip()


    #--------------------------------------
    #
    #  スコア集計
    #
    #

    logs = output_log.readlines()
    
    for log in logs:
            
        log = log.replace(' "','')
        log = log.rstrip('\n')
        log = log.rstrip()
        log = log.lstrip()
        log = log.split("<")

    #--------------------------------------
    #　　バンド、QSO数　
    #


        for i in log:
            if "BAND:" in i:
                a = i
                b = a[5:7]
                b1= b.rstrip(">")
                b2 = len(b1)
                BAND = a[6+b2:7+b2+int(b1)]
                BAND = BAND.rstrip()

                if "160M" == BAND : 
                   QSO_160M = QSO_160M +1
                elif "80M" == BAND : 
                   QSO_80M = QSO_80M +1
                elif "40M" == BAND : 
                   QSO_40M = QSO_40M +1
                elif "20M" == BAND : 
                   QSO_20M = QSO_20M +1
                elif "15M" == BAND : 
                   QSO_15M = QSO_15M +1
                elif "10M" == BAND : 
                   QSO_10M = QSO_10M +1
                elif "6M" == BAND : 
                   QSO_6M = QSO_6M +1
                elif "2M" == BAND : 
                   QSO_2M = QSO_2M +1
                elif "70CM" == BAND : 
                   QSO_70CM = QSO_70CM +1
                elif "23CM" == BAND : 
                   QSO_23CM = QSO_23CM +1
                elif "13CM" == BAND : 
                   QSO_13CM = QSO_13CM +1
                elif "6CM" == BAND : 
                   QSO_6CM = QSO_6CM +1
                elif "3CM" == BAND : 
                   QSO_3CM = QSO_3CM +1


    #--------------------------------------
    #　　マルチ収集、ポイント数　収集　
    #


        for i in log:    
            if "APP_N1MM_EXCHANGE1:" in i:
                a = i
                b = a[19:21]
                b1= b.rstrip(">")
                b2 = len(b1)
                APP_N1MM_EXCHANGE1 = a[20+b2:21+b2+int(b1)]
                APP_N1MM_EXCHANGE1 = APP_N1MM_EXCHANGE1.rstrip()
                EXCHANGE1 = APP_N1MM_EXCHANGE1

                if "JADOMESTIC"  == Contest_name :
                    EXCHANGE1 = EXCHANGE1.rstrip("P")
                    EXCHANGE1 = EXCHANGE1.rstrip("L")
                    EXCHANGE1 = EXCHANGE1.rstrip("M")
                    EXCHANGE1 = EXCHANGE1.rstrip("H")

                if "NTT" == Contest_name :
                    EXCHANGE1 = EXCHANGE1.rstrip("N")
                
                if "BIRTHDAY" == Contest_name :
                    EXCHANGE1 = EXCHANGE1.rstrip("N")
                    EXCHANGE1 = EXCHANGE1[ 2:4 ]

            if "COMMENT:" in i:
                a = i
                b = a[8:10]
                b1= b.rstrip(">")
                b2 = len(b1)
                COMMENT = a[9+b2:10+b2+int(b1)]
                COMMENT = COMMENT.rstrip()
                COMMENT = COMMENT.upper()

            if 'SECTION:' in i :
                a = i
                b = a[8:10]
                b1= b.rstrip(">")
                b2 = len(b1)
                SECTION = a[9+b2:10+b2+int(b1)]
                SECTION = SECTION.rstrip()
                SECTION = SECTION.upper()

            if "APP_N1MM_POINTS:" in i:
                a = i
                b = a[16:18]
                b1= b.rstrip(">")
                b2 = len(b1)
                APP_N1MM_POINTS = a[17+b2:18+b2+int(b1)]
                APP_N1MM_POINTS = APP_N1MM_POINTS.rstrip()
                
                if "160M" == BAND : 
                    point_160M = point_160M + int( APP_N1MM_POINTS )
                elif "80M" == BAND : 
                    point_80M = point_80M + int( APP_N1MM_POINTS )
                elif "40M" == BAND : 
                    point_40M = point_40M + int( APP_N1MM_POINTS )
                elif "20M" == BAND : 
                    point_20M = point_20M + int( APP_N1MM_POINTS )
                elif "15M" == BAND : 
                    point_15M = point_15M + int( APP_N1MM_POINTS )
                elif "10M" == BAND : 
                    point_10M = point_10M + int( APP_N1MM_POINTS )
                elif "6M" == BAND : 
                    point_6M = point_6M + int( APP_N1MM_POINTS )
                elif "2M" == BAND : 
                    point_2M = point_2M + int( APP_N1MM_POINTS )
                elif "70CM" == BAND : 
                    point_70CM = point_70CM + int( APP_N1MM_POINTS )
                elif "23CM" == BAND : 
                    point_23CM = point_23CM + int( APP_N1MM_POINTS )            
                elif "13CM" == BAND : 
                    point_13CM = point_13CM + int( APP_N1MM_POINTS )
                elif "6CM" == BAND : 
                    point_6CM = point_6CM + int( APP_N1MM_POINTS )            
                elif "3CM" == BAND : 
                    point_3CM = point_3CM + int( APP_N1MM_POINTS )

                    
    #----------------------------------------------------------------
    #   マルチ仕分け　集計
 

        if 'JADOMESTIC' == Contest_name :
            c = SECTION
        elif 'FURUSATO' == Contest_name :
            c = COMMENT
        elif 'SCCRTTY' == Contest_name : 
            c = COMMENT
        elif 'KCJ-JA' == Contest_name : 
            c = SECTION
        else :
            c = EXCHANGE1        

            
        if "160M" == BAND : 
            M_160M.add( c )
        elif "80M" == BAND : 
            M_80M.add( c )
        elif "40M" == BAND : 
            M_40M.add( c )
        elif "20M" == BAND : 
            M_20M.add( c )
        elif "15M" == BAND : 
            M_15M.add( c )
        elif "10M" == BAND : 
            M_10M.add( c )
        elif "6M" == BAND : 
            M_6M.add( c )
        elif "2M" == BAND : 
            M_2M.add( c )
        elif "70CM" == BAND : 
            M_70CM.add( c )
        elif "23CM" == BAND : 
            M_23CM.add( c )
        elif "13CM" == BAND : 
            M_13CM.add( c )
        elif "6CM" == BAND : 
            M_6CM.add( c )
        elif "3CM" == BAND : 
            M_3CM.add( c )

    #------------------------------------------
    #
    #   QSO数　集計
    #

    QSO = QSO_160M +  QSO_80M + QSO_40M + QSO_20M + QSO_15M + QSO_10M + QSO_6M + QSO_2M + QSO_70CM + QSO_23CM + QSO_13CM + QSO_6CM + QSO_3CM

            
    #------------------------------------------
    #
    #   ポイント集計
    #

    point = point_160M + point_80M + point_40M + point_20M + point_15M + point_10M + point_6M + point_2M + point_70CM + point_23CM+point_13CM+point_6CM+point_3CM


    #------------------------------------------
    #
    #   マルチ集計
    #


    Multi_160M =len( M_160M )

    Multi_80M = len ( M_80M )

    Multi_40M = len( M_40M )

    Multi_20M = len( M_20M )

    Multi_15M = len( M_15M )

    Multi_10M = len( M_10M )

    Multi_6M = len( M_6M )

    Multi_2M = len( M_2M )

    Multi_70CM = len( M_70CM )

    Multi_23CM = len( M_23CM )

    Multi_13CM = len( M_13CM )

    Multi_6CM = len( M_6CM )

    Multi_3CM = len( M_3CM )


    #************************************************
    #
    #    print("マルチ集計")
    #
    #


    Multi = Multi_160M + Multi_80M + Multi_40M + Multi_20M + Multi_15M + Multi_10M  +Multi_6M + Multi_2M + Multi_70CM +Multi_23CM+Multi_13CM+Multi_6CM+Multi_3CM
                      


    print("     コンテストスコアシート")
    print("           作成年月日:" +str(todaydetail.strftime("%Y/%m/%d %H:%M:%S")) + "\n" )
    print( "" )
    print("---------------------------------------------" )
    print(" BAND　QSOs points Multi Coefficent")
    print(" 160M -> ", QSO_160M , point_160M , Multi_160M )
    print("  80M -> ", QSO_80M , point_80M   , Multi_80M )
    print("  40M -> ", QSO_40M , point_40M   , Multi_40M )
    print("  20M -> ", QSO_20M , point_20M   , Multi_20M )
    print("  15M -> ", QSO_15M , point_15M   , Multi_15M )
    print("  10M -> ", QSO_10M , point_10M   , Multi_10M )
    print("   6M -> ", QSO_6M  , point_6M    , Multi_6M )
    print("   2M -> ", QSO_2M  , point_2M    , Multi_2M )
    print(" 70CM -> ", QSO_70CM , point_70CM , Multi_70CM )
    print(" 23CM -> ", QSO_23CM , point_23CM , Multi_23CM )
    print(" 13CM -> ", QSO_13CM , point_13CM , Multi_13CM )
    print(" 6CM -> ", QSO_6CM , point_6CM , Multi_6CM )
    print(" 3CM -> ", QSO_3CM , point_3CM , Multi_3CM )
    print("---------------------------------------------")

    print( "QSO   --> ", QSO )
    print( "point --> ", point )
    print( "Multi --> ", Multi )
    print( "Coeff --> ", FD_coe )
    Total = point * Multi * FD_coe
    print( "Total --> ",Total )
    TOTALSCORE = str( Total )




#----------------------------------------------------
#
#   スコアファイルの作成
#
#
    score_log.write("                             作成年月日:" +str(todaydetail.strftime("%Y/%m/%d %H:%M:%S")) + "\n" )
    score_log.write("      コンテストスコアシート           "  + "\n" )
    score_log.write("---------------------------------------------------" + " " + "\n" )
    score_log.write(" BAND  QSOs  points  Multi  Coefficent"+ "\n" )
    score_log.write(" 160M -> "+ " " +  str( QSO_160M) + " " +  str( point_160M) + " " +  str( Multi_160M ) + " " + "\n" )
    score_log.write("  80M -> "+ " " +  str( QSO_80M) + " " +  str( point_80M)   + " " +  str( Multi_80M ) + " " + "\n")
    score_log.write("  40M -> "+ " " +  str( QSO_40M) + " " +  str( point_40M)   + " " +  str( Multi_40M ) + " " + "\n")
    score_log.write("  20M -> "+ " " +  str( QSO_20M) + " " +  str( point_20M)   + " " +  str( Multi_20M ) + " " + "\n")
    score_log.write("  15M -> "+ " " +  str( QSO_15M) + " " +  str( point_15M)   + " " +  str( Multi_15M ) + " " + "\n")
    score_log.write("  10M -> "+ " " +  str( QSO_10M) + " " +  str( point_10M)   + " " +  str( Multi_10M ) + " " + "\n")
    score_log.write("   6M -> "+ " " +  str( QSO_6M)  + " " +  str( point_6M)    + " " +  str( Multi_6M ) + " " + "\n")
    score_log.write("   2M -> "+ " " +  str( QSO_2M)  + " " +  str( point_2M)    + " " +  str( Multi_2M ) + " " + "\n")
    score_log.write(" 70CM -> "+ " " +  str( QSO_70CM) + " " +  str( point_70CM) + " " +  str( Multi_70CM ) + " " + "\n")
    score_log.write(" 23CM -> "+ " " +  str( QSO_23CM) + " " +  str( point_23CM) + " " +  str( Multi_23CM )+ " " + "\n")
    score_log.write(" 13CM -> "+ " " +  str( QSO_13CM) + " " +  str( point_13CM) + " " +  str( Multi_13CM ) + " " + "\n")
    score_log.write("  6CM -> "+ " " +  str( QSO_6CM) + " " +  str( point_6CM) + " " +  str( Multi_6CM )+ " " + "\n")
    score_log.write("  3CM -> "+ " " +  str( QSO_3CM) + " " +  str( point_3CM) + " " +  str( Multi_3CM )+ " " + "\n")
    score_log.write("---------------------------------------------------"+ "\n" )


    score_log.write( "QSO   --> "+ " " + str( QSO )  + " " +  str( point ) + " " +  str( Multi ) + " " +  str( FD_coe ) + " " + "\n"  )
    Total =   point *   Multi * FD_coe
    score_log.write( "Total --> "+ " " +  str( Total ) + " " + "\n")

    score_log.write( "\n")
    score_log.write( "\n")

    score_log.write( "Band別マルチリスト --------------------------------"+"\n")

    score_log.write( "\n")
    score_log.write( "160M Band"+"\n")
    for l in sorted( M_160M ) :
        score_log.write( l+" " )
    score_log.write( "\n")

    score_log.write( "\n")
    score_log.write( "80M Band"+"\n")
    for l in sorted( M_80M ) :
        score_log.write( l+" " )
    score_log.write( "\n")

    score_log.write( "\n")
    score_log.write( "40M Band"+"\n")
    for l in sorted( M_40M ) :
        score_log.write( l+" " )
    score_log.write( "\n")

    score_log.write( "\n")
    score_log.write( "20M Band"+"\n")
    for l in sorted( M_20M ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "15M Band"+"\n")
    for l in sorted( M_15M ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "10M Band"+"\n")
    for l in sorted( M_10M ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "6M Band"+"\n")
    for l in sorted( M_6M ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "2M Band"+"\n")
    for l in sorted( M_2M ) :
        score_log.write( l+" " )
    score_log.write( "\n")

    score_log.write( "\n")
    score_log.write( "70CM Band"+"\n")
    for l in sorted( M_70CM ) :
        score_log.write( l+" " )
    score_log.write( "\n")

    score_log.write( "\n")
    score_log.write( "23CM Band"+"\n")
    for l in sorted( M_23CM ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "13CM Band"+"\n")
    for l in sorted( M_13CM ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "6CM Band"+"\n")
    for l in sorted( M_6CM ) :
        score_log.write( l+" " )
    score_log.write( "\n")
    
    score_log.write( "\n")
    score_log.write( "3CM Band"+"\n")
    for l in sorted( M_3CM ) :
        score_log.write( l+" " )
    score_log.write( "\n")



#------------------------------
#
# JARLサマリーシートへ得点を転記
#
#

    summary = open( summary_file , "r" , encoding='utf-8')
    summary2 = open( summary2_file ,"w", encoding='utf-8')

    line = summary.readlines()

    for l in line :
        if "<TOTALSCORE>" in l :
            summary2.write( "<TOTALSCORE>" + TOTALSCORE +"</TOTALSCORE>"+"\n" )
        else:
            summary2.write( l )
            
    summary2.close()
    summary.close()

    os.remove(summary_file)
    os.rename(summary2_file , summary_file)

    output_log.close()
    score_log.close()



    print("\n")

    return

    


            
                  
