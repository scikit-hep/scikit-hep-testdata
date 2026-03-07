/* https://github.com/scikit-hep/uproot5/issues/FIXME */
/* Tests SplitInt32 (std::int32_t) decoding including values >= 2^30 that
 * expose zigzag sign-flip bugs. Values: 0, 1, -1, 2^30, -2^30, INT32_MAX, INT32_MIN */
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>

#include <cstdint>
#include <limits>
#include <string>

using ROOT::RNTupleModel;
using ROOT::RNTupleWriter;

void rntuple_splitint32() {
  std::string fname{"test_splitint32_rntuple_v1-0-1-0.root"};

  auto model = RNTupleModel::Create();
  auto field = model->MakeField<std::int32_t>("value");
  auto writer = RNTupleWriter::Recreate(std::move(model), "ntuple", fname);

  for (std::int32_t v : {(std::int32_t)0,
                         (std::int32_t)1,
                         (std::int32_t)-1,
                         (std::int32_t)1073741824,   // 2^30
                         (std::int32_t)-1073741824,  // -2^30
                         std::numeric_limits<std::int32_t>::max(),
                         std::numeric_limits<std::int32_t>::min()}) {
    *field = v;
    writer->Fill();
  }

  writer.reset();
}
