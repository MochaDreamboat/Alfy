# Dictionaries

# Convert 3-digit abbrev. to full month

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "July": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Jan"])

# .get() can specify default key values
print(monthConversions.get("Hi","Not a valid key"))