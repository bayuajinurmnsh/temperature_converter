# membuat fungsi untuk konversi kelvin atau celsius ke Fahrenheit
# menambah default value di parameter, jadi ketika user lupa menambahkan argumen program tidak akan error
def conv_to_celsius_or_kelvin(temperature=0, temperature_unit='c'):
    # jika temperature_unit nya C atau c maka user akan melakukan konversi ke celsius
    if temperature_unit.lower() == 'c':
        # jika if terpenuhi akan dijalankan program dibawah
        celcius = float(temperature) - 273.15
        # balikkan nilai temperature yang sudah di convert
        return f"{temperature} K equals to{celcius:.2f} C"
    # jika temperature_unit nya K atau k maka user akan melakukan konversi ke kelvin
    elif temperature_unit.lower() == 'k':
        # jika elif terpenuhi akan dijalankan program dibawah
        kelvin = float(temperature) + 273.15
        # balikkan nilai temperature yang sudah di convert
        return f"{temperature} C equals to {kelvin:.2f} K"
    else:
        # balikkan nilai jika kondisi else terpenuhi
        return "please input a valid value"


# membuat fungsi untuk konversi kelvin atau celsius ke Fahrenheit
# menambah default value di parameter, jadi ketika user lupa menambahkan argumen program tidak akan error
def conv_to_fahrenheit(temperature=0, temperature_unit='c'):
    if temperature_unit.lower() == 'c':  # jika temperature_unit nya C atau c maka user melakukan input dari celsius

        # jika if terpenuji jalankan program dibawah
        fahrenheit = (float(temperature) * 9/5) + 32

        # balikkan nilai Celsius yang sudah di konversi ke fahrenheit
        return f"{temperature} C equals to {fahrenheit:.2f} F"

    elif temperature_unit.lower() == 'k':  # jika temperature_unit nya K atau k maka user melakukan input dari kelvin

        # jika else if terpenuhi jalankan program dibawah
        fahrenheit = (float(temperature) - 273.15) * 9/5 + 32

        # balikkan nilai Kelvin yang sudah di konversi ke fahrenheit
        return f"{temperature} K equals to {fahrenheit:.2f} F"
    else:  # jika temperature_unit tidak C atau c , atau K ata k
        # jika kondisi else terpenuhi jalankan program dibawah
        return "Please input a valid temperature unit like C for celcius and K for kelvin"


# membuat fungsi untuk konversi Fahrenheit ke kelvin atau celsius
# menambah default value di parameter, jadi ketika user lupa menambahkan argumen program tidak akan error
def conv_from_fahrenheit(temperature=0, temperature_unit='c'):
    if temperature_unit.lower() == 'c':  # jika temperature_unit nya C atau c maka user melakukan konversi dari Fahrenheit  ke Celsius

        # jika kondisi if terpenuhi jalankan program dibawah
        celcius = (float(temperature) - 32) * 5/9

        # balikkan nilai Celsius yang sudah di konversi dari fahrenheit
        return f"{temperature} F equals to {celcius:.2f} C"

    # jika temperature_unit nya K atau k maka user melakukan konversi dari Fahrenheit  ke Kelvin
    elif temperature_unit.lower() == 'k':

        # jika kondisi else if terpenuhi jalankan program dibawah
        kelvin = (float(temperature) - 32) * 5/9 + 273.15

        # balikkan nilai Kelvin yang sudah di konversi dari fahrenheit
        return f"{temperature} F equals to {kelvin:.2f} K"

    else:  # jika temperature_unit tidak C atau c , atau K ata k
        # jika kondisi else terpenuhi jalankan program dibawah
        return "Please input a valid temperature unit like C for celcius and K for kelvin"
