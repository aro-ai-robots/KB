//parser for opencog
#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <streambuf>
#include <array>


using namespace std;

int main()
{
	std::ifstream inFile("insect_text");

	if (inFile.is_open())
	{
		std::string strLine;

		while (std::getline (inFile, strLine))
		{
			istringstream iss(strLine);
			string word;
			while(iss >> word){
				std::string newWord;
				char *chr = new char[word.length()];
				strcpy(chr,word.c_str());

				for(int i=0; i<strlen(chr); i++){
					if(!std::ispunct(chr[i])){
						newWord += chr[i];
					}
				}
				std::cout << newWord << "\n";
			}
		}

		inFile.close();
	}

	else std::cout << "Can't parse file.";

	return 0;

}
