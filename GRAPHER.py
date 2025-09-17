# GRAPHER.py
# Contains only the graphing functions.

import math
import ti_plotlib as plt
from HELPERS import get_input, CONSTANTS
#apparently tiplotlib likes to consume RAM like a hungry homeless hamster, it could almost compete with chrome
def projectile_graph():
    print("\nProjectile Motion Graph")
    v0 = get_input("v0 (m/s): ")
    ang = get_input("Angle (deg): ")
    if v0 is None or ang is None: return

    ang_r = math.radians(ang)
    g = CONSTANTS["g"]
    t_f = 2*v0*math.sin(ang_r)/g
    if t_f <= 0: return

    pts = 50
    xs, ys = [], []
    for i in range(pts + 1):
        t = t_f * i / pts
        x = v0*math.cos(ang_r)*t
        y = v0*math.sin(ang_r)*t - 0.5*g*t*t
        xs.append(x)
        ys.append(y if y >= 0 else 0)

    plt.cls()
    xmax = xs[-1]*1.1 if xs[-1]>0 else 1
    ymax = max(ys)*1.1 if max(ys)>0 else 1
    plt.window(0, xmax, 0, ymax)
    plt.title("Projectile Motion")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(xmax/5, ymax/5, "dotted")
    plt.axes("on")
    plt.plot(xs, ys, "b-")
    plt.show()
