import math
def ell2xyz(latitude , longitude , ellHeight ):
    a = float(6378137.0000)
    b = float(6356752.3141)
    latitude = float(latitude)
    longitude = float(longitude)
    ellHeight = float(ellHeight)
    square_of_e = float()
    N = float()
    square_of_e = ((a*a) - (b*b))/(a*a)
    N = a / math.sqrt(1 - (square_of_e)*(math.sin(math.radians(latitude))**2))
    x = (N + ellHeight)*(math.cos(math.radians(latitude)))*(math.cos(math.radians(longitude)))
    y = (N + ellHeight)*(math.cos(math.radians(latitude)))*(math.sin(math.radians(longitude)))
    z = ((1 - (square_of_e))*N + ellHeight)*(math.sin(math.radians(latitude)))
    return( round(x , 4) , round(y , 4) , round(z , 4) )
def xyz2ell(x , y , z ):
    x = float(x)
    y = float(y)
    z = float(z)
    a = float(6378137.0000)
    b = float(6356752.3141)
    longtitude = math.atan(y/x)
    square_of_e = ((a*a) - (b*b))/(a*a)
    p = math.sqrt( x**2 + y**2 )
    prime_N = a
    prime_ellHeight = math.sqrt(x**2+y**2+z**2) - math.sqrt(a*b)
    prime_latitude = math.atan(z / ((1 - (square_of_e * prime_N)/(prime_N + prime_ellHeight))*p))
    n_list = []
    n_list.append(prime_N)
    ellHeight_list =[]
    ellHeight_list.append(prime_ellHeight)
    latitude_list = []
    latitude_list.append(prime_latitude)
    k = 0
    while True :
        N = a / math.sqrt(1-(square_of_e)*(math.sin(latitude_list[k])**2))
        ellHeight = p / math.cos(latitude_list[k]) - N
        latitude = math.atan( z / ((1-((square_of_e)*N)/(N + ellHeight))*p))
        n_list.append(N)
        ellHeight_list.append(ellHeight)
        latitude_list.append(latitude)
        k += 1
        if abs(n_list[-1] - n_list[-2])<= 10**-4 and abs(ellHeight_list[-1] - ellHeight_list[-2])<= 10**-4 and abs(latitude_list[-1] - latitude_list[-2]):
            N = n_list[-1]
            ellHeight = ellHeight_list[-1]
            latitude = latitude_list[-1]
            return( round(math.degrees(latitude),8) , round(math.degrees(longtitude),8) , round(ellHeight,2))
            break
def degree2dms(decimal):
    decimal = float(decimal)
    mnt,sec = divmod(decimal*3600 , 60)
    deg,mnt = divmod(mnt,60)
    return "{} , {} , {}".format(deg , mnt , sec)
