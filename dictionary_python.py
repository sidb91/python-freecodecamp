#dictionaries - keys must be unique
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    4:"April",
    5:"May",
}

print(monthConversions[4])
print(monthConversions.get("Nov","Not a valid key"))
