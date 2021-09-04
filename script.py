import requests
import pandas as pd
import yfinance as yf
import time
import schedule
import numpy as np
from datetime import datetime




#New idea hourly volume breakout
def time6():
    

    bot_token='1871182021:AAH565P-1lku9NPFyemEwUFIOFj2_nVmj-A'
    bot_chatID='1967629084'
    weekno = datetime.today().weekday()
    
    if (weekno < 7):
        ticker=["PRESTIGE.NS", "LTTS.NS", "ANGELBRKG.NS", "EXIDEIND.NS", "GRINDWELL.NS", "VAIBHAVGBL.NS", 
            "NATIONALUM.NS", "LINDEINDIA.NS", "SOBHA.NS", "AIAENG.NS", "DCMSHRIRAM.NS", "MCX.NS", "JINDALSAW.NS", "FINEORG.NS", "BEL.NS", "ICIL.NS", "STLTECH.NS", "JINDALSTEL.NS", "GODREJIND.NS", "ONGC.NS", "FORTIS.NS", "ADANITRANS.NS", "DCAL.NS", "IRB.NS", "CERA.NS", "RELIANCE.NS", "SCHAEFFLER.NS", "CARBORUNIV.NS", "ASAHIINDIA.NS", "GARFIBRES.NS", "VGUARD.NS", "HINDPETRO.NS", "SKFINDIA.NS", "SAIL.NS", "EICHERMOT.NS", "HEROMOTOCO.NS", "IOC.NS", "COALINDIA.NS", "VBL.NS", "ZEEL.NS", "INDUSTOWER.NS", "BLUEDART.NS", "JSL.NS", "GAIL.NS", "PNCINFRA.NS", "MASFIN.NS", "KPRMILL.NS", "IPCALAB.NS", "CDSL.NS", "FINPIPE.NS", "KRBL.NS", "MPHASIS.NS", "ELGIEQUIP.NS", "SUNTECK.NS", "NMDC.NS", "SUNDRMFAST.NS", "ICICIPRULI.NS", "MCDOWELL-N.NS", "EMAMILTD.NS", "POWERINDIA.NS", "KSCL.NS", "SHRIRAMCIT.NS", "RESPONIND.NS", "MAHSEAMLES.NS", "SONATSOFTW.NS", "TORNTPHARM.NS", "RELAXO.NS", "COCHINSHIP.NS", "SOLARA.NS", "TCIEXP.NS", "COFORGE.NS", "BSE.NS", "BHARATFORG.NS", "DLF.NS", "IIFL.NS", "FSL.NS", "TITAN.NS", "CENTURYTEX.NS", "GALAXYSURF.NS", "HAVELLS.NS", "CESC.NS", "BIOCON.NS", "BSOFT.NS", "ORIENTELEC.NS", "3MINDIA.NS", "SUNTV.NS", "LAXMIMACH.NS", "TATASTEEL.NS", "TVSMOTOR.NS", "SUVENPHAR.NS", "ASTERDM.NS", "NAM-INDIA.NS", "JKTYRE.NS", "PERSISTENT.NS", "CEATLTD.NS", "VIPIND.NS", "MARUTI.NS", "ASTRAL.NS", "ABFRL.NS", "DEEPAKNTR.NS", "HAPPSTMNDS.NS", "DALBHARAT.NS", "SHILPAMED.NS", "IBREALEST.NS", "ASTRAZEN.NS", "ECLERX.NS", "DCBBANK.NS", "CASTROLIND.NS", "PFIZER.NS", "EIHOTEL.NS", "ZENSARTECH.NS", "PEL.NS", "BAJAJ-AUTO.NS", "MHRIL.NS", "BOSCHLTD.NS", "HAL.NS", "PIIND.NS", "BAJAJELEC.NS", "SUPREMEIND.NS", "SEQUENT.NS", "DBL.NS", "HINDALCO.NS", "DIVISLAB.NS", "SYMPHONY.NS", "JSLHISAR.NS", "MRF.NS", "IRCTC.NS", "LTI.NS", "CANBK.NS", "VEDL.NS", "OBEROIRLTY.NS", "JKCEMENT.NS", "TATAMOTORS.NS", "KOTAKBANK.NS", "JUSTDIAL.NS", "JSWSTEEL.NS", "PGHL.NS", "BIRLACORPN.NS", "KNRCON.NS", "TANLA.NS", "OIL.NS", "RAJESHEXPO.NS", "POLYCAB.NS", "SIS.NS", "WESTLIFE.NS", "LAOPALA.NS", "HEMIPROP.NS", "SCHNEIDER.NS", "BASF.NS", "GRASIM.NS", "JKPAPER.NS", "CAPLIPOINT.NS", "BPCL.NS", "INDIACEM.NS", "WOCKPHARMA.NS", "WABCOINDIA.NS", "KANSAINER.NS", "TATAPOWER.NS", "PRINCEPIPE.NS", "GMMPFAUDLR.NS", "BRITANNIA.NS", "INOXLEISUR.NS", "PETRONET.NS", "TATAMTRDVR.NS", "IGL.NS", "JMFINANCIL.NS", "UBL.NS", "GREAVESCOT.NS", "IFBIND.NS", "RAIN.NS", "WELCORP.NS", "RADICO.NS", "JKLAKSHMI.NS", "PAGEIND.NS", "SOLARINDS.NS", "TORNTPOWER.NS", "NIACL.NS", "MAZDOCK.NS", "UTIAMC.NS", "RALLIS.NS", "HEG.NS", "INDIGO.NS", "RECLTD.NS", "NATCOPHARM.NS", "ITC.NS", "DRREDDY.NS", "AMARAJABAT.NS", "HATSUN.NS", "GODREJAGRO.NS", "RHIM.NS", "MAHSCOOTER.NS", "LUXIND.NS", "VINATIORGA.NS", "VENKEYS.NS", "GLAXO.NS", "SUNPHARMA.NS", "GSPL.NS", "WELSPUNIND.NS", "KEC.NS", "GRAPHITE.NS", "GULFOILLUB.NS", "TATAINVEST.NS", "MGL.NS", "VARROC.NS", "JBCHEPHARM.NS", "SHOPERSTOP.NS", "PFC.NS", "DMART.NS", "CHALET.NS", "CADILAHC.NS", "TTKPRESTIG.NS", "POLYPLEX.NS", "NTPC.NS", "EPL.NS", "HINDCOPPER.NS", "AARTIDRUGS.NS", "ABBOTINDIA.NS", "M&MFIN.NS", "SRF.NS", "INFY.NS", "MIDHANI.NS", "ASIANPAINT.NS", "STAR.NS", "BAJAJHLDNG.NS", "INGERRAND.NS", "RBLBANK.NS", "SRTRANSFIN.NS", "VOLTAS.NS", "AMBUJACEM.NS", "BALMLAWRIE.NS", "GILLETTE.NS", "AUROPHARMA.NS", "BDL.NS", "DHANI.NS", "ESCORTS.NS", "COROMANDEL.NS", "BALKRISIND.NS", "EDELWEISS.NS", "JSWENERGY.NS", "HDFCAMC.NS", "APOLLOTYRE.NS", "MOIL.NS", "SBIN.NS", "ROUTE.NS", "BBTC.NS", "INDIANB.NS", "SCI.NS", "AJANTPHARM.NS", "QUESS.NS", "BLUESTARCO.NS", "ADANIPORTS.NS", "SUDARSCHEM.NS", "MOTILALOFS.NS", "EIDPARRY.NS", "CHOLAHLDNG.NS", "LUPIN.NS", "WIPRO.NS", "GESHIP.NS", "GICRE.NS", "ISEC.NS", "MINDTREE.NS", "AAVAS.NS", "RATNAMANI.NS", "GLENMARK.NS", "BANDHANBNK.NS", "AKZOINDIA.NS", "VSTIND.NS", "TECHM.NS", "AUBANK.NS", "ATUL.NS", "KEI.NS", "GUJGASLTD.NS", "DHANUKA.NS", "ERIS.NS", "VALIANTORG.NS", "CHAMBLFERT.NS", "JTEKTINDIA.NS", "ADANIENT.NS", "ITI.NS", "FLUOROCHEM.NS", "NAVINFLUOR.NS", "OFSS.NS", "SUNDARMFIN.NS", "DABUR.NS", "FINCABLES.NS", "FEDERALBNK.NS", "HEIDELBERG.NS", "HINDZINC.NS", "SHARDACROP.NS", "GLAND.NS", "PVR.NS", "CUMMINSIND.NS", "CENTURYPLY.NS", "ICICIGI.NS", "BURGERKING.NS", "MAXHEALTH.NS", "BAJFINANCE.NS", "CIPLA.NS", "KPITTECH.NS", "ICICIBANK.NS", "COLPAL.NS", "NH.NS", "CSBBANK.NS", "DELTACORP.NS", "TATACOMM.NS", "CYIENT.NS", "LICHSGFIN.NS", "TEAMLEASE.NS", "UPL.NS", "SYNGENE.NS", "TIMKEN.NS", "GSFC.NS", "WHIRLPOOL.NS", "PHILIPCARB.NS", "M&M.NS", "MARICO.NS", "KAJARIACER.NS", "CGCL.NS", "KSB.NS", "L&TFH.NS", "ADVENZYMES.NS", "PGHH.NS", "BLISSGVS.NS", "STARCEMENT.NS", "HCLTECH.NS", "GPPL.NS", "GODFRYPHLP.NS", "SUMICHEM.NS", "BRIGADE.NS", "GEPIL.NS", "IOLCP.NS", "GUJALKALI.NS", "NESTLEIND.NS", "SBILIFE.NS", "SUPRAJIT.NS", "NOCIL.NS", "TCS.NS", "GNFC.NS", "IBULHSGFIN.NS", "BEML.NS", "BALRAMCHIN.NS", "UJJIVAN.NS", "SUNCLAYLTD.NS", "VTL.NS", "INDUSINDBK.NS", "KALPATPOWR.NS", "NESCO.NS", "RAMCOCEM.NS", "SHREECEM.NS", "CANFINHOME.NS", "PIDILITIND.NS", "LAURUSLABS.NS", "NILKAMAL.NS", "ZYDUSWELL.NS", "GRANULES.NS", "JCHAC.NS", "AARTIIND.NS", "APLAPOLLO.NS", "JUBLFOOD.NS", "AEGISCHEM.NS", "SWANENERGY.NS", "POLYMED.NS", "AFFLE.NS", "AVANTIFEED.NS", "POWERGRID.NS", "HONAUT.NS", "TATACHEM.NS", "VMART.NS", "BHARTIARTL.NS", "HUHTAMAKI.NS", "PRSMJOHNSN.NS", "BATAINDIA.NS", "RAYMOND.NS", "LALPATHLAB.NS", "LT.NS", "APOLLOHOSP.NS", "CRISIL.NS", "GODREJPROP.NS", "TATACONSUM.NS", "UFLEX.NS", "JYOTHYLAB.NS", "HDFCBANK.NS", "BERGEPAINT.NS", "JAMNAAUTO.NS", "ASHOKLEY.NS", "CROMPTON.NS", "PNBHOUSING.NS", "SPANDANA.NS", "THERMAX.NS", "ADANIGREEN.NS", "APLLTD.NS", "BAJAJFINSV.NS", "ULTRACEMCO.NS", "TATAELXSI.NS", "FDC.NS", "TATACOFFEE.NS", "BHARATRAS.NS", "SIEMENS.NS", "SANOFI.NS", "CCL.NS", "HDFC.NS", "GODREJCP.NS", "INDIAMART.NS", "ASHOKA.NS", "ALKYLAMINE.NS", "METROPOLIS.NS", "SPARC.NS", "AXISBANK.NS", "MANAPPURAM.NS", "ABCAPITAL.NS", "CONCOR.NS", "TASTYBITE.NS", "IIFLWAM.NS", "MAHINDCIE.NS", "MINDACORP.NS", "DIXON.NS", "TRENT.NS", "INDOCO.NS", "BALAMINES.NS", "ROSSARI.NS", "TIINDIA.NS", "TCNSBRANDS.NS", "HINDUNILVR.NS", "MUTHOOTFIN.NS", "SBICARD.NS", "GRSE.NS", "ACC.NS", "CHOLAFIN.NS", "BAYERCROP.NS", "SUPPETRO.NS", "AMBER.NS", "REDINGTON.NS", "CAMS.NS", "THYROCARE.NS", "INDHOTEL.NS", "ALKEM.NS", "GAEL.NS", "RITES.NS", "INTELLECT.NS", "CREDITACC.NS", "ENDURANCE.NS", "SFL.NS", "MAHLOG.NS", "CUB.NS", "BAJAJCON.NS", "TRITURBINE.NS", "MINDAIND.NS", "NAUKRI.NS", "SWSOLAR.NS", "EQUITAS.NS", "ABB.NS", "ATGL.NS", "MFSL.NS", "PHOENIXLTD.NS", "HDFCLIFE.NS", "IEX.NS", "ALEMBICLTD.NS",
        ]

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
            bot_token='1871182021:AAH565P-1lku9NPFyemEwUFIOFj2_nVmj-A'
            bot_chatID='1967629084'
            send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(x)
            response=requests.get(send_text)        
        
 #****************************************************************************************************************************************       

schedule.clear()

schedule.every(300).seconds.do(time6)

while True:
    schedule.run_pending()
    time.sleep(1)
