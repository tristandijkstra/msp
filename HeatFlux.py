from tqdm import tqdm as tqdm
import math
from math import sqrt, cos, pi
import time
import main as m

AU = 149.6e6  # km
muSun = 1.327178e11
muMars = 42828.37
currentTime = time.time()

AU = 149.6e6  # km
r_a=1.6660*AU
r_p=1.3814*AU
e_m=(r_a-r_p)/(r_a+r_p)
a=1.524*AU
i_m=25*pi/180 #rot. axis inclination
F_0=590 #W/m^2
L=3.9e26 #[W]
T=2*pi*sqrt(a**3/muMars)
n=sqrt(muMars/a**3)

# Mars = m.Planet(muMars, R_m, AU, muSun) This class sets the planet into a circular orbit?

def Flux(theta, l): #with clear sky
    """Find hyperbolic anomaly taking the body's current keplerian values
    Arguments:
        theta  -- true anomaly [rad]
        l  -- latitude angle [rad]
    Returns:
        flux -- Heat flux [W/m^2]
    """
    r=(a*(1-e_m**2))/(1+e_m*cos(theta))
    flux_str = L / (4*pi*(r*10**3)**2) #Now we need to adjust for latitude and axis inclination
    flux=flux_str*cos(l) #not done yet...
    return flux


