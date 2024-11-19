/* https://root.cern/doc/master/ntpl001__staff_8C.html */

R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RRawFile.hxx>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

void rntuple_int_multicluster() {
  std::string rootFileName{"test_int_multicluster_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto int_field = model->MakeField<int16_t>("one_integers");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);
  for(auto j=2; j>0; j--){
      *int_field = j;
      for(auto i=50000000; i>0; i--){
          ntuple->Fill();
      }
  }
}
