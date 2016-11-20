#!/usr/bin/python
# Authors
# Michael McConnell, Aaron Jaeger, Erin Esco, Rene Jacques
# References
# The iterative deepening search was based off the pseudo code found on wikipedia at https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

import sys
import string
import json

# Function to read all lines from a given file
def readfile(filename):
    f = open(filename)
    script = f.readlines()
   
    f.close()
    return script

def writeJson(script):
    response = 0
    resDict = {} 
    for l in script: 
        if ('Response2' == l[0]): 
            response += 1
            resNum = 'response' + str(response)
            resDict [resNum] = l[1]
    with open('script.json', 'w') as json_file: 
        json_file.write(json.dumps(resDict))

    print resDict
    raw_input()

def writeRule(script, person_role):
    lines = []
    rule = ["TopRule = ("]
    line_count = 0
    for line in script:
        if line[0] == person_role:
            line_count +=1
            lines.append("line" + str(line_count) + "= " + line[1] + ";" )
            rule.append("$line" + str(line_count) + "{response='response" + str(line_count) + "'}|")
            
    rule[-1] = ("$line" + str(line_count) + "{response='response" + str(line_count) + "'}")
    rule.append(");")

    rule += lines 
    print rule
    with open('filename.rule', 'w+') as rule_file: 
        for l in rule:
            print l
            rule_file.write(l + "\n")
    

# TopRule =  (
# Main execution function runs on startup
def main():
    filename = sys.argv[1]
    script = readfile(filename)
    play = []
    person_role = None
    for line in script:
        char = line.split(":")[0].strip()
        if person_role == None:
            person_role = char
        print line   
        words = line.split(":")[1].strip().lower().translate(None, string.punctuation)

        play.append((char, words))

    writeJson(play)
    writeRule(play, person_role)

main() 



