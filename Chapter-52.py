"""
Chapter 52: The locale Module
Section 52.1: Currency Formatting US Dollars Using the locale Module



"""
import locale
print(locale.setlocale(locale.LC_ALL, ''))
print(locale.currency(762559748.49))
print(locale.currency(762559748.49, grouping=True)) 
