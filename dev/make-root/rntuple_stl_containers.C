/* https://root.cern/doc/master/ntpl001__staff_8C.html */
/* https://github.com/scikit-hep/uproot5/pull/662 */
/* tests a bunch of stl container */

R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RRawFile.hxx>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

#include <iostream>
#include <vector>
#include <set>
#include <variant>
#include <tuple>

void rntuple_stl_containers() {
  std::string rootFileName{"test_ntuple_stl_containers.root"};
  auto model = RNTupleModel::Create();
  auto string = model->MakeField<std::string>("string");
  auto vector_int32 = model->MakeField<std::vector<int32_t>>("vector_int32");
  auto vector_vector_int32 = model->MakeField<std::vector<std::vector<int32_t>>>("vector_vector_int32");
  auto vector_string = model->MakeField<std::vector<std::string>>("vector_string");
  auto vector_vector_string = model->MakeField<std::vector<std::vector<std::string>>>("vector_vector_string");
  auto variant_int32_float = model->MakeField<std::variant<int32_t, float_t>>("variant_int32_float");
  auto vector_variant_int32_float = model->MakeField<std::vector<std::variant<int32_t, float_t>>>("vector_variant_int32_float");
  auto tuple_int32_string = model->MakeField<std::tuple<int32_t, std::string>>("tuple_int32_string");
  auto vector_tuple_int32_string = model->MakeField<std::vector<std::tuple<int32_t, std::string>>>("vector_tuple_int32_string");

  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);



  *string = "one";
  vector_int32->emplace_back(1);
  vector_string->emplace_back("one");
  vector_vector_int32->emplace_back(std::vector<int32_t>{ 1 });
  vector_vector_string->emplace_back(std::vector<std::string>{ "one" });
  *variant_int32_float = 1.0f;
  vector_variant_int32_float->emplace_back(1);
  *tuple_int32_string = std::tuple<int32_t, std::string>({1, "one"});
  vector_tuple_int32_string->emplace_back(std::tuple<int32_t, std::string>({1, "one"}));

  ntuple->Fill();

  *string = "two";
  vector_int32->emplace_back(2);
  vector_string->emplace_back("two");
  vector_vector_int32->emplace_back(std::vector<int32_t>{ 2 });
  vector_vector_string->emplace_back(std::vector<std::string>{ "two" });
  *variant_int32_float = 2.0f;
  vector_variant_int32_float->emplace_back(2.0f);
  *tuple_int32_string = std::tuple<int32_t, std::string>({2, "two"});
  vector_tuple_int32_string->emplace_back(std::tuple<int32_t, std::string>({2, "two"}));

  ntuple->Fill();

/*   string.clear(); */
/*   string.assign("three"); */
/*   tstring.Clear(); */
/*   tstring.Append("three"); */
/*   vector_int32.clear(); */
/*   vector_int32.push_back(1); */
/*   vector_int32.push_back(2); */
/*   vector_int32.push_back(3); */
/*   vector_string.clear(); */
/*   vector_string.push_back("one"); */
/*   vector_string.push_back("two"); */
/*   vector_string.push_back("three"); */
/*   vector_tstring.clear(); */
/*   vector_tstring.push_back("one"); */
/*   vector_tstring.push_back("two"); */
/*   vector_tstring.push_back("three"); */
/*   vector_vector_int32.clear(); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 }); */
/*   vector_vector_string.clear(); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" }); */
/*   vector_vector_tstring.clear(); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three" }); */
/*   vector_set_int32.clear(); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 }); */
/*   vector_set_string.clear(); */
/*   vector_set_string.push_back(std::set<std::string>{ "one" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three" }); */
/*   set_int32.clear(); */
/*   set_int32.insert(1); */
/*   set_int32.insert(2); */
/*   set_int32.insert(3); */
/*   set_string.clear(); */
/*   set_string.insert("one"); */
/*   set_string.insert("two"); */
/*   set_string.insert("three"); */

/*   tree->Fill(); */

/*   string.clear(); */
/*   string.assign("four"); */
/*   tstring.Clear(); */
/*   tstring.Append("four"); */
/*   vector_int32.clear(); */
/*   vector_int32.push_back(1); */
/*   vector_int32.push_back(2); */
/*   vector_int32.push_back(3); */
/*   vector_int32.push_back(4); */
/*   vector_string.clear(); */
/*   vector_string.push_back("one"); */
/*   vector_string.push_back("two"); */
/*   vector_string.push_back("three"); */
/*   vector_string.push_back("four"); */
/*   vector_tstring.clear(); */
/*   vector_tstring.push_back("one"); */
/*   vector_tstring.push_back("two"); */
/*   vector_tstring.push_back("three"); */
/*   vector_tstring.push_back("four"); */
/*   vector_vector_int32.clear(); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4 }); */
/*   vector_vector_string.clear(); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four" }); */
/*   vector_vector_tstring.clear(); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three", "four" }); */
/*   vector_set_int32.clear(); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4 }); */
/*   vector_set_string.clear(); */
/*   vector_set_string.push_back(std::set<std::string>{ "one" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three", "four" }); */
/*   set_int32.clear(); */
/*   set_int32.insert(1); */
/*   set_int32.insert(2); */
/*   set_int32.insert(3); */
/*   set_int32.insert(4); */
/*   set_string.clear(); */
/*   set_string.insert("one"); */
/*   set_string.insert("two"); */
/*   set_string.insert("three"); */
/*   set_string.insert("four"); */

/*   tree->Fill(); */

/*   string.clear(); */
/*   string.assign("five"); */
/*   tstring.Clear(); */
/*   tstring.Append("five"); */
/*   vector_int32.clear(); */
/*   vector_int32.push_back(1); */
/*   vector_int32.push_back(2); */
/*   vector_int32.push_back(3); */
/*   vector_int32.push_back(4); */
/*   vector_int32.push_back(5); */
/*   vector_string.clear(); */
/*   vector_string.push_back("one"); */
/*   vector_string.push_back("two"); */
/*   vector_string.push_back("three"); */
/*   vector_string.push_back("four"); */
/*   vector_string.push_back("five"); */
/*   vector_tstring.clear(); */
/*   vector_tstring.push_back("one"); */
/*   vector_tstring.push_back("two"); */
/*   vector_tstring.push_back("three"); */
/*   vector_tstring.push_back("four"); */
/*   vector_tstring.push_back("five"); */
/*   vector_vector_int32.clear(); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4 }); */
/*   vector_vector_int32.push_back(std::vector<int32_t>{ 1, 2, 3, 4, 5 }); */
/*   vector_vector_string.clear(); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four" }); */
/*   vector_vector_string.push_back(std::vector<std::string>{ "one", "two", "three", "four", "five" }); */
/*   vector_vector_tstring.clear(); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three", "four" }); */
/*   vector_vector_tstring.push_back(std::vector<TString>{ "one", "two", "three", "four", "five" }); */
/*   vector_set_int32.clear(); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4 }); */
/*   vector_set_int32.push_back(std::set<int32_t>{ 1, 2, 3, 4, 5 }); */
/*   vector_set_string.clear(); */
/*   vector_set_string.push_back(std::set<std::string>{ "one" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three", "four" }); */
/*   vector_set_string.push_back(std::set<std::string>{ "one", "two", "three", "four", "five" }); */
/*   set_int32.clear(); */
/*   set_int32.insert(1); */
/*   set_int32.insert(2); */
/*   set_int32.insert(3); */
/*   set_int32.insert(4); */
/*   set_int32.insert(5); */
/*   set_string.clear(); */
/*   set_string.insert("one"); */
/*   set_string.insert("two"); */
/*   set_string.insert("three"); */
/*   set_string.insert("four"); */
/*   set_string.insert("five"); */

/*   tree->Fill(); */

/*   tree->Write(); */
/*   file->Close(); */
}
