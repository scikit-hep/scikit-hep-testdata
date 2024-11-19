/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RNTupleWriteOptions.hxx>
#include <ROOT/RRawFile.hxx>

#include <cassert>
#include <variant>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;
using RNTupleWriteOptions = ROOT::Experimental::RNTupleWriteOptions;

void rntuple_extension_columns() {
  auto options = RNTupleWriteOptions();
  options.SetMaxUnzippedPageSize(700);
  options.SetApproxZippedClusterSize(2000);
  options.SetMaxUnzippedClusterSize(2000);

  std::string rootFileName{"test_extension_columns_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto int_field = model->MakeField<int>("int_field");

  auto ntuple = RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName, options);

  for (int i = 0; i < 200; i++) {
    *int_field = i;
    ntuple->Fill();
  }

  auto modelUpdater = ntuple->CreateModelUpdater();
  modelUpdater->BeginUpdate();
  auto vec_fload = modelUpdater->MakeField<float>("float_field");
  modelUpdater->CommitUpdate();

  for (int i = 0; i < 200; i++) {
    *int_field = i;
    *vec_fload = i + 0.5;
    ntuple->Fill();
  }

  auto modelUpdater2 = ntuple->CreateModelUpdater();
  modelUpdater2->BeginUpdate();
  auto intvec_field = modelUpdater2->MakeField<std::vector<int>>("intvec_field");
  modelUpdater2->CommitUpdate();

  for (int i = 0; i < 200; i++) {
    *int_field = i;
    *vec_fload = i + 0.5;
    *intvec_field = {i, i + 1};
    ntuple->Fill();
  }
}
