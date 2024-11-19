/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RRawFile.hxx>

#include <atomic>
#include <bitset>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

void rntuple_atomic_bitset() {
  std::string rootFileName{"test_atomic_bitset_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto atomic_int_field = model->MakeField<std::atomic<int>>("atomic_int");
  auto bitset_field = model->MakeField<std::bitset<42>>("bitset");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);

  *atomic_int_field = 1;
  *bitset_field = std::bitset<42>(42);
  ntuple->Fill();

  *atomic_int_field = 2;
  *bitset_field |= 0b1010101010101010;
  ntuple->Fill();

  *atomic_int_field = 3;
  *bitset_field &= 0b1100110011001100;
  ntuple->Fill();
}
