# CA326 Third Year Project - Testing Document

## "Predicto"

### Soccer Score Predictor and Fantasy League Web Application using Machine Learning

#### Ethan Harkin - 16350653

#### Daniel Smyth - 16380836

#### Supervisor: David Sinclair

### Testing

**1. User Testing/Usability Testing**

For user testing, we wrote out a series of tasks that we would get users to do. We then set a target time that users should get each task completed in. We carried out user testing on a random sample of 8 people who were present in the computer labs. This testing was done anonymously and no information was taken off the participants except for the length of time it took them to complete each task.

![User Testing Results](user_testing.png)

By carrying out user testing and usability testing, it helped us to identify any problems users could have with the site. If you examine the results above, you can see that one user had trouble finding the past predictions section for task number 11. This user proved to be an outlier however, as the rest of the users were able to find the section with relative ease. We took feedback from the users to help us improve the site as they pointed out any areas they felt could be made better.

**2. UI Testing**

We evaluated our user interface by using Nielson’s Heuristics and Schneiderman’s Rules. Below is a list of all the evaluation outlines which we compared our site to and critiqued it on.

1. Nielson's Heuristics

Nielson's Heuristics helped us evaluate the UI. The 10 heuristics are:

    1.	Visibility of system status
    
Our application has a lot of feedback messages which always keep the user up to date with what is going on.

    2.	Match between system and the real world
    
Our application does not use any big, fancy words or terms which may confuse the user. It uses very simple and easy to understand language.

    3.	User control and freedom
    
The users are completely in charge of what happens on the app. The system does not make any decisions for the user so they have complete power and freedom. The change password and edit prediction functions also offer undo and redo to the user.

    4.	Consistency and standards
    
The design of the pages stays consistent throughout the whole website. There are no ambiguous terms either and everything does exactly what it says it will do.

    5.	Error prevention
    
The application supports error prevention in the case where users must enter a positive whole number as a prediction for the number of goals that a team will score. There are also error messages throughout the site to guide the user.

    6.	Recognition rather than recall
    
Users are not required to recall much from their memory to use the site. They simply must remember their email and password to gain access to the site.

    7.	Flexibility and efficiency of use
    
The site is very efficient and carries out tasks very quickly. However, there are no shortcuts available to users.

    8.	Aesthetic and minimalistic design
    
Our website is quite basic and does not contain a large amount of images or media content. However, its simplistic design makes it very easy to use so new users should have no problem with it.

    9.	Help users recognize, diagnose, and recover from errors
    
The error messages which get displayed when users enter erroneous input prompt the user in the right direction. These error messages clearly tell the user where the source of the problem was and help them to amend the situation.

    10.	Help and documentation
    
Our application does not contain a help page, but we do not feel there is a need for one as it is a simple website to use. The user manual and video walkthrough would constitute as documentation for the application.


2. Schneiderman's Golden Rules

Schneiderman's Rules also helped us to evaluate our UI. The 8 rules are:

    1.	Strive for consistency
    
All the main pages of our site are designed in the same way. This type of consistency reiterates that feeling of familiarity with the user. We feel that our site is very consistent. 

    2.	Enable frequent users to use shortcuts
    
Our application did not really allow for any shortcuts. The only shortcut is if users are very familiar with the site they will be able to carry out tasks a lot faster than new users.

    3.	Offer informative feedback
    
We made sure to include lots of feedback messages in our application. Most actions a user carries out, for example registering and changing password, contain informative directions and feedback depending on what action was done.

    4.	Design dialogue to yield closure
    
Same as above, our application contains informative feedback messages which always let the user know what they are doing. These messages would certainly yield closure in the user.

    5.	Offer simple error handling
    
Our application contains a lot of error messages which prompt the user in the right direction if an erroneous input has been entered.

    6.	Permit easy reversal of actions
    
There is no action in our application which we feel could be reversible. Any action on the app results in success or an error message appearing on the screen.

    7.	Support internal locus of control
    
Users are in full control of the application. They can complete decide what happens which gives them a feeling of power.

    8.	Reduce short term memory load
    
Our application does not require users to remember much at all. They simply need to remember their email and password which is very straightforward.


**3. Unit Testing**

Unit testing was another vital part of the project. It helped us check for any unknown errors that there may have been in the code. We wrote up a total of 7 different tests. These tests were composed of 51 test cases. The 7 tests which were ran were:

Test1: This tested the length of the table and made sure it was always of length 20 as there are always 20 teams in the league.

Test2: This tested the number of games that were played in a season and made sure it was always equal to 380 as there are always 380 games in a season.

Test3: This tested that every player that was on a match day squad in past results had a corresponding mapping as they needed a rating to contribute towards squad value.

Test4: This tested that the squad values that a team were given by our assigner were correct. Two games per year were chosen at random and the team ratings were validated by this test.

Test5: This tested that the table which our table maker produced for the end of every season was the same as the actual final table that corresponded to the same year.

Test6: This was not used in the end but tested that every player listed in a club’s available squad of players for this season had a corresponding mapping. We discovered that a few players were being returned without a rating but all of these players were youth players who did not even get named on the bench for any game. They also did not have a FIFA rating to get mapped to. If they do get named in a match day squad, they will be assigned a value of 50 by our assigner but they are very irrelevant.

Test7: This tested for any unavailable players at the current moment and removed them from the top 18 players to ensure their ratings were not contributing towards team values.

**Overall Coverage**

Our unit testing provides very high coverage for the scraping and input data for both the website and the use of the neural network.  Our user testing and UI testing also provides us with coverage on the usability side of the product. This testing allowed us to see how users find actually using the application. It gave us valuable feedback which helped us improve the application.
