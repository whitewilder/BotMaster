import requests
import pandas as pd
import yfinance as yf
import time
import schedule
from datetime import datetime

import schedule 
import time
from datetime import datetime



def time1():
    now = datetime.now()
    bot_token='1882490416:AAH9c4S-_ez4J9a-AKaIxj6nm2NA_qhtYLU'
    bot_chatID='715631635'
    
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
        
def time2():
    bot_token='1882490416:AAH9c4S-_ez4J9a-AKaIxj6nm2NA_qhtYLU'
    bot_chatID='715631635'
    
    all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS","AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
   

    df=yf.download(tickers=all_ticker, period='1d', interval='1d')
    df1= (df['Close']-df['Open'])*100/df['Open']


    text1 = df1[df1>2][df1<4].dropna(axis=1).transpose()
    text1.rename(columns={text1.columns[0]:'Change'}, inplace=True)
    text1=text1.sort_values(by=['Change'],ascending =False)

    text2 = df1[df1>4].dropna(axis=1).transpose()
    text2.rename(columns={text2.columns[0]:'Change'}, inplace=True)
    text2=text2.sort_values(by=['Change'],ascending =False)


    text3 = df1[df1<-2][df1>-4].dropna(axis=1).transpose()
    
    text4 = df1[df1<-4].dropna(axis=1).transpose()

    list1=["*Heavy BULLish*",text2, "*Moderate BULL*",text1, "*Bear*", text3, "*Heavy Bear*", text4]
    
    for x in list1:    
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
        response=requests.get(send_text)

        
        
def time3():
    bot_token='1882490416:AAH9c4S-_ez4J9a-AKaIxj6nm2NA_qhtYLU'
    bot_chatID='715631635'
    
    all_ticker=["AMARAJABAT.NS","HDFC.NS","BAJFINANCE.NS","BATAINDIA.NS","BEL.NS","EXIDEIND.NS",
            "CIPLA.NS","DABUR.NS","BHEL.NS","HINDPETRO.NS","SBIN.NS","SAIL.NS","TITAN.NS","DRREDDY.NS","HDFCBANK.NS","HEROMOTOCO.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","TRENT.NS","LICHSGFIN.NS","LUPIN.NS","RAMCOCEM.NS","MFSL.NS","VEDL.NS","GRASIM.NS","PEL.NS","ONGC.NS","RELIANCE.NS","PIDILITIND.NS","TATAPOWER.NS","ACC.NS","TORNTPHARM.NS","AMBUJACEM.NS","HINDALCO.NS","FEDERALBNK.NS","TATASTEEL.NS","ASHOKLEY.NS","CUMMINSIND.NS","BHARATFORG.NS","ESCORTS.NS","LT.NS","M&M.NS","BPCL.NS","SIEMENS.NS","TATAMOTORS.NS","VOLTAS.NS","HINDUNILVR.NS","TATACHEM.NS","TATACONSUM.NS","ASIANPAINT.NS","BRITANNIA.NS","COLPAL.NS","ITC.NS","APOLLOTYRE.NS","BALKRISIND.NS","SRF.NS","EICHERMOT.NS","ZEEL.NS","DEEPAKNTR.NS","WIPRO.NS","APOLLOHOSP.NS","BERGEPAINT.NS","SRTRANSFIN.NS","CHOLAFIN.NS","UPL.NS","ADANIENT.NS","MOTHERSUMI.NS","HAVELLS.NS","PIIND.NS","AARTIIND.NS","AUBANK.NS","SUNPHARMA.NS","AUROPHARMA.NS","MPHASIS.NS","NMDC.NS","SBILIFE.NS","ICICIGI.NS","NAM-INDIA.NS","HDFCLIFE.NS","BANDHANBNK.NS","HDFCAMC.NS","IOC.NS","MANAPPURAM.NS","CONCOR.NS","MARICO.NS","IRCTC.NS","BANKBARODA.NS","GAIL.NS","ICICIBANK.NS","INDUSINDBK.NS","CUB.NS","AXISBANK.NS","NATIONALUM.NS","HCLTECH.NS","JINDALSTEL.NS","GLENMARK.NS","CADILAHC.NS","TVSMOTOR.NS","GODREJCP.NS","MCDOWELL-N.NS","BHARTIARTL.NS","PNB.NS","UBL.NS","GRANULES.NS","CANBK.NS","DIVISLAB.NS","MARUTI.NS","IGL.NS","PETRONET.NS","BIOCON.NS","ULTRACEMCO.NS","TCS.NS","COFORGE.NS","NTPC.NS","PVR.NS","M&MFIN.NS","SUNTV.NS","GMRINFRA.NS","TECHM.NS","NAUKRI.NS","TORNTPOWER.NS","PFC.NS","MINDTREE.NS","IDEA.NS","DLF.NS","POWERGRID.NS","ADANIPORTS.NS","RECLTD.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","GODREJPROP.NS","JUBLFOOD.NS","COALINDIA.NS","MUTHOOTFIN.NS","L&TFH.NS","APLLTD.NS","INDUSTOWER.NS","IBULHSGFIN.NS","GUJGASLTD.NS","IDFCFIRSTB.NS","INDIGO.NS","ALKEM.NS","LALPATHLAB.NS","MGL.NS","LTI.NS","RBLBANK.NS","ICICIPRULI.NS","NAVINFLUOR.NS","PAGEIND.NS","LTTS.NS","SHREECEM.NS",
            "NESTLEIND.NS","BOSCHLTD.NS","PFIZER.NS","^NSEI","^NSEBANK","MRF.NS"]
           
        
    df1=yf.download(tickers=all_ticker, period='2d', interval='2m')
    df1= df1.reset_index()

    a1=(df1['Close'].iloc[188]-df1['Close'].iloc[187])*100 / df1['Close'].iloc[187]
    
    text1=a1[a1>.9] 
    text2=a1[a1<-.9] 
    list1=["*BULLish Opening*",text1, "*Bearish Opening*",text2]
    
    for x in list1:    
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
        response=requests.get(send_text)
          
 #****************************************************************************************************************************************       

schedule.clear()

schedule.every().day.at("09:03").do(time1)
schedule.every().day.at("10:02").do(time2)
schedule.every().day.at("03:48").do(time3)
schedule.every().day.at("05:03").do(time1)
schedule.every().day.at("06:03").do(time1)
schedule.every().day.at("07:03").do(time1)
schedule.every().day.at("08:03").do(time1)
schedule.every().day.at("09:33").do(time1)


    

while True:
    schedule.run_pending()
    time.sleep(1)
