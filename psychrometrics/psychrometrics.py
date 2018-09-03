import math

PATM = 14.696 # Standard atmospheric sea-level pressure.

def water_sat_press(T):
    """Return water saturation pressure in psia given temperature in °F
    Uses formulation from Eq. 6 ASHRAE Fundamentals 2017
    """

    T_abs = T + 459.67
    
    C8 = -1.0440397e4
    C9 = -1.129465e1
    C10 = -2.702355E-2
    C11 = 1.289036E-5
    C12 = -2.4780681E-9
    C13 = 6.5459673
    
    term = C8 / T_abs + C9 + C10 * T_abs + C11 * T_abs * T_abs + C12 * T_abs* T_abs* T_abs + C13 * math.log(T_abs)
    return math.exp(term)

def ω_from_Pv(pv):
    """Returns humidity ratio from partial pressure of water vapor (psia).
    """
    return 0.621945 * pv / (PATM - pv) 


def ω_from_t_db_and_t_wb(t_db, t_wb):
    """Returns humidity ratio from dry bulb temperature and wet bulb temperature (°F)
    """
    
    pv_wb = water_sat_press(t_wb)
    ω_s_wb = ω_from_Pv(pv_wb) # saturation humidity ratio for wet-bulb temp
    return ( (1093-0.556*t_wb ) * ω_s_wb - 0.24 * (t_db - t_wb) ) / (1093 + 0.444* t_db - t_wb)

def ω_from_t_db_and_rh(t_db, rh):
    ps = water_sat_press(t_db)
    pw = ps * rh
    return ω_from_Pv(pw)

def ω_from_t_dp(t_dp):
    pw = water_sat_press(t_dp)
    return ω_from_Pv(pw)

def h_from_t_db_and_ω(t_db, ω):
    return 0.24 * t_db + ω * (1061+0.445*t_db)

def h_from_t_db_and_t_wb(t_db, t_wb):
    """Returns enthalpy (BTU/lb da) from dry bulb and wet bulb temperature,
    both in °F
    """
    ω = ω_from_t_db_and_t_wb(t_db, t_wb)
    return h_from_t_db_and_ω(t_db, ω)


def print_data_to_string(data):
    return [ f'{data[0]:d}',
             f'{data[1]:d}',
             f'{data[2]:0.4f}',
             f'{data[3]:0.2f}']

def check_page_length(page, i):
    if i < len(page):
        return print_data_to_string(page[i])
    else:
        return ["","","",""]

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
