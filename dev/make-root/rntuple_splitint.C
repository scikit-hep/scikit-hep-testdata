/* https://github.com/scikit-hep/uproot5/issues/1592 */
/* Tests SplitInt16/32/64 decoding including values >= 2^(N-2) that
 * expose zigzag sign-flip bugs. For each type, values are:
 * 0, 1, -1, 2^(N-2), -2^(N-2), INT_MAX, INT_MIN */
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>

#include <cstdint>
#include <limits>
#include <string>

using ROOT::RNTupleModel;
using ROOT::RNTupleWriter;

void rntuple_splitint() {
  std::string fname{"test_splitint_rntuple_v1-0-1-0.root"};

  auto model = RNTupleModel::Create();
  auto field16 = model->MakeField<std::int16_t>("int16");
  auto field32 = model->MakeField<std::int32_t>("int32");
  auto field64 = model->MakeField<std::int64_t>("int64");
  auto writer = RNTupleWriter::Recreate(std::move(model), "ntuple", fname);

  std::int16_t values16[] = {(std::int16_t)0,
                              (std::int16_t)1,
                              (std::int16_t)-1,
                              (std::int16_t)16384,   // 2^14
                              (std::int16_t)-16384,  // -2^14
                              std::numeric_limits<std::int16_t>::max(),
                              std::numeric_limits<std::int16_t>::min()};
  std::int32_t values32[] = {(std::int32_t)0,
                              (std::int32_t)1,
                              (std::int32_t)-1,
                              (std::int32_t)1073741824,   // 2^30
                              (std::int32_t)-1073741824,  // -2^30
                              std::numeric_limits<std::int32_t>::max(),
                              std::numeric_limits<std::int32_t>::min()};
  std::int64_t values64[] = {(std::int64_t)0,
                              (std::int64_t)1,
                              (std::int64_t)-1,
                              (std::int64_t)4611686018427387904LL,   // 2^62
                              (std::int64_t)-4611686018427387904LL,  // -2^62
                              std::numeric_limits<std::int64_t>::max(),
                              std::numeric_limits<std::int64_t>::min()};

  for (int i = 0; i < 7; ++i) {
    *field16 = values16[i];
    *field32 = values32[i];
    *field64 = values64[i];
    writer->Fill();
  }

  writer.reset();
}
