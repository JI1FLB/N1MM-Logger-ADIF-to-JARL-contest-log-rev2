
    #--------------------------------------------------------
    #   
    #   コンテスト名抽出ルーチン
    #
    #       仕様：
    #       ADIFファイルのファイル冒頭のContest Nameからコンテスト名を抽出
    #


def phase0_1( a:str, path ):
    
    import os
    
    log = ""
    filename = ""

    c = 0

    Contest_name = ""
    
    Callsign = a

    filename = Callsign + ".adi"

 #--------------------------------------

    output_log = open( path + "/" + Callsign + ".adi" ,'r',encoding='utf-8')


#--------------------------------------

    logs = output_log.readlines()

    for log in logs:
            
        log = log.replace(' "','')
        log = log.rstrip('\n')
        log = log.rstrip()
        log = log.lstrip()
        log = log.split()

        c = c + 1

        for i in log:
                
            if 'Contest' in i:
                Contest_name = log[2]

        if c == 4 :
            break


    output_log.close()


    return Contest_name

