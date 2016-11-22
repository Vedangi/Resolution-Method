
******************************************************************
Author: Nikhil Jain UIN 725004355
******************************************************************

README File for Running First Order Logic: Theorem Prover


Kindly follow the below instructions to run the code.


1. Use Python IDLE for Python 2.7. Using the python command prompt is highly recommended.

2. Open the Python file in command line using the following command: 
python <filename.py> <method_name> <problem name> <Outerloop index>

3. We have the following name for the method name and problem name
   method-name = unit-preference        (For unit preference)
   method-name = two-pointer            (For two pointer strategy)
4. Problem name  should be like
    Howling hound problem   =  howling 
    Roadrunner problem      =  roadrunner
    Drugdealer problem      =  drugdealer
    Harmonia problem        =  Harmonia 
    Harmonia QuestionAnswer =  HarmoniaAnswer
    Customized Problem      =  Problem5
5. Please provide the integer number for outer loop index
    Howling hound problem   =  6
    Roadrunner problem      =  7
    Drugdealer problem      =  7
    Harmonia problem        =  7
    Harmonia QuestionAnswer =  8
    Customized Problem      =  10



6. Enter the correct input to proceed example below:
   python prover.py two-pointer howling 6


   for unit preference give input
   python prover.py unit-preference howling  (no index is needed)

7. If all the above steps are followed correctly, you should see the List of Clauses resolved by the Theorem Prover.
# Resolution-Method
