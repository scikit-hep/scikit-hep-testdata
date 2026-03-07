/* https://github.com/scikit-hep/uproot5/issues/FIXME */
/* Tests SplitInt64 (std::int64_t) decoding including values >= 2^62 that
 * expose zigzag sign-flip bugs. Values: 0, 1, -1, 2^62, -2^62, INT64_MAX, INT64_MIN */
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>

#include <cstdint>
#include <limits>
#include <string>

using ROOT::RNTupleModel;
using ROOT::RNTupleWriter;

void rntuple_splitint64() {
  std::string fname{"test_splitint64_rntuple_v1-0-1-0.root"};

  auto model = RNTupleModel::Create();
  auto field = model->MakeField<std::int64_t>("value");
  auto writer = RNTupleWriter::Recreate(std::move(model), "ntuple", fname);

  for (std::int64_t v : {(std::int64_t)0,
                         (std::int64_t)1,
                         (std::int64_t)-1,
                         (std::int64_t)4611686018427387904LL,   // 2^62
                         (std::int64_t)-4611686018427387904LL,  // -2^62
                         std::numeric_limits<std::int64_t>::max(),
                         std::numeric_limits<std::int64_t>::min()}) {
    *field = v;
    writer->Fill();
  }

  writer.reset();
}
