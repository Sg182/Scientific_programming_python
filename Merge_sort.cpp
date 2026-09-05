#include <iostream>
using namespace std;


void merge_array(int A[], int n, int B[], int m, int C[]){

    int i = 0;
    int j = 0;
    int k = 0;

    while (i < n && j < m){
        if (A[i] < B[j]){
            C[k] = A[i];
            i++;
        }

        else {
            C[k] = B[j];
            j++;
        }

        k++;
    }

    // MERGE THE REMAINING  A ARRAY (IF A IS LEFT)
    while (i < n){
        C[k] = A[i];
        i++;
        k++;
    }
    // MERGE THE REMAINING B ARRAY (IF B IS LEFT)
    while (j < n){
        C[k] = B[j];
        j++;
        k++;
    }



}
int main() {

    int A[] = {1, 4, 7, 10};
    int B[] = {2, 3, 8, 12};

    int n = sizeof(A) / sizeof(A[0]);
    int m = sizeof(B) / sizeof(B[0]);

    int* C = new int[n + m];

    merge_array(A,n,B,m,C);
     
    cout << "[";
    for (int i =0; i < n+m;i++){
        cout << C[i]<<" ";
    }

    cout <<"]";

    delete[] C;

    return 0;
}