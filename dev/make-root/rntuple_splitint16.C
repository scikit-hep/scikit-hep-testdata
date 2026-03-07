/* https://github.com/scikit-hep/uproot5/issues/FIXME */
/* Tests SplitInt16 (std::int16_t) decoding including values >= 2^14 that
 * expose zigzag sign-flip bugs. Values: 0, 1, -1, 2^14, -2^14, INT16_MAX, INT16_MIN */
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>

#include <cstdint>
#include <limits>
#include <string>

using ROOT::RNTupleModel;
using ROOT::RNTupleWriter;

void rntuple_splitint16() {
  std::string fname{"test_splitint16_rntuple_v1-0-1-0.root"};

  auto model = RNTupleModel::Create();
  auto field = model->MakeField<std::int16_t>("value");
  auto writer = RNTupleWriter::Recreate(std::move(model), "ntuple", fname);

  for (std::int16_t v : {(std::int16_t)0,
                         (std::int16_t)1,
                         (std::int16_t)-1,
                         (std::int16_t)16384,   // 2^14
                         (std::int16_t)-16384,  // -2^14
                         std::numeric_limits<std::int16_t>::max(),
                         std::numeric_limits<std::int16_t>::min()}) {
    *field = v;
    writer->Fill();
  }

  writer.reset();
}
