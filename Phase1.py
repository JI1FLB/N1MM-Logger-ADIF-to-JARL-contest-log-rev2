def phase1( a:str, path ):
    
    import os

    filename = ""
    forming_file = ""
    Callsign = ""
    okng = True


#------------------------------------------------------------------------
#
#   ファイルネーム（コールサイン）の入力
#
#


    Callsign = a

    filename = path + "/" + Callsign + ".adi"
    forming_file = path + "/" + Callsign + "_forming.adi"

    adi_file = open(filename,"r",encoding='utf-8')
    output_log = open(forming_file ,"w",encoding='utf-8')


#--------------------------------------------------------------------

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
    text = ""
    FREQ_f=0.0


#--------------------------------------------------------------------


    a1 = "CALL:"
    a2 = "QSO_DATE:"
    a3 = "TIME_ON:"
    a4 = "SECTION:"
    a5 = "BAND:"
    a6 = "STATION_CALLSIGN:"
    a7 = "FREQ:"
    a8 = "CONTEST_ID:"
    a9 = "FREQ_RX:"
    a10 = "MODE:"
    a11 = "RST_RCVD:"
    a12 = "RST_SENT:"
    a13 = "TX_PWR:"
    a14 = "OPERATOR:"
    a15 = "CQZ:"
    a16 = "STX:"
    a17 = "APP_N1MM_EXCHANGE1:"
    a18 = "APP_N1MM_POINTS:"
    a19 = "APP_N1MM_RADIO_NR:"
    a20 = "APP_N1MM_CONTINENT:"
    a21 = "APP_N1MM_CONTACTTYPE:"
    a22 = "APP_N1MM_RUN1RUN2:"
    a23 = "APP_N1MM_RADIOINTERFACED:"
    a24 = "APP_N1MM_ISORIGINAL:"
    a25 = "APP_N1MM_NETBIOSNAME:"
    a26 = "APP_N1MM_ISRUNQSO:"
    a27 = "EOR>"


#------------------------------------------------------------------------
#
# ADIFファイルが改行分割されたレコードを1レコードに編集
#
#

    lines = adi_file.readlines()

    for line in lines:
        
        if "<CALL:"  in line:
            
            if "<EOR>" in line:
                data1=line
                output_log.write(data1)
                continue
            
            data1=line.rstrip('\n')
            continue
        
        if "<CALL:" not in line:
            
            if "<EOR>" in line:
                data1=data1 + line
                output_log.write(data1)
                data1 = ""
                continue
            
            data1= data1 + line.rstrip('\n')
            continue


        output_log.write(line)
        
    adi_file.close()
    output_log.close()


    return



