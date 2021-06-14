import time
import threading

def clock(hours, minutes, seconds):
    global stop_threads

    while True:
        if stop_threads:
            break
            
        time.sleep(1)
        if (seconds == 60):
            seconds = 0
            minutes += 1

        if (minutes == 60):
            minutes = 0
            hours += 1

        if (hours == 24):
            hours = 0

        if hours < 10:
            smallhours = "0" + str(hours)
        else:
            smallhours = str(hours)

        if minutes < 10:
            smallminutes = "0" + str(minutes)
        else:
            smallminutes = str(minutes)

        if seconds < 10:
            smallseconds = "0" + str(seconds)
        else:
            smallseconds = str(seconds)

        print(str(smallhours + ":" + smallminutes + ":" + smallseconds))
        seconds += 1


if __name__ == '__main__':
    print("! Witaj w timerze ! \n")
    print("Dostepne funkcje w programie: ")
    print("  E/e - wyjscie z programu ")
    print("  N/n - aktualna godzina \n")
    print("  Zmien godzine ")
    print("      format HH MM SS (wpisz godzine)")

    global stop_threads

    Hours = int(time.strftime("%H"))
    Minutes = int(time.strftime("%M"))
    Seconds = int(time.strftime("%S"))

    while True:
        input1 = input("")
        words = input1.split()
        try:
            if words[0] == "N" or words[0] == "n":
                Hours = int(time.strftime("%H"))
                Minutes = int(time.strftime("%M"))
                Seconds = int(time.strftime("%S"))

            elif words[0] == "E" or words[0] == "e":
                stop_threads = True
                time.sleep(1)
                break

            else:
                Hours = int(words[0])
                Minutes = int(words[1])
                Seconds = int(words[2])

            stop_threads = True
            time.sleep(1)
            stop_threads = False

            t = threading.Timer(1, clock, [Hours, Minutes, Seconds])
            t.start()
        except:
            print("Zly format")

    t.join()
