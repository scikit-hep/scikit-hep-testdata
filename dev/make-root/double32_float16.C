#include "TFile.h"
#include "TTree.h"

void double32_float16() {
  TFile* file = new TFile("double32-float16.root", "RECREATE");
  TTree* tree = new TTree("tree", "");

  double double32_32;
  double double32_30;
  double double32_20;
  double double32_10;
  double double32_5;
  double double32_3;
  float float16_16;
  float float16_10;
  float float16_5;
  float float16_3;

  double array_30[3];
  float array_10[3];

  tree->Branch("double32_32", &double32_32, "double32_32/d[-2.71,10,32]");
  tree->Branch("double32_30", &double32_30, "double32_30/d[-2.71,10,30]");
  tree->Branch("double32_20", &double32_20, "double32_20/d[-2.71,10,20]");
  tree->Branch("double32_10", &double32_10, "double32_10/d[-2.71,10,10]");
  tree->Branch("double32_5", &double32_5, "double32_5/d[-2.71,10,5]");
  tree->Branch("double32_3", &double32_3, "double32_3/d[-2.71,10,3]");
  tree->Branch("float16_16", &float16_16, "float16_16/f[-2.71,10,16]");
  tree->Branch("float16_10", &float16_10, "float16_10/f[-2.71,10,10]");
  tree->Branch("float16_5", &float16_5, "float16_5/f[-2.71,10,5]");
  tree->Branch("float16_3", &float16_3, "float16_3/f[-2.71,10,3]");

  tree->Branch("array_30", &array_30, "array_30[3]/d[-2.71,10,30]");
  tree->Branch("array_10", &array_10, "array_10[3]/f[-2.71,10,10]");

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = -2.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = -1.5;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = -1.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = -0.5;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = -0.1;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 0.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 0.1;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 0.5;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 1.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 2.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 3.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 4.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 5.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 6.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 7.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 8.0;
  tree->Fill();

  double32_32 = double32_30 = double32_20 = double32_10 = double32_5 = double32_3 = float16_16 = float16_10 = float16_5 = float16_3 = array_30[0] = array_30[1] = array_30[2] = array_10[0] = array_10[1] = array_10[2] = 9.0;
  tree->Fill();

  tree->Write();
  file->Close();
}
