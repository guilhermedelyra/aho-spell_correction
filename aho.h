#ifndef _aho
#define _aho

#include <vector>
#include <string>
#include <queue>
#include <string.h>
#include <iostream>
#include <locale>
#include <codecvt>
#include <map>

int buildMatchingMachine(const std::vector<std::string> & words, int (&f)[310], int (&g)[310][224], int (&out)[310]);
int findNextState(int currentState, int nextInput, int (&f)[310], int (&g)[310][224]);
std::map < std::string, std::vector <int> > search (std::vector<std::string> keywords, std::string text);

#endif