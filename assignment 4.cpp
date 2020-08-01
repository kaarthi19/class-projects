#include <iostream> //defining library
using namespace std;

double x, y, xc, yc, a, b, p, q, r, A, B, limA, limB, sum;
int x1, y1;
string nName;

double textCheck (double p)
{
    while(!(cin >> p))                                                              //while loop to check what kind of input (rejects text)
       {
           cout << "Error! Enter a number: \n";                                     //error message
           cin.clear();                                                             //clears the first input
           cin.ignore(123, '\n');                                                   //ignores the first input
       }
    return p
}
double limFunction (double x, double y, string nName)                               //setting a funtion for repeated set of instructions (for PART 1)
{
    cout << "Enter a limit for the " << nName << " number. \n";                     //text message for the user to input a limit
    y = textCheck (q);
    
    y1 = y;
    yc = y - y1;
    
    while(!(yc == 0))                                                               //while loop to check what kind of input (rejects floats and accepts only integers)
    {
        cout << "Error! Enter a whole number: \n";
        
        y = textCheck (q);
        
        y1 = y;
        yc = y - y1;
    }
    
    cout << "Your limit for the " << nName << " number is " << y << ".\n";          //displays the limit set
    cout << "Enter a value for the " << nName << " number. \n";                     //text message for the user to input a number
    
    x = textCheck (r);
    
    x1 = x;
    xc = x - x1;
    
    while(!(xc == 0))                                                               //while loop to check what kind of input (rejects floats and accepts only integers)
    {
        cout << "Error! Enter a whole number: \n";
        
        x = textCheck (r);
        
        x1 = x;
        xc = x - x1;
    }
    
    
    while (x>=y) // using a while loop to check the limit and the number
    {
        cout << "Your value exceeds the limit set. \nPlease enter a new value. \n"; //error message
        
        x = textCheck(r);
            
        x1 = x;
        xc = x - x1;
        
        while(!(xc == 0))                                                           //while loop to check what kind of input (rejects floats and accepts only integers)
        {
            cout << "Error! Enter a whole number: \n";                              //error message
            
            x = textCheck(r);
            
            x1 = x;
            xc = x - x1;
        }
    }
    
    return x;                                                                       //returns the value to the function
}

int main ()                                                                         //main function
{
    
    cout << "Welcome to your personal Integer Calculator.\n";
    a = limFunction (A, limA, "first");                                             //PART 1 (the operations are done in limFunction function)
    b = limFunction (B, limB, "second");                                            //PART 2 (uses the same function as PART 1)
    
    sum = a + b;                                                                    //PART 3(sums up the numbers)
    
    cout << "The sum of the numbers are \n" << sum;
    
    cout << "\nThank you and goodbye";
    
    return 0;
}
