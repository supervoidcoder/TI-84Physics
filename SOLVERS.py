# SOLVERS.py
# Contains all the physics formula solvers.

import math
from HELPERS import get_input, fmt

def kinematics_submenu():
    print("\nKinematics Formulas:")
    print(" a) v = v0+a*t")
    print(" b) x = x0+v0*t+0.5*a*t^2")
    print(" c) v^2 = v0^2+2*a*dx")
    sub = input("Pick a/b/c: ").strip().lower()
    if sub == "a":
        v,v0,a,t = get_input("v="),get_input("v0="),get_input("a="),get_input("t=")
        if v is None: print("v =", fmt(v0 + a*t))
        elif v0 is None: print("v0 =", fmt(v - a*t))
        elif a is None: print("a =", fmt((v-v0)/t))
        elif t is None: print("t =", fmt((v-v0)/a))
    elif sub == "b":
        x,x0,v0,a,t = get_input("x="),get_input("x0="),get_input("v0="),get_input("a="),get_input("t=")
        if t is None:
            A,B,C = 0.5*a, v0, x0-x
            if abs(A)<1e-9: print("t=",fmt(-C/B))
            else:
              disc=B*B-4*A*C
              if disc<0: print("No real t sol.")
              else: print("t=",fmt((-B+math.sqrt(disc))/(2*A)),"or",fmt((-B-math.sqrt(disc))/(2*A)))
        elif x is None: print("x=",fmt(x0+v0*t+0.5*a*t*t))
        elif x0 is None: print("x0=",fmt(x-v0*t-0.5*a*t*t))
        elif v0 is None: print("v0=",fmt((x-x0-0.5*a*t*t)/t))
        elif a is None: print("a=",fmt(2*(x-x0-v0*t)/(t*t)))
    elif sub == "c":
        v,v0,a,dx = get_input("v="),get_input("v0="),get_input("a="),get_input("dx=")
        if v is None: print("v=",fmt(math.sqrt(v0*v0+2*a*dx)))
        elif v0 is None: print("v0=",fmt(math.sqrt(v*v-2*a*dx)))
        elif a is None: print("a=",fmt((v*v-v0*v0)/(2*dx)))
        elif dx is None: print("dx=",fmt((v*v-v0*v0)/(2*a)))
#since people apparently care about code readibilyness... uhm readibilyty... um red- you get the point
#here's some spaghetti code to fill your tummy
def forces():
    F,m,a = get_input("F="),get_input("m="),get_input("a=")
    if F is None: print("F =", fmt(m*a))
    elif m is None: print("m =", fmt(F/a))
    elif a is None: print("a =", fmt(F/m))

def energy():
    from HELPERS import CONSTANTS
    c=input("1)KE 2)PE: ")
    if c=="1":
        m,v,ke=get_input("m="),get_input("v="),get_input("KE=")
        if ke is None: print("KE=",fmt(0.5*m*v*v))
        elif m is None: print("m=",fmt(2*ke/(v*v)))
        elif v is None: print("v=",fmt(math.sqrt(2*ke/m)))
    else:
        m,h,pe=get_input("m="),get_input("h="),get_input("PE=")
        if pe is None: print("PE=",fmt(m*CONSTANTS["g"]*h))
        elif m is None: print("m=",fmt(pe/(CONSTANTS["g"]*h)))
        elif h is None: print("h=",fmt(pe/(m*CONSTANTS["g"])))

def momentum():
    m,v,p = get_input("m="),get_input("v="),get_input("p=")
    if p is None: print("p =", fmt(m*v))
    elif m is None: print("m =", fmt(p/v))
    elif v is None: print("v =", fmt(p/m))
