'''
Name : Bayu Aji Nurmansah
Code : FSDO001ONL017
Assignment 2 python
'''

from temperature_converter import conv_to_celsius_or_kelvin, conv_to_fahrenheit, conv_from_fahrenheit


def assignment_2():  # membuat fungsi yang akan terus di panggil ketika program di run

    # stop condition , dimana program akan berhenti jika user melakukan input kata - kata di samping
    stop_condition = ["quit", "stop", "exit"]

    while True:  # program akan terus berulang, kondisi while akan selalu true

        print(
            "Program ini akan terus berulang sampai kamu melakukan input quit atau stop! \n")
        print("Silahkan pilih menu: ")
        print("Ketik a untuk konversi celsius ke kelvin atau kelvin ke celsius ")
        print("Ketik b untuk melakukan konversi suhu ke fahrenheit ")
        print("Pilih c untuk melakukan konversi dari fahrenheit ke kelvin atau celcius")

        # meminta user melakukan input dari terminal
        inp = input("Pilih menu: ")
        if inp.lower() in stop_condition:  # jika input == quit / stop / exit program akan berhenti
            break  # hentikan program

        if inp.lower() == 'a':  # jika user melakukan input A/a maka menu ini akan dipilih
            print("\n Konversi suhu dari/ke celsius/kelvin , kelvin/celsius")
            print("\n ket: c = Celsius | k = Kelvin")
            val_temperature = input("Masukkan Suhu : ")
            val_temperature_unit = input(
                "Akan di convert ke celcius / kelvin ? (c/k): ")
            # memanggil fungsi conv_to_celcius_or_kelvin kedalam variable result
            result = conv_to_celsius_or_kelvin(
                val_temperature, val_temperature_unit)
            print(result, '\n')

        if inp.lower() == 'b':  # jika user melakukan input B/b maka menu ini akan dipilih
            print("\n Konversi suhu dari/ke celsius/fahrenheit , kelvin/fahrenheit")
            print("\n ket: c = Celsius | k = Kelvin")
            val_temperature = input("Masukkan Suhu : ")
            val_temperature_unit = input(
                "Masukkan temperature unit,  celcius / kelvin ? (c/k): ")
            # memanggil fungsi conv_to_fahrenheit kedalam variable result
            result = conv_to_fahrenheit(val_temperature, val_temperature_unit)
            print(result, '\n')

        if inp.lower() == 'c':  # jika user melakukan input C/c maka menu ini akan dipilih
            print("\n Konversi suhu dari/ke fahrenheit/celsius , fahrenheit/kelvin")
            print("\n ket: c = Celsius | k = Kelvin")
            val_temperature = input("Masukkan Suhu : ")
            val_temperature_unit = input(
                "Akan di convert ke celcius / kelvin ? (c/k): ")
            # memanggil fungsi conv_from_fahrenheit kedalam variable result
            result = conv_from_fahrenheit(
                val_temperature, val_temperature_unit)
            print(result, '\n')


assignment_2()
