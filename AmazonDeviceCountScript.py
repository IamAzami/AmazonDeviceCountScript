def utilities():
    rf_scanners_input = int(input("\nPlease enter the amount of RF scanners available: "))
    rf_expectation = 263
    if rf_scanners_input >= rf_expectation:
        total = rf_scanners_input / rf_expectation * 100
        if rf_scanners_input > rf_expectation:
            print(f"Passing max threshold, {int(total)}% of RF scanner capacity available, lots of scanners available.")
        elif rf_scanners_input == rf_expectation:
            print(f"{int(total)}% of RF scanner capacity available, lots of scanners available.")
    elif rf_scanners_input >= 131:
        result = rf_scanners_input / rf_expectation * 100
        RF_Scanners_left = int(rf_expectation) - int(rf_scanners_input)
        print(f"{int(result)}% of of RF scanner capacity available. Missing {int(RF_Scanners_left)} scanners!!")
    elif rf_scanners_input == 0:
        print("No more scanners!!")
    else:
        con = rf_scanners_input / 263 * 100
        RF_Scanners_left = int(rf_expectation) - int(rf_scanners_input)
        print(
            f"{int(con)}% of of RF scanner capacity available, need more scanners. Missing {int(RF_Scanners_left)} scanners!!")
    rf_batteries_input = int(input("\nPlease enter the amount of RF batteries available: "))
    rf_expectation2 = 400
    if rf_batteries_input >= rf_expectation2:
        t = rf_batteries_input / rf_expectation2 * 100
        if rf_batteries_input > rf_expectation2:
            print(f"Passing max threshold, {int(t)}% of RF battery capacity available, lots of batteries available.")
        elif rf_batteries_input == rf_expectation2:
            print(f"{int(t)}% of RF battery capacity available, lots of batteries available.")
    elif rf_batteries_input >= 200:
        r = rf_batteries_input / 400 * 100
        RF_batteries_left = int(rf_expectation2) - int(rf_batteries_input)
        print(f"{int(r)}% of RF battery capacity available. Missing {int(RF_batteries_left)} batteries!!")
    elif rf_batteries_input == 0:
        print("No more batteries!!")
    else:
        c = rf_batteries_input / rf_expectation2 * 100
        RF_batteries_left = int(rf_expectation2) - int(rf_batteries_input)
        print(f"{int(c)}% of RF batteries available, Missing {int(RF_batteries_left)} batteries!!")
    pick_carts_input = int(input("\nPlease enter the amount of Pick Carts available: "))
    pick_carts_expectation = 460
    if pick_carts_input >= pick_carts_expectation:
        res = pick_carts_input / pick_carts_expectation * 100
        if pick_carts_input > pick_carts_expectation:
            print(f"Passing max threshold, {int(res)}% of Pick Cart capacity available, more than enough carts.")
        elif pick_carts_input == pick_carts_expectation:
            print(f"{int(res)}% of Pick Cart capacity available, more than enough carts.")
    elif pick_carts_input >= 230:
        add = pick_carts_input / 460 * 100
        pick_carts_left = int(pick_carts_expectation) - int(pick_carts_input)
        print(
            f"{int(add)}% of Pick Cart capacity available, {int(pick_carts_left)} missing/damaged carts reducing max capacity!!")
    elif pick_carts_input == 0:
        print("No more Pick Carts!!")
    else:
        gether = pick_carts_input / pick_carts_expectation * 100
        pick_carts_left = int(pick_carts_expectation) - int(pick_carts_input)
        print(
            f"{int(gether)}% of Pick Cart capacity available. Missing {int(pick_carts_left)} carts, need more pick carts!!")
    totes_input = int(input("\nPlease enter the amount of Totes available: "))
    totes_expec = 25006
    if totes_input >= totes_expec:
        u = totes_input / totes_expec * 100
        if totes_input > totes_expec:
            print(f"Passing max threshold, {int(u)}% of Tote capacity available, more than enough Totes.")
        elif totes_input == totes_expec:
            print(f"{int(u)}% of Tote capacity available, more than enough Totes.")
    elif totes_input >= 12503:
        Q = totes_input / 25006 * 100
        totes_left = int(totes_expec) - int(totes_input)
        print(f"{int(Q)}% of Tote capacity available, missing {int(totes_left)} totes, consider injection!!")
    elif totes_input == 0:
        msg = "no more Totes, where's the Tote Team!!"
        print(msg.upper())
    else:
        e = totes_input / totes_expec * 100
        totes_left = int(totes_expec) - int(totes_input)
        print(f"{int(e)}% of Tote capacity available, missing {int(totes_left)} totes, where's the Tote team!!")
    laptop_input = int(input("\nPlease enter the amount of Laptops available: "))
    laptop_expectation = 7
    if laptop_input >= laptop_expectation:
        amount = laptop_input / laptop_expectation * 100
        if laptop_input > laptop_expectation:
            print(f"Passing max threshold, {int(amount)}% of Laptop capacity available, lots of laptops for everyone.")
        elif laptop_input == laptop_expectation:
            print(f"{int(amount)}% of Laptop capacity available, lots of laptops for everyone.")
    elif laptop_input >= 3:
        addup = laptop_input / laptop_expectation * 100
        laptops_left = int(laptop_expectation) - int(laptop_input)
        print(f"{int(addup)}% of Laptop capacity available. Missing {int(laptops_left)} laptops!!")
    elif laptop_input == 0:
        print("No more Laptops!!")
    else:
        keepadd = laptop_input / 7 * 100
        laptops_left = int(laptop_expectation) - int(laptop_input)
        print(f"{int(keepadd)}% of Laptop capacity available. Missing {int(laptops_left)} laptops!!")
    PS_Carts_input = int(input("\nPlease enter the amount of PS Carts available: "))
    PS_Carts_expec = 7
    if PS_Carts_input >= PS_Carts_expec:
        plus = PS_Carts_input / 7 * 100
        if PS_Carts_input > PS_Carts_expec:
            print(f"Passing max threshold, {int(plus)}% of PS Carts capacity available, more than enough carts.")
        elif PS_Carts_input == PS_Carts_expec:
            print(f"{int(plus)}% of PS Carts capacity available, more than enough carts.")
    elif PS_Carts_input >= 3:
        alwaysup = PS_Carts_input / PS_Carts_expec * 100
        PS_left = int(PS_Carts_expec) - int(PS_Carts_input)
        print(f"{int(alwaysup)}% of PS Carts capacity available. Missing {int(PS_left)} PS Carts!!")
    elif PS_Carts_input == 0:
        print("No more PS Carts!!")
    else:
        uppp = PS_Carts_input / PS_Carts_expec * 100
        PS_left = int(PS_Carts_expec) - int(PS_Carts_input)
        print(f"{int(uppp)}% of PS Carts capacity available. Missing {int(PS_left)} PS Carts!!")
    Full_Batteries_PS_Carts_input = int(input("\nPlease enter the amount of Full batteries for PS Carts available: "))
    Full_Batteries_PS_Carts_expec = 20
    if Full_Batteries_PS_Carts_input >= Full_Batteries_PS_Carts_expec:
        addition = Full_Batteries_PS_Carts_input / Full_Batteries_PS_Carts_expec * 100
        if Full_Batteries_PS_Carts_input > Full_Batteries_PS_Carts_expec:
            print(
                f"Passing max threshold, {int(addition)}% of Full batteries for PS Carts capacity available, lots of batteries.")
        elif Full_Batteries_PS_Carts_input == Full_Batteries_PS_Carts_expec:
            print(f"{int(addition)}% of Full batteries for PS Carts capacity available, lots of batteries.")
    elif Full_Batteries_PS_Carts_input >= 10:
        y = Full_Batteries_PS_Carts_input / Full_Batteries_PS_Carts_expec * 100
        F_B_PS_left = int(Full_Batteries_PS_Carts_expec) - int(Full_Batteries_PS_Carts_input)
        print(f"{int(y)}% of Full batteries for PS Carts capacity available. Missing {int(F_B_PS_left)} batteries!!")
    elif Full_Batteries_PS_Carts_input == 0:
        print("No more PS batteries!!")
    else:
        g = Full_Batteries_PS_Carts_input / Full_Batteries_PS_Carts_expec * 100
        F_B_PS_left = int(Full_Batteries_PS_Carts_expec) - int(Full_Batteries_PS_Carts_input)
        print(
            f"{int(g)}% of Full batteries for PS Carts capacity available. Missing {int(F_B_PS_left)} batteries for PS Carts!!")
    radios_input = int(input("\nPlease enter the amount of Radios available: "))
    radios_expectation = 15
    if radios_input >= radios_expectation:
        k = radios_input / radios_expectation * 100
        if radios_input > radios_expectation:
            print(f"Passing max threshold, {int(k)}% of Radio capacity available, lots of radios.")
        elif radios_input == radios_expectation:
            print(f"{int(k)}% of Radio capacity available, lots of radios.")
    elif radios_input >= 7:
        h = radios_input / 15 * 100
        radios_left = int(radios_expectation) - int(radios_input)
        print(f"{int(h)}% of Radio capacity available. Missing {int(radios_left)} radio!!")
    elif radios_input == 0:
        print("No more Radio!!")
    else:
        i = radios_input / radios_expectation * 100
        radios_left = int(radios_expectation) - int(radios_input)
        print(f"{int(i)}% of Radio capacity. Missing {int(radios_left)} radios!!")
    r_i_m_input = int(input("\nPlease enter the amount of Radios in the Mod available: "))
    r_i_m_expec = 36
    if r_i_m_input >= r_i_m_expec:
        v = r_i_m_input / r_i_m_expec * 100
        if r_i_m_input > r_i_m_expec:
            print(f"Passing max threshold, {int(v)}% of Radios in the Mod, lots of radios.")
        elif r_i_m_input == r_i_m_expec:
            print(f"{int(v)}% of Radios in the Mod, lots of radios.")
    elif r_i_m_input >= 18:
        w = r_i_m_input / r_i_m_expec * 100
        r_i_m_left = int(r_i_m_expec) - int(r_i_m_input)
        print(f"{int(w)}% of Radios in the Mod. Missing {int(r_i_m_left)} radios in the mod!!")
    elif r_i_m_input == 0:
        print("No radios in the mod!!")
    else:
        A = r_i_m_input / 36 * 100
        r_i_m_left = int(r_i_m_expec) - int(r_i_m_input)
        print(f"{int(A)}% of Radios in the Mod. Missing {int(r_i_m_left)} radios!!")
    p_i_t_m_input = int(input("\nPlease enter the amount of Printers in the Mod available: "))
    p_i_t_m_expectation = 36
    if p_i_t_m_input >= p_i_t_m_expectation:
        T = p_i_t_m_input / 36 * 100
        if p_i_t_m_input > p_i_t_m_expectation:
            print(f"Passing max threshold, {int(T)}% of Printers in the Mod, more than enough printers.")
        elif p_i_t_m_input == p_i_t_m_expectation:
            print(f"{int(T)}% of Printers in the Mod, more than enough printers.")
    elif p_i_t_m_input >= 18:
        a = p_i_t_m_input / p_i_t_m_expectation * 100
        p_i_t_m_left = int(p_i_t_m_expectation) - int(p_i_t_m_input)
        print(f"{int(a)}% of Printers in the Mod, {int(p_i_t_m_left)} missing/damaged printers reducing max capacity!!")
    elif p_i_t_m_input == 0:
        print("No more Printers in the Mod or they must be damaged!!")
    else:
        f = p_i_t_m_input / 36 * 100
        p_i_t_m_left = int(p_i_t_m_expectation) - int(p_i_t_m_input)
        print(f"{int(f)}% of Printers in the Mod, {int(p_i_t_m_left)} missing/damaged printers reducing max capacity!!")
    tanker_input = int(input("\nPlease enter the amount of Tote Tankers available: "))
    tanker_expec = 34
    if tanker_input >= tanker_expec:
        tk = tanker_input / tanker_expec * 100
        if tanker_input > tanker_expec:
            print(f"Passing max threshold, {int(tk)}% of Tote Tanker capacity available, lots of tankers.")
        elif tanker_input == tanker_expec:
            print(f"{int(tk)}% of Tote Tanker capacity available, lots of tankers.")
    elif tanker_input == 17:
        hf = tanker_input / 34 * 100
        tankers_left = int(tanker_expec) - int(tanker_input)
        print(
            f"{int(hf)}% of Tote Tanker capacity available, {int(tankers_left)} missing/damaged tankers reducing max capacity!!")
    elif tanker_input == 0:
        print("No Tote Tankers!!!")
    else:
        dn = tanker_input / tanker_expec * 100
        tankers_left = int(tanker_expec) - int(tanker_input)
        print(
            f"{int(dn)}% of Tote Tanker capacity available, {int(tankers_left)} missing/damaged tankers reducing max capacity!!")
    l_boats_input = int(input("\nPlease enter the amount of L-Boats available: "))
    l_boats_expec = 4
    if l_boats_input >= l_boats_expec:
        lb = l_boats_input / l_boats_expec * 100
        if l_boats_input > l_boats_expec:
            print(f"Passing max threshold, {int(lb)}% of l-boats capacity available, lots of l-boats.")
        elif l_boats_input == l_boats_expec:
            print(f"{int(lb)}% of l-boats capacity available, lots of l-boats.")
    elif l_boats_input == 2:
        haf = l_boats_input / 4 * 100
        l_boats_left = int(l_boats_expec) - int(l_boats_input)
        print(f"{int(haf)}% of l-boats capacity available. Missing {int(l_boats_left)} l-boats!!")
    elif l_boats_input == 0:
        print("No more l-boats!!")
    else:
        el = l_boats_input / l_boats_expec * 100
        l_boats_left = int(l_boats_expec) - int(l_boats_input)
        print(f"{int(el)}% of l-boats capacity available. Missing {int(l_boats_left)} l-boats!!")
    gaylord_input = int(input("\nPlease enter the amount of Gaylords available: "))
    gaylord_expec = 39
    if gaylord_input >= gaylord_expec:
        fg = gaylord_expec / gaylord_expec * 100
        if gaylord_input > gaylord_expec:
            print(f"Passing max threshold, {int(fg)}% of gaylords are available, more than enough.")
            print("Finished first part of count on to the actual tote count...")
        elif gaylord_input == gaylord_expec:
            print(f"{int(fg)}% of gaylords are available, more than enough.")
            print("Finished first part of count on to the actual tote count...")
    elif gaylord_input >= 19:
        yu = gaylord_input / 39 * 100
        gaylords_left = int(gaylord_expec) - int(gaylord_input)
        print(f"{int(yu)}% of gaylords are available. Missing {int(gaylords_left)} gaylords!!")
    elif gaylord_input == 0:
        print("No more gaylords on P4!!")
        print("Finished first part of count on to the actual tote count...")
    else:
        op = gaylord_input / gaylord_expec * 100
        gaylords_left = int(gaylord_expec) - int(gaylord_input)
        print(f"{int(op)}% of gaylords are available. Missing {int(gaylords_left)} gaylords!!\n")
    print("Finished Counting Utilities.\n")
def t_count():
    global result, ans, ttl, tger
    P4_mod_input = int(input("\nPlease enter total amount of missing totes on P4 north & south mods: "))
    P4_staging_input = int(input("Please enter total amount of staging for the north & south side of P4 including the outbound buffers: "))
    P4_carts_input = int(input("Please enter total amount of carts for the north & south side of P4: "))
    P4_mod_totes = 4728
    if P4_mod_input < P4_mod_totes:
        result = P4_mod_totes - P4_mod_input
        print(f"We have {result} totes remaining on P4!!")
        total_totes4 = result + P4_staging_input
        print("Adding staging for a total amount of " + str(total_totes4) + " totes.")
        print(f"Total of {P4_carts_input} pick carts on P4 ")
    elif P4_mod_input > P4_mod_totes:
        print("We are out of totes on P4, no more totes!!")
        print(f"Total of {P4_carts_input} pick carts on P4")
    else:
        result = P4_mod_totes - P4_mod_input
        total_staging4 = result + P4_staging_input
        print("Adding staging for a total amount of " + str(total_staging4) + " totes on P4.")
        print("We have a full amount of totes on P4.")
        print(f"Total of {P4_carts_input} pick carts on P4")
    P3_mod_input = int(input("\nPlease enter total amount of missing totes on P3 north & south mods: "))
    P3_staging_input = int(input("Please enter total amount of staging for the north & south side of P3 including the outbound buffers: "))
    P3_carts_input = int(input("Please enter total amount of carts for the north & south side of P3: "))
    P3_mod_totes = 5256
    if P3_mod_input < P3_mod_totes:
        ans = P3_mod_totes - P3_mod_input
        print(f"We have {ans} totes remaining on P3!!")
        total_totes3 = ans + P3_staging_input
        print("Adding staging for a total amount of " + str(total_totes3) + " totes on P3.")
        print(f"Total of {P3_carts_input} pick carts on P3")
    elif P3_mod_input > P3_mod_totes:
        print("We are out of totes on P3, no more totes!!")
        print(f"Total of {P3_carts_input} pick carts on P3")
    else:
        ans = P3_mod_totes - P3_mod_input
        total_staging3 = ans + P3_staging_input
        print("Adding staging for a total amount of " + str(total_staging3) + " totes on P3.")
        print("We have a full amount of totes on P3.")
        print(f"Total of {P3_carts_input} pick carts on P3")
    P2_mod_input = int(input("\nPlease enter total amount of missing totes on P2 north & south mods: "))
    P2_staging_input = int(input("Please enter total amount of staging for the north & south side of P2 including the outbound buffers: "))
    P2_carts_input = int(input("Please enter total amount of carts for the north & south side of P2: "))
    P2_mod_totes = 5136
    if P2_mod_input < P2_mod_totes:
        ttl = P2_mod_totes - P2_mod_input
        print(f"We have {ttl} totes remaining on P2!!")
        total_totes2 = ttl + P2_staging_input
        print("Adding staging for a total amount of " + str(total_totes2) + " totes on P2.")
        print(f"Total of {P2_carts_input} pick carts on P2")
    elif P2_mod_input > P2_mod_totes:
        print("We are out of totes on P2, no more totes!!")
        print(f"Total of {P2_carts_input} pick carts on P2")
    else:
        ttl = P2_mod_totes - P2_mod_input
        total_staging2 = ttl + P2_staging_input
        print("Adding staging for a total amount of " + str(total_staging2) + " totes on P2.")
        print("We have a full amount of totes on P2.")
        print(f"Total of {P2_carts_input} pick carts on P2")
    P1_mod_input = int(input("\nPlease enter total amount of missing totes on P1 north & south mods: "))
    P1_staging_input = int(input("Please enter total amount of staging for the north & south side of P1: "))
    P1_carts_input = int(input("Please enter total amount of carts for the north & south side of P1: "))
    P1_mod_totes = 5808
    if P1_mod_input < P1_mod_totes:
        tger = P1_mod_totes - P1_mod_input
        print(f"We have {tger} totes remaining on P1!!")
        total_totes1 = tger + P1_staging_input
        print("Adding staging for a total amount of " + str(total_totes1) + " totes on P1.")
        print(f"Total of {P1_carts_input} pick carts on P1")
    elif P1_mod_input > P1_mod_totes:
        print("We are out of totes on P1, no more totes!!")
        print(f"Total of {P1_carts_input} pick carts on P1")
    else:
        tger = P1_mod_totes - P1_mod_input
        total_staging1 = tger + P1_staging_input
        print("Adding staging for a total amount of " + str(total_staging1) + " totes on P1.")
        print("We have a full amount of totes on P1.")
        print(f"Total of {P1_carts_input} pick carts on P1")
    full_totes = result + ans + ttl + tger
    full_staging = P4_staging_input + P3_staging_input + P2_staging_input + P1_staging_input
    full_carts = P4_carts_input + P3_carts_input + P2_carts_input + P1_carts_input
    count = full_totes + full_staging
    print("\nAll floors counted for, total amount of totes is " + str(full_totes))
    print("All floors counted for, total amount of staging is " + str(full_staging))
    print("All floors counted for, total amount of carts is " + str(full_carts))
    print(f"=> Your count for today is {str(count)} <=\n")
def dislplay():
    import  os
    os.system('cls')
    os.system('color 4e')
    goC = True
    while goC:
        message = "welcome to The Reapers script for pick automation."
        message += " this script is 'safe' and easy to use."
        print("------------------------------------------------------------------------------------")
        print(message.upper())
        print("------------------------------------------------------------------------------------")
        choice = "for accessing the utilities automator please enter -> 1.\n"
        choice += "for accessing the tote count automator please enter -> 2.\n"
        choice += "to exit the script close me or enter -> 0.\n"
        choice += "enter answer here: "
        answer = input(choice.title())
        if answer == "1":
            utilities()
        elif answer == "2":
            t_count()
        else:
            goC = False
            exit()
dislplay()


