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
    "param": "34",
    "step": "0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720/720-744/744-768/768-792/792-816/816-840/840-864/864-888/888-912/912-936/936-960/960-984/984-1008/1008-1032/1032-1056/1056-1080/1080-1104",
    "stream": "enfh",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})
