import math

print('PSYCHROMETRIC CALCULATIONS')
print('')
print('INPUT DATA:')
print('')
temp = float(input("Please introduce air temperature in Celcius degrees: "))
press = float(input("Please introduce the atmospheric pressure in kPa: "))
relative_humidity = float(input("Please introduce air relative humidity in %: "))

def results ():
    print('')
    print('RESULTS')
    print('')
    saturation_pressure = ps(temp)
    print("Saturation pressure is " + str(round(saturation_pressure,2)) + " kPa")
    vapour_pressure = vp (relative_humidity)
    print("Vapour pressure is " + str(round(vapour_pressure,2)) + " kPa")
    absolute_humidity = abs_hum (press)
    print("Absolute humidity is " + str(round(absolute_humidity,5)) + " kg humidity/kg dry air")
    specific_volume = sp_vol(temp, press)
    print("Specific volume is " + str(round(specific_volume,2)) + " m3/kg dry air")
    dew_point = dpoint (press)
    print("Water dew point is " + str(round(dew_point,2)) + " °C")
    cs = heat (temp)
    print("Humid heat is " + str(round(cs,2)) + " kJ/(kg dry air °C)")
    entalphy = ent (temp)
    print("Entalphy is " + str(round(entalphy,2)) + " kJ/kg dry air")

def ps (temp):
    a=16.5362
    b=3985.44
    c=-38.9974
    c1 = c + temp + 273
    saturation_pressure = math.exp(a-(b/c1))
    return saturation_pressure

def vp (relative_humidity):
    saturation_pressure = ps (temp)
    vapour_pressure = saturation_pressure * relative_humidity / 100
    return vapour_pressure

def abs_hum (press):
    vapour_pressure = vp (relative_humidity)
    absolute_humidity = 0.622 * vapour_pressure / (press-vapour_pressure)
    return absolute_humidity

def sp_vol (temp, press):
    m_air = 28.97
    m_water = 18
    n_press = 101.325
    n_temp = 273
    r_gas = 8.314
    t_k = temp + 273
    molar_volume = (r_gas*n_temp)/n_press
    absolute_humidity = abs_hum (press)
    specific_volume = (molar_volume*((1/m_air)+(absolute_humidity/m_water)))*(t_k/n_temp)*(n_press/press)
    return specific_volume

def dpoint (press):
    a=16.5362
    b=3985.44
    c=-38.9974
    absolute_humidity = abs_hum (press)
    dew_point = ((b/(a-(math.log(press / (1+(0.622/absolute_humidity)))))-c)-273)
    return dew_point

def heat (temp):
    ca = 1.005
    cb = 1.884
    absolute_humidity = abs_hum (press)
    cs = cb + ca * absolute_humidity
    return cs

def ent (temp):
    hfg = 2502.3
    to = 0
    absolute_humidity = abs_hum (press)
    cs = heat (temp)
    entalphy = cs*(temp-to) + (hfg*absolute_humidity)
    return entalphy

if __name__ == "__main__":
    results ()
