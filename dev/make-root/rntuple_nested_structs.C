/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RRawFile.hxx>

#include <cassert>
#include <variant>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

struct SubSubSruct {
  int i;
  std::vector<int> v;
};

struct SubStruct {
  int i;
  SubSubSruct sub_sub_struct;
};

struct TopStruct {
   int i;
   SubStruct sub_struct;
};

void rntuple_nested_structs() {
  std::string rootFileName{"test_nested_structs_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto struct_field = model->MakeField<TopStruct>("my_struct");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);


  *struct_field = TopStruct();
  for (int i = 0; i < 10; i++) {
    struct_field->i = i;
    struct_field->sub_struct.i = i + 1;
    struct_field->sub_struct.sub_sub_struct.i = i + 2;
    struct_field->sub_struct.sub_sub_struct.v = {i, i + 1};
    ntuple->Fill();
  }
}
