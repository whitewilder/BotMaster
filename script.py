import requests
import pandas as pd
import yfinance as yf
import time
import schedule
from datetime import datetime


#Intraday 30m breakout

def time1():
    now = datetime.now()
    bot_token='1921736682:AAF50mVrAKmeNFshRUhYRVdtfDql_Nl4IHE'
    bot_chatID='1967629084'
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS","AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
        df=yf.download(tickers=all_ticker, period='1d', interval='30m')
        df=df.dropna()
#    rat=(df['Close']-df['Open'])/ (df['High']-df['Low']) > 1
        rat = df['Close'].pct_change()*100 > 0.5
        rat_last=rat[-1:]
        pct_change= df['Close'].pct_change()
        pct_change=pd.DataFrame(pct_change*100)
        final=pct_change[-1:][rat_last].dropna(axis=1)
        final=final.transpose()
        final=final.reset_index()


        first_col=final.columns[1]
        final.rename(columns={first_col:'Change %'}, inplace=True)
        text=final.sort_values(by=['Change %'],ascending =False)


        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(text)
        response=requests.get(send_text)

        
        
#Market closing details        
def time2():
    bot_token='1936739673:AAGGoJSVg-H8vgsPkE0R6-Dh6Hw5aWDEDec'
    bot_chatID='1967629084'
    
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS","AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
        
        df=yf.download(tickers=all_ticker, period='1d', interval='1d')
    
        df= df.tail(1)
    
        df1= (df['Close']-df['Open'])*100/df['Open']


        text1 = df1[df1>2][df1<4].dropna(axis=1).transpose()
        text1.rename(columns={text1.columns[0]:'Change'}, inplace=True)
        text1=text1.sort_values(by=['Change'],ascending =False)

        text2 = df1[df1>4].dropna(axis=1).transpose()
        text2.rename(columns={text2.columns[0]:'Change'}, inplace=True)
        text2=text2.sort_values(by=['Change'],ascending =False)


        text3 = df1[df1<-2][df1>-4].dropna(axis=1).transpose()
    
        text4 = df1[df1<-4].dropna(axis=1).transpose()

        list1=["*-------Market CLOSING--------*","*Heavy BULLish*",text2, "*Moderate BULL*",text1, "*Bear*", text3, "*Heavy Bear*", text4]
    
        for x in list1:    
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
            response=requests.get(send_text)

        

#Market Opening details        
        
def time3():
    bot_token='1936739673:AAGGoJSVg-H8vgsPkE0R6-Dh6Hw5aWDEDec'
    bot_chatID='1967629084'
    
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS",
                "AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
        df1=yf.download(tickers=all_ticker, period='2d', interval='2m')
        df1= df1.reset_index()

        a1=(df1['Close'].iloc[188]-df1['Close'].iloc[187])*100 / df1['Close'].iloc[187]
        
        a2=(df1['Volume'].iloc[188]/df1['Volume'].iloc[187]) 
        a2 = round(pd.DataFrame(a2),2)


        
        text1=pd.DataFrame(a1[a1>.9] )
        text1.rename(columns={text1.columns[0]:'Change'}, inplace=True)
        text1=text1.sort_values(by=['Change'],ascending =False)
        text1=pd.concat([(text1), (a2)], axis=1, join="inner")
        text1= round(text1,2)
        text1['in']=""
        text1 = text1[['Change','in',0]]


        text2=pd.DataFrame(a1[a1<-.9]) 
        text2.rename(columns={text2.columns[0]:'Change'}, inplace=True)
        text2=text2.sort_values(by=['Change'],ascending =False)
        text2=pd.concat([(text2), (a2)], axis=1, join="inner")
        text2= round(text2,2)
        text2['in']=""
        text2 = text2[['Change','in',0]]

        list1=["*-------Market OPENING--------*","*BULLish Opening*",text1, "*Bearish Opening*",text2]
    
        for x in list1:    
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
            response=requests.get(send_text)
 





# Current market status

def time4():
    bot_token='1986631476:AAEkVO7KwsPWlIKDaOjYm809xgU1YDFImKo'
    bot_chatID='1967629084'
    
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS","AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
        df=yf.download(tickers=all_ticker, period='1d', interval='1d')
    
        df= df.tail(1)
    
        df1= (df['Close']-df['Open'])*100/df['Open']


        text1 = df1[df1>2][df1<4].dropna(axis=1).transpose()
        text1.rename(columns={text1.columns[0]:'Change'}, inplace=True)
        text1=text1.sort_values(by=['Change'],ascending =False)

        text2 = df1[df1>4].dropna(axis=1).transpose()
        text2.rename(columns={text2.columns[0]:'Change'}, inplace=True)
        text2=text2.sort_values(by=['Change'],ascending =False)


        text3 = df1[df1<-2][df1>-4].dropna(axis=1).transpose()
        text3.rename(columns={text3.columns[0]:'Change'}, inplace=True)
        text3=text3.sort_values(by=['Change'],ascending =False)
    
        text4 = df1[df1<-4].dropna(axis=1).transpose()
        text4.rename(columns={text4.columns[0]:'Change'}, inplace=True)
        text4=text4.sort_values(by=['Change'],ascending =False)

        list1=["*-------Current Market Status--------*","*Heavy BULLish*",text2, "*Moderate BULL*",text1, "*Bear*",
               text3, "*Heavy Bear*", text4,"*------------------------*"]
    
        for x in list1:    
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
            response=requests.get(send_text)

        
        
        
def running_status():
    start_now=datetime.now().replace(hour=3, minute=45, second=0, microsecond=0)
    end_now=datetime.now().replace(hour=10, minute=00, second=0, microsecond=0)
    return start_now<datetime.now()<end_now       
        
#Banknifty Moves
def time5():
    
    a=yf.download(tickers="^NSEBANK", period='5m', interval='1m').dropna(axis=1)
    b=((a['Close']- a['Open']))
    
    cond=(b[-2] > -35) | (b[-2] > 35)

    if (cond ):
        text= round(b[-2])
        bot_token='1945412976:AAG7nq85OUhy5ji6l-nH4TwjuPB7WsjOoEM'
        bot_chatID='1967629084'
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str("Sudden Price change in BN: *{}*".format(text))
        response=requests.get(send_text)


#New idea hourly volume breakout
def time6():
    
    now = datetime.now()
    bot_token='1871182021:AAH565P-1lku9NPFyemEwUFIOFj2_nVmj-A'
    bot_chatID='1967629084'
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        ticker=["PRESTIGE.NS", "LTTS.NS", "ANGELBRKG.NS", "EXIDEIND.NS", "GRINDWELL.NS", "VAIBHAVGBL.NS", 
            "NATIONALUM.NS", "LINDEINDIA.NS", "SOBHA.NS", "AIAENG.NS", "DCMSHRIRAM.NS", "MCX.NS", "JINDALSAW.NS", "FINEORG.NS", "BEL.NS", "ICIL.NS", "STLTECH.NS", "JINDALSTEL.NS", "GODREJIND.NS", "ONGC.NS", "FORTIS.NS", "ADANITRANS.NS", "DCAL.NS", "IRB.NS", "CERA.NS", "RELIANCE.NS", "SCHAEFFLER.NS", "CARBORUNIV.NS", "ASAHIINDIA.NS", "GARFIBRES.NS", "VGUARD.NS", "HINDPETRO.NS", "SKFINDIA.NS", "SAIL.NS", "EICHERMOT.NS", "HEROMOTOCO.NS", "IOC.NS", "COALINDIA.NS", "VBL.NS", "ZEEL.NS", "INDUSTOWER.NS", "BLUEDART.NS", "JSL.NS", "GAIL.NS", "PNCINFRA.NS", "MASFIN.NS", "KPRMILL.NS", "IPCALAB.NS", "CDSL.NS", "FINPIPE.NS", "KRBL.NS", "MPHASIS.NS", "ELGIEQUIP.NS", "SUNTECK.NS", "NMDC.NS", "SUNDRMFAST.NS", "ICICIPRULI.NS", "MCDOWELL-N.NS", "EMAMILTD.NS", "POWERINDIA.NS", "KSCL.NS", "SHRIRAMCIT.NS", "RESPONIND.NS", "MAHSEAMLES.NS", "SONATSOFTW.NS", "TORNTPHARM.NS", "RELAXO.NS", "COCHINSHIP.NS", "SOLARA.NS", "TCIEXP.NS", "COFORGE.NS", "BSE.NS", "BHARATFORG.NS", "DLF.NS", "IIFL.NS", "FSL.NS", "TITAN.NS", "CENTURYTEX.NS", "GALAXYSURF.NS", "HAVELLS.NS", "CESC.NS", "BIOCON.NS", "BSOFT.NS", "ORIENTELEC.NS", "3MINDIA.NS", "SUNTV.NS", "LAXMIMACH.NS", "TATASTEEL.NS", "TVSMOTOR.NS", "SUVENPHAR.NS", "ASTERDM.NS", "NAM-INDIA.NS", "JKTYRE.NS", "PERSISTENT.NS", "CEATLTD.NS", "VIPIND.NS", "MARUTI.NS", "ASTRAL.NS", "ABFRL.NS", "DEEPAKNTR.NS", "HAPPSTMNDS.NS", "DALBHARAT.NS", "SHILPAMED.NS", "IBREALEST.NS", "ASTRAZEN.NS", "ECLERX.NS", "DCBBANK.NS", "CASTROLIND.NS", "PFIZER.NS", "EIHOTEL.NS", "ZENSARTECH.NS", "PEL.NS", "BAJAJ-AUTO.NS", "MHRIL.NS", "BOSCHLTD.NS", "HAL.NS", "PIIND.NS", "BAJAJELEC.NS", "SUPREMEIND.NS", "SEQUENT.NS", "DBL.NS", "HINDALCO.NS", "DIVISLAB.NS", "SYMPHONY.NS", "JSLHISAR.NS", "MRF.NS", "IRCTC.NS", "LTI.NS", "CANBK.NS", "VEDL.NS", "OBEROIRLTY.NS", "JKCEMENT.NS", "TATAMOTORS.NS", "KOTAKBANK.NS", "JUSTDIAL.NS", "JSWSTEEL.NS", "PGHL.NS", "BIRLACORPN.NS", "KNRCON.NS", "TANLA.NS", "OIL.NS", "RAJESHEXPO.NS", "POLYCAB.NS", "SIS.NS", "WESTLIFE.NS", "LAOPALA.NS", "HEMIPROP.NS", "SCHNEIDER.NS", "BASF.NS", "GRASIM.NS", "JKPAPER.NS", "CAPLIPOINT.NS", "BPCL.NS", "INDIACEM.NS", "WOCKPHARMA.NS", "WABCOINDIA.NS", "KANSAINER.NS", "TATAPOWER.NS", "PRINCEPIPE.NS", "GMMPFAUDLR.NS", "BRITANNIA.NS", "INOXLEISUR.NS", "PETRONET.NS", "TATAMTRDVR.NS", "IGL.NS", "JMFINANCIL.NS", "UBL.NS", "GREAVESCOT.NS", "IFBIND.NS", "RAIN.NS", "WELCORP.NS", "RADICO.NS", "JKLAKSHMI.NS", "PAGEIND.NS", "SOLARINDS.NS", "TORNTPOWER.NS", "NIACL.NS", "MAZDOCK.NS", "UTIAMC.NS", "RALLIS.NS", "HEG.NS", "INDIGO.NS", "RECLTD.NS", "NATCOPHARM.NS", "ITC.NS", "DRREDDY.NS", "AMARAJABAT.NS", "HATSUN.NS", "GODREJAGRO.NS", "RHIM.NS", "MAHSCOOTER.NS", "LUXIND.NS", "VINATIORGA.NS", "VENKEYS.NS", "GLAXO.NS", "SUNPHARMA.NS", "GSPL.NS", "WELSPUNIND.NS", "KEC.NS", "GRAPHITE.NS", "GULFOILLUB.NS", "TATAINVEST.NS", "MGL.NS", "VARROC.NS", "JBCHEPHARM.NS", "SHOPERSTOP.NS", "PFC.NS", "DMART.NS", "CHALET.NS", "CADILAHC.NS", "TTKPRESTIG.NS", "POLYPLEX.NS", "NTPC.NS", "EPL.NS", "HINDCOPPER.NS", "AARTIDRUGS.NS", "ABBOTINDIA.NS", "M&MFIN.NS", "SRF.NS", "INFY.NS", "MIDHANI.NS", "ASIANPAINT.NS", "STAR.NS", "BAJAJHLDNG.NS", "INGERRAND.NS", "RBLBANK.NS", "SRTRANSFIN.NS", "VOLTAS.NS", "AMBUJACEM.NS", "BALMLAWRIE.NS", "GILLETTE.NS", "AUROPHARMA.NS", "BDL.NS", "DHANI.NS", "ESCORTS.NS", "COROMANDEL.NS", "BALKRISIND.NS", "EDELWEISS.NS", "JSWENERGY.NS", "HDFCAMC.NS", "APOLLOTYRE.NS", "MOIL.NS", "SBIN.NS", "ROUTE.NS", "BBTC.NS", "INDIANB.NS",
                 "SCI.NS", "AJANTPHARM.NS", "QUESS.NS", "BLUESTARCO.NS", "ADANIPORTS.NS", "SUDARSCHEM.NS", "MOTILALOFS.NS", "EIDPARRY.NS", "CHOLAHLDNG.NS"]

        df=yf.download(tickers=ticker, period='3mo', interval='1h')

        df1=df.dropna()
        change=(df1['Close']-df1['Open'])*100/df1['Open']
        x=change[df1["Volume"]> 2*(df1['Volume'].rolling(150).mean())]
        y=x[(x>2)| (x<-2)]

        po=df1['Close'].dropna(axis=1).tail(1).transpose()
        po.rename(columns={po.columns[0]:'Close'}, inplace=True)


        max1=[]
        min1=[]


        for i in df1['Close'].columns:
            max1.append(max(df1['Close'][i]))
            min1.append(min(df1['Close'][i]))
    
        data={"name": df1['Close'].columns,
          "Close": po['Close'],
          "Min": min1,
          "Max":max1
             }  
        dff=pd.DataFrame(data)
        dff["up_from_low"]= (dff["Close"]-dff["Min"])*100/dff["Min"]
        dff["up_from_low"]= (dff["Close"]-dff["Min"])*100/dff["Min"]
        dff["down_from_high"]= (dff["Max"]-dff["Close"])*100/dff["Max"]


        df1=df
        change=(df1['Close']-df1['Open'])*100/df1['Open']
        x=change[df1["Volume"]> 2*(df1['Volume'].rolling(150).mean())]
        y=x[(x>2)| (x<-2)]
        y1=y.iloc[-1].dropna()
        x1=  (df1["Volume"]- (df1['Volume'].rolling(100).mean()))/(df1['Volume'].rolling(150).mean())
        x2=x1[(x>2)| (x<-2)].iloc[-1].dropna()
        y11=pd.DataFrame(y1)
        x22=pd.DataFrame(x2)
        (y11).rename(columns={y11.columns[0]:'Change %'}, inplace=True)
        (x22).rename(columns={x22.columns[0]:'Volumne increased'}, inplace=True)
        text1=pd.concat([(y11), (x22)], axis=1, join="inner")
        jon1 = pd.concat([(text1), (dff)], axis=1, join="inner")
        text2=jon1[['up_from_low','down_from_high']]

        text1= round(text1,2)
        text2= round(text2,2)
    
        list1=["*-------Breaking Volume Details--------*","*BULLish/ Breakout change*",text1, "*From high low position*",text2]
    
        for x in list1:    
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
            response=requests.get(send_text)        
        
 #****************************************************************************************************************************************       

schedule.clear()

#schedule BN bigmoves

schedule.every(610).seconds.do(time1)




while True:
    schedule.run_pending()
    time.sleep(1)
