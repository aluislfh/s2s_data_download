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
    "date": "2015-01-01/2015-01-05/2015-01-08/2015-01-12/2015-01-15/2015-01-19/2015-01-22/2015-01-26/2015-01-29",
    "expver": "prod",
    "levelist": "500/700/850/925",
    "levtype": "pl",
    "model": "glob",
    "origin": "ecmf",
    "param": "130/133",
    "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
    "stream": "enfo",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})

server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2015-01-01/2015-01-05/2015-01-08/2015-01-12/2015-01-15/2015-01-19/2015-01-22/2015-01-26/2015-01-29",
    "expver": "prod",
    "levelist": "50/200",
    "levtype": "pl",
    "model": "glob",
    "origin": "ecmf",
    "param": "131",
    "step": "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360/384/408/432/456/480/504/528/552/576/600/624/648/672/696/720/744/768",
    "stream": "enfo",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})

