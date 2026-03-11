class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, example):
        if example.hours is None:
            hours = (7 - example.rest_days)*8
            return cls(example.name, hours, example.rest_days,example.email)
        return cls(example.name, example.hours, example.rest_days, example.email) 

    @classmethod
    def get_email(cls, example):
        if example.email is None:
            email = f"{example.name}@email.com"
            return cls(example.name, example.hours, example.rest_days, email)
        return cls(example.name, example.hours, example.rest_days, example.email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment


    def salary(self):
        return f"Заработная плата: {self.hours*self.__class__.hourly_payment}"                



