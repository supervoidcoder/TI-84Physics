# MAIN.py


from HELPERS import press_enter, CONSTANTS
import SOLVERS
import GRAPHER
#bleh case-sensitiveness... er- sensitivity?

while True:
    print("\n=== PHYSICS BUNDLE ===")
    print("1. Kinematics")
    print("2. Forces (F=ma)")
    print("3. Energy (KE/PE)")
    print("4. Momentum (p=mv)")
    print("5. Projectile Graph")
    print("6. Show Constants")
    print("0. Quit")

    choice = input("Choose: ").strip()

    if choice == "1":
        SOLVERS.kinematics_submenu()
    elif choice == "2":
        SOLVERS.forces()
    elif choice == "3":
        SOLVERS.energy()
    elif choice == "4":
        SOLVERS.momentum()
    elif choice == "5":
        GRAPHER.projectile_graph()
    elif choice == "6":
        for k,v in CONSTANTS.items(): print(k,"=",v)
    elif choice == "0":
        print("Done!")
        break
    else:
        print("Invalid option.")
        continue 

    press_enter()
