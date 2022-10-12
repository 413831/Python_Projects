class ConvertidorTemperatura:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def celsius_fahrenheit(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alta: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def fahrenheit_celsius(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alta: {fahrenheit}')
        return (fahrenheit - 32) * 5/9


if __name__ == '__main__':
    resultado = ConvertidorTemperatura.celsius_fahrenheit(15)
    print(f'15 C° es equivalente a F°: {resultado:.2f}')
    resultado = ConvertidorTemperatura.fahrenheit_celsius(70)
    print(f'70 F° es equivalente a C°: {resultado:.2f}')