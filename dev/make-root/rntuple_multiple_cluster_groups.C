/* https://root.cern/doc/master/ntpl001__staff_8C.html */
/* this file tests when we have multiple pages, each page stores 65536 bytes,
 * thus we need to make it longer */
/* https://github.com/scikit-hep/uproot5/pull/630 */

R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RRawFile.hxx>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

void rntuple_multiple_cluster_groups() {
  std::string rootFileName{"test_multiple_cluster_groups_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto int_field = model->MakeField<int>("one");
  auto int_vector = model->MakeField<std::vector<int16_t>>("int_vector");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);
  for(auto i=0; i<1000; i++){
      if (i && i%100==0) {
          ntuple->CommitCluster();
      }
      if (i == 450 || i == 750) { // to add a bit of unevenness
        ntuple->CommitCluster(/*commitClusterGroup*/ true);
      }
      *int_field = i;
      *int_vector = {static_cast<int16_t>(i), static_cast<int16_t>(i+1)};
      ntuple->Fill();
  }
}
