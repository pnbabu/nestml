# Generated from PyNestMLLexer.g4 by ANTLR 4.10
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .PyNestMLLexerBase import PyNestMLLexerBase
else:
    from PyNestMLLexerBase import PyNestMLLexerBase

def serializedATN():
    return [
        4,0,89,694,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,1,
        0,1,0,1,0,1,0,1,1,3,1,189,8,1,1,1,1,1,1,2,4,2,194,8,2,11,2,12,2,
        195,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,207,8,4,10,4,12,4,210,
        9,4,1,4,1,4,4,4,214,8,4,11,4,12,4,215,1,4,1,4,1,5,1,5,5,5,222,8,
        5,10,5,12,5,225,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,234,8,6,1,6,
        1,6,1,6,3,6,239,8,6,3,6,241,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,44,1,44,1,45,1,45,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,
        1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,54,1,55,
        1,55,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,58,1,59,1,59,1,59,
        1,60,1,60,1,61,1,61,1,62,1,62,1,62,1,63,1,63,1,63,1,64,1,64,1,64,
        1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,1,67,1,68,1,68,1,68,1,69,
        1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,72,1,72,1,73,1,73,1,74,1,74,
        1,75,1,75,1,75,1,76,1,76,1,77,1,77,1,78,1,78,1,79,1,79,1,80,1,80,
        1,80,1,81,1,81,1,82,1,82,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,
        1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,1,83,3,83,628,8,83,
        1,84,1,84,1,84,4,84,633,8,84,11,84,12,84,634,1,84,3,84,638,8,84,
        1,84,3,84,641,8,84,1,84,3,84,644,8,84,1,84,5,84,647,8,84,10,84,12,
        84,650,9,84,1,84,1,84,1,85,3,85,655,8,85,1,85,5,85,658,8,85,10,85,
        12,85,661,9,85,1,86,4,86,664,8,86,11,86,12,86,665,1,87,1,87,3,87,
        670,8,87,1,88,3,88,673,8,88,1,88,1,88,1,88,1,88,1,88,3,88,680,8,
        88,1,89,1,89,3,89,684,8,89,1,89,1,89,1,89,1,90,1,90,3,90,691,8,90,
        1,90,1,90,2,208,215,0,91,1,3,3,0,5,4,7,5,9,6,11,7,13,8,15,9,17,10,
        19,11,21,12,23,13,25,14,27,15,29,16,31,17,33,18,35,19,37,20,39,21,
        41,22,43,23,45,24,47,25,49,26,51,27,53,28,55,29,57,30,59,31,61,32,
        63,33,65,34,67,35,69,36,71,37,73,38,75,39,77,40,79,41,81,42,83,43,
        85,44,87,45,89,46,91,47,93,48,95,49,97,50,99,51,101,52,103,53,105,
        54,107,55,109,56,111,57,113,58,115,59,117,60,119,61,121,62,123,63,
        125,64,127,65,129,66,131,67,133,68,135,69,137,70,139,71,141,72,143,
        73,145,74,147,75,149,76,151,77,153,78,155,79,157,80,159,81,161,82,
        163,83,165,84,167,85,169,86,171,87,173,88,175,89,177,0,179,0,181,
        0,1,0,7,2,0,9,9,32,32,2,0,10,10,13,13,4,0,10,10,13,13,34,34,92,92,
        4,0,36,36,65,90,95,95,97,122,5,0,36,36,48,57,65,90,95,95,97,122,
        1,0,48,57,2,0,69,69,101,101,714,0,1,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,
        0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,
        0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,
        0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,
        0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,
        0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,
        0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,
        0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,
        135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,
        0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,
        1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,
        0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,
        0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,1,183,1,0,0,0,3,188,1,0,0,0,5,
        193,1,0,0,0,7,199,1,0,0,0,9,204,1,0,0,0,11,219,1,0,0,0,13,240,1,
        0,0,0,15,244,1,0,0,0,17,252,1,0,0,0,19,257,1,0,0,0,21,264,1,0,0,
        0,23,272,1,0,0,0,25,277,1,0,0,0,27,286,1,0,0,0,29,293,1,0,0,0,31,
        300,1,0,0,0,33,303,1,0,0,0,35,308,1,0,0,0,37,313,1,0,0,0,39,317,
        1,0,0,0,41,323,1,0,0,0,43,326,1,0,0,0,45,331,1,0,0,0,47,335,1,0,
        0,0,49,339,1,0,0,0,51,342,1,0,0,0,53,346,1,0,0,0,55,357,1,0,0,0,
        57,364,1,0,0,0,59,371,1,0,0,0,61,379,1,0,0,0,63,385,1,0,0,0,65,396,
        1,0,0,0,67,406,1,0,0,0,69,413,1,0,0,0,71,423,1,0,0,0,73,429,1,0,
        0,0,75,436,1,0,0,0,77,447,1,0,0,0,79,457,1,0,0,0,81,463,1,0,0,0,
        83,474,1,0,0,0,85,485,1,0,0,0,87,498,1,0,0,0,89,513,1,0,0,0,91,515,
        1,0,0,0,93,519,1,0,0,0,95,521,1,0,0,0,97,523,1,0,0,0,99,525,1,0,
        0,0,101,527,1,0,0,0,103,529,1,0,0,0,105,531,1,0,0,0,107,533,1,0,
        0,0,109,535,1,0,0,0,111,538,1,0,0,0,113,540,1,0,0,0,115,543,1,0,
        0,0,117,546,1,0,0,0,119,549,1,0,0,0,121,552,1,0,0,0,123,554,1,0,
        0,0,125,556,1,0,0,0,127,559,1,0,0,0,129,562,1,0,0,0,131,565,1,0,
        0,0,133,568,1,0,0,0,135,571,1,0,0,0,137,574,1,0,0,0,139,577,1,0,
        0,0,141,580,1,0,0,0,143,583,1,0,0,0,145,585,1,0,0,0,147,587,1,0,
        0,0,149,589,1,0,0,0,151,591,1,0,0,0,153,594,1,0,0,0,155,596,1,0,
        0,0,157,598,1,0,0,0,159,600,1,0,0,0,161,602,1,0,0,0,163,605,1,0,
        0,0,165,607,1,0,0,0,167,627,1,0,0,0,169,629,1,0,0,0,171,654,1,0,
        0,0,173,663,1,0,0,0,175,669,1,0,0,0,177,679,1,0,0,0,179,683,1,0,
        0,0,181,690,1,0,0,0,183,184,5,34,0,0,184,185,5,34,0,0,185,186,5,
        34,0,0,186,2,1,0,0,0,187,189,5,13,0,0,188,187,1,0,0,0,188,189,1,
        0,0,0,189,190,1,0,0,0,190,191,5,10,0,0,191,4,1,0,0,0,192,194,7,0,
        0,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,1,0,
        0,0,196,197,1,0,0,0,197,198,6,2,0,0,198,6,1,0,0,0,199,200,5,92,0,
        0,200,201,3,3,1,0,201,202,1,0,0,0,202,203,6,3,0,0,203,8,1,0,0,0,
        204,208,3,1,0,0,205,207,9,0,0,0,206,205,1,0,0,0,207,210,1,0,0,0,
        208,209,1,0,0,0,208,206,1,0,0,0,209,211,1,0,0,0,210,208,1,0,0,0,
        211,213,3,1,0,0,212,214,3,3,1,0,213,212,1,0,0,0,214,215,1,0,0,0,
        215,216,1,0,0,0,215,213,1,0,0,0,216,217,1,0,0,0,217,218,6,4,1,0,
        218,10,1,0,0,0,219,223,5,35,0,0,220,222,8,1,0,0,221,220,1,0,0,0,
        222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,
        225,223,1,0,0,0,226,227,3,3,1,0,227,228,1,0,0,0,228,229,6,5,1,0,
        229,12,1,0,0,0,230,231,4,6,0,0,231,241,3,5,2,0,232,234,5,13,0,0,
        233,232,1,0,0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,236,5,10,0,0,
        236,238,1,0,0,0,237,239,3,5,2,0,238,237,1,0,0,0,238,239,1,0,0,0,
        239,241,1,0,0,0,240,230,1,0,0,0,240,233,1,0,0,0,241,242,1,0,0,0,
        242,243,6,6,2,0,243,14,1,0,0,0,244,245,5,105,0,0,245,246,5,110,0,
        0,246,247,5,116,0,0,247,248,5,101,0,0,248,249,5,103,0,0,249,250,
        5,101,0,0,250,251,5,114,0,0,251,16,1,0,0,0,252,253,5,114,0,0,253,
        254,5,101,0,0,254,255,5,97,0,0,255,256,5,108,0,0,256,18,1,0,0,0,
        257,258,5,115,0,0,258,259,5,116,0,0,259,260,5,114,0,0,260,261,5,
        105,0,0,261,262,5,110,0,0,262,263,5,103,0,0,263,20,1,0,0,0,264,265,
        5,98,0,0,265,266,5,111,0,0,266,267,5,111,0,0,267,268,5,108,0,0,268,
        269,5,101,0,0,269,270,5,97,0,0,270,271,5,110,0,0,271,22,1,0,0,0,
        272,273,5,118,0,0,273,274,5,111,0,0,274,275,5,105,0,0,275,276,5,
        100,0,0,276,24,1,0,0,0,277,278,5,102,0,0,278,279,5,117,0,0,279,280,
        5,110,0,0,280,281,5,99,0,0,281,282,5,116,0,0,282,283,5,105,0,0,283,
        284,5,111,0,0,284,285,5,110,0,0,285,26,1,0,0,0,286,287,5,105,0,0,
        287,288,5,110,0,0,288,289,5,108,0,0,289,290,5,105,0,0,290,291,5,
        110,0,0,291,292,5,101,0,0,292,28,1,0,0,0,293,294,5,114,0,0,294,295,
        5,101,0,0,295,296,5,116,0,0,296,297,5,117,0,0,297,298,5,114,0,0,
        298,299,5,110,0,0,299,30,1,0,0,0,300,301,5,105,0,0,301,302,5,102,
        0,0,302,32,1,0,0,0,303,304,5,101,0,0,304,305,5,108,0,0,305,306,5,
        105,0,0,306,307,5,102,0,0,307,34,1,0,0,0,308,309,5,101,0,0,309,310,
        5,108,0,0,310,311,5,115,0,0,311,312,5,101,0,0,312,36,1,0,0,0,313,
        314,5,102,0,0,314,315,5,111,0,0,315,316,5,114,0,0,316,38,1,0,0,0,
        317,318,5,119,0,0,318,319,5,104,0,0,319,320,5,105,0,0,320,321,5,
        108,0,0,321,322,5,101,0,0,322,40,1,0,0,0,323,324,5,105,0,0,324,325,
        5,110,0,0,325,42,1,0,0,0,326,327,5,115,0,0,327,328,5,116,0,0,328,
        329,5,101,0,0,329,330,5,112,0,0,330,44,1,0,0,0,331,332,5,105,0,0,
        332,333,5,110,0,0,333,334,5,102,0,0,334,46,1,0,0,0,335,336,5,97,
        0,0,336,337,5,110,0,0,337,338,5,100,0,0,338,48,1,0,0,0,339,340,5,
        111,0,0,340,341,5,114,0,0,341,50,1,0,0,0,342,343,5,110,0,0,343,344,
        5,111,0,0,344,345,5,116,0,0,345,52,1,0,0,0,346,347,5,114,0,0,347,
        348,5,101,0,0,348,349,5,99,0,0,349,350,5,111,0,0,350,351,5,114,0,
        0,351,352,5,100,0,0,352,353,5,97,0,0,353,354,5,98,0,0,354,355,5,
        108,0,0,355,356,5,101,0,0,356,54,1,0,0,0,357,358,5,107,0,0,358,359,
        5,101,0,0,359,360,5,114,0,0,360,361,5,110,0,0,361,362,5,101,0,0,
        362,363,5,108,0,0,363,56,1,0,0,0,364,365,5,110,0,0,365,366,5,101,
        0,0,366,367,5,117,0,0,367,368,5,114,0,0,368,369,5,111,0,0,369,370,
        5,110,0,0,370,58,1,0,0,0,371,372,5,115,0,0,372,373,5,121,0,0,373,
        374,5,110,0,0,374,375,5,97,0,0,375,376,5,112,0,0,376,377,5,115,0,
        0,377,378,5,101,0,0,378,60,1,0,0,0,379,380,5,115,0,0,380,381,5,116,
        0,0,381,382,5,97,0,0,382,383,5,116,0,0,383,384,5,101,0,0,384,62,
        1,0,0,0,385,386,5,112,0,0,386,387,5,97,0,0,387,388,5,114,0,0,388,
        389,5,97,0,0,389,390,5,109,0,0,390,391,5,101,0,0,391,392,5,116,0,
        0,392,393,5,101,0,0,393,394,5,114,0,0,394,395,5,115,0,0,395,64,1,
        0,0,0,396,397,5,105,0,0,397,398,5,110,0,0,398,399,5,116,0,0,399,
        400,5,101,0,0,400,401,5,114,0,0,401,402,5,110,0,0,402,403,5,97,0,
        0,403,404,5,108,0,0,404,405,5,115,0,0,405,66,1,0,0,0,406,407,5,117,
        0,0,407,408,5,112,0,0,408,409,5,100,0,0,409,410,5,97,0,0,410,411,
        5,116,0,0,411,412,5,101,0,0,412,68,1,0,0,0,413,414,5,101,0,0,414,
        415,5,113,0,0,415,416,5,117,0,0,416,417,5,97,0,0,417,418,5,116,0,
        0,418,419,5,105,0,0,419,420,5,111,0,0,420,421,5,110,0,0,421,422,
        5,115,0,0,422,70,1,0,0,0,423,424,5,105,0,0,424,425,5,110,0,0,425,
        426,5,112,0,0,426,427,5,117,0,0,427,428,5,116,0,0,428,72,1,0,0,0,
        429,430,5,111,0,0,430,431,5,117,0,0,431,432,5,116,0,0,432,433,5,
        112,0,0,433,434,5,117,0,0,434,435,5,116,0,0,435,74,1,0,0,0,436,437,
        5,99,0,0,437,438,5,111,0,0,438,439,5,110,0,0,439,440,5,116,0,0,440,
        441,5,105,0,0,441,442,5,110,0,0,442,443,5,117,0,0,443,444,5,111,
        0,0,444,445,5,117,0,0,445,446,5,115,0,0,446,76,1,0,0,0,447,448,5,
        111,0,0,448,449,5,110,0,0,449,450,5,82,0,0,450,451,5,101,0,0,451,
        452,5,99,0,0,452,453,5,101,0,0,453,454,5,105,0,0,454,455,5,118,0,
        0,455,456,5,101,0,0,456,78,1,0,0,0,457,458,5,115,0,0,458,459,5,112,
        0,0,459,460,5,105,0,0,460,461,5,107,0,0,461,462,5,101,0,0,462,80,
        1,0,0,0,463,464,5,105,0,0,464,465,5,110,0,0,465,466,5,104,0,0,466,
        467,5,105,0,0,467,468,5,98,0,0,468,469,5,105,0,0,469,470,5,116,0,
        0,470,471,5,111,0,0,471,472,5,114,0,0,472,473,5,121,0,0,473,82,1,
        0,0,0,474,475,5,101,0,0,475,476,5,120,0,0,476,477,5,99,0,0,477,478,
        5,105,0,0,478,479,5,116,0,0,479,480,5,97,0,0,480,481,5,116,0,0,481,
        482,5,111,0,0,482,483,5,114,0,0,483,484,5,121,0,0,484,84,1,0,0,0,
        485,486,5,64,0,0,486,487,5,104,0,0,487,488,5,111,0,0,488,489,5,109,
        0,0,489,490,5,111,0,0,490,491,5,103,0,0,491,492,5,101,0,0,492,493,
        5,110,0,0,493,494,5,101,0,0,494,495,5,111,0,0,495,496,5,117,0,0,
        496,497,5,115,0,0,497,86,1,0,0,0,498,499,5,64,0,0,499,500,5,104,
        0,0,500,501,5,101,0,0,501,502,5,116,0,0,502,503,5,101,0,0,503,504,
        5,114,0,0,504,505,5,111,0,0,505,506,5,103,0,0,506,507,5,101,0,0,
        507,508,5,110,0,0,508,509,5,101,0,0,509,510,5,111,0,0,510,511,5,
        117,0,0,511,512,5,115,0,0,512,88,1,0,0,0,513,514,5,64,0,0,514,90,
        1,0,0,0,515,516,5,46,0,0,516,517,5,46,0,0,517,518,5,46,0,0,518,92,
        1,0,0,0,519,520,5,40,0,0,520,94,1,0,0,0,521,522,5,41,0,0,522,96,
        1,0,0,0,523,524,5,43,0,0,524,98,1,0,0,0,525,526,5,126,0,0,526,100,
        1,0,0,0,527,528,5,124,0,0,528,102,1,0,0,0,529,530,5,94,0,0,530,104,
        1,0,0,0,531,532,5,38,0,0,532,106,1,0,0,0,533,534,5,91,0,0,534,108,
        1,0,0,0,535,536,5,60,0,0,536,537,5,45,0,0,537,110,1,0,0,0,538,539,
        5,93,0,0,539,112,1,0,0,0,540,541,5,91,0,0,541,542,5,91,0,0,542,114,
        1,0,0,0,543,544,5,93,0,0,544,545,5,93,0,0,545,116,1,0,0,0,546,547,
        5,60,0,0,547,548,5,60,0,0,548,118,1,0,0,0,549,550,5,62,0,0,550,551,
        5,62,0,0,551,120,1,0,0,0,552,553,5,60,0,0,553,122,1,0,0,0,554,555,
        5,62,0,0,555,124,1,0,0,0,556,557,5,60,0,0,557,558,5,61,0,0,558,126,
        1,0,0,0,559,560,5,43,0,0,560,561,5,61,0,0,561,128,1,0,0,0,562,563,
        5,45,0,0,563,564,5,61,0,0,564,130,1,0,0,0,565,566,5,42,0,0,566,567,
        5,61,0,0,567,132,1,0,0,0,568,569,5,47,0,0,569,570,5,61,0,0,570,134,
        1,0,0,0,571,572,5,61,0,0,572,573,5,61,0,0,573,136,1,0,0,0,574,575,
        5,33,0,0,575,576,5,61,0,0,576,138,1,0,0,0,577,578,5,60,0,0,578,579,
        5,62,0,0,579,140,1,0,0,0,580,581,5,62,0,0,581,582,5,61,0,0,582,142,
        1,0,0,0,583,584,5,44,0,0,584,144,1,0,0,0,585,586,5,45,0,0,586,146,
        1,0,0,0,587,588,5,61,0,0,588,148,1,0,0,0,589,590,5,42,0,0,590,150,
        1,0,0,0,591,592,5,42,0,0,592,593,5,42,0,0,593,152,1,0,0,0,594,595,
        5,47,0,0,595,154,1,0,0,0,596,597,5,37,0,0,597,156,1,0,0,0,598,599,
        5,63,0,0,599,158,1,0,0,0,600,601,5,58,0,0,601,160,1,0,0,0,602,603,
        5,58,0,0,603,604,5,58,0,0,604,162,1,0,0,0,605,606,5,59,0,0,606,164,
        1,0,0,0,607,608,5,39,0,0,608,166,1,0,0,0,609,610,5,116,0,0,610,611,
        5,114,0,0,611,612,5,117,0,0,612,628,5,101,0,0,613,614,5,84,0,0,614,
        615,5,114,0,0,615,616,5,117,0,0,616,628,5,101,0,0,617,618,5,102,
        0,0,618,619,5,97,0,0,619,620,5,108,0,0,620,621,5,115,0,0,621,628,
        5,101,0,0,622,623,5,70,0,0,623,624,5,97,0,0,624,625,5,108,0,0,625,
        626,5,115,0,0,626,628,5,101,0,0,627,609,1,0,0,0,627,613,1,0,0,0,
        627,617,1,0,0,0,627,622,1,0,0,0,628,168,1,0,0,0,629,648,5,34,0,0,
        630,643,5,92,0,0,631,633,7,0,0,0,632,631,1,0,0,0,633,634,1,0,0,0,
        634,632,1,0,0,0,634,635,1,0,0,0,635,640,1,0,0,0,636,638,5,13,0,0,
        637,636,1,0,0,0,637,638,1,0,0,0,638,639,1,0,0,0,639,641,5,10,0,0,
        640,637,1,0,0,0,640,641,1,0,0,0,641,644,1,0,0,0,642,644,9,0,0,0,
        643,632,1,0,0,0,643,642,1,0,0,0,644,647,1,0,0,0,645,647,8,2,0,0,
        646,630,1,0,0,0,646,645,1,0,0,0,647,650,1,0,0,0,648,646,1,0,0,0,
        648,649,1,0,0,0,649,651,1,0,0,0,650,648,1,0,0,0,651,652,5,34,0,0,
        652,170,1,0,0,0,653,655,7,3,0,0,654,653,1,0,0,0,655,659,1,0,0,0,
        656,658,7,4,0,0,657,656,1,0,0,0,658,661,1,0,0,0,659,657,1,0,0,0,
        659,660,1,0,0,0,660,172,1,0,0,0,661,659,1,0,0,0,662,664,7,5,0,0,
        663,662,1,0,0,0,664,665,1,0,0,0,665,663,1,0,0,0,665,666,1,0,0,0,
        666,174,1,0,0,0,667,670,3,177,88,0,668,670,3,179,89,0,669,667,1,
        0,0,0,669,668,1,0,0,0,670,176,1,0,0,0,671,673,3,173,86,0,672,671,
        1,0,0,0,672,673,1,0,0,0,673,674,1,0,0,0,674,675,5,46,0,0,675,680,
        3,173,86,0,676,677,3,173,86,0,677,678,5,46,0,0,678,680,1,0,0,0,679,
        672,1,0,0,0,679,676,1,0,0,0,680,178,1,0,0,0,681,684,3,173,86,0,682,
        684,3,177,88,0,683,681,1,0,0,0,683,682,1,0,0,0,684,685,1,0,0,0,685,
        686,7,6,0,0,686,687,3,181,90,0,687,180,1,0,0,0,688,691,3,97,48,0,
        689,691,3,145,72,0,690,688,1,0,0,0,690,689,1,0,0,0,690,691,1,0,0,
        0,691,692,1,0,0,0,692,693,3,173,86,0,693,182,1,0,0,0,25,0,188,195,
        208,215,223,233,238,240,627,634,637,640,643,646,648,654,657,659,
        665,669,672,679,683,690,3,0,1,0,0,2,0,1,6,0
    ]

class PyNestMLLexer(PyNestMLLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 2

    INDENT = 1
    DEDENT = 2
    DOCSTRING_TRIPLEQUOTE = 3
    WS = 4
    LINE_ESCAPE = 5
    DOCSTRING = 6
    SL_COMMENT = 7
    NEWLINE = 8
    INTEGER_KEYWORD = 9
    REAL_KEYWORD = 10
    STRING_KEYWORD = 11
    BOOLEAN_KEYWORD = 12
    VOID_KEYWORD = 13
    FUNCTION_KEYWORD = 14
    INLINE_KEYWORD = 15
    RETURN_KEYWORD = 16
    IF_KEYWORD = 17
    ELIF_KEYWORD = 18
    ELSE_KEYWORD = 19
    FOR_KEYWORD = 20
    WHILE_KEYWORD = 21
    IN_KEYWORD = 22
    STEP_KEYWORD = 23
    INF_KEYWORD = 24
    AND_KEYWORD = 25
    OR_KEYWORD = 26
    NOT_KEYWORD = 27
    RECORDABLE_KEYWORD = 28
    KERNEL_KEYWORD = 29
    NEURON_KEYWORD = 30
    SYNAPSE_KEYWORD = 31
    STATE_KEYWORD = 32
    PARAMETERS_KEYWORD = 33
    INTERNALS_KEYWORD = 34
    UPDATE_KEYWORD = 35
    EQUATIONS_KEYWORD = 36
    INPUT_KEYWORD = 37
    OUTPUT_KEYWORD = 38
    CONTINUOUS_KEYWORD = 39
    ON_RECEIVE_KEYWORD = 40
    SPIKE_KEYWORD = 41
    INHIBITORY_KEYWORD = 42
    EXCITATORY_KEYWORD = 43
    DECORATOR_HOMOGENEOUS = 44
    DECORATOR_HETEROGENEOUS = 45
    AT = 46
    ELLIPSIS = 47
    LEFT_PAREN = 48
    RIGHT_PAREN = 49
    PLUS = 50
    TILDE = 51
    PIPE = 52
    CARET = 53
    AMPERSAND = 54
    LEFT_SQUARE_BRACKET = 55
    LEFT_ANGLE_MINUS = 56
    RIGHT_SQUARE_BRACKET = 57
    LEFT_LEFT_SQUARE = 58
    RIGHT_RIGHT_SQUARE = 59
    LEFT_LEFT_ANGLE = 60
    RIGHT_RIGHT_ANGLE = 61
    LEFT_ANGLE = 62
    RIGHT_ANGLE = 63
    LEFT_ANGLE_EQUALS = 64
    PLUS_EQUALS = 65
    MINUS_EQUALS = 66
    STAR_EQUALS = 67
    FORWARD_SLASH_EQUALS = 68
    EQUALS_EQUALS = 69
    EXCLAMATION_EQUALS = 70
    LEFT_ANGLE_RIGHT_ANGLE = 71
    RIGHT_ANGLE_EQUALS = 72
    COMMA = 73
    MINUS = 74
    EQUALS = 75
    STAR = 76
    STAR_STAR = 77
    FORWARD_SLASH = 78
    PERCENT = 79
    QUESTION = 80
    COLON = 81
    DOUBLE_COLON = 82
    SEMICOLON = 83
    DIFFERENTIAL_ORDER = 84
    BOOLEAN_LITERAL = 85
    STRING_LITERAL = 86
    NAME = 87
    UNSIGNED_INTEGER = 88
    FLOAT = 89

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"COMMENT" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"\"\"'", "'integer'", "'real'", "'string'", "'boolean'", 
            "'void'", "'function'", "'inline'", "'return'", "'if'", "'elif'", 
            "'else'", "'for'", "'while'", "'in'", "'step'", "'inf'", "'and'", 
            "'or'", "'not'", "'recordable'", "'kernel'", "'neuron'", "'synapse'", 
            "'state'", "'parameters'", "'internals'", "'update'", "'equations'", 
            "'input'", "'output'", "'continuous'", "'onReceive'", "'spike'", 
            "'inhibitory'", "'excitatory'", "'@homogeneous'", "'@heterogeneous'", 
            "'@'", "'...'", "'('", "')'", "'+'", "'~'", "'|'", "'^'", "'&'", 
            "'['", "'<-'", "']'", "'[['", "']]'", "'<<'", "'>>'", "'<'", 
            "'>'", "'<='", "'+='", "'-='", "'*='", "'/='", "'=='", "'!='", 
            "'<>'", "'>='", "','", "'-'", "'='", "'*'", "'**'", "'/'", "'%'", 
            "'?'", "':'", "'::'", "';'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "DOCSTRING_TRIPLEQUOTE", "WS", "LINE_ESCAPE", 
            "DOCSTRING", "SL_COMMENT", "NEWLINE", "INTEGER_KEYWORD", "REAL_KEYWORD", 
            "STRING_KEYWORD", "BOOLEAN_KEYWORD", "VOID_KEYWORD", "FUNCTION_KEYWORD", 
            "INLINE_KEYWORD", "RETURN_KEYWORD", "IF_KEYWORD", "ELIF_KEYWORD", 
            "ELSE_KEYWORD", "FOR_KEYWORD", "WHILE_KEYWORD", "IN_KEYWORD", 
            "STEP_KEYWORD", "INF_KEYWORD", "AND_KEYWORD", "OR_KEYWORD", 
            "NOT_KEYWORD", "RECORDABLE_KEYWORD", "KERNEL_KEYWORD", "NEURON_KEYWORD", 
            "SYNAPSE_KEYWORD", "STATE_KEYWORD", "PARAMETERS_KEYWORD", "INTERNALS_KEYWORD", 
            "UPDATE_KEYWORD", "EQUATIONS_KEYWORD", "INPUT_KEYWORD", "OUTPUT_KEYWORD", 
            "CONTINUOUS_KEYWORD", "ON_RECEIVE_KEYWORD", "SPIKE_KEYWORD", 
            "INHIBITORY_KEYWORD", "EXCITATORY_KEYWORD", "DECORATOR_HOMOGENEOUS", 
            "DECORATOR_HETEROGENEOUS", "AT", "ELLIPSIS", "LEFT_PAREN", "RIGHT_PAREN", 
            "PLUS", "TILDE", "PIPE", "CARET", "AMPERSAND", "LEFT_SQUARE_BRACKET", 
            "LEFT_ANGLE_MINUS", "RIGHT_SQUARE_BRACKET", "LEFT_LEFT_SQUARE", 
            "RIGHT_RIGHT_SQUARE", "LEFT_LEFT_ANGLE", "RIGHT_RIGHT_ANGLE", 
            "LEFT_ANGLE", "RIGHT_ANGLE", "LEFT_ANGLE_EQUALS", "PLUS_EQUALS", 
            "MINUS_EQUALS", "STAR_EQUALS", "FORWARD_SLASH_EQUALS", "EQUALS_EQUALS", 
            "EXCLAMATION_EQUALS", "LEFT_ANGLE_RIGHT_ANGLE", "RIGHT_ANGLE_EQUALS", 
            "COMMA", "MINUS", "EQUALS", "STAR", "STAR_STAR", "FORWARD_SLASH", 
            "PERCENT", "QUESTION", "COLON", "DOUBLE_COLON", "SEMICOLON", 
            "DIFFERENTIAL_ORDER", "BOOLEAN_LITERAL", "STRING_LITERAL", "NAME", 
            "UNSIGNED_INTEGER", "FLOAT" ]

    ruleNames = [ "DOCSTRING_TRIPLEQUOTE", "NEWLINE_FRAG", "WS", "LINE_ESCAPE", 
                  "DOCSTRING", "SL_COMMENT", "NEWLINE", "INTEGER_KEYWORD", 
                  "REAL_KEYWORD", "STRING_KEYWORD", "BOOLEAN_KEYWORD", "VOID_KEYWORD", 
                  "FUNCTION_KEYWORD", "INLINE_KEYWORD", "RETURN_KEYWORD", 
                  "IF_KEYWORD", "ELIF_KEYWORD", "ELSE_KEYWORD", "FOR_KEYWORD", 
                  "WHILE_KEYWORD", "IN_KEYWORD", "STEP_KEYWORD", "INF_KEYWORD", 
                  "AND_KEYWORD", "OR_KEYWORD", "NOT_KEYWORD", "RECORDABLE_KEYWORD", 
                  "KERNEL_KEYWORD", "NEURON_KEYWORD", "SYNAPSE_KEYWORD", 
                  "STATE_KEYWORD", "PARAMETERS_KEYWORD", "INTERNALS_KEYWORD", 
                  "UPDATE_KEYWORD", "EQUATIONS_KEYWORD", "INPUT_KEYWORD", 
                  "OUTPUT_KEYWORD", "CONTINUOUS_KEYWORD", "ON_RECEIVE_KEYWORD", 
                  "SPIKE_KEYWORD", "INHIBITORY_KEYWORD", "EXCITATORY_KEYWORD", 
                  "DECORATOR_HOMOGENEOUS", "DECORATOR_HETEROGENEOUS", "AT", 
                  "ELLIPSIS", "LEFT_PAREN", "RIGHT_PAREN", "PLUS", "TILDE", 
                  "PIPE", "CARET", "AMPERSAND", "LEFT_SQUARE_BRACKET", "LEFT_ANGLE_MINUS", 
                  "RIGHT_SQUARE_BRACKET", "LEFT_LEFT_SQUARE", "RIGHT_RIGHT_SQUARE", 
                  "LEFT_LEFT_ANGLE", "RIGHT_RIGHT_ANGLE", "LEFT_ANGLE", 
                  "RIGHT_ANGLE", "LEFT_ANGLE_EQUALS", "PLUS_EQUALS", "MINUS_EQUALS", 
                  "STAR_EQUALS", "FORWARD_SLASH_EQUALS", "EQUALS_EQUALS", 
                  "EXCLAMATION_EQUALS", "LEFT_ANGLE_RIGHT_ANGLE", "RIGHT_ANGLE_EQUALS", 
                  "COMMA", "MINUS", "EQUALS", "STAR", "STAR_STAR", "FORWARD_SLASH", 
                  "PERCENT", "QUESTION", "COLON", "DOUBLE_COLON", "SEMICOLON", 
                  "DIFFERENTIAL_ORDER", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                  "NAME", "UNSIGNED_INTEGER", "FLOAT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "EXPONENT" ]

    grammarFileName = "PyNestMLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.onNewLine()
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[6] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


