
import requests
import pandas as pd
import yfinance as yf
import time
import schedule
import numpy as np
from datetime import datetime


#Intraday 30m breakout




def time1():
    now = datetime.now()
    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS",
                "AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
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
    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS",
                "AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
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
    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS",
                "AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
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
    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        
        all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS",
                "AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
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
    
    cond=(b[-2] < -35) | (b[-2] > 35)

    if (cond & running_status()):
        text= round(b[-2])
        bot_token='1945412976:AAG7nq85OUhy5ji6l-nH4TwjuPB7WsjOoEM'
        bot_chatID='1967629084'
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str("Sudden Price change in BN: *{}*".format(text))
        response=requests.get(send_text)


#New idea hourly volume breakout
def time6():
    

    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        ticker1=["SCHNEIDER.NS", "BASF.NS", "GRASIM.NS", "JKPAPER.NS", "CAPLIPOINT.NS", "BPCL.NS", "INDIACEM.NS", "WOCKPHARMA.NS", "WABCOINDIA.NS", "KANSAINER.NS", "TATAPOWER.NS", "PRINCEPIPE.NS", "GMMPFAUDLR.NS", "BRITANNIA.NS", "INOXLEISUR.NS", "PETRONET.NS", "TATAMTRDVR.NS", "IGL.NS", "JMFINANCIL.NS", "UBL.NS", "GREAVESCOT.NS", "IFBIND.NS", "RAIN.NS", "WELCORP.NS", "RADICO.NS", "JKLAKSHMI.NS", "PAGEIND.NS", "SOLARINDS.NS", "TORNTPOWER.NS", "NIACL.NS", "MAZDOCK.NS", "UTIAMC.NS", "RALLIS.NS", "HEG.NS", "INDIGO.NS", "RECLTD.NS", "NATCOPHARM.NS", "ITC.NS", "DRREDDY.NS", "AMARAJABAT.NS", "HATSUN.NS", "GODREJAGRO.NS", "RHIM.NS", "MAHSCOOTER.NS", "LUXIND.NS", "VINATIORGA.NS", "VENKEYS.NS", "GLAXO.NS", "SUNPHARMA.NS", "GSPL.NS", "WELSPUNIND.NS", "KEC.NS", "GRAPHITE.NS", "GULFOILLUB.NS", "TATAINVEST.NS", "MGL.NS", "VARROC.NS", "JBCHEPHARM.NS", "SHOPERSTOP.NS", "PFC.NS", "DMART.NS", "CHALET.NS", "CADILAHC.NS","PRESTIGE.NS", "LTTS.NS", "ANGELBRKG.NS", "EXIDEIND.NS", "GRINDWELL.NS", "VAIBHAVGBL.NS", 
            "NATIONALUM.NS", "LINDEINDIA.NS", "SOBHA.NS", "AIAENG.NS", "DCMSHRIRAM.NS", "MCX.NS", "JINDALSAW.NS", "FINEORG.NS", "BEL.NS", "ICIL.NS", "STLTECH.NS", "JINDALSTEL.NS", "GODREJIND.NS", "ONGC.NS", "FORTIS.NS", "ADANITRANS.NS", "DCAL.NS", "IRB.NS", "CERA.NS", "RELIANCE.NS", "SCHAEFFLER.NS", "CARBORUNIV.NS", "ASAHIINDIA.NS", "GARFIBRES.NS", "VGUARD.NS", "HINDPETRO.NS", "SKFINDIA.NS", "SAIL.NS", "EICHERMOT.NS", "HEROMOTOCO.NS", "IOC.NS", "COALINDIA.NS", "VBL.NS", "ZEEL.NS",
                
         "INDUSTOWER.NS", "BLUEDART.NS", "JSL.NS", "GAIL.NS", "PNCINFRA.NS", "MASFIN.NS", "KPRMILL.NS", "IPCALAB.NS", "CDSL.NS", "FINPIPE.NS", "KRBL.NS", "MPHASIS.NS", "ELGIEQUIP.NS", "SUNTECK.NS", "NMDC.NS", "SUNDRMFAST.NS", "ICICIPRULI.NS", "MCDOWELL-N.NS", "EMAMILTD.NS", "POWERINDIA.NS", "KSCL.NS", "SHRIRAMCIT.NS", "RESPONIND.NS", "MAHSEAMLES.NS", "SONATSOFTW.NS", "TORNTPHARM.NS", "RELAXO.NS", "COCHINSHIP.NS", "SOLARA.NS", "TCIEXP.NS", "COFORGE.NS", "BSE.NS", "BHARATFORG.NS", "DLF.NS", "IIFL.NS", "FSL.NS", "TITAN.NS", "CENTURYTEX.NS", "GALAXYSURF.NS", "HAVELLS.NS", "CESC.NS", "BIOCON.NS", "BSOFT.NS", "ORIENTELEC.NS", "3MINDIA.NS",
        "SUNTV.NS", "LAXMIMACH.NS", "TATASTEEL.NS", "TVSMOTOR.NS", "SUVENPHAR.NS", "ASTERDM.NS", "NAM-INDIA.NS", "JKTYRE.NS", "PERSISTENT.NS", "CEATLTD.NS", "VIPIND.NS", "MARUTI.NS", "ASTRAL.NS", "ABFRL.NS", "DEEPAKNTR.NS", "HAPPSTMNDS.NS", "DALBHARAT.NS", "SHILPAMED.NS", "IBREALEST.NS", "ASTRAZEN.NS", "ECLERX.NS", "DCBBANK.NS", "CASTROLIND.NS", "PFIZER.NS", "EIHOTEL.NS", "ZENSARTECH.NS", "PEL.NS", "BAJAJ-AUTO.NS", "MHRIL.NS", "BOSCHLTD.NS", "HAL.NS", "PIIND.NS", "BAJAJELEC.NS", "SUPREMEIND.NS", "SEQUENT.NS", "DBL.NS", "HINDALCO.NS", "DIVISLAB.NS", "SYMPHONY.NS", "JSLHISAR.NS", "MRF.NS", "IRCTC.NS", "LTI.NS", "CANBK.NS", "VEDL.NS", "OBEROIRLTY.NS", "JKCEMENT.NS", "TATAMOTORS.NS", "KOTAKBANK.NS", "JUSTDIAL.NS", "JSWSTEEL.NS", "PGHL.NS", "BIRLACORPN.NS", "KNRCON.NS", "TANLA.NS", "OIL.NS", "RAJESHEXPO.NS", "POLYCAB.NS", "SIS.NS", "WESTLIFE.NS", "LAOPALA.NS", "HEMIPROP.NS"]
       
        ticker2=   [        "TTKPRESTIG.NS", "POLYPLEX.NS", "NTPC.NS", "EPL.NS", "HINDCOPPER.NS", "AARTIDRUGS.NS", "ABBOTINDIA.NS", "M&MFIN.NS", "SRF.NS", "INFY.NS", "MIDHANI.NS", "ASIANPAINT.NS", "STAR.NS", "BAJAJHLDNG.NS", "INGERRAND.NS", "RBLBANK.NS", "SRTRANSFIN.NS", "VOLTAS.NS", "AMBUJACEM.NS", "BALMLAWRIE.NS", "GILLETTE.NS", "AUROPHARMA.NS", "BDL.NS", "DHANI.NS", "ESCORTS.NS", "COROMANDEL.NS", "BALKRISIND.NS", "EDELWEISS.NS", "JSWENERGY.NS", "HDFCAMC.NS", "APOLLOTYRE.NS", "MOIL.NS", "SBIN.NS", "ROUTE.NS", "BBTC.NS", "INDIANB.NS", "SCI.NS", "AJANTPHARM.NS", "QUESS.NS", "BLUESTARCO.NS", "ADANIPORTS.NS", "SUDARSCHEM.NS", "MOTILALOFS.NS", "EIDPARRY.NS", "CHOLAHLDNG.NS", "LUPIN.NS", "WIPRO.NS", "GESHIP.NS", "GICRE.NS", "ISEC.NS", "MINDTREE.NS",
        "AAVAS.NS", "RATNAMANI.NS", "GLENMARK.NS", "BANDHANBNK.NS", "AKZOINDIA.NS", "VSTIND.NS", "TECHM.NS", "AUBANK.NS", "ATUL.NS", "KEI.NS", "GUJGASLTD.NS", "DHANUKA.NS", "ERIS.NS", "VALIANTORG.NS", "CHAMBLFERT.NS", "JTEKTINDIA.NS", "ADANIENT.NS", "ITI.NS", "FLUOROCHEM.NS", "NAVINFLUOR.NS", "OFSS.NS", "SUNDARMFIN.NS", "DABUR.NS", "FINCABLES.NS", "FEDERALBNK.NS", "HEIDELBERG.NS", "HINDZINC.NS", "SHARDACROP.NS", "GLAND.NS", "PVR.NS", "CUMMINSIND.NS", "CENTURYPLY.NS", "ICICIGI.NS", "BURGERKING.NS", "MAXHEALTH.NS", "BAJFINANCE.NS", "CIPLA.NS", "KPITTECH.NS", "ICICIBANK.NS", "COLPAL.NS", "NH.NS", "CSBBANK.NS", "DELTACORP.NS", "TATACOMM.NS", "CYIENT.NS", "LICHSGFIN.NS", "TEAMLEASE.NS", "UPL.NS", "SYNGENE.NS", "TIMKEN.NS", "GSFC.NS", "WHIRLPOOL.NS", "PHILIPCARB.NS", "M&M.NS", "MARICO.NS", "KAJARIACER.NS", "CGCL.NS",
         "KSB.NS", "L&TFH.NS", "ADVENZYMES.NS", "PGHH.NS", "BLISSGVS.NS", "STARCEMENT.NS", "HCLTECH.NS", "GPPL.NS", "GODFRYPHLP.NS", "SUMICHEM.NS", "BRIGADE.NS", "GEPIL.NS", "IOLCP.NS", "GUJALKALI.NS", "NESTLEIND.NS", "SBILIFE.NS", "SUPRAJIT.NS", "NOCIL.NS", "TCS.NS", "GNFC.NS", "IBULHSGFIN.NS", "BEML.NS", "BALRAMCHIN.NS", "UJJIVAN.NS", "SUNCLAYLTD.NS", "VTL.NS", "INDUSINDBK.NS", "KALPATPOWR.NS", "NESCO.NS", "RAMCOCEM.NS", "SHREECEM.NS", "CANFINHOME.NS", "PIDILITIND.NS", "LAURUSLABS.NS", "NILKAMAL.NS", "ZYDUSWELL.NS", "GRANULES.NS", "JCHAC.NS", "AARTIIND.NS", "APLAPOLLO.NS", "JUBLFOOD.NS", "AEGISCHEM.NS", "SWANENERGY.NS", "POLYMED.NS", "AFFLE.NS", "AVANTIFEED.NS", "POWERGRID.NS", "HONAUT.NS", "TATACHEM.NS", "VMART.NS", "BHARTIARTL.NS", "HUHTAMAKI.NS", "PRSMJOHNSN.NS", "BATAINDIA.NS", "RAYMOND.NS", "LALPATHLAB.NS", "LT.NS", "APOLLOHOSP.NS", "CRISIL.NS", "GODREJPROP.NS", "TATACONSUM.NS", "UFLEX.NS", "JYOTHYLAB.NS", "HDFCBANK.NS", "BERGEPAINT.NS", "JAMNAAUTO.NS", "ASHOKLEY.NS",
               
        "CROMPTON.NS", "PNBHOUSING.NS", "SPANDANA.NS", "THERMAX.NS", "ADANIGREEN.NS",
                "APLLTD.NS", "BAJAJFINSV.NS", "ULTRACEMCO.NS", "TATAELXSI.NS", "FDC.NS", "TATACOFFEE.NS", "BHARATRAS.NS", "SIEMENS.NS", "SANOFI.NS", "CCL.NS", "HDFC.NS", "GODREJCP.NS", "INDIAMART.NS", "ASHOKA.NS", "ALKYLAMINE.NS", "METROPOLIS.NS", "SPARC.NS", "AXISBANK.NS", "MANAPPURAM.NS", "ABCAPITAL.NS", "CONCOR.NS", "TASTYBITE.NS", "IIFLWAM.NS", "MAHINDCIE.NS", "MINDACORP.NS", "DIXON.NS", "TRENT.NS", "INDOCO.NS", "BALAMINES.NS", "ROSSARI.NS", "TIINDIA.NS", "TCNSBRANDS.NS", "HINDUNILVR.NS", "MUTHOOTFIN.NS", "SBICARD.NS", "GRSE.NS", "ACC.NS", "CHOLAFIN.NS", "BAYERCROP.NS", "SUPPETRO.NS", "AMBER.NS", "REDINGTON.NS", "CAMS.NS", "THYROCARE.NS", "INDHOTEL.NS", "ALKEM.NS", "GAEL.NS", "RITES.NS", "INTELLECT.NS", "CREDITACC.NS", "ENDURANCE.NS", "SFL.NS", "MAHLOG.NS", "CUB.NS", "BAJAJCON.NS", "TRITURBINE.NS", "MINDAIND.NS", "NAUKRI.NS", "SWSOLAR.NS", "EQUITAS.NS", "ABB.NS", "ATGL.NS", "MFSL.NS", "PHOENIXLTD.NS", "HDFCLIFE.NS", "IEX.NS", "ALEMBICLTD.NS",
        ]

        df1=yf.download(tickers=ticker1, period='3mo', interval='1h')
        df2=yf.download(tickers=ticker2, period='3mo', interval='1h')
        
        
        for dat in [df1,df2]:
            
            df1=dat.dropna()
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


            df1=dat.dropna()
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
            
            print(text1)
    
            list1=["*-------Breaking Volume Details--------*","*BULLish/ Breakout change*",text1, "*From high low position*",text2]
    
            for x in list1:    
                send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
                response=requests.get(send_text)        
        
 #****************************************************************************************************************************************            
#New idea dailyr volume breakout
def time7():
    

    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        ticker1=["PRESTIGE.NS", "LTTS.NS", "ANGELBRKG.NS", "EXIDEIND.NS", "GRINDWELL.NS", "VAIBHAVGBL.NS", 
            "NATIONALUM.NS", "LINDEINDIA.NS", "SOBHA.NS", "AIAENG.NS", "DCMSHRIRAM.NS", "MCX.NS", "JINDALSAW.NS", "FINEORG.NS", "BEL.NS", "ICIL.NS", "STLTECH.NS", "JINDALSTEL.NS", "GODREJIND.NS", "ONGC.NS", "FORTIS.NS", "ADANITRANS.NS", "DCAL.NS", "IRB.NS", "CERA.NS", "RELIANCE.NS", "SCHAEFFLER.NS", "CARBORUNIV.NS", "ASAHIINDIA.NS", "GARFIBRES.NS", "VGUARD.NS", "HINDPETRO.NS", "SKFINDIA.NS", "SAIL.NS", "EICHERMOT.NS", "HEROMOTOCO.NS", "IOC.NS", "COALINDIA.NS", "VBL.NS", "ZEEL.NS",
                
         "INDUSTOWER.NS", "BLUEDART.NS", "JSL.NS", "GAIL.NS", "PNCINFRA.NS", "MASFIN.NS", "KPRMILL.NS", "IPCALAB.NS", "CDSL.NS", "FINPIPE.NS", "KRBL.NS", "MPHASIS.NS", "ELGIEQUIP.NS", "SUNTECK.NS", "NMDC.NS", "SUNDRMFAST.NS", "ICICIPRULI.NS", "MCDOWELL-N.NS", "EMAMILTD.NS", "POWERINDIA.NS", "KSCL.NS", "SHRIRAMCIT.NS", "RESPONIND.NS", "MAHSEAMLES.NS", "SONATSOFTW.NS", "TORNTPHARM.NS", "RELAXO.NS", "COCHINSHIP.NS", "SOLARA.NS", "TCIEXP.NS", "COFORGE.NS", "BSE.NS", "BHARATFORG.NS", "DLF.NS", "IIFL.NS", "FSL.NS", "TITAN.NS", "CENTURYTEX.NS", "GALAXYSURF.NS", "HAVELLS.NS", "CESC.NS", "BIOCON.NS", "BSOFT.NS", "ORIENTELEC.NS", "3MINDIA.NS",
        "SUNTV.NS", "LAXMIMACH.NS", "TATASTEEL.NS", "TVSMOTOR.NS", "SUVENPHAR.NS", "ASTERDM.NS"]
       
        ticker2=   ["NAM-INDIA.NS", "JKTYRE.NS", "PERSISTENT.NS", "CEATLTD.NS", "VIPIND.NS", "MARUTI.NS", "ASTRAL.NS", "ABFRL.NS", "DEEPAKNTR.NS", "HAPPSTMNDS.NS", "DALBHARAT.NS", "SHILPAMED.NS", "IBREALEST.NS", "ASTRAZEN.NS", "ECLERX.NS", "DCBBANK.NS", "CASTROLIND.NS", "PFIZER.NS", "EIHOTEL.NS", "ZENSARTECH.NS", "PEL.NS", "BAJAJ-AUTO.NS", "MHRIL.NS", "BOSCHLTD.NS", "HAL.NS", "PIIND.NS", "BAJAJELEC.NS", "SUPREMEIND.NS", "SEQUENT.NS", "DBL.NS", "HINDALCO.NS", "DIVISLAB.NS", "SYMPHONY.NS", "JSLHISAR.NS", "MRF.NS", "IRCTC.NS", "LTI.NS", "CANBK.NS", "VEDL.NS", "OBEROIRLTY.NS", "JKCEMENT.NS", "TATAMOTORS.NS", "KOTAKBANK.NS", "JUSTDIAL.NS", "JSWSTEEL.NS", "PGHL.NS", "BIRLACORPN.NS", "KNRCON.NS", "TANLA.NS", "OIL.NS", "RAJESHEXPO.NS", "POLYCAB.NS", "SIS.NS", "WESTLIFE.NS", "LAOPALA.NS", "HEMIPROP.NS","SCHNEIDER.NS", "BASF.NS", "GRASIM.NS", "JKPAPER.NS", "CAPLIPOINT.NS", "BPCL.NS", "INDIACEM.NS", "WOCKPHARMA.NS", "WABCOINDIA.NS", "KANSAINER.NS", "TATAPOWER.NS", "PRINCEPIPE.NS", "GMMPFAUDLR.NS", "BRITANNIA.NS", "INOXLEISUR.NS", "PETRONET.NS", "TATAMTRDVR.NS", "IGL.NS", "JMFINANCIL.NS", "UBL.NS", "GREAVESCOT.NS", "IFBIND.NS", "RAIN.NS", "WELCORP.NS", "RADICO.NS", "JKLAKSHMI.NS", "PAGEIND.NS", "SOLARINDS.NS", "TORNTPOWER.NS", "NIACL.NS", "MAZDOCK.NS", "UTIAMC.NS", "RALLIS.NS", "HEG.NS", "INDIGO.NS", "RECLTD.NS", "NATCOPHARM.NS", "ITC.NS", "DRREDDY.NS", "AMARAJABAT.NS", "HATSUN.NS", "GODREJAGRO.NS", "RHIM.NS", "MAHSCOOTER.NS", "LUXIND.NS", "VINATIORGA.NS", "VENKEYS.NS", "GLAXO.NS", "SUNPHARMA.NS", "GSPL.NS", "WELSPUNIND.NS", "KEC.NS", "GRAPHITE.NS", "GULFOILLUB.NS", "TATAINVEST.NS", "MGL.NS", "VARROC.NS", "JBCHEPHARM.NS", "SHOPERSTOP.NS", "PFC.NS", "DMART.NS", "CHALET.NS", "CADILAHC.NS",
        "TTKPRESTIG.NS", "POLYPLEX.NS", "NTPC.NS", "EPL.NS", "HINDCOPPER.NS", "AARTIDRUGS.NS", "ABBOTINDIA.NS", "M&MFIN.NS", "SRF.NS", "INFY.NS", "MIDHANI.NS", "ASIANPAINT.NS", "STAR.NS", "BAJAJHLDNG.NS", "INGERRAND.NS", "RBLBANK.NS", "SRTRANSFIN.NS", "VOLTAS.NS", "AMBUJACEM.NS", "BALMLAWRIE.NS", "GILLETTE.NS", "AUROPHARMA.NS", "BDL.NS", "DHANI.NS", "ESCORTS.NS", "COROMANDEL.NS", "BALKRISIND.NS", "EDELWEISS.NS", "JSWENERGY.NS", "HDFCAMC.NS", "APOLLOTYRE.NS", "MOIL.NS", "SBIN.NS", "ROUTE.NS", "BBTC.NS", "INDIANB.NS", "SCI.NS", "AJANTPHARM.NS", "QUESS.NS", "BLUESTARCO.NS", "ADANIPORTS.NS", "SUDARSCHEM.NS", "MOTILALOFS.NS", "EIDPARRY.NS", "CHOLAHLDNG.NS", "LUPIN.NS", "WIPRO.NS", "GESHIP.NS", "GICRE.NS", "ISEC.NS", "MINDTREE.NS"]
        ticker3= ["AAVAS.NS", "RATNAMANI.NS", "GLENMARK.NS", "BANDHANBNK.NS", "AKZOINDIA.NS", "VSTIND.NS", "TECHM.NS", "AUBANK.NS", "ATUL.NS", "KEI.NS", "GUJGASLTD.NS", "DHANUKA.NS", "ERIS.NS", "VALIANTORG.NS", "CHAMBLFERT.NS", "JTEKTINDIA.NS", "ADANIENT.NS", "ITI.NS", "FLUOROCHEM.NS", "NAVINFLUOR.NS", "OFSS.NS", "SUNDARMFIN.NS", "DABUR.NS", "FINCABLES.NS", "FEDERALBNK.NS", "HEIDELBERG.NS", "HINDZINC.NS", "SHARDACROP.NS", "GLAND.NS", "PVR.NS", "CUMMINSIND.NS", "CENTURYPLY.NS", "ICICIGI.NS", "BURGERKING.NS", "MAXHEALTH.NS", "BAJFINANCE.NS", "CIPLA.NS", "KPITTECH.NS", "ICICIBANK.NS", "COLPAL.NS", "NH.NS", "CSBBANK.NS", "DELTACORP.NS", "TATACOMM.NS", "CYIENT.NS", "LICHSGFIN.NS", "TEAMLEASE.NS", "UPL.NS", "SYNGENE.NS", "TIMKEN.NS", "GSFC.NS", "WHIRLPOOL.NS", "PHILIPCARB.NS", "M&M.NS", "MARICO.NS", "KAJARIACER.NS", "CGCL.NS",
         "KSB.NS", "L&TFH.NS", "ADVENZYMES.NS", "PGHH.NS", "BLISSGVS.NS", "STARCEMENT.NS", "HCLTECH.NS", "GPPL.NS", "GODFRYPHLP.NS", "SUMICHEM.NS", "BRIGADE.NS", "GEPIL.NS", "IOLCP.NS", "GUJALKALI.NS", "NESTLEIND.NS", "SBILIFE.NS", "SUPRAJIT.NS", "NOCIL.NS", "TCS.NS", "GNFC.NS", "IBULHSGFIN.NS", "BEML.NS", "BALRAMCHIN.NS", "UJJIVAN.NS", "SUNCLAYLTD.NS", "VTL.NS", "INDUSINDBK.NS", "KALPATPOWR.NS", "NESCO.NS", "RAMCOCEM.NS", "SHREECEM.NS", "CANFINHOME.NS", "PIDILITIND.NS", "LAURUSLABS.NS", "NILKAMAL.NS", "ZYDUSWELL.NS", "GRANULES.NS", "JCHAC.NS", "AARTIIND.NS", "APLAPOLLO.NS", "JUBLFOOD.NS", "AEGISCHEM.NS", "SWANENERGY.NS", "POLYMED.NS", "AFFLE.NS", "AVANTIFEED.NS", "POWERGRID.NS", "HONAUT.NS", "TATACHEM.NS", "VMART.NS", "BHARTIARTL.NS", "HUHTAMAKI.NS", "PRSMJOHNSN.NS", "BATAINDIA.NS", "RAYMOND.NS", "LALPATHLAB.NS", "LT.NS", "APOLLOHOSP.NS", "CRISIL.NS", "GODREJPROP.NS", "TATACONSUM.NS", "UFLEX.NS", "JYOTHYLAB.NS", "HDFCBANK.NS", "BERGEPAINT.NS", "JAMNAAUTO.NS", "ASHOKLEY.NS",
               
        "CROMPTON.NS", "PNBHOUSING.NS", "SPANDANA.NS", "THERMAX.NS", "ADANIGREEN.NS",
                "APLLTD.NS", "BAJAJFINSV.NS", "ULTRACEMCO.NS", "TATAELXSI.NS", "FDC.NS", "TATACOFFEE.NS", "BHARATRAS.NS", "SIEMENS.NS", "SANOFI.NS", "CCL.NS", "HDFC.NS", "GODREJCP.NS", "INDIAMART.NS", "ASHOKA.NS", "ALKYLAMINE.NS", "METROPOLIS.NS", "SPARC.NS", "AXISBANK.NS", "MANAPPURAM.NS", "ABCAPITAL.NS", "CONCOR.NS", "TASTYBITE.NS", "IIFLWAM.NS", "MAHINDCIE.NS", "MINDACORP.NS", "DIXON.NS", "TRENT.NS", "INDOCO.NS", "BALAMINES.NS", "ROSSARI.NS", "TIINDIA.NS", "TCNSBRANDS.NS", "HINDUNILVR.NS", "MUTHOOTFIN.NS", "SBICARD.NS", "GRSE.NS", "ACC.NS", "CHOLAFIN.NS", "BAYERCROP.NS", "SUPPETRO.NS", "AMBER.NS", "REDINGTON.NS", "CAMS.NS", "THYROCARE.NS", "INDHOTEL.NS", "ALKEM.NS", "GAEL.NS", "RITES.NS", "INTELLECT.NS", "CREDITACC.NS", "ENDURANCE.NS", "SFL.NS", "MAHLOG.NS", "CUB.NS", "BAJAJCON.NS", "TRITURBINE.NS", "MINDAIND.NS", "NAUKRI.NS", "SWSOLAR.NS", "EQUITAS.NS", "ABB.NS", "ATGL.NS", "MFSL.NS", "PHOENIXLTD.NS", "HDFCLIFE.NS", "IEX.NS", "ALEMBICLTD.NS",
        ]

        df1=yf.download(tickers=ticker1, period='7d', interval='1d')
        df2=yf.download(tickers=ticker2, period='7d', interval='1d')
        df3=yf.download(tickers=ticker3, period='7d', interval='1d')
        
        
        for df in [df1,df2,df3]:
            rat = df['Close'].pct_change()*100 > 2
            rat_last=rat[-1:]
            pct_change= df['Close'].pct_change()
            pct_change=pd.DataFrame(pct_change*100)
            final=pct_change[-1:][rat_last].dropna(axis=1)
            final=final.transpose()

            final.rename(columns={final.columns[0]:'Change %'}, inplace=True)
            text=final.sort_values(by=['Change %'],ascending =False)



            pct_change1= df['Volume'].pct_change()
            pct_change1=pd.DataFrame(pct_change1*100)
            final1=pct_change1[-1:][rat_last].dropna(axis=1)
            final1=final1.transpose()

            final1.rename(columns={final1.columns[0]:'Volume increased'}, inplace=True)
            text1=final1.sort_values(by=['Volume increased'],ascending =False)
            text1['Volume increased']= text1['Volume increased']/100 +1


            text_f=pd.concat([(text), (text1)], axis=1, join="inner")
       

    
            list1=["*-------Breaking Volume List--------*","*BULLish/ Breakout change*",text_f]
        
            for x in list1:
                bot_token='1871182021:AAH565P-1lku9NPFyemEwUFIOFj2_nVmj-A'
                bot_chatID='1967629084'
                send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
                response=requests.get(send_text)        
                  
 #****************************************************************************************************************************************       
#end report
def time8():
    

    bot_token='5912968938:AAGiqriA5OnLJ9T4dOVPm0PdGBYLDdkvnHo'
    bot_chatID='715631635'
    weekno = datetime.today().weekday()
    
    if (weekno < 5):
        ticker1=["SCHNEIDER.NS", "BASF.NS", "GRASIM.NS", "JKPAPER.NS", "CAPLIPOINT.NS", "BPCL.NS", "INDIACEM.NS", "WOCKPHARMA.NS",  "KANSAINER.NS", "TATAPOWER.NS", "PRINCEPIPE.NS", "GMMPFAUDLR.NS", "BRITANNIA.NS",  "PETRONET.NS", "TATAMTRDVR.NS", "IGL.NS", "JMFINANCIL.NS", "UBL.NS", "GREAVESCOT.NS", "IFBIND.NS", "RAIN.NS", "WELCORP.NS", "RADICO.NS", "JKLAKSHMI.NS", "PAGEIND.NS", "SOLARINDS.NS", "TORNTPOWER.NS", "NIACL.NS", "MAZDOCK.NS", "UTIAMC.NS", "RALLIS.NS", "HEG.NS", "INDIGO.NS", "RECLTD.NS", "NATCOPHARM.NS", "ITC.NS", "DRREDDY.NS", "AMARAJABAT.NS", "HATSUN.NS", "GODREJAGRO.NS", "RHIM.NS", "MAHSCOOTER.NS", "LUXIND.NS", "VINATIORGA.NS", "VENKEYS.NS", "GLAXO.NS", "SUNPHARMA.NS", "GSPL.NS", "WELSPUNIND.NS", "KEC.NS", "GRAPHITE.NS", "GULFOILLUB.NS", "TATAINVEST.NS", "MGL.NS", "VARROC.NS", "JBCHEPHARM.NS", "SHOPERSTOP.NS", "PFC.NS", "DMART.NS", "CHALET.NS","PRESTIGE.NS", "LTTS.NS", "EXIDEIND.NS", "GRINDWELL.NS", "VAIBHAVGBL.NS", 
            "NATIONALUM.NS", "LINDEINDIA.NS", "SOBHA.NS", "AIAENG.NS", "DCMSHRIRAM.NS", "MCX.NS", "JINDALSAW.NS", "FINEORG.NS", "BEL.NS", "ICIL.NS", "STLTECH.NS", "JINDALSTEL.NS", "GODREJIND.NS", "ONGC.NS", "FORTIS.NS", "ADANITRANS.NS", "DCAL.NS", "IRB.NS", "CERA.NS", "RELIANCE.NS", "SCHAEFFLER.NS", "CARBORUNIV.NS", "ASAHIINDIA.NS", "GARFIBRES.NS", "VGUARD.NS", "HINDPETRO.NS", "SKFINDIA.NS", "SAIL.NS", "EICHERMOT.NS", "HEROMOTOCO.NS", "IOC.NS", "COALINDIA.NS", "VBL.NS", "ZEEL.NS",
                
         "INDUSTOWER.NS", "BLUEDART.NS", "JSL.NS", "GAIL.NS", "PNCINFRA.NS", "MASFIN.NS", "KPRMILL.NS", "IPCALAB.NS", "CDSL.NS", "FINPIPE.NS", "KRBL.NS", "MPHASIS.NS", "ELGIEQUIP.NS", "SUNTECK.NS", "NMDC.NS", "SUNDRMFAST.NS", "ICICIPRULI.NS", "MCDOWELL-N.NS", "EMAMILTD.NS", "POWERINDIA.NS", "KSCL.NS",  "RESPONIND.NS", "MAHSEAMLES.NS", "SONATSOFTW.NS", "TORNTPHARM.NS", "RELAXO.NS", "COCHINSHIP.NS", "SOLARA.NS", "TCIEXP.NS", "COFORGE.NS", "BSE.NS", "BHARATFORG.NS", "DLF.NS", "IIFL.NS", "FSL.NS", "TITAN.NS", "CENTURYTEX.NS", "GALAXYSURF.NS", "HAVELLS.NS", "CESC.NS", "BIOCON.NS", "BSOFT.NS", "ORIENTELEC.NS", "3MINDIA.NS",
        "SUNTV.NS", "LAXMIMACH.NS", "TATASTEEL.NS", "TVSMOTOR.NS", "SUVENPHAR.NS", "ASTERDM.NS", "NAM-INDIA.NS", "JKTYRE.NS", "PERSISTENT.NS", "CEATLTD.NS", "VIPIND.NS", "MARUTI.NS", "ASTRAL.NS", "ABFRL.NS", "DEEPAKNTR.NS", "HAPPSTMNDS.NS", "DALBHARAT.NS", "SHILPAMED.NS", "IBREALEST.NS", "ASTRAZEN.NS", "ECLERX.NS", "DCBBANK.NS", "CASTROLIND.NS", "PFIZER.NS", "EIHOTEL.NS", "ZENSARTECH.NS", "PEL.NS", "BAJAJ-AUTO.NS", "MHRIL.NS", "BOSCHLTD.NS", "HAL.NS", "PIIND.NS", "BAJAJELEC.NS", "SUPREMEIND.NS", "SEQUENT.NS", "DBL.NS", "HINDALCO.NS", "DIVISLAB.NS", "SYMPHONY.NS", "JSLHISAR.NS", "MRF.NS", "IRCTC.NS",  "CANBK.NS", "VEDL.NS", "OBEROIRLTY.NS", "JKCEMENT.NS", "TATAMOTORS.NS", "KOTAKBANK.NS", "JUSTDIAL.NS", "JSWSTEEL.NS", "PGHL.NS", "BIRLACORPN.NS", "KNRCON.NS", "TANLA.NS", "OIL.NS", "RAJESHEXPO.NS", "POLYCAB.NS", "SIS.NS", "WESTLIFE.NS", "LAOPALA.NS", "HEMIPROP.NS"]
       
        ticker2=   [        "TTKPRESTIG.NS", "POLYPLEX.NS", "NTPC.NS", "EPL.NS", "HINDCOPPER.NS", "AARTIDRUGS.NS", "ABBOTINDIA.NS", "M&MFIN.NS", "SRF.NS", "INFY.NS", "MIDHANI.NS", "ASIANPAINT.NS", "STAR.NS", "BAJAJHLDNG.NS", "INGERRAND.NS", "RBLBANK.NS",  "VOLTAS.NS", "AMBUJACEM.NS", "BALMLAWRIE.NS", "GILLETTE.NS", "AUROPHARMA.NS", "BDL.NS", "DHANI.NS", "ESCORTS.NS", "COROMANDEL.NS", "BALKRISIND.NS", "EDELWEISS.NS", "JSWENERGY.NS", "HDFCAMC.NS", "APOLLOTYRE.NS", "MOIL.NS", "SBIN.NS", "ROUTE.NS", "BBTC.NS", "INDIANB.NS", "SCI.NS", "AJANTPHARM.NS", "QUESS.NS", "BLUESTARCO.NS", "ADANIPORTS.NS", "SUDARSCHEM.NS", "MOTILALOFS.NS", "EIDPARRY.NS", "CHOLAHLDNG.NS", "LUPIN.NS", "WIPRO.NS", "GESHIP.NS", "GICRE.NS", "ISEC.NS", 
        "AAVAS.NS", "RATNAMANI.NS", "GLENMARK.NS", "BANDHANBNK.NS", "AKZOINDIA.NS", "VSTIND.NS", "TECHM.NS", "AUBANK.NS", "ATUL.NS", "KEI.NS", "GUJGASLTD.NS", "DHANUKA.NS", "ERIS.NS", "VALIANTORG.NS", "CHAMBLFERT.NS", "JTEKTINDIA.NS", "ADANIENT.NS", "ITI.NS", "FLUOROCHEM.NS", "NAVINFLUOR.NS", "OFSS.NS", "SUNDARMFIN.NS", "DABUR.NS", "FINCABLES.NS", "FEDERALBNK.NS", "HEIDELBERG.NS", "HINDZINC.NS", "SHARDACROP.NS", "GLAND.NS", "PVR.NS", "CUMMINSIND.NS", "CENTURYPLY.NS", "ICICIGI.NS", "MAXHEALTH.NS", "BAJFINANCE.NS", "CIPLA.NS", "KPITTECH.NS", "ICICIBANK.NS", "COLPAL.NS", "NH.NS", "CSBBANK.NS", "DELTACORP.NS", "TATACOMM.NS", "CYIENT.NS", "LICHSGFIN.NS", "TEAMLEASE.NS", "UPL.NS", "SYNGENE.NS", "TIMKEN.NS", "GSFC.NS", "WHIRLPOOL.NS",  "M&M.NS", "MARICO.NS", "KAJARIACER.NS", "CGCL.NS",
         "KSB.NS", "L&TFH.NS", "ADVENZYMES.NS", "PGHH.NS", "BLISSGVS.NS", "STARCEMENT.NS", "HCLTECH.NS", "GPPL.NS", "GODFRYPHLP.NS", "SUMICHEM.NS", "BRIGADE.NS", "GEPIL.NS", "IOLCP.NS", "GUJALKALI.NS", "NESTLEIND.NS", "SBILIFE.NS", "SUPRAJIT.NS", "NOCIL.NS", "TCS.NS", "GNFC.NS", "IBULHSGFIN.NS", "BEML.NS", "BALRAMCHIN.NS", "UJJIVAN.NS", "SUNCLAYLTD.NS", "VTL.NS", "INDUSINDBK.NS", "KALPATPOWR.NS", "NESCO.NS", "RAMCOCEM.NS", "SHREECEM.NS", "CANFINHOME.NS", "PIDILITIND.NS", "LAURUSLABS.NS", "NILKAMAL.NS", "ZYDUSWELL.NS", "GRANULES.NS", "JCHAC.NS", "AARTIIND.NS", "APLAPOLLO.NS", "JUBLFOOD.NS", "AEGISCHEM.NS", "SWANENERGY.NS", "POLYMED.NS", "AFFLE.NS", "AVANTIFEED.NS", "POWERGRID.NS", "HONAUT.NS", "TATACHEM.NS", "VMART.NS", "BHARTIARTL.NS", "HUHTAMAKI.NS", "PRSMJOHNSN.NS", "BATAINDIA.NS", "RAYMOND.NS", "LALPATHLAB.NS", "LT.NS", "APOLLOHOSP.NS", "CRISIL.NS", "GODREJPROP.NS", "TATACONSUM.NS", "UFLEX.NS", "JYOTHYLAB.NS", "HDFCBANK.NS", "BERGEPAINT.NS", "JAMNAAUTO.NS", "ASHOKLEY.NS",
               
        "CROMPTON.NS", "PNBHOUSING.NS", "SPANDANA.NS", "THERMAX.NS", "ADANIGREEN.NS",
                "APLLTD.NS", "BAJAJFINSV.NS", "ULTRACEMCO.NS", "TATAELXSI.NS", "FDC.NS", "TATACOFFEE.NS", "BHARATRAS.NS", "SIEMENS.NS", "SANOFI.NS", "CCL.NS", "HDFC.NS", "GODREJCP.NS", "INDIAMART.NS", "ASHOKA.NS", "ALKYLAMINE.NS", "METROPOLIS.NS", "SPARC.NS", "AXISBANK.NS", "MANAPPURAM.NS", "ABCAPITAL.NS", "CONCOR.NS", "TASTYBITE.NS",  "MAHINDCIE.NS", "MINDACORP.NS", "DIXON.NS", "TRENT.NS", "INDOCO.NS", "BALAMINES.NS", "ROSSARI.NS", "TIINDIA.NS", "TCNSBRANDS.NS", "HINDUNILVR.NS", "MUTHOOTFIN.NS", "SBICARD.NS", "GRSE.NS", "ACC.NS", "CHOLAFIN.NS", "BAYERCROP.NS","AMBER.NS", "REDINGTON.NS", "CAMS.NS", "THYROCARE.NS", "INDHOTEL.NS", "ALKEM.NS", "GAEL.NS", "RITES.NS", "INTELLECT.NS", "CREDITACC.NS", "ENDURANCE.NS", "SFL.NS", "MAHLOG.NS", "CUB.NS", "BAJAJCON.NS", "TRITURBINE.NS", "NAUKRI.NS", "SWSOLAR.NS",  "ABB.NS", "ATGL.NS", "MFSL.NS", "PHOENIXLTD.NS", "HDFCLIFE.NS", "IEX.NS", "ALEMBICLTD.NS",
        ]

        df1=yf.download(tickers=ticker1, period='3mo', interval='1h')
        df2=yf.download(tickers=ticker2, period='3mo', interval='1h')
        
        
        for dat in [df1,df2]:
            
            df1=dat.dropna()
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
            
            new1=[]
            new2=[]
            
            
            for i in range(1,6):
                
                df1=dat.dropna()
                change=(df1['Close']-df1['Open'])*100/df1['Open']
                x=change[df1["Volume"]> 2*(df1['Volume'].rolling(150).mean())]
                y=x[(x>2)| (x<-2)]
                y1=y.iloc[-i].dropna()
                x1=  (df1["Volume"]- (df1['Volume'].rolling(100).mean()))/(df1['Volume'].rolling(150).mean())
                x2=x1[(x>2)| (x<-2)].iloc[-i].dropna()
                y11=pd.DataFrame(y1)
                x22=pd.DataFrame(x2)
                (y11).rename(columns={y11.columns[0]:'Change %'}, inplace=True)
                (x22).rename(columns={x22.columns[0]:'Volumne increased'}, inplace=True)
                text1=pd.concat([(y11), (x22)], axis=1, join="inner")
                jon1 = pd.concat([(text1), (dff)], axis=1, join="inner")
                text2=jon1[['up_from_low','down_from_high']]
    
                text1= round(text1,2)
                text2= round(text2,2)
                new1.append(text1)
                new2.append(text2)
            
            
                
            text1=new1
            text2=new2
    
            list1=["*-------Breaking Volume Details--------*","*BULLish/ Breakout change*",text1, "*From high low position*",text2]
    
            for x in list1:    
                send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
                response=requests.get(send_text)     

                
#****************************************************************************************************************************************       
                
                
schedule.clear()

#schedule BN bigmoves

schedule.every(61).seconds.do(time5)


# schedule closing status
schedule.every().day.at("10:02").do(time2)

# schedule opening status
schedule.every().day.at("03:48").do(time3)

#schedule Intrabreakout
schedule.every().day.at("04:32").do(time1)

schedule.every().day.at("05:02").do(time1)
schedule.every().day.at("05:32").do(time1)

schedule.every().day.at("06:03").do(time1)
schedule.every().day.at("06:33").do(time1)

schedule.every().day.at("07:03").do(time1)
schedule.every().day.at("07:33").do(time1)

schedule.every().day.at("08:03").do(time1)
schedule.every().day.at("08:33").do(time1)

schedule.every().day.at("09:32").do(time1)
schedule.every().day.at("09:02").do(time1)


#schedule current market status

schedule.every().day.at("06:15").do(time4)
schedule.every().day.at("06:45").do(time4)

schedule.every().day.at("07:15").do(time4)
schedule.every().day.at("07:45").do(time4)


schedule.every().day.at("08:00").do(time4)


schedule.every().day.at("08:15").do(time4)
schedule.every().day.at("08:45").do(time4)

schedule.every().day.at("09:30").do(time4)
schedule.every().day.at("09:45").do(time4)

#-----------------------------------------------------    

schedule.every().day.at("04:47").do(time6)
schedule.every().day.at("05:47").do(time6)

schedule.every().day.at("06:47").do(time6)
schedule.every().day.at("07:47").do(time6)

schedule.every().day.at("08:47").do(time6)
schedule.every().day.at("09:47").do(time6)

schedule.every().day.at("10:03").do(time7)

schedule.every().day.at("10:06").do(time8)

while True:
    schedule.run_pending()
    time.sleep(1)
