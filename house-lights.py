'''
Problem statement:
Imagine there is a row of 8 houses.
Each house has a street light that turns on and off, denoted by 0 as off and 1 as on.
To determine whether or not to turn the lights on, each owner has to look
to their neighbours' street lights.
If either one neighbour's street lights is on or off, then owner will need to
turn the light on. Otherwise, it will be off.
If both neighbours lights are on, then the owner's light is off. Otherwise, if both are off,
then owner's light is on.
Since the two neighbours on each end only has one neighbour, they will only turn on the light
if their neighbor’s light was off the previous day. Otherwise, it stays off.

Example 1:
Input: [1, 1, 1, 0, 0, 0, 1, 0]

Output:[0, 1, 1, 1, 1, 0, 1, 0]

Explanation:
Since the first neighbour does not have a left neighbour, so it only check the light of the right neighbour.
In this case, it is 1. That means the first neighbour should turn off its light.

Then the subsequent neighbours should check for the lights from neighbours of each sides.

If the (left) neighbour for the last neighbour turn on it's light, then the last neighbour's light is turned off. Otherwise, it is on.

'''


def switchLights2(state):

    #first, we need to check the right neighbour of the first element is on or off
    if(state[0 + 1] == 1):
        state[0] = 0
    elif(state[0 + 1] == 0):
        state[0] = 1
    
    #then we evaluate each of the corresponding neighbours as long as it is not the first or last element
    #and update the appropriate states
    for i in range(1, len(state) - 1):
        if (state[i - 1] == 1 and state[i + 1] == 0 or state[i - 1] == 0 and state[i + 1] == 1
        or state[i - 1] == 0 and state[i + 1] == 0):
            state[i] = 1
        elif((state[i - 1] == 1 and state[i + 1] == 1)):
            state[i] = 0
    
    #then finally we check the left neighbour of the last element is on or off 
    if state[len(state) - 2] == 1:
        state[len(state) - 1] = 0
    elif state[len(state) - 2] == 0:
        state[len(state) - 1] = 1


    print(f"Final state:  {state}")



state = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0]

print(f"Inital state: {state}")
"Output: [0, 1, 1, 1, 1, 0, 1, 0]"
switchLights2(state)
print()
state = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
print(f"Inital state: {state}")
"Output:[0, 1, 0, 1, 0, 1, 1, 0]"
switchLights2(state)
