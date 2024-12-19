/* https://root.cern/doc/master/ntpl001__staff_8C.html */
R__LOAD_LIBRARY(ROOTNTuple)
#include <ROOT/RField.hxx>
#include <ROOT/RNTuple.hxx>
#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>
#include <ROOT/RNTupleUtil.hxx>
#include <ROOT/RRawFile.hxx>

#include <cassert>
#include <variant>

using RNTupleModel = ROOT::Experimental::RNTupleModel;
using RNTupleWriter = ROOT::Experimental::RNTupleWriter;
template <typename T>
using RField = ROOT::Experimental::RField<T>;
using EColumnType = ROOT::Experimental::EColumnType;

void rntuple_float_types() {
  std::string rootFileName{"test_float_types_rntuple_v1-0-0-0.root"};
  auto model = RNTupleModel::Create();

  auto trunc10 = std::make_unique<RField<float>>("trunc10");
  trunc10->SetColumnRepresentatives({{EColumnType::kReal32Trunc}});
  trunc10->SetTruncated(10);
  model->AddField(std::move(trunc10));

  auto trunc16 = std::make_unique<RField<float>>("trunc16");
  trunc16->SetColumnRepresentatives({{EColumnType::kReal32Trunc}});
  trunc16->SetTruncated(16);
  model->AddField(std::move(trunc16));

  auto trunc24 = std::make_unique<RField<float>>("trunc24");
  trunc24->SetColumnRepresentatives({{EColumnType::kReal32Trunc}});
  trunc24->SetTruncated(24);
  model->AddField(std::move(trunc24));

  auto trunc31 = std::make_unique<RField<float>>("trunc31");
  trunc31->SetColumnRepresentatives({{EColumnType::kReal32Trunc}});
  trunc31->SetTruncated(31);
  model->AddField(std::move(trunc31));

  auto quant1 = std::make_unique<RField<float>>("quant1");
  quant1->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant1->SetQuantized(-2.f, 3.f, 1);
  model->AddField(std::move(quant1));

  auto quant8 = std::make_unique<RField<float>>("quant8");
  quant8->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant8->SetQuantized(-2.f, 3.f, 8);
  model->AddField(std::move(quant8));

  auto quant16 = std::make_unique<RField<float>>("quant16");
  quant16->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant16->SetQuantized(-2.f, 3.f, 16);
  model->AddField(std::move(quant16));

  auto quant20 = std::make_unique<RField<float>>("quant20");
  quant20->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant20->SetQuantized(-2.f, 3.f, 20);
  model->AddField(std::move(quant20));

  auto quant24 = std::make_unique<RField<float>>("quant24");
  quant24->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant24->SetQuantized(-2.f, 3.f, 24);
  model->AddField(std::move(quant24));

  auto quant25 = std::make_unique<RField<float>>("quant25");
  quant25->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant25->SetQuantized(-2.f, 3.f, 25);
  model->AddField(std::move(quant25));

  auto quant32 = std::make_unique<RField<float>>("quant32");
  quant32->SetColumnRepresentatives({{EColumnType::kReal32Quant}});
  quant32->SetQuantized(-2.f, 3.f, 32);
  model->AddField(std::move(quant32));

  auto ntuple = RNTupleWriter::Recreate(std::move(model), "ntuple", rootFileName);
  auto e = ntuple->CreateEntry();

  *e->GetPtr<float>("trunc10") = 1.23456789f; // 00111111100111100000011001010010
  *e->GetPtr<float>("trunc16") = 1.23456789f;
  *e->GetPtr<float>("trunc24") = 1.23456789f;
  *e->GetPtr<float>("trunc31") = 1.23456789f;
  *e->GetPtr<float>("quant1") = 1.23456789f;
  *e->GetPtr<float>("quant8") = 1.23456789f;
  *e->GetPtr<float>("quant16") = 1.23456789f;
  *e->GetPtr<float>("quant20") = 1.23456789f;
  *e->GetPtr<float>("quant24") = 1.23456789f;
  *e->GetPtr<float>("quant25") = 1.23456789f;
  *e->GetPtr<float>("quant32") = 1.23456789f;

  ntuple->Fill(*e);

  *e->GetPtr<float>("trunc10") = 1.4660155e13f; // 01010101010101010101010101010101
  *e->GetPtr<float>("trunc16") = 1.4660155e13f;
  *e->GetPtr<float>("trunc24") = 1.4660155e13f;
  *e->GetPtr<float>("trunc31") = 1.4660155e13f;
  *e->GetPtr<float>("quant1") = 1.6666666f;  // 00111111110101010101010101010101
  *e->GetPtr<float>("quant8") = 1.6666666f;
  *e->GetPtr<float>("quant16") = 1.6666666f;
  *e->GetPtr<float>("quant20") = 1.6666666f;
  *e->GetPtr<float>("quant24") = 1.6666666f;
  *e->GetPtr<float>("quant25") = 1.6666666f;
  *e->GetPtr<float>("quant32") = 1.6666666f;

  ntuple->Fill(*e);

  *e->GetPtr<float>("trunc10") = -6.2875986e-22f;  // 10011100001111100000011111110000
  *e->GetPtr<float>("trunc16") = -6.2875986e-22f;
  *e->GetPtr<float>("trunc24") = -6.2875986e-22f;
  *e->GetPtr<float>("trunc31") = -6.2875986e-22f;
  *e->GetPtr<float>("quant1") = -6.2875986e-22f;
  *e->GetPtr<float>("quant8") = -6.2875986e-22f;
  *e->GetPtr<float>("quant16") = -6.2875986e-22f;
  *e->GetPtr<float>("quant20") = -6.2875986e-22f;
  *e->GetPtr<float>("quant24") = -6.2875986e-22f;
  *e->GetPtr<float>("quant25") = -6.2875986e-22f;
  *e->GetPtr<float>("quant32") = -6.2875986e-22f;

  ntuple->Fill(*e);

  *e->GetPtr<float>("trunc10") = -1.9060668f;  // 10111111111100111111100111111111
  *e->GetPtr<float>("trunc16") = -1.9060668f;
  *e->GetPtr<float>("trunc24") = -1.9060668f;
  *e->GetPtr<float>("trunc31") = -1.9060668f;
  *e->GetPtr<float>("quant1") = -1.9060668f;
  *e->GetPtr<float>("quant8") = -1.9060668f;
  *e->GetPtr<float>("quant16") = -1.9060668f;
  *e->GetPtr<float>("quant20") = -1.9060668f;
  *e->GetPtr<float>("quant24") = -1.9060668f;
  *e->GetPtr<float>("quant25") = -1.9060668f;
  *e->GetPtr<float>("quant32") = -1.9060668f;

  ntuple->Fill(*e);
}
