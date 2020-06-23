#include "TInterpreter.h"
#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"

#include <iostream>
#include <vector>
#include <set>
#include <map>

void stl_containers() {
  TFile* file = new TFile("stl_containers.root", "RECREATE");
  TTree* tree = new TTree("tree", "");

  std::vector<int32_t> vector_int32;
  tree->Branch("vector_int32", &vector_int32);

  std::vector<std::string> vector_string;
  tree->Branch("vector_string", &vector_string);

  std::vector<const char*> vector_charstar;
  tree->Branch("vector_charstar", &vector_charstar);

  std::vector<std::vector<int32_t>> vector_vector_int32;
  gInterpreter->GenerateDictionary("vector<vector<int> >", "vector");
  tree->Branch("vector_vector_int32", &vector_vector_int32);

  std::vector<std::vector<std::string>> vector_vector_string;
  gInterpreter->GenerateDictionary("vector<vector<string> >", "vector;string");
  tree->Branch("vector_vector_string", &vector_vector_string);

  std::vector<std::vector<const char*>> vector_vector_charstar;
  gInterpreter->GenerateDictionary("vector<vector<const char*> >", "vector");
  tree->Branch("vector_vector_charstar", &vector_vector_charstar);

  std::vector<std::set<int32_t>> vector_set_int32;
  gInterpreter->GenerateDictionary("vector<set<int> >", "vector;set");
  tree->Branch("vector_set_int32", &vector_set_int32);

  std::set<int32_t> set_int32;
  tree->Branch("set_int32", &set_int32);

  vector_int32.clear();
  vector_int32.push_back(1);
  vector_string.clear();
  vector_string.push_back("one");
  vector_charstar.clear();
  vector_charstar.push_back("one");
  vector_vector_int32.clear();
  vector_vector_int32.push_back(std::vector<int32_t>{ 1 });
  vector_vector_string.clear();
  vector_vector_string.push_back(std::vector<std::string>{ "one" });
  vector_vector_charstar.clear();
  vector_vector_charstar.push_back(std::vector<const char*>{ "one" });
  vector_set_int32.clear();
  vector_set_int32.push_back(std::set<int32_t>{ 1 });
  set_int32.clear();
  set_int32.insert(1);

  tree->Fill();

  vector_int32.clear();
  vector_int32.push_back(1);
  vector_int32.push_back(2);
  vector_string.clear();
  vector_string.push_back("one");
  vector_string.push_back("two");
  vector_charstar.clear();
  vector_charstar.push_back("one");
  vector_charstar.push_back("two");
  vector_vector_int32.clear();
  vector_vector_int32.push_back(std::vector<int32_t>{ 1 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 });
  vector_vector_string.clear();
  vector_vector_string.push_back(std::vector<std::string>{ "one" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two" });
  vector_vector_charstar.clear();
  vector_vector_charstar.push_back(std::vector<const char*>{ "one" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two" });
  vector_set_int32.clear();
  vector_set_int32.push_back(std::set<int32_t>{ 1 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2 });
  set_int32.clear();
  set_int32.insert(1);
  set_int32.insert(2);

  tree->Fill();

  vector_int32.clear();
  vector_int32.push_back(1);
  vector_int32.push_back(2);
  vector_int32.push_back(3);
  vector_string.clear();
  vector_string.push_back("one");
  vector_string.push_back("two");
  vector_string.push_back("three");
  vector_charstar.clear();
  vector_charstar.push_back("one");
  vector_charstar.push_back("two");
  vector_charstar.push_back("three");
  vector_vector_int32.clear();
  vector_vector_int32.push_back(std::vector<int32_t>{ 1 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 });
  vector_vector_string.clear();
  vector_vector_string.push_back(std::vector<std::string>{ "one" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" });
  vector_vector_charstar.clear();
  vector_vector_charstar.push_back(std::vector<const char*>{ "one" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three" });
  vector_set_int32.clear();
  vector_set_int32.push_back(std::set<int32_t>{ 1 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 });
  set_int32.clear();
  set_int32.insert(1);
  set_int32.insert(2);
  set_int32.insert(3);

  tree->Fill();

  vector_int32.clear();
  vector_int32.push_back(1);
  vector_int32.push_back(2);
  vector_int32.push_back(3);
  vector_int32.push_back(4);
  vector_string.clear();
  vector_string.push_back("one");
  vector_string.push_back("two");
  vector_string.push_back("three");
  vector_string.push_back("four");
  vector_charstar.clear();
  vector_charstar.push_back("one");
  vector_charstar.push_back("two");
  vector_charstar.push_back("three");
  vector_charstar.push_back("four");
  vector_vector_int32.clear();
  vector_vector_int32.push_back(std::vector<int32_t>{ 1 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4 });
  vector_vector_string.clear();
  vector_vector_string.push_back(std::vector<std::string>{ "one" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four" });
  vector_vector_charstar.clear();
  vector_vector_charstar.push_back(std::vector<const char*>{ "one" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three", "four" });
  vector_set_int32.clear();
  vector_set_int32.push_back(std::set<int32_t>{ 1 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4 });
  set_int32.clear();
  set_int32.insert(1);
  set_int32.insert(2);
  set_int32.insert(3);
  set_int32.insert(4);

  tree->Fill();

  vector_int32.clear();
  vector_int32.push_back(1);
  vector_int32.push_back(2);
  vector_int32.push_back(3);
  vector_int32.push_back(4);
  vector_int32.push_back(5);
  vector_string.clear();
  vector_string.push_back("one");
  vector_string.push_back("two");
  vector_string.push_back("three");
  vector_string.push_back("four");
  vector_string.push_back("five");
  vector_charstar.clear();
  vector_charstar.push_back("one");
  vector_charstar.push_back("two");
  vector_charstar.push_back("three");
  vector_charstar.push_back("four");
  vector_charstar.push_back("five");
  vector_vector_int32.clear();
  vector_vector_int32.push_back(std::vector<int32_t>{ 1 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4 });
  vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4, 5 });
  vector_vector_string.clear();
  vector_vector_string.push_back(std::vector<std::string>{ "one" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four" });
  vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four", "five" });
  vector_vector_charstar.clear();
  vector_vector_charstar.push_back(std::vector<const char*>{ "one" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three", "four" });
  vector_vector_charstar.push_back(std::vector<const char*>{ "one", "two", "three", "four", "five" });
  vector_set_int32.clear();
  vector_set_int32.push_back(std::set<int32_t>{ 1 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4 });
  vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4, 5 });
  set_int32.clear();
  set_int32.insert(1);
  set_int32.insert(2);
  set_int32.insert(3);
  set_int32.insert(4);
  set_int32.insert(5);

  tree->Fill();

  tree->Write();
  file->Close();
}
