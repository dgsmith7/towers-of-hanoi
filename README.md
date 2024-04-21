# TOWERS OF HANOI

### A simple python script to play Towers of Hanoi

## David G. Smith - Apr 2024

###############################################

### Example view in terminal window:

```
                   TOWERS OF HANOI
             Try to complete in 31 turns!
                     Turns:  0

           |             |             |
           *             |             |
          ***            |             |
         *****           |             |
        *******          |             |
       *********         |             |
      -----------   -----------   -----------
Please enter the 'from tower' and the 'to tower' separated by a dash (eg. 3-2)
 'r' to restart',
 'q' to quit:
```

### Installation:

From teh command line, clone this repo to your local machine with python3 installed

```
gh repo clone dgsmith7/towers-of-hanoi
```

### Rules:

The goal of the game is to move all of the discs from one tower to another. However, you cannot place a larger disc on top of a smaller disc, so accomplishing the goal will require the use of all three towers.

In this version of the game, there are 5 discs. For this reason, the minimum number of moves in which the goal can be accomplished is 31 (2^5-1).

As you play the game more often, you will start to see the pattern of movement required to minimize the number of moves to accomplish the goal. In fact there are algorithmic solutions to solve this problem, even recursive ones. None of those are implemented in this game. It is simply meant as a short mental vacation or meditation. Enjoy!!!

### Play:

Type the following to run the game:

```
python3 towers.py
```

There will be prompts displayed in the game, but generally do the following:
Enter simple commands comprised of the from-tower and the to-tower separated by a dash. For example, to move a disc from tower 1 to tower 2, the command you enter would be: `1-2`
ou can also type `q` or `Q` to quit.
Or you can type `r` or `R` to restart.

### Repository:

https://github.com/dgsmith7/towers-of-hanoi

# towers-of-hanoi
