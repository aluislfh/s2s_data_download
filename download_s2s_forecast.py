#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os, sys, glob
import numpy as np

def main():

    wdir = '/home/adrian/NWP/S2S_Forecast/Data_S2S/data'
    os.chdir(wdir)

    for model,name in zip(['ammc','babj','isac','lfpw','cwao','ecmf','rums','anso','rjtd','rksl','kwbc','egrr'], ['BoM','CMA','CNR-ISAC','CNRM','ECCC','ECMWF','HMCR','IAP-CAS','JMA','KMA','NCEP','UKMO']):

        for yyyy in np.array(np.arange(2015,2024,1),dtype='str'):
            for mm in np.array(np.arange(1,13,1),dtype='str'):
                print(yyyy, mm.zfill(2))

                # sst
                try:
                    daily_sst(yyyy, mm.zfill(2), model, name, wdir)
                except:
                    continue

                # plev
                try:
                    fcst_inst_plev(yyyy, mm.zfill(2), model, name, wdir)
                except:
                    continue

                # sfc
                try:
                    fcst_inst_sfc(yyyy, mm.zfill(2), model, name, wdir)
                except:
                    continue

                sys.exit()




def daily_sst(yyyy, mm, model, name, wdir):

    if not os.path.exists(wdir + "/sst_"+name+"_"+yyyy+"_"+mm+".grb2"):

        server = ECMWFDataServer()

        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levtype": "sfc",
            "model": "glob",
            "origin": model,
            "param": "34",
            "step": "0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720/720-744/744-768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "sst_"+name+"_"+yyyy+"_"+mm+".grb2"
        })



def fcst_inst_plev(yyyy, mm, model, name, wdir):

    if not os.path.exists(wdir + "/temps1_"+name+"_"+yyyy+"_"+mm+".grb2"):

        server = ECMWFDataServer()

        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levelist": "500/700",
            "levtype": "pl",
            "model": "glob",
            "origin": model,
            "param": "130/133",
            "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "temps1_"+name+"_"+yyyy+"_"+mm+".grb2"
        })

    if not os.path.exists(wdir + "/temps2_"+name+"_"+yyyy+"_"+mm+".grb2"):

        server = ECMWFDataServer()

        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levelist": "850/925",
            "levtype": "pl",
            "model": "glob",
            "origin": model,
            "param": "130/133",
            "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "temps2_"+name+"_"+yyyy+"_"+mm+".grb2"
        })

    if not os.path.exists(wdir + "/uwind_"+name+"_"+yyyy+"_"+mm+".grb2"):
        
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levelist": "50/200",
            "levtype": "pl",
            "model": "glob",
            "origin": model,
            "param": "131",
            "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "uwind_"+name+"_"+yyyy+"_"+mm+".grb2"
        })



def fcst_inst_sfc(yyyy, mm, model, name, wdir):

    if not os.path.exists(wdir + "/single_"+name+"_"+yyyy+"_"+mm+".grb2"):
        
        server = ECMWFDataServer()

        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levtype": "sfc",
            "model": "glob",
            "origin": model,
            "param": "134/151/179",
            "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "single_"+name+"_"+yyyy+"_"+mm+".grb2"
        })


    if not os.path.exists(wdir + "/rain_"+name+"_"+yyyy+"_"+mm+".grb2"):
        
        server.retrieve({
            "class": "s2",
            "dataset": "s2s",
            "date": yyyy+"-"+mm+"-01/"+yyyy+"-"+mm+"-15",
            "expver": "prod",
            "levtype": "sfc",
            "model": "glob",
            "origin": model,
            "param": "228228",
            "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384/390/396/402/408/414/420/426/432/438/444/450/456/462/468/474/480/486/492/498/504/510/516/522/528/534/540/546/552/558/564/570/576/582/588/594/600/606/612/618/624/630/636/642/648/654/660/666/672/678/684/690/696/702/708/714/720/726/732/738/744/750/756/762/768",
            "stream": "enfo",
            "time": "00:00:00",
            "type": "cf",
            "target": "rain_"+name+"_"+yyyy+"_"+mm+".grb2"
        })




main()
