#LESSONS LEARNED: RANGE(), [:-1] (This removed the last character in the string so we could continue the for loop for every other possible option), RECURSION, HOW THE CALL STACK WORKS

# GUIDELINE FOR PROBLEM

# * Write a function that generates every sequence of throws a single
# * player could throw over a three-round game of rock-paper-scissors.
# *
# * Your output should look something like:
# *   ["RRR",
# *    "RRP",
# *    "RRS",
# *    "RPR",
# *    ...etc...
# *   ]
# *
# * Extra credit:
# *   - Make your function return answers for any number of rounds.
# *
# * Example:
# * rockPaperScissors(5); // => ['RRRRR', 'RRRRP', 'RRRRS', etc...]
# *
# */

#MY ATTEMPT

# #creating a function that takes in a number of rounds parameter
# def rockPaperScissors(rounds):
#     #result is the list that will hold all of the string answers
#     result = []
#     #all of the options for a round
#     a = "R"
#     b = "P"
#     c = "S"
#     #while it isn't round 0, check for every possible answer
#     while rounds > 0:
#         #creating the sequence for the options within a round
#         sequence = ""
#         for sequence[0] in sequence:
#             if sequence[0] != a:
#                 sequence += a
#             elif sequence[0] == a and sequence[0] != b:
#                 sequence += b
#         #push the string answer into the result list
#         result.append(sequence)
#         rounds = rounds - 1
#     return(result)

# print(rockPaperScissors(1))

# TYLERS SOLUTION
def rockPaperScissors():
  result = []
  options = ['R', 'P', 'S']
  def buildSeq(currentSeq):
    if len(currentSeq) == 3:
      result.append(currentSeq)
      return
    else:
      for x in range(3):
        currentSeq += options[x]
        buildSeq(currentSeq)
        currentSeq = currentSeq[:-1]
  buildSeq('')
  return result

print(rockPaperScissors())
