/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RRawFile.hxx>

#include <cassert>
#include <variant>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

struct EmptyStruct {};

struct StructForVariant {
   int i;
   StructForVariant() = default;
   StructForVariant(int ii) : i(ii) {};
   StructForVariant(const StructForVariant &) { throw std::runtime_error("copy ctor"); }
   StructForVariant &operator=(const StructForVariant &) = default;
};

void rntuple_emptystruct_invalidvar() {
  std::string rootFileName{"test_emptystruct_invalidvar_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();
  auto empty_struct_field = model->MakeField<EmptyStruct>("empty_struct");
  auto variant_field = model->MakeField<std::variant<int,StructForVariant>>("variant");
  auto ntuple =
      RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);

  *empty_struct_field = EmptyStruct{};
  *variant_field = 1; // valid state
  ntuple->Fill();

  try {
    *variant_field = StructForVariant(); // invalid state
  } catch (const std::runtime_error &e) {
    std::cerr << "Caught exception: " << e.what() << std::endl;
  }
  assert(variant_field->valueless_by_exception());
  ntuple->Fill();

  variant_field->emplace<StructForVariant>(2); // valid state
  ntuple->Fill();
}
