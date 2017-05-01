import datetime
def  datize(day, month, year) :
    try :
        date = datetime.date(year, month, day)
        return (True)
    except :
        return(False)
