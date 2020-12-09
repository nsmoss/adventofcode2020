#!/usr/bin/env python

def createpassports(passportfile):
    passports = open(passportfile).read().split("\n\n")
    return passports

def testpassports(passportfile):
    passports = createpassports(passportfile)

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validcount = 0

    for passport in passports:
        validity = True
        for field in required_fields:
            if field not in passport:
                validity = False
                break
        if validity == True:
            validcount += 1
    return validcount

print(testpassports("day4input.txt"))
