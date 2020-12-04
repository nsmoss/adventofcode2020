#!/usr/bin/env python

import re

def createpassports(passportfile):
    passports = open(passportfile).read().split("\n\n")
    return passports

def cleanpassport(passport):
    passportlist = passport.split()
    sorted_passport = [psprt.split(":") for psprt in passportlist]
    passdict = {fields[0]: fields[1] for fields in sorted_passport}
    return passdict

def testpassports(passportfile):
    passports = createpassports(passportfile)

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validcount = 0

    for passport in passports:
        validity = True
        clean_passport = cleanpassport(passport)
        for field in required_fields:
            if field not in clean_passport:
                validity = False
                break
            elif testfields(clean_passport.get(field), field) == False:
                validity = False
                break
        if validity == True:
            validcount += 1
    return validcount

def testfields(fieldvalue, field):
    if field == "byr":
        if int(fieldvalue) >= 1920 and int(fieldvalue) <= 2002:
            return True
    if field == "iyr":
        if int(fieldvalue) >= 2010 and int(fieldvalue) <= 2020:
            return True
    if field == "eyr":
        if int(fieldvalue) >= 2020 and int(fieldvalue) <= 2030:
            return True
    if field == "hgt":
        if fieldvalue.endswith("cm"):
            if int(fieldvalue[:-2]) >= 150 and int(fieldvalue[:-2]) <= 193:
                return True
        if fieldvalue.endswith("in"):
            if int(fieldvalue[:-2]) >= 59 and int(fieldvalue[:-2]) <= 76:
                return True
    if field == "hcl":
        if re.search(r'\#[a-f0-9]{6}', fieldvalue):
            return True
    if field == "ecl":
        if re.search(r'amb|blu|brn|gry|grn|hzl|oth', fieldvalue):
            return True
    if field == "pid":
        if fieldvalue.isdecimal() and len(fieldvalue) == 9:
            return True
    return False

if __name__ == "__main__":
    print(testpassports("day4input.txt"))
