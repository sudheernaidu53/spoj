#include<iostream>
using namespace std;
#define depth 15 //why? because that is maximum i have to take care of 7 steps in a direction and comeback 

long long way[15][depth][depth]; // n is less than 15. so way[15] actually it could be reduced to 14 way[j][k][l] tells that there are jnumber of ways you can take from middle point to [k][l]
int list[15];
int stepNum;

void print_list( void )
{
    way[0][7][7] = 1; // 2 direction. and because we don't want negative indices, start from middle=7, you can go till 0 only way[0][7][7] is 1. everything else is 0
    // for (int i = 0; i < 14; i++){
    // for (int j = 0; j < 14; j++)
    //     {cout << i<< j<< " " <<way[0][i][j]<<endl;} }  
    // cout<< way[0][0][0] <<endl;
    for ( int numstep = 1; numstep <= 14; numstep++) {
        for ( int i = 1; i < depth; i++ ) {
            for ( int j = 1; j < depth; j++ ) {
                // cout << way[numstep-1][i][j+1]<< way[numstep-1][i][j-1] <<endl;
                way[numstep][i][j] = way[numstep-1][i][j+1]+way[numstep-1][i][j-1]
                                +way[numstep-1][i+1][j]+way[numstep-1][i-1][j]
                                +way[numstep-1][i+1][j-1]+way[numstep-1][i-1][j+1]; // 6 directions
            }
        }
        list[numstep] = way[numstep][7][7];
    }
    // for (int i=0; i < 15; i++){
    //     cout<<list[i]<<endl;
    // }
    // for (int m =0; m<=6;m++){
    //         for (int o=0;o<depth;o++){
    //             for (int q=0;q<depth;q++){
    //                 cout<<m<<" "<<o<<" "<<q<<" "<<way[m][o][q]<<endl;
    //             }
    //         }
    //     }   
    
}

int main( void )
{ 
    int caseNum;

    print_list();
    cin >> caseNum;
    while ( caseNum-- ) {
        cin >> stepNum;
        cout << list[stepNum] << endl;
    }
    return 0;
}