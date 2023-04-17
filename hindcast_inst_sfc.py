#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

#In general it is organised, as a huge tree, with the indentation below, showing different levels down that tree:

#   centre (CMA, ECMWF, NCEP, JMA, ...)
#       reforecast
#           type of data (control forecast or perturbed forecast)
#               type of level (single level or pressure level or potential  temperature)
#                   model version date (2014-05-01 or ...)
#                       hindcast dates (2014-01-01 or 2014-01-02 or 2014-01-03, ...)
#                           time-steps
#                               members (for perturbed forecast)
#                                   levels (for pl or pt)
#                                      parameters


server = ECMWFDataServer()

server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2015-01-01",
    "expver": "prod",
    "hdate": "1995-01-01/1996-01-01/1997-01-01/1998-01-01/1999-01-01/2000-01-01/2001-01-01/2002-01-01/2003-01-01/2004-01-01/2005-01-01/2006-01-01/2007-01-01/2008-01-01/2009-01-01/2010-01-01/2011-01-01/2012-01-01/2013-01-01/2014-01-01",
    "levtype": "sfc",
    "model": "glob",
    "origin": "ecmf",
    "param": "134/151/177/179",
    "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
    "stream": "enfh",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2015-01-01",
    "expver": "prod",
    "hdate": "1995-01-01/1996-01-01/1997-01-01/1998-01-01/1999-01-01/2000-01-01/2001-01-01/2002-01-01/2003-01-01/2004-01-01/2005-01-01/2006-01-01/2007-01-01/2008-01-01/2009-01-01/2010-01-01/2011-01-01/2012-01-01/2013-01-01/2014-01-01",
    "levtype": "sfc",
    "model": "glob",
    "origin": "ecmf",
    "param": "228228",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384/390/396/402/408/414/420/426/432/438/444/450/456/462/468/474/480/486/492/498/504/510/516/522/528/534/540/546/552/558/564/570/576/582/588/594/600/606/612/618/624/630/636/642/648/654/660/666/672/678/684/690/696/702/708/714/720/726/732/738/744/750/756/762/768",
    "stream": "enfh",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})
