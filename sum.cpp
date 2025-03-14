#include <iostream>
using namespace std;
#include <cstdlib>

// COMMAND LINE PARAM & PASSING FUNCTION TO ARRAY(2 FUNCT) PRACTICE

int main(int argc, char* argv[]) {
  int sum = 0;
  for (int i=1; i <= argc; i++) {
    
    sum += atoi(argv[i]);
    
  }
  cout << "SUM IS" << sum << endl;
  return 0;
  

  
}
