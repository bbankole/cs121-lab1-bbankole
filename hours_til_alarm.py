def main():
    # write your code here
    cur_time = int(input("what time is it now (0-23):"))

    set_alarm = int(input("time to set the alarm:"))

    alarm = (cur_time + set_alarm) % 24

    print("your alarm will go off in", alarm, "hours")


    
    return


if __name__ == '__main__':
    main()