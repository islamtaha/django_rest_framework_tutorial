#include<bits/stdc++.h>

using namespace std;
int main(){
  int n;
  scanf("%d", &n);
  char s[n];
  scanf("%s", s);
  int cntI = 0;
  int cntA = 0;
  for(int i = 0; i < n; i++){
    if(char[i] == 'I'){
      cntI++;
    }else if(char[i] == 'A'){
      cntA++;
    }
  }
  if(cntI > 1){
    cout << 0;
  }else if(cntI == 1){
    cout << 1;
  }else {
    cout << cntA;
  }
  return 0;
}
