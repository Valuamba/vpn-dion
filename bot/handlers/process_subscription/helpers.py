MonthLocale = {
    1: 'месяц',
    2: 'месяца',
    3: 'месяца',
    4: 'месяца',
    5: 'месяцев',
    6: 'месяцев',
    7: 'месяцев',
    8: 'месяцев',
    9: 'месяцев',
    10: 'месяцев',
    11: 'месяцев',
    12: 'месяцев'
}


DeviceLocale = {
    1: 'устройство',
    2: 'устройства',
    3: 'устройства',
    4: 'и более',
}


CurrencyLocale = {
    'RUB': '₽'
}


def get_device_locale(device_count: int, price, discount, currency: str) -> str:
    return '%s %s: %s %s (дешевле на %s)' % (device_count, DeviceLocale[device_count], price, CurrencyLocale[currency], str(discount) + '%')


def get_month_text(m_count):
    return '%s %s' % (m_count, MonthLocale[m_count])