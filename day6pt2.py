#!/usr/bin/env python

def creategroups(answerfile):
    groups = open(answerfile).read().split("\n\n")
    clean_groups = [group.splitlines() for group in groups]
    return clean_groups

def groupcount(group):
    questions = set(group[0])
    for person in group:
        questions = questions.intersection(set(person))
    return len(questions)

def groupsum(answerfile):
    groups = creategroups(answerfile)
    count_sum = 0
    for group in groups:
        count_sum += groupcount(group)
    return count_sum

if __name__ == "__main__":
    print(groupsum("day6input.txt"))
