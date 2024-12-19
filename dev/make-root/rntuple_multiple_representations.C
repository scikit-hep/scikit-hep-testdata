/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RNTuple.hxx>
#include <ROOT/RFieldBase.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RNTupleUtil.hxx>
#include <ROOT/RRawFile.hxx>

#include <cassert>
#include <variant>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;
using RFieldBase = ROOT::Experimental::RFieldBase;
using EColumnType = ROOT::Experimental::EColumnType;

void rntuple_multiple_representations() {
  std::string rootFileName{"test_multiple_representations_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();

  auto fldReal = RFieldBase::Create("real", "float").Unwrap();
  fldReal->SetColumnRepresentatives({{EColumnType::kReal32}, {EColumnType::kReal16}});
  model->AddField(std::move(fldReal));
  auto ptrReal = model->GetDefaultEntry().GetPtr<float>("real");

  auto ntuple = RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);

  *ptrReal = 1.0;
  ntuple->Fill();
  ntuple->CommitCluster();

  ROOT::Experimental::Internal::RFieldRepresentationModifier::SetPrimaryColumnRepresentation(
         const_cast<RFieldBase &>(ntuple->GetModel().GetConstField("real")), 1);
  *ptrReal = 2.0;
  ntuple->Fill();
  ntuple->CommitCluster();

  ROOT::Experimental::Internal::RFieldRepresentationModifier::SetPrimaryColumnRepresentation(
         const_cast<RFieldBase &>(ntuple->GetModel().GetConstField("real")), 0);
  *ptrReal = 3.0;
  ntuple->Fill();
}
