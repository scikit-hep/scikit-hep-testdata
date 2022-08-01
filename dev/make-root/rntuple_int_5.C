/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RRawFile.hxx>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

void rntuple_int_5() {
  std::string rootFileName{"test_ntuple_int_5.root"};
  auto model = RNTupleModel::Create();
  auto int_field = model->MakeField<int>("one_integers");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);

  *int_field = 9;
  ntuple->Fill();

  *int_field = 8;
  ntuple->Fill();

  *int_field = 7;
  ntuple->Fill();

  *int_field = 6;
  ntuple->Fill();

  *int_field = 5;
  ntuple->Fill();
}
