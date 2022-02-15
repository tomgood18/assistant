# Voice Assistant Application
# query.py
# Author: Thomas Good - 13/02/22

# Interrogative = First word of a question (e.g. What, Why, When).
# Subject = The noun or pronoun-based part of a sentence. (e.g. Time, Definition)
# Predicate = The verb-based part that the subject performs. (e.g. Tell, Define)

# For more info on sentence structure: https://qa-faq.com/en/Q%26A/page=9e3a93cd7ee0799945f6212d4ec828d2

import os
import sys
import what

def scan(query):
    print("Scanning...");
    wordList = query.split();
    interrogative = wordList[0].lower() 
    if interrogative == "what":
        what.init(query, 0)
        return(ClassPlaceholder("what"));
    elif interrogative == "when":
        return(ClassPlaceholder("when"));
    elif interrogative == "why":
        return(ClassPlaceholder("why"));
    elif interrogative == "who":
        return(ClassPlaceholder("who"));
    elif interrogative == "where":
        return(ClassPlaceholder("where"));
    elif interrogative == "which":
        return(ClassPlaceholder("which"));
    elif interrogative == "whose":
        return(ClassPlaceholder("whose"));
    elif interrogative == "how":
        return(ClassPlaceholder("how"));
    elif interrogative == "are":
        return(ClassPlaceholder("are"));
    elif interrogative == "do":
        return(ClassPlaceholder("do"));
    elif interrogative == "should":
        return(ClassPlaceholder("should"));
    elif interrogative == "is":
        return(ClassPlaceholder("is"));
    else:
        return(ClassPlaceholder("else"));


def ClassPlaceholder(className):
    return("<placeholder for '" + className + "' class functions>");







    