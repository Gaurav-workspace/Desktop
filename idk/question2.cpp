#include<iostream>
using namespace std;
void setArrayData(int** array,int m,int n){
    int inputValue;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            cout<<"Enter the value of A["<<i<<"]["<<j<<"] : ";
            cin>>inputValue;
            array[i][j] = inputValue;
        }
    }
}
int getAverage(int** array,int m,int n){
    int sum = 0;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            sum += array[i][j];
        }
    }
    int totalValues = m*n;
    return sum/(totalValues);
}
int findMax(int** array,int m,int n){
    int maxValue = array[0][0];
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (array[i][j]>maxValue){
                maxValue = array[i][j];
            }
        }
    }
    return maxValue;
}
void displayArray(int** array,int m,int n){
    cout<<"Displaying Your Array..."<<endl;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            cout<<array[i][j]<<" ";
        }
        cout<<endl;
    }
}
int main(){
    int m = 3;
    int n = 3;
    int** array = new int*[m];
    for (int i = 0; i < m; i++){
        array[i] = new int[n];
    }

    setArrayData(array,m,n);
    displayArray(array,m,n);

    int avg = getAverage(array,m,n);
    int maxValue = findMax(array,m,n);
    cout<<"The average of all values is : "<<avg<<endl;
    cout<<"The maximum value present in 2D array : "<<maxValue<<endl;
    
    return 0;
}
