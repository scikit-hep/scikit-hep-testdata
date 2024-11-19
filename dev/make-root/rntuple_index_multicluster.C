/* https://root.cern/doc/master/ntpl001__staff_8C.html */

#include <vector>

R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RNTupleWriteOptions.hxx>
#include <ROOT/RRawFile.hxx>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;
using RNTupleWriteOptions = ROOT::Experimental::RNTupleWriteOptions;

void rntuple_index_multicluster() {
  auto options = RNTupleWriteOptions();
  options.SetMaxUnzippedPageSize(512);
  options.SetApproxZippedClusterSize(1000);
  options.SetMaxUnzippedClusterSize(1024);

  std::string rootFileName{"test_index_multicluster_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto int_vector = model->MakeField<std::vector<int16_t>>("int_vector");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName, options);
  for(int16_t j=0; j<2; j++){
      for(int16_t i=0; i<100; i++){
          *int_vector = {i, static_cast<int16_t>(i+j)};
          ntuple->Fill();
      }
  }
}
