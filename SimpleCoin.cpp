//
//  SimpleCoinproblem.cpp
//  DynamicProgram
//
//  Created by Pranav on 4/18/15.
//  Copyright (c) 2015 Minimum Apps. All rights reserved.
//

#include <iostream>

using namespace std;

/*
 findMinCoins
 
 */

void findMinCoins(int sum, int coinValues[], int numCoins) {
    int minValues[sum+1];
    int coinsUsed[sum+1][2];
    
    // Intialise
    for (int i=0; i < sum+1; i++) {
        minValues[i] = 99999;
    }
    
    minValues[0] = 0;
    coinsUsed[0][0] = 0;
    coinsUsed[0][1] = 0;
    
    // Find Minimum
    for (int i = 1; i < sum+1; i++) {
        for (int j = 0; j < numCoins; j++) {
            if (coinValues[j] == i) {
                minValues[i] = 1;
                coinsUsed[i][0] = coinValues[j];
                coinsUsed[i][1] = 0;
            } else if (coinValues[j] <= i && ((minValues[i - coinValues[j]] + 1) < minValues[i])) {
                minValues[i] = (minValues[i - coinValues[j]] + 1);
                coinsUsed[i][0] = coinValues[j];
                coinsUsed[i][1] = (i - coinValues[j]);
            }
        }
    }
    
    // Print Result
    for (int k = 0; k < sum + 1; k++) {
        cout << "Coin " << k << " \t" << coinsUsed[k][0] << " (" << coinsUsed[k][1] << ")" << endl;
    }
    
}


/*
 List has about 'N' coins values are (V1,
 
 */

int main(int argc, const char * argv[]) {
    
    int totalCoins;
    
    cout << "Enter number of coins: ";
    cin >> totalCoins;
    cout << endl;
    
    int temp = 0;
    int coinValues[totalCoins];
    int sum = 0;
    
    while (temp < totalCoins) {
        cout << "Enter the value of coin [" << temp << "]" << ":";
        cin >> coinValues[temp];
        cout << endl;
        temp++;
    }
    
    cout << "Enter the values of Sum: ";
    cin >> sum;
    
    findMinCoins(sum, coinValues, totalCoins);
    
    
    return 0;
}
