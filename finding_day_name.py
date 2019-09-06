while(True):
    year=int(input("Enter the year : "))
    month=input("Enter the name of the month: ")
    date=int(input("Enter the date: "))
    print("\n")
    print("{} / {} / {} ".format(year,month,date))

    #for the calculation of 12 month
    if month=="january" or month=="jan":
        month=1

    elif month=="february" or month=="feb":
        month=4
    elif month=="march" or month=="mar":
        month="marc"
    elif month=="april" or month=="apr":
        month=0
    elif month=="may" or month=="May":
        month=2
    elif month=="june" or month=="June":
        month=5
    elif month=="july" or month=="July":
        month=0
    elif month=="auguest" or month=="aug":
        month=3
    elif month=="september" or month=="sep":
        month=6
    elif month=="october" or month=="oct":
        month="octo"
    elif month=="november" or month=="nov":
        month="novem"
    elif month=="december" or month=="dec":
        month=6
    print("")
    # print(month)


    #for the calculation of year
    if year>1900:
        a=year-1900
        # print(a)
        x=a%4
        if x==0:
            if month==1:
                b=int(a/4)
                z=b-1
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")

            elif month==4:
                b=int(a/4)
                z=b-1
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="marc":
                month=4
                b=int(a/4)
                c=int(a+b+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="octo":
                month=1
                b=int(a/4)
                c=int(a+b+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="novem":
                month=4
                b=int(a/4)
                c=int(a+b+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            else:
                if month=="march" or month=="marc":
                    month=4
                elif month=="october" or month=="octo":
                    month=1
                elif month=="november" or month=="novem":
                    month=4
                b=int(a/4)
                c=int(a+b+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")

        else:
            if month=="march" or month=="marc":
                month=4
            elif month=="october" or month=="octo":
                month=1
            elif month=="november" or month=="novem":
                month=4
            b=int(a/4)
            c=int(a+b+date+month)
            d=c%7
            if d==0:
                print("The day was Saturday")
            elif d==1:
                print("The day was Sunday")
            elif d==2:
                print("The day was Monday")
            elif d==3:
                    print("The day was Tuesday")
            elif d==4:
                print("The day was Wednesday")
            elif d==5:
                print("The day was Thursday")
            elif d==6:
                print("The day was Friday")
    elif 1900>year>1800:
        a=year-1800
        # print(a)
        x=a%4
        if x==0:
            if month==1:
                b=int(a/4)
                z=b+1
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")

            elif month==4:
                b=int(a/4)
                z=b+1
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="marc":
                month=4
                b=int(a/4)
                z=b+2
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="octo":
                month=1
                b=int(a/4)
                z=b+2
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="novem":
                month=4
                b=int(a/4)
                z=b+2
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            else:
                if month=="march" or month=="marc":
                    month=4
                elif month=="october" or month=="octo":
                    month=1
                elif month=="november" or month=="novem":
                    month=4
                b=int(a/4)
                z=b+2
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                        print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")

        else:
            if month=="march" or month=="marc":
                month=4
            elif month=="october" or month=="octo":
                month=1
            elif month=="november" or month=="novem":
                month=4
            b=int(a/4)
            z=b+2
            c=int(a+z+date+month)
            d=c%7
            if d==0:
                print("The day was Saturday")
            elif d==1:
                print("The day was Sunday")
            elif d==2:
                print("The day was Monday")
            elif d==3:
                    print("The day was Tuesday")
            elif d==4:
                print("The day was Wednesday")
            elif d==5:
                print("The day was Thursday")
            elif d==6:
                print("The day was Friday")


    elif 1800>year>1700:
        a=year-1700
        # print(a)
        x=a%4
        if x==0:
            if month==1:
                b=int(a/4)
                z=b+3
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")

            elif month==4:
                b=int(a/4)
                z=b+3
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="marc":
                month=4
                b=int(a/4)
                z=b+4
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="octo":
                month=1
                b=int(a/4)
                z=b+4
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
            elif month=="novem":
                month=4
                b=int(a/4)
                z=b+4
                c=int(a+z+date+month)
                d=c%7
                if d==0:
                    print("The day was Saturday")
                elif d==1:
                    print("The day was Sunday")
                elif d==2:
                    print("The day was Monday")
                elif d==3:
                    print("The day was Tuesday")
                elif d==4:
                    print("The day was Wednesday")
                elif d==5:
                    print("The day was Thursday")
                elif d==6:
                    print("The day was Friday")
        else:
            if month=="march" or month=="marc":
                month=4
            elif month=="october" or month=="octo":
                month=1
            elif month=="november" or month=="novem":
                month=4
            b=int(a/4)
            z=b+4
            c=int(a+z+date+month)
            d=c%7
            if d==0:
                print("The day was Saturday")
            elif d==1:
                print("The day was Sunday")
            elif d==2:
                print("The day was Monday")
            elif d==3:
                    print("The day was Tuesday")
            elif d==4:
                print("The day was Wednesday")
            elif d==5:
                print("The day was Thursday")
            elif d==6:
                print("The day was Friday")


    print("\n \n")
    ch=input("Do want to calculate more with the calculator made by robin ? y/n-------: ")
    if ch=="Y" or ch=="y":
        True
    elif ch=="n" or ch=="N":
        exit()
