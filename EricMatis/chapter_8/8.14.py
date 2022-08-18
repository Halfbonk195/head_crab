def build_car(mark, manufacturer, **kwargs):
    kwargs['mark'] = mark
    kwargs['manufacturer'] = manufacturer
    return kwargs


my_car = build_car('S', 'Subaru', color='blue', tow_package=True, pedal='Low')
print(my_car)
