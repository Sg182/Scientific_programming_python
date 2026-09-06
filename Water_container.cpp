#include <iostream>
using namespace std;


double max_area(int arr[], int size){

    int left;
    int right;
    double max_area = 0;
     
    //int size = sizeof(arr)/sizeof(arr[0]);

    left = 0;
    right = size - 1; 

    while(left < right){
        
        double width = right - left;
        double area = width*min(arr[right], arr[left]);

        if (area > max_area ){
            max_area = area;
        }
        if (arr[left] < arr[right]){
            left++;
        }
        else{
            right--;
        }

    }
    return max_area;
}

int main(){

    int height[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int size = sizeof(height)/sizeof(height[0]);


    cout << "THE MAXIMUM AREA OF WATER CONTAINER IS = "<< max_area(height,size)<< endl;
}